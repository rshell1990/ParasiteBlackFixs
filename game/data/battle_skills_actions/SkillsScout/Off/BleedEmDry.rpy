init python:
    @RegisterBattleSkill("ScoutBleedEmDry")
    class BattleSkill_ScoutBleedEmDry(BattleSkill):
        DisplayName = _("Bleed Em Dry")
        
        Icon = "images/battle_skill_icons/scout/BleedEmDry.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 60

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
                            StatusEffect = BattleStatusEff_Bleed(
                                self.Owner_BattleChar.Damage, 
                                Duration = 2,
                                SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("A double attack against a single enemy. Each strike deals %s damage and makes the enemy bleed for 2 turn.")) % DamageValue