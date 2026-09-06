
# functions listed here you can consider manual OR to be used via gui,
# SOMETIMES they'll be used by gui or code
init python:
    def DEBUG_CompleteAllRealQuests():
        for Quest in GetAllGameQuests():
            QstStart(Quest)
            QstComplete(Quest) 
    def DEBUG_SetAllStatsTo(Value = 10):
        for CharID in ["mc", "markus", "kiara", "myu", "elena", "jana", "ves"]:
            for StatID in ["Strength", "Agility", "Dexterity", "Willpower", "Endurance", "Luck", "Charisma", "Barter"]:
                worldChars[CharID][StatID] = Value
        return
    def DEBUG_AddAllPerks():
        for PerkID in Lib_Perks:
            PlayerAddPerk(PerkID, Soft = True)
        return