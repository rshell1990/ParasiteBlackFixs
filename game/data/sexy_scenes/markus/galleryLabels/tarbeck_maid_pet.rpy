label gallery_markus_fem_tarbeck_maid_pet:
    $ PlayMusicRandom("mus_sex")
    $ tmpvar["stored_mc_clothes"] =    CharGetClothes("mc")
    $ tmpvar["stored_markus_clothes"] = CharGetClothes("markus")
    $ CharSetClothes("mc", "suit")
    $ CharSetClothes("markus", "maid")
    scene cg_tarbeck_master_maid_room_party
    show mc at cleft
    show markus_fem at cright_f
    with dissolve

    play sound "audio/cfx/finger_snap.ogg"
    MARKUS_FEM @angry "This is so fucking degrading."
    MC @talk "Mark- I mean, {i}Marcia.{/i}"
    MC @serious "Remember why we're here. If we don't do this, your brother—"
    show markus_fem at shake
    MARKUS_FEM @angry "I know, I know, I KNOW!"
    MARKUS_FEM @sad "{i}*Sigh*{/i}"
    window hide
    hide markus_fem
    hide mc
    show cg_markus_fem_maid_leash at center
    with dissolve
    $ Pause()
    "Marcia lowered herself to the floor on her hands and knees."
    MARKUS_FEM @sad "O-Okay master, uhh... Let's go or something..."
    MC @smile "Convincing stuff."
    MARKUS_FEM @angry "Shut the fuck up."
    "As I wandered around, Marcia crawled obediently beside me."
    "For half an hour, I wandered almost aimlessly around the lobby as Marcia followed."
    "Another couple was doing the same, except this one's wife seemed fully converted, a fake dog tail plugged into her ass as she beckoned us over."
    PARTY_GUEST "What a lovely pet you have."
    MC "Thank you."
    "I looked down at Marcia, gently petting her head as she pouted irritably."
    MC "{i}I'm still training this one.{/i}"
    "Marcia winced, barely restraining herself from a witty comeback."
    GUESTS_PET "{i}Woof!{/i}"
    "The woman panted, wagging her tail as she looked at Marcia longingly."
    PARTY_GUEST "... Would you like to let our pets play for a while?"
    MC @smile "Why not?"
    MC @smile "Go ahead, Marcia, have some fun."
    GUESTS_PET "{i}*Woof!*{/i}"
    "The guest's wife crawled over, wagging her tail as she sniffed, then licked at Marcia's neck."
    MARKUS_FEM "U-Uhh, good girl?"
    GUESTS_PET "{i}*Woof!*{/i}"
    "The woman leapt onto Marcia, cupping her breasts as she kissed, licked, and nipped at her neck."
    MARKUS_FEM "W-Whoa! Hold on a minute!"
    MARKUS_FEM "What are you—"
    MARKUS_FEM "Mmmfghh...!"
    MARKUS_FEM "{i}*Huff*{/i} Oh... You wanna play, huh?"
    GUESTS_PET "Arffff?"
    scene black with dissolve
    play sound "audio/cfx/body_falling.ogg"
    "Marcia surged forward, wrestling the squirming wife into submission as she yelped."
    GUESTS_PET "Mmmfghh??!"
    MARKUS_FEM "Stop squirming."
    MARKUS_FEM "It's {i}my{/i} turn."
    $ PlaySexFx("audio/sex_sounds/ves69_100.ogg", 1)
    scene markus_fem_tarbeck_maid_pet_loop_1 with dissolve
    $ Pause()
    "With fingers pressed into the wife's mouth, Marcia muffled her moans as her other hand worked between the woman's legs."
    GUESTS_PET "M-Mmfghhh!!"
    MARKUS_FEM "See?"
    MARKUS_FEM "Isn't this better?"
    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
    scene markus_fem_tarbeck_maid_pet_loop_2 with dissolve
    $ Pause()
    "As Marcia drove her fingers deeper, the woman's eyes rolled back while her husband watched, amused and uneasy."
    PARTY_GUEST "Your pet is quite... aggressive."
    MC "O-Oh yes!"
    MC "Uhh, still in training."
    MARKUS_FEM "You like that, huh?"
    GUESTS_PET "Mmmfffhh!"
    MARKUS_FEM "Don't worry."
    MARKUS_FEM "You're in good hands."
    MARKUS_FEM "{i}Slut.{/i}"
    "The wife trembled, her breath ragged as Marcia worked her relentlessly."
    PARTY_GUEST "..."
    MC "Uhh, lots of work left to do."
    GUESTS_PET "Mmmmmfghh!"
    "Her cries grew louder until—"
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    scene markus_fem_tarbeck_maid_pet_finish with flash
    $ Pause()
    GUESTS_PET "MMMFFFFHHHH!!"
    MARKUS_FEM "Haha, now that's a sound I could get used to!"
    "Satisfied, Marcia withdrew her fingers, licking them casually as the wife whimpered back to her husband."
    PARTY_GUEST "Darling! Are you alright?"
    GUESTS_PET "{i}*Huff*{/i} A-Arff..."
    MC @surprised "I-I'm sorry!"
    MC @talk "My pet still gets a little excited!"
    PARTY_GUEST "... Come along dear. Let's find nicer playmates."
    "He tugged her lead and left, casting me a displeased look."
    MC @serious "Urghhh..."
    $ CharSetClothes("mc",      tmpvar["stored_mc_clothes"])
    $ CharSetClothes("markus",  tmpvar["stored_markus_clothes"])
    return