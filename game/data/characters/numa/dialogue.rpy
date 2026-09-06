init python:
    @AppendToAllQuests
    class ShopHamunLibrary(BaseShopLM):
        def __init__(self):
            super().__init__()
            self.WillNotBuyCategories   = GetAllItemShopCats() - {"book"}
            self.WillNotBuyItemIDs      = {"book_prince_onji", "book_legends_far_wide"}
        
        def onStart(self):
            AddItemTo(self.Items, "gold", 300)
            self.onMidnight() # 1st restock is manual

        # daily restock 
        def onMidnight(self):
            super().SimulateTradingItems(self, 
                TargetGold = 500,
                TargetStockValue = 500,
            )

    @AppendToAllQuests
    class DialogueNuma(LogicModule):
        def __init__(self):
            super().__init__()

            self.AskedWhatAreYou = False
            self.AskedAboutBooks = False
            self.SeenFirstMeet   = False

        def extraDialogue(self):
            yield ("numa_root", DNode(_("I have books to trade."), "numa_books_trade"))
            if not self.AskedWhatAreYou:
                yield ("numa_root", DNode(_("I hate to ask but... What are you?"), "numa_whatareyou"))

            if not self.AskedAboutBooks:
                yield ("numa_root", DNode(_("I'd like to look at some books."), "numa_somebooks"))

            yield ("numa_root", DNode(_("Can you tell me more about your people?"), "numa_moreaboutpeople"))
            yield ("numa_root", DNode(_("That's all for now."), "numa_bye", nextNode = "DNodeExit", order = -100))

        def onEnter(self):  
            if GetLocID() == "hamun_library":
                if self.SeenFirstMeet == False:
                    return TriggeredEvent("numa_firstmeet")

        def locationMod(self):
            btnMods = {}
            
            if GetLocID() == "hamun_library":
                if IsDaytime():
                    btnMods["btn_hamun_library_numa_talk"] = BtnJumpLabel(_("Talk to Numa"), "numa_talk")

            if self.AskedAboutBooks == True:
                btnMods["btn_hamun_library_bookshelves"] = BtnShowScreen(_("Bookshelves"), "container", bookshelf_library_hamun, HideOnTakeAll = True)

            return LocButtonMod(directMods = btnMods)

        def AddBooks(self):
            for book_ID in ["book_prince_onji", "book_legends_far_wide"]:
                AddItemTo(bookshelf_library_hamun, book_ID)

        def onStart(self):
            QstStart(ShopHamunLibrary)

label numa_moreaboutpeople:
    NUMA @talk "Speak the wave, and I shall answer."
    menu numa_moreaboutpeople_menu:
        "Your people... What do you do here in Hamun?":
            NUMA @talk "Once a month, our people wash up on the docks bringing supplies and gifts."
            NUMA @talk "Treasure from sunken ships, pearls, some fish..."
            NUMA @talk "In return, we are given weapons and armours forged."
            MC @think "Why would you need such things?"
            NUMA @serious "... The waves are a turbulent thing."
            NUMA @talk "They turn towards war."
            MC @think "War? What war?"
            NUMA @talk "It matters not for you surface breathers."
            NUMA @talk "There are many fiefdoms vying for power below the currents."
            NUMA @talk "The senate-"
            "She stopped herself, her lips curling into a forced smile."
            NUMA @smile "Forgive me, your Thalvën is so good, I forgot myself for a moment."
            jump numa_moreaboutpeople_menu

        "Why are you working in a library?":
            NUMA @talk "In order to maintain good relations with the merchants, a few of our Thalay kin were asked to work within the city."
            NUMA @talk "It is purely for diplomatic reasons, they even asked what role we would like."
            NUMA @smile "I asked to help run a library, so they had built this place to accomodate my needs."
            MC @think "They built a whole library for you?"
            NUMA @talk "No, they built a whole library to keep my kin happy... I just happen to work within it."
            jump numa_moreaboutpeople_menu

        "That's all the questions I have for now.":
            NUMA @talk "Of course... It pleases me to be able to talk to one as clearly as you."
            return

label numa_whatareyou:
    $ DialogueNuma().AskedWhatAreYou = True
    "Numa's eyelids blinked twice as she tilted her head once more."
    NUMA @talk "How can one speak the wave so well and not know what we are?"
    MC @think "It's... complicated."
    NUMA @talk "... I see."
    NUMA @talk "Then to answer your question, I am Thalay."
    NUMA @smile "I presume I may be one of the first, or perhaps THE first, of my kind you've seen since arriving in Hamun."
    MC @talk "Yes."
    NUMA @talk "Mmm... It is not surprising."
    NUMA @talk "Our people conduct only limited business with land breathers."
    return

label numa_talk:
    show numa at center
    with dissolve
    NUMA @smile "Greetings again, how may I help?"
    call processDialogue("numa_root") from _call_processDialogue_58
    $ LocEnter()

label numa_bye:
    NUMA @smile "Come back anytime... It pleases me to have someone I can actually speak the wave with."
    $ LocEnter()

label numa_books_trade:
    NUMA @talk "Okay."
    NUMA @talk "Let's take a look then..."
    call screen trade(ShopHamunLibrary)
    NUMA @talk "Is there anything else?"
    return

label numa_firstmeet:
    $ DialogueNuma().SeenFirstMeet = True
    "Entering into the Hamun library was... an unusual sight."
    "While the usual rows of books were neatly stacked up high as one would expect, a deep, decorated pool lay in the center of the library,"
    "Complete with a strange water fountain statue of what appeared to be a mage striking up a bargain with a strange fish like humanoid."
    "Looking around, I could see no one in the library."
    MC @think "Hello? Is anyone here?"
    "A shadow appeared along waters of the pool, and in a moment, the blue skinned humanoid like woman emerged."
    play sound "audio/cfx/water_splash_bath.ogg"
    show numa at center with easeinbottom
    "Naked, and covered in scales as the water dripped from her body, the gilged creature turned it's gaze towards me."
    UNKNOWN "Lora'shen... Vaalra korril'neth, sollan?"
    MC @think "What?"
    "The strange creature tilted it's head, before motioning towards the many books with it's hand."
    UNKNOWN "Ssharaa… Vellunaa shor'kai, raal ithen vashan…"
    MC @talk "Sorry, I can't-"
    BLACK "({i}Language analysis complete. Sub-acquatic species dialect ready for mimic and translation.{/i})"
    MC "(Wait, what?)"
    BLACK "({i}The echo quality to their voice relies on duplicated syllables and liquid-heavy phonemes like l,r,n and-{/i})"
    MC "(What are you even-)"
    $ UNKNOWN = Character(_("???"), image = "numa")
    UNKNOWN @angry "... You must be new here, surface-breather."
    MC @surprised "I can understand you!"
    "My reply to her, almost instinctively, was one I understood... {i}but it was not Alderian words which flowed from my lips.{/i}"
    "The fish like woman seemed taken aback."
    UNKNOWN @surprised "... Your Thalvënn is excellent!"
    UNKNOWN @smile "I don't think I've ever heard a surface breather speak the wave so clearly!"
    MC "(How did you-)"
    BLACK "(The same way I learned your tongue.)"
    BLACK "(By adapting.)"
    UNKNOWN "Are you well?"
    UNKNOWN "Your mind seems adrift."
    $ UNKNOWN = Character(_("???"))
    MC @talk "Sorry, I was just lost in thought a moment."
    NUMA @smile "I am Numa."
    $ CharMeet("numa")
    MC @smile "[player_name!t]."
    NUMA @smile "How may I help you today, [player_name!t]?"
    call processDialogue("numa_root") from _call_processDialogue_59
    $ LocEnter()

label numa_somebooks:
    NUMA @talk "There are many books here available."
    NUMA @talk "I have found you surface breather's cultures... most interesting."
    $ DialogueNuma().AskedAboutBooks = True
    $ DialogueNuma().AddBooks()
    $ LocEnter()