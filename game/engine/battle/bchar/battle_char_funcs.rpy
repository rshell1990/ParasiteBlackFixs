init python:    
    # a bchar created in battle from an id to belong to a specific side
    def BattleCharFromCharID(CharID, ToLevel = None, Side = 0):
        if ToLevel is not None:
            if ToLevel < 1:
                ToLevel = 1

        if CharID not in worldChars:
            IsMob = True
        else:
            IsMob = False

        if IsMob == True:
            StoryChar = PBCharacter(CharID)
        else:
            StoryChar = copy.deepcopy(worldChars[CharID])

        if ToLevel is not None:
            # seems right
            ExpDiffToAdd = allLvls[ToLevel] - StoryChar["experience"]
            # if difference is negative, then we must eeeeh ummmm uuuuueeeeeemmmmmmmmm
            if ExpDiffToAdd < 0:
                # then what we do is SUBTRACT?
                StoryChar["experience"] += ExpDiffToAdd
                if StoryChar["experience"] < 1:
                    StoryChar["experience"] = 1
            else:
                AddExpDirect(StoryChar, ExpDiffToAdd)
                AutoAllocateAttributes(StoryChar)
            # story chars only heal if you to-level them (coz its for testing anyway)
            if not IsMob:
                if ToLevel is not None:
                    CharHealDirect(StoryChar, 99999)

        # mobs heal on spawn
        if IsMob:
            CharHealDirect(StoryChar, 99999)

        # both mobs and story chars restore ep/mp
        CharRestoreEnergyDirect(StoryChar)
        CharRestoreManaDirect(StoryChar)

        # AFTER THAT we've prepared story-char,
        # so next is B.char class init stage
        return BattleCharClass(StoryChar, CharID, BattleSide = Side, IsTransformed = StoryChar["Transformed"])

    def Battle_ConvertCharIDListToBattleChars(CharIDList, Side = 0):
        BattleCharList = []
        for Entry in CharIDList:
            if isinstance(Entry, str):
                BattleCharList.append(BattleCharFromCharID(Entry, Side = Side))
            if isinstance(Entry, dict):
                AsList = list(Entry.keys())
                CharID = AsList[0]
                TargetLevel = Entry[CharID]
                BattleCharList.append(BattleCharFromCharID(CharID, ToLevel = TargetLevel, Side = Side))
        return BattleCharList

########################################################
    def Battle_GetCharStatMod_Armor(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.StatMod_Armor is not None:
                ReturnVal *= StatusEffect.StatMod_Armor
        return ReturnVal
    def Battle_GetCharStatMod_MagicRes(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.StatMod_Armor is not None:
                ReturnVal *= StatusEffect.StatMod_Armor
        return ReturnVal
    def Battle_GetCharStatMod_AttackRating(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.StatMod_Armor is not None:
                ReturnVal *= StatusEffect.StatMod_Armor
        return ReturnVal
    def Battle_GetCharStatMod_DodgeRating(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.StatMod_Armor is not None:
                ReturnVal *= StatusEffect.StatMod_Armor
        return ReturnVal
    def Battle_GetCharStatMod_CritChance(BattleChar):
        ReturnVal = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.StatMod_Armor is not None:
                ReturnVal *= StatusEffect.StatMod_Armor
        return ReturnVal
########################################################
###### health
    def Battle_GetHealthRecoveryMod(BattleChar):
        RecoveryMod = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.ResRecoverMod_Health is not None:
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
    # its like deal damage but directly and without any fancy-ass stuff
    def Battle_BurnHealth(BattleChar, Value):
        BattleChar.Health -= Value
        if BattleChar.Health < 0:
            BattleChar.Health = 0
        return
################################
###### energy
    def Battle_GetEnergyRecoveryMod(BattleChar):
        RecoveryMod = 1.0
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.ResRecoverMod_Energy is not None:
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
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.ResRecoverMod_Mana is not None:
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
        if PoolType == "Normal":
            BattleChar.Skills = [SkillLib[SkillID](Owner_BattleChar = BattleChar, ToLevel = SkillLevel) for SkillID, SkillLevel in BattleChar.CharRef["CharSkills"].items()]
        elif PoolType == "AltForm":
            BattleChar.Skills = [SkillLib[SkillID](Owner_BattleChar = BattleChar, ToLevel = SkillLevel) for SkillID, SkillLevel in BattleChar.CharRef["AltForm_CharSkills"].items()]
        return

    def Battle_SetBattleCharSkin(BattleChar, SkinID):
        Assert(SkinID in skinLib, "SkinID %s not in skinLib, wtf!" % SkinID)

        BattleChar.BattleSkin = copy.deepcopy(skinLib[SkinID])
        Battle_ResetBattleCharSkin(BattleChar)
        return

######## internals are all over the place, tread carefully
    def Battle_ResetBattleCharSkin(BattleChar):
        NewSkin = BattleChar.BattleSkin
        for AnimID, AnimDataOrList in NewSkin.AnimsDict.items():
            # gotta go fast (this is for list of anims under a single tag support)
            if isinstance(AnimDataOrList, list):
                AnimsToProcess = AnimDataOrList
            else:
                AnimsToProcess = [AnimDataOrList]

            # here we gotta re-calculate data for, and apply a transform
            for AnimData in AnimsToProcess:
                # case 1, default fallback, static + transform
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

                # case 2 image-based anim animation
                # apply transform to a specified image 
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

                # calc warmup and cooldown
                AnimData.Warmup = AnimData.WarmupTo
                AnimData.Cooldown = AnimData.LengthInSeconds - AnimData.WarmupTo

        # flip (or not flip) the offsets
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
        RetList.remove(BattleChar)
        return RetList

    def Battle_GetAliveCharsOnSide(Side):
        return [Char for Char in BattleScene.BattleChars[Side] if Char.IsAlive]