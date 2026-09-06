################################################################################################################################
#The player returns to Marbella's after dark. 
# He appears in the evening suit, scene begins with Marbella
label rom_marbella_love_meet_date:
    show marbella at cleft with dissolve
    show mc at cright_f with easeinright
    MARBELLA @smile "Ahh! There you are!"
    MARBELLA @talk "Ready to get going?"
    menu:
        "I'm ready.":
            pass
        "I have something to do first.":
            MARBELLA @sad "Oh... Uhh, are you not free tonight then?"
            MARBELLA @sad "Umm, let me know when you're ready, I guess."
            scene black with dissolve
            $ CharSetClothes("mc", "normal")
            $ LocSet("hamun_dist_docks")
            $ LocEnter()

    $ NoteLock("marbella_love_meet_date")
    MARBELLA @smile "Great!"
    MARBELLA @smile "Come on then, let's get going..."
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "One hour later..."
    $ Pause(0.5)
    $ LocFlush(dissolve)
    $ LocNameSetTemp(_("The Roasted Serpent restaurant"))
    scene bg_hamun_resturant_night
    show marbella at cright_f
    show mc at cleft
    with dissolve
    MARBELLA @smile "This place is pretty fancy, huh?"
    MARBELLA @emb "Not that um, I've been to many nice places to begin with..."
    MARBELLA @smile "But this place seems nice!"
    MC @smile "Relax, Marbella."
    SERVER "Your table is ready, mi'lady."
    MARBELLA @smile "Mi'lady! Now I do feel classy!"
    MARBELLA @smile "*Cough* I mean, uh, great!"
    SERVER "Right this way..."
    hide marbella at cright_f
    hide mc at cleft
    scene black 
    with dissolve
    "The two of us took a seat at the table, ordering wine and food. Marbella did her best to make small talk, but as her eyes nervously looked around the room, her awkwardness was obvious."
    scene bg_hamun_resturant_night 
    show marbella at cright_f
    show mc at cleft
    with dissolve
    MC @think "Marbella..."
    MARBELLA @sad "..."
    MC @surprised "Marbella!"
    MARBELLA @shock "Hmm?"
    MC @think "Are you alright?"
    MC @think "You seem... nervous."
    MARBELLA @emb "Ah... Ha ha... do I?"
    MARBELLA @emb "Gotta admit, can't help but find all the eyes on us a little... much."
    MARBELLA @emb "I'm not exactly used to places like this."
    MC @think "We can always just leave."
    MARBELLA @shock "No, I..."
    MARBELLA @angry "That would just prove to them people like me don't deserve to be in nice places like this."
    MARBELLA @think "... Can I ask you something?"
    MC @talk "Of course."
    MARBELLA @think "... The whole 'Beast of Novaras' thing."
    MARBELLA @think "How do you really feel about all that?"
    MARBELLA @sad "I mean, there are people out there who think we should just use you and get rid of you after the war is over."
    MARBELLA @shock "Others... others think the fuckin' gods themselves have sent you, or that you may even BE a god!"
    menu:
        "Well, what do YOU think about it?":
            MARBELLA @angry "I think I'd bash someone's skull in if they said it to my face."
            MARBELLA @angry "Especially if I saved the ungrateful bastards."
            pass
        "What's the matter, you don't think divinity suits me?":
            MARBELLA @shock "You can't be a god."
            MARBELLA @talk "You actually answer people's prayers."
            pass
        "I'm here to help people... I don't want people to just think I'm just another monster.":
            MARBELLA @shock "That's my point!"
            MARBELLA @shock "Like, nobody's really thinking about {i}you{/i} anymore, just what {i}you can do for them.{/i}"
            MARBELLA @sad "What I mean is, when they've got what they asked for, what then, y'know?"
            pass
        "Fuck 'em. Better they fear me than think they can try and tame me.":
            MARBELLA @think "Well, that's fair enough I suppose."
            MARBELLA @sad "You best just hope none of them start treating that like some kind of challenge."
            pass

    #All choices continued
    MARBELLA @sad "Anyway, it's getting kind of late."
    MARBELLA @sad "Umm... You could walk me back to the Crooked Shaft."
    MARBELLA @emb "Or um, maybe we could head back to your place for a bit?"
    MARBELLA @emb "For umm... drinks and stuff!"
    "Marbella bit nervously at her lower lip as she waited for my answer."
    menu:
        "Why not? Let's go.":
            pass
        "I think I should just walk you home.":
            MARBELLA @emb "Oh, uh... Alright then." 
            scene black with dissolve
            $ LocNameReset()
            "After paying up for the food and wine, I escorted Marbella back home."
            "She muttered something about 'seeing me in the morning' as she closed the door."
            "I knew what she wanted, but it was for the best we kept things professional..."
            $ NoteUnlock("marbella_love_come_back_after_date")
            $ QstSetProgress(RomanceMarbella, 1)
            $ RomanceMarbella().Love_DayToSkipToAfterDate = GetGameDay() + 2
            $ RomanceMarbella().Love_TookTJ = False
            $ LocSet("hamun_dist_docks")
            $ LocEnter()

    $ RomanceMarbella().Love_TookTJ = False
    MARBELLA @shock "G-Great!"
    MARBELLA @emb "(Oh fuck... I didn't think he'd actually agree!)"
    MARBELLA @emb "(C-Calm down Marbella, this is what you wanted!)"
    MARBELLA @emb "(R-Right...?)"
    scene black with dissolve
    $ LocNameReset()
    "Marbella shifted nervously as we paid for the food and wine before departing."
    "The whole time, she kept nervously looking around as she followed me sheepishly back to The Pale Dragon."
    $ LocSet("hamun_hookah_bar")
    $ LocFlush()
    with dissolve
    show mc at cleft
    show marbella at left
    with easeinleft
    MARBELLA @talk "So uhh, you're staying here then?"
    MARBELLA @think "Don't all the smoke drive you crazy?"
    RANIA @talk "Should I have some wine sent to your room this evening then?"
    "Marbella's cheeks burned red as she averted her gaze, doing her best to hide behind me."
    MC @smile "Yes, that would be nice."
    hide mc
    hide marbella
    with dissolve
    show rania at center with easeinleft
    "As we made our way towards my room, Rania remarked playfully,"
    RANIA @smile "Have fun you two... fufu..."
    label marbella_love_titjob_repeat:
    scene black with dissolve
    if IsFirstTime():
        "Marbella seemed to be nervously pushing me to move faster."
        $ LocSet("hamun_hookah_bar_room")
        $ LocFlush()
        show mc at cright_f
        show marbella at cleft
        with dissolve
        $ PlaySound("audio/cfx/doorthud.ogg")
        MC @talk "Well, this is my room."
        MARBELLA @emb "I-It's nice and spacious."
        MARBELLA @emb "... Umm."
        MC @think "Marbella?"
        MC @think "What's wrong?"
        MARBELLA @sad "It's... been a while since I was."
        MARBELLA @emb "You know."
        MARBELLA @emb "{i}*With*{/i} anyone."
        MC @smile "We don't have to do anything if you don't want."
        MARBELLA @shock "N-No, I do."
        MARBELLA @emb "{i}I really fucking do, to be honest.{/i}"
        MARBELLA @emb "J-Just umm... l-let's go slow?"
        MC @smile "Right."
        MARBELLA @emb "... Could."
        MARBELLA @emb "Could you turn around for a moment?"
        show mc at blurin, cright
        "I did as she asked, heading towards the desk to pour us some wine as I heard the rustling of fabric drop to the floor."
        $ CharSetClothes("marbella", "ling")
        show marbella at nod
        $ PlaySoundRandom("tentFlap")
        show mc at blurin, cright_f
        MC @smile "So, are you-"
        "I stopped, my eyes greedily taking in the sight of Marbella's body pressed into some lingerie."
        MARBELLA @emb "Umm... What do you think?"
        MC @smile "I think you look incredible."
        "Marbella shyly averted her gaze as she muttered 't-thanks' under her breath."
        $ CharSetClothes("mc", "naked")
        $ PlaySound("audio/cfx/cotton_drop.ogg")
        "As I stripped off my clothes, Marbella's eyes widened as she stared at the huge appendage in front of her."
        MARBELLA @shock "FUCK ME WITH SLOAN'S HAMMER!"
        MARBELLA @shock "Is yer dad a fuckin' horse or somethin?'"
        MC @laugh "How'd you know my dad was a stallion?"
        MARBELLA @think "You're fucking with me, right?"
        MC @smile "Neighhhhhh..."
        MARBELLA @angry "Haha, very fuckin' funny."
        "Marbella gulped as she stared at my cock anxiously."
        MARBELLA @emb "Umm... I don't think I'm, uh..."
        MARBELLA @emb "Quite ready for you."
        MC @think "Ah, I'll go put my clothes back on-"
        MARBELLA @shock "W-Wait!"
        MARBELLA @emb "Umm, I mean, I might not be ready to take that monster between your legs."
        MARBELLA @emb "Maybe though..."
        MARBELLA @emb "{i}We could fool around a little?{/i}"
        MC @bitelip "Oh?"
        MARBELLA @lewd "Maybe I could..."
        "Marbella bit her lower lip in anticipation."
        MARBELLA @lewd "{i}H-Have a taste?{/i}"
        MC @think "You sure you're up to that?"
    # repeat variant 
    else:
        $ TimeAdvBy(TIME_1H)
        "Inside my quarters, Marbella wasted no time dropping her clothes to the floor, revealing the lingerie she wore beneath."
        $ CharSetClothes("marbella", "ling")
        $ LocSet("hamun_hookah_bar_room")
        $ LocFlush()
        show mc at cright_f
        show marbella at cleft
        with dissolve
        MARBELLA @lewd "What do you think, handsome?"
        hide marbella
        show cg_marbella_back_ling at cleft_f
        $ PlaySound("audio/cfx/spank.ogg")
        "She turned around for me."
        MARBELLA "Good enough to eat?"
        "After giving her ass a playful spank, she turned back to face me, grinning."
        hide cg_marbella_back_ling
        show marbella at cleft
        with dissolve
        MC @smile "It's too bad I couldn't take you with me on my travels."
        MARBELLA @lewd "Awww, is that because you miss my company?"
        MARBELLA @lewd "Or me keepin' your bed warm?"
        MC @smile "{i}Both.{/i}"
        MARBELLA @lewd "Mmmm... Well, then..."
    show marbella at center with ease
    "A coy Marbella stepped forward, gently taking my hand as she led me towards the bed."
    scene black with dissolve
    label replay_marbella_love_titjob:
    $ AutoMus(False)
    $ AutoAmb(False)
    $ PlayMusicRandom("mus_sex")
    MARBELLA "You just be a good meat stick and keep still for momma!"
    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene marbella_love_titjob_1 with dissolve
    $ Pause()
    "As I lay there, Marbella anxiously pressed her breasts together, squeezing my cock around her soft, pillowy chest."
    # first time variant
    if IsFirstTime():
        MARBELLA "I-I hope you know I don't do this sort of thing on the first date normally!"
        MARBELLA "Umm... I guess I just like you."
        MARBELLA "Like, {i}a lot.{/i}"
        "It was strangely adorable how desperate to avoid eye contact Marbella was,"
        "especially as she lovingly squeezed my cock between her tits, bouncing them happily as she pleasured me."
        MC "Ahhh! It's alright, I-"
        MC "Mmfghh! Like you a lot too..."
        MARBELLA "R-Really?"
        MARBELLA "Uhh, I mean."
        MARBELLA "I bet this feels r-real good for you, eh?"
        "Marbella might have failed to sound confident,"
        "but her bouncing, squeezing tits more than made up for that."
    else:
        MARBELLA "F-Fuck... I don't know if I'm ever going to get used to wrapping my tits around this thing."
        MC "Haha, are you seriously still blushing after all we've done?"
        MARBELLA "S-Shut up..."
        "Pouting, Marbella smirked as she looked down towards my cock and spat on it."
        MC "Ahhh!"
        MARBELLA "See? I ain't so shy I can't lube your meat stick up meself!"
        "The wet warmth combined with the softness of her breasts only made my cock throb painfully hard in excitement."
        MC "Ahh... Marbella!"
        MARBELLA "Shhh, just keep using them, love."
        MARBELLA "Use these big tits to your heart's content."
    # both variants cont
    MC "F-Fuck... Marbella... Mhmm... Your tits feel amazing!"
    # first time variant
    if IsFirstTime():
        MARBELLA "Y-Yes...?"
    else:
        MARBELLA "Fufu, and they're all yours, love. ❤️"
    # both variants cont
    "She trembled slightly at my words, her eyes darting back and forth to meet mine as she carefully watched my expressions."
    "{i}She wanted to know she was doing good,{/i}"
    "{i}She NEEDED to know she was good.{/i}"
    MC "Ahh! Faster... milk my cock with those pillows of yours and go FASTER!"
    MARBELLA "R-Right...!!"
    "Marbella moved faster, sweat glistening on her skin and breasts in the light as she pushed her tits harder together."
    "She bounced desperately, wearing herself out as she did her best to drain my balls with her huge tits."
    MARBELLA "C-Come on - {i}*Huff*{/i} big guy!"
    MARBELLA "A-Are you close?"
    MARBELLA "My arms are starting to ache here, you know!"
    MC "Ahh! Talk dirty to me."
    if IsFirstTime():
        MARBELLA "H-Huh?!"
        MC "I'm close! Ahh! I just need you to push me over the edge a little! Mhfhhfgh!"
        "Marbella bit her lower lip."
        MARBELLA "B-Bet you can't wait to, umm..."
        MARBELLA "Cover these big dwarven tits in your hot spunk!"
        MARBELLA "I mean, uhh, l-let me milk your huge cock!"
        "Marbella fumbled over her words."
        MARBELLA "F-Fuck am I bad at this!"
        MARBELLA "GRRR! HOW MUCH LONGER YOU BIG-COCKED-"
    else:
        MARBELLA "Oooh, you really l-love it when I do that, hm?"
        MARBELLA "You wanna hear about - {i}*Huff*{/i} how I think about you just-"
        MARBELLA "Using these big tits whenever you want?"
        MARBELLA "Mid-meeting, just... Mhmm..."
        MARBELLA "Throwing my ass down in front of guests and slamming your..."
        MARBELLA "Big."
        MARBELLA "Fat."
        MARBELLA "Cock."
        MARBELLA "Right between these chest pillows until you cover me in front of the clients with your thick spunk."
        MARBELLA "I bet you'd love that, wouldn't ya, you big-"
    $ PlaySexFx(audio.ves69_125, 1)
    scene marbella_love_titjob_2 with dissolve
    $ Pause()
    "Marbella's lips parted as her eyes widened in shock."
    "The head of my cock now forced it's way into her mouth as she her tongue thrashed and beat against me."
    MC "Oh f-fuckkk!"
    MARBELLA "Mmmfghh?!"
    "Marbella could only whimper in surprise, her hands still moving to massage my cock with her tits."
    # first time variant
    if IsFirstTime():
        MC "A-Ahh! I didn't mean to-"
        MC "Mmmfghh!"
        MARBELLA "Mmmfhhh!"
        MARBELLA "Itshhhookayhh!"
        MARBELLA "{i}*Slurp!*{/i} Yhouhh thasthhe- {i}*Slurp!*{/i}"
        MARBELLA "Shalthyyy!"
    else:
        MARBELLA "Fufu... {image=[ICON.HEART]}"
        MARBELLA "Yhoughh shuthh {i}*Slurp!*{/i} Chanthh helphh yhourshelff!"
        MARBELLA "Chanhh yhouu?"
        MC "Ah! What did I tell you woman about speaking with your mouth full?"
        MARBELLA "{b}Mmmfghhh...!{/b}"
        MARBELLA "{i}Yheshh dhearhh...{/i}"
    
    # both variants cont
    $ PlaySexFx(audio.ves69_150, 1)
    scene marbella_love_titjob_3 with dissolve
    $ Pause()
    "I began to move faster, thrusting into Marbella's mouth as wet lewd, slurping sounds escaped her lips."
    "She groaned, continuing to squeeze my cock between her soft lips and fat tits, desperate to make me finish."
    MARBELLA "Mmmfghh! {i}*Slurp!*{/i} C-Chummm!"
    MARBELLA "I whanna thastehh yhou...!"
    "As Marbella's tongue continued to work it's magic, I at last, reached my limit."
    $ ReduceInfectionFromSex("marbella")
    if IsFirstTime():
        $ UnlockGalFlag("marbella", "love_titjob", "var_first")
    else:
        $ UnlockGalFlag("marbella", "love_titjob", "var_rep")
    $ UnlockGalSceneAndGrantXp("marbella", "love_titjob")
    $ PlaySexFx(audio.ves69_finish)
    scene marbella_love_titjob_finish 
    with flash
    $ Pause()
    MC "HRGHHHHH!!"
    "Marbella gasped as she felt the first squirt of hot cum splash straight into her mouth."
    "Then a second thick splash followed, this one dripping down onto her tits glazing them, and then, a third load came..."
    "She laughed and giggled as I painted her tits white, letting my cock pop freely out from her mouth."
    $ StopReplay()
    $ AutoMus(True)
    $ AutoAmb(True)
    $ LocFlush()
    show mc at cleft
    show marbella at cright_f
    with dissolve

    # first time variant
    if IsFirstTime():
        MARBELLA @lewd "Gods, are you always this pent up?"
        MC @smile "Afraid so..."
        MC @smile "Looks like you're gonna have your work cut out for you, huh?"
        "Marbella chuckled, scooping up a small bit of my cum and licking it instinctively."
        "Noticing my grin, her cheeks burned red as she abruptly stopped."
        MARBELLA @emb "W-What?"
        MARBELLA @emb "I was just curious!"
        MC @smile "Like the taste?"
        MARBELLA @emb "It's... sweeter than I thought it would be, umm..."
        "Marbella paused for a moment, nervously looking around, unsure of what to say as she began to gather up her clothes."
        MARBELLA @emb "I best umm, head back before Gavkat and the other dwarves notice I'm gone..."
        MC @think "May I see you again?"
        "Marbella paused, her eyes wide as she answered sheepishly."
        MARBELLA @shock "You... You mean you want to-"
        MARBELLA @emb "Umm... T-That would be nice."
        MARBELLA @shock "But don't feel you have to, alright?!"
        MARBELLA @angry "I DON'T ACCEPT NO PITY DATES!"
        MC @smile "Relax, Marbella."
        MC @smile "{i}I want to see you again because I like you, not because I pity you.{/i}"
        MARBELLA @emb "... Oh."
        MARBELLA @emb "Well, if you really want to, I..."
        "Marbella paused before shaking her head."
        MARBELLA @shock "I-I got to go!"
        "Still barely dressed, she hurried out of the door with a racing heart."
        hide marbella with dissolve
        $ PlaySound("audio/cfx/doorthud.ogg")
        MC @smile "(Cute.)"
        MC @smile "(I should check in on her in a day or so.)"
    else:
        MARBELLA "Fuck me... every damn time."
        MARBELLA "You could drown a girl in this much cum, you know!"
        MC "Are you really complaining?"
        "Marbella giggled, flickering a coy smirk."
        MARBELLA "No... Just sayin'."
        MARBELLA "Anyway, I best get dressed..."
        MARBELLA "I got some work still to get done at the Crooked Shaft."
        MC "Really? You let me fuck your tits and then just rush off to work?"
        "I flashed a playful grin."
        MC "I'm gonna start thinking soon you just want me for my body!"
        "With a playful whack to my chest, Marbella rose from the bed and began to gather up her clothes."
        MARBELLA "Please, you big oaf."
        MARBELLA "You really think I'd put up with your annoying ass if it was just this big prick you had going for you?"
        "Squeezing her ass back into her clothes, Marbella blew me a kiss as she headed towards the door."
        MARBELLA "Stop by again soon, love."
    # both continued
    scene black with dissolve
    $ StopReplay()
    $ CharSetClothes("marbella", "normal")
    $ CharSetClothes("mc", "normal")
    if IsFirstTime():
        $ NoteUnlock("marbella_love_come_back_after_date")
        $ RomanceMarbella().Love_DayToSkipToAfterDate = GetGameDay() + 2
        $ QstSetProgress(RomanceMarbella, 1)
    else:
        $ SetRepeatVariant(False)
    $ LocSet("hamun_dist_docks")
    $ LocEnter()

##########################################################################################################################################
# Scene 4: 2 days later, the player returns to the Crooked Shaft and Mining Co 
label rom_marbella_love_return_after_date:    
    $ NoteLock("marbella_love_come_back_after_date")
    show marbella at cleft with dissolve
    show mc at cright_f with easeinright
    # If player had the titjob
    if RomanceMarbella().Love_TookTJ == True:
        MARBELLA @smile "I'll be with you in a minute!"
        MARBELLA @smile "I just need to-"
        "Marbella froze when she saw me, her cheeks flushing a light pink as her whole posture stiffened."
        MARBELLA @emb "O-Oh!"
        MARBELLA @emb "It's um, good to see you again!"
        MARBELLA @emb "Do you - uhh, need anything?"
        MC @smile "I was wondering if you were free."
        MARBELLA @shock "Free?"
        MARBELLA @shock "You mean, um, like to go out again?"
        MC @smile "... Well, how about it?"
        MARBELLA @emb "I... ummm..."
        MARBELLA @smile "Well why in the seven hells not?"
        MARBELLA @smile "Business is pretty slow today anyway."
        MARBELLA @think "Where do you want to go?"
    # If player did not have the titjob
    else:
        MARBELLA @smile "Oh! Nice to see you again."
        MARBELLA @talk "What brings you here?"
        MC @smile "Are you busy right now?"
        MARBELLA @shock "Hm?"
        MC @smile "You're spending too long in this office, want to head out for a bit?"
        MARBELLA @emb "Uhh... Well, alright."
        MARBELLA @smile "It is a pretty quiet day here anyway."
        MARBELLA @smile "Just let me get my things, I suppose."
        MARBELLA @smile "Where'd you want to go?"    
    # Both variants continued 
    MC @smile "We'll make a day of it."
    MARBELLA @think "In that case, you mind if we stop by the library first to see Numa?"
    MARBELLA @smile "I ain't much of a reader, but she's probably one of the only friends I got in this city."
    MARBELLA @think "You met her before?"
    # if player has met numa
    if CharIsMet("numa"):
        MC @talk "The thalay, right?"
        MARBELLA @smile "Aye! That's the one!"
    # If player hasn't
    else:
        MARBELLA @smile "She's a thalay, nice gal."
        MARBELLA @smile "You'll like her, I'm sure!"
    # fade to black 
    scene black with dissolve
    "... A short walk to the library later."
    $ LocSet("hamun_library")
    $ Pause(0.5)
    # Cut to Hamun library
    $ LocFlush(dissolve)
    show marbella at cleft
    show mc at left 
    with easeinleft
    "As we stepped into the airy, cool halls of the library, Marbella stepped closer towards the pool."
    show marbella at center with ease
    show marbella at shake
    MARBELLA "OI! NUMA!"
    MARBELLA "You 'ere?!"
    "After a few moments, a couple pockets of bubbles rose to the surface of the water, and then, climbing her way out of the pool, the thalay woman emerged."
    $ PlaySound(audio.water_splash_bath)
    show marbella at cleft with ease
    show numa at cright_f with dissolve
    NUMA @smile "A pleasure as always, Marbella."
    NUMA @smile "What brings you here?"
    "Her eyes looked up to meet mine."
    if CharIsMet("numa"):
        NUMA @smile "[player_name!t]?"
        NUMA @smile "Are you two perhaps courting?"
        MARBELLA @shock "N-No, no no no!"
        MARBELLA @emb "Umm, we're just, um..."
        MARBELLA @smile "Spending time together!"
        NUMA @smile "I see."
    else:
        NUMA @smile "And you are...?"
        MC @talk "[player_name!t]."
        NUMA @smile "A pleasure to meet you, [player_name!t]."
        NUMA @talk "I am Numa of the Thalay."
        $ CharMeet("numa")
        $ DialogueNuma().SeenFirstMeet = True
    NUMA @talk "Well, if there's something you need, let me know."
    NUMA @talk "Otherwise, feel free to use the books at your leisure."
    NUMA @smile "Just put them back in the right place when you're done."
    $ PlaySound(audio.water_splash_bath)
    hide numa with dissolve
    "With that, Numa returned to her pool, splashing around carelessly in the water as Marbella wandered around the neatly stacked aisles of books."
    show marbella at cright with ease
    show mc at cleft with ease
    MARBELLA @think "Hmmmm..."
    MC @talk "Something the matter?"
    MARBELLA @smile "Just thinkin' it's a shame they don't stack books that are a bit more, you know..."
    show marbella at blurin, cright_f
    MARBELLA @lewd "{i}Exciting.{/i}"
    MARBELLA @angry "It's all bloody history and poetry and blah blah blah!"
    MARBELLA @shock "Bloody hells! Now that's an idea!"
    MARBELLA @lewd "Huehue! Imagine a book with illustrations of sex! I bet that would sell!"
    MC @think "I'm pretty sure those things exist already."
    "Marbella's eyes continued to trace along the rows of books until she stopped."
    MARBELLA @shock "Oooh!"
    show marbella at nod
    "She pulled out one of the books."
    MARBELLA @smile "{i}The Tale of Mirgwen Glimmerfang and Dorric Forgeworth!{/i}"
    MC @think "Does it mean something to you?"
    MARBELLA @shock "How do you not know the story?"
    MARBELLA @smile "It's the most famous romance between dwarves and goblins ever!"
    MARBELLA @think "Without those two, the goblin and dwarven alliance would have never happened."
    MARBELLA @think "We'd still just be warring with each other down in the mines."
    MARBELLA @smile "I can sum the story up a bit, if you want..."
    menu:
        "I'll learn some history another time.":
            MARBELLA @talk "Suit yourself."
        "Sure, I'm interested...":
            "Marbella began to explain the history of the origins of the dwarven and goblin alliance."
            "In the beginning, both sides continued to war in the mines of Iryiad over the precious rocks and materials down there."
            "For centuries, both sides engaged in brutal, tit-for-tat warfare, often under the mountains themselves."
            "King Zorvul Glimmerfang of the goblins was ever a match for King Bramdur Forgeworth, the great dwarven king."
            "By pure happenstance, Mirgwen Glimmerfang, the goblin princess, and Prince Dorric Forgeworth, heir to the dwarven kingdom, were both reluctantly seeking suitors for marriage."
            "Of course, these marriages were arranged by their fathers, and neither side was supposed to ever meet..."
            "By chance, during a terrible storm, the crows delivering the letters to their suitors became confused."
            "By accident, Mirgwen and Dorric's letters were wrongly delivered to each other."
            "The two, perhaps amused at how different their personalities were,"
            "Dorric being a poetic romantic and Mirgwen famous for her wit and occasional crudeness, continued to write to each other, unaware of exactly who they were writing to, with both simply marking their names as 'D' and 'M' respectively."
            "The two agreed to meet in secret. Mirgwen, expecting to meet another goblin warlord, and Dorric, believing he was speaking to Lady Margott, a noble dwarven lady friendly with the family."
            "Mirgwen bathed naked in the hot spring waters, only to be found much earlier than expected by Dorric."
            "The two drew weapons, but quickly realized who the other person was."
            "After some brief confusion, the two left and continued to write to each other. Dorric was completely overtaken by Mirgwen's beauty, not realizing goblins could look like that."
            "Eventually, the two fell in love, and triggered a crisis by openly announcing their engagement."
            "On the verge of the war becoming even more violent, Dorric and Mirgwen pleaded with their fathers to meet, threatening to leave Iryiad if they did not."
            "Reluctantly, both sides met, and to their surprise, King Zorvul and Bramdur got along remarkably well."
            "Having never met before, the two first came to have a begrudging respect for the other and then, realizing the full potential of what this marriage could achieve, became allies... and finally, friends."
            "The marriage was approved to the shock of all Iryiad, but to this day, the dwarven and goblin alliance has only grown in strength, with the kingdoms now so entangled in blood, politics, and culture, they live as 'one people, two races.'"
            MARBELLA @smile "It's pretty much the most beloved story amongst dwarven kind."
            MARBELLA @think "Though I hear the goblins tell it differently..."
            MC @think "How do they tell it?"
            MARBELLA @emb "That Mirgwen had the biggest arse and tits in the land to boot,"
            MARBELLA @emb "and Lord Dorric and half the kingdom were desperate to shag her."
            MC @think "... So, which one's true?"
            MARBELLA @think "{i}*Ahem*{/i} We dwarves prefer the more dignified version."
            MARBELLA @emb "... Though there is mention of her, ummm... 'assets' even in our stories."
            MC @smile "Heh."
    MARBELLA @talk "Alright, that's enough of being here."
    show marbella at center_f with ease
    MARBELLA @smile "Where to next, big guy?"
    "I pondered the thought for a moment."
    MC @smile "... Have you ever actually been to the arena?"
    "Marbella's head tilted."
    MARBELLA @think "The arena?"
    MARBELLA @think "You really think I got time to waste watching people bash each other's skulls in for coin?"
    MC @smile "{i}Would you like to see at least one match?{/i}"
    "Marbella pondered the thought for a few moments, then shrugged."
    MARBELLA @smile "Well, why not."
    MARBELLA @smile "Might as well see what all the fuss is about..."
    scene black with dissolve
    $ LocSet("hamun_arena_int")
    $ Pause(0.5)
    $ LocFlush()
    with dissolve
    show mc at center
    show marbella at cleft
    with easeinleft
    MARBELLA @think "So... Quick question."
    MARBELLA @sad "Do umm... people often fight to the death, or uh, does someone step in, or-"
    MC @talk "It depends on the match. Some matches, especially tournament ones, are usually until the other side yields, or sometimes a specific referee will be brought in to call it."
    MC @talk "Death matches are pretty much guaranteed against monsters, for obvious reasons."
    MC @talk "But that doesn't mean there {i}isn't{/i} death matches."
    MC @talk "Those still happen, but you always walk in knowing you're in one, so it isn't like,"
    MC @surprised "Surprise! You're fighting to the death now!"
    MC @talk "At least, that's commonplace for Alderay... Other places may be different."
    MARBELLA @sad "I see..."
    MARBELLA @sad "I know times are tough, gotta feel a little sorry for the poor bastards who feel they have to join the arena just to get by."
    MC @think "Well, not all of them do."
    MC @talk "Some just want glory... Others just want to prove they're the toughest bastards around."
    MARBELLA @think "Hmmm..."
    MARBELLA @talk "Anyway then, you better get us tickets."
    MC @smile "I'll be back now."
    scene black with dissolve
    scene cg_arena_party_1
    with dissolve
    $ PlaySound("audio/cfx/crowd_cheer.ogg")
    "... After buying our tickets, Marbella and I sat and watched as the arena battle unfolded."
    "A party of four, one mage, an archer, a sword-and-shield user, and a muscular heavy axeman, were to battle against a group of skaliths."
    "At first the party did well, cutting down the skaliths with only minor injuries."
    "The axeman even severed one of the skaliths' heads completely in half."
    "... But the party had signed up to fight the skaliths in waves."
    "Two waves..."
    "Three waves..."
    "Whatever madness or overconfidence possessed them to agree to such a match soon caught up with them."
    scene cg_arena_party_2
    with dissolve
    $ PlaySound("audio/cfx/crowd_clap.ogg")
    "Overwhelmed, the archer fell first, wounded lightly a couple times, the poison from the skaliths' blades finally catching up as he tumbled forward into the sand, gasping for air."
    "Once he fell, the rest fell shortly after."
    "The swordsman fell next. Without his flank covered, a skalith plunged its claws deep into his back before sinking her teeth into his neck and tearing out a chunk of flesh."
    "With the axeman occupied, the mage was left defenseless and torn apart. She screamed in terror as they grabbed hold of her limbs, ripping her apart like the legs from a spider."
    "Finally, the axeman continued to swing futilely until he too was brought down in a fury of teeth and claw."
    "The crowd cheered, but Marbella appeared a little... sheepish."
    $ LocFlush(dissolve)
    show mc at center
    show marbella at cleft
    with easeinleft
    MC @think "Are you alright?"
    MARBELLA @scared "That was... more gory than I was expecting."
    MC @sad "Ahh, they don't normally go quite like that..."
    MC @think "Are you okay?"
    MARBELLA @sad "Yes, just..."
    MARBELLA @think "Is it fucking weird I'm suddenly really horny?"
    MARBELLA @think "Like, that was pretty fucked to watch... and now, all I can think about is sex?"
    menu:
        "Oh you're very weird.":
            MARBELLA @angry "Oh ha ha, lap it up."
            MC @smile "What?"
            MC @smile "That you're my little weirdo?"
            MARBELLA @emb "Laugh while you can, big guy."
        "You'd be surprised how quickly the first thing people do after seeing death is jump into bed with someone...":
            MARBELLA @think "Guess I ain't really been around enough death to know."
    MARBELLA @talk "{i}*Sigh*{/i} I'm kinda starved..."
    MARBELLA @smile "Why don't we head towards the market and grab some food?"
    MC @smile "Why not?"
    scene black with dissolve
    $ LocSet("hamun_market")
    $ Pause(0.5)
    $ LocFlush(dissolve)
    "... After heading to the marketplace, Marbella and I ordered some food from one of the many stalls."
    "Wandering from stall to stall, Marbella inquisitively checked out the many wares on offer."
    show mc at cright_f
    show marbella at center_f
    with easeinright
    show marbella at center
    MARBELLA @smile "Mmm, you know... If you'd asked me back in Iryiad if I'd ever eat 'desert rat on a stick,' I think I might have bashed your head in."
    MARBELLA @talk "But it's pretty good with some salt."
    MC @talk "It's getting kind of late." 
    MARBELLA @think "Aye... It is."
    MARBELLA @blush "Umm... Can I ask you something?"
    MC @think "What is it?"
    MARBELLA @think "Like, {i}what are we exactly?{/i}"
    MC @surprised "Hm?"
    MARBELLA @sad "It's just... I'm not really interested in just a quick fling, you know?"
    MARBELLA @sad "I get it, you're an adventurer and got all kinds of fucked up things that'll keep you away for gods know how long."
    MARBELLA @sad "And I guess I'm alright with that..."
    MARBELLA @sad "{i}If I actually matter.{/i}"
    MARBELLA @sad "If not though, I'd rather us just stay friends."
    menu:
        "{image=[ICON.HEART]} You matter to me... Marbella.":
            MARBELLA @emb "... O-Oh."
            MARBELLA @emb "F-Fuck, mate, um..."
            MARBELLA @emb "I wasn't really expecting-"
            MARBELLA @emb "{i}*Deep breath*{/i}"
            "Marbella's hand reached out to grab mine."
            MARBELLA @talk "Fuck it, take me back to yours."
            $ CharSetLover("marbella")
            show marbella at shake
            MARBELLA @lewd "{i}Now.{/i}"
            label marbella_love_69_repeat:
            scene black with dissolve
            if IsFirstTime():
                "... Practically scooping Marbella up into my arms, she squealed as I hurried back to my room at {i}The Pale Dragon.{/i}"
                $ LocSet("hamun_hookah_bar_room")
                "It didn't take long for the two of us to be stripped of our clothes, locked in a passionate embrace as she pushed her hot tongue into my mouth."
                "Suddenly, as she felt my cock brush up against her bush and the wetness of her slit, she pushed me away."
                $ CharSetClothes("marbella", "naked")
                $ CharSetClothes("mc", "naked")
                $ LocFlush()
                show mc at cleft
                show marbella at cright_f
                with dissolve
                MARBELLA @shock "W-Wait!"
                MC @think "Marbella?"
                MARBELLA @emb "I... I'm still not ready for that."
                MC @sad "Oh..."
                MARBELLA @shock "BUT...!"
                MARBELLA @emb "T-There is something I always wanted to try."
                MC @think "... Oh?"
                scene black with dissolve
                "Marbella coyly smirked as she stepped closer." 
            else:
                $ LocSet("hamun_hookah_bar_room")
                "Later, I heard a knock at the door as Marbella hurried inside."
                $ LocFlush()
                show mc at cleft
                show marbella at cright_f
                with dissolve
                MARBELLA @smile "Phew! Finally finished up with all that paperwork!"
                MARBELLA @lewd "Now then love, what was it you promised me again?"
                MC @smile "That I was going to remind you why I have the best tongue in the city?"
                MARBELLA @lewd "Ahh, a man after me own heart."
                MARBELLA @lewd "And pussy... and ass."
                $ CharSetClothes("marbella", "naked")
                $ PlaySound("audio/cfx/cotton_drop.ogg")
                "Marbella dropped her clothes to the floor coyly, swinging her hips as she stepped closer towards me."
                MARBELLA @lewd "Well... Clothes off, big boy."
                scene black with dissolve
                $ CharSetClothes("mc", "naked")
                "{i}I did as she asked...{/i}"
            label replay_marbella_love_69:
            $ AutoMus(False)
            $ AutoAmb(False)
            $ PlayMusicRandom("mus_sex")
            MARBELLA "Gonna need you to lift me up for this one, big boy."
            MARBELLA "And-"
            MARBELLA "Eeeeep!"
            "Hovering my cock in front of Marbella's face, I held on eagerly to her small body, her pussy inches away from my face."
            if IsFirstTime():
                MARBELLA "W-Whoaaa...!"
                MARBELLA "This is - Mhmm! M-More disorienting than I thought it would be!"
            else:
                MARBELLA "Weeeeeee!"
                MARBELLA "You know, I'm kind of getting used to being yer little ragdoll slut now!"
            $ PlaySexFx(audio.ves69_125, 1)
            scene marbella_love_69_1 with dissolve
            $ Pause()
            "Her womanhood glistened in excitement as the scent of her sweet pussy only hardened my cock in excitement."
            "My hard cock prodded at her cheek, and Marbella, laughing and cheeks now flushed red from arousal, sheepishly opened her mouth obediently."
            "Gently, as I pushed the head into her mouth, her tongue thrashed and beat against my meat as I began to push a few more inches into her mouth."
            "I pushed my head forward, nestling my face between her cheeks as I dug my tongue deep into her sweet pussy, lapping up the juices."
            MARBELLA "{i}*Slurp!*{/i} Mmdffghh...!"
            MARBELLA "OOOOOH!"
            MARBELLA "(F-Fuckkkk meeee...!)"
            if IsFirstTime():
                MARBELLA "(He's really - {i}*huff*{/i} digging in good there!)"
                MARBELLA "(Oh gods... Mmmfgh... That feels s-sooo nice!)"
            else:
                MARBELLA "(Gods - {i}*huff*{/i} He eats cunt like his life depends on it!)"
                MARBELLA "{i}*Slurp!*{/i} Shhho... {i}*Slurp!*{/i} FHUCKINHH' GHOODHHH! Mmmfghh...!"
            $ PlaySexFx(audio.ves69_150, 1)
            scene marbella_love_69_2 with dissolve
            $ Pause()
            "Her body twitched and shivered with excitement as I twisted and prodded with my tongue."
            "Marbella rewarded me in kind, trying to take my cock deeper as she eagerly sucked on the member."
            MARBELLA "{i}*Slurp!*{/i} Mmfghh!"
            if IsFirstTime():
                MARBELLA "Howhh arhyhuuu shooo bhighhh? {i}*Slurp!*{/i}"
                "Not wanting her to talk too much with her mouth full, I gently pulled my tongue back to circle around her asshole."
                MARBELLA "MMMFGHHH!"
                MARBELLA "THATSHHH MHYHH ASHHH...!"
            else:
                MARBELLA "Mmfghh! {i}*Slurp!*{/i} I lhuvhh thishh bhighh chockhhh shooo mhuchh!"
                "Playfully, I once again circled my tongue around the rim of her asshole, prodding at the hole."
                MARBELLA "Mmmfghh! Nhaughtyhh!"
                MARBELLA "Yhouhh rheallhh lhikee eathinghh therehhh! {i}*Slurp!*{/i} dhonthh yhouhh?"
            "Marbella shuddered once again as I rimmed her hole, gently pressing an inch or two of my tongue into her ass before retreating."
            "Marbella's mouth sucked harder, her lips forming a tight seal as I helped her, thrusting forward to force a couple inches into her throat."
            "Lewd, choking sounds escaped her wet lips as I felt her squirm in my arms,"
            "her moans growing louder and more frequent as she sucked my cock clumsily, but with more than enough enthusiasm to make up for it."
            if IsFirstTime():
                MARBELLA "(W-What is happening?!)"
                MARBELLA "(Gods, this is fucking crazy!)"
                MARBELLA "(He could kill a woman with this thing?!)"
                MARBELLA "(F-Fuckkkk...! His tongue! This crazy bastard! Mmmfghh...!)"
                MARBELLA "(H-He's gonna make me cum!)"
                MARBELLA "(He's gonna-)"
            else:
                MARBELLA "(F-Fuck... It feels amazing.)"
                MARBELLA "(Fufu, if me mother and father could see me now, they'd have a heart attack!)"
                MARBELLA "(He just holds me up like I'm a feather or something... ❤️)"
                MARBELLA "(God, I could fuckin' cum just thinking about it!)"
            "Marbella trembled and shook, her eyes rolling back as her whole body seemed to coil and tighten as she suddenly climaxed."
            if IsFirstTime():
                $ UnlockGalFlag("marbella", "love_69", "var_first")
            else:
                $ UnlockGalFlag("marbella", "love_69", "var_rep")
            $ UnlockGalSceneAndGrantXp("marbella", "love_69")
            $ PlaySexFx(audio.ves69_finish)
            $ ReduceInfectionFromSex("marbella")
            scene marbella_love_69_finish with flash
            $ Pause()
            MARBELLA "MMMMFGHHHHHHHHHH...!!"
            "Her body's tension, after a few moments, began to pass, and suddenly she seemed so strangely limp and soft once again."
            "As my balls slapped up against her face, and her cheeks seemed to bulge out as I stuffed her little mouth with my fat cock,"
            "I began to feel my aching heavy balls ready to drown the little dwarf in my thick cream."
            "Finally, the warm, wet sensation of her mouth and its tight seal became too much for me."
            "Pushing my cock as deeply as I could into her, she let out a muffled squeal as I grunted, pouring my thick load into her mouth."
            MC "HRGHH! SWALLOW IT ALL!"
            "Gargling, squealing sounds escaped Marbella's full mouth as she desperately swallowed down my load."
            "The thick seed spilled from the edges of her mouth, overflowing and dripping down onto the floor as her eyes once again rolled to the back of her skull."
            "Slowly, I pulled my cock away as she coughed up some of the cum, gasping for air as I gently lowered her back onto the floor."
            "She wiped at her mouth with her arm, shakily rising back to her feet as she looked me up and down."
            $ StopReplay()
            $ LocFlush()
            show mc at cleft
            show marbella at cright_f
            with dissolve
            if IsFirstTime():
                MARBELLA @emb "That was..."
                MARBELLA @lewd "{i}Fuckin' amazing.{/i}"
                MC @smile "You think that was fun, I can show you some of {i}my{/i} favorite positions next."
                "Marbella stepped back, but not nervously this time, but with a playful giggle."
                MARBELLA @smile "You'll have to show me real soon."
                MC @think "Do you want to stay here tonight?"
                MC @smile "I even promise only to {i}slightly{/i} grope you in the night."
                "Marbella chuckled, her mouth opening to say something before she stopped herself."
                MARBELLA @smile "I-"
                MARBELLA @talk "... Maybe next time, alright?"
                MC @smile "Alright."
                $ CharSetClothes("marbella", "normal")
                $ PlaySound("audio/cfx/clothes_drop.ogg")
                "I watched the little dwarf bend over to grab her clothes from the floor, giving me an eyeful of her tight pussy and ass as she re-dressed herself."
                MARBELLA @talk "Swing by tomorrow when you're free."
                MARBELLA @talk "Got something pretty exciting coming up."
                "Marbella smiled, blowing me a kiss as she closed the door behind her."
                show marbella at cright
                hide marbella with easeoutright
                with dissolve
                $ PlaySound("audio/cfx/doorthud.ogg")
                MC "(Something exciting, huh?)"
                MC @smile "(Wonder what that could be?)"
                $ QstSetProgress(RomanceMarbella, 2)
                $ NoteUnlock("marbella_love_come_back_after_walk")
                scene black with dissolve
                $ AutoMus(True)
                $ AutoAmb(True)
                $ CharSetClothes("mc", "normal")
                $ CharSetClothes("marbella", "normal")
                $ TimeAdvTo(TIME_VISUAL_DAWN)
                $ LocEnter()
            else:
                MARBELLA @lewd "I ever tell you I love sucking your dick?"
                MC @smile "All the time, but I like to hear you repeat it."
                MARBELLA @lewd "Typical bloody man."
                MC @smile "Bring your ass to bed already."
                MARBELLA @smile "Oooh, ordering me around now, huh?"
                MARBELLA @angry "NO SNEAKING IT IN MY ARSE WHILE I SLEEP!"
                MC @smile "I'll wait till you wake up before I try."
                MARBELLA @smile "Good boy."
                scene black with dissolve
                $ AutoMus(True)
                $ AutoAmb(True)
                $ CharSetClothes("mc", "normal")
                $ CharSetClothes("marbella", "normal")
                "Marbella climbed into the bed with me, folding up into a small, warm ball for me to cuddle."
                "As she pushed her soft ass up against me, the two of us quickly drifted off to sleep."
                "By the time morning light came, she was gone."
                $ TimeAdvTo(TIME_VISUAL_DAWN)
                $ SetRepeatVariant(False)
                $ LocEnter()

        "We should just stay friends.": 
            MARBELLA @sad "Ahh..."
            $ RomanceMarbella().Love_IsPlato = True
            MARBELLA @talk "Well then, this has been great, but I should probably head back."
            MARBELLA @talk "Thank you... For not leading me on."
            "Marbella rose up onto her tiptoes, gently giving me a kiss on the cheek before taking her leave."
            MARBELLA @smile "Swing by tomorrow by the way, got something to talk to you about."
            MC @sad "(It's for the best.)"
            $ QstSetProgress(RomanceMarbella, 2)
            $ NoteUnlock("marbella_love_come_back_after_walk")
            $ LocEnter()

##############################################################################################################################################################
#The player returns to the Crooked Shaft and Mining Co the next day - scene auto plays from entering the building
label rom_marbella_love_return_after_walk:
    show marbella at cleft
    with dissolve
    MARBELLA @scared "Fuck! Fuck! Fuck...!"
    show mc at cright_f with easeinright
    $ NoteLock("marbella_love_come_back_after_walk")
    MC @think "Marbella? What's wrong?"
    show marbella at shake
    MARBELLA @scared "The guard! He's fucking dead!"
    MC @surprised "What?"
    MARBELLA @shock "I don't know! Apparently, something fucking ripped the poor bastard apart!"
    MC @think "Ripped him apart?"
    MC @serious "The GTC maybe?"
    MARBELLA @sad "No chance, the last thing the GTC wants is the trade war to spill over into blood in the streets."
    MARBELLA @think "There would be riots and open slaughter across town to throw them out!"
    MARBELLA @scared "Besides, this was some kind of... animal... monster...?"
    MARBELLA @scared "I don't know, point is, Lord Zanzibat sent word he wants to speak to you."
    MC "(Fuck.)"
    MC @talk "Alright, I'll be right back."
    show mc at blurin, cright
    MARBELLA @shock "Wait!"
    show mc at blurin, cright_f
    MC @think "What is it?"
    show marbella at center with ease
    MARBELLA @sad "I... Be safe, alright?"
    MARBELLA @sad "Damn it... What I had planned will have to wait until this is solved."
    MC @talk "Don't worry, I'll be back soon."
    MC @talk "{i}I promise.{/i}"
    show mc at blurin, cright
    hide mc with easeoutright
    "Marbella offered a faint, hopeful smile as she watched me leave."
    $ LocSet("hamun_dist_docks")
    MARBELLA @sad "(He's doing so much for me.)"
    MARBELLA @sad "(...Shit.)"
    scene black with dissolve
    $ NoteUnlock("marbella_love_visit_zanzibat_after_guard_killed")
    $ QstSetProgress(RomanceMarbella, 3)
    $ LocEnter()


################################################################################################################################################################
#The player returns to speak to Lord Zanzibat - scene auto plays
label rom_marbella_love_come_to_zanzibat_after_guard_killed:
    $ NoteLock("marbella_love_visit_zanzibat_after_guard_killed")
    show zanzibat at center_f 
    with dissolve
    ZANZIBAT @talk "Ah, there you are."
    ZANZIBAT @talk "I trust Marbella has told you what happened to my man?"
    MC @think "Are you going to send a replacement?"
    ZANZIBAT @talk "Of course, he's already on his way."
    ZANZIBAT @talk "But I want to hire your services once more, find out what fool would dare try to attack me."
    menu:
        "This wasn't part of the deal... What's in it for me?":
            ZANZIBAT @smile "Coin. Plain and simple."
            ZANZIBAT @talk "Five hundred to be exact."
            menu:
                "Fine.":
                    ZANZIBAT @talk "Excellent."
                "I'm not an assassin... and I'm certainly not that cheap." (Req_Barter = 16):
                    $ RomanceMarbella().Love_TheFaceReward = 800
                    ZANZIBAT @smile "Hmph. Eight hundred, that should more than suffice to deal with whatever this nuisance is."
        "Just point me in the right direction.":
            ZANZIBAT @talk "Eager... Good."
    ZANZIBAT @talk "From what my sources have told me, similar attacks have been occurring quietly all over the city."
    ZANZIBAT @talk "Whatever this creature is, it's likely highly intelligent to avoid detection."
    ZANZIBAT @smile "{i}But I suppose the guards don't have the 'Beast of Novaras' on their payroll, do they?{/i}"
    "Lord Zanzibat produced a small rag covered in a kind of thick blue blood."
    ZANZIBAT @talk "This was recovered from the scene, it seems my man managed to put up a fight before he was killed."
    ZANZIBAT @think "Maybe you can track the blood?"
    "I grabbed hold of the rag uncertainly. Could Shyahtan track the scent?"
    "I smelled the vile, blood-stained rag, and was hit with a scent of... sweetness?"
    MC "(Not what I was expecting...)"
    ZANZIBAT @talk "Find this creature {b}and bring me its head.{/b}"
    MC @talk "I'll do what I can..."
    $ NoteUnlock("marbella_love_deal_with_the_face")
    $ QstSetProgress(RomanceMarbella, 4)
    $ LocEnter()

label rom_marbella_love_theface_para_memo:
    $ RomanceMarbella().Love_SeenTheFaceShyahMemo = True
    show mc at center_f with easeinright
    MC "(Can you actually track the creature from this?)"
    SHYAHTAN "(Yes...)"
    SHYAHTAN "(And I want to devour it.)"
    show mc at blurin, center
    MC @surprised "(What?!)"
    SHYAHTAN "(Devouring it will prove beneficial to us in the long run due to its genetic makeup.)"
    SHYAHTAN "(It is a mostly nocturnal predator... We should look out for it in the evening.)"
    SHYAHTAN "(I will let you know when I have its scent.)"
    $ LocEnter()


###############################################
# (the face sequence happened)
###############################################

# After either killing or letting 'The Face' go, 
# the player returns to Lord Zanzibat
label rom_marbella_love_zanzibat_aboutthatcreature:
    ZANZIBAT @think "Has it been dealt with?"
    menu:
        "Yes." (AppearIf = QstGetProgress(RomanceMarbella) == 5):
            if RomanceMarbella().Shared_TheFaceFate == "dead":
                ZANZIBAT @smile "My men did report finding the body of some strange creature torn apart..."
                ZANZIBAT @smile "I presumed this might be the creature, but was waiting to hear your confirmation."
                ZANZIBAT @smile "Well done, take your coin." 
            elif RomanceMarbella().Shared_TheFaceFate == "negotiated":
                ZANZIBAT @think "I am going to presume, given that you don't have the thing's head, you didn't kill it?"
                MC @serious "It won't be coming back."
                ZANZIBAT @angry "I wanted its head to send a message!"
                ZANZIBAT @sad "{i}*Sigh*{/i} How disappointing..."
                ZANZIBAT @talk "You'll get two hundred coins."
                MC @surprised "What?!"
                ZANZIBAT @angry "The deal was that you killed the damn thing, not scared it off!"
                ZANZIBAT @talk "Half the pay for half the job..."
                "I grit my teeth, stopping myself from protesting for Marbella's sake."
            $ NoteLock("marbella_love_report_theface")
            $ PlayerAddItem("gold", RomanceMarbella().Love_TheFaceReward)
            ZANZIBAT @talk "A replacement guard should be with your dwarven friend shortly."
            ZANZIBAT @smile "And with that, let's put this nasty little business behind us and move on."
            ZANZIBAT @talk "Is there anything else you need?"
            $ QstSetProgress(RomanceMarbella, 6)
            $ NoteUnlock("marbella_love_return_to_marbella_after_face")
            call processDialogue("zanzibat_root") from _call_processDialogue_80
            $ LocEnter()
        "No.":
            ZANZIBAT @talk "Then stop wasting my time."
            $ LocEnter()

####################################################################################################################################
# The player returns to Marbella to report the news 
label rom_marbella_love_return_after_face:
    $ NoteLock("marbella_love_return_to_marbella_after_face")
    MARBELLA @smile "Ah! That's great news!"
    MARBELLA @emb "Gods... You're a real white fucking knight, you know that?"
    MC @smile "Don't mention it."
    MARBELLA @talk "{i}Phew{/i} Well, now that crisis is over, swing by tomorrow once I've sorted out this paperwork."
    MARBELLA @smile "I can finally talk to you about my next big plan!"
    MC @think "Next big plan?"
    MARBELLA @talk "Don't you worry that noggin' of yours too much."
    MARBELLA @talk "I'll tell you allllll about it tomorrow."
    MC @smile "Then I'll see you then, Marbella."
    MARBELLA @sad "[player_name!t]."
    MC @think "What is it?"
    MARBELLA @sad "Just..."
    MARBELLA @smile "Thanks for lookin' out for me, alright?"
    MARBELLA @smile "I'm not used to havin' reliable friends."
    MC @smile "Anytime, Marbella."
    MARBELLA @emb "..."
    if RomanceMarbella().Love_IsPlato == True:
        scene black with dissolve
        $ LocSet("hamun_dist_docks")
        jump rom_marbella_love_return_after_face_ending
    MARBELLA @emb "Umm..."
    MARBELLA @emb "You maybe wanna grab a drink or something this evening?"
    MARBELLA @lewd "I could uhh, swing by {i}The Pale Dragon{/i} later."
    "Marbella inched closer towards me, swaying her hips cutely."
    MC @smile "I'll be waiting."
    MARBELLA @lewd "Perrrrrfect."
    MARBELLA @talk "For now though, I've got some urgent paperwork to catch up on now that I've got a minute."
    MARBELLA @lewd "Let's meet up later, handsome."
    scene black with dissolve
    "Later that day..."
    $ TimeAdvTo(TIME_DAY_END)
    $ LocSet("hamun_hookah_bar")
    if IsFirstTime():
        $ LocFlush()
        show marbella at cright_f
        with dissolve
        show mc at cleft with easeinleft
        MARBELLA @smile "There you are!"
        MC @smile "Evening."
        "My eyes wandered up and down Marbella as she brushed her hair over her shoulder."
        MARBELLA @emb "{i}*Ahem*{/i}"
        MARBELLA @emb "So, uhh... I'll get us the first round?"
        scene black with dissolve
        "A few merry drinks in, Marbella continued to playfully find new ways to push her body and breasts up against me throughout the evening."
        $ LocFlush()
        show mc at cleft
        show marbella at center_f
        with dissolve
        MARBELLA @laugh "Haha! You're so funny!"
        MARBELLA @lewd "Listen, mmm... It's getting kinda late, could you walk me back, handsome?"
        MC @smile "Sure thing, Marbella."
        scene black with dissolve
        $ LocSet("hamun_dist_docks")
        "As I began to escort Marbella back home, she suddenly reached out to grab my hand, pulling me off in a different direction."
        MC @surprised "Marbella!"
        MARBELLA @lewd "Come with me, love."
    else:
        label marbella_love_alleyway_repeat:
        "{i}Later after a few drinks at The Pale Dragon...{/i}"
        MC @surprised "Again?!"
        MARBELLA @lewd "Never mind making love, I want yer now!"
        scene black with dissolve
        $ LocSet("hamun_dist_docks")
    $ LocFlush()
    show marbella at cright_f
    show mc at center
    with dissolve
    "Practically dragging me down into some dark alleyway, Marbella suddenly threw herself onto me."
    MARBELLA @lewd "I wanted to wait till we got back to mine, but I can't wait a second longer."
    "Between her desperate fumbling kisses, she began to pull off her own clothes."
    MARBELLA @lewd "Fucking stop standing there and take your bloody pants off!"
    "As I fumbled and did as she asked, there was a nervous energy shared between us as she threw herself forward towards me."
    "My cock stiffened as it brushed up against her pubic hair as I held her leg up."
    with dissolve
    label replay_marbella_love_alleyway:
    $ AutoMus(False)
    $ AutoAmb(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene marbella_love_alleyway_idle with dissolve
    $ Pause()
    if IsFirstTime():
        MC "Marbella... {i}*Huff*{/i}"
        MC "Are you sure you want this?"
        "Marbella's cheeks flushed as she lightly pushed herself against me."
        MARBELLA "Listen, handsome..."
        MARBELLA "I ain't some precious little thing made of glass."
        MARBELLA "{i}Yer special to me... and I know what I want.{/i}"
        MARBELLA "{i}And what I want is you, alright?{/i}"
        MARBELLA "So quit yer worrying, andddd..."
    else:
        with dissolve
        MARBELLA "Fuckin' hells, I'm on fire!"
        MARBELLA "Don't keep me waiting!"
        MARBELLA "Put it in already!"
    
    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene marbella_love_alleyway_1 with dissolve
    $ Pause()
    "I pushed forward, thrusting my cock into Marbella's tight, wet snatch as her mouth hung agape."
    "Her arms tightened around me as her hands coiled and closed to grip onto me as I slowly began to move in and out of her."
    if IsFirstTime():
        MARBELLA "{i}*Huff!*{/i} Oh fuck! FUCK!"
        MARBELLA "Gods, f-feeling it stretch me is-"
        MARBELLA "Oooooooh!"
        MARBELLA "F-Fuck... I didn't think I'd be able to take it!"
    else:
        MARBELLA "Ooooh...!"
        MARBELLA "I fuckin' love you!"
        MARBELLA "{i}*Huff!*{/i} Mmfghh...!"
        MARBELLA "I fuckin' love you SO MUCH!"
        MC "And my big cock?"
        MARBELLA "Hahaha! And I love your big, stupid COCK!"
    "Marbella's hot breath touched my throat as her tight, wet womanhood squeezed around me."
    MARBELLA "H-Harder..."
    MARBELLA "D-Don't treat me like some - Ahh! maiden, love!"
    MARBELLA "C-Come on."
    MARBELLA "{i}Take me.{/i}"
    $ PlaySexFx(audio.nijah_miss_1, 2)
    scene marbella_love_alleyway_2 with dissolve
    $ Pause()
    "I did as Marbella asked, moving faster in her as her moans grew louder."
    MARBELLA "That's it! Mmfghh!"
    MARBELLA "M-More... {i}More!{/i}"
    "Marbella pushed her face forward into my chest to try and muffle her scream as she tightened around me."
    MARBELLA "MMMMFGHHH...!"
    MARBELLA "(Mwhaa! I can't help it!)"
    MARBELLA "(Every time I see him I just want to kiss him!)"
    MARBELLA "(I wanna sit on his big stupid face and have him bend me over my desk and-)"
    MARBELLA "(AHHH! WHY THE FUCK AM I FEELING LIKE THIS?!)"
    MARBELLA "(It's never been - {i}*Huff*{/i} like this before!)"
    MARBELLA "(Please, please, please! Come see me every day!)"
    MARBELLA "(AHHH! WHAT THE FUCK?! IT'S SOOOO - Mmmfghhh!)"
    MARBELLA "(I love this cock! I love this cock! I love this cock!)"
    "Marbella seemed completely lost in thought as she threw herself forward."
    "Slamming her hips against mine with reckless abandon as I began to feel my balls tighten, my cock ready to burst."
    MC "M-Marbella! {i}*Huff*{/i}"
    MC "I'm gonna-"
    MARBELLA "(In me, in me, IN ME!!)"
    "Marbella refused to let go, ignoring my warnings as she squeezed tightly around me."
    "Doing her best to pull me in and hold me there."
    if IsFirstTime():
        $ UnlockGalFlag("marbella", "love_alleyway", "var_first")
    else:
        $ UnlockGalFlag("marbella", "love_alleyway", "var_rep")
    $ UnlockGalSceneAndGrantXp("marbella", "love_alleyway")
    $ ReduceInfectionFromSex("marbella")
    $ PregRoll("marbella")
    $ PlaySexFx(audio.nijah_miss_finish)
    scene marbella_love_alleyway_finish with flash
    $ Pause()
    "Finally, as I slammed my cock deeply into her, burying it to the hilt,"
    "Marbella gasped, clawing her nails down me as I unloaded inside of her."
    MARBELLA "{i}*Gasps!*{/i}"
    MC "F-FFUCKKKK...!"
    MC "{i}*Huff*{/i}... Marbella...{i}*Huff*{/i} I-"
    MARBELLA "Shhh, it's alright love."
    MARBELLA "... Ha, you really filled me up. ❤️"
    $ StopReplay()
    scene black with dissolve
    "We stood there for a few moments, holding each other as my cock slowly deflated inside of her."
    "Eventually we pulled apart as Marbella began to pull back up her shorts."
    $ LocFlush()
    show mc at cleft
    show marbella at cright_f
    MARBELLA @smile "I think we both needed that."
    MC @think "Figured you would be more of a... 'take me slowly in bed' kind of girl."
    MARBELLA @emb "{i}I want it like that with someone special.{/i}"
    "Marbella's eyes wandered over me as her cheeks continued to remain flushed."
    MARBELLA @emb "Someone like..."
    "She paused, staring at me a moment before shaking her head."
    MARBELLA @emb "C-Come on, now you need to ACTUALLY walk me home!"
    MC @smile "As you command, my lady..."
    scene black with dissolve
    $ AutoMus(True)
    $ AutoAmb(True)
    "After that, I walked Marbella back to {i}The Crooked Shaft,{/i} as she happily clung to my arm."
    "Every so often, she'd reach back to adjust herself, and I was certain I could catch a glimpse of my seed running down her leg."
    $ LocSet("hamun_miningco")
    $ LocFlush()
    show marbella at cleft
    show mc at cright_f
    with dissolve
    MARBELLA @smile "Thanks for walking me back, handsome."
    MC @smile "Well, you certainly made it {i}memorable.{/i}"
    MARBELLA @lewd "Mmmm, don't expect that every time."
    MARBELLA @lewd "Come 'ere though..."
    hide marbella
    hide mc
    with dissolve
    show cg_marbella_mc_kiss at center_f
    with dissolve
    "As I knelt down, Marbella threw herself into my arms, planting her lips against mine."
    "When she pulled away, she smiled, her eyes shyly avoiding mine."
    hide cg_marbella_mc_kiss
    with dissolve
    show mc at cright_f
    show marbella at cleft
    with dissolve
    MARBELLA @lewd "G-Goodnight, love."
    MC @smile "Goodnight, Marbella."
    scene black with dissolve
    $ LocSet("hamun_dist_docks")
    if IsFirstTime():
        MC @smile "(Hmm... me and Marbella seem to be getting closer than ever.)"
        MC @think "(I wonder what this big plan of hers is, exactly?)"
    jump rom_marbella_love_return_after_face_ending

label rom_marbella_love_return_after_face_ending:
    if IsFirstTime():
        $ QstSetProgress(RomanceMarbella, 7)
        $ RomanceMarbella().Love_DayToMeetAfterFaceDate = GetGameDay() + 1
        $ NoteUnlock("marbella_love_return_to_marbella_theplan")
    else:
        $ SetRepeatVariant(False)
    $ LocEnter()

#################################################################################################################################################
# The player returns to Marbella the next day at the Crooked Shaft and Mining Co
# triggers on enter
label rom_marbella_love_return_for_theplan:
    $ QstSetProgress(RomanceMarbella, 8)
    $ NoteLock("marbella_love_return_to_marbella_theplan")
    show marbella at cleft with dissolve
    show mc at cright_f with easeinright
    MARBELLA @smile "Ah! There you are!"
    "A giddy Marbella laid out a map on a table, grinning happily as she pointed."
    show marbella at shake
    MARBELLA @smile "Look, LOOK!"
    MC @think "What's got you so excited?"
    MARBELLA @smile "This right here?"
    MARBELLA @smile "It's an old mine I've found, one hardly anyone knows about."
    MC @think "What?"
    MARBELLA @talk "The main entrance caved in years ago during an accident."
    MARBELLA @talk "For years, the mine has been seen as inaccessible."
    MARBELLA @talk "There was talk about some trying to restore it, but then the war shelved those talks."
    MC @serious "What good is a sealed-off, dangerous mine?"
    MARBELLA @smile "I'm glad you asked!"
    MARBELLA @talk "I did some digging, and you see, there's a much lesser-known way down into the mines."
    label rom_marbella_love_theplan_repeat_next:
    MARBELLA @talk "Smugglers and people sometimes use it to lay low."
    MARBELLA @smile "But I bet my left tit there's still plenty to mine down there."
    MC @think "So, where do I come into this?"
    MARBELLA @emb "Umm... I was uhh..."
    MARBELLA @talk "Hoping you'd maybe help me check it out?"
    MARBELLA @sad "I can't knowingly send the boys into danger, so..."
    MARBELLA @talk "Would you help me clear out whatever's down there?"
    MC @think "Right now?"
    MARBELLA @think "I don't want to wait if it can be helped."
    MARBELLA @talk "I should warn you though, it's going to take a few hours to get there..."
    jump rom_marbella_love_theplan_menu

label rom_marbella_love_theplan_repeat:
    MARBELLA @talk "Yeah, as I've said before, I did some digging, and you see, there's a much lesser-known way down into the mines."
    jump rom_marbella_love_theplan_repeat_next

# re-visitable on prog 8
label rom_marbella_love_theplan_menu:
    menu:
        "{image=[ICON.CLOCK]} Let's do it.":
            $ NoteLock("marbella_love_theplan_memo")
            MARBELLA @smile "Great!"
            MARBELLA @talk "I gave the boys the day off today so the wagon's free."
            MARBELLA @talk "Let's go!"
            jump rom_marbella_love_theplan_setout
        "I need some time.":
            MARBELLA @sad "Ah... R-Right, you're probably busy, of course."
            MARBELLA @talk "Just let me know, alright?"
            $ NoteUnlock("marbella_love_theplan_memo")
            $ LocEnter()

############################################################################################################################################
# Fade to black
label rom_marbella_love_theplan_setout:
    scene black with dissolve
    $ AutoAmb(False)
    #$ AutoMus(False)
    stop music fadeout 1.0
    stop ambience fadeout 0.1
    if IsDaytime():
        $ PlayAmbience(audio.desert_day)
    else:
        $ PlayAmbience(audio.desert_night)
    "... With equipment already loaded onto the wagon, Marbella gave the wagon driver the path we wanted to follow and boarded with me."
    $ LocNameSetTemp(_("Somewhere in the desert"))
    $ TimeAdvBy(TIME_2H)
    play sound "audio/cfx/horse_running.ogg"
    "The next couple hours were spent watching the desert sands pass on and on..."
    if IsDaytime():
        scene cg_wagon_temple_travel_day with dissolve 
    else:
        scene cg_wagon_temple_travel_night with dissolve 
    MC "So, what exactly are you hoping to find in this mine?"
    MC "Iron? Copper?"
    MARBELLA "{i}Gems.{/i}"
    "Marbella giggled and squirmed in her seat."
    MARBELLA "Can you believe it?"
    MARBELLA "We could make a fortune!"
    MC "{i}*Could.*{/i}"
    MC "Let's see what the state of this mine is before we get too excited."
    MARBELLA "Too late!"
    scene black with dissolve
    $ TimeAdvBy(TIME_2H)
    "Eventually, we arrived at the entrance, a small side tunnel down into the mine that you could only find by scaling down a small gorge in the desert."
    "An emergency escape tunnel perhaps? Or part of something that was one day going to branch off the mine somehow?"
    "Either way, climbing through the gap carefully, we traversed through the mine, coming across some of the old tracks..."
    $ LocNameSetTemp(_("Mine"))
    $ PlayAmbience(audio.cave)
    scene bg_mine_gems with dissolve
    show marbella at center_f
    show mc at cright_f 
    with easeinright
    MARBELLA @smile "This is perfect! Look!"
    MARBELLA @shock "Half of the stuff is still here! The boys are gonna be thrilled!"
    show marbella at cleft_f with ease
    MC @think "First, we still need to make sure the mine is-"
    "At first, I heard soft footsteps, followed by chatter."
    show marbella at cleft
    show marbella at shake
    MARBELLA @scared "{i}*Whispering*{/i} S-Shit...!"
    show marbella at right with ease
    show marbella at right_f
    "I reached for my blade."
    show cg_raider at cleft with easeinleft
    show cg_bandit at left with easeinleft
    "Appearing from the shadows, a group of armed men were wandering through one of the connecting tunnels."
    RAIDER "Are you sure this is the right way?"
    BANDIT "Of course it is, idiot!"
    BANDIT "The map says-"
    "The men stopped in their tracks to look towards us."
    BANDIT "... It seems we have unwanted guests."
    "The one glared towards Marbella, who cowered behind me."
    RAIDER "Look at the tits and ass on that dwarf!"
    "Marbella turned pale white."
    BANDIT "You can fuck her when we're done with this one."
    MARBELLA @scared "S-Stay back!"
    MARBELLA @scared "[player_name!t]!"
    RAIDER "Should I smash his skull in?"
    menu:
        "Oh good! More skins for my collection!" (Req_Perk = "terrifying"):
            "The two men froze, the blood draining from them as they looked anxiously towards each other."
            RAIDER "... This guy doesn't seem right."
            BANDIT "I think I recognise this freak!"
            show cg_bandit at shake
            BANDIT "HE'S THE FUCKING BEAST OF NOVARAS, RUN!"
            hide cg_raider 
            hide cg_bandit
            with easeoutright
            "The two men quickly scarpered."
            show mc at cleft_f with ease
            show mc at blurin, cleft
            MC "(Well, that went about as well as I could have hoped.)"
            show marbella at cright_f with ease
            MARBELLA @scared "... You've got this fuckin' terrifying expression sometimes, you know that?"
            MARBELLA @scared "It's like your eyes just turn dead."
            MC @embarr "Ahh... Sorry about that."
        "You can still walk away...":
            BANDIT "Not an option."
            MC @talk "Too fucking bad for you."
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            scene black with dissolve
            "I unsheathed my blade!"
            $ StartBattle(BattleData(BackgroundImage = "pbat_dungeon_2", CharIDList_Right = [{"e_bandit":10}, {"e_raider":10}]))
            scene bg_mine_gems 
            show mc at cright_f
            with dissolve
            "Dragging my blade across the one's throat, he dropped to the ground, clutching at the wound as he choked on his blood."
            stop music fadeout 0.5
            MC @serious "I said you could walk away..."
            show mc at cleft_f with ease
            show mc at blurin, cleft
            show marbella at cright_f with dissolve
            MARBELLA @scared "F-Fuck... There's so much blood!"
            MC @talk "Sorry, there was no other way."
            "The man stopped squirming and now lay lifeless on the floor."
    MC @talk "I'm gonna need to scout out the rest of this mine a bit to make sure-"
    MARBELLA @scared "D-Don't leave me here!"
    show marbella at center_f with ease
    "Marbella stepped closer, clinging to me."
    MARBELLA @sad "What if someone else comes?"
    MC @sad "{i}*Sigh*{/i}"
    MC @talk "Alright, just stay behind me."
    scene black with dissolve
    "Marbella nodded sheepishly as we headed deeper into the mine."
    $ TimeAdvBy(TIME_2H)
    "Time blurred as the two of us explored the mine deeper, finding the odd abandoned cart and pickaxe, but no breathing souls..."
    MC "Alright, it seems to be clear enough now, come on."
    MC "Let's get out of here."
    $ LocNameSetTemp(_("Somewhere in the desert"))
    if IsDaytime():
        $ PlayAmbience(audio.desert_day)
    else:
        $ PlayAmbience(audio.desert_night)
    "Marbella didn't need much persuading, nodding sheepishly as we headed back to the wagon."    
    play sound "audio/cfx/horse_running.ogg"
    if IsDaytime():
        scene cg_wagon_temple_travel_day with dissolve 
    else:
        scene cg_wagon_temple_travel_night with dissolve 
    MARBELLA "..."
    MC "... Well?"
    MARBELLA "T-That was kind of scary, huh?"
    MC "It's nothing I haven't had to deal with before."
    MARBELLA "R-Right."
    scene black with dissolve
    $ TimeAdvBy(TIME_2H)
    "For the rest of the journey, Marbella seemed quiet and lost in thought..."
    $ TimeAdvBy(TIME_2H)
    $ LocSet("hamun_miningco")
    $ LocNameReset()
    $ LocFlush()
    show marbella at cleft
    show mc at cright_f
    with dissolve
    $ PlayMusic("audio/music/37_Rooftops.ogg")
    MARBELLA @sad "... I... I'm not sure."
    MC @think "Not sure of what?"
    MARBELLA @sad "The mine."
    MARBELLA @sad "Maybe I should just forget about it."
    MC @talk "Just bring security, your boys will be safe."
    MARBELLA @sad "I'll... I'll give it some thought."
    MARBELLA @sad "I g-guess... knowing they were going to-"
    "Marbella gulped, pushing the thought aside."
    MC @talk "Try not to dwell on it."
    MC @sad "It can drive you mad thinking about it."
    MARBELLA @scared "If I didn't bring you... then..."
    "She shook her head."
    MARBELLA @sad "... I... Just come back in a day or two, alright?"
    MARBELLA @sad "I just want to be alone right now."
    scene black with dissolve
    $ AutoMus(True)
    $ AutoAmb(True)
    "I wanted to offer some words of comfort, but from Marbella's expression, I knew it wouldn't help."
    $ LocSet("hamun_dist_docks")
    $ LocFlush(dissolve)
    $ NoteUnlock("marbella_love_return_after_minetravel")
    $ RomanceMarbella().Love_DayToReturnAfterMine = GetGameDay() + 2
    $ QstSetProgress(RomanceMarbella, 9)
    show mc at cleft with easeinleft
    MC "(I should check in in a day or two... Poor girl.)"
    $ LocEnter()

####################################################################
label rom_marbella_love_return_after_travel:
    $ NoteLock("marbella_love_return_after_minetravel")
    show marbella at cleft with dissolve
    show mc at cright_f with easeinright
    MARBELLA @talk "Ahh, there you are."
    MC @think "Is everything alright?"
    MARBELLA @talk "Yes."
    MARBELLA @talk "I'm still going to send the boys to that mine."
    "She took a deep breath."
    MARBELLA @sad "I'm not going to let some assholes just threaten me and have me retreat into nothing, you know?"
    MARBELLA @talk "Don't worry though, the boys will be mining that one with a couple sellswords to make sure things run smoothly."
    MC @smile "That's great to hear, Marbella."
    if RomanceMarbella().Love_IsPlato == True:
        MARBELLA @talk "I think I've got things from here."
        MARBELLA @talk "I'll let you know if I need anything else!"
        $ QstSetProgress(RomanceMarbella, 1000)
        $ LocEnter()
    else:
        MARBELLA @think "While I have you here, do you happen to know a good tailor?"
        MC @talk "Why do you ask?"
        MARBELLA @emb "N-No reason particularly... Just..."
        MARBELLA @lewd "Well, I was thinking I might get myself some new 'evening attire,' if you catch my meaning."
        MARBELLA @lewd "I was thinking it might be fun if you came with me."
        MC @think "Hmm..."
        if not CharIsMet("giselra"):
            MC @talk "I shall see what I can find."
            MARBELLA @smile "Great, just... let me know if you find one!"
            $ NoteUnlock("marbella_love_find_tailor")
            $ QstSetProgress(RomanceMarbella, 10)
            $ LocEnter()
        else:
            label rom_marbella_love_tell_about_giselra:
            $ NoteLock("marbella_love_find_tailor")
            MC @smile "Have you been to Giselra's shop?"
            MC @smile "She's a fine tailor, I think she'll be able to help with your needs."
            MARBELLA @smile "Giselra, huh?"
            MC @think "Need me to show you where it is?"
            MARBELLA @smile "Nah, I'll find it."
            MARBELLA @lewd "Just meet me over there tomorrow, love."
            $ NoteUnlock("marbella_love_meet_at_giselra")
            $ RomanceMarbella().Love_DayToMeetMarbellaAtGiselra = GetGameDay() + 1
            $ QstSetProgress(RomanceMarbella, 11)
            $ LocEnter()

label rom_marbella_love_found_tailor:
    MARBELLA @smile "Really?"
    jump rom_marbella_love_tell_about_giselra

###################################################################################
# The player heads to Giselra's at day
label rom_marbella_love_arrive_at_giselra:
    $ NoteLock("marbella_love_meet_at_giselra")
    $ QstSetProgress(RomanceMarbella, 12)
    show marbella at center
    show giselra at cright_f
    with dissolve
    MARBELLA @shock "What do you mean it's not possible?!"
    show marbella at center_f
    "The two women turned to look as I entered."
    show mc at cleft with easeinleft
    MARBELLA @talk "Nice to see you join us, handsome."
    GISELRA @smile "Ahh... Nice of you to join us."
    GISELRA @talk "Unfortunately, as I was explaining to your lady friend here,"
    GISELRA @talk "I am completely booked for the next few months."
    show marbella at center
    MARBELLA @sad "Mm... Is there anything in stock still available?"
    GISELRA @think "There are a few things around, I could adjust them to your size but..."
    GISELRA @talk "Making a design from scratch is out of the question."
    MARBELLA @think "Well, that's better than nothing I suppose."
    show marbella at center_f
    MARBELLA @sad "I doubt we'll find much of what we're looking for here, but might as well while we're here?"
    MC @smile "Let's take a look..."
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    "For the next thirty minutes, Marbella and I wandered around the store with little catching her eye..."
    "{i}Except one dress.{/i}"
    "Staring at the wedding lingerie on the mannequin, Marbella's eyes lit up."
    $ LocFlush()
    show mc at cleft
    show marbella at center
    with dissolve
    MARBELLA @smile "H-Ha... Could you imagine me in something like that?"
    MC @smile2 "Yes."
    MARBELLA @emb "... S-Shut up."
    "Despite her words, she continued to stare longingly towards the dress."
    MARBELLA @sad "... Besides, it's not like I'd ever have a reason to wear it with you."
    MARBELLA @sad "Alderians are only allowed to marry other Alderians, remember?"
    MC @think "Times are changing, once this war ends-"
    MARBELLA @think "{i}Once it ends...{/i}"
    MARBELLA @laugh "I'd rather not think about how many wrinkles will be on my face when that happens."
    "There was a sad bitterness to her laugh."
    show marbella at center_f
    MARBELLA @sad "Anyway, looks like we aren't going to have much luck here."
    MARBELLA @sad "{i}*Sigh*{/i}"
    MARBELLA @sad "Sorry for wasting your time, I guess."
    show giselra at cright_f with easeinright
    GISELRA @shock "Wait!"
    GISELRA @smile "Wait, before you go, let me take your measurements."
    GISELRA @smile "Just for safekeeping... And if I have any other dwarf clients, it could prove handy."
    MARBELLA @think "Well, sure... Why not?"
    scene black with dissolve
    "After having her measurements taken, Marbella gave me a quick kiss before leaving,"
    "muttering something about 'a lot of work to do anyway' dejectedly."
    $ LocFlush()
    show mc at cleft
    hide marbella
    show giselra at cright_f
    with dissolve
    GISELRA @talk "You know... I could find the time to resize that wedding dress."
    MC @surprised "Huh?"
    MC @sad "But-"
    GISELRA @smile "Is being married really just about a piece of paperwork shared between you?"
    MC @talk "In Alderay's eyes, yes."
    GISELRA @talk "A woman's heart is a complicated thing... You might not be able to 'legally' marry."
    GISELRA @smile "But I think it might mean the world to her to know you {i}would{/i} marry her."
    MC @think "Hmm..."
    GISELRA @talk "Just a thought, let me know if you're interested."
    GISELRA @talk "I could do it for eight hundred, as it's just a resize."
    menu rom_marbella_love_arrive_at_giselra_menu:
        "Your coin." (Req_Gold = RomanceMarbella().Love_DressPrice):
            $ PlayerRemItem("gold", RomanceMarbella().Love_DressPrice)
            GISELRA @smile "Very good. Just give me three days, and I'll have it ready."
            $ NoteLock("marbella_love_buy_dress")
            $ NoteUnlock("marbella_love_pickup_dress_later")
            $ RomanceMarbella().Love_DayToPickupDress = GetGameDay() + 3
            $ QstSetProgress(RomanceMarbella, 13)
            $ LocEnter()
        "Coin is a little tight... Would six-fifty suffice?" (AppearIf = RomanceMarbella().Love_DressPrice == 800, Req_Barter = 13):
            GISELRA @smile "{i}*Sigh*{/i}"
            GISELRA @smile "You're lucky you're so handsome, you know that?"
            GISELRA @smile "Very well... Six-fifty."
            $ RomanceMarbella().Love_DressPrice = 650
            jump rom_marbella_love_arrive_at_giselra_menu
        "I will return when I have the coin.":
            GISELRA @talk "Of course."
            $ NoteUnlock("marbella_love_buy_dress")
            $ LocEnter()

label rom_marbella_love_giselra_buydress_rep:
    GISELRA @talk "Yes, do you have the coin?"
    jump rom_marbella_love_arrive_at_giselra_menu

label rom_marbella_love_dress_notready:
    GISELRA @talk "It's not ready yet."
    GISELRA @talk "Come back to pick it up later!"
    return

label rom_marbella_love_dress_ready:
    $ NoteLock("marbella_love_pickup_dress_later")
    $ QstSetProgress(RomanceMarbella, 14)
    show giselra at cright_f
    with dissolve
    show mc at cleft with easeinleft
    GISELRA @smile "Ah! You're back."
    GISELRA @smile "The wedding dress is ready, I hope your lady likes it."
    $ PlayerAddItem("qst_marbella_wedding_ling")
    MC @smile "I'm sure she will."
    scene black with dissolve
    "Giselra laughed as I exited the store."
    $ LocSet("hamun_dist_docks")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    MC @think "(If I'm going to do this properly... I might need a couple things.)"
    MC "(A ring and a bottle of wine.)"
    $ NoteUnlock("marbella_love_get_wine")
    $ NoteUnlock("marbella_love_get_ring")
    MC "(Maybe some flowers?)"
    $ NoteUnlock("marbella_love_get_flowers")

    if PlayerHasItem("qst_wine_bottle") and PlayerHasItem("qst_marbella_flowers") and PlayerHasItem("qst_marbella_ring"):
        $ QstSetProgress(RomanceMarbella, 15)
        $ NoteLock("marbella_love_get_wine")
        $ NoteLock("marbella_love_get_ring")
        $ NoteLock("marbella_love_get_flowers")

        $ NoteUnlock("marbella_love_bring_stuff")
    $ LocEnter()

# new dialogue option with Katiya
label rom_marbella_love_katiya_flowers:
    KATIYA @think "Flowers?"
    KATIYA @talk "It isn't something I sell per se, but as I have some flowers upstairs, I could pluck you one of my roses perhaps?"
    MC @think "How much?"
    KATIYA @happy "For a single rose?"
    KATIYA @happy "I'll give it to you for free, just remember to pay me back and shop here from time to time."
    MC @smile "Thank you."
    "Katiya left briefly before returning with a single rose."
    $ PlayerAddItem("qst_marbella_flowers")
    $ NoteLock("marbella_love_get_flowers")
    if PlayerHasItem("qst_wine_bottle") and PlayerHasItem("qst_marbella_ring"):
        $ QstSetProgress(RomanceMarbella, 15)
        $ NoteUnlock("marbella_love_bring_stuff")
    KATIYA @happy "I hope she appreciates it!"
    $ LocEnter()


#The player can have a ring forged by the blacksmith - new dialogue option 
label rom_marbella_love_beshar_ring_order:
    BESHAR @think "What kind?"
    MC @talk "The kind to give to a special woman."
    "Beshar cracked a smile."
    BESHAR @smile "A simple one?"
    label rom_marbella_love_beshar_ring_order_repeat:
    BESHAR @smile "Two hundred coins for you."
    menu:
        "Here you go." (Req_Gold = 200):
            $ PlayerRemItem("gold", 200)
            BESHAR @talk "Come back tomorrow and I'll have it ready for you."
            $ RomanceMarbella().Love_BesharDayToGetRing = GetGameDay() + 1
            $ LocEnter()

        "I'll come back when I have the coin.":
            $ RomanceMarbella().Love_BesharRingDoRepeat = True
            BESHAR @talk "Aye."
            $ LocEnter()

label rom_marbella_love_beshar_ring_ready:
    #Upon revisiting the next day after buying the ring
    BESHAR @talk "Here's yer ring."
    $ PlayerAddItem("qst_marbella_ring")
    $ NoteLock("marbella_love_get_ring")
    if PlayerHasItem("qst_wine_bottle") and PlayerHasItem("qst_marbella_flowers"):
        $ QstSetProgress(RomanceMarbella, 15)
        $ NoteUnlock("marbella_love_bring_stuff")
    $ LocEnter()

label rom_marbella_love_beshar_ring_notready:
    BESHAR @talk "Not ready yet."
    BESHAR @talk "Come back later."
    return

label rom_marbella_love_luna_get_wine:
    LUNA @smile "Certainly! This one costs three hundred coins."
    LUNA @smile "This one came from Synmaria, so it's quite a flavorful red."
    menu:
        "Here you go." (Req_Gold = 300):
            $ PlayerRemItem("gold", 300)
            $ PlayerAddItem("qst_wine_bottle")
            $ NoteLock("marbella_love_get_wine")
            if PlayerHasItem("qst_marbella_ring") and PlayerHasItem("qst_marbella_flowers"):
                $ QstSetProgress(RomanceMarbella, 15)
                $ NoteUnlock("marbella_love_bring_stuff")
            LUNA @smile "Enjoy!"
            $ LocEnter()

        "I'll return when I have the coin.":
            LUNA @talk "I'll keep it back behind the counter for you."
            $ LocEnter()


################################################################################################################################
#The player returns to Marbella - new dialogue option  - Only if player has
    #  dress, ring, wine, rose 
label rom_marbella_love_bring_wedding_stuff:
    $ NoteLock("marbella_love_bring_stuff")
    $ PlayerRemItem("qst_marbella_wedding_ling", PlayerItemQty("qst_marbella_wedding_ling"))
    $ PlayerRemItem("qst_marbella_flowers", PlayerItemQty("qst_marbella_flowers"))
    $ PlayerRemItem("qst_marbella_ring", PlayerItemQty("qst_marbella_ring"))
    $ PlayerRemItem("qst_wine_bottle", PlayerItemQty("qst_wine_bottle"))
    MARBELLA @shock "Wha... What is-"
    MARBELLA @emb "You... You seriously bought me all this?"
    MARBELLA @emb "You... You..."
    MARBELLA @cry "Oh gods..."
    MARBELLA @cry "Why are you so nice to me?"
    MC @smile "{i}You know why.{/i}"
    MARBELLA @cry "Just... Just say it once, alright?"
    MARBELLA @cry "Even if it's just pretend."
    MC @smile "{b}I love you.{/b}"
    "Her eyes looked down towards the ring."
    MARBELLA @cry "Could... Could you say the words?"
    MC @smile2 "{i}... Marry me?{/i}"
    hide marbella with dissolve
    show cg_marbella_mc_kiss at center with dissolve
    $ Pause()
    "Marbella leapt forward, pulling me down into a kiss."
    hide cg_marbella_mc_kiss with dissolve
    show marbella at cleft
    show mc at cright_f
    with dissolve
    MARBELLA @lewd "I'm going to ride you so fucking hard tonight."
    MARBELLA @lewd "I'm heading to your room at {i}The Pale Dragon{/i} tonight."
    MARBELLA @lewd "Bring your ass over there."
    MARBELLA @lewd "That's an order... {i}hubby.{/i}"
    MC @smile2 "See you tonight."
    hide marbella with dissolve
    "With that, Marbella happily returned to her work."
    show mc at center_f with ease
    MC @bitelip "(Tonight is going to be fun...)"
    $ NoteUnlock("marbella_love_return_night_wedding")
    $ QstSetProgress(RomanceMarbella, 16)
    $ LocEnter()

##########################################################################################################################
label rom_marbella_love_wedding:
    $ NoteLock("marbella_love_return_night_wedding")
    label marbella_love_wedding_repeat:
    if IsFirstTime():
        $ CharSetClothes("marbella", "wedding")
        show marbella at cright_f
        with dissolve
        $ PlaySound("audio/cfx/doorthud.ogg")
        show mc at cleft with easeinleft
        "As I opened the door and entered inside,"
        "Marbella turned sheepishly towards me,"
        "adorned in her wedding lingerie as she let out low, trembling breaths."
        MARBELLA @emb "H-Hello..."
        MC @surprised "Marbella..."
        MC @surprised "You look-"
        MARBELLA @emb "Ridiculous?"
        MC @smile "... Beautiful."
        $ AutoMus(False)
        $ PlayMusicRandom("mus_sex")
        "Marbella's mouth hung open, she looked like she wanted to say something, but didn't."
        "Instead, she stepped forward, gently taking hold of my hand as she pulled me towards the bed."
        MARBELLA @emb "C-Come here, love."
        call rom_marbella_love_wedding_vag from _call_rom_marbella_love_wedding_vag
    else:
        $ LocSet("hamun_hookah_bar_room")
        $ CharSetClothes("marbella", "wedding")
        $ LocFlush()
        show marbella at cright_f
        with dissolve
        show mc at cleft with easeinleft
        "Inside, Marbella was waiting patiently once again in her wedding lingerie."
        "She twirled her hair as she moved closer towards me."
        MARBELLA @emb "D-Do you intend to keep making me wear this thing every time we... you know."
        MARBELLA @emb "H-Ha... If you keep making me wear it, I might ACTUALLY start thinking I'm your wife!" 
        MARBELLA @think "Sooooo, anyway love."
        MARBELLA @emb "I-I was wonderin' if you wanted to try something a little {i}'different'{/i} tonight."
        $ AutoMus(False)
        $ PlayMusicRandom("mus_sex")
        MARBELLA @emb "We could do things as normal."
        MARBELLA @emb "Orrrrrr..."
        MARBELLA @lewd "{b}Maybe you'd wanna try putting it in my ass?{/b}"
        "Marbella gave a playful turn."
        hide marbella
        show cg_marbella_back_wedding at cright
        MARBELLA "What do you think?"
        MARBELLA "Wanna conquer ALL of wifey's ass tonight? Fufu~ {image=[ICON.HEART]}"
        $ PlaySound("audio/cfx/spank.ogg")
        "Marbella playfully spanked herself, and my cock stiffened in excitement at watching her round, juicy ass jiggle with the hit."
        hide cg_marbella_back_wedding
        show marbella at cright_f
        "She turned back to face me, grining mischeviously as she awaited my answer."  
        menu:
            "The only thing I want is to taste your other lips...":
                MARBELLA @lewd "That's a real romantic way of saying you want pussy."
                MARBELLA @smile "{i}*Sigh*{/i} Stop standing there then and do your thing, lover."
                "I smirked, stepping forward as I threw Marbella first over my shoulder, then down onto the bed."
                MARBELLA "Eeeeeep!"
                call rom_marbella_love_wedding_vag from _call_rom_marbella_love_wedding_vag_1
            "What man could resist that ass?":
                MARBELLA @lewd "Pervert."
                MARBELLA @lewd "Good for you I kinda am too, hmm?"
                MARBELLA @lewd "... Well, what are you waiting for?"
                MARBELLA @lewd "That hole isn't going to fuck itself!"
                call rom_marbella_love_wedding_anal from _call_rom_marbella_love_wedding_anal
    $ StopReplay()
    $ LocFlush()
    $ CharSetClothes("mc", "naked")
    show mc at cleft
    show marbella at cright_f
    with dissolve
    if IsFirstTime():
        MC @smile "Then I take it you're staying the night?"
        "Marbella licked her lips playfully."
        MARBELLA @lewd "On my first night with 'hubby?'"
        MARBELLA @lewd "Where else would I go? Fufu..."
    else:
        MC @smile "Stay with me tonight, work can wait."
        MARBELLA @lewd "You could sweet talk me into anything, love..."

    scene black with dissolve
    $ CharSetClothes("marbella", "normal")
    $ CharSetClothes("mc", "normal")
    "With that, Marbella cuddled up to me on the bed."
    $ AutoMus(True)
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    "Time drifted by until the morning, at which point I found she was gone already."
    "In her stead, a note was left and addressed to me."
    "{i}OI HUBBY, GOTTA RUN BACK TO THE OFFICE, LOVE, ME.{/i}"
    $ LocFlush()
    show mc at cright_f
    with dissolve
    "I smirked, reading the note."
    MC @smile "(Marbella...)"
    MC @sad "(I only wish we had more time.)"
    $ QstSetProgress(RomanceMarbella, 1000)
    $ LocEnter()

# these two vag/anal dub as gallery replay starts
label rom_marbella_love_wedding_vag:
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_idle with dissolve
    else:
        scene marbella_love_wedding_nopreg_idle with dissolve
    $ Pause()
    "As she gently laid down on the bed, she ran her hands down my chest as I stripped down my clothes."
    "Gently, I pressed my cock against her as she began to breathe in nervous anticipation."
    MARBELLA "... How did I get so lucky?"
    MC "Marbella."
    MARBELLA "Don't make me wait..."
    MARBELLA "Please..."
    $ PlaySexFx(audio.forgean_075, 1)
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_vag_1 with dissolve
    else:
        scene marbella_love_wedding_nopreg_vag_1 with dissolve
    $ Pause()
    "I didn't say anything. Gently, as I entered her, she gasped, moaning softly as she felt my member slowly push inside of her."
    MARBELLA "Mmmfghh....!"
    "Her whole body tightened as her legs squeezed around me."
    "As the slow, steady rhythm began, she moaned softly, her eyes staring into mine as she felt me stretch her out." 
    MARBELLA "Oooooh..."
    MARBELLA "The way you're lookin' at me right now..."
    MARBELLA "I just wish I could have a painting of it or somethin' so I'll never forget it."
    "She let out another hot moan, her toes curling in delight."
    MC "You better get - {i}*Huff*{/i} used to seeing this face."
    MC "Because I think you're gonna be seeing a lot more of it."
    MARBELLA "Then you better - Ahh! Give me a reason not to ever get tired of seeing it!"
    $ PlaySexFx(audio.forgean_100, 1)
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_vag_2 with dissolve
    else:
        scene marbella_love_wedding_nopreg_vag_2 with dissolve
    $ Pause()
    "I began to move faster, pushing deeper into Marbella."
    "She squeezed effortlessly around my cock, her hot moans matching mine as her sweat glistened in the light."
    MARBELLA "Ah! Ahh! Ahhh!"
    MARBELLA "F-Fuck, I love you..."
    MARBELLA "I love you so much!!"
    "As my balls slapped against her clit, I began to feel them tighten and rise, ready to blow as I continued to stretch out Marbella's wet, tight hole."
    MC "Marbella.... Hrghh! I don't know how much longer I can-"
    "She placed her finger to my lips."
    MARBELLA "Shhh..."
    MARBELLA "Just let it out."
    MARBELLA "Cum in me, love."
    MC "Hrghh!"
    MC "M-Marbella!"
    MARBELLA "Do it."
    MARBELLA "{i}*Huff*{/i} Please... Cum..."
    MARBELLA "Cum in me!"
    "Pushing forward, Marbella trembled as I buried myself deep into her, unable to hold back any longer."
    $ PlaySexFx(audio.forgean_finish)
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_vag_finish with flash
    else:
        scene marbella_love_wedding_nopreg_vag_finish with flash
    $ Pause()
    "Her mouth hung agape as I poured myself into her."
    MARBELLA "{i}*Gasp!*{/i}"
    MC "Hrghhhhhhh...!"
    MARBELLA "{i}*Huff*{/i} Gods, I'm gonna carry so many of your fuckin' babies."
    MC "What was that?"
    MARBELLA "Uhh, n-nothing!"
    scene black with dissolve
    "Gently, Marbella pushed me away as she turned around, climbing onto her hands and knees onto the bed."
    scene marbella_love_wedding_alt_idle with dissolve
    $ Pause()
    MARBELLA "I hope you're ready for round two, love."
    MARBELLA "Because I'm not letting you get away tonight!"
    "My cock sprang to life once more as Marbella spread her cheeks."
    MC "The gods blessed you with an ass that could make a succubus envious!"
    MARBELLA "And it's all yours, love."
    MARBELLA "Now are you just gonna keep teasing me with that big cock of yours, or are you gonna fuck your 'wifey' senseless?"
    "She didn't need to ask twice."
    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene marbella_love_wedding_alt_vag_1 with dissolve
    $ Pause()
    "She cooed happily as I pushed my cock into her once more."
    MARBELLA "Ooooh...!"
    MARBELLA "Ahh, nice to see how quick the ol' soldier stands to attention when I wave my fat ass in your face!"
    "Her pussy squeezed around me as I slammed against her ass."
    "The soft flesh collided against me with lewd slapping sounds as I claimed Marbella."
    MARBELLA "{i}*Huff*{/i} H-Harder!" 
    MARBELLA "Faster, love!"
    MARBELLA "Mmfgh! I love you!"
    $ PlaySexFx(audio.nijah_miss_2, 1)
    scene marbella_love_wedding_alt_vag_2 with dissolve
    $ Pause()
    "I did as she asked, thrusting faster into Marbella's loving honeypot."
    MARBELLA "Ahh! Ah! AHHH!"
    MARBELLA "T-That's it!"
    MARBELLA "F-Fuck your wife!"
    MARBELLA "Fuck me so good!"
    "The soft flesh of her round ass slamming against me resonated throughout the room."
    "{i}*Phap! Phap! Phap!*{/i}"
    "As our grunts and moans filled the room,"
    "the hot, sweaty passion quickly overtook me, as I began to feel my body once more ready to breed the little dwarf beneath me."
    MC "Marbella-"
    MC "I'm-"
    "With maddening, lustful eyes she slurred out,"
    MARBELLA "Cum in me, cum in me, cum in me!"
    MARBELLA "Fill your wifey's pussy up!"
    $ PlaySexFx(audio.nijah_miss_finish)
    $ ReduceInfectionFromSex("marbella")
    $ PregRoll("marbella")
    if CharIsVisiblyPreg("marbella"):
        $ UnlockGalFlag("marbella", "love_wedding", "var_preg_vag")
    else:
        $ UnlockGalFlag("marbella", "love_wedding", "var_nopreg_vag")
    $ UnlockGalSceneAndGrantXp("marbella", "love_wedding")
    scene marbella_love_wedding_alt_vag_finish with flash
    "I pushed deep into Marbella's loving embrace, unable to hold back any longer as I desperately came inside of her once more." 
    "I grunted like an animal, shaking as I poured myself into her."
    MC "MARBELLA...!!"
    "Marbella could only gasp, shaking and tightening with me as she let out the sweetest moan."
    MARBELLA "C-Cumminggg...!"
    "I lay on her back, my cock slowly deflating as she lathered me in passionate kisses,"
    "mumbling, drunk on love and lust, how much she loved me over and over again."
    "Slowly, as she released her grip around me, I rose back to my feet."
    MARBELLA @lewd "That was fuckin' incredible."
    return

label rom_marbella_love_wedding_anal:
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_idle with dissolve
    else:
        scene marbella_love_wedding_nopreg_idle with dissolve
    $ Pause()
    "Marbella carefully lowered herself down onto the bed with bated breath,"
    "raising her legs into the air as she carefully spread her cheeks."
    MARBELLA "H-Here, hubby..."
    "She said with a sheepish smile, cheeks burning red."
    "I moved closer, resting my cock against her body, lightly rubbing the hard member against her."
    MARBELLA "Mhmm..."
    MARBELLA "I k-know I shouldn't be so nervous, but-"
    "Marbella looked down as I teasingly rubbed the head of my cock against her tight rosebud."
    MARBELLA "Y-You're so big..."
    "I lightly prodded against the hole, feeling the tight resistance."
    MARBELLA "Can I really-"
    $ PlaySexFx(audio.forgean_075, 1)
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_anal_1 with dissolve
    else:
        scene marbella_love_wedding_nopreg_anal_1 with dissolve
    $ Pause()
    "Her ass gave way, spreading and stretching around the head of my cock as she gasped, eyes wide in shock."
    MARBELLA "O-OHHHHHHH...!"
    MARBELLA "F-F-F-Fuckkkkkk!!"
    MC "Marbella - Ahh! Are you-"
    MC "Okay?"
    MARBELLA "Y-Yes... Just..."
    MARBELLA "{i}*Huff*{/i} S-Slowly... Please."
    "I did as Marbella asked, slowly gliding my cock back and forth as I fucked her ass."
    "She bit down on her lower lip nervously, watching the huge, thick member sink into her dark hole."
    MARBELLA "{i}M-My ass... You're in my ass!{/i}"
    MC "F-Fuck... Your butt is so tight!"
    "Marbella's tight arse gripped around me like a vice."
    MARBELLA "I-It's - {i}*Huff*{/i} all yours, love."
    MARBELLA "My ass is all yours!"
    $ PlaySexFx(audio.forgean_100, 1)
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_anal_2 with dissolve
    else:
        scene marbella_love_wedding_nopreg_anal_2 with dissolve
    $ Pause()
    "I began to move faster, the soft flesh bouncing against me as the sound of the bedframe slamming against the wall grew louder."
    MARBELLA "OH GODS...!"
    MARBELLA "Mmmfghh...!"
    MARBELLA "I-It's starting to feel - {i}*Huff*{/i} w-weird!!"
    MC "I'm gonna make you cum."
    "Marbella shuddered in response to my command."
    MARBELLA "F-Fuckkk!!"
    MARBELLA "You're stretching me so much!"
    MARBELLA "Ahh!"
    MARBELLA "P-Please..."
    MARBELLA "{i}*Huff*{/i} I l-love you... {i}*Huff*{/i}"
    "Marbella's breathing began to quicken, her heart racing as she continued to mutter over and over again how much she loved me."
    "Suddenly, her eyes rolled to the top of her skull as she gritted her teeth, her whole body trembling as her sphincter tightened around me."
    "A breathless moan escaped her lips, and the sudden tightness as I continued to slam into her sent me over the edge."
    $ PlaySexFx(audio.forgean_finish)
    if CharIsVisiblyPreg("marbella"):
        scene marbella_love_wedding_preg_anal_finish with flash
    else:
        scene marbella_love_wedding_nopreg_anal_finish with flash
    $ Pause()
    MC "HRGHHHHH...!"
    "Grunting, I moaned as I flooded the hot dwarf's bowels with my thick seed."
    "She grunted like an animal as she felt the rush of warmth now in her."
    MARBELLA "{i}M-My ass... You're cumming inside m-my...{/i} {image=[ICON.HEART]}"
    "As I slowly pulled out of her ass, a *PLOP* sound followed as my cum seeped from her fucked hole."
    scene marbella_love_wedding_alt_idle with dissolve
    $ Pause()
    "With a lustful expression, Marbella rolled over, climbing onto her knees as she spread her cheeks."
    MC "Marbella, what are you-"
    MARBELLA "M-More..."
    MARBELLA "I want to feel you like this now."
    "My cock sprang to life once more as I gently began to rub against her ass,"
    "slapping the meat down on her dark rosebud."
    MARBELLA "{i}*Huff*{/i} D-Don't keep me waiting..."
    MARBELLA "{i}Please...{/i}"
    MARBELLA "I need to feel you inside me again."
    "I lightly prodded against her hole once more,"
    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene marbella_love_wedding_alt_anal_1 with dissolve
    $ Pause()
    "Marbella closed her eyes and moaned softly as I pushed in easier this time."
    "Once more, stuffing her tight ass, I began to move back and forth,"
    "pushing my hips up against the soft pillows of her ass cheeks."
    MARBELLA "I feel so full when you're inside me..."
    MC "Ahh... Marbella!"
    MC "Your ass is - Hrgh!"
    MARBELLA "Gotta find some way to keep you - Ahh! - coming back, don't I?"
    MARBELLA "If I've got the - Mmfgh! - T-TIGHTEST ass in the land!"
    MARBELLA "Oooh! Seems like a pretty good way to keep you coming back!"
    $ PlaySexFx(audio.nijah_miss_2, 1)
    scene marbella_love_wedding_alt_anal_2 with dissolve
    $ Pause()
    "I began to move faster, slamming my hips against the softness of her ass as she moaned hotly."
    MC "Gods, if ever there was an ass built to take it - Ahh!"
    MARBELLA "Y-Yes! Fuck my ass harder!"
    MARBELLA "D-Don't stop!"
    MARBELLA "FUCK YER WIFE'S ASS GOOD!"
    "Marbella pushed and threw her ass back onto me, the soft cheeks clapping with each hit as lewd sounds filled the room,"
    "{i}*Phap!* *Phap!* *Phap!*{/i}"
    MARBELLA "Yes! Yes! YES!"
    MARBELLA "F-Fill me up again ya big dick'd bastard!"
    MARBELLA "F-Fucking stuff your wife's ass full of your-"
    $ PlaySexFx(audio.nijah_miss_finish)
    $ ReduceInfectionFromSex("marbella")
    if CharIsVisiblyPreg("marbella"):
        $ UnlockGalFlag("marbella", "love_wedding", "var_preg_anal")
    else:
        $ UnlockGalFlag("marbella", "love_wedding", "var_nopreg_anal")
    $ UnlockGalSceneAndGrantXp("marbella", "love_wedding")
    scene marbella_love_wedding_alt_anal_finish with flash
    "As I slammed my hips forward, Marbella gasped as I once again drained my balls into her tight ass."
    "Her hands coiled and tightened around the pillow as I spilled my load into her bowels, her toes curling in delight."
    MARBELLA "OOOOOOOOOH...! {image=[ICON.HEART]}"
    "After a few moments, slowly letting my cock relax in her ass, I slowly removed it."
    "The seed spilled out of her gaping rosebud as she let out a desperate little whimper."
    "Slowly regaining her senses, she tilted her head to look back towards me."
    MARBELLA "Kinda chilly back there now you're out."
    "I chuckled as Marbella rolled over, and with shaky legs,"
    "did her best to stand."
    return

############################################################################### Repeat upon speaking to Marbella
label rom_marbella_love_repeat_options:
    if RomanceMarbella().Love_WillHaveSex == False:
        "Sorry love, too busy with all this paperwork right now..."
        return
    MARBELLA @smile "Beloved, aye?"
    MARBELLA @lewd "What are you tryna sweet talk me into now then, hmm?"
    menu:
        "A kiss.":
            MARBELLA @smile "Down on one knee, love, I ain't jumpin' to reach ya!"
            hide mc
            hide marbella
            with dissolve
            show cg_marbella_mc_kiss at center_f with dissolve
            "As I lowered myself, Marbella flung herself into my arms, planting her lips against mine."
            "Her hot tongue pushed into my mouth, entwining with my tongue for a few moments."
            MARBELLA "MMMMMWHA!"
            hide cg_marbella_mc_kiss
            show mc at cright_f
            show marbella at cleft
            with dissolve
            MARBELLA @lewd "How was that?"
            MARBELLA @lewd "Just as good as in your dreams?"
            return

        "I was wondering if I could do more than just look at your tits..." (AppearIf = not RomanceMarbella().Love_IsPlato):
            $ RomanceMarbella().Love_WillHaveSex = False
            "Marbella's eyes looked down towards her breasts."
            MARBELLA @lewd "Y-You mean uhh... You wanna shove that fat prick betweeen {i}*these*{/i} to get off?"
            "Marbella cupped her tits and squeezed them together."
            MC @smile "Is that a yes?"
            MARBELLA @lewd "{i}*Giggles*{/i}"
            MARBELLA @lewd "I'll bring me and the *girls* straight over to your room after work, love."
            scene black with dissolve
            "{i}Later...{/i}" 
            $ SetRepeatVariant(True)
            jump marbella_love_titjob_repeat

        "I was wondering if you wanted to try that standing thing we did with our mouths again." (AppearIf = not RomanceMarbella().Love_IsPlato):
            $ RomanceMarbella().Love_WillHaveSex = False
            MARBELLA @lewd "Oooh, say no more, love!"
            MARBELLA @lewd "I'll bring my ass straight over after work."
            scene black with dissolve
            $ SetRepeatVariant(True)
            jump marbella_love_69_repeat

        "How about another date at {i}The Pale Dragon?{/i} Drinks on me." (AppearIf = not RomanceMarbella().Love_IsPlato): 
            $ RomanceMarbella().Love_WillHaveSex = False
            MARBELLA @smile "Drinks on you, aye?"
            MARBELLA @talk "I'll see you tonight, love."
            if CharIsVisiblyPreg("marbella"):
                MARBELLA @think "Maybe just something a bit lighter for me though... You know, given the 'passenger' on board."
            scene black with dissolve
            $ TimeAdvTo(TIME_DAY_END)
            $ SetRepeatVariant(True)
            jump marbella_love_alleyway_repeat

        "How about you bring your ass over to my room tonight and we can rehearse our vows... wifey." (AppearIf = not RomanceMarbella().Love_IsPlato):
            $ RomanceMarbella().Love_WillHaveSex = False
            MARBELLA @emb "Y-You know I still get a little embarrassed hearing you say that, right?"
            MC @think "Is that a no?"
            MARBELLA @lewd "Course not, love."
            MARBELLA @lewd "I'll swing around after work... hubby."
            scene black with dissolve
            $ TimeAdvTo(TIME_DAY_END)
            $ SetRepeatVariant(True)
            jump marbella_love_wedding_repeat

        "On second thought...":
            return
