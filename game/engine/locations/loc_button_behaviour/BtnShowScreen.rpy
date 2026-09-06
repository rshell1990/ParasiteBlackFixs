init -1 python:
    ### shows screen, also takes screen args
    class BtnShowScreen(ButtonBehaviour):
        def __init__(self, hoverTxt, screen, *args, **kwargs):
            super().__init__()

            self.hoverTxt = hoverTxt
            self.screen = screen
            self.args = args
            self.kwargs = kwargs

        def getHoverTxt(self):
            return self.hoverTxt

        def execute(self):
            TooltipClear()
            if self.clickSfx is not None:
                renpy.play(self.clickSfx, channel = "sound")
            renpy.show_screen(self.screen, *self.args, **self.kwargs)