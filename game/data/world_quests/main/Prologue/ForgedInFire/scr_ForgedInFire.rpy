label qst_ForgedInFire_EnterBarracksToGetGear:
    "The barracks were built into the north-eastern wall of the fort."
    "Cold, moist air welcomed us into what seemed to be our living quarters from now on."
    "Recruits were trying on their new armor. Some just sat on their bunks, concerned."
    "As I was circling a particularly big guy adjusting straps on his armor, I found myself standing beside two empty bunks."
    "I turned to face Markus."
    show markusprologue at left with easeinleft
    show mcprologue at right_f with easeinright
    MC "I guess these are as good as any."
    MARKUS "You seriously think we get to pick?"
    MC "Well, I don't see any of them ordering us around."
    "With that, I waved towards a couple of guards at the far end of the room."
    "Markus nodded."
    MARKUS "Fair enough."
    $ LocFlush(dissolve)
    "Wooden trunks Joakim mentioned were set beside each bed."
    "I opened mine and was greeted by predatory glint of a halfway-sheathed sword."
    "Beneath it was a rather heavy set of leather armor."
    scene black with dissolve
    $ PlayerAddItem("scout_sword")
    $ PlayerAddItem("scout_armor")

    if CanEquip(0, "scout_sword", EQP_SLOTS.HANDS[0]):
        $ EquipItem(0, "scout_sword", EQP_SLOTS.HANDS[0])
    if CanEquip(0, "scout_armor", EQP_SLOTS.CHEST[0]):
        $ EquipItem(0, "scout_armor", EQP_SLOTS.CHEST[0])
    $ TooltipClear()

    "A short while later..."
    $ LocFlush()
    $ CharSetClothes("mc", "scout")
    $ CharSetClothes("markus", "scout")
    $ CharSetVar("kiara", "default_look", "scout")
    $ CharSetClothes("kiara", "normal")
    show mcprologue at left
    show markusprologue at right_f
    with dissolve
    "Markus stretched about and flexed his arms as I was fitting the sheath onto my belt."
    MARKUS "It's very tight in my... private area."
    MC "Mine's okay."
    MARKUS "Exactly."
    MC "Go to h~"
    GUARD "Recruits!"
    "One of the guards shouted in a commanding tone, ceasing all activity in the barracks."
    GUARD "Get strapped and head out into the yard now! This is not a fashion contest!"
    $ QstSetProgress(QstForgedInFire, 1)
    "I adjusted my sheath belt and nodded to Markus."
    MARKUS "Mission complete, I guess."
    scene black with dissolve
    "We headed out to the yard along with other recruits."
    "Being no more but a crowd of armed civilians, we now looked like we belonged to a single military unit, for what its worth."
    $ Pause(0.5)
    jump qst_ForgedInFire_ReturnToYard

label qst_ForgedInFire_ReturnToYard:
    $ LocSet("novaras_fort_seb_yard")
    $ LocUpdateDynSound()
    $ LocFlush()
    with dissolve
    show mcprologue at right_f with easeinright
    show markusprologue at left with easeinleft
    "Out on the yard the recruits gathered, talking and examining each other."
    "I noticed that redhead from before walking past us."
    show kiara at center_f with dissolve
    KIARA @happy "Looking good, boys!"
    MARKUS @smile "Yeah, you too, young lady!"
    "As she passed us, I stole another glance at that leather-clad beauty and asked Markus:"
    hide kiara with dissolve
    MC "How's that private area of yours doing now, huh?"
    MARKUS "You have no idea..."
    hide mcprologue
    hide markusprologue
    with dissolve
    $ PlaySoundRandom("woodenDoor")
    show duprey at center
    with flash
    'Suddenly, the doors flung open and a short man with a grey beard stormed through them.'
    'Stocky, he carried with him heavy armour covered in scratches and dirt that clanked with every movement.'
    'More impressive was the monumental axe slung over his back that looked sharp enough to cut glass and the edges of which were traced with enchanted blue lines, eerily incandescent.'
    'He vaulted forward onto the wooden podium Joakim lectured us from and landed with surprising grace, wood creaking under his heavy boots.'
    'He glowered down at us as he scanned the crowd from right to left.'
    'We fell into an ominous silence as we waited for what he would say.'
    'Finally, with a heavy sigh, he began:'

    DUPREY 'I am Captain Duprey, leader of the Second Scouts Division.'
    DUPREY 'It is a great honour to be called upon to serve with the Scouts. I trust that you understand what has been bestowed upon you.'
    DUPREY 'Many of you are pissing yourselves right now and probably have been since you found out you were joining these corps.'
    DUPREY 'You have probably spent these last few years learning all the proper terms, the fancy tactics and no doubt some very pretty footwork as a part of the basic combat training you all had received.'
    DUPREY 'We are going to work you {i}hard{/i} to forget all that!'

    CROWD '{i}*Confused murmurs*{/i}'
    DUPREY 'I am not interested in you showing me your majestic flying three-sixty spinning limp dicked thrust!'
    DUPREY 'You will learn practical things here. You will learn how to be dirty in the fight to level the field against {i}the Demorai{/i}.'
    DUPREY 'You will learn how to kill, without mercy and without hesitation.'
    DUPREY 'You will learn {i}to win.{/i}'
    'One of the men stepped forward nervously to raise his hand.'

    RECRUIT 'A-Aren’t we supposed to fight honourably though?'
    DUPREY '... Come here.'
    'The man looked around, unsure of what to do.'
    show duprey at shake
    DUPREY 'I SAID COME HERE!'
    'Some of the guards moved to shove the man out of the line, where he climbed hesitantly onto the stage with the Captain.'
    show duprey at cleft with easeinleft
    with dissolve
    show cg_black_scout at cright with easeinright
    'Y-Yes, sir?'
    'Taking a small sword, the Captain threw it to the man’s feet.'
    DUPREY 'Strike me down.'
    'The crowd was silent, the man looked at him bewildered.'
    show cg_black_scout at shake
    RECRUIT 'W-What?'
    DUPREY 'Pick that sword up and strike me down, boy! That is an order.'
    RECRUIT '... But I—'
    show duprey at shake
    DUPREY 'YOU FUCKING MAGGOT!'
    DUPREY 'DO AS YOU’RE TOLD OR I’LL FLAY YOU MYSELF AND HANG YOUR BODY FROM THE WALLS AS A WARNING TO ANYONE ELSE THAT CAN’T FOLLOW SIMPLE FUCKING ORDERS.'
    'Terrified, the man scurried to pick up the sword, trembling as he pointed it towards the Captain.'
    DUPREY '... Now, STRIKE ME!'
    $ PlaySoundRandom([
                "audio/battle/swordSwing/hSword-01.ogg",
                "audio/battle/swordSwing/hSword-02.ogg",
                "audio/battle/swordSwing/hSword-03.ogg",
                "audio/battle/swordSwing/hSword-04.ogg",
                "audio/battle/swordSwing/hSword-05.ogg"])
    show cg_black_scout at center
    show duprey at left
    with flash
    'The man cried out as he lunged forward to attack the Captain.'
    'Side stepping the blade, the Captain locked in the man’s arms and the two wrestled vehemently over the sword.'
    show duprey at cleft with easeinleft
    show duprey at shake
    show cg_black_scout at shake
    play sound "audio/cfx/duprey_headbutt.ogg"
    show cg_black_scout:
        parallel:
            easeout 0.6 rotate 90
        parallel:
            easein 0.6 xcenter 0.9 yoffset 200
    'So fast it was almost a blur, the Captain shoved his head forward, violently headbutting the unsuspecting man.'
    'His nose ruptured open; blood streamed down his face so forcefully that when he screamed it spattered over Duprey.'
    RECRUIT 'You... You broke my nose!'
    DUPREY 'MEDIC! Get this man to the ward.'
    hide cg_black_scout with easeoutright
    'As a small team of people hurried over to drag the now delirious man through some black steel gates, the Captain casually continued his speech.'
    show duprey at center with ease
    DUPREY 'Anymore {i}questions{/i} about the practicality of my methods?'
    
    CROWD '...'
    "I turned my head to look at Markus and found him glancing back, eyes wide open."
    DUPREY 'I CAN’T HEAR YOU, YOU FUCKING WORMS!'
    play sound "audio/cfx/training_aye.ogg"
    CROWD 'SIR, NO, SIR!'
    DUPREY 'Good... because the Demorai will not show you mercy!'
    DUPREY 'They will not fight {i}with honour.{/i}'
    DUPREY 'What they will do is rip you limb from limb and leave you with just enough life to watch as they slaughter your brothers and sisters!'
    CROWD '...'
    DUPREY 'I am not an easy man, I am not a {i}nice{/i} man, but if you listen to me, I might just be the man that teaches you how to stay the fuck alive.'
    CROWD 'SIR, YES, SIR!'
    DUPREY 'Your training begins now, maggots.'
    "Duprey leapt off the platform and headed towards an area of the fort the sound of swords clanking was coming from."
    hide duprey with dissolve
    DUPREY "On me!"
    "The crowd of recruits followed the dwarf, shuffling their feet towards the training area."
    "I turned around, and couldn't see Markus."
    MC "(*Sigh* Okay, let's get this over with.)"

    $ QstSetProgress(QstForgedInFire, 2)
    $ LocEnter()

label qst_ForgedInFire_AtTrainingYard:
    "Entering the training area, I navigated my way through a crowd of recruits until I saw Markus beside me."
    show markusprologue at right_f with dissolve
    show mcprologue at left with easeinleft
    MC "Markus?"
    MARKUS "Tried to find an escape route?"
    "A couple recruits glanced at us over their shoulders."
    MARKUS "Yeah, right... Let's enjoy the show now."
    DUPREY "Recruits, stand at attention!"
    play sound "audio/cfx/training_aye.ogg"
    hide mcprologue
    hide markusprologue
    with dissolve
    show duprey at center with dissolve
    DUPREY "Let's see what we're working with here!"
    "Duprey glared at us, evaluating the raw material he was about to begin his work on."
    DUPREY "For starters, give me twenty laps along these walls."
    scene black with dissolve
    'The next few hours were a flurry of footwork and drill manoeuvres.'
    'There was nothing performative about it, no crowds to admire the techniques, utterly practical evaluation of our physical abilities.'
    'Finally, exhausted and covered from head to toe in mud and bruises, the Captain called out for us to cease and form orderly ranks.'
    $ TimeAdvTo(TIME_VISUAL_DUSK)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY 'Very good, all... Very good!'
    show duprey:
        ease 2.0 xcenter 0.6
        ease 2.0 xcenter 0.4
        repeat
    'As the Captain got off the podium, he wandered menacingly up and down the new, now exhausted recruits.'
    'He finally stopped in front of the girl I had eyed up earlier.'
    hide duprey with dissolve
    show duprey at center with dissolve
    DUPREY '{i}You...{/i}'
    show duprey at cleft with easeoutleft
    show kiara scared at cright_f with easeinright
    KIARA @scared'... M-Me, sir?'
    DUPREY 'Yes, fucking you! Who else did you think I was talking to?'
    KIARA @scared 'Yes, sir! Sorry, sir!'
    'Her voice was soft, but clearly northern as it had the heavy twang of the highland regions.'
    'The Captain stared at her for a few moments, allowing the distinctive accent to roll off her tongue before asking.'
    DUPREY '... And where are you from?'
    KIARA'Angmurus, sir!'
    show duprey
    show kiara
    DUPREY @laugh 'Angmurian, you say?'
    'The Captain smirked.'
    show duprey
    DUPREY 'Tell me, girl, is it true you all learn to master dual blades?'
    KIARA'I... It is mostly for traditions sake, sir.'
    DUPREY 'I didn’t ask if it was fucking for tradition or not, I asked if it was true.'
    KIARA @scared'Yes, sir!'
    DUPREY '... So, you’re {i}not{/i} just here to suck cock and spread your legs for the men then?'
    'There was some laughter from the recruits as the girl’s face flooded crimson.'
    KIARA'... No, sir.'
    DUPREY 'Well, then...'
    show duprey at nod
    'The Captain grabbed two wooden blades and threw them at her feet.'
    DUPREY '{i}Prove it.{/i}'
    'The girl paused and waited for a moment as the Captain took out a wooden staff and stepped up onto the podium.'
    DUPREY '... Well, pick them up!'
    show kiara at nod
    'The girl did as she was told.'
    DUPREY 'Now get your fat ass up here, girl. I don’t have all day!'
    'There were some laughs again from a couple of the recruits.'
    DUPREY @angry 'DID I SAY YOU COULD FUCKING LAUGH?'
    DUPREY '... Are you ready?'
    'The girl raised her blades hesitantly.'
    DUPREY '... BEGIN!'
    show duprey:
        ease 0.5 xcenter 0.5
    show kiara:
        ease 0.5 xcenter 0.7
        shake
    'We watched as the Captain lunged forward aggressively with the spear.'
    play sound "audio/cfx/parry_sequence.ogg"
    'Much to everyone’s surprise, the girl did far better than expected.'
    'She deflected each blow parried her way and at one point even managed to kick the Captain back with her foot.'
    show duprey at shake
    show kiara at blurin, shake
    'The possibility that she might win hung tentatively in the air...'
    'At the last moment, she managed to deflect another one of the Captain’s blows before swinging for him with what would have been a deathblow.'
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    hide kiara with easeoutright and flash
    'Before she could make it though, the Captain reached out his hand and, to everyone’s shock, a bolt of energy blasted the girl so brutally that the wood beneath her splintered as she hit the floor.'
    show duprey:
        ease 0.5 xcenter 0.3
    show kiara scared with easeinright:
        xcenter 0.7
        xzoom -1.0
    'As he brushed himself off, the girl looked up at the Captain, dazed and confused.'
    KIARA @scared 'But... {i}how?{/i}'
    KIARA @scared 'There’s no magic circle! How did you—'
    DUPREY 'A good attempt, girl. You almost had me there.'
    'The Captain held out a hand, helping her back to her feet.'
    'As he pulled her up, he leaned in to whisper something in her ear and his lips curled upwards into a small smile.'
    KIARA @scared 'I don’t understand though... That kind of magic...'
    'The Captain smirked as he kicked some of the hay aside and revealed a magic circle concealed beneath.'
    'The crowd murmured, half in awe, half in surprise.'
    DUPREY 'Like I said, girl, here, we don’t teach the fancy stuff.'
    DUPREY 'We teach you how to win. No matter what.'
    'The crowd applauded and cheered as the girl smiled sheepishly.'
    hide kiara with easeoutright
    'When she got off the podium, she was welcomed back by the others who all patted her on the back for a fight well fought.'
    show duprey at center with easeinleft
    DUPREY 'Alright everyone!'
    DUPREY "It's a start alright, but we still have a lot of work ahead of us!"
    DUPREY "Now, go and take some rest."
    $ CharMeet("duprey")
    DUPREY "By the time the sun hits these training dummies, I expect you lot here again!"
    DUPREY 'Dismissed!'
    $ AddExpPlayer(50)
    play sound "audio/cfx/training_aye.ogg"
    $ AutoTimeFreeze(False)
    $ BlockWaitGlobal(False)
    $ QstSetProgress(QstForgedInFire, 3)
    $ ShowTutorialPopup("game_time")
    $ LocEnter()

#############################################################################################################
############# REPEATING TRAINING EVENTS SECTION BEGINS HERE ###############################################
############# FIRST TRAINING EVENT & KIARA SCENE ##########################################################
label qst_ForgedInFire_Training0FirstFight:
    scene black with dissolve
    $ Pause(0.5)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY "It stands to reason, you maggots."
    DUPREY "That to {i}kill{/i} the enemy, you must first strike him."
    DUPREY "You cannot hesitate with your blade, not even for a second."
    DUPREY "The Demorai will spare you no quarter."
    DUPREY "They know no fear."
    DUPREY "Hesitation does not exist in the minds of the enemy you will face."
    DUPREY "They will not stop, they will keep coming until {i}you{/i} are dead."
    DUPREY "...So {i}you{/i} will not stop, {i}you{/i} will know no hesitation either."
    DUPREY "{i}You{/i} will make them kiss the blades you carry and grant them the death they so crave!"
    "There was some cheering, whistles and claps from the recruits, but Captain Duprey remained stoically the same."
    DUPREY "When you strike at an enemy, if you're too slow they may dodge or block the strike."
    DUPREY "Get used to that feeling of metal clashing, you lose your blade out in the field, {i}you're finished.{/i}"
    DUPREY "Now grab someone to spar with."
    DUPREY "...BEGIN!"

    $ ShowTutorialPopup("combat_first")
    $ AutoTimeFreeze(True)

label qst_ForgedInFire_Training0FirstFight_repBattle:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ StartBattle(BattleData(BackgroundImage = "pbat_fort_sebastian", CharIDList_Right = ["markus"], CanAutoBattle = False, CanTransform = False, ContinueOnDefeat = True))

    $ LocFlush()
    show mcprologue at left
    show markusprologue at right_f
    with dissolve

    $ AutoMus(True)

    if LastBattleOutcome == "victory":
        MARKUS "That was... good."
        "Markus caught his breath and asked:"
        MARKUS "Say, wanna go again?"
    if LastBattleOutcome == "defeat":
        MARKUS "You could do better, [player_name!t]."
        "Markus looked around and figured we could go for another round."
        MARKUS "Let's go again, shall we?"
    menu:
        "{image=[ICON.SWORDS]} Go again":
            MARKUS "That's my [player_name!t]!"
            MARKUS "Let's learn to handle these sticks of ours proper..."
            MC "Sticks of ours? Wha~"
            MARKUS "Defend yourself!"
            $ HealParty(Silent = True)
            jump qst_ForgedInFire_Training0FirstFight_repBattle

        "Enough for today":
            MARKUS "Fair enough."

    $ AutoTimeFreeze(False)
    scene black with dissolve

    $ AddExpPlayer(50)
    "We have spent the remainder of the day practicing more basic combat moves."
    $ TimeAdvTo(TIME_DAY_END)
    "Exhausted, I made my way back towards the barracks."
############# borras "goclean" stuff
    $ LocSet("novaras_fort_seb_barracks")
    $ LocFlush(dissolve)
    show mcprologue at cleft with easeinleft
    "Entering the barracks, I was whistled over by a towering warrior I have seen a couple times before in the fort."
    show borras at cright_f with easeinright

    OFFICER @talk "[player_name!t], isn't it?"
    show mcprologue at nod
    MC @talk "Yes sir."
    OFFICER @talk "I am First Officer Borras, Captain Duprey's second in command."
    "I gulped as my body straightened and stiffened on its own."
    MC @talk "S-sir?"
    BORRAS @talk "You're on cleaning duty tonight."
    $ CharMeet("borras")
    MC @talk "(Arrgh! Come on now!)"
    show mcprologue at nod
    MC @talk "...Yes sir."
    scene black with dissolve
    $ LocSet("novaras_fort_seb_train")
    "I spent the next hour or so mopping, polishing and cleaning the barracks from top to bottom."
    $ TimeAdvBy(TIME_1H)
    "Finally, I found myself finished."
    MC "{i}*Sigh*{/i}"
    MC "(All that's left to do is clean the wash area.)"
    "As I headed in, I heard what sounded like... splashing?"
    "At this hour?"
    "Realizing the splashing was coming from the woman's side, I pondered what to do..."
    menu:
        "Investigate":
            scene kiara_prol_wash with dissolve
            $ Pause(0.5)
            "It had felt like forever since I last got the chance to see a woman naked."
            "The temptation was too much to bear, and, letting my curiosity get the best of me, I peeked around the woman's side to take a look."
            if CharGetVar("kiara", "met") == True:
                "Kiara was squatted down naked, washing herself with a wet flannel and bucket."
                KIARA "So, are you just going to stand there and watch?"
                MC @scared "K-Kiara!"
                "Realizing I'd been caught, Kiara, grabbing a towel, wrapped it around herself as she marched over towards me, arms folded."
                MC @scared "It... It isn't what it looked like?"
            else:
                "That scout girl I've seen around was squatted down naked, washing herself with a wet flannel and bucket."
                KIARA "Kiara. Pleasure meeting you."
                $ CharSetVar("kiara", "met", True)
                $ CharMeet("kiara")
                $ KIARA = Character(_("Kiara"), image = "kiara")
                MC @scared "Wh-what..."
                "As I realized I was caught, I shot words at her in an apologetic burst:"
                MC "[player_name!t], pleasure's all mine, I'm sorry I was~"
                "Kiara grabbed a towel, wrapped it around herself as she marched over towards me, arms folded."
            $ CharSetClothes("kiara", "towel")
            $ CharSetClothes("mc", "normal")
            $ LocFlush()
            show mcprologue at cleft
            show kiara at cright_f
            with dissolve
            KIARA @angry "So you {i}weren't{/i} just spying on me then?"
            MC "N-No, I came here to clean the wash rooms, I swear it so!"
            "Kiara's stern expression softened as she laughed."
            KIARA @happy "Haha, relax."
            KIARA "I'm just playing with you."
            "Kiara winked."
            KIARA "You can take a look anytime you want, cutie."
            MC "I - {i}*Cough*{/i}"
            MC @talk "What are you doing here?"
            KIARA "Some guard fell sick, so I got pulled to do some evening patrol duty."
            KIARA "I decided to clean myself up before I went back to my bed."
            MC "I - I see..."
            "Kiara playfully smirked, tracing her finger down my chest."
            KIARA "So... Did you like what you saw then?"
            MC "K-Kiara..."
            KIARA "Don't think I haven't felt your eyes on my ass every time I walk past."
            "Kiara's fingers trailed down my chest towards my belt, which she grabbed a hold of as she pulled me closer."
            KIARA "Hardly fair though, is it?"
            KIARA "You get to go back to sleep now, stroking your cock thinking about my ass and what do I get? Hmm?"
            "Kiara's hands began to gently tug at my clothes to pull them down."
            "Inches away from me, there was something about her, her scent, her sultry eyes, her tight body..."
            "This girl drove me feral with desire."
            KIARA "{i}It's only fair I also get to see...{/i}"
            "Before Kiara could claim her prize, we heard the flap of some cloth."
            
            GUARD "How long are you going to be girl? HURRY UP!"
            KIARA @angry "In a moment!"
            KIARA @angry "{i}...Fuck.{/i}"
            "Grabbing her clothes up from the floor, Kiara smiled as she re-dressed herself, giving me a brief good second show of her body."
            $ CharSetClothes("kiara", "normal")
            show kiara at nod
            "As she left the washroom, she run her hand down my chest once more as she passed by."
            KIARA "We'll have to even the score next time, hm?"
            MC "S-Sure."
            KIARA "Hahaha, {i}you and I are going to make great friends...{/i}"
            hide kiara with easeoutleft
            GUARD "DON'T MAKE ME COME IN THERE GIRL!"
            KIARA @angry "I'M COMING!"
            scene black with dissolve
            $ CharSetClothes("kiara", "normal")
            $ CharSetClothes("mc", "scout")

            GUARD "There you are!"
            GUARD "Get back to your quarters already before the damn captain sees!"
            GUARD "I said I'd give you ten minutes for a quick wash! Not an hour!"
            GUARD "Tschh! I'm going, I'm going!"
            $ UnlockGalSceneAndGrantXp("kiara", "prol_wash")
            MC "{i}*Sigh*{/i}"
            MC "(Something tells me that girl is {i}certain{/i} trouble.)"
            MC "(Why did she have to be so damn... {i}alluring{/i} though?)"
        "Don't investigate.":
            "Deciding it wasn't worth risking getting in trouble over, I simply carried on with my duties before heading back towards the barracks, exhausted and in desperate need of sleep."

    scene black with dissolve
    $ LocSet("novaras_fort_seb_barracks")
    $ LocEnter()

label qst_ForgedInFire_Training0NightEvent:
    scene black with dissolve
    $ tmpvar["advancebydays"] = 10
    while tmpvar["advancebydays"] > 0:
        $ TimeAdvBy(86300)
        $ tmpvar["advancebydays"] -= 1
    $ tmpvar = {}
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ Pause(0.5)
    "Days over days of intense, all-round training consumed us."
    "We had to be up very early every day and stayed out in the yard until the sunset, the sounds of sword fighting following us into our dreams."
    "Captain Duprey enforced a rigorous routine: every day began with us making our beds and ensuring that the living conditions were immaculate."
    "I have noticed a subtle, ongoing change in how we reacted to the disciplinary nightmare around us:"
    "The tasks we normally found annoying and handled with haste or carelessness now became more and more of a mindless, automatic sequences of actions for us."
    "There was a certain weird appeal to it, which left me wondering..."
    "Just how much {i}change{/i} will I go through, being a part of the Scouts Corp?"
    $ Pause(0.5)
    $ TimeAdvTo(TIME_VISUAL_DAWN)

    $ QstSetProgress(QstForgedInFire, 4)
    $ QstForgedInFire().TrainingProgress = 1
    $ LocEnter()

#############################################################################################################
############# SECOND TRAINING EVENT & REGINA ENCOUNTER ###############################################
label qst_ForgedInFire_Training1SkillsAndEnergyAndItems:
    scene black with dissolve
    $ Pause(0.5)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY "How many strikes are needed to end a fight?"
    "There were murmurs amongst the recruits as random answers were thrown out."
    
    RECRUITS "{i}As many as it takes!{/i}"
    RECRUITS "{i}Lots?{/i}"
    RECRUITS "{i}Uhh, depends where you hit?{/i}"
    DUPREY "{i}One.{/i}"
    DUPREY "One is sufficient."
    DUPREY "Do not over exert yourself wasting time when one blow will suffice."
    DUPREY "...Today, we're going to be practicing a special attack."
    DUPREY "The more 'special' the move, the more {i}energy{/i} you waste."
    DUPREY "Becoming too tired in a battle is a death sentence, keep this in mind..."
    DUPREY "Knowing how and {i}when{/i} to use special moves like these can be the difference between life and death."
    DUPREY "Besides that, our weapons, armor and skills are not our {i}only{/i} tools."
    DUPREY "Elixirs, poisons, kick fucking sand in their eyes for all I care."
    DUPREY "The point is, you will each be expected to carry some basic supplies with you such as health vials."
    DUPREY "I cannot count the amount of times I've seen men bought back from the edge of death thanks to these beauties."
    "Captain Duprey dangled one of the elixirs in his hand."
    DUPREY "Each of you will now spar, and upon injuring the other, use one of these."
    show cg_guard at right_f with easeinright
    "Quartermaster Joakim moved down the line, handing each of us a small elixir."
    if PlayerItemQty("potion_heal_minor") < 1:
        $ PlayerAddItem("potion_heal_minor")

    JOAKIM @talk "Don't use it all at once, greenhorns!"
    hide cg_guard with easeoutleft
    "Joakim laughed to himself as he retreated off to the sides, folding his arms and smiling as he waited for the spectacle to begin."
    DUPREY "Now, partner up for sparring."
    DUPREY "...BEGIN!"

    $ ShowTutorialPopup("combat_skills_and_items")

    $ AutoTimeFreeze(True)

label qst_ForgedInFire_Training1SkillsAndEnergyAndItems_repBattle:
    
    if PlayerItemQty("potion_heal_minor") < 1:
        $ PlayerAddItem("potion_heal_minor")
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ worldChars["markus"]["CharSkills"] = {"WarriorHeavySlash":1}

    $ StartBattle(BattleData(BackgroundImage = "pbat_fort_sebastian", CharIDList_Right = ["markus"], CanAutoBattle = False, CanTransform = False, ContinueOnDefeat = True))

    $ LocFlush()
    show mcprologue at left
    show markusprologue at right_f
    with dissolve

    $ AutoMus(True)

    if LastBattleOutcome == "victory":
        MARKUS "*Huff* *Huff* You sure have got some {i}special moves{/i}, [player_name!t]."
        "After Markus caught his breath, he asked:"
        MARKUS @smile "Care to give me another chance?"
    if LastBattleOutcome == "defeat":
        MARKUS "Come on, [player_name!t]."
        MARKUS @smile "Where's your mojo? Your battle-jive?"
        MC "My... *Huff* *Huff* ...What?"
        MARKUS "Let's go again, I felt as if I was swinging it against a training dummy!"

    menu:
        "{image=[ICON.SWORDS]} Go again":
            MARKUS "That's better now!"
            MARKUS @smile "Remember, 'special moves like these can be the difference between life and death'!"
            "Markus smiled as he perfectly quoted Duprey."
            MC "Okay, I'll kick your ass now, {i}captain{/i}."
            MARKUS "On guard!"
            $ HealParty(Silent = True)
            jump qst_ForgedInFire_Training1SkillsAndEnergyAndItems_repBattle

        "Enough for today":
            MARKUS "Okay then."
            MARKUS "It was kinda cool though, wasn't it?"
            MC "Yeah, beats swinging it against these training dummies!"

    $ AutoTimeFreeze(False)

    scene black with dissolve

    $ AddExpPlayer(50)

    "For the remainder of the day, Duprey educated us on the nuances of using various special skills, tools and items in battle."
    "Exhausted, I didn't really get much of it: magic refraction scrolls, ensnarement crystals, Vulshan smoke bombs..."
    "Come dusk, Duprey concluded with showing us some advanced combat moves, I guess to somehow inspire us to master the art of combat."
    $ TimeAdvTo(TIME_DAY_END)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY "...So this is how you do the Waltzing Bazark strike."
    "Duprey caught his breath after executing a rather spectacular combat move."
    "He scanned the crowd of recruits, totally exhausted from another training session, and I can promise I saw a hint of fatherly smile on his face."
    DUPREY "Okay, you lot."
    DUPREY "Go and take some rest now."
    play sound "audio/cfx/training_aye.ogg"
    hide duprey with dissolve
    show mcprologue at left
    show markusprologue at right_f
    with dissolve
    "Me and Markus looked at each other in confusion:"
    MC "A Waltzing Bazark? I'm not even trying something like that."
    MARKUS "You'd be collecting me from all over the yard if I did..."
    $ LocEnter()

transform blur_in_and_out:
    parallel:
        ease 2.5:
            #xoffset 10
            zoom 1.01
        ease 2.5:
            #xoffset -10
            zoom 1.0
        repeat
    parallel:
        ease 1.5:
            blur 6.0
        ease 3.0:
            blur 1.0
        repeat

transform irritating_shake:
    subpixel True
    align (0.5, 0.5)
    zoom 1.05
    parallel:
        linear 0.05:
            xoffset -3
        linear 0.05:
            xoffset 3
        repeat
    parallel:
        linear 0.1:
            yoffset 3
        linear 0.1:
            yoffset -3
        repeat

######### regina walkin event
label qst_ForgedInFire_Training1NightEvent:
    scene black with dissolve
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ TimeAdvBy(TIME_2H)
    $ TimeAdvBy(TIME_1H)
    $ Pause(0.5)
    REGINA "...[player_name!t]."
    REGINA "Wake up, [player_name!t]."
    $ LocFlush()
    show regina at center_f, blur_in_and_out
    with dissolve
    "As my eyes slowly peeled open, a dark, raven haired blob was stood, lurched over the side of my bed."
    "My vision became clearer: there I saw, clear as day, [regina_ref!t] crouched over and smiling towards me."
    MC @surprised "[regina_ref_cap!t]?"
    "[regina_ref_cap!t] placed her finger over her lip and motioned for me to be silent."
    "{i}Was this some kind of a dream?{/i}"
    "She leaned in close to whisper."
    REGINA @smile "I've bought you some things, dear."
    REGINA @talk "{i}Just a little something between the two of us...{/i}"
    MC @surprised "How ... How did you even get in here?"
    REGINA @talk "Don't worry about that now, dear."
    REGINA @talk "I just wanted to see you."
    MC @talk "But-"
    "As her hand gently caressed my cheek, I began to feel myself drifting back to the darkness once again."
    scene black with dissolve
    "{i}Perhaps, this really was a dream?{/i}"
    REGINA @talk "Shhh... {i}Sleep, dear.{/i}"
    REGINA "{i}I'll always be here for you...{/i}"
    REGINA "{i}...no matter what.{/i}" #Flash of creepy CG? "
    $ Pause(0.5)
    $ HideUI(True)
    $ AutoMus(False)
    stop music fadeout 0.05
    play sound "audio/cfx/darkness_erupt.ogg"
    scene cg_kiaradeath at irritating_shake with Dissolve(0.1)
    $ Pause(0.1)
    scene cg_prologue_duprey2 at irritating_shake with Dissolve(0.1)
    $ Pause(0.1)
    scene cg_heavy_fight at irritating_shake with Dissolve(0.1)
    $ Pause(0.1)
    scene cg_obelisks_tentacles at irritating_shake with Dissolve(0.1)
    $ Pause(0.1)
    scene cg_mc_eye at irritating_shake with Dissolve(0.1)
    $ Pause(1.5) 
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ HideUI(False)
    $ LocFlush()
    $ CharSetClothes("mc", "normal")

    show mcprologue scared at cright
    show markusprologue at cleft
    with Dissolve(0.2)
    "Springing upright in my bed, soaked in sweat, I looked around as people prepared themselves for another day of training."
    show mcprologue scared at blurin, cright_f
    $ AutoMus(True)
    MARKUS "[player_name!t]? Are you alright?"
    MC @scared "I ... I think so."
    MARKUS "Bad dreams?"
    show mcprologue at cright_f
    MC @scared "...I'm not sure what it was."
    MARKUS @shock "Well, you look like you've seen a ghost!"
    "Somehow, a ghost felt more explainable than what I saw last night..."
    MARKUS "Come, I'm sure a few whacks from a training sword will take your mind off whatever it was!"
    show markusprologue at blurin, cleft_f
    hide markusprologue with easeoutleft
    "As Markus headed out of the barracks towards the training yard, I shook my head, pushing the strange dream aside."
    show mcprologue at center with easeinright
    "Opening my chest to grab my uniform, I noticed immediately the strangely placed bottle of red wine that wasn't there before..."
    $ PlayerAddItem("qst_wine_bottle")
    MC @scared "(It... It was a dream!)"
    show mcprologue at nod
    $ CharSetClothes("mc", "scout")
    MC @think "(...Right?)"
    $ QstForgedInFire().TrainingProgress = 2
    $ LocEnter()

#############################################################################################################
############# THIRD TRAINING EVENT: TEAMWORK & NIGHT TALK OF DUPREY/BORRAS/NYX ###############################################
label qst_ForgedInFire_Training2Teamwork:
    scene black with dissolve
    $ Pause(0.5)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY "...So, having being around a little, what do you lot think matters the most in battle?"
    "We looked at each other puzzled."
    
    RECRUITS "{i}Strength?{/i}"
    RECRUITS "{i}Our gear!{/i}"
    "Some of us were throwing more words out there, until..."
    RECRUITS "{i}Being like... a single force?{/i}"
    "I swear I saw a hint of suprise on Duprey's face:"
    DUPREY @laugh "Right on, lad!"
    "Silence covered our ranks, as we have began to realize what today's lesson was about."
    "Duprey smiled for a moment as he continued:"
    DUPREY "Teamwork, lads."
    DUPREY "Confidence in a soldier to your left and a soldier to your right, {i}this{/i} is the driving force behind any worthy army."
    "Duprey began pointing at recruits from the crowd:"
    DUPREY "You can have the best gear in all Alderay!"
    DUPREY "And you can be an expert at handling your weapon of choice,"
    DUPREY "While your bag of dirty tricks can grow as large as to become a caravan,"
    "Some recruits laughed as Duprey continued, ever more serious:"
    DUPREY "But if you don't have a warrior, a true battle brother you are dead sure in at your side,"
    DUPREY "One who would stand with you no matter what is coming at you..."
    "Duprey's expression turned pale for a moment, as if his mind's eye erupted with memories."
    DUPREY "You {i}will be{/i} obliterated."
    "Me and Markus looked at each other and nodded stoically, but Duprey's usual commanding tone snapped us out of it quick:"
    DUPREY "None of us would want that to happen, right you maggots?!"
    play sound "audio/cfx/training_aye.ogg"
    DUPREY "Today, you will spar in teams of two!"
    DUPREY "Partner up, and get to it!"
    DUPREY "...BEGIN!"

    $ ShowTutorialPopup("combat_team")
    $ AutoTimeFreeze(True)
###### teamfight rep battle
label qst_ForgedInFire_Training2Teamwork_repBattle:
    
    if PlayerItemQty("potion_heal_minor") < 2:
        $ PlayerAddItem("potion_heal_minor")
    if PlayerItemQty("potion_heal_minor") < 2:
        $ PlayerAddItem("potion_heal_minor")

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ StartBattle(BattleData(BackgroundImage = "pbat_fort_sebastian", CharIDList_LeftExtra = ["e_alderay_scout"], CharIDList_Right = ["markus", "e_alderay_scout"], CanAutoBattle = False, CanTransform = False, ContinueOnDefeat = True))

    $ LocFlush()
    show mcprologue at left
    show markusprologue at right_f
    with dissolve

    $ AutoMus(True)
    if LastBattleOutcome == "victory":
        MARKUS "Phew... You guys kicked our ass!"
        MARKUS "Let's go again now!"
        MARKUS "I swear you won't get us this time!"
    if LastBattleOutcome == "defeat":
        "Markus and his teammate both looked at us two."
        MARKUS "Come on guys, remember what Duprey said!"
        MARKUS "Be a single force!"
        "His teammate interrupted:"
        
        RECRUIT "Actually... it was me who said it..."
        "I let out a laugh which echoed painfully all over my body."
        MARKUS "... Whatever! Come on, let's go for another round!"
    menu:
        "{image=[ICON.SWORDS]} Go again":
            MARKUS "That's what I like to hear!"
            MARKUS @smile "Let's see if our 'army' defeats yours this time!"
            $ HealParty(Silent = True)
            jump qst_ForgedInFire_Training2Teamwork_repBattle
        "Enough for today":
            MARKUS "Okay then."
            MARKUS "I've sprained my ankle anyways..."
    $ AutoTimeFreeze(False)
    scene black with dissolve
    "The rest of the day we have spent learning more nuances about working together as a combat unit."
    "As we have come to realize the importance of teamwork in practice, Duprey's initial statement of it being the crucial aspect of warfare became clear as day."
    "We had to {i}become{/i} the Second Scouts Division."
    $ TimeAdvTo(TIME_DAY_END)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY "...So, that will be it for today, Scouts."
    DUPREY "And one more thing..."
    DUPREY "We can't be training in this cage forever,"
    "Duprey waved at the walls,"
    DUPREY "But before we begin any real training maneuvers, I need to see just how much you lot had learned since you've got here."
    DUPREY "Hit that bunk hard for there will be a test tomorrow!"
    DUPREY "Dismissed!"
    play sound "audio/cfx/training_aye.ogg"
    hide duprey with dissolve
    show mcprologue at left with easeinleft
    show markusprologue at right_f with easeinright
    "Me and Markus exchanged looks."
    MARKUS "A test, huh?"
    MC "Whatever it is, let's go get some sleep."
    hide mcprologue
    hide markusprologue
    with dissolve    
     
    $ AddExpPlayer(50)
    $ QstSetProgress(QstForgedInFire, 5)
    $ LocEnter()

######### event after teamfight
label qst_ForgedInFire_Training2NightEvent:
    scene black with dissolve
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ TimeAdvBy(TIME_2H)
    $ TimeAdvBy(TIME_1H)
    $ TimeAdvBy(TIME_1H)
    $ Pause(0.5)
    "In the dead of night, I was restless."
    $ CharSetClothes("mc", "normal")
    $ LocFlush()
    show mcprologue at center_f
    with dissolve
    "Opening my eyes, I sat-upright in my bunk and looked around."
    show mcprologue at blurin, center
    "Everyone around me was deep in sleep still, including Markus."
    "I sighed, rubbing my forehead as I climbed out of bed."
    "{i}Just a short walk around the fort grounds{/i} I told myself..."
    "I'll be back before anyone even realizes I'm gone."
    show mcprologue at blurin, center_f
    hide mcprologue with easeoutleft
    scene black with dissolve
    $ LocSet("novaras_fort_seb_yard")
    $ LocFlush(dissolve)
    show mcprologue at left with easeinleft
    "As the cold night air hit my lungs, I thought about heading back inside before I heard Captain Duprey's voice."
    DUPREY "Thank you all for coming..."
    MC "(Hm? What's going on?)"
    MC "(It sounds like it's coming from the training yard.)"
    scene black with dissolve
    $ LocSet("novaras_fort_seb_train")
    $ LocFlush()
    $ AutoMus(False)
    $ PlayMusic("audio/music/41_Dunewave.ogg")
    show duprey at cleft
    show borras at cright_f
    with dissolve
    $ CharSetClothes("nyx", "robe")
    
    "Peering around the corner, Captain Duprey stood alongside Borras as two figures joined them."
    show nyx at left with easeinleft
    show lukkan at right_f with easeinright
    "The first, a beautiful, yet stern and cold looking blonde in a hooded robe."
    "The other, a man of larger stature who I had not seen either." #Nyx and Lukkan, both are marked as ??? 

    NYX_BLONDE @angry "Well, out with it."
    NYX_BLONDE @angry "Why did you ask us to meet here and not in my office?"
    NYX_BLONDE @angry "I'm freezing my tits off out here you know."
    LUKKAN_THE_BIG_GUY @happy "I could keep them warm for you if you wish."
    show nyx at shake
    NYX_BLONDE @angry "Lay a hand on me and you will never {i}touch{/i} anything again."
    LUKKAN_THE_BIG_GUY @happy "Feisty as always."
    DUPREY "I'm sorry for summoning you both at such a late hour."
    DUPREY "I couldn't risk the potential of spies listening in on what I had to say now."
    NYX_BLONDE @angry "And out here is safer than my office how?"
    DUPREY "{i}*Sigh*{/i} I recently conducted a private search across the whole fortress with only my most trusted men."
    DUPREY "I found echo crystals everywhere... including your office."
    NYX_BLONDE @shock "You..."
    NYX_BLONDE @shock "{i}Echo crystals?{/i}"
    NYX_BLONDE @angry "That can't be right, I have my office checked, I-"
    "Duprey nodded, holding up a small, glowing yellow crystal that he tossed to the robed blonde."
    show duprey at nod
    DUPREY "I'm afraid it's so."
    "The woman inspected the crystal and gritted her teeth in anger at it."
    DUPREY "It seems our great {i}'emperor'{/i} does not hold our loyalty in high regard."
    "The larger man chuckled."
    LUKKAN_THE_BIG_GUY @happy "After everything that's happened, can you truly blame him?"
    "The blonde woman seemed more frustrated than the others, coiling her one hand into a tight fist."
    LUKKAN_THE_BIG_GUY @happy "Come now, this is all part of the game."
    NYX_BLONDE @angry "Yes, I... I am aware."
    DUPREY "The guards only patrol this area periodically, and it's the one place no echo crystals turned up during the search."
    DUPREY "I suppose they figured the chatter of grunts wasn't worth hearing."
    DUPREY "Which is exactly why we're meeting here now."
    "The larger man raised his brow."
    LUKKAN_THE_BIG_GUY @think "That's all well and good... But why exactly is {i}he{/i} here?"
    "The man pointed towards Borras, whose brow furrowed at the comment."
    LUKKAN_THE_BIG_GUY @angry "He's hardly fit to stand here with the rest of us."
    DUPREY "Officer Borras will be replacing me for command of the Second Scouts Division, within a year or so."
    NYX_BLONDE @shock "You're leaving?"
    DUPREY "My time is nearly up... I'm slowing down too much."
    "While the blonde seemed saddened to hear this, the larger man opened his palm upwards towards the sky."
    LUKKAN_THE_BIG_GUY @talk "I hope you didn't drag us out here to discuss your future retirement plans you old fuck."
    DUPREY "Hmph..."
    DUPREY "Officer Borras, hand them the reports."
    BORRAS @talk "Yes Captain."
    show borras at nod
    "Borras handed over a few sheets of paper towards the robed pair."
    LUKKAN_THE_BIG_GUY @talk "What's this?"
    DUPREY "A report that Alcott attempted to suppress."
    LUKKAN_THE_BIG_GUY @think "About?"
    DUPREY "...{i}Zanarak has returned.{/i}"
    "A great unease filled the air and I felt a shiver tingle it's way up my spine."
    "The name crawled and dragged its way horribly across my thoughts."
    LUKKAN_THE_BIG_GUY @happy "There hasn't been a sighting in years."
    NYX_BLONDE @talk "Wasn't it reported that the beast was hunted down by the Inquisition?"
    DUPREY "A lie told to ease panicking nobles."
    DUPREY "While it is true the beast has vanished for the last few years, this cannot be ignored."
    DUPREY "The beast's return... changes things."
    LUKKAN_THE_BIG_GUY @talk "A specter, a boogeyman..."
    LUKKAN_THE_BIG_GUY @talk "There are dozens of Demorai over the years that people have wrongly mistaken for being Zanarak."
    "The man belligerently crossed his arms."
    LUKKAN_THE_BIG_GUY @talk "...I'm not even convinced this Zanarak was real to begin with."
    DUPREY "Oh... He's as real as you and I alright."
    DUPREY "Make no mistake about that."
    DUPREY "...And when he comes, all of us need to be prepared."
    DUPREY "With, {i}or without{/i} the Emperors knowledge."
    NYX_BLONDE @angry "What are you saying, Duprey?"
    DUPREY "I'm saying, Alcott can bury his head in the fucking sand and play politics all he wants to try and appease wet-fart nobles."
    DUPREY "{i}But we need to be prepared for what's to come whether this knowledge is made public or not.{/i}"
    NYX_BLONDE @talk "Duprey... You need to tread carefully with this."
    NYX_BLONDE @talk "How exactly did {i}you{/i} manage to get your hands on this report anyway?"
    BORRAS @talk "By pure chance."
    "Borras stepped forward."
    BORRAS @talk "I was on a normal patrol through the Valley of Death when I stumbled upon a small, slaughtered convoy."
    BORRAS @talk "Amongst their dead was an Inquisitor, who with his dying breath handed me this report."
    LUKKAN_THE_BIG_GUY @talk "The dying words of a delusional Inquisitor on death's door mean very little."
    BORRAS @talk "There was other reports..."
    LUKKAN_THE_BIG_GUY @think "What?"
    BORRAS @talk "Suppressed as soon as they arrive, but more and more scant reports from our men on the fringes have reported seeing it."
    "Both the woman and man were troubled the more they heard."
    DUPREY "From now on, the three of us need to work closer together."
    NYX_BLONDE @angry "The city guard is barely holding on as it is, what exactly do you expect me to do?"
    DUPREY "Whatever you have to do when the time comes."
    "Duprey seemed to be working himself up into a feverish plea."
    DUPREY "These little camps everyone's set up is leaving us more divided than ever, it'll be the ruin of us all!"
    DUPREY "We need to unite and pledge to each other that when the time comes-"
    LUKKAN_THE_BIG_GUY @talk "I promise you nothing, Duprey."
    "The broad man's words cut through Duprey's like ice."
    LUKKAN_THE_BIG_GUY @talk "...But I shall look into these reports myself."
    LUKKAN_THE_BIG_GUY @talk "And depending on what I find, {i}perhaps{/i} there will be more to discuss."
    "The broad man turned to leave, and as he did so, Captain Duprey looked towards the woman."
    NYX_BLONDE @sad "... I don't know, Duprey, this just maybe isn't the right time."
    NYX_BLONDE @sad "The more we unite our forces, the more we paint ourselves a target for the other factions."
    DUPREY "... I don't care about the factions."
    DUPREY "I don't care about the politics of the damn thing."
    DUPREY "What does any of that matter if there's no one left in the end?"
    DUPREY "Newheart is gone... There's no one left to save us but ourselves now."
    NYX_BLONDE @sad "...Goodnight, Duprey."
    NYX_BLONDE @sad "I hope you're wrong about all this... I really do."
    "The woman turned to leave and join the broad man, leaving Captain Duprey to stand beside Officer Borras alone."
    hide nyx
    hide lukkan
    with dissolve
    "As the two figures passed me by, I hid myself behind a barrel and waited for them to be out of sight."
    show duprey at cleft with easeinleft
    show borras at cright_f with easeinright
    BORRAS @talk "Captain..."
    DUPREY "Return to your quarters, Borras."
    DUPREY "Speak nothing of what has been said tonight."
    BORRAS @sad "But-"
    DUPREY "I'm tired Borras... So very tired."
    DUPREY "The next battle can wait for another day."
    show borras at blurin, cright
    hide borras with easeoutright
    "Slowly, I watched as Captain Duprey slumped towards the barracks, likely back to his quarters."
    hide duprey with dissolve
    MC "(Zanarak... Can it really be?)"
    show mcprologue at center with easeinleft
    "I shook my head, pushing the terrible thoughts away."
    MC "(I need to return to my bed, before someone sees me.)"
    hide mcprologue with easeoutright
    scene black with dissolve
    $ CharSetClothes("nyx", "normal")
    $ CharSetClothes("mc", "scout")
    $ LocSet("novaras_fort_seb_barracks")
    "As I laid down onto the bed, dark, terrible thoughts and dreams returned."
    "Returned to torment me for the rest of the night."
    $ AutoMus(True)
    $ Pause(0.5)
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ QstForgedInFire().TrainingProgress = 3
    $ LocEnter()

#############################################################################################################
############# LAST TRAINING EVENT & DEPARTURE INTO NEXT QUEST ###############################################
label qst_ForgedInFire_Training3Final:
    scene black with dissolve
    $ Pause(0.5)
    $ LocFlush()
    show duprey at center
    with dissolve
    DUPREY "Alright maggots, today I will see whether you lot have made any progress or had you just wasted my time!"
    DUPREY "We will start with duels first!"
    DUPREY "Partner up, grab yourself a healing vial, and fight as if your life depended on it!"
    hide duprey with dissolve
    show mcprologue at cleft
    show markusprologue at cright_f
    with dissolve
    MC "Shit got real, huh?"
    "Markus was certainly not going to fool around this time."
    MARKUS @angry "Come on, [player_name!t], let's do this!"
    MC @angry "Alright, bring it on then!"
    $ AutoTimeFreeze(True)
    $ AutoMus(False)
    scene black
########### final duel
label qst_ForgedInFire_Training3Final_Battle:

    if PlayerItemQty("potion_heal_minor") < 1:
        $ PlayerAddItem("potion_heal_minor")

    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(
        BattleData(
            BackgroundImage = "pbat_fort_sebastian", 
            CharIDList_Right = ["markus"], 
            CanAutoBattle = False, 
            CanTransform = False, 
            Label_Victory = "qst_ForgedInFire_FinalSparring_Complete", 
            ContinueOnDefeat = True
        )
    )

    if LastBattleOutcome == "defeat":
        stop music fadeout 1.0
        call qst_ForgedInFire_Training3Final_Lose from _call_qst_ForgedInFire_Training3Final_Lose
        $ HealParty(Silent = True)
        jump qst_ForgedInFire_Training3Final_Battle

########### lost final duel
label qst_ForgedInFire_Training3Final_Lose:
    play sound "audio/cfx/gameover.ogg"
    play ambience "audio/ambience_scenes/obelisks.ogg" fadein 0.5
    scene black
    with flash
    "Ouch."
    "Darkness."
    "Then, dim light telling shapes apart."
    "A vision."
    "A vision of Alderay under demonic onslaught."
    "Of me, defending it's people."
    "Uniting them under my banners."
    "Power."
    "Wealth."
    "Women..."
    "However, there is something else."
    "Something that drives me onwards, something from outside..."
    "It's..."
    stop ambience fadeout 0.3
    play sound "audio/cfx/water_splash.ogg" volume 0.6
    "Ice-cold water!"
    play sound2 "audio/cfx/kick.ogg" volume 0.6
    play ambience "audio/ambience_loc/sebastian.ogg"
    scene bg_sebastian_yard
    show duprey at center
    with flash
    DUPREY "{b}ON YOUR FEET, MAGGOT!{/b}"
    "Captain Duprey's heavy kick quickly stood me up straight, recent knockout echoing in my head with an irritating, pulsing pain."
    DUPREY "Go again, Demorai won't wait for you to come back to your senses!"
    MC "(Gotta get a grip...)"
    DUPREY @angry "I'm trying to be nice to you maggot, now go again!"
    hide duprey with dissolve
    return

########### march out
label qst_ForgedInFire_FinalSparring_Complete:
    $ AutoTimeFreeze(False)
    $ AutoMus(True)
    $ LocFlush()
    with dissolve
    show mcprologue at left with easeinleft
    show markusprologue at right_f with easeinright
    MARKUS "Gah! You sure know how to make it hurt!"
    MC '{i}*Huff*{/i} Someone’s had to knock some sense into you!'
    'As me and Markus caught our breath, I noticed an unusual figure dressed in fine fabrics speaking to the Captain.'
    'The Captain seemed unimpressed with whatever the man was saying and seemed to be refusing him something before being handed what seemed like a very official looking letter.'
    'I thought I could make out the royal seal.'
    'I couldn’t hear what was being said, but I managed to figure out the words escaping his lips, {i}‘They’re not ready yet!’{/i}'
    MARKUS 'What’s going on?'
    'I nudged him to look over towards Duprey.'
    MARKUS '... Is that someone from the palace?'
    MC 'I think so.'
    MARKUS 'Since when did the palace send its fancy officials down to us mud and grunts?'
    MARKUS 'What do you think they want? It must be serious.'
    MC 'I don’t know... but I don’t think it’s going to be anything good.'
    hide mcprologue
    hide markusprologue
    with dissolve
    show duprey at center with dissolve
    'All of a sudden, the Captain heaved himself reluctantly onto the wooden platform and cried out for our attention.'
    DUPREY 'FORM RANKS!'
    play sound "audio/cfx/training_aye.ogg"
    'The tired and weary Scouts hastily moved to form neat rows and face the Captain, hanging on his every word.'
    DUPREY 'We have been ordered on early leave for a mission.'
    'Confused mutterings swept through the ranks, as most of us expected the training to last for months.'
    DUPREY 'SILENCE!!!'
    DUPREY 'This order has come down from Emperor Alcott himself and has been approved by King Mesamor.'
    DUPREY 'We leave come first light tomorrow.'
    DUPREY 'Get to bed early, make sure you’re well fed and be absolutely certain that your equipment is clean and ready.'
    'A timid hand was raised from the crowd.'
    DUPREY 'What is it?'
    
    RECRUIT 'Where are we to be sent, sir?'
    DUPREY 'The mission is top secret, all I can tell you is that you will be recovering relics from a lost fortress south of here.'
    DUPREY 'Expect at least six weeks march, take this into consideration with your prep.'
    DUPREY 'Dismissed!'
    play sound "audio/cfx/training_aye.ogg"
    hide duprey with easeoutleft
    'With that, the Captain stormed his way off stage, angrily shoving the sealed letter back into the fumbling hands of the palace official before stalking back to his quarters.'
    'The men soon dissolved the ranks and the process of packing up for our departure began.'
    $ QstComplete(QstForgedInFire)
    show mcprologue at left
    show markusprologue at right_f
    with dissolve
    $ HealParty()
    'There was much confused chatter about what this {i}‘secret mission’{/i} entailed, and more so the worry of now being confronted by the Demorai so clearly unprepared.'
    MARKUS 'What the fuck was all that about?'
    MC 'I don’t know, looks like some higher up bullshit to me.'
    MC "Guess we'll be skipping the test then..."
    MARKUS 'Hm... I’ll make sure to pack some extra bread for you, okay?'
    MC 'Where’d you get the extra rations from, you fancy fuck?'
    MARKUS 'My brother sent it to me the other day, figured we could split it...'
    MC 'Oh, thank you.'
    MARKUS 'In return I want some of that sweet wine you got!'
    MC 'What?!'
    MARKUS 'Hey! Don’t hold out on me! I know your dear sweet [regina_ref!t] brought you some!'
    MC 'Alright, alright, {i}we’ll share.{/i}'
    MARKUS 'That’s more like it!'
    MARKUS 'Didn’t want to have to bust your balls the whole trip if I die of dehydration because you wouldn’t spare {i}‘a single drop’{/i} for your dearest and oldest friend!'
    MC 'But then how would I achieve my dream of becoming a drunk?'
    MARKUS 'I have every confidence that you’ll find a way, no matter what.'
    show kiara happy at center_f with easeinright
    'Suddenly, the ginger haired girl strutted over to us, a coy little smile on her face.'
    KIARA 'Looks like I’ve been partnered up with you two for the march.'
    MARKUS 'Oh?'
    KIARA @happy 'Aye, that won’t be a problem, will it?'
    MARKUS 'After that little show you put on with the Captain when we first got here? It’ll be our pleasure.'
    MARKUS 'I’ll be sure to let you soften the Demorai up before I get there!'
    KIARA 'How {i}valiant{/i} of you.'
    if CharGetVar("kiara", "met"):
        "I caught her gaze and nodded:"
        MC 'Kiara.'
        'Kiara nodded and smiled mischievously.'
        KIARA 'What do they call your cute friend here?'
        MARKUS 'Hey! I can hear you!'
        KIARA 'I know, honey. So?'
        MARKUS "...It's Markus."
        KIARA @happy 'Well then, pleasure to meet you, Markus.'
        KIARA "I'll take the rear, is that alright with you guys?"

    else:
        MC 'What’s your name?'
        KIARA 'Kiara, love.'
        $ CharSetVar("kiara", "met", True)
        $ CharMeet("kiara")
        'Kiara smiled and winked mischievously.'
        KIARA 'What do they call you cuties then?'
        MARKUS 'Oooh, did you hear that? She thinks we’re cute!'
        KIARA 'Not when you speak, but I’ve seen worse looking.'
        KIARA 'Even if you are pale as a ghost!'
        MARKUS 'Hey!'
        MC 'I’m [player_name!t].'
        MARKUS 'Markus.'
        MARKUS @angry 'And I ain’t no ghost!'
        KIARA 'Pleasure to meet you both, I’ll take the rear?'

    MC 'I don’t see why not.'
    KIARA 'Thanks, makes a change from you always looking at {i}my{/i} rear.'
    MARKUS 'Ha! She’s caught you out good!'
    MC 'I didn’t—'
    KIARA 'I didn’t say I was complaining!'
    KIARA 'You can keep admiring all you like, you’re only human after all.'
    'Markus grinned at me and laughed to himself as he saw how flustered I became.'
    MC '... Hold on, how come you’ve been told to march with us?'
    MC 'I thought you were going to be further back down the line.'
    KIARA 'I might have asked the commander to move me up next to you two...'
    MC 'Why?'
    MARKUS 'Obviously because of my dazzling good looks, [player_name!t]!'
    KIARA 'Keep lying to yourself if that’s what gets you through the day, love.'
    KIARA 'The truth is... everyone’s seen you two fighting.'
    KIARA 'You boys make a good team.'
    KIARA 'Better than most of this lot at least.'
    KIARA '... Figured I’d stand a better chance of survival being partnered up with you two.'
    KIARA 'So, I asked, and the Captain agreed to move me up.'
    KIARA 'Any problems with that?'
    'Me and Markus looked at each other.'
    MC 'Nope.'
    MARKUS 'I’m alright with it.'
    KIARA 'Good, I’ll see you boys later then...'
    show kiara happy at blurin, center
    $ Pause(0.25)
    hide kiara happy with easeoutright
    'Kiara strutted off, presumably to pack her things for the excursion.'
    'Markus smiled ruefully and whistled at me.'
    MARKUS 'Well... someone’s got a fan!'
    MC 'Ha-ha, something tells me that one’s gonna be trouble.'
    MARKUS 'Trouble or not, if you don’t go for her, I sure as hell will!'
    MC 'Hey!'
    MARKUS 'What? If I get a shot at getting laid again before dying, I’m taking it!'
    MC '{i}*Sigh*{/i} Alright, alright, come on now, let’s get ready for this damn march...'

    $ PlayerAddItem("scout_armor", Silent = True)
    $ PlayerAddItem("scout_sword", Silent = True)
    $ PlayerAddItem("scout_armor", Silent = True)
    $ PlayerAddItem("scout_sword", Silent = True)

    $ PartyAddChar("markus")
    $ PartyAddChar("kiara")

    $ PlayerPartyCharEquipItem("markus", "scout_sword")
    $ PlayerPartyCharEquipItem("markus", "scout_armor")
    $ PlayerPartyCharEquipItem("kiara", "scout_sword")
    $ PlayerPartyCharEquipItem("kiara", "scout_armor")

    $ Pause(1.0)

    $ ShowTutorialPopup("party")

    scene black with dissolve
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)

    $ Pause(0.5)
    $ TimeAdvTo(TIME_MORNING)
    jump qst_TheDarkPass_MarchOut