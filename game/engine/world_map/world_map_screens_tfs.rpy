########### the MAP screen contexts 
# valid contexts, "we have called map screen from ...."
# "world_non_exit_loc"          <- from any non-exit and non-travel location
# "world_at_exit_loc"           <- from any exit-able world location
# "world_at_exit_loc_blocked"   <- from exit location, but we cannot leave (when we're in narrative)
# "travel_initiate"             <- from exit location, after clicking a loc
# "travel_player"               <- from travel path, called by player.
# "travel_input"                <- from travel path, called by game
# "travel_animate"              <- from travel path, called by game, only animates

screen map(OpenTab = "world", Context = None, Travel_Animate_FromNode = None, RouteID = None):
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)

    tag ingame_menu
    modal True
    zorder 1

    default Tab = OpenTab # "world" or "travel"

    if Context == "travel_input":
        imagebutton: # bottom
            xalign 0.5
            yalign 1.0
            xsize 1920
            ysize 115
            keyboard_focus False
            idle "images/gui/blank.webp"
            hover "images/gui/blank.webp"
            hovered TooltipSetUI(tra(_("You must select a destination node on the map.")))
            unhovered TooltipClearUI()
            action NullAction()

        imagebutton: # top
            xalign 0.5
            yalign 0.0
            xsize 1920
            ysize 90
            keyboard_focus False
            idle "images/gui/blank.webp"
            hover "images/gui/blank.webp"
            hovered TooltipSetUI(tra(_("You must select a destination node on the map.")))
            unhovered TooltipClearUI()
            action NullAction()

        imagebutton: # left
            xalign 0.0
            yalign 0.5
            xsize 190
            ysize 1080
            keyboard_focus False
            idle "images/gui/blank.webp"
            hover "images/gui/blank.webp"
            hovered TooltipSetUI(tra(_("You must select a destination node on the map.")))
            unhovered TooltipClearUI()
            action NullAction()

        imagebutton: # right
            xalign 1.0
            yalign 0.5
            xsize 190
            ysize 1080
            keyboard_focus False
            idle "images/gui/blank.webp"
            hover "images/gui/blank.webp"
            hovered TooltipSetUI(tra(_("You must select a destination node on the map.")))
            unhovered TooltipClearUI()
            action NullAction()

    else:
        use close_outside("map")

    use outer_frame(padd_top = 50, padd_left = 50, padd_right = 50, padd_bot = 50):
        frame:
            align (0.5, 0.5)
            xysize (1477, 812)
            if Tab == "world":
                use Map_World(Context = Context)
            elif Tab == "travel":
                use Map_Travel(Context = Context, RouteID = RouteID, Travel_Animate_FromNode = Travel_Animate_FromNode)

screen Map_World(Context = None):
    viewport:
        align (0.5, 0.5)
        child_size (2867, 2867)
        draggable True
        xinitial GetWorldMapRecenterInitialCoord(Context = Context)
        yinitial GetWorldMapRecenterInitialCoord(Context = Context, XCoord = False)
        xadjustment ui.adjustment(value = 500, step = 1, range = 2867)
        yadjustment ui.adjustment(value = 500, step = 1, range = 2867)
        scrollbars "both" 
        add "images/world_map/alderay_map.webp"

        # loop that spawns paths
        for RouteID, RouteData in TravelRoutes.items():
            if RouteData["connects_locations"][0] in seenWMapLocTags and RouteData["connects_locations"][1] in seenWMapLocTags:
                add RouteData["world_map_sprite"]:
                    pos RouteData["world_map_sprite_pos"]

                    if Context in ["world_non_exit_loc", "world_at_exit_loc", "world_at_exit_loc_blocked", "travel_initiate"]:
                        if GetLocID() == RouteData["connects_locations"][0] or GetLocID() == RouteData["connects_locations"][1]:
                            matrixcolor TintMatrix((255, 100, 100))
                        else:
                            matrixcolor TintMatrix((80, 60, 60))
                    else:
                        if TravelState and RouteID == TravelState.RouteID:
                            matrixcolor TintMatrix((255, 100, 100))
                        else:
                            matrixcolor TintMatrix((80, 60, 60))

        # loop that spawns clickable world locs
        for locTag in wLocs:
            if LocationIsWorldMapBound(locTag):
                if locTag in seenWMapLocTags:
                    imagebutton:
                        anchor (0.5, 0.5)
                        pos wLocs[locTag].wMap_spritePos
                        unhovered TooltipClearUI()

                        if locTag == wLocs[GetLocID()].WorldMapRootLocTag:
                            idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = IdentityMatrix())
                            hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = MxMapHover())
                            hovered TooltipSetUI(tra(wLocs[locTag].wMap_DisplayName) + tra(STR_UI.YOU_ARE_HERE))
                            action [Hide("map"), Jump("main_recheck")]
                        else:
                            if Context == "world_at_exit_loc":
                                if locTag in wLocs[wLocs[GetLocID()].WorldMapRootLocTag].wMap_connectsTo:
                                    if GetLocID() != locTag:
                                        idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = IdentityMatrix())
                                        hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = MxMapHover())
                                        hovered TooltipSetUI("{image=[ICON.CLOCK]}" + tra(_(" Travel to ")) + tra(wLocs[locTag].wMap_DisplayName))
                                        action [TooltipClearUI(), Function(Travel_OpenInitiateMap, GetLocID(), locTag)]
                                    else:
                                        idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = IdentityMatrix())
                                        hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = MxMapHover())
                                        hovered TooltipSetUI((tra(wLocs[locTag].wMap_DisplayName) + tra(STR_UI.YOU_ARE_HERE)))
                                        action [Hide("map"), Jump("main_recheck")]
                                else:
                                    idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = SaturationMatrix(0.0))
                                    hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = SaturationMatrix(0.0) * MxMapHover())
                                    hovered TooltipSetUI(tra(wLocs[locTag].wMap_DisplayName) + tra(_(", inaccessible from here")))
                                    action NullAction()

                            elif Context == "world_non_exit_loc":
                                idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = IdentityMatrix())
                                hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = MxMapHover())
                                hovered TooltipSetUI(tra(wLocs[locTag].wMap_DisplayName))
                                action Show("ok_popup", label = STR_UI.TUTORIAL_TITLE, text = tra(_("You are currently in map view mode.\nTo access world travel mode, find a suitable location - one that has a 'travel' button:\n{image=gui/help/travel.webp}\nOnce there, you can either click on the 'travel' button or bring up the map again to enter traveling mode.")), onOk = "hide")

                            elif Context == "world_at_exit_loc_blocked":
                                idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = IdentityMatrix())
                                hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = MxMapHover())
                                hovered TooltipSetUI(tra(wLocs[locTag].wMap_DisplayName))
                                action Show("ok_popup", label = STR_UI.TUTORIAL_TITLE, text = tra(_("You cannot travel at this moment.")), onOk = "hide")

                            elif Context in ["travel_player", "travel_input"]:
                                idle Transform(wLocs[locTag].wMap_spritePath, matrixcolor = IdentityMatrix())
                                hover Transform(wLocs[locTag].wMap_spritePath, matrixcolor = MxMapHover())
                                hovered TooltipSetUI(tra(wLocs[locTag].wMap_DisplayName))

                                if TravelState and locTag in TravelRoutes[TravelState.RouteID]["connects_locations"]:
                                    action Show("map", OpenTab = "travel", Context = Context, RouteID = TravelState.RouteID)
                                else:
                                    action Show("ok_popup", label = STR_UI.TUTORIAL_TITLE, text = tra(_("You are currently traveling in the wilderness.\nTo access world travel mode, reach either of your travel map destinations, marked with an 'exit' figure:\n{image=images/world_travel/nodes/node_content_exit.webp}")), onOk = "hide")
 
        text STR_WMAP.MAP_OF_ALDERAY:
            style "label_text"
            outlines [(2, "#1b1414ff", 0, 0)]
            outline_scaling "step"
            size 100
            anchor (1.0, 0.0)
            pos (0.98, 10)

        for wmapTextID, wmapText in world_map_text.items():
            text wmapText["name"]:
                pos wmapText["pos"]
                style wmapText["style"]

        for locTag in wLocs:
            if LocationIsWorldMapBound(locTag):
                if locTag in seenWMapLocTags:
                    if IsWorldMapLocTracked(locTag):
                        fixed:
                            fit_first True
                            anchor (0.5, 0.5)
                            pos wLocs[locTag].wMap_spritePos
                            use locBtn_QuestMarker(Offset = -75)

    if Context in ["travel_player", "travel_input"] and TravelState:
        frame:
            align (1.0, 1.0)
            hbox:
                xalign 1.0
                textbutton _("Travel map") action Show("map", OpenTab = "travel", Context = Context, RouteID = TravelState.RouteID)

screen Map_Travel(Context = None, RouteID = None, Travel_Animate_FromNode = None):
    default RouteData = TravelRoutes[RouteID]
    default HoveredNodeIndex = None

    default CurrentUIPath = None if (TravelState is None or TravelState.CurrentPath is None) else TravelState.CurrentPath
    default UI_PathfindMode = Travel_PathingMode

    fixed:
        align (0.5, 0.5)
        add RouteData["image_map"]:
            align (0.5, 0.5)

        # route label (X to Y)
        frame:
            xmaximum 1500
            ymaximum 500
            align (0.5, 0.0)
            hbox:
                align (0.5, 0.5)
                spacing 10
                label tra(wLocs[RouteData["connects_locations"][0]].displayName)
                label _("—")
                label tra(wLocs[RouteData["connects_locations"][1]].displayName)

        if config.developer:
            frame:
                align (0.9, 0.1)
                text "dev: map context %s" % Context:
                    ysize 15
                    xsize 350

        # nodes (as buttons)
        for Node_Index, Node_Data in sorted(RouteData["travel_nodes"].items(), key = lambda x: x[1].get("draw_order", 0)):
            fixed:
                xysize (128, 160)
                anchor (0.5, 1.0)
                yoffset 60
                pos Node_Data["position"]
                button:
                    xysize (70, 110)
                    align (0.5, 0.51)
                    background Null()

                    hovered [TooltipSetUI(Travel_GetNodeDesc(RouteID, Node_Index, Node_Data, UI_PathfindMode)), SetScreenVariable("HoveredNodeIndex", Node_Index)]
                    unhovered [TooltipClearUI(), SetScreenVariable("HoveredNodeIndex", None)]

                    # case 1, we're initiating travel
                    if Context == "travel_initiate":
                        if Node_Index == Travel_FindPlayerAtEitherExitPoint(RouteID):
                            action Hide("map", transition = Dissolve(0.15))
                        else:
                            action [TooltipClearUI(), Function(Travel_InitiateTravelFromExit, RouteID, Node_Index, UI_PathfindMode)]

                    # case 2, all other contexts
                    else:
                        if TravelState and Node_Index != TravelState.NodeIndex_Current:
                            if Context == "travel_input":
                                action [TooltipClearUI(), SetField(TravelState, "CurrentPath", Travel_FindPath(RouteID, TravelState.NodeIndex_Current, Node_Index, AutoPathMode = UI_PathfindMode)), Return(UI_PathfindMode)]
                            else:
                                action [SetScreenVariable("CurrentUIPath", Travel_FindPath(RouteID, TravelState.NodeIndex_Current, Node_Index, AutoPathMode = UI_PathfindMode)), SetField(TravelState, "CurrentPath", Travel_FindPath(RouteID, TravelState.NodeIndex_Current, Node_Index, AutoPathMode = UI_PathfindMode))]
                        else:
                            if Context == "travel_input" and Travel_FindPlayerAtEitherExitPoint(RouteID) == Node_Index:
                                action [SetField(TravelState, "CurrentPath", None), TooltipClearUI(), Return(UI_PathfindMode)]

                if CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
                    if Node_Index in CurrentUIPath.Nodes:
                        if Node_Index == CurrentUIPath.Nodes[-1]:
                            add "map_node_path_target":
                                anchor (0.5, 1.0)
                                pos (0.5, 1.0)
                        else:
                            add "map_node_path_selection":
                                anchor (0.5, 1.0)
                                pos (0.5, 1.0)
                                if Context == "travel_animate":
                                    at TravelMapTF_SqueezeIcon_Loop
                                else:
                                    at TravelMapTF_AppearAndSqueezeIcon

                # add node type figure
                if Context == "travel_animate":
                    add NODE_TYPE_IMAGE_MAP[Travel_GetNodeType(RouteID, Node_Index)]:
                        anchor (0.5, 1.0)
                        pos (0.5, 1.0)
                elif Context == "travel_input" and TravelState and Node_Index == TravelState.NodeIndex_Current and not Travel_GetNodeType(RouteID, Node_Index) == "exit":
                    add NODE_TYPE_IMAGE_MAP[Travel_GetNodeType(RouteID, Node_Index)]:
                        anchor (0.5, 1.0)
                        pos (0.5, 1.0)
                        at TravelMapTF_KnockDownFigure
                else:
                    if not ((TravelState and Node_Index == TravelState.NodeIndex_Current) or (Travel_FindPlayerAtEitherExitPoint(RouteID) == Node_Index)):
                        add NODE_TYPE_IMAGE_MAP[Travel_GetNodeType(RouteID, Node_Index)]:
                            anchor (0.5, 1.0)
                            pos (0.5, 1.0)

                # add static player figure
                if (Context == "travel_initiate" and Node_Index == Travel_FindPlayerAtEitherExitPoint(RouteID)) or (Context in ["travel_player", "travel_input"] and TravelState and Node_Index == TravelState.NodeIndex_Current):
                    add "node_figure_shadow":
                        anchor (0.5, 1.0)
                        pos (0.5, 1.0)
                        if HoveredNodeIndex is not None and CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
                            if HoveredNodeIndex == CurrentUIPath.Nodes[-1]:
                                at TravelMapTF_ShadowAnim
                            else:
                                at TravelMapTF_ShadowToPos
                        else:
                            at TravelMapTF_ShadowToPos

                    add "node_content_player":
                        anchor (0.5, 1.0)
                        pos (0.5, 1.0)
                        if HoveredNodeIndex is not None and CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
                            if HoveredNodeIndex == CurrentUIPath.Nodes[-1]:
                                at TravelMapTF_FigureLift
                            else:
                                at TravelMapTF_FigureToPos
                        else:
                            at TravelMapTF_FigureToPos

        if config.developer and DEV_VARIABLES.get("SHOW_EXTRA_MAP_DATA", False):
            for ConnectedNodes, ConnectionNodesList in RouteData["travel_paths"].items():
                frame:
                    anchor (0.5, 0.5)
                    pos (int(0.5 * RouteData["travel_nodes"][ConnectedNodes[0]]["position"][0] + 0.5 * RouteData["travel_nodes"][ConnectedNodes[1]]["position"][0]), int(0.5 * RouteData["travel_nodes"][ConnectedNodes[0]]["position"][1] + 0.5 * RouteData["travel_nodes"][ConnectedNodes[1]]["position"][1]))
                    text "%s-%s" % (ConnectedNodes[0], ConnectedNodes[1]):
                        size 15
                for ConnectionCoord in ConnectionNodesList:
                    add "debug_tiny_cross":
                        anchor (0.5, 0.5)
                        pos ConnectionCoord
        
            for NodeIndex, NodeData in RouteData["travel_nodes"].items():
                frame:
                    anchor (0.5, 0.5)
                    pos NodeData["position"]
                    text "%s" % NodeIndex:
                        size 25
        
        if CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
            if Context != "travel_animate":
                add "map_path_arrow":
                    anchor (0.5, 0.5)
                    zoom 0.3
                    if Context == "travel_initiate":
                        rotate Travel_GetAngleBetweenTwoPoints(RouteID, Travel_FindPlayerAtEitherExitPoint(RouteID), CurrentUIPath.Nodes[0])
                        pos Travel_GetCoordinatesBetweenTwoNodes(RouteID, Travel_FindPlayerAtEitherExitPoint(RouteID), CurrentUIPath.Nodes[0])
                    elif TravelState:
                        rotate Travel_GetAngleBetweenTwoPoints(RouteID, TravelState.NodeIndex_Current, CurrentUIPath.Nodes[0])
                        pos Travel_GetCoordinatesBetweenTwoNodes(RouteID, TravelState.NodeIndex_Current, CurrentUIPath.Nodes[0])
                    at TravelMapTF_AppearAndSqueezeIcon

            for NodeIndex, NodeNumber in enumerate(CurrentUIPath.Nodes):
                if NodeIndex < len(CurrentUIPath.Nodes) - 1:
                    add "map_path_arrow":
                        anchor (0.5, 0.5)
                        zoom 0.3
                        rotate Travel_GetAngleBetweenTwoPoints(RouteID, NodeNumber, CurrentUIPath.Nodes[NodeIndex + 1])
                        pos Travel_GetCoordinatesBetweenTwoNodes(RouteID, NodeNumber, CurrentUIPath.Nodes[NodeIndex + 1])
                        at TravelMapTF_AppearAndSqueezeIcon
                    
        # if we're animating, display animated player node
        if Context == "travel_animate" and Travel_Animate_FromNode is not None and TravelState:
            add "node_figure_shadow":
                anchor (0.5, 1.0)
                at TravelMapTF_MoveShadowOnMap(TravelRoutes[RouteID]["travel_nodes"][Travel_Animate_FromNode]["position"], RouteData["travel_nodes"][TravelState.NodeIndex_Current]["position"])
            add "node_content_player":
                anchor (0.5, 1.0)
                at TravelMapTF_MoveFigureOnMap(TravelRoutes[RouteID]["travel_nodes"][Travel_Animate_FromNode]["position"], RouteData["travel_nodes"][TravelState.NodeIndex_Current]["position"])

        frame:
            align (1.0, 1.0)
            xsize 200
            vbox:
                align (0.5, 0.5)
                label _("Path:") xalign 0.5

                textbutton _("Fastest"):
                    xfill True
                    xalign 1.0
                    hovered TooltipSetUI(_("Your party will favour routes that take as little time as possible."))
                    unhovered TooltipClearUI()
                    style "button_sel"
                    selected UI_PathfindMode == 0
                    if CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
                        if TravelState is not None:
                            action [SetScreenVariable("UI_PathfindMode", 0), SetScreenVariable("CurrentUIPath", Travel_FindPath(RouteID, TravelState.NodeIndex_Current, CurrentUIPath.Nodes[-1], AutoPathMode = 0))]
                        else:
                            action [SetScreenVariable("UI_PathfindMode", 0), SetScreenVariable("CurrentUIPath", Travel_FindPath(RouteID, Travel_FindPlayerAtEitherExitPoint(RouteID), CurrentUIPath.Nodes[-1], AutoPathMode = 0))]
                    else:
                        action SetScreenVariable("UI_PathfindMode", 0)

                textbutton _("Safest"):
                    xfill True
                    xalign 1.0
                    hovered TooltipSetUI(_("Your party will favour routes that have the least chance to encounter an enemy."))
                    unhovered TooltipClearUI()
                    style "button_sel"
                    selected UI_PathfindMode == 1
                    if CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
                        if TravelState is not None:
                            action [SetScreenVariable("UI_PathfindMode", 1), SetScreenVariable("CurrentUIPath", Travel_FindPath(RouteID, TravelState.NodeIndex_Current, CurrentUIPath.Nodes[-1], AutoPathMode = 1))]
                        else:
                            action [SetScreenVariable("UI_PathfindMode", 1), SetScreenVariable("CurrentUIPath", Travel_FindPath(RouteID, Travel_FindPlayerAtEitherExitPoint(RouteID), CurrentUIPath.Nodes[-1], AutoPathMode = 1))]
                    else:
                        action SetScreenVariable("UI_PathfindMode", 1)

        if Context in ["travel_input", "travel_initiate"]:
            if CurrentUIPath is not None and len(CurrentUIPath.Nodes) > 0:
                frame:
                    align (0.5, 1.0)
                    hbox:
                        spacing 10
                        textbutton _("(space) Travel to destination"):
                            if Context == "travel_input":
                                action [TooltipClearUI(), SetField(TravelState, "CurrentPath", CurrentUIPath), Return(UI_PathfindMode)]
                            elif Context == "travel_initiate":
                                action [TooltipClearUI(), Function(Travel_InitiateTravelFromExit, RouteID, CurrentUIPath.Nodes[-1], UI_PathfindMode)]
                            
                            hovered [SetScreenVariable("HoveredNodeIndex", CurrentUIPath.Nodes[-1])]
                            unhovered [SetScreenVariable("HoveredNodeIndex", None)]
                            keysym ["K_SPACE", "K_KP_ENTER"]

                        text tra(_("%s hours")) % CurrentUIPath.TotalHours: 
                            yalign 0.5
                        null width 2

                if config.developer:
                    frame:
                        align (0.0, 0.0)
                        textbutton _("DEV:\n(j) jump to"):
                            if Context == "travel_input":
                                action [TooltipClearUI(), SetField(TravelState, "NodeIndex_Current", CurrentUIPath.Nodes[-1]), SetField(TravelState, "CurrentPath", None), Return(UI_PathfindMode)]
                            elif Context == "travel_initiate":
                                action [TooltipClearUI(), Function(Travel_DEBUG_InitiateJump, RouteID, CurrentUIPath.Nodes[-1])]
                            keysym "K_j"

        if Context in ["travel_player", "travel_input", "travel_initiate"]:
            frame:
                align (0.0, 1.0)
                hbox:
                    xalign 0.0
                    textbutton _("World map"):
                        if Context == "travel_initiate":
                            action Show("map", OpenTab = "world", Context = "world_at_exit_loc")
                        else:
                            action Show("map", OpenTab = "world", Context = Context)

    if Context == "travel_animate":
        button:
            xsize 1920
            ysize 1080
            padding (0, 0, 0, 0)
            background Null()
            selected False
            action [TooltipClearUI(), Return(UI_PathfindMode)] 
            keysym ["K_SPACE", "K_KP_ENTER"]

        if TravelState and Travel_Animate_FromNode == TravelState.NodeIndex_Current:
            timer 0.033 action [TooltipClearUI(), Return(UI_PathfindMode)]
        else:
            timer 1.0 action [TooltipClearUI(), Return(UI_PathfindMode)]

transform TravelMapTF_KnockDownFigure:
    subpixel True
    xoffset 60
    yoffset 45
    parallel:
        ease 1.0 xoffset 120
    parallel:
        ease 1.0 rotate 90
    parallel:
        linear 1.0 yoffset 70
    parallel:
        0.5
        linear 0.5 alpha 0.0

transform TravelMapTF_FigureLift:
    subpixel True
    ease 0.3 yoffset -25
    ease 0.5 yoffset -10
    repeat

transform TravelMapTF_ShadowAnim:
    ease 0.3 alpha 0.4
    ease 0.5 alpha 0.8
    repeat

transform TravelMapTF_ShadowToPos:
    ease 0.15:
        alpha 1.0

transform TravelMapTF_FigureToPos:
    subpixel True
    ease 0.15:
        xoffset 0
        yoffset 0

transform TravelMapTF_AppearAndSqueezeIcon:
    subpixel True
    alpha 0.0
    ease 0.25:
        alpha 0.5
    TravelMapTF_SqueezeIcon_Loop
    
transform TravelMapTF_SqueezeIcon_Loop:
    alpha 0.5
    subpixel True
    ease 0.75:
        zoom 0.95
    ease 0.25:
        zoom 1.0
    repeat

transform TravelMapTF_MoveFigureOnMap(From, To):
    subpixel True
    yoffset 20
    pos From
    parallel:
        ease 1.0:
            pos (To[0] - 60, To[1] + 10)
    parallel:
        ease 0.5:
            yoffset 0
        ease 0.5:
            yoffset 60

transform TravelMapTF_MoveShadowOnMap(From, To):
    subpixel True
    yoffset 60
    pos From
    parallel:
        ease 1.0:
            pos (To[0] - 60, To[1] + 10)
    parallel:
        ease 0.5:
            alpha 0.1
        ease 0.5:
            alpha 1.0