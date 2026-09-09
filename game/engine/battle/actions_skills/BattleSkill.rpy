init -1 python:
    class BattleSkill:
        Owner_PBCharID      = None
        Owner_BattleChar    = None

        Level = 1
        Level_Max = 1

        DisplayName = ""
        Icon = "images/battle_skill_icons/no_icon.webp"

        SpendTurn = True
        AutoSelectNextInPartyOnExecute = True
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 0
        Cost_Mana = 0
        Cost_Infection = 0         # mc only
        Cost_PercHealthCurr = 0.0  # % of current hp, 0.5 == 50%
        Cost_PercHealthMax = 0.0   # % of max hp

        OncePerTurn = True
        UsedThisTurn = False

        AITags = set()
        AIBaseWeight = 1.0

        ShowHitChance = True       # for 100% hit stuff, disable this

        def __init__(self, Owner_BattleChar = None, Owner_PBCharID = None, ToLevel = 1):
            Assert(Owner_BattleChar != None or Owner_PBCharID != None, "Skill  must have either pbchar or battle char owner")
            self.Owner_PBCharID = Owner_PBCharID
            self.Owner_BattleChar = Owner_BattleChar
            self.Level = ToLevel
            return

        def OwnerCharCanPaySkillCost(self):
            # energy cost
            if self.Cost_Energy > 0:
                if self.Owner_BattleChar.Energy < self.Cost_Energy:
                    return False

            # mana cost
            if self.Cost_Mana > 0:
                if self.Owner_BattleChar.Mana < self.Cost_Mana:
                    return False

            # current hp % cost
            if self.Cost_PercHealthCurr:
                if self.Owner_BattleChar.Health <= 1:
                    return False

            # max hp % cost
            if self.Cost_PercHealthMax:
                IntHpCostValue = int(self.Owner_BattleChar.HealthMax * self.Cost_PercHealthMax)
                if (self.Owner_BattleChar.Health + 1) < IntHpCostValue:
                    return False

            # infection cost
            if self.Cost_Infection > 0:
                # only test for player-controlled mc
                if self.Owner_BattleChar.BattleSide == 0:
                    if (InfectionModule().MaxValue - InfectionModule().CurrentValue) <= self.Cost_Infection:
                        return False

            return True

        # extra test to check if skill can be executed
        def CanExecute(self):
            if self.OncePerTurn and self.UsedThisTurn:
                return False
            return True

        # fires right before execution to drain resources
        def DrainCosts(self):
            if self.Cost_Energy > 0:
                self.Owner_BattleChar.Energy -= self.Cost_Energy
            if self.Cost_Mana > 0:
                self.Owner_BattleChar.Mana -= self.Cost_Mana
            if self.Cost_Infection > 0:
                if self.Owner_BattleChar.BattleSide == 0:
                    InfectionModule().CurrentValue += self.Cost_Infection
            if self.Cost_PercHealthCurr > 0.0:
                self.Owner_BattleChar.Health = ClampValue(int(self.Owner_BattleChar.Health * (1.0 - self.Cost_PercHealthCurr)), 1, self.Owner_BattleChar.HealthMax)
            if self.Cost_PercHealthMax > 0.0:
                self.Owner_BattleChar.Health = ClampValue(self.Owner_BattleChar.Health - int(self.Owner_BattleChar.HealthMax * self.Cost_PercHealthMax), 1, self.Owner_BattleChar.HealthMax)
            return

        # actual logic
        def Execute(self, Target):
            return

        # description text
        def GetDesc(self, DescLevel = 1):
            return "No desc"

    # for ui
    def Battle_GetUnmetCostAsString(SkillObj):
        ResultStrings = []
        # energy cost
        if SkillObj.Cost_Energy > 0:
            if SkillObj.Owner_BattleChar.Energy < SkillObj.Cost_Energy:
                ResultStrings.append(tra(_("Not enough energy!")))

        # mana cost
        if SkillObj.Cost_Mana > 0:
            if SkillObj.Owner_BattleChar.Mana < SkillObj.Cost_Mana:
                ResultStrings.append(tra(_("Not enough mana!")))

        # current hp % cost
        if SkillObj.Cost_PercHealthCurr:
            if SkillObj.Owner_BattleChar.Health <= 1:
                ResultStrings.append(tra(_("Not enough health!")))

        # max hp % cost
        if SkillObj.Cost_PercHealthMax:
            IntHpCostValue = int(SkillObj.Owner_BattleChar.HealthMax * SkillObj.Cost_PercHealthMax)
            if (SkillObj.Owner_BattleChar.Health + 1) < IntHpCostValue:
                ResultStrings.append(tra(_("Not enough health!")))

        # infection cost
        if SkillObj.Cost_Infection > 0:
            # only test for player-controlled mc
            if SkillObj.Owner_BattleChar.BattleSide == 0:
                if (InfectionModule().MaxValue - InfectionModule().CurrentValue) <= SkillObj.Cost_Infection:
                    ResultStrings.append(tra(_("Cannot afford the infection hit!")))

        for Index, String in enumerate(ResultStrings):
            ResultStrings[Index] = "{size=+6}{color=[BATTLE_COLORS.REQ_MISSING]}" + String + "{/color}{/size}\n"

        return "".join(ResultStrings)

    class BattleSkill_ChargedStrike(BattleSkill):
        def __init__(self, Owner_BattleChar=None, Owner_PBCharID=None, ToLevel=1):
            super(BattleSkill_ChargedStrike, self).__init__(Owner_BattleChar, Owner_PBCharID, ToLevel)
            
            self.DisplayName = _("Power Surge")
            self.Icon = "images/battle_skill_icons/charged_strike.webp"
            self.Cost_Energy = 20
            self.ValidTargets = BATTLE_TARGETS.ANY_ENEMY
            self.OncePerTurn = True

        def Execute(self, Target):
            actor = self.Owner_BattleChar
            charge_effect = Battle_GetStatusEffect(actor, "status_charging_strike")

            if charge_effect is None:
                ##### PHASE 1: START CHARGE
                ##### Attach status effect to track charge state until next turn
                new_status = BattleStatusEffect_Charging(actor, Target, self)
                actor.StatusEffects.append(new_status)

                ##### Visuals & Audio
                Battle_RunCharAnim(actor, "charge_pose")
                Battle_ShowChargeVFX(actor)
                Battle_AddLogEntry(_("{color=#FFFF00}%s begins gathering power!{/color}") % actor.DisplayName)[cite: 1]

            else:
                ########RELEASE ATTACK
                #######Remove VFX and status effect
                Battle_HideChargeVFX(actor)[cite: 1]
                actor.StatusEffects.remove(charge_effect)

                # Queue the attack action for damage processing
                release_action = BattleAction_ChargedRelease(
                    UserBattleChar=actor,
                    TargetList=[Target],
                    BaseDamage=int(actor.Attack * 2.5) # 250% damage
                )
                Battle_ScheduleAttack(release_action)[cite: 1]

        def GetDesc(self, DescLevel=1):
            return _("Gather energy for 1 turn, then unleash a powerful blow for 250% damage.")

#####################STATUS EFFECT TO TRACK CHARGING
    class BattleStatusEffect_Charging(object):
        def __init__(self, UserChar, TargetChar, SkillRef):
            self.ID = "status_charging_strike"
            self.DisplayName = _("Charging")
            self.IsPermanent = False
            self.Duration = 1
            self.UserChar = UserChar
            self.TargetChar = TargetChar
            self.SkillRef = SkillRef

        def OnTurnStart(self):
            # Auto-triggers Phase 2 on character's next turn
            if self.TargetChar and getattr(self.TargetChar, "IsAlive", True):
                self.SkillRef.Execute(self.TargetChar)
            else:
                # Retarget to another living enemy if original target died
                actor = self.SkillRef.Owner_BattleChar
                alive_enemies = Battle_GetAliveCharsOnSide(1 if actor.BattleSide == 0 else 0)
                if alive_enemies:
                    self.SkillRef.Execute(alive_enemies[0])
                else:
                    Battle_HideChargeVFX(actor)
                    actor.StatusEffects.remove(self)

        def TickDuration(self, AtEnd=False):
            pass


    # -------------------------------------------------------------------------
    # 3. SCHEDULED ATTACK ACTION
    # -------------------------------------------------------------------------
    class BattleAction_ChargedRelease(object):
        def __init__(self, UserBattleChar, TargetList, BaseDamage):
            self.UserBattleChar = UserBattleChar
            self.TargetList = TargetList
            self.BaseDamage = BaseDamage
            self.IsChargedAttackRelease = True  # Triggers release VFX in loop[cite: 1]
            self.AllowDeadTargets = False[cite: 1]

        def ExecuteAction(self):
            target = self.TargetList[0]
            actor = self.UserBattleChar

            # Animations & Impact VFX
            Battle_RunCharAnim(actor, "attack")[cite: 1]
            Battle_PlayReleaseChargeVFX(actor, target)[cite: 1]

            # Calculate and apply damage
            damage_dealt = max(int(self.BaseDamage - getattr(target, "Defense", 0)), 1)
            target.Health = max(target.Health - damage_dealt, 0)

            if target.Health == 0:
                target.IsAlive = False[cite: 1]
                Battle_RunCharAnim(target, "defeat")

            Battle_AddLogEntry(_("{color=#FF0000}%s unleashes Power Surge on %s for %d damage!{/color}") 
                               % (actor.DisplayName, target.DisplayName, damage_dealt))