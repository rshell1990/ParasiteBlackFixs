init python:
    @AppendToAllQuests
    class ShopHamunGeneral(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = {"crafting", "book", "illegal"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 1000)
            self.onMidnight()
            return

        # restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 1000,
                TargetStockValue = 2000,
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
                },
            )
            return

    @AppendToAllQuests
    class DialogueKatiya(LogicModule):
        def __init__(self):
            super().__init__()

            self.isFlashing = False
            self.AlwaysShowTits = False # set via dreamhouse

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_general_store":
                if IsDaytime():
                    btnMods["btn_talk_katiya_store"] = BtnJumpLabel(_("Talk to the Shopkeeper"), "katiya_store_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("katiya_root", DNode(_("I'd like to see your wares."), "katiya_trade"))
            if self.AlwaysShowTits == False:
                if not self.isFlashing:
                    yield ("katiya_root", DNode(_("Those are some... Impressive assets."), "katiya_flash_ask"))
            yield ("katiya_root", DNode(_("Your Alderian is surprisingly good."), "katiya_good_alderian"))
            yield ("katiya_root", DNode(_("I'm just looking around."), "katiya_bye", nextNode = "DNodeExit", order = -100))

        def onStart(self):
            QstStart(ShopHamunGeneral)
            return


label katiya_store_talk:
    if DialogueKatiya().AlwaysShowTits == True:
        show katiya at center with dissolve
        $ PlaySoundRandom("tentFlap")
        hide katiya
        show cg_katiya_flash at blurin, center:
            offset CHAR_OFFSET.KATIYA
        with dissolve
    else:
        show katiya at center with dissolve
        KATIYA "Ah! Welcome! Welcome to my store!"
    KATIYA "How may Katiya help you today?"
    $ CharMeet("katiya")
    call processDialogue("katiya_root") from _call_processDialogue_57
    $ DialogueKatiya().isFlashing = False
    $ LocEnter()

label katiya_trade:
    KATIYA "Katiya has many things to show... For a price."
    call screen trade(ShopHamunGeneral)
    KATIYA "You will be back soon, I can tell!"
    $ DialogueKatiya().isFlashing = False
    $ LocEnter()

label katiya_bye:
    KATIYA "Sure, feel free to."
    $ DialogueKatiya().isFlashing = False
    $ LocEnter()

label katiya_good_alderian:
    KATIYA "Is that so?"
    KATIYA "My father is Alderian, he taught me to speak your tongue well from a young age."
    MC @smile "Oh, that’s impressive."
    MC @talk "Is your father still well?"
    KATIYA "Tsch... He is a drunkard who left me and my mother for some Alderian merchants daughter."
    MC @sad "Oh, I’m... Sorry."
    KATIYA "It is life. Many daughters have had worse fathers."
    return

label katiya_flash_ask:
    KATIYA "Fifty coins and I’ll let you look, but no touch."
    menu:
        "Deal." (Req_Gold = 50):
            $ PlayerRemItem("gold", 50)
            KATIYA "Enjoy thinking about them tonight ~"
            $ DialogueKatiya().isFlashing = True
            $ PlaySoundRandom("tentFlap")
            hide katiya
            show cg_katiya_flash at blurin, center:
                offset CHAR_OFFSET.KATIYA
            with dissolve
            $ Pause()

        "Another time, perhaps":
            KATIYA "When you have the coin, you let me know."
            return
