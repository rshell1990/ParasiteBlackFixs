label travel_event_set_camp:
    show mc serious at left with easeinleft
    MC "This place looks like a suitable one to set up a camp."
    if CharGetVar("mc", "Health") < CharGetVar("mc", "HealthMax") * 0.9:
        MC "I could use some rest."
    menu:
        "{image=[ICON.CLOCK]} Set up a camp":
            pass
        "Move on":
            return

    scene black with dissolve
    "Finding a nice clearing and deciding it was a good spot to set up camp for the day, I pitched my tent."
    scene expression TravelRoutes[TravelState.RouteID]["image_camp"]
    with dissolve

    $ Travel_RollPartyBanter_Camp()

    show mc serious at left
    with easeinleft

    $ Pause(1.5)

######################## random camp encounters section
    $ tmpvar = []

    # 1/5 chance to add pregnant lizard visits
    if RngInt(1, 5) == 1: 
        $ tmpvar.append("preg_lizards")

    # 1/10 base chance to add pregnant jackal visit
    if TravelRoutes[TravelState.RouteID]["biome_type"] == "desert":
        if RngInt(1, 20) == 1: 
            if QstIsActive(EventJackalGirlEncounter):
                if PregJackalGirl().NumBabiesShown < PregJackalGirl().NumBirths:
                    $ tmpvar.append("jackal_girl_shows_baby")

    # myu sex event
    if CharInParty("myu"):
        $ tmpvar.append("sex_myu")

    # myu/elena sex event
    if CharInParty("myu") and CharInParty("elena"):
        $ tmpvar.append("sex_myu_elena")

    # kiara encounter
    if CharInParty("kiara"):
        if QstIsOver(QstJudgementDay):
            if CharIsLover("kiara"):
                $ tmpvar.append("kiara_camp_scene")

### choose
    if len(tmpvar) > 0:
        $ tmpvar = renpy.random.choice(tmpvar)

############### pregnant lizards visit
    if tmpvar == "preg_lizards":
        call travel_event_lizard_camp_visit_choose from _call_travel_event_lizard_camp_visit_choose

######################## myu solo        
    elif tmpvar == "sex_myu":
        call travel_event_camp_myu_solo from _call_travel_event_camp_myu_solo

################ myu + elena
    elif tmpvar == "sex_myu_elena":
        call travel_event_camp_myu_elena from _call_travel_event_camp_myu_elena

########## jackal girl
    elif tmpvar == "jackal_girl_shows_baby":
        call travel_event_jackal_girl_pregnant_camp_visit from _call_travel_event_jackal_girl_pregnant_camp_visit
    
##### kiara visit
    elif tmpvar == "kiara_camp_scene":
        call travel_event_kiara_camp_scene from _call_travel_event_kiara_camp_scene

    $ tmpvar = {}
############## time skipping (sleepin restin)
    scene black with dissolve
    $ tmpvar = 8
    $ PlaySoundRandom("clockWind", Channel = "guisfx")
    while tmpvar > 0:
        $ TimeAdvBy(TIME_1H)
        $ tmpvar -= 1
        $ Pause(0.1)
        
    $ HealParty()
    $ tmpvar = {}
    return
