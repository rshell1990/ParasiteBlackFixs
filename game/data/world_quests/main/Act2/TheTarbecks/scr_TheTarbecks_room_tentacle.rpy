label qst_TheTarbecks_Room_Tentacle_main:
    if "tentacle" in QstTheTarbecks().PlayedInRooms:
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
    $ LocSet("hamun_tarbeck_room_tentacle")
    "Entering into the room, it led down to another winding stone staircase."
    "Just how deep did this manor go?"
    $ LocFlush(dissolve)
    "Down into the depths, we found ourselves in a stone, circular room."
    "In the centre, a pit descending into the darkness."
    MC @think "What the hell is this?"
    show mc at cleft
    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_7
    if QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "ves":
        show ves at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "esme":
        show esme at left with easeinleft
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left with easeinleft
    "As I stepped closer, I heard a rumbling sound, and the whole room shook slightly."
    MC @surprised "What the—!"
    "A few moments later, I heard it. *Slithering.*"
    scene cg_tarbeck_tentacle_room_monster
    show mc at cleft
    if QstTheTarbecks().PartyCompanion == "markus":
        show markus_fem at left
    elif QstTheTarbecks().PartyCompanion == "ves":
        show ves at left
    elif QstTheTarbecks().PartyCompanion == "esme":
        show esme at left
    elif QstTheTarbecks().PartyCompanion == "kiara":
        show kiara at left
    with dissolve
    "In seconds, protruding from the hole in the centre… tentacles."
    "They swayed and rose, standing to attention."
    MC @think "What is this thing?"
    MC @serious "Why does Lord Tarbeck have this?"
    "The tentacles swayed on the spot, but seemed particularly interested in my companion…"
    "In that moment, one of the watchers appeared."
    show cg_tarbeck_watcher at cright_f with easeinright
    WATCHER "This is a game for the ladies only, I am afraid."
    WATCHER "Simply step forward, and the creature will do the rest."
    MC @think "What is this thing?"
    WATCHER "A creature the master of the house found on his travels."
    WATCHER "It will not harm your companion."
    WATCHER "It wants their… essence."
    MC @talk "Essence, huh?"
    if QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Tentacle_kiara
    elif QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Tentacle_ves
    elif QstTheTarbecks().PartyCompanion == "markus":
        jump qst_TheTarbecks_Room_Tentacle_markus
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Tentacle_esme

label qst_TheTarbecks_Room_Tentacle_kiara:
    KIARA @smile "Looks like you aren't the only horny thing out there with tentacles."
    MC @think "Wait, how do you—"
    KIARA @smile "Come on love, you really think Lord Perv's-His-Name wouldn't find something like this?"
    KIARA @blush "...So, uhh… how about it?"
    KIARA @blush "Wanna see me ride this thing?"
    menu:
        "Yes.":
            pass

        "No.":
            KIARA @smile "Only your tentacles inside me, huh?"
            KIARA @smile "Relax, I'm just messin' with you."
            KIARA @talk "Come on now, let's get out of here before this thing gets too horny for its own good."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    KIARA @shock "...Wait, what?"
    KIARA @shock "You're serious?"
    KIARA @blush "Well… if that'll really make you happy."
    hide cg_tarbeck_watcher with easeoutleft
    "Kiara stared at the swaying tentacles."
    KIARA @think "*Deep breath.*"
    KIARA @talk "Alright… l-let's do this."
    show kiara at center with ease
    "Kiara stepped closer, and as she did so, the tentacles leaned closer toward her, gently rubbing against her."
    KIARA "E-Easy now!"
    "One of the tendrils carefully wrapped around her back, nudging her forward."
    "Another brushed up against her face, almost as if trying to tickle her."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    KIARA "...Heh, quite an affectionate one, aren't ya?"
    "One of the tentacles mischievously moved toward her chest, cupping one of her breasts before slipping into the gap of her dress to cop a feel."
    KIARA "Oi!"
    KIARA "Eager little fucker, aren't you?"
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    scene kiara_tarbeck_tentacle_1 with dissolve
    $ Pause()
    "Kiara giggled—and then the tentacles suddenly swept her off her feet, dangling her in the air."
    KIARA "Oooooh!"
    KIARA "E-Easy now!"
    KIARA "N-Not used to having my feet off the ground!"
    "The tendrils clambered over her body, gently pulling aside parts of her dress as they rubbed against her."
    KIARA "Mmffghh…"
    KIARA "That feels…"
    KIARA "A little ticklish but—"
    KIARA "N-Nice…"
    KIARA "Oooh!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene kiara_tarbeck_tentacle_2 with dissolve
    $ Pause()
    "Suddenly one of the tendrils pushed its way into her tight, teased little pussy, and she let out a sharp gasp."
    KIARA "O-Oh fuck!"
    "The tendril began to move quickly, pushing in and out of her as it buried itself deep."
    KIARA "Just putting it in without—mmfhh—"
    KIARA "Even askin', huh?"
    KIARA "You cocky little—"
    scene kiara_tarbeck_tentacle_3 with dissolve
    $ Pause()
    "The tendril began to move faster, plunging in and out of Kiara's tight womanhood as a soft moan escaped her lips."
    KIARA "Little - {i}*huff*{/i} shit!"
    KIARA "Mmmfghh..."
    KIARA "You're getting too-"
    KIARA "Ahh! Sure of yourself!"
    KIARA "You gotta start slower! treat a lady properly!"
    KIARA "How about s-something more tender! like a-"
    "Before she could finish, her expression changed as another tendril prodded at her rosebud."
    KIARA "W-Wait a minute!"
    KIARA "Oi! Don't just put it in there! That's my—"
    scene kiara_tarbeck_tentacle_4 with dissolve
    $ Pause()
    "As the second tendril forced its way into her ass, Kiara gasped, eyes wide as her mouth hung open."
    KIARA "B-BLOODY HELLS!"
    KIARA "Ah! You—mmfghh—greedy little—!"
    KIARA "Essence my ass! I can f-feel you—oooh—digging around back there!"
    "Maybe tired of her endless talking, a third tendril appeared..."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene kiara_tarbeck_tentacle_5 with dissolve
    $ Pause()
    "...Pushing past her lips and forcing its way into her mouth."
    KIARA "Mmmfghh!?"
    "Kiara squirmed as the three tendrils thrust in and out of her, more tendrils squeezing and playing with her breasts while the creature used her completely."
    KIARA "MMffhh! *Slurp!* *Slurp!*"
    "For the next twenty minutes I watched as the mindless creature continued to please her, until at last her eyes rolled back and she shuddered violently, moaning out as a powerful orgasm swept through her."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene kiara_tarbeck_tentacle_finish with flash
    $ UnlockGalSceneAndGrantXp("kiara", "tarbeck_tentacle")
    $ Pause()
    KIARA "MMMFGHHHH!"
    KIARA "*Huff* *Huff*"
    "...Satisfied, the tendrils lowered Kiara gently back to the ground before slipping back into the pit."
    $ LocFlush()
    show kiara at cright_f
    show mc at cleft
    with dissolve
    MC @surprised "Kiara! Are you alright?"
    show mc at center with ease
    $ AutoMus(True)
    KIARA @smile "Bloody hells…"
    KIARA @smile "If your cock ever gets tired, do you mind if we keep one of these things around?"
    KIARA @smile "That was… *phew!*"
    show cg_tarbeck_watcher at cleft with easeinleft
    "The watcher approached, handing over a golden token."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    KIARA @talk "Right, come on then love,"
    hide cg_tarbeck_watcher with easeoutright
    KIARA @talk "More of Lord Perv-a-lot's games to play and all that."
    MC @talk "Right…"
    "Kiara nudged me playfully."
    KIARA @smile "Relax, nothing compares to your cock."
    KIARA @smile "There's a reason half the bloody women you meet seem ready to spread their legs for you."
    hide kiara with easeoutleft
    MC "*Sigh*"
    show mc at blurin, center_f
    MC "(How many more of these games are left?)"
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Tentacle_over

label qst_TheTarbecks_Room_Tentacle_ves:
    VES @angry "... You cannot ask of me to lay with this creature."
    VES @blush "I will only lay with a mate worthy of me, as all of my people do."
    menu:
        "It's... not really a mate.":
            pass
        "I will not ask such a thing of you.":
            VES @smile "...Thank you."
            VES @smile "Come. Let us find another way."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()
    VES @think "What do you mean?"
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    MC @talk "The creature is just a toy of Lord Tarbeck's."
    MC @talk "And it wishes to mate to..."
    MC @talk "Sustain itself."
    VES @think "So?"
    MC @talk "So don't think of it as a mate."
    MC @talk "It's just a toy for your use."
    "Ves raised a brow at the comment."
    VES @think "...A toy?"
    "Ves paused, pondering for a moment."
    VES @talk "Yes... I suppose a toy would be acceptable."
    VES @talk "There is no shame in using a toy."
    show ves at center with ease
    "Ves stared at the swaying tentacles protruding from the pit, stepping forward proudly."
    VES @angry "Toy!"
    VES @angry "Your role is to please me!"
    VES @angry "Now please me, or I shall punish you for being a bad toy!"
    "Ves waited with her arms folded, and after a few moments, the tentacles slithered towards her."
    "They crawled up and around her body, and she winced slightly as one tendril pressed gently against her cheek—as if giving a small kiss."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    VES "Ha! Good toy!"
    VES "You know how to submit to—"
    "Ves' concentration broke as one of the tendrils slipped into her dress, fondling her breasts as her cheeks flushed a bright pink."
    VES "T-To your master..."
    "Another tendril looped around her back, tugging her forward, and for a moment she glanced toward me with anxious uncertainty."
    "I nodded, and Ves turned forward again, allowing the tentacles to embrace her."
    VES "I hope you know I am—"
    "Ves cried out as the tentacles suddenly raised her off her feet into the air."
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    scene ves_tarbeck_tentacle_1 with dissolve
    $ Pause()
    VES "W-What do you think you're doing?!"
    VES "Your mistress commands you—"
    "Ves gasped as she felt one tentacle rub against her clit while another slipped into her dress, squeezing and groping one of her tits."
    VES "A-Ahh!"
    VES "Are you trying to mess with me?!"
    VES "Grrr!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene ves_tarbeck_tentacle_2 with dissolve
    $ Pause()
    "The tentacles clearly had no interest in listening."
    "The first tendril pushed its way into her tight, green cunt."
    VES "A-AHHHHFGHH!"
    VES "B-Bad tentacle!"
    VES "Obey your—mmmfgh!—master!"
    scene ves_tarbeck_tentacle_3 with dissolve
    $ Pause()
    "The tentacle moved quicker, plowing the orc's wet, tight hole."
    VES "{i}*Huff*{/i} Ahhh!"
    VES "This is - Mmfghh!"
    VES "So strange!"
    VES "[player_name!t], I - Mmfghh!"
    scene ves_tarbeck_tentacle_4 with dissolve
    $ Pause()
    "Another tendril slithered down, prodding firmly at her tight rosebud."
    VES "W-WAIT!"
    VES "A STRANGE BEAST! THAT HOLE IS NOT FOR—"
    "The sentence was never finished."
    "Only her wheezing, wide-eyed expression followed as her asshole spread to accept the intruder."
    VES "EEEEEEEP!"
    VES "M-MY REAR! I-IT IS IN MY—"
    "Ves gasped as she felt the tendrils pound at both of her holes mercilessly."
    VES "My ashhh! Mmfghh! My poor ashh!"
    VES "G-Gods have mercy!"
    VES "Mmfghhh...!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene ves_tarbeck_tentacle_5 with dissolve
    $ Pause()
    "A third tendril pressed against her lips."
    "The creature was no longer playing."
    "It wanted to show Ves who really was in charge."
    "Her lips parted, and the tentacle pushed in, sliding down her throat as she could only whimper and moan helplessly."
    VES "Mmmfghhh!"
    VES "*Shlick!* *Slurp!*"
    "I watched as the tendrils pounded her holes. Ves, reduced to a helpless plaything for the fleshy mass, could only groan as her eyes rolled into the back of her skull."
    "Wet, squelching sounds filled the room."
    "Inch by inch, the tentacles stuffed themselves into the orc, thrashing her body until—"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene ves_tarbeck_tentacle_finish with flash
    $ UnlockGalSceneAndGrantXp("ves", "tarbeck_tentacle")
    $ Pause()
    VES "MMMMFGHHHH!!"
    "With a trembling, shaking orgasm, Ves cried out."
    "Satisfied, the tentacles gently lowered her back to the ground—a shivering, well-used mess—before retreating into the pit."
    $ LocFlush()
    show ves at cright_f
    show mc at cleft
    MC @surprised "Ves! Are you alright?"
    show mc at center with ease
    $ AutoMus(True)
    VES "A-Ahhhh..."
    VES "S-Shoo shoree..."
    VES "Mhyy ashhh... myhh..."
    "I helped Ves back to her feet."
    MC @sad "Ves?"
    VES @talk "I am... *huff* I am fine..."
    VES @think "My head feels like it is spinning..."
    show cg_tarbeck_watcher at cleft with easeinleft
    "As she tried to adjust her dress, a watcher approached, handing over a golden token."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    WATCHER "Her performance was... exquisite."
    MC @talk "Thanks."
    WATCHER "Please, enjoy the other games."
    WATCHER "We eagerly await your next performance."
    hide cg_tarbeck_watcher with easeoutright
    MC @sad "Are you going to be alright?"
    VES @talk "Yes... just..."
    VES @talk "Let us perhaps try to find an easier game next time."
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Tentacle_over

label qst_TheTarbecks_Room_Tentacle_markus:
    MARKUS_FEM @think "Why are you looking at me like that?"
    MARKUS_FEM @surp "... C-Come on!"
    MARKUS_FEM @angry "You can't seriously expect me to let that thing fuck me!"
    menu:
        "I mean, we *really* need to win.":
            pass

        "You're right, let's get out of here.":
            MARKUS_FEM @talk "Gods be praised."
            MARKUS_FEM @talk "Come on then, let's try a different game."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    MARKUS_FEM @angry "I'm aware of that! Just—"
    MARKUS_FEM @angry "Urghh! I swear if you speak of this to anyone, I'll throw your ass at every bandit, ghoul, and monster we meet next time!"
    MC @think "...So you'll do it?"
    MARKUS_FEM @angry "Not much bloody choice, is there?"
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    $ Pause(0.1)
    show markus_fem at center with ease
    "Marcia looked back toward the tentacles, her anger draining into nervous dread as she sheepishly stepped closer, turning pale."
    MARKUS_FEM "N-Nice tentacles."
    MARKUS_FEM "Good little abomination…"
    "The tendrils slowly slithered toward her, carefully wrapping around Marcia as they tugged her closer."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MARKUS_FEM "E-Easy now! Haha!"
    MARKUS_FEM "Uh… n-nice and gentle,"
    "One tentacle brushed across Marcia's cheek."
    MARKUS_FEM "Ha! That tickles!"
    MARKUS_FEM "See? You're not so—"
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    scene markus_fem_tarbeck_tentacle_1 with dissolve
    $ Pause()
    "Suddenly, she was yanked into the air, squealing as the creature hoisted her up and restrained her."
    MARKUS_FEM "AHHH!"
    MARKUS_FEM "W-What are you doing?! Put me down at once!"
    "The first tendril slithered forward, rubbing itself teasingly against Marcia's womanhood."
    MARKUS_FEM "M-Mmffh!"
    MARKUS_FEM "W-What do you think you're doing?!"
    MARKUS_FEM "Mmm… e-easy now! Uhh…!"
    MARKUS_FEM "L-Let's not get the wrong idea! I need things a little slower before I—"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene markus_fem_tarbeck_tentacle_2 with dissolve
    $ Pause()
    "Her words broke into a gasp as the tendril pushed inside, sliding into her tight pussy."
    MARKUS_FEM "OOOOHH!"
    "Slowly at first, the creature began thrusting in and out of her."
    MARKUS_FEM "{i}*Huff*{/i} [player_name!t]!"
    MARKUS_FEM "It—It's inside me!"
    MARKUS_FEM "F-Fuck! IT'S INSIDE ME!"
    MARKUS_FEM "What do I—"
    MARKUS_FEM "Mmfgh!"
    MC "Uh…"
    MC "Enjoy yourself and think of Novaras?"
    MARKUS_FEM "THINK OF—?!"
    scene markus_fem_tarbeck_tentacle_3 with dissolve
    $ Pause()
    "The tendril began moving faster."
    "Marcia's moans grew louder as her eyes rolled back."
    MARKUS_FEM "OOOOH!"
    MARKUS_FEM "It's—{i}*Huff!*{/i} so different as a woman!"
    MARKUS_FEM "It's—mmfghh!"
    MARKUS_FEM "{i}F-Filling!{/i}"
    "She trembled, not even noticing the second tendril slithering up her leg until it prodded against her asshole."
    "Her eyes snapped wide open."
    MARKUS_FEM "H-HOLD ON!"
    MARKUS_FEM "WAIT A MINUTE, YOU WEIRD FUCK! THAT'S MY ASS YOU—!"
    scene markus_fem_tarbeck_tentacle_4 with dissolve
    $ Pause()
    "The tendril forced its way inside, stretching her backdoor open as she gritted her teeth."
    MARKUS_FEM "{i}*Huff!*{/i} Oh gods…!"
    MARKUS_FEM "M-My ass!"
    MARKUS_FEM "What's it doing to my ass?!"
    "Both tendrils began fucking her in unison, her helpless moans filling the chamber."
    MARKUS_FEM "URGHHHH!"
    MARKUS_FEM "F-Fuck! FUCK! FUCK!"
    MARKUS_FEM "I can f-feel them wriggling around inside me!"
    MARKUS_FEM "{i}Oh gods!{/i}"
    "Her whole body quivered, reduced to the creature's plaything."
    MARKUS_FEM "{i}*Huff!*{/i} P-Please! Mmfghh! I don't—"
    MARKUS_FEM "{i}*Huff!*{/i} Ahhh!"
    MARKUS_FEM "I-I don't know how much more I can—!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene markus_fem_tarbeck_tentacle_5 with dissolve
    $ Pause()
    "Perhaps amused by her panic, a third tendril slid toward her panting mouth."
    "Before she could protest, it pushed past her lips and down her throat."
    MARKUS_FEM "MMMMFGHHHH!"
    MARKUS_FEM "Whatharehhh you dhoinggg! Mhffgh!"
    MARKUS_FEM "{i}*Slurp!* *Slurp!*{/i}"
    "The tentacles moved faster, pounding her in perfect rhythm."
    "Her stretched holes swallowed them greedily as she choked and moaned."
    "Only wet, obscene squelching and throat-deep gags filled the room as she was fucked senseless."
    "After some time, Marcia's eyes rolled completely back as her body trembled violently."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene markus_fem_tarbeck_tentacle_finish with dissolve
    $ Pause()
    $ UnlockGalSceneAndGrantXp("markus", "tarbeck_tentacle")
    MARKUS_FEM "C-CUMMINHGHHHHHHH!"
    "With a shuddering cry, she climaxed."
    "The tendrils buried themselves deep before slowly sliding free of her."
    "Satisfied, they lowered her limp body toward the ground."
    $ LocFlush()
    show markus_fem at cright_f
    show mc at center
    with dissolve
    "She would've collapsed if I hadn't rushed forward to catch her as the tentacles retreated into the pit."
    $ AutoMus(True)
    MC @surprised "Are you alright?"
    MARKUS_FEM @blush "I—"
    show mc at cleft with ease
    MARKUS_FEM @blush "Gods… it was so… {i}different.{/i}"
    show cg_tarbeck_watcher at right_f with easeinright
    "Clapping softly, one of the watchers approached, placing a golden token into Marcia's shaky hand."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    WATCHER "Quite the delight, isn't it?"
    MARKUS_FEM @surp "What even is that thing?!"
    WATCHER "Just a pet of our master's."
    WATCHER "One of many curiosities Lord Tarbeck has collected over the years."
    "They bowed politely."
    WATCHER "Please, enjoy the rest of the evening's games."
    WATCHER "We look forward to more of your performances…"
    show cg_tarbeck_watcher at blurin, right
    hide cg_tarbeck_watcher with easeoutright
    "As the figure slipped away, Marcia adjusted her dress and hair."
    MC @think "Are you sure you're fine?"
    MARKUS_FEM @talk "Aside from the fact I'll never look at your tentacles the same way again without blushing?"
    MARKUS_FEM @talk "{i}Peachy.{/i}"
    MARKUS_FEM @talk "Anyway—come on."
    MARKUS_FEM @talk "Let's see what else Lord Tarbeck has prepared."
    hide markus_fem with easeoutleft
    MC @talk "Right."
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Tentacle_over

label qst_TheTarbecks_Room_Tentacle_esme:
    ESME @smile "... Bet I can win."
    MC @think "It's not a fight?"
    ESME @happy "OH, it is for me!"
    ESME @talk "So then, how about it?"
    ESME @talk "Wanna find out how many tentacles I can take on?"
    menu:
        "Bet you can't take more than three.":
            pass

        "I still need you able to walk afterwards, so no.":
            ESME @sad "Tsch!"
            ESME @talk "... Well, I suppose you can make it up to me later anyway."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

    ESME @smile "Challenge accepted!"
    show cg_tarbeck_watcher at blurin, cright
    hide cg_tarbeck_watcher with easeoutright
    $ Pause(0.1)
    show esme at center with ease
    "Esme moved closer toward the pit, and as she did, the swaying tentacles took notice, slowly slithering their way toward her."
    "Confident as ever, Esme stepped forward as the tendrils began to gently coil around her."
    "One brushed carefully against her face."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    ESME "Come on now, no need to be shy."
    "Grinning, Esme licked her lips and ran her tongue along the tentacle in front of her."
    "It jerked back for a moment, startled, before eagerly leaning in again."
    ESME "We both know what you want."
    ESME "{i}And I want it too.{/i}"
    "Perhaps sensing her eagerness, the tentacles wasted no time..."
    $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
    scene esme_tarbeck_tentacle_1 with dissolve
    $ Pause()
    "...Restraining her and lifting her into the air as she laughed."
    "Hands tugged her clothes aside as their slick bodies fondled her."
    "She shivered when one rubbed teasingly against her womanhood."
    ESME "Ahhh..."
    ESME "Stop teasing a girl and just put it in already!"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene esme_tarbeck_tentacle_2 with dissolve
    $ Pause()
    "The tentacle obliged, pushing between her legs into her eager hole."
    "Esme sighed with pleasure, relaxing into its rhythm."
    ESME "Mmm… that's it."
    ESME "Oooh… you are trying to get deep, aren't you?"
    ESME "Oooooh—t-that's nice…"
    "The tendril moved steadily at first, then began to build confidence."
    ESME "Come on now, we ain't got all day!"
    ESME "Faster!"
    scene esme_tarbeck_tentacle_3 with dissolve
    $ Pause()
    "Whether it truly understood or not, it certainly understood her intent."
    "It sped up, thrusting harder as lewd sounds slipped from Esme's lips."
    ESME "Mmmfghh! That's it!"
    ESME "Pound it harder!"
    ESME "D-Don't stop!"
    "Then she suddenly barked—"
    ESME "Ahh! Come on!"
    ESME "I've got two more holes, don't I?"
    "A nervous tentacle crept toward her ass, prodding as if asking permission."
    "It was strangely amusing."
    "Like the poor beast had never dealt with someone so..."
    "...{i}Confident{/i} about what they wanted."
    ESME "That hole isn't going to fuck itself!"
    scene esme_tarbeck_tentacle_4 with dissolve 
    $ Pause()
    "The tentacle obeyed, stuffing her tight ass."
    "Her eyes rolled back as she groaned happily, drool slipping down her lip."
    ESME "Mmfghh!"
    ESME "That's it!"
    ESME "Fill me up good!"
    ESME "Don't stop! Go faster!"
    scene esme_tarbeck_tentacle_5 with dissolve
    $ Pause()
    "Two tentacles plunged in and out of Esme's eager holes as she moaned greedily, squirming in their grip."
    ESME "Shoooo ghoodhhh!"
    ESME "Mmmfghh!"
    ESME "M-More, you fuck!"
    ESME "Give me—"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene esme_tarbeck_tentacle_6 with dissolve
    $ Pause()
    "A third tentacle shoved into her mouth, sliding down her throat as her tongue thrashed against it."
    ESME "{i}*Slurp!*{/i} Mmfghh! {i}*Slurp!*{/i}"
    ESME "Dhpehherr! {i}*Slurp!*{/i}"
    "They gave it everything they had, pounding their eager katai prize."
    "Despite their best efforts, the creature almost seemed clumsy—nervous even, like it wasn't prepared for a woman like this and was desperately trying to keep up."
    "It pushed harder… harder… until—"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene esme_tarbeck_tentacle_finish with flash
    $ UnlockGalSceneAndGrantXp("esme", "tarbeck_tentacle")
    $ Pause()
    ESME "MMMFGHHH!"
    "They buried themselves deep as Esme shuddered violently, her whole body trembling as her eyes rolled back."
    "After a few moments, the tendrils slowly slid free, popping out one by one before lowering her to the ground."
    "Then, in a panic, they retreated into the pit."
    $ LocFlush()
    show mc at cleft
    show esme at cright_f
    with dissolve
    "Esme immediately lurched after them."
    ESME "ONE TIME?!"
    ESME "YOU ONLY MADE ME FINISH ONCE?!"
    ESME "GET BACK HERE, YOU CHEAP BASTARD!"
    MC @talk "...So, only three, huh?"
    ESME @angry "If it didn't run off before finishing the job, I could've handled more!"
    $ AutoMus(True)
    MC @think "How could you have—"
    "I shook my head, banishing the thought."
    MC @talk "Never mind. I don't want to know."
    show cg_tarbeck_watcher at left with easeinleft
    WATCHER "Well… I've never seen THAT before."
    "I turned to see one of the watchers slowly clapping as they approached."
    WATCHER "I think you're the first woman to ever make it run away."
    ESME @talk "Hmm."
    ESME @smile "I've handled more impressive things."
    "Her eyes flicked toward me with a smirk."
    WATCHER "Be that as it may…"
    show cg_tarbeck_watcher at center with ease
    "They handed her a small golden token with a polite bow."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token")
    WATCHER "Please, enjoy the rest of the games this evening."
    WATCHER "We look forward to seeing what you'll play next."
    hide cg_tarbeck_watcher with easeoutright
    ESME @talk "Phew..."
    show esme at center_f with ease
    ESME @talk "Well then, come on. Let's see what else is on offer."
    MC @think "Don't you need a minute to recover?"
    ESME @smile "Recover from what?"
    ESME @smile "{i}My warm-up?{/i}"
    MC @smile "Well, if you're good to go then…"
    ESME @talk "Come on! Let's see what other 'games' await us!"
    hide esme with easeoutleft
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Tentacle_over

label qst_TheTarbecks_Room_Tentacle_over:
    $ QstTheTarbecks().CalcGoldTokens()
    $ QstTheTarbecks().PlayedInRooms.add("tentacle")
    $ LocEnter()