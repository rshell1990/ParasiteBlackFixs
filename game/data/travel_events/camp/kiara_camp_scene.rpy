# this variable can be annihilated after we 
default TravelEvent_KiaraCampScene_FirstTime = True

label travel_event_kiara_camp_scene:
    # choose betnwee 1 and rep
    if TravelEvent_KiaraCampScene_FirstTime:
        $ TravelEvent_KiaraCampScene_FirstTime = False
        call travel_event_kiara_camp_scene_firsttime from _call_travel_event_kiara_camp_scene_firsttime
    else:
        call travel_event_kiara_camp_scene_repeat from _call_travel_event_kiara_camp_scene_repeat
    return

label travel_event_kiara_camp_scene_firsttime:
    scene bg_player_camp_tent
    show mc at cright_f
    with dissolve
    $ Pause(0.1)
    $ PlaySoundRandom("tentFlap")
    $ Pause(0.1)
    show kiara sad at cleft with dissolve
    "As I was laying down to rest, I heard the rustling of the flap as Kiara entered."
    KIARA @talk "Evening..."
    $ AutoMus(False)
    $ PlayMusic("audio/music/38_SinfulRetreat.ogg")
    MC @talk "Kiara."
    "Kiara stepped further into the tent, void of her usual confidence."
    "In fact, she seemed more nervous than anything."
    KIARA @sad "..."
    MC @think "Kiara, what is it?"
    KIARA @sad "We didn't really talk much about me..."
    "She paused, reluctant to finish the sentence."
    MC @talk "... Dying?"
    KIARA @sad "Aye... That."
    KIARA @sad "Must have been quite a shock seeing me again."
    menu:
        "I mourned you.":
            KIARA @sad "F-Fucking seven hells."
            KIARA @sad "Do you know how hard it is hearing you say that?"
            MC @talk "You always said what we had wasn't serious... Just while we served."
            KIARA @angry "I-" 
            KIARA @sad "... Fuck."
            pass

        "At this point, I just wake up anticipating being shocked.":
            KIARA @laugh "Ha...That's the spirit!"
            KIARA @smile "Now you're just inviting me to try to see if I can out-do coming back from the dead!"
            MC @smile "Preferably not with the part where you actually died this time."
            "The smile faded from her face."
            KIARA @sad "H-Ha..."
            pass

    KIARA @sad "... There's something I need to talk to you about."
    MC @think "What is it?"
    KIARA @sad "The truth."
    KIARA @sad "The truth about our time together before... back in the scouts."
    MC @talk "What are you talking about?"
    KIARA @sad "I wasn't... entirely honest with you."
    MC @surprised "I have no idea still what you're going on about."
    KIARA @sad "You know, no matter what you say when I tell you, I still think you and I are destined to be together, the gods-"
    MC @serious "Kiara, get to the point."
    KIARA @sad "..."
    KIARA @sad "{b}I was using you.{/b}"
    MC @surprised "What?"
    KIARA @sad "{i}*Sigh*{/i}"
    KIARA @sad "Why'd you think they let men and women intermingle in the scouts?"
    MC @think "Because... There are not enough men alone to fill every division?"
    KIARA @sad "Partly... But not exactly."
    KIARA @sad "If a girl happens to get herself knocked up, they send you back home and let you leave the scouts."
    KIARA @sad "... If you're willing to give up the little one, let em' be raised to be whatever they need, another soldier probably."
    "The realization slowly dawned upon me as I felt my heart drop to the floor."
    MC @sad "You..."
    "Sadness and confusion quickly turn to hot anger."
    MC @angry "You were going to what? Have my child and then just sell them off for your own life!?"
    KIARA @sad "What choice did I have?"
    MC @angry "And then what? Ride off into the sunset, forget I existed, and just pretend it was all some bad dream?"
    KIARA @shock "No! I promise you, I..."
    KIARA @sad "{i}I don't know if I was going to look for you after I got out.{/i}"
    KIARA @shock "But I promise you, I was going to use my funds to try and have her sent to serve in Angharad where it was safe!"
    KIARA @shock "On my life, it's the truth!"
    MC @surprised "... {i}Her?{/i}"
    KIARA @sad "..."
    MC @surprised "What do you mean by {i}her?{/i}"
    "Kiara's eyes dropped down towards her stomach as she gently rested her hands over it."
    KIARA @sad "..."
    "An empty void filled my soul as I felt my heart shatter into pieces."
    MC @sad "...No, Kiara, don't tell me-"
    KIARA @sad "I was going to tell you."
    MC @sad "But... You..."
    KIARA @cry "I'm sorry."
    KIARA @cry "I'm so sorry."
    MC @sad "Kiara..."
    KIARA @cry "You and I both know it was a miracle's miracle that we both walked out of the scouts alive."
    KIARA @cry "I couldn't..."
    "Kiara stopped herself, biting down on her lip as she turned her head away, closing her eyes as she pushed away the memories."
    KIARA @sad "I understand if you hate me right now."
    KIARA @sad "Believe me... I've been fucking hating myself for months over it."
    KIARA @sad "... {i}But I'm here now.{/i}"
    KIARA @sad "{i}If you can forgive me.{/i}"
    menu:
        "I forgive you.":
            KIARA @shock "You... What?"
            KIARA @sad "I... I thought you might need more time, or-"
            MC @sad "We both know either of us would have done anything to get out of the scouts."
            MC @sad "It was just..."
            "I ponder the next painful words carefully."
            MC @sad "{i}Impossible choices for everyone.{/i}"
            "Impossible choices."
            "If only I was stronger back then."
            "{i}If only.{/i}"
            "{b}I could have-{/b}"
            "I closed my eyes and sighed, banishing the thought."
            "No one can change the past, I can't look back."
            "{i}Otherwise I may never be able to look away...{/i}"
            "Kiara's eyes dropped to the floor, as her hand carefully reached out to take mine."
            show kiara sad at center with ease
            KIARA @sad "{i}I can stay with you tonight if you want.{/i}"
            KIARA @sad "{i}I can make it go away.{/i}"
            menu:
                "{i}*Embrace her*{/i}":
                    scene black with dissolve
                    $ PlayMusic("audio/music/48_Glooming_Desire.ogg")
                    "Kiara gasped as I pulled her to the floor with me."
                    "With nervous breathes, she looked up towards me as we stripped off our clothes."

                    scene kiara_camp_missionary_idle with dissolve
                    $ Pause()

                    KIARA "Are you... Are you sure about this?"
                    KIARA "I don't want you to feel you need to rush this."
                    "I gently caressed Kiara's face with my hand as she tilted it towards me."
                    MC "... We can't go back and fix the past."
                    MC "{i}But we can still look ahead.{/i}"
                    call travel_event_kiara_camp_sex_scene from _call_travel_event_kiara_camp_sex_scene

                "Not tonight.":
                    "I slipped my hand away from Kiara's."
                    show kiara sad at cleft with ease
                    MC @sad "No... Not tonight."
                    "She rubbed at the wrist of her rejected hand tenderly."
                    KIARA @sad "I understand."
                    KIARA @sad "... Goodnight, [player_name!t]."
                    hide kiara with dissolve
                    $ PlaySoundRandom("tentFlap")
                    "Reluctantly, Kiara turned to leave, the flap of my tent rustling as she stepped outside."
                    pass

        "I don't know if I can...":
            $ CharSetAcquaintance("kiara")
            KIARA @sad "I understand."
            KIARA @sad "I'll be here for you... whenever you're ready."
            hide kiara with dissolve
            $ PlaySoundRandom("tentFlap")
            "Kiara turned, leaving the tent as she entered out into the cool night air." 
            show mc at center_f with ease
            "Nothingness washed over as she left... And nothingness turned quickly to regret."
            "I had no idea if I could forgive her or not."
            "All I knew was that right now, I had never felt so alone before..."
            pass
    $ AutoMus(True)
    return


label travel_event_kiara_camp_scene_repeat:
    scene bg_player_camp_tent
    show mc at cleft
    with dissolve
    $ Pause(0.1)
    $ PlaySoundRandom("tentFlap")
    $ Pause(0.1)
    show kiara sad at cright_f with dissolve

    "I turned towards the rustling of the tent's flap as Kiara stepped coyly inside."
    KIARA @smile "Evening."
    MC @smile "Kiara?"
    KIARA @blush "So... I was wondering if you were ummm..."
    KIARA @blush "In the {i}*mood*{/i} tonight, love."
    menu:
        "I am.":
            show kiara at center_f with ease
            $ AutoMus(False)
            $ PlayMusic("audio/music/48_Glooming_Desire.ogg")
            "Kiara smiled alluringly, stepping closer towards me."
            KIARA @blush "{i}What did you have in mind tonight?{/i}"
            menu:
                "To be honest.. {i}I just need you tonight...{/i}": 
                    "Kiara's lewd expression softened slightly, as she let out a little sigh."
                    KIARA @happy "Alright love... I may not be the most lovey-dovey lass out there, but..."
                    KIARA @blush "{i}If that's what you need. I'm here.{/i}"
                    scene black with dissolve
                    "As she moved closer towards me, with gentle kisses the two of collapsed down onto the floor of the tent."
                    "With nervous breathes, she looked up towards me as we stripped off our clothes."
                    scene kiara_camp_missionary_idle with dissolve
                    $ Pause()
                    KIARA "[player_name!t]..."
                    KIARA "{i}Take what you need love, alright?{/i}"
                    KIARA "{b}Take what you need.{/b}"
                    "Kiara offered a soft smile as I gently rubbed my head against her opening."
                    "A hot trembling breath escaped her lips, for all her usual boy-ish mannerisms, Kiara was demure and nervous tonight." 
                    "As I felt the wetness on her slit, I gently pushed forward."
                    "Her sweet lips parted as she let out breathless moan."
                    KIARA "Mmm..."
                    MC "Are you ready?"
                    "Kiara smiled faintly, nodding cutely."
                    call travel_event_kiara_camp_sex_scene from _call_travel_event_kiara_camp_sex_scene_1

        "Not tonight...":
            KIARA @sad "Ahh... Alright then."
            KIARA @sad "I'll leave you be."
            hide kiara with dissolve
            $ PlaySoundRandom("tentFlap")
            "Kiara slumped her way out of my tent dejectedly."
            show mc at center with ease
            pass

    $ AutoMus(True)
    return

label travel_event_kiara_camp_sex_scene:
    "Kiara offered a soft smile as I gently rubbed my head against her opening."
    "A hot trembling breath escaped her lips; for all her usual boy-ish mannerisms, Kiara was demure and nervous tonight." 
    "As I felt the wetness on her slit, I gently pushed forward."
    "Her sweet lips parted as she let out a breathless moan."
    KIARA "Mmm..."
    MC "Are you ready?"
    "Kiara smiled faintly, nodding cutely."
    

    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene kiara_camp_missionary_1_slow with dissolve
    $ Pause()

    "As I pushed the head of my cock against her, she widened her legs and moaned softly as the length of my member slowly entered her."
    KIARA "M-Mmfghh!"
    KIARA "F-Fuck..."
    "She offered up a sheepish smile."
    KIARA "I'm not sure I'm ever going to get used to that thing swinging between your legs you know."
    "Her eyes widened as she felt my member push deeper, moving in and out of her as her nails pressed into my back."
    KIARA "A-Ahhh...! ❤️"
    MC "{i}*Huff*{/i} Kiara..."
    "Kiara's cheeks burned red as she shyly averted her gaze."
    KIARA "B-Bloody hells."
    KIARA "It's so embarrassing when you look at me like that."
    "Our heavy breaths entwined as I slowly took her."
    "Her wet womanhood stretched, squeezing around my cock as her skin glistened in the pale light."
    "Her hot moans became more trembling and frequent as she laid there, her eyes glancing back and forth to look into mine and then away."
    MC "Kiara - {i}*Huff*{/i}"
    MC "Are you ready for more?"
    "A hot, desperate whimper escaped her lips as she nodded her head."
    KIARA "Y-Yes..."
    "She laughed pitifully."
    KIARA "{i}*Huff*{/i} You tryna'- Mmmm... Make me feel like a fresh maiden or something?"
    KIARA "Ahhh!"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene kiara_camp_missionary_2_fast with dissolve
    $ Pause()

    "I smiled, saying nothing as I began to move faster."
    "Kiara's mouth parted as her eyes widened,"
    "As the length of my cock moved quickly in and out of her, her body tightened as she let out a sweet, soft moan."
    KIARA "G-Gods...!"
    KIARA "I don't know if I'm ever gonna get used to your new {i}size.{/i}"
    MC "Should I slow down?"
    "Kiara shook her head as I felt her womanhood tighten and squeeze in almost steady rhythms."
    KIARA "N-No..."
    KIARA "Mmmfghhh!"
    KIARA "{i}I-I feel so... {b}connected{/b} to you like this.{/i}"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene kiara_camp_missionary_3_slow with dissolve
    $ Pause()

    "Kiara's hands run down my chest, her fingers tracing along the faint outline of scars as she wrapped her legs around me."
    MC "Kiara... {i}*Huff*{/i}"
    MC "I-"
    KIARA "Stop thinking."
    "Once more her cheeks flushed red."
    KIARA "Y-You wanna keep treating me like one of those soft Novaras ladies..."
    KIARA "{i}But I can take it.{/i}"
    KIARA "{i}Just... Just give me everything you've got.{/i}"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    scene kiara_camp_missionary_4_fast with dissolve
    $ Pause()

    "Kiara rocked her hips enticingly as I began to once more move faster."
    "Her hot moans filled the tent as the sweat continued to glisten on both our skins by the candlelight."
    KIARA "A-Ahh! Ahh! ❤️"
    KIARA "That's it! Mhhfhg!"
    KIARA "{i}I'm here!{/i}"
    KIARA "{b}I'm here now for you always!{/b}"
    KIARA "Gods...! Mmmfghh!"
    MC "K-Kiara - {i}*Huff*{/i} What are we-"
    KIARA "D-Don't even think about it!"
    "By now, the intensity was overwhelming,"
    "Kiara's passionate embrace was more than just a desperate need to heal whatever trauma's the two of us had endured."
    "Whether she was still quite the same girl I remembered was debatable,"
    "{i}But there was no doubt she loved me.{/i}"
    "As she felt I was drawing closer, her eyes had a twinkle-like quality to them as they widened."
    KIARA "Y-You're close."
    KIARA "{b}I can tell...*Huff*{/b}"
    "I only grunted in response, and with a soft smile, she pulled me in."
    KIARA "Do it... It's alright, love."
    KIARA "{i}I'm here...{/i}"
    KIARA "I'm-"

    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("kiara")
    $ UnlockGalSceneAndGrantXp("kiara", "camp_missionary")
    scene kiara_camp_missionary_finish with flash
    $ Pause()

    MC "H-HRGHHHHHH!!"
    "Kiara's nails dug deep into my back as my whole body tightened."
    "Her legs squeezed around me as she trembled, letting out a soft, muffled moan."
    KIARA "M-Mmmfghhh!! ❤️"
    scene black with dissolve
    "When the moment passed, she gently ran her hand through my hair as she spoke of sweet, soothing things."  
    MC "{i}*Huff*{/i} Kiara... I-"
    KIARA "Shhhh..."
    KIARA "Go to sleep now, love."
    KIARA "{i}It'll be alright... I've got you.{/i}"
    KIARA "{i}I'm here for you...{/i}"
    "... I drifted off into a peaceful slumber till morning light pierced through the tent."
    return

############################################
# Repeat version (CLICK)
# The player selects on Kiara at the camp site
label UNUSED_clickey_repeat:
    KIARA @smile "Something the matter, love?"
    menu:
        "Come join me in my tent tonight.":
            #Only if player has Kiara marked as lover - note: additional options will be added in this menu eventually, like general chat stuff or whatever's needed.
            KIARA @smile "Oooh?"
            KIARA @smile "{i}Looking for some company tonight, Mmm?{/i}"
            KIARA @talk "Alright, I'll join you in a bit."
            #Player when they select to go to sleep - *now* Kiara will appear in their tent.
            KIARA @blush "So... You ready love?"
            KIARA @blush "What are you in the mood for tonight?"
            menu: #Note - other sex scenes will be added here eventually
                "To be honest.. {i}I just need you tonight...{/i}": 
                    "Kiara's lewd expression softened slightly, as she let out a little sigh."
                    KIARA @happy "Alright love... I may not be the most lovey-dovey lass out there, but..."
                    KIARA @blush "{i}If that's what you need. I'm here.{/i}"
                    "As she moved closer towards me, with gentle kisses the two of collapsed down onto the floor of the tent."
                    "With nervous breathes, she looked up towards me as we stripped off our clothes."
                    #Idle
                    KIARA "[player_name!t]..."
                    KIARA "{i}Take what you need love, alright?{/i}"
                    KIARA "{b}Take what you need.{/b}"
                    "Kiara offered a soft smile as I gently rubbed my head against her opening."
                    "A hot trembling breath escaped her lips, for all her usual boy-ish mannerisms, Kiara was demure and nervous tonight." 
                    "As I felt the wetness on her slit, I gently pushed forward."
                    "Her sweet lips parted as she let out breathless moan."
                    KIARA "Mmm..."
                    MC "Are you ready?"
                    "Kiara smiled faintly, nodding cutely."
                    call travel_event_kiara_camp_sex_scene from _call_travel_event_kiara_camp_sex_scene_2

        "Nothing.":
            KIARA @happy "Then at least be more subtle when you're checking out my ass in the meanwhile."
            pass
    
    return