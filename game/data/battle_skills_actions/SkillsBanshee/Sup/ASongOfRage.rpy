init python:
    @RegisterBattleSkill("BansheeASongOfRage")
    class BattleSkill_BansheeASongOfRage(BattleSkill):    
        DisplayName = _("A song of rage")

        Icon = "images/battle_skill_icons/banshee/ASongOfRage.webp"

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALL_ALLIES

        Cost_Energy = 80

        ArmorCritBuff = {1:1.3, 2:1.35, 3:1.4}

        def Execute(self, Target):
            AllTargets = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)

            PlayedAnim = Battle_RunCharAnim(self.Owner_BattleChar, "cast")
            Battle_PlayCharSkinSound("Char_UseSkill", self.Owner_BattleChar, Voice = True, Chance = 0.25)

            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["BattleSkill_Defend_Use"]), self.Owner_BattleChar)
            Battle_LoopStep(PlayedAnim.Warmup)

            for Char in AllTargets:
                Multiplier = 0.0
                if (Char.Health / Char.HealthMax) < 0.5:
                    Multiplier = 1.0
                Battle_ApplyStatusEffect(TargetChar = Char,
                                        StatusEffect = BattleStatusEff_StatMod_Armor(
                                            Duration = 2, 
                                            StatMod_Armor = self.ArmorCritBuff[self.Level] + Multiplier * (self.ArmorCritBuff[self.Level] - 1.0), 
                                            StatusEffectID = "banshee_songofrage_armorbuff", 
                                            SourceName = self.DisplayName))
                Battle_ApplyStatusEffect(TargetChar = Char,
                                        StatusEffect = BattleStatusEff_StatMod_CritChance(
                                            Duration = 2, 
                                            StatMod_CritChance = self.ArmorCritBuff[self.Level] + Multiplier * (self.ArmorCritBuff[self.Level] - 1.0), 
                                            StatusEffectID = "banshee_songofrage_critbuff", 
                                            SourceName = self.DisplayName))
            
            Battle_AddLogEntry_Autoformat(
                    USER = self.Owner_BattleChar,
                    SKILL_NAME = self.DisplayName,
                    String = tra(_("USER_NAME uses SKILL_NAME!")))

            Battle_LoopStep(PlayedAnim.Cooldown)

            return

        def GetDesc(self, DescLevel = 1):
            BuffPercentage = Battle_FormatDescVal(round((self.ArmorCritBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("All party members gain %s armor and critical chance buff for 2 turns. Allies with less than 50%% of health have the buff's strength doubled.")) % BuffPercentage