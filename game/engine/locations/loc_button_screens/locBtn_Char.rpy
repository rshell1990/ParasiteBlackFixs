# its alot like complex, but night-tint is opt-in, and quest tracker is disabled 
screen locBtn_Char(locTag, tag, idleSprite, hoverSprite, transObj, key = None, NightTint = False):
    if key is not None:
        if len(key[0]) == 3:
            if key[0].startswith("K_"):
                default key_string = "(" + key[0].strip("K_") + ") "
            else:
                default key_string = "(" + key[0] + ") "
        else:
            default key_string = "(" + key[0] + ") "
    else:
        default key_string = ""
    if wLocs[locTag].isBtnEnabled(tag):
        fixed:
            fit_first True
            anchor (0.5, 0.5)
            at transObj

            imagebutton:
                if NightTint == True:
                    idle    Transform(idleSprite,  matrixcolor = wLocs[locTag].DayNightMatrix)
                    hover   Transform(hoverSprite, matrixcolor = wLocs[locTag].DayNightMatrix)
                else:
                    idle        idleSprite
                    hover       hoverSprite
                focus_mask  idleSprite

                hovered     TooltipSetUI(key_string + wLocs[locTag].getHoverTxt(tag))
                unhovered   TooltipClearUI() 

                clicked [TooltipClearUI(), Return(tag)]
                if key is not None:
                    keysym key
    
            if wLocs[locTag].isBtnQuestTracked(tag):
                use locBtn_QuestMarker

screen locBtn_QuestMarker(Offset = 0):
    add "images/gui/journal/quest_marker.webp":
        anchor (0.5, 1.0)
        # crazy fucking tricks
        xpos 0.5
        ypos 20
        yoffset Offset
        at questMarkerFloat
        matrixcolor OpacityMatrix(0.85)
