label scr_nijah_damzelDizztrezz_goToTarekOfficeWithEvidence:
    'Knocking on the iron door, a slider opened as two piercing eyes looked the other side.'

    THUG @talk 'Password?'
    MC @talk "Silver tits on top of a golden ass."
    THUG @talk 'Wha~'
    MC @talk "Go tell Tarek we've brought proof!"
    scene black with dissolve
    "After some muffled cursing, I heard the thug on the other side shuffle away."
    "In a moment, a door opened and we were let in."
    "Tarek awaited in his office."
    $ LocSet("novaras_black_diamond_office")
    $ LocFlush()
    show tarek at center_f
    with dissolve
    show markus at right_f
    show mc at left
    with easeinleft
    MC @talk 'I have the proof you require Tarek.'
    TAREK @shock 'What?! Show me!'
    $ PlayerRemItem('qst_tarek_bloody_scroll',1)
    $ GoalComplete(QstDamzelInDiztrezz, 9)

    'I handed over the bloodied scroll to Tarek.'
    MC @talk "The other factions are about to turn on you, the Vulshan and Khazah's know you are trying to weaken them by handing over their territory to the lesser factions."
    TAREK 'I-'
    "Tarek's face became sullen as the reality dawned on him."
    TAREK @sad "Yes... I can see now, it's all falling apart."
    MC @talk 'Surely you must have known trying to weaken their factions would result on them to turn on you?'
    TAREK 'The Vulshan and Khazahs have been fighting for decades, I knew both were undermining my authority so what else was I supposed to do?'
    TAREK @sad 'Not that it matters now... You were right it seems, this was inevitable.'
    MC @talk 'What will you do now?'
    TAREK 'Worry not, I will keep my word and leave...'
    TAREK '...But not before I let loose and hand over all the information I have to the inquisitors!'
    MC @talk "You'll try strike a deal with them?"
    TAREK "Why not? As it stands, I am a dead man... At least if I can offer them something in return, perhaps I may just walk away from all this with something to show still..."
    MC @talk '...And Nijah?'
    TAREK 'Consider her debt settled.'
    TAREK 'Before I go, you should know in my absence things may become more... {i}violent{/i} for a while.'
    TAREK @angry "The violence I've tried to hold back will spill out in the power struggle to follow."
    MC @talk 'Where will you go?'
    TAREK 'Who knows!'
    TAREK 'Perhaps we may even run into each other again...'
    TAREK "Don't worry, I won't forget what you did for me here today."
    TAREK 'You could have just tried to kill me.'
    MC @talk "That's not my way."
    TAREK "Hm... Perhaps there are still honest men in this land then."
    TAREK 'Farewell friend, I will be gone by nightfall.'
    $ QstDamzelInDiztrezz().PlayerMadeTarekLeaveEvidence = True
    $ BlackDiamondLogic().tarekFate = "walked"
    MC @talk 'Farewell, Tarek.'
    scene black with dissolve
    jump nijah_damzelDiztrezz_afterActionEvidence
