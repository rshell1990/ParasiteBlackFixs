init python:
    # this is to quickly grab all cats (by shops)
    def GetAllItemShopCats():
        Result = set()
        for ItemID in static_item_defs:
            Item = static_item_defs[ItemID]
            if "shop_category" in Item:
                Result.add(Item["shop_category"])
        return Result

    def GetMaxToBuy(ItemID, ShopLM):
        return min(ShopLM.Items[ItemID], int(GetItemQty(player_inv, "gold") / all_items[ItemID]["value_per_unit"]))

    def GetMaxToSell(ItemID, ShopLM):
        return min(player_inv[ItemID], int(GetItemQty(ShopLM.Items, "gold") / all_items[ItemID]["value_per_unit"]))

    def UI_CanBuy(ItemID, ShopLM):
        if ItemID == "gold":
            return False

        if GetShopBuyPrice(ItemID, ShopLM) <= GetItemQty(player_inv, "gold"):
            return True
        else:
            return False
    
    def IsItemExcludedFromShop(ShopLM, ItemID):
        # no if id in id excluded list
        if ItemID in ShopLM.WillNotBuyItemIDs:
            return True
        # no if category in exc. categories
        if all_items[ItemID]["shop_category"] in ShopLM.WillNotBuyCategories:
            return True
        if all_items[ItemID]["shop_category"] == None:
            return True
        return False

    def UI_CanSell(ShopLM, ItemID):
        if IsItemExcludedFromShop(ShopLM, ItemID):
            return False
        if GetShopSellToPrice(ItemID, ShopLM) > GetItemQty(ShopLM.Items, "gold"):
            return False
        if all_items[ItemID]["cannot_lose"]:
            return False
        if ItemID == "gold":
            return False
        return True

    def UI_BuyItem(ShopLM, ItemID, Amount = 1): # by UI only
        ### fair exchange achievement
        if ShopLM in [ShopHamunGeneral(), ShopNovarasGeneral()]:
            store._total_gold_spent_on_merchant += GetShopBuyPrice(ItemID, ShopLM) * Amount
            if store._total_gold_spent_on_merchant > 5000 and can_unlock_achievement("A_FAIR_EXCHANGE"):
                unlock_achievement("A_FAIR_EXCHANGE")

        # logic itself
        TransferItem(ShopLM.Items, ItemID, player_inv, Amount, ShopLM = ShopLM)
        renpy.music.play("audio/interface/buy.ogg", channel = "sound", loop = False, relative_volume = 0.75)
        return

    def UI_SellItem(ShopLM, ItemID, Amount = 1): # by UI only
        TransferItem(player_inv, ItemID, ShopLM.Items, Amount, FromPlayer = True, ShopLM = ShopLM, sell = True)
        renpy.music.play("audio/interface/sell.ogg", channel = "sound", loop = False, relative_volume = 0.75)
        return

    def GetShopBuyPrice(ItemID, ShopLM):
        BaseValue = all_items[ItemID]["value_per_unit"]
        DiscountValue = int(BaseValue * (1 - ShopLM.Discount))
        AdjustedValue = max(DiscountValue, 1)
        return AdjustedValue

    def GetShopSellToPrice(ItemID, ShopLM):
        BaseValue = all_items[ItemID]["value_per_unit"]
        SellFactor = 0.5 # always sell at 50%
        AdjustedValue = max(int(BaseValue * SellFactor), 1)
        # this check avoids selling higher than we buy at the same trader
        BuyValue = GetShopBuyPrice(ItemID, ShopLM)
        if AdjustedValue >= BuyValue:
            AdjustedValue = max((BuyValue - 1), 1)

        return AdjustedValue