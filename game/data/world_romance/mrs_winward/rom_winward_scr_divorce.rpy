# Tanner store - returning - Kionni won't be available to speak to for 1 week in game. 
# If player attempts to enter the store, they're prompted with "I should probably give her some more time..."
label rom_winward_divorce_visit_after_some_time:
    $ RomanceWinward().Divorce_SeenReturnFewDaysLaterScene = True
    $ NoteLock("RomWinward_VisitInAWeek")

    show mc at cleft with easeinleft
    MC  "Kionni? Are you here?"
    MRS_WINWARD "J-Just a moment!"
    show mrs_winward at cright_f with easeinright
    "From the back room, Kionni emerged and smiled sheepishly at me."
    MRS_WINWARD @embarr "H-Hello..."
    MC @think "Is everything okay?"
    MRS_WINWARD @sad "As well as things can be, I suppose."
    MC @think "Have you, spoken to your husband since?"
    MRS_WINWARD @sad "No, but apparently he spends all his time drunk at the Iron Unicorn or seeking out Ramonian whores..."
    MC @sad "Ahh..."
    MC @sad "I'm sorry to hear that."
    MRS_WINWARD @sad "...I don't want to wait around feeling sorry anymore."
    MC @think "Huh?"
    MRS_WINWARD @angry "That prick hasn't given a second thought to me in years."
    MRS_WINWARD @angry "All he's ever cared about is the damn 'Winward' name."
    MRS_WINWARD @angry "Well damn him!"
    "Mrs Winward grabbed a hold of my hand suddenly."
    MC @surprised "Kion-!"
    MRS_WINWARD @angry "Come with me."
    MRS_WINWARD @angry "{i}There's something we need to do...{/i}"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene black with dissolve
    "Five minutes later..."
    MRS_WINWARD "H-Hurry up! I n-need this! {i}*Huff*{/i}"
    
    scene mrs_winward_missionary_solo_naked_nopreg_idle with dissolve
    $ Pause()

    "Mrs Winward's eyes widened as she stared down at the massive appendage rubbing against her wet hole,"
    "Pinned down at the wrists, I could feel her tremble with nervousness as her chest rose and fell in heavy deep breaths."
    "Flushed red, she bit down on her lower lip in anticipation of what was to come."
    MRS_WINWARD "P-Please, be gentle with your c-cow!"
    menu rom_winward_divorce_visit_after_some_time_sexmenu:
        "Put it in her pussy.":
            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            scene mrs_winward_missionary_solo_naked_nopreg_vag_slow with dissolve
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
            "Those words made Kionni's pussy tighten and squeeze around me, the shame and embarrassment of the words slipping out of her mouth turning her on all the more."
            "Her desperation for my cock only further excited me, as I began to move faster."
            MRS_WINWARD "Oooh! D-Dear!"
            MRS_WINWARD "Mmfhghh!"

            scene mrs_winward_missionary_solo_naked_nopreg_vag_fast with dissolve
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
            $ UnlockGalFlag("mrs_winward", "missionary", "naked")
            $ UnlockGalFlag("mrs_winward", "missionary", "nopreg")
            $ UnlockGalFlag("mrs_winward", "missionary", "vag")

            $ ReduceInfectionFromSex("mrs_winward")
            $ PregRoll("mrs_winward")
            scene mrs_winward_missionary_solo_naked_nopreg_vag_finish with flash
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
            "As I gently prodded the head of my sword against her tight asshole, Mrs Winward gasped in shock." 
            MRS_WINWARD "N-Not there!"
            MRS_WINWARD "P-Please! I've never even had a finger back there!"
            MC "(Hmm... If I wanna fuck her tight rear, I'm going to need to help her practice and loosen up back here.)"
            MC "(Perhaps there's something I can buy that will assist?)"
            if not QstIsActive(EventArlenaOrderButtplugForWinward) and not QstIsOver(EventArlenaOrderButtplugForWinward):
                $ QstStart(EventArlenaOrderButtplugForWinward)
            jump rom_winward_divorce_visit_after_some_time_sexmenu

label rom_winward_divorce_initiate_sex:
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
            MRS_WINWARD @lewd "Mmm... One moment dear."
            scene black with dissolve
            $ CharSetClothes("mrs_winward", "cowl")
            $ LocFlush(dissolve)
            show mrs_winward at center_f with dissolve
            MRS_WINWARD @blush "Now what, handsome?"
            pass

        "I was thinking about us going to your bedroom tonight.":
            $ RomanceWinward().Divorce_SetUpEveningScene = True
            $ NoteUnlock("RomWinward_SetUpEveningScene")
            MRS_WINWARD @lewd "Mmm, then I best prepare myself, hadn't I?{image=[ICON.HEART]}"
            return

    menu rom_winward_divorce_initiate_sex_menu:
        "How about a kiss?":
            MRS_WINWARD @lewd "Coming right up, handsome." #MC and Mrs Winward kiss sprite
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
            jump rom_winward_divorce_initiate_sex_menu

        "I was thinking you could wrap those lips around my cock.":
            jump rom_winward_divorce_rep_bj

        "I was thinking about pinning you up against the wall.":  #Fuck against wall repeat
            jump rom_winward_divorce_rep_doggy_wall

label rom_winward_divorce_rep_doggy_wall:
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
    menu rom_winward_divorce_rep_doggy_wall_sexmenu:
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
                jump rom_winward_divorce_rep_doggy_wall_sexmenu
            
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

            "Moving my cock slightly higher, I lightly prodded against her forbidden back door."
            MRS_WINWARD "{i}*Gasp!*{/i}"
            MRS_WINWARD "If... If you're going to try and put it {i}there,{/i} p-please."
            MRS_WINWARD "Start slowly?"
            "Grabbing a fist full of her hair, she let out another short gasp as she felt the head of my cock sink into her tight, clutching asshole."
            MRS_WINWARD "A-AHHHH!!"
            "Slowly, I began to thrust my cock in and out of Mrs Winward's ass."
            "Her ass rippled with every thrust as I squeezed my free hand on her round ass for better grip, feeling the fat slip between my fingers."
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

            $ UnlockGalFlag("mrs_winward", "doggy_wall", "no_cuck")
            $ UnlockGalFlag("mrs_winward", "doggy_wall", "anal")
            
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
            "Only a soft whimpered escaped her lips as I held her body upright in my arms."
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
            MRS_WINWARD @embarr "I... {i}I didn't say that I didn't like it.{/i}"
            MRS_WINWARD @embarr "Only that I needed a little more prep!"
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
            "Her eyes rolled back as she trembled and nearly collapsed back into my arms."
            "I held her up as I continued to pump my load into her body."
            "Only a soft whimpered escaped her lips as I held her body upright in my arms."
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

label rom_winward_divorce_visit_bedroom_miss:
    $ RomanceWinward().Divorce_SetUpEveningScene = False
    $ NoteLock("RomWinward_SetUpEveningScene")
    
    show mrs_winward at cright_f with dissolve
    show mc at cleft with easeinleft

    MRS_WINWARD @lewd "Mmm, looks like my big {i}strong{/i} bull has come to empty his balls in his little cow again?"
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

    MRS_WINWARD "Oooh! We have all night dear! No need to hurry! Mhmm!"
    "Mrs Winward's eyes widened as she stared down at the massive appendage rubbing against her wet hole,"
    "Pinned down at the wrists, I could feel her tremble with nervousness as her chest rose and fell in heavy deep breaths."
    "Flushed red, she bite down on her lower lip in anticipation of what was to come."
    MRS_WINWARD "A-Ah, start slow dear... You know I have to get used to your size!"
    menu rom_winward_divorce_visit_bedroom_miss_sexmenu:
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
            "Mrs Winward shook as her mouth hung agape, her eyes rolling back as a choking, silent moan escaped her lips as she climaxed with me feeling the rush of warmth flood her womb."
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
                jump rom_winward_divorce_visit_bedroom_miss_sexmenu

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
            MRS_WINWARD "A-Ahhh! It still - Mhmm! Feels like it burns but-"
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
            $ ReduceInfectionFromSex("mrs_winward")
            
            $ UnlockGalFlag("mrs_winward", "missionary", "solo")
            $ UnlockGalFlag("mrs_winward", "missionary", "anal")

            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            if CharGetClothes("mrs_winward") == "naked":
                $ UnlockGalFlag("mrs_winward", "missionary", "naked")
                if CharIsVisiblyPreg("mrs_winward"):
                    scene mrs_winward_missionary_solo_naked_preg_anal_finish with dissolve
                    $ UnlockGalFlag("mrs_winward", "missionary", "preg")
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
            "Mrs Winward's eyes rolled back as she cooed and twitched feeling my cum fill up her ass."
            "As I poured out every last drop of the thick seed into her ass, she quivered and moaned softly, not saying a word as I slowly unsheathed my cock from her now loosened ass."
            "With a small {i}*pop!*{/i} sound, my cock pulled out of her quivering, winking asshole as my seed poured out of her gaping hole on the bed."
            MRS_WINWARD "A-Ahhh....!! {image=[ICON.HEART]}"
            MC "{i}*Huff*{/i} Are you alright, Mrs Winward?"
            MRS_WINWARD "M-Mhmmm...."
            "Mrs Winward simply quivered and moaned in response, some of my cum continued to seep out of her hole as she laid there motionless on the bed."
            MC "Thanks for letting me use your ass, Mrs Winward."
            MRS_WINWARD "A-Ahhhh...{image=[ICON.HEART]}"
            pass

    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    $ LocSet("novaras_dist_house")
    $ AutoMus(True)
    "Leaving her to rest, I slipped out of the store, locking the door behind me."
    $ LocEnter()

label rom_winward_divorce_rep_bj:
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

    "Gently, her tongue slipped out of her mouth to tenderly run along the shaft, and after she gently teased it, she took a deep breath, and wrapped her lips around the head of my cock." #BJ behind counter
    MRS_WINWARD "M-Mhmm!"
    MC "Mhmmff! That's it Mrs Winward, all our time together is really paying off, isn't it?"
    "Mrs Winward, embarrassed, didn't answer, instead, she began to glide her head back and forth in a slow but steady motion."
    "Her soft lips formed a tight seal around my cock as her tongue sheepishly wrapped and teased my member."
    "Her puffy stuffed cheeks were bright red as her eyes looked up pleadingly towards me, unsure if she was doing a good enough job at pleasing me."
    MRS_WINWARD "{i}*Slurp!* *Slurp!*{/i} Mhmmfhh!"
    MRS_WINWARD "(If only my husband was half as big as him.)"
    MRS_WINWARD "(Urghhh! Forget that moron!)"
    MRS_WINWARD "(I could just worship this cock all night!)"
    "Suddenly, Mrs Winward groaned happily as she threw her head forward, pushing the cock deeper and deeper into her throat as she became enthralled in her task."
    MRS_WINWARD "(It's h-his fault for being such a fool! Mhmm, now a bigger, {i}better{/i} man is here to take care of my needs fufufu! {image=[ICON.HEART]})"

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
    "With defiant, fiery eyes she looked up towards me, tongue thrashing furiously around my cock."
    "With her eyes she told me clearly, {i}'You're going to cum down my throat whether you like it or not!'{/i}"
    "I grabbed a hold of Mrs Winward's head and held her there, my balls tightened as I exploded into her mouth."
    "Her eyes widened as she felt the hot rush of my heavy load flood down her throat."
    "I grunted loudly, watching the excess of my seed spill out the sides of her mouth as her eyes began to roll back."
    "Desperately, Mrs Winward tried to swallow down as much of the load as possible, her stomach lightly bulging from the seed being pumped into her as her eyes rolled back."
    MC "H-HRGHHHHH...!"

    $ ReduceInfectionFromSex("mrs_winward")

    
    $ UnlockGalFlag("mrs_winward", "bj", "winward_gone")
    $ UnlockGalFlag("mrs_winward", "bj", "no_cuck")

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    if CharGetClothes("mrs_winward") == "cowl":
        $ UnlockGalFlag("mrs_winward", "bj", "cow")
        scene mrs_winward_bj_cow_solo_finish with flash
    if CharGetClothes("mrs_winward") == "normal":
        $ UnlockGalFlag("mrs_winward", "bj", "dress")
        scene mrs_winward_bj_dress_solo_finish with flash
    $ Pause()
    $ UnlockGalSceneAndGrantXp("mrs_winward", "bj")

    MRS_WINWARD "{i}*Glug!*{/i} Mfhghhh?!"
    "Finally, I released my tight grip on the back of Mrs Winward's head."
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
    MRS_WINWARD @embarr "I hope that was good for you dear."
    MC @lewd "That was very good."
    MRS_WINWARD @blush "Well then, now that {i}my man{/i} has been satisfied, I best get back to work, hadn't I?"
    "As she turned to leave, I playfully slapped at her round ass."
    MRS_WINWARD @shock "Oooh!"
    MRS_WINWARD @blush "Later dear.{image=[ICON.HEART]}" 
    scene black with dissolve
    $ CharSetClothes("mrs_winward", "normal")
    "Leaving her to rest, I slipped out of the store, locking the door behind me."
    $ LocSet("novaras_dist_house")
    $ LocEnter()

label rom_winward_divorce_murder_first_impreg:
    show mc at cleft with easeinleft
    "Upon entering into the store, a flustered Kionni hurried towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @scared "W-We need to talk."
    MC @think "What is it?"
    MRS_WINWARD @scared "I-"
    MRS_WINWARD @scared "I'm pregnant!"
    MC @surprised "You... You're what?!"
    MRS_WINWARD @shock "I couldn't believe it at first, it shouldn't be possible!"
    MRS_WINWARD @embarr "But I... I carry your child!"
    MC @think "Well... We knew this {i}could{/i} happen."
    MC @smile2 "I guess I'm just shocked is all!"
    MRS_WINWARD @sad "I... Are you okay with this?"
    MRS_WINWARD @sad "I mean, having a child with a woman my age?"
    MC @smile "Your age is of no concern to me."
    MC @smile "In fact, I hope you're ready to carry a few more for me."
    MRS_WINWARD @shock "...O-Oh my...!"
    MRS_WINWARD @embarr "But, be serious! With my husband no longer around, I-"
    MRS_WINWARD @sad "I'm not sure I can afford to have this child!"
    MRS_WINWARD @sad "N-Nevermind the problems with my age!"
    MRS_WINWARD @sad "What if I die before they-"
    MC  "Don't worry, Kionni, I will make sure you and the child are looked after."
    MRS_WINWARD @sad "{i}*Sigh*{/i} I hope you're right..."
    MRS_WINWARD @sad "I best get back to my work."
    "Mrs Winward slumped off to continue her tanning work."
    MC "(Hm... While it's not a problem for now, I'll need to put some thought into helping Kionni, especially now that we're having a child together!)"
    $ LocEnter()

label rom_winward_divorce_rep_impreg:
    show mc at cleft with easeinleft
    "Upon entering into the store, a flustered Kionni hurried towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @scared "W-We need to talk."
    MC @think "What is it?"
    MRS_WINWARD @scared "I-"
    MRS_WINWARD @scared "I'm pregnant!"
    MC @surprised "{i}Again?{/i}"
    MRS_WINWARD @scared "{i}Oh gods, what are we going to do?{/i}"
    MC @think "Perhaps the church can offer some support if you explain the situation?"
    MC  "At least while I figure something out..."
    MRS_WINWARD @sad "{i}*Sigh*{/i} Yes, they might offer me some extra food at least."
    MRS_WINWARD @sad "I just hope things improve soon..."
    MRS_WINWARD @sad "I best get back to my work."
    hide mrs_winward with easeoutleft
    "Mrs Winward slumped off to continue her tanning work."
    MC "(Hm... While it's not a problem for now, I'll need to put some thought into helping Kionni, especially now that we're having a child together!)"
    $ LocEnter()

label rom_winward_divorce_first_birth:
    $ PregWinward().DoFirstBabyScene = False
    show mc at cleft with easeinleft
    "As I entered into the store, Mrs Winward, clutching TWO small cutely gurgling babies wrapped in warm cloths smiled towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @happy "Look little ones."
    MRS_WINWARD @happy "{i}Father is here.{/i}"
    MC @surprised "Two?!"
    MC @surprised "Is that...?"
    MRS_WINWARD @happy "Who else could it be, dear?"
    MRS_WINWARD @laugh "Fufu, aren't they beautiful?"
    MRS_WINWARD @happy "What shall we call them?"
    $ PregWinward().BabyName1 = renpy.input(_("What names shall we call them?"), default = PregWinward().BabyName1Default)
    $ PregWinward().BabyName2 = renpy.input(_("...And?"), default = PregWinward().BabyName2Default)
    MRS_WINWARD  "Hmm, good choices."
    MRS_WINWARD @happy "I'm gonna go put the little ones down for a nap."
    MC @smile "You seem happier today."
    MRS_WINWARD @blush "It's... a strange feeling, being a mother again."
    MRS_WINWARD  "And seeing their cute faces did wash away my fears for a moment at least..."
    MRS_WINWARD  "I'm going to go lay the two of them down for a nap."
    MRS_WINWARD  "Come by later, I'm sure we'll have lots to talk about."
    $ LocEnter()

label rom_winward_divorce_rep_birth:
    show mc at cleft with easeinleft
    "As I entered into the store, Mrs Winward, clutching TWO small cutely gurgling babies wrapped in warm cloths smiled towards me."
    show mrs_winward at cright_f with easeinright
    MRS_WINWARD @happy "Look little ones."
    MRS_WINWARD @happy "{i}Father is here.{/i}"
    MC @surprised "Two?!"
    MC @surprised "Is that...?"
    MRS_WINWARD @happy "Who else could it be, dear?"
    MRS_WINWARD @laugh "Fufu, aren't they beautiful?"
    MRS_WINWARD @happy "What shall we call them?"
    $ PregWinward().BabyName1 = renpy.input(_("What names shall we call them?"), default = PregWinward().BabyName1Default)
    $ PregWinward().BabyName2 = renpy.input(_("...And?"), default = PregWinward().BabyName2Default)
    MRS_WINWARD  "Hmm, good choices."
    MRS_WINWARD @happy "I'm gonna go put the little ones down for a nap."
    MC @smile "You seem happier today."
    MRS_WINWARD @blush "It's... a strange feeling, being a mother again."
    MRS_WINWARD  "And seeing their cute faces did wash away my fears for a moment at least..."
    MRS_WINWARD  "I'm going to go lay the two of them down for a nap."
    MRS_WINWARD  "Come by later, I'm sure we'll have lots to talk about."
    $ LocEnter()

label rom_winward_divorce_how_is_our_child:
    $ rng = renpy.random.randint(1, 2)
    if rng == 1:
        MRS_WINWARD @happy "Wonderful!"
        MRS_WINWARD @shock "I was worried about their health, but they seem so strong already!"
    if rng == 2:
        MRS_WINWARD @shock "They seem to never tire! I've never seen a child like them!" #variant 2
        MRS_WINWARD @think "Now that I think about it, ever since I got pregnant with them, I've felt stronger myself, and it's like I've had non-stop energy as well!"
        MRS_WINWARD @shock "Did you have something to do with that?"
    return

label rom_winward_divorce_enter_at_night:
    $ RomanceWinward().Divorce_DidDoorSceneToday = True
    show mrs_winward at cright_f with dissolve
    show mc at cleft with easeinleft
    MRS_WINWARD @shock "[player_name!t]! You're here!"
    MC @think "Is that a problem?"
    MRS_WINWARD @embarr "N-No, it's just... "
    play sound "audio/cfx/door_knock.ogg"
    "There was a loud bang at the door."
    show mc at blurin, cleft_f
    MR_WINWARD "Let me in would ya?!"
    MR_WINWARD "{i}*Hiccup!*{/i} We need to - Urghh ..."
    MR_WINWARD "T-Talk!"
    MRS_WINWARD @sad "H-He's been coming around recently when he gets drunk, he says he wants to talk but usually he just yells at me."
    menu:
        "Usher away the old man.":
            MC "One moment."
            MRS_WINWARD @shock "W-Wait! What are you-"
            hide mrs_winward with easeoutright
            show mc at cright_f with easeoutright
            show mr_winward at cleft with easeinleft
            "Swinging open the door, a surprised Mr Winward looked up towards me in a drunken stupor."
            MR_WINWARD @shock "W-What are'ya doin' in my-"
            MC @serious "You're drunk and it's late, go home."
            MR_WINWARD @angry "No! I need to spechhh to dhatt old haggg!"
            MC @angry "{i}Go home, old man.{/i}"
            MC @angry "{i}Come back when you are sober.{/i}"
            MR_WINWARD @angry "T-This is my home! You can't just-"
            show mr_winward at left with easeoutleft
            "As I glared at Mr Winward, he took a few sheepish steps back."
            MR_WINWARD @scared "T-This is outrageous!"
            MR_WINWARD @angry "Thishh ishh still my home!"
            MC @serious "Not tonight it isn't."
            "Mr Winward opened his mouth to say something, but instead of answering back, he turned tail to leave quickly."
            MR_WINWARD @scared "T-Tell her I'll be by soon!"
            hide mr_winward with easeoutleft
            "As he limped away pathetically, I slammed the door shut."
            $ PlaySoundRandom("woodenDoor")
            show mc at blurin, cleft with easeoutleft
            show mrs_winward at cright_f with easeinright
            "Feeling a soft hand on my shoulder, I turned to face a demure looking Mrs Winward."
            MRS_WINWARD @embarr "Thank you."
            MRS_WINWARD @embarr "You didn't need to do that."
            MC @smile "I wanted to."
            MRS_WINWARD @embarr "{i}*Sigh*{/i} I still have no idea what you see in an old lady like me."
            MRS_WINWARD @blush "...But I intend to give you more than a few reasons. {image=[ICON.HEART]}"
            MRS_WINWARD @lewd "N-Now, can I help you with anything?"
            call processDialogue("mrs_winward_root") from _call_processDialogue_52
            $ LocEnter()

        "Let her speak to her husband and have some fun.":
            if RomanceWinward().Divorce_FirstTimeDoingDoorScene:
                $ RomanceWinward().Divorce_FirstTimeDoingDoorScene = False
                jump rom_winward_divorce_enter_at_night_door_sex_first_time
            else:
                jump rom_winward_divorce_enter_at_night_door_sex_rep

label rom_winward_divorce_enter_at_night_door_sex_first_time:
    MC @smile "Don't open the door, just talk to him through it."
    MRS_WINWARD @shock "Hm?"
    MRS_WINWARD @think "But... {i}Why?{/i}"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    MC @lewd "Just do it."

    scene mrs_winward_doggydoor_dress_nopreg_idle with dissolve
    $ Pause()

    "As Mrs Winward approached the door, she sheepishly placed her hands onto the wooden frame as she spoke softy." 
    MRS_WINWARD "W-What do you want now?"
    MR_WINWARD "Why won'tcha lemme in?"
    MR_WINWARD "I've got - Urghh! Thingshaa say to you!"
    "Moving behind Mrs Winward, she gasped as she felt my hands rolling and hiking up her skirt."
    MRS_WINWARD "{i}*Whispering* W-What do you think you're doing?!{/i}"
    MR_WINWARD "What was thattthh? I can't hear ya!"
    MRS_WINWARD "N-Nothing!"
    "As I slapped my cock across her soft ass, Mrs Winward welped slightly, but as she felt the head press up against her womanhood, she spread her legs wider for easier access."
    MRS_WINWARD "J-Just dealing with a very {i}big{/i} problem right now!"
    
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mrs_winward_doggydoor_dress_nopreg_vag_slow with dissolve
    $ Pause()

    "As the head of my cock pushed through into her slit, she let out a little gasp as I began to slowly push my cock deeper into her."
    "Her dryness didn't last long, already, as she pressed her face against the doorframe, I could feel her become more and more excited by each passing moment."
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

    $ UnlockGalFlag("mrs_winward", "doggy_door", "dress")
    $ UnlockGalFlag("mrs_winward", "doggy_door", "nopreg")
    $ UnlockGalFlag("mrs_winward", "doggy_door", "vag")

    $ UnlockGalSceneAndGrantXp("mrs_winward", "doggy_door")
    $ ReduceInfectionFromSex("mrs_winward")

    scene mrs_winward_doggydoor_dress_nopreg_vag_finish with flash
    $ Pause()

    "I grunted loudly through gnashed teeth as I slammed my cock to the hilt inside of her, mashing up her insides as I poured my hot load into her welcoming hole."
    "Her eyes widened once more as her mouth hung agape, choking on air before a guttural grunt of pleasure escaped her lis."
    MRS_WINWARD "Mmmmmfghhhhhhhhhhh!!"
    MRS_WINWARD "{i}*Huff* *Huff*{/i} By the gods..."
    "I held up Mrs Winward before her legs could give out from under her, and as she regained her footing, the two of us realised neither of us could no longer hear Mr Winward's voice."
    $ LocFlush()
    show mc at cleft
    show mrs_winward at cright_f
    with dissolve
    MRS_WINWARD @shock "He... He must have ran away."
    MC "Sounds like it."
    MRS_WINWARD @sad "...Do you think he'll come back after that?"
    MC @think "Probably by the next time he's drunk he'll have convinced himself that was all a dream."
    MRS_WINWARD @embarr "A-Ahh... Of course."
    MRS_WINWARD @blush "I think I best lay down for a while before my legs give out, deary..."
    $ AutoMus(True)
    MRS_WINWARD @happy "Feel free to stay and rest here as long as you wish."
    scene black with dissolve
    "Mrs Winward gently kissed me on the cheek before hobbling her way towards her bedroom."
    MC "(I wonder what the old man's thinking right now?)"
    $ LocEnter()

label rom_winward_divorce_enter_at_night_door_sex_rep:
    MC @smile "Wanna have some {i}fun{/i} again?"
    MRS_WINWARD @shock "Y-You mean-"
    MC @smile "Don't open the door, just talk to him through it."

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    "As Mr Winward continued to bang against the door, Mrs Winward nodded sheepishly."
    MRS_WINWARD @blush "O-Okay..."

    menu:
        "Tell her to quickly get changed into the cow outfit":
            MRS_WINWARD @embarr "B-But he-"
            MC "He's not going anywhere."
            MC "Now go change, {i}quickly.{/i}"
            scene black with dissolve
            "Mrs Winward nodded once more as she hurried to go get changed, her cheeks burning red as her soon to be ex-husband continued to bash against the door."
            $ CharSetClothes("mrs_winward", "cowl")

        "Let her stay dressed":
            pass

    if CharGetClothes("mrs_winward") == "cowl":
        scene mrs_winward_doggydoor_cow_nopreg_idle with dissolve
    else:
        scene mrs_winward_doggydoor_dress_nopreg_idle with dissolve
    $ Pause()

    "As Mrs Winward approached the door, she sheepishly placed her hands onto the wooden frame as she spoke softy."
    MRS_WINWARD "G-Go home dear!"
    MRS_WINWARD "You're going to wake the neighbours!"
    MR_WINWARD "Yhouuhh WHOREEEE! I knowhh yhourhh fhuckinn him in there!"
    MR_WINWARD "Openhh thishh doorhhh!"
    MR_WINWARD "I've got - Urghh! Thingshaa say to you!"
    "Moving behind Mrs Winward, she gasped as she felt my hands rolling and hiking up her skirt."
    MRS_WINWARD "{i}*Whispering* A-Ah! Careful!{/i}"
    MR_WINWARD "What was thattthh? I can't hear ya!"
    MRS_WINWARD "N-Nothing!"
    "As I slapped my cock across her soft ass, Mrs Winward welped slightly, but as she felt the head press up against her womanhood, she spread her legs wider for easier access."
    MRS_WINWARD "J-Just dealing with a very {i}big{/i} problem right now!"
    menu rom_winward_divorce_enter_at_night_door_sex_rep_sexmenu:
        "Put it in her ass":
            if not RomanceWinward().UnlockedAnalSex:
                MRS_WINWARD "D-Darling! Please!"
                MRS_WINWARD "Not there!"
                MC "(Hmm, I'm gonna need to 'train' her hole a little back there if I'm going to want to use it.)"
                MC "(Perhaps gifting her a small toy is in order?)"
                if not QstIsActive(EventArlenaOrderButtplugForWinward) and not QstIsOver(EventArlenaOrderButtplugForWinward):
                    $ QstStart(EventArlenaOrderButtplugForWinward)
                jump rom_winward_divorce_enter_at_night_door_sex_rep_sexmenu

            $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)

            if CharGetClothes("mrs_winward") == "cowl":
                scene mrs_winward_doggydoor_cow_nopreg_anal_slow with dissolve
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

            if CharGetClothes("mrs_winward") == "cowl":
                scene mrs_winward_doggydoor_cow_nopreg_anal_fast with dissolve
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

            $ UnlockGalFlag("mrs_winward", "doggy_door", "nopreg")
            $ UnlockGalFlag("mrs_winward", "doggy_door", "anal")

            $ ReduceInfectionFromSex("mrs_winward")

            if CharGetClothes("mrs_winward") == "cowl":
                $ UnlockGalFlag("mrs_winward", "doggy_door", "cow")
                scene mrs_winward_doggydoor_cow_nopreg_anal_finish with dissolve
            else:
                $ UnlockGalFlag("mrs_winward", "doggy_door", "dress")
                scene mrs_winward_doggydoor_dress_nopreg_anal_finish with dissolve
            $ Pause()

            $ UnlockGalSceneAndGrantXp("mrs_winward", "doggy_door")

            "I grunted loudly through gnashed teeth as I slammed my cock to the hilt inside of her, mashing up her insides as I poured my hot load into her bowels."
            "Her eyes widened once more as her mouth hung agape, choking on air before a guttural grunt of pleasure escaped her lips."
            MRS_WINWARD "Mmmmmfghhhhhhhhhhh!! {image=[ICON.HEART]}"
            MRS_WINWARD "{i}*Huff* *Huff*{/i} By the gods..."
            "I held up Mrs Winward before her legs could give out from under her, and as she regained her footing, the two of us realized neither of us could no longer hear Mr Winward's voice."

        "Put it in her pussy":
            $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)

            if CharGetClothes("mrs_winward") == "cowl":
                scene mrs_winward_doggydoor_cow_nopreg_vag_slow with dissolve
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

            if CharGetClothes("mrs_winward") == "cowl":
                scene mrs_winward_doggydoor_cow_nopreg_vag_fast with dissolve
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
            
            $ ReduceInfectionFromSex("mrs_winward")

            $ UnlockGalFlag("mrs_winward", "doggy_door", "nopreg")
            $ UnlockGalFlag("mrs_winward", "doggy_door", "vag")

            if CharGetClothes("mrs_winward") == "cowl":
                $ UnlockGalFlag("mrs_winward", "doggy_door", "cow")
                scene mrs_winward_doggydoor_cow_nopreg_vag_finish with dissolve
            else:
                $ UnlockGalFlag("mrs_winward", "doggy_door", "dress")
                scene mrs_winward_doggydoor_dress_nopreg_vag_finish with dissolve
            $ Pause()

            $ UnlockGalSceneAndGrantXp("mrs_winward", "doggy_door")

            "I grunted loudly through gnashed teeth as I slammed my cock to the hilt inside of her, mashing up her insides as I poured my hot load into her welcoming hole."
            "Her eyes widened once more as her mouth hung agape, choking on air before a guttural grunt of pleasure escaped her lips."
            MRS_WINWARD "Mmmmmfghhhhhhhhhhh!! {image=[ICON.HEART]}"
            MRS_WINWARD "{i}*Huff* *Huff*{/i} By the gods..."
            "I held up Mrs Winward before her legs could give out from under her, and as she regained her footing, the two of us realized neither of us could no longer hear Mr Winward's voice."

    $ LocFlush()
    show mc at cleft
    show mrs_winward at cright_f
    with dissolve

    MRS_WINWARD @shock "He... He must have ran away."
    MC  "Sounds like it."
    MRS_WINWARD @sad "...Do you think he'll come back after that?"
    MC @think "Probably by the next time he's drunk he'll have convinced himself that was all a dream."
    MRS_WINWARD @embarr "A-Ahh... Of course."
    MRS_WINWARD @blush "I think I best lay down for a while before my legs give out, deary..."
    $ AutoMus(True)
    MRS_WINWARD @happy "Feel free to stay and rest here as long as you wish."
    scene black with dissolve
    "Mrs Winward gently kissed me on the cheek before hobbling her way towards her bedroom."
    $ CharSetClothes("mrs_winward", "normal")
    MC "(I wonder what the old man's thinking right now?)"
    $ LocEnter()