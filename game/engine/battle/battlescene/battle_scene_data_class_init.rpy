init python:
    class BattleData:
        def __init__(self,  BackgroundImage = None,
                            
                            CharIDList_Right = [],
                            CharIDList_Left = [], 
                            CharIDList_LeftExtra = [], 

                            AutoNightBackground = True,
                            CanRetreat = False,
                            CanAutoBattle = True,
                            GrantXp = True, 

                            RiggedOnWinLoot = dict(),
                            GiveLoot = True, # can be disabled (for arena fights)

                            CanTransform = True,
                            
                            Label_Victory = None,
                            Label_Defeat = None,
                            Label_Retreat = None,
                            Label_BattleDefeatExtraNarrative = None, # <- call into a label to show extra stuff on defeat, but within "restart menu" context

                            ContinueOnDefeat = False,

                            CanUseItems = True,
                            
                            TurnLimit = None,       # < integer, forces "defeat" after certain number of turns passed

                            LeftSideForcedAIControl = False, # for fully forced "auto battles" (arena)

                            ):

            self.BackgroundImage = BackgroundImage 

            self.CharIDList_Right = CharIDList_Right
            self.CharIDList_Left = CharIDList_Left 
            self.CharIDList_LeftExtra = CharIDList_LeftExtra 

            self.AutoNightBackground = AutoNightBackground

            self.CanRetreat = CanRetreat
            self.CanAutoBattle = CanAutoBattle
            self.CanTransform = CanTransform
            
            self.GrantXp = GrantXp 
            self.RiggedOnWinLoot = RiggedOnWinLoot # {"goblin_cleaver":3 "scout_sword":5}
            self.GiveLoot = GiveLoot

            # if not none these jump to the specified label on corresp. outcome
            # if none return control flow to right after battle
            self.Label_Victory = Label_Victory
            self.Label_Defeat = Label_Defeat
            self.Label_Retreat = Label_Retreat
            self.Label_BattleDefeatExtraNarrative = Label_BattleDefeatExtraNarrative

            self.ContinueOnDefeat = ContinueOnDefeat

            self.CanUseItems = CanUseItems

            self.TurnLimit = TurnLimit

            self.LeftSideForcedAIControl = LeftSideForcedAIControl
            return

    class BattleSceneClass(object):
        def __init__(self, BattleData):
            # looks trippy but all it does is auto-sets to night/day variant
            if BattleData.AutoNightBackground:
                if BattleData.BackgroundImage.endswith("_night"):
                    if IsDaytime():
                        if renpy.has_image(BattleData.BackgroundImage.removesuffix("_night")):
                            self.BackgroundImage = BattleData.BackgroundImage.removesuffix("_night")
                        else:
                            self.BackgroundImage = BattleData.BackgroundImage
                    else:
                        self.BackgroundImage = BattleData.BackgroundImage
                else:
                    if IsDaytime():
                        self.BackgroundImage = BattleData.BackgroundImage
                    else:
                        if renpy.has_image(BattleData.BackgroundImage + "_night"):
                            self.BackgroundImage = BattleData.BackgroundImage + "_night"
                        else:
                            self.BackgroundImage = BattleData.BackgroundImage
            else:
                self.BackgroundImage = BattleData.BackgroundImage

            self.CharIDList_Right = BattleData.CharIDList_Right

            self.CanRetreat = BattleData.CanRetreat
            self.CanAutoBattle = BattleData.CanAutoBattle
            self.CanTransform = BattleData.CanTransform
            
            self.GrantXp = BattleData.GrantXp

            # if not none these jump to the specified label on corresp. outcome
            # if none return control flow to right after battle
            self.Label_Victory = BattleData.Label_Victory
            self.Label_Defeat = BattleData.Label_Defeat
            self.Label_Retreat = BattleData.Label_Retreat
            self.Label_BattleDefeatExtraNarrative = BattleData.Label_BattleDefeatExtraNarrative

            self.ContinueOnDefeat = BattleData.ContinueOnDefeat

            self.CanUseItems = BattleData.CanUseItems

            self.TurnLimit = BattleData.TurnLimit

            # if left side list is not passed in, it will always grab PlayerCombatTeam var
            if len(BattleData.CharIDList_Left) == 0:
                MaximumChars = 4 - len(BattleData.CharIDList_LeftExtra)

                # case 1, player has more chars than maximum, 
                # do the stored char ids, then call for "select chars" screen
                if GetPartySize() > MaximumChars:
                    # if last combat team id list is not none, 
                    # auto-select the chars who were on the list, 
                    # then IF len of that list greater than max chars, trim
                    # then call screen 
                    if store.LastCombatTeam is not None:
                        setattr(store, "PlayerCombatTeam", [])

                        RemainingCharIDs = copy.copy(player_party)
                        for CharID in store.LastCombatTeam:
                            if CharInParty(CharID):
                                getattr(store, "PlayerCombatTeam").append(CharID)
                                RemainingCharIDs.remove(CharID)

                        # this *can* happen if our last stored combat team was larger than currently available one
                        if len(getattr(store, "PlayerCombatTeam")) > MaximumChars:
                            setattr(store, "PlayerCombatTeam", getattr(store, "PlayerCombatTeam")[:MaximumChars])
                            renpy.call_screen("select_combat_team", RightBeforeBattle = True, MaximumCharsForTeam = MaximumChars)
                        
                        # if we're less than max chars *and theres some remaining chars*,
                        # fill with them
                        elif len(getattr(store, "PlayerCombatTeam")) < MaximumChars:
                            if (len(getattr(store, "PlayerCombatTeam")) + len(RemainingCharIDs)) <= MaximumChars:
                                setattr(store, "PlayerCombatTeam", getattr(store, "PlayerCombatTeam") + RemainingCharIDs)
                            else:
                                while len(getattr(store, "PlayerCombatTeam")) < MaximumChars:
                                    getattr(store, "PlayerCombatTeam").append(RemainingCharIDs.pop())
                                renpy.call_screen("select_combat_team", RightBeforeBattle = True, MaximumCharsForTeam = MaximumChars)
                        
                        else:
                            if len(RemainingCharIDs) > 0:
                                renpy.call_screen("select_combat_team", RightBeforeBattle = True, MaximumCharsForTeam = MaximumChars)

                    # else just auto-select then call screen
                    else:
                        setattr(store, "PlayerCombatTeam", player_party[:MaximumChars])
                        renpy.call_screen("select_combat_team", RightBeforeBattle = True, MaximumCharsForTeam = MaximumChars)

                # case 2, player has less chars than maximum. if autofill is true, then autofill, else call for screen
                else:
                    if persistent.BattlePref_AutoFillPlayerCombatTeam:
                        setattr(store, "PlayerCombatTeam", player_party[:MaximumChars])
                    else:
                        renpy.call_screen("select_combat_team", RightBeforeBattle = True, MaximumCharsForTeam = MaximumChars)

                # the list of left chars is now finalized, set the variable
                self.CharIDList_Left = copy.deepcopy(getattr(store, "PlayerCombatTeam"))
                # and also store the Last Used Combat Team
                store.LastCombatTeam = getattr(store, "PlayerCombatTeam")

            # if the left list is passed in, use it
            else:
                self.CharIDList_Left = BattleData.CharIDList_Left

            # make sure any "extras" we put into the battle are prioritized
            # a battle initiated with PlayerCombatTeam + ["ves"] will 100% have ves present
            self.CharIDList_Left = (self.CharIDList_Left + BattleData.CharIDList_LeftExtra)[-4:]

            Assert(4 >= len(self.CharIDList_Left) > 0,  "Left side is empty/too big, wtf!")
            Assert(4 >= len(self.CharIDList_Right) > 0, "Right side is empty/too big, wtf!")

            # 0 are left side 1 are right side
            self.BattleChars = {}
            self.BattleChars[0] = Battle_ConvertCharIDListToBattleChars(self.CharIDList_Left)
            self.BattleChars[1] = Battle_ConvertCharIDListToBattleChars(self.CharIDList_Right, Side = 1)

            self.ItemPools = {}

            self.ItemPools[0] = player_inv
            self.ItemPools[1] = {} # unused, eventually will be enemy-used items. EVENTUALLY

            # BattleSide:{ItemID:Qty}
            # for restart only, will re-add this many items to corresp itempools
            self.ItemsRemovedDuringBattle = {0:{}, 1:{}}

            # a list of [{item_id:qty}, {item_id:qty}], this DOESNT insantiate post battle loot items!
            # these are instantiated (and discarded if necessary) on victory
            self.ItemsToBeDroppedOnVictory = []

            if BattleData.GiveLoot == True:
                for CharID in BattleData.CharIDList_Right:
                    # "to_level" case, only grab id
                    if isinstance(CharID, dict):
                        CharID = list(CharID.keys())[0]
                    # if char id has no loot drop data, bail
                    if CharID not in LootDropData:
                        continue
                    
                    # work through lootdrop entries and assemble resulting ItemID:Qty collection
                    for ItemEntryDict in LootDropData[CharID]:
                        DropItemID = ItemEntryDict["ItemID"]
                        DropItemMinDropRolls = ItemEntryDict["MinDropRolls"]
                        DropItemMaxDropRolls = ItemEntryDict["MaxDropRolls"]
                        DropChance = ItemEntryDict["ChancePerSingleEntry"]
                        if "AmountPerSingleEntry" in ItemEntryDict:
                            AmountPerSingleEntry = ItemEntryDict["AmountPerSingleEntry"]
                        else:
                            AmountPerSingleEntry = 1

                        DropRolls = renpy.random.randint(DropItemMinDropRolls, DropItemMaxDropRolls)
                        SuccRolls = 0
                        for i in range(DropRolls):
                            if RngFloat(0.0, 1.0) > DropChance:
                                continue
                            else:
                                SuccRolls += 1

                        if SuccRolls > 0:
                            self.ItemsToBeDroppedOnVictory.append({DropItemID:SuccRolls * AmountPerSingleEntry})

                # add rigged loot to items to be dropped
                for ItemID, ItemQty in BattleData.RiggedOnWinLoot.items():
                    self.ItemsToBeDroppedOnVictory.append({ItemID:ItemQty})

            # for restarting the battle
            self.StoredPlayerInfectionValue = InfectionModule().CurrentValue


            self.Turn = 0
            self.Outcome = None # "victory", "defeat", "retreat"

            self.LogEntries = []

            self.SelectedActionToProcess = None

            self.ScheduledAttackQueue = []
            self.ScheduledActionToExecute = None

            self.SelectedLeft = None
            self.SelectedRight = None

            self.AIControlSide = {0: False, 1: True}

            if BattleData.LeftSideForcedAIControl:
                self.AIControlSide[0] = True
                # be aware, this below overrides previous assignment in the same call! order matters
                self.CanAutoBattle = False 
            else:
                if self.CanAutoBattle:
                    self.AIControlSide[0] = (True if persistent.BattlePref_AutoBattleByDefault else False)

            self.ActingSide = 0

            self.ActiveCharsList = []

            # if this is not None, click-to-select-char behaviour changes
            self.ActionAwaitingTarget = None 
            # if action is awaiting target, this list is assumed to list all possible targets
            self.ActionAwaitingTarget_PotentialTargetsList = []

            # only for taunted chars
            self.TauntedCharsForCurrentlyActiveSide = []

            self.NextFloatingValScreenIndex = 0

            self.PostBattleGlobalPoison = dict() # battlechar:poisonduration

            # this is ONLY for inventory description check to tell that we're both "in battle" and "in loot screen"
            self.PostBattleFlag = False

    # reset all chars to their original state
    def Battle_ReinitializeScene(TargetBattleScene):
        InfectionModule().CurrentValue = TargetBattleScene.StoredPlayerInfectionValue

        TargetBattleScene.BattleChars[0] = Battle_ConvertCharIDListToBattleChars(TargetBattleScene.CharIDList_Left)
        TargetBattleScene.BattleChars[1] = Battle_ConvertCharIDListToBattleChars(TargetBattleScene.CharIDList_Right, Side = 1)

        TargetBattleScene.Outcome = None
        TargetBattleScene.Turn = 0

        TargetBattleScene.LogEntries = []

        TargetBattleScene.SelectedActionToProcess = None
        
        TargetBattleScene.ScheduledAttackQueue = []
        TargetBattleScene.ScheduledActionToExecute = None

        TargetBattleScene.SelectedLeft = None
        TargetBattleScene.SelectedRight = None

        TargetBattleScene.ActingSide = 0
        TargetBattleScene.ActiveCharsList = []

        TargetBattleScene.ActionAwaitingTarget = None
        TargetBattleScene.ActionAwaitingTarget_PotentialTargetsList = []

        TargetBattleScene.TauntedCharsForCurrentlyActiveSide = []
        TargetBattleScene.PostBattleGlobalPoison = dict()

        for SideID in range(2):
            for ItemID, ItemQty in TargetBattleScene.ItemsRemovedDuringBattle[SideID].items():
                AddItemTo(TargetBattleScene.ItemPools[SideID], ItemID, ItemQty)

        TargetBattleScene.ItemsRemovedDuringBattle = {0:{}, 1:{}}

        return
