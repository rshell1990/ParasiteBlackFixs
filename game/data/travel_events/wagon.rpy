label travel_event_wagon_wreck:
    # this assumes it can only happen in forest
    scene bg_forest_clearing_wagon with dissolve
    show mc at left with easeinleft
    "Heading out into a clearing in the forest, I heard the sounds of crows squawking as they circled overhead the wreckage of a wagon."
    "Littered around the decimated remains of the overturned wagon, the bloodied, torn to shred remains of a few Alderian soldiers."
    "The blood still dripped down from the tips of the pikes as the horrible, sickening smell nearly made me convulse."
    "As I lightly dipped my finger into one of the pools of blood, it was not warm, but not cold either."
    "These men were not slain that long ago..."
    if CharInParty("markus"):
        show markus at center with easeinleft
        MARKUS "Let's walk around... I've got a bad feeling about this."
        hide markus with easeoutright
    if CharInParty("elena"):
        show elena at center with easeinleft
        ELENA @sad "These poor men."
        ELENA @sad "What could have done this?"
        hide elena with easeoutright
    if CharInParty("regina"):
        show regina at center_f with easeinleft
        REGINA "...Hmm."
        hide regina with easeoutright
    if CharInParty("ves"):
        show ves at center with easeinleft
        VES @talk "There might be something worth taking on that wagon."
        VES "But is it worth it?"
        hide ves with easeoutright
    if CharInParty("myu"):
        show myu at center with easeinleft
        MYU @scared "M-Myu...!"
        hide myu with easeoutright
    MC "(Hm... What should I do?)"
    menu:
        "Investigate the wagon":
            MC "(Nothing ventured, nothing gained!)"
            "As I stepped cautiously towards the wagon..."
            $ rng = renpy.random.randint(0, 3)
            if rng == 0:
                call travel_event_wagon_wreck_demorai() from _call_travel_event_wagon_wreck_demorai
            elif rng == 1:
                call travel_event_wagon_wreck_bandits() from _call_travel_event_wagon_wreck_bandits
            elif rng == 2:
                call travel_event_wagon_wreck_no_trap() from _call_travel_event_wagon_wreck_no_trap
            elif rng == 3:
                call travel_event_wagon_wreck_no_trap_empty() from _call_travel_event_wagon_wreck_no_trap_empty

        "Ignore the wagon.":
            MC "(No, why take unnecessary risks?)"
            MC "(I imagine that thing has been looted already.)" 
            "Deciding it was best to ignore the bloody wreck, we took a slightly longer route around... Avoiding passing by it entirely." #Ends scene
    return

label travel_event_wagon_wreck_demorai:
    "I found my foot pressed up against a wire tied across the path, connected from one of the many littered corpses to a loud bell attached to the wagon."
    "As it rang out, a small horde of Demorai soldiers came rushing out to face us!"
    if GetPartySize() > 1:
        MC @scared "DEMORAIIII!"
    $ StartBattle(BattleData(TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = ["e_dark_soldier", "e_dark_soldier", "e_dark_soldier"]))

    scene bg_forest_clearing_wagon with dissolve
    "With the last of the Demorai foot-soldiers slain at my feet, I caught my breath as I wiped the blood off from me."
    "The wagon indeed was completely ransacked; what few bags were there had been tied up and loaded with random rocks and wood to give the {i}appearance{/i} there was still something worth taking."
    MC "(I have to be more careful... The Demorai likely have more ambushes like these all over these roads!)"
    if CharInParty("elena") and GetPartySize() > 2:
        ELENA "Is everyone alright?"
        if CharInParty("regina"):
            REGINA @smile "Never better, dear!"
            REGINA @smile "What's a little blood to ruin my day?"
    if CharInParty("ves"):
        VES @angry "These damn things are tough to kill... Much tougher than the scouts they usually send out."
    if CharInParty("markus"):
        MARKUS @angry "Could we {i}please{/i} next time avoid the massacred sites in the hopes of finding what? A bag of coins and some bread?"
    return

label travel_event_wagon_wreck_bandits:
    "I heard a sharp whistle, and as I turned to look around swiftly, from the tall grass and trees, we found ourselves surrounded by a group of bandits."
    show cg_bandit at right_f with dissolve
    BANDIT "Going somewhere, are we?"
    BANDIT "Heh... You've got to pay the toll first."
    MC @angry "{i}The toll?{/i}"
    BANDIT "Either you give us three hundred coins, or we take {i}all{/i} your coins."
    # If the player has Ves in the party 
    # BANDIT "Although, looking at the company you keep, we could come to {i}another{/i} arrangement... Heh..."
    #"The bandit's eyes hungrily look over Ves, who, upon noticing his lustful gaze, seethes with embarrassed rage."
    menu:
        "{image=[ICON.SWORDS]} How about I just slaughter you all?":
            BANDIT "You can try!"

            $ StartBattle(BattleData(TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = ["e_bandit", "e_bandit", "e_bandit"]))

            scene bg_forest_clearing_wagon with dissolve
            show mc at left with easeinleft
            "As the last of the bandits pleaded, desperately dragging himself across the floor with his hand raised towards me, he squealed."
            BANDIT "P-Please! Don't!"
            menu:
                "Finish him off.":
                    show mc at shake
                    "He let out one final ghastly scream as I took his head."
                "Go on, get out of here!":
                    BANDIT "T-Thank you!"
                    "The bandit got up and sprinted into the trees to escape."
                    MC "(These roads become more and more dangerous everyday.)"
                    MC "(I need to be more careful...)"

        # terrifying perk 
        "Leave. Now... I will feast on your corpses and then come for the ones you love." (Req_Perk = "terrifying"):
            BANDIT "...H-How about you just head on through, and we pretend this never happened?"
            BANDIT "You go your way, we go ours..."
            MC @angry "Fine."
            hide cg_bandit with dissolve
            "The terrified bandits step aside as we made our way past the bloody wreckage..."

        # If the player has coin 
        "Pay them." (Req_Gold = 300):
            $ PlayerRemItem("gold", 300)
            BANDIT "Pleasure doing business with ya, heh..."
            "We passed on through uninterrupted."

        # Charm persuade
        "The inquisitors will be here soon!" (Req_Charm = 8): 
            BANDIT "W-What?"
            MC @serious "That wagon you just slew? Who do you think was on it?"
            MC @talk "They're inquisitor agents, you fools!"
            BANDIT "I-"
            "I continued to lie as easily as I breathed."
            MC @serious "Why do you think we're here? We were sent to head along this path and find the lost wagon!"
            BANDIT "...Shit."
            MC @serious "{i}Do you know what they'll do to you once you're caught?{/i}"
            BANDIT "U-Uhh, how'sabout we jus' go our seperate ways?"
            BANDIT "Uhh, m-me and the boys will do our 'business' elsewhere."
            MC @talk "Better hurry then."
            MC @serious "The others will be here soon."
            BANDIT "Boys! Pack it up! We're leaving!"
            hide cg_bandit with easeoutright
            "The bandit leader motioned for them to follow, and the other bandits, with mild grumbling and protests, sheepishly hurried off into the woods."
            MC "(Idiots.)"

        #"You like Ves?": #N/A for now
        #    BANDIT "Heh! Haven't ever had me'self an orc before!"
            #Note: Dependent on the players choices with Ves later on, decides how receptive she is to this idea - As Ves isn't available as a companion yet, this is just a footnote
        #    BANDIT "Are her lips green down there, too?" 
    return

label travel_event_wagon_wreck_no_trap:
    show mc at center with easeinleft
    "Stepping closer to the wagon, I inspected the spilled-over bags of goods."
    MC "(Looks like whoever ambushed them came to kill and nothing else.)"
    $ PlayerAddItem("gold", 50)
    $ PlayerAddItem("potion_heal_minor", 2)
    "Rummaging through the bags, I found a few coins and some useful things." 
    MC "(Hm, it's something at least.)"
    "For a moment, I contemplated burying the poor souls, but being stuck out in one spot on these roads for two long was too dangerous an idea."
    "I resigned myself to reporting about the wagon to someone when I had the chance..."
    return

label travel_event_wagon_wreck_no_trap_empty:
    show mc at center with easeinleft
    "Stepping closer to the wagon, I inspected the spilled-over bags of goods."
    MC "(Looks like whoever ambushed them came to kill and nothing else.)"
    "Rummaging through the bags, I only found sacks of grain, too heavy for us to carry, unfortunately."
    MC "(Damn... What a waste.)"
    "For a moment, I contemplated burying the poor souls, but being stuck out in one spot on these roads for two long was too dangerous an idea."
    "I resigned myself to reporting about the wagon to someone when I had the chance..."
    return