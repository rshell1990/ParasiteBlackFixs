transform TFSatyrLogo_ArrowAnim:
    subpixel True
    ease 0.35:
        xoffset 30
        alpha 1.0
    ease 0.4:
        xoffset 0
    repeat

transform TFSatyrLogo_ArrowDefaultPos:
    subpixel True
    easeout 0.35:
        xoffset 0
        alpha 0.0

transform TFSatyrLogo_GlowInOut:
    linear 0.5:
        alpha 0.0
    linear 0.5:
        alpha 1.0
    repeat

transform TFSatyrLogo_AlphaAt(AlphaAmt):
    ease 0.25:
        alpha AlphaAmt

screen satyr_main_menu():
    default Hovered = False
    button:
        anchor (0.5, 0.5)
        pos (0.94, 0.915)
        xysize (160, 160)
        background Null()
        add "images/gui/satyr/bg.webp": 
            xsize 150 
            fit "contain" 
            align (0.5, 0.5)
            if Hovered:
                at TFSatyrLogo_AlphaAt(0.8)
            else:
                at TFSatyrLogo_AlphaAt(0.2)
        add "images/gui/satyr/glow.webp": 
            xsize 150 
            fit "contain" 
            align (0.5, 0.5)
            if Hovered:
                matrixcolor BrightnessMatrix(0.1)
                at TFSatyrLogo_GlowInOut
            else:
                at TFSatyrLogo_AlphaAt(0.2)
        add "images/gui/satyr/persona.webp": 
            xsize 150 
            fit "contain" 
            align (0.5, 0.5)
            if Hovered:
                matrixcolor BrightnessMatrix(0.1)
                at TFSatyrLogo_AlphaAt(1.0)
            else:
                at TFSatyrLogo_AlphaAt(0.2)
        #add "images/gui/satyr/arrow.webp": 
        #    xsize 90 
        #    fit "contain" 
        #    align (0.5, 0.5)
        #    xoffset -125
        #    if Hovered:
        #        matrixcolor BrightnessMatrix(0.1)
        #        at TFSatyrLogo_ArrowAnim
        #    else:
        #        at TFSatyrLogo_ArrowDefaultPos
        hovered SetLocalVariable("Hovered", True)
        unhovered SetLocalVariable("Hovered", False)

        action [
            If(
                persistent.launcheroptimization,
                true=[
                    SetVariable("launcher_downloads_requested", False),
                    SetVariable("launcher_cover_selected", 1),
                    SetVariable("launcher_thumb_txpos", 0),
                    SetVariable("launcher_show", True),
                    SetVariable("launcher_show_bg", False),
                    SetField(persistent, "launcheroptimization", False),
                    Function(refresh_launcher_session)
                ],
                false=[
                    SetVariable("launcher_thumb_txpos", -config.screen_width * 7 // 8 - 50),
                    SetVariable("launcher_show", False),
                    SetField(persistent, "launcheroptimization", True)
                ]
            )
        ]
