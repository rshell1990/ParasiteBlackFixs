init python:
    @AppendToAllQuests
    class QstGuildDarkMage(BaseQuest):
        GOALS = {
            0: QuestStage(_("Investigate the kidnappings"), hintTxt = _("According to the evidence, the kidnappers' hideout should be somewhere in the slums.")),
            1: QuestStage(_("Muster your intellect"),  hintTxt = _("Riddles? Oh gods, no...")),
            2: QuestStage(_("Defeat the abomination"), hintTxt = _("A dark mage was using kidnapped victims' bodies for... construction purposes. Purge the unclean!")),
            3: QuestStage(_("Return for your reward"), hintTxt = _("Another monster and his pet gone, time to collect our reward.")),
            }
        TITLE = _("Dark Mage")
        DESCRIPTION = _("Alarming rumors have circulated about a dark mage kidnapping people for some nefarious experiment...")
        PRE_START_STRINGS_LIST = [_("This one might be dangerous.")]
        LABEL = "nov_adv_guild_board_qst_darkmage_starter"
        ICONS = ["swords"]

        def __init__(self):
            super().__init__()

            self.XpReward = 500
            self.appears_on_board = True
            self.times_completed = 0
            self.reappear_day = -1

            self.riddles_label_list = [ # original labels list do not tamper with
                "qst_guild_darkmage_riddle_0",
                "qst_guild_darkmage_riddle_1",
                "qst_guild_darkmage_riddle_2",
                "qst_guild_darkmage_riddle_3",
                "qst_guild_darkmage_riddle_4",
                "qst_guild_darkmage_riddle_5",
                "qst_guild_darkmage_riddle_6",
                "qst_guild_darkmage_riddle_7",
                "qst_guild_darkmage_riddle_8",
                "qst_guild_darkmage_riddle_9",
                "qst_guild_darkmage_riddle_10",
                "qst_guild_darkmage_riddle_11",
            ]
            self.active_riddles_list = []
            self.correct_answers = 0
            self.suggestedLevel = 6

        def onStart(self):
            self.correct_answers = 0
            self.active_riddles_list = self.riddles_label_list.copy()
            renpy.random.shuffle(self.active_riddles_list)

        def onComplete(self):
            PlayerAddItem("gold", 150)
            self.XpReward = 0 # grant xp only once
            self.times_completed += 1
            self.appears_on_board = False
            self.reappear_day = GetGameDay() + 2
            QstGuildBehemoth().TryUnlock()

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_darkmage_room":
                btnMods["btn_darkmage_shelf"] = BtnJumpLabel(_("Move aside"), "qst_guild_darkmage_shelf_click")
            return LocButtonMod(directMods=btnMods)

init 1 python:
    adv_guild_quests.append(QstGuildDarkMage)

label nov_adv_guild_board_qst_darkmage_starter:
    $ QstStart(QstGuildDarkMage)
    jump qst_guild_darkmage
