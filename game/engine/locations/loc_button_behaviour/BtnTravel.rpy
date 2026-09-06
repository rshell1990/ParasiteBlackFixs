init -1 python:
    ### shows travel screen (only to travel out of some loc)
    class BtnTravel(ButtonBehaviour):
        def __init__(self):
            super().__init__()

            self.hoverTxt = _("Travel")

        def getHoverTxt(self):
            return self.hoverTxt

        def execute(self):
            TooltipClear()
            if self.clickSfx is not None:
                renpy.play(self.clickSfx, channel = "sound")
            renpy.show_screen("map", OpenTab = "world", Context = "world_at_exit_loc")
            renpy.with_statement(Dissolve(0.15))
            return