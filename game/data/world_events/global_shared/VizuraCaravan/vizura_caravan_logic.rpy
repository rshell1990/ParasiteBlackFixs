init python:
    @AppendToAllQuests
    class ShopVizuraCaravan(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = {"book", "crafting"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 1670)
            AddItemTo(self.Items, "potion_heal_minor", 13)
            AddItemTo(self.Items, "potion_heal_regular", 4)
            AddItemTo(self.Items, "goblin_stims", 4)
            AddItemTo(self.Items, "sword_2h", 1)
            AddItemTo(self.Items, "goblin_cleaver", 1)
            self.onMidnight()

        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 1000,
                TargetStockValue = 3000,
                ExcludeItemsFromAutoSell = ["sword_2h"],
                RestockItemsPool = {
                    "potion_heal_minor":{
                        "restock_if_below":10,
                        "daily_amt":7.0},
                    "potion_heal_regular":{
                        "restock_if_below":6, 
                        "daily_amt":3.0},
                    "goblin_stims":{
                        "restock_if_below":8,
                        "daily_amt":4.0},
                    "goblin_cleaver":{
                        "restock_if_below":1,
                        "daily_amt":0.5},
                },
            )

    @AppendToAllQuests
    class VizuraCaravan(LogicModule):
        def __init__(self):
            super().__init__()
            
            # prog 0 firstmeet, 1 first-talk (the shop talk), 2+ afterwards
            self.MoneySpent = 0         # amount of money player had invested
            self.MoneyToOfferSex = 500  # amount of money player has to invest for her to offer fucking
            self.SexOptions = False     # enabled after 1 sex enc.
            self.ShopDiscountIfHadSex = 0.2 # aka 'apply 20% discount if had sex'
            self.WantsSexToday = False  # flips back and forth each time you visit her
            self.HasOfferedSex = False  # if player refuses her once, she wont ask again

        def OverrideLocBg(self):
            if TravelState is None:
                return {}
            Result = {}
            Result["travel_node_vizura_caravan"] = TravelRoutes[TravelState.RouteID]["image_loc_bg"]
            return Result

        def onStart(self):
            QstStart(ShopVizuraCaravan)
            return

        def onMidnight(self):
            self.WantsSexToday = not self.WantsSexToday
            return

        def onEnter(self):  
            if GetLocID() == "travel_node_vizura_caravan":
                if self.progress == 0:
                    return TriggeredEvent("vizura_caravan_firstmeet")
                else:
                    EventLabel = None
                    if CharIsVisiblyPreg("vizura"):
                        if PregVizura().ShareFirstImpregNews:
                            EventLabel = "vizura_share_first_impreg_news"
                        elif PregVizura().ShareSecondImpregNews:
                            EventLabel = "vizura_share_second_impreg_news"
                    elif PregVizura().DoFirstBabyScene:
                        if PregVizura().NumBirths > 0:
                            EventLabel = "vizura_first_baby_scene"

                    if EventLabel is not None:
                        return TriggeredEvent(EventLabel)
                    else:
                        return TriggeredEvent("vizura_caravan_revisit_talk")