label qst_DamzelDizzt_3_VulshanRevolt:
    'The man nodded, and as he stepped towards one of the other guards, he suddenly unsheathed his blade and slashed him down!'
    THUG @talk 'LONG LIVE THE VULSHAN!'
    MARKUS "Well this isn't how I expected things to go!"
    $ PlayMusic("audio/music/31_Encounter.ogg")
    $ AutoMus(False)
    'Suddenly, the whole Hall erupted into violence.'
    play sound2 "audio/cfx/transform.ogg"
    'Me and Markus transformed and threw ourselves into the fight.'
    $ TransformMC(True)
    $ TransformMarkus(True)
     
    $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_bandit", "e_thug", "e_bandit"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    scene bg_diamond_blood with dissolve

    show mc_transformed:
        xcenter 0.2
    show markus_transformed:
        xcenter 0.8
        xzoom -1.0

    $ GoalComplete(QstDamzelInDiztrezz, 4)
    TAREK 'What is this madness? Traitors! Show yourselves!'
    "Tarek's eyes glanced over towards us."
    TAREK 'M-Monsters! What have you brought into this place you fools?!'
    THUG @talk 'You are the traitor Tarek! No longer will we be subservient to your lies!'
    THUG @talk 'VULSHAN! LET US END THIS!'

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ StartBattle(BattleData(BackgroundImage = "pbat_diamond", CharIDList_Right = ["e_corruptGuard", "tarek", "e_bandit"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    $ BlackDiamondLogic().tarekFate = "diedVulshan"
    'Tarek finally dropped to the floor, gashes and wounds deep into his flesh as he wretched up blood, the surviving Vulshan hacking at him with his blades.'
    'Finally, they turned towards me and Markus.'
    scene bg_diamond_blood

    show markus_transformed:
        xcenter 0.2
    show mc_transformed:
        xcenter 0.5
    show cg_bandit at right_f
    with dissolve
    THUG @talk 'The deed is done.'
    THUG @talk 'Go now, before the guards arrive, we will clean up the mess.'
    'Turning towards a terrified Nijah, I called her forward and she nervously stepped closer, her face sickly pale white as her eyes remained fixed on me and Markus in our other forms.'
    show nijah with easeinright:
        xcenter 0.7
        xzoom -1.0
    NIJAH 'You... You are both...'
    MC @talk 'This one, Nijah... Her debt is to be wiped.'
    THUG @talk 'Consider it done! Now go!'
    $ QstDamzelInDiztrezz().PlayerSidedWithVulshan = True
    scene black with dissolve
    'Taking Nijah by hand, I led her away with Markus as we hurried away into the night.'
    $ AutoMus(True)
    jump nijah_damzelDiztrezz_afterAction
