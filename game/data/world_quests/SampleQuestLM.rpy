init python:
    # uncomment this to make it appear
    #@AppendToAllQuests
    # inherit from LogicModuel to make it initially hidden and not tracked
    class DEV_SampleQuestOrLogicModule(BaseQuest):
        TITLE = _("<sample quest/lm>")
        DESCRIPTION = _("<sample quest/lm description>")
        GOALS = {
            0: QuestStage(_("(dev) sample quest goal title"),   trackTag = "some_btn_id", hintTxt = _("sample description")),
            1: QuestStage(_("(dev) sample quest goal 2 title"), trackTag = "some_btn_id", hintTxt = _("sample description 2")),
        }

        # if this is true, goals need to be manually set/hidden/completed
        # setting this to true makes functions such as GoalShow, GoalComplete
        # or checks such as IsGoalVisible relevant
        # SIMPLE_GOALS = True
############
        # alter behaviour of location buttons
        def locationMod(self):
            # a dict of buttonID, buttonbehaviour
            btnMods = {}
            # example altering the behaviour of an existing button:
            # btnMods["btn_talk_adara"] = BtnJumpLabel(_("Talk to Adara"), "adara_talk")
            return LocButtonMod(directMods = btnMods)
############
        # add extra dialogue to characters
        def extraDialogue(self):
            # note theres no return, you just yield arbitrary amount of DNodes.
            # note there can be logic going on in here
            # yield ("adara_root", DNode(_("I have to go."), "adara_bye", nextNode = "DNodeExit", order = -100))
            pass
############
        # triggered when you enter or re-enter *any* location with LocEnter (or main recheck)
        def onEnter(self):  
            return
        # triggered only when you actually enter a location: it will not fire on *re-entering the same location*
        def onEnterOnce(self):
            return
############
        # alter data every day at 12:00
        def onNoon(self):
            return

        # alter data every day at 00:00
        def onMidnight(self):
            return
############
        # alter data on quest start
        def onStart(self):
            return
        # alter data on quest end and complete
        def onComplete(self):
            return
        # alter data on quest end and failed
        def onFail(self):
            return
        # alter data when the quest is over, regardless of outcome
        def onOver(self):
            return
############
        # alter data on altering quest progress
        def onSetProgress(self):
            return

        # experimental, called any time an item is added to player inv
        def onItemAcquired(self, ItemID, Amount):
            return
        # same as above, but for losing an item
        def onItemLost(self, ItemID, Amount):
            return
############
        # allows active logic module to override a location's music/ambience track
        # doesnt have any priority mechanism or whatnot, 
        # just injects another tune in place of existing 
        # parses strictly by path only
        def OverrideAmbienceOrMusicTrack(self):
            Result = {}
            # replace PathX with PathY
            # Result[PathX] = PathY
            return Result
############
        # allows active logic module to override a location bg (or locations plural)
        # no priorities, just injects arbitrary amt of override image tags for locs
        def OverrideLocBg(self):
            Result = {}
            # if somevar:
            #     Result["some_loc_id"] = "some_new_bg"
            #     Result["some_other_loc_id"] = "some_new_bg_2"
            return Result
############