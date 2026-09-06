init python:
    notesLib["tarbeck_rom_1visit"] = Note(
        _("Return to Lady Tarbeck"),
        _("Now that things have settled... Perhaps I should visit Lady Tarbeck and see if there's more than just business between us?"), 
    )
    notesLib["tarbeck_rom_romance_meetmarket"] = Note(
        _("Meet Lady Tarbeck at the market"),
        _("Lady Tarbeck has asked to meet me at the market for our first 'date.'"),
    )
    notesLib["tarbeck_rom_romance_meetlibrary"] = Note(
        _("Meet Lady Tarbeck at the library"),
        _("Lady Tarbeck has asked me to meet her at the library so I might help her with... {i}reading material.{/i}"), 
    )
    notesLib["tarbeck_rom_romance_meetatmanor_afterlibrary"] = Note(
        _("Meet Lady Tarbeck at the manor"),
        _("Lady Tarbeck has requested my presence at the Tarbeck Mannor. We have a lot to discuss I imagine..."), 
    )
    notesLib["tarbeck_rom_romance_meetatquarters"] = Note(
        _("Meet Lady Tarbeck at her quarters"),
        _("Lady Tarbeck has requested I join her in her private quarters... Well, I wouldn't want to keep a lady waiting."), 
    )
    notesLib["tarbeck_rom_romance_scheduledtrio"] = Note(
        _("Meet the ladies at Tarbeck manor"),
        _("Lady Tarbeck will invite Lady Belamore and her friends to her estate tonight. I can stop by for some 'entertainment'."),
    )

    @AppendToAllQuests
    class RomanceLadyTarbeck(LogicModule):
        def __init__(self):
            super().__init__()

            # 0 initial scene & path choice
            # progress "BIMBO" variant
            # 1 meet a couple days after 
            # 2 hunt 3 gangs
            # 3 return
            # 4 wait
            # 5 wait some more
            # 6 wait some more
            # 7 break fast
            # 8 party
            # 9 freeroam

            # progress "ROMANCE" variant
            # 1 meet at market
            # 2 meet at lib
            # 3 meet at manor after lib
            # 4 meet at quarters at night
            # 5 talk to her at daytime, in main hall
            # 6 return to her after dark to meet darkmage
            # 7 return after darkmage (table bj)
            # 8 meet her to escort to brothel
            # 9 meet her after brothel
            # 10 meet her at tarbecks'
            # 11 freeroam

            # progress "DARKMAGE" variant
            # 1 meet at manor next day
            # 2 deal with lord zanzibat about the book
            # 3 wait for lord zanzibat to find book
            # 4 return to lady tarbeck with book
            # 5 return to lady tarbeck after 2 days
            # 6 return to lady tarbeck after dark to meet with darkmange

            self.Kind = "romance"
            # valid: "romance", "darkmage", "bimbo", "closed"

            # even though some of these are prefixed Romance_, 
            # they can be reused for darkmage/bimbo paths

            self.HadSexToday = False

            self.Romance_ScheduledGig = None 
            self.Romance_ScheduledTrio = False
            # valid values vary (like "miss_vag", "miss_anal", "lib" ...)
            self.Romance_AskedForSexToday_Her  = False
            self.Romance_AskedForSexToday_Her_Refused = False
            self.Romance_AskedForSexToday_Trio = False
            self.Romance_AskedForSexToday_Trio_Refused = False
            self.Romance_NextPossibleDragonVisitDay = 0

            self.Darkmage_ZanzibatFee = 2000
            self.Darkmage_TalkedToZanzibatBoutBookOnce = False

            self.Bimbo_SlainGangs = 0 

        def onStart(self):
            NoteUnlock("tarbeck_rom_1visit")
            return

        def onEnter(self):
            if self.progress == 0:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    if IsDaytime():
                        return TriggeredEvent("rom_tarbeck_intro")
            if self.Kind == "romance":
                if self.progress == 2:
                    if GetLocID() == "hamun_library":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_romance_meet_library")
                elif self.progress == 3:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            if QstDelayCheck(self):
                                return TriggeredEvent("rom_tarbeck_romance_meet_manor")
                elif self.progress == 4:
                    if GetLocID() == "hamun_tarbeck_quarters_lady":
                        if not IsDaytime():
                            return TriggeredEvent("rom_tarbeck_romance_meet_quarters")
                elif self.progress == 5:
                    if GetLocID() == "hamun_library":
                        if self.Romance_ScheduledGig == "lib":
                            if IsDaytime():
                                return TriggeredEvent("rom_tarbeck_romance_meet_library")
                    elif GetLocID() == "hamun_tarbeck_quarters_lady":
                        if self.Romance_ScheduledGig == "miss_vag":
                            if not IsDaytime():
                                return TriggeredEvent("rom_tarbeck_romance_meet_quarters")
                        elif self.Romance_ScheduledGig == "miss_anal":
                            if not IsDaytime():
                                return TriggeredEvent("rom_tarbeck_romance_meet_quarters_anal")
            elif self.Kind == "darkmage":
                if self.progress == 1:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_darkmage_meet_manor")
                elif self.progress == 3:
                    if GetLocID() == "hamun_zanzibat_house":
                        return TriggeredEvent("rom_tarbeck_darkmage_zanzibat_pickup_grimoire")
                elif self.progress == 4:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_darkmage_bring_grimoire")
                elif self.progress == 5:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_darkmage_return_after_grimoire")
                elif self.progress == 6:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if not IsDaytime():
                            return TriggeredEvent("rom_tarbeck_darkmage_meetmage")
                elif self.progress == 7:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_darkmage_returnaftermage")
                elif self.progress == 8:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if not IsDaytime():
                            if QstDelayCheck(self):
                                return TriggeredEvent("rom_tarbeck_darkmage_escorttobrothel")
                elif self.progress == 9:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if not IsDaytime():
                            return TriggeredEvent("rom_tarbeck_darkmage_meetafterbrothel")
                elif self.progress == 10:
                    if GetLocID() == "hamun_tarbeck_quarters_lord":
                        return TriggeredEvent("rom_tarbeck_darkmage_spell")
                elif self.progress == 11:
                    if GetLocID() == "hamun_brothel":
                        if self.Romance_ScheduledGig == "date_brothel":
                            return TriggeredEvent("repeat_tarbeck_darkmage_brothel")
                    elif GetLocID() == "hamun_tarbeck_quarters_lady":
                        if not IsDaytime():
                            if self.Romance_ScheduledGig == "portal_vag":
                                return TriggeredEvent("repeat_tarbeck_darkmage_portal_vag")
                            elif self.Romance_ScheduledGig == "portal_anal":
                                return TriggeredEvent("rom_tarbeck_darkmage_portal_anal")
            elif self.Kind == "bimbo":
                if self.progress == 1:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_meet_coupledays")
                elif self.progress == 2:
                    renpy.hide_screen("RomLadyTarbeckKillBandits")
                    if self.Bimbo_SlainGangs < 3:
                        if not IsDaytime():
                            if GetLocID() in ["hamun_dist_docks"]:
                                renpy.show_screen("RomLadyTarbeckKillBandits")
                elif self.progress == 3:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_meet_after_bandits_slain")
                elif self.progress == 4:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_return_after_rest")
                elif self.progress == 5:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_return_tf_again")
                elif self.progress == 6:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_return_after_tf")
                elif self.progress == 7:
                    if GetLocID() == "hamun_tarbeck_dining":
                        if IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_join_breakfast")
                elif self.progress == 8:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if not IsDaytime():
                            return TriggeredEvent("rom_tarbeck_bimbo_party")
                elif self.progress >= 9:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        if not IsDaytime():
                            if self.Romance_ScheduledGig == "bimboparty":
                                return TriggeredEvent("rom_tarbeck_bimbo_party")
            if GetLocID() == "hamun_tarbeck_mainhall":
                if not IsDaytime():
                    if self.Romance_ScheduledTrio:
                        return TriggeredEvent("rom_tarbeck_hamun_trio_choices")

        def onMidnight(self):
            if self.Romance_ScheduledGig == None:
                self.HadSexToday = False
                self.Romance_AskedForSexToday_Her  = False
                self.Romance_AskedForSexToday_Her_Refused = False
                self.Romance_AskedForSexToday_Trio = False
                self.Romance_AskedForSexToday_Trio_Refused = False
            return

        def locationMod(self):
            btnMods = {}
            # love locmods
            if self.Kind == "romance":
                if self.progress == 1:
                    if GetLocID() == "hamun_market":
                        if IsDaytime() == False:
                            btnMods["btn_hamun_market_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "rom_tarbeck_romance_meet_market")
                if self.progress >= 5:
                    if self.Romance_ScheduledGig == None:
                        if GetLocID() == "hamun_tarbeck_mainhall":
                            if IsDaytime():
                                btnMods["btn_hamun_tarbeck_mainhall_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "rom_tarbeck_romance_talk_mainhall")
            elif self.Kind == "darkmage":
                if self.progress == 2:
                    btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnChangeLoc(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "hamun_zanzibat_house")
                elif self.progress == 3:
                    if QstDelayCheck(self):
                        btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnChangeLoc(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "hamun_zanzibat_house")
                elif self.progress == 10:
                    btnMods["hamun_tarbeck_mainhall_to_dist_merch_lord"] = BtnJumpLabel(STR_LOC.HAMUN_DIST_MERCH_LORD , "rom_tarbeck_darkmage_cantleave")

                elif self.progress >= 11:
                    if self.Romance_ScheduledGig == None:
                        if GetLocID() == "hamun_tarbeck_mainhall":
                            if IsDaytime():
                                btnMods["btn_hamun_tarbeck_mainhall_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "rom_tarbeck_darkmage_talk_mainhall")
            elif self.Kind == "bimbo":
                if self.progress >= 9:
                    if self.Romance_ScheduledGig == None:
                        if GetLocID() == "hamun_tarbeck_mainhall":
                            if IsDaytime():
                                btnMods["btn_hamun_tarbeck_mainhall_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "rom_tarbeck_bimbo_talk_mainhall")
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onPostSleepHamunHookahBar(self):
            if self.Kind == "romance":
                if self.progress >= 5:
                    if GetGameDay() > self.Romance_NextPossibleDragonVisitDay:
                        if self.Romance_ScheduledGig == None:
                            if RngInt(1, 5) == 1:
                                return TriggeredEvent("rom_tarbeck_romance_nightvisit")

        def extraDialogue(self):
            if self.Kind == "darkmage":
                # talk to zanzibat bout book
                if self.progress == 2:
                    if self.Darkmage_TalkedToZanzibatBoutBookOnce:
                        yield ("zanzibat_root", DNode(_("About the grimoire..."), "rom_tarbeck_darkmage_zanzibat_grimoire_repeat", order = 100))
                    else:
                        yield ("zanzibat_root", DNode(_("I have a private matter I wish to discuss with you..."), "rom_tarbeck_darkmage_zanzibat_grimoire_first", order = 100))
        # reused by all 3 variants
        def AskForSex(self):
            Result = False
            if self.Romance_AskedForSexToday_Her:
                if self.Romance_AskedForSexToday_Her_Refused or self.HadSexToday:
                    Result = False
                else:
                    Result = True
            else:
                Roll = RngInt(1,2)
                if Roll == 1:
                    Result = True
                elif Roll == 2:
                    Result = False
            self.Romance_AskedForSexToday_Her = True
            if Result == False:
                self.Romance_AskedForSexToday_Her_Refused = True
            return Result
        # reused by all 3 variants
        def AskForSexTrio(self):
            Result = False
            if self.Romance_AskedForSexToday_Trio:
                if self.Romance_AskedForSexToday_Trio_Refused:
                    Result = False
                else:
                    Result = True
            else:
                Roll = RngInt(1,2)
                if Roll == 1:
                    Result = True
                elif Roll == 2:
                    Result = False
            self.Romance_AskedForSexToday_Trio = True
            if Result == True:
                self.Romance_ScheduledTrio = True
                NoteUnlock("tarbeck_rom_romance_scheduledtrio")
            else:
                self.Romance_AskedForSexToday_Trio_Refused = True
            return Result











label rom_tarbeck_romance_talk_mainhall:
    show lady_tarbeck at center with dissolve
    LADY_TARBECK @smile "I've been waiting for you to come back."
    LADY_TARBECK @talk "How can I help?"
    menu rom_tarbeck_romance_talk_mainhall_menu:
        "I was wondering if you might be interested in having some... {i}fun?{/i}" (AppearIf = (RomanceLadyTarbeck().Romance_ScheduledGig == None)):
            $ tmpvar = {}
            $ tmpvar["agree"] = RomanceLadyTarbeck().AskForSex()

            # refusal
            if tmpvar["agree"] == False:
                LADY_TARBECK @talk "Not today, I'm afraid. There are some urgent accounts that need settling."
                $ tmpvar = {}
                jump rom_tarbeck_romance_talk_mainhall_menu
            $ tmpvar = {}

            # agree
            LADY_TARBECK @blush2 "... What did you have in mind?"
            menu:
                "Perhaps we could continue reading at the library...":
                    "Lady Tarbeck fluttered her eyes."
                    LADY_TARBECK @blush2 "Hmm, reading a few extra chapters does sound fun."
                    LADY_TARBECK @smile "I'll head over to the library shortly."
                    LADY_TARBECK @blush2 "Don't keep me waiting."
                    hide lady_tarbeck with dissolve
                    $ RomanceLadyTarbeck().Romance_ScheduledGig = "lib"
                    $ NoteUnlock("tarbeck_rom_romance_meetlibrary")
                    $ LocEnter()

                "I was thinking we could take a stroll through your gardens again...":
                    $ RomanceLadyTarbeck().HadSexToday = True
                    "Lady Tarbeck looked down as she licked her lips."
                    LADY_TARBECK "Yes... Let's go for another..."
                    LADY_TARBECK "{i}walk.{/i}"
                    scene black with dissolve
                    $ SetRepeatVariant(True)
                    jump rom_tarbeck_romance_meet_manor_repeat

                "I was thinking I might come to your chambers tonight...":
                    LADY_TARBECK @blush2 "How presumptuous!"
                    LADY_TARBECK @blush2 "And what did you plan to do to this poor little wife once you burst your way into her chambers?"
                    menu:
                        # missionary vag
                        "To remind you that you might be his wife, but you're my woman.":
                            $ RomanceLadyTarbeck().Romance_ScheduledGig = "miss_vag"
                            LADY_TARBECK @blush2 "Bold little savage when you want to be, aren't you?"
                            LADY_TARBECK @smile "{i}*Sigh*{/i} Well, I guess there's no helping it..."
                            LADY_TARBECK @blush2 "Head to my chambers tonight... I'll be waiting."

                        # missionary anal
                        "To bury my cock in the one place you wouldn't dream of letting Lord Tarbeck touch... Your tight ass.":
                            $ RomanceLadyTarbeck().Romance_ScheduledGig = "miss_anal"
                            LADY_TARBECK @shock "By Malakai's balls, you really are something, aren't you!"
                            MC @smile "Is that a no?"
                            "Lady Tarbeck pouted at my request, her eyes wandering around the room before she stepped closer."
                            LADY_TARBECK @talk "... Be on your best behaviour and maybe, {i}MAYBE{/i}, I'll let you put it there."
                            MC @smile "Always, my lady."
                            LADY_TARBECK @smile "Don't be late. Bring your ass to my chambers tonight..."
                            LADY_TARBECK @talk "And don't let me regret telling you where to {i}put{/i} it..."

                    $ NoteUnlock("tarbeck_rom_romance_meetatquarters")
                    $ LocEnter()

                "Nevermind.":
                    LADY_TARBECK "...Okay."
                    jump rom_tarbeck_romance_talk_mainhall_menu

        "How is our child?" (AppearIf = CharGetBirths("lady_tarbeck") > 0):            
            $ tmpvar = {}
            $ tmpvar = RngInt(1, 3)
            if tmpvar == 1:
                LADY_TARBECK @smile "Strong... And being spoiled rotten by their {i}'father.'{/i}"
                MC @think "Is... Lord Tarbeck-"
                LADY_TARBECK @talk "He can hardly complain, given he's introduced me to at least a dozen of his bastards over the years."
                LADY_TARBECK @talk "I can't tell whether he's pleased for me or if... {i}he quietly enjoys knowing.{/i}"
                LADY_TARBECK @talk "Possibly both, knowing him."
            elif tmpvar == 2:
                LADY_TARBECK @think "Do... Do children normally speak their first words so soon?"
                LADY_TARBECK @shock "Whatever child you and I have sired, they might be a genius!"
            elif tmpvar == 3:
                LADY_TARBECK @smile "A cute, adorable little ball."
                LADY_TARBECK @talk "... Though I swear they're already growing up so fast!"
            $ tmpvar = {}

        "Are you well?" (AppearIf = CharIsVisiblyPreg("lady_tarbeck")):
            $ tmpvar = {}
            $ tmpvar = RngInt(1, 3)
            if tmpvar == 1:
                LADY_TARBECK @shock "When they kick, I swear if I'm not careful they might break a rib!"
                LADY_TARBECK @think "I've never heard of a child being so strong..."
                LADY_TARBECK @think "... Your fault, I presume?"
            elif tmpvar == 2:
                LADY_TARBECK @smile "I can't stop looking at myself in the mirror."
                LADY_TARBECK @blush "Me... A mother."
            elif tmpvar == 3:
                LADY_TARBECK @think "I have an insatiable desire for... mangos?"
            $ tmpvar = {}

        "Lady Belamore and her friends... Can you summon them?" (AppearIf = (RomanceLadyTarbeck().Romance_AskedForSexToday_Trio == False)):
            $ tmpvar = {}
            $ tmpvar["agree"] = RomanceLadyTarbeck().AskForSexTrio()

            if tmpvar["agree"] == False:
                LADY_TARBECK @talk "Not tonight. Lord Tarbeck intends to entertain... {i}other guests.{/i}"
                $ tmpvar = {}
                jump rom_tarbeck_romance_talk_mainhall_menu
            $ tmpvar = {}

            LADY_TARBECK @smile "... Come back this evening."
            LADY_TARBECK @blush2 "I'll make sure the ladies are here... Fufu."
            

        "I must take my leave.":
            LADY_TARBECK @sad "C-Come back soon..."
            $ LocEnter()

    jump rom_tarbeck_romance_talk_mainhall_menu









######## darkmage variant
# this is mostly duped above so watch out
label rom_tarbeck_darkmage_talk_mainhall:
    show lady_tarbeck at center with dissolve
    LADY_TARBECK @smile "What do you need?"
    menu rom_tarbeck_darkmage_talk_mainhall_menu:
        "I was wondering if you might be interested in some... Fun." (AppearIf = (RomanceLadyTarbeck().Romance_ScheduledGig == None)):
            $ tmpvar = {}
            $ tmpvar["agree"] = RomanceLadyTarbeck().AskForSex()

            # refusal
            if tmpvar["agree"] == False:
                LADY_TARBECK @sad "As tempting as it would be to straddle you in front of my husband..."
                LADY_TARBECK @sad "I have studies to attend to... *sigh.*"
                $ tmpvar = {}
                jump rom_tarbeck_romance_talk_mainhall_menu
            $ tmpvar = {}

            # agree
            LADY_TARBECK @smile "Now that sounds fun..."
            LADY_TARBECK @smile "What do you propose?"
            menu:
                "I was wondering if you could do that thing with your thighs again...":
                    $ RomanceLadyTarbeck().HadSexToday = True
                    "Lady Tarbeck smiled mischievously."
                    LADY_TARBECK @smile "... Come with me."
                    scene black with dissolve
                    $ SetRepeatVariant(True)
                    jump replay_tarbeck_darkmage_thighjob

                "Is Lord Tarbeck here... I was wondering if perhaps you would enjoy what we did beneath the table again.":
                    $ RomanceLadyTarbeck().HadSexToday = True
                    LADY_TARBECK @smile "I am always happy to make a cuckold of my husband. You should know this by now."
                    LADY_TARBECK @smile "... I'll call him down and tell him you want to talk while you eat."
                    scene black with dissolve
                    $ SetRepeatVariant(True)
                    $ LocSet("hamun_tarbeck_dining")
                    jump replay_tarbeck_darkmage_tablebj

                "I was thinking we might go on another... date, if you were interested.":
                    LADY_TARBECK @smile "Hmm... I wonder if those Katai are missing us already after that last performance?"
                    LADY_TARBECK @blush "... Meet me at that brothel tonight. I'll be waiting."
                    $ RomanceLadyTarbeck().Romance_ScheduledGig = "date_brothel"
                    $ NoteUnlock("tarbeck_rom_darkmage_meet_at_brothel_rep")
                    $ LocEnter()

                "So... I would love to stay the night again.":
                    LADY_TARBECK @smile "Miss seeing my ass shoved through a portal, hm?"
                    LADY_TARBECK @talk "I'll let Lord Tarbeck know you'll be staying here tonight."
                    menu:
                        "I look forward to it...":
                            $ RomanceLadyTarbeck().Romance_ScheduledGig = "portal_vag"
                            LADY_TARBECK @smile "Sweet dreams..."

                        "I have a special request... Your ass.":
                            $ RomanceLadyTarbeck().Romance_ScheduledGig = "portal_anal"
                            "Lady Tarbeck blinked at the request, then smiled mischievously."
                            LADY_TARBECK @smile "Wanting the place I don't let my husband touch..."
                            LADY_TARBECK @blush "Tsk... Tsk... How naughty."
                            LADY_TARBECK @blush2 "I'll see what I can do about it... No promises."

                    $ NoteUnlock("tarbeck_rom_romance_meetatquarters")
                    $ LocEnter()

                "You know... I think Lord Tarbeck could really do with another long sleep.":
                    "Lady Tarbeck grinned as she licked her lips."
                    LADY_TARBECK @smile "He does work sooooo hard."
                    LADY_TARBECK @blush "... Oh darling! Come here a moment!"
                    TARBECK "Dear, what is it?"
                    LADY_TARBECK @smile "{i}*Chuckles*{/i}"
                    scene black with dissolve
                    $ SetRepeatVariant(True)
                    $ RomanceLadyTarbeck().HadSexToday = True
                    $ LocSet("hamun_tarbeck_quarters_lord")
                    "Which way should I fuck her this time?"
                    menu:
                        "Anal":
                            jump rom_tarbeck_darkmage_spell_anal
                        "Vaginal":
                            jump repeat_tarbeck_darkmage_spell_vag

                "On second thought...":
                    LADY_TARBECK @think "... Go on?"
                    jump rom_tarbeck_darkmage_talk_mainhall_menu

        "How is the little one?" (AppearIf = CharGetBirths("lady_tarbeck") > 0):
            $ tmpvar = {}
            $ tmpvar = RngInt(1, 4)
            if tmpvar == 1:
                LADY_TARBECK @smile "Our child is already showing signs of brilliance!"
                LADY_TARBECK @smile "She will prove to be a powerful mage... I can feel it."
            elif tmpvar == 2:
                LADY_TARBECK @smile "She seems to know instinctively when you are around... She laughs more."
            elif tmpvar == 3:
                LADY_TARBECK @smile "Very good. Now put another one in me."
            elif tmpvar == 4:
                LADY_TARBECK @think "My husband spoils her already. He seems to think she should be educated privately here when she is older, but I think Newyark might be better... What do you think?"
            $ tmpvar = {}

        "How are you feeling?" (AppearIf = CharIsVisiblyPreg("lady_tarbeck")):
            $ tmpvar = {}
            $ tmpvar = RngInt(1, 3)
            if tmpvar == 1:
                LADY_TARBECK @think "I have a craving for... mangoes?"
            elif tmpvar == 2:
                LADY_TARBECK @smile "I love her already..."
                LADY_TARBECK @sad "I hate what she is doing to my back."
            elif tmpvar == 3:
                LADY_TARBECK @smile "Awww, concerned are we?"
                LADY_TARBECK @smile "You're sweet..."
            $ tmpvar = {}

        "How about a kiss?":
            LADY_TARBECK @think "A kiss?"
            "Lady Tarbeck stared for a moment before smiling."
            LADY_TARBECK @smile "{i}*Sigh*{/i} Even now, you're still my white knight."
            LADY_TARBECK @smile "... Come here."
            hide lady_tarbeck
            hide mc
            show cg_lady_tarbeck_darkmage_kiss_normal at center
            with dissolve
            "Lady Tarbeck pressed her lips up against mine as I gentlys squeezed at her ass."
            LADY_TARBECK "Mmmfghh..."
            hide cg_lady_tarbeck_darkmage_kiss_normal
            show lady_tarbeck at center
            with dissolve
            LADY_TARBECK @smile "There, satisfied?"
        
        "I was thinking of paying Lady Belamore and her friends a visit." (AppearIf = (RomanceLadyTarbeck().Romance_AskedForSexToday_Trio == False)):
            $ tmpvar = {}
            $ tmpvar["agree"] = RomanceLadyTarbeck().AskForSexTrio()

            if tmpvar["agree"] == False:
                LADY_TARBECK @talk "Not tonight. Lord Tarbeck intends to entertain... {i}other guests.{/i}"
                $ tmpvar = {}
                jump rom_tarbeck_darkmage_talk_mainhall_menu
            $ tmpvar = {}

            LADY_TARBECK @think "Hm... It has been a while, I suppose."
            LADY_TARBECK @smile "I'll summon them to the manor..."
            LADY_TARBECK @smile "Something tells me those pitiful whores will come running."

        "How goes your studies?":
            LADY_TARBECK @think "Lazarian seems impressed with my studies so far."
            LADY_TARBECK @sad "Though I must admit... It is rather disconcerting seeing a man get aroused whenever he passes a graveyard."
            MC @talk "As long as his hands stay away from you, he can fuck as many ghouls as he likes."
            LADY_TARBECK @smile "{i}I love it when you're possessive...{/i}"
            LADY_TARBECK @blush "It's just so... {i}primal.{/i}"

        "For now, I'd best take my leave.":
            LADY_TARBECK @smile "Return soon... {i}My love.{/i}"
            $ LocEnter()
    jump rom_tarbeck_darkmage_talk_mainhall_menu





label rom_tarbeck_bimbo_talk_mainhall:
    show lady_tarbeck at center with dissolve
    LADY_TARBECK @smile "Hellooooo!"
    menu rom_tarbeck_bimbo_talk_mainhall_menu:
        "I was wondering if you might be interested in some... Fun.":
            $ tmpvar = {}
            $ tmpvar["agree"] = RomanceLadyTarbeck().AskForSex()

            # refuse
            if tmpvar["agree"] == False:
                LADY_TARBECK @sad "Sadly, I've gotta like, go with my husband and be all normal and respectable..."
                LADY_TARBECK @sad "{i}*Sigh*{/i} I'm gonna miss your cock so much when I'm BOREDDDDD!"
                $ tmpvar = {}
                jump rom_tarbeck_bimbo_talk_mainhall_menu
            $ tmpvar = {}

            # accept
            LADY_TARBECK @smile "OOOOH! What do you want to do?"
            menu:
                "I was thinking I could slam my cock between your tits and mouth again.":
                    $ RomanceLadyTarbeck().HadSexToday = True
                    "Lady Tarbeck licked her lips."
                    LADY_TARBECK @blush "MY LOVEEE!"
                    TARBECK "What is it, dear!?"
                    LADY_TARBECK @blush "Come watch [player_name] fuck my tits and mouth again!"
                    TARBECK "{i}*Sigh*{/i} Coming now..."
                    scene black with dissolve
                    $ SetRepeatVariant(True)
                    jump repeat_tarbeck_bimbo_tj

                "I was wondering if we could head to your private quarters again.":
                    $ RomanceLadyTarbeck().HadSexToday = True
                    LADY_TARBECK @smile "Awww, you big romantic!"
                    LADY_TARBECK @blush "I'll go see if Lord Tarbeck wants to watch us make love again, teehee!"
                    scene black with dissolve
                    $ SetRepeatVariant(True)
                    jump repeat_tarbeck_bimbo_miss

                "I was wondering if I might join you at the dining table.":
                    LADY_TARBECK @smile "Huh? Are you hungry? I can have the chefs prepare some-"
                    LADY_TARBECK @shock "... Oooooh! You wannna fuck me over the table again!"
                    LADY_TARBECK @blush "Hehe, I'm so silly!"
                    $ tmpvar = {}
                    menu:
                        "What if this time... You let me put it in your rear instead?": 
                            $ tmpvar["variant"] = "anal"
                            LADY_TARBECK @shock "You wanna put it in my butt?!"
                            LADY_TARBECK @blush "... Sounds fun!"
                            MC @shock "Just like that?"
                            LADY_TARBECK @blush "Uhuh, just lemme call my husband and prep my little hole for you!"
                            LADY_TARBECK @blush "He's {i}DEFINITELY{/i} gonna wanna see this!"

                        "I'm starving already...": 
                            $ tmpvar["variant"] = "vag"
                            LADY_TARBECK @blush "Then let me see if my husband is busy so I can feed you what you need, {i}darling.{/i}"
                    $ SetRepeatVariant(True)
                    $ RomanceLadyTarbeck().HadSexToday = True
                    if tmpvar["variant"] == "anal":
                        jump rom_tarbeck_bimbo_breakfast_anal
                    elif tmpvar["variant"] == "vag":
                        jump repeat_tarbeck_bimbo_breakfast

                "When are you throwing another party?":
                    LADY_TARBECK @blush "Mhmm... We were thinking about throwing one tonight."
                    LADY_TARBECK @blush "You know what that means... Bring your cute butt and monstrous cock over here this evening, {i}handsome.{/i}"
                    $ RomanceLadyTarbeck().Romance_ScheduledGig = "bimboparty"
                    $ NoteUnlock("tarbeck_rom_bimbo_party")

                "On second thought...":
                    LADY_TARBECK @talk "Mmm?"
                    jump rom_tarbeck_bimbo_talk_mainhall_menu

        "How is the little one?"  (AppearIf = CharGetBirths("lady_tarbeck") > 0):
            $ tmpvar = {}
            $ tmpvar = RngInt(1, 4)
            if tmpvar == 1:
                LADY_TARBECK @smile "SHE'S. JUST. SO. CUTEEEE!"
                LADY_TARBECK @smile "I wuv her shooo muchh!"
            elif tmpvar == 2:
                LADY_TARBECK @smile "Hehe, my husband and I love to spoil our little princess so much."
            elif tmpvar == 3:
                LADY_TARBECK @smile "TODAY SHE ROLLED OVER AND GIGGLED! IT WAS AMAZING!"
            elif tmpvar == 4:
                LADY_TARBECK @think "She really likes my milk..."
                LADY_TARBECK @smile "Maybe something she learned from you?"
            $ tmpvar = {}

        "How are you feeling?" (AppearIf = CharIsVisiblyPreg("lady_tarbeck")):
            $ tmpvar = {}            
            $ tmpvar = RngInt(1, 3)
            if tmpvar == 1:
                LADY_TARBECK @think "Is it weird I like, miss your cum?"
                LADY_TARBECK @shock "Like, I have a real craving for you to just cum down my throat right now!"
            elif tmpvar == 2:
                LADY_TARBECK @smile "Hehe, I can feel the little one kick occasionally!"
                LADY_TARBECK @sad "I'm gonna be the best mother ever to ALL your littluns! I promise!"
            elif tmpvar == 3:
                LADY_TARBECK @smile "You're SOOOO sweet for asking!"
                LADY_TARBECK @smile "I'm good, thank you!"
            $ tmpvar = {}

        "How about a kiss?":
            LADY_TARBECK @smile "Duhh! Do you even need to ask?"
            "Lady Tarbeck practically flung herself into my arms."
            hide lady_tarbeck
            hide mc
            show cg_lady_tarbeck_bimbo_kiss_normal at center
            with dissolve
            "She pressed her pillowy, soft lips and tongue up against mine as I fondled her fat ass."
            LADY_TARBECK "Mmmfghh..."
            hide cg_lady_tarbeck_bimbo_kiss_normal
            show lady_tarbeck at center
            with dissolve
            LADY_TARBECK @smile "That was fun!"
            LADY_TARBECK @blush "Now I'm just horny though!"
            jump rom_tarbeck_bimbo_talk_mainhall_menu

        "Could you invite Lady Belamore and her friends here for me?" (AppearIf = (RomanceLadyTarbeck().Romance_AskedForSexToday_Trio == False)):
            $ tmpvar = {}
            $ tmpvar["agree"] = RomanceLadyTarbeck().AskForSexTrio()

            if tmpvar["agree"] == False:
                LADY_TARBECK @talk "Not tonight. Lord Tarbeck intends to entertain... {i}other guests.{/i}"
                $ tmpvar = {}
                jump rom_tarbeck_bimbo_talk_mainhall_menu
            $ tmpvar = {}

            LADY_TARBECK @smile "Ooooh! Like, of course I can!"
            LADY_TARBECK @smile "I really hope they all learn to stop being so mad and just enjoy your cock like I do!"
            LADY_TARBECK @blush "Then we can have like, fuck-fests together instead of fighting all the time!"
            LADY_TARBECK @blush "Doesn't that sound more fun, hehe?"

        "For now, I'd best take my leave.":
            LADY_TARBECK @smile "C-Come back soon, alright?!"
            LADY_TARBECK @smile "I LOVE YOUUUU!"
            $ LocEnter()

    jump rom_tarbeck_bimbo_talk_mainhall_menu
