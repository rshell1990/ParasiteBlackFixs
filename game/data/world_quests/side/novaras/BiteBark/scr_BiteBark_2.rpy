# in case player havent bought her off instantly
label qst_BiteBark_2_RepTalkToKennelMaster:
    show kennelmaster with dissolve:
        xcenter 0.7
        xzoom -1.0
    show mc with easeinleft:
        xcenter 0.15
    KENNELMASTER "Look what them hounds dragged in..."
    KENNELMASTER "Got the gold?"
    KENNELMASTER "Seven hundred and fifty to rid us of this beast."
    menu:
        'Here.' (Req_Gold = 750): #(Only available if player has gold available)
            $ PlayerRemItem("gold", 750) #If coin amount is available (750)
            KENNELMASTER"Alright, she's your problem now."
            'The man moved to open the cell up and allow the wolf out.'
            KENNELMASTER"Come on then bitch! Looks like you get another chance!"
            KENNELMASTER"Try not to fuck this one up would ya, {i}please?{/i}"
            hide kennelmaster with easeoutright
            ELENA_W "..."
            show mc with easeinleft:
                xcenter 0.2
            show elena_w with dissolve:
                xcenter 0.45
                xzoom -1.0
            'I crouched down towards the wolf.'
            MC @smile 'Hello, my name is [player_name!t], and-'
            'The wolf trotted off, seemingly uninterested in what I had to say.'
            hide elena_w with dissolve
            'Waiting by the door for us to leave, it stared at me with disinterest.'
            KENNELMASTER'Heh heh! Told you!'
            KENNELMASTER"Oh... by the way, no collar... She'll rip your fucking head off if you try."
            MC @angry 'You could have mentioned that before.'
            KENNELMASTER"Oh don't worry! She'll follow you alright!"
            KENNELMASTER"No problems there, till she just decides 'fuck it' and decides to stroll off and leave you eventually."
            KENNELMASTER"Anyway, she's {i}your{/i} problem now! Hahaha!"
            MC @talk'(This... could be more difficult than I hoped.)'
            hide mc with dissolve
            MC @sad 'Come on then girl, let me show you your new home.'
            ELENA_W "..."
            $ QstSetProgress(QstBiteBark, 2)
            $ LocSet("novaras_dist_army")
            $ LocEnterQ()

        "I don't have the money yet...":
            KENNELMASTER"She ain't going anywhere mate, come back when you do."
            $ LocSet("novaras_dist_army")
            $ LocEnterQ()