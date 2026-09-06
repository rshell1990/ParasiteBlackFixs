label travel_event_vizura_encounter:
    $ LocSet("travel_node_generic")
    $ LocSet("travel_node_vizura_caravan")
    $ LocEnter()

label vizura_caravan_revisit_talk:
    show cg_goblin_caravan with dissolve
    show vizura at center with easeinright
    VIZURA @happy "Ahh! Welcome back!"
    VIZURA @talk "How's the roads treatin' ya? What can Vizura do for you?"
    jump vizura_caravan_talk_menu

label vizura_caravan_talk_menu:
    $ tmpvar = {}
    menu:
        "Show me your wares.":
            VIZURA @happy "Ho ho! Take a looksie!"
            $ tmpvar["StoredPlayerGoldBefore"] = PlayerItemQty("gold")
            call screen trade(ShopVizuraCaravan)
            $ tmpvar["StoredPlayerGoldAfter"] = PlayerItemQty("gold")
            $ tmpvar["GoldSpent"] = tmpvar["StoredPlayerGoldBefore"] - tmpvar["StoredPlayerGoldAfter"]
            if tmpvar["GoldSpent"] > 0:
                $ VizuraCaravan().MoneySpent += tmpvar["GoldSpent"]
            $ tmpvar = {}
            if VizuraCaravan().MoneySpent > VizuraCaravan().MoneyToOfferSex and not VizuraCaravan().HasOfferedSex:
                jump vizura_sex_offer
            VIZURA @happy "Anything else you need?"
            jump vizura_caravan_talk_menu

        "You free for an hour or so for some ... {i}fun?{/i}" if VizuraCaravan().SexOptions:
            if not VizuraCaravan().WantsSexToday:
                VIZURA @talk "Hmm, tempting."
                VIZURA @talk "But sadly, I ain't got time to roll around in the hay with you, we gotta be on the move soon."
                VIZURA @talk "Let me know if you want anything else though."
                jump vizura_caravan_talk_menu
            else:
                VIZURA @lewd "Fufu, couldn't stop thinking about this green arse, hm?"
                $ CharSetClothes("vizura", "naked")
                show vizura at nod
                "Vizura stripped her clothes off in front of me, uncaring at anyone who might see as she smirked."
                VIZURA @lewd "Step into my office, {i}love.{/i}"
                #VIZURA @lewd "Get in that caravan and wait for me there, handsome~"
                scene black with dissolve
                jump vizura_sex_options

        "How's our, uh... child?" if PregVizura().NumBirths > 0:
            $ rng = RngInt(1, 3)
            if rng == 1:
                VIZURA @think "You got some kinda funny seed?"
                VIZURA @surp "He's bigger and stronger than any other littlun I've ever seen!"
                VIZURA @lewd "Let's go make another! Just thinking about how strong our children are is doing it for me!"
            if rng == 2:
                VIZURA @talk "Fufu, aren't you a sweetheart, worryin' about our spawn?"
                VIZURA @happy "Don't you worry, he's doing just fine."
                VIZURA @talk "Lookin' at the size of his {i}'sword'{/i} already, he's gonna make some goblin girls very happy when we head home!"
            if rng == 3:
                VIZURA @surp "Ehh?! You really wanna know?"
                VIZURA @lewd "Fufu, I'm gonna come back and expect you to put another in me soon if you keep being sweet like that you know..."
                VIZURA @talk "And the littlun's fine, gonna prove one strong bastard when he's grown up fully!"
                VIZURA @think "He might even become a chieftain if he keeps growin' at this rate..."
            jump vizura_caravan_talk_menu

        "I have some questions...":
            VIZURA @talk "Fine, but make them quick, time is money and all that."
            menu vizura_caravan_talk_menu_questions:
                "What's a goblin doing in Alderay?":
                    VIZURA @angry "Tsch! You tryna' say somethin' human?"
                    VIZURA @angry "Ain't nothin' illegal about a goblin travellin!'"
                    VIZURA @talk "Well, if you must know, I'm what they call a {i}freehelm{/i} goblin."
                    VIZURA @talk "We get permission and what-not with the various kingdoms to travel across borders and do some business as we go."
                    MC @talk "And the rulers don't mind that?"
                    VIZURA @talk "Don't matter if they {i}don't{/i} like it, if you're gonna be allied to Irydian, one of the terms are to allow us freehelm folk passage to do business."
                    VIZURA @talk "We don't intervere with human politics and what-not, so most just begrudingly accept us for the sake of wider trade."
                    jump vizura_caravan_talk_menu_questions

                "Why not set up in one of the cities?":
                    VIZURA @surp "AND PAY TAXES? ARE YOU FUCKING CRAZY HUMAN?"
                    VIZURA @angry "Bloody thiefing bastards!"
                    VIZURA @talk "{i}Oooh! We use your taxes to improve the roads and things though!{/i}"
                    VIZURA @angry "You seen the roads recently? My ass is fucking sore from bouncing on all the uneven bumps!"
                    jump vizura_caravan_talk_menu_questions

                "I heard a few voices coming from that caravan... How many goblins are in there?":
                    VIZURA @talk "I dunno, like, a dozen of us maybe?"
                    MC @talk "Why so many?"
                    VIZURA @talk "Goblins are strong in numbers, gotta keep the caravan safe in case of thieves and what-not."
                    jump vizura_caravan_talk_menu_questions

                "That's all I wanted to ask.":
                    VIZURA @talk "Great, any other business?" #Loops back to main menu
                    jump vizura_caravan_talk_menu

        "That's all.":
            VIZURA @happy "Very well, until next time, handsome."
            hide vizura with dissolve
            scene black with dissolve
            $ GetOutToWorldMap()
