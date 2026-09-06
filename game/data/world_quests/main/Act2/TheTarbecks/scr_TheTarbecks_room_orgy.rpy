label qst_TheTarbecks_Room_Orgy_main:
    if "orgy" in QstTheTarbecks().PlayedInRooms:
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
    $ LocSet("hamun_tarbeck_room_orgy")
    $ LocFlush(dissolve)
    "Entering the red room, a massive bed dominated the chamber, overflowing with bodies tangled together in a writhing, breathless mass of pleasure."
    "The watchers lingered silently at the edges, handing out golden tokens to exhausted, sweaty couples who finally separated themselves from the orgy."

    show mc at cleft with easeinleft

    call qst_TheTarbecks_DEBUG_CompanionChoice from _call_qst_TheTarbecks_DEBUG_CompanionChoice_5

    if QstTheTarbecks().PartyCompanion == "markus":
        jump qst_TheTarbecks_Room_Orgy_markus
    elif QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Orgy_ves_start
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Orgy_esme_start
    elif QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Orgy_kiara_start

label qst_TheTarbecks_Room_Orgy_markus:
    show markus_fem at left with easeinleft
    MARKUS_FEM @surp "...!"
    MC @think "Well, uh… how about—"
    show mc at blurin, cleft_f
    MARKUS_FEM @angry "No way. Absolutely not!"
    MC @talk "But—"
    MARKUS_FEM @talk "There are many things I'm willing to do for you."
    MARKUS_FEM @angry "Letting myself get stuffed full of random cocks is NOT one of them."
    show markus_fem at blurin, left_f
    hide markus_fem with easeoutleft
    MC "(Well... that's that then, I guess...)"
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    $ LocEnter()

label qst_TheTarbecks_Room_Orgy_esme_start:
    show esme at left with easeinleft
    ESME @smile "Sooo, what's behind this—"
    ESME @sad "*Sigh* …just a plain old orgy, huh?"
    ESME @angry "I was hoping for something a little more… interesting."
    ESME @smile "Anyway, what do you think then?"
    ESME @smile "Want to fuck a bunch of strangers?"
    menu:
        "Why not?":
            ESME @smile "That's the spirit!"
            jump qst_TheTarbecks_Room_Orgy_enter
        "I'd rather find a more interesting game to play.":
            ESME @sad "Hmmm… For someone who brought a whore to a perverted lord's sex party, you're a little more *reserved* than I expected."
            ESME @talk "Oh well. Let's see what else there is."
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

label qst_TheTarbecks_Room_Orgy_kiara_start:
    show kiara at left with easeinleft
    KIARA @talk "Sooo, what does that perv have in—"
    KIARA @talk "…and it's just a straight-up orgy, isn't it?"
    MC @surprised "Looks that way!"
    MC @think "What do you think?"
    KIARA @think "Love, I mean…"
    KIARA @sad "Maybe there's another game instead?"
    KIARA @think "Not that I'm a prude or anything!"
    KIARA @sad "But… I'd kinda like you to still look at me the same afterward, yeah?"
    KIARA @sad "Would you really be alright seeing me with a load of other men?"
    menu:
        "We need more tokens, Kiara… The mission has to come first." (Req_Charm = 15):
            KIARA @sad "Bloody hells…"
            KIARA @talk "Alright then. For the mission."
            jump qst_TheTarbecks_Room_Orgy_enter
        "You're right… your ass is mine and mine alone.":
            show mc at blurin, cleft_f
            KIARA @smile "My ass, huh?"
            KIARA @smile "I *love* it when you talk like that~"
            scene black with dissolve
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

label qst_TheTarbecks_Room_Orgy_ves_start:
    show ves at left with easeinleft
    VES @talk "So, what twisted challenge lies in—"
    show ves at shake
    VES @shock "...!"
    MC @think "Now, don't panic too much—"
    VES @blush "Oh no. No no no no!"
    VES @shock "This is too much!"
    VES @blush "I've never even been with ONE mate… nevermind twenty!"
    VES @sad "I cannot do this!"
    menu:
        "We need the tokens, Ves… (Persuade Ves to do a bukkake)" (Req_Charm = 16):
            VES @shock "Y-You want what?!"
            MC @think "Listen — no man is going to touch you."
            MC @talk "Not unless you want them to."
            VES @angry "Men are pigs. I should cut them—"
            MC @talk "Ves…"
            VES @angry "Grrrr!"
            VES @think "...Do you swear? On your life?"
            MC @talk "On my life."
            VES @sad "…Very well."
            VES @angry "By your gods and mine… you owe me for this."
            jump qst_TheTarbecks_Room_Orgy_enter
        "Let's find a different game… One you're more comfortable with.":
            show mc at blurin, cleft_f
            scene black with dissolve
            "Ves nodded quickly, eager to leave as she practically glued herself to my back."
            $ LocSet("hamun_tarbeck_playhallway")
            $ LocEnter()

label qst_TheTarbecks_Room_Orgy_enter:
    scene black with dissolve
    $ Pause(0.1)
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/moans_muffled_suckey.ogg", 1)
    scene mc_tarbeck_orgy_1 with dissolve
    $ Pause()
    "In the wall of writhing bodies, a group beckoned me closer."
    "Before I could even greet them, a dark-skinned woman moaned around her partner's cock, pushing her plump ass back against me."
    "My cock sprang to life immediately, sliding into her wet, eager hole as she groaned happily, slamming her hips back to meet me."
    scene mc_tarbeck_orgy_1 with dissolve
    $ Pause()
    "Warm breasts pressed into my back from behind, soft lips trailing kisses up my neck before that body lowered between my legs…"
    "Time melted away. Minutes? An hour? More? Only heat… bodies… moans…"
    "My balls ached. My cock throbbed. Every part of me gripped, stroked, squeezed… worshipped… consumed."
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    scene mc_tarbeck_orgy_finish with flash
    $ ReduceInfectionFromSex()
    $ Pause()
    "At last, gripping the ass wrapped tight around me, I thrust deep and held, growling like an animal as I spilled my load inside her."
    "...and then I moved on to the next."
    if QstTheTarbecks().PartyCompanion == "ves":
        jump qst_TheTarbecks_Room_Orgy_ves_cont
    elif QstTheTarbecks().PartyCompanion == "kiara":
        jump qst_TheTarbecks_Room_Orgy_kiara_cont
    elif QstTheTarbecks().PartyCompanion == "esme":
        jump qst_TheTarbecks_Room_Orgy_esme_cont

label qst_TheTarbecks_Room_Orgy_ves_cont:
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg", 1)
    scene ves_tarbeck_orgy_1 with dissolve
    $ Pause()
    "...A short while later, a small group of men had gathered in a circle around Ves, their eyes wide with fascination."
    PARTY_GUEST "Look at this! I heard a greenskin came tonight, but I didn't believe it!"
    VES "Grrr…"
    PARTY_GUEST_PERVY "Gods… I heard orcs were hideous… but she's beautiful."
    PARTY_GUEST_PERVY "If they're all like this, maybe I need to visit Skarshire."
    PARTY_GUEST_PERVY "Careful boys, don't scare her off."
    "Ves' ears twitched slightly."
    VES "Y-You… really think I'm beautiful?"
    "The men exchanged a knowing grin."
    PARTY_GUEST "Of course."
    PARTY_GUEST_PERVY "We've never seen one of your kind before."
    PARTY_GUEST_PERVY "Are all orc women like you?"
    "Ves' cheeks burned red."
    VES "I… no one has ever called orcs beautiful before."
    VES "...A-Aren't you supposed to… stroke yourselves to me?"
    "The men chuckled."
    PARTY_GUEST "Of course."
    PARTY_GUEST "But maybe you could give us some… encouragement?"
    VES "E-Encouragement?"
    PARTY_GUEST "Just a few words to… spice things up."    
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
    scene ves_tarbeck_orgy_2 with dissolve
    $ Pause()
    "Ves gulped… then froze as the men stroked their cocks faster while staring at her."
    VES "...!"
    PARTY_GUEST_PERVY "So… how big do you think they are?"
    VES "T-They seem… large…"
    VES "I only have one other human to compare them to and he's…"
    "She paused, biting her lip."
    VES "…very large."
    PARTY_GUEST "And do you *like* big human cocks?"
    VES "I…"
    VES "An orc wouldn't degrade herself preferring—"
    PARTY_GUEST_PERVY "Who said anything about preferring?"
    PARTY_GUEST_PERVY "Just answer honestly."
    "Ves panted, flustered, eyes darting hungrily between them."
    VES "M-Maybe…"
    PARTY_GUEST "Touch yourself."
    VES "WHAT?!"
    PARTY_GUEST "We can't touch you."
    PARTY_GUEST_PERVY "But that doesn't mean you can't touch yourself."
    "Ves swallowed hard."
    VES "…Would that help?"
    PARTY_GUEST_PERVY "It'll… speed things up."
    PARTY_GUEST_PERVY "And it's not breaking the rules."
    "Ves hesitated… then nodded."
    "With trembling hands, Ves groped one breast, her other hand slipping between her legs as she rubbed her wet slit."
    VES "*Huff* F-Fuck…"
    VES "This is…"
    VES "Mmmfgh…"
    PARTY_GUEST "So… do you like big human cocks?"
    VES "*Huff* I like {i}his{/i} cock."
    PARTY_GUEST "Describe it."
    VES "*Huff* Thick…"
    VES "H-His B-Big… almost too big…"
    VES "It smells… musky…"
    PARTY_GUEST "And do you like that?"
    VES "Y-Yes…!"
    VES "Ahh—what are you doing to me?!"
    PARTY_GUEST "Tell us."
    PARTY_GUEST "Do you dream about his cock?"
    VES "N-No—!"
    VES "…I mean… yes… sometimes…"
    VES "There's no harm in dreaming… r-right?"
    "They stroked faster."
    PARTY_GUEST "And in those dreams?"
    VES "It's too embarrassing to say!"
    PARTY_GUEST "It's just a dream!"
    PARTY_GUEST_PERVY "Yeah! Just a dream!"
    PARTY_GUEST_PERVY "You can tell us."
    VES "... Ummm."
    VES "H-He's stronger than me."
    VES "He and his big… perfect cock…"
    VES "I'm his {i}*huff*{/i} good little orc… his pet…"
    VES "And I drain his balls Every. Single. Night!"
    "The men groaned, reaching their peak."
    PARTY_GUEST "Then take it!"
    PARTY_GUEST_PERVY "Cumming!"
    PARTY_GUEST_PERVY "Same!"
    PARTY_GUEST_PERVY "Get painted, greenskin slut!"
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    scene ves_tarbeck_orgy_finish with flash
    $ UnlockGalSceneAndGrantXp("ves", "tarbeck_orgy")
    $ Pause()
    "Hot ropes of cum splashed across Ves' face… her chest… her tits… covering her in thick, sticky white."
    "Panting breathlessly, she stared up at them, dazed… flustered… strangely radiant."
    PARTY_GUEST "Ahh… good job, boys."
    PARTY_GUEST_PERVY "If Skarshire women look like THIS, I'm visiting."
    PARTY_GUEST_PERVY "Come on lads, Jonas' wife is waiting."
    "They wandered off arguing about it."
    scene black with dissolve
    $ AutoMus(True)
    "...After cleaning herself, Ves returned."
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    MC @talk "So… do you want to talk about that?"
    VES @talk "…We shall never speak of this again."
    hide ves with easeoutleft
    $ Pause(0.15)
    show cg_tarbeck_watcher at center_f with easeinright
    WATCHER "...For your participation."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token", 2)
    $ Pause(0.1)
    show cg_tarbeck_watcher at blurin, center
    hide cg_tarbeck_watcher with easeoutright
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Orgy_over

label qst_TheTarbecks_Room_Orgy_kiara_cont:
    "As she sauntered forward, her cute freckled ass wiggling with an exaggerated sway, it didn't take long before a group of men noticed."
    "Kiara smiled alluringly, running a hand slowly down the chest of the closest man, and before long, she was surrounded."
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop.ogg", 1)
    scene kiara_tarbeck_orgy_1 with dissolve
    $ Pause()
    "In what felt like mere moments as I glanced back and forth, Kiara was already riding one of them, moaning happily as another pressed in behind her, pushing his cock into her ass."
    KIARA "F-Fucking hells, boys!"
    KIARA "Take it easy—are you trying to break my holes or what!?"
    PARTY_GUEST "I thought Northern girls were used to handling two swords at once?"
    KIARA "We—ahhh—ARE!"
    KIARA "Mmfghh!"
    "Kiara continued to moan as the men stuffed her greedy holes, her eyes occasionally flicking toward me, seeking approval."
    "*SLAP!*"
    "Kiara gasped as her ass jiggled, a bright pink handprint blooming across her cheek."
    KIARA "O-Oi!"
    PARTY_GUEST_PERVY "Couldn't resist, girl!"
    PARTY_GUEST_PERVY "F-Fuck… your ass is tight!"
    KIARA "Ahh! Th—mmmfghh—thank you!"
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop5.ogg", 1)
    scene kiara_tarbeck_orgy_2 with dissolve
    $ Pause()
    "As the men continued pounding into her, Kiara threw her ass back into them, her moans deep and feral, her tits bouncing wildly..."
    KIARA "S-SHIT!"
    KIARA "Gods… *huff* this is… mmfghh!"
    KIARA "I feel so f-full!"
    PARTY_GUEST "Are all Northern girls as good a fuck as you!?"
    KIARA "A-AHH!"
    KIARA "Hahah—mmmf—haha!"
    KIARA "Us Northerners know—mhffghh!"
    KIARA "HOW TO FUCK!"
    "Sweat glistened across her chest as Kiara moaned breathlessly."
    KIARA "T-Tschh… you're stretching me—mmfghh—good boys!"
    PARTY_GUEST_PERVY "Is that your husband over there?"
    KIARA "H-He's not my—*Huff!*"
    KIARA "Oh fuck it!"
    KIARA "Y-YES! Mmmfghh!"
    KIARA "HE'S MINE!"
    KIARA "NOW STOP WASTING TIME AND FUCK ME HARDER!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene kiara_tarbeck_orgy_3 with dissolve
    $ Pause()
    "As the two men obliged, a third, stroking his cock just inches from her face, grinned and pressed himself against her lips."
    "Without hesitation, Kiara's mouth opened eagerly, swallowing him down as she moaned happily."
    PARTY_GUEST_PERVY "Fuuuuuck!"
    KIARA "Mmfghh! *Slurp!* Mmmffghh!!"
    "Her lips moved greedily along him as the others continued to slam into her, the wet sounds of flesh meeting flesh echoing all around."
    "*Phlap!* *Phlap!* *Phlap!*"
    "Their sweat dripped, their breathing staggered, each of them fighting not to finish too soon."
    PARTY_GUEST "F-Fuck! I don't know how much longer I can—"
    PARTY_GUEST_PERVY "GODS, IS SHE A DEMON!?"
    PARTY_GUEST_PERVY "HER MOUTH FEELS LIKE IT'S SUCKING MY SOUL OUT!"
    PARTY_GUEST_PERVY "Ahh! I'm nearly there too!"
    PARTY_GUEST_PERVY "Her ass is too damn—"
    KIARA "*Slurp!* Shudhupp and chumm! *Slurp!*"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene kiara_tarbeck_orgy_finish with flash
    $ UnlockGalSceneAndGrantXp("kiara", "tarbeck_orgy")
    $ Pause()
    PARTY_GUEST_PERVY "HRGHHHH!"
    "One by one, they came in quick succession, flooding Kiara's holes."
    "She let out a high, breathless gasp as she swallowed the load in her mouth, while the others spilled from her in hot streams down her thighs."
    PARTY_GUEST "Phew!"
    PARTY_GUEST "That was fun!"
    PARTY_GUEST_PERVY "Come on, the Bala sisters are here tonight—let's go pay them a visit!"
    PARTY_GUEST_PERVY "Ha! You should've said that sooner!"
    "The men laughed and staggered away, leaving Kiara trembling, coated in their seed, slowly pulling herself upright again."
    scene black with dissolve
    $ AutoMus(True)
    "After wiping herself off as best she could, she returned to me."
    $ LocFlush()
    show mc at cleft
    show kiara at cright_f
    with dissolve
    MC @surprised "...Uhh."
    KIARA @talk "Everything is sore."
    KIARA @think "You looked like you were having fun."
    MC @talk "I—"
    show cg_tarbeck_watcher at left with easeinleft
    WATCHER "...For your participation."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token", 2)
    WATCHER "We hope you enjoy the rest of the *games* this evening."
    hide cg_tarbeck_watcher with easeoutright
    MC @talk "You ready to go?"
    KIARA @talk "Of course."
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    KIARA @blush "..."
    show kiara at center_f with ease
    MC "Kiara!"
    KIARA @shock "C-Coming!"
    hide kiara with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Orgy_over

label qst_TheTarbecks_Room_Orgy_esme_cont:
    "It didn't take Esme long to find some entertainment herself."
    "Grabbing hold of a couple of men, she practically dragged them in."
    "The first man lifted her up into his arms."
    "With practiced ease, he aligned the head of his cock with her tight asshole."
    PARTY_GUEST "Listen, are you sure abo—"
    ESME "Stop talking and both of you stuff me with your huge cocks."
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop.ogg", 1)
    scene esme_tarbeck_orgy_1 with dissolve
    $ Pause()
    "The two men looked at each other, then obliged, wedging Esme between them as they filled her tight pussy and ass at once."
    ESME "Mmmfghhh!"
    ESME "*Huff* So good! Ahh!"
    "They began to thrust into her, treating Esme like nothing more than a toy for their pleasure as she moaned wildly."
    PARTY_GUEST_PERVY "Tight little… ahh! Slut!"
    "Their groans mixed with hers, the lewd sound of flesh colliding echoing through the room as Esme's eyes began to roll back."
    ESME "T-That's it! Mmfghh!"
    ESME "Stuff your little katai whore!"
    ESME "F-F-F-Fuckkkk!"
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop5.ogg", 1)
    scene esme_tarbeck_orgy_2 with dissolve
    $ Pause()
    PARTY_GUEST_PERVY "Haha! This is why I love fucking katai women!"
    PARTY_GUEST_PERVY "They're all crazy about cock!"
    ESME "Mmmfghh! S-Stop talking and—"
    ESME "Keep f-fucking me!"
    "Her holes stretched around their cocks as she bounced greedily in their arms, moaning like she was in heaven."
    ESME "Come on boys!"
    "She held tight, her small fangs gently pressing against one man's shoulder as they rammed their cocks into her."
    PARTY_GUEST "F-FUCKKK!"
    "They pounded her harder, making Esme whimper and squeal with bliss."
    ESME "Ooooooh!"
    ESME "I love my job! I love my job! I love my job!"
    PARTY_GUEST "What is she talking about?"
    PARTY_GUEST_PERVY "Urghh—who cares?!"
    PARTY_GUEST_PERVY "I'm about to—"
    PARTY_GUEST "F-Fuck! So am I!"
    PARTY_GUEST_PERVY "Then let's fill this little katai slut up!"
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_finish.ogg")
    scene esme_tarbeck_orgy_finish with flash
    $ UnlockGalSceneAndGrantXp("esme", "tarbeck_orgy")
    $ Pause()
    "They slammed deep into Esme, grunting like animals as they came inside both of her holes."
    PARTY_GUEST "GRGHHH!"
    PARTY_GUEST_PERVY "S-So damn tight!"
    "Esme's legs locked around the man in front of her, a squealing cry escaping her lips, mouth hanging open in bliss."
    ESME "EEEEEEEEEEEEEP!"
    "Fully spent, the men eventually let her go."
    "Her feet touched the ground again, while the two men bent forward, hands on their knees, were left aching to catch their breath."
    PARTY_GUEST "Gods girl… I've never seen a katai fuck half as good as you."
    ESME "*yawn*"
    ESME "Be dears and go find me some more toys."
    PARTY_GUEST_PERVY "You're not done!?"
    ESME "No."
    "She licked her lips."
    ESME "I'm still hungry."
    scene black with dissolve
    "{i}... An hour later...{/i}"
    $ AutoMus(True)
    $ LocFlush()
    show mc at cleft
    show esme at cright_f
    with dissolve
    ESME @smile "Have fun?"
    MC @think "…"
    ESME @shock "What?"
    MC @talk "You have quite the… appetite."
    ESME @smile "Either men devour you in the bedroom…"
    ESME @smile "Or you devour them."
    MC "I see…"
    show cg_tarbeck_watcher at center with easeinleft
    "From the corner of my eye, one of the watchers approached, gold tokens in hand."
    WATCHER "One for each."
    WATCHER "And what a spectacle it was to witness, even in a room already full of lust and passion."
    show cg_tarbeck_watcher at nod
    $ PlayerAddItem("qst_tarbeck_golden_token", 2)
    ESME @smile "I should start charging for the privilege of watching."
    ESME @smile "I'd make a killing."
    show cg_tarbeck_watcher at blurin, center_f
    WATCHER "Please… enjoy the rest of the games."
    WATCHER "We'll be watching…"
    show cg_tarbeck_watcher at blurin, center
    hide cg_tarbeck_watcher with easeoutright
    "The watcher quietly slipped away."
    show esme at center_f with ease
    ESME @smile "Well then, let's get moving, shall we?"
    ESME @smile "More tokens to win and all that."
    MC @talk "Come on then."
    show mc at blurin, cleft_f
    ESME @smile "Right behind you…"
    hide mc
    hide esme
    with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_tarbeck_playhallway")
    jump qst_TheTarbecks_Room_Orgy_over

label qst_TheTarbecks_Room_Orgy_over:
    $ QstTheTarbecks().CalcGoldTokens()
    $ QstTheTarbecks().PlayedInRooms.add("orgy")
    $ LocEnter()