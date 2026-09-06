init python:
    @RegisterBattleSkill("NeutralTeamUp")
    class BattleSkill_NeutralTeamUp(BattleSkill):    
        DisplayName = _("Team Up")
        Icon = "images/battle_skill_icons/neutral/StrongAttack.webp"

        ValidTargets = BATTLE_TARGETS.ANY_ENEMY
        Cost_Energy = 40

        DamageValue = {1: 1.0}

        AITags = {AI_TAGS.ONLY_IF_ALLIES_EXIST}
        AIBaseWeight = 2.0

        def Execute(self, Target):
            Battle_ScheduledAttack( 
                SourceSkillObj = self, 
                AttackTarget = Target)

            # teamed up attack
            AllAllies = Battle_GetAliveCharsOnSide(self.Owner_BattleChar.BattleSide)
            AllAllies.remove(self.Owner_BattleChar)

            for Char in reversed(AllAllies):
                if Battle_HasStatusEffect(Char, "stun"):
                    AllAllies.remove(Char)

            if len(AllAllies) > 0:
                RandomAlly = renpy.random.choice(AllAllies)

                Battle_ScheduledAttack(
                    SourceSkillObj = RandomAlly.Skill_Attack,
                    AttackTarget = Target)
            return

        def GetDesc(self, DescLevel = 1):
            if self.Owner_BattleChar:
                DamageValue = Battle_FormatDescVal(Battle_GetBCharDmgTupleAsText(self.Owner_BattleChar, self.DamageValue[DescLevel]))
            else:
                DamageValue = Battle_FormatDescVal(Battle_GetPBCharDmgTupleAsText(self.Owner_PBCharID, self.DamageValue[DescLevel]))

            return tra(_("Team up with a random ally to do a basic attack against the target enemy. This character's attack will deal %s damage.")) % DamageValue