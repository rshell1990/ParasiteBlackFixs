init python:
    notesLib["MiningCoExpeditionOngoing"] = Note(
        _("Crooked Shaft expedition"), 
        _("I've commissioned an expedition at the Crooked Shaft Mining Co. in Hamun City. I should pick up my order when it arrives."),
        journal_flag_delayed = True)

    notesLib["MiningCoIncome"] = Note(
        _("Mining company income"), 
        _("I've invested a hefty sum into the Crooked Shaft Mining Co at Hamun. I can collect my share of the profits weekly now."),
        journal_flag_persistent = True)

    @AppendToAllQuests
    class DialogueMarbella(LogicModule):
        def __init__(self):
            super().__init__()

            # progress 0 is firstmeet, 1 everything else

            self.FirstTimeInvestTalkAtLevel_0 = True
            self.FirstTimeInvestTalkAtLevel_1 = True

            self.InvestLevel = 0

            self.InvestCostToLevel_1 = 10000
            self.InvestCostToLevel_2 = 15000

            self.NegotiatedBetterDeal = False

            # [item_id, amount, days], [item_id, amount, days]?
            self.Expeditions = [] 
            # flag to check if ANY expeditions are ready to collects
            self.ExpeditionsReadyToCollect = False

            # this aint a flag its actually an amount
            self.MoneyReadyToCollect = 0
            # increments each week (if income active), caps out at 4, resets to 0
            self.MoneyIncrements = 0

            self.Rel = 0 # 0 is default, 1 is after bigtrouble quest dom variant

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_miningco":
                if IsDaytime():
                    btnMods["btn_talk_marbella"] = BtnJumpLabel(_("Talk to the Chief Miner"), "marbella_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            if len(self.Expeditions) > 0:
                yield ("marbella_root", DNode(_("About that expedition..."), "marbella_aboutexp"))
            if self.InvestLevel > 0:
                yield ("marbella_root", DNode(_("About the profits..."), "marbella_aboutprofits"))
            if self.InvestLevel < 2:
                yield ("marbella_root", DNode(_("I'd like to discuss investing in your company."), "marbella_invest"))
            yield ("marbella_root", DNode(_("I'd like to commission a mining expedition."), "marbella_expedition"))
            yield ("marbella_root", DNode(_("I have a few questions..."), "marbella_questions"))
            yield ("marbella_root", DNode(_("Nothing for now."), "marbella_bye", nextNode = "DNodeExit", order = -100))

        def onEnter(self):  
            if GetLocID() == "hamun_miningco":
                if IsDaytime():
                    if self.progress == 0:                    
                        return TriggeredEvent("marbella_firstmeet")
                    else:
                        if self.ExpeditionsReadyToCollect:
                            return TriggeredEvent("marbella_hasshittogivetoplayer")

        def onMidnight(self):
            # subtracts 1 day from all standing by expeditions
            # if expedition has days left as 0, its "ready" to collect
            for ExpeditionEntry in self.Expeditions:
                if ExpeditionEntry[2] > 0:
                    ExpeditionEntry[2] -= 1
                if ExpeditionEntry[2] == 0:
                    self.ExpeditionsReadyToCollect = True

            # income
            if self.InvestLevel > 0:
                if GetGameDay() % 7 == 0:
                    if self.MoneyIncrements < 4:
                        self.MoneyIncrements += 1
                        if self.InvestLevel == 1:
                            if self.NegotiatedBetterDeal:
                                self.MoneyReadyToCollect += 220
                            else:
                                self.MoneyReadyToCollect += 180
                        elif self.InvestLevel == 2:
                            if self.NegotiatedBetterDeal:
                                self.MoneyReadyToCollect += 300
                            else:
                                self.MoneyReadyToCollect += 260
            return

        def MiningExpedition(self, ItemID = None, ItemAmount = 0, ExpDelay = 0):
            Assert(ItemID is not None, "no item id for expedition, wtf")
            Assert(ItemAmount > 0, "no item amt for expedition, wtf")
            Assert(ExpDelay > 0, "no delay for expedition wtf")
            if "MiningCoExpeditionOngoing" not in store.unlockedNotes:
                NoteUnlock("MiningCoExpeditionOngoing")
            self.Expeditions.append([ItemID, ItemAmount, ExpDelay])
            return

        def DeliverAllExpeditions(self):
            self.ExpeditionsReadyToCollect = False
            for ExpeditionEntry in reversed(self.Expeditions):
                if ExpeditionEntry[2] == 0:
                    PlayerAddItem(ExpeditionEntry[0], ExpeditionEntry[1])
                    self.Expeditions.remove(ExpeditionEntry)
            if len(self.Expeditions) == 0:
                NoteLock("MiningCoExpeditionOngoing")
            return

label marbella_aboutexp:
    MARBELLA @talk "Yeah, ongoing."
    MARBELLA @smile "You'll be the first to know when it returns with goodies!"
    return

label marbella_aboutprofits:
    if DialogueMarbella().MoneyReadyToCollect > 0:
        MARBELLA @shock "Sure, there you go!"
        $ PlayerAddItem("gold", DialogueMarbella().MoneyReadyToCollect)
        $ DialogueMarbella().MoneyReadyToCollect = 0
        $ DialogueMarbella().MoneyIncrements = 0
        show marbella at nod
        MARBELLA @talk "Pleasure doing business!"
    else:
        MARBELLA @talk "Yea, I have nothing to give to you as of now."
        MARBELLA @talk "Come back every week or so, I'll have your cut ready by then!"
    return

label marbella_talk:
    show marbella at center with dissolve
    if DialogueMarbella().Rel == 0:
        MARBELLA @smile "Ahh! What can I do for ya?"
    elif DialogueMarbella().Rel == 1:
        MARBELLA @lewd "Couldn't stay away, huh?"
        MARBELLA @smile "What can I do for you?"
    call processDialogue("marbella_root") from _call_processDialogue_63
    $ LocEnter()

label marbella_bye:
    MARBELLA @talk "Alright, come speak to me whenever!"
    $ LocEnter()

label marbella_questions:
    MARBELLA @smile "Ask away."
    menu marbella_questions_menu:
        "Can you explain to me more about these enchantment runes?":
            MARBELLA @smile2 "Ah."
            MARBELLA @think "Enchantment runes are special stones infused with some kind of magecraft."
            MARBELLA @talk "There are lots of different types. You can find them deep within mines."
            MARBELLA @talk "Normally you'd need to take one to a mage for inspection, but thankfully, if there's one thing us dwarves know, it's mining."
            MARBELLA @smile "...We can pick out some good ones for ya."
            jump marbella_questions_menu

        "You mentioned you were looking for investors... Could I ask why?":
            MARBELLA @talk "Ahh, yes."
            MARBELLA @concern "It's no secret that the Crooked Shaft Mining Co. is still somewhat in its infancy."
            MARBELLA @angry "Between those bastards at the Greater Trading Company and the government-owned mines, there's not a lot of room for independent miners like meself."
            show marbella at shake
            MARBELLA @fury "I don't know who's worse. Those cheap bastards will pay you barely enough to—"
            "The red-faced dwarf stopped herself before she burst into a full-blown rant."
            MARBELLA @talk "{i}*Ahem,*{/i} as I was saying..."
            MARBELLA @smile "I intend to grow the Crooked Shaft Mining Co."
            MARBELLA @think "To be able to mine more valuable ores further afield, we need more funds."
            MARBELLA @think "Equipment, transport, food...."
            MARBELLA @angry "Guards, so those Demorai fuckers or bandits don't get at us."
            MARBELLA @sad "An expedition isn't cheap..."
            jump marbella_questions_menu

        "How does a dwarf end up in Hamun starting a mining company?":
            MARBELLA @angry "She ends up in Hamun because she gets pissed off with everyone trying to rip her off for her services."
            MARBELLA @angry "I swear, sometimes I think I should have just stayed in Iryiad."
            MARBELLA @fury "But nooo, King Radacan wants us to seek out new mines and businesses."
            MARBELLA @fury "Tschh! All I've had until now is bastards trying either to get me to work for half the coin a human would, or perverts trying to feel me up!"
            jump marbella_questions_menu

        "That's all for questions for now.":
            MARBELLA @talk "Alright then, anything else?"
            pass
    return

label marbella_firstmeet:
    show marbella at cleft with dissolve
    show mc at cright_f with easeinright
    MARBELLA @shock "... Oooh!"
    MARBELLA @smile "Yer a new face, ain't ya?"
    MARBELLA @lewd "Pretty easy on the eyes too, if I do say so meself!"
    MC @think "What is this place, some kind of... store?"
    MARBELLA @laugh2 "I'm Marbella, and this is the office of the Crooked Shaft Mining Co.!"
    $ CharMeet("marbella")
    show marbella at nod
    "Marbella took a playful bow."
    MARBELLA @smile "At yer service, m'lord."
    MC "Mining? So you sell ore then?"
    MARBELLA @think "Ehhh, not quite."
    MARBELLA @laugh2 "You commission us to do some mining for ya, and depending on what and how much of it you want, we'll deliver it for ya!"
    MARBELLA @smile "For a price, of course."
    MARBELLA @concern_lookaway "Though really, we're looking for investors right now..."
    MC @talk "Investors?"
    MARBELLA @smile2 "We want to branch out, get the right equipment and things to mine."
    "Marbella added awkwardly, her eyes averting away from mine."
    MARBELLA @sad "We uhh, only have access to one mine right now."
    MARBELLA @smile2 "But I'm planning on changing that! Don't worry!"
    MARBELLA @smile "Anyway, ehh... I'll be right over here if you want to discuss any business."
    MARBELLA @smile "You just let me know!"
    hide marbella with easeoutright
    show mc at center_f with ease
    MC "(Hmm... It would be useful having someone else collecting ore for me.)"
    MC "(Gods, could you imagine trying to gather all that ore just by myself? It would take hours!)"
    $ QstSetProgress(DialogueMarbella, 1)
    $ LocEnter()

label marbella_invest_menu_to_level_1:
    menu:
        "Here you go." (Req_Gold = DialogueMarbella().InvestCostToLevel_1): 
            $ PlayerRemItem("gold", DialogueMarbella().InvestCostToLevel_1)
            $ DialogueMarbella().InvestLevel = 1
            show marbella at shake
            MARBELLA @shock "Bloody seven hells!"
            MARBELLA @concern_lookaway "I mean, uhh..."
            MARBELLA @concern "T-Thanks!"
            MARBELLA @sad2 "It's uhh... nice to have someone have faith in me!"
            MARBELLA @smile "Come back in a week once I've bought some supplies and sorted the paperwork."
            $ NoteUnlock("MiningCoIncome")
            MARBELLA @talk "Then we can finally start doing some serious mining!"
            
        "I don't have that kind of coin on me right now...":
            MARBELLA @sad "A-Ahh... I see."
            MARBELLA @smile "Perhaps we should discuss some other business then in the meanwhile?"
    return

label marbella_invest_menu_to_level_2:
    menu:
        "Here you go." (Req_Gold = DialogueMarbella().InvestCostToLevel_2):
            $ PlayerRemItem("gold", DialogueMarbella().InvestCostToLevel_2)
            $ DialogueMarbella().InvestLevel = 2
            MARBELLA @smile "Ahh! I knew I could count on you!"
            MARBELLA  "You know... you might just be the most reliable man I know around here."
            MARBELLA  "{i}I do like reliable men...{/i}"
            MC @smile "Is that so?"
            MARBELLA  "{i}*Ahem...*{/i} Let's get back to business for now, handsome."
            MARBELLA @talk "Well, with this we can start pulling in some serious profits now!"
            MARBELLA @smile "They won't be seeing us as a joke any longer!"

        "I don't have that kind of coin on me right now...":
            MARBELLA @sad "A-Ahh... I see."
            MARBELLA @smile "Perhaps we should discuss some other business then in the meanwhile?"
    return

label marbella_invest:
    if DialogueMarbella().InvestLevel == 0:
        if DialogueMarbella().FirstTimeInvestTalkAtLevel_0 == True:
            $ DialogueMarbella().FirstTimeInvestTalkAtLevel_0 = False
            show marbella at shake
            MARBELLA @shock "REALLY?"
            MARBELLA @laugh2 "I mean, {i}*cough!*{/i} That's wonderful!"
            MARBELLA @concern "... Sorry, most people don't exactly take us too seriously yet."
            MARBELLA @talk "Anyway, we don't expect you to just hand over the coin for nothing."
            MARBELLA @talk "I'll give you a ten percent profit share of any {i}other{/i} expeditions we do."
            MARBELLA @smile2 "I'll keep your share stashed somewhere safe, then, you can just come in and collect it!"
            MARBELLA @smile2 "The more you invest, not only will we be able to get access to different ore mines for you, but also the greater your share at the end of the month."
            MARBELLA @smile "Sound fair?"
            menu:
                "Ten percent is too low for such high investments on an upstart business with high risks — make it fifteen percent." (Req_Barter = 16):
                    MARBELLA @think "Hmm... Quite the shrewd one, ain't ya?"
                    MARBELLA @smile "Alright, fifteen it is."
                    MARBELLA @think "Anymore and it affects profit margins too much."
                    $ DialogueMarbella().NegotiatedBetterDeal = True
                    call marbella_invest_menu_to_level_1 from _call_marbella_invest_menu_to_level_1

                "Sounds good to me.":
                    MARBELLA @smile "Great! So, to avoid complicating things, I've prioritized investments into a list."
                    MARBELLA @smile "First and foremost is better equipment and official paperwork for us to mine and trade iron ore."
                    MARBELLA @talk "So far, we've only got permission for copper mines."
                    MARBELLA @talk "It'll be ten thousand coins."
                    call marbella_invest_menu_to_level_1 from _call_marbella_invest_menu_to_level_1_1

        else:
            MARBELLA @talk "You got the coin to invest?"
            call marbella_invest_menu_to_level_1 from _call_marbella_invest_menu_to_level_1_2
    elif DialogueMarbella().InvestLevel == 1:
        if DialogueMarbella().FirstTimeInvestTalkAtLevel_1 == True:
            $ DialogueMarbella().FirstTimeInvestTalkAtLevel_1 = False
            MARBELLA @smile "You wanna invest more in us?"
            MARBELLA @think "Well, one thing I'd like is to be able to increase our cargo capacity."
            MARBELLA @sad2 "Right now, we can only haul back about twenty ore between us."
            MARBELLA @smile "With some better equipment, wagons and horses though, we could double our output!"
            MARBELLA @think "That uhh, that'll be at least fifteen thousand coins though..."
            call marbella_invest_menu_to_level_2 from _call_marbella_invest_menu_to_level_2
        else:
            MARBELLA @talk "You got the coin to invest?"
            call marbella_invest_menu_to_level_2 from _call_marbella_invest_menu_to_level_2_1
    return

label marbella_expedition:
    MARBELLA @smile "Can do!"
    MARBELLA @smile "What you looking for?"
    menu marbella_expedition_rootmenu:
        "Iron ore":
            if DialogueMarbella().InvestLevel < 1:
                MARBELLA @sad "Sorry, handsome, we don't have the equipment or the paperwork to handle iron ore mines."
                MARBELLA @shock "But we're looking for some investors which should sort that out!"
                jump marbella_expedition_rootmenu
            MARBELLA @smile "Thanks to your generous investment, we can get you as much iron ore as you like!"
            MARBELLA @talk "So, how much you looking to get?"
            menu marbella_expedition_iron_choice:
                "40 iron ore." (Req_Gold = 8500) if DialogueMarbella().InvestLevel >= 2:
                    $ PlayerRemItem("gold", 8500)
                    $ DialogueMarbella().MiningExpedition(ItemID = "iron_ore", ItemAmount = 40, ExpDelay = 7 * 4)
                    MARBELLA "Oooh, now that's a big order!"
                    MARBELLA  "{i}*mutters* Ain't that the only thing that's big either, I bet.{/i}"
                    MC @think "What was that?"
                    show marbella at shake
                    MARBELLA @laugh2 "Nothing!"
                    MARBELLA @smile "I'll keep it stored here for you to pick up when it's arrived."
                    MARBELLA @talk "It should take about... {b}four weeks.{/b}"
                    jump marbella_expedition_rootmenu

                "20 iron ore." (Req_Gold = 6000):
                    $ PlayerRemItem("gold", 6000)
                    $ DialogueMarbella().MiningExpedition(ItemID = "iron_ore", ItemAmount = 20, ExpDelay = 7 * 3)
                    MARBELLA "Pleasure doing business as always, handsome."
                    MARBELLA @smile "I'll keep it stored here for you to pick up when it's arrived."
                    MARBELLA @talk "It should take about... {b}three weeks.{/b}"
                    jump marbella_expedition_rootmenu

                "10 iron ore." (Req_Gold = 3500):
                    $ PlayerRemItem("gold", 3500)
                    $ DialogueMarbella().MiningExpedition(ItemID = "iron_ore", ItemAmount = 10, ExpDelay = 7 * 2)
                    MARBELLA @talk "Alright, I'll put the order in for you!"
                    MARBELLA @smile "I'll keep it stored here for you to pick up when it's arrived."
                    MARBELLA @talk "It should take about... {b}two weeks.{/b}"
                    jump marbella_expedition_rootmenu

                "On second thought...":
                    MARBELLA @think "Have something else in mind?"
                    jump marbella_expedition_rootmenu

        "Copper ore":
            MARBELLA @smile "Copper ore, we can do!"
            MARBELLA @talk "So, how much you looking to get?"   
            menu marbella_expedition_copper_choice:
                "40 Copper ore." (Req_Gold = 7000) if DialogueMarbella().InvestLevel >= 2:
                    $ DialogueMarbella().MiningExpedition(ItemID = "copper_ore", ItemAmount = 40, ExpDelay = 7 * 4)
                    $ PlayerRemItem("gold", 7000)
                    MARBELLA "Oooh, now that's a big order!"
                    MARBELLA  "{i}*mutters* Ain't that the only thing that's big either, I bet.{/i}"
                    MC @think "What was that?"
                    MARBELLA @smile "Nothing!"
                    MARBELLA @smile "I'll keep it stored here for you to pick up when it's arrived."
                    MARBELLA @talk "It should take about... {b}four weeks.{/b}"
                    jump marbella_expedition_rootmenu

                "20 Copper ore." (Req_Gold = 4000):
                    $ DialogueMarbella().MiningExpedition(ItemID = "copper_ore", ItemAmount = 20, ExpDelay = 7 * 3)
                    $ PlayerRemItem("gold", 4000)
                    MARBELLA  "Pleasure doing business as always, handsome."
                    MARBELLA @smile "I'll keep it stored here for you to pick up when it's arrived."
                    MARBELLA @talk "It should take about... {b}three weeks.{/b}"
                    jump marbella_expedition_rootmenu

                "10 Copper ore." (Req_Gold = 2500):
                    $ DialogueMarbella().MiningExpedition(ItemID = "copper_ore", ItemAmount = 10, ExpDelay = 7 * 2)
                    $ PlayerRemItem("gold", 2500)
                    MARBELLA @talk "Alright, I'll put the order in for you!"
                    MARBELLA @smile "I'll keep it stored here for you to pick up when it's arrived."
                    MARBELLA @talk "It should take about... {b}two weeks.{/b}"
                    jump marbella_expedition_rootmenu

                "On second thought...":
                    MARBELLA @think "Have something else in mind?"
                    jump marbella_expedition_rootmenu

        "Syax Ore":
            # also should be gated by level 2+ AFTER the seals exist
            MARBELLA @sad "Oooh... Sorry, lovely."
            MARBELLA @sad "You need a royal seal for that, and we just ain't got one."
            MARBELLA @think "I'd like to keep my head on my shoulders, so unless we get that seal, we don't mine."
            jump marbella_expedition_rootmenu

        "How about some enchantment runes?":
            MARBELLA @smile "Can do!"
            MARBELLA @talk "What kinda rune you lookin' for?"
            menu:
                "A rune of quickness." (Req_Gold = 2000):
                    $ PlayerRemItem("gold", 2000)
                    $ DialogueMarbella().MiningExpedition(ItemID = "rune_of_quickness", ItemAmount = 1, ExpDelay = 7)
                    MARBELLA @talk "Alright, one rune of quickness I'll have treated and delivered here with the next expedition." 
                    MARBELLA @talk "It should take about... {b}one week.{/b}"
                    jump marbella_expedition_rootmenu

                "A rune of power" (Req_Gold = 2000):
                    $ PlayerRemItem("gold", 2000)
                    $ DialogueMarbella().MiningExpedition(ItemID = "rune_of_power", ItemAmount = 1, ExpDelay = 7)
                    MARBELLA @talk "Ahh, those power runes are a bit trickier to get and treat, but I'll have one delivered here with the next expedition."
                    MARBELLA @talk "It should take about... {b}one week.{/b}"
                    jump marbella_expedition_rootmenu

                "A rune of defence" (Req_Gold = 2000):
                    $ PlayerRemItem("gold", 2000)
                    $ DialogueMarbella().MiningExpedition(ItemID = "rune_of_defence", ItemAmount = 1, ExpDelay = 7)
                    MARBELLA @talk "A defence rune? Alright, next expedition I'll have it found and treated before being brought back here."
                    MARBELLA @talk "It should take about... {b}one week.{/b}"
                    jump marbella_expedition_rootmenu

                "On second thought...":
                    MARBELLA @think "Have something else in mind?"
                    jump marbella_expedition_rootmenu

        "Actually, I've changed my mind...":
            MARBELLA @angry "Seven hells, man... cruel to tease a girl like that!"
            return

label marbella_hasshittogivetoplayer:
    show mc at cright_f with easeinright
    show marbella at cleft with easeinleft
    if DialogueMarbella().ExpeditionsReadyToCollect == True:
        
        MARBELLA @talk "Ahh! Just who I was looking for!"
        MARBELLA @talk "Your order's in!"
        $ DialogueMarbella().DeliverAllExpeditions()
        show marbella at nod
        MARBELLA @smile "Here you go."
        if DialogueMarbella().MoneyReadyToCollect > 0:
            MARBELLA @shock "... Oh!"
            $ PlayerAddItem("gold", DialogueMarbella().MoneyReadyToCollect)
            $ DialogueMarbella().MoneyReadyToCollect = 0
            $ DialogueMarbella().MoneyIncrements = 0
            show marbella at nod
            MARBELLA @smile "And your profit share for your generous donation as well."
    else:
        if DialogueMarbella().MoneyReadyToCollect > 0:
            MARBELLA @smile "Ahh! There you are!"
            $ PlayerAddItem("gold", DialogueMarbella().MoneyReadyToCollect)
            $ DialogueMarbella().MoneyReadyToCollect = 0
            $ DialogueMarbella().MoneyIncrements = 0
            show marbella at nod
            MARBELLA @smile "Here's your cut of the profits!"
    call processDialogue("marbella_root") from _call_processDialogue_64
    $ LocEnter()
