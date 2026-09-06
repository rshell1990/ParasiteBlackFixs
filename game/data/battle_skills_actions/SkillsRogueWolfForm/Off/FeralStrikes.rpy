init python:
    @RegisterBattleSkill("RogueWolfFeralStrikes")
    class BattleSkill_RogueWolfFeralStrikes(BattleSkill):
        DisplayName = _("Feral Strikes")
        Icon = "images/battle_skill_icons/rogue_wolf/FeralStrikes.webp"

        Level_Max = 5
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 70

        DamageValue = {
            1:1.5,
            2:1.6,
            3:1.6,
            4:1.7,
            5:1.7}
        ArmorDebuff = {
            1:0.6,
            2:0.6,
            3:0.5,
            4:0.5,
            5:0.4}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE}

        def Execute(self, Target):
            Battle_ScheduledAttack(
                SourceSkillObj = self,
                AttackTarget = self.ValidTargets,
                DamageMod = self.DamageValue[self.Level],
                CustomImpactVfxID = "Battle_VfxImpactSlashUppercut",
                Effects_OnHit_Target = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = self.ArmorDebuff[self.Level], StatusEffectID = "wolf_feralstrikes_armordebuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_Bleed(BaseValue = self.Owner_BattleChar.Damage, Duration = 1, SourceName = self.DisplayName))])                    
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            ArmorDebuffPerc = Battle_FormatDescVal(round((1.0 - self.ArmorDebuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Slash, bite and claw at everyone in your way! Attacks all enemies, dealing %s damage, reducing the hit enemies' armor by %s for 2 turns and making them bleed for 1 turn.")) % (DamageValue, ArmorDebuffPerc)