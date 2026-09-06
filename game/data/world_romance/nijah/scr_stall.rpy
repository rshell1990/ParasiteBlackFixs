label rom_Nijah_stage2_stall_lines:
    # yeah this shit is necessary otherwise the background borks up
    if IsDaytime():
        show bg_novaras_market_stalls_open_under_day:
            align (1.0, 1.0)
            matrixcolor wLocs[GetLocID()].DayNightMatrixClass(GetDaytimeTintFactor())
        show nijah onlayer master:
            anchor (0.5, 0.5)
            pos (0.82, 0.67)
            zoom 0.35
            xzoom -1.0
        show bg_novaras_market_stalls_open_over_day:
            align (1.0, 1.0)
            matrixcolor wLocs[GetLocID()].DayNightMatrixClass(GetDaytimeTintFactor())
    else:
        show bg_novaras_market_stalls_open_under_night:
            align (1.0, 1.0)
        show nijah onlayer master:
            anchor (0.5, 0.5)
            pos (0.82, 0.67)
            zoom 0.35
            xzoom -1.0
        show bg_novaras_market_stalls_open_over_night:
            align (1.0, 1.0)

    show mc at left with easeinleft
    MC @talk '(It looks like Nijah is working today.)'
    MC @talk '(Perhaps I should see how she is getting on with her stall?)'

    menu:
        "Head closer to Nijah's stall.":
            hide mc
            scene black
            with dissolve
            'As I made my way through the narrow winding street stalls of the markets, I was pleasantly overwhelmed by an assortment of smells and sights.'
            'Traders desperately continued to peddle their wares, anything from live chickens and goats to pelts and trinkets and things.'
            'The market was abuzz with the sounds of coins dropping onto tables, loud chatter, and aggressive bartering.'
            'Fish brought in from the rivers and lakes were brought up and chopped on tables, being sold to those with coin.'
            'Suddenly, smelling the air, the delicious aroma of hot cooking food brought me towards a stall further back, one with eager people gathering around.'
            $ LocFlush()

            if IsDaytime():
                show bg_novaras_market_stalls_open_under_day:
                    align (1.0, 1.0)
                    matrixcolor wLocs[GetLocID()].DayNightMatrixClass(GetDaytimeTintFactor())
            else:
                show bg_novaras_market_stalls_open_under_night:
                    align (1.0, 1.0)
            show mc at left
            show nijah at right_f
            with dissolve
            NIJAH '[player_name!t]! There you are!'
            'She shouted, beaming from her stall as she served some food wrapped for a customer who handed her some gold coins.'
            NIJAH 'Business iz good, no?'
            pass

        "Do nothing.":
            $ LocEnter()

    menu nijah_food:
        "Buy some food":
            NIJAH "Take a look!"
            call screen trade(ShopNijahStall)
            NIJAH "Anything else, [player_name!t]?"
            jump nijah_food

        'Need some help?':
            NIJAH 'Hm? Zat would be good!'
            hide mc
            scene black
            with dissolve
            "Heading behind the market stall, I noticed Nijah’s stall was surrounded by hanging cloths to hide the various meat and things kept behind the front of the stall which the customers saw."
            'Peering behind the cloth curtain, Nijah smiled,'
            NIJAH 'Can you pass me some of the onions my love?'
            'Grabbing from one of the open barrels some onions, I passed them to her and she thanked me as she began to cut them out front.'
            'Suddenly, I had a particularly mischievous idea...'
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            scene cg_nijah_stall with dissolve
            'As Nijah peered back once again to ask for something, I pulled her out back once again, reaching around to fondle at her round ass and firm tits.'
            NIJAH 'M-My love!'
            'Nijah whispered with excited breath,'
            NIJAH 'Za customers!'
            MC @talk 'Turn around and serve them then, but keep this half back here.'
            "I gave Nijah’s soft ass a squeeze."
            NIJAH 'H-Huh?'
            'Spinning Nijah around, I pushed her head and torso back through the curtains to serve the impatient customers, all while I hiked up her dress.'
            'Suddenly realizing what I was doing, Nijah spread her legs and waited anxiously while desperately trying to not let anyone realize what was going on behind the curtain.'
            "Pulling out my cock, I grabbed onto Nijah’s hips and felt her shudder slightly."
            
            CUSTOMER @talk 'Give me another one of those rolls for my daughter girl!'
            NIJAH 'C-Coming right up sir!'
            scene nijah_market_stall_normal with dissolve
            $ PlaySexFx('audio/sex_sounds/kiara_tent_fast.ogg',1)
            $ Pause()
            'She was nervous, but as I rubbed the large head of my cock against her pussy and felt her wet as she was, I knew she was ready for something but we had to be quick!'
            NIJAH 'What can I-'
            NIJAH '{i}*Gasp!*{/i}'
            'Forcing my cock into her, Nijah gasped loudly as I felt her tight pussy squeeze effortlessly around my cock.'
            BLACK '(Gooood... Claim her.)'
            "From behind, with my hands gripped onto her soft butt, I began to thrust in and out of Nijah’s tight body, feeling her squeeze me effortlessly as she quickly became wet, turned on by our secretive sex."
            NIJAH '(In front of – Ah! – Everyone!)'
            scene nijah_market_stall_fast with dissolve
            NIJAH '(M-Mhmm... If zey could only see him claim me zo publically!)'
            CUSTOMER @talk 'Hey! Girl! What’s with that face?'
            CUSTOMER @talk 'Get on with the roll damn it'
            NIJAH 'C-Coming sir!'
            'As Nijah desperately tried to make the roll, I continued to slam my cock deeply into her from behind, listening out for her every little grunt and moan that secretly escaped her lips.'
            'As the crowds outside continued to build, Nijah struggled to keep her composure as her legs began to tremble, and inside me I felt the Parasite’s nature surge as I found myself wildly throwing into her.'
            BLACK 'This one is good...'
            BLACK 'Her body is fertile, she shall sire us many children...'
            'Pushing the voice aside, it was impossible to deny my animal desires to claim her, to finish inside of her and to hear her moan in pleasure.'
            'Whether it was the Parasite or my own twisted fetish desire, the thought of her belly round with my child left my excited cock desperately ready to finish, but where?'
            menu:
                "Cover Nijah’s ass":
                    "Pulling out at the last minute, I stroked my cock furiously as I unloaded my hot seed onto Nijah’s brown butt. Nijah playfully wiggled her butt as she felt the splash of hot seed, and I continued to force out the last of my seed onto her  now coated ass."
                    scene nijah_market_stall_finish_out with flash
                    $ PlaySexFx('audio/sex_sounds/kiara_tent_finish.ogg')
                    $ Pause()
                    $ UnlockGalFlag("nijah","market_stall","var_out")
                'Finish inside of her':
                    "Unable to hold back any longer, I pushed deeply into Nijah’s tight canal, flooding her with my hot seed."
                    scene nijah_market_stall_finish_in with flash
                    $ PlaySexFx('audio/sex_sounds/kiara_tent_finish.ogg')
                    $ Pause()
                    $ UnlockGalFlag("nijah","market_stall","var_in")
                    'When I was finally spent, I slowly unsheathed my cock from her and watched as some of the excessive seed poured and dripped down onto the floor.'
            # BOTH ROUTES CONTINUED.
            $ ReduceInfectionFromSex("nijah")
            $ UnlockGalSceneAndGrantXp("nijah", "market_stall")
            NIJAH 'Just a moment everyone! Need to grab more rolls!'
            'Appearing back through the curtain, Nijah pulled her dress back down as she leapt forward to give me a kiss.'
            NIJAH 'Iz fine but now go!'
            NIJAH 'Before others see you!'
            scene cg_nijah_stall:
                blur 20
            show cg_nijah_kiss_clothed:
                xalign 0.4
                ypos 0.05
                zoom 1.4
            with dissolve
            'I laughed slightly, stealing another kiss from her quickly as I groped her soft butt with both hands.'
            $ Pause()
            MC @talk 'See you tonight, my love.'
            'With that, I snuck out of the Stall out the back.'
            scene black with dissolve
            NIJAH '(Maybe I should ask if we fuck more like this?)'
            $ AutoMus(True)
            $ LocEnter()

        'I’ll let you get back to it!':
            #Continued (ENDS DIALOGUE)
            NIJAH 'I shall see you later my love!~'
            hide nijah with easeoutright
            $ LocEnter()
