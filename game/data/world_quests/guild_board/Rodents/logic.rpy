init python:
    @AppendToAllQuests
    class QstGuildRodents(BaseQuest):
        GOALS = {
            0: QuestStage(_("Investigate the sewers"), hintTxt = _("It's time to delve into the sewers, see how the local fauna is doing.")),
            1: QuestStage(_("Defeat the swarm"), hintTxt = _("The 'alarming reports' were indeed true — the place is crawling with oversized rats. Weapons free!")),
            2: QuestStage(_("Collect your reward"), hintTxt = _("Deratification complete. Time to collect our reward."))
            }
        TITLE = _("Rodents of unusual size")
        DESCRIPTION = _("There have been alarming reports about aggressive rats the size of dogs emerging out of the sewers at night and stealing whole barrels of food.")
        PRE_START_STRINGS_LIST = [_("Huge rats, huh?"), _("Sounds like I'll have to fight them out of the city's sewers.")]
        LABEL = "nov_adv_guild_board_qst_rodents_starter"
        ICONS = ["swords"]

        def __init__(self):
            super().__init__()

            self.XpReward = 300
            self.appears_on_board = True
            self.times_completed = 0
            self.reappear_day = -1
            self.suggestedLevel = 7
        
        def onComplete(self):
            PlayerAddItem("gold", 150)
            self.XpReward = 0 # grant xp only once
            self.times_completed += 1
            self.appears_on_board = False
            self.reappear_day = GetGameDay() + 2
            QstGuildBehemoth().TryUnlock()

init 1 python:
    adv_guild_quests.append(QstGuildRodents)

label nov_adv_guild_board_qst_rodents_starter:
    $ QstStart(QstGuildRodents)
    jump qst_guild_rodents