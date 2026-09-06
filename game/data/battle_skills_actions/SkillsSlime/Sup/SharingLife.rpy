init python:
    @RegisterBattleSkill("SlimeSharingLife")
    class BattleSkill_SlimeSharingLife(BattleSkill):
        DisplayName = _("Sharing Life")
        Icon = "images/battle_skill_icons/slime/SharingLife.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 100
        HealPerc = {1:0.2, 2:0.25, 3:0.3}

        AITags = {AI_TAGS.HEAL_TARGET, AI_TAGS.FAVOURED_HIGH_OWN_HP_RATIO}

        def Execute(self, Target):
            PlayedAnim = Battle_RunCharAnim(self.Owner_BattleChar, "cast")

            Battle_PlayCharSkinSound("Char_UseSkill", self.Owner_BattleChar, Voice = True, Chance = 0.25)
            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["BattleSkill_Defend_Use"]), self.Owner_BattleChar)

            Battle_LoopStep(PlayedAnim.Warmup)

            Allies = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)
            SumOfAllAlliedHp = 0
            SumOfAllAlliedHpMax = 0
            for AllyChar in Allies:
                SumOfAllAlliedHp += AllyChar.Health
                SumOfAllAlliedHpMax += AllyChar.HealthMax
            
            HpRatioForAllChars = SumOfAllAlliedHp / SumOfAllAlliedHpMax

            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                SUM_OF_ALLIED_HP = SumOfAllAlliedHp,
                SKILL_NAME = self.DisplayName,
                String = tra(_("USER_NAME uses SKILL_NAME, collecting SUM_OF_ALLIED_HP health points and sharing them across her team!")))

            # hit here
            for AllyChar in Allies:
                AllyChar.Health = round(AllyChar.HealthMax * HpRatioForAllChars)
                if AllyChar.Health < AllyChar.HealthMax:
                    Battle_RestoreHealth(AllyChar, round(Battle_GetHealthRecoveryMod(AllyChar) * self.HealPerc[self.Level] * AllyChar.HealthMax), IgnoreRecoveryMod = True)

            Battle_LoopStep(PlayedAnim.Cooldown)
            return

        def GetDesc(self, DescLevel = 1):
            HealPerc = Battle_FormatDescVal(round(self.HealPerc[DescLevel] * 100), Percentage = True)
            return tra(_("Balances the hp of all allies and heals the hp of all allies by %s of your max hp.")) % HealPerc
