# each distinct map node needs:
# 1) an entry in Travel_NodeLogicLabels to map node type ID to a label
# 2) an entry (or entries plural) in Travel_RandomNodesForBiomes to make it spawn randomly
# 3) an entry in NODE_TYPE_IMAGE_MAP that maps node type ID to an image name, for map token
# 4) an entry in NODE_PATHFIND_WEIGHTS to tell how dangerous this node is for safe-first pathfinding
# check all 4 to add a new node type.
# the label target label from #1 is your content entry point,
# use GetOutToWorldMap() to quickly end whatever's inside the node

init -1 python:
    # each route is defined into this dict in sep. files
    TravelRoutes = {}

    # maps NodeTypeID:Label
    Travel_NodeLogicLabels = {
        "normal" :"travel_node_logic_normal",
        "enemy"  :"travel_node_logic_enemy",
        "safe"   :"travel_node_logic_safe",
        "nature" :"travel_node_logic_nature",
        "mine"   :"travel_node_logic_mine",

        "fortress_inn_cat"   :"travel_node_logic_tavern_cat",
        "fortress_inn_wench" :"travel_node_logic_tavern_wench",
        "fortress_inn_frog"  :"travel_node_logic_tavern_frog",
    }

    # maps biome:NodeTypeID:weighted chance
    Travel_RandomNodesForBiomes = {
        # stick to 100 sum in each of these
        "forest":{
            # 85% for stuff
            "normal" :17,
            "enemy"  :17,
            "safe"   :17,
            "nature" :17,
            "mine"   :17,
            "fortress_inn_cat":5,
            "fortress_inn_wench":5,
            "fortress_inn_frog":5,
        },
        "desert":{
            "normal" :20,
            "enemy"  :20,
            "safe"   :20,
            "nature" :20,
            "mine"   :20,
        },
    }

    # maps NodeTypeID to image name
    NODE_TYPE_IMAGE_MAP = {
        "normal":   "node_content_random",
        "nature":   "node_content_nature",
        "mine":     "node_content_mine",
        "safe":     "node_content_camp",
        "exit":     "node_content_exit",
        "enemy":    "node_content_enemy",
        "fortress_inn_cat":   "node_content_fortress_inn",
        "fortress_inn_wench": "node_content_fortress_inn",
        "fortress_inn_frog":  "node_content_fortress_inn",
        
    }

    # maps NodeTypeID to safe-first pathfinding weights
    NODE_PATHFIND_WEIGHTS = {
        "normal":   3, 
        "safe":     1,
        "exit":     1, 
        "mine":     1,
        "enemy":    1000,
        "nature":   2,
        "fortress_inn_cat":   1,
        "fortress_inn_wench": 1,
        "fortress_inn_frog":  1,

    }

# for the 50 locs achievement
default persistent.Travel_TotalEnteredNodes = 0

# this can be null-checked to tell if player is traveling
default TravelState = None

# 0 -- fastest, 1 -- safest
default Travel_PathingMode = 0

# toggle to make ctrl skip "space to proceed"
default persistent.TravelPref_SkipMap = False

# this is dynamic and will store path_ID:{node_ID:type, node_ID:type}
# updated each midnight IF we're outside of travel mode
default TravelRoutes_RandomNodes = {}

# so this loop is we're in "travel mode"
label Travel_MainLoop:
    $ LocSet("travel_node_generic")
    $ LocFlush(dissolve)

    # we "call" travel map screen in input context.
    # if on show there is more nodes to traverse, "hit space to continue".
    # clicking will set our new target and close the screen.
    if TravelState is not None:
        call screen map(OpenTab = "travel", Context = "travel_input", RouteID = TravelState.RouteID)
        # this ugly _return crutch is the only way i could hastily duct tape the "fastest/safest reset" bug -tmm 
        $ Travel_PathingMode = _return
    # this branch will only (hopefully) be executed in save-recover cases
    else:
        $ LocSet("novaras_gates")
        $ LocEnter()

    label Travel_MainLoop_PostInput:
    # then we do "move to target node" routine:
    # store comingfrom (for animation)
    $ TravelState.NodeIndex_ComingFrom = TravelState.NodeIndex_Current
    # and set our new position to first one on the path to that target node
    $ Travel_SetCurrentNodeDuringTravelAndClearTarget()

    # re-show TravelMap screen with move-to parameters for anim
    call screen map(OpenTab = "travel", Context = "travel_animate", Travel_Animate_FromNode = TravelState.NodeIndex_ComingFrom, RouteID = TravelState.RouteID)
    # this ugly _return crutch is the only way i could hastily duct tape the "fastest/safest reset" bug -tmm 
    $ Travel_PathingMode = _return

    $ Travel_AdvanceTimeToNextNode()

    $ persistent.Travel_TotalEnteredNodes += 1
    if persistent.Travel_TotalEnteredNodes >= 50 and can_unlock_achievement("YOU_ARE_GOING_PLACES"):
        $ unlock_achievement("YOU_ARE_GOING_PLACES")

    # after anim ends,
    # we process node we're at.
    # if we're at exit, we hide the map and jump into the location
    if Travel_GetNodeType(TravelState.RouteID, TravelState.NodeIndex_Current) == "exit":
        if TravelState.CurrentPath == None:
            $ LocSet(TravelRoutes[TravelState.RouteID]["travel_nodes"][TravelState.NodeIndex_Current]["exit_location_tag"])
            $ TravelState = None
            $ LocEnter()
        else:
            $ LocFlush(dissolve)
            jump Travel_MainLoop
    else:
        $ LocFlush(dissolve)
        $ Travel_CallEventLabel(TravelState.RouteID, TravelState.NodeIndex_Current)
        $ Travel_RollPartyBanter_Map()
        # loop back to the top
        jump Travel_MainLoop

init python:
    class TravelPath:
        def __init__(self, Nodes, TotalHours):
            self.Nodes = Nodes
            self.TotalHours = TotalHours

    class TravelStateClass:
        def __init__(self, RouteID, EnterNodeIndex, InitialPath):
            self.RouteID = RouteID
            self.NodeIndex_Current = EnterNodeIndex
            self.CurrentPath = InitialPath
            # for anim
            self.NodeIndex_ComingFrom = None 
        
            LocationID_A = TravelRoutes[RouteID]["connects_locations"][0]
            LocationID_B = TravelRoutes[RouteID]["connects_locations"][1]

            self.RecenterLocation = (int(0.5 * wLocs[LocationID_A].wMap_spritePos[0] + 0.5 * wLocs[LocationID_B].wMap_spritePos[0]), 
                                    int(0.5 * wLocs[LocationID_A].wMap_spritePos[1] + 0.5 * wLocs[LocationID_B].wMap_spritePos[1]))

    # this exists to bind into onMidnight, nothing more
    # NOPE it also hotswaps bgs!
    @AppendToAllQuests
    class TravelNodesRandomizer(LogicModule):
        def __init__(self):
            super().__init__()
            self.RandomizeNodes()

        def onStart(self):
            self.RandomizeNodes()

        def OverrideLocBg(self):
            Result = {}
            if TravelState is not None:
                Result["travel_node_generic"] = store.TravelRoutes[TravelState.RouteID]["image_loc_bg"]
            return Result

        def onMidnight(self):
            self.RandomizeNodes()
            return

        def RandomizeNodes(self):
            if store.TravelState is None:
                store.TravelRoutes_RandomNodes = {}
                for RouteID, RouteData in store.TravelRoutes.items():
                    store.TravelRoutes_RandomNodes[RouteID] = {}
                    # get total weights number
                    # roll random int between 0 and total weight number
                    # store cummulative weight
                    # iterate dict while incrementing cummulative weght
                    # if target is less or equals than cumm weight, return result
                    BiomeType = RouteData["biome_type"]
                    Assert(BiomeType in Travel_RandomNodesForBiomes, "must define random node weights for %s in Travel_RandomNodesForBiomes" % RouteData["biome_type"])
                    TotalWeight = sum(Travel_RandomNodesForBiomes[BiomeType].values())
                    for NodeIndex, NodeData in RouteData["travel_nodes"].items():
                        if "type" not in NodeData or NodeData["type"] == "random":
                            Done = False
                            Target = RngInt(1, TotalWeight)
                            CummWeight = 0
                            for NodeTypeID, Weight in Travel_RandomNodesForBiomes[BiomeType].items():
                                CummWeight += Weight
                                if Target <= CummWeight:
                                    store.TravelRoutes_RandomNodes[RouteID][NodeIndex] = NodeTypeID
                                    Done = True
                                    break
            return

    # shows clickable place on a world map
    def WorldMapLocAdd(LocID):
        store.seenWMapLocTags.add(LocID)
        return

    # for map screen, shows quest markers
    def IsWorldMapLocTracked(LocID):
        for qstObj in GetAllActiveQuests():
            if qstObj.isTracked:
                for GoalKey, GoalVal in qstObj.GoalStates.items():
                    if GoalVal == GoalState.VISIBLE:
                        TrackTagsWorldMap = []
                        if qstObj.GOALS[GoalKey].trackTagWorldMap is not None:
                            if isinstance(qstObj.GOALS[GoalKey].trackTagWorldMap, list):
                                TrackTagsWorldMap = qstObj.GOALS[GoalKey].trackTagWorldMap
                            else:
                                TrackTagsWorldMap = [qstObj.GOALS[GoalKey].trackTagWorldMap]
                        for TrackTag in TrackTagsWorldMap:
                            if LocID == TrackTag:
                                return True

    def Travel_GetCurrentBiome():
        if TravelState is not None:
            return TravelRoutes[TravelState.RouteID]["biome_type"]
        else:
            return None

    def Travel_AdvanceTimeToNextNode():
        Hours = Travel_GetConnectionCostInHours(TravelState.RouteID, TravelState.NodeIndex_Current, TravelState.NodeIndex_ComingFrom)
        while Hours > 0:
            TimeAdvBy(TIME_1H)
            Hours -= 1
            #renpy.say(None, "advanced time by 1h")
            renpy.pause(0.1)
        return

    def Travel_GetConnectionCostInHours(RouteID, NodeA, NodeB):
        PathCostsInHours = TravelRoutes[RouteID].get("path_costs_in_hours", {})
        Connection = (NodeA, NodeB)
        if Connection in PathCostsInHours:
            Result = PathCostsInHours[Connection]
        else:
            if (Connection[1], Connection[0]) in PathCostsInHours:
                Result = PathCostsInHours[(Connection[1], Connection[0])]
            else:
                Result = 4
        if config.developer:
            Connections = TravelRoutes[RouteID]["travel_paths"]
            for HoursConnection, Cost in PathCostsInHours.items():
                Assert(HoursConnection in Connections, "ERROR: path costs dict for route ID %s has a mismatched connection defined: (%s, %s)" % (RouteID, HoursConnection[0], HoursConnection[1]))

        return Result

    def Travel_SetCurrentNodeDuringTravelAndClearTarget():
        # if there's any path (a list of nodes), traverse
        if TravelState.CurrentPath is not None:
            # traverse means just set our current index as next popped one
            TravelState.NodeIndex_Current = TravelState.CurrentPath.Nodes.pop(0)
            TravelState.CurrentPath.TotalHours -= Travel_GetConnectionCostInHours(TravelState.RouteID, TravelState.NodeIndex_Current, TravelState.NodeIndex_ComingFrom)
            # delete path if we're there
            if len(TravelState.CurrentPath.Nodes) == 0:
                TravelState.CurrentPath = None
        return

    def Travel_CallEventLabel(RouteID, NodeIndex):
        NodeType = Travel_GetNodeType(RouteID, NodeIndex)
        #EventLabel = store.TravelRoutes[RouteID]["node_labels"][NodeType]
        EventLabel = Travel_NodeLogicLabels[NodeType]
        renpy.call(EventLabel)
        return

    # CAREFUL with this shit
    def Travel_ForceEnd():
        store.TravelState = None
        return

    # looks in random nodes if need be
    def Travel_GetNodeType(RouteID, NodeIndex):
        Result = None
        DefinedNodeType = store.TravelRoutes[RouteID]["travel_nodes"][NodeIndex].get("type", None)
        if DefinedNodeType is not None and DefinedNodeType != "random":
            return DefinedNodeType
        else:
            return store.TravelRoutes_RandomNodes[RouteID][NodeIndex]

    def GetOutToWorldMap():
        renpy.jump("Travel_MainLoop")
        return

    def IsPlayerTraveling():
        if store.TravelState is not None:
            return True
        else:
            return False

    def Travel_GetNodeDesc(RouteID, NodeIndex, NodeData, AutoPathMode):
        Result = ""
        ### main desc line
        if Travel_GetNodeType(RouteID, NodeIndex) == "normal":
            Result += tra(_("Anything can happen at this place. We should watch out."))
        elif Travel_GetNodeType(RouteID, NodeIndex) == "safe":
            Result += tra(_("This area seems safe: we can set up a camp there."))
        elif Travel_GetNodeType(RouteID, NodeIndex) == "enemy":
            Result += tra(_("We will certainly walk into a fight there."))
        elif Travel_GetNodeType(RouteID, NodeIndex) == "nature":
            Result += tra(_("There are wild creatures roaming about this place."))
        elif Travel_GetNodeType(RouteID, NodeIndex) == "mine":
            Result += tra(_("There is an abandoned mine at this place."))
        elif Travel_GetNodeType(RouteID, NodeIndex) in ["fortress_inn_cat", "fortress_inn_wench", "fortress_inn_frog"]:
            Result += tra(_("There is an inn at this place."))
        # exit is checked directly from nodedata bc it cant be randomized
        elif NodeData["type"] == "exit":
            Result += tra(wLocs[NodeData["exit_location_tag"]].displayName)
        if TravelState:
            if NodeIndex == TravelState.NodeIndex_Current:
                Result += "\n"
                Result += tra(_("You are here"))
            else:
                Path = Travel_FindPath(RouteID, TravelState.NodeIndex_Current, NodeIndex, AutoPathMode)
                ### time estimated
                Result += "\n"
                Result += "{image=[ICON.CLOCK]} "
                Result += tra(_("%s hours")) % Path.TotalHours
        else:
            if NodeIndex == Travel_FindPlayerAtEitherExitPoint(RouteID):
                Result += "\n"
                Result += tra(_("You are here"))
            else:
                Path = Travel_FindPath(RouteID, Travel_FindPlayerAtEitherExitPoint(RouteID), NodeIndex, AutoPathMode)
                ### time estimated
                Result += "\n"
                Result += "{image=[ICON.CLOCK]} "
                Result += tra(_("%s hours")) % Path.TotalHours

        ShowDebugStuff = False
        if config.developer and ShowDebugStuff:
            Result += "{color=#a3a3a3}"
            Result += "\nDEV: Node idx: %s" % NodeIndex
            Result += "\nDEV: RouteID: %s" % RouteID
            Result += "\nDEV: Node type: %s" % Travel_GetNodeType(RouteID, NodeIndex)
            Result += "{/color}"

        return Result

    def Travel_GetRouteID(From_ID, To_ID):
        for RouteID, RouteData in store.TravelRoutes.items():
            if From_ID in RouteData["connects_locations"] and To_ID in RouteData["connects_locations"]:
                return RouteID

    def Travel_FindPlayerAtEitherExitPoint(RouteID):
        for NodeID, NodeData in TravelRoutes[RouteID]["travel_nodes"].items():
            if NodeData.get("exit_location_tag") == GetLocID():
                return NodeID
        return None

    def Travel_DEBUG_InitiateJump(RouteID, ClickedNode):
        store.TravelState = TravelStateClass(RouteID, ClickedNode, None)
        LocSet("travel_node_generic")
        renpy.jump("Travel_MainLoop_PostInput")
        return

    def Travel_InitiateTravel(RouteID, InitialNode, ClickedNode, PassedInPath):
        store.TravelState = TravelStateClass(RouteID, InitialNode, ClickedNode)
        store.TravelState.CurrentPath = PassedInPath
        LocSet("travel_node_generic")
        renpy.jump("Travel_MainLoop_PostInput")
        return

    def Travel_FindPath(RouteID, FromNodeIndex, TargetNodeIndex, AutoPathMode = None):
        store.Travel_PathingMode = AutoPathMode

        Connections = list(TravelRoutes[RouteID]["travel_paths"].keys())

        from queue import PriorityQueue
        FrontierQueue = PriorityQueue()
        # (weight , hours , node)
        FrontierQueue.put((0, 0, FromNodeIndex))

        ComingFrom = {FromNodeIndex : None}

        WeightedCostSoFar = {FromNodeIndex : 0}   # “safety weight”
        HoursCostSoFar    = {FromNodeIndex : 0}   # real-time hours

        while not FrontierQueue.empty():
            CurrentNodeIndex = FrontierQueue.get()[2]

            if CurrentNodeIndex == TargetNodeIndex:
                break

            AllConnectedNodeIndexes = {
                c[0] if c[1] == CurrentNodeIndex else c[1]
                for c in Connections if CurrentNodeIndex in c
            }

            for ConnectedNode in AllConnectedNodeIndexes:
                hrs = Travel_GetConnectionCostInHours(RouteID, CurrentNodeIndex, ConnectedNode)

                # this dont seem 2work tbh, 
                # tie-breaker :  weight first, hours second
                if AutoPathMode == 0:
                    w = hrs # fastest
                else:
                    w = NODE_PATHFIND_WEIGHTS[Travel_GetNodeType(RouteID, ConnectedNode)] # safest

                new_w  = WeightedCostSoFar[CurrentNodeIndex] + w
                new_hrs = HoursCostSoFar[CurrentNodeIndex] + hrs

                better = (
                    ConnectedNode not in WeightedCostSoFar or
                    new_w  <  WeightedCostSoFar[ConnectedNode] or
                    (new_w == WeightedCostSoFar[ConnectedNode] and
                    new_hrs < HoursCostSoFar[ConnectedNode])
                )
                if better:
                    WeightedCostSoFar[ConnectedNode] = new_w
                    HoursCostSoFar[ConnectedNode]    = new_hrs
                    FrontierQueue.put((new_w, new_hrs, ConnectedNode))
                    ComingFrom[ConnectedNode] = CurrentNodeIndex

        CurrentNodeIndex = TargetNodeIndex
        PathNodes = []
        if TargetNodeIndex not in ComingFrom:
            return []
        while CurrentNodeIndex != FromNodeIndex:
            PathNodes.insert(0, CurrentNodeIndex)
            CurrentNodeIndex = ComingFrom[CurrentNodeIndex]

        return TravelPath(PathNodes, HoursCostSoFar[TargetNodeIndex])

    def GetWorldMapRecenterInitialCoord(Context = None, XCoord = True):
        Result = 0
        if Context in ["travel_player", "travel_input"]:
            if XCoord:
                Result = store.TravelState.RecenterLocation[0] - 718
            else:
                Result = store.TravelState.RecenterLocation[1] - 389
        else:
            if XCoord:
                Result = store.wLocs[store.wLocs[GetLocID()].WorldMapRootLocTag].wMap_spritePos[0] - 718
            else:
                Result = store.wLocs[store.wLocs[GetLocID()].WorldMapRootLocTag].wMap_spritePos[1] - 389
        return Result

    def LocationIsWorldMapBound(LocTag):
        if hasattr(store.wLocs[LocTag], "wMap_DisplayName"):
            return True
        return False

    def Travel_GetMapContext():
        if TravelState is None:
            if LocationIsWorldMapBound(GetLocID()):
                if PlayerIsInNarrative():
                    return "world_at_exit_loc_blocked"
                else:
                    return "world_at_exit_loc"
            else:
                return "world_non_exit_loc"
        else:
            return "travel_player"

    # if we're in "vn section"
    def PlayerIsInNarrative():
        if renpy.get_screen("say") or renpy.get_screen("choice") or PausedInNarrative or (renpy.get_ongoing_transition() is not None):
            return True
        else:
            return False

    def Travel_GetCoordinatesBetweenTwoNodes(RouteID, NodeA, NodeB):
        X = int(0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeA]["position"][0] + 0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeB]["position"][0]) 
        Y = int(0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeA]["position"][1] + 0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeB]["position"][1])
        return (X, Y)

    def Travel_GetAngleBetweenTwoPoints(RouteID, NodeA, NodeB):
        NodeA_Coords = TravelRoutes[RouteID]["travel_nodes"][NodeA]["position"]
        NodeB_Coords = TravelRoutes[RouteID]["travel_nodes"][NodeB]["position"]
        from math import atan2, degrees
        Result = degrees(atan2(NodeB_Coords[1] - NodeA_Coords[1], NodeB_Coords[0] - NodeA_Coords[0]))
        Result += 90 # "reproject" into our coord sys
        return Result

#####################################################################
    ### generic reused travel node location
    WorldLocation("travel_node_generic", "", "black", parent = None)
    LocDef = wLocs["travel_node_generic"]

    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")

    LocDef.withDayMusic("audio/music/40_Wander.ogg")
    LocDef.withNightMusic("audio/music/40_Wander.ogg")
    
    LocDef.SetDayNightMatrixClass(MxDayNight)


screen loc_travel_node_generic():
    default locTag = "travel_node_generic"
