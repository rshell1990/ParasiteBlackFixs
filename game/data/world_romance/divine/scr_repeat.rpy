label rom_divine_rep_sex:
    DIVINE @lewd "Well..."
    DIVINE @lewd "Should I put on my lingerie?"
    menu:
        "Put it on":
            DIVINE @happy "As you wish..."
            $ CharSetClothes("divine", "ling")
        "Just undress":
            DIVINE "So be it."
            $ CharSetClothes("divine", "naked")
    show divine at blurin, nod
    DIVINE @lewd "Now then..."
    show divine at cright_f with easeoutright
    show mc at cleft with easeinleft
    MC @surprised "You're-"
    DIVINE @lewd "Ready to play."
    DIVINE "But it seems you’re not...{i}’in proper attire’{/i} yet..."
    "I smiled clumsily."
    MC @smile "Ahh, of course."
    $ CharSetClothes("mc", "pants")
    show mc at blurin, nod
    "As I stripped down naked, Sister Divine sat back onto her bed."
    $ CharSetClothes("mc", "naked")
    show mc at blurin, nod
    "Her eyes looked over me hungrily, her cock twitching in excitement as her eyes stared at my dangling cock."
    scene black with dissolve
    play sound2 "audio/cfx/transform.ogg"
    "Sister Divine watched the gruesome transformation happen yet again with both morbid fascination and blushing arousal as I now towered over her in my other form."
    $ LocFlush()
    show divine at cright_f
    show mc_transformed_erect at cleft
    with dissolve
    "I stood before her with my monstrous hard-on at the ready."
    "While the perfume she wore was soft but alluring, in this form, I could smell her natural scents beneath it, and she gave away her excitement as I moved closer towards her."
    "I could hear her heart race as she enticed me forward."
    jump rom_divine_rep_sex_choicemenu

label rom_divine_rep_sex_choicemenu:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    DIVINE @lewd "So, beast, what should we do this time?"
    menu:
        "Standing fuck":
            jump rom_divine_standing
        "Missionary":
            jump rom_divine_missionary
        "Make her suck your cock":
            jump rom_divine_blowjob

label rom_divine_standing:
    "Stepping towards Sister Divine I saw her grow nervous for a moment as I towered over her, my powerful large hands grabbing at her sides."
    show mc_transformed_erect at center with easeinleft
    DIVINE "M-My... What did you-"
    DIVINE "{i}*Gasp!*{/i}"
    "Spinning her around, I used my hands to bend her forward, her round plump ass now fully exposed for me as it bathed in the moonlight."
    "Beneath her enticing, wet, tight holes dangled her cock, hard with anticipation as she waited for me to take her from behind."
    "I could feel her heart racing beneath my fingertips as she breathed heavily in an intoxicating mix of nervousness and arousal." 
    "As my cock rubbed against the crack of her butt she cooed:"
    DIVINE "So... This is how you want to take me this time, huh?"
    DIVINE "{i}...I’m ready.{/i}"
    "I leaned forward, grunting as I nuzzled at her neck before pulling back."
    "Now all that was left to decide was, which hole should I take?"
    menu:
        "Fuck her pussy":
            "As I pressed and prodded my member against her wet, tight pussy, I felt Sister Divine tighten up."
            "I pushed my member as far I could into her."
            DIVINE "A-Ahh! I almost forgot how big you were!"
            DIVINE "Give me a moment to adjust!"
            "I paused for a moment, letting Sister Divine catch her breath as she trembled beneath my claws, her legs slightly shaking."
            DIVINE "I've missed this sword of yours..."
            DIVINE "Come, continue!"
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_vag_preg_notent with dissolve
                else:
                    scene divine_standing_ling_vag_nopreg_notent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_vag_preg_notent with dissolve
                else:
                    scene divine_standing_naked_vag_nopreg_notent with dissolve
            $ Pause()
            DIVINE "Mmmfgh! Yes! That’s it!"
            "Her body tightened around me as we picked up the pace."
            "Sister Divine backed her round, large butt up onto me slowly as she began to moan."
            "Her hard member moved as her large breasts swayed with every thrust."
            DIVINE "Yes ... J-just like that."
            DIVINE "F-Faster ... Go faster!"
            "I did as she asked, the fleshy sounds of her butt slapping against me grew louder and faster as I took her from behind."
            DIVINE "Yes! That's it! YES!"
            DIVINE "Gods, you're huge!"
            "In that moment, the dark desires came bubbling to the surface, and I remembered what my tentacles could do..."
            "Suddenly, as one of tentacles appeared over my shoulder, it slowly made it’s way towards the back of Sister Divine’s head."
            "With the teeth retracted, it began to swallow her head from behind."
            "Sister Divine panicked for a moment, seeking to break away but I held her firmly in place."
            DIVINE "W-What are you-!"
            DIVINE "Mmmfgh?!"
            $ PlaySexFx("audio/sex_sounds/ves69_150.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_vag_preg_tent with dissolve
                else:
                    scene divine_standing_ling_vag_nopreg_tent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_vag_preg_tent with dissolve
                else:
                    scene divine_standing_naked_vag_nopreg_tent with dissolve
            $ Pause()
            "In that moment, the tentacle swallowed over the top of Sister Divine’s head, and she squirmed in worry for a moment, before she felt the tongue slip deep down her throat." 
            DIVINE "(Ahh... T-These again!)"
            DIVINE "(Thank the gods I can still breathe with this thing down my throat!)"
            "Roaring with delight, I began to pump her body from behind furiously."
            "Muffled cries and moans escaped Sister Divine from inside the bulbous head of the tentacle, but her wetness gave away her excitement as I continued to slam against her soft round ass from behind."
            DIVINE "Mmmmfghhh!!"
            DIVINE "(It’s pumping something into me again... Mhmm!)"
            DIVINE "(Gods... {i}It’s wonderful!{/i})"
            DIVINE "(My body feels like fire!)"
            "Sister Divine’s body continuously tightened, she was now just a play doll for me to use, not a person but a thing for me to mate and have my way with."
            "Continuous grunts and muffled moans escaped her lips uncontrollably as she had her third and fourth orgasms, her juices dripping down onto the floor, but I wasn’t done yet..."
            DIVINE "(Oh gods... How much longer will this last?)"
            DIVINE "(I feel like I am melting!)"
            scene black with dissolve
            $ Pause(0.5)
            $ TimeAdvBy(TIME_1H)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_vag_preg_tent with dissolve
                else:
                    scene divine_standing_ling_vag_nopreg_tent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_vag_preg_tent with dissolve
                else:
                    scene divine_standing_naked_vag_nopreg_tent with dissolve
            "Before I knew it, an hour had passed."
            "I held tightly onto her soft ass cheeks and sharply pulled her back, shoving my cock in all the way."
            DIVINE "(Oh gods ... I can't even think anymore!)"
            DIVINE "(Mhmm! He's close! I can f-feel he's finally close!)"
            "I dug my claws into Divine's round ass, making her yelp out as I slammed my cock into her the last few times before I forced it inside her and held it there."
            "Emptying myself deeply into her pussy, I roared."
            $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
            play sound2 "audio/cfx/transform.ogg"
            
            $ ReduceInfectionFromSex("divine")
            $ PregRoll("divine")
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_vag_preg_finish with flash
                    $ UnlockGalFlag("divine", "standing", "ling_vag_preg")
                else:
                    scene divine_standing_ling_vag_nopreg_finish with flash
                    $ UnlockGalFlag("divine", "standing", "ling_vag_nopreg")
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_vag_preg_finish with flash
                    $ UnlockGalFlag("divine", "standing", "naked_vag_preg")
                else:
                    scene divine_standing_naked_vag_nopreg_finish with flash
                    $ UnlockGalFlag("divine", "standing", "naked_vag_nopreg")
            $ Pause()
            $ UnlockGalSceneAndGrantXp("divine", "standing")
            DIVINE "(T-There's so much of it! H-He's filling me up so much again! {image=[ICON.HEART]})"
            DIVINE "(It's so hot! I c-can feel it overflowing!)"
            "Finally satisfied, I slowly unsheathed my cock from her, and as the tentacle loosened and released her head, Sister Divine slumped to the floor deliriously."
            "I watched as my seed poured from her aching, stretched pussy while some of my... chemical poured from the side of her mouth onto the floor."
            "She shook slightly, her body overcome by pleasure as I leaned down to pick her up and rest her on the bed, nuzzling and soothing her."
            DIVINE "Urghh..."
            "After a few moments of slight anxious worry that I had pushed her too far, the murmured, exhausted words escaped her lips:"
            DIVINE "{i}Incredible...{/i} {image=[ICON.HEART]}"

        "Fuck her ass":
            "With a snort of hot air, I pressed my cock against the rosebud of Sister Divine’s tight asshole."
            "She gasped in surprise at first, before giggling and looking over her shoulder with a playful smirk."
            DIVINE "Oh my..."
            DIVINE "Quite the mischievous beast wanting {i}that{/i} hole, aren’t you?"
            "I grunted in acknowledgment, my raspy voice remarking,"
            MC "Your body belongs to me, again."
            DIVINE "Ahh~ then do what you must with me..."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_anal_preg_notent with dissolve
                else:
                    scene divine_standing_ling_anal_nopreg_notent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_anal_preg_notent with dissolve
                else:
                    scene divine_standing_naked_anal_nopreg_notent with dissolve
            $ Pause()
            "Sister Divine let out a gasp followed shortly by a loud moan as I forced my cock into her tight ass."
            DIVINE "Gods... You really are-ah! S-Stretching it back there!"
            DIVINE "Mmmfgh... {image=[ICON.HEART]}"
            DIVINE "Don’t stop, k-keep going!"
            "In that moment, the dark desires came bubbling to the surface, and I remembered what my tentacles could do..."
            "Suddenly, as one of tentacles appeared over my shoulder, it slowly made its way towards the back of Sister Divine’s head."
            "With the teeth retracted, it began to swallow her head from behind."
            DIVINE "W-What are you-"
            DIVINE "Mmmfgh?!"
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_anal_preg_tent with dissolve
                else:
                    scene divine_standing_ling_anal_nopreg_tent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_anal_preg_tent with dissolve
                else:
                    scene divine_standing_naked_anal_nopreg_tent with dissolve
            $ Pause()

            "In that moment, the tentacle swallowed up the top of Sister Divine’s head, and she squirmed in worry for a moment before she felt the tongue slip deep down her throat."
            DIVINE "(Ahh... T-These again!)"
            DIVINE "(Thank the gods I can still breathe with this thing down my throat!)"
            "Roaring with delight, I began to pump her from behind."
            "Muffled cries and moans escaped Sister Divine from inside the bulbous head of the tentacle, but her tight asshole quivered around my cock as her pussy beneath became soaking wet."
            "Dripping onto the floor, her juices gave away her excitement while I continued to slam against her soft round ass from behind."
            DIVINE "Mmmmfghhh!!"
            DIVINE "(It’s pumping something into me again...Mhmm!)"
            DIVINE "(Gods...{i}It’s wonderful!{/i})"
            DIVINE "(My ass! Oh gods! It’s never felt {i}this{/i} good before!)"
            DIVINE "(My body feels like fire!)"
            DIVINE "{i}(Mmmfghh!){/i}"
            "Unable to control herself anymore, I felt Sister Divine’s body continuously tighten and shake around me."
            "She was now just a play doll for me to use, not a person but a thing for me to mate and have my way with."
            "Her asshole gripped me tight, and despite my best efforts not to hurt her, it was next to impossible not to let the pulsating darkness in me thrust furiously into her backdoor."
            "Continuous grunts and muffled moans escaped her lips now, as she had her third and fourth orgasms."
            "A puddle of her juices formed beneath her, but I wasn’t done yet..."
            scene black with dissolve
            $ Pause(0.5)
            $ TimeAdvBy(TIME_1H)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_anal_preg_tent with dissolve
                else:
                    scene divine_standing_ling_anal_nopreg_tent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_naked_anal_preg_tent with dissolve
                else:
                    scene divine_standing_naked_anal_nopreg_tent with dissolve
            $ Pause()
            "Before I knew it, an hour had passed."
            "I held tightly onto her soft ass cheeks and sharply pulled her back on my cock."
            DIVINE "(Oh gods ... I can't even think anymore!)"
            DIVINE "(Mhmm! He's close! I can f-feel he's finally close!)"
            "I dug my claws into Divine's round ass, making her yelp out, slamming my cock into her the last few times before I forced it all the way in."
            "I pushed the whole length of my cock inside of her ass and held it there."
            "Emptying myself deeply into her asshole, I roared." #cum
            $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
            $ ReduceInfectionFromSex("divine")
            play sound2 "audio/cfx/transform.ogg"
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_standing_ling_anal_preg_finish with flash
                    $ UnlockGalFlag("divine", "standing", "ling_anal_preg")
                else:
                    scene divine_standing_ling_anal_nopreg_finish with flash
                    $ UnlockGalFlag("divine", "standing", "ling_anal_nopreg")
            else:
                if CharIsVisiblyPreg("divine"):
                    $ UnlockGalFlag("divine", "standing", "naked_anal_preg")
                    scene divine_standing_naked_anal_preg_finish with flash
                else:
                    $ UnlockGalFlag("divine", "standing", "naked_anal_nopreg")
                    scene divine_standing_naked_anal_nopreg_finish with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("divine", "standing")
            DIVINE "(T-There's so much of it! H-He's filling me up so much! {image=[ICON.HEART]})"
            DIVINE "(It's so hot! I c-can feel it overflowing!)"
            "Finally satisfied, I unsheathed my cock from her, and as the tentacle loosened and released from her head, Sister Divine slumped to the floor deliriously."
            "I watched as my seed poured from her aching, stretched ass while some of the chemical poured from the side of her mouth onto the floor."
            "She shook slightly, her body overcome by pleasure as I leaned down to pick her up and rest her on the bed, nuzzling and soothing her."
            DIVINE "Urghh..."
            "After a few moments of anxious worry that I had pushed her too far, the murmured, exhausted words escaped her lips:"
            DIVINE "{i}So good...{/i} {image=[ICON.HEART]}"
    jump rom_divine_notfirsttime_after_sex

label rom_divine_missionary:
    DIVINE "Feeling romantic this time, are we?"
    "I let some hot air from my snout as Sister Divine giggled, sitting down on the bed as she grabbed hold of both her legs and raised them into the air."
    "She exposed both of her holes and gave me a passionate look."
    DIVINE "Very well {i}lover...{/i}"
    DIVINE "Take what you will..."
    menu:
        "Fuck Sister Divine’s pussy":
            "Placing the bulbous head of my cock against Sister Divine’s already wet pussy, I gently pushed the head into her."
            "As her pussy gave way to the head and spread around it, Sister Divine moaned softly, closing her eyes as she felt my cock pushing into her."
            DIVINE "Ooooh~"
            DIVINE "C-Careful lover."
            "Sister Divine giggled, but as I forced the last few inches in abruptly, she gasped in shock, reaching forward to grab me to steady herself."
            DIVINE "W-Wait a moment!"
            DIVINE "By the gods... I need a minute to get used to it!"
            "Heeding her words, I paused for a moment or two while she caught her breath."
            DIVINE "..O-Okay..."
            DIVINE "{i}Continue.{/i}"
            "Slowly, I began to thrust in and out of Sister Divine’s eager body."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_ling_vag_preg_notent with dissolve
                else:
                    scene divine_missionary_ling_vag_nopreg_notent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_naked_vag_preg_notent with dissolve
                else:
                    scene divine_missionary_naked_vag_nopreg_notent with dissolve
            $ Pause()
            "Hot, sultry breaths escaped her pursed lips as she felt my cock sink in and out of her velvety grip."
            "Between her hot moans, she playfully goaded me on, softly muttering:"
            DIVINE "Mmmfgh! I've missed this!"
            DIVINE "Ahh {image=[ICON.HEART]}"
            DIVINE "I can feel the power coursing through you... It’s..."
            DIVINE "{i}Incredible...{/i}"
            "Encouraged, I began to move faster, rutting with her like an animal as I thrusted into her tight body."
            "Responding in kind, Sister Divine moaned as I felt her tighten around me greedily."
            DIVINE "Y-Yes! So good!"
            DIVINE "D-Don’t stop! Gods please!"
            DIVINE "Fuck me harder!"
            "I continued to force my cock deep into her when I felt the dark impulses of the parasite surfacing."
            "As if a dark veil had covered my mind..."
            "I gave in, two tentacles sliding from over my shoulders, their teeth retracted as they snaked their way up past Sister Divine’s stomach, towards her breasts."
            DIVINE "W-What are you-"
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_ling_vag_preg_tent with dissolve
                else:
                    scene divine_missionary_ling_vag_nopreg_tent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_naked_vag_preg_tent with dissolve
                else:
                    scene divine_missionary_naked_vag_nopreg_tent with dissolve
            $ Pause()
            "Suddenly, the two tentacles attached to her breasts and began to suckle at them."  
            DIVINE "Ooooooh!~"
            DIVINE "These things?!"
            DIVINE "Ah... ~They sure are – Oooh!~"
            DIVINE "Hungry...aren’t they? Ah! {image=[ICON.HEART]}"
            DIVINE "Mmmfgh! Yes!"
            DIVINE "You’re so deep inside me... so hot... so..."
            DIVINE "A-Ahh! {image=[ICON.HEART]}"
            "Sister Divine’s body tightened around me as I continued to thrust into her, my body burning with primal desire as I breathed heavily."
            "I rolled out my tongue to lick at her hardened nipples."
            DIVINE "{i}*Giggles!*{/i} That tickles!"
            DIVINE "Ooooh! I can feel how hard you are in me..."
            DIVINE "Are you close, my beast?"
            DIVINE "Yes!... YES! I can feel you throbbing!"
            DIVINE "You’re so c-close!"
            DIVINE "Do it! Finish inside me and claim me, you beast!"
            "Unable to hold back any longer, I dragged Sister Divine towards me, forcing myself as deeply as I could into her."
            "Her eyes widened as she moaned, trembling beneath my claws as she felt the hot seed pour into her."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            $ PregRoll("divine")
            $ ReduceInfectionFromSex("divine")
            play sound2 "audio/cfx/transform.ogg"
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    $ UnlockGalFlag("divine", "missionary", "ling_vag_preg")
                    scene divine_missionary_ling_vag_preg_finish with flash
                else:
                    $ UnlockGalFlag("divine", "missionary", "ling_vag_nopreg")
                    scene divine_missionary_ling_vag_nopreg_finish with flash
            else:
                if CharIsVisiblyPreg("divine"):
                    $ UnlockGalFlag("divine", "missionary", "naked_vag_preg")
                    scene divine_missionary_naked_vag_preg_finish with flash
                else:
                    $ UnlockGalFlag("divine", "missionary", "naked_vag_nopreg")
                    scene divine_missionary_naked_vag_nopreg_finish with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("divine", "missionary")
            DIVINE "Mmmfghh! {image=[ICON.HEART]}"
            DIVINE "There’s... so much of it!"
            DIVINE "Just like before!"
            DIVINE "Ahh...!~"
            "Breathing heavily, I slowly unsheathed my softening member from her."
            "As I pulled out, Sister Divine shuddered slightly, loads of hot seed flowing out of her onto the bed quilts."
            DIVINE "O-Oooh~"
            DIVINE "That was..."
            "Sister Divine licked her lips."
            DIVINE "{i}Wonderful.{/i} {image=[ICON.HEART]}"

        "Fuck Sister Divine’s ass":
            "Staring at her tight, button like asshole, I gently prodded my cock against her backdoor, and Sister Divine laughed a little before remarking playfully."
            DIVINE "Oh my...!"
            DIVINE "Well...You better start gentle if you’re going to take me like that~"
            "I pushed in, {b}hard.{/b}"
            "Sister Divine’s asshole stretched to accommodate the dripping head of my cock."
            "She winced in pain, closing her eyes as she gritted her teeth while I forced myself deeper into her ass."
            DIVINE "G-Grghh!"
            DIVINE "E-Easy! Ah!"
            "I tilted my head quizzically for a few moments, watching her breathing outward as she tried to relax."
            DIVINE "Ahhh... It’s a good thing your {i}weapon{/i} is self-lubricating, isn’t it?"
            "I waited for a few moments to let Sister Divine get comfortable, before she finally said,"
            DIVINE "Slowly... Go slowly."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_ling_anal_preg_notent with dissolve
                else:
                    scene divine_missionary_ling_anal_nopreg_notent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_naked_anal_preg_notent with dissolve
                else:
                    scene divine_missionary_naked_anal_nopreg_notent with dissolve
            $ Pause()
            "I began to inch my cock deeper into her tight ass."
            "Sister Divine moved between winces of pain and soft moans..."
            "Finally, with the last jolt forward, the final inch bottomed out in her ass, and Sister Divine gasped in surprise before cooing softly."
            DIVINE "Ooooh~"
            DIVINE "What is it you’re secreting?"
            DIVINE "It’s... Mmmhmm... Wonderful!"
            "After a few thrusts, Sister Divine’s sultry moans and hot breaths had let me know she was eager for me to continue pounding her tight ass."
            DIVINE "Ah! Yes! T-That’s it!"
            DIVINE "Fuck me... Fuck me harder!"
            "In that moment, I felt a primal urge..."
            "Two tentacles appeared over my shoulders, their teeth retracted as they snaked their way up past Sister Divine’s stomach towards her breasts."
            DIVINE "W-What are you-"
            "Suddenly, the two tentacles attached to her breasts and began to suckle at them."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_ling_anal_preg_tent with dissolve
                else:
                    scene divine_missionary_ling_anal_nopreg_tent with dissolve
            else:
                if CharIsVisiblyPreg("divine"):
                    scene divine_missionary_naked_anal_preg_tent with dissolve
                else:
                    scene divine_missionary_naked_anal_nopreg_tent with dissolve
            $ Pause()
            DIVINE "Ooooooh!~"
            DIVINE "These things?!"
            DIVINE "Ah... They sure are – Oooh!~"
            DIVINE "Hungry...aren’t they? Ah! {image=[ICON.HEART]}"
            DIVINE "Mmmfgh! Yes!"
            DIVINE "Oh gods! Yes! Pound that little ass!"
            DIVINE "Your cock is... is..."
            DIVINE "{i}So different!{/i}"
            DIVINE "Ahh {image=[ICON.HEART]}"
            DIVINE "I can feel the power coursing inside you... It’s..."
            DIVINE "{i}Incredible...{/i}"
            "Encouraged, I began to move faster, rutting with her like an animal, thrusting into her tight body."
            "Sister Divine moaned as I felt her asshole tighten around me greedily."
            DIVINE "Yes! So good!"
            DIVINE "My ass! You’re stretching it so much!"
            DIVINE "Are you trying to make it so that I – Ah! Can’t sit down properly for the next few weeks?"
            DIVINE "D-Don’t stop! Gods please! Fuck me harder!"
            DIVINE "P-Please, I can feel you throbbing...!"
            DIVINE "D-Do it! Finish inside me already! I want to feel you pour it into me!"
            "Thrusting in and out of Sister Divine’s ass, she grunted and moaned with every sudden thrust deep into her."
            "She let out pleading moans, urging me not to stop till I had finished inside of her."
            "As my cock began to ache, I knew I couldn’t hold on any longer, and promptly forced my cock deeply into her."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            $ ReduceInfectionFromSex("divine")
            play sound2 "audio/cfx/transform.ogg"
            if CharGetClothes("divine") == "ling":
                if CharIsVisiblyPreg("divine"):
                    $ UnlockGalFlag("divine", "missionary", "ling_anal_preg")
                    scene divine_missionary_ling_anal_preg_finish with flash
                else:
                    $ UnlockGalFlag("divine", "missionary", "ling_anal_nopreg")
                    scene divine_missionary_ling_anal_nopreg_finish with flash
            else:
                if CharIsVisiblyPreg("divine"):
                    $ UnlockGalFlag("divine", "missionary", "naked_anal_preg")
                    scene divine_missionary_naked_anal_preg_finish with flash
                else:
                    $ UnlockGalFlag("divine", "missionary", "naked_anal_nopreg")
                    scene divine_missionary_naked_anal_nopreg_finish with flash
            $ Pause()
            $ UnlockGalSceneAndGrantXp("divine", "missionary")
            "I bottomed out all the way inside her and held her in place as I roared while pouring my seed into her ass."
            "Sister Divine trembled beneath my claws, her eyes wide and mouth agape as she shuddered, whimpering from the overwhelming pleasure."
            "Slowly, unsheathing my cock from her ass, I watched Sister Divine shudder when the head finally popped out, the overflowing cum poured from her stretched hole."
            DIVINE "O-Oooh...!"
            DIVINE "My butt... Mhmm!"
            DIVINE "That was..."
            "Sister Divine licked her lips."
            DIVINE "{i}So good.{/i} {image=[ICON.HEART]}"
    jump rom_divine_notfirsttime_after_sex

label rom_divine_blowjob:
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_ling_idle_preg_notent with dissolve
        else:
            scene divine_bj_ling_idle_nopreg_notent with dissolve
    else:
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_naked_idle_preg_notent with dissolve
        else:
            scene divine_bj_naked_idle_nopreg_notent with dissolve
    $ Pause()
    "From my back, two of the tentacles emerged and coiled around Sister Divine, her shock quickly made way to giggles as the tentacles lifted her off her feet and dangled her in front of my hardened cock."
    DIVINE "Oh...!"
    "My rock hard, ribbed cock pressed up and rubbed against her cheek."
    DIVINE "Well, I suppose that’s one way to tell me you want me to suck your cock."
    "The tentacles suspending her in the air gently rocked her back and forward, tapping the head of my cock against her face playfully."
    "Sister Divine laughed once again,"
    DIVINE "Keen... Aren’t we?"
    "I let out a low rumble."
    DIVINE "Such an impatient lover!"
    DIVINE "Very well~"
    
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_ling_bj_preg_notent with dissolve
        else:
            scene divine_bj_ling_bj_nopreg_notent with dissolve
    else:
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_naked_bj_preg_notent with dissolve
        else:
            scene divine_bj_naked_bj_nopreg_notent with dissolve
    $ Pause()

    "Opening her mouth, Sister Divine gently wrapped her lips over the head as she slowly rocked her head as far forward as she could."
    "Her tongue flicking and dancing over the sensitive head sent sparks of pleasure coursing through me."
    DIVINE "{i}*Slurp!*{/i} mmmfghh...! {image=[ICON.HEART]}"
    "Sister Divine continued to coo and moan as she worked her wet mouth over my cock."
    "Letting out heavy, animal like breaths, I let her continue to pleasure me obediently, gently rocking her forward to try and force her face deeper onto my cock."
    "She grunted and slurped on it, devouring it eagerly."
    DIVINE "(Mfghh... I feel like I can barely wrap my lips around it.)"
    DIVINE "(Fufu, doesn't mean I won't give it a good try! {image=[ICON.HEART]})"
    DIVINE "{i}Slurp!{/i} Mfghhh!"
    "I let out another low rumble of approval, gently rocking her suspended body back and forth further as I tried to get her to swallow my cock more deeply."
    DIVINE "(Ooh! So you want me to shove this cock even deeper into me, huh?)"
    DIVINE "(Such a naughty creature... Come then, let's see what you've got!)"
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_ling_dt_preg_notent with dissolve
        else:
            scene divine_bj_ling_dt_nopreg_notent with dissolve
    else:
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_naked_dt_preg_notent with dissolve
        else:
            scene divine_bj_naked_dt_nopreg_notent with dissolve
    $ Pause()
    "Divine's mouth opened wider as she swallowed a few more inches of my cock, slightly gagging in the process." # - DEEP THROAT BJ
    "My cock was secreting the sensation-enhancing chemicals and pretty soon, Sister Divine was dripping sweat as she hungrily sucked on it, forcing it as deeply down her throat as she could go."
    DIVINE "Mmmfghh!!"
    DIVINE "(Incredible... My whole body feels like it’s burning up!)"
    DIVINE "(I just don’t want to stop!)"
    "As I watched Sister Divine’s breasts swing back and forth, her lips glided over my cock coating it in silvery saliva."
    "I felt the animalistic urge to use the rest of my tentacles..."
    "From over my shoulders, two more tentacles slid down, their teeth retracted as they snaked their way up past Sister Divine’s stomach towards her breasts."
    DIVINE "(W-What are you-)"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_ling_dt_preg_tent with hpunch
        else:
            scene divine_bj_ling_dt_nopreg_tent with hpunch
    else:
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_naked_dt_preg_tent with hpunch
        else:
            scene divine_bj_naked_dt_nopreg_tent with hpunch
    $ Pause()
    "Suddenly, the two tentacles attached to her breasts and began to suckle at them." 
    DIVINE "Mmmfgh?!"
    DIVINE "(They’re... They’re sucking me like... like...)"
    DIVINE "(Ooooh! They’re a little rough but it feels so nice!)"
    DIVINE "(Hungry... aren’t they? Ah! {image=[ICON.HEART]})"
    DIVINE "{i}*Glug!* *Slurp!*{/i} mmmffgh!!"
    "Sister Divine grunted in pleasure as the two tentacles did their best to milk her large dangling breasts."
    "Her rock-hard cock twitched in excitement, helpless as I continued to plunge my own past her soft lips."
    DIVINE "Mhmm! MHHH!"
    "Sister Divine's body began to drip with sweat, the aphrodisiac omitting from my skin drove her deeper and deeper into a fever of lust."
    DIVINE "(Gods... What's happening to me?)"
    DIVINE "(I didn't understand at first but-)"
    DIVINE "(Mmmfghh! Every time we fuck it becomes more and more clear to me!)"
    DIVINE "(It's so good!)"
    "I continued to thrust my cock into Sister Divine's warm, wet mouth for some time, listening to her hot wet slurps and moans as she tried to take my cock as deeply as she could down her throat."
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_ling_idle_preg_tent with dissolve
        else:
            scene divine_bj_ling_idle_nopreg_tent with dissolve
    else:
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_naked_idle_preg_tent with dissolve
        else:
            scene divine_bj_naked_idle_nopreg_tent with dissolve
    $ Pause()
    "For a brief moment, I unsheathed my cock from Sister Divine's mouth." #idle + tit milking
    DIVINE "What - {i}*Huff*{/i} are you doing?"
    DIVINE "Give it back! Give me your cock!"
    "I let out another low rumble and Divine laughed."
    DIVINE "Haha! You want me to beg?"
    "I nodded, rumbling once more in acknowledgment."
    DIVINE "Ooooh! They feel so good milking me! Mmfhh! "
    DIVINE "F-Fine you petulant beast, ram that fucking cock down my throat!"
    DIVINE "Make me your bitch!"
    play sound2 "audio/cfx/transform.ogg"
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_ling_dt_preg_tent with hpunch
        else:
            scene divine_bj_ling_dt_nopreg_tent with hpunch
    else:
        if CharIsVisiblyPreg("divine"):
            scene divine_bj_naked_dt_preg_tent with hpunch
        else:
            scene divine_bj_naked_dt_nopreg_tent with hpunch
    $ Pause()
    "I roared as I slammed my cock down into her throat once more." #DEEP THROAT BJ 
    DIVINE "Mmfghh!! {i}Slurp!{/i}"
    DIVINE "(Yes! Yes! More!)"
    DIVINE "(I'm so... I'm so...!)"
    "Between Divine's legs, a small pool was growing as her wet juices trickled down her leg onto the floor in little drops."
    "Her tongue thrashed desperately to please me as she let out muffled moaned so very sweetly for me."
    DIVINE "Mmfghhhhhhh...!! {i}Slurp!{/i}"
    "Eventually, after body continued to shudder time and time again with orgasms rippling through her, I felt my own climax finally drawing close."
    DIVINE "{i}*Slurp!* *Slurp!* Mhmfghh!{/i} {image=[ICON.HEART]}"
    DIVINE "(Mhff! He's close! I c-can feel him throbbing in my mouth!)"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    $ ReduceInfectionFromSex("divine")
    play sound2 "audio/cfx/transform.ogg"
    if CharGetClothes("divine") == "ling":
        if CharIsVisiblyPreg("divine"):
            $ UnlockGalFlag("divine", "bj", "ling_preg")
            scene divine_bj_ling_preg_finish with flash
        else:
            $ UnlockGalFlag("divine", "bj", "ling_nopreg")
            scene divine_bj_ling_nopreg_finish with flash
    else:
        if CharIsVisiblyPreg("divine"):
            $ UnlockGalFlag("divine", "bj", "naked_preg")
            scene divine_bj_naked_preg_finish with flash
        else:
            $ UnlockGalFlag("divine", "bj", "naked_nopreg")
            scene divine_bj_naked_nopreg_finish with flash
    $ Pause()
    "Unable to hold back any longer, I gripped Sister Divine's head and pulled her forward towards me, forcing every inch of my cock down her throat as I roared and flooded her belly with my seed."
    $ UnlockGalSceneAndGrantXp("divine", "bj")
    DIVINE "{i}*Glughhh!*{/i} Mmmfghhhh...! {image=[ICON.HEART]}"
    "Sister Divine shuddered as she desperately tried to swallow the overflowing seed that seeped out of her mouth onto the floor."
    "Her stomach began to bloat slightly as I continued pouring into her, till finally, I slowly unsheathed my cock, letting her gasp for air as she coughed and spluttered."
    DIVINE "*Cough!* Gods...!"
    DIVINE "{i}*Huff*{/i} {i}*Huff*{/i}"
    "With two loud *plops* my tentacles unshackled themselves from her now sore, over-stimulated breasts, and I gently pulled and laid her down to rest on her bed."
    jump rom_divine_notfirsttime_after_sex

label rom_divine_notfirsttime_after_sex:
    $ RomanceDivine().CanRepeatSex = False
    $ AutoMus(True)
    $ LocFlush()
    show divine at cright_f
    show mc_transformed_erect at cleft
    with dissolve
    DIVINE @happy "Ah~... Ah...~"
    DIVINE @lewd "I knew I chose wisely with you."
    $ CharChangeRel("divine", 1)
    "I rumbled soothingly, and in my raspy voice answered,"
    MC "I am glad you approve."
    DIVINE @happy "{i}Very{/i} much so..."
    DIVINE "Tell me, would you like to stay the night?"
    MC "...But, the students?"
    DIVINE "Oh, no one will disturb us in my quarters, don’t worry."
    DIVINE @happy "And you can sleep in whatever form you prefer should you wish."
    "Sister Divine's eyes nervously met the floor as she blushed."
    DIVINE "It would be nice to... Have the company."
    menu:
        "Cuddle with Sister Divine.":
            jump rom_divine_notfirsttime_cuddles
        "Leave.":
            jump rom_divine_notfirsttime_ishouldgo

label rom_divine_notfirsttime_cuddles:
    DIVINE @happy "What a romantic beast you are."
    "Sister Divine chuckled nervously."
    DIVINE "Now come, {i}lover.{/i}"
    scene cg_mc_divine_cuddles with dissolve
    $ Pause()
    DIVINE "...{image=[ICON.HEART]}"
    $ HealParty()
    scene black with dissolve
    $ TimeAdvTo(TIME_MORNING)
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ Pause(0.5)
    $ CharSetClothes("mc", "pants")
    $ CharSetClothes("divine", "normal")
    $ LocFlush()
    show mc at cleft
    show divine at cright_f
    "Come morning, Sister Divine awoke me with a gentle kiss as she dressed herself."
    DIVINE "Good morning, my beast."
    MC @smile "Morning."
    DIVINE "I'll let you go before most of the students rise from their beds."
    DIVINE "Come, get dressed and follow me."
    jump rom_divine_notfirsttime_leavetower
    
label rom_divine_notfirsttime_ishouldgo:
    DIVINE @sad "Hmm, what a shame."
    DIVINE "But if you must leave now, then so be it."
    DIVINE "Come, get dressed and follow me."
    jump rom_divine_notfirsttime_leavetower

label rom_divine_notfirsttime_leavetower:
    scene black with dissolve
    "After I was dressed, Sister Divine led me out of the tower as quietly as she could..."
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("divine", "normal")
    $ LocSet("novaras_dist_mage")
    $ LocEnter()