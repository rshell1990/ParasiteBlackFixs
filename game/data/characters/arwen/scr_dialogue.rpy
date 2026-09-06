label dialogue_arwen_othergirls:
    ARWEN @talk "Tell me darling, who in all of Mirnos would you want to talk about them... when {i}I'm{/i} by your side?"
    menu dialogue_arwen_othergirls_menu:
        "Come on, {i}you can tell me...{/i}" (Req_Charm = 7):
            ARWEN @blush "Gods... I bet you have half the women in this city wrapped around your finger, don't you handsome?"
            MC @smile "{i}Would you like to be wrapped around my finger, Arwen?{/i}"
            ARWEN @laugh "Haha! Alright..."
            ARWEN @talk 'What do you want to know?'
            jump dialogue_arwen_othergirls_menu_paid
        'Would some coin loosen your tongue?' (Req_Gold = 100): #Only if player has 100 coins
            ARWEN @talk "Well... Now you're speaking a girls favourite language!"
            $ PlayerRemItem("gold", 100)
            ARWEN @talk 'Was there someone specific you wanted to ask about?'
            menu dialogue_arwen_othergirls_menu_paid:
                'What do you think of Helena?':
                    ARWEN @angry "Hm? Oh, {i}her{/i} I'd avoid her if I was you."
                    ARWEN @angry "Overpriced to put it mildly, you'd think she was a virgin princess with how highly she views herself."
                    ARWEN @blush "Don't worry though, I'll show you what a {i}real{/i} woman can do."
                    jump dialogue_arwen_othergirls_menu_paid
                'What do you think of Shani?':
                    ARWEN @think "Hmm, nice enough girl."
                    ARWEN @talk "But I think she's a little {i}too{/i} desperate to work in here."
                    ARWEN @talk "As far as I know, they let her stay and serve clients outside for a reduced rate, but I doubt she'll get through the door."
                    MC @talk "Why's that?"
                    ARWEN @talk "Look around you, we're not the {i}Black Diamond,{/i} we general serve adventurers and merchants with coin to burn."
                    ARWEN @talk  "And she's out there letting the city guard take put it in her ass behind a wall... Hardly a good fit."
                    MC @talk 'That seems rather harsh...'
                    ARWEN @talk "It's just business darling... it's always cut-throat, no matter the trade."
                    jump dialogue_arwen_othergirls_menu_paid
                "I think that's all I wanted to ask.": #Loops back to main menu
                    ARWEN @talk 'Alright then, was there something else?'
                    return
        "Let's talk about something else...":
            ARWEN @talk "Alright then, let's hear it."
            return
