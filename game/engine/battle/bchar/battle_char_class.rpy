init python:
    class BattleCharClass:
        def __init__(self, StoryChar, CharID, BattleSide, IsTransformed = False):
            self.CharID = CharID # stored only for player party health restore thing
            self.CharRef = StoryChar
            self.CharRef["BattleChar"] = self

            self.BattleSide = BattleSide # 0 left 1 right

            self.IsAlive = True

            self.StatusEffects = []

            self.SpriteTag = "BattleCharSprite_%s" % id(self)
            self.SpriteZorder = 0 # will be 0-10-20-30 dep on position
            self.HudZorder = 0 # will be spritezorder + 1
            self.PositionSlotIndex = 0

            # instantiate skills to levels here
            # also apply tf stat eff
            if IsTransformed:
                HPRatio = self.Health / self.HealthMax

                if CharID in ["mc", "markus"]:
                    Battle_ApplyStatusEffect(TargetChar = self, StatusEffect = BattleStatusEff_TransformedPara())
                elif CharID == "elena":
                    Battle_ApplyStatusEffect(TargetChar = self, StatusEffect = BattleStatusEff_TransformedWolf())
                Battle_SetBattleCharSkillPool(self, "AltForm")

                self.Health = ClampValue(math.ceil(self.HealthMax * HPRatio), 1, self.HealthMax)
            else:
                Battle_SetBattleCharSkillPool(self, "Normal")

            # apply raza seed if its in story mode
            if StoryCharHasStatusEff(CharID, "RazaEffect"):
                Battle_ApplyStatusEffect(TargetChar = self, StatusEffect = BattleStatusEff_RazaSeed())
        
            self.Skill_Attack = BattleSkill_Attack(Owner_BattleChar = self)
            self.Skill_Defend = BattleSkill_Defend(Owner_BattleChar = self)

            if StoryChar["HasAltForm"] == True:
                self.Skill_ExtraTransform = SkillLib[StoryChar["AltForm_TransformSkill"]](Owner_BattleChar = self)
                self.Skill_ExtraUnTransform = SkillLib[StoryChar["AltForm_UnTransformSkill"]](Owner_BattleChar = self)
            else:
                self.Skill_ExtraTransform = None
                self.Skill_ExtraUnTransform = None

            self.AudioChannelVoice = "" # str
            self.AudioChannelsFX = ["", "", ""] # str channel names
            self.AudioChannelsFX_NextIndex = 0 # int

            self.SkinID_Current = (StoryChar["AltForm_BattleSkin"] if IsTransformed else StoryChar["BattleSkin"])
            self.SkinID_Normal = StoryChar["BattleSkin"]
            self.SkinID_AltForm = (StoryChar["AltForm_BattleSkin"] if StoryChar["HasAltForm"] else None)

            self.BattleSkin = None
            Battle_SetBattleCharSkin(self, self.SkinID_Current)
###############################################
######### battle-related stats
        @property
        def Damage(self): 
            if self.BattleSide == 1:
                ReturnVal = max(int(Battle_GetOutgoingDamageMod(self) * self.CharRef["Damage"] * DIFFICULTY.ENEMYSIDE_DMG[CurrentDifficulty]), 1)
            else:
                ReturnVal = max(int(Battle_GetOutgoingDamageMod(self) * self.CharRef["Damage"] * DIFFICULTY.PLAYERSIDE_DMG[CurrentDifficulty]), 1)
            return ReturnVal

        @property
        def Armor(self): 
            Val = self.CharRef["Armor"]
            for StatusEffect in self.StatusEffects:
                if StatusEffect.StatMod_Armor is not None:
                    Val *= StatusEffect.StatMod_Armor
            # return max(round(Val), 1)
            return round(Val)

        @property
        def MagicRes(self):
            Val = self.CharRef["MagicRes"]
            for StatusEffect in self.StatusEffects:
                if StatusEffect.StatMod_MagicRes is not None:
                    Val *= StatusEffect.StatMod_MagicRes
            return max(round(Val), 1)

        @property
        def AttackRating(self):
            Val = self.CharRef["AttackRating"]
            for StatusEffect in self.StatusEffects:
                if StatusEffect.StatMod_AttackRating is not None:
                    Val *= StatusEffect.StatMod_AttackRating
            # return max(round(Val), 1)
            return round(Val)

        @property
        def DodgeRating(self):
            Val = self.CharRef["DodgeRating"]
            for StatusEffect in self.StatusEffects:
                if StatusEffect.StatMod_DodgeRating is not None:
                    Val *= StatusEffect.StatMod_DodgeRating
            # return max(round(Val), 1)
            return round(Val)

        @property
        def CritChance(self):
            Val = self.CharRef["CritChance"]
            for StatusEffect in self.StatusEffects:
                if StatusEffect.StatMod_CritChance is not None:
                    Val *= StatusEffect.StatMod_CritChance
            return max(round(Val), 1)
        @property
        def Willpower(self):
            Val = self.CharRef["derived_Willpower"]
            return max(round(Val), 1)

###############################################
######### resources
        @property
        def HealthMax(self): return self.CharRef["HealthMax"]
        @property
        def Health(self): return self.CharRef["Health"]
        @Health.setter
        def Health(self, Value): self.CharRef["Health"] = Value

        @property
        def EnergyMax(self): return self.CharRef["EnergyMax"]
        @property
        def Energy(self): return self.CharRef["Energy"]
        @Energy.setter
        def Energy(self, Value): self.CharRef["Energy"] = Value

        @property
        def ManaMax(self): return self.CharRef["ManaMax"]
        @property
        def Mana(self): return self.CharRef["Mana"]
        @Mana.setter
        def Mana(self, Value): self.CharRef["Mana"] = Value