init python:
    @RegisterBattleSkill("ScoutDanceOfDeath")
    class BattleSkill_ScoutDanceOfDeath(BattleSkill):
        DisplayName = _("Dance Of Death")
        
        Icon = "images/battle_skill_icons/scout/DanceOfDeath.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 90

        DamageValue = {1:0.4, 2:0.44, 3:0.48, 4:0.53}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            for i in range(4):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = 0.5,
                            StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = 0.3, StatusEffectID = "scout_dod_armordebuff", SourceName = self.DisplayName))],
                    Effects_OnCrit_User = [
                        BattleEffect_RestoreEnergy(RestoreValue = 20)])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks the enemy 4 times to reduce their armor by 70%% for 2 turns with a 50%% chance on each attack. Each attack deals %s damage and recovers 20 energy on a critical hit.")) % StrikeDamage