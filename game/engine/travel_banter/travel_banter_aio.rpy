default SeenBanterLabels_Map = set()
default SeenBanterLabels_Camp = set()

# banter day is stored so that 1 banter event cant happen more often than 1 week
default LastBanterDay = None

init python:
    def Travel_RollPartyBanter_Map():
        if LastBanterDay is not None:
            if GetGameDay() - 7 < LastBanterDay:
                return
        if RngInt(1, 60) != 1:
            return
        LegitBanterLabels = TravelModeBanter_Map_GetAllSeeableBanterLabels()
        if len(LegitBanterLabels) == 0:
            return
    
        LocFlush(dissolve)
        Pause(0.75)
        BanterLabel = renpy.random.choice(LegitBanterLabels)
        SeenBanterLabels_Map.add(BanterLabel)

        store.LastBanterDay = GetGameDay()

        renpy.call(BanterLabel)
        return

    def Travel_RollPartyBanter_Camp():
        if LastBanterDay is not None:
            if GetGameDay() - 7 < LastBanterDay:
                return
        if RngInt(1, 60) != 1:
            return
        LegitBanterLabels = TravelModeBanter_Camp_GetAllSeeableBanterLabels()
        if len(LegitBanterLabels) == 0:
            return
    
        Pause(0.25)
        BanterLabel = renpy.random.choice(LegitBanterLabels)
        SeenBanterLabels_Camp.add(BanterLabel)

        store.LastBanterDay = GetGameDay()
        
        renpy.call(BanterLabel)
        return

    def TravelModeBanter_CheckBanterLabelConditions(BanterLabel):
        ### elena x mc
        if BanterLabel == "travelmodebanter_map_elena_mc_1":
            if CharInParty("elena"):
                return True
        elif BanterLabel == "travelmodebanter_map_elena_mc_2":
            if CharInParty("elena"):
                return True
        elif BanterLabel == "travelmodebanter_map_elena_mc_3_romance":
            if CharInParty("elena"):
                if CharIsLover("elena"):
                    return True

        ### elena x markus
        elif BanterLabel == "travelmodebanter_map_elena_markus_1":
            if CharInParty("elena"):
                if CharInParty("markus"):
                    return True
        elif BanterLabel == "travelmodebanter_map_elena_markus_2":
            if CharInParty("elena"):
                if CharInParty("markus"):
                    return True
        elif BanterLabel == "travelmodebanter_map_elena_markus_3":
            if CharInParty("elena"):
                if CharInParty("markus"):
                    return True

        ### mc x myu
        elif BanterLabel == "travelmodebanter_map_myu_1":
            if CharInParty("myu"):
                return True
        elif BanterLabel == "travelmodebanter_map_myu_2":
            if CharInParty("myu"):
                return True
        ### myu x elena
        elif BanterLabel == "travelmodebanter_map_myu_elena_1":
            if CharInParty("myu"):
                if CharInParty("elena"):
                    return True
        elif BanterLabel == "travelmodebanter_map_myu_elena_2":
            if CharInParty("myu"):
                if CharInParty("elena"):
                    # means #1 was seen by player
                    if "travelmodebanter_map_myu_elena_1" in SeenBanterLabels_Map:
                        return True
        elif BanterLabel == "travelmodebanter_map_myu_elena_3":
            if CharInParty("myu"):
                if CharInParty("elena"):
                    return True
        ### myu x markus
        elif BanterLabel == "travelmodebanter_map_myu_markus_1":
            if CharInParty("myu"):
                if CharInParty("markus"):
                    return True
        elif BanterLabel == "travelmodebanter_map_myu_markus_2":
            if CharInParty("myu"):
                if CharInParty("markus"):
                    return True
        elif BanterLabel == "travelmodebanter_map_myu_markus_3":
            if CharInParty("myu"):
                if CharInParty("markus"):
                    return True
        ### camp one
        if BanterLabel == "travelmodebanter_camp_myu_markus":
            if CharInParty("myu") and CharInParty("markus"):
                return True
        return False     

    def TravelModeBanter_Map_GetAllSeeableBanterLabels():
        Result = []
        for BanterLabel in store.BanterLabels_Map:
            if BanterLabel not in SeenBanterLabels_Map:
                if TravelModeBanter_CheckBanterLabelConditions(BanterLabel):
                    Result.append(BanterLabel)
        return Result    

    def TravelModeBanter_Camp_GetAllSeeableBanterLabels():
        Result = []
        for BanterLabel in store.BanterLabels_Camp:
            if BanterLabel not in SeenBanterLabels_Camp:
                if TravelModeBanter_CheckBanterLabelConditions(BanterLabel):
                    Result.append(BanterLabel)
        return Result
