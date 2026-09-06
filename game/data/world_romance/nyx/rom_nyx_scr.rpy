# Upon visiting Nyx after the 'successful' mission
label rom_nyx_start:
    if not IsDaytime():
        MC "It's too late to have this discussion with her. I'll try tomorrow."
        $ LocSet("novaras_fort_seb_barracks")
        $ LocEnter()

    show nyx angry at center_f with dissolve
    NYX @angry "What are you doing here?"
    NYX @angry "I didn't ask for you."
    menu:
        "I came here to talk about what happened.":
            NYX @angry "There's nothing to talk about."
            NYX @sad "The mission was a success and ... That's it."
            MC @talk "And what about what happened {i}during{/i} the mission?"
            NYX @angry "W-What happened during a mission doesn't leave the mission!"

        "Do I need to wait for you to summon me now to come here?":
            show nyx sad
            NYX @sad "Y-Yes."
            NYX @sad "People will start to make ... unnecessary assumptions should you keep turning up here unannounced."
            MC @talk "Such as?"
            NYX @angry "You know damn well what they'll say!"
            NYX @sad "Especially after ...{i}What we needed to do.{/i}"
  
    menu:
        "Why are you so afraid to admit you enjoyed it? {image=[ICON.HEART]}":
            $ CharSetLover("nyx")
            NYX @shock "E-Enjoy myself?!"
            NYX @angry "Are you insane?"
            NYX @disg "We did what we {i}had{/i} to do! That's all."
            show nyx disg
            NYX @disg "If you can't separate the job from your own personal {i}feelings{/i} then I suggest just sticking to the regular guilds work."

            menu:
                "Bullshit. (Dominant route)":
                    $ RomanceNyx().route = "dominant"

                    NYX shock "Excuse me?"
                    scene ss_nyx_dominant_first_stage with dissolve
                    'Nyx sat up onto her desk and stared towards me.' #Nyx sat on desk animation 
                    NYX "Are you aware I could have your head for speaking back to me like that?"
                    MC "I think you're just too afraid to admit you liked it, no..."
                    MC "{i}You loved it.{/i}"
                    "Captain Nyx glared towards me."
                    NYX "Haha! What an arrogant little man you are!"
                    NYX "What, are you expecting me to fall on my hands and knees and beg you for your cock or something?"
                    MC "Something like that..."
                    NYX "Don't make me laugh!"
                    scene ss_nyx_dominant_second_stage_paper_on with vpunch
                    $ Pause(1.8)
                    scene ss_nyx_dominant_second_stage_paper_off
                    "I stepped towards Captain Nyx, gently shoving her back down onto the desk with surprising ease." #Cut to animation - paper flying - then just her on table
                    NYX "{i}*Gasp!*{/i}"
                    NYX "You ... You laid your hands on me!"
                    MC "Sit up."
                    NYX "I'LL FUCKING-"
                    MC "SIT. UP."
                    NYX "..."
                    "With trembling breath, Nyx sat upright."
                    "Her cheeks burned red as she sat defiantly on the desk."
                    NYX "W-What do you think you're-"
                    scene ss_nyx_dominant_third_stage_1 with hpunch
                    "I reached out to cup and squeeze her cheeks together." #Cut to MC squeezes cheeks animation
                    NYX "Mmfghh?!"
                    MC "You can put on the tough ice-bitch routine all you want."
                    MC "But I think I know what you need."
                    "Captain Nyx shook and freed her head from my grasp."
                    NYX "W-WHO DO YOU THINK YOU'RE TALKING TO?!"
                    NYX "I'm the fucking captain of the city guard and I-"
                    "I didn't let Nyx finish, with a light slap across her face, she sat and stared bewildered in shock."
                    "Only murmuring as she struggled to form an answer."
                    NYX "You ... Who ..."
                    "I pressed my thumb onto her lips, and her eyes, wide with uncertainty stared towards me." 
                    MC "Put your lips around it."
                    NYX "..."
                    scene ss_nyx_dominant_third_stage_2 with dissolve
                    "Nervously, Nyx without breaking eye-contact with me, opened her mouth and wrapped her lips around my thumb." #Cut to thumb suck animation
                    "She sucked on it for a moment, gently gliding her lips back and forth over it as she let out a reluctant moan."
                    MC "There we go ... See? Aren't you much happier when I put things in your mouth?"
                    "There's was a grumbled moan of angry protest, but I simply smirked and kept gently rocking my thumb lightly in and out of her mouth."
                    scene ss_nyx_dominant_third_stage_3 with dissolve
                    "Decide to play with her mouth a bit, I tugged and pulled at the side of her cheeks as she let out a gargled, weak protest." #Cut to cheek pulling animation
                    NYX "G-Graghh!"
                    MC "You're going to need to open this mouth nice and wide if you're going to handle my cock you know!"
                    NYX "GGRGHHHH!!"
                    "Some saliva drooled out the side of her mouth as she continued to glare angrily and ashamedly towards me."
                    scene ss_nyx_dominant_third_stage_1 with dissolve
                    "Pulling my thumb from her mouth entirely, she pouted, eyes ashamedly looking away from me as her cheeks burned red." #Cut back to face squeeze
                    "Squeezing her cheeks once more, I turned to tilt her head to look towards me."
                    MC "I'm coming back here from now on, and I'm going to give you what you {i}need,{/i} understand?"
                    "Nyx didn't answer, she simply stared ahead towards me with impotent rage and embarrassment over what just happened."
                    "Taking a few steps away from her, I smirked as I turned and left her Office." #Animation ends
                    $ LocFlush()
                    show nyx angry at center_f
                    with dissolve
                    #MC leaves the room 
                    NYX @angry "(...Why ...Why the fuck did I let him do that?!)"
                    NYX @angry "(What in the seven hells is wrong with me?!)"
                    scene black with dissolve
                    $ QstSetDelay(RomanceNyx, 1)
                    $ QstSetProgress(RomanceNyx, 1)
                    $ NoteLock("romanceNyxStart")
                    $ CharAddRelEntry("nyx", "romance_dom")
                    $ NoteUnlock("romanceNyxDominant1")
                    $ LocSet("novaras_fort_seb_barracks")
                    $ LocEnter()

                "Is that what you really think? (Romance route)":
                    $ RomanceNyx().route = "love"

                    NYX @sad "I..."
                    NYX @disg "Do I need to remind you there's a war going on outside?"
                    NYX @angry "We both have commitments! Honor! Duty! Integrity!"
                    NYX @angry "These are the things that need to ALWAYS take priority!"
                    show nyx sad
                    NYX @sad "Not ... selfish desires!"
                    MC @talk "So {i}you do{/i} feel something then?"
                    NYX @shock "I-"
                    NYX @blush "No, of course not!"
                    NYX @blush "I'm just trying to explain to you how even if I {i}did{/i} feel some sort of connection to you it wouldn't matter!"
                    show mc at cleft with easeinleft
                    "I nodded, taking in Captain Nyx's words, and then slowly moved towards her."
                    NYX @shock "What do you think you're doing?" 
                    "I gently grabbed Captain Nyx's arms and pulled her closer towards me."
                    show nyx angry
                    NYX @angry "I'll scream!"
                    MC @talk  "...Do you really want me to let go?"
                    NYX @shock "I-It doesn't matter what I want!"
                    NYX @angry "What matters is our duty! That is what-"
                    hide nyx
                    hide mc
                    show cg_nyx_kiss_armor surprised at cleft with hpunch
                    "I didn't let Nyx finish her sentence, as her chest pressed against mine our lips met." #surprise kiss art
                    show cg_nyx_kiss_armor relaxed
                    "There was a momentarily squeal of protest before she sank into the kiss, wrapping her arms around my neck as she closed her eyes." #relax kiss art
                    hide cg_nyx_kiss_armor
                    show mc at cleft
                    show nyx shock at center_f
                    with Dissolve(0.3)
                    "After a few moments, Nyx snapped out of the trance like state she was in and gently shoved me back." 
                    NYX @shock "We ... We shouldn't have-"
                    show nyx angry
                    NYX @angry "Get out! JUST GET OUT!"
                    hide mc
                    show nyx angry at left_f
                    with easeinleft
                    "Angrily, Nyx shoved and pushed me out of her Office, beating at my chest before she slammed the door shut behind her."
                    scene black with dissolve
                    $ LocSet("novaras_fort_seb_barracks")
                    $ CharAddRelEntry("nyx", "romance")
                    $ QstSetDelay(RomanceNyx, 1)
                    $ QstSetProgress(RomanceNyx, 1)
                    $ NoteLock("romanceNyxStart")
                    $ NoteUnlock("romanceNyxLove1")
                    $ LocFlush()
                    show mc at center
                    with dissolve
                    MC "(Fuck ... Maybe I screwed that up?)"
                    $ LocEnter()

        "Yes, we should keep things professional, regardless of what happened. {image=[ICON.HEART_CROSS]}":
            NYX @sad "I-"
            NYX @talk "Yes, exactly."
            NYX @talk "I am, um, glad that you're being so mature about this."
            show nyx
            "There was a tinge of disappointment in Captain Nyx's voice that she masked with a smile."
            show nyx laugh
            NYX @laugh "Yes, yes, it's for the best."
            NYX @laugh "I will contact you when I'm need of your services again."
            "Captain Nyx stepped forward, gently pushing me towards the door."
            NYX @laugh "Now if you don't mind, I have plenty of work to be getting back to!"
            "Nyx gently pushed me outside of her office."
            MC @talk "Very well, {i}Nyx.{/i}"
            NYX @laugh "That's {i}Captain{/i} Nyx to you."
            "Captain Nyx slammed the doors shut behind me."
            show nyx sad
            NYX @sad "...{i}*Sigh*{/i}"
            NYX "(It's for the best.)"
            #Cut to MC outside
            scene black with dissolve
            $ LocSet("novaras_fort_seb_barracks")
            $ LocFlush()
            show mc at center
            with dissolve
            MC "(I wonder what would have happened if I pushed her a little more back there?)"
            $ NoteLock("romanceNyxStart")
            $ QstFail(RomanceNyx)
            $ LocEnter()
