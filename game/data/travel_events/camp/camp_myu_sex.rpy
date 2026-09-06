label travel_event_camp_myu_solo:
    $ PlaySoundRandom("tentFlap")
    "Getting ready to rest for the day, the flaps of my tent were ruffled and parted as Myu stepped inside."
    show myu at cright_f with easeinright
    MYU @blush "Myuuu... ❤️"
    show mc at cleft with easeinleft
    MC @think "Myu?"
    MC @think "What are you doing here?"
    show myu at center_f with easeinright
    "Myu gently stepped forward, pushing her sticky, cool breasts up against my body as she ran her hands down my chest."
    "Her left hand continued to trail down even after the right had stopped, gently cupping my groin."
    MYU @blush "Play with Myu? ❤️"
    menu:
        "Yes, Myu, let's {i}'play'{/i}":
            call sexscene_myu_camp_deepthroat from _call_sexscene_myu_camp_deepthroat

            scene expression TravelRoutes[TravelState.RouteID]["image_camp"] with dissolve

            "Rising to her feet, Myu stood cutely before me, her arms outstretched as her hands clasped and closed repeatedly."
            MYU "{i}Cuddles please?{/i}"
            menu:
                "Let Myu sleep with you.":
                    scene black with dissolve
                    "Patting some of the quilts beside me, Myu hurried over, nestling herself up against me."
                    "She was still cool, but her pleasant rumbling was relaxing as she rested one of her hands on my chest."
                    MYU "Myuuu..."
                    "With her eyes gently closed, the cuddly, sleepy Myu quickly began to drift off."
                    "Only occasionally squirming in my arms, I couldn't help but appreciate how cute Myu was."
                    "... One might also forget how lethal a predator she could actually be."
                    "Slowly, content and warm with my companion for the day, I too began to drift off to sleep..."
                    pass

                "Not tonight, Myu.":
                    MYU @sad "M-Myu..."
                    hide myu with dissolve
                    $ PlaySoundRandom("tentFlap")
                    "Dejectedly, Myu sadly slumped her way out of my tent, leaving me alone for the day."
                    pass

        "Not tonight, Myu.":
            MYU @sad "M-Myu..."
            "Dejectedly, Myu sadly slumped her way out of my tent, leaving me alone for the day."
            pass
    
    return