label rom_Dros_preTf_lines:
    DROS @shock 'Umm... What?!'
    DROS @shock 'I... You mean-'
    MC @talk "You heard what I said."
    MC @talk "You're over-complicating things."
    'Dros stuttered as he seemed taken aback at the comment.'
    DROS @lewd 'I - Y-You... Um...'
    MC @talk 'So, how about it?'
    DROS @sad "Y-You're joking? Right?"
    MC @talk 'Do you always question everyone who actually want to fuck you?'
    DROS @lewd 'O-Oh...'
    DROS @lewd "I... Need to charge you f-for the room... Madam's rules."
    MC @talk "How much?"
    DROS @lewd "F-Four hundred... It's the lowest she'll let me charge."
    menu:
        'Here.' (Req_Gold = 400): #If coin available 
            $ PlayerRemItem("gold",400)
            'I handed over the coins to Dros who counted them out.'
            DROS @lewd 'O-Okay then.'
            DROS @lewd 'This way...{i}sir.{/i}' #Cut to MC and Dros in brothel scene.
            jump dros_bordello_sex_preTf_root
        "Damn, I can't afford that.":
            DROS @sad 'Oh, I see...'
            'Dros seemed to sink down dejectedly.'
            DROS @sad "Well, I guess if you're still serious."
            DROS @talk "I'll be here."
            return

label dros_preTf_firstSex:
    $ CharSetClothes("dros", "dress")
    scene bg_weeping_heart_brothel_room
    show dros at center
    with dissolve
    #All routes continued - post the FIRST fuck/blowjob with non-tf Dros in the brothel
    DROS @smile 'That was... That was wonderful!'
    DROS @talk 'Are you really sure about this?'
    DROS @talk 'I mean, {i}us.{/i}'
    DROS @talk 'What even are we now?'
    DROS @sad "I mean, I will u-understand if this was just a one time thing o-or nothing serious then, I'd prefer you said now."
    menu:
        '{image=[ICON.HEART]} Your ass is mine, understand?':
            $ QstStart(RomanceDros)
            $ CharSetLover("dros")
            $ CharAddRelEntry("dros", "romance_male")
            $ CharReplaceRelEntry("dros", "initial", "romanced")
            $ CharChangeRel("dros", 1)
            DROS @talk 'I... Yes... Yes I do.'
            DROS @talk 'So, what should I call you?'
            python:
                dros_player_ref = renpy.input(_("What should I call you, [player_name!t]?"), default = _("Master"))
                dros_player_ref = dros_player_ref.strip() or __("Master")
                renpy.restart_interaction()
            #Menu input name option - default is master.
            DROS @talk '[dros_player_ref!t]... Yes, If that is what you like.'
            DROS @lewd "Oh my, I really don't quite know what to do with myself now!"
            DROS @talk "Nor, any idea how to thank you properly for this."
            MC @talk "Your ass wasn't enough?"
            DROS @sad 'I appreciate the companionship just as much... It is lonely being an elf sometimes.'
            if DialogueDros().discount == 0:
                DROS @smile '...I know! I can give you a discount at my store!'
                DROS @talk "I'll give you a permanent fifteen percent discount on my store from now on." #Permanent unlock of fifteen % off buying anything in Dros store.
                $ DialogueDros().discount = 15
                menu:
                    'Only fifteen percent?' (Req_Charm = 7): #Charm check 
                        DROS @talk '{i}*Cough*{/i} I see you still drive a hard bargain... Very well, twenty percent.' #Charm check pass - permanent 20% off buying anything in Dros store
                        $ DialogueDros().discount = 20

                    'Thank you.':
                        DROS @talk "I'm sure its the least I can offer."
                        #Both routes continued
            DROS @talk "Well... I suppose I better escort you back before the mistress starts wondering what's taking so long."
            DROS @talk 'Follow me.'
            #Dros returns with MC to main brothel.
        "{image=[ICON.HEART_CROSS]} What happens in the brothel, stays in the brothel.":
            DROS @sad 'I see... Well, thank you for... {i}a good time.{/i}'
            DROS @talk "I hope um, maybe you'll come back soon?"
            MC @talk "I will see, but its difficult with the nature of my work."
            DROS @talk 'I understand, really, I do.'
            DROS @sad "It's just... Things are very lonely I suppose."
            DROS @sad '{i}*Sigh*{/i} But never mind all that...'
            DROS @talk 'I suppose I better escort you back before the mistress complains.'
            DROS @talk 'Follow me.'
            #DROS returns with MC to main brothel room
    $ LocNameReset()
    $ DrosInBordello().bordelloFirstFuck = False
    $ LocEnter()