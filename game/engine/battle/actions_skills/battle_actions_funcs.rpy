init python:
    def Battle_GetAllTargetsList(ActionInstance):
        Owner = ActionInstance.Owner_BattleChar
        
        # Check if the action specifically targets dead/fallen allies
        if getattr(ActionInstance, "AllowDeadTargets", False):
            # Target dead allies on the owner's side
            return [Char for Char in BattleScene.BattleChars[Owner.BattleSide] if not Char.IsAlive]
        
        # Standard targeting logic for living allies/enemies
        if ActionInstance.ValidTargets == BATTLE_TARGETS.ANY_ALLY:
            return Battle_GetAllAlliesOfChar(Owner)
        elif ActionInstance.ValidTargets == BATTLE_TARGETS.ANY_ENEMY:
            return Battle_GetAllEnemiesOfChar(Owner)
        else:
            return Battle_GetAliveCharsOnSide(Owner.BattleSide)

    def Battle_TryLandStrike(attacker, target, GuaranteedHit = False):
        if GuaranteedHit == True:
            return True

        hit_prob = Battle_GetHitProb(attacker, target)
        if random.randint(1, 100) <= hit_prob:
            return True
        else:
            return False

    # used to determine if attack/skill lands. also should display % values in battle
    def Battle_GetHitProb(Attacker, Target):
        OwnAccuracy = Attacker.AttackRating
        EnemyDodge = Target.DodgeRating

        hit_prob = 1 - (0.99 * (1 - math.exp(-0.052 * ( EnemyDodge - OwnAccuracy ))))
        if int( OwnAccuracy ) >= int( EnemyDodge ):
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
        return

    # for player-side ui
    def Battle_PlayerScheduleActionOrEnterTargetingMode(BattleChar, ActionInstance):
        TooltipClear()
        ActionTarget = None

        OwnSide = BattleChar.BattleSide
        
        # Fetch potential targets (respects AllowDeadTargets)
        PotentialTargets = Battle_GetAllTargetsList(ActionInstance)

        if ActionInstance.ValidTargets == BATTLE_TARGETS.SELF:
            ActionTarget = ActionInstance.Owner_BattleChar
        elif ActionInstance.ValidTargets in [BATTLE_TARGETS.ANY_ALLY, BATTLE_TARGETS.ALLY_NOT_SELF, BATTLE_TARGETS.ANY_ENEMY]:
            if len(PotentialTargets) == 1:
                ActionTarget = PotentialTargets[0]
        elif ActionInstance.ValidTargets in [BATTLE_TARGETS.ALL_ENEMIES, BATTLE_TARGETS.ALL_ALLIES, BATTLE_TARGETS.EVERYONE, BATTLE_TARGETS.ALL_ALLIES_NOT_SELF]:
            if len(PotentialTargets) > 0:
                ActionTarget = PotentialTargets[0]

        if ActionTarget is not None:
            Battle_SetCharAction(BattleChar, ActionInstance, ActionTarget)
        else:
            BattleScene.ActionAwaitingTarget = ActionInstance
            BattleScene.ActionAwaitingTarget_PotentialTargetsList = PotentialTargets
        return

        Alive_Allies = Battle_GetAliveCharsOnSide(Side = (0 if OwnSide == 0 else 1))
        Alive_Enemies = Battle_GetAliveCharsOnSide(Side = (1 if OwnSide == 0 else 0))

        if ActionInstance.ValidTargets == BATTLE_TARGETS.SELF:
            ActionTarget = ActionInstance.Owner_BattleChar

        if ActionInstance.ValidTargets == BATTLE_TARGETS.ANY_ALLY:
            if len(Alive_Allies) == 1:
                ActionTarget = ActionInstance.Owner_BattleChar

        if ActionInstance.ValidTargets == BATTLE_TARGETS.ALLY_NOT_SELF:
            if len(Alive_Allies) == 2:
                for OtherBattleChar in Alive_Allies:
                    if OtherBattleChar != ActionInstance.Owner_BattleChar:
                        ActionTarget = OtherBattleChar

        if ActionInstance.ValidTargets == BATTLE_TARGETS.ANY_ENEMY:
            if len(Alive_Enemies) == 1:
                ActionTarget = Alive_Enemies[0]

        # this will always pick same enemy bc ALL_ENEMIES is supposed to ignore skill-specific target
        if ActionInstance.ValidTargets == BATTLE_TARGETS.ALL_ENEMIES:
            ActionTarget = Alive_Enemies[0]
        # same as above, this will always pick same ally bc ALL_ALLIES is supposed to ignore skill-specific target
        if ActionInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES:
            ActionTarget = Alive_Allies[0]
        # same as above
        if ActionInstance.ValidTargets == BATTLE_TARGETS.EVERYONE:
            ActionTarget = Alive_Allies[0]
        if ActionInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF:
            ActionTarget = Alive_Allies[0]

        if ActionTarget is not None:
            Battle_SetCharAction(BattleChar, ActionInstance, ActionTarget)
        else:
            BattleScene.ActionAwaitingTarget = ActionInstance
            BattleScene.ActionAwaitingTarget_PotentialTargetsList = Battle_GetAllTargetsList(ActionInstance)
        return

    def Battle_SetCharAction(BattleChar, ActionInstance, Target):
        if getattr(ActionInstance, "SpendTurn", True) == True:
            BattleScene.ActiveCharsList.remove(BattleChar)
            if ActionInstance.AutoSelectNextInPartyOnExecute == True:
                if BattleChar.BattleSide == 0:
                    if len(BattleScene.ActiveCharsList) > 0:
                        Battle_SelectLeftChar(BattleScene.ActiveCharsList[0])
        BattleScene.SelectedActionToProcess = ScheduledAction(ActionInstance, Target)
        return

    def Battle_GetAllTargetsList(SkillInstance):    
        OwnSide = SkillInstance.Owner_BattleChar.BattleSide
        OpposingSide = (0 if OwnSide == 1 else 1)
        # Handle revival / dead target actions
        if getattr(SkillInstance, "AllowDeadTargets", False):
            return [Char for Char in BattleScene.BattleChars[OwnSide] if not Char.IsAlive]

        if SkillInstance.ValidTargets == BATTLE_TARGETS.SELF:
            return [SkillInstance.Owner_BattleChar]
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ANY_ALLY:
            return Battle_GetAliveCharsOnSide(OwnSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALLY_NOT_SELF:
            return [BattleChar for BattleChar in BattleScene.BattleChars[OwnSide] if BattleChar != SkillInstance.Owner_BattleChar and BattleChar.IsAlive]
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ANY_ENEMY:
            return Battle_GetAliveCharsOnSide(OpposingSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALL_ENEMIES:
            return Battle_GetAliveCharsOnSide(OpposingSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES:
            return Battle_GetAliveCharsOnSide(OwnSide)
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF:
            return [BattleChar for BattleChar in BattleScene.BattleChars[OwnSide] if BattleChar != SkillInstance.Owner_BattleChar and BattleChar.IsAlive]
        elif SkillInstance.ValidTargets == BATTLE_TARGETS.EVERYONE:
            return Battle_GetAliveCharsOnSide(OpposingSide) + Battle_GetAliveCharsOnSide(OwnSide)
        return []

    def Battle_ClearActionAwaitingTarget():
        BattleScene.ActionAwaitingTarget = None
        BattleScene.ActionAwaitingTarget_PotentialTargetsList = []
        return

    def Battle_CanExecuteItemAction(ActionInstance):
        return ActionInstance.CanExecute()

    def Battle_ProcessTargetList(UserBattleChar, AttackTarget):
        if AttackTarget == BATTLE_TARGETS.SELF:
            return [UserBattleChar]
        elif AttackTarget == BATTLE_TARGETS.ALL_ALLIES:
            return [BattleChar for BattleChar in BattleScene.BattleChars[UserBattleChar.BattleSide]]
        elif AttackTarget == BATTLE_TARGETS.ALL_ALLIES_NOT_SELF:
            TargetList = [BattleChar for BattleChar in BattleScene.BattleChars[UserBattleChar.BattleSide]]
            TargetList.remove(UserBattleChar)
            return TargetList
        elif AttackTarget == BATTLE_TARGETS.EVERYONE:
            return BattleScene.BattleChars[0] + BattleScene.BattleChars[1]
        elif AttackTarget == BATTLE_TARGETS.ALL_ENEMIES:
            OpposingSide = (0 if UserBattleChar.BattleSide == 1 else 1)
            return [BattleChar for BattleChar in BattleScene.BattleChars[OpposingSide]]
        elif isinstance(AttackTarget, list):
            return AttackTarget
        else:
            return [AttackTarget]