screen infection_bar():
    default ComingStormCountdownFade = 1.0

    if QstIsActive(InfectionModule) and IsUIDisplayed():
        ###
        if QstIsActive(QstTheComingStorm):
            if QstTheComingStorm().ShowAndSpinCountdown:
                if QstTheComingStorm().DaysLeft > 0:
                    if not IsPlayerInBattle():
                        mousearea:
                            area (0.2, 0.0, 0.6, 0.1)
                            hovered SetScreenVariable("ComingStormCountdownFade", 0.35)
                            unhovered SetScreenVariable("ComingStormCountdownFade", 1.0)

                        frame:
                            anchor (0.5, 0.5)
                            pos (0.5, 0.045)
                            padding (20, 10)
                            at UITF_ComingStormFade(ComingStormCountdownFade)
                            hbox:
                                label tra(_("Days before Demorai siege: %s")) % QstTheComingStorm().DaysLeft
        button:
            add "images/gui/unsorted/infection_bar.webp":
                xalign 0.5
                xzoom 0.73
            bar:
                xalign 0.5
                yalign 0.0
                xsize 666
                ysize 20
                left_bar Frame(Transform("images/gui/bars/bar2_fill_red.webp", zoom = 0.35), Borders(32, 32, 32, 32))
                right_bar Frame(Transform("images/gui/bars/bar2_under_red.webp", zoom = 0.35), Borders(32, 32, 32, 32))
                value AnimatedValue(value = InfectionModule().CurrentValue, range = InfectionModule().MaxValue, delay = 0.1)
            xsize 666
            ysize 30
            align (0.5, 0.0)
            background Null()
            keyboard_focus False
            hovered TooltipSetUI(tra(_("Parasite infection level: %s/100\nIf it reaches maximum, {color=#e60f00}it's game over.{/color}")) % InfectionModule().CurrentValue)
            unhovered TooltipClearUI()
            action NullAction()

transform UITF_ComingStormFade(Value):
    alpha Value