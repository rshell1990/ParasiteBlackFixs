label rom_marbella_shared_the_face:
    ###########################################################################################################
    #Domination route 8 - Hamun city map - night time
    # if khazah
    show mc at cleft with easeinleft
    if RomanceMarbella().Kind == "gang":
        SHYAHTAN "(I have its scent.)"
        MC @think "(You mean whatever's killing the Khazah?)"
        SHYAHTAN "(We can pursue it... should you wish.)"
    elif RomanceMarbella().Kind in ["dom", "love"]:
        SHYAHTAN "(I have its scent.)"
        SHYAHTAN "(We should pursue.)"

    menu:
        "Pursue the creature.":
            pass
        "Do nothing.":
            SHYAHTAN "(The creature will return to hunt another night, no doubt...)"
            if RomanceMarbella().Kind in ["dom", "gang", "love"]:
                $ RomanceMarbella().Shared_TheFaceRefusedHuntPromptTonight = True
            $ LocEnter()

    # cont. from "pursue"
    hide mc with easeoutright
    "The scent was thick with heavy blood. Had the creature found a victim?"
    "What even was it?"
    $ AutoMus(False)
    $ PlayMusic("audio/music/35_CrowsNest.ogg")
    scene cg_the_face_intro with dissolve
    "Down the dark alleyways, kicking up cold sand, I turned a corner to see... {i}it.{/i}"
    "A woman — a prostitute — pressing a man up against a wall."
    "Her red lips were pressed to his throat, his eyes rolled back, his face deathly white."
    "The creature snapped her neck toward me, revealing the huge, gaping wound in the man's neck and the blood splattered around her mouth."
    "Her eyes glowed yellow as she inched closer, taking in a deep inhale."
    "Before I knew it, the fleshy skin of the woman dropped to the floor as though it was a suit... her severed head rolling along the floor."
    "The creature... The real creature, perhaps sensing something was {i}different{/i} about me too,"
    "appeared before me in all it's hideous, terror."
    $ LocFlush()
    show cg_theface at right_f
    show mc at cleft
    with dissolve
    THE_FACE "You're not human."
    THE_FACE "At least not fully... Who are you?"
    THE_FACE "{i}... What are you?{/i}"
    $ tmpvar = ["a", "b"]
    menu rom_marbella_shared_the_face_menu:
        "I could ask you the same thing." (AppearIf = ("a" in tmpvar)):
            $ tmpvar.remove("a")
            "The creature grinned."
            THE_FACE "I'm you."
            THE_FACE "I'm them."
            THE_FACE "I'm whatever face I wear."
            jump rom_marbella_shared_the_face_menu
        "You... You remind me of the things I saw in Novaras during the siege." (AppearIf = ("b" in tmpvar)):
            $ tmpvar.remove("b")
            THE_FACE "Cheap imitations."
            THE_FACE "Toys of the one called Zanarak."
            "The face grinned."
            THE_FACE "We are older."
            MC @think "Is there many of you left?"
            THE_FACE "I have not sensed another of my kind in over four-hundred years."
            MC @think "... Then maybe you're the last?"
            "The creature grinned."
            THE_FACE "{i}No.{/i}"
            jump rom_marbella_shared_the_face_menu
        "I am [player_name!t]":
            # cont
            pass
    # cont 
    THE_FACE "And what do you want... [player_name!t]?"
    if RomanceMarbella().Kind in ["dom", "love"]:
        SHYAHTAN "{i}To eat you.{/i}"
        MC "(Gods be damned, man! Why would you blurt that out?!)"
        THE_FACE "... Interesting."
        THE_FACE "Then let me make you an offer."
        THE_FACE "I will give you a piece to eat if you leave me alone."
        MC "... What?"
        MC "(This thing is unnerving as all seven hells.)"
        MC "(Should we take its offer?)"
        MC "(Will a piece of it be enough?)"
        SHYAHTAN "(Yes.)"
        "My eyes drifted toward the poor bastard the creature was devouring."
        SHYAHTAN "(That is, if you are fine with letting this creature continue what it's doing...)"
    # if khazah
    elif RomanceMarbella().Kind == "gang":
        MC @talk "You to leave this city."
        THE_FACE "And why would I do that?"
        MC @talk "You've preyed on the wrong people. They sent me to deal with you, one way or another."
        THE_FACE "And why should I not just kill you... and then kill them?"
        THE_FACE "I rather like this hunting ground."
    ### variants over

    menu:
        # only in gang/khazah variant, & Charm 17 
        "More will come... People are beginning to notice."(AppearIf = (RomanceMarbella().Kind == "gang"), Req_Charm = 17): 
            THE_FACE "I can always find a new face to wear."
            MC @serious "But whatever the hells you are, you need to feed."
            MC @think "The bodies are stacking up. It won't be long before the merchant lords hire inquisitors or someone worse."
            MC @talk "Then it's only a matter of time."
            "The creature seemed to contemplate my words."
            THE_FACE "... Hm."
            THE_FACE "Perhaps it is time I found a new hunting ground."
            jump rom_marbella_shared_the_face_negotiate

        # only in dom variant
        "Let the creature go." (AppearIf = (RomanceMarbella().Kind in ["dom", "love"])):
            $ RomanceMarbella().Shared_TheFaceFate = "negotiated"
            "The creature grinned as it ripped off its arm and threw it toward me."
            "Strange tendrils still writhed from the open flesh wound."
            MC @scared "... What. The. Fuck."
            THE_FACE "A wise choice."
            jump rom_marbella_shared_the_face_negotiate

        "Sorry, I can't let you hurt anyone else.":
            $ RomanceMarbella().Shared_TheFaceFate = "dead"
            THE_FACE "... Wearing your skin is going to be fun."
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData("pbat_hamun_street_night", CharIDList_Right = ["e_the_face"]))
            "With a death rattle, the creature writhed on the ground in agony."
            "A pool of blood spread from its wounds until at last it lay still."
            $ LocFlush()
            show mc at cleft
            with dissolve
            MC @scared "(... What in the hells was that?)"
            $ AutoMus(True)
            if RomanceMarbella().Kind == "gang":
                SHYAHTAN "(Just another predator trying to survive.)"
                MC @think "(Well... I should head back to the Khazah at least.)"
            elif RomanceMarbella().Kind in ["dom", "love"]:
                SHYAHTAN "(Food.)"
                MC @angry "(Is that really all you can think about?!)"
                "I felt my own hand fight against me, rising toward the creature's body."
                "Black tendrils pushed out, wrapping around and inspecting the corpse."
                "Suddenly, one of the tendrils pierced the flesh, draining it until, within moments, it became a withered husk."
                MC @talk "Uhh, you got what you needed?"
                SHYAHTAN "Yes."
                SHYAHTAN "Now we can return to our mate tomorrow."
                MC "Right..."
            jump rom_marbella_shared_the_face_end

label rom_marbella_shared_the_face_negotiate:
    scene cg_the_face_swap with dissolve
    "To my horror, I watched as the creature made short work of the man, stuffing it's face with his inards before turning it's gaze back towards the lifeless body of the woman."
    "Clambering back inside of her, the skin stretching over the flesh unnaturally, and then, it began to settle over the the strange creature's body as it contorted itself into shape."
    "Bones breaking and snapping into place as the creature shrink, fitting itself inside of her."
    "It grabbed the severed head, with tendrils protruding from the open wound of the neck and connected the head there, almost as if it was screwing the head back on."
    "From the open wound where his head had been, the lifeless face moved once more."
    "In a few gory moments, sinew, flesh, and skin covered all wounds."
    "The eyes opened."
    "{i}It looked like a normal woman.{/i}"
    $ LocFlush()
    show theface_humanoid at cright_f
    show mc at cleft
    with dissolve
    "It smiled at me."
    THE_FACE @smile "Now I take my leave."
    THE_FACE @smile "Perhaps we will meet again one day?"
    THE_FACE "You are..."
    THE_FACE @smile "{i}Interesting.{/i}"
    MC @talk "You never told me your name."
    "The creature grinned again, its eyes black as it bared razor-thin teeth."
    THE_FACE @smile "I don't have a name... I just take them."
    THE_FACE "... People like to think when they're alone, they're safe."
    "It stepped back, disappearing into the darkness."
    hide theface_humanoid with dissolve
    "The last thing I saw were its razor teeth and glowing yellow eyes."
    THE_FACE "{i}But we are waiting for them every night.{/i}"
    "And with that, it was gone."
    show mc at center with ease
    MC @scared "That... thing..."
    MC @scared "How many of those things walk among us?"
    SHYAHTAN "(In our travels, I have occasionally sensed their presence.)"
    SHYAHTAN "(They are very few in number.)"
    SHYAHTAN "({i}But they are out there...{/i})"
    "Pushing the thought aside, I looked down at the severed arm and reached to pick it up."
    if RomanceMarbella().Kind == "gang":
        MC @think "(With that sorted, I should head back to the Khazah and let them know this won't be a problem anymore.)"
    elif RomanceMarbella().Kind in ["dom", "love"]:
        "From my other hand, Shyahtan's black tendrils pushed out, wrapping around and inspecting the arm."
        "Suddenly, one of the tendrils pierced the flesh, draining it until, within moments, it became a withered husk."
        MC @talk "Uhh, you got what you needed?"
        SHYAHTAN "Yes."
        SHYAHTAN "Now we can return to our mate tomorrow."
        MC "If you say so..."
    jump rom_marbella_shared_the_face_end

label rom_marbella_shared_the_face_end:
    if RomanceMarbella().Kind == "dom":
        $ NoteLock("marbella_chase_creature")
        $ NoteUnlock("marbella_dom_return_after_face")
        $ QstSetProgress(RomanceMarbella, 2)
    elif RomanceMarbella().Kind == "gang":
        $ NoteLock("marbella_gang_hunt_face")
        $ NoteUnlock("marbella_gang_report_face")
        $ QstSetProgress(RomanceMarbella, 1)
    elif RomanceMarbella().Kind == "love":
        $ NoteLock("marbella_love_deal_with_the_face")
        $ NoteUnlock("marbella_love_report_theface")
        $ QstSetProgress(RomanceMarbella, 5)
    $ AutoMus(True)
    $ LocEnter()
