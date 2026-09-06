init python:
    @AppendToAllQuests
    class ShopNovarasButcher(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = GetAllItemShopCats() - {"food"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 300)
            AddItemTo(self.Items, "red_meat")
            AddItemTo(self.Items, "cow_hide")
            self.onMidnight()   # 1st restock is manual

        # daily restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 500,
                TargetStockValue = 500,
                KeepOneOf = ["cow_hide"],
                RestockItemsPool = {
                    "red_meat":{
                        "restock_if_below":5,
                        "daily_amt":2.0},
                    "cow_hide":{
                        "restock_if_below":1, 
                        "daily_amt":0.15},
                },
            )

    @AppendToAllQuests
    class DialogueButcher(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_market_stalls":
                if IsDaytime():
                    btnMods["btn_novaras_market_stalls_butcher"] = BtnJumpLabel(_("Talk to the Butcher"), "novaras_butcher_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("novaras_butcher_root", DNode(_("I'd like to see your wares."), "novaras_butcher_trade"))
            yield ("novaras_butcher_root", DNode(_("Never mind."), "novaras_butcher_bye", nextNode = "DNodeExit", order = -100))

        def onStart(self):
            QstStart(ShopNovarasButcher)
            return

label novaras_butcher_talk:
    show butcher at cright_f
    with dissolve
    BUTCHER "Hello traveler! Need anything?"
    call processDialogue("novaras_butcher_root") from _call_processDialogue_31
    $ LocEnter()

label novaras_butcher_bye:
    BUTCHER "Goodbye!"
    $ LocEnter()

label novaras_butcher_trade:
    BUTCHER "Of course, take a look!"
    call screen trade(ShopNovarasButcher)
    BUTCHER "That all?"
    return