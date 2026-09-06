init python:
    @AppendToAllQuests
    class QstGuildCaravan(BaseQuest):
        GOALS = {
            0: QuestStage(_("Protect the caravan"), hintTxt = _("We have to protect the caravan from any... troublemakers we might encounter on the way to Hamun.")),
            1: QuestStage(_("Protect the caravan!"), hintTxt = _("As expected, we walked straight into an ambush. To arms!")),
            2: QuestStage(_("Collect your reward"), hintTxt = _("With bandits defeated, it's time to collect my reward.")),
            }
        TITLE = _("Caravan Protection")
        DESCRIPTION = _("A group of traders on their way to Free City of Hamun are willing to pay generously for some protection...")
        PRE_START_STRINGS_LIST = [
            _("Ruffians are known to roam the roads to the City of Hamun."),
            _("This one looks like a long, dangerous trip.")]
        LABEL = "nov_adv_guild_board_qst_caravan_starter"
        ICONS = ["clock", "swords"]

        def __init__(self):
            super().__init__()

            self.XpReward = 300
            self.appears_on_board = True
            self.times_completed = 0
            self.reappear_day = -1
            self.suggestedLevel = 4

        def onComplete(self):
            PlayerAddItem("gold", 150)
            self.XpReward = 0 # grant xp only once
            self.times_completed += 1
            self.appears_on_board = False
            self.reappear_day = GetGameDay() + 2
            QstGuildBehemoth().TryUnlock()
            return

init 1 python:
    adv_guild_quests.append(QstGuildCaravan)

label nov_adv_guild_board_qst_caravan_starter:
    if QstIsActive(QstTheComingStorm):
        MC "(I can't leave the city due to the lockdown.)"
        MC "(That task will have to wait until later...)"
        $ LocEnter()
    else:
        $ QstStart(QstGuildCaravan)
        jump qst_guild_caravan