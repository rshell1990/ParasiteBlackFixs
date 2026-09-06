
screen location_name():
    if gui_parts["location_name"] and not IsPlayerInBattle() and not IsPlayerInBaratiGame() and PlayerPos.getName() is not None and IsUIDisplayed():
        fixed:
            fit_first True
            anchor (0.0, 1.0)
            pos    (0.0, 1.0)
            xsize  320
            add "images/gui/unsorted/corner.webp":
                xzoom -1    
            vbox:
                anchor  (0.0,  1.0)
                pos     (0.03, 0.97)
                spacing  0
                xsize    320
                text "%s" % PlayerPos.getName():
                    style "say_dialogue"
                    anchor (0.0, 1.0)
                    pos    (0.0, 1.0)
                    outlines [(1, "#303030", 0, 0)]
                    outline_scaling "step"
                if config.developer and DEV_VARIABLES["LOC_IDS"]:
                    textbutton "(dev) copy loc id":
                        align (0.0, 1.0)
                        hovered TooltipSetUI("(dev) copy loc id to clipboard")
                        unhovered TooltipClearUI()
                        action Function(DEBUG_GUI_SaveLocIDToClipboard)
                    text "{color=#949494}(DEV) internal loc tag: %s{/color}" % GetLocID():
                        style "say_dialogue"
                        anchor (0.0, 1.0)
                        pos    (0.0, 1.0)
                        outlines [(1, "#303030", 0, 0)]
                        outline_scaling "step"

init python:
    def DEBUG_GUI_SaveLocIDToClipboard():
        import pygame.scrap
        pygame.scrap.put(pygame.SCRAP_TEXT, GetLocID().encode("utf-8", "ignore"))
        return