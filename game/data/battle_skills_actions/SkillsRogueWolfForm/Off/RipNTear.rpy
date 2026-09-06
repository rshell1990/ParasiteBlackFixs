init python:
    @RegisterBattleSkill("RogueWolfRipNTear")
    class BattleSkill_RogueWolfRipNTear(BattleSkill):
        DisplayName = _("Rip and Tear")
        Icon = "images/battle_skill_icons/rogue_wolf/RipNTear.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 40

        DamageValue = {
            1:0.6, 
            2:0.65, 
            3:0.7, 
            4:0.8}
        
        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.HEAL_SELF}

        def Execute(self, Target):
            for i in range(2):
                Battle_ScheduledAttack(
                    SourceSkillObj = self,
                    AttackTarget = Target,
                    DamageMod = self.DamageValue[self.Level],
                    DamageRecoversAttackerHealth = 0.3,
                    Effects_OnHit_Target = [
                        BattleEffect_ApplyStatusOnEnemy(
                            Chance = 0.3,
                            StatusEffect = BattleStatusEff_Bleed(BaseValue = self.Owner_BattleChar.Damage, Duration = 1, SourceName = self.DisplayName))])
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Go for the throat... Launch yourself onto an enemy for a vicious tear attacking twice, dealing %s damage, causing bleeding with a 30%% chance for 1 turn with each attack and recover your hp by 30%% of the damage dealt.")) % DamageValue