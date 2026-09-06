init python:
    @RegisterBattleSkill("ParasiteBlackParasiteBalance")
    class BattleSkill_ParasiteBlackParasiteBalance(BattleSkill):
        DisplayName = _("Parasite Balance")
        
        Icon = "images/battle_skill_icons/parablack/ParasiteBalance.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.EVERYONE

        Cost_Energy = 170

        AllyEnergyRecoverValue = {1:0.2, 2:0.25, 3:0.3}
        AIBaseWeight = 1.1

        def Execute(self, Target):
            AllTargets = Battle_GetAliveCharsOnSide(0) + Battle_GetAliveCharsOnSide(1)
            PlayedAnim = Battle_RunCharAnim(self.Owner_BattleChar, "cast")
            Battle_PlayCharSkinSound("Char_UseSkill", self.Owner_BattleChar, Voice = True, Chance = 0.25)
            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["BattleSkill_Defend_Use"]), self.Owner_BattleChar)
            Battle_LoopStep(PlayedAnim.Warmup)

            Battle_AddLogEntry_Autoformat(
                USER = self.Owner_BattleChar,
                SKILL_NAME = self.DisplayName,
                String = tra(_("USER_NAME uses SKILL_NAME!")))

            for BChar in AllTargets:
                BChar.StatusEffects = []
            AllAllies = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)
            AllAllies.remove(self.Owner_BattleChar)
            if len(AllAllies) > 0:
                for BChar in AllAllies:
                    Battle_RestoreEnergy(BChar, round(BChar.EnergyMax * self.AllyEnergyRecoverValue[self.Level]))
                    Battle_GrantExtraTurn(BChar, OnlyIfHasActed = True)

            Battle_LoopStep(PlayedAnim.Cooldown)
            return

        def GetDesc(self, DescLevel = 1):
            EnergyRecoverPerc = Battle_FormatDescVal(round(self.AllyEnergyRecoverValue[DescLevel] * 100), Percentage = True)
            return tra(_("Summons a mystical energy and removes all harmful and beneficial effects from all allies and enemies.\nAll your allies have their energy recovered by %s and recieve an extra turn if they have already acted.")) % EnergyRecoverPerc