label DarkKnightNovarasPatrol:
    show mc with dissolve:
        xcenter 0.15
    MC "(City at night means trouble.)"
    MC "(Should I try find some?)"
    menu:
        "(DEV) complete" (AppearIf = config.developer):
            $ QstDarkKnight().gangsSlain = 3
            MC "(That should be enough law enforcement for now.)"
            MC "(I should report to Captain Nyx.)"
            $ QstSetProgress(QstDarkKnight, 2)
            $ LocEnterQ()
        "{image=[ICON.CLOCK]} Patrol the streets":
            hide mc with dissolve
            jump DarkKnightNovarasPatrolTry
        "Not now":
            hide mc with dissolve
            show screen NovarasPatrolScreen()
            $ LocEnterQ()

label DarkKnightNovarasPatrolTry:
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "I've walked the streets of Novaras preparing myself for a fight."
    $ rng = RngInt(1,2)
    if rng == 1:
        "However, no matter which dark corner I poked my nose in, I could not find a single troublemaker."
        $ TimeAdvBy(TIME_05H)
        $ LocFlush(dissolve)
        show screen NovarasPatrolScreen()
        $ LocEnterQ()
    else:
        "For better or worse, I have stumbled upon a group of shady looking men."
        $ LocFlush()
        show mc:
            xcenter 0.15
        with dissolve
        show cg_bandit_dark onlayer characters as bandit1:
            xcenter 0.6
            zoom 1.0
            xzoom -1.0
        with dissolve
        show cg_bandit_dark onlayer characters as bandit2:
            xcenter 0.4
            zoom 0.9
            xzoom -1.0
        with dissolve
        show cg_bandit_dark onlayer characters as bandit3:
            xcenter 0.8
            zoom 0.8
            yoffset 50
            xzoom -1.0
        with dissolve

        THUG "You'll know better than stroll around here."

        $ AutoMus(False)
        $ PlayMusicRandom("mus_battle_generic")

        THUG "Get him, boys!"
        hide mc
        hide bandit1 onlayer characters 
        hide bandit2 onlayer characters 
        hide bandit3 onlayer characters 
        with dissolve
         
        $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = GetEnemyList("novaras_patrol_bandits"), CanTransform = False))

        $ TimeAdvBy(TIME_05H)
        "No thugs left standing, I caught my breath."
        $ AutoMus(True)
        $ LocFlush()
        show mc:
            xcenter 0.15
        with dissolve
        MC "(Phew... That'll teach them.)"
        $ QstDarkKnight().gangsSlain += 1
        if QstDarkKnight().gangsSlain >= 3:
            MC "(That should be enough law enforcement for now.)"
            MC "(I should report to Captain Nyx.)"
            $ QstSetProgress(QstDarkKnight, 2)
        else:
            show screen NovarasPatrolScreen()
        $ LocEnter()

screen NovarasPatrolScreen():
    if not block_wait_global and not block_wait_dynamic and wLocs[GetLocID()].CanWait:
        if QstGetProgress(QstDarkKnight) == 1:
            if not IsDaytime():
                if QstDarkKnight().gangsSlain < 3:
                    fixed:
                        fit_first True
                        align (0.75,0.85)
                        text tra(_("Gangs slain: %s/3")) % QstDarkKnight().gangsSlain:
                            xalign 0.5
                            yoffset -40
                        add "images/gui/buttons_loc/underlay.webp":
                            xalign 0.5
                        imagebutton:
                            idle "images/gui/buttons_loc/fight.webp"
                            hovered TooltipSetUI(_("Patrol"))
                            unhovered TooltipClearUI()
                            focus_mask "images/gui/buttons_loc/underlay.webp"
                            xalign 0.5
                            action [TooltipClearUI(), Hide("NovarasPatrolScreen"), Jump("DarkKnightNovarasPatrol")]

image cg_bandit_dark:
    "images/characters/_chars_cg/cg_bandit.webp"
    matrixcolor BrightnessMatrix(-1.0)
# shorthands
image cg_bandit2:
    "images/characters/_chars_cg/cg_bandit.webp"
image cg_bandit3:
    "images/characters/_chars_cg/cg_bandit.webp"
image cg_bandit4:
    "images/characters/_chars_cg/cg_bandit.webp"