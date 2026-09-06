default CurrentDifficulty = 1 # 0 == easy, 1 == normal, 2 == hard

init python in DIFFICULTY:
    _constant = True
    PLAYERSIDE_DMG = {0:1.5, 1:1.0, 2:0.5}
    ENEMYSIDE_DMG = {0:0.5, 1:1.0, 2:1.5}
    NAMES = {0:_("Easy"), 1:_("Normal"), 2:_("Hard")}
    INFECTION_GAIN = {0:0.75, 1:1.0, 2:1.0}

init python:
    CurrentDifficultyDesc = {
        0: _("For those more interested in the story than the struggle..."),
        1: _("The default Parasite Black experience... As it was intended to be played."),
        2: _("(WIP) For those ready to prove their mettle and truly earn their conquests."),
    }

    CurrentDifficultyDescColor = {
        0: "#00ff00ff",
        1: "#fffb00ff",
        2: "#ff0000ff",
    }
