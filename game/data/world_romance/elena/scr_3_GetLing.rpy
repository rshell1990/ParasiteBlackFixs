label rom_Elena_GetLingerie:
    $ LocSet("mc_house_bedroom")
    $ LocFlush(dissolve)
    $ CharSetVar("regina", "hide", False)
    MC "(Well, last night sure was 'interesting')"
    show elena at center_f with dissolve
    ELENA @lewd 'Hm? Oh...!'
    ELENA @grumpy "Uhh, you're not regretting it, right?"
    MC @talk "I just wanted to see how you're doing."
    ELENA @talk "I'm fine, I mean-"
    ELENA @lewd "I feel a little strange with it all so sudden but, I'm happy."
    ELENA @lewd 'I was thinking, with how beautiful some of those girls looked back in the Brothel.'
    ELENA @talk 'Perhaps... I could have something like that to wear?'
    MC @talk 'You mean those lingerie like clothes the elf makes?'
    ELENA @sad 'Would that be so wrong?'
    ELENA @grumpy 'To want to feel attractive off the battlefield?'
    MC @talk 'Very well, I will see what I can do...'
    ELENA @talk 'Thank you, [player_name!t].'
    $ QstSetProgress(RomanceElena, 3)
    $ NoteUnlock('ElenaRomanceGetLingerie')
    $ LocEnter()


label rom_ElenaGetLingerieDrosLines:
    DROS @talk 'Ahh, something for your lycanite friend?'
    DROS @talk 'Finally, something interesting to make to truly test my skills!'
    DROS @talk "Two hundred and fifty coins and it's yours."
    menu:
        'Here you go' (Req_Gold = 250): #If money available
            $ PlayerRemItem('gold', 250)
            DROS @talk 'Wonderful, come back in a few days and I will have it ready for you.'
            $ QstSetProgress(RomanceElena, 4)
            $ NoteLock('ElenaRomanceGetLingerie')
            $ NoteUnlock('ElenaRomanceLingerieInProgress')
            $ LocEnter()
        "My coin is a little short at the moment...":
            DROS @talk 'You know well enough by now that my materials are costly and my craftsmanship time consuming.'
            DROS @talk 'Return to me when you have the coin.'
            $ LocEnter()

label rom_ElenaGetLingerieDrosInProgress:
    DROS @talk "Still on it, sorry."
    DROS @talk "Come back later."
    return

label rom_ElenaGetLingerieDrosComplete:
    DROS @talk "Ah right, there you go."
    $ NoteLock('ElenaRomanceLingerieInProgress')
    $ NoteUnlock('ElenaRomanceDeliverLingerie')
    $ QstSetProgress(RomanceElena, 5)
    return

label rom_ElenaGetLingerieDeliver:
    #Upon returning to Elena, new dialogue choice appears 'I have something to give you...'
    ELENA @talk 'What is it?'
    MC @talk 'Here, those clothes you asked for.'
    ELENA @lewd 'Ah! Thank you!'
    MC @talk 'So, what now?'
    MC @talk 'Will you try them on now?'
    ELENA @lewd 'No... I have something special planned.'
    ELENA @talk 'Maybe you could get us some alone time again?'
    MC @talk 'Hm? Why again?'
    ELENA @grumpy "I need more room for what I'm planning... And you're room isn't exactly the biggest."
    MC @talk 'Well, I can try ask [regina_ref!t].'
    ELENA @lewd "Thank you... I promise it will be worth it."
    $ NoteLock('ElenaRomanceDeliverLingerie')
    $ NoteUnlock('ElenaRomanceGetReginaOutAgain')
    $ QstSetProgress(RomanceElena, 6)
    $ LocEnter()
