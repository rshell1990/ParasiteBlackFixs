init python:
    import math

    def Battle_TryLandStrike(attacker, target, GuaranteedHit = False):
        if GuaranteedHit:
            return True

        hit_prob = Battle_GetHitProb(attacker, target)
        if renpy.random.randint(1, 100) <= hit_prob:
            return True
        else:
            return False

    # used to determine if attack/skill lands. also should display % values in battle
    def Battle_GetHitProb(Attacker, Target):
        OwnAccuracy = Attacker.AttackRating
        EnemyDodge = Target.DodgeRating

        hit_prob = 1 - (0.99 * (1 - math.exp(-0.052 * (EnemyDodge - OwnAccuracy))))
        if int(OwnAccuracy) >= int(EnemyDodge):
            hit_prob = 1.0

        return int(15 + 70 * hit_prob)

    def Battle_GrantExtraTurn(BattleChar, OnlyIfHasActed = False, IgnoreDebuffs = False):
        if not IgnoreDebuffs:
            if Battle_HasStatusEffect(BattleChar, "stun") or Battle_HasStatusEffect(BattleChar, "taunt"):
                return
        if OnlyIfHasActed:
            if BattleChar not in BattleScene.ActiveCharsList:
                BattleScene.ActiveCharsList.append(BattleChar)
        else:
            BattleScene.ActiveCharsList.append(BattleChar)

    # for player-side ui
    def Battle_PlayerScheduleActionOrEnterTargetingMode(BattleChar, ActionInstance):
        TooltipClear()
        ActionTarget = None

        OwnSide = BattleChar.BattleSide
        OpposingSide = (1 if OwnSide == 0 else 0)

        Alive_Allies = Battle_GetAliveCharsOnSide(Side = OwnSide)
        Alive_Enemies = Battle_GetAliveCharsOnSide(Side = OpposingSide)
        Alive_Other_Allies = [c for c in Alive_Allies if c != ActionInstance.Owner_BattleChar]

        if ActionInstance.ValidTargets == BATTLE_TARGETS.SELF:
            ActionTarget = ActionInstance.Owner_BattleChar

        elif ActionInstance.ValidTargets == BATTLE_TARGETS.ANY_ALLY:
            if len(Alive_Allies) == 1:
                ActionTarget = ActionInstance.Owner_BattleChar

        elif ActionInstance.ValidTargets == BATTLE_TARGETS.ALLY_NOT_SELF:
            if len(Alive_Other_Allies) == 1:
                ActionTarget = Alive_Other_Allies[0]

        elif ActionInstance.ValidTargets == BATTLE_TARGETS.ANY_ENEMY:
            if len(Alive_Enemies) == 1:
                ActionTarget = Alive_Enemies[0]

        elif ActionInstance.ValidTargets == BATTLE_TARGETS.ALL_ENEMIES:
            if Alive_Enemies:
                ActionTarget = Alive_Enemies[0]

        elif ActionInstance.ValidTargets in (BATTLE_TARGETS.ALL_ALLIES, BATTLE_TARGETS.EVERYONE):
            if Alive_Allies:
                ActionTarget = Alive_Allies[0]

        elif ActionInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF:
            if Alive_Other_Allies:
                ActionTarget = Alive_Other_Allies[0]

        if ActionTarget is not None:
            Battle_SetCharAction(BattleChar, ActionInstance, ActionTarget)
        else:
            BattleScene.ActionAwaitingTarget = ActionInstance
            BattleScene.ActionAwaitingTarget_PotentialTargetsList = Battle_GetAllTargetsList(ActionInstance)

    def Battle_SetCharAction(BattleChar, ActionInstance, Target):
        if getattr(ActionInstance, "SpendTurn", True):
            if BattleChar in BattleScene.ActiveCharsList:
                BattleScene.ActiveCharsList.remove(BattleChar)
            
            if getattr(ActionInstance, "AutoSelectNextInPartyOnExecute", False):
                if BattleChar.BattleSide == 0 and len(BattleScene.ActiveCharsList) > 0:
                    Battle_SelectLeftChar(BattleScene.ActiveCharsList[0])

        BattleScene.SelectedActionToProcess = ScheduledAction(ActionInstance, Target)

    def Battle_GetAllTargetsList(SkillInstance):    
        OwnSide = SkillInstance.Owner_BattleChar.BattleSide
        OpposingSide = (0 if OwnSide == 1 else 1)

        if SkillInstance.ValidTargets == BATTLE_TARGETS.SELF:
            return [SkillInstance.Owner_BattleChar]
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ANY_ALLY:
            return Battle_GetAliveCharsOnSide(OwnSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALLY_NOT_SELF:
            return [BattleChar for BattleChar in BattleScene.BattleChars[OwnSide] if BattleChar != SkillInstance.Owner_BattleChar and getattr(BattleChar, "IsAlive", True)]
        elif SkillInstance.ValidTargets in (BATTLE_TARGETS.ANY_ENEMY, BATTLE_TARGETS.ALL_ENEMIES):
            return Battle_GetAliveCharsOnSide(OpposingSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES:
            return Battle_GetAliveCharsOnSide(OwnSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF:
            return [BattleChar for BattleChar in BattleScene.BattleChars[OwnSide] if BattleChar != SkillInstance.Owner_BattleChar and getattr(BattleChar, "IsAlive", True)]
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.EVERYONE:
            return Battle_GetAliveCharsOnSide(OpposingSide) + Battle_GetAliveCharsOnSide(OwnSide)
        return []

    def Battle_ClearActionAwaitingTarget():
        BattleScene.ActionAwaitingTarget = None
        BattleScene.ActionAwaitingTarget_PotentialTargetsList = []

    def Battle_CanExecuteItemAction(ActionInstance):
        return ActionInstance.CanExecute()

    def Battle_ProcessTargetList(UserBattleChar, AttackTarget):
        if AttackTarget == BATTLE_TARGETS.SELF:
            return [UserBattleChar]
        elif AttackTarget == BATTLE_TARGETS.ALL_ALLIES:
            return [BattleChar for BattleChar in BattleScene.BattleChars[UserBattleChar.BattleSide]]
        elif AttackTarget == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF:
            return [BattleChar for BattleChar in BattleScene.BattleChars[UserBattleChar.BattleSide] if BattleChar != UserBattleChar]
        elif AttackTarget == BATTLE_TARGETS.EVERYONE:
            return BattleScene.BattleChars[0] + BattleScene.BattleChars[1]
        elif AttackTarget == BATTLE_TARGETS.ALL_ENEMIES:
            OpposingSide = (0 if UserBattleChar.BattleSide == 1 else 1)
            return [BattleChar for BattleChar in BattleScene.BattleChars[OpposingSide]]
        elif isinstance(AttackTarget, list):
            return AttackTarget
        else:
            return [AttackTarget]