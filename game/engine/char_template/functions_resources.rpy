init -2 python:
# all these functions are supposed for *story mode* (except "direct" variants on the bottom)
    def CharHeal(CharID, Value = 0):
        Char = worldChars[CharID]
        CharHealDirect(Char, Value = Value)
        return

    def CharRestoreEnergy(CharID, Value = 0):
        Char = worldChars[CharID]
        CharRestoreEnergyDirect(Char, Value = Value)
        return

    def CharRestoreMana(CharID, Value = 0):
        Char = worldChars[CharID]
        CharRestoreManaDirect(Char, Value = Value)
        return    

    def HealParty(Silent = False, ClearStatusEffects = True, NotifyLine = _("Resting has healed your party to full health!")):
        for CharID in player_party:
            CharHeal(CharID, worldChars[CharID]["HealthMax"])
            if ClearStatusEffects == True:
                if CharID in StoryStatusEffects:
                    StoryStatusEffects.pop(CharID)
        if not Silent:
            AddNotif(NotifyLine, Kind = "heal_party")
        return

    def DamagePlayer(Value, Silent = False, Lethal = True): 
        DamageChar("mc", Value, Silent = Silent, Lethal = Lethal)
        return

    def DamageParty(Value, Silent = False, Lethal = True):
        for CharID in player_party:
            DamageChar(CharID, Value, Silent = Silent, Lethal = Lethal)
        return

    def DamageChar(CharID, Value, Soft = False, Silent = False, Lethal = True):
        NewVal = int(Value)

        # clamp to just 1 if non-lethal
        if Lethal == False:
            if worldChars[CharID]["Health"] <= NewVal:
                NewVal = worldChars[CharID]["Health"] - 1

        # subtract health
        worldChars[CharID]["Health"] -= NewVal

        # notify
        if Silent == False:
            if CharID == "mc":
                if NewVal == 0:
                    AddNotif(tra(_("You took some damage and nearly died!")), Kind = "story_damage_mc")
                else:
                    AddNotif(tra(_("You took %s damage!")) % NewVal, Kind = "story_damage_mc")
            else:
                if CharID in player_party:
                    if NewVal == 0:
                        AddNotif(tra(_("%s took some damage and nearly died!")) % worldChars[CharID]["name"], Kind = "story_damage_nonmc")
                    else:    
                        AddNotif(tra(_("%s took %s damage!")) % (worldChars[CharID]["name"], NewVal), Kind = "story_damage_nonmc")
        
        # jump to 
        if CharID == "mc":
            if worldChars["mc"]["Health"] <= 0:
                if Lethal:
                    renpy.jump("defeat_generic")
        return

########## "direct" variants operate directly on worldchar, 
##### used to convert story to battle chars
    def CharHealDirect(Char, Value = 0):
        Assert(isinstance(Char, PBCharacter), "Wrong char input for CharHealDirect")
        # if 0, to full?
        if Value == 0:
            Char["Health"] = Char["HealthMax"]
        else:
            Char["Health"] = ClampValue(Char["Health"] + int(Value), 1, Char["HealthMax"])
        return

    def CharRestoreManaDirect(Char, Value = 0):
        Assert(isinstance(Char, PBCharacter), "Wrong char input for CharRestoreManaDirect")
        # if 0, to full?
        if Value == 0:
            Char["Mana"] = Char["ManaMax"]
        else:
            Char["Mana"] = ClampValue(Char["Mana"] + Value, 1, Char["ManaMax"])
        return

    def CharRestoreEnergyDirect(Char, Value = 0):
        Assert(isinstance(Char, PBCharacter), "Wrong char input for CharRestoreEnergyDirect")
        # if 0, to full?
        if Value == 0:
            Char["Energy"] = Char["EnergyMax"]
        else:
            Char["Energy"] = ClampValue(Char["Energy"] + Value, 1, Char["EnergyMax"])
        return
