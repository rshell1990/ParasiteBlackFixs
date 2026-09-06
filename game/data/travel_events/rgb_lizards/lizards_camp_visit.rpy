label travel_event_lizard_camp_visit_choose:
    if TravelRoutes[TravelState.RouteID]["biome_type"] == "desert":
            if CharIsVisiblyPreg("lizard_red"):
                call travel_event_lizard_camp_visit_pregnant("red") from _call_travel_event_lizard_camp_visit_pregnant
            elif CharGetPreg("lizard_red") == 4:
                call travel_event_lizard_camp_visit_gavebirth("red") from _call_travel_event_lizard_camp_visit_gavebirth
    elif TravelRoutes[TravelState.RouteID]["biome_type"] == "forest":
        $ rng == renpy.random.randint(0, 1)
        if rng == 0:
            if CharIsVisiblyPreg("lizard_blue"):
                call travel_event_lizard_camp_visit_pregnant("blue") from _call_travel_event_lizard_camp_visit_pregnant_1
            elif CharGetPreg("lizard_blue") == 4:
                call travel_event_lizard_camp_visit_gavebirth("blue") from _call_travel_event_lizard_camp_visit_gavebirth_1
        elif rng == 1:
            if CharIsVisiblyPreg("lizard_green"):
                call travel_event_lizard_camp_visit_pregnant("green") from _call_travel_event_lizard_camp_visit_pregnant_2
            elif CharGetPreg("lizard_green") == 4:
                call travel_event_lizard_camp_visit_gavebirth("green") from _call_travel_event_lizard_camp_visit_gavebirth_2
    return

label travel_event_lizard_camp_visit_pregnant(LizardColor):
    "While moving around the camp, I picked up a distinct scent that made me stop in my tracks."
    "As I looked around, I listened carefully, and for a moment, I thought perhaps I was wrong; perhaps there was nothing there."
    "Then I heard it, that distinct {i}hissing{/i} sound, calling to me."
    if LizardColor == "red":
        show lizard_red as lizard at cright_f with easeinright
    if LizardColor == "green":
        show lizard_green as lizard at cright_f with easeinright
    if LizardColor == "blue":
        show lizard_blue as lizard at cright_f with easeinright
    show mc at cleft with easeinleft
    "Following the voice towards the outskirts of the camp, I found the Skalith waiting for me."
    "She let out a low rumble when she saw me, but my eyes were naturally drawn to the round, pregnant belly she tenderly rubbed at."
    MC @surprised "You're-"
    "I stopped myself. The girl didn't seem to register my words, but she understood my surprise."
    show mc at center with easeinleft
    "Stepping forward, she tenderly placed my hands onto her belly for a moment, letting me feel the child moving around inside."
    "As I looked up to her to meet her eyes, she stepped back, turning tail to flee into the distance!"
    hide lizard with easeoutright
    MC "Wait! Stop!"
    MC @serious "(That Skalith... It came to see me to let me know she carried my child?)"
    MC @think "(I thought those things were just mindless killers?)"
    return

label travel_event_lizard_camp_visit_gavebirth(LizardColor):
    "While moving around the camp, I picked up a distinct scent that made me stop in my tracks."
    "As I looked around, I listened carefully, and for a moment, I thought perhaps I was wrong; perhaps there was nothing there."
    "Then I heard it, that distinct {i}hissing{/i} sound, calling to me."
    if LizardColor == "red":
        show lizard_red as lizard at cright_f with easeinright
    if LizardColor == "green":
        show lizard_green as lizard at cright_f with easeinright
    if LizardColor == "blue":
        show lizard_blue as lizard at cright_f with easeinright
    show mc at cleft with easeinleft
    "Following the voice towards the outskirts of the camp, I found the Skalith waiting for me."
    "She let out a low rumble when she saw me, but my eyes were naturally drawn to the small, gurgling, lizard-like child in her arms."
    MC @surprised "Is that our-"
    "The Skalith rumbled soothingly in approval, her eyes filled towards me with... {i}adoration?{/i}"
    show mc at center with easeinleft
    "Stepping forward, she let me look closer at our child, who sleepily reached out to grab at one of my fingers and squeeze it tightly."
    "Gently, I found my Skalith's mate's clawed hands gently cupping over my crotch as she lightly rubbed against it."
    "Her body secreted that same powerful scent to tell me her intentions without even saying a word."
    "{i}She wants more offspring, she wants to keep mating...{/i}"
    "We looked into each other's eyes for a moment before she finally stepped back, turning tail to flee into the distance. She hurried off with our child, leaving me to contemplate her...{i}proposal.{/i}"
    hide lizard with easeoutright
    return
