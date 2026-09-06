init python:
    notesLib["DraxBronze"] = Note(
        _("Drax needs bronze scraps"), 
        _("A blacksmith of Novaras will take any bronze scraps I might scavenge in exchange for gold. He is only interested in batches of five, for whatever reason."),
        journal_flag_persistent = True)

    @AppendToAllQuests
    class ShopNovarasSmithy(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories = {"book", "jewelry", "illegal", "magecraft"}

        def onStart(self):
            AddItemTo(self.Items, "gold", 800)
            AddItemTo(self.Items, "reinforced_leather_armor", 2)
            AddItemTo(self.Items, "chainmail", 1)
            AddItemTo(self.Items, "bronze_armor", 2)
            AddItemTo(self.Items, "bronze_sword", 2)
            AddItemTo(self.Items, "bronze_pickaxe")
            AddItemTo(self.Items, "iron_pickaxe")
            AddItemTo(self.Items, "syax_pickaxe")
            self.onMidnight()

        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 500,
                TargetStockValue = 3000,
                KeepOneOf = ["bronze_pickaxe", "iron_pickaxe", "syax_pickaxe"],
                RestockItemsPool = {
                    "reinforced_leather_armor":{
                        "restock_if_below":2,
                        "daily_amt":0.5},
                    "chainmail":{
                        "restock_if_below":1, 
                        "daily_amt":0.25},
                    "bronze_armor":{
                        "restock_if_below":2, 
                        "daily_amt":0.5},
                    "bronze_sword":{
                        "restock_if_below":2, 
                        "daily_amt":0.5},
                },
            )

    @AppendToAllQuests
    class DialogueDrax(LogicModule):
        def __init__(self):
            super().__init__()

            self.AgreedToBringMoreBronze = False
            self.ShopFirstTime = True # turned false after 1st shoppin

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_blacksmith":
                if IsDaytime():
                    btnMods["btn_nov_talk_drax"] = BtnJumpLabel(_("Drax"), "drax_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            if self.AgreedToBringMoreBronze:
                if PlayerItemQty("bronze_scraps") > 0:
                    yield ("drax_root", DNode(_("Here is some more bronze you wanted."), "drax_bronzeDeliverRepeat"))

            if self.ShopFirstTime:
                yield ("drax_root", DNode(_("Can I see your wares?"), "drax_shop_first"))
            else:
                yield ("drax_root", DNode(_("Can I see your wares?"), "drax_shop"))

            yield ("drax_root", DNode(_("I wanted to talk to you about crafting something for me."), "drax_craft"))
            yield ("drax_root", DNode(_("I have a few questions..."), "drax_questions", nextNode = "_sub"))
            yield ("drax_root", DNode(_("Never mind."), "drax_bye", nextNode = "DNodeExit", order = -100))

        #### questions sub-menu
            yield ("drax_sub", DNode(_("Has much changed since I left?"), "drax_qChanges"))            
            yield ("drax_sub", DNode(_("Any ideas on getting into Arlena’s good books?"), "drax_qBooks"))
            yield ("drax_sub", DNode(_("That’s all for now."), "drax_qEnd", nextNode = "_root"))

        def onStart(self):
            QstStart(ShopNovarasSmithy)

label drax_talk:
    show drax at center_f with dissolve
    DRAX 'How can I help?'
    call processDialogue("drax_root") from _call_processDialogue_6
    $ LocEnter()

label drax_bronzeDeliverRepeat:
    if PlayerItemQty("bronze_scraps") < 5:
        DRAX "No, that won't do."
        DRAX "Come back after you've scavenged more bronze."
        return

    $ PlayerRemItem("bronze_scraps", 5)
    $ PlayerAddItem("gold", 100)
    DRAX 'ARLENAAAAA!'
    DRAX 'WE HAVE BRONZE!'
    show arlena at cright_f with easeinright
    'Arlena emerged once again with her arms folded.'
    if CharGetRel("arlena") < 3:
        $ CharChangeRel("arlena", 1)
    $ rng = RngInt(1, 4)
    if rng == 1:
        ARLENA "Not bad... Who knows? Maybe one day you'll be able to improve your personality like you've done your work ethic!"
    if rng == 2:
        ARLENA "Hmph... It's better than nothing I suppose. Don't be getting sloppy on us now!"
    if rng == 3:
        ARLENA "I'm almost impressed!"
    if rng == 4:
        ARLENA "Urgh... Just take your gold and get out of here, I'm in no mood for you today."
    hide arlena with easeoutright
    if CharGetRel("arlena") >= 3 and QstGetProgress(QstDaughterOfMetal) == 0:
        $ LocSet("novaras_blacksmith")
        $ LocFlush(fade)
        jump DaughterOfMetal_stage_01
    return

label drax_shop_first:
    $ DialogueDrax().ShopFirstTime = False
    DRAX "Of course."
    DRAX "Take a peak and see if anything catches your eye..."
    call screen trade(ShopNovarasSmithy)
    return

label drax_shop:
    DRAX "Take a look."
    call screen trade(ShopNovarasSmithy)
    return

label drax_questions:
    DRAX "What do you want to know?"
    return

label drax_qChanges:
    DRAX "Not much to be honest, business carries on as usual here."
    DRAX "Usual petty neighbour drama shite, more Black Mages getting caught..."
    DRAX "Biggest thing that’s happened for a while is you two coming home the way you did!"
    return

label drax_qBooks:
    DRAX "If you figure that one out..."
    "Drax placed his hand on my shoulder as he smiled."
    DRAX "... Let me know!"
    return

label drax_qEnd:
    DRAX "What else do you need?"
    return

label drax_bye:
    DRAX "Come back anytime."
    return

label drax_craft:
    DRAX "Ah! You need something forged?"
    menu:
        "Yes, there's something I'd like you to make for me...":
            $ UpdateCraftRecipesAndIngredientsContainer(SmithyID = "drax")
            call screen SmithyCrafting(SmithyID = "drax") with dissolve
            DRAX "Anytime."
            $ LocEnter()

        "Could you explain it to me?":
            DRAX "I can smelt you just about any kind of armor and weapons you'd like, trouble is, it ain't just about the coin."
            DRAX "There's a shortage of raw materials coming in, and most of what {i}does{/i} come in goes to the war effort."
            DRAX "If you want me to make you something, you may have to source the raw materials yourself..."
            return

        "Nevermind, I've changed my mind.":
            DRAX "Very well then... Let me know if you need anything!"
            return
