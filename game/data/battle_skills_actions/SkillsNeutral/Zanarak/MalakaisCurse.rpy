init python:
    @RegisterBattleSkill("ZanarakMalakaisCurse")
    class BattleSkill_ZanarakMalakaisCurse(BattleSkill):
        DisplayName = _("Malakai's Curse")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 80

        ShowHitChance = False

        AITags = {AI_TAGS.REMOVE_BUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_RemoveBuffsOnTarget(),
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_Burn(self.Owner_BattleChar.Damage, Duration = 2, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_Poison(self.Owner_BattleChar.Damage, Duration = 2, SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_DamageOut(DamageDealt_Mod = 0.6, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "zanarak_malakaicurse_dmgoutdebuff")),
                    BattleEffect_ApplyStatusOnEnemy(StatusEffect = BattleStatusEff_StatMod_Dodge(StatMod_DodgeRating = 0.6, Duration = 2, SourceName = self.DisplayName, StatusEffectID = "zanarak_malakaicurse_dodgedebuff"))
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Remove all beneficial effects of the enemy team inflict 1 poison and 1 burning on them for 2 rounds. Debuffs both dmg and dodge by 40% for 2 rounds."