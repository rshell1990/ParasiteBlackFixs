label vizura_caravan_firstmeet:
    #scene black
    show cg_goblin_caravan
    show mc at left with easeinleft
    "The strange caravan in front of me rocked and shook, with what sounded like inhuman chattering inside of it with at least a dozen voices."
    "As the front door of the caravan swung open, a curvy, short, green-skinned girl stepped outside and smiled brightly towards me with her sharp, brilliant teeth."
    show vizura happy at cright_f with easeinright
    $ Pause()
    GOBLIN "Heh, you're a good lookin' human, aren't ya?"
    show vizura lewd
    "The goblin girl licked her lips hungrily as she eyed me up."
    menu:
        "{i}*Wait to see what the goblin does.*{/i}":
            show vizura think
            GOBLIN "... Not much of a talker, are ya?"
            show vizura -think
            GOBLIN "Usually I hear a lot of 'ooohs' and 'AHHHHS!' When they see me."
        "{i}*Draw your blade*{/i}":
            jump vizura_caravan_draw_blade

        "{i}*Pull your cock out*{/i}":
            $ CharSetClothes("mc", "naked")
            show mc at blurin, nod
            "The goblin girl stared at the cock in front of her and blushed profusely."
            show vizura surp
            GOBLIN "FUCKING HELLS, YOU'RE A FORWARD ONE AIN'T YA?"
            show vizura angry
            GOBLIN "You better not be one of those {i}'green-chaser'{/i} weirdos!"
            "Despite her words, the goblins eyes continue to stare at my cock before she reluctantly pulls herself away."
            $ CharChangeRel("vizura", 1)
            show vizura talk
            GOBLIN "Put that thing away, aye?"
            show vizura lewd
            GOBLIN "Hard to do any thinkin' when you got that sword swingin' around in front of me!"
            $ CharSetClothes("mc", "normal")
            show mc at blurin, nod
            "I did as the goblin asked."
    jump vizura_caravan_first_talk

label vizura_caravan_draw_blade:
    show vizura surp
    GOBLIN "WHOA! WHOA! There's no need for that!"
    MC @angry "How do I know this isn't some kind of trick?"
    show vizura angry
    GOBLIN "I'm a goblin! Not a bandit! BAH!"
    GOBLIN "I know you daft fucks see green and think we're all the same, but We fall under the Irydian kingdom!" 
    "Remembering back to my time still in class, while we didn't cover other kingdoms histories as much, there was something about goblins and dwarves in Irydian..."
    menu:
        "{i}*Attack - it's not worth the risk trusting her*{/i}":
            jump vizura_caravan_battle
            
        "{i}*Put your sword away.*{/i}":
            show mc at cleft with easeinleft
            MC @think "...My apologies, one can never be too careful on these roads."
            show vizura talk
            GOBLIN "Hmph... Apology accepted."
            if CharInParty("markus"):
                show markus at left with easeinleft
                MARKUS @angry "Be on your guard ... I don't trust {i}this one.{/i}"
                show vizura angry
                GOBLIN "BAH! You humans don't trust anyone!"
                hide markus with dissolve
            if CharInParty("myu"):
                show myu laugh at left with easeinleft
                MYU "{i}...Green lady is pretttty.{/i}"
                show vizura surp
                GOBLIN "Bloody hells! Never seen a slime wandering around like that before!"
                GOBLIN "You're quite a bunch of oddballs travelling together, ain't ya?"
                hide myu with dissolve
            #-Elena 
            if CharInParty("elena"):
                show elena at left with easeinleft
                ELENA @talk "I am Elena of Thornfall, and who might you be?"
                GOBLIN "Ooooh! That's a fancy title for a wolf-girl like yourself, ain't it?"
                hide elena with dissolve
            jump vizura_caravan_first_talk

label vizura_caravan_first_talk:
    $ QstSetProgress(VizuraCaravan, 1)
    MC @talk "Who are you?"
    VIZURA @happy "Vizura, at your service human!"
    $ CharMeet("vizura")
    VIZURA @happy "Weapons? Armour? Potions?"
    VIZURA @happy "{i}Vizura's travelling wares{/i} has all your needs!"
    MC @think "So ... You're a merchant?"
    VIZURA @talk "I am indeed! Got me papers in order to prove it as well!"
    VIZURA @talk "And you are...?"
    MC @talk "[player_name!t]."
    VIZURA @talk "[player_name!t] eh? Nice to meet ya!"
    VIZURA @talk "So, now we're acquainted properly, you interested in doing a little {i}business?{/i}"

    
    hide mc with dissolve
    show vizura at center_f with easeinright
    jump vizura_caravan_talk_menu