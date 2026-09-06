init python:
    @RegisterBattleSkill("BansheeASongOfDeath")
    class BattleSkill_BansheeASongOfDeath(BattleSkill):    
        DisplayName = _("A song of death")

        Icon = "images/battle_skill_icons/banshee/ASongOfDeath.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 50

        DamageValue = {1:1.3, 2:1.4, 3:1.5}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = Target,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_Burn(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = 3, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_Poison(
                            BaseValue = self.Owner_BattleChar.Damage,
                            Duration = 3, 
                            SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.5,
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1, 
                            SourceName = self.DisplayName))
                    ])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Target a single enemy, dealing %s damage with a 50%% chance of triggering 3 turns of burn, 3 turns of poison and 1 turn of stun.")) % StrikeDamage