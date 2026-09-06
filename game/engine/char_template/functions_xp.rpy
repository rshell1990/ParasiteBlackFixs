init -2 python:
### get level via id or char
    def GetPlayerLevel():
        return GetCharLevelFromID("mc")

    def GetCharLevelFromID(CharID):
        # if its a mob, grab chardef xp value
        if CharID not in worldChars:
            return GetLevelFromExpValue(CharDefs[CharID]["experience"])
        else:
            return GetCharLevelFromChar(worldChars[CharID])

    # distinction bc battle chars
    def GetCharLevelFromChar(Char):
        #CharLevel = 0
        # clamp to maximum
        if Char["experience"] >= allLvls[max(allLvls)]:
            Char["experience"] = allLvls[max(allLvls)]
        return GetLevelFromExpValue(Char["experience"])
        #elif Char["experience"] == -1:
        #    return 0

    def GetLevelFromExpValue(XpValue):
        # edge case for ??? level in battle
        if XpValue == -1:
            return -1
        for Lvl in sorted(list(allLvls.keys())):
            if XpValue <= allLvls[Lvl]:
                return Lvl

### these are for setting a level in char def, 
# might misfire if used somewhere else
    def ExpSetToLevel(TargetLvl):
        return store.allLvls[TargetLvl]

    def ExpShowLevelAsUnknown():
        return -1

    


### functions for adding xp
    # use top two when possible
    def AddExp(CharID, Amount):
        if CharID == "mc":
            AddExpPlayer(Amount)
        else:
            Char = worldChars[CharID]
            AddExpDirect(Char, Amount)

    def AddExpPlayer(Amount):
        AddExpDirect(worldChars["mc"], Amount)
        for CharID in [Char for Char in player_party if Char != "mc" ]:
            AddExperienceToMatchPlayer(CharID)
        return

    # this one is to add directly to char
    def AddExpDirect(Char, Amount):
        if Amount == 0:
            return
        old_lvl = GetCharLevelFromChar(Char)
        Char["experience"] += int(Amount)
        if Char == worldChars["mc"]:
            ShowTutorialPopup("experience")

        new_lvl = GetCharLevelFromChar(Char)
        if new_lvl > old_lvl:
            Char["lvlPoints"]   += (new_lvl - old_lvl) * 2
            Char["skillPoints"] += (new_lvl - old_lvl)
            if Char["HasAltForm"] and new_lvl >= 4:
                # count only levels from 4 onwards
                levels_from_4_onwards = new_lvl - max(3, old_lvl)
                Char["AltForm_SkillPoints"] += max(0, levels_from_4_onwards)

            if Char == worldChars["mc"]:
                HealParty(Silent = True) # <- level ups heal party
                if new_lvl >= 2:
                    ShowTutorialPopup("first_level_up")
                    store.gui_parts["characters"] = True
                if len(GetNextPerkBunch()) > 0:
                    ShowTutorialPopup("perks")
                if store.ShowLevelUpFloatingText:
                    renpy.show_screen("level_up")

                PlaySound(["<silence 0.15>", "audio/interface/level_up.ogg"], Channel = "guisfx2")

                if GetCharLevelFromChar(Char) >= 10 and can_unlock_achievement("A_HERO_IN_THE_MAKING"):
                    unlock_achievement("A_HERO_IN_THE_MAKING")

############# internals
    # Returns XP needed to reach a certain level
    def GetXpRequiredToReachLevel(lvl):
        if lvl == max(allLvls):
            return allLvls[lvl]
        else:
            if lvl in allLvls:
                return allLvls[lvl]
            else:
                return 0

    # Update a character's XP in order to catch up with MC's XP
    def AddExperienceToMatchPlayer(CharID):
        if "experience" in worldChars[CharID]:
            # literally calcs diff and adds it
            Val = worldChars["mc"]["experience"] - worldChars[CharID]["experience"]
            AddExp(CharID, Val)
        return

    # (for ui) return a value from 0.00 to 1.00 (1.00 is 100%)
    # (yea i know these can likely be made saner)
    def getCurrentXpPercentageToReachNextLevel(CharID):
        Char = worldChars[CharID]
        Value = GetXpRequiredToReachLevel(GetCharLevelFromChar(Char)) - GetXpRequiredToReachLevel(GetCharLevelFromChar(Char) - 1)
        if Value > 0:
            return (Char["experience"] - GetXpRequiredToReachLevel(GetCharLevelFromChar(Char) - 1)) / Value
        else:
            return 1.0

    # (for ui) calc for xp bar
    def getCurrentXpInLevel(CharID):
        Char = worldChars[CharID]
        CurrentLevelReqExp = GetXpRequiredToReachLevel(GetCharLevelFromChar(Char) - 1)
        CharInLevelXP = Char["experience"] - CurrentLevelReqExp
        return CharInLevelXP

    # (for ui) more xp bar stuff
    def getXpInLevelToReachNext(CharID):
        Char = worldChars[CharID]
        # a lower bound we start from, for ex we needed 800 to reach our current level
        CurrentLevelReqExp = GetXpRequiredToReachLevel(GetCharLevelFromChar(Char) - 1)
        # a higher bound, for ex we need a total of 1600 to reach next lvl
        NextLevelReqExp = GetXpRequiredToReachLevel(GetCharLevelFromChar(Char))
        return NextLevelReqExp - CurrentLevelReqExp

    

    # this recalculates attribute points, skill points, and alt form skill points
    # it is "generous": if char has MORE than they should, 
    # they will keep the extra points
    # but if they had less than they should, they'll receive more points
    # USED in save fixer and when char joins
    def RecalcSkillAndAttrPoints(CharID):
        VerboseLog_General = False
        VerboseLog_Attr = False
        VerboseLog_Skills = False
        VerboseLog_AltSkills = False
        
        if VerboseLog_General:
            print("------------")
            print("running attr/skill/altskill recalc for %s" % CharID)
        Assert(CharID in worldChars)
        Char = worldChars[CharID]

        ### attributes come first
        ### calculate attr point "diff" from base char template:
        if VerboseLog_Attr:
            print("___")
            print("processing attributes for %s" % CharID)
        AttrList = ["Strength", "Endurance", "Willpower", "Mana_Power", "Agility", "Dexterity", "Luck", "Charisma", "Barter"]
        TotalAttrPointsDiff = 0
        for AttrID in AttrList:
            DiffValue = Char[AttrID] - CharDefs[CharID][AttrID]
            if DiffValue == 0:
                continue
            elif DiffValue < 0:
                if VerboseLog_Attr:
                    print("sth wrong, attribute %s has diff value of %s" % (AttrID, DiffValue))
            elif DiffValue > 0:
                TotalAttrPointsDiff += DiffValue

        if VerboseLog_Attr:
            print("total attribute points difference from base character: %s " % TotalAttrPointsDiff)

        ### calculate how much attr points we should have according to level
        # each level grants 2 attr points
        AttrPointsAtThisLevel = (GetCharLevelFromChar(Char) - 1) * 2
        if VerboseLog_Attr:
            print("should have attribute points to distribute based on lvl: %s " % AttrPointsAtThisLevel)

        ### now factor in directy added attributes
        DirectlyAddedAttrPoints = Char["directly_added_attribute_points"]
        if VerboseLog_Attr:
            print("directly added (books or quests) attr points: %s " % DirectlyAddedAttrPoints)
        AttrPointsWithDirectlyAdded = AttrPointsAtThisLevel + DirectlyAddedAttrPoints

        if VerboseLog_Attr:
            print("total attr points this char can possibly have: %s " % AttrPointsWithDirectlyAdded)

        ### calc the legit possible difference
        LeftoverAttrPoints = AttrPointsWithDirectlyAdded - TotalAttrPointsDiff
        if VerboseLog_Attr:
            print("legal diff/leftover is %s " % LeftoverAttrPoints)
            print("this char's original lvlPoints were %s " % Char["lvlPoints"])
            if LeftoverAttrPoints == Char["lvlPoints"]:
                print("-> All good")

        ### write value ONLY IF LESS, we're generous
        if LeftoverAttrPoints >= 0:
            if LeftoverAttrPoints > Char["lvlPoints"]:
                if VerboseLog_Attr:
                    print("writing %s as char's new free lvlpoints" % LeftoverAttrPoints)
                Char["lvlPoints"] = LeftoverAttrPoints
        else:
            if VerboseLog_Attr:
                # big brain statement
                print("char has negative free attr points: %s " % CharID)

        ### now, skill points
        ### calculate skill points diff from base char template
        if VerboseLog_Skills:
            print("___")
            print("processing skills for %s" % CharID)

        TotalSkillPointsDiff = 0

        for SkillID, SkillValue in Char["CharSkills"].items():
            DiffValue = Char["CharSkills"][SkillID] - CharDefs[CharID]["CharSkills"].get(SkillID, 0)
            if DiffValue == 0:
                continue
            elif DiffValue < 0:
                if VerboseLog_Skills:
                    print("sth wrong, skill %s has diff value of %s" % (SkillID, DiffValue))
            elif DiffValue > 0:
                TotalSkillPointsDiff += DiffValue
        
        if VerboseLog_Skills:
            print("total skill points difference from base character: %s " % TotalSkillPointsDiff)


        ### calculate how much skill points we should have according to level
        # each level grants 1 skill point
        SkillPointsAtThisLevel = GetCharLevelFromChar(Char) - 1
        if VerboseLog_Skills:
            print("should have skill points to distribute based on lvl: %s " % SkillPointsAtThisLevel)

        ### calc the legit possible difference
        LeftoverSkillPoints = SkillPointsAtThisLevel - TotalSkillPointsDiff
        if VerboseLog_Skills:
            print("legal diff/leftover skill pts: %s " % LeftoverSkillPoints)
            print("this char's original skillPoints were %s " % Char["skillPoints"])
            if LeftoverSkillPoints == Char["skillPoints"]:
                print("-> All good")

        ### write value ONLY IF LESS, we're generous
        if LeftoverSkillPoints >= 0:
            if LeftoverSkillPoints > Char["skillPoints"]:
                if VerboseLog_Skills:
                    print("writing %s as char's new free skillPoints" % LeftoverSkillPoints)
                Char["skillPoints"] = LeftoverSkillPoints
        else:
            if VerboseLog_Skills:
                # big brain statement
                print("char has negative free skill points: %s " % CharID)

        ### now, alt form skill points
        ### calculate skill points diff from base char template
        if Char["HasAltForm"] == False:
            return

        if VerboseLog_AltSkills:
            print("___")
            print("processing alt form skills for %s" % CharID)

        TotalAltSkillPointsDiff = 0

        for SkillID, SkillValue in Char["AltForm_CharSkills"].items():
            DiffValue = Char["AltForm_CharSkills"][SkillID] - CharDefs[CharID]["AltForm_CharSkills"].get(SkillID, 0)
            if DiffValue == 0:
                continue
            elif DiffValue < 0:
                if VerboseLog_AltSkills:
                    print("sth wrong, skill %s has diff value of %s" % (SkillID, DiffValue))
            elif DiffValue > 0:
                TotalAltSkillPointsDiff += DiffValue
        
        if VerboseLog_AltSkills:
            print("total alt skill points difference from base character: %s " % TotalAltSkillPointsDiff)

        ### calculate how much alt skill points we should have according to level
        # each level PAST FOURTH grants 1 skill point
        AltSkillPointsAtThisLevel = GetCharLevelFromChar(Char) - 3
        if VerboseLog_AltSkills:
            print("should have alt skill points to distribute based on lvl: %s " % AltSkillPointsAtThisLevel)

        ### calc the legit possible difference
        LeftoverAltSkillPoints = AltSkillPointsAtThisLevel - TotalAltSkillPointsDiff
        if VerboseLog_AltSkills:
            print("legal diff/leftover alt skill pts: %s " % LeftoverAltSkillPoints)
            print("this char's original AltForm_SkillPoints were %s " % Char["AltForm_SkillPoints"])
            if LeftoverAltSkillPoints == Char["AltForm_SkillPoints"]:
                print("-> All good")

        ### write value ONLY IF LESS, we're generous
        if LeftoverAltSkillPoints >= 0:
            if LeftoverAltSkillPoints > Char["AltForm_SkillPoints"]:
                if VerboseLog_AltSkills:
                    print("writing %s as char's new free AltForm_SkillPoints" % LeftoverAltSkillPoints)
                Char["AltForm_SkillPoints"] = LeftoverAltSkillPoints
        else:
            if VerboseLog_AltSkills:
                # big brain statement
                print("char has negative free alt form skill points: %s " % CharID)

        
