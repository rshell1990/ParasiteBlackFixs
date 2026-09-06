################################################################################################################
################################################################################################################
################################################################################################################
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
    use Battle_Portrait(BattleScene.SelectedLeft)
    if BattleScene.SelectedLeft:
        use Battle_StatBox(BattleScene.SelectedLeft)
        use Battle_NameBox(BattleScene.SelectedLeft)

    # empty space (separate action sel panel)
    
    ##
    ##
    ##

    # portrait & statbox right (first for layering)
    if BattleScene.SelectedRight:
        use Battle_StatBox(BattleScene.SelectedRight, RightSide = True)
        use Battle_NameBox(BattleScene.SelectedRight, RightSide = True)

    # log
    use Battle_LogOrSkillDesc()
    # portrait 
    use Battle_Portrait(BattleScene.SelectedRight, RightSide = True)
################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_ActionSelectPanel(WaitForPlayerInput = False):
    # skills, items
    hbox:
        anchor (0.5, 0.0)
        pos (640, 861)
        if BattleScene.SelectedLeft:
            vbox:
                use Battle_SkillIcon(BattleScene.SelectedLeft.Skill_Attack, HotKey = "K_a", HotKeyText = "a", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)
                use Battle_SkillIcon(BattleScene.SelectedLeft.Skill_Defend, HotKey = "K_d", HotKeyText = "d", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)
                
                if BattleScene.SelectedLeft.CharRef["HasAltForm"]:
                    if BattleScene.CanTransform:
                        if BattleScene.SelectedLeft.CharRef["Transformed"]:
                            use Battle_SkillIcon(BattleScene.SelectedLeft.Skill_ExtraUnTransform, HotKey = "K_x", HotKeyText = "x", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)
                        else:
                            if BattleScene.SelectedLeft.CharRef["AltForm_Unlocked"]:
                                use Battle_SkillIcon(BattleScene.SelectedLeft.Skill_ExtraTransform, HotKey = "K_x", HotKeyText = "x", FromSkillMenu = False, WaitForPlayerInput = WaitForPlayerInput)

            vbox:
                if BattleScene.CanUseItems:
                    textbutton _("(e) Items"):
                        yalign 0.5
                        style "battle_itemskills_button"
                        keysym "K_e"
                        if BattleScene.SelectedLeft in BattleScene.ActiveCharsList and WaitForPlayerInput and len([ItemID for ItemID in player_inv.keys() if all_items[ItemID]["on_use_battle"] is not None]) > 0:
                            action Show("Battle_ItemMenu", BattleChar = BattleScene.SelectedLeft)

                textbutton _("(s) Skills"):
                    yalign 0.5
                    style "battle_itemskills_button"
                    keysym "K_s"
                    if BattleScene.SelectedLeft in BattleScene.ActiveCharsList and WaitForPlayerInput and len(BattleScene.SelectedLeft.Skills) > 0:
                        action Show("Battle_SkillMenu", BattleChar = BattleScene.SelectedLeft, WaitForPlayerInput = WaitForPlayerInput)

    # selection arrows over portrait
    if len(Battle_GetAliveCharsOnSide(Side = 0)) > 1 and BattleScene.SelectedLeft:
        hbox:
            anchor (0.5, 0.5)
            pos (0.081, 0.97)
            spacing 80
            textbutton "<< (z)":
                if BattleScene.ActionAwaitingTarget is None:
                    action Function(Battle_SelectArrowLeft) keysym "K_z"
            textbutton "(c) >>":
                if BattleScene.ActionAwaitingTarget is None:
                    action Function(Battle_SelectArrowRight) keysym "K_c"
        
init python:
    def Battle_SelectArrowLeft():
        AllAliveChars = Battle_GetAliveCharsOnSide(Side = 0)
        ThisCharIndex = AllAliveChars.index(BattleScene.SelectedLeft)
        Battle_SelectLeftChar(AllAliveChars[ThisCharIndex - 1])
        return

    def Battle_SelectArrowRight():
        AllAliveChars = Battle_GetAliveCharsOnSide(Side = 0)
        ThisCharIndex = AllAliveChars.index(BattleScene.SelectedLeft)
        if ThisCharIndex + 1 == len(AllAliveChars):
            Battle_SelectLeftChar(AllAliveChars[0])
        else:
            Battle_SelectLeftChar(AllAliveChars[ThisCharIndex + 1])
        return
################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_SkillIcon(SkillInstance, HotKey = None, HotKeyText = None, FromSkillMenu = False, WaitForPlayerInput = False):
    fixed:
        fit_first True
        imagebutton:
            sensitive WaitForPlayerInput
            if not WaitForPlayerInput:
                idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
            unhovered   TooltipClearUI()
            if WaitForPlayerInput:
                if SkillInstance.Owner_BattleChar in BattleScene.ActiveCharsList:
                    # cant use bc once per turn/used
                    if (SkillInstance.OncePerTurn and SkillInstance.UsedThisTurn):
                        idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                        hover       Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1) * SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                        hovered     TooltipSetUI(Text("{size=+6}{color=[BATTLE_COLORS.REQ_MISSING]}Already used this turn{/color}{/size}\n" + GetSkillDesc(SkillInstance)))
                        action      NullAction()
                    else:
                        # char can cover resource cost
                        if SkillInstance.OwnerCharCanPaySkillCost() and SkillInstance.CanExecute():
                            # case 1 there are valid targets
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
                            # case 2 theres no valid targets:
                            else:
                                idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                                hover       Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1) * SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                                hovered     TooltipSetUI(Text(GetSkillDesc(SkillInstance) + "\nNO TARGETS"))
                                action      NullAction()

                        # char cant conver resource cost
                        else:
                            idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                            hover       Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.1) * SaturationMatrix(0.0), size = gui.general_icon_size_lower)
                            hovered     TooltipSetUI(Text(Battle_GetUnmetCostAsString(SkillInstance) + GetSkillDesc(SkillInstance)))
                            action      NullAction()

                    
                else:
                    idle        Transform(SkillInstance.Icon, matrixcolor = SaturationMatrix(0.0), size = gui.general_icon_size_lower)

        if HotKey and HotKeyText:
            add "images/gui/battle/caret_up.webp":
                align (0.5, 1.05)
                zoom 0.7
            text HotKeyText:
                size 24
                align (0.5, 1.04)
################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_CharSelectionPanels(SelectSkillTarget = False):
    layer "master"
    for BattleChar in BattleScene.BattleChars[0] + BattleScene.BattleChars[1]:
        if BattleChar.IsAlive:
            button:
                if Battle_ShowSelectionOutlines:
                    style "frame_trans"
                elif SelectSkillTarget and BattleChar in BattleScene.ActionAwaitingTarget_PotentialTargetsList:
                    style "frame_battle_target_sel"
                    keysym "%s" % (BattleScene.ActionAwaitingTarget_PotentialTargetsList.index(BattleChar) + 1)
                else:
                    background Null()
                xsize int(BattleChar.BattleSkin.FocusRectSize[0] * (0.9 if BattleChar.PositionSlotIndex in [0, 1] else 1.0))
                ysize int(BattleChar.BattleSkin.FocusRectSize[1] * (0.9 if BattleChar.PositionSlotIndex in [0, 1] else 1.0))
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]

                offset BattleChar.BattleSkin.FocusRectOffset

                if SelectSkillTarget:
                    if BattleChar in BattleScene.ActionAwaitingTarget_PotentialTargetsList:
                        action  [Function(Battle_ClearActionAwaitingTarget),
                                    Function(Battle_SetCharAction, BattleScene.ActionAwaitingTarget.Owner_BattleChar, BattleScene.ActionAwaitingTarget, BattleChar),
                                    Function(Battle_SetUISelection, Side = BattleChar.BattleSide, Char = BattleChar),
                                    TooltipSetUI(BattleChar.CharRef["name"]),
                                    Return()]
                else:
                    action Function(Battle_SetUISelection, Side = BattleChar.BattleSide, Char = BattleChar)

                hovered [TooltipSetUI(Battle_GetTargetingTooltipForCurrentAction(BattleChar)), Function(BattleUI_BringInfoForward, BattleChar)]
                unhovered [TooltipClearUI(), Function(BattleUI_BringInfoBackward, BattleChar)]

init python:
    def Battle_GetTargetingTooltipForCurrentAction(TargetBattleChar):
        
        ReturnStrings = []
        ReturnStrings.append(tra(TargetBattleChar.CharRef["name"]))

        if BattleScene.ActionAwaitingTarget is not None:
            ActionToCheck = BattleScene.ActionAwaitingTarget
            if ActionToCheck.ShowHitChance == True:
                IsEnemy = (False if TargetBattleChar.BattleSide == ActionToCheck.Owner_BattleChar.BattleSide else True)
                if IsEnemy:
                    HitProb = Battle_GetHitProb(ActionToCheck.Owner_BattleChar, TargetBattleChar)
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
################################################################################################################
################################################################################################################
default Battle_ShowSelectionOutlines = False

init python:
    def BattleUI_BringInfoForward(Char):
        renpy.hide_screen("BattleCharInfoScreen_%s" % id(Char), layer = "master")
        renpy.show_screen("Battle_CharInfoOnBattlefield", 
                    BattleChar = Char, 
                    _zorder = Char.HudZorder + 6,
                    _tag = "BattleCharInfoScreen_%s" % id(Char),
                    _layer = "master")

    def BattleUI_BringInfoBackward(Char):
        renpy.hide_screen("BattleCharInfoScreen_%s" % id(Char), layer = "master")
        renpy.show_screen("Battle_CharInfoOnBattlefield", 
                    BattleChar = Char, 
                    _zorder = Char.HudZorder,
                    _tag = "BattleCharInfoScreen_%s" % id(Char),
                    _layer = "master")
    
screen Battle_CharInfoOnBattlefield(BattleChar):
    if BattleChar.IsAlive:
        if BattleChar == BattleScene.SelectedLeft:
            add "images/gui/battle/sel_over.webp":
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
                yoffset 40
                matrixcolor OpacityMatrix(0.3) * TintMatrix((80, 80, 250))
        elif BattleChar == BattleScene.SelectedRight:
            add "images/gui/battle/sel_over.webp":
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
                yoffset 40
                matrixcolor OpacityMatrix(0.3) * TintMatrix((250, 80, 80))
        vbox:
            anchor (0.5, 1.0)
            pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]

            # status effs box
            hbox:
                xalign 0.5
                spacing 4
                for StatusEffect in BattleChar.StatusEffects:
                    fixed:
                        fit_first True
                        # buff -- green
                        if StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.BUFF:
                            add Transform(("images/gui/battle/skill_matrix_bg.webp"), 
                                size = (44, 44), align = (0.5, 0.5), 
                                matrixcolor = TintMatrix((3, 107, 3)))
                        # debuff -- red
                        elif StatusEffect.EffectType == BATTLE_STATUS_EFFECT_TYPE.DEBUFF:
                            add Transform(("images/gui/battle/skill_matrix_bg.webp"), 
                                size = (44, 44), align = (0.5, 0.5), 
                                matrixcolor = TintMatrix((107, 3, 3)))
                        # neutral -- yellow
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

                        if StatusEffect.Permanent == False:
                            text f"{StatusEffect.Duration}":
                                size 30
                                align (0.5, 1.0)
                                outlines [(absolute(1), "#000", absolute(0), absolute(0))]
            frame:
                style "frame_trans"
                yoffset 7
                padding (18, 4)
                xalign 0.5
                text BattleChar.CharRef["name"]:
                    xalign 0.5 
                    text_align 0.5
                    if BattleChar.BattleSide == BattleScene.ActingSide:
                        if BattleChar not in BattleScene.ActiveCharsList:
                            color "#747678"
                    else:
                        color "#dddee0"
            bar:
                xalign 0.5
                style "bar_red_256"
                xsize 200
                ysize 20
                value AnimatedValue(value = BattleChar.Health, range = BattleChar.HealthMax, delay = 0.15)
            if BattleChar.CharRef["is_mage"] == True:
                bar:
                    xalign 0.5
                    style "bar_blue_256"
                    xsize 200
                    ysize 20
                    value AnimatedValue(value = BattleChar.Mana, range = BattleChar.ManaMax, delay = 0.15)
            else:
                bar:
                    xalign 0.5
                    style "bar_green_256"
                    xsize 200
                    ysize 20
                    value AnimatedValue(value = BattleChar.Energy, range = BattleChar.EnergyMax, delay = 0.15)
        # number caret
        if BattleScene.ActionAwaitingTarget and BattleChar in BattleScene.ActionAwaitingTarget_PotentialTargetsList:
            fixed:
                anchor (0.5, 1.0)
                pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
                yoffset 10
                xmaximum 96
                ymaximum 10
                add "images/gui/battle/caret_up.webp":
                    align (0.5, 1.0)
                    matrixcolor OpacityMatrix(0.6)
                    zoom 0.98
                text "%s" % (BattleScene.ActionAwaitingTarget_PotentialTargetsList.index(BattleChar) + 1):
                    align (0.5, 1.0)


################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_Portrait(CharObj = None, RightSide = False):
    fixed:
        xysize (200, 200)
        anchor (0.5, 0.5)
        if RightSide:
            pos (0.94, 0.89)
            if CharObj:
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
            if CharObj:
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
            # if len(Battle_GetAliveCharsOnSide(0)) > 1:
            #     hbox:
            #         align (0.5, 0.5)
            #         textbutton "<"
            #         textbutton ">"


################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_StatBox(BattleChar, RightSide = False):
    frame:
        padding (4, 4)
        anchor (0.5, 0.0)
        if RightSide:
            pos (0.78, 861)
        else:
            pos (0.22, 861)
        vbox:
            use Battle_StatEntry(BattleChar, "Health", MaxStatID = "HealthMax", Big = True)
            if BattleChar.CharRef["is_mage"] == True:
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
################################################################################################################
################################################################################################################
screen Battle_StatEntry(BattleChar, StatID, MaxStatID = None, Big = False):
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
            add GUI_ATTRIBUTE_ICON_MAP[StatID] size(30, 30) align(0.5, 0.5)
            if MaxStatID:
                text f"{getattr(BattleChar, StatID)}/{getattr(BattleChar, MaxStatID)}" size 27
            else:
                text f"{getattr(BattleChar, StatID)}" size 27
        #hovered TooltipSetUI(f"{GUI_STAT_NAME_MAP[StatID]}\n{GUI_STAT_NAME_MAP[StatID + "_desc"]}")
        hovered TooltipSetUI("%s\n%s" % (tra(GUI_STAT_NAME_MAP[StatID]), tra(GUI_STAT_NAME_MAP[StatID + "_desc"])))
        unhovered TooltipClearUI()
        keyboard_focus False

################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_NameBox(BattleChar, RightSide = False):
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
            if GetCharLevelFromChar(BattleChar.CharRef) > 0:
                label tra(BattleChar.CharRef["name"]) + " " + tra(_("(Lvl %s)")) % GetCharLevelFromChar(BattleChar.CharRef):
                    text_size 35
                    text_color "#f0cbc2"
            else:
                label tra(BattleChar.CharRef["name"]) + tra(_("(Lvl ??)")):
                    text_size 35
                    text_color "#f0cbc2"
################################################################################################################
################################################################################################################
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
                        for Entry in reversed(BattleScene.LogEntries):
                            text "{size=-5}" + str(Entry) + "{/size}" 

            textbutton _("(Esc) Close"):
                style "confirm_button"
                action Hide("Battle_FullLog")
                keysym "game_menu"

################################################################################################################
################################################################################################################
################################################################################################################

# log/desc is centered between 2 panels
screen Battle_LogOrSkillDesc():
    # "if we're in spectator battle"
    if (BattleScene.CanAutoBattle == False and BattleScene.AIControlSide[0] == True):
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
                    for Entry in reversed(BattleScene.LogEntries[-10:]):
                        text "{size=-5}" + str(Entry) + "{/size}" 
    else:
        frame:
            anchor (0.5, 1.0)
            pos (0.57, 1.0)
            xsize 585
            ysize 227
            yoffset -3
            padding (15, 10)
            if BattleScene.ActionAwaitingTarget is not None:
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
                            keysym ["K_SPACE"]
                        text BattleScene.ActionAwaitingTarget.GetDesc() size 28
            else:
                viewport:
                    scrollbars "vertical"
                    draggable True
                    mousewheel True
                    side_spacing 10
                    vbox:
                        for Entry in reversed(BattleScene.LogEntries[-10:]):
                            text "{size=-5}" + str(Entry) + "{/size}" 
    frame:
        padding (20, 8)
        anchor (0.5, 1.0)
        xpos 0.5
        ypos 860
        if BattleScene.ActionAwaitingTarget != None:
            label _("Select target") text_size 30
        else:
            label _("Battle log") text_size 30

    if BattleScene.ActionAwaitingTarget is None:
        # full log btn
        imagebutton:    
            pos (1354, 1046)
            anchor (0.5, 0.5)
            idle Transform("images/gui/top_right/hist_b.webp", size = (48, 48))
            hover Transform("images/gui/top_right/hist_h.webp", size = (48, 48))
            hovered TooltipSetUI(_("Open full battle log"))
            action Show("Battle_FullLog")

################################################################################################################
################################################################################################################
################################################################################################################
init python:
    def Battle_ToggleAutoBattle():
        BattleScene.AIControlSide[0] = not BattleScene.AIControlSide[0]
        return

screen Battle_TurnCounter():
    if BattleScene.CanAutoBattle:
        imagebutton:
            idle Transform("images/gui/battle/auto_battle_idle.webp", size = (78, 78), matrixcolor = IdentityMatrix())
            hover Transform("images/gui/battle/auto_battle_hover.webp", size = (78, 78), matrixcolor = IdentityMatrix())
            selected_idle Transform("images/gui/battle/auto_battle_hover.webp", size = (78, 78), matrixcolor = BrightnessMatrix(0.2))
            selected_hover Transform("images/gui/battle/auto_battle_hover.webp", size = (78, 78), matrixcolor = BrightnessMatrix(0.3))
            insensitive Transform("images/gui/battle/auto_battle_insen.webp", size = (78, 78), matrixcolor = IdentityMatrix())
            selected BattleScene.AIControlSide[0]
            hovered TooltipSetUI(_("Toggle auto-battle"))
            unhovered TooltipClearUI()
            anchor (0.5, 0.5)
            pos (0.0475, 0.155)
            action Function(Battle_ToggleAutoBattle)
    fixed:
        anchor (0.0,0.0)
        pos (0.0,0.0)
        add "images/gui/battle/turn_circle.webp":
            anchor (0.5,0.5)
            zoom 0.5
            pos (45, 45)
            if BattleScene.ActingSide == 1:
                rotate 180
        add "images/gui/battle/time_tracker_battle.webp":
            pos (-30,-30)
            zoom 0.5
        if BattleScene.CanRetreat:
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
        if BattleScene.Turn > 0:
            text f"{BattleScene.Turn}":
                anchor (0.5, 0.5)
                size 41
                pos (46, 106)
                color "#edd0be"
################################################################################################################
################################################################################################################
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
                for SkillIndex, SkillInstance in enumerate(BattleChar.Skills):
                    if SkillIndex < 9:
                        use Battle_SkillIcon(SkillInstance, HotKey = f"K_{SkillIndex + 1}", HotKeyText = str(SkillIndex + 1), FromSkillMenu = True, WaitForPlayerInput= WaitForPlayerInput)
                    elif SkillIndex == 9:
                        use Battle_SkillIcon(SkillInstance, HotKey = "K_0", HotKeyText = str(0), FromSkillMenu = True, WaitForPlayerInput = WaitForPlayerInput)
                    else:
                        use Battle_SkillIcon(SkillInstance, FromSkillMenu = True, WaitForPlayerInput = WaitForPlayerInput)
            textbutton _("(s) Close"):
                text_size 40
                action [TooltipClearUI(), Hide("Battle_SkillMenu")]
                keysym ["K_s", "game_menu"]

################################################################################################################
################################################################################################################
################################################################################################################
screen Battle_ItemMenu(BattleChar):
    modal True
    tag BattleSubMenu

    dismiss action Hide("Battle_ItemMenu")

    frame:
        anchor (0.0, 1.0)
        pos (0.31, 0.84)
        vbox:
            vpgrid:
                cols 4
                spacing 5
                for ItemNum, ItemID in enumerate([ItemID for ItemID in player_inv.keys() if all_items[ItemID]["on_use_battle"] is not None]):
                    fixed:
                        fit_first True
                        imagebutton:
                            idle        Transform(all_items[ItemID]["icon"], matrixcolor = IdentityMatrix(),       size = gui.general_icon_size)
                            hover       Transform(all_items[ItemID]["icon"], matrixcolor = MxMapHover(),           size = gui.general_icon_size)
                            insensitive Transform(all_items[ItemID]["icon"], matrixcolor = SaturationMatrix(0.0),  size = gui.general_icon_size)

                            sensitive   BattleChar in BattleScene.ActiveCharsList
                            hovered     TooltipSetUI(GetItemDesc(ItemID, BattleChar = BattleChar))
                            unhovered   TooltipClearUI()
                            if player_inv[ItemID] >= 1:
                                if Battle_CanExecuteItemAction(ItemActionLib[all_items[ItemID]["on_use_battle"]](Owner_BattleChar = BattleChar, ItemID = ItemID)):
                                    action [Hide("Battle_ItemMenu"), 
                                        Function(Battle_PlayerScheduleActionOrEnterTargetingMode, BattleChar, 
                                                ItemActionLib[all_items[ItemID]["on_use_battle"]](Owner_BattleChar = BattleChar, ItemID = ItemID)),
                                        TooltipClearUI(),
                                        Return()]

                            if ItemNum < 9:
                                keysym f"K_{ItemNum + 1}"
                                # text is str(ItemNum + 1)
                            elif ItemNum == 9:
                                keysym "K_0"
                                # text is str(0)

                        if ItemNum <= 9:
                            add "images/gui/battle/caret_up.webp":
                                align (0.5, 1.05)
                                zoom 0.7
                            text (str(ItemNum + 1) if ItemNum < 9 else str(0)):
                                size 24
                                align (0.5, 1.04)
                                
                        if player_inv[ItemID] > 1:
                            text "x" + str(player_inv[ItemID]):
                                size 20
                                align (1.0, 0.9)
                            

            textbutton _("(e) Close"):
                text_size 40
                action [TooltipClearUI(), Hide("Battle_ItemMenu")]
                keysym ["K_e", "game_menu"]
################################################################################################################
################################################################################################################
################################################################################################################

screen Battle_NewTurnEffect():
    zorder -1
    add "circle_blip_blue":
        anchor (0.5,0.5)
        pos (0.0,0.0)
        at Battle_TfVfxTurnCircleExpand
    timer 0.6 action Hide("Battle_NewTurnEffect")


transform Battle_TfVfxTurnCircleExpand():
    zoom 0.0
    ease 0.6: 
        zoom 3.0
        alpha 0.0
################################################################################################################
################################################################################################################
################################################################################################################