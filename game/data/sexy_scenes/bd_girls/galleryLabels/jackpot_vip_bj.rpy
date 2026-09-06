label gallery_jackpot_vip_bj:
    $ PlayMusicRandom("mus_sex")
    if GalFlagCount("bd_girls", "jackpot_vip") == 2:
        "Was she..."
        menu:
            "Wearing her dress?":
                $ tmpvar = "clothed"
            "Naked?":
                $ tmpvar = "nude"
    else:
        if GalFlag("bd_girls", "jackpot_vip", "var_dress"):
            $ tmpvar = "clothed"
        if GalFlag("bd_girls", "jackpot_vip", "var_naked"):
            $ tmpvar = "nude"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)

    if tmpvar == "clothed":
        scene bd_girls_jackpot_vip_bj_dress_slow with dissolve
    if tmpvar == "nude":
        scene bd_girls_jackpot_vip_bj_naked_slow with dissolve
    $ Pause()

    BLACK_DIAMOND_SERVICE_GIRL "{i}*Slurp!* *Slurp!*{/i}"
    BLACK_DIAMOND_SERVICE_GIRL "Mhmmmfghh! Shuchhaabhigg mhmmmff!"
    "I let out a sigh as the girl worked her {i}talents{/i} excellently on me."
    "Time seemed to drift by as the girls' tongue and wet mouth glided up and down my cock."
    "I sunk back into the soft furniture, a free bottle drunk between us as the time began to drift on by."
    MC "Mhhfhh..."

    if tmpvar == "clothed":
        scene bd_girls_jackpot_vip_bj_dress_fast with dissolve
    if tmpvar == "nude":
        scene bd_girls_jackpot_vip_bj_naked_fast with dissolve
    $ Pause()

    "I groaned in pleasure as the girl sunk my cock deeper down into her throat, wiggling her round ass enticingly as she did so."
    "The girls' tongue flickered and and beat around my cock occasionally as she let out hot whimpers and muffled words of appreciation."
    BLACK_DIAMOND_SERVICE_GIRL "{i}Mhhfh! *Shlick!*{/i} Shuchahhh - Mhhfhh! Ghooodhh chockhh! {i}*Slurp!*{/i}"
    "Eventually, our brief time of play was at an end."
    "As I felt my balls tighten and rise from her expert teasing, I grunted through gritted teeth to warn her of my impending finish."
    MC "Ahhh...! I'm gonna-"
    BLACK_DIAMOND_SERVICE_GIRL "{i}*Slurp!*{/i} Mhmmfhh! Jhusthh fhinishhh whennhh rheadhyy! {i}*Slurp!*{/i} Mhmmff!"
    "Soon, as her tongue flickered over the head of my cock before gliding down to deep throat my member, she held it there and waited expectently."
    "After her long, continuous teasing, I finally felt overwhelmed with her mouth, and grabbing the back of her head, held at her soft hair as I poured my thick load down her throat."
    MC "H-HRGHHHHH!!"

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")

    if tmpvar == "clothed":
        scene bd_girls_jackpot_vip_bj_dress_finish with flash
    if tmpvar == "nude":
        scene bd_girls_jackpot_vip_bj_naked_finish with flash
    $ Pause()

    BLACK_DIAMOND_SERVICE_GIRL "{i}*Gulp!*{/i} Mhmmff! {i}*Slurp!*{/i}"
    "As the rush of seed flooded down her throat, I noticed her legs trembling slightly as some sweet, glistening juices dripped down between her legs onto the floor."
    "{i}Had she just finished from sucking my cock alone?{/i}"
    "The girl eagerly swallowed and licked up every last hint of my seed, making sure not to waste a drop."
    "Satisfied my member had been cleaned, she pulled back, wipping her mouth clean with a cloth delicately."
    BLACK_DIAMOND_SERVICE_GIRL "Thank you for zer meal, sir, fufu {image=[ICON.HEART]}"
    scene black with dissolve
    return