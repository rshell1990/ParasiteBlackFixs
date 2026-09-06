label regina_dildo_peek:
    scene bg_mc_house_bedroom_night with dissolve
    $ PlaySexFx("audio/sex_sounds/reginamasturbate_loop_fade.ogg",1)
    REGINA 'Ah...'
    REGINA 'Mmm...'
    MC @talk 'What is that sound?'
    MC @talk 'It sounds like it’s coming from [regina_ref!t]’s room...'
    MC @talk '... Should I investigate?'
    menu:
        'Ignore the sounds and go back to sleep.':
            $ StopSexFx()
        'Investigate the sounds.':
            scene bg_mc_house_kitchen_night with dissolve
            "I slowly tiptoed to [regina_ref!t]'s bedroom and gave the door a gentle push."
            "It was unlocked."
            "Pushing it open a couple inches further, I took a peek inside..."
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            $ PlaySexFx("audio/sex_sounds/reginamasturbate_loop.ogg",1)
            scene regina_riding_slow with dissolve
            $ Pause()
            'There, I found [regina_ref!t] laid out on the bed in all her splendour.'
            'I watched, unable to tear my eyes away, as she pushed herself unto a phallic-like toy and moaned in muffled delight.'
            'With each thrust of the toy inside she writhed on the bed, her back arching in pleasure.'
            'She had to bring her hand to her mouth and clamp it down to stop herself from crying out:'
            REGINA @talk 'M-Mmm!...'
            "My cock grew harder with each thrust she made until..."
            REGINA @talk 'Ahh...'
            "Until I realised she was looking {b}straight at me.{/b}"
            "Frozen still, I swallowed and stared back."
            "In a moment, I moved about a little."
            "She did not react in any way, enjoying her time with her artificial friend."
            "Only at that point did I remember..."
            "There was a mirror inside her bedroom, right beside the door."
            "Was she {b}staring at herself{/b} riding that thing?"
            "Such a perverse thought made me rock hard, and I couldn't help myself anymore."
            "Watching her mature, voluptuous body riding the dildo I reached down my pants and started stroking my cock."
            "[regina_ref_cap!t] moaned harder as I enjoyed the show, cascading fantasies of plowing my cock all the way inside that marvelous ass of her overflowing me."
            REGINA @talk 'Ohh... Yessh...'
            "I heard her whisper to herself as she amped up her tempo:"
            scene regina_riding_fast with dissolve
            $ Pause()
            REGINA @talk "Yes, mount me..."
            "I wondered whom she may be imagining as I stroked on, licking my lips..."
            REGINA @talk "M-mmmhph pound my ass like you mean it,"
            REGINA @talk "{b}[player_name!t]...{/b}"
            "[player_name!t]?! I felt my heartbeat catapult, yet I kept going, hypnotic scene devouring my senses..."
            REGINA @talk "Ahh.. I saw you stare..."
            REGINA @talk "With animal lust..."
            REGINA @talk "{b}Let it free!{/b}"
            "She moaned the last few words out loud and quickly caught her mouth with her arm, but kept on riding."
            "I couldn't help but imagine breaking in there {i}right now{/i} and giving her large, ripe ass a proper fuck."
            "...Pounding her hard along with her artificial toy..."
            "She upped her tempo even further as I realised that she was approaching her climax..."
            REGINA @talk "Mmmh.. Yes... Ravage my holes [player_name!t]..."
            "The images running through my mind were too much to bear..."
            "Releasing ropes of hot cum I watched her orgasmic agony, shaking with waves of pleasure."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            scene regina_riding_finish with flash
            $ UnlockGalSceneAndGrantXp("regina","riding")
            $ Pause()
            "My legs shaking I almost tipped over inside her room, and realised I better find my way back to bed..."
            scene bg_mc_house_kitchen_night with dissolve
            stop music fadeout 3.0
            "If she found me there, like this..."
            "Who knows what would have happened."
            "Quietly walking back to my room, I realised she may find {i}some traces{/i} of my presence, but was too drained to care."
            scene bg_mc_house_bedroom_night with dissolve
            "Exhausted, I jumped back into my bed."
            "Slowly, I was engulfed into a sweet sleep full of vivid, perverse dreams."
            hide text
    $ AutoMus(True)
    return
