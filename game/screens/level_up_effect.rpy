init python:
    config.context_copy_remove_screens.append("level_up")
    DEBUG_HideLevelUpEffect = False

screen level_up():
    if DEBUG_HideLevelUpEffect == False:
        frame:
            at level_up_display
            padding (0, 0)
            anchor  (0.5, 0.2)   
            pos     (0.5, 0.1)
            # Background is used to display the black outline only
            background Text(_("{size=200}Level Up!{/size}"), outlines = [(2,"#000000")])
            # Foreground is used to diplay the yellow/red text
            foreground AlphaMask(Frame("images/gui/frames/gradient_yellow_to_red.webp"), Text(_("{size=200}Level Up!{/size}"), outlines = [(2, "#00000000")]))

            # Transparent text used to size the frame
            text _("{size=200}Level Up!{/size}"):
                size 200
                color "#00000000"
                outlines [(2, "#00000000")]

    timer 4.0 action Hide("level_up")

transform level_up_display:
    subpixel True
    alpha   0.0
    easein 1.0 zoom 1.0 alpha 1.0
    pause 2.5
    ease 0.5 alpha 0.0
