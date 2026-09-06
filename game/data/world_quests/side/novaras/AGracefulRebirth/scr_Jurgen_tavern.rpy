label jurgen_0_tavern:
    #Meeting Jurgen at the Iron Unicorn at Night - generic guard NPC 
    # ??? by default
    show cg_guard at cright_f
    with dissolve
    $ QstGracefulRebirth().knowJurgen = True
    UNKNOWN "Hm? What do you want?"
    MC @talk "You wouldn't happen to know a guard by the name of Jurgen, would you?"
    # name shown
    
    JURGEN "You're speaking to him, now what do you want?" 
    menu:
        'Never mind... I have to go.':
            JURGEN "Quit wasting my time!"
            hide cg_guard with dissolve
            MC "(Okay, that's our mark.)"
            $ LocEnterQ()

        'The Merchants would like you to stop harrassing them.':
            $ QstGracefulRebirth().spokeToJurgenBoutMerchants = True
            JURGEN "I'm sure they would."
            JURGEN "So, are you the lap dog they've sent then?"
            MC @talk "What will it take to get you to back off?"
            JURGEN "Nothing."
            MC @talk "Really?"
            JURGEN "If the Merchants wish to come clean, they may do so at their leisure for a less harsh sentence when the time comes."
            JURGEN "But {i}I know{/i} that the Merchant's guild no doubt has tied itself to the Black Market, however much they deny it."
            JURGEN "And nothing you offer me is going to be worth the promotion when I'm done."
            MC @talk "It's far more likely you'll be killed than rewarded."
            JURGEN "Ha! You think you can fool me?"
            MC @talk "Do you really think anyone is going to thank you for causing them a bureaucratic nightmare?"
            MC @talk "You're a single guard crossing some powerful people on both sides... All you're going to do is get yourself cared."
            JURGEN "C-Cease your lies!"
            JURGEN "Now leave me be at once before I have you arrested for attempting to bribe an officer!"
            MC "(This is fruitless... I will need to find a different solution.)"
            MC "(Perhaps I could slip something into his drink?)"
            $ LocEnter()

label jurgen_0_tavern_revisit:
    show cg_guard:
        xalign 0.85
        xzoom -1.0
    JURGEN "What do you want?"
    menu:

        'The Merchants would like you to stop harrassing them.' if QstGracefulRebirth().spokeToJurgenBoutMerchants: # if already asked
            "Jurgen chuckled and turned away, as if he saw Alcott stand in my place, naked."
            MC @talk "(Yeah, this clearly doesn't work.)"
            $ LocEnter()

        "{image=[ICON.SWORDS]} The merchants wish to meet with you Jurgen, they have an offer." if QstGracefulRebirth().spokeToJurgenBoutMerchants: # if already spoke about merchants
            JURGEN "What is this about?"
            jump jurgen_1_tavern_assassinate

        "{image=[ICON.SWORDS]} I hear you are the man going against the guild... I may have information that could help you." if not QstGracefulRebirth().spokeToJurgenBoutMerchants: # if not ^
            JURGEN "Show me."
            jump jurgen_1_tavern_assassinate

        # Player can either obtain Amira's Tears from Nijah 
        # or Raza from a prostitute at the Black Diamond - 
        # player has choice to insert whatever he gets or has a 
        # additional choice to choose between which drug to put in if he acquires both
        "{i}*Distract him and slip poison into his drink*{/i}" if PlayerItemQty("qst_amiras_tears") > 0 or PlayerItemQty("qst_raza_bottle") > 0: # if either of poisons in inv:
            MC "(Okay, let's do this...)"
            jump jurgen_1_tavern_poison

        "Never mind... I'm just enjoying my ale here.":
            JURGEN "Yeah you better!"
            $ LocEnter()