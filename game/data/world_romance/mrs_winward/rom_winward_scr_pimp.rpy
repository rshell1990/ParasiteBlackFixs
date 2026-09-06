label rom_winward_pimp_returnnextday:
    $ RomanceWinward().Pimp_SeenReturnNextDayScene = True
    $ NoteLock("RomWinward_VisitTomorrow")

    show mc at cleft with easeinleft

    MC  "Kionni? Are you here?"
    MRS_WINWARD "J-Just a moment!"

    show mrs_winward at cright_f with easeinright

    "From the back room, Kionni emerged and smiled sheepishly at me."
    MRS_WINWARD @embarr "H-Hello..."
    MC @think "Is everything okay?"
    MRS_WINWARD @embarr "Y-Yes... I've just been preparing myself for this moment is all."
    MRS_WINWARD @blush "Sorry if I seem so nervous deary, it's been a long time since... You know."
    MC @smile "Ah... Why don't you get yourself ready and I'll join you in the bedroom."
    "Mrs Winward sheepishly nodded."
    MRS_WINWARD @embarr "Y-Yes."
    "Before she left, Kionni shyly turned to face me once again, biting at her lower lip anxiously."
    MRS_WINWARD @embarr "Y-You won't laugh, will you?"
    MRS_WINWARD @embarr "If I ... wear that outfit again?"
    MC @lewd "No, Kionni, I {i}definitely{/i} won't laugh."
    MRS_WINWARD @embarr "A-Alright then, come up in five minutes."

    show mrs_winward at blurin, cright
    hide mrs_winward with easeoutright
    $ Pause(0.5)
    scene black with dissolve

    "As Mrs Winward hurried off towards her private room, I waited and allowed time to tick by for a couple minutes before I heard her voice softly calling." #brief fade to black
    MRS_WINWARD "You can come in now!"

    $ LocSet("novaras_tanner_shop_bedroom")

    "Following her call, I headed into her bedroom."

    $ CharSetClothes("mrs_winward", "cowl")
    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft with easeinleft

    MC  "Kionni, are you-"
    MC @surprised "...!"
    MRS_WINWARD @blush "T-This cow needs a big, {i}strong{/i} bull to fill in while her husband is away."
    MRS_WINWARD @lewd "D-Do you mind helping her out?"
    "Panting, the dark passenger pulsed beneath my skin as I felt my heart race and cock harden."
    MRS_WINWARD @shock "...Oh my, that's... That's quite a look you're giving me."
    MRS_WINWARD @blush "Are you going to-"

    show mc at center with easeinleft

    "I leapt onto Mrs Winward, pushing her down onto the bed."
    MRS_WINWARD "W-Whoa!"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene mrs_winward_missionary_solo_cow_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "(Oh gods! This is... This is really happening!)"
    "Mrs Winward's eyes widened as she stared down at the massive appendage rubbing against her wet hole,"
    "Pinned down at the wrists, I could feel her tremble with nervousness as her chest rose and fell in heavy deep breaths."
    "Flushed red, she bit down on her lower lip in anticipation of what was to come."
    MRS_WINWARD "P-Please, be gentle with your c-cow!"
    menu rom_winward_pimp_returnnextday_sexmenu:
        "Put it in her pussy.":
            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            scene mrs_winward_missionary_solo_cow_nopreg_vag_slow with dissolve
            $ Pause()

            "Gently, I pressed the head of my cock against Mrs Winward's tight, wet hole."
            "After some light prodding, her body opened to me, and gently, I slowly pushed inch by inch into her."
            MRS_WINWARD "M-Mmmmfghhhh!!"
            "Her body tightened and squeezed around me, and sensing shock, I paused for a brief moment."
            MRS_WINWARD "I'm f-fine, just... {i}continue.{/i}"
            "Slowly, I picked up pace, gently fucking Mrs Winward as I pushed my cock inch by inch deeper into her womanhood."
            "Soft, hot moans escaped her lips as she slowly became more comfortable with my size."
            MRS_WINWARD "Y-Yes, that's - Mhmm! Goooood!"
            MRS_WINWARD "Ahh! B-Breed your little cow!"
            MC "Is it better than your husband's?"
            MRS_WINWARD "Ooooh! W-Why would you - Ahh! Make me say such - Mhmm! Cruel things?"
            MC "Because if you don't tell me, your {i}'bull'{/i} will stop."
            MRS_WINWARD "N-No! Don't stop! Mhmm!"
            MRS_WINWARD "Y-Yours! Your cock is so much - Mhmm! Better!"
            "Her words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth turning her on all the more."
            "Her desperation for my cock only further excited me, as I began to move faster."
            MRS_WINWARD "Oooh! D-Dear!"
            MRS_WINWARD "Mmfhghh!"

            scene mrs_winward_missionary_solo_cow_nopreg_vag_fast with dissolve
            $ Pause()

            "Now slamming my cock deeply into her hole, Mrs Winward gasped and moaned, sweat dripping from her body as she took me excitedly."
            MRS_WINWARD "OOOOOOOOOH!"
            MRS_WINWARD "Itshhh shooo ghoood!"
            MRS_WINWARD "S-Slow down! Mhmm! I can't - Ahhhh!"
            "Ignoring her pleas this time, I thrust deeply into Mrs Winward, reshaping her tight box to fit my needs."
            "As her grunts and moans grew louder, she trembled and shook beneath me, overwhelmed by the waves of pleasure flowing across her neglected body."
            "As her eyes began to roll up towards the ceiling, I felt her body melt as the last hints of nervous resistance flickered away."
            "Broken in, her mind overwhelmed, her perverse thoughts and words came tumbling out freely."
            MRS_WINWARD "{i}F-Fuck me!{/i}"
            MRS_WINWARD "Breed your little whore cow!{image=[ICON.HEART]} "
            MRS_WINWARD "Show my loser husband how it's - Ahh! Done!"
            "Slamming into her, the wetness of her now soaking cunt filled the room as she choked with pleasure."
            MRS_WINWARD "C-Cum in me!"
            MRS_WINWARD "{i}Fill your cow up!{/i}"
            "As my cock twitched and throbbed, I knew I couldn't hold on much longer."
            "Giving in to the overwhelming desire, I slammed my cock to the hilt and pushed her wrists harder down."
            "Grunting loudly, I poured my thick, heavy load into her tight womanhood."

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "solo")
            $ UnlockGalFlag("mrs_winward", "missionary", "vag")
            $ UnlockGalFlag("mrs_winward", "missionary", "cow")
            $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")

            $ ReduceInfectionFromSex("mrs_winward")
            $ PregRoll("mrs_winward")
            scene mrs_winward_missionary_solo_cow_nopreg_vag_finish with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "missionary")

            MC "H-HRGHHHHH...!!"
            "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me feeling the rush of warmth flood her womb."
            MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
            "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
            "She shuddered slightly as she felt some of my seed trickle in a steady stream out of her, panting hotly."
            MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
            MC "Ahhh...Are you alright, Mrs Winward?"
            MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
            MRS_WINWARD "Just need a little... A little..."

            $ AutoMus(True)
            scene black with dissolve
            $ CharSetClothes("mrs_winward", "normal")

            "As Mrs Winward closed her eyes, she was soon drifting off to sleep, snoring lightly as my cum continued to ooze from her well fucked hole."
            "Leaving her to rest, I slipped out of the store, locking the door behind me."
            $ LocSet("novaras_dist_house")
            $ LocFlush(dissolve)
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
            $ LocEnterQ()

        "Put it in her ass.":
            "As I gently prodded the head of my sword against her tight asshole, Mrs Winward gasped in shock." #If player tries to fuck her ass anyway
            MRS_WINWARD "N-Not there!"
            MRS_WINWARD "P-Please! I've never even had a finger back there!"
            MC "(Hmm... If I wanna fuck her tight rear, I'm going to need to help her practice and loosen up back here.)"
            MC "(Perhaps there's something I can buy that will assist?)"
            if not QstIsActive(EventArlenaOrderButtplugForWinward) and not QstIsOver(EventArlenaOrderButtplugForWinward):
                $ QstStart(EventArlenaOrderButtplugForWinward)
            jump rom_winward_pimp_returnnextday_sexmenu

label rom_winward_pimp_initiate_sex:
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

        "I was thinking about us going to your bedroom tonight.":
            $ RomanceWinward().Pimp_SetUpEveningScene = True
            $ NoteUnlock("RomWinward_SetUpEveningScene")
            MRS_WINWARD @lewd "Mmm, I'll make sure to prepare for whatever you've got in mind..."
            return

    menu rom_winward_pimp_initiate_sex_menu:
        "How about a kiss?":
            MRS_WINWARD @lewd "Coming right up, handsome."

            hide mrs_winward
            if CharGetClothes("mrs_winward") == "normal":
                show cg_winward_kiss at center
            if CharGetClothes("mrs_winward") == "cowl":
                show cg_winward_kiss_cowl at center
            with dissolve

            MRS_WINWARD "Mhmmm...{image=[ICON.HEART]}"
            MRS_WINWARD "(His hands feel so strong...)"

            hide cg_winward_kiss
            hide cg_winward_kiss_cowl
            show mrs_winward at center_f
            with dissolve

            MRS_WINWARD @lewd "Oh my... That was nice."
            MRS_WINWARD @lewd "Now what, deary?"
            jump rom_winward_pimp_initiate_sex_menu

        "I was thinking you could wrap those lips around my cock.":
            jump rom_winward_pimp_rep_bj        
            
        "I was thinking about pinning you up against the wall.":
            jump rom_winward_pimp_rep_doggy_wall

label rom_winward_pimp_rep_doggy_wall:
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

    "Turning towards the wall, she pressed her hands against it as she pushed out her large, round ass for me."
    "Aligning myself behind Mrs Winwards soft, large rump, she lightly rubbed her butt up against my manhood as she bit down on her lower lip."
    MRS_WINWARD "Is that big cock all for me, deary?"
    MRS_WINWARD "Fufu {image=[ICON.HEART]} Your cock is so wonderfully huge and thick dear, you might need to take it easy on me!"
    menu rom_winward_pimp_rep_doggy_wall_sexmenu:
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
                jump rom_winward_pimp_rep_doggy_wall_sexmenu

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
            MRS_WINWARD "If... If you're going to try put and it {i}in there,{/i} p-please."
            MRS_WINWARD "Start slowly?"
            "Grabbing a fist full of her hair, she let out another short gasp as she felt the head of my cock sink into her tight, clutching asshole."
            MRS_WINWARD "A-AHHHH!!"
            "Slowly, I began to thrust my cock in and out of Mrs Winward's ass."
            "Her ass rippled with every thrust as I squeezed my free hand on her round ass for a better grip, feeling the fat slip between my fingers."
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
            "Giving her what she wanted, I dug my hand deep into the soft flesh of her large, round ass and slammed deeply into her."
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
            "Her eyes rolled back as she trembled and collapsed back into my arms."
            "I held her up as I continued to pump my load into her now limp body."
            "Only a soft whimper escaped her lips as I help her body upright in my arms."
            MRS_WINWARD "M-Mhmmm..."
            MRS_WINWARD "Oh gods...That was..."
            MRS_WINWARD "...{i}Oh my...{/i}"
            "Slowly, As I unsheathed my cock from Mrs Winward's now loosened asshole, she shuddered as my seed spilled out of her and onto the floor." 
            "Letting go of her hair, her legs shook and buckled as she slid down onto the floor in a puddle of our cum."
            "Catching her breath, I slowly helped her back to her feet as she sweatily looked towards me, brushing her now ruffled hair over her shoulder."
            "Licking her lips, she giggled."
            MRS_WINWARD @sad "{i}*Ow ow ow!*{/i}"
            MRS_WINWARD @embarr "I don't think I'm going to be able to sit down properly for a week after that!"
            MC @smile "Sorry, I couldn't control myself."
            "Mrs Winward pouted, playfully tapping at my chest."
            MRS_WINWARD @lewd "Do give me a little more forewarning next time you plan on putting something {i}there.{/i}"
            MC @lewd "Oh, so there {i}is{/i} a next time?"
            MRS_WINWARD @embarr "I... {i}I didn't say that I didn't like it.{/i}"
            MRS_WINWARD @blush "Only that I needed a little more prep!"
            MC @smile "I see..."
            MRS_WINWARD @blush "G-Get home safe now, deary, I don't think I'll be able to keep standing much longer."
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

            "As her wetness brushed up against me along with her pubic hair, I knew what Mrs Winward needed, and I wasn't going to waste anytime giving it to her!"
            "Grabbing her hair and pulling, she gasped as she felt my cock plunge deeply into her tight, wet hole."
            MRS_WINWARD "H-HMhmmffhhh!!"
            "Slowly, I began to thrust my cock in and out of Mrs Winward's pussy."
            "Her ass rippled with every thrust as I squeezed my free hand on her round ass for better grip, feeling the fat slip between my fingers."
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
            "I wondered what Mr Winward would think if he ever saw his wife's lewd expressions as she felt my cock fill her up properly?"
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
            "Giving her what she wanted, I dug my hand deep into the soft flesh of her large, round ass and slammed deeply into her."
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
            "Her eyes rolled back as she trembled and collapsed back into my arms."
            "I held her up as I continued to pump my load into her now limp body."
            "Only a soft whimper escaped her lips as I held her body upright in my arms."
            MRS_WINWARD "M-Mhmmm..."
            MRS_WINWARD "Oh gods...That was..."
            MRS_WINWARD "...{i}Oh my...{/i}"

            "Slowly, As I unsheathed my cock from Mrs Winward's now loosened hole, she shuddered as my seed spilled out of her and onto the floor." 
            "Letting go of her hair, her legs shook and buckled as she slid down onto the floor in a puddle of our cum."
            "Catching her breath, I slowly helped her back to her feet as she sweatily looked towards me, brushing her now ruffled hair over her shoulder."
            "Licking her lips, she giggled."
            MRS_WINWARD @lewd "{i}*Phew!*{/i}"
            MRS_WINWARD @lewd "You really put this old lady through her paces back there!"
            MRS_WINWARD @lewd "You always make it feel so... so..."
            "She giggled, playfully tapping at my chest."
            MC @smile "Good?"
            MRS_WINWARD @lewd "Mmmm, {i}incredible.{/i}"
            MRS_WINWARD @lewd "Come here tomorrow, {i}deary,{/i} I'm sure we will have so much to talk about now."
            MC @smile "I'm sure we will."
            "My smile melted her, and shyly, she giggled as she nervously looked away."
            MRS_WINWARD @blush "G-Get home safe now, deary, I don't think I'll be able to keep standing much longer."
            MRS_WINWARD @lewd "These old bones need some rest after what you just put them through."
            MC @smile "I shall return soon, goodnight... Kionni."
            pass

    scene black with dissolve
    $ AutoMus(True)
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    "With trembling legs, Mrs Winward saw me out, my cum still seeping out of her and running down her leg onto the floor as she did so."
    $ LocEnter()

label rom_winward_pimp_visit_bedroom_miss:
    $ RomanceWinward().Pimp_SetUpEveningScene = False
    $ NoteLock("RomWinward_SetUpEveningScene")

    show mrs_winward at cright_f with dissolve
    show mc at cleft with easeinleft
    MRS_WINWARD @lewd "Mmm, looks like my big {i}strong{/i} bull has come to empty his balls in his little cow again while her husband is away."
    MRS_WINWARD @lewd "Fufu {image=[ICON.HEART]}"
    "My eyes darted over towards Mr Winward, peacefully asleep."
    MRS_WINWARD @think "Oh, don't worry about {i}him.{/i}"
    MRS_WINWARD @happy "I just gave him some special tea... He won't bother us."
    MRS_WINWARD "Should I put on my... outfit, or?"
    menu:
        "Put on the cow outfit":
            show mrs_winward at nod
            $ CharSetClothes("mrs_winward", "cowl")
        "Just undress":
            show mrs_winward at nod
            $ CharSetClothes("mrs_winward", "naked")
    "Panting, I felt the dark passenger pulse beneath my skin as my heart raced and cock hardened."
    MRS_WINWARD @shock "...Oh my..."
    MRS_WINWARD @lewd "T-There's that look again."
    MRS_WINWARD @lewd "Are you going to-"
    show mc at center with easeinleft
    "I leapt onto Mrs Winward, pushing her down onto the bed."
    MRS_WINWARD "Ahh! Easy! {i}Easy!{/i}"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    if CharGetClothes("mrs_winward") == "naked":
        if CharIsVisiblyPreg("mrs_winward"):
            scene mrs_winward_missionary_oldmansleep_naked_preg_idle with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_naked_nopreg_idle with dissolve
    else:
        if CharIsVisiblyPreg("mrs_winward"):
            scene mrs_winward_missionary_oldmansleep_cow_preg_idle with dissolve
        else:
            scene mrs_winward_missionary_oldmansleep_cow_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "Oooh! We have all night dear! No need to hurry! Mhmm!"
    "Mrs Winward's eyes widened as she stared down at the massive appendage rubbing against her wet hole,"
    "Pinned down at the wrists, I could feel her tremble with nervousness as her chest rose and fell in heavy deep breaths."
    "Flushed red, she bit down on her lower lip in anticipation of what was to come."
    MRS_WINWARD "A-Ah, start slow dear... You know I have to get used to your size!"
    menu rom_winward_pimp_visit_bedroom_miss_sexmenu:
        "Put it in her pussy.":
            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)

            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_oldmansleep_naked_preg_vag_slow with dissolve
                else:
                    scene mrs_winward_missionary_oldmansleep_naked_nopreg_vag_slow with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
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
            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_oldmansleep_naked_preg_vag_fast with dissolve
                else:
                    scene mrs_winward_missionary_oldmansleep_naked_nopreg_vag_fast with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
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
            "Grunting loudly, I poured my thick, heavy load into her tight womanhood." #Cum

            $ PregRoll("mrs_winward")
            $ ReduceInfectionFromSex("mrs_winward")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "oldmansleep")
            $ UnlockGalFlag("mrs_winward", "missionary", "vag")

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            if CharGetClothes("mrs_winward") == "naked":
                $ UnlockGalFlag("mrs_winward", "missionary", "naked")
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_oldmansleep_naked_preg_vag_finish with dissolve
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                else:
                    scene mrs_winward_missionary_oldmansleep_naked_nopreg_vag_finish with dissolve
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
            else:
                $ UnlockGalFlag("mrs_winward", "missionary", "cow")
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_oldmansleep_cow_preg_vag_finish with dissolve
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                else:
                    scene mrs_winward_missionary_oldmansleep_cow_nopreg_vag_finish with dissolve
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "missionary")

            MC "H-HRGHHHHH...!!"
            "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me feeling the rush of warm fluid flood her womb."
            MRS_WINWARD "M-MMFGHHHHH...!! {image=[ICON.HEART]}" 
            "As I poured out the last of my seed into her body, I slowly unsheathed my cock from her now loosened hole."
            "She shuddered slightly as she felt some of my seed trickle in a steady stream out of her, panting hotly."
            MRS_WINWARD "Oh... {i}Oh m-my...{/i}"
            MC "Ahhh...Are you alright, Mrs Winward?"
            MRS_WINWARD "Y-Yes deary, I just... Mhmm... N-Need to close my eyes a little."
            MRS_WINWARD "Just need a little... A little..."
            "As Mrs Winward closed her eyes, she was soon drifting off to sleep, snoring lightly as my cum continued to ooze from her well fucked hole."
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
                jump rom_winward_pimp_visit_bedroom_miss_sexmenu

            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_oldmansleep_naked_preg_anal_slow with dissolve
                else:
                    scene mrs_winward_missionary_oldmansleep_naked_nopreg_anal_slow with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
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
            if CharGetClothes("mrs_winward") == "naked":
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_oldmansleep_naked_preg_anal_fast with dissolve
                else:
                    scene mrs_winward_missionary_oldmansleep_naked_nopreg_anal_fast with dissolve
            else:
                if CharIsVisiblyPreg("mrs_winward"):
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
            "Unable to hold back any longer, I buried my cock as deeply as I could into her rump, grunting loudly as I poured my hot seed into her bowels." #Cum
            $ ReduceInfectionFromSex("mrs_winward")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "oldmansleep")
            $ UnlockGalFlag("mrs_winward", "missionary", "anal")

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            if CharGetClothes("mrs_winward") == "naked":
                $ UnlockGalFlag("mrs_winward", "missionary", "naked")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                    scene mrs_winward_missionary_oldmansleep_naked_preg_anal_finish with dissolve
                else:
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
                    scene mrs_winward_missionary_oldmansleep_naked_nopreg_anal_finish with dissolve
            else:
                $ UnlockGalFlag("mrs_winward", "missionary", "cow")
                if CharIsVisiblyPreg("mrs_winward"):
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
                    scene mrs_winward_missionary_oldmansleep_cow_preg_anal_finish with dissolve
                else:
                    $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
                    scene mrs_winward_missionary_oldmansleep_cow_nopreg_anal_finish with dissolve
            $ Pause()
            $ UnlockGalSceneAndGrantXp("mrs_winward", "missionary")
            
            MC "H-Hrghhhhh...!"
            "Mrs Winward's eyes rolled back as she cooed and twitched feeling my cum fill up her ass."
            "As I poured out every last drop of the thick seed into her ass, she quivered and moaned softly, not saying a word as I slowly unsheathed my cock from her now loosened ass."
            "With a small {i}*pop!*{/i} sound, my cock pulled out of her quivering, winking asshole as my seed poured out of her gaping hole on the bed."
            MRS_WINWARD "A-Ahhh....!! {image=[ICON.HEART]}"
            MC "{i}*Huff*{/i} Are you alright, Mrs Winward?"
            MRS_WINWARD "M-Mhmmm...."
            "Mrs Winward simply quivered and moaned in response, some of my cum continued to seep out of her hole as she laid there motionless on the bed."
            MC "(I best leave before Mr Winward wakes up.)"
            MC "Thanks for letting me use your ass, Mrs Winward."
            MRS_WINWARD "A-Ahhhh...{image=[ICON.HEART]}"
            pass

    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    $ AutoMus(True)
    "Leaving her to rest, I slipped out of the store, locking the door behind me."
    $ LocEnter()

label rom_winward_pimp_rep_bj:
    MRS_WINWARD @lewd "Mhmm, and I've missed feeling that fat monster wrapped around my lips."
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
    "Gently, her tongue slipped out her mouth to tenderly run along the shaft, and after some gentle teasing, she took a deep breath, and wrapped her lips around the head of my cock." #BJ behind counter
    MRS_WINWARD "M-Mhmm!"
    MC "Mhmmff! That's it Mrs Winward, all our time together is really paying off, isn't it?"
    "Mrs Winward, embarrassed, didn't answer, instead, she began to glide her head back and forth in a slow but steady motion."
    "Her soft lips formed a tight seal around my cock as her tongue sheepishly wrapped and teased my member."
    "Her puffy stuffed cheeks were bright red as her eyes looked up pleadingly towards me, unsure if she was doing a good enough job at pleasing me."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhmmfhh!"
    MRS_WINWARD "(If only my husband was half as big as him.)"
    MRS_WINWARD "(I could just worship this cock all night!)"
    MRS_WINWARD "(The s-shame is - Mhmm! So hot! A woman of my age to be cheating on my... my...)"
    "Suddenly, Mrs Winward groaned happily as she threw her head forward, pushing the cock deeper and deeper into her throat as she became enthralled in her task."
    MRS_WINWARD "({i}P-Pathetic husband....!{/i})"
    MRS_WINWARD "(It's his fault for being such a fool! Mhmm, now a bigger, {i}better{/i} man is here to take care of my needs fufufu! {image=[ICON.HEART]})"
    MRS_WINWARD "(Thank the gods he's such a fool!)"

    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_solo_fast with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_solo_fast with dissolve
    $ Pause()

    "As the minutes passed, more and more, Mrs Winward seemed enthralled and excited with what she was doing."
    MC "Ahh...! You're getting real good at sucking cock, Mrs Winward."
    "Mrs Winward shuddered with pleasure, moaning as she slammed her head forward in excitement, her glasses beginning to steam up."
    MRS_WINWARD "Mhhfhh!"
    "Suddenly, the two of us heard the sounds of soft footsteps followed by the banging of a wooden cane on the floor as Mr Winward came down."
    MRS_WINWARD "(Urghh! Go away you old nuisance!)"
    MRS_WINWARD "(Not now! Not while I'm enjoying myself!)"
    MRS_WINWARD "Mhhfghh!"

    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_oldman_slow with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_oldman_slow with dissolve
    $ Pause()

    "I pulled Mrs Winward's head forward, letting her know she was to continue even with her husband standing there, causing her to momentarily choke for a second from the sudden extra inch pressing down into her throat."
    MR_WINWARD "You seen Kionni anywhere?"
    MC "No, can't say I - ahh! Have!"
    MR_WINWARD "She was supposed to have my dinner ready thirty minutes ago!"
    MC "Mhmm, was she?"
    MR_WINWARD "...You're fucking her too much! That's why she keeps forgetting things! She's too bloody tired!"
    MC "Ahh! You can't - Mhmm! Seriously be blaming me for that!"
    MRS_WINWARD "({i}Get between me and this cock you old grumpy bastard and you can forget about dinner altogether!{/i})"
    "Incensed, Mrs Winward once again threw her head forward, surprising me with her sudden keenness as she wrapped her tongue lewdly around my cock."
    "The warm, wet sensation almost overpoweringly pleasant."
    MC "I think she's - Ahh! Just busy recently with how the shop is doing!"
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i}"
    MR_WINWARD "What's that sound?"
    MC "Hm? N-No idea, probably came from outside."
    MRS_WINWARD "*Slurp* {image=[ICON.HEART]}"
    MR_WINWARD "..."
    MR_WINWARD "Why are you standing behind that counter?"

    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_oldman_fast with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_oldman_fast with dissolve
    $ Pause()

    MC "Oh, uh, Mrs Winward said she'd be right back and to just stand behind the - Ah! Counter till she gets back!"
    MR_WINWARD "I thought you said you hadn't seen her?"
    MC "My - Ah! Mistake, I meant she'll be back shortly!"
    MR_WINWARD "Hmph! Typical bloody woman!"
    MR_WINWARD "Always thinking about herself and forgetting everyone else!"
    "Mrs Winward suddenly pressed her head forward, taking my cock fully to the hilt and holding it there."
    "With defiant, fiery eyes she looked up towards me, tongue thrashing furiously around my cock."
    "With her eyes she told me clearly, {i}'You're going to cum down my throat in front of my prick of a husband, whether you like it or not now!{/i}"

    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_bj_cow_oldman_fast with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        scene mrs_winward_bj_dress_oldman_fast with dissolve
    $ Pause()

    "As Mr Winward turned to leave, grumbling under his breath, I grabbed a hold of Mrs Winward's head and held her there, my balls tightened as I exploded into her mouth." #cum
    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    MC "H-HRGHHHHH...!"

    $ ReduceInfectionFromSex("mrs_winward")

    $ UnlockGalFlag("mrs_winward", "bj", "winward_watches")
    $ UnlockGalFlag("mrs_winward", "bj", "no_cuck")

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if CharGetClothes("mrs_winward") == "cowl":
        $ UnlockGalFlag("mrs_winward", "bj", "cow")
        scene mrs_winward_bj_cow_oldman_finish with dissolve
    if CharGetClothes("mrs_winward") == "normal":
        $ UnlockGalFlag("mrs_winward", "bj", "dress")
        scene mrs_winward_bj_dress_oldman_finish with dissolve
    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "bj")

    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    MR_WINWARD "Huh? You say something boy?"
    MC "N-No, Mr Winward! Have a - Ahh! Nice day!"
    MR_WINWARD "Bah!"
    "As Mr Winward left, slamming the door behind him, finally, I released my tight grip on the back of Mrs Winward's head."
    "As she dragged her wet lips off from my cock, with a loud {i}*PLOP*{/i} she pulled her head away and gasped for air, a silvery trail of cum and saliva between her lips and my cock dissipiated quickly to the ground between us."
    MRS_WINWARD "{i}*Huff*{/i} Oh my... {i}*Huff*{/i} Deary..."
    MRS_WINWARD "Looks like I might have to skip eating later! Fufu!"

    scene black with dissolve
    $ AutoMus(True)

    "As Mrs Winward rose back to her feet, she wiped her mouth with her hands and smiled shyly towards me once again, hands clasped together." #End of sex scene

    $ LocFlush()
    show mrs_winward at cright_f
    show mc at cleft
    with dissolve

    MRS_WINWARD @embarr "I've not had much experience outside of my husband, and n-never with one like yours."
    MRS_WINWARD @blush "I hope that was good for you dear."
    MC @lewd "That was very good."
    MRS_WINWARD @happy "Well then, now {i}my man{/i} has been satisfied, I best get back to work, hadn't I?"
    "As she turned to leave, I playfully slapped at her round ass."
    MRS_WINWARD @shock "Oooh!"
    MRS_WINWARD @blush "Later dear.{image=[ICON.HEART]}" 
    
    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    "Leaving her to rest, I slipped out of the store, locking the door behind me."
    $ LocSet("novaras_dist_house")
    $ LocEnter()

label rom_winward_pimp_first_impreg:
    show mc at cleft with easeinleft
    "Upon entering the store, a flustered Kionni hurried towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @scared "W-We need to talk."
    MC @think "What is it?"
    MRS_WINWARD @scared "I-"
    show mr_winward at right_f with easeinright
    MR_WINWARD "She's carrying a child!"
    "Startled, Mrs Winward turned as a scowling Mr Winward hobbled his way over."
    MC @think "...Is it mine?"
    MRS_WINWARD @embarr "Y-Yes, I believe so."
    MRS_WINWARD @sad "I used red moon when dealing with clients, but I ..."
    MRS_WINWARD @sad "{i}S-Sometimes forget to take it when I'm with you.{/i}"
    MR_WINWARD @angry "Un-bloody-believeable..."
    MR_WINWARD @angry "Are you seriously telling me you were fucked so senseless you forgot to take it with him?"
    "Mrs Winward's cheeks burned bright red."
    MRS_WINWARD @shock "I - I never even took it as a serious precaution! Bearing a child at my age shouldn't be possible!"
    MR_WINWARD @think "It doesn't matter whether you think it should be possible."
    MR_WINWARD "You're pregnant, there's no changing that."
    MR_WINWARD "The good news is, though, we can make this work."
    MRS_WINWARD @shock "H-How...?"
    MR_WINWARD "I shall claim the child is a blessing from the gods, and thankfully, it's good to have a spare child in case anything happens to our son."
    MRS_WINWARD @shock "Don't even say such a thing!"
    MR_WINWARD @angry "I'm not hoping anything will happen!"
    MR_WINWARD @angry "But we can't pretend our boy isn't at war... Having a backup line to inherit everything is a smart idea."
    MRS_WINWARD @angry "How do you make everything sound so cold?"
    MR_WINWARD @angry "My dear... I'm literally tolerating you carrying another man's child right now."
    MR_WINWARD @think "By all rights, I could just throw you out."
    MRS_WINWARD @sad "I... Yes."
    MRS_WINWARD @sad "I don't suppose anyone would bat an eye if you did at this point."
    MR_WINWARD "Now then, as long as we're clear that this child is {i}mine{/i} should anyone ask, I'll consider the matter resolved."
    "Mr Winward made his way towards the door."
    MRS_WINWARD @shock "W-Wait!"
    MRS_WINWARD @think "That's it? You have nothing else to add?"
    MR_WINWARD "Yes."
    MR_WINWARD "Next time, be more careful when you let him spunk in you!"
    show mr_winward at blurin, right_f
    hide mr_winward with easeoutright
    "Mr. Winward closed the door abruptly behind him."
    MRS_WINWARD @sad "I... Are you okay with this?"
    MRS_WINWARD @sad "I mean, having a child with a woman my age?"
    MC @smile "Your age is of no concern to me."
    MC @smile "In fact, I hope you're ready to carry a few more for me."
    MRS_WINWARD @shock "...O-Oh my...!"
    MRS_WINWARD @embarr "I - Umm, I best get back to my work!"
    hide mrs_winward with easeoutleft
    "Embarrassed, Mrs Winward quickly returned to continue her tanning work."
    MC "(I should stop by from time to time to check in on how the child is doing.)"
    $ LocEnter()

label rom_winward_pimp_rep_impreg:
    show mc at cleft with easeinleft
    "Upon entering the store, a flustered Kionni hurried towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @embarr "D-Dear..."
    MRS_WINWARD @embarr "Ummm..."
    MC @think "What is it?"
    "Mrs Winward gently rubbed at her belly."
    MRS_WINWARD @embarr "We did it again, dear."
    MRS_WINWARD @embarr "I'm pregnant once more."
    show mr_winward at right_f with easeinright
    MC @think "Are you sure it's...mine?"
    MRS_WINWARD @embarr "Y-Yes, I'm certain."
    MRS_WINWARD @embarr "I continue to take the red moon with clients."
    MRS_WINWARD @think "It's... Only with you, I forget to take the red moon."
    MR_WINWARD "Do you even try? Or can your brain not even think of anything else once a cock is in you?"
    "Mr Winward hobbled his way over."
    MR_WINWARD @angry "You fucking put ya child in her again, ya bloody fool!"
    MRS_WINWARD @embarr "D-Dear, please."
    MRS_WINWARD @embarr "We can't help how passionate and... {i}fertile{/i} he is."
    MR_WINWARD @think "{i}*Sigh*{/i} Well, nothing has changed."
    MR_WINWARD "As long as we're clear that this child is {i}mine{/i} should anyone ask, let us consider this matter resolved."
    "Mr Winward made his way towards the door."
    MR_WINWARD "If you're going to keep having more of the sprogs drop from between your legs, you better start having them help you out with your work when they can."
    MR_WINWARD "More mouths to feed equals more bills!"
    show mr_winward at blurin, right_f
    hide mr_winward with easeoutright
    "Mr. Winward closed the door abruptly behind him."
    MRS_WINWARD @angry "I swear all that man thinks about is coin!"
    MC @smile "And what do {i}you{/i} think about, Mrs Winward?"
    MRS_WINWARD @lewd "Oh, I think you know deary."
    MRS_WINWARD @blush "I best get back to work for now, but there'll be plenty of time for us to catch up later."
    MC @lewd "I look forward to it."
    hide mrs_winward with easeoutleft
    "Kionni licked her lips as she hurried off to continue her tanning work."
    "She made sure to wiggle her hips slightly as she left, her fat ass making my cock twitch in excitement for what was to come."
    BLACK "({i}This mate is pleasing. She is keen to sire more of our young.{/i})"
    MC "(I should stop by from time to time to check in on how the child is doing.)"
    $ LocEnter()

label rom_winward_pimp_first_birth:
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
    $ PregWinward().BabyName1 = renpy.input(_("What names shall we call them?"), default = PregWinward().BabyName1Default)
    $ PregWinward().BabyName2 = renpy.input(_("...And?"), default = PregWinward().BabyName2Default)
    MRS_WINWARD "Hmm, good choices."
    MRS_WINWARD @happy "I'm gonna go put the little ones down for a nap."
    MRS_WINWARD @blush "Perhaps after we could..."
    MRS_WINWARD @lewd "{i}Work on giving them another little sister or brother?{/i}"
    $ LocEnter()

label rom_winward_pimp_rep_birth:
    show mc at cleft with easeinleft
    "As I entered the store, Mrs Winward, clutching two small cutely gurgling babies wrapped in warm cloths, smiled towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @happy "Look, little ones."
    MRS_WINWARD @happy "{i}Father is here.{/i}"
    MC @surprised "Twins...{i}again{/i}?"
    MRS_WINWARD @blush "Well, you know, my great-grandmother had twins, fufu."
    MRS_WINWARD @laugh "Fufu, aren't they beautiful?"
    MRS_WINWARD @happy "What shall we call them?"
    $ PregWinward().BabyName1 = renpy.input(_("What names shall we call them?"), default = _("Rysa"))
    $ PregWinward().BabyName2 = renpy.input(_("...And?"), default = PregWinward().BabyName2Default)
    MRS_WINWARD "Hmm, I like it."
    MRS_WINWARD @happy "I'm gonna put the little one down for a nap."
    MRS_WINWARD @blush "Perhaps after we could..."
    MRS_WINWARD @lewd "{i}Work on potentially giving them a little sister or brother?{/i}"
    $ LocEnter()

label rom_winward_pimp_how_is_our_child:
    $ rng = renpy.random.randint(1, 2)
    if rng == 1:
        MRS_WINWARD @happy "Wonderful!"
        MRS_WINWARD @shock "I was worried about their health, but they seem so strong already!"
    if rng == 2:
        MRS_WINWARD @shock "They seem to never tire! I've never seen a child like them!"
        MRS_WINWARD @think "Now that I think about, ever since I got pregnant with them, I've felt stronger myself, and it's like I've had non-stop energy as well!"
        MRS_WINWARD @shock "Did you have something to do with that?"
    return

##################################################
label dialogue_mr_winward_pimp_howareyou:
    MR_WINWARD @think "Hm?"
    MR_WINWARD @happy "Well, my pockets sure are deeper! Heeheeee!"
    MR_WINWARD @angry "Though must admit, having to listen to that slut's moans all the damn time now."
    return

label dialogue_mr_winward_pimp_discusswife:
    MR_WINWARD @think "What's there to discuss?"
    MR_WINWARD "You getting tired of her fat ass?"
    MC @talk "Well, no?"
    MR_WINWARD "You making each other miserable?"
    MC @think "Not as far as I'm aware."
    MR_WINWARD "Ain't nothing to discuss then, is there?"
    MR_WINWARD "She's been a lot calmer these last few days since you showed up, and I don't see a reason to start changing this little 'arrangement' now."
    return

label dialogue_mr_winward_pimp_cut:
    if GetGameDay() >= RomanceWinward().Pimp_DayPlayerCanGetHisCut:
        MR_WINWARD "Hm? Oh, here."
        $ PlayerAddItem("gold", renpy.random.randint(300, 500))
        "Grabbing a small bag of coins from a nearby shelf, Mr Winward handed it to me."
        MR_WINWARD "Ere' come back in a fortnight for your next cut."
        $ RomanceWinward().Pimp_DayPlayerCanGetHisCut = GetGameDay() + 14
    else:
        MR_WINWARD @angry "Settle down, would ya?"
        MR_WINWARD @angry "Come back another time; Kionni hasn't had time to earn that much yet!"
    return

label rom_winward_pimp_double_hj:
    show mc at cleft with easeinleft
    "While wandering through the brothel district, I heard a distinctively familiar, mature voice playfully chastising some people down one of the many winding alleyways."
    MRS_WINWARD "Fufu, you're all so impatient! {image=[ICON.HEART]}"
    menu:
        "Investigate the sounds.":
            pass

        "Ignore it.":
            "Ignoring the sounds, I decided it was best to simply walk on."
            hide mc with easeoutright
            $ LocEnterQ()

    "She was..."
    $ tmpvar = {}
    menu:
        "Wearing her lingerie.":
            "Dressed in that cow-pattern clothes she had fashioned for herself, the young 'clients' seemed to love it."
            $ tmpvar = "cow"
        "Exposed completely!":
            "Completely naked and exposed to her young, grinning 'clients' who seemed enthralled by her."
            $ tmpvar = "nude"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    
    if tmpvar == "cow":
        scene mrs_winward_pimp_doublehj_cow_slow with dissolve
    if tmpvar == "nude":
        scene mrs_winward_pimp_doublehj_nude_slow with dissolve
    $ Pause()

    "As I peered around the corner, Mrs Winward was on her knees grinning from ear to ear with her huge breasts exposed as she stroked at two cocks."
    "The third cock was all but consumed by her colossal tits, which the young man held and pressed together."
    
    YOUNG_MAN "Ahh! Gods! Your tits are so - Ahh! Soft but heavy!"
    MRS_WINWARD "Oooh, I'm sure a big, {i}strong{/i} young lad like yourself will be fine!"
    "Mrs Winward laughed as she continued to stroke the other two young men's cocks."
    
    TALL_YOUNG_MAN "Uhh, M-Mrs, when can we - Ahh!"
    TALL_YOUNG_MAN "Y-You know... {i}Go all the way?{/i}"
    MRS_WINWARD "Now, now, boys."
    MRS_WINWARD "We have to work up to that!"
    
    THIN_YOUNG_MAN "But - Ahh! We're all dying to"
    MRS_WINWARD "Shhh, just let me work my magic and drain your big, silly cocks, dry, boys."
    if tmpvar == "cow":
        scene mrs_winward_pimp_doublehj_cow_fast with dissolve
    if tmpvar == "nude":
        scene mrs_winward_pimp_doublehj_nude_fast with dissolve
    $ Pause()
    "Mrs. Winward continued to stroke the two boys' cocks, who groaned happily, whilst the third continued to lewdly thrust and fuck Mrs. Winward's huge tits, which glistened in the light thanks to some lube she must have used."
    YOUNG_MAN "A-Ahh! Your breasts feel so nice!"
    YOUNG_MAN "Mhhfhh! I-I'm really close, Mrs!"
    TALL_YOUNG_MAN "M-Me too!"
    THIN_YOUNG_MAN "Ahhh! L-Let me finish! Please!"
    MRS_WINWARD "Oooh? Already?"
    MRS_WINWARD "Fufu, you boys will need more practice if you're going to please your lady friends!"
    YOUNG_MAN "M-Mhhfhh! P-Please! D-Don't tell Kathryn about this!"
    TALL_YOUNG_MAN "A-Anya's noticed an improvement thanks to your training!"
    THIN_YOUNG_MAN "Venza s-says I last longer now..."
    MRS_WINWARD "Don't worry dearies, {i}My lips are sealed{/i}"
    MRS_WINWARD "Now cover me in your spunk."
    YOUNG_MAN "Y-Yes, ma'am!"
    TALL_YOUNG_MAN "H-Hrghhh!"
    THIN_YOUNG_MAN "S-So good! {i}*Huff*{/i}"

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")

    if tmpvar == "cow":
        $ UnlockGalFlag("mrs_winward", "pimp_doublehj", "cow")
        scene mrs_winward_pimp_doublehj_cow_finish with dissolve
        
    if tmpvar == "nude":
        $ UnlockGalFlag("mrs_winward", "pimp_doublehj", "nude")
        scene mrs_winward_pimp_doublehj_nude_finish with dissolve

    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "pimp_doublehj")

    "The three boys, on command, grunted quickly one after the other as they fired their loads, covering a very smug-looking Mrs. Winward, now plastered in their dripping seed."
    "Mrs. Winward scooped up some of the seed spilt onto her chest and pushed the finger into her mouth to taste."
    MRS_WINWARD "Mhmm!"
    MRS_WINWARD "Very good boys, don't forget, same time next week! Fufu! {image=[ICON.HEART]}"
    $ AutoMus(True)
    $ tmpvar = {}
    $ LocEnter()

label rom_winward_pimp_threesome:
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    show mc at center with easeinleft

    MRS_WINWARD "Ah! Yes... Mhfhh! P-Please! All of you!"
    MRS_WINWARD "S-Slow down! Mhfghhh! {image=[ICON.HEART]}"
    MC "(Is that...?)"
    show mr_winward at left with easeinleft
    MR_WINWARD "She's busy with some clients right now... Come back later."
    hide mr_winward with easeoutright
    "As Mr Winward shuffled back to one of the backrooms, I debated whether to just leave or... take a peek?"
    menu:
        "Take a peek.":
            pass

        "Just leave.":
            scene black with dissolve
            "I headed for the door and left."
            $ LocSet("novaras_dist_house")
            $ LocEnter()

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    scene mrs_winward_pimp_threesome_slow with dissolve
    $ Pause()
    
    "Peering into the backroom, Mrs Winward was on her hands and knees, as three men gathered around her, stuffing each of her holes."
    MRS_WINWARD "Mhhfhhh! {i}*Slurp!*{/i}"
    
    TALL_GUY "Ahh! This old bitch sure knows how to suck a cock!"
    TALL_GUY "You think that old guy is her husband outside?"
    
    THIN_GUY "No idea, Mhh! Damn it!"
    THIN_GUY "Ahh! Her ass feels good!"
    THIN_GUY "Hrghh! Don't know how much longer I can keep this up!"
    
    BIG_GUY "Haha! Wasn't this your idea?"
    BIG_GUY "Ahh! I told you all we could have found some younger whore to fuck in the brothel district! But you both insisted she'd-"
    BIG_GUY "S-Shit! She is pretty tight, though..."
    MRS_WINWARD "Mhhfhhh! M-Mhoreee! {image=[ICON.HEART]}"
    "As the hot room was filled with the lewd wet sounds of flesh slapping together, it quickly became clear the three sweaty men wouldn't be able to handle much more."
    TALL_GUY "Haa! Gods! Grghh! I'm close, boys!"
    THIN_GUY "Mee too!"
    BIG_GUY "Gahh!"
    MRS_WINWARD "F-Fhishhhh! Mhhh!"
    TALL_GUY "Hear that, boys?"
    TALL_GUY "Let's give the old girl what she wants! Haha!"
    "The men slammed into her as Mrs Winward's lewd moans rose."
    MRS_WINWARD "Mhh! Mhh! Mhh!!! {image=[ICON.HEART]}"
    
    $ UnlockGalSceneAndGrantXp("mrs_winward", "pimp_threesome")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")

    scene mrs_winward_pimp_threesome_finish with flash
    $ Pause()

    "Finally, as the men grunted one after another in quick succession, the three began filling up each of Kionni's holes." #Cum
    TALL_GUY "H-Hrghh! That's it, you old slut! Swallow it all!"
    MRS_WINWARD "Mhhhhfhhh!"
    THIN_GUY "Ahh, boss, I'm done too!"
    BIG_GUY "Me also!"
    TALL_GUY "{i}*Phew!*{/i}" 
    TALL_GUY "Let's get going, boys, I wanna get a few more rounds in me before heading back to the missus!"
    "The man playfully slapped Mrs Winward's round ass, and it jiggled with the impact."
    MRS_WINWARD "Mhhff!"
    TALL_GUY "Heheh! We'll be back for you another time!"
    $ AutoMus(True)
    scene black with dissolve
    "Pulling away from the scene, I quickly left before they saw me standing there."
    $ LocEnter()

label rom_winward_pimp_markus_bj:
    show mc at center with easeinleft
    show markus at cleft with easeinleft
    MARKUS @shock "Uhh! [player_name!t]!"
    MARKUS @smile "If I might have a couple minutes to myself."
    MARKUS @lewd "I need to uhhh... {i}tend to my needs.{/i}"
    MC @talk "Ahh, of course."
    MARKUS @smile "Thanks friend, I promise to be quick."
    MARKUS @smile "Your next girl is on me the next time we'll down the brothel district."
    MC @smile "I'll hold you to that."
    hide markus with easeoutright
    "Smiling, I watched as Markus briefly made his way down the street, wondering which house he might turn off into."
    "...To my surprise, he entered the Tanner's store."
    MC @surprised "...Wait, is he going to see-"
    menu:
        "Follow Markus into the tanner store.":
            hide mc with easeoutright
            pass

        "Wait for Markus to return.":
            "Well, I shouldn't be too surprised."
            "There was always a chance Markus was going to run into Mrs Winward with the amount of ladies of the night he frequented."
            scene black with dissolve
            $ TimeAdvBy(TIME_05H)
            "About half an hour later, a sweaty, red-faced Markus returned to me."
            $ LocFlush()
            show mc at cleft 
            with dissolve
            show markus at cright_f with easeinright
            MARKUS @smile "Apologises for the wait friend!"
            MC @talk "Ready to continue?"
            MARKUS @smile "Of course!"
            $ LocEnter()
    
    scene black with dissolve
    $ LocSet("novaras_tanner_shop")
    $ LocFlush(dissolve)
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    show mc at center with easeinleft

    MRS_WINWARD "Ah! Mhfhh! B-Be careful! Please!"
    MRS_WINWARD "Mhfghhh! {image=[ICON.HEART]}"
    MC "(...Sounds like the two of them are having fun.)"
    show mr_winward at left with easeinleft
    MR_WINWARD "She's busy with some clients right now... Come back later."
    MC @think "Is it normal for her to work this early?"
    MR_WINWARD "He's becoming quite the regular..."
    hide mr_winward with easeoutright
    "As Mr Winward shuffled back to one of the backrooms, I debated whether to just leave or... take a peek?"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    scene mrs_winward_pimp_markus_slow with dissolve
    $ Pause()
    "Peering into the room again, I watched to see what Markus and Mrs Winward were up to." 
    "On her knees, Mrs Winward wrapped her huge tits around Markus' cock as she sucked on the head."
    MARKUS "Ahhh! B-Bloody hells, are you good at that!"
    MRS_WINWARD "{i}*Slurp* *Slurp*{/i} Mhhfhhh..."
    "Mrs Winward grabbed and pressed her huge tits together, moving them up and down to massage Markus' huge prick."
    MARKUS "You're good with your tongue you know!"
    "Mrs Winward giggled at the comment despite her mouth being full."
    MRS_WINWARD "Mhhhh! Fhankyhuuu! {i}*Slurp!*{/i}"
    MARKUS "Ha! You like big cocks, don't you?"
    MRS_WINWARD "Mhhhhh!!"
    MARKUS "A-Ahh! I have this - Mhhh! Friend..."
    MARKUS "I should bring him to meet you some - Ooh! Easy now! Ahh...!"
    MARKUS "He's uhh, {i}just like me.{/i}"
    MARKUS "Heh, I think he'll like you a lot!"
    "Mrs Winward pushed her head down slightly further, trying to take Markus' thick cock deeper as he groaned happily in appreciation."
    MRS_WINWARD "Shoundshhhlhikehhhfhunn! Mhhfhh!"
    MRS_WINWARD "I lhuvhh {i}*Slurp!*{/i} yhourhh chockhh! {image=[ICON.HEART]}"
    MARKUS "Ooooh! I'm g-getting close! Ahh!"
    "Mrs Winward's head continued to glide back and forth, her lips coating as much of his cock in her glistening saliva as she could."
    "Finally, all of Markus' body seemed to tense up as he grabbed the back of Mrs Winward's head and did his best to pull her head forward."

    $ UnlockGalSceneAndGrantXp("mrs_winward", "pimp_markus")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")

    scene mrs_winward_pimp_markus_finish with flash
    $ Pause()

    MARKUS "H-HRGHHH!"
    "Mrs Winward's eyes widened in surprise as she felt the rush of cum pouring into her mouth."
    MRS_WINWARD "Mmmfghhh?!"
    "Obediently, she did her best to swallow down every drop, but much of it over-spilled and covered her tits in a white layer."
    "Once he was spent, Markus slowly unsheathed his cock, and as it fully pulled out of Mrs Winward's mouth, she let out a light giggle as she gave the head a little kiss."
    $ AutoMus(True)
    scene black with dissolve
    MRS_WINWARD "Mhmm, come back soon, deary. {image=[ICON.HEART]}"
    $ LocFlush()
    show mc at cleft
    with dissolve
    show markus at cright_f with easeinright
    "As Markus headed out the door, he bumped into me."
    MARKUS @shock "[player_name!t]!"
    MARKUS @smile "I told you I'd be back shortly!"
    MARKUS @smile "Ahh, you must have heard about uh... {i}the new talent.{/i}"
    MC @smile "The new talent, huh?"
    MARKUS "I know she's definitely older than most of the girls out there, but when I heard the rumors about her 'talents,' I was intrigued."
    MC "(Rumors huh?)"
    MC "(Sounds like Kionni's already making quite the name for herself...)"
    MARKUS @smile "Have some fun with her sometime or go half with me if you wanna see just how much she can take! She's worth every coin!"
    MC "Are you finished and ready to re-join me?"
    MARKUS @smile "Of course, friend!"
    $ LocEnter()