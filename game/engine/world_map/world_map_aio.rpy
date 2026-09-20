# each distinct map node needs:
# 1) an entry in Travel_NodeLogicLabels to map node type ID to a label
# 2) an entry (or entries plural) in Travel_RandomNodesForBiomes to make it spawn randomly
# 3) an entry in NODE_TYPE_IMAGE_MAP that maps node type ID to an image name, for map token
# 4) an entry in NODE_PATHFIND_WEIGHTS to tell how dangerous this node is for safe-first pathfinding

init -1 python:
    from queue import PriorityQueue
    from math import atan2, degrees

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
        "forest": {
            "normal": 17,
            "enemy": 17,
            "safe": 17,
            "nature": 17,
            "mine": 17,
            "fortress_inn_cat": 5,
            "fortress_inn_wench": 5,
            "fortress_inn_frog": 5,
        },
        "desert": {
            "normal": 20,
            "enemy": 20,
            "safe": 20,
            "nature": 20,
            "mine": 20,
        },
    }

    # maps NodeTypeID to image name
    NODE_TYPE_IMAGE_MAP = {
        "normal": "node_content_random",
        "nature": "node_content_nature",
        "mine": "node_content_mine",
        "safe": "node_content_camp",
        "exit": "node_content_exit",
        "enemy": "node_content_enemy",
        "fortress_inn_cat": "node_content_fortress_inn",
        "fortress_inn_wench": "node_content_fortress_inn",
        "fortress_inn_frog": "node_content_fortress_inn",
    }

    # maps NodeTypeID to safe-first pathfinding weights
    NODE_PATHFIND_WEIGHTS = {
        "normal": 3, 
        "safe": 1,
        "exit": 1, 
        "mine": 1,
        "enemy": 1000,
        "nature": 2,
        "fortress_inn_cat": 1,
        "fortress_inn_wench": 1,
        "fortress_inn_frog": 1,
    }

# achievement track
default persistent.Travel_TotalEnteredNodes = 0
default TravelState = None
default Travel_PathingMode = 0
default persistent.TravelPref_SkipMap = False
default TravelRoutes_RandomNodes = {}

# Travel Loop Controller
label Travel_MainLoop:
    $ LocSet("travel_node_generic")
    $ LocFlush(dissolve)

    if TravelState is not None:
        call screen map(OpenTab="travel", Context="travel_input", RouteID=TravelState.RouteID)
        $ Travel_PathingMode = _return
    else:
        $ LocSet("novaras_gates")
        $ LocEnter()

    label Travel_MainLoop_PostInput:
    $ TravelState.NodeIndex_ComingFrom = TravelState.NodeIndex_Current
    $ Travel_SetCurrentNodeDuringTravelAndClearTarget()

    call screen map(OpenTab="travel", Context="travel_animate", Travel_Animate_FromNode=TravelState.NodeIndex_ComingFrom, RouteID=TravelState.RouteID)
    $ Travel_PathingMode = _return

    $ Travel_AdvanceTimeToNextNode()

    $ persistent.Travel_TotalEnteredNodes += 1
    if persistent.Travel_TotalEnteredNodes >= 50 and can_unlock_achievement("YOU_ARE_GOING_PLACES"):
        $ unlock_achievement("YOU_ARE_GOING_PLACES")

    if Travel_GetNodeType(TravelState.RouteID, TravelState.NodeIndex_Current) == "exit":
        if TravelState.CurrentPath is None:
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
            self.NodeIndex_ComingFrom = None 
        
            LocationID_A = TravelRoutes[RouteID]["connects_locations"][0]
            LocationID_B = TravelRoutes[RouteID]["connects_locations"][1]

            self.RecenterLocation = (
                int(0.5 * wLocs[LocationID_A].wMap_spritePos[0] + 0.5 * wLocs[LocationID_B].wMap_spritePos[0]), 
                int(0.5 * wLocs[LocationID_A].wMap_spritePos[1] + 0.5 * wLocs[LocationID_B].wMap_spritePos[1])
            )

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

        def RandomizeNodes(self):
            if store.TravelState is None:
                store.TravelRoutes_RandomNodes = {}
                for RouteID, RouteData in store.TravelRoutes.items():
                    store.TravelRoutes_RandomNodes[RouteID] = {}
                    BiomeType = RouteData["biome_type"]
                    assert BiomeType in Travel_RandomNodesForBiomes, "Must define random node weights for %s in Travel_RandomNodesForBiomes" % BiomeType
                    
                    TotalWeight = sum(Travel_RandomNodesForBiomes[BiomeType].values())
                    for NodeIndex, NodeData in RouteData["travel_nodes"].items():
                        if "type" not in NodeData or NodeData["type"] == "random":
                            Target = RngInt(1, TotalWeight)
                            CummWeight = 0
                            for NodeTypeID, Weight in Travel_RandomNodesForBiomes[BiomeType].items():
                                CummWeight += Weight
                                if Target <= CummWeight:
                                    store.TravelRoutes_RandomNodes[RouteID][NodeIndex] = NodeTypeID
                                    break

    def WorldMapLocAdd(LocID):
        store.seenWMapLocTags.add(LocID)

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
        return False

    def Travel_GetCurrentBiome():
        if TravelState is not None:
            return TravelRoutes[TravelState.RouteID]["biome_type"]
        return None

    def Travel_AdvanceTimeToNextNode():
        Hours = Travel_GetConnectionCostInHours(TravelState.RouteID, TravelState.NodeIndex_Current, TravelState.NodeIndex_ComingFrom)
        while Hours > 0:
            TimeAdvBy(TIME_1H)
            Hours -= 1
            renpy.pause(0.1)

    def Travel_GetConnectionCostInHours(RouteID, NodeA, NodeB):
        PathCostsInHours = TravelRoutes[RouteID].get("path_costs_in_hours", {})
        Connection = (NodeA, NodeB)
        
        if Connection in PathCostsInHours:
            Result = PathCostsInHours[Connection]
        elif (Connection[1], Connection[0]) in PathCostsInHours:
            Result = PathCostsInHours[(Connection[1], Connection[0])]
        else:
            Result = 4
            
        if config.developer:
            Connections = TravelRoutes[RouteID]["travel_paths"]
            for HoursConnection, Cost in PathCostsInHours.items():
                assert HoursConnection in Connections, "ERROR: path costs dict for route ID %s has a mismatched connection defined: (%s, %s)" % (RouteID, HoursConnection[0], HoursConnection[1])

        return Result

    def Travel_SetCurrentNodeDuringTravelAndClearTarget():
        if TravelState.CurrentPath is not None:
            TravelState.NodeIndex_Current = TravelState.CurrentPath.Nodes.pop(0)
            TravelState.CurrentPath.TotalHours -= Travel_GetConnectionCostInHours(TravelState.RouteID, TravelState.NodeIndex_Current, TravelState.NodeIndex_ComingFrom)
            if len(TravelState.CurrentPath.Nodes) == 0:
                TravelState.CurrentPath = None

    def Travel_CallEventLabel(RouteID, NodeIndex):
        NodeType = Travel_GetNodeType(RouteID, NodeIndex)
        EventLabel = Travel_NodeLogicLabels[NodeType]
        renpy.call(EventLabel)

    def Travel_ForceEnd():
        store.TravelState = None

    def Travel_GetNodeType(RouteID, NodeIndex):
        DefinedNodeType = store.TravelRoutes[RouteID]["travel_nodes"][NodeIndex].get("type", None)
        if DefinedNodeType is not None and DefinedNodeType != "random":
            return DefinedNodeType
        return store.TravelRoutes_RandomNodes[RouteID][NodeIndex]

    def GetOutToWorldMap():
        renpy.jump("Travel_MainLoop")

    def IsPlayerTraveling():
        return store.TravelState is not None

    def Travel_GetNodeDesc(RouteID, NodeIndex, NodeData, AutoPathMode):
        Result = ""
        NodeType = Travel_GetNodeType(RouteID, NodeIndex)
        
        if NodeType == "normal":
            Result += tra(_("Anything can happen at this place. We should watch out."))
        elif NodeType == "safe":
            Result += tra(_("This area seems safe: we can set up a camp there."))
        elif NodeType == "enemy":
            Result += tra(_("We will certainly walk into a fight there."))
        elif NodeType == "nature":
            Result += tra(_("There are wild creatures roaming about this place."))
        elif NodeType == "mine":
            Result += tra(_("There is an abandoned mine at this place."))
        elif NodeType in ["fortress_inn_cat", "fortress_inn_wench", "fortress_inn_frog"]:
            Result += tra(_("There is an inn at this place."))
        elif NodeData.get("type") == "exit":
            Result += tra(wLocs[NodeData["exit_location_tag"]].displayName)

        StartNode = TravelState.NodeIndex_Current if TravelState else Travel_FindPlayerAtEitherExitPoint(RouteID)

        if StartNode == NodeIndex:
            Result += "\n" + tra(_("You are here"))
        else:
            Path = Travel_FindPath(RouteID, StartNode, NodeIndex, AutoPathMode)
            Result += "\n{image=[ICON.CLOCK]} "
            if Path and hasattr(Path, "TotalHours"):
                Result += tra(_("%s hours")) % Path.TotalHours
            else:
                Result += tra(_("Unreachable"))

        return Result

    def Travel_GetRouteID(From_ID, To_ID):
        From_ID = store.wLocs[From_ID].WorldMapRootLocTag
        To_ID = store.wLocs[To_ID].WorldMapRootLocTag
        for RouteID, RouteData in store.TravelRoutes.items():
            if From_ID in RouteData["connects_locations"] and To_ID in RouteData["connects_locations"]:
                return RouteID
        return None

    def Travel_OpenInitiateMap(From_ID, To_ID):
        RouteID = Travel_GetRouteID(From_ID, To_ID)
        if RouteID is None:
            return
        renpy.hide_screen("map")
        renpy.show_screen("map", OpenTab = "travel", Context = "travel_initiate", RouteID = RouteID)
        renpy.restart_interaction()

    def Travel_FindPlayerAtEitherExitPoint(RouteID):
        CurrentLocationID = store.wLocs[GetLocID()].WorldMapRootLocTag
        for NodeID, NodeData in TravelRoutes[RouteID]["travel_nodes"].items():
            if NodeData.get("exit_location_tag") == CurrentLocationID:
                return NodeID
        return None

    def Travel_DEBUG_InitiateJump(RouteID, ClickedNode):
        store.TravelState = TravelStateClass(RouteID, ClickedNode, None)
        LocSet("travel_node_generic")
        renpy.jump("Travel_MainLoop_PostInput")

    def Travel_InitiateTravel(RouteID, InitialNode, ClickedNode, PassedInPath):
        if RouteID not in TravelRoutes:
            return
        if InitialNode not in TravelRoutes[RouteID]["travel_nodes"] or ClickedNode not in TravelRoutes[RouteID]["travel_nodes"]:
            return
        if PassedInPath is None or len(PassedInPath.Nodes) == 0:
            return

        store.TravelState = TravelStateClass(RouteID, InitialNode, PassedInPath)
        LocSet("travel_node_generic")
        renpy.jump("Travel_MainLoop_PostInput")

    def Travel_InitiateTravelFromExit(RouteID, TargetNode, AutoPathMode):
        InitialNode = Travel_FindPlayerAtEitherExitPoint(RouteID)
        Path = Travel_FindPath(RouteID, InitialNode, TargetNode, AutoPathMode = AutoPathMode)
        Travel_InitiateTravel(RouteID, InitialNode, TargetNode, Path)

    def Travel_FindPath(RouteID, FromNodeIndex, TargetNodeIndex, AutoPathMode=None):
        if AutoPathMode is None:
            AutoPathMode = 0
        store.Travel_PathingMode = AutoPathMode

        if RouteID not in TravelRoutes:
            return TravelPath([], 0)

        Nodes = TravelRoutes[RouteID].get("travel_nodes", {})
        if FromNodeIndex not in Nodes or TargetNodeIndex not in Nodes:
            return TravelPath([], 0)

        if FromNodeIndex == TargetNodeIndex:
            return TravelPath([], 0)

        Connections = list(TravelRoutes[RouteID].get("travel_paths", {}).keys())

        FrontierQueue = PriorityQueue()
        counter = 0
        
        # (weight, hours, counter, node)
        FrontierQueue.put((0, 0, counter, FromNodeIndex))

        ComingFrom = {FromNodeIndex: None}
        WeightedCostSoFar = {FromNodeIndex: 0}
        HoursCostSoFar = {FromNodeIndex: 0}

        while not FrontierQueue.empty():
            _, _, _, CurrentNodeIndex = FrontierQueue.get()

            if CurrentNodeIndex == TargetNodeIndex:
                break

            AllConnectedNodeIndexes = {
                c[0] if c[1] == CurrentNodeIndex else c[1]
                for c in Connections if CurrentNodeIndex in c
            }

            for ConnectedNode in AllConnectedNodeIndexes:
                hrs = Travel_GetConnectionCostInHours(RouteID, CurrentNodeIndex, ConnectedNode)

                if AutoPathMode == 0:
                    w = hrs
                else:
                    NodeType = Travel_GetNodeType(RouteID, ConnectedNode)
                    w = NODE_PATHFIND_WEIGHTS.get(NodeType)
                    if w is None:
                        continue

                new_w = WeightedCostSoFar[CurrentNodeIndex] + w
                new_hrs = HoursCostSoFar[CurrentNodeIndex] + hrs

                better = (
                    ConnectedNode not in WeightedCostSoFar or
                    new_w < WeightedCostSoFar[ConnectedNode] or
                    (new_w == WeightedCostSoFar[ConnectedNode] and new_hrs < HoursCostSoFar[ConnectedNode])
                )
                if better:
                    WeightedCostSoFar[ConnectedNode] = new_w
                    HoursCostSoFar[ConnectedNode] = new_hrs
                    counter += 1
                    FrontierQueue.put((new_w, new_hrs, counter, ConnectedNode))
                    ComingFrom[ConnectedNode] = CurrentNodeIndex

        if TargetNodeIndex not in ComingFrom:
            return TravelPath([], 0)

        CurrentNodeIndex = TargetNodeIndex
        PathNodes = []
        while CurrentNodeIndex != FromNodeIndex:
            PathNodes.insert(0, CurrentNodeIndex)
            CurrentNodeIndex = ComingFrom[CurrentNodeIndex]

        return TravelPath(PathNodes, HoursCostSoFar[TargetNodeIndex])

    def GetWorldMapRecenterInitialCoord(Context=None, XCoord=True):
        if Context in ["travel_player", "travel_input"]:
            if XCoord:
                return store.TravelState.RecenterLocation[0] - 718
            return store.TravelState.RecenterLocation[1] - 389
        else:
            RootTag = store.wLocs[GetLocID()].WorldMapRootLocTag
            if XCoord:
                return store.wLocs[RootTag].wMap_spritePos[0] - 718
            return store.wLocs[RootTag].wMap_spritePos[1] - 389

    def LocationIsWorldMapBound(LocTag):
        return hasattr(store.wLocs[LocTag], "wMap_DisplayName")

    def Travel_GetMapContext():
        if TravelState is None:
            RootTag = store.wLocs[GetLocID()].WorldMapRootLocTag
            if LocationIsWorldMapBound(RootTag):
                if PlayerIsInNarrative():
                    return "world_at_exit_loc_blocked"
                return "world_at_exit_loc"
            return "world_non_exit_loc"
        return "travel_player"

    def PlayerIsInNarrative():
        return (
            renpy.get_screen("say") is not None or 
            renpy.get_screen("choice") is not None or 
            getattr(store, "PausedInNarrative", False) or 
            renpy.get_ongoing_transition() is not None
        )

    def Travel_GetCoordinatesBetweenTwoNodes(RouteID, NodeA, NodeB):
        X = int(0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeA]["position"][0] + 0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeB]["position"][0]) 
        Y = int(0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeA]["position"][1] + 0.5 * TravelRoutes[RouteID]["travel_nodes"][NodeB]["position"][1])
        return (X, Y)

    def Travel_GetAngleBetweenTwoPoints(RouteID, NodeA, NodeB):
        NodeA_Coords = TravelRoutes[RouteID]["travel_nodes"][NodeA]["position"]
        NodeB_Coords = TravelRoutes[RouteID]["travel_nodes"][NodeB]["position"]
        Result = degrees(atan2(NodeB_Coords[1] - NodeA_Coords[1], NodeB_Coords[0] - NodeA_Coords[0]))
        return Result + 90

#####################################################################
    # Generic reused travel node location
    WorldLocation("travel_node_generic", "", "black", parent=None)
    LocDef = wLocs["travel_node_generic"]

    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")

    LocDef.withDayMusic("audio/music/40_Wander.ogg")
    LocDef.withNightMusic("audio/music/40_Wander.ogg")
    
    LocDef.SetDayNightMatrixClass(MxDayNight)

screen loc_travel_node_generic():
    default locTag = "travel_node_generic"