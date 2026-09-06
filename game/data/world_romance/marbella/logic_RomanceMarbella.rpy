init python:
######## dominance path notes
    notesLib["marbella_dom_cooldown"] = Note(
        _("Return to Marbella later"), 
        _("After what happened, I should give Marbella a day or two to cool off before checking in on her again..."),
        journal_flag_delayed = True,
    )
    notesLib["marbella_chase_creature"] = Note(
        _("Pursue the 'creature' at night"),
        _("Shyahtan claims he knows a way to push Marbella even further - but first, we must hunt a strange creature. He believes that if I walk the streets at night, he’ll be able to catch its scent."),
    )
    notesLib["marbella_dom_return_after_face"] = Note(
        _("Return to Marbella"),
        _("Now I've done as Shyahtan asked, I should return to Marbella... I just hope whatever Shyahtan has planned was worth it."),
    )
    notesLib["marbella_dom_get_disguise"] = Note(
        _("Buy a disguise for Marbella"),
        _("Marbella needs a disguise for what I have planned next... I think a tailor should be able to assist."),
    )
    notesLib["marbella_dom_wait_for_disguise"] = Note(
        _("Collect the disguise when it's ready"),
        _("Giselra will need a few days to prepare Marbella's disguise... I should check in then."),
    )
    notesLib["marbella_dom_return_with_disguise"] = Note(
        _("Give Marbella her disguise"),
        _("I need to give Marbella her disguise... I hope she likes it."),
    )
    notesLib["marbella_dom_market_meet"] = Note(
        _("Head to the Market at night and find Marbella"),
        _("Marbella should be waiting at the market tonight in disguise... This is going to be fun!"),
    )
    notesLib["marbella_dom_check_after_market"] = Note(
        _("Check in on Marbella"),
        _("After a crazy night, I should check in to make sure Marbella is still alright..."),
    )
    notesLib["marbella_dom_meet_at_pale_dragon"] = Note(
        _("Meet Marbella at The Pale Dragon at night"),
        _("It seems the secret of our affair is out... I need to meet with Marbella tonight at The Pale Dragon to smooth things over with Gavkat and the other dwarves..."),
    )
#################################
######### gang route notes
    notesLib["marbella_gang_hunt_face"] = Note(
        _("Hunt the 'creature' at night"),
        _("A strange creature has been killing gang members at night... The khazah have hired me to kill it for a reward."),
    )
    notesLib["marbella_gang_report_face"] = Note(
        _("Return to the Khazah leader"),
        _("Now that the strange creature has been dealt with, I should return to the Khazah leader and report what's happened."),
    )
    notesLib["marbella_gang_package_reminder"] = Note(
        _("Khazah gang supplies"),
        _("I should remember to check in bi-weekly to collect supplies from the Khazah."),
        journal_flag_persistent = True,
    )
#################################
######### love route notes
    # for when she asks you to come back at night for a date
    notesLib["marbella_love_meet_date"] = Note(
        _("Date night with Marbella"), 
        _("Marbella and I have a date this evening... I should head back to The Crooked Shaft and Co after dark."), 
    )
    # says visit marbella "2 days later" or whatever, after date 
    notesLib["marbella_love_come_back_after_date"] = Note(
        _("Check in on Marbella"), 
        _("I should check how Marbella is doing later..."), 
        journal_flag_delayed = True,
    )
    #  visit marbella after the library-arena-whatever event
    notesLib["marbella_love_come_back_after_walk"] = Note(
        _("Return to Marbella"), 
        _("That was quite the evening... I should pass by to make sure things are still going well with the business"), 
    )
    # visit zanzibat about the slaughtered guard
    notesLib["marbella_love_visit_zanzibat_after_guard_killed"] = Note(
        _("Report the dead guard to Lord Zanzibat"), 
        _("Someone or {i}something{/i} has murdered Lord Zanzibat's guard... I must report the news to him."), 
    )
    # seek the creature at night and kill it (about the face)
    notesLib["marbella_love_deal_with_the_face"] = Note(
        _("Find the murderer"), 
        _("The creature that murdered the guard stalks Hamun at night... If I'm going to find it, I should wander around the city after dark."), 
    )
    # face dealt with, report to zanzibat
    notesLib["marbella_love_report_theface"] = Note(
        _("Report to Zanzibat"), 
        _("The creature has been dealt with, I should tell Lord Zanzibat the news."), 
    )
    # return to marbella after dealing w/zanzibat about the face
    notesLib["marbella_love_return_to_marbella_after_face"] = Note(
        _("Tell Marbella the good news"), 
        _("I should let Marbella know a new guard is on the way and I've dealt with the problem."), 
    )
    # return to marbella tmorrow to talk about "her plan"
    notesLib["marbella_love_return_to_marbella_theplan"] = Note(
        _("Speak to Marbella about her big plan"), 
        _("Marbella keeps mentioning some kind of 'big plan' she has... I should speak to her about it tomorrow."),
        journal_flag_delayed = True,
    )
    # memo if you puss out of the plan first time, FOR REPEAT
    notesLib["marbella_love_theplan_memo"] = Note(
        _("Give your answer to Marbella"), 
        _("Marbella is awaiting an answer on whether I'll help her or not with her plan to scout out that mine."), 
    )
    # "return to marbella" after the mine travel thing
    notesLib["marbella_love_return_after_minetravel"] = Note(
        _("Check in on how Marbella is doing."), 
        _("Marbella seemed quite frightened by that encounter in the mine... I should check in to see how she is holding up in a couple days."), 
        journal_flag_delayed = True,
    )
    # find tailor for marbella only if you havent met giselra at the moment
    notesLib["marbella_love_find_tailor"] = Note(
        _("Find a tailor in Hamun"), 
        _("There has to be a good tailor around here... But where?"), 
    )
    # meet marbella at giselra's store
    notesLib["marbella_love_meet_at_giselra"] = Note(
        _("Meet Marbella at Giselra's"), 
        _("Marbella is meeting me at Giselra the tailor's store, tomorrow. I should head over when I am ready to join her."), 
        journal_flag_delayed = True,
    )
    # buy dress for marbella only appears if yu say "no coin atm"
    notesLib["marbella_love_buy_dress"] = Note(
        _("buy wedding dress for Marbella"), 
        _("Marbella deserves to be happy, we may not be able to marry, but perhaps we can at least pretend if I buy this dress?"), 
    )
    # pickup dress in 3 days
    notesLib["marbella_love_pickup_dress_later"] = Note(
        _("wait for Giselra"), 
        _("Giselra will need a few days to finish the dress for Marbella... I should wait."), 
        journal_flag_delayed = True,
    )
    # get bottle of wine (from luna at spa)
    notesLib["marbella_love_get_wine"] = Note(
        _("Find wine for Marbella"), 
        _("I need to find some expensive wine for a special occasion... Perhaps I might be able to purchase some at the bathhouse?"), 
    )
    # get ring (from beshar)
    notesLib["marbella_love_get_ring"] = Note(
        _("Find a ring for Marbella"), 
        _("I need to find a ring for Marbella... Perhaps I should speak to a blacksmith to have one forged?"), 
    )
    # get flowers (from katiya)
    notesLib["marbella_love_get_flowers"] = Note(
        _("Find flowers for Marbella"), 
        _("Some roses would do nicely... I wonder if I could get some in the store?"), 
    )
    # bring all the stuff (wine, ling, ring, flwoers) to marbella
    notesLib["marbella_love_bring_stuff"] = Note(
        _("Give Marbella her gifts."), 
        _("I have everything I need, now I just need to give the dress and items to Marbella."), 
    )
    # return at night for thw edding shit
    notesLib["marbella_love_return_night_wedding"] = Note(
        _("Head to your room for the wedding night."), 
        _("Marbella will be waiting for me in my quarters at {i}The Pale Dragon{/i} tonight, I should be there... After all, it {i}is{/i} our wedding night."), 
    )


##################################
    # progress variable is linear
    @AppendToAllQuests
    class RomanceMarbella(LogicModule):
        def __init__(self):
            super().__init__()
            self.Kind = "love" # "dom", "gang", "love"
            # default/canon is love

            ### for dom, progress is 
            # 0 return in a few days 
            # 1 hunt the face
            # 2 return after face
            # 3 get disguise
            # 4 wait for disguise
            # 5 bring disguise to marbella
            # 6 meet marbella at market, at night
            # 7 check in after meeting at the market
            # 8 meet at pale dragon after dwarves walk in on you
            # 1000 over (as in, rep. content stage)

            ### for gang
            # 0 hunt the face, marbella works at their place
            # 1 return after face
            # 1000 "over" phase, rep content & supplies

            ### love route
            # 0 return to her for the post-quest date
            # 1 return t her after date
            # 2 return after the "walk" with library and arena
            # 3 talk to zanzibat about guard having been killed
            # 4 find and kill the face
            # 5 report face killed
            # 6 retuirn to marbella after face
            # 7 return to marbella after the post-face stuff (date or w/e)
            # 8 marbella stands by for the plan (for repeat) OR the plan is in prog
            # 9 return to marbella after traveling to mine
            # 10 fgind tailor for marbella
            # 11 met ma,rbella at tailor
            # 12 buy dress for marbella 
            # 13 wait for marbella dress 3 days
            # 14 pick up other shit
            # 15 bring all stuff (4 items) to marbella
            # 16 return at night for the wedding shit

            self.Dom_AfterGolemDelay = 2
            
            self.Shared_TheFaceRefusedHuntPromptTonight = False
            self.Shared_TheFaceFate = "dead" # dead, negotiated

            self.Dom_DisguisePrice = 750
            self.Dom_DisguiseDaysLeft = 3
            self.Dom_DisguiseRepeatFlag = False
            self.Dom_WillHaveSex = True # flip flops

            self.Gang_SuppliesDelay = 14   # "reset to this value"
            self.Gang_SuppliesDaysLeft = 0 # actual counter

            # cycles
            # 0 bj
            # 1 anal slave
            # 2 negotiation toy
            self.Gang_NextRepScene = 0 
            # flip flops
            self.Gang_MarbellaAtHideoutTonight = True 
            self.Gang_SeenMarbellaSceneTonight = False

            self.Love_KhazahChosenApproach = None # "kill", "device"
            # this true means player doesnt want sex scenes w/marbella thats it
            self.Love_IsPlato = False
            self.Love_TheFaceReward = 500
            self.Love_SeenTheFaceShyahMemo = False
            self.Love_DayToSkipToAfterDate = None 
            self.Love_DayToMeetAfterFaceDate = None 
            self.Love_DayToReturnAfterMine = None 
            self.Love_DayToMeetMarbellaAtGiselra = None 
            self.Love_DressPrice = 800
            self.Love_BesharRingDoRepeat = False
            self.Love_BesharDayToGetRing = None
            self.Love_TookTJ = False
            self.Love_WillHaveSex = True

        def onStart(self):
            self.Kind = QstBigTroubleLH().Kind
            if self.Kind == "dom":
                NoteUnlock("marbella_dom_cooldown")
            QstStart(PregMarbella)
            return

        def onMidnight(self):
            if self.Kind == "dom":
                if self.progress == 0:
                    if self.Dom_AfterGolemDelay > 0:
                        self.Dom_AfterGolemDelay -= 1
                elif self.progress == 4:
                    if self.Dom_DisguiseDaysLeft > 0:
                        self.Dom_DisguiseDaysLeft -= 1
                elif self.progress == 1000:
                    if self.Dom_WillHaveSex == False:
                        self.Dom_WillHaveSex = True

            elif self.Kind == "gang":
                if self.Gang_SuppliesDaysLeft > 0:
                    self.Gang_SuppliesDaysLeft -= 1
            
            elif self.Kind == "love":
                if self.progress == 1000:
                    if self.Love_WillHaveSex == False:
                        self.Love_WillHaveSex = True
            return
 
        def onNoon(self):
            if self.Kind == "dom":
                if self.progress == 1:
                    if self.Shared_TheFaceRefusedHuntPromptTonight == True:
                        self.Shared_TheFaceRefusedHuntPromptTonight = False
            elif self.Kind == "gang":
                if self.progress == 1000:
                    self.Gang_MarbellaAtHideoutTonight = not self.Gang_MarbellaAtHideoutTonight
                    self.Gang_SeenMarbellaSceneTonight = False

        def locationMod(self):
            btnMods = {}
            # dom locmods
            if self.Kind == "dom":
                if self.progress == 0:
                    if GetLocID() == "hamun_dist_docks":
                        if self.Dom_AfterGolemDelay > 0:
                            btnMods["hamun_docks_to_miningco"] = BtnJumpLabel(STR_LOC.HAMUN_MININGCO, "rom_marbella_dom_cooloff")
                if self.progress == 6:
                    if GetLocID() == "hamun_market":
                        if not IsDaytime():
                            btnMods["btn_hamun_market_marbella_dom_disguise"] = BtnJumpLabel(_("Talk to Marbella"), "rom_marbella_dom_market_meet")
            # love locmods
            elif self.Kind == "love":
                if self.progress in [3, 4, 5]:
                    if GetLocID() == "hamun_dist_merch_lord":
                        btnMods["hamun_dist_merch_lord_to_zanzibat_house"] = BtnJumpLabel(STR_LOC.HAMUN_ZANZIBAT_HOUSE, "qst_BigTroubleLHamun_zanzibat_doors")
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onEnter(self):
            if self.Kind == "dom":
                if self.progress == 0:
                    if IsDaytime():
                        if GetLocID() == "hamun_miningco":
                            return TriggeredEvent("rom_marbella_dom_return_after_golem")
                elif self.progress == 1:
                    if not IsDaytime():
                        if GetLocID() in ["hamun_dist_docks", "hamun_dist_merch_lord"]:
                            if self.Shared_TheFaceRefusedHuntPromptTonight == False:
                                if RngInt(1, 3) == 1:
                                    return TriggeredEvent("rom_marbella_shared_the_face")
                # return after dealing with face
                elif self.progress == 2:
                    if IsDaytime():
                        if GetLocID() == "hamun_miningco":
                            return TriggeredEvent("rom_marbella_dom_return_after_face")
                elif self.progress == 7:
                    if IsDaytime():
                        if GetLocID() == "hamun_miningco":
                            return TriggeredEvent("rom_marbella_dom_check_after_market")
                elif self.progress == 8:
                    if not IsDaytime():
                        if GetLocID() == "hamun_hookah_bar":
                            return TriggeredEvent("rom_marbella_dom_meet_at_pale_dragon")
            elif self.Kind == "gang":
                if self.progress == 0:
                    if not IsDaytime():
                        if GetLocID() in ["hamun_dist_docks", "hamun_dist_merch_lord"]:
                            if self.Shared_TheFaceRefusedHuntPromptTonight == False:
                                if RngInt(1, 3) == 1:
                                    return TriggeredEvent("rom_marbella_shared_the_face")
                elif self.progress == 1000:
                    if not IsDaytime():
                        if GetLocID() == "hamun_khazah_hideout":
                            if self.Gang_MarbellaAtHideoutTonight == True:
                                if self.Gang_SeenMarbellaSceneTonight == False:
                                    return TriggeredEvent("rom_marbella_gang_rep_scene_main")
            elif self.Kind == "love":
                if self.progress == 0:
                    if GetLocID() == "hamun_miningco":
                        if not IsDaytime():
                            return TriggeredEvent("rom_marbella_love_meet_date")
                if self.progress == 1:
                    if GetLocID() == "hamun_miningco":
                        if self.Love_DayToSkipToAfterDate <= GetGameDay():
                            if IsDaytime():
                                return TriggeredEvent("rom_marbella_love_return_after_date")
                if self.progress == 2:
                    if GetLocID() == "hamun_miningco":
                        if IsDaytime():
                            return TriggeredEvent("rom_marbella_love_return_after_walk")
                if self.progress == 3:
                    if GetLocID() == "hamun_zanzibat_house":
                        return TriggeredEvent("rom_marbella_love_come_to_zanzibat_after_guard_killed")
                if self.progress == 4:
                    if self.Love_SeenTheFaceShyahMemo == False:
                        if GetLocID() == "hamun_dist_merch_lord":
                            return TriggeredEvent("rom_marbella_love_theface_para_memo")
                    if not IsDaytime():
                        if GetLocID() in ["hamun_dist_docks", "hamun_dist_merch_lord"]:
                            if self.Shared_TheFaceRefusedHuntPromptTonight == False:
                                if RngInt(1, 3) == 1:
                                    return TriggeredEvent("rom_marbella_shared_the_face")
                if self.progress == 7:
                    if GetLocID() == "hamun_miningco":
                        if IsDaytime():
                            if self.Love_DayToMeetAfterFaceDate <= GetGameDay():
                                return TriggeredEvent("rom_marbella_love_return_for_theplan")
                if self.progress == 9:
                    if GetLocID() == "hamun_miningco":
                        if IsDaytime():
                            if self.Love_DayToReturnAfterMine <= GetGameDay():
                                return TriggeredEvent("rom_marbella_love_return_after_travel")
                if self.progress == 11:
                    if GetLocID() == "hamun_giselra_store":
                        if IsDaytime():
                            if self.Love_DayToMeetMarbellaAtGiselra <= GetGameDay():
                                return TriggeredEvent("rom_marbella_love_arrive_at_giselra")
                if self.progress == 13:
                    if GetLocID() == "hamun_giselra_store":
                        if IsDaytime():
                            if self.Love_DayToPickupDress <= GetGameDay():
                                return TriggeredEvent("rom_marbella_love_dress_ready")
                if self.progress == 16:
                    if GetLocID() == "hamun_hookah_bar_room":
                        if not IsDaytime():
                            return TriggeredEvent("rom_marbella_love_wedding")


        def extraDialogue(self):
            if self.Kind == "dom":
                if self.progress == 3:
                    if self.Dom_DisguiseRepeatFlag == True:
                        yield ("giselra_root", DNode(_("About that disguise I wanted..."), "rom_marbella_dom_get_disguise_menu", order = 100))
                    else:
                        yield ("giselra_root", DNode(_("I need you to make me a disguise..."), "rom_marbella_dom_get_disguise_dialogue", order = 100))
                elif self.progress == 4:
                    if self.Dom_DisguiseDaysLeft > 0:
                        yield ("giselra_root", DNode(_("About that disguise..."), "rom_marbella_dom_disguise_notready", order = 100))
                    else:
                        yield ("giselra_root", DNode(_("About that disguise..."), "rom_marbella_dom_disguise_ready", order = 100))
                elif self.progress == 5:
                    yield ("marbella_root", DNode(_("I have a gift for you..."), "rom_marbella_dom_disguise_return_to_marbella", order = 100))
                elif self.progress == 1000:
                    yield ("marbella_root", DNode(_("I was thinking we might have some fun..."), "rom_marbella_dom_rep_main", order = 99))
            elif self.Kind == "gang":
                if self.progress in [0, 1]:
                    yield ("hamun_khazah_leader_root", DNode(_("About that creature..."), "qst_BigTroubleLHamun_marbella_khazah_rivals_talk_about_face", order = 100))
                if self.progress == 1000:
                    yield ("hamun_khazah_leader_root", DNode(_("Do you have a supply package for me?"), "rom_marbella_gang_supplies", order = 100))
            elif self.Kind == "love":
                if self.progress in [4, 5]:
                    yield ("zanzibat_root", DNode(_("About that creature..."), "rom_marbella_love_zanzibat_aboutthatcreature", order = 100))
                if self.progress == 6:
                    yield ("marbella_root", DNode(_("A new guard should be here soon..."), "rom_marbella_love_return_after_face", order = 99))
                if self.progress == 8:
                    yield ("marbella_root", DNode(_("About that plan of yours..."), "rom_marbella_love_theplan_repeat", order = 99))
                if self.progress == 10:
                    if CharIsMet("giselra"):
                        yield ("marbella_root", DNode(_("I found a good tailor..."), "rom_marbella_love_found_tailor", order = 99))
                if self.progress == 12:
                    yield ("giselra_root", DNode(_("About that wedding dress..."), "rom_marbella_love_giselra_buydress_rep", order = 99))
                if self.progress == 13:
                    yield ("giselra_root", DNode(_("About that wedding dress..."), "rom_marbella_love_dress_notready", order = 99))
                if self.progress == 14:
                    if not PlayerHasItem("qst_marbella_flowers"):
                        yield ("katiya_root", DNode(_("Do you sell any flowers perhaps?"), "rom_marbella_love_katiya_flowers", order = 100))
                    if not PlayerHasItem("qst_marbella_ring"):
                        if self.Love_BesharDayToGetRing is None:
                            if self.Love_BesharRingDoRepeat:
                                yield ("beshar_root", DNode(_("About that ring..."), "rom_marbella_love_beshar_ring_order_repeat", order = 100))
                            else:
                                yield ("beshar_root", DNode(_("Could you forge me a simple ring?"), "rom_marbella_love_beshar_ring_order", order = 100))
                        else:
                            if self.Love_BesharDayToGetRing <= GetGameDay():
                                yield ("beshar_root", DNode(_("About that ring..."), "rom_marbella_love_beshar_ring_ready", order = 100))
                            else:
                                yield ("beshar_root", DNode(_("About that ring..."), "rom_marbella_love_beshar_ring_notready", order = 100))
                    if not PlayerHasItem("qst_wine_bottle"):
                        yield ("luna_root", DNode(_("Do you have any bottles of wine?"), "rom_marbella_love_luna_get_wine", order = 100))
                if self.progress == 15:
                    if PlayerHasItem("qst_marbella_wedding_ling") and PlayerHasItem("qst_marbella_flowers") and PlayerHasItem("qst_marbella_ring") and PlayerHasItem("qst_wine_bottle"):
                        yield ("marbella_root", DNode(_("I have something for you..."), "rom_marbella_love_bring_wedding_stuff", order = 99))
                if self.progress == 1000:
                    if not self.Love_IsPlato:
                        yield ("marbella_root", DNode(_("I've come to spend some time with my beloved, of course."), "rom_marbella_love_repeat_options", order = 99))

label rom_marbella_dom_cooloff:
    MC "(I should let Marbella cool off, come back another day.)"
    $ LocEnterQ()