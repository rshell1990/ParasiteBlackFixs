label vizura_sex_offer:
    $ VizuraCaravan().HasOfferedSex = True
    VIZURA @happy "You know handsome, as you're my favorite customer and all that."
    VIZURA @lewd "Got a little proposal for ya if you're interested?"
    MC @think "Go on?"
    VIZURA @talk "Sooooo..."
    "A big grin stretches across Vizura's face."
    VIZURA @lewd "{i}Wanna fuck?{/i}"
    MC @surprised "...Wait, what?"
    VIZURA @happy "How'd you think there's so many of us runnin' around, us goblins LOVE a good fuckin!'"
    VIZURA @lewd "So, here's what I'm thinkin' I drain those fat balls and big human cock of yours,"
    VIZURA @lewd "{i}Maybe,{/i} if you knock me up, I'll give you a ten percent discount!"
    menu vizura_sex_offer_menu:
        "{image=[ICON.HEART]} I'm interested...":
            $ CharSetLover("vizura")
            $ CharChangeRel("vizura", 1)
            $ VizuraCaravan().SexOptions = True
            $ VizuraCaravan().WantsSexToday = False
            $ ShopVizuraCaravan().Discount = VizuraCaravan().ShopDiscountIfHadSex
            VIZURA @lewd "Ho ho, I bet you are!"
            MC @talk "Are you sure you can handle me?"
            MC @talk "I mean, uh, you're a goblin and I'm... Well, {i}large{/i} by human standards."
            VIZURA @happy "Don't you worry about that! Us goblins are, {i}*Ahem* Stretchy.{/i}"        
            VIZURA @happy "My younger sister once let a minotaur strap her to himself so he could walk around whilst fucking her!"
            MC @surprised "Did she survive?"
            VIZURA @laugh "Said it was the best week of her life!"
            VIZURA @talk "So don't you worry about a thing."
            "Vizura winked at me."
            VIZURA @talk "So then ... How'sa about you and I step into my office a moment to ummm ... discuss things more privately?"
            hide vizura
            with dissolve
            "Vizura banged her fist on the caravan."
            VIZURA @angry "GO FEED THE FUCKING HORSES! I NEED THE WAGON FOR SOME ALONE TIME YOU FUCKS!"
            "The flood of goblins stormed out of the caravan and hurried off towards presumably where the horses were being kept."
            "Without wasting a second, Vizura slipped off her clothes in front of me, letting her luscious tits hang free and my cock instinctively throbbed in excitement."
            "She gave her fat green ass a playful slap as she stepped into the caravan."
            $ CharSetClothes("vizura", "naked")
            show vizura at center
            with dissolve
            $ Pause()
            VIZURA @lewd "Right this way, you handsome fuck."
            scene black with dissolve
            "Vizura placed her hands against the walls of the caravan and wiggled her fat butt enticingly towards me."
            "She licked her lips as she pulled one of her cheeks aside, showing me her bare green pussy."
            jump vizura_vag

        "Raising a child will cost me more in the long run than your discount!":
            VIZURA @angry "Ehh? Raising the kid?"
            VIZURA @angry "The fuck, why would I need you for that?"
            VIZURA @talk "We raise our spawn communally, whether your around or not is optional."
            jump vizura_sex_offer_menu

        "{image=[ICON.HEART_CROSS]} Sorry, not for me.":
            VIZURA @sad "{i}*Sigh*{/i} Pity... All well, was worth a try!"
            $ VizuraCaravan().HasOfferedSex = True
            jump vizura_caravan_talk_menu

label vizura_sex_options:
    $ VizuraCaravan().WantsSexToday = False
    "As we entered the caravan, Vizura placed her hands against the walls and wiggled her fat butt enticingly towards me."
    menu:
        "Have Vizura give you a blowjob.":
            jump vizura_blowjob
        "Lift Vizura up and fuck her.":
            VIZURA "Just pick me up and use whatever hole you want!"
            "Vizura licked her lips as she pulled one of her cheeks aside, showing me her bare green pussy and asshole."
            menu:
                "Fuck Vizura's pussy.":
                    jump vizura_vag
                "Fuck Vizura's ass":
                    jump vizura_anal

label vizura_aftersex:
    $ Pause(0.5)
    $ CharSetClothes("vizura", "normal")
    $ CharSetClothes("mc", "normal")
    $ LocFlush()
    show cg_goblin_caravan
    show mc lewd at left
    show vizura lewd at right_f
    with dissolve
    $ AutoMus(True)
    VIZURA @happy "Ahh! Just what I needed!"
    $ CharChangeRel("vizura", 1)
    $ CharAddRelEntry("vizura", "post_sex")
    VIZURA @happy "Nothing like a good {i}'stretching'{/i} I say! Fufu!"
    VIZURA @lewd "Let me know when you start needing another taste of things on the {i}'greener'{/i} side again!"
    hide mc with dissolve
    show vizura at center_f with easeinright
    jump vizura_caravan_talk_menu

label vizura_blowjob:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Grabbing the goblin by the hair and pulling her towards my member, she wrapped her hands around it and cooed happily."
    "With both of her small hands wrapped around stroking it, she teased,"
    VIZURA "You wanna shove this {i}big, hard, fat{/i} human cock down my throat, don't you?" 
    VIZURA "Bet you wanna see it bulging out in my throat fufu!"
    if CharIsVisiblyPreg("vizura"):
        MC "I hesitated for a moment, looking at Vizura's round belly protruding out." #####
        VIZURA "Don't worry about the bun in the oven, fufu." #####
        VIZURA "Us goblins are sturdy! I'll stop if there's a problem." ####
        VIZURA "Go on now, weren't you about to call me your slutty little green whore or something?" ####
        "Encouraged by her words, I smiled and carried on." ####
    MC "You sure like to talk ... But I'm not seeing enough cock down your throat for all that lip flapping your doing."
    VIZURA "Mhmmm, come here!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_bj_preg_slow 
    else:
        scene ss_vizura_bj_normal_slow 
    with dissolve
    $ Pause()
    "Vizura wrapped her wet lips around my cock, forming a tight seal as her head bopped back and forth."
    VIZURA "{i}*Slurp! Slurp!*{/i} Mmfghh...!"
    "I groaned in pleasure as her wet, silk like tongue thrashed and wrapped around my cock as her mouth glided back and forth over my member."
    "Vizura giggled as she took inch after inch of my cock deeper into her throat, cooing and moaning as her tongue beat against my cock."
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_bj_preg_fast
    else:
        scene ss_vizura_bj_normal_fast
    with dissolve
    $ Pause()
    MC "{i}*Huff*{/i} Ahhh...! How are you taking it so deep?"
    VIZURA "Mmfghh! {i}*Slurp!*{/i}"
    VIZURA "Fufu!"
    "Vizura's eyes looked up towards me, filled with desire as she knew she had me exactly where she wanted."
    "Wet slurping sounds escaped her lips as her continued to tease out the increasingly close climax wanting to flood into her mouth."
    VIZURA "(He's so cute breathing like that, I can't wait to feel that warm load inside of me!)"
    VIZURA "(Come on now handsome, give it to me!)"
    "My grip around Vizura's hair tightened as I moved my hand back and forth faster, grunting with pleasure as no matter how deep I forced my cock into Vizura's mouth, she eagerly took it."
    MC "F-Fuck! Suck that cock you little goblin whore!"
    VIZURA "{i}*Slurp! Slurp!*{/i} Mmfghhhh!! {i}*Slurp!*{/i}"
    "I continued to let Vizura work her magic for some time, until finally, I felt the growing need to finish becoming almost unbearable..."
    VIZURA "(I can feel his cock throbbin!' He's getting close!)"
    VIZURA "(Hehe! Come on! Lemme taste that thick seed!)"
    MC "Vizura ... {i}*Huff*{/i} I'm c-close to-"
    "Vizura didn't even let me finish my sentence, the front of her tongue suddely moved to the end of my cock and swirled and pushed rapidly."
    "The sudden intense sensation finally pushed me over the edge as I pulled Vizura's head forward."
    MC "HRGHHHHHH!!" #Cum 
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_bj_preg_cum
    else:
        scene ss_vizura_bj_normal_cum
    with flash
    $ Pause()
    $ ReduceInfectionFromSex("vizura")
    if CharIsVisiblyPreg("vizura"):
        $ UnlockGalFlag("vizura", "bj", "var_preg")
    else:
        $ UnlockGalFlag("vizura", "bj", "var_nopreg")
    $ UnlockGalSceneAndGrantXp("vizura", "bj")
    VIZURA "Mmfghh?!"
    "Vizura's eyes widened as she felt the rushing stream of hot, thick cum pouring down into her throat."
    "Vizura's eyes half closed as her cheeks flushed red in arousal."
    "I watched as Vizura swallowed down load after load of thick cum greedily, making sure to clean my cock thoroughly with her tongue afterwards."
    "With sultry eyes, as she dragged her lips slowly off of my cock, they pulled off the head with a loud {i}*PLOP!*{/i} sound and she giggled, showing me her open mouth to show she had swallowed all of my load." #Brief fade to black 
    VIZURA "Fufu, how was that?"
    MC "{i}*Huff*{/i} Draining."
    VIZURA "That's what I like to hear handsome."
    "Vizura wiped her lips and burped."
    if CharIsVisiblyPreg("vizura"):
        VIZURA "Well, looks like me and the littlun won't have to worry about dinner this afternoon! Hehe!"
        VIZURA "{i}Nutritious!{/i}"
    else:
        VIZURA "Well, looks like I won't have to worry about dinner this afternoon! Hehe!"
        VIZURA "When you're cleaned up and ready, I'll be outside."
    scene black with dissolve
    "Vizura wiggled her butt playfully as she left the caravan, happily humming to herself."
    "Once re-dressed, and re-composed, I too joined her and left the caravan."
    jump vizura_aftersex

label vizura_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_alter_preg_idle
    else:
        scene ss_vizura_standing_alter_normal_idle
    with dissolve
    $ Pause()
    "Lifting Vizura off the ground, she giggled as I aligned my cock against her wet, tight womanhood."
    if CharIsVisiblyPreg("vizura"):
        "I paused for a moment, looking down at the round hanging belly."
        VIZURA "Don't worry about the baby, handsome, us goblins are sturdy!"
        VIZURA "Besides! Feels nice not to actually have to feel that extra weight for a little while! Hehe!"
        "Reassured, I nodded and smiled at her words."
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_idle
    else:
        scene ss_vizura_standing_normal_normal_idle
    with dissolve
    $ Pause()
    "With ease, I pressed the head of my cock against her hole, she let out a hot sigh as I pressed my cock in deeper and deeper into her and began fucking her."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_vag
    else:
        scene ss_vizura_standing_normal_normal_vag
    with dissolve
    $ Pause()
    VIZURA "Oooooh! That's it - Mhhfgh! Handsome! You fuck that little green hole!"
    "Vizura's pussy, despite taking my cock with more ease than any human girl, was incredibly tight."
    VIZURA "{i}*Huff!*{/i} Come on! No need to go gentle! Don't stop till you've stuffed me with your hot cum!"
    if CharIsVisiblyPreg("vizura"):
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
    if CharIsVisiblyPreg("vizura"):
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
    if CharIsVisiblyPreg("vizura"):
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
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_vag_cum
    else:
        scene ss_vizura_standing_normal_normal_vag_cum
    with flash
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ Pause()
    $ ReduceInfectionFromSex("vizura")
    if CharIsVisiblyPreg("vizura"):
        $ UnlockGalFlag("vizura", "vag", "var_preg")
    else:
        # first time is 100% impreg
        if PregVizura().NumImpregs == 0:
            $ PregRoll("vizura", ChanceOverride = 100)
        # on repeat 
        else:
            $ PregRoll("vizura")
        $ UnlockGalFlag("vizura", "vag", "var_nopreg")
    $ UnlockGalSceneAndGrantXp("vizura", "vag")

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
    jump vizura_aftersex

label vizura_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_alter_preg_idle
    else:
        scene ss_vizura_standing_alter_normal_idle
    with dissolve
    $ Pause()
    "Lifting Vizura off the ground, she giggled as I aligned my cock against her tight, dark spinchter."
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_idle
    else:
        scene ss_vizura_standing_normal_normal_idle
    with dissolve
    $ Pause()
    VIZURA "Fufu, you really want this goblin butt, don't you?"
    if CharIsVisiblyPreg("vizura"):
        "I paused for a moment, looking down at the round hanging belly."
        VIZURA "Don't worry about the baby, handsome, us goblins are sturdy!"
        VIZURA "Besides! Feels nice not to actually have to feel that extra weight for a little while! Hehe!"
        "Reassured, I nodded and smiled at her words."
    "As I pressed the head of my cock against her asshole, after some brief resistance and grunting, her backdoor spread open and wrapped around my cock as I pressed it into her ass."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_anal
    else:
        scene ss_vizura_standing_normal_normal_anal
    with dissolve
    $ Pause()
    VIZURA "Urghh! You wanna fuck that goblin arse handsome? Mmfghh! Y-You better re-shape it properly into being a little cocksleeve for you!"
    "Vizura's ass felt immensely tight, yet, much to my surprise, was wet and lubricated inside."
    VIZURA "{i}*Huff!*{/i} Bet you didn't know goblin arse did that, huh? Fufu, we're built for taking cock anywhere!" 
    VIZURA "Come on! No need to go gentle! Stuff that butt properly!"
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_alter_preg_anal
    else:
        scene ss_vizura_standing_alter_normal_anal
    with dissolve
    $ Pause()
    "Squeezing Vizura's soft ass, she groaned happily as I picked up the pace, throwing her tight asshole back onto me."
    "Her tight hole gripped and squeezed my cock effortlessly as her feet freely dangled in the air."
    MC "{i}*Huff*{/i} Fuck! You're just- Hrghh!"
    VIZURA "Your portable little balls drainer?"
    VIZURA "Fufu, You better stuff my ass good with this HUGE cock human!"
    if CharIsVisiblyPreg("vizura"):
        VIZURA "I'm gonna be - {i}*Huff!*{/i} the envy of those goblin sluts when they see me parading around our littluns!"
    VIZURA "I want bragging rights when I get back home!"
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_anal
    else:
        scene ss_vizura_standing_normal_normal_anal
    with dissolve
    $ Pause()
    "Slapping wet sounds filled the caravan as I fucked Vizura's ass relentlessly, sweat begining to pour from the two of us as I used the little goblin slut's body for my own pleasure."
    VIZURA "OH! THAT'S IT! MFGHH! CALL ME YOUR LITTLE GREEN SLUT!"

    if CharIsVisiblyPreg("vizura"):
        VIZURA "PULL MY HAIR AND FILL UP YOUR BRED GOBLIN WHORE!"
    else:
        VIZURA "PULL MY HAIR AND TELL ME HOW YOU'RE GONNA USE MY ARSE WHENEVER YOU WANT!"

    "Vizura only seemed to get wetter as she spoke, desperately squeezing me with every thrust into her fat, green butt."
    "As hard as it was to focus on anything else but the wet slapping *phap! phap! phap!* sounds from where my groin hit up against her soft ass, I did my best to humour her."
    MC "Hrghh! You better keep this - {i}*Huff*{/i} Litle asshole ready for me to mess it up good anytime!"

    if CharIsVisiblyPreg("vizura"):
        VIZURA "Haha! You little pervert! Bet you stroke that big cock thinkin' about what you've done to me, eh?"
        VIZURA "I'd be the envy of my tribe right now! Hehe!"
    else:
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
    "Vizura's ass squeezed me as she spoke, her voice becoming a higher pitch as she got closer to finishing."
    "I too was finally drawing near, the intense need to finish quickly building as I pounded her little backdoor."
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_alter_preg_anal
    else:
        scene ss_vizura_standing_alter_normal_anal
    with dissolve
    $ Pause()
    MC "Oh, is that - {i}*Huff*{/i} so?"
    MC "So you want the husband to sneak out of bed in the night to pound his little goblin slut, huh?"
    VIZURA "Mmmfghh! Yes!"
    VIZURA "S-She could be his little slutty goblin maid in the daytime!"
    MC "Bet the wife would wake up hearing all the slamming wouldn't she?"
    VIZURA "Ooooooooooh! So hot! SO HOT!"
    VIZURA "Cum in me already! FUCKING CUM IN YOUR LITTLE GOBLIN WHORE!"
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_anal
    else:
        scene ss_vizura_standing_normal_normal_anal
    with dissolve
    $ Pause()
    "Unable to hold back any longer, I flooded the little goblin with my load."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    if CharIsVisiblyPreg("vizura"):
        scene ss_vizura_standing_normal_preg_anal_cum
    else:
        scene ss_vizura_standing_normal_normal_anal_cum
    with flash
    $ Pause()
    $ ReduceInfectionFromSex("vizura")
    if CharIsVisiblyPreg("vizura"):
        $ UnlockGalFlag("vizura", "anal", "var_preg")
    else:
        $ UnlockGalFlag("vizura", "anal", "var_nopreg")
    $ UnlockGalSceneAndGrantXp("vizura", "anal")
    MC "HRGHHH! Take it all you little green slut!"
    "Vizura's feet twitched as I held my cock as deeply into her as I could, making sure every drop was poured into her backdoor."
    "Vizura's eyes rolled back as only a hot, broken moan escaped her lips."
    VIZURA "E-EHHHHHFHHH...!!"
    "After a few breathless moments passed, I slowly slipped my cock out of Vizura's gaping, well-fucked asshole."
    scene black
    with dissolve
    "She let out a little squeal and trembled as a burst of my cum poured out of her and splashed onto the floor."
    "As I let Vizura go she dropped onto the floor, face first into the pool of my cum and began to moan, shivering as she tried to lick it up."
    MC "...You need a minute?"
    VIZURA "Urghhh..."
    VIZURA "M-My a-asshh...Mhmmm."
    jump vizura_aftersex