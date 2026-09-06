init -2 python:
    class ButtonBehaviour(object):
        BtnLocTag = None

        def __init__(self):
            self.clickSfx = None

        def withSfx(self,sfxPath):
            self.clickSfx = sfxPath
            return self

        def isEnabled(self):
            return True

        def getHoverTxt(self):
            return ""

        def execute(self):
            TooltipClear()
            if self.clickSfx is not None:
                renpy.play(self.clickSfx, channel = "sound")
            pass
