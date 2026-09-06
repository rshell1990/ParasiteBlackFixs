init python:
    @AppendToAllQuests
    class QstTheJackpot(BaseQuest):
        GOALS = {
            0: QuestStage(_("Check up on Mr. Winward in the Iron Unicorn, at night"), trackTag = "btn_novaras_tavern", hintTxt = _("I've gotta check Iron Unicorn. I am likely to find Mr. Winward there.")),

            # this stage can fail
            10: QuestStage(_("Win at Barati"), hintTxt = _("Mr. Winward is a gambler, playing Barati with some dangerous peole. I have decided to intervene on his behalf.")),

            # if 10 fails OR if player "lets him lose"
            20: QuestStage(_("Follow Mr. Winward"), hintTxt = _("Mr. Winward's game of Barati is over. Time to hunt the hunters.")),
            30: QuestStage(_("Settle Mr. Winward's debt"), hintTxt = _("Mr. Winward's in trouble. I must find a way to help him out.")),

            40: QuestStage(_("Return to tanner's store"), trackTag = "btn_tanner_shop", hintTxt = _("I have dealt with Mr. Winward's situation. Time to report back to Mrs. Winward.")),

            # get cowhide
            50: QuestStage(_("Get cowhide for Mrs. Winward"), trackTag = "btn_novaras_market_stalls", hintTxt = _("Mrs. Winward asked me to procure a cowhide for her. I can buy one off a butcher, down at the city market.")),
            60: QuestStage(_("Bring cowhide to Mrs. Winward"), trackTag = "btn_tanner_shop", hintTxt = _("Time to head back to tanner's workshop.")),

            70: QuestStage(_("Meet Mr. Winward at Black Diamond, night time"), trackTag = "novaras_diamond", hintTxt = _("Mr. Winward wants me to meet him at the Black Diamond, in the Pleasure district. The big game is likely up...")),
            80: QuestStage(_("Figure out your next step"), trackTag = "novaras_diamond", hintTxt = _("The big game is on. I wonder if we will be able to walk away alive, let alone win the game...")),

            85: QuestStage(_("Let 'Crystal Eyes' win"), trackTag = "novaras_diamond", hintTxt = _("The big game is on. I have found a way to keep Mr. Winward from losing big - another player will play in his stead, while he will be... distracted by the Black Diamond staff.")),

            # this can fail
            90: QuestStage(_("Win the big game"), trackTag = "novaras_diamond", hintTxt = _("The big game is on. I wonder if we will be able to walk away alive, let alone win the game...")),

            100: QuestStage(_("Return to tanner's shop"), trackTag = "btn_tanner_shop", hintTxt = _("The big game is over. Time to head to the tanner's store.")),

            # only if won
            110: QuestStage(_("Check up on Mrs. Winward tomorrow"), trackTag = "btn_tanner_shop", hintTxt = _("I should return to the tanner's store later.")),

            # only if killed
            120: QuestStage(_("Check up on Mrs. Winward in a few days"), trackTag = "btn_tanner_shop", hintTxt = _("I should return to the tanner's store later."))
        }

        SIMPLE_GOALS = False
        TITLE = _("The Jackpot")
        DESCRIPTION = _("Mrs. Winward asked me to investigate her husband's late night activities.")

        def __init__(self):
            super().__init__()

            self.XpReward = 300
            # prog:
            # 0:: unicorn barati 
            # 1:: return to tanner
            # 2:: get cowhide
            # 3:: return with cowhide
            # 4:: go to black diamond
            # 5:: we're at BD and we have talked to winward
            # 6:: we're at BD and we're on the vulshan help route
            # 70:: return to tanner shop

            self.WonBDWithVulshanHelp = False
            self.WonBDSolo = False
            self.LostBDSolo = False

            self.VulshanRouteSeenVIPScene = False
            self.VulshanRouteSeenCheckupScene = False

            self.MrWinwardDead = False

            self.Outcome = None # "control" "invest" "pimp" "divorce" "murder"

            self.suggestedLevel = 4


        def onStart(self):
            GoalShow(self, 0)

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tavern":
                if IsInTimeFrame(TIME_DAY_END, TIME_LATENIGHT):
                    if self.progress == 0:
                        btnMods["btn_mr_winward_gambling"] = BtnJumpLabel(_("Talk to Mr. Winward"), "qst_jackpot_unicorn_barati")
            
            elif GetLocID() == "novaras_black_diamond":
                if self.progress == 4:
                    btnMods["btn_jackpot_winward"] = BtnJumpLabel(_("Talk to Mr. Winward"), "qst_jackpot_black_diamond_winward")
                elif self.progress == 5:  
                    btnMods["btn_jackpot_winward"] = BtnJumpLabel(_("Talk to Mr. Winward"), "qst_jackpot_black_diamond_winward_2")
                    if QstDamzelInDiztrezz().PlayerSidedWithVulshan:
                        btnMods["btn_jackpot_vulshan_guard"] = BtnJumpLabel(_("Talk to the guard"), "qst_jackpot_black_diamond_vulshan_distraction")
                elif self.progress == 6:
                    if not self.VulshanRouteSeenVIPScene:
                        btnMods["btn_jackpot_vulshan_vip"] = BtnJumpLabel(_("Visit the VIP lounge"), "qst_jackpot_black_diamond_vip_scene")
                    if not self.VulshanRouteSeenCheckupScene:
                        btnMods["btn_jackpot_vulshan_checkup"] = BtnJumpLabel(_("Check up on Mr. Winward"), "qst_jackpot_black_diamond_vulshan_checkup")
                    btnMods["btn_jackpot_vulshan_couch"] = BtnJumpLabel(_("Relax on the couches"), "qst_jackpot_black_diamond_vulshan_couch")
            
            elif GetLocID() == "novaras_dist_house":
                if self.progress == 110 or self.progress == 120:  
                    if self.delayCheck() == False:
                        btnMods["btn_tanner_shop"] = BtnJumpLabel(tra(STR_LOC.NOV_TANNER_SHOP), "qst_jackpot_wait_for_another_day")

            return LocButtonMod(directMods = btnMods, priority = 1)

        def onEnter(self):  
            if GetLocID() == "novaras_tanner_shop":
                if self.progress == 1:
                    GoalComplete(QstTheJackpot, 40)
                    return TriggeredEvent("qst_jackpot_return_from_unicorn")
                elif self.progress == 70:
                    return TriggeredEvent("qst_jackpot_return_from_bd")
                elif self.progress == 110:
                    if self.delayCheck():
                        return TriggeredEvent("qst_jackpot_won_outcome_2")
                elif self.progress == 120:
                    if self.delayCheck():
                        return TriggeredEvent("qst_jackpot_outcome_murder_2")

        def extraDialogue(self):
            if self.progress == 3:
                if PlayerItemQty("cow_hide") > 0:
                    yield ("mrs_winward_root", DNode(_("Here's a cowhide you wanted."), "qst_jackpot_return_with_cowh", order = 666))

        def onComplete(self):
            # save compat
            if not CharIsAlive("mr_winward"):
                CharAddRelEntry("mr_winward", "killed_by_mc_jackpot")

        def onItemAcquired(self, ItemID, Amt):
            if self.progress == 2:
                if ItemID == "cow_hide":
                    QstSetProgress(QstTheJackpot, 3)
                    GoalComplete(QstTheJackpot, 50)
                    GoalShow(QstTheJackpot, 60)


label qst_jackpot_wait_for_another_day:
    MC "(I don't think it's time for me to go in there.)"
    $ LocEnterQ()