init python:
    @RegisterBattleSkill("NeutralAncientCurse")
    class BattleSkill_NeutralAncientCurse(BattleSkill):
        DisplayName = _("Ancient Curse")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 60

        DamageValue = {1:0.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        AIBaseWeight = 3.0

        def Execute(self, Target):
            # reduce armor by 70% with 0.8
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.8,
                        StatusEffect = BattleStatusEff_StatMod_Armor(
                            Duration = 2, 
                            StatMod_Armor = 0.3, 
                            StatusEffectID = "neutral_ancientcurse_armordebuff", 
                            SourceName = self.DisplayName))])
            # reduce accuracy by 70% with 0.8
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.8,
                        StatusEffect = BattleStatusEff_StatMod_Accuracy(
                            Duration = 2, 
                            StatMod_AttackRating = 0.3, 
                            StatusEffectID = "neutral_ancientcurse_accdebuff", 
                            SourceName = self.DisplayName))])
            # reduce health/en recovery by 100% with 0.8
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.8,
                        StatusEffect = BattleStatusEff_HealthRecoveryMod(
                            ResRecoverMod_Health = 0.0,
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "neutral_ancientcurse_hp_recover_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.8,
                        StatusEffect = BattleStatusEff_EnergyRecoveryMod(
                            ResRecoverMod_Energy = 0.0,
                            Duration = 2, 
                            SourceName = self.DisplayName,
                            StatusEffectID = "neutral_ancientcurse_ep_recover_debuff"))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Attacks all enemies 3 times with each blow dealing %s damage and having an 80%% chance of granting a harmful effect. The first attack reduces the enemy's armour by 70%%, the second attack reduces the enemy's accuracy by 70%% and the third attack reduces the enemy's health and energy recovery by 100%% for 2 turns.")) % DamageValue