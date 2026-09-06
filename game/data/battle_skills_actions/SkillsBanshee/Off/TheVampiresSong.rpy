init python:
    @RegisterBattleSkill("BansheeTheVampiresSong")
    class BattleSkill_BansheeVampiresSong(BattleSkill):    
        DisplayName = _("Vampire's song")

        Icon = "images/battle_skill_icons/banshee/TheVampiresSong.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ALL_ENEMIES

        Cost_Energy = 90

        DamageValue = {1:1.4, 2:1.45, 3:1.5, 4:1.6}

        AITags = {AI_TAGS.DEAL_PHYS_DAMAGE, AI_TAGS.HEAL_SELF}

        ShowHitChance = False

        def Execute(self, Target):
            HpRestoredRatio = 0.0
            HpToRestore = 0
            
            
            PlayedAnim = Battle_RunCharAnim(self.Owner_BattleChar, "cast")
            Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["BattleSkill_Defend_Use"]), self.Owner_BattleChar)

            Battle_LoopStep(PlayedAnim.Warmup)

            AllTargets = Battle_GetAllAlliesOfChar(self.Owner_BattleChar) + Battle_GetAllEnemiesOfChar(self.Owner_BattleChar)
            
            for TargetChar in AllTargets:
                if TargetChar.Health > 2:
                    OneTenthInHP = int(TargetChar.Health / 10.0)
                    DmgValue = OneTenthInHP
                else:
                    DmgValue = 1
                
                HpToRestore += DmgValue
                Battle_DealDamage(TargetChar, DmgValue, IgnoreArmor = True)
                Battle_LoopStep(0.1)


            StoredHpValue = self.Owner_BattleChar.Health
            # heal 
            Battle_RestoreHealth(self.Owner_BattleChar, HpToRestore)

            HpRestoredRatio = StoredHpValue / self.Owner_BattleChar.Health

            Battle_ScheduledAttack(
                    GuaranteedHit = True,
                    SourceSkillObj = self,
                    AttackTarget = self.ValidTargets,
                    DamageMod = self.DamageValue[self.Level] + (1 - HpRestoredRatio),
                    Effects_OnHit_Target = [])
            
            Battle_LoopStep(PlayedAnim.Cooldown)

            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                StrikeDamage = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                StrikeDamage = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))
            return tra(_("Drain 10%% of current health of each unit on the battlefield (including allies), then attack all enemies with %s base damage. The damage is increased in proportion to health recovered.")) % StrikeDamage