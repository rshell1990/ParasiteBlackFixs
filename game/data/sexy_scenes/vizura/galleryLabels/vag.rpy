label gallery_vizura_vag:
    scene black with dissolve
    if GalFlag("vizura", "vag", ["var_preg", "var_nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False
    elif GalFlag("vizura", "vag", "var_preg"):
        $ tmpvar["preg"] = True
    elif GalFlag("vizura", "vag", "var_nopreg"):
        $ tmpvar["preg"] = False
    
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if tmpvar["preg"]:
        scene ss_vizura_standing_alter_preg_idle
    else:
        scene ss_vizura_standing_alter_normal_idle
    with dissolve
    $ Pause()
    "Lifting Vizura off the ground, she giggled as I aligned my cock against her wet, tight womanhood."
    if tmpvar["preg"]:
        "I paused for a moment, looking down at the round hanging belly."
        VIZURA "Don't worry about the baby, handsome, us goblins are sturdy!"
        VIZURA "Besides! Feels nice not to actually have to feel that extra weight for a little while! Hehe!"
        "Reassured, I nodded and smiled at her words."
    if tmpvar["preg"]:
        scene ss_vizura_standing_normal_preg_idle
    else:
        scene ss_vizura_standing_normal_normal_idle
    with dissolve
    $ Pause()
    "With ease, I pressed the head of my cock against her hole, she let out a hot sigh as I pressed my cock in deeper and deeper into her and began fucking her."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["preg"]:
        scene ss_vizura_standing_normal_preg_vag
    else:
        scene ss_vizura_standing_normal_normal_vag
    with dissolve
    $ Pause()
    VIZURA "Oooooh! That's it - Mhhfgh! Handsome! You fuck that little green hole!"
    "Vizura's pussy, despite taking my cock with more ease than any human girl, was incredibly tight."
    VIZURA "{i}*Huff!*{/i} Come on! No need to go gentle! Don't stop till you've stuffed me with your hot cum!"
    if tmpvar["preg"]:
        scene ss_vizura_standing_alter_preg_vag
    else:
        scene ss_vizura_standing_alter_normal_vag
    with dissolve
    $ Pause()
    "Squeezing Vizura's soft ass, she groaned happily as I picked up the pace, throwing her tight pussy back onto me."
    "Her tight hole gripped and squeezed my cock effortlessly as her feet freely dangled in the air."
    MC "{i}*Huff*{/i} Fuck! You're just- Hrghh!"
    VIZURA "Your portable little balls drainer?"
    VIZURA "Fufu, You better stuff me good with this HUGE cock human!"
    VIZURA "I want bragging rights when I get back home!"
    if tmpvar["preg"]:
        scene ss_vizura_standing_normal_preg_vag
    else:
        scene ss_vizura_standing_normal_normal_vag
    with dissolve
    $ Pause()
    "Slapping wet sounds filled the caravan as I fucked Vizura relentlessly, sweat begining to pour from the two of us as I used the little goblin slut's body for my own pleasure."
    VIZURA "OH! THAT'S IT! MFGHH! CALL ME YOUR LITTLE GREEN SLUT!"
    VIZURA "PULL MY HAIR AND TELL ME HOW YOU'RE GONNA FILL ME UP AND SEND ME BACK HOME LIKE A GOOD BRED GOBLIN WHORE!"
    "Vizura only seemed to get wetter as she spoke, desperately squeezing me with every thrust into her fat, green butt."
    "As hard as it was to focus on anything else but the wet slapping *phap! phap! phap!* sounds from where my groin hit up against her soft ass, I did my best to humour her."
    MC "Hrghh! I've always wanted - {i}*Huff*{/i} my own goblin slut for breeding!"
    VIZURA "Haha! I KNEW you were one of those perverts wanting a little goblin whore! Ooooh, who am I kidding?"
    VIZURA "The thought of being some of you big'uns little fuck slaves drives half us goblin girls wild!"
    "Our juices squealched and dripped out of her hole onto the floor beneath her feet as the goblin moaned lewdly."
    VIZURA "MMFGH! FUCK YES! Ooooh! Don't stop!"
    MC "You have such a - {i}*Huff*{/i} fat little ass!"
    VIZURA "Fufu! All the better for pumping me with, right?"
    VIZURA "Ahhh, all you humans love a nice fat arse like mine, right?"
    VIZURA "Ahh! I have this - Mmfgghh! Oh yeah! Hit it like t-that! Ooh!"
    "Vizura's tits swung back and forth with every motion as she trembled in pleasure."
    VIZURA "T-This fantasy about-"
    VIZURA "Ooooh! Being some married human's secret l-little cum dump!"
    VIZURA "His wife wondering why he never - Ooofgh! Asks for sex anymore,"
    VIZURA "Because's he's stuffing me every night!"
    "Vizura's pussy squeezed me as she spoke, her voice becoming a higher pitch as she got closer to finishing."
    "I too was finally drawing near, the intense need to finish quickly building as I pounded her little hole."
    if tmpvar["preg"]:
        scene ss_vizura_standing_alter_preg_vag
    else:
        scene ss_vizura_standing_alter_normal_vag
    with dissolve
    $ Pause()
    MC "Oh, is that - {i}*Huff*{/i} so?"
    MC "So you want the husband to sneak out of bed in the night to pound his little goblin slut, huh?"
    VIZURA "Mmmfghh! Yes!"
    VIZURA "S-She could be his little slutty goblin maid in the daytime!"
    MC "Bet the wife would wake up hearing all the slamming wouldn't she?"
    VIZURA "Ooooooooooh! So hot! SO HOT!"
    VIZURA "Cum in me already! FUCKING CUM IN YOUR LITTLE GOBLIN WHORE!"
    "Unable to hold back any longer, I flooded the little goblin with my load."
    if tmpvar["preg"]:
        scene ss_vizura_standing_normal_preg_vag_cum
    else:
        scene ss_vizura_standing_normal_normal_vag_cum
    with flash
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ Pause()

    MC "HRGHHH! Take it all you little green slut!"
    "Vizura's feet twitched as I held my cock as deeply into her as I could, making sure every drop was poured into her womb."
    "Vizura's eyes rolled back as only a hot, broken moan escaped her lips."
    VIZURA "E-EHHHHHFHHH...!!"
    "After a few breathless moments passed, I slowly slipped my cock out of Vizura's gaping, well-fucked pussy."
    scene black
    with dissolve

    "She let out a little squeal and trembled as a burst of my cum poured out of her and splashed onto the floor."
    "As I let Vizura go she dropped onto the floor, face first into the pool of my cum and began to moan, shivering as she tried to lick it up."
    MC "...You need a minute?"
    
    VIZURA "Urghhh..."
    VIZURA "M-My p-pussy...Mhmmm."

    return