# Player speaks to Regina, new dialogue option appears in menu: - 'I need to ask something of you...(persuade to leave the house)'
label rom_Elena_AskReginaLeave:
    $ NoteLock("ElenaRomanceGetReginaOut")
    REGINA @talk 'Hm? What is it my dear?'
    MC @talk 'I was thinking that, when was the last time you had a night off?'
    '[regina_ref_cap!t] laughed at the comment.'
    REGINA @smile_talk 'A night off?'
    MC @talk "Well, everyday you cook for me and look after the house and such..."
    MC @talk "So, why don't I get some food for myself and you perhaps just enjoy a evening to yourself?"
    REGINA @smile_talk "...You've got a girl coming over haven't you?"
    MC @talk 'I... uhh...'
    'Regina laughed.'
    REGINA @smile_talk "I will give you two hours and no more..."
    'Slightly flustered, my cheeks rosy red as I struggled to look her in the eyes, I awkwardly fumbled some words out.'
    MC @talk 'A-Ahh... T-thank you.'
    REGINA @smile_talk 'Have fun [player_name!t]!'
    'Smiling, [regina_ref!t] hummed to herself as she headed towards the door, waving playfully goodbye to me as she closed the door behind her.'
    hide regina with easeoutright
    MC '{i}*Sigh*{/i}'
    #Elena appears
    show elena at left with easeinleft
    ELENA @talk 'That was kind of her.'
    MC @talk 'Were you listening in?'
    ELENA @talk '[player_name!t]... I hear everything in this house no matter where I am.'
    'Elena stood awkwardly for a moment, her cheeks flushed red as she tapped her foot on the floor.'
    ELENA @lewd 'Would... Would you like to join me?'
    ELENA @shock "I mean, you {i}don't{/i} have to of course!"
    ELENA @lewd "I'm just thinking perhaps it would be a waste for me to go to such efforts pouring all the water and n-not let you take advantage of it is as well."
    'Her flushed expression gives away her real intentions, and her cute comments trying to mask her feelings warms my heart a little.'
    $ RomanceElena().reginaReturnTime = store.rpTime + TIME_2H
    $ QstSetProgress(RomanceElena, 2)
    $ CharSetVar("regina", "hide", True)
    menu:
        "Of course, just make sure the water is warm.":
            jump rom_Elena_WaterWarm
        "I will have to decline, thank you":
            jump rom_Elena_WaterCold
