init python:
    @RegisterBattleSkill("ScoutEaglesEye")
    class BattleSkill_ScoutEaglesEye(BattleSkill):
        DisplayName = _("Eagle's Eye")
        
        Icon = "images/battle_skill_icons/scout/EaglesEye.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.ANY_ENEMY

        Cost_Energy = 100

        AccDamageBuff = {1:1.2, 2:1.3, 3:1.4, 4:1.5}

        ShowHitChance = False

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = [
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_DamageIn(Duration = 2, DamageRecieved_Mod = 1.5, SourceName = self.DisplayName, StatusEffectID = "scout_eagleeye_dmgin_debuff")),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Armor(Duration = 2, StatMod_Armor = 0.5, StatusEffectID = "scout_eagleeye_armor_debuff", SourceName = self.DisplayName)),
                    BattleEffect_ApplyStatusOnEnemy(
                        StatusEffect = BattleStatusEff_StatMod_Dodge(Duration = 2, StatMod_DodgeRating = 0.5, StatusEffectID = "scout_eagleeye_dodge_debuff", SourceName = self.DisplayName))])
            # ally effs
            for Char in Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide):
                Battle_ApplyStatusEffect(
                    TargetChar = Char, 
                    StatusEffect = BattleStatusEff_DamageOut(
                        DamageDealt_Mod = self.AccDamageBuff[self.Level], 
                        Duration = 2, 
                        SourceName = self.DisplayName, 
                        StatusEffectID = "scout_eagleeye_dmgoutbuff"))
                Battle_ApplyStatusEffect(
                    TargetChar = Char, 
                    StatusEffect = BattleStatusEff_StatMod_Accuracy(
                        Duration = 2, 
                        StatMod_AttackRating = self.AccDamageBuff[self.Level], 
                        StatusEffectID = "scout_eagleeye_accbuff", 
                        SourceName = self.DisplayName))
            return

        def GetDesc(self, DescLevel = 1):
            AllyAccDmgBuff = Battle_FormatDescVal(round((self.AccDamageBuff[DescLevel] - 1.0) * 100), Percentage = True)
            return tra(_("Reveals the target enemy's weak point: increases the damage they take, decreases their chance to dodge and their armor by 50%% for 2 turns. Increases all allies' accuracy and damage dealt by %s for 2 turns.")) % AllyAccDmgBuff