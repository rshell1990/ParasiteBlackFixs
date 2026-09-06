label debug_fortress_in_teleport:
    "DEBUG: which variant?"
    menu:
        "wench":
            jump travel_event_fortress_inn_wench
        "frog":
            jump travel_event_fortress_inn_frog
        "cat":
            jump travel_event_fortress_inn_cat

# root entry points
label travel_event_fortress_inn_wench:
    $ EventFortressInn().SetVariant("wench")
    jump travel_event_fortress_inn

label travel_event_fortress_inn_frog:
    $ EventFortressInn().SetVariant("frog")
    jump travel_event_fortress_inn

label travel_event_fortress_inn_cat:
    $ EventFortressInn().SetVariant("cat")
    jump travel_event_fortress_inn

label travel_event_fortress_inn:
    if IsDaytime():
        scene bg_inn_exterior
    else:
        scene bg_inn_exterior_night
    with dissolve
    show mc at cleft with easeinleft
    MC "(A fortress inn... We should consider stopping here to rest.)"
    menu:
        "Head in.":
            hide mc with easeoutright
            scene black with dissolve
            "We headed into the Fortress inn for a reprieve from our travels..."
            pass
        "Move on.":
            MC "(On second thought, it was probably best to keep moving.)"
            $ GetOutToWorldMap()
    # this assumes the correct variant is already picked by the intro
    $ LocSet("fortress_inn")
    $ LocEnter()

label fortress_inn_to_room:
    scene black with dissolve
    $ AutoAmb(False)
    stop ambience fadeout 1.0
    if IsDaytime():
        $ TimeAdvTo(TIME_LATEEVENING)
    if EventFortressInn().ScheduledFuntime:
        if EventFortressInn().VariantID == "cat":
            call fortress_inn_lucy_night from _call_fortress_inn_lucy_night
            jump fortress_inn_sleep
        elif EventFortressInn().VariantID == "wench":
            call fortress_inn_betty_night from _call_fortress_inn_betty_night
            jump fortress_inn_sleep
        elif EventFortressInn().VariantID == "frog":
            call fortress_inn_vivian_night from _call_fortress_inn_vivian_night
            jump fortress_inn_sleep
    else:
        jump fortress_inn_sleep

label fortress_inn_sleep:
    scene black with dissolve
    $ Pause(0.5)
    $ HealParty()
    $ TimeAdvTo(TIME_MORNING)
    $ Pause(0.5)
    if IsDaytime():
        scene bg_inn_exterior
    else:
        scene bg_inn_exterior_night
    with dissolve
    show mc at center with dissolve
    MC "(Let's move on.)"
    hide mc with easeoutright
    $ AutoAmb(True)
    $ GetOutToWorldMap()

label travel_fortress_inn_leave:
    MC "(Should we leave this place and move on?)"
    menu:
        "Continue travel":
            scene black with dissolve
            $ LocNameReset()
            $ GetOutToWorldMap()
        "Stay":
            $ LocEnterQ()
        "DEBUG: jump to hamun docks":
            $ LocNameReset()
            $ Travel_ForceEnd()
            $ LocSet("hamun_dist_docks")
            $ LocEnterQ()
