init python:
    @RegisterBattleSkill("SummonDemon")
    class BattleSkill_SummonDemon(BattleSkill):
        DisplayName = _("SummonDemon")
        Icon = "images/battle_skill_icons/no_icon.webp"

        Level_Max = 4
        ValidTargets = BATTLE_TARGETS.SELF
        Cost_Energy = 60
        #AITags = {AI_TAGS.Summon}

        SummonedCharID = "e_summoned_demon"
        SummonStatMultiplier = {1: 1.00, 2: 1.25, 3: 1.50, 4: 1.75}

        def CanExecute(self):
            if not BattleSkill.CanExecute(self):
                return False

            Allies = BattleScene.BattleChars[self.Owner_BattleChar.BattleSide]
            return len(Allies) < 4 and not any(Char.CharID == self.SummonedCharID for Char in Allies)

        def Execute(self, Target):
            Summoner = self.Owner_BattleChar
            SummonedAlly = BattleCharFromCharID(
                self.SummonedCharID,
                ToLevel = self.Level,
                Side = Summoner.BattleSide)

            StatMultiplier = self.SummonStatMultiplier[self.Level]
            for StatID in ["base_health", "base_damage", "base_energy", "Strength", "Endurance", "Willpower", "Agility", "Dexterity", "Luck"]:
                SummonedAlly.CharRef[StatID] = round(SummonedAlly.CharRef[StatID] * StatMultiplier)
            SummonedAlly.Health = SummonedAlly.HealthMax
            SummonedAlly.Energy = SummonedAlly.EnergyMax
            SummonedAlly.Mana = SummonedAlly.ManaMax

            BattleScene.BattleChars[Necromancer.BattleSide].append(SummonedAlly)
            Battle_SetCharPositionsAndZorder()
            Battle_OnStartShowChars()
            return

        def GetDesc(self, DescLevel = 1):
            StatBonus = round((self.SummonStatMultiplier[DescLevel] - 1.0) * 100)
            return tra(_("Summons a Spectral Demon into an empty allied slot. Its health, damage, energy, and attributes are increased by %s%%. The demon acts from the next turn. Only one demon may be summoned at a time.")) % StatBonus
