label qst_TheTarbecks_Room_Temptations_main:   
    if "temptations" in QstTheTarbecks().PlayedInRooms:
        if config.developer:
            "DEBUG: already been to this room. override the block and go again?"
            menu:
                "yes":
                    pass
                "no":
                    jump qst_TheTarbecks_AlreadyPlayedInThisRoom
        else:
            jump qst_TheTarbecks_AlreadyPlayedInThisRoom

    "Etched onto the door was the phrase,"
    "{i}Love is sometimes a game of restraint.{/i}"
    scene black with dissolve
    "Pushing open the door, we stepped inside."
    $ LocSet("hamun_tarbeck_room_temptations")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_6

    if QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "ves":
        show ves at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "esme":
        show esme at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left with easeinleft

    "Inside the room were a series of tables, each topped with two large wine glasses and a single lit candle."
    "Couples, hot and flustered, drank with trembling hands and flushed cheeks."
    "A few, already lost to frenzy, straddled one another, wildly fucking atop the tables."
    "Notably, for every couple fucking, their drinks lay spilled on the marble floor and their candle had been extinguished by passing staff."
    "A masked figure drifted closer."
    show cg_tarbeck_watcher at cright_f with easeinright
    WATCHER "Greetings! Are you interested in playing this room's game?"
    MC @think "What game is it?"
    WATCHER "Ahh! It's rather simple!"
    WATCHER "On each table are two glasses for you both to drink."
    WATCHER "You simply need to {i}finish{/i} the drink before losing control!"
    MC @think "Losing control?"
    WATCHER "You'll see..."
    MC @think "What's in the drinks?"
    WATCHER "{i}That's a secret.{/i}"
    WATCHER "Do you wish to play?"
    if QstTheTarbecks().PartyCompanion == "markus":
        jump qst_TheTarbecks_Room_Temptations_markus
    elif QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Temptations_ves
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Temptations_esme
    elif QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Temptations_kiara

label qst_TheTarbecks_Room_Temptations_kiara:
    KIARA @smile "Ha! Sounds like fun to me!"
    "Kiara nudged me and winked."
    KIARA @smile "How hard can it be, hm?"
    KIARA @smile "If being raised in the north taught me anything, it's how to handle my drink!"
    MC @smile "This should be pretty easy for us."
    WATCHER "{i}*Giggles*{/i}"
    WATCHER "Right this way then!"
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    hide mc
    hide kiara
    with easeoutright
    scene black with dissolve
    "Led to a nearby table, Kiara and I took our seats and began to sip our drinks."
    "The first sip was smooth, its richness sweet and tingly on the lips."
    "At first we laughed, thinking perhaps our tolerance—or our dark {i}'gifts'{/i}—would protect us."
    "But quickly the tingle turned to a burn, not painful, but tightening my whole body as my cock hardened."
    "Kiara's hand began to shake as she stared at me, biting her lower lip hard enough to draw blood."
    "Her breath trembled as she took another sip."
    MC "Kiara... {i}*Huff*{/i} we need to stay focused, we need to—"
    "Suddenly, Kiara flung herself across the table."
    MC "Kiara! No!"
    play sound "audio/cfx/bottleBreak.ogg"
    "Her lips crashed into mine, her tongue slipping into my mouth as she clambered onto the table, knocking our glasses to the floor."
    "As the wine spilled, staff rushed over, snuffing out our candle as I forced her back."
    MC "Kiara! KIARA!"
    KIARA "E-Ehhh?!"
    "She blinked, snapping out of it."
    KIARA "S-Shit!"
    KIARA @scared "I didn't mean to—"
    $ LocFlush()
    show mc at cleft
    show kiara at center_f
    with dissolve
    show cg_tarbeck_watcher at cright_f with easeinright
    WATCHER "So sorry! Looks like you lose this game!"
    WATCHER "Better luck in the next one!"
    hide cg_tarbeck_watcher with easeoutleft
    KIARA @sad "Fuck!"
    show kiara at cright_f with ease
    KIARA @sad "I'm sorry, I didn't-"
    MC @talk "It's okay, let's just... Move onto the next game."
    KIARA @sad "Damn it..."
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    show kiara at center_f with ease
    KIARA @sad "(And I'm still horny as shit with nothing to show for it!)"
    hide kiara with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Temptations_over

label qst_TheTarbecks_Room_Temptations_ves:
    menu:
        "Well, how about it, Ves?":
            pass
        "I have a bad feeling about this one.":
            VES @think "Hm... If you think it is unwise to play, then let us move on."
            MC @talk "Lets."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    VES @smile "Ha! An orc laughs in the face of such a challenge!"
    MC @smile "Alright, how hard can one glass of wine be?"
    WATCHER "Come."
    scene ves_tarbeck_temptations_1 with dissolve
    $ Pause()
    "The watcher beckoned us to a candlelit table."
    WATCHER "Take a seat. {i}Relax.{/i}"
    WATCHER "Savor every drop..."
    "Confidently, we sat."
    "With a light clink, we both took a long gulp."
    "The wine was smooth, rich, sweet, and tingling."
    VES "Ha! See?"
    VES "This wine is no match for me!"
    MC "Tell me then, what {i}do{/i} orcs usually drink?"
    VES "Hmm?"
    MC "I'm curious."
    VES "We drink a brew called Hothstol."
    VES "Stronger than anything here, made from a fruit called koopas."
    MC "Koopas?"
    VES "Like your apples, only purple, sharp, often mixed with mushrooms."
    "I laughed, taking another sip."
    MC "Is it just me, or is it getting really warm in here?"
    "Ves stared at me, eyes heavy and alluring."
    "Her breathing had deepened."
    MC "...Ves?"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    VES "I will take you there one day."
    VES "We'll drink all the Hothstol you want."
    scene ves_tarbeck_temptations_2 with dissolve
    $ Pause()
    "Without breaking eye contact, Ves tugged at her dress, exposing one breast."
    $ PlaySexFx("audio/cfx/girl_breathing.ogg", 1)
    MC "Ves!"
    VES "I'm thinking about all the things I want to do to you."
    VES "My handsome, strong..."
    VES "{i}HUMAN{/i} mate."
    "Her breathing became heavier and heavier, and then I felt it too..."
    "As my cock stiffened in excitement, the whole world suddenly seemed to slow as my heart raced."
    "Gods, Ves was so fucking beautiful."
    "All I wanted to do was leap across the table and fuck—"
    "I paused, looking down at the half-drunk glass of wine, and realized what was happening."
    MC "V-Ves! It's the wine!"
    MC "The wine is—"
    scene ves_tarbeck_temptations_3 with dissolve
    $ Pause()
    "Now with both breasts exposed, Ves took another sip of the wine, her cheeks burning red with lust as she spoke aloud her most private, forbidden thoughts."
    VES "Mmm, you're funnyyyy."
    MC "W-What?"
    VES "A strong orc like me isn't weak enough to fall for such a trick."
    VES "{i}*Huff*{/i} I should just pin you down and— {i}*Huff*{/i}"
    "Ves seemed to be getting more and more worked up, my words seemingly falling on deaf ears."
    MC "Ves... {i}*Huff*{/i} We need to finish the wine."
    MC "We need to—"
    "I flinched as I felt Ves' foot brush against my leg beneath the table."
    VES "...Mmmfff..."
    "Her foot continued to slowly slide higher up my leg."
    VES "My big, strong..."
    "Her foot pressed against my cock, straining against my clothes as her toes flexed."
    VES "{i}Mate.{/i}"
    MC "Ves... {i}*Huff*{/i} Please, we need to— Ahh!"
    MC "F-Focus!"
    VES "{i}*Huff*{/i} Hmm? What are we supposed to be focusing on again?"
    "I felt like I might lose it at any moment, and Ves, for whatever reason, seemed completely absorbed in her lustful thoughts."
    "The watcher stared from the sides, perhaps waiting to see if we would crack."
    "Then... an idea came to me."
    MC "Ves."
    VES "Mmmffffhh...?"
    MC "You know, I'm not sure you're strong enough to be my mate."
    VES "...What?"
    VES "WHAT?!"
    $ StopSexFx()
    "The lustful spell over Ves cracked, if only for the briefest moment."
    MC "My mate would be strong enough to finish that glass with ease."
    MC "But here you are, stalling because you can't do it, can you?"
    "Ves ground her teeth, eyes wide as the pink shade of her cheeks turned a furious red."
    VES "YOU..."
    VES "GRGHHHH!"
    VES "You dare call me weak?"
    VES "I am not weak!"
    VES "YOU ARE WEAK!"
    MC "I hear a lot of talking, but that wine is still in your hand."
    "In a moment, Ves gulped down the remains of her glass, then reached over and grabbed mine, downing it as well."
    MC "Ves! No!"
    MC "(Oh fuck, she drank both! She wasn't supposed to—)"
    VES "{i}*Huff*{/i} See?"
    VES "Ves is... {i}*Huff*{/i} strong!"
    "Clapping their hands together happily, the watcher approached."
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    # note that scene ends way down not here
    show cg_tarbeck_watcher at right_f with easeinright
    WATCHER "How delightful!"
    WATCHER "Congratulations! You both managed to withstand your temptations long enough to finish your drinks!"
    $ AutoMus(True)
    WATCHER "Here, for your efforts."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    MC @think "So we're {i}*Huff*{/i} done?"
    WATCHER "Of course..."
    WATCHER "Feel free to do whatever you want now!"
    WATCHER "{i}And I do mean whatever you want.{/i}"
    hide cg_tarbeck_watcher with easeoutleft
    show mc at center with ease
    MC @surprised "... Ves, are you alright?"
    MC @surprised "You drank both glasses! Why would you do such a thing?"
    VES @sad "..."
    MC @sad "... Ves, I-"
    VES @sad "T-Tell me."
    MC @think "Huh?"
    VES @angry "{i}*Huff*{/i} Tell me Ves is strong enough to be your mate."
    MC @sad "Ves... I didn't mean-"
    VES @sad "Say it!"
    MC @sad "... Yes, of course you are."
    $ AutoMus(False)
    stop music fadeout 1.0
    "Ves squirmed on the spot, her cheeks bright red as she averted her gaze."
    VES @sad "{i}*Huff*{/i} P-Please."
    VES @sad "Give me compliments."
    "Her plea was almost a whimper; it was strange seeing Ves quite so..."
    "{i}Feminine.{/i}"
    $ PlayMusicRandom("mus_sex")
    MC @think "... Do you want me to tell you how strong you are?"
    MC @smile2 "{i}Or how beautiful I think you are?{/i}"
    "Ves squirmed again, breathing heavily as she listened."
    MC @bitelip "{b}... Or are you waiting to hear about how I think about fucking you every night?{/b}"
    VES @blush "{i}*Huff*{/i} M-More than the others?"
    MC @think "The others?"
    VES @sad "I know {i}*Huff*{/i} I am not... {i}*Huff*{/i} the most feminine woman."
    VES @sad "But I..."
    show ves at shake
    VES @angry "I g-get jealous of the way you look at them."
    VES @sad "{i}P-Please...{/i}"
    VES @sad "{b}I always want your eyes on me.{/b}"
    MC @sad "Ves..."
    MC @smile "I can barely pull my eyes away from you as it is."
    "Ves trembled, the drink's full effects coursing hotly through her veins."
    VES @blush "I want to taste you."
    MC @surprised "Wait, what?"
    VES @blush "The drink... it's like my whole body is on fire."
    VES @lewd "And hearing you say that..."
    VES @smile "It's enough to drive a girl crazy!"
    "My cock ached painfully, the drink still taking effect in my veins."
    MC @surprised "Ves, we're not... we're not thinking clearly! We can't-"
    VES @blush "My mouth."
    VES @blush "Please... {i}I want it to taste you in my mouth.{/i}"
    MC @surprised "I-"
    show ves at shake
    VES @angry "No more talking!"
    VES @angry "My mate does not just talk!"
    VES @blush "{i}He takes.{/i}"
    MC @surprised "..."
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    $ PlaySexFx2("audio/cfx/body_fall_ground_shorter.ogg")
    scene ves_tarbeck_temptations_4 with dissolve
    $ Pause()
    "Throwing Ves down onto the table, she waited with nervous breath."
    "With my cock out, rubbing against her face, she opened her mouth and ran her tongue along the shaft teasingly."
    VES "Y-Yessss..."
    MC "Is this what you want?"
    VES "Do it! Give me your-"
    $ PlaySexFx("audio/sex_sounds/ves69_150.ogg", 1)
    scene ves_tarbeck_temptations_5 with dissolve
    $ Pause()
    "As I pushed my cock into her mouth, Ves' tongue thrashed and beat against me as she moaned softly."
    VES "{i}*Glug!*{/i} Mmfghh! {i}*Slurp!*{/i}"
    "I let out a sigh of pleasure as I sank my cock a few inches deeper down her throat."
    "Her mouth widened as I slid deeper still."
    VES "{i}*Slurp!*{/i} Mmfghh! {i}*Slurp!*{/i}"
    MC "{i}*Huff*{/i} Oh gods— Ahh!"
    MC "V-Ves! You feel so-"
    VES "{i}*Slurp!*{/i} Mhhfhhhgh!"
    VES "Shuchahhbhighhchockhh! {i}*Slurp!*{/i}"
    scene ves_tarbeck_temptations_6 with dissolve
    $ Pause()
    "Ves' womanhood dripped with excitement as my member slid in and out of her throat."
    "Were others watching?"
    "I could hardly pull my eyes away from her to check, all that mattered was the thought of cumming down Ves' throat as she choked on my cock."
    VES "Mmfghh!"
    "Her eyes began to roll back as I fucked her throat harder, like a man possessed, unable to stop myself as she writhed and squirmed."
    "Was she holding out to prove how strong she was?"
    "Or was she determined to prove how much better she was than the other girls?"
    "As her wet tongue continued to beat and wrap around my cock, at last I felt my aching balls rise until..."
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    scene ves_tarbeck_temptations_finish with flash
    $ ReduceInfectionFromSex("ves")
    $ UnlockGalSceneAndGrantXp("ves", "tarbeck_temptations")
    $ Pause()
    MC "H-HRGHHHHH!!"
    "Ves' eyes widened as she felt thick seed pour down her throat."
    "I watched as she struggled to gulp down every drop of it,"
    "And at last, fully spent, I unsheathed my cock from her mouth as she took a desperate gasp."
    VES "{i}*Cough!* *Cough!*{/i}"
    MC "{i}*Huff*{/i} Ves!"
    MC "You-"
    VES "Your seed..."
    "Ves said breathlessly."
    VES "It tastes so..."
    VES "{i}manly.{/i}"
    scene black with dissolve
    "... Ves rose from the table, wiping her mouth clean as the burning aphrodisiac desire began to fade."
    $ AutoMus(True)
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    VES @surprised "... I can't believe I just did that!"
    VES @shock "What would my clan think if they saw me so... so..."
    MC @smile "Incredible?"
    VES @think "{i}Submissive.{/i}"
    MC @think "Well, it was just the drinks."
    MC @think "You need not worry so much."
    VES @sad "I..."
    VES @angry "Let us leave this place!"
    VES @talk "The next game I will not allow to mess with my mind so much!"
    hide ves with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Temptations_over

label qst_TheTarbecks_Room_Temptations_markus:
    menu:    
        "Well, surely you and I can handle this?":
            pass
        "I have a bad feeling about this one.":
            MARKUS_FEM @happy "Goin soft on me huh?"
            MARKUS_FEM @happy "Thought you and I could handle this!"
            show mc at blurin, cleft_f
            MC @serious "Trust me, something about this seems...{i}off.{/i}"
            MARKUS_FEM @talk "{i}*Sigh*{/i}"
            MARKUS_FEM @talk "Well, if you say so."
            MARKUS_FEM @talk "Let's find a different game then."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    MC @smile "Remember that time we won that drinking competition in the {i}Dancing Goblin?{/i}"
    MARKUS_FEM @happy "Ha! You're right!"
    MARKUS_FEM @happy "A single glass of wine? We might even be able to down it in one!"
    WATCHER "Am I to take it then, you're both ready to play?"
    "Confidently, the two of us looked at each other and nodded."
    WATCHER "Very well then, come take a seat!"
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    hide mc
    hide markus_fem
    with easeoutright
    "Confidently, the two of us took our seats."
    "With a light clink of the glasses, the two of us took a large gulp."
    "The wine was smooth, its richness sweet and tingly on the lips."
    show mc at cright_f
    show markus_fem at cleft
    with dissolve
    MC "See? We're already halfway through our glasses!"
    MARKUS_FEM "Right! This challenge is-"
    "What started as a hot, tingly sensation on my lips soon became a burning lust coursing through my body."
    "Flushed red and breathing heavily, my eyes drifted down toward Markus—{i}I mean,{/i} Marcia's cleavage as my cock sprang painfully hard."
    "From her trembling breaths, I could tell Marcia was feeling its effects too."
    "Her cheeks flushed red as she nervously sipped at the wine."
    MARKUS_FEM "Gods... This is... Mhmm..."
    MARKUS_FEM "A strange feeling."
    MC "Y-Yes."
    "I nervously took another sip of my wine, feeling another brief rush of intense heat as the Watcher looked on, amused."
    "The two of us stared at each other nervously; {i}perhaps this was a mistake after all...{/i}"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MARKUS_FEM "{i}*Huff*{/i} You look... {i}*Huff*{/i} different today."
    MC "Well, I certainly prefer how you look like this."
    MARKUS_FEM "{i}*Giggles*{/i}"
    "Marcia twirled her hair as she giggled at my comment, which only made me more nervous."
    MC "({i}...Did I just flirt with Markus?{/i})"
    MC "({i}And is Markus... flirting back?{/i})"
    "With a shaking hand, Marcia—no, Markus—took another sip of the wine."
    "It was getting hard to think straight. I took a sip myself; we barely had a quarter left in our glasses."
    "How much longer was this agony going to last?"
    "I could feel her eyes staring intensely at me as she spoke."
    MARKUS_FEM "{i}*Huff*{/i} Are you— {i}*Huff*{/i} alright?"
    MC "Yes, I'm... {i}*Huff*{/i} f-fine..."
    MC "You?"
    MARKUS_FEM "M-Mm... Y-Yes..."
    MC "..."
    MARKUS_FEM "... T-Tell me— {i}*Huff*{/i}"
    MARKUS_FEM "{i}Do you...{/i}"
    MARKUS_FEM "{b}Prefer me like this?{/b}"
    MC "...W-What?"
    MARKUS_FEM "{i}*Heavy breathing*{/i}"
    MARKUS_FEM "I'm sorry... It's just so... so hard to think right now."
    "Her soft, delicate hand moved toward the strap of her dress."
    MC "...W-What are you-"
    $ PlaySexFx("audio/cfx/girl_breathing.ogg", 1)
    scene markus_fem_tarbeck_temptations_1 with dissolve
    $ Pause()
    "Gently, the dress slid down from her shoulder, exposing one of her breasts as she bit her lower lip."
    MC "...W-We can't."
    MARKUS_FEM "{i}I-I know.{/i}"
    MARKUS_FEM "{i}But don't you want to?{/i}"
    scene markus_fem_tarbeck_temptations_2 with dissolve
    $ Pause()
    "My eyes stared towards Marcia's voluptuous, milky white breasts as the whole world became a haze of lust."
    "As I went to take another sip of my wine, I looked down to see my glass was empty—and so was Marcia's."
    "How long had we been sitting here, unaware?"
    $ StopSexFx()
    $ LocFlush()
    show mc at cright_f
    show markus_fem at cleft
    with dissolve
    show cg_tarbeck_watcher at right_f with easeinright
    stop music fadeout 1.0
    "With a soft clap, the watcher hovered her way toward the table."
    WATCHER "Congratulations, both! You managed to stop yourselves and finish your drinks!"
    $ AutoMus(True)
    WATCHER "Here you both go!"
    "The Watcher placed a golden token onto the table."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    MC "...T-Thanks."
    show cg_tarbeck_watcher at left_f with ease
    MC "What— {i}*Huff*{/i} What do we do about-"
    WATCHER "Oh..."
    show cg_tarbeck_watcher at blurin, left
    "The watcher smiled playfully."
    WATCHER "Well, this game's over. You can do what you'd like now!"
    WATCHER "Do what you want, I have other guests to tend to!"
    show cg_tarbeck_watcher at blurin, left_f
    hide cg_tarbeck_watcher with easeoutleft
    MC "..."
    MARKUS_FEM "..."
    MC "We... We should go now."
    MC "Before we do something we might regret."
    MARKUS_FEM "Y-Yes."
    "Rising from my seat, my hands and body moved before I even had time to think things through."
    #Titjob idle here??
    "Pinned down onto the table, Marcia looked up at me breathlessly as I tugged down the dress to fully expose her breasts."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MC "I... I don't know what I'm do-"
    MARKUS_FEM "Shut up and fuck my tits already."
    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene markus_fem_tarbeck_temptations_3 with dissolve
    $ Pause()
    "With my cock shoved between her tits, I began to fuck her huge breasts."
    "She moaned softly as she squeezed them together, wrapping them around my cock."
    MARKUS_FEM "{i}F-Fuck... What are we doing?!{/i}"
    MC "I DON'T KNOW!"
    "Like a man possessed, I thrust between her soft, heavy tits as Marcia moaned beneath me."
    MARKUS_FEM "F-Fuck...!"
    MARKUS_FEM "Mmm, gods!"
    MARKUS_FEM "Y-Your cock is throbbing so hard!"
    "Markus' face remained flushed red as I continued to fuck the yielding mounds of her chest."
    $ PlaySexFx(audio.nijah_miss_2, 1)
    scene markus_fem_tarbeck_temptations_4 with dissolve
    $ Pause()
    "The watchers smirked, amused by the scene, as Marcia's legs squirmed pitifully beneath me."
    "Sapped of her strength, all she could do was helplessly watch as my cock slammed between her tits."
    MC "F-Fuckkkk!"
    MC "Your tits feel incredible!"
    MARKUS_FEM "C-Calm down! Mmhhfh!"
    MARKUS_FEM "It's still— {i}*Huff*{/i} me, r-remember?"
    MARKUS_FEM "W-We need to... to..."
    "Markus bit down on her lower lip, a hot, lewd moan slipping free as she squirmed beneath me."
    MARKUS_FEM "G-Gahhhhh! EVERYTHING IS SO SENSITIVE!"
    MARKUS_FEM "M-Mmmfghhh!"
    MC "{i}*Huff*{/i} What should— {i}*Huff*{/i} What should we-"
    MARKUS_FEM "Shut up! Shut up and fuck my tits, you bastard!"
    "Marcia's legs writhed beneath me as she moaned, her nipples hard like small stones as sweat poured from us both."
    "With trembling breaths, she squirmed as I felt my balls tighten, the thought of painting her tits and face with my load overwhelming."
    MC "I'm... {i}*Huff*{/i} I'm gonna-"
    "Unable to hold back any longer, Marcia gasped as I slammed forward, barely turning her face in time as I pressed the tip against her cheek."
    $ PlaySexFx(audio.nijah_miss_finish)
    scene markus_fem_tarbeck_temptations_finish with flash
    $ Pause()
    $ UnlockGalSceneAndGrantXp("markus", "tarbeck_temptations")
    $ ReduceInfectionFromSex("markus")
    "Grunting like an animal, I came, still sliding my cock back and forth as I painted her face and tits with my hot, thick load."
    MC "G-GRGHHHHHHHHHHHH!"
    MARKUS_FEM "G-Gods!"
    MC "{i}*Huff*... *Huff*...{/i}"
    MARKUS_FEM "..."
    scene black with dissolve
    "As the overwhelming lust finally began to subside, it dawned on us what we had just done..."
    $ AutoMus(True)
    $ LocFlush()
    show mc at cright_f
    show markus_fem at cleft
    with dissolve
    "With a light shove, Markus pushed me off and stood, wiping the cum from herself."
    MC @sad "U-Uhh, I didn't mean to-"
    MARKUS_FEM @sad "It's fine..."
    MARKUS_FEM @blush "Let's just, um... forget this ever happened, shall we?"
    show cg_tarbeck_watcher at center with easeinleft
    "One of the watchers approached, placing a golden token into my palm."
    show cg_tarbeck_watcher at nod
    $ Pause(0.1)
    $ PlayerAddItem("qst_tarbeck_golden_token")
    hide cg_tarbeck_watcher with easeoutright
    MC @talk "Markus, I-"
    MARKUS_FEM @talk "Let's just... keep moving."
    show markus_fem at blurin, cleft_f
    hide markus_fem with easeoutleft
    show mc at center_f with ease
    MC @sad "(... Fuck.)"
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Temptations_over

label qst_TheTarbecks_Room_Temptations_esme:
    menu:
        "Well, interested in trying a little wine with a little extra kick?":
            pass
        "I have a bad feeling about this one.":
            ESME @shock "Oh no! We might end up..."
            ESME @shock "Shock! Gasp! Horror!"
            ESME @shock "FUCKING!"
            ESME @smile "What exactly are you so worried about here?"
            show mc at blurin, cleft_f
            MC @serious "I've learned to trust my instincts, come on."
            hide mc with easeoutleft
            ESME @sad "Ehh... Fine, fine."
            show esme at blurin, left_f
            ESME @sad "You're the client after all."
            hide esme with easeoutleft
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    ESME @smile "Do you even need to ask?"
    ESME @smile "Come on, let's play."
    WATCHER "Right this way..."
    WATCHER "Come, take a seat at this table."
    $ PlaySexFx("audio/cfx/girl_breathing.ogg", 1, Volume = 1.1)
    scene esme_tarbeck_temptations_1 with dissolve
    $ Pause()
    "I joined Esme at the table, staring down at the dark red wine in front of us."
    "Confidently, the two of us took our seats."
    "With a light clink of the glasses, the two of us took a large gulp."
    "The wine was smooth, its richness sweet and tingly on the lips."
    MC "See? We're already halfway through our glasses!"
    ESME "In a hurry to finish, dear?"
    "Esme giggled as she playfully swirled her drink in her hand."
    MC "Well, I did come here for a reason..."
    ESME "Mmmmm..."
    scene esme_tarbeck_temptations_2 with dissolve
    $ Pause()
    ESME "But that doesn't mean we can't have a bit of fun in the meanwhile, does it?"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "As she spoke, I felt my pulse quicken, my breathing growing heavy as my cock stiffened."
    MC "Esme... I-"
    ESME "Got more kick than you first thought, doesn't it?"
    MC "I... It..."
    "My vision began to blur as my heart felt like it was beating out of my chest."
    "Had the room suddenly reached boiling point?"
    "Why was I feeling so... so..."
    ESME "I bet your cock already feels like it's going to explode."
    "I gulped; she was right, of course."
    "But how? How did Esme seem so calm and in control?"
    ESME "I bet you can't wait to play with..."
    scene esme_tarbeck_temptations_3 with dissolve
    $ Pause()
    "Pulling out her tits, Esme grinned, her pointed fangs visible as her sultry eyes watched me."
    ESME "{b}THESE!{/b}"
    "Esme laughed as she carefully watched my strained expression."
    "All I could think about was pouncing over the table and fucking this naughty little-"
    "No... No, no, no, no."
    "We can't afford to waste time; we {i}have{/i} to win this game!"
    "I pushed the thought aside and, with a shaking hand, took another sip of the wine."
    ESME "Mhmmm..."
    ESME "I'm surprised you aren't bending me over and trying to put it in my ass already."
    "Esme took another playful sip of the wine."
    MC "You are not— {i}*Huff*{/i} helping!"
    ESME "Where's the fun in that?"
    MC "Gods help me... {i}*Huff*{/i}"
    "My vision blurred further, my whole body tightening as Esme continued to tease."
    ESME "Oh, come on..."
    "Her hands reached for her nipples as she playfully tugged at them."
    ESME "Just a few more sips!"
    ESME "{i}You've barely got a quarter of your glass left!{/i}"
    "Esme watched, bemused, as I reached for the glass again, my thoughts a frenzied blur of lust as I struggled to control myself."
    "Somehow, by some miracle, I finished the last drop, dropping the empty glass onto the table as Esme clapped."
    $ StopSexFx()
    ESME "Well done!"
    $ UnlockGalSceneAndGrantXp("esme", "tarbeck_temptations")
    "With ease, she finished the rest of her drink, and the moment her glass touched the table, the watcher made their way over as we rose from our seats."
    $ LocFlush()
    show mc at cleft
    show esme at cright_f
    with dissolve
    show cg_tarbeck_watcher at right_f with easeinright
    WATCHER "Congratulations."
    WATCHER "Such willpower!"
    $ AutoMus(True)
    WATCHER "Why, you positively look like you're about to die sitting there."
    MC @bitelip "{i}*Huff*{/i} Fuck..."
    MC @angry "You."
    WATCHER "Hahaha!"
    WATCHER "Here, a token for your efforts."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    "As the watcher handed over the golden token, a playful Esme rose from her seat."
    hide cg_tarbeck_watcher with easeoutleft
    ESME "Well then, that's one more down, isn't it?"
    MC @bitelip "How are you— {i}*Huff*{/i}"
    MC @bitelip "So fine?"
    ESME "Hm?"
    ESME @smile "Oh, we were made to drink that stuff all the time when we were still learning the ropes in whorehouses."
    ESME @smile "You would be surprised how many men tried to give the new girls a taste so they could {i}really{/i} get their coin's worth."
    MC "{i}*Huff*{/i} I..."
    MC "Everything is a blur."
    "Esme pouted for a moment, her eyes locked firmly on the straining, aching cock pressing against my clothes."
    ESME @smile "Good thing there's still plenty more games to play then, isn't it?"
    ESME @smile "Come on, before you lose your head completely."
    hide esme with easeoutleft
    MC @talk "Urgh... coming now."
    show mc at blurin, cleft_f
    $ Pause(0.1)
    hide mc with easeoutleft
    $ Pause(0.1)
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Temptations_over

label qst_TheTarbecks_Room_Temptations_over:
    $ QstTheTarbecks().CalcGoldTokens()
    $ QstTheTarbecks().PlayedInRooms.add("temptations")
    $ LocEnter()