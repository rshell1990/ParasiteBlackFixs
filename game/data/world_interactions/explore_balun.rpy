init python:
    @AppendToAllQuests
    class ExploreLakeBalun(LogicModule):
        def locationMod(self):
            btnMods = {}
            if not 2 <= QstGetProgress(QstTheBloodhound) <= 3: # basically if there's no defenders of realm camp
                btnMods["btn_lake_balun_explore"] = BtnJumpLabel(_("Explore"), "explore_lake_balun")
            return LocButtonMod(directMods = btnMods)

label explore_lake_balun:
    MC "(I will most likely find some slimelarks wandering around here.)"
    menu:
        "Collect wildflowers" if QstIsActive(QstHumanExp) and QstGetProgress(QstHumanExp) == 10:
            scene black with dissolve
            $ TimeAdvBy(TIME_05H)
            MC "(Okay, hopefully these will be enough.)"
            $ PlayerAddItem("qst_wild_flowers")
            $ LocFlush()
            with dissolve
            MC "(I just hope this works...)"
            $ QstSetProgress(QstHumanExp, 11)
            $ LocEnterQ()

        "{image=[ICON.CLOCK]} Look around":
            scene black with dissolve
            $ TimeAdvBy(TIME_1H)
            "I've wandered around the lake and in a while, looking for slimelarks."
            $ rng = RngInt(1,3)
            if rng == 1:
                "However, I could not find any."
                $ LocEnter()
            else:
                scene cg_blue_slimelarks with dissolve
                "I have soon spotted a group of slimelarks near the water."
                "Drawing my blade, I rushed towards them!"
                $ AutoMus(False)
                $ PlayMusicRandom("mus_battle_generic")
                $ StartBattle(BattleData(BackgroundImage = "pbat_lake", CharIDList_Right = GetEnemyList("lake_balun_slimelarks")))
                $ AutoMus(True)
                "Slimelarks defeated, I checked if there were any remains left."
                MC "(There, that should do.)"
                $ PlayerAddItem("slimelark_remains", RngInt(1, 2))
                $ LocEnter()
        "Don't":
            $ LocEnterQ()