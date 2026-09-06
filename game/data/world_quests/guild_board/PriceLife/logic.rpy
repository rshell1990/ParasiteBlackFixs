init python:
    @AppendToAllQuests
    class QstGuildPriceLife(BaseQuest):
        GOALS = {
            0: QuestStage(_("Meet with the kidnappers"), hintTxt = _("I should meet with whoever kidnapped the merchant's child.")),
            1: QuestStage(_("Rescue the merchant's child"), hintTxt = _("Seems like the merchant's child is being held captive by a group of bandits. I have to... deal with them one way or another.")),
            2: QuestStage(_("Return to Novaras"), hintTxt = _("With the merchant's child relatively safe in my company, I should return to claim my reward.")),
            }
        TITLE = _("Price for life")
        DESCRIPTION = _("A Merchants daughter has been kidnapped by marauders who are now demanding a hefty ransom price.")
        PRE_START_STRINGS_LIST = [
            _("Whoever takes this one must bring back the merchant's child by any means necessary...")]
        LABEL = "nov_adv_guild_board_qst_pricelife_starter"
        ICONS = ["swords", "clock"]

        def __init__(self):
            super().__init__()

            self.XpReward = 400
            self.appears_on_board = True
            self.times_completed = 0
            self.reappear_day = -1
            self.sex_scene = False
            self.variant = "daughter" # swaps to "son" and back
            self.suggestedLevel = 4

        def onStart(self):
            PlayerAddItem("qst_ransom_money")

        def onComplete(self):
            PlayerAddItem("gold", 350)
            if PlayerItemQty("qst_ransom_money") > 0:
                PlayerRemItem("qst_ransom_money")
                PlayerAddItem("gold", 500)
            self.XpReward = 0 # grant xp only once
            self.times_completed += 1
            self.appears_on_board = False
            self.reappear_day = GetGameDay() + 2
            if self.variant == "daughter":
                self.variant = "son"
                QstGuildPriceLife.DESCRIPTION = _("A Merchants son has been kidnapped by marauders who are now demanding a hefty ransom price.")
            else:
                self.variant = "daughter"
                QstGuildPriceLife.DESCRIPTION = _("A Merchants daughter has been kidnapped by marauders who are now demanding a hefty ransom price.")
            self.sex_scene = False
            QstGuildBehemoth().TryUnlock()

init 1 python:
    adv_guild_quests.append(QstGuildPriceLife)

label nov_adv_guild_board_qst_pricelife_starter:
    if QstIsActive(QstTheComingStorm):
        MC "(I can't leave the city due to the lockdown.)"
        MC "(That task will have to wait until later...)"
        $ LocEnter()
    else:
        $ QstStart(QstGuildPriceLife)
        if QstGuildPriceLife().variant == "daughter":
            jump qst_guild_price_life_daughter_start
        if QstGuildPriceLife().variant == "son":
            jump qst_guild_price_life_son_start