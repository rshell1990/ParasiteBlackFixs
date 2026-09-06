label gallery_winward_missionary:
########################
    if GalFlag("mrs_winward", "missionary", ["naked", "cow"]):
        "Was she wearing her cow outfit?"
        menu:
            "Yes":
                $ tmpvar["cow"] = True
            "No":
                $ tmpvar["cow"] = False

    elif GalFlag("mrs_winward", "missionary", "cow"):
        $ tmpvar["cow"] = True

    elif GalFlag("mrs_winward", "missionary", "naked"):
        $ tmpvar["cow"] = False
#######################
    if GalFlag("mrs_winward", "missionary", ["preg", "nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False

    elif GalFlag("mrs_winward", "missionary", "preg"):
        $ tmpvar["preg"] = True

    elif GalFlag("mrs_winward", "missionary", "nopreg"):
        $ tmpvar["preg"] = False
########################
    if GalFlag("mrs_winward", "missionary", ["vag", "anal"]):
        "Was the encounter vaginal or anal?"
        menu:
            "Vaginal":
                $ tmpvar["vag"] = True
            "Anal":
                $ tmpvar["vag"] = False

    elif GalFlag("mrs_winward", "missionary", "vag"):
        $ tmpvar["vag"] = True

    elif GalFlag("mrs_winward", "missionary", "anal"):
        $ tmpvar["vag"] = False
#######################
    "What about Mr. Winward?"
    menu:
        "Mr. Winward was sleeping" if GalFlag("mrs_winward", "missionary", "oldmansleep"):
            $ tmpvar["oldman"] = "sleep"
        "Mr. Winward was watching us" if GalFlag("mrs_winward", "missionary", "oldmanwatch"):
            $ tmpvar["oldman"] = "watch"
        "Mr. Winward wasn't there" if GalFlag("mrs_winward", "missionary", "solo"):
            $ tmpvar["oldman"] = "solo"

    if tmpvar["oldman"] == "sleep":
        if tmpvar["vag"] == True:
            jump gallery_winward_missionary_sleep_vag
        else:
            jump gallery_winward_missionary_sleep_anal

    if tmpvar["oldman"] == "watch":
        if tmpvar["vag"] == True:
            jump gallery_winward_missionary_watch_vag
        else:
            jump gallery_winward_missionary_watch_anal

    if tmpvar["oldman"] == "solo":
        if tmpvar["vag"] == True:
            jump gallery_winward_missionary_solo_vag
        else:
            jump gallery_winward_missionary_solo_anal

label gallery_winward_missionary_sleep_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)

    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_naked_preg_vag_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_vag_slow with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_cow_preg_vag_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_vag_slow with dissolve

    $ Pause()

    "Gently, I pressed the head of my cock against Mrs Winward's tight, wet hole."
    "After some light prodding, her body opened up to me, and I gently and slowly pushed inch by inch into her."
    MRS_WINWARD "M-Mmmmfghhhh!!"
    "Her body tightened and squeezed around me, and sensing shock, I paused for a brief moment."
    MRS_WINWARD "Ooooh, it's always even b-bigger than I remember! Mhmm!"
    "Slowly, I picked up pace, gently fucking Mrs Winward as I pushed my cock inch by inch deeper into her womanhood."
    "Soft, hot moans escaped her lips as she slowly become more comfortable with my size."
    MRS_WINWARD "Y-Yes, that's - Mhmm! Goooood!"
    MRS_WINWARD "Ahh! B-Breed your little cow!"
    MC "Tell me again whose you prefer!"
    MRS_WINWARD "Ooooh! Why do y-you make me say such - Ahh! Cruel things especially with my husband sleeping - oooh! Next to me!!"
    MC "Because if you don't tell me, your {i}'bull'{/i} will stop."
    MRS_WINWARD "Mhmmm... {image=[ICON.HEART]}"
    MRS_WINWARD "Y-Yours! Your cock is so much - Mhmm! Better!"
    MRS_WINWARD "His cock is worthless compared to yours!"
    MRS_WINWARD "Y-Your little cow needs breeding by a real man's cock!"
    MRS_WINWARD "Do you hear that dear? Do you hear how your wife enjoys spreading her legs for another man?"
    MR_WINWARD "{i}*Grumbles*{/i}"
    "Her words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth turning her on all the more."
    "Her desperation for my cock only further excited me, as I began to move faster."
    MRS_WINWARD "Oooh! D-Dear!"
    MRS_WINWARD "Mmfhghh!"

    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_naked_preg_vag_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_vag_fast with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_cow_preg_vag_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_vag_fast with dissolve
    $ Pause()

    "Now slamming my cock deeply into her hole, Mrs Winward gasped and moaned, sweat dripping from her body as she took me excitedly."
    MRS_WINWARD "OOOOOOOOOH!"
    MRS_WINWARD "Itshhh shooo ghoood!"
    MRS_WINWARD "S-Slow down! Mhmm! I can't - Ahhhh!"
    "Ignoring her pleas this time, I thrust deeply into Mrs Winward, reshaping her tight box to fit my needs."
    "As her grunts and moans grew louder, she trembled and shook beneath me, overwhelmed by waves of pleasure flowing across her neglected body."
    "As her eyes began to roll up towards the ceiling, I felt her body melt as the last hints of nervous resistance flickered away."
    "Broken in, her mind overwhelmed, her perverse thoughts and words came tumbling out freely."
    MRS_WINWARD "{i}F-Fuck me!{/i}"
    MRS_WINWARD "Breed your little whore cow!{image=[ICON.HEART]}"
    MRS_WINWARD "Show my loser husband how it's - Ahh! Done!"
    MRS_WINWARD "Let him wake up and see your seed - Ahh! Running down my shaking legs!"
    MRS_WINWARD "I want him to know you've - ahh! Fucked me better than he ever could!"
    "Slamming into her, the wetness of her now soaking cunt filled the room as she choked with pleasure."
    MRS_WINWARD "C-Cum in me!"
    MRS_WINWARD "{i}Fill your cow up!{/i}"
    MRS_WINWARD "Do you hear that dear? He's g-going to breed me!"
    MRS_WINWARD "Your wife is getting bred by a real man while you sleep next to her!"
    "As my cock twitched and throbbed, I knew I couldn't hold on much longer."
    "Giving in to the overwhelming desire, I slammed my cock to the hilt and pushed her wrists harder down."
    "Grunting loudly, I poured my thick, heavy load into her tight womanhood."

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_naked_preg_vag_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_vag_finish with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_cow_preg_vag_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_vag_finish with dissolve
    $ Pause()

    MC "H-HRGHHHHH...!!"
    "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me feeling the rush of warm fluid flood her womb."
    MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
    "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
    "She shuddered slightly as she felt some of my seed trickle in a steady stream out of her, panting hotly."
    MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
    MC "Ahhh...Are you alright, Mrs Winward?"
    MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
    MRS_WINWARD "Just need a little... A little..."
    return

label gallery_winward_missionary_sleep_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_naked_preg_anal_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_anal_slow with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_cow_preg_anal_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_anal_slow with dissolve
    $ Pause()

    "As I gently prodded the head of my sword against her tight asshole, Mrs Winward let out a little gasp."
    MC "Are you ready to take it back here?"
    "Mrs Winward cooed and nodded alluringly."
    "She gulped nervously."
    MRS_WINWARD "M-My ass is all yours, dear."
    MRS_WINWARD "P-Please dear, be gentle with my rear."
    "Gently, as I pushed against her wet, lubed hole, the rim of her tight asshole stretched and swallowed the head of my cock."
    "She let out a lewd gasp as she felt my cock sink inch by inch deeper into her backdoor."
    "Her mouth hung agape as she watched my cock sink deeper into her ass."
    MRS_WINWARD "Oooooh! I f-feel so..."
    MRS_WINWARD "{i}Stuffed.{/i}"
    "Slowly, I moved my cock in and out of her tight ass, which clung and squeezed me effortlessly as I did so."
    "Mrs Winward would wince in pain occasionally, a trembling nervous breath escaping her lips as she did her best to relax with the huge log of meat in her ass."
    "Slowly though, as I pushed in and out of her ass, the pain began to subside as soft, hot moans escaped her lips."
    MRS_WINWARD "A-Ahhh! It still - Mhmm! Feels like it burns but-"
    MRS_WINWARD "Mhmm! My poor ass! It's starting to f-feel quite... Ooooh!"
    MRS_WINWARD "{i}N-Nice...{/i}"
    
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_naked_preg_anal_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_anal_fast with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_cow_preg_anal_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_anal_fast with dissolve
    $ Pause()

    "Slowly, I began to pick up speed, ramming my cock into her incredibly tight, soft ass as Mrs Winward's guttural moans grew louder and louder."
    MRS_WINWARD "Y-Yes! Pound my ass!"
    MRS_WINWARD "Do you hear that - Ahhh! Honey?"
    MRS_WINWARD "I'd n-never give you this hole! But he-"
    MRS_WINWARD "Mhmmfhh! He can have it whenever he wants!"
    MRS_WINWARD "Fuck my asshhh! It feels shooo ghoood! Mhfhh!"
    "Mrs Winward's eyes began to roll back into her head as she allowed me to freely slam my cock into her now welcoming ass."
    "She groaned, moaning with pleasure as her tight insides squeezed and teased my cock closer and closer to the edge."
    MC "Ahh! Your ass is so tight! Kionni!"
    MC "I'm gonna make sure you're not able to walk straight for days when I'm done!"
    MRS_WINWARD "OOOOOOH! Y-Yes! Fuck my little hole!"
    MRS_WINWARD "F-Fill this old lady's rear up with your load!"
    "Her body trembled beneath me, her heart racing as I defiled her forbidden hole, sweat dripping from her body."
    MRS_WINWARD "{i}*Huff*{/i} D-Dear! Mhmm! He's too much for my - Ahh! Poor little ashhh!"
    MRS_WINWARD "He's g-gonna - Mhfhhh! M-Make me c-cummm from... from..."
    MRS_WINWARD "{i}*Gasp!*{/i}"
    "Mrs Winward's body trembled and shook in orgasm as her asshole tightened and squeezed around my cock intensely."
    "The sudden, swift sensation overpowered me, and my cock twitched in excitement as I felt my balls rise."
    "On the edge of release, I grunted to warn Mrs Winward."
    MC "{i}G-Gonna...!{/i}"
    MRS_WINWARD "{i}Do it! Fill my butt up!{/i} {image=[ICON.HEART]}"
    
    "Unable to hold back any longer, I buried my cock as deeply as I could into her rump, grunting loudly as I poured my hot seed into her bowels." 
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_naked_preg_anal_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_anal_finish with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmansleep_cow_preg_anal_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_anal_finish with dissolve
    $ Pause()

    MC "H-Hrghhhhh...!"
    "Mrs Winward's eyes rolled back as she cooed and twitched feeling my cum fill up her ass."
    "As I poured out every last drop of the thick seed into her ass, she quivered and moaned softly, not saying a word as I slowly unsheathed my cock from her now loosened ass."
    "With a small {i}*pop!*{/i} sound, my cock pulled out of her quivering, winking asshole as my seed poured out of her gaping hole on the bed."
    MRS_WINWARD "A-Ahhh....!! {image=[ICON.HEART]}"
    MC "{i}*Huff*{/i} Are you alright, Mrs Winward?"
    MRS_WINWARD "M-Mhmmm...."
    return

label gallery_winward_missionary_watch_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)

    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_naked_preg_vag_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_naked_nopreg_vag_slow with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_cow_preg_vag_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_cow_nopreg_vag_slow with dissolve

    $ Pause()

    "Gently, I pressed the head of my cock against Mrs Winward's tight, wet hole."
    "After some light prodding, her body opened to me, and gently, I slowly pushed inch by inch into her."
    MRS_WINWARD "M-Mmmmfghhhh!!"
    "Her body tightened and squeezed around me, and sensing shock, I paused for a brief moment."
    MRS_WINWARD "I'm f-fine, just... {i}continue.{/i}"
    "Slowly, I picked up the pace, gently fucking Mrs. Winward as I pushed my cock inch by inch deeper into her womanhood."
    "Soft, hot moans escaped her lips as she slowly became more comfortable with my size."
    MRS_WINWARD "Y-Yes, that's - Mhmm! Goooood!"
    "Mr Winward stroked his cock faster as he watched my cock sink deeper into his wife."
    MR_WINWARD "That's - {i}*Huff*{/i} it lad! Fuck her good!"
    MR_WINWARD "Your cock was made to fill my wife!"
    MRS_WINWARD "Ahh! B-Breed your little cow!"
    MC "Is it better than your husband's?"
    "Mrs. Winward giggled mischievously as her husband beside her listened intently, hanging on every word she said."
    MRS_WINWARD "Fufu, yours of course!"
    MRS_WINWARD "Y-You really think that tiny thing next to me could ever satisfy me now I've had your wonderful, {i}huge{/i} cock?"
    "Her words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth, turning her on all the more."
    "Mr. Winward stroked faster, mumbling in approval as Mrs. Winward continued to degrade him with his encouragement."
    MR_WINWARD "Y-Yes dear... {i}*Huff*{/i} You need to be - ahh! Filled up with that cock nightly! Oooh!"
    MRS_WINWARD "You old - ahh! Pervert!"
    MRS_WINWARD "Fufu! Fine, I'll get a REAL MAN to fuck me nightly if that's what you really want!"
    "Her desperation for my cock only further excited me as I began to move faster."
    MRS_WINWARD "Oooh! D-Dear!"
    MRS_WINWARD "Mmfhghh!"
    
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_naked_preg_vag_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_naked_nopreg_vag_fast with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_cow_preg_vag_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_cow_nopreg_vag_fast with dissolve
    $ Pause()

    "Now slamming my cock deeply into her hole, Mrs Winward gasped and moaned, sweat dripping from her body as she took me excitedly."
    MRS_WINWARD "OOOOOOOOOH!"
    MRS_WINWARD "Itshhh shooo ghoood!"
    MRS_WINWARD "S-Slow down! Mhmm! I can't - Ahhhh!"
    "Ignoring her pleas this time, I thrust deeply into Mrs Winward, reshaping her tight box to fit my needs."
    MC "Are you - Ahh! Watching you, old pervert?"
    MC "Your wife ever gives these expressions with you?"
    MR_WINWARD "N-No! Never!"
    MR_WINWARD "P-Please don't stop! Can't you see how desperate she's needed a cock like yours?"
    MR_WINWARD "I've neglected her delicious body for too long! Now it's up to you to fix this foolish old man's mistakes!"
    "As her grunts and moans grew louder, she trembled and shook beneath me, overwhelmed by waves of pleasure across her neglected body."
    "As her eyes began to roll up towards the ceiling, I felt her body melt as the last hints of nervous resistance flickered away."
    "Broken in, her mind overwhelmed, her perverse thoughts and words came tumbling out freely."
    MRS_WINWARD "{i}F-Fuck me!{/i}"
    MRS_WINWARD "Breed your little whore cow!{image=[ICON.HEART]}"
    MRS_WINWARD "Show my loser husband how it's - Ahh! Done!"
    "Slamming into her, the wetness of her now soaking cunt filled the room as she choked with pleasure."
    MRS_WINWARD "C-Cum in me!"
    MRS_WINWARD "{i}Fill your cow up!{/i}"
    "As my cock twitched and throbbed, I knew I couldn't hold on much longer."
    MR_WINWARD "Y-Yes! Finish inside of her!"
    MR_WINWARD "Your seed needs to take root!"
    "Giving in to the overwhelming desire, I slammed my cock to the hilt and pushed her wrists harder down."
    "Grunting loudly, I poured my thick, heavy load into her tight womanhood."

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_naked_preg_vag_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_naked_nopreg_vag_finish with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_cow_preg_vag_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_cow_nopreg_vag_finish with dissolve
    $ Pause()

    MC "H-HRGHHHHH...!!"
    "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me, feeling the rush of warmth flood her womb."
    MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
    "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
    "She slightly shuddered as she felt some of my seed trickle in a steady stream out of her, panting hotly."
    MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
    "As my seed seeped out of her well-fucked hole, Mr Winward himself finally finished, squirting a load over himself as he grunted in pleasure."
    MR_WINWARD "H-Hrghhh!"
    MR_WINWARD "{i}*Huff*{/i} Gods lad, when are you going to be up for fucking her again?"
    MR_WINWARD "She should be ready to go in a few hours!"
    "Ignoring the perverted old man, I turned my attention towards Kionni."
    MC "Ahhh...Are you alright, Mrs Winward?"
    MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
    MRS_WINWARD "Just need a little... A little..."
    return

label gallery_winward_missionary_watch_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_naked_preg_anal_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_naked_nopreg_anal_slow with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_cow_preg_anal_slow with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_cow_nopreg_anal_slow with dissolve
    $ Pause()

    "As I gently prodded the head of my cock against her tight asshole, Mrs Winward let out a little gasp."
    MC "Are you ready to take it back here?"
    "Mrs Winward cooed and nodded alluringly."
    "She gulped nervously."
    MRS_WINWARD "M-My ass is all yours, dear."
    MRS_WINWARD "P-Please dear, be gentle with my rear."
    "She let out a lewd gasp as she felt my cock sink inch by inch deeper into her backdoor."
    "Her mouth hung agape as she watched my cock sink deeper into her ass."
    MRS_WINWARD "Oooooh! I f-feel so..."
    MRS_WINWARD "{i}Stuffed.{/i}"
    "Mr Winward stroked his cock faster and watched in wide-eyed awe as his wife's tight ass was ruined before him."
    MR_WINWARD "M-My love! He's stretching out your-"
    MRS_WINWARD "H-Hrghh! My a-assshhh!"
    MRS_WINWARD "You better get used to - Ahh! Watching this! Mhhhhff!"
    MRS_WINWARD "Something tells me he's gonna want to - {i}*Huff*{/i} Stuff my little hole again!"
    "Mr. Winward said nothing, only stroking furiously at her words."
    "Slowly, I moved my cock in and out of her tight ass, which clung and squeezed me effortlessly as I did so."
    "Mrs Winward would wince in pain occasionally, a trembling nervous breath escaping her lips as she did her best to relax with the huge log of meat in her ass."
    "Slowly though, as I pushed in and out of her ass, the pain began to subside as soft, hot moans escaped her lips."
    MRS_WINWARD "A-Ahhh! It still - Mhmm! Feels like it burns, but-"
    MRS_WINWARD "Mhmm! My poor ass! It's starting to f-feel quite... Ooooh!"
    MRS_WINWARD "{i}N-Nice...{/i}"

    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_naked_preg_anal_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_naked_nopreg_anal_fast with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_cow_preg_anal_fast with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_cow_nopreg_anal_fast with dissolve
    $ Pause()

    "Slowly, I began to pick up speed, ramming my cock into her incredibly tight, soft ass as Mrs. Winward's guttural moans grew louder and louder."
    MRS_WINWARD "Y-Yes! Pound my ass!"
    MRS_WINWARD "Do you hear that - Ahhh! Honey?"
    MRS_WINWARD "I'd n-never give you this hole! But he-"
    MRS_WINWARD "Mhmmfhh! He can have it whenever he wants!"
    MRS_WINWARD "Fuck my asshhh! It feels shooo ghoood! Mhfhh!"
    "Mrs Winward's eyes began to roll back into her head as she allowed me to freely slam my cock into her now welcoming ass."
    "She groaned, moaning with pleasure as her tight insides squeezed and teased my cock closer and closer to the edge."
    MC "Ahh! Your ass is so tight! Kionni!"
    MC "I'm gonna make sure you can't walk straight for days when I'm done!"
    MRS_WINWARD "OOOOOOH! Y-Yes! Fuck my little hole!"
    MRS_WINWARD "F-Fill this old lady's rear up with your load!"
    "Her body trembled beneath me, her heart racing as I defiled her forbidden hole, sweat dripping from her body."
    MRS_WINWARD "{i}*Huff*{/i} D-Dear! Mhmm! He's too much for my - Ahh! Poor little ashhh!"
    MRS_WINWARD "He's g-gonna - Mhfhhh! M-Make me c-cummm from... from..."
    MRS_WINWARD "{i}*Gasp!*{/i}"
    "Mrs Winward's body trembled and shook in orgasm as her asshole tightened and squeezed around my cock intensely."
    "The sudden, swift sensation overpowered me; my cock twitched in excitement as I felt my balls rise."
    "On the edge of release, I grunted to warn Mrs Winward."
    MC "{i}G-Gonna...!{/i}"
    MRS_WINWARD "{i}Do it! Fill my butt up!{/i} {image=[ICON.HEART]}"
    "Unable to hold back any longer, I buried my cock as deeply as I could into her rump, loudly grunting as I poured my hot seed into her bowels." #Cum

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_naked_preg_anal_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_naked_nopreg_anal_finish with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_oldmanwatch_cow_preg_anal_finish with dissolve
        else:
            scene mrs_winward_missionary_oldmanwatch_cow_nopreg_anal_finish with dissolve
    $ Pause()
    MC "H-Hrghhhhh...!"
    "Mrs Winward's eyes rolled back as she cooed and twitched, feeling my cum fill up her ass."
    "As I poured out every last drop of the thick seed into her ass, she quivered and moaned softly, not saying a word as I slowly unsheathed my cock from her now loosened ass."
    "With a small {i}*pop!*{/i} sound, my cock pulled out of her quivering, winking asshole as my seed poured out of her gaping hole on the bed."
    MRS_WINWARD "A-Ahhh....!! {image=[ICON.HEART]}"
    MC "{i}*Huff*{/i} Are you alright, Mrs Winward?"
    MRS_WINWARD "M-Mhmmm...."
    "Kionni simply quivered and moaned in response; some of my cum continued to seep out of her hole as she laid there motionless on the bed."
    MC "Thanks for letting me use your ass, Mrs Winward."
    MRS_WINWARD "A-Ahhhh...{image=[ICON.HEART]}"
    return

label gallery_winward_missionary_solo_vag:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)

    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_naked_preg_vag_slow with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_vag_slow with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_cow_preg_vag_slow with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_vag_slow with dissolve

    $ Pause()

    "Gently, I pressed the head of my cock against Mrs Winward's tight, wet hole."
    "After some light prodding, her body opened to me, and gently, I slowly pushed inch by inch into her."
    MRS_WINWARD "M-Mmmmfghhhh!!"
    "Her body tightened and squeezed around me, and sensing shock, I paused for a brief moment."
    MRS_WINWARD "Ooooh, it's always even b-bigger than I remember! Mhmm!"
    "Slowly, I picked up pace, gently fucking Mrs Winward as I pushed my cock inch by inch deeper into her womanhood."
    "Soft, hot moans escaped her lips as she slowly become more comfortable with my size."
    MRS_WINWARD "Y-Yes, that's - Mhmm! Goooood!"
    MRS_WINWARD "Ahh! B-Breed your little cow!"
    MC "Tell me again whose you prefer!"
    MRS_WINWARD "Ooooh! Y-You make me say such - Ahh! Cruel things!!"
    MC "Because if you don't tell me, your {i}'bull'{/i} will stop."
    MRS_WINWARD "Mhmmm... {image=[ICON.HEART]}"
    MRS_WINWARD "Y-Yours! Your cock is so much - Mhmm! Better!"
    MRS_WINWARD "His cock is worthless compared to yours!"
    MRS_WINWARD "Y-Your little cow needs breeding by a real man's cock!"
    "Her words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth turning her on all the more."
    "Her desperation for my cock only further excited me, as I began to move faster."
    MRS_WINWARD "Oooh! D-Dear!"
    MRS_WINWARD "Mmfhghh!"

    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_naked_preg_vag_fast with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_vag_fast with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_cow_preg_vag_fast with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_vag_fast with dissolve
    $ Pause()

    "Now slamming my cock deeply into her hole, Mrs Winward gasped and moaned, sweat dripping from her body as she took me excitedly."
    MRS_WINWARD "OOOOOOOOOH!"
    MRS_WINWARD "Itshhh shooo ghoood!"
    MRS_WINWARD "S-Slow down! Mhmm! I can't - Ahhhh!"
    "Ignoring her pleas this time, I thrust deeply into Mrs Winward, reshaping her tight box to fit my needs."
    "As her grunts and moans grew louder, she trembled and shook beneath me, overwhelmed by waves of pleasure flowing across her neglected body."
    "As her eyes began to roll up towards the ceiling, I felt her body melt as the last hints of nervous resistance flickered away."
    "Broken in, her mind overwhelmed, her perverse thoughts and words came tumbling out freely."
    MRS_WINWARD "{i}F-Fuck me!{/i}"
    MRS_WINWARD "Breed your little whore cow!{image=[ICON.HEART]}"
    "Slamming into her, the wetness of her now soaking cunt filled the room as she choked with pleasure."
    MRS_WINWARD "C-Cum in me!"
    MRS_WINWARD "{i}Fill your cow up!{/i}"
    "As my cock twitched and throbbed, I knew I couldn't hold on much longer."
    "Giving in to the overwhelming desire, I slammed my cock to the hilt and pushed her wrists harder down."
    "Grunting loudly, I poured my thick, heavy load into her tight womanhood." #Cum

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_naked_preg_vag_finish with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_vag_finish with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_cow_preg_vag_finish with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_vag_finish with dissolve
    $ Pause()

    MC "H-HRGHHHHH...!!"
    "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me feeling the rush of warmth flood her womb."
    MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
    "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
    "She shuddered slightly as she felt some of my seed trickle in a steady stream out of her, panting hotly."
    MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
    MC "Ahhh...Are you alright, Mrs Winward?"
    MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
    MRS_WINWARD "Just need a little... A little..."
    "As Mrs Winward closed her eyes, she was soon drifting off asleep, snoring lightly as my cum continued to ooze from her well fucked hole."
    return

label gallery_winward_missionary_solo_anal:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_naked_preg_anal_slow with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_anal_slow with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_cow_preg_anal_slow with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_anal_slow with dissolve
    $ Pause()

    "As I gently prodded the head of my cock against her tight asshole, Mrs Winward let out a little gasp."
    MC "Are you ready to take it back here?"
    "Mrs Winward cooed and nodded alluringly."
    "She gulped nervously."
    MRS_WINWARD "M-My ass is all yours, dear."
    MRS_WINWARD "P-Please dear, be gentle with my rear."
    "Gently, as I pushed against her wet, lubed hole, the rim of her tight asshole stretched and swallowed the head of my cock."
    "She let out a lewd gasp as she felt my cock sink inch by inch deeper into her backdoor."
    "Her mouth hung agape as she watched my cock sink deeper into her ass."
    MRS_WINWARD "Oooooh! I f-feel so..."
    MRS_WINWARD "{i}Stuffed.{/i}"
    "Slowly, I moved my cock in and out of her tight ass, which clung and squeezed me effortlessly as I did so."
    "Mrs Winward would wince in pain occasionally, a trembling nervous breath escaping her lips as she did her best to relax with the huge log of meat in her ass."
    "Slowly though, as I pushed in and out of her ass, the pain began to subside as soft, hot moans escaped her lips."
    MRS_WINWARD "A-Ahhh! It still - Mhmm! Feels like it burns but-"
    MRS_WINWARD "Mhmm! My poor ass! It's starting to f-feel quite... Ooooh!"
    MRS_WINWARD "{i}N-Nice...{/i}"
    
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_naked_preg_anal_fast with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_anal_fast with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_cow_preg_anal_fast with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_anal_fast with dissolve
    $ Pause()

    "Slowly, I began to pick up speed, ramming my cock into her incredibly tight, soft ass as Mrs Winward's guttural moans grew louder and louder."
    MRS_WINWARD "Y-Yes! Pound my ass!"
    MRS_WINWARD "Fuck my asshhh! It feels shooo ghoood! Mhfhh!"
    "Mrs Winward's eyes began to roll back into her head as she allowed me to freely slam my cock into her now welcoming ass."
    "She groaned, moaning with pleasure as her tight insides squeezed and teased my cock closer and closer to the edge."
    MC "Ahh! Your ass is so tight! Kionni!"
    MC "I'm gonna make sure you're not able to walk straight for days when I'm done!"
    MRS_WINWARD "OOOOOOH! Y-Yes! Fuck my little hole!"
    MRS_WINWARD "F-Fill this old lady's rear up with your load!"
    "Her body trembled beneath me, her heart racing as I defiled her forbidden hole, sweat dripping from her body."
    MRS_WINWARD "{i}*Huff*{/i} D-Dear! Mhmm! He's too much for my - Ahh! Poor little ashhh!"
    MRS_WINWARD "He's g-gonna - Mhfhhh! M-Make me c-cummm from... from..."
    MRS_WINWARD "{i}*Gasp!*{/i}"
    "Mrs Winward's body trembled and shook in orgasm as her asshole tightened and squeezed around my cock intensely."
    "The sudden, swift sensation overpowered me, my cock twitched in excitement as I felt my balls rise."
    "On the edge of release, I grunted to warn Mrs Winward."
    MC "{i}G-Gonna...!{/i}"
    MRS_WINWARD "{i}Do it! Fill my butt up!{/i} {image=[ICON.HEART]}"
    "Unable to hold back any longer, I buried my cock as deeply as I could into her rump, grunting loudly as I poured my hot seed into her bowels." #Cum

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    if tmpvar["cow"] == False:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_naked_preg_anal_finish with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_anal_finish with dissolve
    else:
        if tmpvar["preg"] == True:
            scene mrs_winward_missionary_solo_cow_preg_anal_finish with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_anal_finish with dissolve

    $ Pause()

    MC "H-Hrghhhhh...!"
    "Mrs Winward's eyes rolled back as she cooed and twitched feeling my cum fill up her ass."
    "As I poured out every last drop of the thick seed into her ass, she quivered and moaned softly, not saying a word as I slowly unsheathed my cock from her now loosened ass."
    "With a small {i}*pop!*{/i} sound, my cock pulled out of her quivering, winking asshole as my seed poured out of her gaping hole on the bed."
    MRS_WINWARD "A-Ahhh....!! {image=[ICON.HEART]}"
    MC "{i}*Huff*{/i} Are you alright, Mrs Winward?"
    MRS_WINWARD "M-Mhmmm...."
    "Mrs Winward simply quivered and moaned in response, some of my cum continued to seep out of her hole as she laid there motionless on the bed."
    MC "Thanks for letting me use your ass, Mrs Winward."
    MRS_WINWARD "A-Ahhhh...{image=[ICON.HEART]}"
    return

