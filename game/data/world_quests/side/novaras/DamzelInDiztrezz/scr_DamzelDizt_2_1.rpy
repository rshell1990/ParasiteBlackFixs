label qst_DamzelDizzt_2_frontal:
    MARKUS "Feeling a little bloodthirsty today, aren't we?"
    MARKUS 'Fine, but we’ll have to be quick...'
    MARKUS 'The commotion will likely draw the attention of the guards and if they see us we’re in trouble...'
    NIJAH 'Y-You intend to fight zem all?!'
    MC @talk 'I do.'
    NIJAH 'But... You will die!'
    MC @talk 'Trust me Nijah, we will not be the ones dying tonight...'
    MC @talk "But the guards are a problem Markus, you're right."
    MARKUS 'We should scout the place out first at night, before anything.'
    MARKUS "At least try get some kind of understanding of what we're up against..."
    MC @talk "That's a good idea."
    MARKUS "Meet me in the Pleasure District tonight, we'll do some scouting from there."
    NIJAH 'I come.'
    MC @talk "It's too dangerous Nijah, if they see you with us they could try something."
    NIJAH @sad 'But-'
    MC @talk 'Can you handle a sword?'
    NIJAH 'I... No.'
    MC @talk "If they catch us Nijah, we might not be able to protect you."
    MC @talk "It's too dangerous..."
    'Nijah looked like she might say something at first, but instead she bite her lip and nodded reluctantly.'
    NIJAH 'Y-Yes, I stay.'
    MC @talk "We'll be back shortly, promise."
    NIJAH 'A-Alright...'
    $ GoalComplete(QstDamzelInDiztrezz, 1)
    $ GoalShow(QstDamzelInDiztrezz, 1.5)
    $ LocEnter()

label qst_DamzelDizzt_2_ScoutDiamond:
    show markus at cright_f
    show mc at cleft
    with dissolve
    MARKUS 'There you are.'
    MARKUS 'Are you ready for this?'
    menu:
        "Let's do this.":
            MARKUS "Alright, let's head up onto some of these rooftops and scout out the perimeter."
            MC @talk 'Sounds like a plan.'
            hide markus
            hide mc
            scene black with dissolve
            'Clambering onto the rooftops, we moved our way as silently as we could and watched from afar.'
            'Here and there the odd guards, always in twos, would patrol around the boundaries of the Black Diamond, while another two always stayed at the Entrance.'
            'From inside, I focused and could hear a few dozen heart beats, but it was impossible to tell the difference between the clients, girls and guards.'
            'After some time we decided to take a closer look.'
            'Climbing in through one of the windows, we watched and looked down from the rafters concealed in darkness... Seeing the Black Diamond below.'
            $ LocFlush()
            with dissolve
            show mc_transformed at left
            show markus_transformed at right_f
            MC '(Can you hear me?)'
            MARKUS '(Yes, now quit shouting!)'
            MC "(I'm not shouting! I'm just not used to talking with my mouth shut!)"
            MARKUS '(Bah! Focus! How many guards can you see?)'
            'Through the darkness I peered around, my vision once I focused in, was able to make out through these strange red like outlines where people stood even in pitch black corners.'
            MC '(...I count fourteen here.)'
            MARKUS '(There is probably more upstairs.)'
            MC "(Don't suppose you two have anything to say.)"
            BLACK '{i}(Something beneath feet...){/i}'
            BLACK '{i}(Can hear it... rumbling.){/i}'
            WHITE '{i}(Cautious... More danger than appears.){/i}'
            MARKUS '(Well, what is it?)'
            MARKUS '(...Hello? HELLO!)'
            MARKUS '(Fucking hells! Why do they just stop talking like that?)'
            MC '(We should go Markus, before someone notices us here.)'
            MARKUS '(Yes, we should-)'
            MARKUS '(Hold on, that one... Is that our man?)'
            'We watched as the one bandit strolled his way into the Black Diamond, he looked different than the others, and four bandit guards walked protectively alongside him.'
            'As he entered, all eyes seemed to turn towards him, and one of the bandits moved out to greet him.'
            #Use blue bandit character model
            hide markus_transformed
            hide mc_transformed
            with dissolve
            show tarek at cleft
            show cg_bandit at cright_f
            with dissolve
            BANDIT 'Great Khan, I am here to deliver your tribute from your vassals.'
            TAREK 'And who pays me greatest tribute today?'
            BANDIT '...The khazahs my khan.'
            TAREK 'The Khazahs... {i}again?{/i}'
            TAREK @angry 'Should I always expect the Vulshans to fall behind everytime now?'
            BANDIT 'We are pushing our men as hard as we can!'
            BANDIT 'But with your restrictions, things are... {i}difficult.{/i}'
            TAREK 'My rules are in place to protect all of us.'
            TAREK @angry "But I don't see the Khazahs complaining about them."
            BANDIT '...Of course Great Khan, we will do better next time.'
            TAREK 'See it done.'
            hide tarek
            hide cg_bandit
            with dissolve
            show mc_transformed at left
            show markus_transformed at right_f
            with dissolve
            'As Tarek marched off, I could sense the furious rage brewing inside the man he just spoke to.'
            "If I didn't know any better, one would think he wanted to {i}kill{/i} Tarek."
            hide markus_transformed
            hide mc_transformed
            with dissolve
            scene black with dissolve
            MC "(I've seen enough, come on, before we are seen...)"
            $ GoalComplete(QstDamzelInDiztrezz, 1.5)
            $ QstDamzelInDiztrezz().hasScoutedDiamond = True
            jump qst_DamzelDizzt_2_frontal_return
        'Not yet, I have a few things I need to sort.':
            MARKUS "Don't be too long."
            $ LocEnter()

label qst_DamzelDizzt_2_frontal_return:
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    with dissolve
    show nijah at center_f
    show mc at cleft
    show markus at cright_f
    with dissolve
    NIJAH "You're back!"
    MC @talk "We scouted the place out, it's heavily guarded but we think we can take it."
    MARKUS "I'm not sure about this [player_name!t]... You heard what... uh... 'our friends' told us, there's something more dangerous lurking there."
    MARKUS 'And that amount of guards is nothing to laugh at!'
    MC @talk "We'll need to be prepared for it..."
    'Nijah seemed to ponder our words for a moment, before her eyes seemed to light up.'
    NIJAH '... I haz idea.'
    'Both of us looked curiously towards Nijah as she explained to us her plan...'
    NIJAH 'I could make distraction with fire powder sticks.'
    MARKUS 'Fire powder sticks?'
    NIJAH 'Yis, zey make pretty patterns when explode in sky.'
    NIJAH 'Very loud, guards come to investigate... Buy you time.'
    MARKUS 'Can you get a hold of them in time?'
    'Nijah nodded.'
    MARKUS 'Alright... Sounds like a plan to me.'
    MARKUS 'But are you sure about this?'
    MARKUS 'You too saw Tarek with that other man... I think there are weaknesses there we can exploit.'
    MARKUS "We don't necessarily need to storm the place but, it's up to you."
    menu menu_damzeldizt_decide_on_frontal:
        "Hmm... You're right, we should try a different strategy.":
            #loops to Diplomacy route stuff
            jump qst_DamzelDizzt_2_sneaky
        'No, we take the bastards down ourselves.':
            MARKUS 'As you wish [player_name!t].'
            #Assault path continued
            NIJAH 'Let know when you want me to get zer sticks...'
            # ON INTERACTING WITH NIJAH
            NIJAH 'Iz you ready?'
            menu:
                '{image=[ICON.SWORDS]} Let’s do it!':
                    jump qst_DamzelDizzt_2_frontal_postScout
                'On second thought...':
                    jump menu_damzeldizt_decide_on_frontal
