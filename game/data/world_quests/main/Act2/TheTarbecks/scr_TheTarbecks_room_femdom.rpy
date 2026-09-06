label qst_TheTarbecks_Room_Femdom_main:
    if "femdom" in QstTheTarbecks().PlayedInRooms:
        if config.developer:
            "DEBUG: already been to this room. override the block and go again?"
            menu:
                "yes":
                    pass
                "no":
                    jump qst_TheTarbecks_AlreadyPlayedInThisRoom
        else:
            jump qst_TheTarbecks_AlreadyPlayedInThisRoom
    scene black with dissolve
    "Entering the room, the sharp crack of whips, flogs, and other devices echoed through the air."
    $ LocSet("hamun_tarbeck_room_femdom")
    scene cg_tarbeck_femdom_dungeon_party with dissolve
    "The sounds were quickly followed by the whelps of men as scantily clad women sauntered around, playfully tormenting their male counterparts in this lavish, makeshift dungeon."
    show mc at cleft with easeinleft

    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_2

    if QstTheTarbecks().PartyCompanion == "ves":
        show ves at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "esme":
        show esme at left with easeinleft
    
    show cg_tarbeck_watcher at cright_f with easeinright
    WATCHER "Welcome. Would you like to play {i}Lady of the house?{/i}"
    "Two women stood behind a blindfolded, bound man, pink claw marks running down his body."
    "One of them giggled as she dripped hot wax onto his cock, laughing as he winced and struggled."
    MC @surprised "Gods..."
    WATCHER "The rules are simple."
    WATCHER "In this room, the ladies rule the house."
    WATCHER "Be a good boy and let your lady take charge."
    WATCHER "The watchers will be watching, rewarding those who put on the most... {i}interesting show.{/i}"

    if QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Femdom_ves
    elif QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Femdom_kiara
    elif QstTheTarbecks().PartyCompanion == "markus":
        jump qst_TheTarbecks_Room_Femdom_markus
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Femdom_esme

label qst_TheTarbecks_Room_Femdom_ves:
    VES @smile "Ha! This one sounds fun!"
    VES @blush "We should play this one!"
    menu:
        "... What did you have in mind then?":
            pass
        "I prefer to be the one on top.":
            VES @sad "This saddens me..."
            VES @angry "This is a battlefield!"
            VES @sad "How else am I to prove I am a worthy orc?"
            show mc at blurin, cleft_f
            MC @think "You are more than a worthy orc Ves."
            hide cg_tarbeck_watcher with dissolve
            MC @smile "Think I would waste my time with you if I thought otherwise?"
            VES @sad "R-Right."
            show mc at blurin, cleft
            MC @talk "Now come on, let's find a different game."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    VES @smile "Good!"
    "Ves turned her head to one of the watchers."
    VES @angry "We wish to play!"
    WATCHER "We have just the outfit for you."
    WATCHER "Right this way..."
    hide ves with easeoutright
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    scene black with dissolve
    $ Pause(0.5)
    scene cg_tarbeck_femdom_dungeon_party 
    show mc at cleft
    with dissolve
    $ CharSetClothes("ves", "dom")
    show ves at cright_f with easeinright
    $ Pause()
    MC @surprised "Ves!"
    MC @surprised "You look-"
    VES @smile "Like I'm ready to make my favourite human my bitch for the evening."
    MC @surprised "... O-Oh!"
    VES @smile "..."
    MC @think "...What?"
    MC @think "Why are you looking at me like that?"
    show ves at center_f with ease
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    VES @smile "I have just the idea."
    MC @surprised "...H-Hold on a minute!"
    VES @smile "You're the one who chose to court an orc."
    VES @smile "Come now, my strong man..."
    VES @smile "You should have guessed something like this might happen."
    MC @surprised "{i}*Gulp*{/i}"
    scene black with dissolve
    "Ten minutes later..."
    $ PlaySexFx(audio.moans_breaths_loop, 1)
    scene ves_tarbeck_femdom_1 with dissolve
    $ Pause()
    VES "...There we are."
    VES "Maybe I should have done this from the start."
    "Ves ground her ass against my cock, grabbing a fistful of my hair."
    MC "Ah! Ves—eas-"
    "She pressed her lips forcefully against mine, slipping her tongue into my mouth."
    MC "Mhmm..."
    "She pulled back only long enough to speak between wild kisses."
    VES "{i}You are mine.{/i}"
    VES "My mate."
    VES "{i}My human.{/i}"
    MC "Ves... I'm not even sure if I'm still—"
    scene ves_tarbeck_femdom_2 with dissolve
    $ Pause()
    "Ves silenced me with another kiss, her ass grinding harder against my painfully stiff cock."
    "Her wet slit rubbed against me as she moaned softly."
    VES "{i}*Huff*{/i} I have never met..."
    VES "{i}*Huff*{/i} Someone as strong as you."
    VES "I pledge to you—Ves will conquer your body."
    VES "Then your heart."
    MC "Ves... {i}*Huff*{/i} Let me put it inside you."
    VES "No."
    MC "Urghh! This is torture!"
    VES "It is."
    VES "Ache for me."
    VES "Let no other female stir your passion."
    MC "Ves... {i}*Huff*{/i} I—"
    scene black with dissolve
    $ StopSexFx()
    play sound "audio/cfx/body_falling.ogg"
    "With a sharp push, I tumbled onto the floor."
    MC "Ahh! Ves!"
    MC "What are you—"
    MC "Mmmfghhh!!"
    $ PlaySexFx(audio.ves69_125, 1)
    scene ves_tarbeck_femdom_3 with dissolve
    $ Pause()
    "Ves ground her pussy over my face, rocking back and forth as she moaned."
    "As my tongue plunged into her sweet, soaking green cunt, she shuddered, wrapping her lips around my cock as she grinded her ass into my face."
    VES "{i}*Slurp!*{/i}"
    VES "Eathh ithh! {i}*Slurp!*{/i}"
    VES "Mmfghh! {i}*Shlick!*{/i}"
    VES "Eathhh myhhh orchh cunthh!"
    VES "{i}*Slurp! *Slurp!*{/i}"
    "Ves' tongue thrashed and beat and against my cock as my buried my tongue deeper into her pussy."
    "Greedily, I lapped up her juices as I listened out for her hot moans whilst choking on my cock."
    $ PlaySexFx(audio.ves69_150, 1)
    scene ves_tarbeck_femdom_4 with dissolve
    $ Pause()
    "Her mouth glided back and forth faster over my cock, coating it in her wet, warm saliva."
    "I sucked at her clit, my tongue pushing through the folds to taste every crevice of her..."
    VES "Ooooooh!"
    MC "Mmfghhh!"
    MC "Chan'th breathe!"
    VES "Mhmmhh??"
    VES "Whathh yhouhhh shayhh? {i}*Slurp!*{/i}"
    VES "Mmfghh!"
    MC "Airhh! Nedhhh airhh!"
    "Ves' body began to shake as her mouth's seal around my cock tightened."
    "Her whole body trembling atop of me as the pleasure swept over her like a wave."
    "And suddenly, I too lost all control."
    VES "Y-YHESHHHH!"
    $ PlaySexFx(audio.ves69_finish)
    scene ves_tarbeck_femdom_finish with flash
    $ ReduceInfectionFromSex("ves")
    $ UnlockGalSceneAndGrantXp("ves", "tarbeck_femdom")
    $ Pause()
    MC "VHESHH!"
    "My balls burned as I finished, spilling over Ves' hand, seed dripping down onto me."
    VES "{i}*Huff*{/i} Praise be to Vishta. {i}*Huff*{/i}"
    MC "Chan'thh breathe!"
    VES "Hm?"
    VES "Oh—OH!"
    scene black with dissolve
    $ AutoMus(True)
    "Ves quickly sprang up as I gasped for air."
    scene cg_tarbeck_femdom_dungeon_party
    show ves at cright_f
    show mc at cleft
    with dissolve
    VES @shock "I—I am sorry!"
    VES @shock "I forgot myself in the moment!"
    show cg_tarbeck_watcher at right_f with easeinright
    "A watcher approached, handing Ves a golden token."
    $ PlayerAddItem("qst_tarbeck_golden_token")
    WATCHER "A wonderful performance."
    WATCHER "Would you believe a participant died before doing what you just did?"
    WATCHER "But what is life without a little risk?"
    WATCHER "Enjoy the rest of your evening."
    hide cg_tarbeck_watcher with easeoutleft
    "The watcher glided away as quickly as they arrived."
    show ves at center_f with ease
    VES @sad "Are you okay?"
    VES @sad "I did not mean to hurt you."
    MC @talk "I'm fine, Ves."
    MC @smile "A little breathless, but fine."
    VES @talk "Good."
    VES @talk "Shall we continue with these games?"
    MC @talk "Come on. There are more tokens to be won."
    scene black with dissolve
    $ CharSetClothes("ves", "dress")
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Femdom_over


label qst_TheTarbecks_Room_Femdom_kiara:
    KIARA @smile "Oooh... Me in charge, hm?"
    KIARA @smile "Well, this could be fun!"
    "Kiara licked her lips as she looked towards me, a twinkle in her eye as she laughed."
    KIARA @smile "So..."
    KIARA @blush "Wanna find out how we northern girls normally deal with you soft southern boys?"
    menu:
        "I take it you have something in mind already?":
            pass

        "No thanks...":
            KIARA @angry "... Well that's bloody dissapointing, isn't it?"
            KIARA @sad "Fine, whatever."
            KIARA @sad "Job first and all that."
            KIARA @angry "Let's just find another game or something!"
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    KIARA @smile "Just a little something I wanna try..."
    show kiara at center with ease
    KIARA @smile "Don't suppose you've got something for a girl who wants to boss her man around to slip into?"
    WATCHER "Why of course... Come, let us find a uniform that fits you."
    hide kiara with easeoutright
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    scene black with dissolve
    $ Pause(0.5)
    $ CharSetClothes("kiara", "dom")
    scene cg_tarbeck_femdom_dungeon_party
    show mc at cleft
    with dissolve
    show kiara at cright_f with easeinright
    $ Pause()
    MC @surprised "... Oh!"
    MC @surprised "I wasn't quite expecting {i}that.{/i}"
    show kiara at center_f with ease
    KIARA @blush "Face it lover."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    KIARA @blush "Your ass is mine tonight."
    scene black with dissolve
    MC @surprised "... What have I talked myself into?"
    "{i}...Ten minutes later.{/i}"
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene kiara_tarbeck_femdom_loop_1 with dissolve
    $ Pause()
    "Kiara grinned as she trailed her finger slowly down my chest."
    KIARA "Oh my... I could get used to having you like this, huehue."
    MC "Cute."
    "Turning her back to me, Kiara pressed my cock up against her ass, wiggling her butt teasingly."
    KIARA "Tell me something, big boy."
    KIARA "I bet you've gotten real used to having this ass on call, haven't you?"
    MC "Ahh... What are you talking about?"
    KIARA "I think it's time, love, we started making things a little more equal around here, don't you agree?"
    "Kiara's soft ass continued to push and wiggle against me, forcing my cock between her cheeks."
    MC "I don't know what you—Ahh!"
    MC "Gods, girl, let me put it in already, would you?"
    KIARA "Ah ah ah!"
    KIARA "If you want it in, you're gonna have to learn to appreciate this maiden a little more, love."
    MC "I do—Mmfgh! Appreciate you!"
    $ PlaySexFx(audio.adara_hj_loop_x2, 1)
    scene kiara_tarbeck_femdom_loop_2 with dissolve
    $ Pause()
    KIARA "Then worship my ginger, freckled ass."
    MC "What?!"
    KIARA "I wanna hear you talk about how much you love this ass."
    KIARA "How you stroke that big, silly, fat cock of yours thinking about it."
    MC "Kiara, I—"
    KIARA "Your {i}mistress{/i} isn't hearing enough praise!"
    KIARA "Maybe I should just stop and leave you here, hmm?"
    MC "But... the mission!"
    "Kiara chuckled."
    KIARA "Fuck the mission. It's hotter watching you squirm a bit, love."
    MC "Ahh! Wait, wait!"
    KIARA "I'm listeninggg..."
    MC "Kiara—gahh! I love your ass, it's... so good!"
    KIARA "Mmmm, not good enough!"
    KIARA "Later!"
    MC "Wait! WAIT!"
    MC "... I fucking love your tight, freckled ass."
    KIARA "... Go on."
    MC "Every time you walk past, all I can think about is pinning you down and fucking you right there in front of everyone!"
    KIARA "Would you fuck me in front of that mousey-haired lass you got back home?"
    MC "Ahh! You mean Adara?"
    KIARA "Yes."
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene kiara_tarbeck_femdom_loop_3 with dissolve
    $ Pause()
    "Grabbing my cock, Kiara slipped it between her legs, pushing the head against her tight, wet womanhood."
    "I thrust forward uselessly as she chuckled, squeezing my cock between her thighs."
    KIARA "Tell me you'd fuck me in front of that mousey wench."
    MC "Ahh!"
    MC "Kiara, but—"
    "As she squeezed her thighs tighter, I groaned, my cock aching to fill her."
    KIARA "Say. It."
    "Despite her commanding tone, her breath trembled with excitement."
    "As I slid my cock back and forth against her cunt, she moaned softly."
    KIARA "If you want this tight northern pussy, you'll say it!"
    MC "Kiara... {i}*Huff*{/i}"
    $ PlaySexFx(audio.adara_hj_loop_x2, 1)
    scene kiara_tarbeck_femdom_loop_4 with dissolve
    $ Pause()
    KIARA "(Say it! Say it! Say it!)"
    MC "I'd fuck you in front of Adara!"
    MC "I'd make her watch as I dumped my balls into your tight hole!"
    KIARA "Oooooh f-fuck!"
    KIARA "You have no idea how much that does things for me!"
    KIARA "Shut up, love."
    KIARA "Tonight, you're just a massive cock for me to ride!"
    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene kiara_tarbeck_femdom_loop_5 with dissolve
    $ Pause()
    "Grabbing my member, Kiara moaned sweetly as she pushed my cock into her eager hole."
    "Her wet, tight pussy squeezed around me as she pushed her cute ass back."
    KIARA "Oh fuck! Fuck! Fuck!"
    KIARA "That's it! Mmfghh! Right there, big boy!"
    MC "Gods! Kiara!"
    MC "You're so—urfghh!"
    MC "Tight!"
    $ PlaySexFx(audio.kiara_tent_slow, 1)
    scene kiara_tarbeck_femdom_loop_6 with dissolve
    $ Pause()
    "I strained against the chains as Kiara rode me mercilessly."
    "My cock slid easily in and out of her hot, wet honeypot."
    KIARA "Mmfghh! And you're hard as fuck!"
    KIARA "{i}*Huff*{/i} Come on! I can feel how close you are already!"
    KIARA "Ahh! I fucking love it when your balls slap against my clit!"
    MC "Ahh! You keep squeezing—I'm getting close!"
    KIARA "Tell me when!"
    KIARA "I can feel you stretching me so good!"
    "My balls swelled and ached as I neared the edge."
    "Kiara must have felt it too, because she suddenly stopped."
    $ PlaySexFx(audio.adara_hj_loop_x3, 1)
    scene kiara_tarbeck_femdom_loop_7 with dissolve
    $ Pause()
    MC "What are you doing?!"
    "Turning with a mischievous grin, she stroked my cock."
    KIARA "Sorry, lovely."
    KIARA "But you won't be filling me up today!"
    MC "But I-"
    scene kiara_tarbeck_femdom_loop_8 with dissolve
    $ Pause()
    KIARA "Was close to cumming inside my-"
    KIARA "{i}Tight.{/i}"
    KIARA "{i}Wet.{/i}"
    KIARA "{i}Pussy?{/i}"
    MC "Ahhh! YES!"
    KIARA "Awww, too bad love!"
    KIARA "Because you're gonna spill your sily, thick load alllllll over the floor!"
    MC "K-Kiara! Wait! I—"
    $ PlaySexFx(audio.nijah_miss_finish)
    scene kiara_tarbeck_femdom_finish with flash
    $ ReduceInfectionFromSex("kiara")
    $ UnlockGalSceneAndGrantXp("kiara", "tarbeck_femdom")
    $ Pause()
    MC "HRGHHHH!"
    "Kiara laughed as my seed spilled uselessly onto the floor."
    KIARA "Oooh! So {i}that's{/i} how much you usually pump into me!"
    MC "Why would you—"
    KIARA "Frustrating, isn't it?"
    KIARA "Kinda like watching you saunter off to lay with some random whore."
    MC "..."
    scene black with dissolve
    $ AutoMus(True)
    "Releasing me from the chains, I rubbed at my sore wrists as Kiara smirked."
    scene cg_tarbeck_femdom_dungeon_party
    show mc at cleft
    show kiara at cright_f
    with dissolve
    KIARA @smile "Well, that was fun, wasn't it?"
    MC @think "What was that back there?"
    KIARA @think "What are you talking about?"
    MC @think "Well all that about Adara and appreciating you more..."
    KIARA @smile "Why ever would you think that, love?"
    show cg_tarbeck_watcher at left with easeinleft
    "Before I could answer, one of the watchers approached, handing us a golden token."
    $ PlayerAddItem("qst_tarbeck_golden_token")
    show cg_tarbeck_watcher at nod
    WATCHER "For your performance."
    WATCHER "What a wonderful show that was. {i}*Chuckles*{/i}"
    hide cg_tarbeck_watcher with easeoutright
    KIARA @talk "Well, that's that then."
    show kiara at center_f with ease
    KIARA @talk "Come on, love. Let's keep moving."
    KIARA "Got more tokens to win, right?"
    MC @talk "... Right."
    scene black with dissolve
    $ CharSetClothes("kiara", "dress")
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Femdom_over


label qst_TheTarbecks_Room_Femdom_esme:
    ESME @talk "Sure, I'm game."
    ESME @smile "How about you?"
    "Esme licked her lips as her tail swished bac kand forth excitedly."
    ESME @happy "Wanna see what I can {i}reallyyyyy{/i} do?"
    menu:
        "Well, I'm always open to new things...":
            pass
        "No thanks.":
            ESME @smile "Always want to be on top, huh?"
            ESME @smile "Fine, fine."
            ESME @smile "Whatever you want mr manly man."
            ESME @talk "Come on then, let's find a different game to play."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    WATCHER "Perfect, madam."
    WATCHER "We have just the outfit for you to change into..."
    hide esme with easeoutright
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    scene black with dissolve
    $ Pause(0.5)
    $ CharSetClothes("esme", "dom")
    scene cg_tarbeck_femdom_dungeon_party
    show mc at cleft
    with dissolve
    show esme at cright_f with easeinright
    $ Pause()
    ESME @smile "Well, what do you think?"
    MC @smile "Like you're ready to tell me how to think and how to feel."
    ESME @smile "Well, aren't you a good boy?"
    show esme at center_f with ease
    "Esme stepped closer, her heels clicking with each slow step towards me."
    MC @talk "So... what did you have in mind?"
    "Esme looked around thoughtfully."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    ESME @talk "Hmmm..."
    ESME @smile "I have just the thing."
    scene black with dissolve
    MC "... Really now?"
    ESME "What?"
    ESME "Seems quite fair to me."
    scene esme_tarbeck_femdom_1 with dissolve
    $ Pause()
    ESME "With those tentacles of yours, how many ladies have you tied up?"
    ESME "Seems only fair that {i}this{/i} lady gets to tie you up for a change."
    MC "Fair enough."
    MC "Well, you've got me where you want me."
    MC "Now what do you want to—"
    "I feel the sharp sting of a crop snapping across my ass."
    MC "Ow!"
    MC "Fuck!"
    ESME "Haha!"
    ESME "Oh my, it practically bounces right off your ass!"
    "Esme brings the crop down on the other cheek."
    MC "Tsch!"
    ESME "Gods, it just makes me want to take a bite out of you."
    MC "Don't even think—"
    "{i}*WHACK!*{/i}"
    MC "Gah!"
    ESME "Tsk, tsk, tsk."
    ESME "You're far too used to being in charge."
    ESME "This will be good for you."
    ESME "{i}Whore.{/i}"
    MC "Must you hit so hard?"
    "{i}*WHACK!*{/i}"
    ESME "Yes."
    "{i}*WHACK!* *WHACK!*{/i}"
    MC "Tschh..."
    MC "{i}*Huff*{/i} Esme..."
    "Despite my protests and stinging ass, my cock ached painfully hard."
    ESME "Ahh! There you are!"
    "Esme grinned."
    ESME "I'll tell you what."
    ESME "Since I'm in a good mood, I'll let you decide."
    ESME "I can either drain those balls..."
    ESME "{i}If you beg your mistress.{/i}"
    "{i}*WHACK!*{/i}"
    ESME "...Or—"
    ESME "I can keep beating this ass."
    ESME "Which is it going to be, slut?"
    MC "Go fuck your—"
    "{i}*WHACK!* *WHACK!*{/i}"
    $ PlaySexFx(audio.girl_breathing, 1)
    scene esme_tarbeck_femdom_2 with dissolve
    $ Pause()
    "Esme moved to kneel in front of my cock, smirking at the dangling, large appendage in front of her."
    MC "Gah! Enough!"
    MC "You know I can break out of these ropes anytime I want, right?"
    ESME "Mmmm, but then you won't get your little golden tokennn~"
    MC "Tschhh!"
    ESME "Oh hush."
    ESME "Don't be such a little bitch."
    ESME "Now what's it going to be?"
    ESME "Do you want your ass beaten, or me to drain these fat balls?"
    MC "Drain my balls obviously!"
    ESME "I didn't hear a 'please mistress, drain my silly balls.'"
    MC "You can't be serious!"
    ESME "I could just walk away and leave you like this you know!"
    MC "You wouldn't dare..."
    ESME "Hmm, too bad!"
    ESME "I better get going!"
    MC "Wait, wait, wait!"
    MC "..."
    ESME "... I'm waiting."
    MC "{i}Please drain my balls.{/i}"
    ESME "Please what?"
    MC "Grrr..."
    MC "{i}'Mistress,'{/i} happy now?"
    ESME "And what do you want me to drain?"
    MC "{i}'My silly, fat balls'{/i}"
    MC "Now how long are you going to keep this up?"
    MC "I swear when I get out of this I'll—"
    $ PlaySexFx(audio.kiara_bj_loop, 1)
    scene esme_tarbeck_femdom_3 with dissolve
    $ Pause()
    "I never finish the sentence."
    "I'm left breathless as Esme suddenly wraps her lips around my cock."
    ESME "{i}*Slurp!* *Slurp!*{/i}"
    "She pulls off with a loud *PLOP*, stroking me with a grin."
    $ PlaySexFx(audio.girl_breathing, 1)
    scene esme_tarbeck_femdom_2 with dissolve
    $ Pause()
    ESME "I'm sorry. Were you still being a little bitch?"
    MC "{i}*Huff*{/i} Esme... fuck..."
    ESME "Yes, little bitch?"
    MC "Stop calling me that!"
    ESME "Calling you what, little bitch?"
    MC "I mean—"
    $ PlaySexFx(audio.ves69_150, 1)
    scene esme_tarbeck_femdom_4 with dissolve
    $ Pause()
    "She leans forward again and engulfs my cock."
    MC "…!"
    ESME "{i}*Slurp!* *Shlick!*{/i}"
    ESME "Mmmfghh..."
    ESME "I lhuvv your bhig chockhh!"
    MC "Ahh... Esme!"
    MC "Please, that's it!"
    MC "Just a little more!"
    MC "Suck it just a little—"
    "{i}*PLOP!*{/i}"
    $ PlaySexFx(audio.girl_breathing, 1)
    scene esme_tarbeck_femdom_2 with dissolve
    $ Pause()
    MC "FOR FUCK'S SAKE, WOMAN!"
    ESME "Hahaha! Ooopsy!"
    ESME "Mmm, what's the matter?"
    ESME "Were you close, bitch?"
    MC "Stop—"
    ESME "Bitch, bitch, bitch, bitch, bitch."
    MC "...You're so dead."
    ESME "Hehe! I'll tell you what."
    ESME "I'll finish you..."
    ESME "{i}*If...*{/i}"
    ESME "{i}You promise to visit me at The Kitten's Paw.{/i}"
    MC "What?"
    MC "That's it?"
    ESME "Uh-huh."
    ESME "Because I don't know what I like more."
    ESME "Draining your balls..."
    ESME "Or draining your coin pouch!"
    MC "Ahh!"
    MC "Yes... I'll visit you again soon."
    ESME "{i}*Deep breath*{/i}"
    ESME "Not good enough."
    MC "What?!"
    MC "I just did what you asked!"
    ESME "I'm not {i}convinced{/i} you'll visit me."
    ESME "Convince me."
    ESME "{i}Praise me.{/i}"
    MC "Urghh...!"
    MC "My balls feel ready to—"
    ESME "Praaaiiise~"
    MC "Fuck! Fine!"
    MC "Of course I'll see you again!"
    MC "You're probably the best piece of ass in this city!"
    MC "And you're..."
    MC "{i}Surprisingly more fun and interesting than I expected.{/i}"
    "For the briefest second, Esme pauses."
    ESME "...That's the nicest thing a man whose cock I've sucked has ever said."
    MC "Yeah, well how about—"
    $ PlaySexFx(audio.ves69_150, 1)
    scene esme_tarbeck_femdom_4 with dissolve
    $ Pause()
    "Esme wraps her lips around my cock once more and sucks."
    "This time she goes deeper, tongue thrashing as unbearable pleasure floods me."
    MC "H-HRGHHHH!"
    $ PlaySexFx(audio.ves69_finish)
    scene esme_tarbeck_femdom_finish with flash
    $ ReduceInfectionFromSex("esme")
    $ UnlockGalSceneAndGrantXp("esme", "tarbeck_femdom")
    $ Pause()
    "Grunting like a beast, I finished in Esme's mouth."
    "She purred and swallowed eagerly, savoring every drop."
    "Finally satisfied, she slowly pulled her lips away until—"
    scene esme_tarbeck_femdom_finish_2 with dissolve
    $ Pause()
    "{i}*PLOP!*{/i}"
    ESME "Ahh..."
    ESME "That'll do, cock."
    ESME "That'll do."
    MC "...Are you going to untie me, or do I need to break out myself?"
    ESME "Uhuh, just hold your horses..."
    scene black with dissolve
    "...A few moments later, after untying me."
    $ AutoMus(True)
    scene cg_tarbeck_femdom_dungeon_party
    show mc at cleft
    show esme at cright_f
    with dissolve
    ESME @smile "See? Was that so bad?"
    MC @think "...You know I'm going to get revenge on your ass for that, right?"
    ESME @smile "Of course I do."
    show cg_tarbeck_watcher at right_f with easeinright
    "Just then, a watcher approached, handing a golden token to Esme."
    WATCHER "For the performance..."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")    
    ESME @smile "Thanks."
    WATCHER "You know, if you're interested, there are many clients who would pay handsomely for the novelty of a katai mistress."
    ESME @talk "No thanks. I only do domination with men I like."
    WATCHER "I see. Enjoy the rest of your evening."
    hide cg_tarbeck_watcher with easeoutleft
    MC @think "Only with men you like, huh?"
    ESME @talk "Don't let it go to your head..."
    ESME @talk "Otherwise I'll charge you extra next time."
    ESME @smile "Anyway—come on. We've got more of these weird token things to win, right?"
    MC @talk "Right."
    scene black with dissolve
    $ CharSetClothes("esme", "dress")
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Femdom_over

label qst_TheTarbecks_Room_Femdom_markus:
    MARKUS_FEM @talk "..."
    show mc at blurin, cleft_f
    MC @talk "... So—"
    MARKUS_FEM @angry "No."
    MC @surprised "What? You don't even know what I was going to ask!"
    MARKUS_FEM @angry "I don't know how to do any of this stuff!"
    MARKUS_FEM @talk "Throwing a girl around is one thing. This is…"
    MARKUS_FEM @talk "{i}different.{/i}"
    MARKUS_FEM @angry "And especially weird with you!"
    menu:
        "We came here for a reason.":
            pass

        "You're right, this is too weird.":
            MARKUS_FEM @talk "Let's find a different game and get out of here."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    MC @serious "We need the tokens, or else your brother and-"
    MARKUS_FEM @angry "I know, I KNOW!"
    MARKUS_FEM @talk "{i}*Sigh*{/i} Well… any bright ideas?"
    MARKUS_FEM @think "Even if I did agree to this thing, I don't think a couple whips or whatever is going to be enough to win a token."
    MC @think "Well, I'm not exactly used to this either."
    show mc at blurin, cleft
    "Marcia's eyes wandered around the room for a moment. Then, suddenly, they widened."
    MARKUS_FEM @surp "Perhaps… there *is* something we could try."
    MC @think "...?"
    scene black with dissolve
    $ CharSetClothes("markus", "dom")
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Ten minutes later…"
    $ PlaySexFx(audio.girl_breathing, 1)
    scene markus_fem_tarbeck_femdom_1 with dissolve 
    $ Pause()
    "Marcia grinned smugly as she tugged the collar, leading me around."
    MARKUS_FEM "No slowing down now!"
    MC "Ah! Easy! EASY!"
    MC "Gods! You're going to rip it off if you keep that up!"
    MARKUS_FEM "You're the one who keeps reminding me we need these tokens!"
    MARKUS_FEM "I'm just making it believable like you keep asking."
    MC "I didn't think you'd—"
    scene markus_fem_tarbeck_femdom_2 with dissolve 
    $ Pause()
    "Marcia tugged the collar again."
    MC "OW!"
    MARKUS_FEM "Didn't think what?"
    MARKUS_FEM "That I wouldn't take the chance to get a little revenge?"
    MARKUS_FEM "After you paraded me around like your slutty toy earlier?"
    MC "That's not—"
    MC "Gah! Would you *stop* tugging so hard?!"
    MARKUS_FEM "Awww, poor thing."
    MARKUS_FEM "{i}Just remember how important these tokens are.{/i}"
    MARKUS_FEM "That should keep you motivated, I'm sure!"
    MC "Urghhh…"
    MARKUS_FEM "Come on then, we still have *plentyyyy* more guests to impress!"
    MC "{i}Great.{/i}"
    $ UnlockGalSceneAndGrantXp("markus", "tarbeck_femdom")
    scene black with dissolve
    $ StopSexFx()
    "Over the next half hour Marcia happily paraded me around, chatting casually with the other women while they tormented their own partners."
    scene cg_tarbeck_femdom_dungeon_party
    show mc at cleft
    show markus_fem at cright_f
    with dissolve
    "Eventually, one of the watchers approached."
    show cg_tarbeck_watcher at right_f with easeinright
    WATCHER "For your efforts."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    "The watcher carefully placed a small golden token into Marcia's hand before drifting away."
    show cg_tarbeck_watcher at blurin, right
    hide cg_tarbeck_watcher with easeoutright
    MARKUS_FEM @happy "Well, looks like the fun is over."
    MC @angry "...I'm so going to get you back for this."
    "Marcia laughed, sticking out her tongue playfully before heading off to change."
    show markus_fem at blurin, cright
    hide markus_fem with easeoutright
    MC "{i}*Sigh*{/i}"
    show mc at center with ease
    MC "(Just how many more of these games are there?)"
    scene black with dissolve
    $ CharSetClothes("markus", "dress")
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Femdom_over

label qst_TheTarbecks_Room_Femdom_over:
    $ QstTheTarbecks().CalcGoldTokens()
    $ QstTheTarbecks().PlayedInRooms.add("femdom")
    $ LocEnter()
