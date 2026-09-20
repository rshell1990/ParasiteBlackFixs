init python:
    def Battle_SetUISelection(Side = None, Char = None):
        if Side == 0:
            Battle_SelectLeftChar(Char)
        elif Side == 1:
            Battle_SelectRightChar(Char)
        return

screen Battle_BottomPanel():
    # decorative under
    frame:
        xsize 2000
        ysize 470
        align (0.5, 1.0)
        yoffset 180
        top_padding 60
        style "frame_outer"

    # portrait & statbox & namebox left
    $ selected_left = getattr(store.BattleScene, "SelectedLeft", None)
    use Battle_Portrait(selected_left)
    if selected_left:
        use Battle_StatBox(selected_left)
        use Battle_NameBox(selected_left)

    # portrait & statbox right (first for layering)
    $ selected_right = getattr(store.BattleScene, "SelectedRight", None)
    if selected_right:
        use Battle_StatBox(selected_right, RightSide = True)
        use Battle_NameBox(selected_right, RightSide = True)

    # log
    use Battle_LogOrSkillDesc()
    # portrait 
    use Battle_Portrait(selected_right, RightSide = True)

################################################################################################################
screen Battle_ActionSelectPanel(WaitForPlayerInput = False):
    $ sel_left = getattr(store.BattleScene, "SelectedLeft", None)
    $ char_ref = getattr(sel_left, "CharRef", {}) if sel_left else {}
    $ can_transform = getattr(store.BattleScene, "CanTransform", False)
    $ active_chars = getattr(store.BattleScene, "ActiveCharsList", [])
    $ can_use_items = getattr(store.BattleScene, "CanUseItems", False)
    $ inv = getattr(store, "player_inv", {})
    $ items_dict = getattr(store, "all_items", {})

    # skills, items
    hbox:
        anchor (0.5, 0.0)
        pos (640, 861)
        if sel_left:
            vbox:
                if hasattr(sel_left, "Skill_Attack") and sel_left.Skill_Attack:
                    use Battle_SkillIcon(sel_left.Skill_Attack, HotKey = "K_a", HotKeyText = "a", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)
                if hasattr(sel_left, "Skill_Defend") and sel_left.Skill_Defend:
                    use Battle_SkillIcon(sel_left.Skill_Defend, HotKey = "K_d", HotKeyText = "d", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)
                
                if char_ref.get("HasAltForm", False):
                    if can_transform:
                        if char_ref.get("Transformed", False):
                            if hasattr(sel_left, "Skill_ExtraUnTransform") and sel_left.Skill_ExtraUnTransform:
                                use Battle_SkillIcon(sel_left.Skill_ExtraUnTransform, HotKey = "K_x", HotKeyText = "x", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)
                        else:
                            if char_ref.get("AltForm_Unlocked", False):
                                if hasattr(sel_left, "Skill_ExtraTransform") and sel_left.Skill_ExtraTransform:
                                    use Battle_SkillIcon(sel_left.Skill_ExtraTransform, HotKey = "K_x", HotKeyText = "x", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)

            vbox:
                if can_use_items:
                    $ valid_item_count = len([k for k, v in inv.items() if items_dict.get(k, {}).get("on_use_battle") is not None])
                    textbutton _("(e) Items"):
                        yalign 0.5
                        style "battle_itemskills_button"
                        keysym "K_e"
                        if sel_left in active_chars and WaitForPlayerInput and valid_item_count > 0:
                            action Show("Battle_ItemMenu", BattleChar = sel_left)

                $ skill_count = len(getattr(sel_left, "Skills", []))
                textbutton _("(s) Skills"):
                    yalign 0.5
                    style "battle_itemskills_button"
                    keysym "K_s"
                    if sel_left in active_chars and WaitForPlayerInput and skill_count > 0:
                        action Show("Battle_SkillMenu", BattleChar = sel_left, WaitForPlayerInput = WaitForPlayerInput)

    # selection arrows over portrait
    if len(Battle_GetAliveCharsOnSide(Side = 0)) > 1 and sel_left:
        hbox:
            anchor (0.5, 0.5)
            pos (0.081, 0.97)
            spacing 80
            textbutton "<< (z)":
                if getattr(store.BattleScene, "ActionAwaitingTarget", None) is None:
                    action Function(Battle_SelectArrowLeft) keysym "K_z"
            textbutton "(c) >>":
                if getattr(store.BattleScene, "ActionAwaitingTarget", None) is None:
                    action Function(Battle_SelectArrowRight) keysym "K_c"
        
init python:
    def Battle_SelectArrowLeft():
        AllAliveChars = Battle_GetAliveCharsOnSide(Side = 0)
        if not AllAliveChars:
            return
        selected_left = getattr(store.BattleScene, "SelectedLeft", None)
        if selected_left in AllAliveChars:
            ThisCharIndex = AllAliveChars.index(selected_left)
            Battle_SelectLeftChar(AllAliveChars[ThisCharIndex - 1])
        else:
            Battle_SelectLeftChar(AllAliveChars[0])
        return

    def Battle_SelectArrowRight():
        AllAliveChars = Battle_GetAliveCharsOnSide(Side = 0)
        if not AllAliveChars:
            return
        selected_left = getattr(store.BattleScene, "SelectedLeft", None)
        if selected_left in AllAliveChars:
            ThisCharIndex = AllAliveChars.index(selected_left)
            if ThisCharIndex + 1 >= len(AllAliveChars):
                Battle_SelectLeftChar(AllAliveChars[0])
            else:
                Battle_SelectLeftChar(AllAliveChars[ThisCharIndex + 1])
        else:
            Battle_SelectLeftChar(AllAliveChars[0])
        return

################################################################################################################
screen Battle_SkillIcon(SkillInstance, HotKey = None, HotKeyText = None, FromSkillMenu = False, WaitForPlayerInput = False):
    if SkillInstance:
        $ can_pay = SkillInstance.OwnerCharCanPaySkillCost() if hasattr(SkillInstance, "OwnerCharCanPaySkillCost") else True
        $ can_exec = SkillInstance.CanExecute() if hasattr(SkillInstance, "CanExecute") else True
        fixed:
            fit_first True
            imagebutton:
                sensitive WaitForPlayerInput
                if not WaitForPlayerInput:
                    idle Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                unhovered TooltipClearUI()
                if WaitForPlayerInput:
                    if getattr(SkillInstance, "Owner_BattleChar", None) in getattr(store.BattleScene, "ActiveCharsList", []):
                        if getattr(SkillInstance, "OncePerTurn", False) and getattr(SkillInstance, "UsedThisTurn", False):
                            idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                            hover       Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1) * SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                            hovered     TooltipSetUI(Text("{size=+6}{color=[BATTLE_COLORS.REQ_MISSING]}Already used this turn{/color}{/size}\n" + GetSkillDesc(SkillInstance)))
                            action      NullAction()
                        else:
                            if can_pay and can_exec:
                                if len(Battle_GetAllTargetsList(SkillInstance)) > 0:
                                    idle            Transform(SkillInstance.Icon, matrixcolor = IdentityMatrix(),      size = gui.general_icon_size_lower)
                                    hover           Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1), size = gui.general_icon_size_lower)
                                    selected_idle   Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.2), size = gui.general_icon_size_lower)
                                    insensitive     Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)

                                    hovered     TooltipSetUI(Text(GetSkillDesc(SkillInstance)))
                                    if HotKey:
                                        keysym HotKey
                                    if FromSkillMenu:
                                        action [Function(Battle_PlayerScheduleActionOrEnterTargetingMode, SkillInstance.Owner_BattleChar, SkillInstance), Hide("Battle_SkillMenu"), Return()]
                                    else:
                                        action [Function(Battle_PlayerScheduleActionOrEnterTargetingMode, SkillInstance.Owner_BattleChar, SkillInstance), Return()]
                                else:
                                    idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                                    hover       Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1) * SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                                    hovered     TooltipSetUI(Text(GetSkillDesc(SkillInstance) + "\nNO TARGETS"))
                                    action      NullAction()

                            else:
                                idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                                hover       Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1) * SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                                hovered     TooltipSetUI(Text(Battle_GetUnmetCostAsString(SkillInstance) + GetSkillDesc(SkillInstance)))
                                action      NullAction()

                    else:
                        idle Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)

            if HotKey and HotKeyText:
                add "images/gui/battle/caret_up.webp":
                    align (0.5, 1.05)
                    zoom 0.7
                text HotKeyText:
                    size 24
                    align (0.5, 1.04)

################################################################################################################
screen Battle_CharSelectionPanels(SelectSkillTarget = False):
    layer "master"
    $ side_0 = getattr(store.BattleScene, "BattleChars", {}).get(0, [])
    $ side_1 = getattr(store.BattleScene, "BattleChars", {}).get(1, [])
    $ potential_targets = getattr(store.BattleScene, "ActionAwaitingTarget_PotentialTargetsList", [])
    $ awaiting_action = getattr(store.BattleScene, "ActionAwaitingTarget", None)

    for BattleChar in side_0 + side_1:
        if getattr(BattleChar, "IsAlive", False):
            $ rect_size = getattr(BattleChar.BattleSkin, "FocusRectSize", (100, 100))
            $ slot_idx = getattr(BattleChar, "PositionSlotIndex", 0)
            $ target_xsize = int(rect_size[0] * (0.9 if slot_idx in [0, 1] else 1.0))
            $ target_ysize = int(rect_size[1] * (0.9 if slot_idx in [0, 1] else 1.0))
            button:
                xsize target_xsize
                ysize target_ysize
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[BattleChar.BattleSide][slot_idx]
                offset getattr(BattleChar.BattleSkin, "FocusRectOffset", (0, 0))

                if getattr(store, "Battle_ShowSelectionOutlines", False):
                    style "frame_trans"
                elif SelectSkillTarget and BattleChar in potential_targets:
                    style "frame_battle_target_sel"
                    keysym "%s" % (potential_targets.index(BattleChar) + 1)
                else:
                    background Null()

                if SelectSkillTarget:
                    if BattleChar in potential_targets and awaiting_action:
                        action  [Function(Battle_ClearActionAwaitingTarget),
                                    Function(Battle_SetCharAction, getattr(awaiting_action, "Owner_BattleChar", None), awaiting_action, BattleChar),
                                    Function(Battle_SetUISelection, Side = BattleChar.BattleSide, Char = BattleChar),
                                    TooltipSetUI(getattr(BattleChar, "CharRef", {}).get("name", "")),
                                    Return()]
                else:
                    action Function(Battle_SetUISelection, Side = BattleChar.BattleSide, Char = BattleChar)

                hovered [TooltipSetUI(Battle_GetTargetingTooltipForCurrentAction(BattleChar)), Function(BattleUI_BringInfoForward, BattleChar)]
                unhovered [TooltipClearUI(), Function(BattleUI_BringInfoBackward, BattleChar)]

init python:
    def Battle_GetTargetingTooltipForCurrentAction(TargetBattleChar):
        ReturnStrings = []
        char_name = getattr(TargetBattleChar, "CharRef", {}).get("name", "")
        ReturnStrings.append(tra(char_name))

        action_awaiting = getattr(store.BattleScene, "ActionAwaitingTarget", None)
        if action_awaiting is not None:
            if getattr(action_awaiting, "ShowHitChance", False):
                owner_char = getattr(action_awaiting, "Owner_BattleChar", None)
                IsEnemy = (False if getattr(TargetBattleChar, "BattleSide", None) == getattr(owner_char, "BattleSide", None) else True)
                if IsEnemy and owner_char:
                    HitProb = Battle_GetHitProb(owner_char, TargetBattleChar)
                    String = "\n%s: %s%%" % (tra(_("Chance to hit")), HitProb)
                    ReturnStrings.append(String)

        return "".join(ReturnStrings)

image Battle_SelectionFramePulsin:
    "images/gui/battle/frame_target_sel.webp"
    Battle_TfVfx_SelectionFramePulse

transform Battle_TfVfx_SelectionFramePulse:
    ease 0.65 zoom 1.05
    ease 0.35 zoom 1.0
    repeat

style frame_battle_target_sel:
    background Frame("Battle_SelectionFramePulsin", Borders(96, 96, 96, 96))
    padding (32, 32)

################################################################################################################
default Battle_ShowSelectionOutlines = False

init python:
    def BattleUI_BringInfoForward(Char):
        renpy.hide_screen("BattleCharInfoScreen_%s" % id(Char), layer = "master")
        renpy.show_screen("Battle_CharInfoOnBattlefield", 
                    BattleChar = Char, 
                    _zorder = getattr(Char, "HudZorder", 0) + 6,
                    _tag = "BattleCharInfoScreen_%s" % id(Char),
                    _layer = "master")

    def BattleUI_BringInfoBackward(Char):
        renpy.hide_screen("BattleCharInfoScreen_%s" % id(Char), layer = "master")
        renpy.show_screen("Battle_CharInfoOnBattlefield", 
                    BattleChar = Char, 
                    _zorder = getattr(Char, "HudZorder", 0),
                    _tag = "BattleCharInfoScreen_%s" % id(Char),
                    _layer = "master")
    
screen Battle_CharInfoOnBattlefield(BattleChar):
    if getattr(BattleChar, "IsAlive", False):
        $ slot_idx = getattr(BattleChar, "PositionSlotIndex", 0)
        $ side_idx = getattr(BattleChar, "BattleSide", 0)
        $ char_ref = getattr(BattleChar, "CharRef", {})
        $ active_chars = getattr(store.BattleScene, "ActiveCharsList", [])
        $ potential_targets = getattr(store.BattleScene, "ActionAwaitingTarget_PotentialTargetsList", [])

        if BattleChar == getattr(store.BattleScene, "SelectedLeft", None):
            add "images/gui/battle/sel_over.webp":
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[side_idx][slot_idx]
                yoffset 40
                matrixcolor OpacityMatrix(0.3) * TintMatrix((80, 80, 250))
        elif BattleChar == getattr(store.BattleScene, "SelectedRight", None):
            add "images/gui/battle/sel_over.webp":
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[side_idx][slot_idx]
                yoffset 40
                matrixcolor OpacityMatrix(0.3) * TintMatrix((250, 80, 80))

        vbox:
            anchor (0.5, 1.0)
            pos BattleChar_ScreenPositions[side_idx][slot_idx]

            # status effs box
            hbox:
                xalign 0.5
                spacing 4
                for StatusEffect in getattr(BattleChar, "StatusEffects", []):
                    fixed:
                        fit_first True
                        $ eff_type = getattr(StatusEffect, "EffectType", None)
                        if eff_type == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                            add Transform(("images/gui/battle/skill_matrix_bg.webp"), 
                                size = (44, 44), align = (0.5, 0.5), 
                                matrixcolor = TintMatrix((3, 107, 3)))
                        elif eff_type == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                            add Transform(("images/gui/battle/skill_matrix_bg.webp"), 
                                size = (44, 44), align = (0.5, 0.5), 
                                matrixcolor = TintMatrix((107, 3, 3)))
                        else:
                            add Transform(("images/gui/battle/skill_matrix_bg.webp"), 
                                size = (44, 44), align = (0.5, 0.5), 
                                matrixcolor = TintMatrix((107, 107, 3)))

                        imagebutton:
                            align (0.5, 0.5)
                            idle Transform(StatusEffect.Icon, xcenter = 0.5, size = (38, 38))
                            hovered [TooltipSetUI(GetStatusEffectDesc(StatusEffect)), Function(BattleUI_BringInfoForward, BattleChar)]
                            unhovered [TooltipClearUI(), Function(BattleUI_BringInfoBackward, BattleChar)]
                            keyboard_focus False
                            action NullAction()

                        if not getattr(StatusEffect, "Permanent", False):
                            text f"{StatusEffect.Duration}":
                                size 30
                                align (0.5, 1.0)
                                outlines [(absolute(1), "#000", absolute(0), absolute(0))]
            frame:
                style "frame_trans"
                yoffset 7
                padding (18, 4)
                xalign 0.5
                text char_ref.get("name", ""):
                    xalign 0.5 
                    text_align 0.5
                    if side_idx == getattr(store.BattleScene, "ActingSide", None):
                        if BattleChar not in active_chars:
                            color "#747678"
                    else:
                        color "#dddee0"
            bar:
                xalign 0.5
                style "bar_red_256"
                xsize 200
                ysize 20
                value AnimatedValue(value = getattr(BattleChar, "Health", 0), range = getattr(BattleChar, "HealthMax", 1), delay = 0.15)

            if char_ref.get("is_mage", False):
                bar:
                    xalign 0.5
                    style "bar_blue_256"
                    xsize 200
                    ysize 20
                    value AnimatedValue(value = getattr(BattleChar, "Mana", 0), range = getattr(BattleChar, "ManaMax", 1), delay = 0.15)
            else:
                bar:
                    xalign 0.5
                    style "bar_green_256"
                    xsize 200
                    ysize 20
                    value AnimatedValue(value = getattr(BattleChar, "Energy", 0), range = getattr(BattleChar, "EnergyMax", 1), delay = 0.15)

        # number caret
        if getattr(store.BattleScene, "ActionAwaitingTarget", None) and BattleChar in potential_targets:
            fixed:
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[side_idx][slot_idx]
                yoffset 10
                xmaximum 96
                ymaximum 10
                add "images/gui/battle/caret_up.webp":
                    align (0.5, 1.0)
                    matrixcolor OpacityMatrix(0.6)
                    zoom 0.98
                text "%s" % (potential_targets.index(BattleChar) + 1):
                    align (0.5, 1.0)

################################################################################################################
screen Battle_Portrait(CharObj = None, RightSide = False):
    fixed:
        xysize (200, 200)
        anchor (0.5, 0.5)
        if RightSide:
            pos (0.94, 0.89)
            if CharObj and hasattr(CharObj, "BattleSkin"):
                add "images/gui/battle/portrait_under_enemy.webp" align (0.5, 0.5) xoffset -45 yoffset -32 size (260, 260)
                add AlphaMask(CharObj.BattleSkin.Portrait, Transform("images/gui/battle/portrait_under_enemy.webp", size = (256, 256))):
                    align (0.5, 0.5)
                    xoffset -45
                    yoffset -22
                    xzoom -1.0
            else:
                add "images/gui/battle/portrait_under_blank.webp" align (0.5, 0.5) xoffset -45 yoffset -32 size (260, 260)
                text _("Select\nan enemy"):
                    align (0.5, 0.5) 
                    text_align 0.5 
                    xoffset -45 
                    yoffset -32 
                    color "#666363" 
                    size 40
            add "images/gui/battle/panel_enemy_port_over.webp" align (0.5, 0.5) xoffset 90 yoffset -12
        else:
            pos (0.06, 0.89)
            if CharObj and hasattr(CharObj, "BattleSkin"):
                add "images/gui/battle/portrait_under_ally.webp" align (0.5, 0.5) xoffset 45 yoffset -32 size (260, 260)
                add AlphaMask(CharObj.BattleSkin.Portrait, Transform("images/gui/battle/portrait_under_ally.webp", size = (256, 256))):
                    align (0.5, 0.5)
                    xoffset 45
                    yoffset -22
            else:
                add "images/gui/battle/portrait_under_blank.webp" align (0.5, 0.5) xoffset 45 yoffset -32 size (260, 260)
                text _("Select\nan ally"):
                    align (0.5, 0.5)
                    text_align 0.5
                    xoffset 45
                    yoffset -32
                    color "#666363"
                    size 40
            add "images/gui/battle/panel_ally_port_over.webp" align (0.5, 0.5) xoffset -90 yoffset -12

################################################################################################################
screen Battle_StatBox(BattleChar, RightSide = False):
    $ char_ref = getattr(BattleChar, "CharRef", {}) if BattleChar else {}
    frame:
        padding (4, 4)
        anchor (0.5, 0.0)
        if RightSide:
            pos (0.78, 861)
        else:
            pos (0.22, 861)
        vbox:
            use Battle_StatEntry(BattleChar, "Health", MaxStatID = "HealthMax", Big = True)
            if char_ref.get("is_mage", False):
                use Battle_StatEntry(BattleChar, "Mana", MaxStatID = "ManaMax", Big = True)
            else:
                use Battle_StatEntry(BattleChar, "Energy", MaxStatID = "EnergyMax", Big = True)
            hbox:
                vbox:
                    use Battle_StatEntry(BattleChar, "Damage")
                    use Battle_StatEntry(BattleChar, "AttackRating")
                    use Battle_StatEntry(BattleChar, "CritChance")
                vbox:
                    use Battle_StatEntry(BattleChar, "Armor")
                    use Battle_StatEntry(BattleChar, "DodgeRating")
                    use Battle_StatEntry(BattleChar, "MagicRes")

################################################################################################################
screen Battle_StatEntry(BattleChar, StatID, MaxStatID = None, Big = False):
    $ stat_name = tra(GUI_STAT_NAME_MAP.get(StatID, ""))
    $ stat_desc = tra(GUI_STAT_NAME_MAP.get(StatID + "_desc", ""))
    $ tooltip_text = f"{stat_name}\n{stat_desc}"
    button:
        action NullAction()
        background Frame("images/gui/battle/frame_tiny.webp", Borders(4, 4, 4, 4))
        if Big:
            xsize 160
        else:
            xsize 80
        ysize 39
        hbox:
            xoffset -6
            align (0.0, 0.5)
            spacing 2
            add GUI_ATTRIBUTE_ICON_MAP.get(StatID, "images/gui/battle/frame_tiny.webp") size (30, 30) align (0.5, 0.5)
            if MaxStatID:
                text f"{getattr(BattleChar, StatID, 0)}/{getattr(BattleChar, MaxStatID, 0)}" size 27
            else:
                text f"{getattr(BattleChar, StatID, 0)}" size 27

        hovered TooltipSetUI(tooltip_text)
        unhovered TooltipClearUI()
        keyboard_focus False

################################################################################################################
screen Battle_NameBox(BattleChar, RightSide = False):
    $ char_ref = getattr(BattleChar, "CharRef", {}) if BattleChar else {}
    $ char_name = tra(char_ref.get("name", ""))
    $ lvl = GetCharLevelFromChar(char_ref) if char_ref else 0
    hbox:
        spacing 5
        if RightSide:
            anchor (1.0, 1.0)
            pos (0.83, 0.76)
        else:
            anchor (0.0, 1.0)
            pos (0.17, 0.76)
        if RightSide:
            box_reverse True
        frame:
            padding (20, 10)
            if lvl > 0:
                label f"{char_name} (Lvl {lvl})":
                    text_size 35
                    text_color "#f0cbc2"
            else:
                label f"{char_name} (Lvl ??)":
                    text_size 35
                    text_color "#f0cbc2"

################################################################################################################
screen Battle_FullLog():
    modal True
    add "images/gui/unsorted/black_under.webp"
    frame:
        style "frame_outer"
        align (0.5, 0.5)
        vbox:
            spacing 30
            label _("Battle log"):
                xalign 0.5
            frame:
                xsize 650
                ysize 650
                viewport:
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    side_spacing 10
                    vbox:
                        for Entry in reversed(getattr(store.BattleScene, "LogEntries", [])):
                            text "{size=-5}" + str(Entry) + "{/size}" 

            textbutton _("(Esc) Close"):
                style "confirm_button"
                action Hide("Battle_FullLog")
                keysym "game_menu"

################################################################################################################
screen Battle_LogOrSkillDesc():
    $ ai_side = getattr(store.BattleScene, "AIControlSide", [False])
    $ can_auto = getattr(store.BattleScene, "CanAutoBattle", False)
    $ awaiting_action = getattr(store.BattleScene, "ActionAwaitingTarget", None)
    $ log_entries = getattr(store.BattleScene, "LogEntries", [])

    if not can_auto and ai_side[0]:
        frame:
            anchor (0.5, 1.0)
            pos (0.5, 1.0)
            xsize 880
            ysize 227
            yoffset -3
            padding (15, 10)
            viewport:
                scrollbars "vertical"
                draggable True
                mousewheel True
                side_spacing 10
                vbox:
                    for Entry in reversed(log_entries[-10:]):
                        text "{size=-5}" + str(Entry) + "{/size}" 
    else:
        frame:
            anchor (0.5, 1.0)
            pos (0.57, 1.0)
            xsize 585
            ysize 227
            yoffset -3
            padding (15, 10)
            if awaiting_action is not None:
                viewport:
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    hbox:
                        yoffset 4
                        spacing 10
                        imagebutton:
                            align (0.0, 0.0)
                            idle Transform("images/gui/battle/no_cross.webp", size = (100, 100), matrixcolor = IdentityMatrix())
                            hover Transform("images/gui/battle/no_cross.webp", size = (100, 100), matrixcolor = MxMapHover())
                            hovered TooltipSetUI(_("(Space) Cancel"))
                            unhovered TooltipClearUI()
                            action [TooltipClearUI(), Function(Battle_ClearActionAwaitingTarget), Return()]
                            keysym "K_SPACE"
                        text awaiting_action.GetDesc() size 28
            else:
                viewport:
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    side_spacing 10
                    vbox:
                        for Entry in reversed(log_entries[-10:]):
                            text "{size=-5}" + str(Entry) + "{/size}" 
    frame:
        padding (20, 8)
        anchor (0.5, 1.0)
        xpos 0.5
        ypos 860
        if awaiting_action is not None:
            label _("Select target") text_size 30
        else:
            label _("Battle log") text_size 30

    if awaiting_action is None:
        imagebutton:    
            pos (1354, 1046)
            anchor (0.5, 0.5)
            idle Transform("images/gui/top_right/hist_b.webp", size = (48, 48))
            hover Transform("images/gui/top_right/hist_h.webp", size = (48, 48))
            hovered TooltipSetUI(_("Open full battle log"))
            action Show("Battle_FullLog")

################################################################################################################
init python:
    def Battle_ToggleAutoBattle():
        if hasattr(store.BattleScene, "AIControlSide"):
            store.BattleScene.AIControlSide[0] = not store.BattleScene.AIControlSide[0]
        return

screen Battle_TurnCounter():
    $ can_auto = getattr(store.BattleScene, "CanAutoBattle", False)
    $ ai_side = getattr(store.BattleScene, "AIControlSide", [False])
    $ acting_side = getattr(store.BattleScene, "ActingSide", 0)
    $ turn_num = getattr(store.BattleScene, "Turn", 0)

    if can_auto:
        imagebutton:
            idle Transform("images/gui/battle/auto_battle_idle.webp", size = (78, 78), matrixcolor = IdentityMatrix())
            hover Transform("images/gui/battle/auto_battle_hover.webp", size = (78, 78), matrixcolor = IdentityMatrix())
            selected_idle Transform("images/gui/battle/auto_battle_hover.webp", size = (78, 78), matrixcolor = BrightnessMatrix(0.2))
            selected_hover Transform("images/gui/battle/auto_battle_hover.webp", size = (78, 78), matrixcolor = BrightnessMatrix(0.3))
            insensitive Transform("images/gui/battle/auto_battle_insen.webp", size = (78, 78), matrixcolor = IdentityMatrix())
            selected ai_side[0]
            hovered TooltipSetUI(_("Toggle auto-battle"))
            unhovered TooltipClearUI()
            anchor (0.5, 0.5)
            pos (0.0475, 0.155)
            action Function(Battle_ToggleAutoBattle)
    fixed:
        anchor (0.0, 0.0)
        pos (0.0, 0.0)
        add "images/gui/battle/turn_circle.webp":
            anchor (0.5, 0.5)
            zoom 0.5
            pos (45, 45)
            if acting_side == 1:
                rotate 180
        add "images/gui/battle/time_tracker_battle.webp":
            pos (-30, -30)
            zoom 0.5
        if getattr(store.BattleScene, "CanRetreat", False):
            imagebutton:
                idle Transform("images/gui/battle/retreat_base.webp", size = gui.button_size)
                hover Transform("images/gui/battle/retreat_hov.webp", size = gui.button_size)
                pos (12, 12)
                action Show("confirm", 
                            message = _("You are about to retreat from battle, are you sure? this will count as a {color=#ff0000}defeat{/color}."), 
                            yes_action = [Function(Battle_Retreat), Hide("confirm")],
                            no_action = Hide("confirm"))
        else:
            add "images/gui/battle/retreat_base.webp":
                size gui.button_size
                pos (12, 12)
                matrixcolor SaturationMatrix(0.0)
        if turn_num > 0:
            text f"{turn_num}":
                anchor (0.5, 0.5)
                size 41
                pos (46, 106)
                color "#edd0be"

################################################################################################################
screen Battle_SkillMenu(BattleChar, WaitForPlayerInput = False):
    modal True
    tag BattleSubMenu

    dismiss action Hide("Battle_SkillMenu")

    frame:
        anchor (0.0, 1.0)
        pos (0.31, 0.89)
        vbox:
            vpgrid:
                cols 4
                spacing 5
                for SkillIndex, SkillInstance in enumerate(getattr(BattleChar, "Skills", [])):
                    if SkillIndex < 9:
                        use Battle_SkillIcon(SkillInstance, HotKey = f"K_{SkillIndex + 1}", HotKeyText = str(SkillIndex + 1), FromSkillMenu = True, WaitForPlayerInput = WaitForPlayerInput)
                    elif SkillIndex == 9:
                        use Battle_SkillIcon(SkillInstance, HotKey = "K_0", HotKeyText = "0", FromSkillMenu = True, WaitForPlayerInput = WaitForPlayerInput)
                    else:
                        use Battle_SkillIcon(SkillInstance, FromSkillMenu = True, WaitForPlayerInput = WaitForPlayerInput)
            textbutton _("(s) Close"):
                text_size 40
                action [TooltipClearUI(), Hide("Battle_SkillMenu")]
                keysym "game_menu"

################################################################################################################
screen Battle_ItemMenu(BattleChar):
    modal True
    tag BattleSubMenu

    dismiss action Hide("Battle_ItemMenu")

    $ inv = getattr(store, "player_inv", {})
    $ items_dict = getattr(store, "all_items", {})
    $ valid_items = [ItemID for ItemID in inv.keys() if items_dict.get(ItemID, {}).get("on_use_battle") is not None]

    frame:
        anchor (0.0, 1.0)
        pos (0.31, 0.84)
        vbox:
            vpgrid:
                cols 4
                spacing 5
                for ItemNum, ItemID in enumerate(valid_items):
                    $ item_def = items_dict.get(ItemID, {})
                    $ action_func = store.ItemActionLib.get(item_def.get("on_use_battle")) if hasattr(store, "ItemActionLib") else None
                    $ item_action = action_func(Owner_BattleChar = BattleChar, ItemID = ItemID) if action_func else None
                    fixed:
                        fit_first True
                        imagebutton:
                            idle        Transform(item_def.get("icon"), matrixcolor = IdentityMatrix(),       size = gui.general_icon_size)
                            hover       Transform(item_def.get("icon"), matrixcolor = MxMapHover(),           size = gui.general_icon_size)
                            insensitive Transform(item_def.get("icon"), matrixcolor = SaturationMatrix(0.0),  size = gui.general_icon_size)

                            sensitive   BattleChar in getattr(store.BattleScene, "ActiveCharsList", [])
                            hovered     TooltipSetUI(GetItemDesc(ItemID, BattleChar = BattleChar))
                            unhovered   TooltipClearUI()
                            if inv.get(ItemID, 0) >= 1 and item_action:
                                if Battle_CanExecuteItemAction(item_action):
                                    action [Hide("Battle_ItemMenu"), 
                                        Function(Battle_PlayerScheduleActionOrEnterTargetingMode, BattleChar, item_action),
                                        TooltipClearUI(),
                                        Return()]

                            if ItemNum < 9:
                                keysym f"K_{ItemNum + 1}"
                            elif ItemNum == 9:
                                keysym "K_0"

                        if ItemNum <= 9:
                            add "images/gui/battle/caret_up.webp":
                                align (0.5, 1.05)
                                zoom 0.7
                            text (str(ItemNum + 1) if ItemNum < 9 else "0"):
                                size 24
                                align (0.5, 1.04)
                                
                        if inv.get(ItemID, 0) > 1:
                            text "x" + str(inv.get(ItemID)):
                                size 20
                                align (1.0, 0.9)

            textbutton _("(e) Close"):
                text_size 40
                action [TooltipClearUI(), Hide("Battle_ItemMenu")]
                keysym "game_menu"

################################################################################################################
screen Battle_NewTurnEffect():
    zorder -1
    add "circle_blip_blue":
        anchor (0.5, 0.5)
        pos (0.0, 0.0)
        at Battle_TfVfxTurnCircleExpand
    timer 0.6 action Hide("Battle_NewTurnEffect")

transform Battle_TfVfxTurnCircleExpand():
    zoom 0.0
    ease 0.6: 
        zoom 3.0
        alpha 0.0