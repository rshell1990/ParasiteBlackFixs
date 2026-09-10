default DEBUG_EndlessBattle = False
define BattleChar_SpriteZorder = {0: {0: (5, 6), 1: (1, 2), 2: (7, 8), 3: (3, 4)}, 1: {0: (5, 6), 1: (1, 2), 2: (7, 8), 3: (3, 4)}}
define BattleChar_ScreenPositions = {0: {0: (720, 730), 1: (560, 440), 2: (340, 740), 3: (230, 455)}, 1: {0: (1200, 730), 1: (1360, 440), 2: (1580, 740), 3: (1690, 455)}}
default BattleChar_ScreenPositions_Offset = {0: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}, 1: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}}
default BattleChar_ScreenPositions_Offset_Anim = {0: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}, 1: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}}
default BattleChar_ScreenPositions_Offset_Anim_Active = {0: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}, 1: {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0)}}
default BattleScene_ActiveChar = None
default BattleScene_ActiveChar_Anim = None

# Real-time countdown battle timer state variables
default battle_realtime_timer = 0.0
default battle_realtime_timer_active = False

# Screen for rendering and driving the real-time battle countdown
screen Battle_RealtimeCountdown():
    zorder 100
    
    if store.battle_realtime_timer_active:
        timer 0.1 repeat True action SetVariable("battle_realtime_timer", max(0.0, store.battle_realtime_timer - 0.1))

        frame:
            align (0.5, 0.02)
            padding (20, 10)
            background "#000000aa"
            text _("TIME REMAINING: [battle_realtime_timer:.1f]s") size 26 color "#FF4444" bold True align (0.5, 0.5)

        if store.battle_realtime_timer <= 0.0:
            timer 0.01 action [
                Function(Battle_StopRealtimeTimer),
                Function(Battle_Lose)
            ]

init python:
    BattleData = None
    BattleSceneClass = None
    BattleSetup_GetAllCharsWithSkin = None

    def Battle_StartRealtimeTimer(seconds):
        """Starts a real-time battle countdown for the specified duration in seconds."""
        store.battle_realtime_timer = float(seconds)
        store.battle_realtime_timer_active = True
        renpy.show_screen("Battle_RealtimeCountdown")

    def Battle_StopRealtimeTimer():
        """Stops and clears the real-time countdown screen."""
        store.battle_realtime_timer_active = False
        renpy.hide_screen("Battle_RealtimeCountdown")

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
        BattleScene.ActionAwaitingTarget = None
        return

    def Battle_Setup(BattleDataObj, BattleSceneClassObj, BattleSetup_GetAllCharsWithSkinFunc):
        global BattleData, BattleSceneClass, BattleSetup_GetAllCharsWithSkin
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
        for StatusEffect in getattr(BattleChar, "StatusEffects", []):
            if getattr(StatusEffect, "ID", None) == StatusEffectID:
                return True
        return False

    def Battle_GetAllCharsWhoCanAct(Side = None):
        ReturnList = Battle_GetAliveCharsOnSide(Side)
        for BattleChar in reversed(ReturnList):
            if Battle_HasStatusEffect(BattleChar, "stun") or Battle_HasStatusEffect(BattleChar, "freeze"):
                ReturnList.remove(BattleChar)
        return ReturnList

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
        for BattleChar in Battle_GetAllCharsOnSide(Side):
            for StatusEffect in copy.copy(BattleChar.StatusEffects):
                StatusEffect.TickDuration(AtEnd)
        return

    def Battle_StatusEffect_OnTurnStart(Side):
        for BattleChar in Battle_GetAllCharsOnSide(Side):
            for StatusEffect in copy.copy(BattleChar.StatusEffects):
                StatusEffect.OnTurnStart()
        return

    def Battle_StatusEffect_OnTurnEnd(Side):
        for BattleChar in Battle_GetAliveCharsOnSide(Side):
            for StatusEffect in copy.copy(BattleChar.StatusEffects):
                StatusEffect.OnTurnEnd()

    def Battle_DoAITurn(BattleChar):
        if Battle_HasStatusEffect(BattleChar, "freeze") or Battle_HasStatusEffect(BattleChar, "stun"):
            Battle_ForceEndTurnForChar(BattleChar)
            return

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

    def StartBattle(BattleDataObj):
        store.BattleScene = BattleSceneClass(BattleDataObj)
        renpy.call("Battle_Start")
        return

    def IsPlayerInBattle():
        return store.BattleScene is not None

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
        if BattleScene.GrantXp == False:
            return 

        NewCharIDList_Right = []
        for Entry in BattleScene.CharIDList_Right:
            if isinstance(Entry, dict):
                AsList = list(Entry.keys())
                CharID = AsList[0]
                TargetLevel = Entry[CharID]
                NewCharIDList_Right.append(CharID + "_lv" + str(TargetLevel))
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
                for ItemID, Qty in ItemEntry.items():
                    AddItemTo(TemporaryLootContainer, ItemID, Amount = Qty)
            if persistent.BattlePref_AutoLootAll:
                TakeAllItems(TemporaryLootContainer, Silent = False)
            else:
                renpy.call_screen("container", TemporaryLootContainer, ContainerName = _("Battle loot"), DoReturn = True, DoReturnOnTakeAll = True)
                if len(TemporaryLootContainer) > 0:
                    for ItemID, ItemQty in copy.copy(TemporaryLootContainer).items():
                        RemItemFrom(TemporaryLootContainer, ItemID, Amount = ItemQty)

    def Battle_GatherAllTauntedCharsForSide(Side):
        BattleScene.TauntedCharsForCurrentlyActiveSide = [BattleChar for BattleChar in Battle_GetAliveCharsOnSide(Side) if (Battle_HasStatusEffect(BattleChar, "taunt") and BattleChar in BattleScene.ActiveCharsList)]
        return

    def Battle_AutoScheduleTauntedAttackForChar(BattleChar):
        Battle_SetCharAction(BattleChar, BattleChar.Skill_Attack, Battle_GetStatusEffect(BattleChar, "taunt").TauntedBy)
        return

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
            BattleCharsAmt = len(CharList)

            for idx in range(min(BattleCharsAmt, 6)):
                CharList[idx].PositionSlotIndex = idx

            for Char in CharList:
                Char.SpriteZorder = BattleChar_SpriteZorder[Char.BattleSide][Char.PositionSlotIndex][0]
                Char.HudZorder = BattleChar_SpriteZorder[Char.BattleSide][Char.PositionSlotIndex][1]

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
    $ Battle_SetCharPositionsAndZorder()
    $ Battle_OnStartShowChars()

    $ Battle_SelectLeftChar(BattleScene.BattleChars[0][0])
    $ Battle_SelectRightChar(BattleScene.BattleChars[1][0])

    $ Battle_PlacePermaStatusEffects()

    show screen Battle_BottomPanel()
    show screen Battle_TurnCounter()
    show screen Battle_CharSelectionPanels()
    with dissolve
    
    jump Battle_Loop

label Battle_Loop:
    $ Battle_AddLogEntry(tra(_("{color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}Battle starts!{/color}")))
    while BattleScene.Outcome == None:
        $ BattleScene.Turn += 1
        $ BattleScene.ActingSide = 0 
        
        while BattleScene.ActingSide < 2:
            $ Battle_TurnStartResetSkillsUsed(BattleScene.ActingSide)
            $ Battle_TurnStartRestoreEnergyOrMana(BattleScene.ActingSide)

            $ Battle_StatusEffect_OnTurnStart(BattleScene.ActingSide)
            $ Battle_TickStatusEffectDuration(BattleScene.ActingSide)
            $ Battle_LoopStep(0.15)
            
            if BattleScene.Turn != 1 and BattleScene.ActingSide == 0:
                $ Battle_AddLogEntry(tra(_("{color=[BATTLE_COLORS_LOG.BATTLE_STATUS]}New turn: %s!{/color}")) % BattleScene.Turn)
                hide screen Battle_NewTurnEffect
                show screen Battle_NewTurnEffect()
                $ renpy.music.play(renpy.random.choice(soundLib["BattleNewTurn"]), channel = "sound", loop = False, relative_volume = 0.55)
            
            $ BattleScene.ActiveCharsList = Battle_GetAllCharsWhoCanAct(Side = BattleScene.ActingSide)
            $ Battle_UIAutoSelectIfOneAliveOnSide(Side = BattleScene.ActingSide)
            
            while len(BattleScene.ActiveCharsList) > 0:
                if len(Battle_GetAliveCharsOnSide(Side = (0 if BattleScene.ActingSide == 1 else 1))) > 0:
                    $ Battle_GatherAllTauntedCharsForSide(BattleScene.ActingSide)
                    if len(BattleScene.TauntedCharsForCurrentlyActiveSide) > 0:
                        $ Battle_AutoScheduleTauntedAttackForChar(BattleScene.TauntedCharsForCurrentlyActiveSide.pop())
                    else:
                        if BattleScene.AIControlSide[BattleScene.ActingSide] == True:
                            $ Battle_DoAITurn(renpy.random.choice(BattleScene.ActiveCharsList))
                        else:
                            call screen Battle_ActionSelectPanel(WaitForPlayerInput = True)
                            show screen Battle_ActionSelectPanel()

                            while BattleScene.ActionAwaitingTarget is not None:
                                call screen Battle_CharSelectionPanels(SelectSkillTarget = True)
                                $ BattleScene.ActionAwaitingTarget = None
                            show screen Battle_CharSelectionPanels()
                else:
                    $ BattleScene.ActiveCharsList.pop()

                if BattleScene.SelectedActionToProcess is not None:
                    $ BattleScene.SelectedActionToProcess.ActionInstance.DrainCosts()
                    $ BattleScene.SelectedActionToProcess.ActionInstance.Execute(BattleScene.SelectedActionToProcess.Target)
                    $ BattleScene.SelectedActionToProcess.ActionInstance.UsedThisTurn = BattleScene.SelectedActionToProcess.ActionInstance.OncePerTurn
                    $ BattleScene.SelectedActionToProcess = None

                while len(BattleScene.ScheduledAttackQueue) > 0:
                    $ BattleScene.ScheduledActionToExecute = BattleScene.ScheduledAttackQueue.pop()

                    if BattleScene.ScheduledActionToExecute is not None:
                        $ ActionAllowsDead = getattr(BattleScene.ScheduledActionToExecute, "AllowDeadTargets", False)
                        $ ValidTargetPresent = any([BattleChar.IsAlive or ActionAllowsDead for BattleChar in BattleScene.ScheduledActionToExecute.TargetList])

                        if BattleScene.ScheduledActionToExecute.UserBattleChar.IsAlive and ValidTargetPresent:
                            $ Attacker = BattleScene.ScheduledActionToExecute.UserBattleChar
                            
                            if Battle_HasStatusEffect(Attacker, "freeze") or Battle_HasStatusEffect(Attacker, "stun"):
                                $ AttackerName = getattr(Attacker, "DisplayName", getattr(Attacker, "CharID", "Unit"))
                                $ Battle_AddLogEntry(tra(_("%s is frozen and cannot act!")) % AttackerName)
                            else:
                                $ BattleScene.ScheduledActionToExecute.ExecuteAction()

                            $ BattleScene.ScheduledActionToExecute = None

                    if BattleScene.AIControlSide[0] == True:
                        call screen Battle_AvoidEmptyLoopSpin()
                $ Battle_EndIfEitherSideDefeated(BattleScene)

            $ Battle_TickStatusEffectDuration(BattleScene.ActingSide, AtEnd = True)
            $ BattleScene.ActingSide += 1
    jump Battle_Over

label Battle_Over:
    $ TooltipClear()
    $ Battle_StopRealtimeTimer() # Cleans up and stops the countdown timer
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