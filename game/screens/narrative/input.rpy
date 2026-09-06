screen input(prompt):
    modal True
    zorder -1

    on "show" action SetVariable("block_wait_dynamic", True)
    on "hide" action SetVariable("block_wait_dynamic", False)

    add "images/gui/story/textbox.webp":
        align (0.5, 1.0)
        
    text prompt:
        style "say_dialogue"
        size 35
        xalign 0.5
        ypos 850
        xmaximum 1100
    input id "input":
        style "say_dialogue"
        xalign 0.5
        ypos 900
        