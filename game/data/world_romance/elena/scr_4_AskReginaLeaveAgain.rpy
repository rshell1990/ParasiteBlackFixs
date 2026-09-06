#Quest log:
#Player approaches Regina, new dialogue option
label rom_AskReginaLeaveAgain:
    REGINA @talk '{i}Again?{/i}'
    MC '...'
    REGINA @angry_talk '...Alright, enough of this.'

    REGINA @talk 'Elena!'
    REGINA @talk 'Come here!'
    'I felt the blood drain from my face as Elena trotted out towards [regina_ref!t], barking.'
    show elena_w at cleft with easeinleft
    REGINA @smile_talk 'Enough of that girl, show your true form.'
    MC @surprised 'You... What are you-'
    REGINA @angry_talk "Don't make me ask again."
    'Elena whimpered and look towards me before she shyly transformed.'
    scene black with dissolve
    play sound "audio/cfx/detect_magic.ogg"
    $ LocFlush()
    show regina at left
    show elena at center
    show mc at cright_f
    with dissolve
    ELENA @shock 'How... How did you-'
    REGINA @talk "I literally live with an inquisitor, I've known my way around magecraft long enough to know when someone is hiding their form."
    'I remained frozen still in place, shocked as I stared at [regina_ref!t] who quizzically looked over Elena.'
    MC @talk "You've known this whole time?!"
    REGINA @smile_talk '[player_name!t], please... Why do you think I was so pleased when you brought her home?'
    ELENA @shock 'Please, if I may-'
    REGINA @smile_talk 'You may do as you wish, Elena... So long as you protect [player_name!t].'
    REGINA @talk 'Now I suppose you want to use my room for the bath tub or something again?'
    MC '...'
    ELENA '...'
    REGINA @shy_talk 'The leftover hairs was a giveaway.'
    REGINA @smile_talk 'But yes, you may use my room should you wish.'
    MC "I... I still don't quite know what to say."
    REGINA @talk '{i}*Sigh*{/i}'
    REGINA @smile_talk 'Just know that I have your best interests at heart...'
    REGINA @talk "We'll talk more some other time, now please."
    REGINA @smile_talk "I have some food I need to put on, perhaps you'd like to join us properly after, Elena?"
    ELENA @shock 'If... If that is no trouble to you my lady!'
    REGINA @smile_talk 'Ahh, nice to see you finally bringing home such a well-mannered lady [player_name!t].'
    REGINA @talk 'Of course, it is no problem, Elena.'
    REGINA @talk 'Please, from now on, feel free to wander around this house as you see fit.'
    REGINA @talk 'And if you need to use my room for whatever, simply ask from now on.'
    REGINA @smile_talk 'Now both of you, shoo!'
    'As [regina_ref!t] dismissed us both, we sheepishly made our way back into my room for a moment.'
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    with dissolve
    show mc at left
    show elena at cright_f
    with dissolve
    ELENA @shock 'She... {i}knew?{/i}'
    MC @talk 'I should speak with her on this matter again...'
    'Something about her knowing did not sit right with me.'
    'A thousand thoughts swirled through my mind about how exactly she knew.'
    "I didn't buy her excuse about Erika."
    "Something about it did not sit right with me."
    'I have always felt [regina_ref!t] kept things from me, now more than ever.'
    ELENA @talk 'Wait!'
    MC '...'
    ELENA @lewd 'Can that conversation not wait?'
    ELENA @talk 'She has given us her blessing and I do not wish to seem ungrateful.'
    MC @talk 'Elena...'
    ELENA @lewd '{i}And...{/i} I had other plans tonight.'
    MC @smile '...Very well, Elena, I will hold my tongue.'
    'Elena leaned forward to kiss me once again.'
    ELENA @talk 'Thank you, [player_name!t].'
    ELENA @talk "...Let me know when you're ready to meet me in her room?"
    MC @talk 'As you wish, Elena.'
    hide elena with easeoutright
    "As Elena practically skipped out of my room, I waited, still thinking about [regina_ref!t]'s words."
    "And the more I thought, the more I realized I had always in the past dismissed [regina_ref!t]'s strange quirks as nothing more than her eccentric self."
    "But now, I felt like some veil that had covered my eyes was begining to lift, and I knew ..."
    "Something was awry ... Something I would need to finally look closer at when the time came."
    scene black with dissolve
    $ NoteLock("ElenaRomanceGetReginaOutAgain")
    $ QstSetProgress(RomanceElena, 7)
    $ TimeAdvTo(TIME_DAY_END)
    jump rom_FirstDanceGrind
