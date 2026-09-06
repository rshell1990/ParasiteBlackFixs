init python:
    @RegisterBattleSkill("InquisitorBurningJudgement")
    class BattleSkill_InquisitorBurningJudgement(BattleSkill):    
        DisplayName = _("Burning Judgement")

        Icon = "images/battle_skill_icons/inquisitor/BurningJudgement.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue = {1:0.6, 2:0.65, 3:0.7, 4:0.75}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            for i in range(2):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = self.DamageValue[self.Level],
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = 0.7,
                            StatusEffect = BattleStatusEff_Burn(BaseValue = self.Owner_BattleChar.Damage, Duration = 2, SourceName = self.DisplayName)),
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = 0.7,
                            StatusEffect = BattleStatusEff_Curse(Duration = 1, SourceName = self.DisplayName))
                    ])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Slash multiple times at the enemy dealing %s damage, each strike having a 70%% chance to curse for 1 turn and inflict 1 burning debuff on the enemy for 2 turns.(Cursed units cannot receive beneficial effects)")) % StrikeDamage