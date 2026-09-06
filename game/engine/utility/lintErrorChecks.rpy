    # LINT_CHECK_LIST uncomment to add
    # lint will be slower with these, 
    # so comment them out when not needed!
    # after you uncomment all these, run LINT and scroll down
# init 1 python:    
#     renpy.config.lint_stats_callbacks.append(LINT_LocationReport)
#     renpy.config.lint_stats_callbacks.append(LINT_MakeSureButtonTagsAreUnique)
#     renpy.config.lint_stats_callbacks.append(LINT_CheckLootDropDataItemIDs)
#     renpy.config.lint_stats_callbacks.append(LINT_CheckSkillIDs)
#     renpy.config.lint_stats_callbacks.append(LINT_CheckWorldMapLocations)
#     renpy.config.lint_stats_callbacks.append(LINT_CheckQuestTrackTags)
init python:
###################################################################
    ### checks if trackTags are fucked
    def LINT_CheckQuestTrackTags():
        ErrorStrings = []
        AllBtnIDs = set()
        for WorldLocationID, WorldLocationObject in wLocs.items():
            for BtnID, BtnData in WorldLocationObject.btns.items():
                AllBtnIDs.add(BtnID)

        for QstObj in GetAllQuests():
            for GoalKey, GoalVal in QstObj.GoalStates.items():
                TrackTags = []
                if QstObj.GOALS[GoalKey].TrackTag is not None:
                    if isinstance(QstObj.GOALS[GoalKey].TrackTag, list):
                        TrackTags = QstObj.GOALS[GoalKey].TrackTag
                    else:
                        TrackTags = [QstObj.GOALS[GoalKey].TrackTag]
                for TrackTag in TrackTags:
                    if TrackTag not in AllBtnIDs:
                        ErrorStrings.append("%s, goal %s has tracktag that is not a button ID: %s" % (QstObj.TITLE, GoalVal, TrackTag))

        print("=================")
        print(" Qst track tag issues ")

        for ErrorString in ErrorStrings:
            print(ErrorString)

        print("\n%d total issues" % len(ErrorStrings))
        print("=================")
        return

###################################################################
    ### checks if a loc has a screen missing
    def LINT_LocationReport():
        ErrorStrings = []

        for Tag, LocObj in wLocs.items():
            screenVar = renpy.display.screen.get_screen_variant("loc_%s" % Tag)
            if screenVar is None:
                ErrorStrings.append("Location %s: missing a screen" % Tag)

        print("=================")
        print(" Location issues ")

        for ErrorString in ErrorStrings:
            print(ErrorString)

        print("\n%d total issues" % len(ErrorStrings))
        print("=================")
        return

    
###################################################################
    ### checks if any world location buttons have overlapping ids
    def LINT_MakeSureButtonTagsAreUnique():
        ErrorStrings = []

        UniqueButtonIDs = {} # button_id:wloc_id
        for WorldLocationID, WorldLocationObject in wLocs.items():
            for button_ID in WorldLocationObject.btns.keys():
                if button_ID not in UniqueButtonIDs:
                    UniqueButtonIDs[button_ID] = WorldLocationID
                else:
                    ErrorStrings.append("Overlapping button IDs: Button ID '%s' found in both world location '%s' and in world location: '%s'." % (button_ID, WorldLocationID, UniqueButtonIDs[button_ID]))

        for ButtonID, WorldLocationID in UniqueButtonIDs.items():
            for QstObj in GetAllQuests():
                if hasattr(QstObj, "locationMod"):
                    locMod = QstObj.locationMod()
                    if locMod is not None:
                        for ButtonID, ButtonStuff in locMod.directMods.items():
                            if ButtonID not in UniqueButtonIDs:
                                ErrorStrings.append("Missing button ID definition: Button ID '%s' defined in a locationMod() in quest/module '%s' has no behaviour definition in any location." % (ButtonID, type(QstObj).__name__))

        print("=================")
        print(" Button tag issues ")

        for ErrorString in ErrorStrings:
            print(ErrorString)

        print("\n%d total issues" % len(ErrorStrings))
        print("=================")
        return

###################################################################
    # this returns a list of wrong item ids and/or wrong mob ids in lootdropdata
    def LINT_CheckLootDropDataItemIDs():
        ErrorStrings = []

        for MobID, MobDropList in LootDropData.items():
            if MobID not in CharDefs:
                ErrorStrings.append("Mob ID %s defined in LootDropData does not exist" % MobID)
            for Entry in MobDropList:
                if Entry["ItemID"] not in static_item_defs:
                    ErrorStrings.append("Wrong item ID %s in drop data entry %s" % (Entry["ItemID"], MobID))

        print("=================")
        print(" Loot drop issues ")

        for ErrorString in ErrorStrings:
            print(ErrorString)

        print("\n%d total issues" % len(ErrorStrings))
        print("=================")
        return


    
###################################################################
    # this checks if any skill ID on a char is not in skilllib
    def LINT_CheckSkillIDs():
        ErrorStrings = []

        for CharID, CharData in CharDefs.items():
            for SkillID in CharData["CharSkills"]:
                if SkillID not in SkillLib:
                    ErrorStrings.append("Skill %s not found in SkillLib!" % SkillID)
            for SkillID in CharData["AltForm_CharSkills"]:
                if SkillID not in SkillLib:
                    ErrorStrings.append("Skill %s not found in SkillLib!" % SkillID)

        print("=================")
        print(" Skill ID issues ")

        for ErrorString in ErrorStrings:
            print(ErrorString)

        print("\n%d total issues" % len(ErrorStrings))
        print("=================")
        return

###################################################################
    # this checks if world map locations are defined properly
    def LINT_CheckWorldMapLocations():
        ErrorStrings = set()

        for LocTag in wLocs:
            RootTag = wLocs[LocTag].WorldMapRootLocTag
            if RootTag == None:
                if hasattr(wLocs[LocTag], "wMap_DisplayName"):
                    ErrorStrings.add("Supposedly root location ID %s doesnt have a WorldMapRootLocTag defined!" % LocTag)
            else:
                if not hasattr(wLocs[RootTag], "wMap_DisplayName"):
                    ErrorStrings.add("Supposedly root location ID %s doesnt have a world-map definition!" % RootTag)

        print("=================")
        print(" World map location def issues ")

        for ErrorString in ErrorStrings:
            print(ErrorString)

        print("\n%d total issues" % len(ErrorStrings))
        print("=================")
        return
