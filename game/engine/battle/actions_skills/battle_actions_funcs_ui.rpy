init python:
    # used alot in skilldesc to quickly wrap var into () or add %
    def Battle_FormatDescVal(Value, Percentage = False, Parentheses = False):
        NewString = "{color=[BATTLE_COLORS.SKILLDESC_GREEN]}"
        if Parentheses:
            NewString += "("
        NewString += str(Value)
        if Percentage:
            NewString += "%"
        if Parentheses:
            NewString += ")"
        NewString += "{/color}"
        return NewString

    def GetSkillDesc(SkillObject):
        text_strings = []

        # name and skill level
        if SkillObject.Level_Max > 1 and SkillObject.Level > 0:
            text_strings.append("{size=+6}" + tra(SkillObject.DisplayName) + " " + tra(_("(Level %s)")) % SkillObject.Level + "{/size}")
        else:
            text_strings.append("{size=+6}" + tra(SkillObject.DisplayName) + "{/size}")

        if SkillObject.Level == 0:
            text_strings.append(SkillObject.GetDesc(DescLevel = 1))
        else:
            text_strings.append(SkillObject.GetDesc(DescLevel = SkillObject.Level))

        CostStrings = []
        if SkillObject.Cost_Energy:
            CostStrings.append("\n{color=[BATTLE_COLORS.ENERGY]}" + tra(_("Energy cost: ")) + f"{SkillObject.Cost_Energy}" + "{/color}")
        if SkillObject.Cost_Infection:
            CostStrings.append("\n{color=[BATTLE_COLORS.INFECTION]}" + tra(_("Infection cost: ")) + f"{SkillObject.Cost_Infection}" + "{/color}")
        if SkillObject.Cost_Mana:
            CostStrings.append("\n{color=[BATTLE_COLORS.MANA]}" + tra(_("Mana cost: ")) + f"{SkillObject.Cost_Mana}" + "{/color}")
        if SkillObject.Cost_PercHealthCurr:
            CostStrings.append("\n{color=[BATTLE_COLORS.HEALTH]}" + tra(_("Current health %-cost: ")) + f"{max(int(SkillObject.Cost_PercHealthCurr * 100), 1)}%" + "{/color}")
        if SkillObject.Cost_PercHealthMax:
            CostStrings.append("\n{color=[BATTLE_COLORS.HEALTH]}" + tra(_("Max health %-cost: ")) + f"{max(int(SkillObject.Cost_PercHealthMax * 100), 1)}%" + "{/color}")
        CostString = (" ".join(CostStrings) if len(CostStrings) > 0 else None)

        if CostString:
            text_strings.append(CostString)

        # means we're in battle, show hit %
        if SkillObject.Owner_BattleChar is not None:
            if SkillObject.ShowHitChance == True:
                if SkillObject.ValidTargets == BATTLE_TARGETS.ANY_ENEMY:
                    AllTargets = Battle_GetAllTargetsList(SkillObject)
                    if len(AllTargets) == 1:
                        SoleTarget = AllTargets[0]
                        if SoleTarget.BattleSide != SkillObject.Owner_BattleChar.BattleSide:
                            HitProb = Battle_GetHitProb(SkillObject.Owner_BattleChar, SoleTarget)
                            String = "%s %s: %s%%" % (tra(_("Chance to hit")), tra(SoleTarget.CharRef["name"]), HitProb)
                            text_strings.append(String)
                elif SkillObject.ValidTargets == BATTLE_TARGETS.ALL_ENEMIES:
                    AllTargets = Battle_GetAllTargetsList(SkillObject)
                    for Target in AllTargets:
                        HitProb = Battle_GetHitProb(SkillObject.Owner_BattleChar, Target)
                        String = "%s %s: %s%%" % (tra(_("Chance to hit")), tra(Target.CharRef["name"]), HitProb)
                        text_strings.append(String)

        return "\n".join(text_strings)