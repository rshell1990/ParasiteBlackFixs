init python:
    @RegisterBattleSkill("ParasiteWhiteParasiteCurse")
    class BattleSkill_ParasiteWhiteParasiteCurse(BattleSkill):
        DisplayName = _("Parasite Curse")

        Icon = "images/battle_skill_icons/parawhite/ParasiteCurse.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 80

        DamageValue = {1:1.4, 2:1.5, 3:1.6, 4:1.7}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.REMOVE_BUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self, 
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                Effects_OnHit_Target = [
                    BattleEffect_RemoveBuffsOnTarget(),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Curse(
                            Duration = 2,
                            SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Attacks all enemies, dealing %s damage and removing all buffs from enemies hit.\nCurses all targets hit for 2 turns. Cursed enemies cannot receive buffs.")) % StrikeDamage
