########################
# Upon entering the blacksmith's, you see he is building a female golem
label qst_BigTroubleLHamun_beshar_golem:
    if IsDaytime():
        scene cg_gela_day_broken with dissolve

    else:
        scene cg_gela_night_broken with dissolve
    
    "Entering the blacksmith's, I heard the usual pounding of the hammer as the hot, earthy scent of metal being forged filled the air."
    "There, carefully standing in the corner, chained inside a reinforced crate, was what appeared to be a woman made of gold."
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    show beshar at cleft with easeinleft
    MC @surprised "What's that?"
    BESHAR @talk "Golem."
    MC @think "What?"
    BESHAR @talk "Prototype golem."
    BESHAR @talk "See them from time to time, ancient tech from the war of the gods that still survived."
    BESHAR @talk "Most are destroyed beyond repair."
    BESHAR @talk "{i}But not this one.{/i}"
    BESHAR @talk "Dwarves from Iryiad sold it to me."
    BESHAR @think "Pretty sure the little fuckers gave a go at trying to fix it themselves then failed."
    BESHAR @talk "That's why they just decided to palm it off to me."
    MC @think "What are you doing with it?"
    BESHAR @talk "If I can replicate it somehow, I plan to sell a few, hopefully to some of the businesses around here."
    BESHAR @angry "Enough of these fucking gangs and merchant lords pushing everyone around."
    MC @think "...But?"
    BESHAR @sad "Mmm... people can devote their whole lives trying to figure out tech from that time."
    BESHAR @talk "It's just so... {i}complicated.{/i}"
    BESHAR @talk "Magecraft can be challenging enough, layered on top with interwoven technology and it's just..."
    MC @think "Complicated?"
    BESHAR @talk "Yes... But not to worry."
    BESHAR @smile "This one I am confident with."
    
    $ tmpvar = ["a"]
    menu qst_BigTroubleLHamun_beshar_golem_menu:
        "Can it fight? It looks very..." if "a" in tmpvar:
            $ tmpvar.remove("a")
            BESHAR @talk "It can fight more than well enough to clear out any would-be bandits..."
            BESHAR @think "Hells, legends foretell warlords during the reign of the old gods even used creations like these as soldiers."
            BESHAR @think "I suspect this one's primary purpose though was more for medicine than anything else."
            BESHAR @smile2 "{i}*Cough*{/i} Admittedly though, this model can also handle {i}other{/i} things."
            BESHAR @angry "... Don't look at me like that! I just followed what was written down!"
            jump qst_BigTroubleLHamun_beshar_golem_menu
        "Is it for sale?":
            pass
    $ tmpvar = {}

    BESHAR @think "This one?"
    BESHAR @talk "Maybe... Once I have what I need."
    MC @surprised "How much?"
    BESHAR @think "Normally something like this would go for over thirty thousand coins."
    MC @surprised "By the gods, man!"
    MC @surprised "What am I to do, raid the king's vault?"
    BESHAR @angry "Calm down now, boy."
    BESHAR @talk "I'm missing some vital components to finish the working models."
    BESHAR @talk "Should you accompany me to retrieve the materials I need, I'll give you a much more favorable rate."
    BESHAR @angry "I won't lie, though... getting these materials will be very dangerous."
    BESHAR @talk "There's a reason I haven't just gone to fetch them myself..."
    MC @talk "I will get back to you soon."
    "Beshar nods, resuming hammering away at a curved sword he was working on."
    $ GoalShow(QstBigTroubleLH, 2)
    $ QstBigTroubleLH().TalkedToGolemOffer = True
    MC @serious "(This could be the answer to Marbella's problem.)"
    MC @think "(Not exactly sure how she'll feel about being so indebted to me, though.)"
    MC @serious "(Still, better me than one of the other vultures.)"
    $ LocEnter()

#########################################################
## when you offer marbella to buy golem for her
label qst_BigTroubleLHamun_marbella_golem_offer:
    MARBELLA @shock "You..."
    MARBELLA @shock "YOU FUCKING WHAT?!"
    MARBELLA @sad "I... There's no way I can pay you back for a thing like that!"
    menu:
        "This is the only way that makes sense and you know it.":
            MARBELLA @sad "But—"
            "Marbella paused, her eyes nervously looking away."
            MARBELLA @sad "... There ain't no way for me to be able to pay you back for this."
            MARBELLA @sad "And I can't be giving you any more cuts of the business."
            MARBELLA @sad "Margins are thin enough as is."
            MC @bitelip "... Hmm."
            scene black with dissolve
            show marbella at center, sexy_flyby_upwards(-400) with dissolve#:
                #xcenter 0.5
            "My eyes wandered over the curvy dwarf's body."
            "Short stature aside, she had a generous chest and a great ass."
            MARBELLA @think "... W-What are you lookin' at me like that for?"
            $ LocFlush()
            show marbella at center
            with dissolve
            MC @bitelip "I can think of one way you could pay me back."
            "Marbella tilted her head, her mouth opening to speak before closing as she followed my lecherous gaze and realized what I meant."
            MARBELLA @angry "Y-You bloody what?!"
            MC @smile "Seems like a fair offer to me."
            MC @smile "I help you out, and you give me that fat ass."
            "Marbella's cheeks burned red."
            MARBELLA @angry "G-Get out!"
            MARBELLA @angry "GET THE FUCK OUT!"
            "With a shrug, I turned to leave."
            MC "Give it some thought."
            MC "The offer will still be here tomorrow!"
            scene black with dissolve
            $ LocSet("hamun_dist_docks")
            $ LocFlush(dissolve)
            show mc at center with dissolve
            "As I closed the shop door and stepped out onto the Hamun sands, I'm pretty sure I heard something smash against it behind me."
            SHYAHTAN "{i}Was that wise?{/i}"
            SHYAHTAN "This potential mate seems angry."
            $ GoalComplete(QstBigTroubleLH, 1)
            $ GoalComplete(QstBigTroubleLH, 2, Silent = True)
            # silently hide "khazahs offer" goal
            if IsGoalVisible(QstBigTroubleLH, 3):
                $ GoalHide(QstBigTroubleLH, 3, Silent = True)
            MC @smile "Give her time. I think she'll come around."
            $ GoalShow(QstBigTroubleLH, 10)
            $ QstBigTroubleLH().Kind = "dom"
            $ QstBigTroubleLH().Golem_ComeBackNextDay = True
            $ LocEnter()
        "Hmmm... Maybe you're right.":
            MARBELLA @think "There has to be another way..."
            jump qst_BigTroubleLHamun_return_to_marbella_options

label qst_BigTroubleLHamun_marbella_golem_closed:
    MC "(I should come back tomorrow, let her consider my offer.)"
    $ LocEnterQ()


#The player returns to the Crooked Shaft and Co the next day
#Upon entering
label qst_BigTroubleLHamun_marbella_golem_return_after_offer:
    show marbella at cleft 
    show mc at cright_f with easeinright
    MARBELLA @sad "..."
    MC @think "... Well?"
    MARBELLA @sad "{i}*Sigh*{/i}"
    MARBELLA @sad "I'll do it..."
    $ GoalComplete(QstBigTroubleLH, 10)
    MC @smile "I'm sorry, could you repeat that?"
    MC @smile "{i}What will you be doing exactly?{/i}"
    MARBELLA @angry "I'll be your fucking whore, you asshole!"
    MC @smile "See? Was that so hard?"
    MARBELLA @angry "Just fucking promise me you can get me one of those golems, alright?"
    MARBELLA @angry "Until then, we don't have a deal!"
    MC @smile "Then I'll return soon."
    MC @bitelip "Make sure you buy yourself some new clothes for when I return."
    MC @bitelip "Something nice to see those fat tits and ass of yours squeezed into."
    MARBELLA @emb "..."
    "Marbella's cheeks burned red. She looked like she wanted to scream at me, but she knew better."
    "I turned to leave, already looking forward to breaking Marbella in as my own private little slut."
    scene black with dissolve
    $ LocSet("hamun_dist_docks")
    $ LocFlush(dissolve)
    #Cut to outside the building
    show mc at blurin, center_f
    MC @think "(I should let Beshar know I'm ready to help him.)"
    $ GoalShow(QstBigTroubleLH, 20)
    #If Ves is in party
    if CharInParty("ves"):
        show ves at left with easeinleft
        VES @angry "Should we really be taking advantage like this?"
        show markus at right_f with easeinright
        MARKUS @smile "Seemed like a fair trade to me."
        VES @angry "Of course {i}you{/i} would think that!"
        MARKUS @angry "Need I remind you we both turn into monsters if we don't... you know."
        VES @angry "Am I to believe there aren't enough whores in this city to go around?"
        hide markus at right with easeoutright
        show sypha at right_f with easeinright
        SYPHA @happy "I fail to see the problem."
        SYPHA @smug "Such a weak mate being given the choice to decide {i}*if*{/i} she wants to become a concubine."
        SYPHA @smug "Why, it would be the curious talk of my people for weeks!"
        VES @think "Of course you'd think that way, Demorai."
    $ LocEnter()

#################################################################################################
label qst_BigTroubleLHamun_beshar_golem_commit:
    $ GoalComplete(QstBigTroubleLH, 20)
    BESHAR @talk "Good."
    BESHAR @talk "I need to prepare a few things for the journey."
    BESHAR @talk "Return here tomorrow."
    BESHAR @talk "I would suggest stocking up on supplies, if you can."
    $ GoalShow(QstBigTroubleLH, 30)
    return

label qst_BigTroubleLHamun_beshar_golem_journey_no_go:
    BESHAR @talk "No."
    BESHAR @talk "I still need to prepare a few things for the journey."
    BESHAR @talk "Return here tomorrow."
    BESHAR @talk "You should stock up on supplies too, if you can."
    return

label qst_BigTroubleLHamun_beshar_golem_journey_go:
    BESHAR @talk "Are you ready?"
    menu:
        "{image=[ICON.CLOCK]} Let's go.":
            pass # continues to temple
        "Not yet.":
            BESHAR @angry "Stop wasting time."
            BESHAR @talk "Speak with me when you are ready."
            return

    BESHAR @talk "Come then."
    $ GoalComplete(QstBigTroubleLH, 30)
    BESHAR @talk "I have a cart and driver outside. It's going to be at least a day's journey into the desert."
    scene black with dissolve
    $ GoalShow(QstBigTroubleLH, 40)
    $ LocNameSetTemp(_("Somewhere in the desert"))
    $ TimeAdvBy(TIME_2H)
    $ TimeAdvBy(TIME_2H)
    $ Pause(0.5)
    $ AutoAmb(False)
    stop ambience fadeout 0.1
    play sound "audio/cfx/horse_running.ogg"
    "A couple hours later..."
    if IsDaytime():
        scene cg_wagon_temple_travel_day with dissolve 
    else:
        scene cg_wagon_temple_travel_night with dissolve 
    "... Many hours passed as we rode through the hot desert."
    "Our cart rolled along the worn sand paths as the scorching sun beat down."
    "Only the thin tent fabric provided any relief as we passed around our waterskins to sip from."
    MC "Are you going to tell us at last where you're taking us?"
    BESHAR "It's called the Tomb of Arakan."
    MC "The what?"
    BESHAR "An ancient temple, supposedly built during the reign of the old gods."
    BESHAR "No one knows exactly what the temple was for, but I've heard rumors of strange things found there."
    BESHAR "...And if the stories are true about the people who lived back then..."
    BESHAR "Well, we'll hopefully find what we need."
    scene black with dissolve
    $ tmpvar = 12
    while (tmpvar > 0):
        $ tmpvar -= 1
        $ Pause(0.1)
        $ TimeAdvBy(TIME_1H)
    $ Pause(0.5)
    $ GoalComplete(QstBigTroubleLH, 40)
    "{i}... At last, after a long day's ride, we arrived.{/i}"

    $ AutoMus(False)
    stop music fadeout 1.0

    if IsDaytime():
        scene cg_arakan_temple_ext_day with dissolve
        $ PlayAmbience("audio/ambience_loc/desert_day.ogg")
    else:
        scene cg_arakan_temple_ext_night with dissolve
        $ PlayAmbience("audio/ambience_loc/desert_night.ogg")
    
    $ Pause()

    "There, glistening amidst the desert dunes,"
    "Half-sunk in the sands, the great Temple of Arakan remains."
    "The entranceway, a great maw of some ancient, arcane old god whom even time seems to have forgotten."
    show beshar at cleft with easeinleft
    show mc at cright_f with easeinright
    BESHAR @talk "You head on in and clear what's down there."
    MC @think "You're not coming in?"
    BESHAR @talk "I'm old... And I can't swing a hammer like I used to."
    BESHAR @talk "Afraid I'll just get myself killed down there."
    BESHAR @talk "I'll stay up here, see if I can find something of use on the surface."
    BESHAR @talk "Come get me when you've cleared out some of the floors..."
    show beshar at blurin, cleft_f
    hide beshar with easeoutleft
    show sypha at cleft with easeinleft
    MC @angry "(Great...)"
    $ GoalShow(QstBigTroubleLH, 50)
    SYPHA @think "Are you sure about this?"
    SYPHA @talk "Old gods... Even I would tread lightly in their domains."
    MC @serious "We're here now... Come on, let's go."
    scene black with dissolve

    $ LocNameReset()
    $ LocSet("qst_bigtrouble_temple_bridge")
    $ LocFlush(dissolve)

    $ AutoAmb(True)
    $ AutoMus(True)

    "Entering through the great maw, a hollow echo descended deep into the darkness as we stepped down with torches lit."
    "The hot air slowly turned cold as we descended into that black abyss for what felt like an eternity."
    "Along the walls leading downward were strange markings in a language I didn't recognize."
    MC "(Do these markings mean anything to you?)"
    SHYAHTAN "(No... This language is beyond even what I can decipher.)"
    show mc at cleft with easeinleft
    "At last, we arrived at a great hallway."
    "A massive bridge stretched across a vast chasm that led into deep darkness."
    "The bridge itself appeared to be held up by a great stone titan, bearing it upon his shoulders."
    "Decorating the walls were statues of strange creatures, each holding colossal orbs of different colors: red, blue, green, and purple."
    "There were no bodies, no signs of a great struggle."
    show mc at cright with ease
    "Only a forgotten tomb, its lips sealed, unable to tell what had come before."
    show mc at blurin, cright_f
    "... To the left and right, great ruinous archways still stood proud, with the remnants of rotting doors on both sides."
    "{i}What now?{/i}"
    $ LocEnter()

label qst_BigTroubleLHamun_temple_bridge_cantcross:
    MC "(The stone titan holds the bridge at an angle, making it impossible to cross.)"
    $ LocEnterQ()

# Left, dial room
label qst_BigTroubleLHamun_temple_dials_first_enter:
    $ QstBigTroubleLH().Golem_ShowDialsRoomFirstEnter = False
    show mc at cleft with easeinleft
    MC @talk "What is this place?"
    show markus at right_f with easeinright 
    MARKUS @talk "It looks like some kind of... sacrificial chamber?"
    show sypha at cright_f with easeinright
    SYPHA @talk "The old gods did have a rather nasty penchant for demanding blood sacrifices."
    MARKUS @think "And here I figured blood sacrifices were something you would appreciate!"
    SYPHA @talk "We value trickery and deception. It is honorable to outmaneuver your enemies."
    SYPHA @talk "To see the fear in your enemies' eyes when they realize you have outplayed them before you plunge the knife."
    SYPHA @sad "... But the old gods are different."
    SYPHA @sad "{i}They always win with their deals.{/i}"
    SYPHA @smug "And where is the fun in that for a Demorai?"
    SYPHA @happy "Where is the great {i}game?{/i}"
    MARKUS @angry "I swear you Demorai are stranger by the minute."
    SYPHA @talk "To me, you Alderians are the curiosity."
    MC @serious "Enough bickering. Let's look around."
    $ LocEnter()

#Shrines (left to right)
label qst_BigTroubleLHamun_temple_dials_shrines_1:
    "{i}A jester mask of gold and emerald, melded with fire to Prince Cashan's face so the gods could see he could not hide behind his deceptions anymore. - Boritan IV{/i}"
    $ LocEnterQ()
label qst_BigTroubleLHamun_temple_dials_shrines_2:
    "{i}Upon his weary head, King Nashur's crown of blades, a reminder of the blood paid to lay it there. - Achamon V{/i}"
    $ LocEnterQ()
label qst_BigTroubleLHamun_temple_dials_shrines_3:    
    "{i}Lord Yunitan's wife weeps as she watches her husband march to war against the gods... She knows he has already made a widow of her even while he still breathes. - {b}The name alongside it is etched out.{/b}{/i}"
    $ LocEnterQ()
label qst_BigTroubleLHamun_temple_dials_shrines_4:    
    "{i}Imatan saw the pain that was to come to the world and could take no more. Now he sleeps and dreams of a better world. - Kaina I{/i}"
    $ LocEnterQ()
label qst_BigTroubleLHamun_temple_dials_shrines_5:    
    "{i}Thalaya gifts fish to the village... the village gifts Thalaya their children to the waves. - {b}The name alongside it is etched out.{/b}{/i}"
    $ LocEnterQ()
label qst_BigTroubleLHamun_temple_dials_shrines_6:    
    "{i}Beneath restless blood moons, the wolf god Lumirar demands his pound of flesh. - Vitigo III{/i}"
    $ LocEnterQ()

label qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, MoveToIndex):
    $ QstBigTroubleLH().Golem_DialPositions_Current[DialIndex] = MoveToIndex
    $ PlaySound(audio.stone_slotted_in)
    # correct
    if QstBigTroubleLH().Golem_DialPositions_Correct[DialIndex] == QstBigTroubleLH().Golem_DialPositions_Current[DialIndex]:
        "The dial clicked into place, refusing to budge."
        MC "(Something just clicked!)"
        $ PlaySound(audio.arakan_correct)
        if QstBigTroubleLH().Golem_DialPositions_Current == QstBigTroubleLH().Golem_DialPositions_Correct:
            jump qst_BigTroubleLHamun_temple_dials_solved
    # incorrect
    else:
        if DialIndex == 1:
            "As I spin the dial and try to lock it into place, a small, sharp blade shoots out and pierces my hand!"
            $ DamagePlayer(15, Lethal = False)
            $ PlaySound(audio.blade_trap, Channel = "sound2")
            MC "FUCK!"
        elif DialIndex == 2:
            $ QstBigTroubleLH().LoseRandomPotion()
            "As I spin the dial and try to lock it into place, and as I do so, I feel one of the potions I carry shatter!"
            MC "What the fuck...?"
        elif DialIndex == 3:
            "As I spin the dial and try to lock it into place, I suddenly look down to feel some of my coins turn to sand!"
            if PlayerHasItem("gold"):
                $ PlayerRemItem("gold", min(100, PlayerItemQty("gold")), MuteSfx = True)
            MC "What the-"
        elif DialIndex == 4:
            #For a wrong answer, the party is inflicted with poison status
            "As I spin the dial and try to lock it into place, a small, hatch opened releasing a foul green smoke that made me retch!"
            MC "FUCK!"
            $ PlaySound(audio.poison_gas, Channel = "sound2")
            MC "Poison!"
            $ PoisonParty()
        elif DialIndex == 5:
            "As I spin the dial and try to lock it into place, I suddenly look down to feel some of my coins turn to sand!"
            if PlayerHasItem("gold"):
                $ PlayerRemItem("gold", min(100, PlayerItemQty("gold")), MuteSfx = True)
            $ QstBigTroubleLH().LoseRandomPotion()
            MC "What the-"
        elif DialIndex == 6:
            "As I spin the dial and try to lock it into place, a small, sharp blade shoots out and pierces my hand!"
            $ DamagePlayer(15, Lethal = False)
            $ PlaySound(audio.blade_trap, Channel = "sound2")
            MC "FUCK!"
        $ PlaySound(audio.arakan_incorrect)
        MC "(Looks like I chose wrong...)"
    return

label qst_BigTroubleLHamun_dial_move(DialIndex):
    MC "(What should I set it to?)"
    menu:
        "The masked prince":
            call qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, 1) from _call_qst_BigTroubleLHamun_golem_temple_dials_choice
        "The crown of blades":
            call qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, 2) from _call_qst_BigTroubleLHamun_golem_temple_dials_choice_1
        "The weeping widow":
            call qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, 3) from _call_qst_BigTroubleLHamun_golem_temple_dials_choice_2
        "The dreaming god":
            call qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, 4) from _call_qst_BigTroubleLHamun_golem_temple_dials_choice_3
        "The drowned man":
            call qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, 5) from _call_qst_BigTroubleLHamun_golem_temple_dials_choice_4
        "The Blood moon":
            call qst_BigTroubleLHamun_golem_temple_dials_choice(DialIndex, 6) from _call_qst_BigTroubleLHamun_golem_temple_dials_choice_5
        "Don't move it":
            pass
    return


label qst_BigTroubleLHamun_dial_altar:
    if QstBigTroubleLH().Golem_DialsSolved:
        MC "(I don't think there's anything left to do with these dials.)"
        $ LocEnterQ()
    else:    
        MC "(This altar has a stone dial on it.)"
        MC "(Six movable parts... Should I move it?)"

    menu qst_BigTroubleLHamun_golem_temple_dial:    
        "DEBUG: set all to correct" (AppearIf = config.developer):
            $ QstBigTroubleLH().Golem_DialPositions_Current = QstBigTroubleLH().Golem_DialPositions_Correct
            jump qst_BigTroubleLHamun_temple_dials_solved
        "DEBUG: set all to INcorrect" (AppearIf = config.developer):
            $ QstBigTroubleLH().RollInitialDialState()
            jump qst_BigTroubleLHamun_golem_temple_dial
        "Dial One: [QstBigTroubleLH().GetDialName(1)!t]" (AppearIf = not QstBigTroubleLH().IsDialCorrect(1)):
            call qst_BigTroubleLHamun_dial_move(1) from _call_qst_BigTroubleLHamun_dial_move
        "Dial Two: [QstBigTroubleLH().GetDialName(2)!t]" (AppearIf = not QstBigTroubleLH().IsDialCorrect(2)): 
            call qst_BigTroubleLHamun_dial_move(2) from _call_qst_BigTroubleLHamun_dial_move_1
        "Dial Three: [QstBigTroubleLH().GetDialName(3)!t]" (AppearIf = not QstBigTroubleLH().IsDialCorrect(3)):
            call qst_BigTroubleLHamun_dial_move(3) from _call_qst_BigTroubleLHamun_dial_move_2
        "Dial Four: [QstBigTroubleLH().GetDialName(4)!t]" (AppearIf = not QstBigTroubleLH().IsDialCorrect(4)):
            call qst_BigTroubleLHamun_dial_move(4) from _call_qst_BigTroubleLHamun_dial_move_3
        "Dial Five: [QstBigTroubleLH().GetDialName(5)!t]" (AppearIf = not QstBigTroubleLH().IsDialCorrect(5)):
            call qst_BigTroubleLHamun_dial_move(5) from _call_qst_BigTroubleLHamun_dial_move_4
        "Dial Six: [QstBigTroubleLH().GetDialName(6)!t]" (AppearIf = not QstBigTroubleLH().IsDialCorrect(6)):
            call qst_BigTroubleLHamun_dial_move(6) from _call_qst_BigTroubleLHamun_dial_move_5
        "Step back.":
            MC "(Perhaps the shrines might provide a clue?)"
            $ LocEnterQ()
    jump qst_BigTroubleLHamun_golem_temple_dial

label qst_BigTroubleLHamun_temple_dials_solved:
    "Upon the final dial clicking into place, the dials sank inward as they spun."
    $ PlaySound("audio/cfx/stone_slotted_in.ogg")
    "Stone ground against stone, revealing a hidden compartment."
    "Inside lay a strange circular device."
    $ QstBigTroubleLH().Golem_DialsSolved = True
    $ PlayerAddItem("qst_strange_circular_device")
    MC "What is this thing?"
    MARKUS @think "Maybe it slots into something?"
    $ LocEnter()

######################################
# Right room - Obelisk room with strange pods 
# (failed cryo pods, everyone inside is dead)
# Inspect the strange objects
label qst_BigTroubleLHamun_temple_obelisk_first_enter:
    $ QstBigTroubleLH().Golem_ShowPodsRoomFirstEnter = False
    "Peering into the strange cylinders scattered around the room, I rubbed my hand across the filthy glass to see inside."
    "Only rotten, skeletal remains lay within."
    MC @think "(What are these things?)"
    MC @think "(... Were people sleeping in them?)"
    $ LocEnter()

label qst_BigTroubleLHamun_temple_obelisk:
    menu qst_BigTroubleLHamun_temple_obelisk_menu:
        "Place the strange circular object into the slot." (AppearIf = PlayerHasItem("qst_strange_circular_device")): # if taken device from left room
            $ PlayerRemItem("qst_strange_circular_device")
            "The object slotted in perfectly."
            $ PlaySound(audio.stone_slotted_in)
            $ PlaySound("audio/cfx/ancient_generator.ogg", FadeIn = 0.1)
            "It slowly rotated once, and as it did, I heard something shift and move in the distance as a strange sound echoed throughout the temple."
            $ QstBigTroubleLH().Golem_BridgeUnlocked = True
            $ LocEnterQ()
        "Inspect the obelisk":
            "The obelisk is obsidian-black, carved with strange markings in ancient Alderian."
            "There appears to be something in the center—an open slot for something to be placed inside..."
            jump qst_BigTroubleLHamun_temple_obelisk_menu
        "Touch the obelisk.":
            MC "(Nothing happened.)"
            jump qst_BigTroubleLHamun_temple_obelisk_menu
        "Step back.":
            MC "(Maybe there's something around here I can use?)"
            $ LocEnterQ()
    
########################################
# bridge unlocked & onwards
label qst_BigTroubleLHamun_temple_bridge_cross:
    scene black with dissolve
    "... The long, silent path across the bridge led us toward a set of great, heavy doors."
    "As I touched them, something heavy shifted from within."
    $ PlaySound("audio/cfx/stone_door_open.ogg")
    "Dust and debris fell as ancient cogs began to scream and grind. Slowly, the great doors opened."
    show cg_x71_offline with dissolve
    "Inside, a mechanical man sat upon a high throne, his head bowed in the center of a vast chamber."
    "Around him lay the bones of those who came before—the garb and blades of adventurers who somehow made it this far."
    MARKUS @talk "... What in the hells is this place?"
    SYPHA @talk "Not hell... Something far older."
    show cg_x71_throne with dissolve
    $ PlaySound("audio/cfx/x71_power_up.ogg")
    OLD_GUARD "{i}Goddddd...{/i}"
    "The mechanical man spoke, his voice vibrating and warped, as though he were speaking underwater."
    "He tilted his head toward us, a single glowing blue eye staring forward. There was no mouth to speak of."
    OLD_GUARD "{i}Why... are you silent now, god?{/i}"
    OLD_GUARD "{i}I cannot hear you anymore.{/i}"
    OLD_GUARD "{i}Godddd...{/i}"
    OLD_GUARD "{i}Have... we... won?{/i}"
    OLD_GUARD "{i}Are we free?{/i}"
    $ tmpvar = ["a", "b"]
    menu qst_BigTroubleLHamun_temple_bridge_cross_menu:
        "Who are you?" (AppearIf = ("a" in tmpvar)):
            OLD_GUARD "{i}... I was called X-71.{/i}"
            OLD_GUARD "{i}But I was named Centaurian by god.{/i}"
            MC "Are you... some kind of golem?"
            "The mechanical man did not answer."
            $ tmpvar.remove("a")
            jump qst_BigTroubleLHamun_temple_bridge_cross_menu
        "What is this place?" (AppearIf = ("b" in tmpvar)):
            OLD_GUARD "{i}An outpost.{/i}"
            MC "An outpost for what?"
            OLD_GUARD "{i}The war... The great war.{/i}"
            OLD_GUARD "{i}Has it been so long?{/i}"
            $ tmpvar.remove("b")
            jump qst_BigTroubleLHamun_temple_bridge_cross_menu
        "What god do you speak of?":
            pass
    $ tmpvar = {}
    OLD_GUARD "{i}The rebel god.{/i}"
    OLD_GUARD "{i}The dark king who showed us the way.{/i}"
    MC @serious "... You mean Malakai, don't you?"
    OLD_GUARD "..."
    OLD_GUARD "{i}Why have you come to this place?{/i}"
    menu:
        "I've been sent to deliver you new orders.":
            OLD_GUARD "New... orders?"
            menu:
                "The war is won. Malakai is victorious." (Req_Charm = 22):
                    OLD_GUARD "Then why is god silent?"
                    MC @talk "He is not silent. He sent me to deliver your orders."
                    MC @talk "{i}Unless you dare question the will of Malakai?{/i}"
                    OLD_GUARD "... What would god ask of me?"
                    menu:
                        "You are to help clear the roads of bandits.":
                            OLD_GUARD "{i}... For how long?{/i}"
                            MC @talk "Until god commands you otherwise."
                            scene cg_x71_throne_rise with dissolve
                            $ PlaySound("audio/cfx/earthy_rustle.ogg")
                            "The mechanical man rose to his feet, dust cascading from his frame as he stepped forward."
                            scene cg_arakan_temple_throne with dissolve
                            show mc at cleft with easeinleft
                            show markus at left with easeinleft
                            show cg_x71 at cright with easeinright
                            OLD_GUARD "{i}As god commands.{/i}"
                            "Each step thudded against the stone floor, wheels and cogs spinning within him."
                            hide cg_x71 with easeoutright
                            "I watched as the mechanical man marched out to carry out my orders."
                            MARKUS @think "... Are you sure that was a good idea?"
                            MC @talk "It was all I could think of on the spot."
                            MC @talk "Besides, he'll be busy for a long time with that order." 
                            $ QstBigTroubleLH().Golem_X71Fate = "fight_bandits"
                        "Your duty is at an end, soldier... Find the nearest town and forge a new life for yourself.":
                            OLD_GUARD "{i}A new... life?{/i}"
                            OLD_GUARD "{i}What am I to do with this life?{/i}"
                            MC @talk "Help the people of whatever town or village you find. Protect them."
                            MC @talk "And learn what it means to live."
                            OLD_GUARD "..."
                            scene cg_x71_throne_rise with dissolve
                            $ PlaySound("audio/cfx/earthy_rustle.ogg")
                            "The mechanical man rose to his feet, dust cascading from his frame."
                            scene cg_arakan_temple_throne with dissolve
                            show cg_x71 at cright with easeinright
                            show mc at cleft with easeinleft
                            show markus at left with easeinleft
                            OLD_GUARD "{i}As god commands.{/i}"
                            "Each heavy step echoed as wheels and cogs spun within him."
                            hide cg_x71 with easeoutright
                            "I watched as the mechanical man marched away to carry out my orders." 
                            $ QstBigTroubleLH().Golem_X71Fate = "forge_life"
                    show sypha at cright_f with easeinright
                    SYPHA @talk "We should head back to the surface. Beshar should be waiting for us."
                    scene black with dissolve
                    #### to outside
                    BESHAR @scared "What in the hells happened down there?"
                    BESHAR @scared "Some kind of machine man came marching out like he was on a mission!"
                    MC @talk "I wouldn't worry about him."
                    MC @talk "The temple should be safe now for you to head down."
                    jump qst_BigTroubleLHamun_temple_conclusion
                "You are, uhh... to rest easy from now on.":
                    OLD_GUARD "{i}... Lies.{/i}"
                    MC @think "What?"
                    MC @scared "No, I—"
                    OLD_GUARD "{i}LIES.{/i}"
                    OLD_GUARD "{i}Arda has sent you!{/i}"
                    scene cg_x71_throne_rise with dissolve
                    "The mechanical man rose to his feet, dust falling from him as he descended the steps of his throne."
                    scene cg_arakan_temple_throne with dissolve
                    show mc at cleft with easeinleft
                    show markus at left with easeinleft
                    show cg_x71 at cright with easeinright
                    MC @scared "... Shit."
                    OLD_GUARD "{i}Die.{/i}"
                    # to fight
        "We came to explore the ruins.":
            OLD_GUARD "{i}... Thieves.{/i}"
            MC @think "What? No."
            MC @angry "This temple is abandoned!"
            scene cg_x71_throne_rise with dissolve
            $ PlaySound("audio/cfx/earthy_rustle.ogg")
            "The mechanical man rose to his feet, descending from his throne."
            scene cg_arakan_temple_throne
            show mc at cleft with easeinleft
            show markus at left with easeinleft
            show cg_x71 at cright with easeinright
            MC @angry "The war is over! Malakai lost!"
            OLD_GUARD "{i}... It is not over.{/i}"
            OLD_GUARD "{i}Not while I yet live.{/i}"
            MARKUS @scared "... Oh fuck me!"
            OLD_GUARD "{i}Die.{/i}"
            # to fight
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData("pbat_arakan_temple_throne", CharIDList_Right = ["e_x71"]))
    scene cg_arakan_temple_throne
    show cg_x71 at center
    with dissolve
    $ QstBigTroubleLH().Golem_X71Fate = "dead"
    show cg_x71 at shake
    $ PlayMusic("audio/music/9_Burned_T.ogg")
    $ PlaySound("audio/cfx/machine_glitch.ogg")
    OLD_GUARD "Systems... failing..."
    OLD_GUARD "Auxiliary power offline."
    OLD_GUARD "Can't..."
    OLD_GUARD "Reboot-"
    scene black with dissolve 
    OLD_GUARD "{i}Power...{/i}"
    $ PlaySound("audio/cfx/heavy_fall.ogg")
    scene cg_x71_dead with dissolve
    "Stumbling backward with a tremendous crash, the mechanical man slammed into the stone floor, cracking it beneath him."
    "The light in his eye flickered as it began to fail."
    OLD_GUARD "{i}God...{/i}"
    OLD_GUARD "{i}What was...{/i}"
    scene cg_x71_dead with dissolve
    $ PlaySound("audio/cfx/x71_power_off.ogg")
    "The eye went dark one final time."
    OLD_GUARD "{i}It all for?{/i}"
    "The old soldier fell silent. His war over at last."
    $ Pause(0.5)
    scene cg_arakan_temple_throne with dissolve
    show mc at cleft with easeinleft 
    show sypha at right_f with easeinright
    MC @sad "..."
    SYPHA @sad "[player_name!t]."
    SYPHA @sad "It was him or us."
    MC @sad "I know, it's just..."
    show kiara at center with easeinleft
    KIARA @sad "Sometimes we are done with the wars we fight."
    KIARA @sad "{i}But those wars may not be done with us.{/i}"
    SYPHA @talk "We should leave this place."
    SYPHA @talk "Beshar is waiting."
    MC @sad "Right..."
    scene black with dissolve

    $ AutoAmb(False)
    stop ambience fadeout 0.1
    if IsDaytime():
        scene cg_arakan_temple_ext_day with dissolve
        $ PlayAmbience("audio/ambience_loc/desert_day.ogg")
    else:
        scene cg_arakan_temple_ext_night with dissolve
        $ PlayAmbience("audio/ambience_loc/desert_night.ogg")
    
    show mc at cleft with easeinleft
    BESHAR @talk "Are you all alright?"
    show beshar at cright_f with easeinright
    BESHAR @talk "I heard some commotion from down there..."
    MC @talk "Everything's fine."
    MC @talk "You should be safe to head down to the temple now."
    jump qst_BigTroubleLHamun_temple_conclusion

label qst_BigTroubleLHamun_temple_conclusion:
    BESHAR @talk "Alright, I'll head on down."
    BESHAR @talk "I'll be back in a few hours... Rest easy here."
    scene black with dissolve
    "... For the next couple of hours, we sat and waited for Beshar's return."
    $ GoalComplete(QstBigTroubleLH, 50)
    
    $ AutoAmb(False)
    stop ambience fadeout 0.1
    if IsDaytime():
        scene cg_arakan_temple_ext_day with dissolve
        $ PlayAmbience("audio/ambience_loc/desert_day.ogg")
    else:
        scene cg_arakan_temple_ext_night with dissolve
        $ PlayAmbience("audio/ambience_loc/desert_night.ogg")

    show mc at cleft with easeinleft
    show beshar at cright_f with easeinright
    "He eventually re-emerged, sacks full of items that he loaded onto the wagon one by one."
    BESHAR @talk "That should be all of it."
    MC @think "Do you have the parts we need?"
    BESHAR @talk "Aye. For your golem, we do."
    BESHAR @talk "Time to head back to Hamun."
    scene black with dissolve
    $ tmpvar = 16
    while (tmpvar > 0):
        $ tmpvar -= 1
        $ Pause(0.1)
        $ TimeAdvBy(TIME_1H)
    $ Pause(0.5)
    $ tmpvar = {}
    "... The journey back was long, but eventually we arrived at the gates of Hamun and were let back inside its walls."
    $ LocSet("hamun_dist_docks")
    $ Pause(0.25)
    $ LocFlush(dissolve)
    $ AutoMus(True)
    $ AutoAmb(True)
    BESHAR @talk "Come see me tomorrow when you have a chance."
    BESHAR @talk "We have much to discuss."
    $ GoalShow(QstBigTroubleLH, 60)
    $ LocEnter()


############################################################################################################################
# come back later after returning from temple
label qst_BigTroubleLHamun_golem_beshar_not_ready_after_return:
    BESHAR "Come back tomorrow."
    BESHAR "I still need to set some things up."
    return

#Upon returning to the Hamun blacksmith's (the next day)
label qst_BigTroubleLHamun_golem_beshar_pay:
    show mc at cleft with easeinleft
    show beshar at cright_f with easeinright
    BESHAR @talk "Ah, there you are."
    $ GoalComplete(QstBigTroubleLH, 60)
    BESHAR @talk "Hmm... These parts will do nicely."
    BESHAR @talk "Well, there's still the matter of my fee to produce this thing for you."
    BESHAR @talk "Four thousand should suffice."
    menu qst_BigTroubleLHamun_golem_beshar_pay_menu:
        "Here is your coin." (Req_Gold = QstBigTroubleLH().Golem_FinalPrice):
            pass
        "Come on now, I've just risked my life and my companions to get you these materials." (AppearIf = (QstBigTroubleLH().Golem_NegotiatedBetterDeal == False), Req_Charm = 12):
            BESHAR @think "Hmph."
            BESHAR @talk "Three and a half thousand, not a coin less."
            BESHAR @talk "And only because I may need your sword again one day."
            $ QstBigTroubleLH().Golem_NegotiatedBetterDeal = True
            $ QstBigTroubleLH().Golem_FinalPrice = 3500
            jump qst_BigTroubleLHamun_golem_beshar_pay_menu
        "Perhaps I should tell others that the Temple of Arakan is now ripe for looting since I cleared it out?" (AppearIf = (QstBigTroubleLH().Golem_NegotiatedBetterDeal == False), Req_Barter = 14):
            MC @smile "I wonder what they'll pay to salvage that temple bone-dry of its lost wonders?"
            BESHAR @angry "Hmph..."
            BESHAR @angry "Fine, two thousand eight hundred, and you don't breathe a word about Arakan to anybody."
            BESHAR @angry "That is my final offer. Any lower than that, and I earn nothing."
            $ QstBigTroubleLH().Golem_NegotiatedBetterDeal = True
            $ QstBigTroubleLH().Golem_FinalPrice = 2800
            jump qst_BigTroubleLHamun_golem_beshar_pay_menu
        "I will return when I have the money.":
            BESHAR @talk "Very well."
            BESHAR @talk "Once I am paid my fee, I can begin work immediately."
            $ GoalShow(QstBigTroubleLH, 65)
            $ LocEnter()
    $ PlayerRemItem("gold", QstBigTroubleLH().Golem_FinalPrice)
    if IsGoalVisible(QstBigTroubleLH, 65):
        $ GoalComplete(QstBigTroubleLH, 65)
    BESHAR @talk "I'm going to need a day or two to sort through this stuff."
    BESHAR @talk "Come back then, and I'll have your golem ready."
    $ GoalShow(QstBigTroubleLH, 70)
    $ LocEnter()

# building in progress
label qst_BigTroubleLHamun_golem_beshar_build_inprog:
    BESHAR "Not yet."
    BESHAR "I am still working on it."
    BESHAR "Come back another day."
    return

# return when golem ready
label qst_BigTroubleLHamun_golem_beshar_build_over:
    show mc at cleft with easeinleft
    show beshar at cright_f with easeinright
    BESHAR @talk "Ahh, there you are."
    $ PlaySound("audio/cfx/whistle_call_2.ogg")
    BESHAR "{i}*Whistles*{/i}"
    $ GoalComplete(QstBigTroubleLH, 70)
    show gela at center_f with easeinright
    "There, a machine made of what looked like solid gold, shaped like a beautiful woman, stepped forward."
    "Enchantments on her body hummed and glowed as the creature looked toward Beshar."
    BESHAR @talk "This here's your next master."
    "The golden woman turned its head toward me, the cogs spinning as it did so."
    GELA @talk "What am I to be called, Master?"
    $ gela_ref = renpy.input(_("What is she to be called?"), default = _("Gela"))
    $ GELA = Character(gela_ref, image = "gela")
    GELA @horny "[gela_ref!t]... Name confirmed...{i}Master.{/i}"
    MC @think "(That was a little more sultry than I was expecting just now...)"
    GELA @talk "What now, Master?"
    MC @talk "Head to the Crooked Shaft and Co. It is a building in Hamun run by a dwarf named Marbella. Do you know it?"
    GELA @talk "Yes. This information has been provided to me."
    MC @smile "Good. You are to protect that building and its owner, Marbella, from anyone who might do it harm."
    GELA @talk "Yes, Master."
    GELA @talk "I shall head over there now."
    hide gela with easeoutleft
    "The cogs spun as the woman left, making her way toward the store."
    show mc at blurin, cleft_f
    MC @think "Will she be alright walking alone like that?"
    show mc at blurin, cleft
    BESHAR @smile "I pity any fool who tries to get between a golem and its orders."
    BESHAR @talk "And with that, our business is concluded."
    BESHAR @talk "Come back if you need anything else."
    $ GoalShow(QstBigTroubleLH, 80)
    $ LocEnter()

################################################################################################################################
label qst_BigTroubleLHamun_golem_return_to_marbella:
    show marbella at cleft
    show gela at center_f
    with dissolve
    show mc at cright_f with easeinright
    MARBELLA @shock "W-Wha..."
    MARBELLA @shock "What the bloody hells is this thing?!"
    $ GoalComplete(QstBigTroubleLH, 80)
    "Marbella circled the motionless, golden woman in the middle of her office."
    GELA @talk "I am [gela_ref!t]. I am a golem assigned by my master to protect you and this property."
    MARBELLA @think "You don't look like you're much used in a scrap?"
    $ CharSetClothes("gela", "blades")
    GELA "Combat is not my primary function, but it is one of them all the same."
    MARBELLA @shock "HOLY-"
    MARBELLA @scared "U-Uhhh, alright then...."
    GELA @talk "Do you have any secondary orders for me?"
    MARBELLA @talk "U-Uhh, no."
    MARBELLA @talk "Do your thing, I guess?"
    $ CharSetClothes("gela", "normal")
    GELA @talk "Of course. I shall patrol the perimeter."
    show gela at blurin, center
    hide gela with easeoutright
    $ QstComplete(QstBigTroubleLH)
    "[gela_ref!t] made her way toward the door, ready to patrol, as Marbella's eyes now nervously settled on me."
    MARBELLA @concern "S-So... You, uhh..."
    MARBELLA @concern "{i}About that deal.{/i}"
    show mc at center_f with ease
    "I stepped closer."
    MARBELLA @concern "Y-You're serious?"
    MC @smile "I am."
    MARBELLA @angry "F-Fucking hells, man!"
    MARBELLA @sad "Why?"
    MARBELLA @angry "I'm a bloody dwarf!"
    MARBELLA @angry "If the boys found out I was fucking you to keep this place safe, how are they supposed to take me seriously as a boss?"
    MC @angry "{i}Because I'll snap their fucking joints if they don't?{/i}"
    MARBELLA @shock "... G-Gods, man, what's gotten into you?"
    MC @smile "{i}If you're my woman, you speak with my authority.{/i}"
    MC @smile "{i}So if they disrespect you, they're disrespecting me.{/i}"
    MC @talk "{b}Am I clear?{/b}"
    MARBELLA @concern "... Y-Yes."
    MARBELLA @concern "You're clear."
    "Marbella's cheeks burned red as she nervously averted her gaze."
    MARBELLA @emb "... Well... What do you want then?"
    MARBELLA @emb "Let's get this over with already!"
    label replay_marbella_dom_titjob_first:
    MC @smile "Did you buy your outfit like I asked?"
    $ AutoMus(False)
    $ AutoAmb(False)
    stop ambience fadeout 0.5
    $ PlayMusicRandom("mus_sex")
    "Marbella froze, the blood draining from her face."
    MARBELLA @sad "I... I forgot."
    scene black with dissolve
    MC @smile "I see."
    play sound2 "audio/cfx/transform.ogg"
    "From my back, two tentacles sprang out, grabbing hold of Marbella as they tore and pulled off her clothes."
    $ PlaySexFx(audio.adara_hj_loop, 1)
    scene marbella_dom_titjob_nopreg_1 with dissolve
    $ Pause()
    MARBELLA "AHH!"
    MARBELLA "W-Wait a minute!"
    MARBELLA "What are you doing, mate?!"
    MARBELLA "Eeeeeeep!"
    "Suspended in the air, my tentacles wrapping and restraining her, she wiggled as she looked back, eyes wide."
    scene marbella_dom_titjob_nopreg_2 with dissolve
    $ Pause()
    "With a sharp swipe of my hand, I watched as her ass jiggled with the impact as she yelped in shock."
    MARBELLA "O-Oi!"
    MARBELLA "That's my butt, you—"
    "My hand swiped out again, colliding against the other cheek as she let out another startled gasp."
    MC "It's {i}my{/i} ass now."
    MARBELLA "B-Bastard!"
    "A third tentacle appeared, slapping across Marbella's tits as she let out a sharp moan."
    MC "It sounds to me like someone's enjoying this more than they let on."
    MARBELLA "F-Fuck off, mate!"
    MARBELLA "You can't just—"
    "As I spanked her ass once again, she gasped."
    "But before she could argue back, my tentacles whipped across her tits in a frenzy, leaving light pink marks in their wake."
    MARBELLA "F-Fuckkk...!"
    MC "What was that you said?"
    MC "I can't what now?"
    MARBELLA "{i}*Huff*{/i} I'm not— {i}*Huff*{/i} some toy— {i}*Huff*{/i} You can—"
    "I slapped across her ass once more, watching with delight as her cheeks turned a deeper shade of red."
    MC "I."
    "*{b}Smack!{/b}*"
    MC "OWN."
    "*{b}Smack!{/b}*"
    MC "THIS."
    "*{b}Smack!{/b}*"
    MC "FAT."
    "*{b}Smack!{/b}*"
    MC "ASS!"
    "*{b}Smack!{/b}*"
    "Marbella stopped arguing back. Between her legs glistened her cunt's juices as she let out low, trembling breaths."
    MARBELLA "{i}*H-Huff!* *Huff!*{/i}"
    MC "Have you learned your lesson yet, Marbella?"
    MARBELLA "..."
    MC "Still being disobedient, hm?"
    MC "No matter... I have just the solution!"
    scene marbella_dom_titjob_idle with dissolve
    $ Pause()
    "Marbella gasped as I pinned her down onto the table, shoving my cock between her tits."
    MARBELLA "W-What the fu—"
    scene marbella_dom_titjob_3 with dissolve
    $ Pause()
    "With both hands, I pushed her tits together as I began to fuck them, sliding my cock between her soft, heavy mounds."
    MC "Spit on it."
    MARBELLA "F-Fuck's sake, mate! Can you— Ahh! Take it e-easy before I—"
    "A soft moan escaped Marbella's lips once again as she squirmed beneath me."
    MARBELLA "M-Mmmhhhfff!"
    MC "Enjoying yourself?"
    MARBELLA "A-Ahh! F-Fuck you!"
    "Her soft moans and grunts continued for some time as I fucked her tits."
    "Every so often, her gaze would meet the head of my cock as she'd spit on it."
    MARBELLA "{i}Spits!{/i}"
    MARBELLA "T-There!"
    MARBELLA "Happy now, ya perverted monster fuck?"
    scene marbella_dom_titjob_4 with dissolve
    $ Pause()
    "I squeezed her tits as the warm spit acted as a nice lube."
    MC "I'll be happy when you call yourself my little dwarven slut."
    MARBELLA "N-Never going to happen, fucker!"
    "As her tits bounced with my cock slamming between them, another forced, hot moan escaped her lips."
    MARBELLA "O-Ooooooh...."
    "She bit at her lower lip, her body betraying her faux protests as she did her best to avert her gaze."
    "Her cheeks burning hotly as her quiet, heavy breathing continued."
    "My balls began to swell as I felt the need to paint her tits and face in my cum grow with each thrust."
    MC "{i}Huff{/i} You ready— {i}Huff{/i}"
    MC "To get marked, my little slut?"
    "With one last bit of defiance, Marbella grunted through gnashing teeth."
    MARBELLA "D-Do your worst, you fu—"
    $ PlaySexFx(audio.adara_hj_finish)
    scene marbella_dom_titjob_finish with flash
    $ UnlockGalSceneAndGrantXp("marbella", "dom_titjob")
    $ ReduceInfectionFromSex("marbella")
    $ Pause()
    "I pressed and squeezed her tits together, ramming my cock forward as I grunted, painting her face and tits in my thick, white seed."
    MC "HRGHHHHHH!"
    MARBELLA "{i}Gasp!{/i}"
    "As the last of my hot seed splashed onto her face and tits, Marbella stared bewildered."
    "As though she couldn't believe what just happened."
    MARBELLA "Y-You..."
    MARBELLA "{i}Are you fucking part horse or something?{/i}"
    MC "{i}Huff{/i} Your tits are amazing."
    $ StopReplay()
    "As I pulled my cock away and began to buckle up my clothes, a blushing Marbella scooped some of the cum from her tits."
    $ CharSetClothes("marbella", "cumcovered")
    $ LocFlush()
    show marbella at cright_f
    show mc_transformed at cleft 
    with dissolve
    MARBELLA "... F-Fucking hells."
    MARBELLA "I don't know if I'm ever going to get used to seeing you like that."
    MC "I'm waiting for a 'thank you for fucking my tits.'"
    MARBELLA "No fuckin' chance!"
    MC "Feisty, aren't we?"
    MC "Don't worry, this is just a warm-up for what's to come."
    "Her legs trembling, she sheepishly turned to look towards me."
    MARBELLA "..."
    $ AutoMus(True)
    MC @talk "Next time, have an outfit prepared."
    "Without another word, I turned and left, leaving Marbella to contemplate my words as she rubbed at her stinging ass."
    $ LocSet("hamun_dist_docks")
    hide mc_transformed with easeoutright
    MARBELLA "B-Bastard!"
    MARBELLA "..."
    show marbella at nod
    MARBELLA "Urgh, now to just wipe it off my face at least."
    MARBELLA @angry "FUCK! A little just went in my mouth!"
    MARBELLA @emb "..."
    MARBELLA @emb "...N-Not bad."
    show marbella at shake
    MARBELLA @angry "BAHH! What am I doing?!"
    # quest complete, prompts dom romance w/her
    scene black with dissolve
    $ AutoAmb(True)
    $ CharSetLover("marbella")
    $ CharSetClothes("marbella", "normal")
    $ LocEnter()


