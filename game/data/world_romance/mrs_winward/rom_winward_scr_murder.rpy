label rom_winward_murder_visit_at_graveyard:
    $ RomanceWinward().Murder_FirstGraveyardScene_SpokeAtGraveyardAboutNightScene = True
    $ NoteLock("RomWinward_MurderVisitAtGraveyard")
    $ CharSetClothes("mrs_winward", "funeral")
    show mrs_winward at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MC @talk "Mrs Winward?"
    MRS_WINWARD @shock "[player_name!t]?"
    MRS_WINWARD @sad "Why... Why are you here?"
    MC @talk "I came to check on you."
    MRS_WINWARD @sad "...He's just been buried about an hour ago."
    MRS_WINWARD @sad "No one came."
    MRS_WINWARD @sad "I'm not even sure if the letters arrived to our children in time..."
    MRS_WINWARD @sad "Or if they've received the letter and truly just don't care enough to bury him."
    MC @talk "It's a few days' travel; they may not have had the time to make the journey."
    MRS_WINWARD @sad "I know, it's just..."
    MRS_WINWARD @sad "He was never that good of a father, even back there."
    "Mrs Winward gritted her teeth bitterly."
    MRS_WINWARD @angry "Always too obsessed with the damn family name!"
    MC "..."
    MRS_WINWARD @sad "{i}*Sigh*{/i}"
    MRS_WINWARD @sad "I shouldn't speak ill of the dead; there's no point holding onto all that bitterness now he's gone."
    "There was a long pause shared between us; Mrs Winward's eyes met mine as her cheeks flushed red."
    "She took a step closer towards me once more."
    MRS_WINWARD @embarr "{i}...I haven't been able to stop thinking about you.{/i}"
    MRS_WINWARD @embarr "Even when he was being laid to rest, I-"
    "She clutched tightly at her clothes."
    show mrs_winward at center_f with easeinright
    MRS_WINWARD @embarr "{i}Miss you.{/i}"
    MRS_WINWARD @embarr "Oh gods, hearing an old lady pinning for you like that... You must think I'm pathetic."
    MC @sad "Mrs Winward-"
    if IsDaytime():
        MRS_WINWARD @sad "I ... I need to say goodbye properly."
        MRS_WINWARD @angry "Away from everyone else, away from having to pretend to still be the good wife."
        MRS_WINWARD @embarr "C-Could you come back here later tonight?"
        MC @think "You want me to come back to meet you at this graveyard after dark?"
        MRS_WINWARD @embarr "Y-Yes..."
        $ NoteUnlock("RomWinward_MurderVisitGraveyardAtNight")
        MRS_WINWARD @embarr "I'll need you for this part."
        MC @talk "Very well, I shall return this evening."
        MRS_WINWARD @embarr "T-Thank you..."
        $ RomanceWinward().Murder_FirstGraveyardScene_TriggerGraveyardEnterSexscene = True
        $ CharSetClothes("mrs_winward", "normal")
        $ LocEnter()

    else:
        MRS_WINWARD @embarr "C-Could you follow me, please?"
        MC @think "Okay, I guess..."
        jump rom_winward_murder_visit_at_graveyard_night_sexscene
    
label rom_winward_murder_visit_at_graveyard_dont:
    MC "(I should leave her be for now.)"
    $ LocEnterQ()

#######################################################################################################################################
label rom_winward_murder_visit_at_graveyard_night:
    $ RomanceWinward().Murder_FirstGraveyardScene_TriggerGraveyardEnterSexscene = False
    $ CharSetClothes("mrs_winward", "funeral")
    show mrs_winward at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MRS_WINWARD @embarr "Y-You came..."
    MRS_WINWARD @embarr "Are you ready?"
    menu rom_winward_murder_visit_at_graveyard_night_menu:
        "I am.":
            MRS_WINWARD @embarr "Mmm, good."
            MRS_WINWARD @embarr "This way then, dear."
            jump rom_winward_murder_visit_at_graveyard_night_sexscene

        "What is this about?":
            MRS_WINWARD @embarr "J-Just some things I needed to say to him."
            MRS_WINWARD @embarr "Away from everyone else."
            MC @think "And you need {i}me{/i} there for this?"
            MRS_WINWARD @embarr "Y-Yes..."
            jump rom_winward_murder_visit_at_graveyard_night_menu
        
label rom_winward_murder_visit_at_graveyard_night_sexscene:
    scene black with dissolve
    "It was a concise walk to Mr. Winward's grave; Mrs. Winward had placed a lit candle or two around it, along with a singular rose at the foot of the tombstone."
    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft
    with dissolve
    "With her hands clasped together, she nervously began."
    MRS_WINWARD @sad "I ... I know we've already said goodbye."
    MRS_WINWARD @sad "I know I cried and wept for days when you left me."
    MRS_WINWARD @sad "I-It's hard to move on after more than four decades of marriage..."
    MRS_WINWARD @sad "B-But I, I just want you to know, now that it's just the two of us."
    MRS_WINWARD @angry "{i}...I hate you.{/i}"
    MC @think "Uhh, Mrs Win-"
    MRS_WINWARD @angry "Even when times were good, you were a bastard."
    MRS_WINWARD @angry "Wealth... Power, you were a self-absorbed monster."
    "Mrs Winward suddenly began to unbutton the clasps on her clothes."
    MRS_WINWARD "And that's why..."
    MC "Mrs Winward?!"
    hide mrs_winward
    show cg_winward_funeral_tits at cright
    with dissolve
    "As she pulled out her huge tits and let them drop down, she bent forward, placing one hand on her husband's tombstone as she hiked up her dress with her other hand."
    MRS_WINWARD "I-It's important I remind myself I have {i}other{/i} things in my life now."
    "As she wiggled her bare ass towards me, I knew what she wanted."
    "Taking a cursory glance around for anyone watching, I quickly stepped up behind her."
    "With my cock pulled out, the cool night air lightly passed us by as I lightly rubbed my cock against her warm, soft ass."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if CharIsVisiblyPreg("mrs_winward"):
        scene mrs_winward_grave_preg_idle with dissolve
    else:
        scene mrs_winward_grave_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "Mhmmm..."
    MRS_WINWARD "I hope you're watching this, dear... Wherever you are."
    MRS_WINWARD "I want you to {i}see{/i} why I won't be crying over you anymore..."
    "As Mrs Winward lightly wiggled and pushed her immense ass up against me, swallowing my cock briefly in the crack, I could feel rubbed up against her just how wet she was becoming."
    "She tilted her head to look back towards me as she muttered,"
    MRS_WINWARD "I - I'm ready."
    MRS_WINWARD "{i}Put it in.{/i}"
    
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    if CharIsVisiblyPreg("mrs_winward"):
        scene mrs_winward_grave_preg_slow with dissolve
    else:
        scene mrs_winward_grave_nopreg_slow with dissolve
    $ Pause()

    "Doing as she asked, I first pressed the head of my cock against her wet slit, and as I pushed against her, she moaned softly as her lips spread and wrapped around my cock."
    MRS_WINWARD "Mhfghhh...!"
    MC "Are you okay?"
    MRS_WINWARD "I'm fine - {i}*Huff*{/i} Just... Put it in!"
    "Inch by inch, I pushed the rest of my cock into her warm insides."
    "At first, she gasped in a mixture of shock and surprise as she felt the large member push its way up into her."
    "She winced with pain, but as she squeezed around me, I slowly began to rock back and forth, gently fucking her."
    MRS_WINWARD "Oooooh!!"
    MRS_WINWARD "H-He's so big dear... Mfghh!"
    MRS_WINWARD "{i}So big.{/i}"
    "Gently, flesh collided as I slapped up against her butt, her ass jiggling with every thrust and impact."
    "She moaned softly, her huge breasts swinging like two huge church bells with every motion."
    MRS_WINWARD "Ahhh! Ahhh! Mmfghh!! {image=[ICON.HEART]}"
    "As her moans grew louder, once again, I took another quick cursory glance around for anyone who might be watching us."
    "Nothing... Nothing but the sounds of nighttime bugs going about their business as Mrs Winward pushed her fat ass back into me."
    MRS_WINWARD "H-Harder! Harder deary!"
    MRS_WINWARD "Mmfghhh! So good!"

    if CharIsVisiblyPreg("mrs_winward"):
        scene mrs_winward_grave_preg_fast with dissolve
    else:
        scene mrs_winward_grave_nopreg_fast with dissolve
    $ Pause()

    "Picking up the pace, I began to slam against her fat ass as she groaned hotly into the night."
    "Had the air warmed up suddenly? Or did her body feel so good that I no longer noticed the cool breeze?"
    "Her ass rippled with every thrust as I kneaded the fat between my fingertips as I squeezed her round butt."
    MRS_WINWARD "OOOOOOOOOH!! Y-Yes! That's it! Mhfghh! Just like that!"
    MRS_WINWARD "S-See dear? I'm going to - Ahh!"
    MRS_WINWARD "B-Be just fine without you!"
    MRS_WINWARD "F-Fuckkk! Ooooh!!"
    MC "Mrs Winward - {i}*Huff*{/i} We should - Ahh!"
    MC "Hurry up before someone sees us!"
    MRS_WINWARD "Ahh! Just - Mhhfghh! F-Fill me up whenever you're ready, dear!"
    MRS_WINWARD "F-Filling me up is {i}your{/i} job now, dear!"
    "Mrs Winward continued to sickly moan in pleasure, her knees trembling as I continued to thrust into her slick, wet, tight hole."
    "As our sweat glistened in the moonlight, I began to feel my balls rise as my cock tightened,"
    "The inevitable building sensation for release becoming increasingly unbearable with each passing thrust."
    MRS_WINWARD "Yes... Mhfghh! J-Just like that! Just like-"
    MRS_WINWARD "MMMFGHHHHH!! {image=[ICON.HEART]}"
    "As Mrs Winward's whole body shuddered and tightened around me, the sudden sensation was too much."
    "I grunted loudly as I spilled my load into her body; her mouth hung open as she gasped, feeling the thick seed fill her up."

    $ ReduceInfectionFromSex("mrs_winward")
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    if CharIsVisiblyPreg("mrs_winward"):
        $ UnlockGalFlag("mrs_winward", "grave", "preg")
        scene mrs_winward_grave_preg_finish with flash
    else:
        $ UnlockGalFlag("mrs_winward", "grave", "nopreg")
        scene mrs_winward_grave_nopreg_finish with flash
    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "grave")

    MC "H-HRGHHHH!"
    MRS_WINWARD "O-Oooooooooooooooooh!!"
    "As I poured out the last of my seed into her willing, eager body, I held her in my grasp tightly for a moment, letting the waves of pleasure pass by."
    "After a few moments, I slowly stumbled back, pulling my cock outside of her now well fucked hole."
    "As my seed ran down her legs onto the ground, Mrs Winward, as though a spell had been broken, quickly began to re-dress and recompose herself."
    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft
    with dissolve
    MRS_WINWARD @embarr "T-Thank you for that."
    MC @think "That was... {i}different.{/i}"
    MRS_WINWARD @blush "It was just what I needed, deary."
    MC @talk "So... What happens now?"
    MRS_WINWARD @blush "Now, I move on with my life properly."
    MRS_WINWARD @blush "Focus on getting things in order."
    MC @think "And we...?"
    MRS_WINWARD @lewd "{i}You can take me anytime you feel like it.{/i}"
    MRS_WINWARD @lewd "This body is all yours, fufu. {image=[ICON.HEART]}"
    MC @smile "Good to know."
    MRS_WINWARD @blush "Come by the store soon, we should... {i}continue where we left off before we were rudely interrupted last time.{/i}"
    MC @lewd "I'll be sure to visit soon."
    MRS_WINWARD @blush "...Oh, and I'll be visiting here every {b}Tuesa{/b} to make sure his grave is clean."
    MRS_WINWARD @lewd "If you were to stumble upon me while I was doing so... Well..."
    MRS_WINWARD @lewd "{i}You know I can't resist doing whatever you tell me.{/i}"
    MC @smile "...Need me to walk you home safe tonight?"
    MRS_WINWARD @lewd "I think that if you did, we both know exactly how that would end."
    MRS_WINWARD @laugh "And my poor heart can't take any more excitement for one night!"
    MC @smile "I see..."
    MC @lewd "How's your heart for tomorrow?"
    MRS_WINWARD @lewd "{i}Beating far too fast at the thought already...{/i}"
    MRS_WINWARD @laugh "Oh, shoo!"
    MRS_WINWARD @lewd "Before I do something, I regret..."
    scene black with dissolve
    $ RomanceWinward().Murder_FirstGraveyardScene_IsAtGraveyard = False
    $ RomanceWinward().Murder_FirstGraveyardScene_SpokeAtGraveyardAboutNightScene = False
    $ RomanceWinward().Murder_FirstGraveyardScene_TriggerGraveyardEnterSexscene = False
    $ RomanceWinward().Murder_FirstGraveyardScene_IsOver = True
    $ CharSetClothes("mrs_winward", "normal")
    $ AutoMus(True)
    $ LocSet("novaras_dist_house_south")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    MC @smile "(Well... That went well.)"
    $ NoteLock("RomWinward_MurderVisitGraveyardAtNight")
    BLACK "({i}She will prove a fine mate.{/i})"
    MC "(I guess I should head to the store again when I'm ready...)"
    hide mc with easeoutleft
    $ LocEnterQ()

label rom_winward_murder_rep_graveyard:
    $ RomanceWinward().Murder_RepGraveyardScene_IsAtGraveyard = False
    $ CharSetClothes("mrs_winward", "funeral")
    show mrs_winward at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MC @talk "Mrs Winward?"
    MRS_WINWARD @shock "[player_name!t]?"
    MRS_WINWARD @sad "What are you doing here again?"
    MC @talk "I wondered if you might be here..."
    MRS_WINWARD @sad "... I sometimes still like to visit."
    MRS_WINWARD @sad "Tell him what I've been up to."
    MRS_WINWARD @sad "Not sure why."
    MRS_WINWARD @sad "It's not like he'd have anything nice to say if he could answer back."
    MC "..."
    MRS_WINWARD @sad "{i}Sigh{/i}"
    "There was a long pause shared between us; Mrs Winward's eyes met mine as her cheeks flushed red."
    "She took a step closer towards me once more."
    MRS_WINWARD @embarr "I-"
    "She clutched tightly at her clothes."
    show mrs_winward at center_f with easeinright
    MRS_WINWARD @embarr "Could you help me forget all these memories once more... {i}like we did last time?{/i}"
    MC @sad "Mrs Winward-"
    scene black with dissolve
    "It was a concise walk to Mr. Winward's grave; Mrs. Winward had placed a lit candle or two around it, along with a singular rose at the foot of the tombstone."
    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft
    with dissolve
    "With her hands clasped together, she nervously began."
    MRS_WINWARD @sad "I ... I know we've already said goodbye."
    MRS_WINWARD @sad "I know I cried and wept for days when you left me."
    MRS_WINWARD @sad "I-It's hard to move on after more than four decades of marriage..."
    MRS_WINWARD @sad "B-But I, I just want you to know, now that it's just the two of us."
    MRS_WINWARD @angry "{i}...I hate you.{/i}"
    MRS_WINWARD @angry "Even when times were good, you were a bastard."
    MRS_WINWARD @angry "Wealth... Power, you were a self-absorbed monster."
    "Mrs Winward suddenly began to unbutton the clasps on her clothes."
    hide mrs_winward
    show cg_winward_funeral_tits at cright
    with dissolve
    "As she pulled out her huge tits and let them drop down, she bent forward, placing one hand on her husband's tombstone as she hiked up her dress with her other hand."
    MRS_WINWARD "I-It's important I remind myself I have {i}other{/i} things in my life now."
    "As she wiggled her bare ass towards me, I knew what she wanted."
    "Taking a cursory glance around for anyone watching, I quickly stepped up behind her."
    "With my cock pulled out, the cool air lightly passed us by as I lightly rubbed my cock against her warm, soft ass."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if CharIsVisiblyPreg("mrs_winward"):
        scene mrs_winward_grave_preg_idle with dissolve
    else:
        scene mrs_winward_grave_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "Mhmmm..."
    MRS_WINWARD "I hope you're watching this, dear... Wherever you are."
    MRS_WINWARD "I want you to {i}see{/i} why I won't be crying over you anymore..."
    "As Mrs Winward lightly wiggled and pushed her immense ass up against me, swallowing my cock briefly in the crack, I could feel rubbed up against her just how wet she was becoming."
    "She tilted her head to look back towards me as she muttered,"
    MRS_WINWARD "I - I'm ready."
    MRS_WINWARD "{i}Put it in.{/i}"
    
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    if CharIsVisiblyPreg("mrs_winward"):
        scene mrs_winward_grave_preg_slow with dissolve
    else:
        scene mrs_winward_grave_nopreg_slow with dissolve
    $ Pause()

    "Doing as she asked, I first pressed the head of my cock against her wet slit, and as I pushed against her, she moaned softly as her lips spread and wrapped around my cock."
    MRS_WINWARD "Mhfghhh...!"
    MC "Are you okay?"
    MRS_WINWARD "I'm fine - {i}*Huff*{/i} Just... Put it in!"
    "Inch by inch, I pushed the rest of my cock into her warm insides."
    "At first, she gasped in a mixture of shock and surprise as she felt the large member push its way up into her."
    "She winced with pain, but as she squeezed around me, I slowly began to rock back and forth, gently fucking her."
    MRS_WINWARD "Oooooh!!"
    MRS_WINWARD "H-He's so big dear... Mfghh!"
    MRS_WINWARD "{i}So big.{/i}"
    "Gently, flesh collided as I slapped up against her butt, her ass jiggling with every thrust and impact."
    "She moaned softly, her huge breasts swinging like two huge church bells with every motion."
    MRS_WINWARD "Ahhh! Ahhh! Mmfghh!! {image=[ICON.HEART]}"
    MRS_WINWARD "H-Harder! Harder deary!"
    MRS_WINWARD "Mmfghhh! So good!"

    if CharIsVisiblyPreg("mrs_winward"):
        scene mrs_winward_grave_preg_fast with dissolve
    else:
        scene mrs_winward_grave_nopreg_fast with dissolve
    $ Pause()

    "Picking up the pace, I began to slam against her fat ass as she groaned hotly."
    "Had the air warmed up suddenly? Or did her body feel so good that I no longer noticed the cool breeze?"
    "Her ass rippled with every thrust as I kneaded the fat between my fingertips as I squeezed her round butt."
    MRS_WINWARD "OOOOOOOOOH!! Y-Yes! That's it! Mhfghh! Just like that!"
    MRS_WINWARD "S-See dear? I'm going to - Ahh!"
    MRS_WINWARD "B-Be just fine without you!"
    MRS_WINWARD "F-Fuckkk! Ooooh!!"
    MC "Mrs Winward - {i}*Huff*{/i} We should - Ahh!"
    MC "Hurry up before someone sees us!"
    MRS_WINWARD "Ahh! Just - Mhhfghh! F-Fill me up whenever you're ready, dear!"
    MRS_WINWARD "F-Filling me up is {i}your{/i} job now, dear!"
    "Mrs Winward continued to sickly moan in pleasure, her knees trembling as I continued to thrust into her slick, wet, tight hole."
    "As our sweat glistened in the moonlight, I began to feel my balls rise as my cock tightened,"
    "The inevitable building sensation for release becoming increasingly unbearable with each passing thrust."
    MRS_WINWARD "Yes... Mhfghh! J-Just like that! Just like-"
    MRS_WINWARD "MMMFGHHHHH!! {image=[ICON.HEART]}"
    "As Mrs Winward's whole body shuddered and tightened around me, the sudden sensation was too much."
    "I grunted loudly as I spilled my load into her body; her mouth hung open as she gasped, feeling the thick seed fill her up."

    $ ReduceInfectionFromSex("mrs_winward")
    
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    if CharIsVisiblyPreg("mrs_winward"):
        $ UnlockGalFlag("mrs_winward", "grave", "preg")
        scene mrs_winward_grave_preg_finish with flash
    else:
        $ UnlockGalFlag("mrs_winward", "grave", "nopreg")
        scene mrs_winward_grave_nopreg_finish with flash
    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "grave")

    MC "H-HRGHHHH!"
    MRS_WINWARD "O-Oooooooooooooooooh!!"
    "As I poured out the last of my seed into her willing, eager body, I held her in my grasp tightly for a moment, letting the waves of pleasure pass by."
    "After a few moments, I slowly stumbled back, pulling my cock outside of her now well fucked hole."
    "As my seed ran down her legs onto the ground, Mrs Winward, as though a spell had been broken, quickly began to re-dress and recompose herself."
    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft
    with dissolve
    MRS_WINWARD @embarr "T-Thank you for that."
    MRS_WINWARD @blush "It was just what I needed, deary."
    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    $ AutoMus(True)
    $ LocSet("novaras_dist_house_south")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    MC @smile "(Well... That went well.)"
    $ RomanceWinward().Murder_RepGraveyardIsOver = True
    hide mc with easeoutleft
    $ LocEnterQ()

label rom_winward_murder_after_graveyard:
    $ RomanceWinward().Murder_SeenReturnFromGraveyardScene = True
    $ RomanceWinward().Murder_DoRepeatTuesaGraveVisits = True
    show mc at cleft with easeinleft
    MC @talk "Kionni? Are you here?"
    MRS_WINWARD "J-Just a moment!"
    show mrs_winward at cright_f with easeinright
    "From the back room, Kionni emerged and smiled sheepishly at me."
    MRS_WINWARD @embarr "H-Hello..."
    MC @think "Is everything okay?"
    MRS_WINWARD @embarr "Y-Yes... I've just been preparing myself for this moment, that is all."
    MRS_WINWARD @embarr "Sorry if I seem so nervous deary, it's been a long time since... You know."
    MC @smile "Ah... Why don't you get yourself ready, and I'll join you in the bedroom."
    "Mrs Winward sheepishly nodded."
    MRS_WINWARD @embarr "Y-Yes."
    "Before she left, Kionni shyly turned to face me again, biting her lower lip anxiously."
    MRS_WINWARD @embarr "Y-You won't laugh, will you?"
    MRS_WINWARD @embarr "If I ... wear that outfit again?"
    MC @lewd "No, Kionni, I {i}definitely{/i} won't laugh."
    MRS_WINWARD @embarr "A-Alright then, come up in five minutes."
    scene black with dissolve
    "As Mrs Winward hurried off towards her private room, I waited and allowed time to tick by for a couple minutes before I heard her voice softly calling." #brief fade to black
    MRS_WINWARD "You can come in now!"
    "Following her call, I headed into her bedroom."
    $ LocSet("novaras_tanner_shop_bedroom")
    $ CharSetClothes("mrs_winward", "cowl")
    $ LocFlush()
    show mrs_winward at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MC @talk "Kionni, are you-"
    MC @surprised "...!"
    MRS_WINWARD @blush "T-This cow looking for a new, big, {i}strong{/i} bull."
    MRS_WINWARD @lewd "D-Do you mind helping her out?"
    "Panting, the dark passenger pulsed beneath my skin as I felt my heart race and cock harden."
    MRS_WINWARD @shock "...Oh my, that's... That's quite a look you're giving me."
    MRS_WINWARD @lewd "Are you going to-"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene black with dissolve
    "I leapt onto Mrs Winward, pushing her down onto the bed."
    MRS_WINWARD "W-Whoa!"

    scene mrs_winward_missionary_solo_cow_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "(Oh gods! This is... This is really happening!)"
    "Mrs. Winward's eyes widened as she stared down at the massive appendage rubbing against her wet hole."
    "Pinned down at the wrists, I could feel her tremble with nervousness as her chest rose and fell in heavy, deep breaths."
    "Flushed red, she bit her lower lip, anticipating what was to come."
    MRS_WINWARD "P-Please, be gentle with your c-cow!"
    menu rom_winward_murder_after_graveyard_sexmenu:
        "Put it in her pussy.":
            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            scene mrs_winward_missionary_solo_cow_nopreg_vag_slow with dissolve
            $ Pause()

            "Gently, I pressed the head of my cock against Mrs Winward's tight, wet hole."
            "After some light prodding, her body opened to me, and gently, I slowly pushed inch by inch into her."
            MRS_WINWARD "M-Mmmmfghhhh!!"
            "Her body tightened and squeezed around me, and sensing shock, I paused for a brief moment."
            MRS_WINWARD "I'm f-fine, just... {i}continue.{/i}"
            "Slowly, I picked up the pace, gently fucking Mrs. Winward as I pushed my cock inch by inch deeper into her womanhood."
            "Soft, hot moans escaped her lips as she slowly became more comfortable with my size."
            MRS_WINWARD "Y-Yes, that's - Mhmm! Goooood!"
            MRS_WINWARD "Ahh! B-Breed your little cow!"
            MC "Is it better than your- ahh! Husbands ever was?"
            MRS_WINWARD "Ooooh! W-Why would you - Ahh! Make me say such - Mhmm! Cruel things?"
            MRS_WINWARD "H-He's dead, and you're - ooooh!"
            MRS_WINWARD "Isn't that enough?"
            MC "Because if you don't tell me, your {i}'bull'{/i} will stop."
            MRS_WINWARD "N-No! Don't stop! Mhmm!"
            MRS_WINWARD "Y-Yours! Your cock is so much - Mhmm! Better!"
            MRS_WINWARD "Better than his tiny pathetic cock ever was!"
            "Her words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth, turning her on all the more."
            "Her desperation for my cock only further excited me as I began to move faster."
            MRS_WINWARD "Oooh! D-Dear!"
            MRS_WINWARD "Mmfhghh!"

            scene mrs_winward_missionary_solo_cow_nopreg_vag_fast with dissolve
            $ Pause()

            "Now slamming my cock deeply into her hole, Mrs Winward gasped and moaned, sweat dripping from her body as she took me excitedly."
            MRS_WINWARD "OOOOOOOOOH!"
            MRS_WINWARD "Itshhh shooo ghoood!"
            MRS_WINWARD "S-Slow down! Mhmm! I can't - Ahhhh!"
            "Ignoring her pleas this time, I thrust deeply into Mrs Winward, reshaping her tight box to fit my needs."
            "As her grunts and moans grew louder, she trembled and shook beneath me, overwhelmed by waves of pleasure across her neglected body."
            "As her eyes began to roll up towards the ceiling, I felt her body melt as the last hints of nervous resistance flickered away."
            "Broken in, her mind overwhelmed, her perverse thoughts and words came tumbling out freely."
            MRS_WINWARD "{i}F-Fuck me!{/i}"
            MRS_WINWARD "Breed your little whore cow!{image=[ICON.HEART]}"
            "Slamming into her, the wetness of her now soaking cunt filled the room as she choked with pleasure."
            MRS_WINWARD "C-Cum in me!"
            MRS_WINWARD "{i}Fill your cow up!{/i}"
            "As my cock twitched and throbbed, I knew I couldn't hold on much longer."
            "Giving in to the overwhelming desire, I slammed my cock to the hilt and pushed her wrists harder down."
            "Grunting loudly, I poured my thick, heavy load into her tight womanhood."

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
            $ UnlockGalFlag("mrs_winward", "missionary", "vag")
            $ UnlockGalFlag("mrs_winward", "missionary", "cow")
            $ UnlockGalFlag("mrs_winward", "missionary", "solo")

            $ ReduceInfectionFromSex("mrs_winward")
            $ PregRoll("mrs_winward")
            scene mrs_winward_missionary_solo_cow_nopreg_vag_finish with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "missionary")

            MC "H-HRGHHHHH...!!"
            "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me, feeling the rush of warmth flood her womb."
            MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
            "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
            "She shuddered slightly as she felt some of my seed trickle in a steady stream out of her, panting hotly."
            MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
            MC "Ahhh...Are you alright, Mrs Winward?"
            MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
            MRS_WINWARD "Just need a little... A little..."
            "As Mrs Winward closed her eyes, she was soon drifting off asleep, snoring lightly as my cum continued to ooze from her well fucked hole."
            "Leaving her to rest, I slipped out of the store, locking the door behind me."
            $ LocSet("novaras_dist_house")
            $ LocFlush(dissolve)
            $ AutoMus(True)
            show mc at cright_f with easeinright
            BLACK "({i}Our new mate needs rest... Soon she shall be capable of siring us many young.{/i})"
            MC "(Are you sure about that? She's... quite old.)"
            BLACK "(Our species was built to procreate, by siring our young, her life-span will be extended in order to ensure our young are brought to fruition.)"
            MC "(...Wait, you mean she'll live longer if she has a child with us?)"
            BLACK "(This assessment is correct.)"
            MC "(But, can she even have children at her age?)"
            BLACK "(We were built to breed... This will not be an issue.)"
            MC "(...I see.)"
            hide mc with easeoutleft
            $ CharSetClothes("mrs_winward", "normal")
            $ LocEnterQ()

        "Put it in her ass.":
            "As I gently prodded the head of my cock against her tight asshole, Mrs Winward gasped in shock." #If the player tries to fuck her ass anyway
            MRS_WINWARD "N-Not there!"
            MRS_WINWARD "P-Please! I've never even had a finger back there!"
            MC "(Hmm... If I wanna fuck her tight rear, I'm going to near to help her practice loosen up back here.)"
            MC "(Perhaps there's something I can buy that will assist?)"
            if not QstIsActive(EventArlenaOrderButtplugForWinward) and not QstIsOver(EventArlenaOrderButtplugForWinward):
                $ QstStart(EventArlenaOrderButtplugForWinward)
            jump rom_winward_murder_after_graveyard_sexmenu

label rom_winward_murder_initiate_sex:
    MRS_WINWARD @blush "Is that so?"
    MRS_WINWARD @lewd "{i}And what did my bull have in mind?{/i}"
    MRS_WINWARD @lewd "Should I... dress appropriately?"
    menu:
        "No time, I need you {i}NOW.{/i}":
            MRS_WINWARD @shock "O-Oh!"
            MRS_WINWARD @lewd "{i}So eager... I love it.{/i}"
            MRS_WINWARD @blush "Now what, handsome?"
            pass

        "Yes, be a good little cow.":
            MRS_WINWARD @blush "Mmm... One moment dear."
            scene black with dissolve
            $ CharSetClothes("mrs_winward", "cowl")
            $ LocFlush(dissolve)
            show mrs_winward at center_f with dissolve
            MRS_WINWARD @lewd "Now what, handsome?"
            pass

        "Actually, I was thinking about us going to your bedroom tonight.":
            if IsCurWeekday(WEEKDAY_MON):
                MRS_WINWARD "Mmm, I'm afraid I cannot be with you tonight, [player_name!t]."
                MRS_WINWARD "I will be visiting my husband's grave."
                MC "Oh... I see."
            else:
                $ RomanceWinward().Murder_SetUpEveningScene = True
                $ NoteUnlock("RomWinward_SetUpEveningScene")
                MRS_WINWARD @lewd "Mmm, I'll make sure to prepare for whatever you've got in mind..."
            return

    menu rom_winward_murder_initiate_sex_menu:
        "How about a kiss?":
            MRS_WINWARD @lewd "Coming right up, handsome."
            hide mrs_winward
            if CharGetClothes("mrs_winward") == "normal":
                show cg_winward_kiss at center
            if CharGetClothes("mrs_winward") == "cowl":
                show cg_winward_kiss_cowl at center
            with dissolve
            MRS_WINWARD "Mhmmm... {image=[ICON.HEART]}"
            MRS_WINWARD "(His hands feel so strong...)"
            hide cg_winward_kiss
            hide cg_winward_kiss_cowl
            show mrs_winward at center_f
            with dissolve
            MRS_WINWARD @lewd "Oh my... That was nice."
            MRS_WINWARD @lewd "Now what, deary?"
            jump rom_winward_murder_initiate_sex_menu

        "I was thinking you could wrap those lips around my cock.":
            jump rom_winward_murder_rep_bj

        "I was thinking about pinning you up against the wall.":
            jump rom_winward_murder_rep_doggy_wall

label rom_winward_murder_rep_doggy_wall:
    MRS_WINWARD @lewd "You want me against the wall again, hmm?"
    MRS_WINWARD @think "W-Well, just make sure you don't take too long, dear."
    MRS_WINWARD @embarr "These old knees aren't what they used to be."

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if CharGetClothes("mrs_winward") == "cowl":
        if CharIsVisiblyPreg("mrs_winward"):
            scene mrs_winward_doggywall_cow_preg_idle_solo with dissolve
        else:
            scene mrs_winward_doggywall_cow_nopreg_idle_solo with dissolve

    if CharGetClothes("mrs_winward") == "normal":
        "As Mrs. Winward stepped towards me, she slid out of her clothes and turned around."
        if CharIsVisiblyPreg("mrs_winward"):
            scene mrs_winward_doggywall_nude_preg_idle_solo with dissolve
        else:
            scene mrs_winward_doggywall_nude_nopreg_idle_solo with dissolve
    $ Pause()

    "Mrs Winward moved towards the wall once again, pressing her hands against it as she pushed out her large, round ass for me."
    "Aligning myself behind Mrs. Winward's soft, large rump, she lightly rubbed her butt up against my manhood as she bit down on her lower lip."
    MRS_WINWARD "Is that big cock all for me, deary?"
    MRS_WINWARD "Fufu {image=[ICON.HEART]} Your cock is so wonderfully huge and thick dear, you might need to take it easy on me!"
    menu rom_winward_murder_rep_doggy_wall_sexmenu:
        "Try and put it in her ass":
            if RomanceWinward().UnlockedAnalSex:
                pass
            else:
                "As I gently prodded the head of my sword against her tight asshole, Mrs Winward gasped in shock." 
                MRS_WINWARD "N-Not there!"
                MRS_WINWARD "P-Please! I've never even had a finger back there!"
                MC "(Hmm... If I wanna fuck her tight rear, I'm going to need to help her practice and loosen up back here.)"
                MC "(Perhaps there's something I can buy that will assist?)"
                if not QstIsActive(EventArlenaOrderButtplugForWinward) and not QstIsOver(EventArlenaOrderButtplugForWinward):
                    $ QstStart(EventArlenaOrderButtplugForWinward)
                jump rom_winward_murder_rep_doggy_wall_sexmenu

            $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)

            if CharGetClothes("mrs_winward") == "cowl":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_doggywall_cow_preg_slow_solo with dissolve
                else:
                    scene mrs_winward_doggywall_cow_nopreg_slow_solo with dissolve

            if CharGetClothes("mrs_winward") == "normal":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_doggywall_nude_preg_slow_solo with dissolve
                else:
                    scene mrs_winward_doggywall_nude_nopreg_slow_solo with dissolve
            $ Pause()

            "Moving my cock slightly higher, I lightly prodded against her forbidden back door."
            MRS_WINWARD "{i}*Gasp!*{/i}"
            MRS_WINWARD "If... If you're going to try put it {i}there,{/i} p-please."
            MRS_WINWARD "Start slowly?"
            "Grabbing a fist full of her hair, she let out another short gasp as she felt the head of my cock sink into her tight, clutching asshole."
            MRS_WINWARD "A-AHHHH!!"
            "Slowly, I began to thrust my cock in and out of Mrs Winward's ass."
            "Her ass rippled with every thrust as I squeezed both hands on her round ass for better grip, feeling the fat slip between my fingers."
            MRS_WINWARD "M-MMFGHHH!"
            MRS_WINWARD "C-Careful! My - A-Ass! - Mhmm! You're so - Big!"
            MRS_WINWARD "I-It's burning from how much you're - ahhh! Stretching!"
            "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her forbidden back door."
            "As her now loosened asshole stretched and slowly grew more accustomed to my member, I began to move faster."
            "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
            MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
            MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"
            "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
            "I wondered what Mr Winward would think if he ever saw his wife with my cock stretching out her ass?"
            MC "Does Mr Winward get to fuck this hole?"
            MRS_WINWARD "M-Mhhfhhhgh!"
            MRS_WINWARD "M-My assshhh! - Hrghhh! You're - Ahh! Re-shaping all my insides!"
            MC "That doesn't answer the question!"
            MRS_WINWARD "A-Ahhh! N-No! He doesn't get to put it my ass!!"
            "Satisfied with her answer, I slammed my cock to the hilt, determined to claim this hole just for myself..."
            MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
            MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
            MRS_WINWARD "C-Cum already!"
            MRS_WINWARD "I don't know how much more my poor ass can - Ahh! Take!"
            "I continued to have my way with her for a little while longer, enjoying the feeling of her ass squeezing my member with desperation to bring me to climax."
            "Eventually, she got her wish."
            "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
            MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
            "Giving her what she wanted, I dug my hands deep into the soft flesh of her large, round ass and slammed deeply into her."
            "Grunting loudly, I flooded Mrs Winward's ass with my hot, thick seed."

            $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
            
            $ UnlockGalFlag("mrs_winward", "doggy_wall", "anal")
            $ UnlockGalFlag("mrs_winward", "doggy_wall", "no_cuck")
            
            $ ReduceInfectionFromSex("mrs_winward")

            if CharGetClothes("mrs_winward") == "cowl":
                $ UnlockGalFlag("mrs_winward", "doggy_wall", "cow")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "preg")
                    scene mrs_winward_doggywall_cow_preg_finish_solo with flash
                else:
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "nopreg")
                    scene mrs_winward_doggywall_cow_nopreg_finish_solo with flash

            if CharGetClothes("mrs_winward") == "normal":
                $ UnlockGalFlag("mrs_winward", "doggy_wall", "dress")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "preg")
                    scene mrs_winward_doggywall_nude_preg_finish_solo with flash
                else:
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "nopreg")
                    scene mrs_winward_doggywall_nude_nopreg_finish_solo with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "doggy_wall")

            MC "H-HRGHHHHH!!"
            "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
            "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
            "I held her up as I continued to pump my load into her now limp body."
            "Only a soft whimper escaped her lips as I held her body upright in my arms."
            MRS_WINWARD "M-Mhmmm..."
            MRS_WINWARD "Oh gods...That was..."
            MRS_WINWARD "...{i}Oh my...{/i}"
            "Slowly, As I unsheathed my cock from Mrs Winward's now loosened asshole, she shuddered as my seed spilled out of her onto the floor." 
            "Letting go of her hair, her legs shook and buckled as she slid down onto the floor in a puddle of our cum."
            "Catching her breath, I slowly helped her back to her feet as she sweatily looked towards me, brushing her now ruffled hair over her shoulder."
            "Licking her lips, she giggled."
            MRS_WINWARD @sad "{i}*Ow ow ow!*{/i}"
            MRS_WINWARD @embarr "I don't think I'm going to be able to sit down properly for a week after that!"
            MC @smile "Sorry, I couldn't control myself."
            "Mrs Winward pouted, playfully tapping at my chest."
            MRS_WINWARD @lewd "Do give me a little more forewarning next time you plan on putting something {i}there.{/i}"
            MC @lewd "Oh, so there {i}is{/i} a next time?"
            MRS_WINWARD @blush "I... {i}I didn't say that I didn't like it.{/i}"
            MRS_WINWARD @blush "Only that I needed a little more prep!"
            MC @smile "I see..."
            MRS_WINWARD @blush "G-Get home safe now, deary; I don't think I'll be able to keep standing much longer."
            MRS_WINWARD @lewd "These old bones need some rest after what you just put them through."
            MC @smile "I shall return soon, goodnight... Kionni."
            pass

        "Put it in her pussy":

            $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
            if CharGetClothes("mrs_winward") == "cowl":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_doggywall_cow_preg_slow_solo with dissolve
                else:
                    scene mrs_winward_doggywall_cow_nopreg_slow_solo with dissolve

            if CharGetClothes("mrs_winward") == "normal":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_doggywall_nude_preg_slow_solo with dissolve
                else:
                    scene mrs_winward_doggywall_nude_nopreg_slow_solo with dissolve
            $ Pause()

            "As her wetness brushed up against me along with her pubic hair, I knew what Mrs Winward needed, and I wasn't going to waste any time giving it to her!"
            "Grabbing her hair and pulling, she gasped as she felt my cock plunge deeply into her tight, wet hole."
            MRS_WINWARD "H-HMhmmffhhh!!"
            "Slowly, I began to thrust my cock in and out of Mrs Winward's pussy."
            "Her ass rippled with every thrust as I squeezed both hands on her round ass for better grip, feeling the fat slip between my fingers."
            MRS_WINWARD "D-Dear! Ahh!"
            MRS_WINWARD "You feel so - Mhmm! Big!"
            "Hot moans escaped Mrs Winward's lips as her legs began to tremble whilst my cock continued to plunge in and out of her tight clutching hole."
            "As her wet pussy grew more accustomed to my member, I began to move faster."
            "The sounds of sweet flesh colliding grew louder and more frequent as Mrs Winward's guttural moans filled the room."
            MRS_WINWARD "Ahh! Ahh! Mhmfghh! C-Careful! You're-"
            MRS_WINWARD "Oooooooooh!! {image=[ICON.HEART]}"

            if CharGetClothes("mrs_winward") == "cowl":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_doggywall_cow_preg_fast_solo with dissolve
                else:
                    scene mrs_winward_doggywall_cow_nopreg_fast_solo with dissolve

            if CharGetClothes("mrs_winward") == "normal":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_doggywall_nude_preg_fast_solo with dissolve
                else:
                    scene mrs_winward_doggywall_nude_nopreg_fast_solo with dissolve
            $ Pause()

            "Her sweet groans of pleasure became more frequent as I took Mrs Winward from behind."
            "I wondered what Mr Winward would have thought had he ever seen his wife's lewd expressions as she felt my cock fill her up properly?"
            MC "Have you ever been fucked this deeply, Mrs Winward?"
            MRS_WINWARD "M-Mhhfhhhgh!"
            MRS_WINWARD "I-It's like you're - Hrghhh! Re-shaping all my insides!"
            MC "That doesn't answer the question!"
            MRS_WINWARD "A-Ahhh! N-No! I've never even SEEN anyone bigger than you!"
            "Satisfied with her answer, I slammed my cock to the hilt, determined to fuck her senseless so she'd know for sure {i}who{/i} her body belonged to from now on..."
            MRS_WINWARD "M-MHHHHHHHHHFFFHH!"
            MRS_WINWARD "P-Please! {i}*Huff*{/i} Mhfghhh!"
            MRS_WINWARD "F-Fill me up!"
            MRS_WINWARD "I don't know how much more I can - Mhhhfhh! Take!"
            "I continued to have my way with her for a little while longer, enjoying the feeling of her pussy squeezing my member with desperation to bring me to climax."
            "Eventually, she got her wish."
            "As my balls began to tighten and rise, my cock, still plunging mercilessly in and out of her now trembling body, began to feel increasingly ready for release."
            MRS_WINWARD "{i}*Huff*{/i} F-Finish dear! {i}*Huff*{/i} I beg you! P-Please!!"
            "Giving her what she wanted, I dug my hands deep into the soft flesh of her large, round ass and slammed deeply into her."
            "Grunting loudly, I flooded Mrs Winward's womb with my hot, thick seed."

            $ UnlockGalFlag("mrs_winward", "doggy_wall", "no_cuck")
            $ UnlockGalFlag("mrs_winward", "doggy_wall", "vag")
            
            $ ReduceInfectionFromSex("mrs_winward")
            $ PregRoll("mrs_winward")
            $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")

            if CharGetClothes("mrs_winward") == "cowl":
                $ UnlockGalFlag("mrs_winward", "doggy_wall", "cow")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "preg")
                    scene mrs_winward_doggywall_cow_preg_finish_solo with flash
                else:
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "nopreg")
                    scene mrs_winward_doggywall_cow_nopreg_finish_solo with flash

            if CharGetClothes("mrs_winward") == "normal":
                $ UnlockGalFlag("mrs_winward", "doggy_wall", "dress")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "preg")
                    scene mrs_winward_doggywall_nude_preg_finish_solo with flash
                else:
                    $ UnlockGalFlag("mrs_winward", "doggy_wall", "nopreg")
                    scene mrs_winward_doggywall_nude_nopreg_finish_solo with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "doggy_wall")

            MC "H-HRGHHHHH!!"
            "Mrs Winward gasped as she felt the rush of warm fluid pouring into her."
            "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
            "I held her up as I continued to pump my load into her body."
            "Only a soft whimper escaped her lips as I held her body upright in my arms."
            MRS_WINWARD "M-Mhmmm..."
            MRS_WINWARD "Oh gods...That was..."
            MRS_WINWARD "...{i}Oh my...{/i}"
            "Slowly, As I unsheathed my cock from Mrs Winward's now loosened hole, she shuddered as my seed spilled out of her onto the floor." 
            "Letting go of her hair, her legs shook and buckled as she slid down onto the floor in a puddle of our cum."
            "Catching her breath, I slowly helped her back to her feet as she sweatily looked towards me, brushing her now ruffled hair over her shoulder."
            "Licking her lips, she giggled."
            MRS_WINWARD @lewd "{i}*Phew!*{/i}"
            MRS_WINWARD @lewd "You really put this old lady through her paces back there!"
            MRS_WINWARD @lewd "You always make it feel so... so..."
            "She giggled, playfully tapping at my chest."
            MC @smile "Good?"
            MRS_WINWARD @lewd "Mmmm, {i}incredible.{/i}"
            MRS_WINWARD @lewd "Come here tomorrow, {i}deary,{/i} I'm sure we all have so much to talk about now."
            MC @smile "I'm sure we will."
            "My smile melted her, and shyly, she giggled as she nervously looked away."
            MRS_WINWARD @blush "G-Get home safe now, deary; I don't think I'll be able to keep standing much longer."
            MRS_WINWARD @lewd "These old bones need some rest after what you just put them through."
            MC @smile "I shall return soon, goodnight... Kionni."
            pass

    scene black with dissolve
    $ AutoMus(True)
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    "With trembling legs, Mrs Winward saw me out, my cum still seeping out of her and running down her leg onto the floor as she did so."
    $ LocEnter()

label rom_winward_murder_visit_bedroom_miss:
    $ RomanceWinward().Murder_SetUpEveningScene = False
    $ NoteLock("RomWinward_SetUpEveningScene")

    show mrs_winward at cright_f with dissolve
    show mc at cleft with easeinleft
    MRS_WINWARD @lewd "Mmm, looks like my big {i}strong{/i} bull has come to empty his balls in his little cow again."
    MRS_WINWARD @lewd "Fufu {image=[ICON.HEART]}"
    MRS_WINWARD "Should I put on my... outfit, or?"
    menu:
        "Put on the cow outfit":
            show mrs_winward at nod
            $ CharSetClothes("mrs_winward", "cowl")
        "Just undress":
            show mrs_winward at nod
            $ CharSetClothes("mrs_winward", "naked")
    "Panting, the dark passenger pulsed beneath my skin as I felt my heart race and cock harden."
    MRS_WINWARD @shock "...Oh my..."
    MRS_WINWARD @lewd "T-There's that look again."
    MRS_WINWARD @blush "Are you going to-"
    show mc at center with easeinleft
    "I leapt onto Mrs Winward, pushing her down onto the bed."
    MRS_WINWARD "Ahh! Easy! {i}Easy!{/i}"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharGetClothes("mrs_winward") == "naked":
        if CharIsVisiblyPreg("mrs_winward"):
            scene mrs_winward_missionary_solo_naked_preg_idle with dissolve
        else:
            scene mrs_winward_missionary_solo_naked_nopreg_idle with dissolve
    else:
        if CharIsVisiblyPreg("mrs_winward"):
            scene mrs_winward_missionary_solo_cow_preg_idle with dissolve
        else:
            scene mrs_winward_missionary_solo_cow_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "Oooh! We have all night, dear! No need to hurry! Mhmm!"
    "Mrs. Winward's eyes widened as she stared down at the massive appendage rubbing against her wet hole."
    "Pinned down at the wrists, I could feel her tremble with nervousness as her chest rose and fell in heavy, deep breaths."
    "Flushed red, she bit her lower lip, anticipating what would come."
    MRS_WINWARD "A-Ah, start slow, dear... You know I have to get used to your size!"
    menu rom_winward_murder_visit_bedroom_miss_sexmenu:
        "Put it in her pussy.":
            
            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)

            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_naked_preg_vag_slow with dissolve
                else:
                    scene mrs_winward_missionary_solo_naked_nopreg_vag_slow with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_cow_preg_vag_slow with dissolve
                else:
                    scene mrs_winward_missionary_solo_cow_nopreg_vag_slow with dissolve

            $ Pause()

            "Gently, I pressed the head of my cock against Mrs Winward's tight, wet hole."
            "After some light prodding, her body opened to me, and gently, I slowly pushed inch by inch into her."
            MRS_WINWARD "M-Mmmmfghhhh!!"
            "Her body tightened and squeezed around me, and sensing shock, I paused for a brief moment."
            MRS_WINWARD "Ooooh, it's always even b-bigger than I remember! Mhmm!"
            "Slowly, I picked up the pace, gently fucking Mrs. Winward as I pushed my cock inch by inch deeper into her womanhood."
            "Soft, hot moans escaped her lips as she slowly became more comfortable with my size."
            MRS_WINWARD "Y-Yes, that's - Mhmm! Goooood!"
            MRS_WINWARD "Ahh! B-Breed your little cow!"
            MC "Tell me again whose you prefer!"
            MRS_WINWARD "Ooooh! Y-You make me say such - Ahh! Cruel things!"
            MRS_WINWARD "H-He's already gone, why do you - Ahh!"
            MC "Because if you don't tell me, your {i}'bull'{/i} will stop."
            MRS_WINWARD "Mhmmm... {image=[ICON.HEART]}"
            MRS_WINWARD "Y-Yours! Your cock is so much - Mhmm! Better!"
            MRS_WINWARD "His cock was worthless compared to yours!"
            MRS_WINWARD "Y-Your little cow needs breeding by a real man's cock!"
            "Her words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth, turning her on all the more."
            "Her desperation for my cock only further excited me as I began to move faster."
            MRS_WINWARD "Oooh! D-Dear!"
            MRS_WINWARD "Mmfhghh!"

            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_naked_preg_vag_fast with dissolve
                else:
                    scene mrs_winward_missionary_solo_naked_nopreg_vag_fast with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_cow_preg_vag_fast with dissolve
                else:
                    scene mrs_winward_missionary_solo_cow_nopreg_vag_fast with dissolve
            $ Pause()

            "Now slamming my cock deeply into her hole, Mrs Winward gasped and moaned, sweat dripping from her body as she took me excitedly."
            MRS_WINWARD "OOOOOOOOOH!"
            MRS_WINWARD "Itshhh shooo ghoood!"
            MRS_WINWARD "S-Slow down! Mhmm! I can't - Ahhhh!"
            "Ignoring her pleas this time, I thrust deeply into Mrs Winward, reshaping her tight box to fit my needs."
            "As her grunts and moans grew louder, she trembled and shook beneath me, overwhelmed by waves of pleasure across her neglected body."
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

            $ PregRoll("mrs_winward")
            $ ReduceInfectionFromSex("mrs_winward")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "solo")
            $ UnlockGalFlag("mrs_winward", "missionary", "vag")

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            if CharGetClothes("mrs_winward") == "naked":
                $ UnlockGalFlag("mrs_winward", "missionary", "naked")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                    scene mrs_winward_missionary_solo_naked_preg_vag_finish with dissolve
                else:
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
                    scene mrs_winward_missionary_solo_naked_nopreg_vag_finish with dissolve
            else:
                $ UnlockGalFlag("mrs_winward", "missionary", "cow")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                    scene mrs_winward_missionary_solo_cow_preg_vag_finish with dissolve
                else:
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
                    scene mrs_winward_missionary_solo_cow_nopreg_vag_finish with dissolve
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "missionary")

            MC "H-HRGHHHHH...!!"
            "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me, feeling the rush of warmth flood her womb."
            MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
            "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
            "She shuddered slightly as she felt some of my seed trickle in a steady stream out of her, panting hotly."
            MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
            MC "Ahhh...Are you alright, Mrs Winward?"
            MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
            MRS_WINWARD "Just need a little... A little..."
            "As Mrs Winward closed her eyes, she was soon drifting off asleep, snoring lightly as my cum continued to ooze from her well fucked hole."
            pass

        "Put it in her ass.":
            if RomanceWinward().UnlockedAnalSex:
                pass
            else:
                "As I gently prodded the head of my sword against her tight asshole, Mrs Winward gasped in shock." 
                MRS_WINWARD "N-Not there!"
                MRS_WINWARD "P-Please! I've never even had a finger back there!"
                MC "(Hmm... If I wanna fuck her tight rear, I'm going to need to help her practice and loosen up back here.)"
                MC "(Perhaps there's something I can buy that will assist?)"
                if not QstIsActive(EventArlenaOrderButtplugForWinward) and not QstIsOver(EventArlenaOrderButtplugForWinward):
                    $ QstStart(EventArlenaOrderButtplugForWinward)
                jump rom_winward_murder_visit_bedroom_miss_sexmenu

            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_naked_preg_anal_slow with dissolve
                else:
                    scene mrs_winward_missionary_solo_naked_nopreg_anal_slow with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
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
            MRS_WINWARD "A-Ahhh! It still - Mhmm! Feels like it burns, but-"
            MRS_WINWARD "Mhmm! My poor ass! It's starting to f-feel quite... Ooooh!"
            MRS_WINWARD "{i}N-Nice...{/i}"

            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_naked_preg_anal_fast with dissolve
                else:
                    scene mrs_winward_missionary_solo_naked_nopreg_anal_fast with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_cow_preg_anal_fast with dissolve
                else:
                    scene mrs_winward_missionary_solo_cow_nopreg_anal_fast with dissolve
            $ Pause()

            "Slowly, I began to pick up speed, ramming my cock into her incredibly tight, soft ass as Mrs. Winward's guttural moans grew louder and louder."
            MRS_WINWARD "Y-Yes! Pound my ass!"
            MRS_WINWARD "Mhmmfhh! You can have it whenever you want!"
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
            "The sudden, swift sensation overpowered me; my cock twitched in excitement as I felt my balls rise."
            "On the edge of release, I grunted to warn Mrs Winward."
            MC "{i}G-Gonna...!{/i}"
            MRS_WINWARD "{i}Do it! Fill my butt up!{/i} {image=[ICON.HEART]}"
            "Unable to hold back any longer, I buried my cock as deeply as I could into her rump, grunting loudly as I poured my hot seed into her bowels." #Cum
            $ ReduceInfectionFromSex("mrs_winward")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "solo")
            $ UnlockGalFlag("mrs_winward", "missionary", "anal")

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            if CharGetClothes("mrs_winward") == "naked":
                $ UnlockGalFlag("mrs_winward", "missionary", "naked")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                    scene mrs_winward_missionary_solo_naked_preg_anal_finish with dissolve
                else:
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
                    scene mrs_winward_missionary_solo_naked_nopreg_anal_finish with dissolve
            else:
                $ UnlockGalFlag("mrs_winward", "missionary", "cow")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                    scene mrs_winward_missionary_solo_cow_preg_anal_finish with dissolve
                else:
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
                    scene mrs_winward_missionary_solo_cow_nopreg_anal_finish with dissolve
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "missionary")
            MC "H-Hrghhhhh...!"
            "Mrs Winward's eyes rolled back as she cooed and twitched, feeling my cum fill up her ass."
            "As I poured out every last drop of the thick seed into her ass, she quivered and moaned softly, not saying a word as I slowly unsheathed my cock from her now loosened ass."
            "With a small {i}*pop!*{/i} sound, my cock pulled out of her quivering, winking asshole as my seed poured out of her gaping hole on the bed."
            MRS_WINWARD "A-Ahhh....!! {image=[ICON.HEART]}"
            MC "{i}*Huff*{/i} Are you alright, Mrs Winward?"
            MRS_WINWARD "M-Mhmmm...."
            "Mrs. Winward simply quivered and moaned in response; some of my cum continued to seep out of her hole as she laid there motionless on the bed."
            MC "Thanks for letting me use your ass, Mrs Winward."
            MRS_WINWARD "A-Ahhhh...{image=[ICON.HEART]}"
            pass

    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    $ AutoMus(True)
    "Leaving her to rest, I slipped out of the store, locking the door behind me."
    $ LocEnter()

label rom_winward_murder_rep_bj:
    MRS_WINWARD @lewd "Mhmm and I've missed feeling that fat monster wrapped around my lips."
    MRS_WINWARD @lewd "Come around here, deary, let me take care of that for you, fufu {image=[ICON.HEART]}"
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Following Mrs Winward around the back of the counter, she suddenly squatted down, scrambling to unbuckle my clothes with bated breath."
    "As she pulled out my cock, she licked her lips enticingly at the meal before her."
    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_solo_idle with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_solo_idle with dissolve
    $ Pause()
    MRS_WINWARD "Mhmm... {i}Such a big boy!{/i}"
    "Mrs Winward's cheeks flushed red as she smelt the thick, heavy member resting on her face, moaning softly as she did so."
    MC "Missed me?"
    MRS_WINWARD "You and your {i}wonderful{/i} cock. {image=[ICON.HEART]}"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_solo_slow with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_solo_slow with dissolve
    $ Pause()
    "Gently, her tongue slipped out her mouth to tenderly run along the shaft, and after she gently teased my cock, she took a deep breath and wrapped her lips around the head of my cock." #BJ behind the counter
    MRS_WINWARD "M-Mhmm!"
    MC "Mhmmff! That's it, Mrs Winward; all our time together is paying off, isn't it?"
    "Mrs Winward, embarrassed, didn't answer; instead, she glided her head back and forth slowly but steadily."
    "Her soft lips formed a tight seal around my cock as her tongue sheepishly wrapped and teased my member."
    "Her puffy stuffed cheeks were bright red as her eyes looked up pleadingly towards me, unsure if she was doing a good enough job pleasing me."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhmmfhh!"
    MRS_WINWARD "(I could just worship this cock all night!)"
    MRS_WINWARD "(The s-shame is - Mhmm! So hot! A woman of my age...)"
    MRS_WINWARD "({i}A-A newly made widow, fawning over some young man's cock!{/i})"
    "Suddenly, Mrs Winward groaned happily as she threw her head forward, pushing the cock deeper and deeper into her throat as she became enthralled in her task."
    MRS_WINWARD "(N-No, {i}I deserve this.){/i}"
    MRS_WINWARD "(Mhmm, it's not my f-fault; he's so much bigger than he was!)"
    MRS_WINWARD "(I j-just need someone to take care of my needs, {i}I'm sure he'd understand...{/i}"
    MRS_WINWARD "Fufufu! {image=[ICON.HEART]})"
    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_solo_fast with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()
    "As the minutes passed, more and more, Mrs Winward seemed enthralled and excited with what she was doing."
    MC "Ahh...! You're getting real good at sucking cock, Mrs Winward."
    "Mrs Winward shuddered with pleasure, moaning as she slammed her head forward in excitement, her glasses beginning to steam up."
    MRS_WINWARD "Mhhfhh!"
    "I pulled Mrs Winward's head forward, causing her to momentarily choke for a second from the sudden extra inch pressing down into her throat."
    "Incensed, Mrs Winward once again threw her head forward, surprising me with her sudden keenness as she wrapped her tongue lewdly around my cock."
    "The warm, wet sensation almost overpoweringly pleasant."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i}"
    MRS_WINWARD "*Slurp* {image=[ICON.HEART]}"
    "Mrs Winward suddenly pressed her head forward, taking my cock fully to the hilt and holding it there."
    "With defiant, fiery eyes, she looked up towards me, tongue thrashing furiously around my cock."
    "Grabbing a hold of Mrs Winward's head, I held her there; my balls tightened as I exploded into her mouth." #cum
    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    $ ReduceInfectionFromSex("mrs_winward")

    $ UnlockGalFlag("mrs_winward", "bj", "winward_gone")
    $ UnlockGalFlag("mrs_winward", "bj", "no_cuck")

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if CharGetClothes("mrs_winward") == "cowl":
        $ UnlockGalFlag("mrs_winward", "bj", "cow")
        scene mrs_winward_bj_cow_solo_finish with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        $ UnlockGalFlag("mrs_winward", "bj", "dress")
        scene mrs_winward_bj_dress_solo_finish with dissolve
    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "bj")
    MC "H-HRGHHHHH...!"
    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    "Finally, I released my tight grip on the back of Mrs Winward's head."
    "As she dragged her wet lips off from my cock, with a loud {i}*PLOP*{/i} she pulled her head away and gasped for air, a silvery trail of cum and saliva between her lips and my cock dissipated quickly to the ground between us."
    MRS_WINWARD "{i}*Huff*{/i} Oh my... {i}*Huff*{/i} Deary..."
    MRS_WINWARD "Looks like I might have to skip eating later! Fufu!"
    scene black with dissolve
    $ AutoMus(True)
    "As Mrs Winward rose back to her feet, she wiped her mouth with her hands and smiled shyly towards me again, hands clasped together." #End of sex scene
    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft
    with dissolve
    MRS_WINWARD @embarr "I've not had much experience outside of my husband, and n-never with one like yours."
    MRS_WINWARD @embarr "I hope that was good for you, dear."
    MC @lewd "That was very good."
    MRS_WINWARD @blush "Well then, now {i}my man{/i} has been satisfied, I best get back to work, shouldn't I?"
    "As she turned to leave, I playfully slapped at her round ass."
    MRS_WINWARD @shock "Oooh!"
    MRS_WINWARD @blush "Later, dear.{image=[ICON.HEART]}" 
    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    $ LocEnter()

label rom_winward_murder_impreg_first:
    show mc at cleft with easeinleft
    "Upon entering the store, a flustered Kionni hurried towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @scared "W-We need to talk."
    MC @think "What is it?"
    MRS_WINWARD @scared "I-"
    MRS_WINWARD @scared "I'm pregnant!"
    MC @surprised "You... You're what?!"
    MRS_WINWARD @shock "I couldn't believe it at first, it shouldn't be possible!"
    MRS_WINWARD @embarr "But I... I carry your child!"
    MC @think "Well... We knew this {i}could{/i} happen."
    MC @smile2 "I guess I'm just shocked, is all!"
    MRS_WINWARD @sad "I... Are you okay with this?"
    MRS_WINWARD @sad "I mean, having a child with a woman my age?"
    MC @smile "Your age is of no concern to me."
    MC @smile "In fact, I hope you're ready to carry a few more for me."
    MRS_WINWARD @shock "...O-Oh my...!"
    MRS_WINWARD @embarr "But, be serious! With my husband no longer around, I-"
    MRS_WINWARD @sad "I'm not sure I can afford to have this child!"
    MRS_WINWARD @sad "N-Nevermind the problems with my age!"
    MRS_WINWARD @sad "What if I die before they-"
    MC @talk "Don't worry, Kionni, I will make sure you and the child are looked after."
    MRS_WINWARD @sad "{i}*Sigh*{/i} I hope you're right..."
    MRS_WINWARD @sad "I best get back to my work."
    hide mrs_winward with easeoutleft
    "Mrs Winward slumped off to continue her tanning work."
    MC "(Hm... While it's not a problem for now, I'll need to put some thought into helping Kionni, especially now we're having a child together!)"
    $ LocEnter()

label rom_winward_murder_impreg_rep:
    show mc at cleft with easeinleft
    "Upon entering the store, a flustered Kionni hurried towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @scared "W-We need to talk."
    MC @think "What is it?"
    MRS_WINWARD @scared "I-"
    MRS_WINWARD @scared "I'm pregnant!"
    MC @surprised "{i}Again?{/i}"
    MRS_WINWARD @scared "{i}Oh gods, what are we going to do?{/i}"
    MC @think "Perhaps the church can offer some support if you explain the situation?"
    MC @talk "At least while I figure something out..."
    MRS_WINWARD @sad "{i}*Sigh*{/i} Yes, they might offer me some extra food at least."
    MRS_WINWARD @sad "I just hope things improve soon..."
    MRS_WINWARD @sad "I best get back to my work."
    hide mrs_winward with easeoutleft
    "Mrs Winward slumped off to continue her tanning work."
    MC "(Hm... While it's not a problem for now, I'll need to put some thought into helping Kionni, especially now we're having a child together!)"
    $ LocEnter()

label rom_winward_murder_birth_first:
    $ PregWinward().DoFirstBabyScene = False
    show mc at cleft with easeinleft
    "As I entered the store, Mrs Winward, clutching TWO small cutely gurgling babies wrapped in warm cloths, smiled towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @happy "Look, little ones."
    MRS_WINWARD @happy "{i}Father is here.{/i}"
    MC @surprised "Two?!"
    MC @surprised "Is that...?"
    MRS_WINWARD @happy "Who else could it be, dear?"
    MRS_WINWARD @laugh "Fufu, aren't they beautiful?"
    MRS_WINWARD @happy "What shall we call them?"
    $ PregWinward().BabyName1 = renpy.input(_("What names shall we call them?"), default = _("Rysa"))
    $ PregWinward().BabyName2 = renpy.input(_("...And?"), default = PregWinward().BabyName2Default)
    MRS_WINWARD "Hmm, good choices."
    MRS_WINWARD @happy "I'm gonna go put the little ones down for a nap."
    MC @smile "You seem happier today."
    MRS_WINWARD @blush "It's... a strange feeling, being a mother again."
    MRS_WINWARD "And seeing their cute faces did, in fact, wash away my fears for a moment at least..."
    MRS_WINWARD "I'm going to go lay the two of them down for a nap."
    MRS_WINWARD "Come by later, I'm sure we'll have lots to talk about."
    $ LocEnter()

label rom_winward_murder_birth_rep:
    show mc at cleft with easeinleft
    "As I entered the store, Mrs Winward, clutching TWO small cutely gurgling babies wrapped in warm cloths, smiled towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @happy "Look, little ones."
    MRS_WINWARD @happy "{i}Father is here.{/i}"
    MC @surprised "Two?!"
    MC @surprised "Is that...?"
    MRS_WINWARD @happy "Who else could it be, dear?"
    MRS_WINWARD @laugh "Fufu, aren't they beautiful?"
    MRS_WINWARD @happy "What shall we call them?"
    $ PregWinward().BabyName1 = renpy.input(_("What names shall we call them?"), default = PregWinward().BabyName1Default)
    $ PregWinward().BabyName2 = renpy.input(_("...And?"), default = PregWinward().BabyName2Default)
    MRS_WINWARD "Hmm, good choices."
    MRS_WINWARD @happy "I'm gonna go put the little ones down for a nap."
    MC @smile "You seem happier today."
    MRS_WINWARD @blush "It's... a strange feeling, being a mother again."
    MRS_WINWARD "And seeing their cute faces did, in fact, wash away my fears for a moment at least..."
    MRS_WINWARD "I'm going to go lay the two of them down for a nap."
    MRS_WINWARD "Come by later, I'm sure we'll have lots to talk about."
    $ LocEnter()

label rom_winward_murder_how_is_our_child:
    $ rng = renpy.random.randint(1, 2)
    if rng == 1:
        MRS_WINWARD @happy "Wonderful!"
        MRS_WINWARD @shock "I was worried about their health, but they seem so strong already!"
    if rng == 2:
        MRS_WINWARD @shock "They seem to never tire! I've never seen a child like them!" #variant 2
        MRS_WINWARD @think "Now that I think about it, ever since I got pregnant with them, I've felt stronger, and it's like I've had non-stop energy as well!"
        MRS_WINWARD @shock "Did you have something to do with that?"
    return