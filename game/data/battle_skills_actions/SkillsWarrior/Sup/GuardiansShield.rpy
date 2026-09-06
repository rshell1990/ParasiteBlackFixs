init python:
    @RegisterBattleSkill("WarriorGuardiansShield")
    class BattleSkill_WarriorGuardiansShield(BattleSkill):
        DisplayName = _("Guardians Shield")
        Icon = "images/battle_skill_icons/warrior/GuardiansShield.webp"
        

        Level_Max = 3
        ValidTargets = BATTLE_TARGETS.ALLY_NOT_SELF

        Cost_Energy = 40
        DamageResBuff = {1:0.8, 2:0.7, 3:0.6}
        AutoSelectNextInPartyOnExecute = False

        AITags = {AI_TAGS.HEAL_TARGET, AI_TAGS.REMOVE_DEBUFFS_ON_TARGET, AI_TAGS.RAISE_OWN_PHYS_DAMAGE_RESISTANCE}

        def Execute(self, Target):
            Battle_ScheduledCast( 
                SourceSkillObj = self, 
                CastTarget = Target,
                Effects_OnTarget = [BattleEffect_RemoveDebuffsOnTarget(), 
                                    BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_Protected(
                                            Duration = 2,
                                            ProtectedBy = self.Owner_BattleChar,
                                            SourceName = self.DisplayName))],
                Effects_OnSelf = [BattleEffect_ApplyStatusOnAlly(
                                        StatusEffect = BattleStatusEff_DamageIn(
                                            StatusEffectID = "warrior_shield_damageinbuff",
                                            DamageRecieved_Mod = self.DamageResBuff[self.Level],
                                            Duration = 2,
                                            SourceName = self.DisplayName))])
            Battle_GrantExtraTurn(self.Owner_BattleChar)
            return

        def GetDesc(self, DescLevel = 1):
            DamageResPerc = Battle_FormatDescVal(round((1.0 - self.DamageResBuff[DescLevel]) * 100), Percentage = True)
            return tra(_("Removes all harmful effects from the target ally and protects them for 2 turns, redirecting any attack made against them onto you.\nDecreases the damage you take by %s for 2 turns and grants you an extra turn.")) % DamageResPerc