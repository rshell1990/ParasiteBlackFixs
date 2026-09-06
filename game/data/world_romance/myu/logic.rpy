init python:
    @AppendToAllQuests
    class RomanceMyu(LogicModule):
        def __init__(self):
            super().__init__()

            self.tumbleMood = True

        def onMidnight(self):
            if self.tumbleMood == False:
                self.tumbleMood = True
                return
            if RngInt(1, 3) == 1:
                self.tumbleMood = False

        def extraDialogue(self):
            yield ("myu_root", DNode(_("How about a hug?"), "rom_myu_hug"))
            yield ("myu_root", DNode(_("Myu, are you in the mood for some... {i}private time?{/i}"), "rom_myu_somefun"))