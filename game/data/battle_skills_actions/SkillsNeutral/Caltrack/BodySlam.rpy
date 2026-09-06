init python:
    @RegisterBattleSkill("NeutralBodySlam")
    class BattleSkill_NeutralBodySlam(BattleSkill):
        DisplayName = _("Body Slam")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 80

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.REMOVE_BUFFS_ON_TARGET, AI_TAGS.FAVOURED_LOWER_TARGET_HP_RATIO}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = 1.5,
                Effects_OnHit_Target = [
                    BattleEffect_RemoveBuffsOnTarget(),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1, 
                            SourceName = self.DisplayName),
                        IfHealthBelowOrEq = 0.5,
                    ),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(
                            Duration = 2, 
                            StatMod_DodgeRating = 0.4, 
                            StatusEffectID = "body_slam_dodge_mod", 
                            SourceName = self.DisplayName), 
                        IfHealthBelowOrEq = 0.5,
                    ),
                ]
            )
            return

        def GetDesc(self, DescLevel = 1):
            return "Attacks all enemies, all enemies hit removes all beneficial effects. (150% damage) (Cost: 80) enemies below 50% health are stunned for 1 turn and decreasing their dodge chance by 60% for 2 turns"