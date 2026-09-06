init -1 python: # <- because children shop logic modules come 1 step later
    def IsItemNotLoseable(ItemID):
        return static_item_defs[ItemID].get("cannot_lose", False)

    class BaseShopLM(LogicModule):
        def __init__(self):
            super().__init__()

            self.Items      = dict()
            self.Discount   = 0.0
            self.WillNotBuyCategories   = set()
            self.WillNotBuyItemIDs      = set()

        # in a nutshell, what this does is
        # 1) tries to remove extra items so that a merchant has at least X value worth of items in their inventory at any time.
        # --- the more the difference from target value of stock, the more aggressively it sells
        # 2) tries to keep gold level in merchant's inventory at a target level by adding or removing gold (yes thin air)
        # --- same, more diff -> more aggressive add/remove
        def SimulateTradingItems(self, ShopLM, 
                TargetStockValue    = 1000, 
                TargetGold          = 2000, 
                ExcludeItemsFromAutoSell = [], # <- dont autosell ever
                KeepOneOf           = [], # <- dont autosell item if 1 left
                RestockItemsPool    = {},
            ):

            VerboseLog_General = False
            if VerboseLog_General:
                print("------------")

            ItemContainer = ShopLM.Items
######## part 1 auto-sell items. this grabs sellable items, calculates their value and sells them until target-value-to-sell is met or too little stock value left
            TotalValOfSellableStuff = 0
            ItemsWeCantSell = set()
            for ItemID, ItemQty in ItemContainer.items():
                if ItemID == "gold":
                    continue
                # 1) shit we cant sell
                if (ItemID in ExcludeItemsFromAutoSell) or (ItemID in KeepOneOf and ItemQty == 1) or (IsItemNotLoseable(ItemID)):
                    ItemsWeCantSell.add(ItemID)
                # 2) total value of shit we've got (all of it)
                TotalValOfSellableStuff += GetItemValue(ItemID) * ItemQty


            if VerboseLog_General:
                print("shop update: %s has %s total value of sellable items, target stock value is %s" % (ShopLM.__class__.__name__, TotalValOfSellableStuff, TargetStockValue))

            # get "wanna sell" value: a 10% of extra stored value adjusted further, randomly
            SellableVsTargetValuesDiff = TotalValOfSellableStuff - TargetStockValue
            if SellableVsTargetValuesDiff < 0:
                SellableVsTargetValuesDiff = 0
            # randomize value to sell within range
            TryToSellDaily_Modified = round((SellableVsTargetValuesDiff * 0.1) * RngFloat(0.75, 1.25) * RngFloat(0.75, 1.25))

            if TryToSellDaily_Modified > 0:
                if VerboseLog_General:
                    print("shop update: %s needs to sell %s (adjusted) worth of stuff" % (ShopLM.__class__.__name__, TryToSellDaily_Modified))
                ValueLeftToSellToday = TryToSellDaily_Modified

                while ValueLeftToSellToday > 0:
                    # if theres nothing really to sell, bail
                    if len(ItemsWeCantSell) >= len(ItemContainer):
                        if VerboseLog_General:
                            print("shop update: %s has no items it can auto-sell" % (ShopLM.__class__.__name__))
                        break
                    # if total value of items we have left is less than desired on-shelves value, bail
                    if TotalValOfSellableStuff < TargetStockValue:
                        if VerboseLog_General:
                            print("shop update: %s has less value in inventory than its minimum of %s, stopping auto-selling" % (ShopLM.__class__.__name__, TargetStockValue))
                        break
                    RemItemID = renpy.random.choice([X for X in ItemContainer if X not in ItemsWeCantSell])
                    RemItemPrice = GetItemValue(RemItemID)
                    if VerboseLog_General:
                        print("shop update: %s sold item %s and earned %s gold" % (ShopLM.__class__.__name__, static_item_defs[RemItemID]["name"], RemItemPrice))
                    RemItemFrom(ItemContainer, RemItemID)
                    AddItemTo(ItemContainer, "gold", RemItemPrice)
                    ValueLeftToSellToday -= RemItemPrice
                    TotalValOfSellableStuff -= RemItemPrice

                if VerboseLog_General:
                    if ValueLeftToSellToday > 0:
                        print("shop update: %s did not sell enough items to meet its (adjusted) daily target of %s" % (ShopLM.__class__.__name__, TryToSellDaily_Modified))
                    else:
                        print("shop update: %s sold enough items to meet its (adjusted) daily target of %s" % (ShopLM.__class__.__name__, TryToSellDaily_Modified))

###### part 2 update gold. this simply adds or removes SOME gold to meet target value.
            GoldDiffFromTarget = GetItemQty(ItemContainer, "gold") - TargetGold
            IsSurplus = (True if GoldDiffFromTarget > 0 else False)
            if IsSurplus:
                GoldToTrim = round((GoldDiffFromTarget * 0.25) * RngFloat(0.5, 1.5))
                if VerboseLog_General:
                    print("shop update: %s is at %s gold, which is over %s (adjusted) target gold: removing %s gold" % (ShopLM.__class__.__name__, GetItemQty(ItemContainer, "gold"), TargetGold, GoldToTrim))
                RemItemFrom(ItemContainer, "gold", GoldToTrim)
            else:
                GoldToAdd = abs(round((GoldDiffFromTarget * 0.25) * RngFloat(0.5, 1.5))) + RngInt(round(-(TargetGold * 0.2)), round(TargetGold * 0.2))
                AddItemTo(ItemContainer, "gold", GoldToAdd)
                if VerboseLog_General:
                    print("shop update: %s is under %s (adjusted) target gold, added %s (fudged) gold" % (ShopLM.__class__.__name__, TargetGold, GoldToAdd))
            if VerboseLog_General:
                print("shop update: %s is at %s gold" % (ShopLM.__class__.__name__, GetItemQty(ItemContainer, "gold")))

###### part 3 restock items. rolls & adds.
            for ItemID, ItemRestockData in RestockItemsPool.items():
                if GetItemQty(ItemContainer, ItemID) < ItemRestockData["restock_if_below"]:
                    if VerboseLog_General:
                        print("shop update: daily restock for %s, adding item %s" % (ShopLM.__class__.__name__, ItemID))
                    DailyAmt = ItemRestockData["daily_amt"]
                    DailyAmt_f, DailyAmt_i = math.modf(DailyAmt)
                    for i in range(round(DailyAmt_i)):
                        if RngInt(1, 2) == 1:
                            AddItemTo(ItemContainer, ItemID)
                    if RngFloat(0, 1) <= DailyAmt_f:
                        AddItemTo(ItemContainer, ItemID)
            return