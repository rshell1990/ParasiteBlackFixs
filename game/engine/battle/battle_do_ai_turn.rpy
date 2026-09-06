init python:
    def Battle_DoAITurn(BattleChar):
        # counter-killed chars can be still present in activecharslist
        if not BattleChar.IsAlive:
            if BattleChar in BattleScene.ActiveCharsList:
                BattleScene.ActiveCharsList.remove(BattleChar)
            return

        if Battle_HasStatusEffect(BattleChar, "taunt"):
            Battle_SetCharAction(BattleChar, BattleChar.Skill_Attack, Battle_GetStatusEffect(BattleChar, "taunt").TauntedBy)
            return

        # gather all usable skills
        # note the transform skills are left out intentionally
        CharDoableActions = []
        CharDoableActions.append(BattleChar.Skill_Attack)
        CharDoableActions.append(BattleChar.Skill_Defend)
        for Skill in BattleChar.Skills:
            if Skill.CanExecute() and len(Battle_GetAllTargetsList(Skill)) > 0 and Skill.OwnerCharCanPaySkillCost():
                CharDoableActions.append(Skill)

        # assmeble skill-targetlist pairs
        ActionTargetPairs = []
        for Action in CharDoableActions:
            if Action.ValidTargets == BATTLE_TARGETS.SELF:
                ActionTargetPairs.append([Action, [BattleChar]])
            elif (Action.ValidTargets == BATTLE_TARGETS.ANY_ALLY 
                or Action.ValidTargets == BATTLE_TARGETS.ALLY_NOT_SELF
                or Action.ValidTargets == BATTLE_TARGETS.ANY_ENEMY):
                    for ActionTarget in Battle_GetAllTargetsList(Action):
                        ActionTargetPairs.append([Action, [ActionTarget]])
            elif (Action.ValidTargets == BATTLE_TARGETS.ALL_ENEMIES
                or Action.ValidTargets == BATTLE_TARGETS.ALL_ALLIES
                or Action.ValidTargets == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF
                or Action.ValidTargets == BATTLE_TARGETS.EVERYONE):
                    ActionTargetPairs.append([Action, Battle_GetAllTargetsList(Action)])

        # forward-gather relevant variables
        CharDmgMod_Incoming = Battle_GetIncomingDamageMod(BattleChar)
        CharDmgMod_Dealt = Battle_GetOutgoingDamageMod(BattleChar)

        CharStatMod_Armor = Battle_GetCharStatMod_Armor(BattleChar)
        CharStatMod_AttackRating = Battle_GetCharStatMod_AttackRating(BattleChar)
        CharStatMod_DodgeRating = Battle_GetCharStatMod_DodgeRating(BattleChar)
        CharStatMod_MagicRes = Battle_GetCharStatMod_MagicRes(BattleChar)
        CharStatMod_CritChance = Battle_GetCharStatMod_CritChance(BattleChar)

        CharHealthRatio = BattleChar.Health / BattleChar.HealthMax
        CharHealthRatioMissing = 1.0 - CharHealthRatio

        CharEnergyRatio = BattleChar.Energy / BattleChar.EnergyMax
        CharEnergyRatioMissing = 1.0 - CharEnergyRatio

        AliveAllies = Battle_GetAllAlliesOfChar(BattleChar)

        # ai smartness knob, 0.0 dumb 1.0 smart
        AISmartness = 0.75
        # priority factors based on smartness.
        # "prioritizing" factor 
        # ranges from 1.0 to 2.0 dep on smartness
        RaisePriorityFactor = 1.0 + AISmartness
        # "deprioritizing" factor 
        # ranges from 1.0 to 0.0 dep on smartness
        LowerPriorityFactor = 1.0 - AISmartness

        # assemble weighted action-targetlist pairs
        ActionTargetPairsWeighted = []
        for ActionTargetPair in ActionTargetPairs:
            Action = ActionTargetPair[0]
            TargetOrTargets = ActionTargetPair[1]

            LowestHealthTarget = TargetOrTargets[0]
            if len(TargetOrTargets) > 1:
                for OtherTarget in TargetOrTargets:
                    if OtherTarget.Health < LowestHealthTarget.Health:
                        LowestHealthTarget = OtherTarget

            if len(Action.AITags) > 0:
                NewActionWeight = 0.0
                for Target in TargetOrTargets:
                    CumulativeWeight = Action.AIBaseWeight

                    TargetHealthRatio = Target.Health / Target.HealthMax
                    TargetHealthRatioMissing = 1.0 - TargetHealthRatio

                    TargetManaRatio = Target.Mana / Target.ManaMax

                    TargetEnergyRatio = Target.Energy / Target.EnergyMax
                    TargetEnergyRatioMissing = 1.0 - TargetEnergyRatio

                    if AI_TAGS.DEAL_PHYS_DAMAGE in Action.AITags:
                        # PROS
                        # if we're under damage mult, ++
                        if CharDmgMod_Dealt > 1.0:
                            CumulativeWeight *= RaisePriorityFactor
                        # if we're under acc buff ++
                        if CharStatMod_AttackRating > 1.0:
                            CumulativeWeight *= RaisePriorityFactor
                        # if we're under crit buff ++
                        if CharStatMod_CritChance > 1.0:
                            CumulativeWeight *= RaisePriorityFactor
                        # if enemy is stunned, ++
                        if Battle_HasStatusEffect(Target, "stun"):
                            CumulativeWeight *= RaisePriorityFactor
                        # if enemy is taunted, ++
                        if Battle_HasStatusEffect(Target, "taunt"):
                            CumulativeWeight *= RaisePriorityFactor

                        if LowestHealthTarget == Target:
                            CumulativeWeight *= RaisePriorityFactor

                    if AI_TAGS.FAVOURED_HIGHER_AGI_THAN_TARGETS in Action.AITags:
                        if BattleChar.CharRef["Agility"] > Target.CharRef["Agility"]:
                            CumulativeWeight *= RaisePriorityFactor

                    if AI_TAGS.FAVOURED_HIGHER_DEX_THAN_TARGETS in Action.AITags:
                        if BattleChar.CharRef["Dexterity"] > Target.CharRef["Dexterity"]:
                            CumulativeWeight *= RaisePriorityFactor

                    if (AI_TAGS.REMOVE_DEBUFFS_ON_TARGET in Action.AITags or AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET in Action.AITags):
                        DebuffsCountOnTarget = 0
                        for StatusEffect in Target.StatusEffects:
                            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                                DebuffsCountOnTarget += 1

                        if DebuffsCountOnTarget > 1:
                            CumulativeWeight *= (2.0 * RaisePriorityFactor * DebuffsCountOnTarget)

                    if (AI_TAGS.REMOVE_BUFFS_ON_TARGET in Action.AITags 
                    or AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_BUFFS_ON_TARGET in Action.AITags):
                        BuffsCountOnTarget = 0
                        for StatusEffect in Target.StatusEffects:
                            if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                                BuffsCountOnTarget += 1

                        if BuffsCountOnTarget >= 1:
                            CumulativeWeight *= (RaisePriorityFactor * BuffsCountOnTarget)

                    if AI_TAGS.STRONGER_ON_BURNING_ENEMY in Action.AITags:
                        if Battle_HasStatusEffect(Target, "burn"):
                            CumulativeWeight *= RaisePriorityFactor

                    if (AI_TAGS.IGNORES_ENEMY_DODGE in Action.AITags or AI_TAGS.FAVOURED_HIGHEST_DODGE in Action.AITags):
                        HighestDodgeTarget = TargetOrTargets[0]
                        for OtherTarget in TargetOrTargets:
                            if OtherTarget.DodgeRating > HighestDodgeTarget.DodgeRating:
                                HighestDodgeTarget = OtherTarget
                        if HighestDodgeTarget == Target:
                            CumulativeWeight *= RaisePriorityFactor

                    if AI_TAGS.IGNORES_ENEMY_ARMOR in Action.AITags:
                        HighestArmorTarget = TargetOrTargets[0]
                        for OtherTarget in TargetOrTargets:
                            if OtherTarget.Armor > HighestArmorTarget.Armor:
                                HighestArmorTarget = OtherTarget
                        if HighestArmorTarget == Target:
                            CumulativeWeight *= RaisePriorityFactor
                        
                    if AI_TAGS.HEAL_SELF in Action.AITags:
                        if CharHealthRatio < 1.0:
                            CumulativeWeight *= (RaisePriorityFactor * CharHealthRatioMissing * 2)
                            if CharHealthRatio < 0.5:
                                CumulativeWeight *= (RaisePriorityFactor * CharHealthRatioMissing * 2)

                    if AI_TAGS.HEAL_TARGET in Action.AITags:
                        if TargetHealthRatio < 1.0:
                            CumulativeWeight *= (RaisePriorityFactor * TargetHealthRatioMissing)
                            if TargetHealthRatio < 0.5:
                                CumulativeWeight *= (RaisePriorityFactor * TargetHealthRatioMissing)

                    if AI_TAGS.FAVOURED_LAST_HIT in Action.AITags:
                        if TargetHealthRatio < 0.25:
                            CumulativeWeight *= RaisePriorityFactor

                    if AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO in Action.AITags:
                        CumulativeWeight *= (RaisePriorityFactor * CharHealthRatio * 2)

                    if AI_TAGS.FAVOURED_HIGH_OWN_ENERGY_RATIO in Action.AITags:                        
                        CumulativeWeight *= (RaisePriorityFactor * CharEnergyRatio * 2)

                    if AI_TAGS.FAVOURED_LOW_OWN_ENERGY_RATIO in Action.AITags:                        
                        CumulativeWeight *= (RaisePriorityFactor * CharEnergyRatioMissing * 2)

                    if AI_TAGS.FAVOURED_LOW_TARGET_ENERGY in Action.AITags:
                        CumulativeWeight *= 1.0 + (RaisePriorityFactor * TargetEnergyRatioMissing)

                    if AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO in Action.AITags:
                        CumulativeWeight *= 1.0 + (RaisePriorityFactor * TargetHealthRatioMissing)

                    if (AI_TAGS.RAISE_TARGET_PHYS_DAMAGE_RESISTANCE in Action.AITags or AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE in Action.AITags):
                        AllEnemies = Battle_GetAllEnemiesOfChar(BattleChar)
                        for EnemyBchar in AllEnemies:
                            if Battle_HasStatusEffect(EnemyBchar, "taunt"):
                                if Battle_GetStatusEffect(EnemyBchar, "taunt").TauntedBy == BattleChar:
                                    CumulativeWeight *= (RaisePriorityFactor * 0.75)
                            if Battle_GetOutgoingDamageMod(EnemyBchar) > 1.0:
                                CumulativeWeight *= (RaisePriorityFactor * 0.75)

                    if AI_TAGS.TAUNT_TARGET in Action.AITags:
                        if len(AliveAllies) > 0:
                            HealthRatio = BattleChar.Health / BattleChar.HealthMax
                            if HealthRatio > 0.5:
                                CumulativeWeight *= RaisePriorityFactor * 0.75 * len(AliveAllies)

                    if AI_TAGS.ONLY_IF_ALLIES_EXIST in Action.AITags:
                        CumulativeWeight *= RaisePriorityFactor * len(AliveAllies)

                    if AI_TAGS.DEAL_PHYS_DAMAGE in Action.AITags:
                        # CONS
                        # if enemy under armor buff, --
                        if Battle_GetCharStatMod_Armor(Target) > 1.0:
                            CumulativeWeight *= LowerPriorityFactor
                        # if enemy under dodge buff, --
                        if Battle_GetCharStatMod_DodgeRating(Target) > 1.0:
                            CumulativeWeight *= LowerPriorityFactor
                        # if enemy is protected by someone, --
                        if Battle_HasStatusEffect(Target, "protect"):
                            CumulativeWeight *= LowerPriorityFactor
                        # if enemy is under defensive dmgin buff, --
                        if Battle_GetIncomingDamageMod(Target) < 1.0:
                            CumulativeWeight *= LowerPriorityFactor
                        # if enemy is invincible, --
                        if Battle_HasStatusEffect(Target, "godmode"):
                            CumulativeWeight *= LowerPriorityFactor

                    if AI_TAGS.GAIN_TURN in Action.AITags:
                        CumulativeWeight *= RaisePriorityFactor

                    if AI_TAGS.INCREASE_SELF_DAMAGE in Action.AITags:
                        if Battle_GetOutgoingDamageMod(BattleChar) > 1.0:
                            CumulativeWeight *= LowerPriorityFactor * 0.8
                        else:
                            CumulativeWeight *= RaisePriorityFactor * 40

                    NewActionWeight += CumulativeWeight
            else:
                NewActionWeight = Action.AIBaseWeight

            # if len(TargetOrTargets) > 1:
            #     TargetName = "All targets"
            # else:
            #     TargetName = TargetOrTargets[0].CharRef['name']

            ActionTargetPairsWeighted.append([ActionTargetPair, NewActionWeight])

        # roll and pick action and target from weight-altered action-target pairs dict
        SelectedAction = None
        TotalWeightSum = sum([ActionWeightPair[1] for ActionWeightPair in ActionTargetPairsWeighted])
        RngValue = RngFloat(0, TotalWeightSum)
        for ActionTargetPairActionWeight in ActionTargetPairsWeighted:
            NewValue = RngValue - ActionTargetPairActionWeight[1]
            if NewValue < ActionTargetPairActionWeight[1]:
                AISelectedAction = ActionTargetPairActionWeight[0][0]
                AIActionTarget = ActionTargetPairActionWeight[0][1][0]
                break
            else:
                RngValue = NewValue

        # UI auto-selection
        if persistent.Battle_AutoSelectActorAndTargetForAI:
            if BattleChar.BattleSide == 0:
                Battle_SelectLeftChar(BattleChar)
                if AIActionTarget.BattleSide != BattleChar.BattleSide:
                    BattleScene.SelectedRight = AIActionTarget
                    Battle_SelectRightChar(AIActionTarget)
            else:
                Battle_SelectRightChar(BattleChar)
                if AIActionTarget.BattleSide != BattleChar.BattleSide:
                    Battle_SelectLeftChar(AIActionTarget)

        # set selected action
        Battle_SetCharAction(BattleChar, AISelectedAction, AIActionTarget)
        return