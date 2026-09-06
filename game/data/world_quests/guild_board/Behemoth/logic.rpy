init python:
    @AppendToAllQuests
    class QstGuildBehemoth(BaseQuest):
        GOALS = {
            0: QuestStage(_("Find the mother rat"), hintTxt = _("I have signed up to take down the creature responsible for the vermin threat. It should be somewhere in the sewers, down below.")),
            1: QuestStage(_("Defeat the abomination!"), hintTxt = _("No turning back now... Take it out!")),
            2: QuestStage(_("Claim your reward"), hintTxt = _("The abomination is dealt with. Now, to take our spoils.")),
            }
        TITLE = _("The Behemoth Below")
        DESCRIPTION = _("A gigantic white rat seems to be mass-breeding and even coordinating the vermin below our very streets!")
        PRE_START_STRINGS_LIST = [_("Sounds like a dangerous one."), _("However, dealing with this contract will impress the guild for sure.")]
        LABEL = "nov_adv_guild_board_qst_behemoth_starter"
        ICONS = ["swords"]

        def __init__(self):
            super().__init__()

            self.XpReward = 850
            self.appears_on_board = False # unlocked by doing all the other quests once
            self.suggestedLevel = 8

        def TryUnlock(self):
            for quest in [QstGuildCaravan, QstGuildDarkMage, QstGuildRodents, QstGuildPriceLife]:
                if quest().times_completed == 0:
                    return
            if not self.isComplete:
                self.appears_on_board = True

        def onComplete(self):
            ### achievement
            if can_unlock_achievement("MAKING_A_NAME_FOR_YOURSELF"):
                unlock_achievement("MAKING_A_NAME_FOR_YOURSELF")

            PlayerAddItem("gold", 750)
            self.XpReward = 0 # grant xp only once
            self.appears_on_board = False
            NovarasAdvBoard().player_tier = 1
            QstStart(RomanceThea)
            return

init 1 python:
    adv_guild_quests.append(QstGuildBehemoth)

label nov_adv_guild_board_qst_behemoth_starter:
    $ QstStart(QstGuildBehemoth)
    jump qst_guild_behemoth