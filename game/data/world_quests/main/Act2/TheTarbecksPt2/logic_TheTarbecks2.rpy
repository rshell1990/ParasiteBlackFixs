init python:
    @AppendToAllQuests
    class PrimerTheTarbecks2(LogicModule):
        def onEnter(self):  
            if GetLocID() in ["hamun_dist_docks", "hamun_dist_arena", "hamun_dist_merch_lord"]:
                if IsDaytime():
                    if QstDelayCheck(self):
                        return TriggeredEvent("qst_TheTarbecks2_PrimerInvite")

label qst_TheTarbecks2_PrimerInvite:
    show mc at cleft with easeinleft
    show cg_guard_hamun at cright_f with easeinright
    GUARD "Lady Tarbeck sends word that she wishes to speak to you at your earliest convenience."
    MC @talk "Tell Lady Tarbeck I shall attend when I can."
    show cg_guard_hamun at nod
    show cg_guard_hamun at blurin, cright
    hide cg_guard_hamun with easeoutright
    show mc at center with ease
    $ QstStart(QstTheTarbecks2)
    MC @serious "(Lady Tarbeck seems quite pious.)"
    MC @talk "(Something tells me this won't be the easiest task...)"
    SHYAHTAN "(During my conquests, we too found mates such as these.)"
    MC @think "(And what did you do?)"
    SHYAHTAN "({i}Gave them something else to worship.{/i})"
    MC @smile "(Somehow, I'm not sure telling her to worship my cock is going to cut it.)"
    SHYAHTAN "(Faith and piety can quickly be displaced.)"
    SHYAHTAN "(Go slow... Let her own feelings do most of the work.)"
    SHYAHTAN "(Then simply offer her the words she needs to hear to twist her faith.)"
    MC @think "(... You don't talk like you used to anymore.)"
    SHYAHTAN "(My memories return slowly.)"
    SHYAHTAN "(Now go... Claim us another mate for the hive.)"
    $ LocEnter()

init python:
    @AppendToAllQuests
    class QstTheTarbecks2(BaseQuest):
        TITLE = _("The Tarbecks, part II")
        DESCRIPTION = _("As per Lord Tarbeck's request, I must help make his resentful, pious wife more 'interesting' if I want his support to allow the deal to pass with Garen and the Greater Trading Company.")
        GOALS = {
            0: QuestStage(_("Meet Lady Tarbeck at the Tarbeck manor"),
                hintTxt = _("A guard has approached me asking me to meet with Lady Tarbeck... I should see what she wants."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall"
            ),
            1: QuestStage(_("Follow Lady Tarbeck"),
                hintTxt = _("Lady Tarbeck had agreed to walk with me. That's a start.")
            ),
            2: QuestStage(_("Return to Tarbeck Manor after dark"),
                hintTxt = _("After escorting Lady Tarbeck around Hamun, it seems an opportunity has arisen by which the two of us can strike up a deal... I should head back to the manor and speak to her when I can."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            3: QuestStage(_("Take Lady Tarbeck around the city"),
                hintTxt = _("Lady Tarbeck and I have struck a deal, I will help her win over Lady Belamore and the others, and in return, she will persuade her husband to give me what I want... As part of that deal, she has agreed to spend time privately with me. I should speak to her when I am ready to take her on our first 'date.', daytime."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            4: QuestStage(_("Wait for Lady Tarbeck's call"),
                hintTxt = _("Lady Tarbeck will call on me to attend another tea party in the coming days... I should wait until then.")
            ),
            5: QuestStage(_("Meet Lady Tarbeck at the castle in Hamun"),
                hintTxt = _("Lady Tarbeck has summoned me to join her for another tea party with Lady Belamore... I should head there to meet her once I'm ready."),
                trackTag = "hamun_dist_merch_lord_to_castle",
            ),
            6: QuestStage(_("Meet Lady Tarbeck at the Pale Dragon in a couple days"),
                hintTxt = _("After saving her from being kidnapped and uncovering she is a dark mage by birth, I have told Lady Tarbeck to meet me at the Pale Dragon when she is ready to get to know her further."),
                trackTag = "hamun_docks_to_hookah_bar",
            ),
            7: QuestStage(_("Return to the Tarbeck Manor after dark"),
                hintTxt = _("It's time to keep my end of the deal, I must return to the Tarbeck Manor this evening to 'entertain' Lady Belamore and her friends... Once the deal is secured, Lord Tarbeck should step aside from blocking the GTC."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            8: QuestStage(_("Wait for Lady Tarbeck to make contact"),
                hintTxt = _("Lady Tarbeck has asked me to wait till I hear back from her... I hope nothing goes wrong in the meanwhile."),
            ),
            9: QuestStage(_("Speak to Lady Tarbeck at the Tarbeck manor"),
                hintTxt = _("Lord Tarbeck has been kidnapped! I must hurry to the Tarbeck manor to speak to Lady Tarbeck at once!"),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            10: QuestStage(_("Speak to Lady Tarbeck at the Pale Dragon"),
                hintTxt = _("I should head to the Pale Dragon... Lady Tarbeck will meet me there."), 
                trackTag = "hamun_docks_to_hookah_bar",
            ),
            11: QuestStage(_("Shyahtan wants me to wait once more"),
                hintTxt = _("Those treacherous whores have betrayed myself and Lady Tarbeck... But the voice inside of me wants me to simply wait for something to happen?"),
            ),
            12: QuestStage(_("Return to the Tarbeck Manor"),
                hintTxt = _("I have recieved an urgent message to come back to the Tarbeck Manor... Shyahtan seems convinced something has happened, but what?"),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            13: QuestStage(_("Wait for word from Lady Tarbeck at The Pale Dragon"),
                hintTxt = _("Lady Belamore and her co-conspirators will need a few days to feel the affects fully... I should wait at The Pale Dragon until Lady Tarbeck summons me."),
                trackTag = "hamun_docks_to_hookah_bar",
            ),
            14: QuestStage(_("Return to the Tarbeck manor"),
                hintTxt = _("I have been summoned back to the Tarbeck manor... One of the ladies must be beginning to crack."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            15: QuestStage(_("Meet Lord Belamore at the castle in Hamun"),
                hintTxt = _("Lady Tarbeck wants me to apply some 'pressure.' She has asked me to meet Lord Belamore at the castle in the morning... I'm sure Lady Belamore will be impressed."),
                trackTag = "hamun_dist_merch_lord_to_castle",
            ),
            16: QuestStage(_("Head back to the Tarbeck manor after dark"),
                hintTxt = _("Lady Belamore is furious... I should head back to the Tarbeck manor this evening to see what happens."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            17: QuestStage(_("Meet Lady Tarbeck's spy on the outskirts of Hamun"),
                hintTxt = _("Lady Tarbeck has asked me to meet one of her spies outside the city walls of Hamun tonight... I should tread carefully."),
            ),
            18: QuestStage(_("Report back in the morning to Lady Tarbeck that her spy is dead"),
                hintTxt = _("I was too late. Lady Belamore's assassins had already killed the spy... I'll let Lady Tarbeck know in the morning."),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            19: QuestStage(_("Drown your sorrows at The Pale Dragon"),
                hintTxt = _("How much longer is this misery going to last? I need a drink..."),
                trackTag = "hamun_docks_to_hookah_bar",
            ),
            20: QuestStage(_("Speak to lady Belamore and the others at the castle"),
                hintTxt = _("I can only hope lady Bargore and lady Narisha and bought some sense to lady Belamore... I should head to the castle today and see if I can fix this mess."),
                trackTag = "hamun_dist_merch_lord_to_castle",
            ),
            21: QuestStage(_("Wait for now..."),
                hintTxt = _("The only thing left to do now is wait until I hear from Lady Tarbeck or someone."),
            ),
            22: QuestStage(_("Return to the Tarbeck Manor"),
                hintTxt = _("Lady Belamore and the others have called for truce talks... I must hurry to Lady Tarbeck's side at once!"),
                trackTag = "hamun_dist_merch_lord_to_tarbeck_mainhall",
            ),
            23: QuestStage(_("Rescue Lord Tarbeck from the Hamun sewers"),
                hintTxt = _("Lady Belamore has revealed Lord Tarbeck is being held in the sewers! I must rescue him before it's too late!"),
                trackTag = "btn_hamun_dist_merch_lord_to_sewers",
            ),
            24: QuestStage(_("Report back to Garen Quiltshire of your success at The Pale Dragon"),
                hintTxt = _("Garen will be pleased... He's probably waiting at The Pale Dragon for me to deliver the news."),
                trackTag = "hamun_docks_to_hookah_bar",
            ),
        }

        def __init__(self):
            super().__init__()

            self.IsMain = True
            self.XpReward = 850
            self.suggestedLevel = 13 
#################################################################
            self.Stage2OfferRepeat = False
            self.Stage2OfferLittleMorePicked = False
            self.Entertain_ToldAboutVes = False
            self.KidnappedTrustParasite = True

        def onEnter(self):
            if self.progress == 4:
                if GetLocID() in ["hamun_dist_docks", "hamun_dist_arena", "hamun_dist_merch_lord"]:
                    if IsDaytime():
                        if QstDelayCheck(self):
                            if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                                return TriggeredEvent("qst_TheTarbecks2_tea_invite")
            elif self.progress == 6:
                if GetLocID() == "hamun_hookah_bar":
                    if QstDelayCheck(self):
                        if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                            return TriggeredEvent("qst_TheTarbecks2_meet_at_pale_dragon")
            elif self.progress == 7:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    if not IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks2_entertain")
            elif self.progress == 8:
                if GetLocID() in ["hamun_dist_docks", "hamun_dist_arena", "hamun_dist_merch_lord"]:
                    if IsDaytime():
                        if QstDelayCheck(self):
                            if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                                return TriggeredEvent("qst_TheTarbecks2_lord_tarbeck_kidnapped")
            elif self.progress == 9:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    return TriggeredEvent("qst_TheTarbecks2_kidnapped_arrive_mansion")
            elif self.progress == 11:
                if GetLocID() in ["hamun_dist_docks", "hamun_dist_arena", "hamun_dist_merch_lord"]:
                    if IsDaytime():
                        if QstDelayCheck(self):
                            if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                                if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                                    return TriggeredEvent("qst_TheTarbecks2_summoned_again")
            elif self.progress == 12:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    return TriggeredEvent("qst_TheTarbecks2_summoned_mansion")
            elif self.progress == 13:
                if GetLocID() == "hamun_hookah_bar":
                    if IsDaytime():
                        if QstDelayCheck(self):
                            if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                                return TriggeredEvent("qst_TheTarbecks2_paledragon_after_waiting")
            elif self.progress == 14:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    return TriggeredEvent("qst_TheTarbecks2_return_to_manor_after_waiting")
            elif self.progress == 15:
                if GetLocID() == "hamun_castle_entrance":
                    if IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks2_meetlord")
            elif self.progress == 16:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    if not IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks2_return_to_manor_once_more")
            elif self.progress == 18:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    if IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks2_return_to_manor_after_spy")
            elif self.progress == 20:
                if GetLocID() == "hamun_castle_tea_room":
                    if IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks2_tearoom_after_drunk")
            elif self.progress == 21:
                if GetLocID() in ["hamun_dist_docks", "hamun_dist_arena", "hamun_dist_merch_lord"]:
                    if IsDaytime():
                        if QstDelayCheck(self):
                            if IsInTimeFrame(TIME_MORNING, TIME_DAY_END):
                                return TriggeredEvent("qst_TheTarbecks2_guard_approach_again")
            elif self.progress == 22:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    if IsDaytime():
                        return TriggeredEvent("qst_TheTarbecks2_return_to_manor_once_more_once_more")


        def locationMod(self):
            btnMods = {}
            if self.progress == 0:
                if GetLocID() == "hamun_dist_merch_lord":
                    btnMods["hamun_dist_merch_lord_to_tarbeck_mainhall"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ESTATE, "qst_TheTarbecks2_enter_manor")
            elif self.progress == 2:
                if self.Stage2OfferRepeat == False:
                    if GetLocID() == "hamun_dist_merch_lord":
                        if IsDaytime() == False:
                            btnMods["hamun_dist_merch_lord_to_tarbeck_mainhall"] = BtnJumpLabel(STR_LOC.HAMUN_TARBECK_ESTATE, "qst_TheTarbecks2_return_to_manor")
                else:
                    if GetLocID() == "hamun_tarbeck_mainhall":
                        btnMods["btn_hamun_tarbeck_mainhall_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "qst_TheTarbecks2_offer_repeat")
            elif self.progress == 3:
                if GetLocID() == "hamun_tarbeck_mainhall":
                    if IsDaytime():
                        btnMods["btn_hamun_tarbeck_mainhall_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "qst_TheTarbecks2_prep_to_tour")
            elif self.progress == 5:
                if GetLocID() == "hamun_castle_entrance":
                    if IsDaytime():
                        btnMods["btn_hamun_castle_entrance_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "qst_TheTarbecks2_tea_party2")

            elif self.progress == 10:
                if GetLocID() == "hamun_hookah_bar":
                    if IsDaytime():
                        btnMods["btn_hamun_hookah_bar_lady_tarbeck"] = BtnJumpLabel(_("Talk to Lady Tarbeck"), "qst_TheTarbecks2_paledragon_kidnapgo")
            elif self.progress == 17:
                if GetLocID() == "hamun_gates":
                    if not IsDaytime():
                        btnMods["btn_hamun_gates_spy"] = BtnJumpLabel(_("Talk to the spy"), "qst_TheTarbecks2_talkspy")
            elif self.progress == 19:
                if GetLocID() == "hamun_hookah_bar":
                    btnMods["btn_hamun_hookah_bar_drown_sorrows"] = BtnJumpLabel(_("Drown your sorrows"), "qst_TheTarbecks2_drown_sorrows")
            elif self.progress == 23:
                if GetLocID() == "hamun_dist_merch_lord":
                    btnMods["btn_hamun_dist_merch_lord_to_sewers"] = BtnJumpLabel(_("Enter the sewers"), "qst_TheTarbecks2_to_sewers")
            elif self.progress == 24:
                if GetLocID() == "hamun_hookah_bar":
                    if IsDaytime():
                        btnMods["btn_hamun_hookah_bar_garen"] = BtnJumpLabel(_("Enter the sewers"), "qst_TheTarbecks2_garen_at_bar")                        
            return LocButtonMod(directMods = btnMods, priority = 1)

        def onStart(self):
            QstStart(PregHamunTrio)
            QstComplete(PrimerTheTarbecks2)
            return

        def onComplete(self):
            # for autocomplete
            QstSetProgress(HouseLockTarbeckHouse, 2)
            QstStart(HouseLockHamunCastle)
            QstStart(RomanceLadyTarbeck)
            return
