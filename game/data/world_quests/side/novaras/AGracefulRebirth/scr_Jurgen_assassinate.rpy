label jurgen_1_tavern_assassinate:
    MC @talk "Not here, there's too many people."
    MC @talk 'We need to talk somewhere private.'
    'Jurgen seemed suspicious, he waved over two of his friends.'
    JURGEN 'You lads stay back but come with me.'
    JURGEN "This one here says he might have something to help us."
    MC '(Shit... Not what I was hoping for.)'
    JURGEN "Well? Where shall we speak?"
    MC "This way..."
    scene black with dissolve
    #Cut to black - Show city map as player and Jurgen talk
    'I lead Jurgen down into one of the quiet back Alleyways, the two guards kept enough of a distance not to listen in but follow us.'
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    with dissolve
    show mc:
        xcenter 0.15
    show cg_guard:
        xalign 0.77
        xzoom -1.0
    with dissolve
    JURGEN "Now, what have you got for me?"
    menu:
        'Nothing but the sweet embrace of death.':
            JURGEN 'I should have known!'
            JURGEN 'Men! To arms!' #Battle begins 
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = [{"e_jurgen":3}, "e_guard", "e_guard"], CanTransform = False))
            'After slaying Jurgen and his men, I fled into the many back alleys, doing my best to not be seen.'
            'My heart raced at what had just happened, no doubt about it... {i}I was a murderer.{/i}'
            "But still I told myself I did what needed to be done, or at least, {i}that's what I kept telling myself anyway.{/i}"
            $ QstGracefulRebirth().jurgenActive = False
            $ QstGracefulRebirth().jurgenGone = True
            $ GoalComplete(QstGracefulRebirth, 1.5)
            $ AutoMus(True)
            $ LocEnter()

        '{i}*Whistle a signal to the Vulshan*{/i}' if BlackDiamondLogic().tarekFate == "diedVulshan": #Only available if player helped the Vulshan takeover the Black Diamond 
            'From out the shadows, the Vulshan came, blades drawn.'
            JURGEN 'W-What is-' #battle where the Vulshan help MC or not?
            scene black with dissolve
            "The guards behind Jurgen fell, their throats slit by the Vulshan assassins."
            "A second later, Jurgen himself joined his entourage on the rocky alley floor."
            "Blood poured from beneath his armour plates as he struggled to breathe."
            JURGEN "Who- Argh..."
            "A final, gargled choking gasp escaped his lips before he finally fell silent."
            $ LocFlush()
            show cg_bandit at right_f:
                matrixcolor BrightnessMatrix(-0.1)
            with dissolve
            VULSHAN @talk 'Leave now... We will take care of the rest.'
            scene black with dissolve
            'I nodded, taking off into the shadows once again, the dark deed done.'
            $ QstGracefulRebirth().jurgenActive = False
            $ QstGracefulRebirth().jurgenGone = True
            $ GoalComplete(QstGracefulRebirth, 1.5)
            $ LocEnter()