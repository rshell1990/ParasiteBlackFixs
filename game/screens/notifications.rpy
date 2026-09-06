
screen NotifBox():
    if (not IsPlayerInBattle()
        and not IsPlayerInBaratiGame()
        and IsUIDisplayed()
        and not UI_PartyCharsExtend):
        add "images/gui/unsorted/corner.webp":
            zoom 1.2
            align (1.0, 1.0)
            xoffset 4 # <- zoom fucks up offset
            yoffset 4
            matrixcolor OpacityMatrix(0.65)

    frame:
        background Null()
        xsize 340
        anchor (1.0, 1.0)
        pos (1.0, 1.0)
        if IsPlayerInBattle():
            yoffset -350
        else:
            if UI_PartyCharsExtend:
                # in english, "offset upwards by 190 then if party over 3, offset by 118 more for each extra three chars"
                yoffset -190 - (118 * (math.ceil(GetPartySize() / 3) - 1))
        
        vbox:
            box_reverse True
            #spacing 5
            xalign 0.5
            xfill True
            for msg_info index msg_info[1] in Notify_Messages:
                if msg_info[1] > renpy.time.time() - Notify_TotalDuration:
                    use NotifItem(msg_info[0], msg_info[2])

screen NotifItem(Message, Kind):
    frame:
        background Null()
        xalign 0.5
        #xoffset -25
        at TF_Notif
        text tra(Message):
            style "say_dialogue"
            text_align 0.5
            outlines [(1, "#303030", 0, 0)]
            outline_scaling "step"

transform TF_Notif():
    subpixel True
    # show
    yoffset -100
    alpha 0.0
    ease Notify_FadeIn:
        yzoom 1.0 
        yoffset 0 
        alpha 1.0
    # display 
    pause Notify_Stay
    # hide
    parallel:
        ease Notify_FadeOut:
            alpha 0.0
    parallel:
        ease Notify_MoveOut:
            yzoom 0.0
            yoffset 100

init python:
    # this is here bc its essentially a part of the transform
    Notify_FadeIn = 0.25
    Notify_Stay = 4.0
    Notify_FadeOut = 0.25
    Notify_MoveOut = 1.0
    Notify_TotalDuration = Notify_FadeIn + Notify_Stay + Notify_FadeOut + Notify_MoveOut

    config.context_copy_remove_screens.append("NotifBox") # <- old notif thing had this so lets do this too
    config.overlay_screens.append("NotifBox")
    