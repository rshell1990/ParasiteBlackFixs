init python:
    @RegisterBattleSkill("BansheeASongOfPain")
    class BattleSkill_BansheeASongOfPain(BattleSkill):
        DisplayName = _("A song of pain")

        Icon = "images/battle_skill_icons/banshee/ASongOfPain.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 80

        DamageValue = {1: 0.9, 2:0.95, 3:1.0, 4:1.05}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.EFFECT_SCALES_WITH_AMOUNT_OF_DEBUFFS_ON_TARGET}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                DamageMod_DoubleIfTargetHasAtleastOneDebuff = True)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
                DoubledStrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel] * 2))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
                DoubledStrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel] * 2))
            return tra(_("Unleash an ear shattering cry, causing %s damage that is doubled (%s) if the enemy has one or more harmful effects.")) % (StrikeDamage, DoubledStrikeDamage)