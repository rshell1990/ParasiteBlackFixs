init python:
    @AppendToAllQuests
    class ShopHamunSmithy(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories   = {"book", "jewelry", "illegal", "magecraft"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 666)
            AddItemTo(self.Items, "bronze_pickaxe")
            AddItemTo(self.Items, "iron_pickaxe")
            AddItemTo(self.Items, "syax_pickaxe")
            self.onMidnight() # 1st restock is manual

        # daily restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 1000,       # total amt of gold to balance towards
                TargetStockValue = 2500, # sum of $ of all shit (exc gold ofc) to balance towards
                KeepOneOf = ["bronze_pickaxe", "iron_pickaxe", "syax_pickaxe"],
                RestockItemsPool = {
                    "leather_armor":{
                        "restock_if_below":1, 
                        "daily_amt":0.5},
                    "reinforced_leather_armor":{
                        "restock_if_below":1, 
                        "daily_amt":0.25},
                    "chainmail":{
                        "restock_if_below":1, 
                        "daily_amt":0.25},
                    "bronze_armor":{
                        "restock_if_below":1, 
                        "daily_amt":0.25},
                    "bronze_sword":{
                        "restock_if_below":1, 
                        "daily_amt":0.25},
                    "leather":{
                        "restock_if_below":16, 
                        "daily_amt":8.0},
                },
            )

    @AppendToAllQuests
    class DialogueBeshar(LogicModule):
        def __init__(self):
            super().__init__()

            self.QuestionsAsked = False
            self.FirstTrade = True
        
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_smithy":
                if IsDaytime():
                    btnMods["btn_talk_beshar"] = BtnJumpLabel(_("Talk to the Blacksmith"), "beshar_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("beshar_root", DNode(_("Do you sell anything?"), "beshar_trade"))
            yield ("beshar_root", DNode(_("I'd like you to craft something for me."), "beshar_craft"))
            if self.QuestionsAsked == False:
                yield ("beshar_root", DNode(_("Can I ask you some questions?"), "beshar_questions"))
            yield ("beshar_root", DNode(_("That's all for now."), "beshar_bye", nextNode = "DNodeExit", order = -100))

        def onEnter(self):  
            if GetLocID() == "hamun_smithy":
                if self.progress == 0:
                    return TriggeredEvent("beshar_firstmeet")

        def onStart(self):
            QstStart(ShopHamunSmithy)
        
label beshar_questions:
    BESHAR @angry "... No."
    $ DialogueBeshar().QuestionsAsked = True
    return

label beshar_talk:
    show beshar at center
    with dissolve
    BESHAR @talk "Be quick. I don't like to waste time talking."
    call processDialogue("beshar_root") from _call_processDialogue_61
    $ LocEnter()

label beshar_craft:
    $ UpdateCraftRecipesAndIngredientsContainer(SmithyID = "hamun_smithy")
    call screen SmithyCrafting(SmithyID = "hamun_smithy") with dissolve
    BESHAR @talk "What do you need?"
    return

label beshar_trade:
    BESHAR "A few things. Come look."
    if DialogueBeshar().FirstTrade == True:
        $ DialogueBeshar().FirstTrade = False
    call screen trade(ShopHamunSmithy)
    return

label beshar_bye:
    BESHAR "{i}*Nods.*{/i}"
    $ LocEnter()

label beshar_firstmeet:
    $ QstSetProgress(DialogueBeshar, 1)
    show mc at cright_f with easeinright
    "As I entered into the blacksmith's, the familiar blast of hot heat hit me, as did the sounds of iron being smashed into shape by the powerful blows of the hammer."
    show beshar at cleft with easeinleft
    "The figure, a muscular man, perhaps in his fifties, stopped what he was doing as he turned towards me."
    BESHAR @talk "... Speak."
    MC @think "I might be in need of a blacksmith. Are your services available?"
    BESHAR @talk "They are."
    MC @talk "I'm [player_name!t], I—"
    BESHAR @talk "Beshar Ironsong."
    BESHAR @talk "Be quick. I don't like to waste time talking."
    call processDialogue("beshar_root") from _call_processDialogue_62
    return
