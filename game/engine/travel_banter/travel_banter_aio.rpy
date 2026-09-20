default SeenBanterLabels_Map = set()
default SeenBanterLabels_Camp = set()

# Banter day is stored so that 1 banter event can't happen more often than 1 week
default LastBanterDay = None

init python:
    def Travel_RollPartyBanter_Map():
        if LastBanterDay is not None and (GetGameDay() - LastBanterDay < 7):
            return
        if RngInt(1, 60) != 1:
            return
            
        LegitBanterLabels = TravelModeBanter_Map_GetAllSeeableBanterLabels()
        if not LegitBanterLabels:
            return
    
        renpy.with_statement(dissolve)
        renpy.pause(0.75)
        
        BanterLabel = renpy.random.choice(LegitBanterLabels)
        SeenBanterLabels_Map.add(BanterLabel)

        store.LastBanterDay = GetGameDay()
        renpy.call_in_new_context(BanterLabel)

    def Travel_RollPartyBanter_Camp():
        if LastBanterDay is not None and (GetGameDay() - LastBanterDay < 7):
            return
        if RngInt(1, 60) != 1:
            return
            
        LegitBanterLabels = TravelModeBanter_Camp_GetAllSeeableBanterLabels()
        if not LegitBanterLabels:
            return
    
        renpy.pause(0.25)
        
        BanterLabel = renpy.random.choice(LegitBanterLabels)
        SeenBanterLabels_Camp.add(BanterLabel)

        store.LastBanterDay = GetGameDay()
        renpy.call_in_new_context(BanterLabel)

    def TravelModeBanter_CheckBanterLabelConditions(BanterLabel):
        # Elena x MC
        if BanterLabel in ("travelmodebanter_map_elena_mc_1", "travelmodebanter_map_elena_mc_2"):
            return CharInParty("elena")
        elif BanterLabel == "travelmodebanter_map_elena_mc_3_romance":
            return CharInParty("elena") and CharIsLover("elena")

        # Elena x Markus
        elif BanterLabel in ("travelmodebanter_map_elena_markus_1", "travelmodebanter_map_elena_markus_2", "travelmodebanter_map_elena_markus_3"):
            return CharInParty("elena") and CharInParty("markus")

        # MC x Myu
        elif BanterLabel in ("travelmodebanter_map_myu_1", "travelmodebanter_map_myu_2"):
            return CharInParty("myu")

        # Myu x Elena
        elif BanterLabel in ("travelmodebanter_map_myu_elena_1", "travelmodebanter_map_myu_elena_3"):
            return CharInParty("myu") and CharInParty("elena")
        elif BanterLabel == "travelmodebanter_map_myu_elena_2":
            return CharInParty("myu") and CharInParty("elena") and ("travelmodebanter_map_myu_elena_1" in SeenBanterLabels_Map)

        # Myu x Markus
        elif BanterLabel in ("travelmodebanter_map_myu_markus_1", "travelmodebanter_map_myu_markus_2", "travelmodebanter_map_myu_markus_3"):
            return CharInParty("myu") and CharInParty("markus")

        # Camp
        elif BanterLabel == "travelmodebanter_camp_myu_markus":
            return CharInParty("myu") and CharInParty("markus")

        return False

    def TravelModeBanter_Map_GetAllSeeableBanterLabels():
        return [
            label for label in store.BanterLabels_Map
            if label not in SeenBanterLabels_Map and TravelModeBanter_CheckBanterLabelConditions(label)
        ]

    def TravelModeBanter_Camp_GetAllSeeableBanterLabels():
        return [
            label for label in store.BanterLabels_Camp
            if label not in SeenBanterLabels_Camp and TravelModeBanter_CheckBanterLabelConditions(label)
        ]