label sexscene_arwen_betweenlegs:
    ARWEN @blush 'Oh would you now?'
    ARWEN @laugh 'Right this way...'
    scene black with dissolve
    "I followed Arwen as she lead me into one of the bordello's private rooms."
    scene bg_weeping_heart_brothel_room
    $ CharSetClothes("arwen", "normal")
    $ LocNameSetTemp(_("Brothel Room"))
    show arwen at center_f
    with dissolve
    ARWEN @talk "Would you like me to keep my dress on, or take it off?"
    menu:
        "Leave it on":
            pass
        "Off it goes!":
            $ CharSetClothes("arwen", "naked")
    ARWEN @talk "As you wish."
    if DialogueArwen().firstSex:
        "Arwen gasped as I was removing my clothes."
        ARWEN @scared 'Gods!'
        ARWEN @blush "You're... very {i}blessed{/i} aren't you?"
        ARWEN @laugh 'Were the local girls even able to walk afterwards?'
        $ DialogueArwen().firstSex = False
    else:
        ARWEN @blush "Ahh... It's even bigger than I remember."
        MC @smile "Worried you won't be able to handle it?"
        'Arwen smiled mischeviously.'
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    ARWEN @blush '...Get over here and fuck me.'
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
    if CharGetClothes("arwen") == "normal":
        scene arwen_doggy_dress_vag with dissolve
    if CharGetClothes("arwen") == "naked":
        scene arwen_doggy_naked_vag with dissolve
    $ Pause()
    'On her hands and knees, it did not Arwen long to get going.'
    ARWEN 'Harder! Pull my hair harder while you fuck me!'
    ARWEN "Mhmmff! F-Fuck! You're so fucking big!"
    'Sweat dripped off the two of us as Arwen continued to throw and bash her round soft ass against my cock filling her up.'
    'Arwen moaned loudly as her tight body squeezed me effortlessly, writhing as she laughed between her grunts of pleasure and pain interwoven.'
    MC 'Arwen, {i}*Huff*{/i} Are you-'
    ARWEN "Don't even think of - Hrgh! Stopping!"
    ARWEN 'Keep slamming that big cock into me!'
    MC 'As you wish whore!'
    ARWEN 'Ah! Ah! AH! Yes!'
    ARWEN 'Harder! Pull me onto you just like that! Mmmfgh!'
    ARWEN 'Make me your little whore!'
    ARWEN "Mmm! {i}*Huff*{/i} It's the best right?"
    MC 'What?'
    ARWEN 'Tell me why cunt is the best - Argh! Damn it!'
    if CharGetClothes("arwen") == "normal":
        scene arwen_doggy_dress_vag_alt with dissolve
    if CharGetClothes("arwen") == "naked":
        scene arwen_doggy_naked_vag_alt with dissolve
    $ Pause()
    MC 'Ahh! Your cunt feels good slut!'
    ARWEN 'A perfect little cunt for a perfect little whore? Ahh!'
    MC "Arwen {i}*Huff*{/i} I'm close to finishing!"
    ARWEN "Cum in me! Fucking fill me up!"
    MC 'Hrghh! A-Arwen!'
    ARWEN "You're not fucking leaving here till your balls are fucking empty!"
    'Unable to hold back any longer, the intense pleasure like fire scourching through my veins drove me wild as the Parasite seemed to almost pulse inside of me.'
    'Pulling Arwen as deeply as I could onto me, I held her there as I gritted my teeth and dug my hands into the soft flesh of her ass.'
    MC 'ARWEN!'
    ARWEN 'AHH! YES!'
    'Unable to hold back any longer, I began to pour my load into Arwen, whose lip bitting whimper of pleasure became a loud, hot moan as she became overwhelmed.'
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    if CharGetClothes("arwen") == "normal":
        scene arwen_doggy_dress_vag_finish with dissolve
        $ UnlockGalFlag("arwen","doggy","var_dress_vag")
    if CharGetClothes("arwen") == "naked":
        scene arwen_doggy_naked_vag_finish with dissolve
        $ UnlockGalFlag("arwen","doggy","var_naked_vag")
    $ Pause()
    $ ReduceInfectionFromSex("arwen")
    $ UnlockGalSceneAndGrantXp("arwen","doggy")
    ARWEN 'Oooh! Y-Yes...'
    ARWEN 'Fill me... Fill me up.'
    'Arwen began to tremble beneath my hands, drenched in sweat as she breathed heavily tryig to recompose herself.'
    ARWEN 'Gods...{i}There was so much of it.{/i}'
    ARWEN "Ahh, help me back onto my feet."
    scene black with dissolve
    $ CharSetClothes("arwen", "normal")
    'I helped Arwen back to her feet as her legs still shook beneath her.'
    'Arwen laughed, brushing back her messed up hair as she sensually run her hand down my chest.'
    $ AutoMus(True)
    scene bg_weeping_heart_brothel_room
    show arwen at center_f
    with dissolve
    ARWEN @blush 'I think you might be my new favourite client after that...'
    MC @smile 'How about a discount?'
    ARWEN @laugh 'Haha!'
    ARWEN @laugh 'Nice try...'
    jump dialogue_arwen_postSex
