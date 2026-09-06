label gallery_regina_buttplug:
    $ AutoMus(False)
    $ PlayMusic(wLocs["mc_house_kitchen"].dn_music.dayTrack)
    scene bg_mc_house_kitchen with dissolve
    show cg_regina_cooking_back at cleft
    with dissolve
    MC "(Looks like [regina_ref_cap!t] is busy cooking)."
    MC "({i}It doesn't seem like she's noticed me come in{/i})."
    MC "(Maybe I can ... ?)"

    $ PlayMusicRandom("mus_sex")
    scene regina_buttplug_1 with dissolve
    $ Pause()
    "While [regina_ref_cap!t] was distracted, I gently began to hike up her skirt more and more, revealing the black lace panties hugging against her butt beneath."
    "Wedged beneath, I could make out the outline of something beneath the panties themselves."
    "[regina_ref_cap!t] continued to hum away, and I contemplated just how much further I should push my luck ..."

    "Gently, I tugged and pulled down [regina_ref_cap!t]'s panties very slowly."

    scene regina_buttplug_2 with dissolve
    $ Pause()
    "Now fully visible, pressed between her ass was one of the jeweled toys."
    "A bronze plug with a green emerald like gem in the center."
    REGINA "... Are you enjoying the view back there?"
    MC "[regina_ref_cap!t]! I-"
    MC "How long have you known I've been stood here?!"
    REGINA "Long enough."
    REGINA "It's fine ... If you like what you see so much, why don't you touch it?"
    MC "I ..."

    menu:
        'Step back.':
            "Flustered, I quickly pulled back."
            #Scene goes back to character models talking

            $ PlayMusic(wLocs["mc_house_kitchen"].dn_music.dayTrack)
            scene black with dissolve
            scene bg_mc_house_kitchen with dissolve
            show regina lewd at cright_f
            show mc at cleft
            with dissolve

            REGINA @smile_talk "There's no point being shy now."
            REGINA @lewd_talk "You've caught me red-handed."
            MC @surprised "Y-Yes, but-"
            MC @surprised "I don't know what came over me!"
            "[regina_ref_cap!t] simply laughed."
            show regina smile
            REGINA @smile_talk "It's fine, you shouldn't be ashamed of such desires."

        'Grab her ass.':
            scene regina_buttplug_3 with dissolve
            $ Pause()
            "Reaching out, I nervously pawed and squeezed at [regina_ref_cap!t]'s ass."
            REGINA "Mhhff..."
            REGINA "See? There's nothing to worry about ..."
            MC "Should we really be-"
            REGINA "Mmhh, You have such strong hands now dear!"
            "I pulled back, heart racing." #scene goes back to character models talking 

            $ PlayMusic(wLocs["mc_house_kitchen"].dn_music.dayTrack)
            scene black with dissolve
            scene bg_mc_house_kitchen with dissolve
            show mc surprised at cleft
            show regina smile at cright_f
            with dissolve

            REGINA @smile_talk "There's no need to be embarrassed!"
            REGINA @smile_talk "You shouldn't feel ashamed of such desires."

    "There was something strange with her expression, a part of me wondered why she was so ... easy about all this."
    "But I remembered she had always been unusual when it came to affection with me."
    "Ever since I was young, she had been overly-affectionate, and remarkably candid when it came to the topic of sex."
    MC @surprised "I ... think I should go."
    REGINA @smile_talk "Be safe, dear!"
    return
