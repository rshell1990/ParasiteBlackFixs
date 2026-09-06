label gallery_winward_doggy_door:
    $ tmpvar = {}

    $ tmpvar["preg"] = False

########
    if GalFlag("mrs_winward", "doggy_door", ["dress", "cow"]):
        "Was she wearing her cow outfit?"
        menu:
            "Yes":
                $ tmpvar["cow"] = True
            "No":
                $ tmpvar["cow"] = False

    elif GalFlag("mrs_winward", "doggy_door", "dress"):
        $ tmpvar["cow"] = False
    elif GalFlag("mrs_winward", "doggy_door", "cow"):
        $ tmpvar["cow"] = True

########
    if GalFlag("mrs_winward", "doggy_door", ["vag", "anal"]):
        "Was the encounter anal or vaginal?"
        menu:
            "Vaginal":
                $ tmpvar["anal"] = False
            "Anal":
                $ tmpvar["anal"] = True
    elif GalFlag("mrs_winward", "doggy_door", "vag"):
        $ tmpvar["anal"] = False
    elif GalFlag("mrs_winward", "doggy_door", "anal"):
        $ tmpvar["anal"] = True
########
    if tmpvar["anal"] == True:
        jump gallery_winward_doggy_door_anal
    else:
        jump gallery_winward_doggy_door_vag

label gallery_winward_doggy_door_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)

    if tmpvar["cow"]:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_cow_nopreg_vag_slow with dissolve
        else:
            scene mrs_winward_doggydoor_cow_nopreg_vag_slow with dissolve
    else:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_dress_nopreg_vag_slow with dissolve
        else:
            scene mrs_winward_doggydoor_dress_nopreg_vag_slow with dissolve
    $ Pause()

    "As the head of my cock pushed through into her slit, she let out a little gasp as I began to slowly push my cock deeper into her."
    "Her dryness didn't last long, already, as she pressed her face against the door frame, I could feel her become more and more excited by each passing moment."
    MC "{i}Keep the idiot! Ahh! Talking!{/i}"
    MRS_WINWARD "M-Mhfhghh!"
    MRS_WINWARD "{i}Y-You're so - Ahh! Terrible!{/i}"
    MR_WINWARD "What's going on in there?!"
    MRS_WINWARD "Ahh! N-Nothing dear!"
    "With both hands squeezing her round ass, feeling the fat press it's way in between my fingers, I began to thrust steadily."
    MRS_WINWARD "O-Oooh! J-Just {i}v-very{/i} busy right now!"
    MR_WINWARD "You should open thishhh door right nowhhh!"
    MR_WINWARD "Youhhh nheedhh meee!"
    "Mrs Winward let out another involuntary moan as she felt the length of my cock push in and out of her tight, wet, hole."
    "The old man's venomous vitriol which used to sting so much, was now but a whisper as she grunted with pleasure."
    MRS_WINWARD "Mhhhhhurghhh... {image=[ICON.HEART]}"
    MRS_WINWARD "D-Dear - {i}*Huff*{/i} S-Stop talking and - Mhmm! G-Go home!"
    MRS_WINWARD "You're drunk and I - Mhhfhh! I'm t-too busy for this!"
    "The sounds of flesh slapping together grew louder and more frequent as I fucked Mrs Winward faster from behind."
    "The fat of her ass jiggled with every thrust as her old pussy clung and squeezed me desperately."
    "Her glasses began to steam up as the sweat began to pour down from her, her glasses steaming up."

    if tmpvar["cow"]:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_cow_nopreg_vag_fast with dissolve
        else:
            scene mrs_winward_doggydoor_cow_nopreg_vag_fast with dissolve
    else:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_dress_nopreg_vag_fast with dissolve
        else:
            scene mrs_winward_doggydoor_dress_nopreg_vag_fast with dissolve
    $ Pause()

    MRS_WINWARD "Ahhhh!"
    MRS_WINWARD "O-Ooooh!"
    MRS_WINWARD "{i}*Whispering* S-Slow down dear! He'll - Mhhfhh! H-Hear us if you keep going like that!{/i}"
    "I ignored her pleas, let the old bastard hear and wonder what his precious little wife was up to behind that door!"
    MR_WINWARD "W-What's going on in there?"
    MR_WINWARD "IS SOMEONE WITH YOU?!"
    "Mrs Winward grunted and moaned louder, this time the old man {i}definitely{/i} had heard her!"
    MRS_WINWARD "Ooooh! M-More! Don't stop!"
    "As her legs began to buckle, her body convulsed and tightened in spasms as I felt her body reaching an orgasm."
    "The other side of the door, the old man furiously tried at the lock to try and get in."
    MR_WINWARD "O-OPEN THIS DOOR AT ONCE!!"
    MR_WINWARD "WHOSE IN THERE WITH YOU?!"
    MRS_WINWARD "Urghhhh! S-Shut up you miserable old - Mhfhghh! B-BASTARD!"
    MR_WINWARD "W-Who the hell do you think you're-"
    MRS_WINWARD "Mfghh! L-Leave me alone! Can't you hear I'm- Ahh! B-Busy in here?!"
    MRS_WINWARD "O-Ooooooooooooh!"
    MRS_WINWARD "{i}*Whispering*{/i} D-Don't stop! F-Fuck me harder! P-Please! Mhhfhh!!"
    MR_WINWARD "Let me in dear!"
    MR_WINWARD "LET ME IN RIGHT NOW!!"
    "Mrs Winward's huge tits swayed back and forth as I continued to slam my cock into her."
    "As Mr Winward desperately tried to get in, I felt Mrs Winward's body tremble even more as she pleaded pitifully."
    MRS_WINWARD "{i}C-Cum in me...P-Please cum in me!{/i}"
    MRS_WINWARD "I need it so much!!"
    MR_WINWARD "What?! What did you just say?!"
    MRS_WINWARD "A-AHHHHHHHHHHHHHHHH!! {image=[ICON.HEART]}"
    "Mrs Winward's eyes rolled back as her own climax washed over her, from the other side of the door, Mr Winward furiously continued to bash against the door."
    "As he screamed his frustrations, his voice began to break pitifully... Was he crying?"
    MR_WINWARD "D-Dear... Please... Open the door PLEASE!"
    "Mrs Winward, tilted her head briefly back to look towards me, flushed red and exhausted."
    MRS_WINWARD "{i}...Cum in me.{/i}"
    "There was a coldness to Mrs Winward's eyes, an indifference to the old man's cries outside."
    "Giving her what she wanted, I continued to slam into her from behind until I began to feel my cock throb in desperation."
    "My balls raised up as the intensity grew and grew, bubbling over until finally..."
    MC "C-CUMMING!!"

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    
    if tmpvar["cow"]:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_cow_nopreg_vag_finish with dissolve
        else:
            scene mrs_winward_doggydoor_cow_nopreg_vag_finish with dissolve
    else:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_dress_nopreg_vag_finish with dissolve
        else:
            scene mrs_winward_doggydoor_dress_nopreg_vag_finish with dissolve
    $ Pause()

    "I grunted loudly through gnashed teeth as I slammed my cock to the hilt inside of her, mashing up her insides as I poured my hot load into her welcoming hole."
    "Her eyes widened once more as her mouth hung agape, choking on air before a guttural grunt of pleasure escaped her lips."
    MRS_WINWARD "Mmmmmfghhhhhhhhhhh!! {image=[ICON.HEART]}"
    MRS_WINWARD "{i}*Huff* *Huff*{/i} By the gods..."
    return

label gallery_winward_doggy_door_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)

    if tmpvar["cow"]:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_cow_nopreg_anal_slow with dissolve
        else:
            scene mrs_winward_doggydoor_cow_nopreg_anal_slow with dissolve
    else:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_dress_nopreg_anal_slow with dissolve
        else:
            scene mrs_winward_doggydoor_dress_nopreg_anal_slow with dissolve
    $ Pause()

    "As the head of my cock prodded against her tight rosebud, she let out a little panicked gasp, briefly glancing back at me with wide-eyed nervousness."
    MRS_WINWARD "{i}*Whispering*{/i} T-That's my-"
    MRS_WINWARD "{i}*Whispering*{/i} H-He'll hear us!"
    "Pushing gently against her dry asshole, I quickly felt the resistance from her body,"
    "Yet, I felt something stir within me as my cock lightly secreted through the skin some kind of...lubricant?"
    "With the next prod, she whimpered, but her tight forbidden passage gave way thanks to the lubricant." 
    MRS_WINWARD "M-MHMMMM!"
    MRS_WINWARD "{i}*Whispering*{/i} M-My ass...My ass!"
    "She pressed her face against the door frame, mouth hung agape as as I ever so slowly sunk my cock deeper into her hole."
    "All the while, her idiot husband continued to bang on the door as I filled his abandoned's wife's bowels with my cock."
    MR_WINWARD "Why aren'thh yhouu thalkin' no mhoreee??"
    "Slowly, as I gently fucked Mrs Winward's ass, her nervousness stiffness slowly began to pass as she felt the huge member slide in and out of her ass."
    MRS_WINWARD "A-Ah-h-h!"
    "I could feel her become more and more excited by each passing moment."
    MC "{i}Keep the idiot! Ahh! Talking!{/i}"
    MRS_WINWARD "M-Mhfhghh!"
    MRS_WINWARD "{i}Y-You're so - Ahh! Terrible!{/i}"
    MRS_WINWARD "{i}F-Fucking my ass and expecting me to hold a conversation!{/i}"
    MR_WINWARD "What's going on in there?!"
    MRS_WINWARD "Ahh! N-Nothing dear!"
    "With both hands squeezing her round ass, feeling the fat press it's way in between my fingers, I began to thrust steadily."
    MRS_WINWARD "O-Oooh! J-Just {i}v-very{/i} busy right now!"
    MR_WINWARD "You should open thishhh door right nowhhh!"
    MR_WINWARD "Youhhh nheedhh meee!"
    "Mrs Winward let out another involuntary moan as she felt the length of my cock push in and out of her now, stretched out asshole."
    "The old man's venomous vitriol which used to sting so much, was now but a whisper as she grunted with pleasure."
    MRS_WINWARD "Mhhhhhurghhh... {image=[ICON.HEART]}"
    MRS_WINWARD "D-Dear - {i}*Huff*{/i} S-Stop talking and - Mhmm! G-Go home!"
    MRS_WINWARD "You're drunk and I - Mhhfhh! I'm t-too busy for this!"
    "The sounds of flesh slapping together grew louder and more frequent as I fucked Mrs Winward faster from behind."
    "The fat of her ass jiggled with every thrust as the tight ring of her asshole clung and squeezed at me desperately."
    "Her tight asshole having molded itself to fit and squeeze around my cock perfectly."
    "Her glasses began to steam up as the sweat began to pour down from her, her glasses steaming up."

    if tmpvar["cow"]:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_cow_nopreg_anal_fast with dissolve
        else:
            scene mrs_winward_doggydoor_cow_nopreg_anal_fast with dissolve
    else:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_dress_nopreg_anal_fast with dissolve
        else:
            scene mrs_winward_doggydoor_dress_nopreg_anal_fast with dissolve
    $ Pause()

    MRS_WINWARD "Ahhhh!"
    MRS_WINWARD "O-Ooooh!"
    MRS_WINWARD "{i}*Whispering* S-Slow down dear! He'll - Mhhfhh! H-Hear us if you keep going like that!{/i}"
    "I ignored her pleas, let the old bastard hear and wonder what his precious little wife was up to behind that door!"
    MR_WINWARD "W-What's going on in there?"
    MR_WINWARD "IS SOMEONE WITH YOU?!"
    "Mrs Winward grunted and moaned louder, this time the old man {i}definitely{/i} had heard her!"
    MRS_WINWARD "Ooooh! M-More! Don't stop!"
    "As her legs began to buckle, her body convulsed and tightened in spasms as I felt her body reaching an orgasm."
    "The other side of the door, the old man furiously tried at the lock to try and get in."
    MR_WINWARD "O-OPEN THIS DOOR AT ONCE!!"
    MR_WINWARD "WHOSE IN THERE WITH YOU?!"
    MRS_WINWARD "Urghhhh! S-Shut up you miserable old - Mhfhghh! B-BASTARD!"
    MR_WINWARD "W-Who the hell do you think you're-"
    MRS_WINWARD "Mfghh! L-Leave me alone! Can't you hear I'm- Ahh! B-Busy in here?!"
    MRS_WINWARD "O-Ooooooooooooh!"
    MRS_WINWARD "{i}*Whispering*{/i} D-Don't stop! F-Fuck me harder! P-Please! Mhhfhh!!"
    MR_WINWARD "Let me in dear!"
    MR_WINWARD "LET ME IN RIGHT NOW!!"
    "Mrs Winward's huge tits swayed back and forth as I continued to slam my cock into her."
    "As Mr Winward desperately tried to get in, I felt Mrs Winward's body tremble even more as she pleaded pitifully."
    MRS_WINWARD "{i}C-Cum in me...P-Please cum in me!{/i}"
    MRS_WINWARD "{i}Fill this old ass up!{/i}"
    MRS_WINWARD "I need it so much!!"
    MR_WINWARD "What?! What did you just say?!"
    MRS_WINWARD "A-AHHHHHHHHHHHHHHHH!! {image=[ICON.HEART]}"
    "Mrs Winward's eyes rolled back as her own climax washed over her, from the other side of the door, Mr Winward furiously continued to bash against the door."
    "As he screamed his frustrations, his voice began to break pitifully... Was he crying?"
    MR_WINWARD "D-Dear... Please... Open the door PLEASE!"
    "Mrs Winward, tilted her head briefly back to look towards me, flushed red and exhausted."
    MRS_WINWARD "{i}...Cum in me.{/i}"
    MRS_WINWARD "Cum in my ass like a common whore!! {image=[ICON.HEART]}{image=[ICON.HEART]} "
    "There was a coldness to Mrs Winward's eyes, an indifference to the old man's cries outside."
    "Giving her what she wanted, I continued to slam into her from behind until I began to feel my cock throb in desperation."
    "My balls raised up as the intensity grew and grew, bubbling over until finally..."
    MC "C-CUMMING!!"

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")

    if tmpvar["cow"]:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_cow_nopreg_anal_finish with dissolve
        else:
            scene mrs_winward_doggydoor_cow_nopreg_anal_finish with dissolve
    else:
        if tmpvar["preg"]:
            scene mrs_winward_doggydoor_dress_nopreg_anal_finish with dissolve
        else:
            scene mrs_winward_doggydoor_dress_nopreg_anal_finish with dissolve
    $ Pause()

    "I grunted loudly through gnashed teeth as I slammed my cock to the hilt inside of her, mashing up her insides as I poured my hot load into her bowels."
    "Her eyes widened once more as her mouth hung agape, choking on air before a guttural grunt of pleasure escaped her lips."
    MRS_WINWARD "Mmmmmfghhhhhhhhhhh!! {image=[ICON.HEART]}"
    MRS_WINWARD "{i}*Huff* *Huff*{/i} By the gods..."
    return