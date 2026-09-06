label sexscene_arwen_backdoor:
    ARWEN 'Oh, I bet you would!'
    ARWEN "Now I definitely know what you're looking at when I'm walking away!"
    ARWEN @laugh '{i}*giggles*{/i} Come With me...'
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
    if DialogueArwen().firstAnal:
        "Arwen gasped as I was removing my clothes."
        ARWEN @scared "Gods... I know I'm brave but-"
        ARWEN @blush "You... You expect me to fit {i}all{/i} that in my ass?"
        ARWEN @scared "I won't be able to walk straight for a week!"
        $ DialogueArwen().firstAnal = False
    else:
        ARWEN @blush "Gods, last time was so... {i}intense,{/i} I'm a little nervous about letting you back {i}there{/i} again."
        MC @smile "And here I thought you were the best fuck in Novaras."
        'Arwen smiled mischeviously.'
        ARWEN @blush "Oh, that's how it is huh?"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    ARWEN @blush 'Get over here...'
    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg",1)
    if CharGetClothes("arwen") == "normal":
        scene arwen_doggy_dress_anal with dissolve
    if CharGetClothes("arwen") == "naked":
        scene arwen_doggy_naked_anal with dissolve
    $ Pause()
    'On her hands and knees, it did not take Arwen long to get going.'
    ARWEN 'F-Fuck my ass! Oh gods! {i}*Huff*{/i}'
    ARWEN 'GRGHHH! Pull my hair harder while you f-fuck me!'
    "The ring of Arwen's tight asshole squeezed tightly around my cock as she whimpered and moaned, doing her best to push herself back onto me but it was clear she was struggling."
    "Arwen's hands coiled into fists as she trembled, bitting down hard onto her lower lip as her eyes began to water up from the intense session."
    ARWEN "GHHH! You're so f-fucking big!"
    ARWEN 'Ah! My fucking - Ah! Ass!'
    'Sweat dripped off of Arwen as she struggled between juggling between pleasure and pain, the sensations from her tight body driving me wild into a frenzy.'
    ARWEN 'You - Ah! You like that?'
    MC 'Arwen, {i}*Huff*{/i} Do you-'
    ARWEN "K-Keep going!"
    ARWEN "Just tell me how much tighter my ass is than the others!"
    MC 'Grghh!'
    MC "Your ass is the tightest I've ever fucked you little whore!"
    ARWEN 'Ah! Ah! AH! Yes!'
    ARWEN 'Hurt me! Hurt me while you fuck me!'
    'Despite whatever shock of pain she was initially feeling, Arwen seemed to increasingly aroused as we progressed.'
    'The pulsing darkness inside of me struggled to restrain myself, to consider her well-being, driven by hot-bloodedness, her body felt too good.'
    ARWEN 'Harder! Shove that cock deeper into my ass! Mmmfgh!'
    ARWEN 'Make me your little whore!'
    MC 'A-Arwen! {i}*Huff*{/i}'
    if CharGetClothes("arwen") == "normal":
        scene arwen_doggy_dress_anal_alt with dissolve
    if CharGetClothes("arwen") == "naked":
        scene arwen_doggy_naked_anal_alt with dissolve
    $ Pause()
    ARWEN 'A perfect little ass for a perfect little whore, r-right? Ahh!'
    MC "Arwen {i}*Huff*{/i} I'm close to finishing!"
    ARWEN "Mhmm! That's it! Finish in me!"
    ARWEN 'Finish in my ass!'
    MC 'Hrghh! A-Arwen!'
    ARWEN "Empty your fucking balls in my ass!"
    'Unable to hold back any longer, the intense pleasure like fire scourching through my veins drove me wild as the Parasite seemed to almost pulse inside of me.'
    'Pulling Arwen as deeply as I could onto me, I held her there as I gritted my teeth and dug my hands into the soft flesh of her ass.'
    MC 'ARWEN!'
    ARWEN 'AHH! YES!'
    "Unable to hold back any longer, I began to pour my load into Arwen's tight ass."
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    if CharGetClothes("arwen") == "normal":
        scene arwen_doggy_dress_anal_finish with dissolve
        $ UnlockGalFlag("arwen","doggy","var_dress_anal")
    if CharGetClothes("arwen") == "naked":
        scene arwen_doggy_naked_anal_finish with dissolve
        $ UnlockGalFlag("arwen","doggy","var_naked_anal")
    $ Pause()
    $ ReduceInfectionFromSex("arwen")
    $ UnlockGalSceneAndGrantXp("arwen","doggy")
    'Arwen, whose lip bitting whimper of pleasure became a loud, hot moan as she became overwhelmed, trembled as she felt my hot seed flood her stretched backdoor.'
    ARWEN 'Oooooooh...!'
    ARWEN '{i}M-my poor ass...{/i}'
    ARWEN 'Fill me... Fill me up.'
    'Arwen began to tremble beneath my hands, drenched in sweat as she breathed heavily trying to recompose herself.'
    ARWEN 'Gods... {i}There was so much of it.{/i}'
    ARWEN "Ahh, help me back onto my feet."
    scene black with dissolve
    $ CharSetClothes("arwen", "normal")
    'I helped Arwen back to her feet as her legs still shook beneath her.'
    'Arwen laughed, brushing back her messed up hair as she sensually run her hand down my chest.'
    $ AutoMus(True)
    scene bg_weeping_heart_brothel_room
    show arwen at center_f
    with dissolve
    ARWEN @blush "I don't think anyone's ever fucked me quite like that!"
    MC @smile 'In a good kind of way, I hope?'
    ARWEN @laugh 'Mmm, yes...'
    ARWEN @blush '{i}Painful... But very good.{/i}'
    $ LocNameReset()
    jump dialogue_arwen_postSex
