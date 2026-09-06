init -2 python:
    def PlayerHasPerk(Perk_ID):
        return Perk_ID in worldChars["mc"]["perks"]

    def PlayerAddPerk(Perk_ID, Soft = False):
        if Perk_ID not in Lib_Perks.keys():
            raise Exception("perk ID %s not found in Lib_Perks" % Perk_ID)
        if Soft == False:
            if Perk_ID in worldChars["mc"]["perks"]:
                raise Exception("tried to add already present perk ID %s, this shouldnt happen ever" % Perk_ID)
        if not PlayerHasPerk(Perk_ID):
            store.worldChars["mc"]["perks"].append(Perk_ID)

        if Perk_ID == "energized":
            InfectionModule().UniqueDailyChars = 3

        #renpy.restart_interaction()
        return

    # used by char screen to get perk pairs/triples/whatever
    # someone call mental doctors i'm goin crazy
    def GetNextPerkBunch():
        for Level in range(1, 100): # 100 arbitrary max level for perks
            # means we went too far to make sense
            if GetPlayerLevel() < Level:
                return {}
            ThisLevelPerkIDs = []
            ThisLevelPerkAmount = 0
            for PerkID, PerkData in Lib_Perks.items():
                if PerkData["level"] == Level:
                    ThisLevelPerkIDs.append(PerkID)
                    ThisLevelPerkAmount += 1
            if ThisLevelPerkAmount != 0 and len(ThisLevelPerkIDs) == ThisLevelPerkAmount:
                if all([not PlayerHasPerk(CheckPerkID) for CheckPerkID in ThisLevelPerkIDs]):
                    ReturnBunch = {}
                    for ReturnPerkID in ThisLevelPerkIDs:
                        ReturnBunch[ReturnPerkID] = Lib_Perks[ReturnPerkID]
                    return ReturnBunch
        return {}