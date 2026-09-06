init python:
    def Battle_QueueFloatingTextOnChar(BattleChar, String, Kind = 0):
        BattleScene.NextFloatingValScreenIndex += 1
        ScreenTag = "FloatingValScreen_" + str(BattleScene.NextFloatingValScreenIndex)
        if BattleScene.NextFloatingValScreenIndex >= 10: # <- max floating val screens shown
            BattleScene.NextFloatingValScreenIndex = 0
        renpy.hide_screen(ScreenTag)
        CharPos = BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
        renpy.show_screen("Battle_FloatingVal", 
            _tag = ScreenTag, 
            FloatingVal = String, 
            Pos = (CharPos[0] + BattleChar.BattleSkin.SpriteVFXOffset[0], CharPos[1] + BattleChar.BattleSkin.SpriteVFXOffset[1]),
            Flip = (True if BattleChar.BattleSide == 1 else False),
            Kind = Kind)
        return

# kind 0 == damage
# kind 1 == healing
# kind 2 == crit damage
# kind 3 == burn damage
# kind 4 == poison damage
# kind 5 == bleed damage
screen Battle_FloatingVal(FloatingVal, Pos, Flip = False, Kind = 0):
    timer 1.5 action Hide(immediately = True)
    fixed:
        anchor (0.5, 0.5)
        maximum (300, 300)
        at FloatingValFadeout(Pos, Flip)
        add "images/gui/battle/floating_number_under.webp":
            align (0.5, 0.5)
            zoom 0.8
            if Kind == 0:
                matrixcolor TintMatrix(BATTLE_COLORS_LOG.DAMAGE)
            elif Kind == 1:
                matrixcolor TintMatrix(BATTLE_COLORS_LOG.RESTORE_ENERGY)
            elif Kind == 2:
                matrixcolor TintMatrix(BATTLE_COLORS_LOG.CRITICAL)
            elif Kind == 3:
                matrixcolor TintMatrix(BATTLE_COLORS_LOG.DAMAGE_BURN)
            elif Kind == 4:
                matrixcolor TintMatrix(BATTLE_COLORS_LOG.DAMAGE_POISON)
            elif Kind == 5:
                matrixcolor TintMatrix(BATTLE_COLORS_LOG.DAMAGE_BLEED)
        if Kind == 0:
            text "{color=[BATTLE_COLORS_LOG.DAMAGE]}" + str(FloatingVal) + "{/color}":
                size 45
                align (0.5, 0.5)
                outlines [(absolute(1), "#252121", absolute(0), absolute(0))]
        elif Kind == 1:
            text "{color=[BATTLE_COLORS_LOG.RESTORE_ENERGY]}" + str(FloatingVal) + "{/color}":
                size 45
                align (0.5, 0.5)
                outlines [(absolute(1), "#252121", absolute(0), absolute(0))]
        elif Kind == 2:
            text "{color=[BATTLE_COLORS_LOG.CRITICAL]}" + str(FloatingVal) + "\n" + tra(_("Crit!")) + "{/color}":
                text_align 0.5
                size 45
                align (0.5, 0.5)
                outlines [(absolute(1), "#252121", absolute(0), absolute(0))]
        elif Kind == 3:
            text "{color=[BATTLE_COLORS_LOG.DAMAGE_BURN]}" + str(FloatingVal) + "{/color}":
                size 45
                align (0.5, 0.5)
                outlines [(absolute(1), "#252121", absolute(0), absolute(0))]
        elif Kind == 4:
            text "{color=[BATTLE_COLORS_LOG.DAMAGE_POISON]}" + str(FloatingVal) + "{/color}":
                size 45
                align (0.5, 0.5)
                outlines [(absolute(1), "#252121", absolute(0), absolute(0))]
        elif Kind == 5:
            text "{color=[BATTLE_COLORS_LOG.DAMAGE_BLEED]}" + str(FloatingVal) + "{/color}":
                size 45
                align (0.5, 0.5)
                outlines [(absolute(1), "#252121", absolute(0), absolute(0))]

            
init python in BATTLE_COLORS_LOG:
    _constant = True
    BATTLE_STATUS = "#ffaa5b" # new turn/battle starts/char defeated

    DAMAGE = "#ff0000"
    DAMAGE_BLEED = "#ff0000"
    DAMAGE_POISON = "#3cff66"
    DAMAGE_BURN = "#ff8818"

    CRITICAL = "#ff0000"

    MISS = "#ff9d9d"

    NAME_ALLY = "#4b9fff"
    NAME_ENEMY = "#df223b"
    NAME_SKILL = "#f5bb3d"
    NAME_ITEM = "#69e6d5"

    RESTORE_HEALTH = "#ff9d9dff"
    RESTORE_ENERGY = "#bbff9cff"

transform FloatingValFadeout(Pos, Flip = False):
    subpixel True
    pos Pos
    alpha 0.0
    yoffset 45  
    ease 0.05:
        alpha 0.75
        zoom 1.5
    ease 1.25:
        alpha 0.0
        zoom 0.5
        yoffset -70
        xoffset (120 if Flip == True else -120)