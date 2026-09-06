init python:
    @AppendToAllQuests
    class ShopNovarasGeneral(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = {"crafting", "book", "illegal"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 900)
            AddItemTo(self.Items, "leather_armor")
            self.onMidnight() # more items as a manual restock
            return

        # restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 1000,
                TargetStockValue = 1000,
                RestockItemsPool = {
                    "potion_heal_minor":{
                        "restock_if_below":8,
                        "daily_amt":6.0},
                    "potion_antidote":{
                        "restock_if_below":4, 
                        "daily_amt":0.5},
                    "potion_heal_regular":{
                        "restock_if_below":6, 
                        "daily_amt":3.0},
                    "potion_heal_large":{
                        "restock_if_below":4, 
                        "daily_amt":2.0},
                    "leather_armor":{
                        "restock_if_below":1, 
                        "daily_amt":0.75},
                },
            )
            return

    @AppendToAllQuests
    class DialogueLuciusMal(LogicModule):
        def __init__(self):
            super().__init__()

            self.shopsClosed = True

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_store_int":
                if IsDaytime():
                    btnMods["talkNovarasStorekeep"] = BtnJumpLabel(_("Talk to the Shopkeeper"), "luciusmal_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            if self.shopsClosed:
                yield ("luciusmal_root", DNode(_("Let me see your stock."), "luciusmal_shop"))
            else:
                yield ("luciusmal_root", DNode(_("I'd like to see your wares."), "luciusmal_shopOpen", nextNode = "DNodeExit"))
            yield ("luciusmal_root", DNode(_("I'm just looking around."), "luciusmal_bye", nextNode = "DNodeExit", order = -100))

        def onStart(self):
            QstStart(ShopNovarasGeneral)
            return

label luciusmal_talk:
    show luciusmal at center_f with dissolve
    LUCIUSMAL "Hello traveler! Need anything?"
    $ CharMeet("luciusmal")
    call processDialogue("luciusmal_root") from _call_processDialogue_26
    $ LocEnter()

label luciusmal_shop:
    LUCIUSMAL "I don't have much at the moment I'm afraid, let me see what I can rustle up for you."
    $ DialogueLuciusMal().shopsClosed = False
    call screen trade(ShopNovarasGeneral)
    return

label luciusmal_shopOpen:
    LUCIUSMAL "Take a look."
    call screen trade(ShopNovarasGeneral)
    $ LocEnter()

label luciusmal_bye:
    LUCIUSMAL "Come back anytime, friend!"
    $ LocEnter()