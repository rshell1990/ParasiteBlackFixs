label sexscene_arwen_mouth:
    ARWEN @laugh 'Oh, tired of hearing me talk huh?'
    ARWEN @blush 'Rather see me put my mouth to... {i}other uses?{/i}'
    ARWEN @blush '{i}*giggles*{/i} right this way...'
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
    if DialogueArwen().firstBJ:
        "Arwen gasped as I was removing my clothes."
        ARWEN @scared 'Gods!'
        ARWEN @blush 'Well, {i}do you come from a family of centaurs by any chance?{/i}'
        MC @smile 'Fully human.'
        BLACK '{i}(I find this assessment dubious at best).{/i}'
        $ DialogueArwen().firstBJ = False
    'Arwen smiled mischeviously.'
    ARWEN @laugh "Well, aren't I a lucky girl?"
    ARWEN @blush "Come on, let's not keep you waiting any longer!"
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Arwen dropped to her knees and inches closer towards my hardened member, her cheeks flushed red as she smiled staring at it.'
    'Brushing her hair back over head, Arwen leaned in, pressing a soft, warm kiss on the head that made me shudder before her mouth wrapped over it.'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    if CharGetClothes("arwen") == "normal":
        scene arwen_bj_dress with dissolve
    if CharGetClothes("arwen") == "naked":
        scene arwen_bj_naked with dissolve
    $ Pause()
    ARWEN '{i}*Slurp*{/i} Mmhmm...!'
    "As Arwen's head moved back and forth, her wet lips gliding across my member smoothly as her tongue thrashed and beat against my meat, my whole body shuddered in pleasure."
    "Arwen might have boasted a lot, {i}but she knew how to back it up.{/i}"
    MC "Ahh! {i}*Huff*{/i} You're good at this!"
    ARWEN "Mhmmhmm! Imhmbhestt! {i}*Slurp!*{/i}"
    'Arwen wiggled her round butt back and forth slightly as she continued to throw her head down onto my cock, lewd wet sounds escaping her lips as she greedily took me as deeply as she could.'
    "Every so often, I'd hear the sound of her choking from having tried to take it too deep, but Arwen would push herself on anyway, taking me as deeply as she could."
    'My body began to burn up, the Parasite inside of me thrashing around as the pleasure overtook us, I groaned, fighting back every urge to just leap onto Arwen now and mount her like a wild animal.'
    ARWEN 'Glrghh! Mhhfff!'
    ARWEN '{i}*Slurp!* *Slurp!*{/i}'
    MC "Ah! That feels incredible!"
    if CharGetClothes("arwen") == "normal":
        scene arwen_bj_dress_alt with dissolve
    if CharGetClothes("arwen") == "naked":
        scene arwen_bj_naked_alt with dissolve
    $ Pause()
    'For some time, Arwen continued driving her head back and forth onto my sensitive cock, the wonderful sensation washing over me began to push me closer towards the edge.'
    MC "Arhhh! A-Arwen... {i}*Huff*{/i} I don't think I can last much longer!"
    "Incentivised, Arwen's lips curved into a smile as she giggle, her green eyes looking up to mine as she threw herself forward once again, determined to drain me dry."
    MC "GRGHH! I'm c-close!"
    MC "Arwen, I- {i}*Huff*{/i} I'm going to-"
    'Unable to hold back any longer, I felt the pleasure quickly override me like a tidal wave crashing down.'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if CharGetClothes("arwen") == "normal":
        scene arwen_bj_dress_finish with dissolve
        $ UnlockGalFlag("arwen","bj","var_dress")
    if CharGetClothes("arwen") == "naked":
        scene arwen_bj_naked_finish with dissolve
        $ UnlockGalFlag("arwen","bj","var_naked")
    $ Pause()
    $ ReduceInfectionFromSex("arwen")
    "As I pulled Arwen's head down as deeply as I could onto my cock, Arwen's eyes widened in surprise as she let out a little whelp like sound."
    "I grunted loudly as the hot seed poured into her mouth, and Arwen obediently began to swallow as much as she could of the massive load."
    "Finally, fully spent, Arwen pulled her lips away from my cock, cheeks puffed out still till she swallowed down the last of my seed, opening her mouth to show me she had done so."
    ARWEN '{i}*Huff* *Huff...*{/i}'
    ARWEN 'You taste {i}*Huff*{/i} So good!'
    MC 'Good girl...'
    $ UnlockGalSceneAndGrantXp("arwen","bj")
    scene black with dissolve
    $ Pause(0.5)
    $ CharSetClothes("arwen", "normal")
    scene bg_weeping_heart_brothel_room
    show arwen at center_f
    with dissolve
    $ AutoMus(True)
    jump dialogue_arwen_postSex
