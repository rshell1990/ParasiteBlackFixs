label qst_FromAnotherWorld_GoToValleyWithMarkus:
    $ LocSet("novaras_dist_house")
    $ AutoAmb(True)
    $ LocFlush()
    show markus at left
    with dissolve
    show mc at cright_f with easeinright
    "Markus stood just outside the house, tense, eager to take off."
    MC "So Markus... What now?"
    MC "We are so fucked."
    MC "Those things... If what they’re saying is true..."
    MARKUS "Let's go now."
    MC "Yeah, I doubt the Guild will be as scary as the Scouts..."
    MARKUS "We're not going to the guild. Not yet."
    MC @talk "Huh?"
    MARKUS "Come now, we’re heading into {i}the Valley of Death{/i}."
    MC @talk 'What?!'
    MARKUS "It's going to be alright."
    MARKUS "We just need to get out of sight to practice changing into..."
    MARKUS "{i}Whatever{/i} it is we’re going to change into."
    MC @talk 'Markus?!'
    hide markus with easeoutleft
    scene black with dissolve
    $ QstSetProgress(QstFromAnotherWorld, 2)
    $ LocSet("novaras_dist_army")
    $ LocFlush(dissolve)
    show markus at left with easeinright
    show mc at right_f with easeinright
    MC @talk "Markus? Hold up!"
    MARKUS "I’ve thought about what they said..."
    show markus at cleft with easeinleft
    "Markus looked around, making sure no one listens in:"
    MARKUS "If what they say is true, perhaps this could be the key to having the life we’ve always wanted."
    MC @talk "By being cursed?"
    MARKUS "It’s not a curse if we can manage it."
    MARKUS "Anyway, you heard them... they have already given us a lot of benefits."
    MARKUS "AND we owe those things our lives."
    MC @talk "Markus, we have no actual idea of what’s going on with us!"
    MARKUS "And we’re not ever going to know if we don’t at least try to understand them!"
    MARKUS "We have to give them a chance."
    MARKUS "If what those {i}things{/i} told us is true, this is the only way."
    hide markus with easeoutleft
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("novaras_gates")
    $ PlaySound("audio/interactables/gate_drop.ogg")
    $ LocFlush()
    show markus at cright with easeinleft
    "As we passed through the city gate, I felt all kinds of distressing thoughts popping in and out of existence."
    show mc at cleft with easeinleft
    MC "(What are we doing? Will whatever Markus has in mind work? What exactly is going to happen to us now? Is there a 'cure' or something?)"
    hide markus with easeoutright
    "Confident, Markus simply began making his way towards the expanse of the desert."
    MARKUS "Keep up, [player_name!t]!"
    MC "Snapping out of it, I followed Markus."
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("valley_of_death")
    $ TimeAdvBy(TIME_1H)
    $ LocFlush()
    show markus at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MC @talk '... I still don’t like this.'
    MC @talk 'How will we explain to anyone what we were doing beyond the walls?'
    MARKUS 'Easy, we’re part of the Adventurer’s Guild now, remember? Just say we were patrolling for enemies or whatever...'
    MARKUS 'Come on, as long as we’re out of view of the wall it should be safe enough for us.'
    MC @talk 'As long as we don’t get clawed or bitten or disembowelled by some passing Demorai...'
    'Trekking towards the great dunes of the valley, we finally arrived at a spot safely away from the gaze of any watchers on the walls.'
    MARKUS 'Okay... This should do.'
    MC @talk '...Well, what now?'
    MARKUS 'I guess, we just change...'
    MC @talk '...How do we do it exactly?'
    MARKUS 'They said we needed to focus, like it was some extra limb that we just needed to think about using.'
    MC @talk 'Easier said than done! '
    'Without warning, Markus began to strip off his clothes.'
    MC @talk '...What are you doing?'
    MARKUS 'Whatever we change into is likely to tear through our clothes, right?'
    MARKUS 'I don’t particularly want to have to walk through Novaras naked when we return.'
    MC @talk '...You sure you’re into girls?'
    MC @talk 'Because this might be the clumsiest come on ever.'
    'Markus shot me a look of ‘shut up and just do it’, clearly taking this too seriously to acknowledge the ridiculousness of the situation.'
    'I sighed and begrudgingly began to strip.'
    MARKUS 'We’ll keep the clothes by this rock for when we return.'
    MARKUS 'Should be easy to find with that dead hooked tree over there nearby.'
    $ CharSetClothes("markus", "naked")
    show markus at nod
    MC @talk 'If you say so.'
    $ CharSetClothes("mc", "naked")
    show mc at nod
    'Now stark naked, I looked to Markus awaiting his next suggestion.'
    MARKUS 'Okay... Let’s just try and think.'
    MC @talk '...'
    MARKUS '... Hmmmm...'
    MC @talk '....'
    MARKUS 'HMMMMM...'
    show mc at shake
    MC @talk 'What the fuck is that?'
    MARKUS 'I’m trying to channel my thoughts to focus!'
    MC @talk 'By going ‘Hmmmmm’ loudly?'
    MARKUS 'Well, if you’ve got a better idea let’s hear it! '
    MC @talk 'It wasn’t my idea to stand bollock naked in the middle of the desert! '
    MARKUS 'Gah! We just need to focus! And this is the safest place to test it! '
    MC @talk 'Fine. Whatever.'
    MARKUS '...'
    MC @talk '...'
    'Clamping my eyes shut, I tried to reach deep into myself, thinking about changing into... whatever I was supposed to be changing into.'
    'As the moments passed, I was growing ever more hopeless, convinced that whatever I was trying to reach was impossible without an understanding of what it actually was.  '
    MC @talk 'It’s not work—'
    'All of a sudden, I felt a strange pain surge through my body.'
    MARKUS '[player_name!t]? What’s—'
    'Markus suddenly bent double, clutching at his stomach as he gasped for air.'
    show markus at shake
    MC @talk 'Markus... I can feel—'
    play sound2 "audio/cfx/transform.ogg"
    scene black with flash
    'A sharp pain coursed through me and I screamed like a man possessed.'
    'I felt my bones shatter in quick succession and then form again, the broken pieces growing, becoming larger, stronger.'
    'The pain forced me to my knees, and I let out a roar of agony as I felt my spine elongating before the pain travelled to my head and my mind cracked.'
    'Fragments of my thoughts were being melded with the symbiote; I could feel its long fingers on the inside of my skull as it picked through my mind.'
    'My whole body burned as I felt it mould and shape itself to me, creating a monstrous new form.'
    'Somewhere on the edge of my vision I could see Markus lying on the floor, his head in his hands, screaming.'
    'Any hopes of it being a painless transformation were thwarted as the agonising ordeal continued.'
    'Finally, as I felt strange snake like creatures force their way out of my back, I stood upright to stare at Markus... or at least... what I {i}knew{/i} was Markus.'
    play sound "audio/cfx/darkness_erupt.ogg"
    $ LocFlush()
    show markus_transformed at right_f
    show mc_transformed at left
    with flash
    MARKUS '[player_name!t]... we’re...'
    'His voice was distorted, {i}inhuman{/i}.'
    'I gawped down at my clawed hands and then towards the slither of one of my tentacles as it slid over my shoulder and turned to look at me inquisitively before retreating.'
    'Curiously, Markus did not possess any of the strange tentacles that protruded from my back, but instead, large white wings that kicked up the hot sand as they beat ferociously behind him.'
    MC 'How do you feel?'
    'It seemed both of our voices had changed to be more guttural, but they were clear enough to understand.'
    BLACK 'It will be less painful the next time...'
    WHITE 'Quicker as well...'
    'Examining ourselves thoroughly, Markus began to laugh.'
    MARKUS 'Incredible!'
    $ QstSetProgress(QstFromAnotherWorld, 3)
    MARKUS 'Can you feel it? It’s like fire in my veins!'
    MC 'I feel... {i}strong,{/i}'
    MARKUS 'I wonder...'
    hide markus with dissolve
    'Markus sprinted forward, launching himself into the air as his wings lifted him off the ground.'
    'With an elated cry of joy, he called to me to keep up with him.'
    hide mc with easeoutright
    scene black with dissolve
    'Chasing him like some great bird in the sky, I found instinctively that sprinting after him on all fours meant that I could achieve speeds faster than any human could ever hope to.'
    $ TimeAdvBy(TIME_05H)
    'Suddenly, my tentacles slammed into the ground, throwing me along in steady motions as we crossed huge swathes of land in no time.'
    'Finally, I caught up to Markus and the two of us settled down to catch our breath.'
    scene bg_valley_of_death
    show markus_transformed at left
    show mc_transformed at right_f
    with dissolve
    MARKUS 'Ha... Not bad!'
    MC 'Markus, do you know what this means?'
    MC 'This changes everything! We can turn the tides of the war with these things!'
    MARKUS '... Heh... Let’s not get too ahead of ourselves.'
    MARKUS 'How about we just focus on {i}our{/i} plan.'
    MARKUS 'Let’s save ourselves first before we think about saving the kingd—'
    'Suddenly, we both heard the sound of a battle cry and blades loudly clashing.'
    MC '... Could it be Scouts?'
    MARKUS 'We’d have spotted them if it was.'
    MC 'Come on! Let’s take a look!'
    scene black with dissolve
    MC  'As we made our way towards the erratic sounds, we came across a group of Demorai ferociously attacking an...'
    $ AutoMus(False)
    $ PlayMusic("audio/music/21_BossBattle2.ogg")
    scene cg_ves_desert_fight
    MC '{i}Orc?{/i}'
    MARKUS 'What is an orc doing in Alderay?'
    'As one of the beasts lunged at her, she swung her axes with ferocious speed, slamming the blade through its skull as it reached out to grab her.'
    'She spun on her heels, deflecting a blow from the other before slicing through its neck and severing its head in one quick, clean cut.'
    'As she pulled her blade from the skull of the first, more Demorai descended, incensed by the bloodshed.'
    MARKUS 'What should we do?'

    menu:
        "{image=[ICON.SWORDS]} We have to help her!":
            pass
        "{image=[ICON.DEATH]} We are still at war with the Orcs... It’s not our business.":
            $ QstFromAnotherWorld().LetVesDie = True
            scene black with dissolve
            'Me and Markus hastily departed the scene, listening as we heard the clashing of blades followed by screams... {i}And then the most awful silence.{/i}'
            $ TimeAdvBy(TIME_1H)
            $ TimeAdvBy(TIME_1H)
            $ CharSetClothes("mc", "normal")
            $ CharSetClothes("markus", "normal")

            $ AutoMus(True)
            "Making our way back to Novaras, we've barely exchanged looks, let alone words."
            "Our minds racing with questions, we found ourselves in front of the city's massive walls again."
            $ LocSet("novaras_gates")
            $ LocFlush()
            show markus at left
            show mc at right_f
            with dissolve
            MARKUS "I need some time to think about all this, [player_name!t]."
            MARKUS "These {i}things{/i} inside us..."
            MC "Yeah, I think we should~"
            MARKUS "I'll take a walk. Alone."
            MARKUS "Join me later in the tavern, we'll talk."
            hide markus with easeoutleft
            "There I stood, my new inner companion keenly observing every thought drifting across my mind."
            "As I watched Markus walking towards the city gates, I couldn't help but wonder..."
            MC "...What do we do now?"
            MC "What do {i}I{/i} do now?"
            $ QstComplete(QstFromAnotherWorld)
            $ LocEnter()

    MARKUS 'But it’s an orc!'
    MC 'It doesn’t matter! They’re going to rip her apart!'
    MARKUS 'Aaargh! Fine!'
    MC 'HEY! OVER HERE!'
    MC 'As the orc spun around to look our way, the Demorai were momentarily distracted as we came hurtling towards them.'
    scene bg_valley_of_death
    show markus_transformed at cleft
    show mc_transformed at left
    show ves angry at right_f
    with dissolve
    
    MC 'For a moment, the orc drew her weapons against us, expecting us to attack her before we launched ourselves backwards and began to slash at the Demorai.'
    VES @angry'What the hell are {b}you?!{/b}'
    MARKUS 'Lady, questions later!'
    MARKUS 'FIGHTING NOW!'

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_LeftExtra = ["ves", "markus"], CharIDList_Right = ["e_demorai_scout", "e_demorai_scout", "e_demorai_scout"], CanTransform = False))

    $ AutoMus(True)

    $ TransformMC(False)
    $ TransformMarkus(False)

    MC @talk '{i}*Huff*{/i} Are you—'
    $ TimeAdvBy(TIME_05H)
    scene bg_valley_of_death
    show markus_transformed at left
    show mc_transformed at cleft
    show ves at right_f
    with dissolve
    'The orc drew her bloodied axes in our direction.'
    VES @angry 'What are you?'
    VES @angry 'Some kinds of... demons?'
    MC "We are, uhh..."
    "Me and Markus share an uncertain look of how to answer."
    MC "Not your enemy."
    MARKUS "{i}*Mumbles* Really? That was the best you could come up with?{/i}"
    MC "{i}*Mumbles* Shut the fuck up!{/i}"
    "The last thing we needed was an orc-"
    hide ves
    hide mc_transformed 
    hide markus_transformed 
    show cg_ves_crystal
    with dissolve
    $ PlaySound("audio/cfx/magic_woosh.ogg")
    "Suddenly, the strange crystal around the orc's neck began to glow."
    VES "What is-"
    "As it glowed, the crystal suddenly cracked, and as it did so, me and Markus found ourselves forcibly transformed back into human."
    hide cg_ves_crystal
    with dissolve

    $ CharAltFormUnlock("mc")
    $ CharAltFormUnlock("markus")

    $ ShowTutorialPopup("para_skills")

    ##
    scene bg_valley_of_death
    hide mc_transformed 
    hide markus_transformed 
    show markus at left
    show mc at cleft
    show ves at right_f
    with dissolve
    VES @angry "DECIEVERS!"
    MC @surprised 'Whoa! Take it easy!'
    MC @surprised 'We’re human!'
    VES @angry 'Don’t look like no humans I ever saw.'
    MARKUS @angry "What in the hell's did that crystal thing do?"
    VES @angry "It was given to me as a child."
    VES @angry "Kala's blessing to protect me from deceit!"
    "The orc's grip tightened around her axe."
    VES @angry "And now it's broken!"
    MC @surprised "H-Hold on a moment!"
    MC @talk "Look, we weren't decieving you, alright?"
    MC @think "This... secret of ours."
    MC @talk "Like you, we'd be killed if we were discovered for it."
    "The orc paused."
    VES @think "... Hmm."
    VES @talk "Let us say for a moment I believe you."
    VES @angry "{i}Why did you save me?{/i}"
    MARKUS @angry "Believe me, orc, it wasn't my idea."
    MC @talk "Because it was the right thing to do."
    "The orc paused, pondering my words."
    VES @talk "How... Virtuous."
    MC @sad "I told you, we're not your enemy."
    VES @talk "..."
    'The orc began to relax as she smirked at us both.'
    'With the uncomfortable realisation that we were both naked, we reached to cover ourselves and smiled awkwardly.'
    VES @lewd 'Nice... {i}equipment.{/i}'
    'The orc was clearly enjoying our embarrassment.'
    show markus at shake
    'Markus flushed red covering his groin before he hastily added...'
    MARKUS '... Uhh, give me one moment!'
    hide markus with easeoutleft
    'Markus transformed once again and began to fly across the desert sands, on a mission to bring us our clothes.'
    MC @talk 'Markus!'
    MC @talk 'Markus! Don’t just leave me—'
    'The orc raised a curious eyebrow, struggling to conceal her smirk as she glanced from me to the ground.'
    MC @talk '... {i}Alone.{/i}'
    VES @lewd 'What are you both really?'
    MC @talk 'We’re human.'
    VES @smile 'Yeah, and I’m Princess Cecilia.'
    MC @talk 'Okay, well... {i}kind of.{/i}'
    MC @talk 'It’s a long story.'
    VES @talk 'Why did you save me?'
    MC @talk 'I wasn’t just going to let you die!'
    VES @talk 'Your kind have had no problem with watching my kind die in the past.'
    'The orc scoffed.'
    'I shifted uncomfortably, not too sure how to answer her.'
    'Now that the battle had subsided and all was calm, I was able to get a good look at her.'
    'I’d never been this close to an orc before but having learned about them in books, it was no surprise that her skin was green and that two of her fang-like teeth were upturned and rested outside of her mouth.'
    'Half of her hair was long and black, wildly dangling down her back in a scraggly mess, while the other half of her head was shaved.'
    'She was incredibly athletic and, wearing just light desert robes, I caught glimpses of her body through the material as it shifted and moved around her shape.'
    'She had been hardened from war, with the occasional scar and scratch here and there, but both her face and curves gave her a femininity I hadn’t anticipated in a race known for its brutality.'
    VES @talk 'What are you gawking at?'
    'The orc suddenly became the one that was flushing red and looked away irritably.'
    VES @talk '... Do you mind?'
    'Looking down, I realised my growing hard-on wasn’t exactly subtle.'
    MC @talk 'Ah! Shit! Uh...'
    show markus with easeinleft:
        xalign 0.4
    'I hastened to cover myself, not wanting to offend and by some miracle Markus promptly returned as I was shuffling about and handed me some clothes.'
    MC @talk 'Thanks.'
    show ves at blurin(1.0):
        xzoom 1.0
    with dissolve
    'The orc looked away until we were fully dressed.'
    $ CharSetClothes("mc", "normal")
    show mc at nod
    MC @talk 'It’s okay to look now.'
    $ CharSetClothes("markus", "normal")
    show markus at nod
    'She turned to look back towards us then breathed out a sigh of relief.'
    show ves at blurin(1.0):
        xzoom -1.0
    with dissolve
    VES @talk '...Who are you?'
    MARKUS 'I’m Markus.'
    MC @talk 'And I’m [player_name!t].'
    VES @talk 'Why are you here?'
    MARKUS 'We came out this way to test our new forms.'
    VES @talk "...'New forms'?"
    MC @talk 'It’s... a long story, like I said.'
    VES @talk '...Hmph.'
    VES @talk 'I am Ves, of the clan Harkon.'
    $ CharMeet("ves")
    MARKUS 'And why are you here, Ves, of the clan Harkon?'
    VES @talk 'My business does not concern either of you.'
    MARKUS 'Oh, I think it does!'
    'Markus said with a rare hint of menace in his voice.'
    VES @talk 'Is that a threat?'
    MARKUS 'We both know your kind are still baying for blood!'
    MARKUS 'Even during this fucking war!'
    VES @talk '‘Baying for blood’?'
    'Ves spat back at him.'
    VES @talk 'After decades of imprisonment and slavery?'
    VES @talk 'Humiliation, genocide and rape at the hands of you human’s ‘Greater Trading Company’.'
    VES @talk 'Yet WE are the ones baying for blood?'
    MARKUS 'Those lot are nothing to do with Alderay!'
    VES @talk 'Lies! We know of your trades; you aid the slave masters wherever you can, for gold is all you humans care for!'
    VES @talk 'We will not help you win some war that does not concern us just to trade one master for another!'
    MARKUS 'Oh, how noble of you! How very fucking noble! Well, I’m glad you’ve clearly made peace with sitting back and allowing the continued mindless slaughter of innocent men, women and children!'
    MARKUS 'You’re nothing more than glorified bandits on a fucking martyrdom course!'
    'Ves scowled, the two seemed ready to fight there and then.'
    MC @talk 'Hey, hey! Both of you, settle down...'
    MC @talk 'The real enemy is the Demorai, REMEMBER that.'
    VES @talk '...{i}*Sigh*{/i}'
    MC @talk 'Do you live nearby?'
    VES @talk '...'
    MC @talk 'We mean you no harm.'
    MC @talk 'Ves answered hesitantly.'
    VES @talk 'I have my own camp, yes.'
    MC @talk 'Then let us escort you there.'
    VES @talk 'I’m fine.'
    MC @talk 'You’re hurt.'
    MC @talk 'And you have no idea how many other Demorai linger.'
    MC @talk 'Ves sized me up as she tried to decipher whether I was telling the truth or not.'
    VES @talk 'How do I know you won’t just send other humans after me once I’ve shown you the camp?'
    MC @talk 'Because you’ve seen our other forms.'
    MC @talk 'They’re just as likely to imprison or kill us as they are you.'
    VES @talk '... Fine.'
    VES @talk 'But only because you are not fully human, I lend you this trust.'
    $ CharChangeRel("ves", 1)
    'I nodded in understanding.'
    VES @talk 'Stay a few feet behind me...'
    VES @talk 'I trust neither of you THAT much.'
    'Ves began to march across the hot desert sand as Markus placed his hand on my shoulder from behind.'
    hide ves with easeoutright
    MARKUS 'And now...'
    MARKUS 'We’re willingly following her into an orc ambush... Great.'
    MC @talk 'You don’t know that.'
    MARKUS 'She’s an orc, or have you forgotten Kalliban’s first war?'
    'Markus trapsed on ahead, letting his displeasure with the situation be known with every step.'
    MARKUS 'She’s the last thing we should be trusting...'
    scene black with dissolve
    'After about twenty minutes of wandering through the hot desert, we finally arrived at Ves’ camp.'
    $ TimeAdvBy(TIME_05H)
    $ LocNameReset()
    $ LocSet("ves_camp")
    $ LocFlush()
    show ves at cright_f
    with dissolve
    show mc at cleft
    show markus at left
    with easeinleft
    'It was small but well-equipped from the outside.'
    'A large tent had been erected, with some stones cobbled together around what looked to be a hastily constructed spit roast fire that was burning in an almost cheerful manner.'
    'Littered around the place was the occasional bowl that, presumably, she kept out to gather what water she could when it rained.'
    VES @talk 'Well, this is my camp.'
    VES @talk 'Thank you for... your assistance.'
    VES @talk 'Here, take this.'

    $ PlayerAddItem("potion_heal_minor",    2)
    $ PlayerAddItem("potion_heal_regular",  1)
    $ PlayerAddItem("gold",                 125)

    VES @talk 'From my many salvage exploits in this land.'
    MARKUS 'You never told us what you’re doing all the way out here.'
    VES @talk 'I am lost from my clan.'
    MC @talk 'You mean there’s more of you?'
    MARKUS 'Oh great... more of you.'
    'Ves growled, not quite under her breath.'
    VES @talk 'I will say no more.'
    MC @talk 'Do you know where the others went?'
    VES @talk 'No... We were separated while moving camp.'
    VES @talk 'I am alone.'
    'Markus didn’t seem to entirely believe her story, but he didn’t argue with it either.'
    MARKUS 'Well, as fun as this has been...'
    MARKUS 'We must get back to Novaras soon.'
    'As Markus turned to leave, I couldn’t help but ask Ves...'
    MC @talk 'Would you mind me coming to check in on you sometime if I’m out this way?'
    VES @talk '... Why?'
    MC @talk 'I’m worried about you being out here on your own like this, it’s dangerous.'
    VES @talk 'It’s more dangerous to move in large groups.'
    VES @talk 'I am fine, I can take care of myself.'
    'Ves sighed and relented slightly.'
    VES @talk 'But...'
    VES @talk 'Do as you wish.'
    VES @talk 'I will welcome you if you come.'
    'Markus gave me a {i}look.{/i}'
    MARKUS "Okay, I'll be heading out back to Novaras."
    MARKUS "Meet me at the tavern later, [player_name!t]."
    MARKUS "We have to figure out what to do next."
    MARKUS "Goodbye."
    MARKUS "And you, orc lady."
    hide markus with easeoutleft
    "Markus left, leaving us two alone in the Valley."
    hide ves with easeoutright
    "Indifferent to me, Ves headed off to her tent and slid inside."
    MC "...Some day."
    hide mc with dissolve

    $ PlayerAddItem("potion_heal_minor",    2)
    $ PlayerAddItem("potion_heal_regular",  2)
    $ PlayerAddItem("potion_heal_large",    1)
    $ QstComplete(QstFromAnotherWorld)
    $ WorldMapLocAdd("ves_camp")
    $ ShowTutorialPopup("freeroam")
    $ LocEnter()