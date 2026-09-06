label qst_TwoEmperors_2:
    play sound "audio/cfx/war__drums.ogg" loop
    'From the depths of the cavern, the sound of drums... Drums beating in the depths of the darkness.'
    show mc_transformed with easeinright:
        xcenter 0.8
        xzoom -1.0
    show markus_transformed with easeinleft:
        xcenter 0.1
    MARKUS 'What is that?'
    MC "...Come on, let's get closer."
    show mc_transformed at blurin:
        xzoom 1.0
    hide mc_transformed with easeoutright
    MARKUS '...F-Fuck?! Are you not hearing the same thing as me?'
    MC 'Shh! Just follow me damn it!'
    MARKUS '{i}*Sigh*{/i} ...Fuck!'
    hide markus_transformed with easeoutright
    scene black with dissolve
    'Following the sounds, we decided it was best to avoid the main pathway where the others would have walked, and instead clambered our way through one of the other connecting winding passages.'
    'The less traversed pathway rose up as we continued to walk along it, till finally, we stumbled upon an opening which we cautiously approached.'
    $ AutoMus(False)
    $ PlayMusic("audio/music/14_Zanaraks.ogg")
    scene cg_khazel_speech with dissolve
    'Peering through the opening cautiously, we could see we were high above the many thousands of Demorai down below in the great Cavern like hall.'
    'Organized into neat rows, the Demorai forces gathered and waited patiently, staring down at some great oval stone stage with strange markings on it and lit burning iron fire pits all around.'
    'The front row beat their drums in a synchronized steady rhythm, each boom echoing deeply through the ruins.'
    'Markus and I shared a brief look of bewilderment as we continued to watch the scene unfold below us.'
    'Down below, one group of the Demorai stood away from the rest, many of them robed and distinctly on the fringes.'
    'Amongst them though, an old, hunched woman with ashen skin, and beside her, perhaps the most strangely ethereally beautiful, and yet, oddly baleful woman I had ever laid my eyes on, who watched the whole affair with arms crossed looking sternly ahead towards the stage.'
    'Finally, the drum beats abruptly stopped as a robed figure emerged onto the stage.'
    stop sound 
    scene cg_khazel_speech with dissolve:
        blur 8
    show khazel with dissolve:
        xcenter 0.5
        xzoom -1.0
    DARK_EMPEROR '{i}...How long since we last stood in these hallowed halls?{/i}'
    'Me and Markus shared another look towards each other.'
    MC '({i}It speaks... A fucking Demorai speaks!{/i})'
    DARK_EMPEROR 'How long since our great dream began and led us to this most sacred war?'
    DARK_EMPEROR 'The sacrifices our people have shouldered to bring us this far have been immeasurable.'
    DARK_EMPEROR 'From the bloody battle rivers of Ashara to the black mines of Helenos, we have fought, and we have prevailed.'
    DARK_EMPEROR 'Now your Emperor calls upon you once again...'
    DARK_EMPEROR 'It is no secret this war has taken longer than any of us first expected.'
    DARK_EMPEROR 'Our mistakes early on cost us dearly... But now, the time has come to end this endless stalemate!'
    'The mass of Demorai roared in excitement.'
    DARK_EMPEROR "Malakai blesses us with Lord Zanarak's return from his great crusade, and with his aid, I pledge to you."
    DARK_EMPEROR "WE SHALL CAST OUT THOSE WHO STAND IN OUR WAY AND SWEEP AWAY THEIR ARMIES LIKE DUST!"
    DARK_EMPEROR "THE LAND SHALL FLOW RED WITH THEIR BLOOD TILL THEY ARE BUT A FORGOTTEN DREAM WE ONE DAY TELL OUR YOUNG!"
    'The Demorai horde had now been worked up into a roaring frenzy.'
    DARK_EMPEROR "Do you hear it my children?"
    DARK_EMPEROR "The drums of war beat once again... Our great plan is finally set in motion!"
    DARK_EMPEROR "Our Empire stands on the edge of victory! Will you shed your blood with me one final time till the sweet night sings our people songs once again?"
    DARK_EMPEROR "WILL YOU?!"
    play sound "audio/cfx/crowd_cheer_smaller.ogg"
    'The Demorai beat at the drums wildly as the Demorai crowds now roared so loud it was almost painful to the ears.'
    'The dark emperor rose up his arms into the air as he cried out.'
    DARK_EMPEROR 'LET THE CELEBRATIONS BEGIN!'
    play sound2 "audio/cfx/crowd_cheer.ogg"
    scene cg_khazel_speech with dissolve
    'The Demorai roared out in thunderous cries of jubilation, huge trays of beautifully cooked food were brought and shared amongst them.'
    'The drum beat now became faster and other instruments tuned in.'
    'It was perhaps the most bizarre thing I ever witnessed, the Demorai, the unspeakable terrors thought as nothing more than savage beasts... jovial and dancing with glee.'
    'In the corner as they danced still, that same stern ethereal woman stood unfazed, arms folded as she watched the scene unfold before her.'
    "I could barely pull my eyes away from her beauty till I found Markus' claw on my shoulder as he leaned over to whisper to me."
    MARKUS 'We should leave.'
    'I nodded, and the two of us crawled our way backwards away from the strange party and made our way back the way we came.'
    scene cg_khazel_speech with dissolve:
        blur 8
    show sypha at left with easeinleft
    UNKNOWN '...I see we continue to dance on the edge of oblivion.' # syph
    show myresu at right_f with easeinright
    UNKNOWN '{i}...I trust you saw them?{/i}' # myr
    show sypha at nod
    UNKNOWN 'Of course.' # syph
    UNKNOWN '{i}Then you know what to do, girl.{/i}' # myr
    show sypha at nod
    UNKNOWN 'Of course, High Mother.' # syph
    #Cut to black, show MC and Markus trying to leave the temple - they are confronted by Sypha 
    scene black with dissolve
    'As we made our way hastily back, the jovial sounds of the party became more and more distant behind us.'
    MARKUS "Fucking hells... Now there's {i}two{/i} Emperors?"
    MARKUS "One was enough!"
    MARKUS "We need to tell the others what we've seen."
    $ QstSetProgress(QstTwoEmperors, 3)
    MARKUS "The Demorai... They-"
    UNKNOWN "{i}Talk?{/i}"
    $ AutoMus(True)

    $ LocFlush()
    
    show mc_transformed:
        xcenter 0.15
    show markus_transformed:
        xcenter 0.85
        xzoom -1.0
    show sypha at center_f
    with dissolve
    # show markus, sypha, mc
    'The two of us spun around, claws ready as we stared down at the same ethereal beauty I had seen earlier.'
    MC "How did you-"
    UNKNOWN "Please... You make pitiful spies."
    MC 'What do you want, Demorai?'
    'The girl laughed.'
    UNKNOWN "My name is Sypha... Sypha of House Lamont."
    MC 'House... {i}Lamont?{/i}'
    'The Demorai known as Sypha pointed first towards me.'
    SYPHA @laugh "And you are [player_name!t]."
    'Then, she pointed towards Markus.'
    show sypha at blurin, center
    SYPHA @laugh "And you are Markus."
    MC 'You... Know who we are?'
    SYPHA @smug "{i}I know many things.{/i}"
    'The two of us nervously glanced towards each other, how was our secrecy so easily exposed?'
    SYPHA @talk "Now, you should come with me if you want to make it out of this place alive."
    show sypha at blurin, center_f
    MARKUS 'No chance, Demorai.'
    'Markus readied himself for battle.'
    SYPHA @angry "There are hordes of guards now stationed outside the entrance which you came in through."
    'Sypha shrugged.'
    SYPHA @think "Perhaps you will be able to fight your way through them all, perhaps not."
    SYPHA @talk "But if you follow me, I can lead you out safely."
    MC 'Why in all of the hells would we trust you?'
    'Sypha smiled.'
    SYPHA @smug "...You really don't have any idea about what's {i}really{/i} going on, do you?"
    'Once again me and Markus shared another glance at each other, unsure of how to proceed.'
    SYPHA @happy "Let us just say that I am a friend."
    SYPHA @think "And the situation you two have found yourself in is vastly more complicated than you could ever imagine."
    'Behind us, we heard the sounds of footsteps drawing ever closer.'
    SYPHA @talk "I imagine all that fighting while you're both stuck in that tunnel will only draw the attention of more Demorai though."
    SYPHA @angry "Won't be very pleasant... Squeezed in shoulder to shoulder like that, desperately trying to fight your way out."
    SYPHA @talk "Probably turn into a real bloodbath."
    'The sound of footsteps continued to grow louder as me and Markus remained frozen in indecision, my heart racing.'
    SYPHA @angry "Mmm, sounds like times running out... Make your choice."
    MARKUS "It's a trick [player_name!t]! She's just trying to lead us astray!"
    MARKUS "She'll walk us right into a fucking trap!"
    MC '(Fuck... What should I do?)'
    menu:
        "Okay... I trust you.":
            'Markus stared at me, jaw hung open in shock as Sypha smiled.' #+1 affection Sypha
            $ QstTwoEmperors().tookSyphaHelp = True
            $ CharChangeRel("sypha", 1)
            MARKUS "You... You can't be serious!"
            MARKUS "[player_name!t]! She's a fucking Demorai!"
            SYPHA @talk "Follow me, quickly!"
            hide sypha with easeoutleft
            # they leave screen
            # to black?
            scene black with dissolve
            'As I followed after Sypha, Markus very reluctantly followed behind, still voicing his displeasure at what a terrible idea this was.'
            'Sypha continued to lead us down another winding path, and as we followed after her, the sounds of footsteps behind us grew quieter and quieter.'
            'There was an eerie echo throughout the strange cave like tunnels as we followed her through, and for a moment, I thought perhaps this might have been a mistake.'
            'Who knows where she was really taking us?'
            'In my haste, I agreed to follow her, but why?'
            'I had no reason to trust her, in fact, I have every reason {i}not{/i} to trust her.'
            'And yet, I followed her all the same into the strange depths of this dark abyss world.'
            MC '...Why are you helping us?'
            SYPHA @talk "Everything will be made clear in time."
            SYPHA @talk "I don't have time to explain everything now."
            MARKUS 'Well what the fuck is this place even?'
            SYPHA  "..."
            "Sypha didn't answer, she cast a glance over her shoulder to make sure we were still following."
            "Deeper and deeper through the winding paths we tread, till finally, an opening up ahead."
            $ LocSet("demorai_temple")
            $ LocFlush()
            show mc_transformed:
                xcenter 0.15
            show markus_transformed:
                xcenter 0.85
                xzoom -1.0
            show sypha at center
            with dissolve
            "Leading us out into the open desert, Sypha pointed off into the distance."
            SYPHA @talk "Novaras is that way."
            'Both me and Markus cautiously looked around, half-expecting an ambush from Demorai amidst the dunes.'
            SYPHA @talk "...There's no one coming."
            SYPHA @talk "Now go."
            MC "Hold on a second."
            MC "Who are you really?"
            SYPHA @happy "I am friend, we share a common goal."
            MC @talk "What goal is that?"
            SYPHA @happy "{i}To end this war, of course.{/i}"
            MARKUS "With your side winning, right?"
            SYPHA @talk "{i}*Sigh*{/i}"
            SYPHA @angry "There is more at stake here than either of you could possibly imagine."
            SYPHA @happy "All you need to know for now is I'm a friend and I will send one of my agents to make contact soon."
            MC @talk "Your... {i}agents?{/i}"
            SYPHA @talk "Don't worry..."
            SYPHA @happy "She's been dying to meet you again."
            MC "{i}Again?{/i}"
            SYPHA @talk "Go now... Both of you."
            'Me and Markus shared another still bewildered look as we turned to leave.'
            hide markus_transformed with easeoutleft
            'As we did so, Sypha called back to me once more.'
            SYPHA @happy "Oh, [player_name!t]."
            SYPHA @happy "That reminds me..."
            SYPHA @perv "{i}I look forward to claiming you!{/i}"
            "As I pondered Sypha's words, Markus' hand grabbed me by the shoulder and pulled me away."
            $ CharMeet("sypha")
            hide mc_transformed with easeoutleft
            MARKUS "Come on... Forget the witch."
            scene black with dissolve
            MARKUS "Let's get out of here."
        "{image=[ICON.SWORDS]} Get out of our way, Demorai!":
            SYPHA @talk "{i}*Sigh*{/i}" # -1 affection point with Sypha 
            $ CharChangeRel("sypha", 1)
            SYPHA @disgust "Have it your way, morons."
            'The sounds of footsteps drew closer and closer as Sypha continued to look at us with pure disappointment.'
            scene black with dissolve
            'We hurried past her, heading back the way we came as quickly as we could before we were confronted by dozens of Demorai.'

            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")

            MARKUS 'FUCK!'

            $ TransformMC(True)
            $ TransformMarkus(True)

            $ StartBattle(BattleData(BackgroundImage = "pbat_demorai_temple", CharIDList_Right = [{"e_demorai_scout":8}, {"e_demorai_scout":8}, {"e_demorai_brute":5}, {"e_demorai_brute":6}]))

            $ TransformMarkus(False)
            $ TransformMC(False)

            $ LocFlush()
            with dissolve

            show mc_transformed with easeinleft:
                xcenter 0.5
            BLACK "More on their way."
            MC "Bring it on, demon spawn!"
            BLACK "Bringing it on."
            MC "(That's not what I~)"
            BLACK "Focus."
            hide mc_transformed with dissolve
            $ TransformMC(True)
            $ TransformMarkus(True)
             
            $ StartBattle(BattleData(BackgroundImage = "pbat_demorai_temple", CharIDList_Right = [{"e_dark_soldier":8}, {"e_demorai_scout":6}, {"e_demorai_brute":7}, {"e_demorai_brute":6}]))

            $ TransformMC(False)
            $ TransformMarkus(False)

            'The dozens of bloodied, torn to shreds Demorai bodies littered the tunnel and piled up so high we had to clamber over the piles of their torn limbs to reach the outside.'
            'Behind us, Sypha stood watching the whole thing.'
            SYPHA @talk "{i}...Fucking idiots.{/i}"
            $ AutoMus(True)
            "We didn't want to waste anymore time, we could hear the sound of new stomping feet hurrying their way towards us, and quickly, we sprung our escape." 
    'We made our way back to Novaras as quickly as we could.'
    'What we had seen left both of us shaken, our whole worlds as we understood it, collapsing around us.'
    'Near by the gates of Novaras, we changed back into our human forms and picked up our clothes from where we left them.'
    'In silence, we made our way back to the Gate.'
    $ LocSet("novaras_gates")
    $ LocEnter()