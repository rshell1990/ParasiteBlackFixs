init python:
    @RegisterBattleSkill("NeutralSmokeBomb")
    class BattleSkill_NeutralSmokeBomb(BattleSkill):
        DisplayName = _("Smoke Bomb")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES
        Cost_Energy = 45

        AITags = {AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            Battle_ScheduledCast(
                SourceSkillObj = self,
                CastTarget = self.ValidTargets,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        Chance = 0.2,
                        StatusEffect = BattleStatusEff_Stun(
                            Duration = 1,
                            SourceName = self.DisplayName))],
                Effects_OnSelf = [
                    BattleEffect_RestoreHealth(
                        RestoreValue = 0.25, 
                        RatioFromMax = True),
                    BattleEffect_ApplyStatusOnAlly(
                        StatusEffect = BattleStatusEff_Immunity(
                            Duration = 1, 
                            SourceName = self.DisplayName))
                ],

                # copied from goblin bomb
                SoundUse_CustomList = ["audio/battle/swordSwing/hSword-01.ogg", "audio/battle/swordSwing/hSword-02.ogg", "audio/battle/swordSwing/hSword-03.ogg", "audio/battle/swordSwing/hSword-04.ogg", "audio/battle/swordSwing/hSword-05.ogg"],
                SoundImpact_OneShotList = ["audio/battle/explosion/explosion1.ogg", "audio/battle/explosion/explosion2.ogg", "audio/battle/explosion/explosion3.ogg"],
                TargetVFXID = self.Owner_BattleChar.BattleSkin.BasicAttackImpactImageID,
            )

            return

        def GetDesc(self, DescLevel = 1):
            return "Create confusion for the player’s party. Has a 20% chance to stun each member of the player's party for 1 round. Also grants immunity to the skill user for 1 round, as well as heals his current HP by 25%. (Cost: 45)"