init python:    
    # a bchar created in battle from an id to belong to a specific side
    def BattleCharFromCharID(CharID, ToLevel = None, Side = 0):
        if ToLevel is not None:
            if ToLevel < 1:
                ToLevel = 1

        world_chars = getattr(store, "worldChars", {})
        if CharID not in world_chars:
            IsMob = True
        else:
            IsMob = False

        if IsMob:
            StoryChar = PBCharacter(CharID)
        else:
            if CharID in ("mc", "markus") and QstIsOver(QstFromAnotherWorld):
                worldChars[CharID]["AltForm_Unlocked"] = True
            StoryChar = copy.deepcopy(world_chars[CharID])

        all_lvls = getattr(store, "allLvls", {})
        if ToLevel is not None and ToLevel in all_lvls:
            # calculate exp diff safely
            ExpDiffToAdd = all_lvls[ToLevel] - StoryChar.get("experience", 0)
            if ExpDiffToAdd < 0:
                StoryChar["experience"] = StoryChar.get("experience", 0) + ExpDiffToAdd
                if StoryChar["experience"] < 1:
                    StoryChar["experience"] = 1
            else:
                AddExpDirect(StoryChar, ExpDiffToAdd)
                AutoAllocateAttributes(StoryChar)
            # story chars only heal if you to-level them (coz its for testing anyway)
            if not IsMob:
                CharHealDirect(StoryChar, 99999)

        # mobs heal on spawn
        if IsMob:
            CharHealDirect(StoryChar, 99999)

        # both mobs and story chars restore ep/mp
        CharRestoreEnergyDirect(StoryChar)
        CharRestoreManaDirect(StoryChar)

        is_transformed = StoryChar.get("Transformed", False) if isinstance(StoryChar, dict) else False
        BattleChar = BattleCharClass(StoryChar, CharID, BattleSide = Side, IsTransformed = is_transformed)
        if not hasattr(BattleChar, "SpriteTag"):
            BattleChar.SpriteTag = "battle_char_%s_%s_%s" % (Side, CharID, id(BattleChar))

        PoolType = "AltForm" if is_transformed else "Normal"
        Battle_SetBattleCharSkillPool(BattleChar, PoolType)
        BattleChar.Skill_Attack = BattleSkill_Attack(Owner_BattleChar = BattleChar)
        BattleChar.Skill_Defend = BattleSkill_Defend(Owner_BattleChar = BattleChar)

        SkillLib = getattr(store, "SkillLib", {})
        TransformSkillID = BattleChar.CharRef.get("AltForm_TransformSkill")
        UnTransformSkillID = BattleChar.CharRef.get("AltForm_UnTransformSkill")
        if TransformSkillID in SkillLib:
            BattleChar.Skill_ExtraTransform = SkillLib[TransformSkillID](Owner_BattleChar = BattleChar)
        if UnTransformSkillID in SkillLib:
            BattleChar.Skill_ExtraUnTransform = SkillLib[UnTransformSkillID](Owner_BattleChar = BattleChar)

        BattleChar.SkinID_Normal = StoryChar.get("BattleSkin")
        BattleChar.SkinID_AltForm = StoryChar.get("AltForm_BattleSkin")
        SkinID = BattleChar.SkinID_AltForm if is_transformed else BattleChar.SkinID_Normal
        if SkinID is not None and SkinID in getattr(store, "skinLib", {}):
            Battle_SetBattleCharSkin(BattleChar, SkinID)

        return BattleChar

    def Battle_ConvertCharIDListToBattleChars(CharIDList, Side = 0):
        BattleCharList = []
        for Entry in CharIDList:
            if isinstance(Entry, str):
                BattleCharList.append(BattleCharFromCharID(Entry, Side = Side))
            elif isinstance(Entry, dict):
                AsList = list(Entry.keys())
                if AsList:
                    CharID = AsList[0]
                    TargetLevel = Entry[CharID]
                    BattleCharList.append(BattleCharFromCharID(CharID, ToLevel = TargetLevel, Side = Side))
        return BattleCharList

########################################################
    def Battle_GetCharStatMod_Armor(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "StatMod_Armor", None) is not None:
                ReturnVal *= StatusEffect.StatMod_Armor
        return ReturnVal

    def Battle_GetCharStatMod_MagicRes(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "StatMod_MagicRes", None) is not None:
                ReturnVal *= StatusEffect.StatMod_MagicRes
        return ReturnVal

    def Battle_GetCharStatMod_AttackRating(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "StatMod_AttackRating", None) is not None:
                ReturnVal *= StatusEffect.StatMod_AttackRating
        return ReturnVal

    def Battle_GetCharStatMod_DodgeRating(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "StatMod_DodgeRating", None) is not None:
                ReturnVal *= StatusEffect.StatMod_DodgeRating
        return ReturnVal

    def Battle_GetCharStatMod_CritChance(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "StatMod_CritChance", None) is not None:
                ReturnVal *= StatusEffect.StatMod_CritChance
        return ReturnVal
########################################################
###### health
    def Battle_GetHealthRecoveryMod(BattleChar):
        RecoveryMod = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "ResRecoverMod_Health", None) is not None:
                RecoveryMod *= StatusEffect.ResRecoverMod_Health
        return RecoveryMod

    def Battle_RestoreHealth(BattleChar, Value, FloatingVal = True, IgnoreRecoveryMod = False, RatioFromMax = False):
        if RatioFromMax:
            Value = BattleChar.HealthMax * Value
        if not IgnoreRecoveryMod:
            Value = Value * Battle_GetHealthRecoveryMod(BattleChar)
        Value = round(Value)
        BattleChar.Health += Value
        if BattleChar.Health > BattleChar.HealthMax:
            BattleChar.Health = BattleChar.HealthMax
        if FloatingVal:
            Battle_QueueFloatingTextOnChar(BattleChar, Value, Kind = 1)
        return

    # deal direct health reduction
    def Battle_BurnHealth(BattleChar, Value):
        BattleChar.Health -= Value
        if BattleChar.Health < 0:
            BattleChar.Health = 0
        return
################################
###### energy
    def Battle_GetEnergyRecoveryMod(BattleChar):
        RecoveryMod = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "ResRecoverMod_Energy", None) is not None:
                RecoveryMod *= StatusEffect.ResRecoverMod_Energy
        return RecoveryMod

    def Battle_RestoreEnergy(BattleChar, Value, IgnoreRecoveryMod = False):
        if not IgnoreRecoveryMod:
            Value = round(Value * Battle_GetEnergyRecoveryMod(BattleChar))
        BattleChar.Energy += Value
        if BattleChar.Energy > BattleChar.EnergyMax:
            BattleChar.Energy = BattleChar.EnergyMax
        return

    def Battle_BurnEnergy(BattleChar, Value):
        BattleChar.Energy -= Value
        if BattleChar.Energy < 0:
            BattleChar.Energy = 0
        return
###############################
###### mana
    def Battle_GetManaRecoveryMod(BattleChar):
        RecoveryMod = 1.0
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "ResRecoverMod_Mana", None) is not None:
                RecoveryMod *= StatusEffect.ResRecoverMod_Mana
        return RecoveryMod

    def Battle_RestoreMana(BattleChar, Value):
        BattleChar.Mana += Value
        if BattleChar.Mana > BattleChar.ManaMax:
            BattleChar.Mana = BattleChar.ManaMax
        return

    def Battle_BurnMana(BattleChar, Value):
        BattleChar.Mana -= Value
        if BattleChar.Mana < 0:
            BattleChar.Mana = 0
        return
#################

    def Battle_SetBattleCharSkillPool(BattleChar, PoolType):
        skill_lib = getattr(store, "SkillLib", {})
        char_ref = getattr(BattleChar, "CharRef", {})
        
        if PoolType == "Normal":
            skills_dict = char_ref.get("CharSkills", {})
        elif PoolType == "AltForm":
            skills_dict = char_ref.get("AltForm_CharSkills", {})
        else:
            skills_dict = {}

        BattleChar.Skills = [
            skill_lib[SkillID](Owner_BattleChar = BattleChar, ToLevel = SkillLevel)
            for SkillID, SkillLevel in skills_dict.items()
            if SkillID in skill_lib
        ]
        return

    def Battle_SetBattleCharSkin(BattleChar, SkinID):
        skin_lib = getattr(store, "skinLib", {})
        assert SkinID in skin_lib, "SkinID %s not in skinLib!" % SkinID

        BattleChar.BattleSkin = copy.deepcopy(skin_lib[SkinID])
        Battle_ResetBattleCharSkin(BattleChar)
        return

    def Battle_ResetBattleCharSkin(BattleChar):
        NewSkin = BattleChar.BattleSkin
        for AnimID, AnimDataOrList in NewSkin.AnimsDict.items():
            if isinstance(AnimDataOrList, list):
                AnimsToProcess = AnimDataOrList
            else:
                AnimsToProcess = [AnimDataOrList]

            for AnimData in AnimsToProcess:
                if AnimData.Displayable == "StaticSprite":
                    if AnimID == "attack":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(NewSkin.Sprite, Battle_TransformAttack(BattleChar))
                        else:
                            AnimData.Displayable = NewSkin.Sprite
                        AnimData.LengthInSeconds = 0.45
                        AnimData.WarmupTo = 0.15
                        NewSkin.SoundsExtraSilence["BasicAttack_Swing"] = 0.1

                    elif AnimID == "idle":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(NewSkin.Sprite, Battle_TransformIdle(BattleChar))
                        else:
                            AnimData.Displayable = NewSkin.Sprite
                        AnimData.LengthInSeconds = 0.95

                    elif AnimID == "cast":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(NewSkin.Sprite, Battle_TransformCast(BattleChar))
                        else:
                            AnimData.Displayable = NewSkin.Sprite
                        AnimData.LengthInSeconds = 0.45
                        AnimData.WarmupTo = 0.2

                    elif AnimID == "hit":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(NewSkin.Sprite, Battle_TransformHit(BattleChar))
                        else:
                            AnimData.Displayable = NewSkin.Sprite
                        AnimData.LengthInSeconds = 0.25
                        AnimData.WarmupTo = 0.05

                else:
                    if AnimID == "attack":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(AnimData.Displayable, Battle_TransformAttack(BattleChar, AnimData.Transform_AttackDelay))

                    elif AnimID == "idle":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(AnimData.Displayable, Battle_TransformIdle(BattleChar))
                    
                    elif AnimID == "cast":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(AnimData.Displayable, Battle_TransformCast(BattleChar))
                    
                    elif AnimID == "hit":
                        if AnimData.ApplyTransform:
                            AnimData.Displayable = At(AnimData.Displayable, Battle_TransformHit(BattleChar))

                AnimData.Warmup = AnimData.WarmupTo
                AnimData.Cooldown = AnimData.LengthInSeconds - AnimData.WarmupTo

        if BattleChar.BattleSide == 1:
            NewSkin.SpriteOffset = (-NewSkin.SpriteOffset[0], NewSkin.SpriteOffset[1])
            NewSkin.FocusRectOffset = (-NewSkin.FocusRectOffset[0], NewSkin.FocusRectOffset[1])
            NewSkin.SpriteVFXOffset = (-NewSkin.SpriteVFXOffset[0], NewSkin.SpriteVFXOffset[1])

        return

############ these are often used in skills
    def Battle_GetAllEnemiesOfChar(BattleChar):
        OpposingSide = (0 if BattleChar.BattleSide == 1 else 1)
        return Battle_GetAliveCharsOnSide(OpposingSide)

    def Battle_GetAllAlliesOfChar(BattleChar):
        RetList = Battle_GetAliveCharsOnSide(BattleChar.BattleSide)
        if BattleChar in RetList:
            RetList.remove(BattleChar)
        return RetList

    def Battle_GetAliveCharsOnSide(Side):
        battle_scene = getattr(store, "BattleScene", None)
        if battle_scene and hasattr(battle_scene, "BattleChars"):
            return [Char for Char in battle_scene.BattleChars.get(Side, []) if getattr(Char, "IsAlive", False)]
        return []