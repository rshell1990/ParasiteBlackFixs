label qst_bloodhound_3_safehouse_onenter:
    $ QstTheBloodhound().azulSafehouseOneOff = False
    show mc:
        xcenter 0.15
    with dissolve
    MC @talk 'Hello? Is there anyone home?'
    MC '...'
    MC "(Something's not right here, the air feels... Off.)"
    BLACK '{i}Danger...{/i}'
    MC '(Do you know something?)'
    BLACK '{i}Someone else is here...{/i}'
    MC '(I should tread carefully looking around.)' 
    $ LocEnter()

    #player from here has to click around to find the secret switch
    #Item 2 Drawing of monster
label qst_bloodhound_3_azul_monster:
    MC "(...Creepy, what is that thing?)"
    $ LocEnterQ()

label qst_bloodhound_3_fireplace:
    MC "(It's cold and a little damp... Been a while since someone used this fireplace.)" 
    $ LocEnterQ()

label qst_bloodhound_3_azul_rug:
    MC "(The man is no stranger to decoration.)"
    MC "(Hey... Looks like there is something underneath this rug.)"
    MC "(Should I?..)"
    menu:
        "Pull the rug to the side":
            MC "(Let's see...)"
            scene black with dissolve
            $ QstTheBloodhound().rugPulled = True
            "Removing the rug revealed a large, sturdy hatch underneath."
            $ LocFlush()
            with dissolve
            MC "(Huh?)"
            "I tried to open it, but it won't budge."
            MC "(Who would ever lock their own basement?)"
            $ LocEnterQ()

        "Don't":
            MC "(Nah, it really ties the room together.)"
            $ LocEnterQ()

label qst_bloodhound_3_azul_mad_ramblings:
    #Item 3 - Mad ramblings on wall 
    MC "(What's with all this paper? Had Azul lost his mind?)" 
    MC "({i}'He is watching?'{/i})"
    MC "(Was someone stalking him?)" 
    $ LocEnterQ()

label qst_bloodhound_3_azul_filthy_bed:
    #item 4 - bed
    MC "(His bed is filthy.)" 
    MC "(Spellbooks and other such things....)"
    MC "(A lot of protection spells and rituals seem to be marked.)"
    MC "(What was he trying to protect himself from?)"
    $ LocEnterQ()

label qst_bloodhound_3_azul_strange_book:
    #Item 6 - strange purple book
    MC "(Hm? This book looks odd.)"
    "As I tried to pull one of the books..."
    $ QstTheBloodhound().basementOpen = True
    play sound "audio/cfx/doorthud_muffled.ogg"
    MC "(Huh?)" 
    MC '(That sounds like it opened something.)'
    $ LocEnterQ()

label qst_bloodhound_3_azul_hatch_cant_unlock:
    MC "(The hatch is locked.)"
    $ LocEnterQ()

label qst_bloodhound_3_azul_hatch_unlock:
    MC "(Let's try this...)"
    "Pulling hard on the handle I stumbled backwards as the hatch flew open easily."
    $ PlaySoundRandom("woodenDoor")
    MC "(Whoa, okay now...)"
    $ QstTheBloodhound().basementHatchOpen = True
    $ LocEnter()

label qst_bloodhound_3_azul_basement_hatch:
    MC '(Something is down there... I can feel it.)'
    MC '(I should be prepared before heading down.)'
    menu:
        "Go":
            jump qst_bloodhound_3_toBasement
        "Not yet":
            $ LocEnterQ()

label qst_bloodhound_3_toBasement:    
    #Scene 10 - Safehouse Basement.
    scene black with dissolve
    "Heading down into the darkness with a lit torch, each step echoing as I descended down."
    $ AutoAmb(False)
    play ambience "audio/ambience_loc/cave.ogg" fadein 5.0
    "Down the stairs, I could hear the sound of dripping grow louder."
    "Through a small underground passage, I could see a light at the end of the tunnel."
    "Moving towards and peering around the corner..."
    "A nightmare awaited me."
    play sound2 ["<silence 0.25>", "audio/cfx/darkness_erupt.ogg"] volume 0.8
    $ AutoMus(False)
    $ PlayMusic("audio/music/35_CrowsNest.ogg")
    scene cg_azulcorpse with flash
    $ Pause()
    #Azul is hung upside down, his eyes torn out and his body body ritualistically desecrated in horrific fashion. 
    'The man I presumed to be Azul hung upside down, his lower jaw broken and hang by the thinnest thread of flesh.'
    'His eyes were torn out leaving red trails of blood decorating his horrified, pale face.'
    "His body desecrated, long hooks dug into the flesh pulling back sheets of flesh as a pool of blood circled his body beneath."
    'In his exposed ribcage, a crude cage was formed with sharp metal shards, inside a black crow cried as it pecked at his insides angrily.'
    MC @talk "{i}...Gods.{/i}"
    'The repugnant smell of rotting flesh began to make me nearly hurl as a dozen flies circled around the pale flesh.'
    'Behind me, I heard the sounds of some mechanism ticking...'
    scene black with dissolve
    play sound2 "audio/cfx/ticks.ogg"
    'Sensing danger, I turned.'
    show cg_mib at blurin with dissolve:
        xalign 0.55
        zoom 0.8
    'A man in black stood before me, his face not visible behind the mask and strange goggles, unnerving ticking sound coming from inside his chest.'
    'The thing moved jankily, making strange sounds as it curiously turned its head to look at me before drawing out the long blades from its arms.'
    MC @angry "I take it talking is out of the question?"
    'The thing stepped forward, its hand shaking slightly.'
    show cg_mib at blurin:
        xalign 0.58
        zoom 1.0
    play sound2 "audio/cfx/ticks.ogg"
    MC @angry 'Fuck!'
    $ PlaySoundRandom([
                "audio/battle/swordSwing/hSword-01.ogg",
                "audio/battle/swordSwing/hSword-02.ogg",
                "audio/battle/swordSwing/hSword-03.ogg",
                "audio/battle/swordSwing/hSword-04.ogg",
                "audio/battle/swordSwing/hSword-05.ogg"])
    play sound2 "audio/cfx/transform.ogg"
    'Once again, I quickly tore from my flesh just as the thing was about to strike, barely blocking it in time with my own claws and managing to push it back.'
    $ PlayMusicRandom("mus_battle_boss")
    MC 'No choice now!'

    $ QstSetProgress(QstTheBloodhound, 5)

    $ TransformMC(True)
    $ TransformMarkus(True)
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_dungeon", CharIDList_Right = ["e_man_in_black"], ContinueOnDefeat = True))

    $ TransformMarkus(False)
    $ TransformMC(False)

    scene cg_mib_fight with dissolve
    

    'Dodging left and right, the man in black moved quicker than I anticipated, dodging most of my strikes and managing to land hit after hit against me.'
    "Its blades were unlike any other blade I'd seen before."
    "Perhaps they were enchanted, but they seemed sharper and able to cut at my flesh unlike any other."
    "I managed to strike it with my tail, piercing a gaping hole through its chest."
    "But instead of turning limp, it slashed down, causing a painful wound in my tail as it continued on despite its horrific injury."
    MC "(What the fuck is this thing?!)"
    MC "(Is it even killable?)"
    "Once again, the thing leapt forward, and after a few clashes of our blades, it suddenly pierced through me with one of it's claw hands."
    'Screaming in pain, I charged forward, managing to knock the man in black against the opposing wall but it dodged my subsequent lethal swipe to take its head off.'
    'It felt like a horrific dance as the thing moved around me, taking piece after piece.'
    "I began to feel dizzy and increasingly weak..."
    "Just how much longer could I keep this up?"
    MC '(F-Fuck! Can you help me out here?)'
    BLACK 'Flee.'
    MC "(Flee?! You can't be serious!)"
    BLACK 'Cannot stabilize damage much longer.'
    BLACK 'His blades are coated with something slowing the rapid healing response.'
    MC '(Fuck! FUCK!)'
    'I looked towards the stairs once again.'
    'The man in black blocked my path, blades ready.' 
    MC '(I have to try, I just need to get past!)'
    'I darted onto the side wall, springing off from my foot to bounce off as I twisted my whole body and swung my tail to try and knock the man back.'
    'It grabbed onto my tail as I slammed it against the wall, sending shards of stone flying.'
    'The man in black refused to give up, forcing blades through my tail.'
    'I screeched out in pain but the man in black kept coming no matter what I did.'
    'Only now did I realize how close death was...'
    UNKNOWN '{i}*Whistles*{/i}'
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    'As the man in black turned sharply towards the sound, he was suddenly blasted back by a bolt of lightning.'
    'Beside Captain Nyx, four mages stood at the ready, their staffs pointed towards the convulsing automaton.'
    scene cg_azulcorpse
    show nyx at center_f
    show cg_mage as mage1:
        xcenter 0.1
        yoffset 140
        zoom 0.65
        blur 3
        matrixcolor BrightnessMatrix(-0.5)
    show cg_mage as mage2:
        xcenter 0.2
        yoffset 90
        zoom 0.75
        xzoom -1.0
        matrixcolor BrightnessMatrix(-0.1)
    show cg_mage as mage3:
        yoffset 65
        xcenter 0.6
        zoom 0.8
        matrixcolor BrightnessMatrix(-0.22)
    show cg_mage as mage4:
        xcenter 0.8
        yoffset 120
        zoom 0.7
        blur 4
        xzoom -1.0
        matrixcolor BrightnessMatrix(-0.4)
    with dissolve
    'It struggled and rose to its feet again, charging towards the Captain and the mages.'
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    show vfx_magick_glow with flash:
        anchor (0.5,0.5)
        pos (0.13,0.2)
        zoom 0.6
    hide vfx_magick_glow with dissolve
    '...But another blast sent him wheeling backwards.'
    play sound2 "audio/cfx/ticks.ogg"
    'Clambering back to its feet before they could finish it off, the man in black charged forward, dodging the third blast right through the Captain and her mages, scurrying its way up the stairs.'
    NYX @angry 'AFTER HIM!'
    MAGE 'But... What about the other one?'
    NYX @angry 'Leave him!'
    NYX @angry "{i}He's with us.{/i}"
    hide mage1
    hide mage2
    with easeoutleft
    hide mage3
    hide mage4 
    with easeoutright
    scene black with dissolve
    $ AutoAmb(True)
    'The mages followed after him as I weakly stumbled behind them deliriously, blood pouring out of me.'
    #Scene cuts to back upstairs.
    "Dizzy, I saw mages and Nyx fight the thing relentlessly."
    "After a few blows, the Man in black knocked back Captain Nyx before leaping through one of the glass windows, shattering it."
    play sound "audio/cfx/glass_shatter.ogg"
    if IsDaytime():
        scene cg_mib_jump_day with dissolve
    else:
        scene cg_mib_jump_night with dissolve
    "From outside, we watched as he contorted his body with unnatural speed, dragging himself up unto a building and moving away too fast for us to even see."
    MAGE "Captain! Do we pursue?"
    SECOND_MAGE "We need more time to prepare another charge!"
    $ LocFlush()
    show nyx angry:
        xcenter 0.25
    show cg_mage as mage1:
        zoom 0.9
        xcenter 0.55
        yoffset 50
    show cg_mage as mage2:
        xcenter 0.75
        yoffset 120
        zoom 0.8
        blur 3
        matrixcolor BrightnessMatrix(-0.1)
    NYX @angry "No... Whatever that thing is, its gone."
    'Unable to handle a single step more my buckling legs gave and I dropped to my knees.'
    show nyx shock
    'Blood poured from all over my mangled body as I crashed forward with a thud.'
    scene black with Dissolve(1.0)
    $ AutoMus(True)
    NYX "SHIT!"
    "Darkness."
    $ Pause()
    $ LocFlush()
    show nyx:
        xalign 0.45
    show cg_mage as mage1:
        xcenter 0.1
    show cg_mage as mage2:
        xcenter 0.65
        yoffset 120
        xzoom -1.0
        zoom 0.8
        blur 3
        matrixcolor HueMatrix(-20)
    with Dissolve(1.0)
    NYX @shock "...Hey, HEY! He's opening his eyes!"
    MC 'Urghh...'
    MAGE_TALL "We did our best to heal the creatures wounds but-"
    MAGE_TALL "Captain... What is this thing?"
    MAGE_SLIM "It... It looks like a man, but earlier-"
    NYX @angry 'Never you mind.'
    NYX @talk 'Now help him back to his feet!'
    scene black
    with dissolve
    'The mages weakly helped me back to my feet which trembled and shook, barely able to hold me upright.'

    $ CharSetClothes("mc", "naked")
    $ LocFlush()
    show cg_mage as mage1:
        xcenter 0.85
    show cg_mage as mage2:
        xcenter 0.7
        yoffset 120
        xzoom -1.0
        zoom 0.8
        blur 3
        matrixcolor HueMatrix(-20)
    show nyx:
        xalign 0.62
        xzoom -1.0
    show mc:
        xcenter 0.15
    with dissolve
    MC @talk '{i}*Cough*{/i} How did you-'
    NYX @talk "We will talk later, I will explain everything soon."
    'Captain Nyx turned towards the other mages.'
    show nyx at blurin:
        xalign 0.62
    NYX @angry 'None of you will speak of what you have seen today, understand?'
    'The mages look at each other sheepishly.'
    NYX @angry 'I assure you, {i}the fates will not favor you for a lack of discretion, ladies.{/i}'
    'The mages all nervously nodded.'
    show cg_mage as mage1 at nod:
        xcenter 0.85
    show cg_mage as mage2 at nod:
        xcenter 0.7
        yoffset 120
        xzoom -1.0
        zoom 0.8
        blur 3
        matrixcolor HueMatrix(-20)
    NYX @talk 'Now help me dress him.'
    show nyx at blurin:
        xalign 0.62
        xzoom -1.0
    'The Mages eyes looked downwards as their cheeks flushed red.'
    NYX @angry '...Oh for the love of-'
    NYX @blush 'Sisters... {i}Eyes up{/i} and focus.'
    scene black
    with dissolve
    jump qst_bloodhound_4_atFort