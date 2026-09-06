default DEBUG_EndlessBattle = False
default BattleChar_SpriteZorder = {0: {0: (100, 200), 1: (110, 210), 2: (120, 220), 3: (130, 230)}, 1: {0: (100, 200), 1: (110, 210), 2: (120, 220), 3: (130, 230)}}
default BattleChar_ScreenPositions = {0: {0: (480, 540), 1: (720, 540), 2: (960, 540), 3: (1200, 540)}, 1: {0: (1440, 540), 1: (1200, 540), 2: (960, 540), 3: (720, 540)}}
default BattleChar_ScreenPositions_Offset = {0: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}, 1: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}}
default BattleChar_ScreenPositions_Offset_Anim = {0: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}, 1: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}}
default BattleChar_ScreenPositions_Offset_Anim_Active = {0: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}, 1: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}}

init python:
    # the function you start a battle with, from script. needs a valid BattleData object, full of various stuff. for examples, search
    BattleData = None
    BattleSceneClass = None
    BattleSetup_GetAllCharsWithSkin = None
    def Battle_ReinitializeScene(BattleScene):
        BattleScene.BattleChars = [[], []]
        BattleScene.BattleLog = []
        BattleScene.TurnLimit = BattleScene.BattleData.TurnLimit
        BattleScene.Turn = 0
        BattleScene.Outcome = None
        BattleScene.ActingSide = 0
        BattleScene.SelectedLeft = None
        BattleScene.SelectedRight = None
        BattleScene.ActiveCharsList = []
        BattleScene.TauntedCharsForCurrentlyActiveSide = []
        BattleScene.ScheduledAttackQueue = []
        BattleScene.ScheduledActionToExecute = None
        BattleScene.SelectedActionToProcess = None
        return
    def Battle_Setup(BattleDataObj, BattleSceneClassObj, BattleSetup_GetAllCharsWithSkinFunc):
        global BattleData
        global BattleSceneClass
        global BattleSetup_GetAllCharsWithSkin

        BattleData = BattleDataObj
        BattleSceneClass = BattleSceneClassObj
        BattleSetup_GetAllCharsWithSkin = BattleSetup_GetAllCharsWithSkinFunc
        return
    def Battle_GetScene():
        return BattleScene
    def Battle_GetAliveCharsOnSide(Side):
        return [BattleChar for BattleChar in BattleScene.BattleChars[Side] if BattleChar.IsAlive]
    def Battle_GetAllCharsOnSide(Side):
        return BattleScene.BattleChars[Side]
    def Battle_GetAllChars():
        return BattleScene.BattleChars[0] + BattleScene.BattleChars[1]
    def Battle_GetStatusEffect(BattleChar, StatusEffectID):
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.ID == StatusEffectID:
                return StatusEffect
        return None
    def Battle_HasStatusEffect(BattleChar, StatusEffectID):
        for StatusEffect in BattleChar.StatusEffects:
            if StatusEffect.ID == StatusEffectID:
                return True
        return False
    def Battle_SetCharAction(BattleChar, ActionInstance, Target):
        BattleScene.SelectedActionToProcess = BattleActionInstance(BattleChar, ActionInstance, Target)
        return
    def Battle_ScheduleAttack(BattleActionInstanceObj):
        BattleScene.ScheduledAttackQueue.append(BattleActionInstanceObj)
        return
    def Battle_RunCharAnim(BattleChar, AnimName):
        BattleChar.BattleSkin.PlayAnim(AnimName)
        return
    def Battle_RestoreEnergy(BattleChar, Amount):
        BattleChar.Energy = min(BattleChar.Energy + Amount, BattleChar.EnergyMax)
        return
    def Battle_RestoreMana(BattleChar, Amount):
        BattleChar.Mana = min(BattleChar.Mana + Amount, BattleChar.ManaMax)
        return
    def Battle_AddLogEntry(Text):
        BattleScene.BattleLog.append(Text)
        return
    def Battle_ClearLog():
        BattleScene.BattleLog = []
        return
    def Battle_PlacePermaStatusEffects():
        for BattleChar in BattleScene.BattleChars[0] + BattleScene.BattleChars[1]:
            for StatusEffect in BattleChar.StatusEffects:
                if StatusEffect.IsPermanent:
                    renpy.show_screen("Battle_CharStatusEffectIcon", 
                        BattleChar = BattleChar, 
                        StatusEffect = StatusEffect, 
                        _zorder = 1000, 
                        _tag = "BattleCharStatusEffect_%s_%s" % (id(BattleChar), StatusEffect.ID),
                        _layer = "master")
        return
    def Battle_RemovePermaStatusEffects():
        for BattleChar in BattleScene.BattleChars[0] + BattleScene.BattleChars[1]:
            for StatusEffect in BattleChar.StatusEffects:
                if StatusEffect.IsPermanent:
                    renpy.hide_screen("BattleCharStatusEffect_%s_%s" % (id(BattleChar), StatusEffect.ID))
        return
    def Battle_TickStatusEffectDuration(Side, AtEnd = False):
        for BattleChar in Battle_GetAliveCharsOnSide(Side):
            for StatusEffect in copy.copy(BattleChar.StatusEffects):
                if AtEnd:
                    StatusEffect.TickDuration(AtEnd = True)
                else:
                    StatusEffect.TickDuration(AtEnd = False)
        return
    def Battle_StatusEffect_OnTurnStart(Side):
        for BattleChar in Battle_GetAliveCharsOnSide(Side):
            for StatusEffect in copy.copy(BattleChar.StatusEffects):
                StatusEffect.OnTurnStart()
        return
    def Battle_StatusEffect_OnTurnEnd(Side):
        for BattleChar in Battle_GetAliveCharsOnSide(Side):
            for StatusEffect in copy.copy(BattleChar.StatusEffects):
                StatusEffect.OnTurnEnd()
    def Battle_DoAITurn(BattleChar):
        pass
    def Battle_ForceEndTurnForChar(BattleChar):
        if BattleChar in BattleScene.ActiveCharsList:
            BattleScene.ActiveCharsList.remove(BattleChar)
        return
    def Battle_ForceEndTurnForSide(Side):
        BattleScene.ActiveCharsList = []
        return
    def Battle_ForceEndTurnForAll():
        BattleScene.ActiveCharsList = []
    def Battle_ForceEndTurnForAllExcept(BattleChar):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char != BattleChar:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSide(Side):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndChar(Side, BattleChar):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char != BattleChar:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharList(Side, CharList):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptCharList(CharList):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char not in CharList:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharListAndStatusEffect(Side, CharList, StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList and not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndStatusEffect(Side, StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptStatusEffect(StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndChar(Side, BattleChar):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char != BattleChar:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharList(Side, CharList):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharListAndStatusEffect(Side, CharList, StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList and not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndStatusEffect(Side, StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptStatusEffect(StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndChar(Side, BattleChar):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char != BattleChar:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharList(Side, CharList):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharListAndStatusEffect(Side, CharList, StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList and not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndStatusEffect(Side, StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptStatusEffect(StatusEffectID):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if not Battle_HasStatusEffect(Char, StatusEffectID):
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndChar(Side, BattleChar):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char != BattleChar:
                BattleScene.ActiveCharsList.remove(Char)
    def Battle_ForceEndTurnForAllExceptSideAndCharList(Side, CharList):
        for Char in copy.copy(BattleScene.ActiveCharsList):
            if Char.BattleSide != Side and Char not in CharList:
                BattleScene.ActiveCharsList.remove(Char)
    def StartBattle(BattleDataObj):
        store.BattleScene = BattleSceneClass(BattleDataObj)
        renpy.call("Battle_Start")
        return

    def IsPlayerInBattle():
        return store.BattleScene is not None


############################### internals 
######## funcs
# all these are very varied and used in "top-ish level" battle code.
# more specialized b.related functions can be found in other files
    def Battle_Win():
        BattleScene.Outcome = "victory"
        renpy.jump("Battle_Over")
        return

    def Battle_Lose():
        BattleScene.Outcome = "defeat"
        renpy.jump("Battle_Over")
        return

    def Battle_Retreat():
        BattleScene.Outcome = "retreat"
        renpy.jump("Battle_Over")
        return

    def Battle_ClearSceneAndJumpTo(TargetLabel):
        store.BattleScene = None
        renpy.jump(TargetLabel)
        return

    def Battle_LoopStep(Value):
        if persistent.BattlePref_FastLoop:
            # some delay otherwise it looks wack and is hard 2debug
            renpy.pause(0.016)
        else:
            renpy.pause(Value)
        return

    def Battle_UIAutoSelectIfOneAliveOnSide(Side):
        AliveSideChars = Battle_GetAliveCharsOnSide(Side)
        if len(AliveSideChars) == 1:
            if Side == 0:
                Battle_SelectLeftChar(AliveSideChars[0])
            if Side == 1:
                Battle_SelectRightChar(AliveSideChars[0])
        return

    def Battle_EndIfEitherSideDefeated(BattleScene):
        if len(Battle_GetAliveCharsOnSide(Side = 0)) == 0:
            BattleScene.Outcome = "defeat"
            return
        if len(Battle_GetAliveCharsOnSide(Side = 1)) == 0:
            BattleScene.Outcome = "victory"
            return
        if BattleScene.TurnLimit is not None:
            if BattleScene.Turn >= BattleScene.TurnLimit:
                BattleScene.Outcome = "defeat"
                return

    def Battle_SelectLeftChar(Char):
        if BattleScene.SelectedLeft is not None:
            BattleUI_BringInfoBackward(BattleScene.SelectedLeft)
        BattleScene.SelectedLeft = Char
        BattleUI_BringInfoForward(Char)
        return

    def Battle_SelectRightChar(Char):
        if BattleScene.SelectedRight is not None:
            BattleUI_BringInfoBackward(BattleScene.SelectedRight)
        BattleScene.SelectedRight = Char
        BattleUI_BringInfoForward(Char)
        return

    def Battle_HideCharInfoScreens():
        for BattleChar in BattleScene.BattleChars[0] + BattleScene.BattleChars[1]:
            renpy.hide_screen("BattleCharInfoScreen_%s" % id(BattleChar))
        return

    def Battle_HideBattleVFXSprites():
        for BattleChar in BattleScene.BattleChars[0] + BattleScene.BattleChars[1]:
            renpy.hide(BattleChar.BattleSkin.BasicAttackImpactImageID)
        return

    def Battle_ApplyPlayerPartyHealthAndCarryOverStatusEffects():
        for Char in BattleScene.BattleChars[0]:
            CharID = Char.CharID
            if CharID in worldChars:
                if CharInParty(CharID):
                    HealthRatio = Char.Health / Char.HealthMax
                    worldChars[CharID]["Health"] = max(round(worldChars[CharID]["HealthMax"] * HealthRatio), 1)
                    if Char in BattleScene.PostBattleGlobalPoison:
                        ApplyStatusEffect_Story(CharID, "Poison", BattleScene.PostBattleGlobalPoison[Char])
        return

    def Battle_StoreEnemyMatchupAndGrantVictoryExp(BattleScene):
        # early out if we dont give xp
        if BattleScene.GrantXp == False:
            return 

        NewCharIDList_Right = []
        # examine all entries and build a new ID list
        for Entry in BattleScene.CharIDList_Right:
            ### to-level case
            if isinstance(Entry, dict):
                AsList = list(Entry.keys())
                CharID = AsList[0]
                TargetLevel = Entry[CharID]
                NewCharIDList_Right.append(CharID + "_lv" + str(TargetLevel))
            ### plain id case
            else:
                NewCharIDList_Right.append(Entry)
        if sorted(NewCharIDList_Right) not in Playthrough_FoughtEnemyTeams:
            Playthrough_FoughtEnemyTeams.append(sorted(NewCharIDList_Right))
            XpSum = sum([EnemyBattleChar.CharRef["base_xp_value"] for EnemyBattleChar in BattleScene.BattleChars[1]])
            AddExpPlayer(XpSum)
        return

    def Battle_ShowPostBattleLoot(BattleScene):
        if len(BattleScene.ItemsToBeDroppedOnVictory) > 0:
            TemporaryLootContainer = {}
            for ItemEntry in BattleScene.ItemsToBeDroppedOnVictory:
                # kringe pighat
                for ItemID, Qty in ItemEntry.items():
                    AddItemTo(TemporaryLootContainer, ItemID, Amount = Qty)
            if persistent.BattlePref_AutoLootAll:
                TakeAllItems(TemporaryLootContainer, Silent = False)
            else:
                renpy.call_screen("container", TemporaryLootContainer, ContainerName = _("Battle loot"), DoReturn = True, DoReturnOnTakeAll = True)
                # mandatory! deletion of leftover items
                if len(TemporaryLootContainer) > 0:
                    for ItemID, ItemQty in copy.copy(TemporaryLootContainer).items():
                        RemItemFrom(TemporaryLootContainer, ItemID, Amount = ItemQty)
    
    # this is here just bc its big
    def Battle_GatherAllTauntedCharsForSide(Side):
        BattleScene.TauntedCharsForCurrentlyActiveSide = [BattleChar for BattleChar in Battle_GetAliveCharsOnSide(Side) if (Battle_HasStatusEffect(BattleChar, "taunt") and BattleChar in BattleScene.ActiveCharsList)]
        return

    def Battle_AutoScheduleTauntedAttackForChar(BattleChar):
        Battle_SetCharAction(BattleChar, BattleChar.Skill_Attack, Battle_GetStatusEffect(BattleChar, "taunt").TauntedBy)
        return

    def Battle_GetAllCharsWhoCanAct(Side = None):
        ReturnList = Battle_GetAliveCharsOnSide(Side)

        for BattleChar in reversed(ReturnList):
            if Battle_HasStatusEffect(BattleChar, "stun"):
                ReturnList.remove(BattleChar)
        return ReturnList

    
    def Battle_TurnStartRestoreEnergyOrMana(SideIndex):
        for Char in BattleScene.BattleChars[SideIndex]:
            Battle_RestoreEnergy(Char, int(Char.EnergyMax / 10))
            Battle_RestoreMana(Char, int(Char.ManaMax / 10))
        return

    def Battle_TurnStartResetSkillsUsed(SideIndex):
        for Char in BattleScene.BattleChars[SideIndex]:
            Char.Skill_Defend.UsedThisTurn = False
            for Skill in Char.Skills:
                Skill.UsedThisTurn = False
        return

    def Battle_SetCharPositionsAndZorder():
        for CharList in [BattleScene.BattleChars[0], BattleScene.BattleChars[1]]:
            # count chars
            BattleCharsAmt = len(CharList)

            # assign positions dep on amount
            if BattleCharsAmt == 1:
                CharList[0].PositionSlotIndex = 0

            elif BattleCharsAmt == 2:
                CharList[0].PositionSlotIndex = 0
                CharList[1].PositionSlotIndex = 1

            elif BattleCharsAmt == 3:
                CharList[0].PositionSlotIndex = 0
                CharList[1].PositionSlotIndex = 1
                CharList[2].PositionSlotIndex = 2

            elif BattleCharsAmt == 4:
                CharList[0].PositionSlotIndex = 0
                CharList[1].PositionSlotIndex = 1
                CharList[2].PositionSlotIndex = 2
                CharList[3].PositionSlotIndex = 3

            # set sprite zorders
            for Char in CharList:
                Char.SpriteZorder = BattleChar_SpriteZorder[Char.PositionSlotIndex][0]
                Char.HudZorder = BattleChar_SpriteZorder[Char.PositionSlotIndex][1]

            # set audio channels
            for Char in CharList:
                NewPanValue = round((1.0 - (BattleChar_ScreenPositions[Char.BattleSide][Char.PositionSlotIndex][0] / (1920 / 2))), 2)
                NewPanValue *= 0.5

                Char.AudioChannelsFX = []
                for FXChannelIndex in range(3):
                    CharChannelName = "BattleSFX_%s_%s_%s" % (Char.BattleSide, Char.PositionSlotIndex, FXChannelIndex)
                    Char.AudioChannelsFX.append(CharChannelName)
                    renpy.music.set_pan(-NewPanValue, 0.1, channel = CharChannelName)

                Char.AudioChannelVoice = "BattleSFX_%s_%s_voice" % (Char.BattleSide, Char.PositionSlotIndex)
                renpy.music.set_pan(-NewPanValue, 0.1, channel = Char.AudioChannelVoice)
        return

    def Battle_OnStartShowChars():
        for BattleChar in BattleScene.BattleChars[0] + BattleScene.BattleChars[1]:
            Battle_RunCharAnim(BattleChar, "idle")
            renpy.show_screen("Battle_CharInfoOnBattlefield", 
                BattleChar = BattleChar, 
                _zorder = BattleChar.HudZorder, 
                _tag = "BattleCharInfoScreen_%s" % id(BattleChar),
                _layer = "master")
        return
    


########## labels
# start (and restart) battle 
label Battle_Start:
    $ TooltipClear()
    hide screen Battle_BottomPanel
    hide screen Battle_CharInfoOnBattlefield
    hide screen Battle_TurnCounter
    hide screen Battle_CharSelectionPanels
    scene black 
    with dissolve

    $ Battle_ReinitializeScene(BattleScene)

    scene expression BattleScene.BackgroundImage    
    # show all dudes
    $ Battle_SetCharPositionsAndZorder()
    $ Battle_OnStartShowChars()

    $ Battle_SelectLeftChar(BattleScene.BattleChars[0][0])
    $ Battle_SelectRightChar(BattleScene.BattleChars[1][0])

    # place perma status effs (faymore gear)
    $ Battle_PlacePermaStatusEffects()

    show screen Battle_BottomPanel()
    show screen Battle_TurnCounter()
    show screen Battle_CharSelectionPanels()
    with dissolve
    
    jump Battle_Loop

# loop through battle until either Win, Lose or Retreat is achieved
label Battle_Loop:
    $ Battle_AddLogEntry(tra(_("{color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}Battle starts!{/color}")))
    while BattleScene.Outcome == None:
        # new turn
        $ BattleScene.Turn += 1

        # 0 == left, 1 == right
        $ BattleScene.ActingSide = 0 
        while BattleScene.ActingSide != 2:
            $ Battle_TurnStartResetSkillsUsed(BattleScene.ActingSide)
            $ Battle_TurnStartRestoreEnergyOrMana(BattleScene.ActingSide)

            # do the status effect' effects
            $ Battle_StatusEffect_OnTurnStart(BattleScene.ActingSide)
            # tick all status effects duration
            $ Battle_TickStatusEffectDuration(BattleScene.ActingSide)
            $ Battle_LoopStep(0.15)
            if BattleScene.Turn != 1 and BattleScene.ActingSide == 0:
                $ Battle_AddLogEntry(tra(_("{color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}New turn: %s!{/color}")) % BattleScene.Turn)
                hide screen Battle_NewTurnEffect
                show screen Battle_NewTurnEffect()
                $ renpy.music.play(renpy.random.choice(soundLib["BattleNewTurn"]), channel = "sound", loop = False, relative_volume = 0.55)
            # gather all chars of this side who will act
            $ BattleScene.ActiveCharsList = Battle_GetAllCharsWhoCanAct(Side = BattleScene.ActingSide)
            $ Battle_UIAutoSelectIfOneAliveOnSide(Side = BattleScene.ActingSide)
            # run until all chars of this side has acted
            while len(BattleScene.ActiveCharsList) > 0:
                # only do turn if there's someone alive on the opposite side
                if len(Battle_GetAliveCharsOnSide(Side = (0 if BattleScene.ActingSide == 1 else 1))) > 0:
                    $ Battle_GatherAllTauntedCharsForSide(BattleScene.ActingSide)
                    if len(BattleScene.TauntedCharsForCurrentlyActiveSide) > 0:
                        $ Battle_AutoScheduleTauntedAttackForChar(BattleScene.TauntedCharsForCurrentlyActiveSide.pop())
                    else:
                        if BattleScene.AIControlSide[BattleScene.ActingSide] == True:
                            # ai controlled side
                            $ Battle_DoAITurn(renpy.random.choice(BattleScene.ActiveCharsList))
                        else:
                            # player-controlled
                            call screen Battle_ActionSelectPanel(WaitForPlayerInput = True)
                            show screen Battle_ActionSelectPanel()

                            # check if we need to pick skill target and enter targeting loop
                            while BattleScene.ActionAwaitingTarget is not None:
                                call screen Battle_CharSelectionPanels(SelectSkillTarget = True)
                            show screen Battle_CharSelectionPanels()
                # skip any remaining char's turn if no alive enemies present
                # acts like a "break"
                else:
                    $ BattleScene.ActiveCharsList.pop()

                if BattleScene.SelectedActionToProcess is not None:
                    $ BattleScene.SelectedActionToProcess.ActionInstance.DrainCosts()
                    $ BattleScene.SelectedActionToProcess.ActionInstance.Execute(BattleScene.SelectedActionToProcess.Target)
                    $ BattleScene.SelectedActionToProcess.ActionInstance.UsedThisTurn = BattleScene.SelectedActionToProcess.ActionInstance.OncePerTurn
                    $ BattleScene.SelectedActionToProcess = None

                    while len(BattleScene.ScheduledAttackQueue) > 0:
                        $ BattleScene.ScheduledActionToExecute = BattleScene.ScheduledAttackQueue.pop()
                        if BattleScene.ScheduledActionToExecute.UserBattleChar.IsAlive and any([BattleChar.IsAlive for BattleChar in BattleScene.ScheduledActionToExecute.TargetList]):
                            $ BattleScene.ScheduledActionToExecute.ExecuteAction()
                            $ BattleScene.ScheduledActionToExecute = None

                        # reason this exists is, if you enable autobattle and shift+r 
                        # or load a battle-save that had autobattle enabled, renpy chokes up
                        if BattleScene.AIControlSide[0] == True:
                            call screen Battle_AvoidEmptyLoopSpin()
                $ Battle_EndIfEitherSideDefeated(BattleScene)

            # tick all status effects duration
            $ Battle_TickStatusEffectDuration(BattleScene.ActingSide, AtEnd = True)
            $ BattleScene.ActingSide += 1
    jump Battle_Over

# battle has concluded, will handle either of 3 outcomes
label Battle_Over:
    $ TooltipClear()
    hide screen Battle_ActionSelectPanel
    hide screen Battle_BottomPanel
    $ Battle_HideCharInfoScreens()
    $ Battle_HideBattleVFXSprites()
    hide screen Battle_TurnCounter
    hide screen Battle_CharSelectionPanels
    scene black
    with dissolve

    if DEBUG_EndlessBattle:
        $ BattleScene = None
        scene black with dissolve
        return

    $ Assert(BattleScene.Outcome != None, "Battle is over but outcome is none, sth's fucked")

    $ BlockWaitDynamic(False)

    if BattleScene.Outcome == "victory":
        $ LastBattleOutcome = "victory"
        $ PlaySoundRandom("BattleWon", Volume = 0.7)

        $ BattleScene.PostBattleFlag = True
        $ Battle_ShowPostBattleLoot(BattleScene)

        $ Battle_StoreEnemyMatchupAndGrantVictoryExp(BattleScene)
        $ Battle_ApplyPlayerPartyHealthAndCarryOverStatusEffects()
        if BattleScene.Label_Victory:
            $ Battle_ClearSceneAndJumpTo(BattleScene.Label_Victory)

    if BattleScene.Outcome == "defeat":
        $ LastBattleOutcome = "defeat"
        $ PlaySoundRandom("BattleLost", Volume = 0.7)

        if BattleScene.Label_Defeat:
            $ Battle_ApplyPlayerPartyHealthAndCarryOverStatusEffects()
            $ Battle_ClearSceneAndJumpTo(BattleScene.Label_Defeat)
        elif BattleScene.ContinueOnDefeat:
            $ Battle_ApplyPlayerPartyHealthAndCarryOverStatusEffects()
            pass
        else:
            scene cg_lose with flash
            if BattleScene.Label_BattleDefeatExtraNarrative is not None:
                call expression BattleScene.Label_BattleDefeatExtraNarrative from _call_expression_1
            label Battle_Defeat_Menu:
            "You were defeated in battle."
            menu:
                "Restart battle":
                    call screen confirm(_("Restart battle?"), yes_action = Jump("Battle_Start"), no_action = Jump("Battle_Defeat_Menu"))
                "Load game":
                    call screen save_load(HideOnReturnBtn = True, BlockSave = True)
                    jump Battle_Defeat_Menu
                "Quit to main menu":
                    call screen confirm(_("Leave to main menu?"), yes_action = Function(renpy.full_restart), no_action = Jump("Battle_Defeat_Menu"))    
                "(DEV) continue" if config.developer:
                    $ Battle_ApplyPlayerPartyHealthAndCarryOverStatusEffects()
                    pass

    if BattleScene.Outcome == "retreat":
        $ LastBattleOutcome = "retreat"
        $ PlaySoundRandom("BattleLost", Volume = 0.7)
        $ Battle_ApplyPlayerPartyHealthAndCarryOverStatusEffects()
        if BattleScene.Label_Retreat:
            $ Battle_ClearSceneAndJumpTo(BattleScene.Label_Retreat)

    $ BattleScene = None
    scene black with dissolve
    return

screen Battle_AvoidEmptyLoopSpin():
    on "show" action Return()
