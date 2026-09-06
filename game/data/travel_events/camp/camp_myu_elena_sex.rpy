label travel_event_camp_myu_elena:
    scene black with dissolve
    "As I laid there restlessly in my bedrolls, I heard the sounds of fabric ruffling, looking up to see Myu enter my tent."
    scene bg_player_camp_tent
    show myu at center_f
    with dissolve
    MYU @blush "Myuuu..."
    MC @smile "What brings you here at this hour, Myu?"
    MC @lewd "Looking for some entertainment perhaps?"
    "Myu stepped closer towards me alluringly."
    MYU @blush "Myuuuu... ❤️"
    show myu at cright_f with easeoutright
    show elena at center_f with dissolve
    show elena at cleft_f with easeoutleft
    "Abruptly, the two of us heard the fabric ruffle again as Elena stepped into the tent."
    ELENA @lewd "[player_name!t], are you still-"
    ELENA @shock "... Oh!"
    ELENA @sad "I - I didn't realize you already had company."
    "Elena rubbed at her arms as she shyly looked away from the scene before her."
    ELENA @sad "... I should go."
    menu:
        "Nudge Myu to stop her.":
            call sexscene_myu_elena_camp_threesome from _call_sexscene_myu_elena_camp_threesome
            $ AutoMus(True)
            "Myu flung herself onto me, nuzzling her head against my chest as she threw her leg over me."
            MYU "Mmmm... ❤️"
            MC "...Like that."
            "Elena sheepishly looked around the tent, nervously standing there for a couple moments as she wondered how to proceed."
            "As she brushed her hair over her shoulder, she dropped to the floor, nervously snuggling herself up against me."
            ELENA "...T-This is nice."
            ELENA "Strange, but nice."
            "Elena slowly began to relax, her hand gently running down my chest as Myu closed her {i}eyes.{/i}"
            "I wasn't sure if she was actually asleep or merely resting, but she was content."
            ELENA "...G-Goodnight, [player_name!t]."
            MC "Goodnight, Elena."
            MYU "{i}Grumbles{/i} ❤️"
            "Gently I slowly closed my own eyes, relaxing as I felt the light swish of Elena's tail brush soothingly past me..."
            pass

        "Let Elena leave.":
            $ PlaySoundRandom("tentFlap")
            hide elena with dissolve
            "As Elena hurried out of the tent, Myu turned towards me."
            show myu at center_f with easeinright
            MYU @think "...We play?"
            menu:
                "Yes, Myu, let's {i}'play'{/i}":
                    call sexscene_myu_camp_deepthroat from _call_sexscene_myu_camp_deepthroat_1
                    
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
                            "Slowly, content and warm with my companion for the evening, I too began to drift off to sleep..."
                            pass

                        "Not tonight, Myu.":
                            MYU @sad "M-Myu..."
                            hide myu with dissolve
                            $ PlaySoundRandom("tentFlap")
                            "Dejectedly, Myu sadly slumped her way out of my tent, leaving me alone for the evening."
                            pass


                "Not tonight, Myu.":
                    MYU @sad "M-Myu..."
                    "Myu sadly slumped her way out of my tent, leaving me alone."
                    pass
    
    return