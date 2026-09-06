screen locBtn_basic(locTag, tag, hoverSprite, transObj, key = None, IconAllTheTime = False):
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

    $ locObj = wLocs[locTag]
    if locObj.isBtnEnabled(tag):
        fixed:
            fit_first True
            anchor (0.5, 0.5)
            at transObj

            imagebutton:
                align (0.5, 0.5)
                #at transObj

                if IconAllTheTime:
                    idle_background "images/gui/buttons_loc/underlay.webp"
                    idle hoverSprite
                    hover_background "images/gui/buttons_loc/underlay.webp"
                    hover hoverSprite
                else:
                    idle "images/gui/buttons_loc/underlay.webp"
                    hover_background "images/gui/buttons_loc/underlay.webp"
                    hover hoverSprite
                focus_mask "images/gui/buttons_loc/underlay.webp"
                hovered TooltipSetUI(key_string + locObj.getHoverTxt(tag))
                clicked [TooltipClearUI(), Return(tag)]
                if key is not None:
                    keysym key

            if wLocs[locTag].isBtnQuestTracked(tag):
                use locBtn_QuestMarker(Offset = -40)