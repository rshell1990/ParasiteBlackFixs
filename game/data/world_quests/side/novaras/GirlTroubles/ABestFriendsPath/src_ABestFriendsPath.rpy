#################################################################################################################
#OPTIONAL SCENE 1 - IF PLAYER AGREES TO SPEAK TO MARKUS FOR MIKA- SCENE TRIGGERS AS PLAYER LEAVES THE TOWER OF PALAM 
label qst_a_best_friends_path_1:
    $ LocSet("novaras_dist_mage")
    "Stepping outside the tower, I approached Markus."
    $ LocFlush()
    show markus at cleft
    with dissolve
    show mc at cright_f with easeinright
    MC @talk "Markus, I need to speak to you about something."
    MARKUS @smile "Of course, friend, what was it?"
    MC @talk "If I said there was a young lady interested in meeting you, what would you say?"
    MARKUS @smile "I'd say you sly dog, what's the catch?"
    MC @talk "{i}*Cough*{/i} The lady in question is a mage of Palam."
    MARKUS @shock "A mage of Palam?!"
    MARKUS @sad "I ... I don't know, [player_name!t]."
    MARKUS @talk "If anyone found out I was having relations with one of them, I'd be made into a pariah."
    MC @think "I need your help with this, I know you mentioned finding them attractive before..."
    MARKUS @shock "Well, yes, of course!"
    MARKUS @smile "Everyone knows they can be quite beautiful."
    MARKUS @talk "But the risks involved with being with one... Not to mention, I know they have {i}both sets{/i} but, I'm not exactly sure about my partners also carrying swords like me!"
    MC @talk "I have permission to be in the tower at night; as long as you don't stray from the tower grounds, there's virtually no risk."
    MARKUS @talk "Hmmm ... And you're sure you need my help on this matter?"
    MC @talk "I do."
    MARKUS @talk "{i}*Sigh*{/i} Very well."
    MARKUS @talk "But you'll have to get me permission as well to come and go from the tower."
    MARKUS @smile "Unless you want to be chaperoning us all the time."
    MC @smile "Cute, but I'll leave the romantic stuff to you."
    MC @talk "I'll speak to the head Mage at the tower and see what can be done."
    MARKUS @talk "Let me know."
    scene black with dissolve
    $ LocSet("novaras_palam_mainhall")
    "Having explained the situation to Sister Divine, I hoped for the best."
    $ LocFlush()
    show mc at cleft
    show divine at cright_f
    with dissolve
    DIVINE @shock "Wait, what?!"
    show divine at shake
    DIVINE @angry "You understand the reason for the secrecy around this kind of thing, yes?"
    DIVINE @sad "... How do I know we can trust him?"
    MC @talk "He's like {i}me,{/i} he shares my ..."
    "The word is on the tip of my tongue, gift? {i}Curse?{/i}"
    MC @talk "{b}...Abilities.{/b}"
    DIVINE @angry "That doesn't mean he's-"
    DIVINE @sad "{i}*Sigh*{/i}"
    "Sister Divine rubbed her brow in frustration."
    DIVINE @talk "Do I have your word he will not mention anything about the inner workings of this tower?"
    MC @talk "You do."
    DIVINE @talk "Very well then, give your friend this."
    "Sister Divine handed me over a similar item as before."
    DIVINE @talk "It will grant him passage into the tower during the evenings, such as yourself."
    scene black with dissolve
    $ LocSet("novaras_dist_mage")
    $ LocFlush()
    show markus at cleft
    with dissolve
    show mc at cright_f with easeinright
    MC @talk "Here."
    "I handed over the small stone to Markus."
    MARKUS @talk "Huh? What's this?"
    MC @talk "It shall grant you passage to come and go from the tower of Palam as you wish."
    MARKUS @shock "Really?"
    MARKUS @smile "Very well, friend, what's this young lady's name? I shall call upon her."
    MC @talk "Her name is Mika."
    MARKUS @smile "Mika ... What a lovely name, don't worry, I shall call upon her soon."
    MARKUS @talk "Hopefully, we actually like each other."
    MC @smile "She's a sweet girl; I'm sure she'll be fawning over you."
    MARKUS @smile "We'll see about that."
    MARKUS @smile "Anyway, I'll let you know how things go!"
    hide markus with easeoutright
    show mc at center_f with ease
    MC "(I'll check in on Mika and Markus later when I have a chance.)"
    $ QstSetProgress(QstABestFriendsPath, 1)
    $ QstSetDelay(QstABestFriendsPath, 1)
    $ LocEnter()

label qst_a_best_friends_path_3:
    show markus at cright_f
    show mika at center
    with dissolve
    show mc at left with easeinleft
    "As I entered the main hall, Mika stood beside a smirking Markus, giggling at something he was saying."
    "As Mika saw me, she smiled and waved shyly."
    "Markus, noticing me, turned and smiled brightly in my direction."
    MARKUS @smile "Ah! [player_name!t]! Mika and I were just having a delightful conversation here."
    show mc at cleft with easeinleft
    "Mika giggled once again."
    MIKA @blush "Your um, friend is quite funny."
    "The two shared another chuckle as Markus turned to face me."
    MARKUS @smile "Thank you for introducing us, friend, {i}she's quite the interesting lady.{/i}"
    MARKUS @smile "Later, we should head to the {i}Iron Unicorn{/i} should you wish to grab a few rounds in."
    "Markus turned one last time towards Mika."
    MARKUS @smile "I look forward to seeing you again soon, Miss Mika."
    MIKA @blush "L-Likewise."
    "Markus smiled as he left to give Mika and me some alone time."
    MC @smile "So, you like him then?"
    MIKA @blush "He's very nice... Has nothing but praise when talking about you."
    MC @smile "He better be, or he might find his next ale ruined with some extra spice added."
    MIKA @talk "Mmm... So, I suppose it's my turn now to keep to my end of the bargain?"
    MC @talk "It is."
    "Mika nodded and lightly bowed, lifting her dress."
    MIKA @smile "I look forward to our next sparring session.."
    "Mika turned and left, seemingly pleased with my choice in picking Markus for her."
    show mika at blurin, center_f
    hide mika with easeoutleft
    MARKUS @talk "[player_name!t], a moment?"
    MC @talk "What is it, Markus?"
    show markus at center_f with easeinright
    MARKUS @talk "That girl, Mika..."
    MARKUS @smile "If you're interested in having fun with her, you only need to ask."
    MC @think "You say that now, but what if you end up falling for her?"
    MARKUS @smile "Haha, we'll see about that."
    MARKUS @talk "But with our, {i}*Cough*{/i} 'conditions,' should the need arise, I'd rather choose that than have you dying on me."
    MARKUS @think "Though, I must ask ... What made you turn her offer down and seek me out?"
    menu:
        "I'm simply not interested in her that way.":
            MARKUS @talk "Hmm... Fair enough, I suppose."
        "I have my eyes set on another girl.":
            MARKUS @smile "Bloody romantic."
        "Given my task, it could land me in trouble if it was seen I was taking advantage.":
            MARKUS @think "Hmm, it makes sense to be cautious."
    MARKUS @smile "Regardless, don't let me stop you from having fun with her should you change your mind."
    MC @think "Hmm ... I'll give it some thought."
    $ QstSetProgress(QstABestFriendsPath, 2)
    $ LocEnter()

##################################################################################################################
label qst_a_best_friends_path_4:
    show mika at center_f with dissolve
    MIKA @smile "N-No more light sparring!"
    "Mika clenched her fists and raised them confidently to her chest."
    MIKA @smile "I can do this!"
    menu:
        "{image=[ICON.SWORDS]} Let's do this!":
            "L-Let's go!"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            scene black with dissolve
            $ AutoMus(True)
            $ LocFlush()
            show mika at center
            with dissolve
            if LastBattleOutcome == "defeat":
                MIKA @smile "I did it! I won!"
                MIKA @smile "I can't believe I actually won!"
                MC @smile "Ahh... Well done, Mika."
            elif LastBattleOutcome == "victory":
                MIKA @scared "{i}*Huff* ...*Huff*{/i} "
                MIKA @scared "So ... {i}*Huff*{/i} close!"
                MC @smile "You did very well, Mika."
            MIKA @smile "T-Thank you... [player_name!t]."
            MIKA @blush "I umm..."
            MIKA @blush "M- Markus plans to come here later to spend some time."
            MIKA @blush "H-He says he's just bringing some wine for us to s-share, but..."
            MC @think "{i}But...?{/i}"
            MIKA @blush "I-I'm kinda nervous he's expecting more; what should I do?"
            MC @talk "Whatever you want to do, Mika, I'm sure Markus won't force you to do anything you don't want to."
            MIKA @shock "N-No! I..."
            MIKA @blush "I {i}want{/i} to do stuff with him; it's just, I don't know how to approach him."
            menu:
                "Just be yourself, Mika, you'll be fine.":
                    MIKA @blush "A-Alright, if you say so..."
                "Just drop to your knees; that should do it.":
                    MIKA @shock "{i}*Gulp*{/i}"
                    MIKA @blush "J-Just drop to my knees?"
                    MIKA @blush "A-Alright, I'll think on your advice."
            #Both choices continued
            MIKA @talk "Well, I'd better go get ready for the evening."
            MIKA @talk "And [player_name!t]."
            MIKA @smile "Thank you for introducing me to Markus."
            MIKA @blush "H-He's quite sweet when you get to know him."
            MC @smile "May the gods smile upon you both."
            show mika at blurin, center_f
            hide mika with easeoutleft
            "With a skip in her step, Mika hurried off to prepare for her evening with Markus."
            $ QstSetProgress(QstABestFriendsPath, 3)
            show mc at center_f with easeinright
            MC "(Hm... Perhaps I should check on the two of them later?)"
            MC "(See how they're getting on.)"
            hide mc with easeoutleft
            $ LocEnter()
            # check up on mika and markus at evening. the timeframe should be TIME_DUSK TIME_LATENIGHT
            # they should be 'somewhere in the tower', trigger on eastern wing

        "I have some other business I need to attend to first.":
            MIKA @talk "I see; well, let me know when you are free."
            $ LocEnter()

##############################################################################################################################
# Scene 5 - Tower of Palam -corridor hallway - Evening
# Quest log: I should check in with Mika and Markus this evening at the tower of Palam. 
# Scene triggers when entering into eastern wing
label qst_a_best_friends_path_5:
    show mc at center with easeinleft
    $ PlaySexFx("audio/sex_sounds/reginamasturbate_loop_fade.ogg", 1)
    MIKA "Mhmm...! ❤️"
    MARKUS "{i}*Groans*{/i}"
    "Faintly, I could hear the sounds of Mika and Markus' moans and grunts from the other side of the women's living quarters."
    MC "(Well... I suppose the two of them are getting on fine.)"
    MC "({i}...Hmmm.{/i})"
    MC "(Should I?)"
    menu:
        "Peek through the door.":
            scene black with dissolve
            $ StopSexFx()
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            scene mika_markus_bj_stroke_slow
            with dissolve
            $ Pause()
            "Gently pushing open the door to the girls' dorm, Markus is sat naked on a chair, a nearly empty bottle at his side as Mika kneels naked between his legs."
            $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
            scene mika_markus_bj_loop_slow
            with dissolve
            $ Pause()
            "Her head bopped up and down as he grabbed a hold of her pigtails with his fist, guiding her head."
            "Lewd slurping sounds escaped from Mika's mouth as she undoubtedly pleasured his member, obscured from my view."
            MIKA "{i}*Slurp!* *Slurp!*{/i}"
            MIKA "Mhmmmm...{i}*Slurp*{/i}"
            scene mika_markus_bj_loop_fast
            with dissolve
            $ Pause()
            MARKUS "Ahhh!!"
            MARKUS "That's it, Mika!"
            MARKUS "Tell me how you love that cock, girl!"
            scene mika_markus_bj_stroke_fast
            with dissolve
            $ Pause()
            MIKA "Mhmm! Ilhuvv yhourrr bhiggh chockk! {i}*Slurp!*{/i} ❤️"
            scene mika_markus_bj_loop_fast
            with dissolve
            $ Pause()
            MARKUS "Oooh! That's it!"
            MARKUS "My - Ahh! slutty little mage! Hrghhh!"
            "As he continued to push Mika's head down, his eyes briefly glanced over to meet mine, and he smirked."
            "With a wave of his other hand, it appeared he was inviting me in..."
            menu:
                "Enter.":
                    jump qst_a_best_friends_path_5_join

                "Refuse Markus' offer.":
                    "With a shake of my head and wave of my hands, Markus returned to focusing solely on Mika as I slipped back out into the hallway."
                    MC @smile "(Well... Looks like Mika had nothing to worry about.)"
                    $ StopSexFx()
                    $ AutoMus(True)
                    $ QstSetProgress(QstABestFriendsPath, 4)
                    $ LocEnter()

        "Don't peek through the door.":
            "I decided it was probably best to give the two of them their privacy."
            MC "(Hm, hopefully Mika will be in a good mood to continue her training tomorrow.)"
            $ QstSetProgress(QstABestFriendsPath, 4)
            $ LocEnter()

label qst_a_best_friends_path_5_join:
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    
    $ LocSet("novaras_palam_dorm")
    $ StopSexFx()
    $ CharSetClothes("mika", "naked")
    $ CharSetClothes("markus", "naked")
    $ LocFlush()
    show mika at center
    show markus at cright_f
    with dissolve
    show mc at cleft with easeinleft
    
    "As I opened the door and entered inside, Mika abruptly stopped what she was doing upon hearing the door swinging open."
    
    hide mika
    show mika at blurin, center_f, shake
    
    MIKA @shock "[player_name!t]!"
    MIKA @shock "I- I...!"
    MIKA @shock "W-We were just-"
    MARKUS @smile "Relax, Mika."

    hide mika
    show mika at blurin, center

    MARKUS @smile "It seems my friend here caught a glimpse of your ass and just couldn't resist."
    MIKA @blush "You... But I thought you didn't-"
    MARKUS @smile "Mika, there's no need to overthink things so much."
    MARKUS @talk "[player_name!t]'s very busy, but..."
    "Markus grinned."
    MARKUS @smile "I'm sure he could make time for the occasional bit of fun."
    MARKUS @smile "That is if you're interested."
    MIKA @shock "Y-You BOTH want to-"
    MIKA @shock "{i}W-With me?{/i}"

    hide mika
    show mika at blurin, center_f

    MIKA @sad "I... I didn't think you'd actually {i}wanted{/i} me like that."
    MC @talk "My life is lived by the day; it wouldn't be in your interests to get too attached to me like that."
    MC @smile "But... We {i}could{/i} still have some fun if you wish."
    MIKA @blush "...C-Can you take your clothes off first?"

    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("mc", "naked")
    show mc at nod

    "Smirking, I stripped down naked and stood beside Markus."
    "Mika, eyes wide and cheeks burning red, twirled one of her pigtails with her finger as her eyes darted between us."
    
    hide mika
    show mika at blurin, center

    MIKA @shock "...{i}Oh my.{/i}"
    "Mika gently bit down on her lower lip."
    MIKA @blush "W-Well, if you both need me {i}that much.{/i}"
    MIKA @blush "U-Umm, I'm sure I c-could help you both if that's what you want..."    
    "Mika licked at her lips as she stared at the two dangling cocks in front of her."
    scene black with dissolve
    "...On her knees, with our cocks in both of her hands Mika was trembling with burning lust."

    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mika_double_bj_left_stroke_slow 
    with dissolve
    $ Pause()

    MIKA "S-So thick..."
    MIKA "So big..."
    MIKA "Mhmmm!"
    MARKUS "Ahhh! That's it, girl! Hrghh! Stroke our cocks!"
    MC "{i}*Grunts*{/i} Good girl, Mika..."

    scene mika_double_bj_right_stroke_slow 
    with dissolve
    $ Pause()

    "Mika's eyes briefly pulled away from the thick cocks in front of her to meet my eyes."
    MIKA "Mmm, will you review my progress here, too?"
    MC "That depends..."
    MC "{i}On how much you please us.{/i}"
    "Mika smiled before dipping her head forward onto my cock, wrapping her lips around it whilst she continued to stroke Markus."

    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
    scene mika_double_bj_right_suck_slow 
    with dissolve
    $ Pause()

    MC "Ahhh...!"
    MIKA "{i}*Slurp* *Slurp...*{/i}"
    MIKA "Mmmm, shoo bhigghh...❤️"
    MIKA "I chann bharleyhh fhithh ithhh inhh mhyhh mhouthh! {i}*Slurp!*{/i}"
    "Mika's head continued to gently move back and forth as she tried to take as much of my cock as she could."
    "Her head rocked forward, her sweet, wet lips gliding over my now glistening cock thanks to her saliva, her tongue nervously explored my cock, rubbing and wrapping against it."
    "With a loud *PLOP* sound, she smiled as she pulled her lips away from my member."
    
    scene mika_double_bj_right_suck_slow 
    with dissolve
    $ Pause()

    MIKA "{i}*Huff*{/i} Did I - {i}*Huff*{/i} pass your review?"
    MC "Mmm, a great start."
    MC "But I'm going to need to see more before I can tell you if your cock sucking skills are to my standards!"
    MARKUS "Allow me to assist!"
    "With a light pulling of Mika's head, she giggled as she wrapped her lips now around Markus' cock, sucking and dragging her lips down as she stroked my member."

    scene mika_double_bj_left_suck_slow
    with dissolve
    $ Pause()

    MIKA "{i}*Slurp!* *Slurp!*{/i} Mhhfhh!"
    MARKUS "Ahh! That's it, Mika!"
    MARKUS "Tell us how you love sucking our big cocks!"
    MIKA "Mhhfhh! Ihh Lhuvhhh {i}*Slurp!*{/i} shuckinghhh yhourhhh - Mhmmm! - bhighhh chockhhs! {i}*Slurp!*{/i} ❤️"
    "Mika's lips continued to glide over Markus's cock, coating it in her saliva as she tried to swallow as much of his {i}sword{/i} as she could."
    "Her hand continued to stroke at my cock whilst Markus groaned happily as her sweet mouth worked its magic on him."
    "After a few moments passed though, Mika's lips pulled away from Markus' cock, and she was giggling as she continued to stroke both of us once more."

    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mika_double_bj_right_stroke_slow
    with dissolve
    $ Pause()

    MIKA "{i}*Huff*{/i} W-what's a Palam mage to do?"
    MIKA "I'm - {i}*huff*{/i} s-sure Palam will understand! Fufu! ❤️"

    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
    scene mika_double_bj_left_suck_fast
    with dissolve
    $ Pause()

    "Mika's head moved from cock to cock, sliding down our members as she gagged and lightly choked on each one."

    scene mika_double_bj_right_suck_fast
    with dissolve
    $ Pause()

    "Her tongue thrashed and beat against each member as she fully became absorbed in her lust, her nervous nature seemingly numbed and vanished into nothing."
    "Instead, me and Markus were being serviced by a ferocious succubus, determined to suck us dry."

    scene mika_double_bj_left_suck_fast
    with dissolve
    $ Pause()

    MIKA "Ahhh! It's shooo ghood! Mhhhfh! I love it!"
    MIKA "I lhuvvhh yhourhhh chockkkss sliding dhownn my throattt shoo much!! ❤️"
    MIKA "Ghivhhh ithh to mheee!"

    scene mika_double_bj_right_suck_fast
    with dissolve
    $ Pause()

    MIKA "Cover yourhh little mage whore in all your seed!"
    MIKA "Make me beg for itthhh! ❤️"
    MARKUS "Oh godsss! Hrghhh! I'm... I'm going to finish!"
    "As I felt my balls begin to tighten and rise, I knew from my aching, now desperately sensitive cock, I was close to finishing as well."
    MC "M-Me too!"
    "Mika pulled back, opening out her mouth and letting her tongue flop out as she stroked the two of us enthusiastically."
    MARKUS "O-OOOH! FUCK!"
    MC "H-HRGHHHH!"
    "Unable to hold back any longer, I grunted loudly as I unleashed my hot load onto Mika's face and tongue."

    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")

    scene mika_double_bj_finish
    with flash
    $ Pause()

    $ ReduceInfectionFromSex("mika")
    $ UnlockGalSceneAndGrantXp("mika", "mika_double_bj")

    "Markus finished only a moment or two later, plastering Mika with another burst of his seed."
    "Mika, drunk on lust, continued to giggle and stroke us, making sure she'd thoroughly drained us for every last drop."
    "As the seed dripped down from her face onto her tits, her tongue swirled around her mouth to swallow as much of the seed as she could."
    MIKA "Mmm... You both taste so..."
    MIKA "Delicious. ❤️"
    MARKUS "Ahh... Mika and I are going to head to the baths and clean ourselves."
    MARKUS "I'll re-join you shortly once I'm clean."

    scene black with dissolve
    "As Mika rose to her feet, Markus playfully reached out to slap her butt."
    $ LocFlush()
    show mc at cleft
    show mika at center_f
    show markus at cright_f
    with dissolve

    MIKA "Eeeep!"
    MARKUS "Move your cute ass, girl!"
    MIKA "Mhmm, y-yes sir..."
    hide mika 
    hide markus
    with easeoutleft
    show mc at blurin, cleft
    show mc at center_f
    with ease
    show mc at blurin, center_f
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("mc", "normal")
    show mc at nod
    "As the two of them left to head towards the baths, I re-dressed myself, heading out to carry on with the remainder of my evening."
    $ CharSetClothes("markus", "normal")
    $ CharSetClothes("mika", "dress")
    $ AutoMus(True)
    $ QstSetProgress(QstABestFriendsPath, 4)
    $ LocEnter()

##############################################################################################################################################
#Scene - 6 - Mika can be found in the training yard again - Morning - learning event 2 
#Markus romance route 
#scene begins as player selects on Mika 
label qst_a_best_friends_path_6:
    show mika at center_f with dissolve
    MIKA @smile "H-Hello again..."
    MIKA @talk "Are you ready for our next sparring sessions?"
    menu:
        "{image=[ICON.SWORDS]} Let's begin.":
            MIKA @talk "R-Right..."
            "Mika seemed unusually anxious, as though her mind was clearly elsewhere."
            MC @think "Mika? Is everything alright?"
            MIKA @blush "Y-Yes."
            "Mika's eyes seemed to dart around anywhere but look me in the eye."
            MC @think "...Mika."
            MIKA @talk "H-Hm?"
            MC @talk "Is something on your mind?"
            MIKA @shock "N-No!"
            "She paused sheepishly."
            MIKA @talk "P-Perhaps I was hoping we might finish sparring a little earlier today?"
            MIKA @blush "It's just, um... Me and Markus-"
            MC @smile "Sparring first, then I'll let you off the hook."
            MIKA @talk "R-Right."
            "Mika took her position and faced me."
            MIKA @talk "I'm ready!"
            MC @talk "Good."
            MC @angry "BEGIN!"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            $ LocFlush()
            show mc at cleft
            show mika at cright_f
            with dissolve
            $ AutoMus(True)
            if LastBattleOutcome == "victory":
                MIKA @talk "{i}*Huff!* *Huff!*{/i}"
                MIKA @sad "Damn it."
                MC @talk "You did well today, regardless, Mika."
                MIKA @smile "Y-You really think so?"
            elif LastBattleOutcome == "defeat":
                MIKA @smile "I did it! I won!"
                MC @smile "Well done, Mika, you continue to improve."
                MIKA @shock "Y-You really think so?"
            MC @smile "Yes, it won't be long till I think I can say you won't need any more sparring sessions from me."
            MIKA @shock "I won't?"
            MC @talk "No... I don't think it'll be long before it's safe to say you'll be alright."
            MC @talk "At least, Sister Divine won't have to worry about you being unable to defend yourself."
            "My words seemed to resonate with Mika, who wiped away a stray tear forming in her eye."
            show mika at nod
            MIKA @sad "...I won't let you down."
            MC @smile "Go on now, don't keep Markus waiting."
            MIKA @smile "Y-Yes sir!"
            show mika at blurin, cright
            $ Pause(0.1)
            hide mika with easeoutright
            "Mika hurried off, no doubt excited for whatever she and Markus had planned."
            show mc at center with ease
            MC "(I wonder how their relationship... Progresses?)"
            $ QstSetProgress(QstABestFriendsPath, 5)
            $ LocEnter()

        "Not right now.":
            MIKA @talk "Very well, let me know, I guess..."
            $ LocEnter()
    
######################################################################################################################################################
# Scene 7 - Tower of Palam hallway - Evening
# Scene triggers when entering into the corridor hallway
label qst_a_best_friends_path_7:
    show mc at center with easeinleft
    $ PlaySexFx("audio/sex_sounds/forgean_100_muffled.ogg", 1)
    "Once more, whilst making my way through the hallways in the tower of Palam, I heard Mika's loud moans coming from the girls' quarters."
    "Accompanied by the sounds of flesh slapping, I could smell the sex from here."
    MIKA "Ahhhh...! ❤️"
    "{i}*Plap!* *Plap!* *Plap!*{/i}"
    MARKUS "{i}*Groans*{/i}"
    MARKUS "Gods girl, are you tight!"
    MC "(Those two are at it like rabbits again...)"
    MC "({i}...Hmmm.{/i})"
    MC "(Should I?)"

    
    
    menu:
        "Peek through the door.":
            scene black with dissolve

            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")

            $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)

            scene mika_missionary_nopreg_vag_fast with dissolve
            $ Pause()

            MIKA "Hrhghh! Y-Yesshh! Mhmm!"
            MIKA "You're messing up m-my insides so much!"
            "With her legs parted wide for him, Markus pushed his cock deep into her tight hole, drawing euphoric cries from Mika."
            "Her snug pussy greedily swallowed his thick length as she looked up at him lovingly, one hand resting atop her breast."
            "Markus pounded into her with abandon, treating her body like his personal toy."
            MARKUS "F-Fuck! Are all mages of Palam like you?!"
            MIKA "Nghhhh! Mhmm! W-We're all so f-fucking horny, all the time!"
            MIKA "Slam your cock into me—mhmm!"
            MIKA "M-Make me your little mage bitch!"
            "From the doorway, Markus glanced over and caught sight of me watching."
            "Mika was far too preoccupied, holding her legs up in the air for his member, to notice much of anything."
            "Markus smirked and gave a beckoning wave."

            menu:
                "Head inside.":
                    jump qst_a_best_friends_path_7_join

                "Shake your head.":
                    "Refusing Markus' offer, he nodded in acknowledgement before turning his focus entirely back onto Mika."
                    MIKA "Oooooh! D-Daddy... Mhmm..."
                    MIKA "Don't stop! ❤️"
                    "The loud moans and sounds of flesh slapping continued to fill the hallway for some time, I imagine..."
                    "As I stepped away from the scene, I left them to it, deciding I would speak to Mika in the morning."
                    $ StopSexFx()
                    $ AutoMus(True)
                    $ QstSetProgress(QstABestFriendsPath, 6)
                    $ LocEnter()

        "Don't peek through the door.":
            "I decided it was probably best to give the two of them their privacy."
            MC "(Hm, hopefully Mika will be in a good mood to continue her training tomorrow.)"
            $ QstSetProgress(QstABestFriendsPath, 6)
            $ LocEnter()

label qst_a_best_friends_path_7_join:
    ##########################
    $ PlaySoundRandom("woodenDoor")
    $ LocSet("novaras_palam_dorm")
    "At his invitation, I stepped into the room and shut the door behind me." 
    MARKUS "Come here."
    MARKUS "It's time for a change of position!" 
    $ StopSexFx()
    MIKA "Wait, what are you—" 
    $ CharSetClothes("mika", "naked")
    $ CharSetClothes("markus", "naked")
    $ LocFlush()
    show markus at cright_f
    show mika at center
    with dissolve

    MIKA "Eeeeep!"
    show mc at left with easeinleft
    "Hoisted up into Markus' arms, his cock plunged deep inside her once more."
    "She gasped, instinctively wagging her blue ass toward me." 
    MIKA "Oh Palam, YES!" 
    "Mika, now locked in Markus' firm grip, squirmed slightly when she finally noticed me entering." 
    MIKA "W-Wait a minute?! M-Markus! What's he—" 
    MARKUS "He's here to join in on our fun, of course." 
    "Markus flashed a wide grin as Mika's cheeks flushed crimson, her eyes fixed on me as I stripped." 

    $ CharSetClothes("mc", "naked")
    $ PlaySoundRandom("tentFlap")

    show mc at blurin, nod

    MIKA "Y-You want me to t-take you and [player_name!t]?!" 
    MARKUS "Don't feel—ahh!—up to it?" 
    MIKA "Oh gods, my heart is beating so fast...!" 
    MIKA "I—I didn't say I wouldn't!" 
    MIKA "Mhmm! B-But doesn't that mean he's going to put it in my—"

    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mika_threesome_dp_loop_slow 
    with dissolve
    $ Pause()

    "As I pushed the head of my cock against her tight rosebud, Mika's ass quickly gave way as she felt my cock stretch it out."
    MIKA "M-MY ASSSSSSHHH!!"
    "Mika howled in a mixture of pleasure and pain as she felt the two huge cocks stuff both of her holes."
    "Her tight, back tunnel squeezed my cock desperately."
    "Her body was immediately overwhelmed by the two huge cocks now sliding in and out of her stretched, defiled holes."
    MIKA "{i}*Huff*{/i} I luhvhh yhouuu! I lhuvvv yourhh chockkhhss!! {i}*huff*{/i}"
    "Mika's insides felt amazing, wedged between me and Markus; we treated her body like some kind of toy, mercilessly ramming our cocks into her drenched holes."
    MARKUS "Hrghh! Your pussy feels like it was built for my - Ahh! Cock!"
    MARKUS "How's her ass feel, [player_name!t]?"
    MC "H-Hrghh! She's - Mhmm! T-Tight!"
    MC "Her ass feels like it's - Ahh! Moulding around my cock!"
    MARKUS "Haha! Hear that slut?"
    MARKUS "Keep shaking that ass!"

    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)
    scene mika_threesome_dp_loop_fast 
    with dissolve
    $ Pause()

    MIKA "Mhhfhhhhhhhh....!! ❤️"
    "Mika seemed almost delirious, her eyes rolling to the back of her skull as she did as she was told, shaking her little blue ass on command."
    MIKA "F-Feel so - Mhhfhhh!"
    MIKA "S-Stuffed! ❤️"
    "Mika's tongue flopped out of her mouth as the two of us continued slamming our cocks into her."
    "Her tight holes squeezed and convulsed, seemingly as Mika experienced wave after wave of her own climaxes."
    "Her toes curled as she slurred out her lewd, desperate moans."
    MIKA "C-Cummmhh inhhh mheee!"
    MIKA "F-Fhill mheee uphh likeee ahhh whoreee!! ❤️"
    MARKUS "Grghh! You heard her! Ahh!"
    MARKUS "I-I'm close! I'm gonna..."
    "Markus grunted, tightening his grip around Mika as he flooded her womanhood with his load."
    "Mika's sudden gasp and tightening around me as she shook with a powerful orgasm was enough to tip me over the scales as well."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    scene mika_threesome_dp_finish
    with flash
    $ Pause()

    $ ReduceInfectionFromSex("mika")
    $ UnlockGalSceneAndGrantXp("mika", "mika_threesome")

    "With a grunting, animal-like 'Hrghhh!' sound, I poured my own thick, hot load into Mika's rectum."
    MIKA "A-Ahhhhhhh...! ❤️"
    "Mika shivered and trembled as we did so, her stomach lightly bulging from the sheer volume of cum being pumped into her."
    MIKA "G-Ghhhh!!"
    MC "Hrghh! T-Take it all, Mika!"
    "Eventually, with every last drop pumped into Mika, drenched in sweat, we slowly lowered Mika back onto the floor." 

    scene black with dissolve
    "Her feet touched the ground, but in a moment, she collapsed onto her back, our cum seeping from both her holes. "
    MC "Mika!"

    $ CharSetClothes("mc", "naked")
    $ CharSetClothes("markus", "naked")

    $ LocFlush()
    show mc at cleft
    show markus at cright_f
    with dissolve

    MIKA "F-Fine... {i}*Huff*{/i} Just n-need... {i}*Huff*{/i}"
    MIKA "...Rest."
    "Markus' eyes looked up to meet mine."
    MARKUS "...Wanna grab some ale over at the Iron Unicorn?"
    MC "Sure."
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("markus", "normal")
    $ CharSetClothes("mika", "dress")
    "The two of us got dressed and left a quivering, content Mika on the floor."
    MIKA "M-Mmm... ❤️"
    $ AutoMus(True)
    $ QstSetProgress(QstABestFriendsPath, 6)
    $ LocEnter()

###############################################
#Scene 8 - Training yard - Morning 
#Mika can be found once again waiting for the MC - Upon selecting 
label qst_a_best_friends_path_8:
    show mika at center_f with dissolve
    MIKA @talk "I hope you're ready!"
    menu:
        "{image=[ICON.SWORDS]} Let's do this!":
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            $ LocFlush()
            show mc at cleft
            show mika at cright_f
            with dissolve
            $ AutoMus(True)
            if LastBattleOutcome == "victory":
                MIKA @talk "{i}*Huff!* *Huff!*{/i} How did you - {i}*Huff*{/i} move so fast?"
                MC @smile "{i}Training.{/i}"
                MIKA @talk "{i}*Huff*{/i} Figures..."
            elif LastBattleOutcome == "defeat":
                MIKA @smile "I - {i}*Huff*{/i} did it!"
                MC @smile "Well - {i}*Huff*{/i} done, Mika."
            MIKA @talk "...I was thinking we could celebrate."
            MC @smile "Celebrate?"
            MIKA @smile "You're nearly done training me, right?"
            MIKA @smile "I feel so much more alive now, and-"
            "Mika paused, blushing as she grabbed a hold of both of her arms."
            MIKA @smile "I just haven't been this happy in a long t-time and-"
            MIKA @smile "{i}I wanna spend some time with Markus.{/i}"
            MC @smile "Very well, Mika."
            "Mika pondered the thought for a moment."
            MIKA @smile "T-Tomorrow, perhaps you'd like to meet me and Markus at the Iron Unicorn!"
            MC @think "Me?"
            MC @talk "I'd hate to spoil your date..."
            MIKA @shock "O-Of course you wouldn't!"
            MIKA @smile "It's just... I want to celebrate andddd..."
            MIKA @smile "I guess I'd like you both there if that's alright?"
            MC @smile "If that's what you wish."
            MIKA @smile "Great! We'll all have s-so much fun!"
            show mika at blurin, cright
            $ Pause(0.1)
            hide mika with easeoutright
            "With a skip in her step, Mika hurried off to prepare for her date with Markus."
            show mc at center with ease
            MC "(Well, a night of drinking with Mika and Markus should be fun...)"
            $ QstSetProgress(QstABestFriendsPath, 7)
            $ LocEnter()

        "Not yet; I have some things I need to take care of first.":
            MIKA @talk "Mmm, stalling huh?"
            MIKA @talk "Fine, I can wait!"
            $ LocEnter()

######################################################################################################################################################
# Scene 9 - Iron Unicorn - Evening 
# happens on enter
label qst_a_best_friends_path_9:
    show markus at right_f
    show mika at cright_f
    with dissolve
    MIKA @smile "[player_name!t]! Over here!"
    show mc at cleft with easeinleft
    MARKUS @smile "Ah! There you are, friend!"
    MARKUS @smile "I'll get you ale, come join us!"
    MIKA @smile "M-Markus and I grabbed us a table."
    scene black with dissolve
    $ TimeAdvBy(TIME_2H)

    "...After ordering our food, Mika spent the evening smiling, laughing at many of Markus' jokes, and generally being in high spirits."
    MIKA "I - I just wanted to thank you both for everything you've done for me."
    MIKA "I... I was thinking, m-maybe that-"
    DRUNKARD "{i}Disgusting.{/i}"
    $ LocFlush()
    show cg_drunkard_dark at left_f:
        yoffset 80
    show markus at right_f
    show mika at cright_f
    show mc at center
    with dissolve
    $ Pause(0.1)
    show mc at blurin, center_f
    "The drunkard glared down at us."
    DRUNKARD "What the hell are you two lads doin' with a mage of Palam?"
    DRUNKARD "She shouldn't be ere!' She should be in that tower!"
    show mika at shake
    MIKA "T-They're my friends! They're here to keep me safe!"
    DRUNKARD "Tsch! You had yer hand on the blonde one's lap!"
    DRUNKARD "What's he done to ya?"
    MIKA "N-Nothing! We're just enjoying a meal!"
    DRUNKARD "Standards are slippin' these days..."
    DRUNKARD "In my day, we'd never see any of you lot leave those towers!"
    DRUNKARD "And we were better for it!"
    DRUNKARD "You mages can't help yerselves; we all know that!"
    DRUNKARD "That's why you gotta stay put!"
    DRUNKARD "What kinda freak would want one of you anyway?"
    "I rose from my seat, but before I could act, Markus had already lunged across from the table to slam his fist into the drunkard's face."
    show markus at blurin, cleft_f with easeinright
    play sound "audio/cfx/duprey_headbutt.ogg"
    show markus at shake
    show cg_drunkard_dark:
        parallel:
            easeout 0.6 rotate -90
        parallel:
            easein 0.6 xcenter 0.1 yoffset 200
    "With one sharp punch, the man went hurdling backwards, his back slamming against the opposing table; he dropped to the floor."
    "The drinks on the table spilled and knocked over as the people rose from their seats."
    show markus at shake
    MARKUS @angry "There's your fucking 'standards' cunt!"
    CUSTOMER "For fuck sake!"
    CUSTOMER_2 "The fucking drinks went everywhere!"
    MIKA @sad "I-"
    show mika at blurin, cright
    CUSTOMER "Can't you just leave?"
    CUSTOMER "Your kind shouldn't even be here!"
    show mika at blurin, cright_f
    MIKA @cry "I... I'm not..."
    hide mika with easeoutleft
    "With tears in her eyes, Mika bolted for the door."
    $ PlaySoundRandom("woodenDoor")
    MC @surprised "Mika!"
    "With the whole tavern's attention now firmly on Markus and me, the barmaid, Shay, hurried over to intervene before the place turned into a full-blown brawl."
    show shay at cright with easeinleft
    SHAY @talk "I'll sort the drinks out."
    show mc at blurin, center
    SHAY @talk "Just go..."
    "Deciding it was best not to argue, I followed Shay's advice."
    show mc at blurin, center_f
    MC @angry "Markus, we need to leave."
    MARKUS @angry "..."
    show mc at shake
    MC @angry "Markus!"
    MARKUS @angry "I'm leaving..."
    hide markus with easeoutleft
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    show mika cry at cright
    with dissolve
    "Outside the tavern, I found Mika making her way back to the tower of Palam, wiping her eyes clean of the tears."
    show mc at cleft with easeinleft
    MC @surprised "Mika! Hold on!"
    show mika at blurin, cright_f
    MIKA @cry "You've seen how it is..."
    MIKA @cry "It's always like this for us!"
    MIKA @cry "And worse, they don't even blame {i}us,{/i} it's like we're not even real people!"
    MIKA @cry "All they do is push away everyone who tries to get close to us!"
    MIKA @cry "We {i}all{/i} feel invisible."
    MIKA @cry "Every single one of us!"
    MC @sad "I'm sorry for what happened back there."
    show mika cry at blurin, cright
    MC @sad "...You're not invisible, Mika."
    show mc at center with ease
    MC @sad "{i}I see you.{/i}"
    MIKA @sad "...I ... I need to go home and think."
    show mika cry at blurin, cright_f
    MIKA @sad "Don't follow me, please."
    MIKA @sad "I've had enough eyes staring at me as it is."
    show mika cry at blurin, cright
    $ Pause(0.1)
    hide mika with easeoutright
    $ Pause(0.1)
    show markus at left with easeinleft
    MARKUS @sad "I'll follow from a distance to make sure she gets home safe."
    show mc at nod
    MC "Good idea."
    MARKUS @sad "{i}*Sigh*{/i} What a waste of a good night..." #Markus exits off-screen
    hide markus with easeoutright
    MC "(I'll check in on her tomorrow.)"
    MC "(Damn...)"
    $ QstSetProgress(QstABestFriendsPath, 8)
    $ LocEnter()

######################################################################################################################################################
#Scene 10 - Mika approaches MC in the daytime (except dusk/evening) when he enters the tower of Palam ANY hall/wings except the gardens (because time might fuck it up)
label qst_a_best_friends_path_10:
    show mc at center with easeinleft
    show mika sad at cleft with easeinleft
    MIKA @sad "H-Hello."
    show mc at blurin, cright_f with ease
    MC "Mika? What is it?"
    MIKA @sad "I need to talk with you about something in private."
    MIKA @sad "Could ... Could you follow me to the gardens please?"
    MC @talk "Of course, Mika."
    hide mika with easeoutright
    show mc at blurin, cright
    MC "(I wonder what is that all about?)"
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("novaras_palam_garden")
    $ LocFlush()
    show mika sad at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MIKA @sad "I ... after what happened that night."
    MIKA @sad "I thought about a lot of things... A lot of things I could have done better."
    MIKA @sad "...I wrote a letter."
    MC @think "A letter?"
    MC @talk "What kind of letter?"
    MIKA @sad "To the families."
    "Mika's hands tightened into balls of fists that she squeezed."
    MIKA @sad "I wanted them to know what happened, I wanted-"
    MIKA @cry "I wanted to tell them I was sorry for failing my friends back then."
    MC @sad "...Mika."
    DIVINE "You never failed your friends, Mika."
    show mc at blurin, cleft_f
    show divine at left with easeinleft
    "Mika gasped in shock as Sister Divine stepped into the light from the stairway behind us."
    MIKA @shock "S-Siter Divine!"
    show divine at center with ease
    show mc at blurin, cleft
    DIVINE @sad "It saddens my heart greatly that you never felt you could share the weight of such a burden with me."
    MIKA @shock "H-How do you know?"
    DIVINE @sad "Zara, after your argument with her, came to my office."
    DIVINE @sad "She told me everything about the promise you girls had made to keep things a secret."
    "Tears began to sting Mika's face as she was overwhelmed with emotion."
    MIKA @sad "I ... I ..."
    "Dropping to her knees, Mika began to sob openly as Sister Divine gently rubbed at her back."
    show mika cry at shake
    MIKA @cry "I hate myself! I HATE MYSELF SO MUCH!"
    MIKA @cry "They were my friends!"
    "Her scratched voice broke and began a high-pitched, desperate cry."
    MIKA @cry "... I failed them! I failed them all!"
    DIVINE @sad "Mika! It's alright, Mika!"
    "Sister Divine began to cradle Mika's head, pulling her into an embrace."
    DIVINE @sad "No one blames you, you silly girl."
    DIVINE @sad "For god's sake, Mika."
    DIVINE @sad "Why did you never say? Were you so afraid I would yell at you?"
    MIKA @cry "I was afraid I'd only disappoint you again."
    "Her words seem to have struck a chord with Sister Divine, whose mouth opened to say something, but instead. she chose to simply embrace the girl once again."
    DIVINE @sad "You foolish, foolish girl..."
    "Sister Divine wiped away Mika's tears with her sleeve."
    DIVINE @sad "You have never been a disappointment to me, Mika."
    DIVINE @sad "You, nor any of the other girls."
    "Mika didn't answer; she bowed her head ashamedly to the floor, still sniffling."
    DIVINE @sad "We'll speak of this again, just the two of us, do you understand?"
    "Mika nodded lightly."
    DIVINE @sad "Return to the girl's dorm, Mika."
    "Mika looked up sheepishly towards me."
    MIKA @sad "T-Tomorrow..."
    MIKA @shock "I won't let you down! I promise!"
    hide mika with easeoutleft
    show divine at blurin, cright_f with ease
    show mc at blurin, cleft_f
    MC @talk "...Will the families ever receive those letters she wrote?"
    DIVINE @think "No."
    show mc at blurin, cleft
    DIVINE @think "To let them out would risk another scandal we can't afford."
    "Sister Divine tilted her head towards me, her eyes meeting mine."
    DIVINE @think "{i}And Mika must never know that the letters never arrived.{/i}"
    "Understanding that was an order, not a suggestion, I nodded in agreement."
    DIVINE @think "I can sense a great change within Mika... Tomorrow, her training will be complete."
    show mc at blurin, cleft_f
    MC @think "How can you be sure?"
    DIVINE @happy "She's still afraid... But she's no longer letting it hold her back."
    hide divine with easeoutleft
    "Sister Divine, without another word, almost glided across the floor as she left."
    "Her expression was stern, but the pain beneath the mask was visible beneath the cracks."
    show mc at blurin, center_f with ease
    $ QstSetProgress(QstABestFriendsPath, 9)
    $ QstSetDelay(QstABestFriendsPath, 1)
    $ LocEnter()
    # new goal next day train with her

#Scene 12 - Tower of Palam training ground
#The next day - player can find Mika waiting on the training ground - Player selects on Mika 
label qst_a_best_friends_path_12:
    show mika at center_f with dissolve
    MIKA @talk "I - I'm ready for my final test!"
    menu:
        "{image=[ICON.SWORDS]} Let's begin.":
            MIKA @smile "This time, I'll definitely win!"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            $ AutoMus(True)
            $ LocFlush()
            show mika at cright_f
            show mc at cleft
            with dissolve
            if LastBattleOutcome == "victory":
                MIKA @sad "D-Damn it!"
                MC @talk "{i}*Huff*{/i} Don't put yourself down..."
                MC @smile "You're ready, Mika."
                MIKA @shock "But... {i}I lost!{/i}"
                MC @smile "Trust me, you can handle a few Demorai."
                MC @smile "{i}You're ready.{/i}"
            elif LastBattleOutcome == "defeat":
                MIKA @shock "I... {i}I did it!{/i}"
                MC @smile "Well done, Mika."
                MC @smile "You're definitely ready."
            show mika smile at blurin, center_f with ease
            "Mika leapt into my arms for a tight hug, squealing happily before pulling herself away."
            MIKA @smile "I did it! I can't believe I actually did it!"
            MC @smile "I'll let Sister Divine know you're ready."
            MIKA @smile "T-Thank you... [player_name!t]."
            MIKA @smile "For believing in me."
            "As I smiled at her, I could feel the absolute adoration emitting from her eyes."
            MC @smile "You'll do great things, Mika, of that I'm sure."
            $ QstComplete(QstABestFriendsPath)
            $ LocEnter()

        "Soon, I have some things I need to attend to first.":
            MIKA @talk "M-Mmm, alright!"
            $ LocEnter()