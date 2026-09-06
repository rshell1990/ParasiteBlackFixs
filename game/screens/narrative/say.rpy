screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):
    zorder -1
    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)

    add "images/gui/story/textbox.webp":
        align (0.5, 1.0)
    if who is not None:
        label who id "who":
            pos (400, 830)
    fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect:
        if who is not None:
            ypos 880
        else:
            ypos 855
        xpos 420
        xmaximum 1100