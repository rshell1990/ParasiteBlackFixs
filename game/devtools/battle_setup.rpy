default battle_setup_search = ""
default battle_setup_battle_maps = []
### id:target_lvl
default battle_setup_chars_left_side  = []
default battle_setup_chars_right_side = []
###
default persistent.battle_setup_last_chosen_left_char_IDs  = dict()
default persistent.battle_setup_last_chosen_right_char_IDs = dict() # IDs AND TARGET LEVELS
###
init python:
    def BattleSetup_ParseBattleMaps():
        results = []
        for entry in renpy.list_images():
            if "pbat_" in entry:
                results.append(entry)
        store.battle_setup_battle_maps = results

    def BattleSetup_GetBattleMaps():
        results = []
        for entry in renpy.list_images():
            if "pbat_" in entry:
                results.append(entry)
        return results

    def BattleSetup_GetAllCharsWithSkin():
        results = {}
        for CharID in CharDefs.keys():
            if CharDefs[CharID]["BattleSkin"] is not None:
                results[CharID] = {}
                char_skin = skinLib[CharDefs[CharID]["BattleSkin"]]
                results[CharID]["portrait"] = char_skin.Portrait
                results[CharID]["name"] = CharDefs[CharID]["name"]
                results[CharID]["char_id"] = CharID
        return results
    BattleSetup_AllCharsWithSkin = BattleSetup_GetAllCharsWithSkin()

    def BattleSetup_GUI_DeselectChar(CharList, Index):
        CharList.remove(Index)
        return

    def BattleSetup_GUI_SelectChar(CharList, CharID, TargetLevel = None):
        CharDict = copy.deepcopy(BattleSetup_AllCharsWithSkin[CharID])
        if TargetLevel:
            CharDict["lvl"] = TargetLevel
        else:
            CharDict["lvl"] = GetCharLevelFromID(CharID)
        CharDict["CharID"] = CharID
        CharList.append(CharDict)
        return

    def BattleSetup_GUI_GiveRandomFour():
        Result = []
        for i in range(4):
            CharID = renpy.random.choice(list(BattleSetup_AllCharsWithSkin.keys()))
            BattleSetup_GUI_SelectChar(Result, CharID)
        return Result

    def BattleSetup_GUI_SetFromParty():
        Result = []
        for CharID in player_party:
            BattleSetup_GUI_SelectChar(Result, CharID)
        return Result

    def BattleSetup_GUI_StoreCharIDs(Left, Right):
        persistent.battle_setup_last_chosen_left_char_IDs  = Left
        persistent.battle_setup_last_chosen_right_char_IDs = Right
        return
    def BattleSetup_GUI_FromIDAndLevelList(PersDict):
        Result = []
        for CharData in PersDict:
            # "to level" case; {charID:level}
            if isinstance(CharData, dict):
                for key, val in CharData.items():
                    if key in CharDefs:
                        BattleSetup_GUI_SelectChar(Result, key, TargetLevel = val)
            # just a char id
            else:
                if CharData in CharDefs:
                    BattleSetup_GUI_SelectChar(Result, CharData)
        return Result
    def BattleSetup_GUI_GetIDsAndLevelsList(CharList):
        Result = []
        for char_dict in CharList:
            # Serializes back into [{charID: lvl}] format expected by persistent storage and battle setup
            Result.append({char_dict["CharID"]: char_dict["lvl"]})
        return Result

screen battle_setup():
    predict False
    modal True

    default battle_setup_battle_maps = BattleSetup_GetBattleMaps()
    default selected_battle_map = renpy.random.choice(battle_setup_battle_maps) if battle_setup_battle_maps else ""

    on "show" action [
        SetVariable("battle_setup_chars_left_side", BattleSetup_GUI_FromIDAndLevelList(persistent.battle_setup_last_chosen_left_char_IDs)), 
        SetVariable("battle_setup_chars_right_side", BattleSetup_GUI_FromIDAndLevelList(persistent.battle_setup_last_chosen_right_char_IDs))]
    
    default override_night_tint = True      # so that we can test night maps w/o extra clicks
    default adding_to_left = True           # swaps side we're adding to

    frame:
        xfill True
        yfill True
        vbox:
            xfill True
            hbox:
                xalign 0.5
                spacing 25
                vbox:
                    textbutton "Party"  xalign 1.0 action [SetVariable("battle_setup_chars_left_side", BattleSetup_GUI_SetFromParty()), If(len(player_party) > 3, true = SetLocalVariable("adding_to_left", False))]
                    textbutton "Random" xalign 1.0 action SetVariable("battle_setup_chars_left_side",  BattleSetup_GUI_GiveRandomFour())
                    textbutton "Clear"  xalign 1.0 action SetVariable("battle_setup_chars_left_side",  [])
                for i in range(4):
                    fixed:
                        fit_first True
                        frame:
                            xysize (110, 110)
                            if i < len(battle_setup_chars_left_side):
                                vbox:
                                    xalign 0.5
                                    imagebutton:
                                        align (0.5, 0.5)
                                        idle    Transform(battle_setup_chars_left_side[i]["portrait"], size = (96, 96), matrixcolor = IdentityMatrix())
                                        hover   Transform(battle_setup_chars_left_side[i]["portrait"], size = (96, 96), matrixcolor = BrightnessMatrix(0.2))
                                        action  Function(BattleSetup_GUI_DeselectChar, battle_setup_chars_left_side, battle_setup_chars_left_side[i])
                                    hbox:
                                        xalign 0.5
                                        textbutton  "-" action SetDict(battle_setup_chars_left_side[i], "lvl", battle_setup_chars_left_side[i]["lvl"] - 1)
                                        text        str(battle_setup_chars_left_side[i]["lvl"])
                                        textbutton  "+" action SetDict(battle_setup_chars_left_side[i], "lvl", battle_setup_chars_left_side[i]["lvl"] + 1)
                if adding_to_left:
                    textbutton _("<- add to"):
                        yalign 0.5
                        if len(battle_setup_chars_right_side) != 4:
                            action SetLocalVariable("adding_to_left", False)
                else:
                    textbutton _("add to ->"):
                        yalign 0.5
                        if len(battle_setup_chars_left_side) != 4:
                            action SetLocalVariable("adding_to_left", True)
                for i in range(4):
                    fixed:
                        fit_first True
                        frame:
                            xysize (110, 110)
                            if i < len(battle_setup_chars_right_side):
                                vbox:
                                    xalign 0.5
                                    imagebutton:
                                        idle    Transform(battle_setup_chars_right_side[i]["portrait"], size = (96, 96), matrixcolor = IdentityMatrix())
                                        hover   Transform(battle_setup_chars_right_side[i]["portrait"], size = (96, 96), matrixcolor = BrightnessMatrix(0.2))
                                        action  Function(BattleSetup_GUI_DeselectChar, battle_setup_chars_right_side, battle_setup_chars_right_side[i])
                                    hbox:
                                        xalign 0.5
                                        textbutton  "-" action SetDict(battle_setup_chars_right_side[i], "lvl", battle_setup_chars_right_side[i]["lvl"] - 1)
                                        text        str(battle_setup_chars_right_side[i]["lvl"])
                                        textbutton  "+" action SetDict(battle_setup_chars_right_side[i], "lvl", battle_setup_chars_right_side[i]["lvl"] + 1)
                vbox:
                    textbutton "Random" xalign 1.0 action SetVariable("battle_setup_chars_right_side",  BattleSetup_GUI_GiveRandomFour())
                    textbutton "Clear"  xalign 1.0 action SetVariable("battle_setup_chars_right_side",  [])
            null height 15
            hbox:
                spacing 40
                xalign 0.5
                vbox:
                    hbox:   
                        text _("Char name/internal ID:")
                        input:
                            value VariableInputValue("battle_setup_search")
                    ### grid of selectable chars
                    frame:
                        xsize 1050
                        ysize 800
                        vpgrid:
                            cols 4
                            allow_underfull True
                            mousewheel True
                            scrollbars "vertical"
                            for CharID, entry in BattleSetup_AllCharsWithSkin.items():
                                if battle_setup_search.casefold() in entry["name"].casefold() or battle_setup_search.casefold() in CharID.casefold():
                                    frame:
                                        xsize 250
                                        ysize 120
                                        imagebutton:
                                            idle  Transform(entry["portrait"], size = (96, 96), fit = "contain", matrixcolor = IdentityMatrix())
                                            hover Transform(entry["portrait"], size = (96, 96), fit = "contain", matrixcolor = BrightnessMatrix(0.2))
                                            if adding_to_left:
                                                if len(battle_setup_chars_left_side) < 4:
                                                    action [Function(BattleSetup_GUI_SelectChar, battle_setup_chars_left_side, CharID), If(len(battle_setup_chars_left_side) == 3, true = SetLocalVariable("adding_to_left", False))]
                                            else:
                                                if len(battle_setup_chars_right_side) < 4:
                                                    action [Function(BattleSetup_GUI_SelectChar, battle_setup_chars_right_side, CharID), If(len(battle_setup_chars_right_side) == 3, true = SetLocalVariable("adding_to_left", True))]
                                        text entry["name"]:
                                            align (1.0, 0.0)
                                            size  20
                                        text CharID:
                                            align (1.0, 1.0)
                                            color "#fff12c"
                                            size  20
                frame:
                    ysize 850
                    vbox:
                        spacing 40
                        frame: 
                            xalign 0.5
                            xsize 250
                            ysize 120
                            if selected_battle_map:
                                add selected_battle_map:
                                    xalign 0.5
                                    ysize 100
                                    fit "contain"
                            text str(selected_battle_map or ""):
                                align (0.1, 0.9)
                                color "#fff12c"
                                size 20

                        frame:
                            xsize 500
                            ysize 650
                            vpgrid:
                                xfill True
                                cols 2
                                allow_underfull True
                                mousewheel True
                                scrollbars "vertical"
                                for battle_map in battle_setup_battle_maps:
                                    fixed:
                                        xsize 250
                                        ysize 120
                                        imagebutton:
                                            idle   Transform(battle_map, ysize = 96, fit = "contain", matrixcolor = IdentityMatrix())
                                            hover  Transform(battle_map, ysize = 96, fit = "contain", matrixcolor = BrightnessMatrix(0.2))
                                            action SetLocalVariable("selected_battle_map", battle_map)
                                        text str(battle_map):
                                            align (0.1, 0.9)
                                            color "#fff12c"
                                            size  20
        ### bottom return/start buttons
        hbox:
            align (0.5, 0.99)
            spacing 30
            textbutton _("Return") action Return(True)
            textbutton _("Start"):
                if len(battle_setup_chars_left_side) > 0 and len(battle_setup_chars_right_side) > 0:
                    action [Function(BattleSetup_GUI_StoreCharIDs, BattleSetup_GUI_GetIDsAndLevelsList(battle_setup_chars_left_side), BattleSetup_GUI_GetIDsAndLevelsList(battle_setup_chars_right_side)), 
                        Return([selected_battle_map, 
                            BattleSetup_GUI_GetIDsAndLevelsList(battle_setup_chars_left_side),
                            BattleSetup_GUI_GetIDsAndLevelsList(battle_setup_chars_right_side)])] 