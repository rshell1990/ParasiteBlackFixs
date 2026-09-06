label scr_SharedInThorns_babazhulClue:
    show babazhul:
        pos (0.0, 0.0)
    with dissolve
    BABAZHUL @talk 'Heh heh! Yes, the Thornfalls.'
    MC 'How did you know?'
    BABAZHUL @talk 'Child, have you not learned by now such questions are meaningless?'
    BABAZHUL @talk 'You seek to know what shadow plagues their bloodline.'
    MC 'So it is true then? They {i}are{/i} cursed?'
    BABAZHUL @talk 'Such a strong word... {i}cursed.{/i}'
    MC 'Then what are they?'
    BABAZHUL @talk 'Hehehe!'
    BABAZHUL @talk '{i}...Elena.{/i}'
    ELENA  '...'
    BABAZHUL @talk 'How long you have spent hiding your true self? Come girl.'
    BABAZHUL @talk 'Show some courage and perhaps I might answer your questions.'
    "Standing onto her hind legs, Elena's body shifted and formed back into her humanoid shape."
    ELENA 'Satisfied Soothsayer?'
    BABAZHUL @talk '...Beautiful, such a shame to see one so hidden away from the world.'
    ELENA 'Enough games! You swore to answer our questions!'
    BABAZHUL @talk "I swore nothing, only said I 'might' girl."

    ELENA "She's just wasting our time, let's-"

    hide babazhul
    show cg_nov_witch_glow
    with dissolve
    play sound "audio/cfx/detect_magic.ogg"
    $ CharSetVar("babazhul", "lit", "yes")
    BABAZHUL @talk 'Heed my words and listen close.'
    BABAZHUL_MAD @talk 'All this gold, such a delight!'
    BABAZHUL_MAD @talk "But fortune's favor, comes with a price!"
    BABAZHUL_MAD @talk "Come darkness falls, the toll is paid."
    BABAZHUL_MAD @talk "Come morning light, their souls are saved."
    #the ball dims
    hide cg_nov_witch_glow
    with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    show babazhul
    MC 'But what did any of that mean?'
    BABAZHUL @talk 'I can say no more...'
    hide babazhul
    MC "(I need to talk to Elena later in private about what we've heard.)"
    $ QstSharedInThorns().cluesCollected.append("witch")
    $ GoalComplete(QstSharedInThorns, 1)
    $ GoalShow(QstSharedInThorns, 5)
    return
