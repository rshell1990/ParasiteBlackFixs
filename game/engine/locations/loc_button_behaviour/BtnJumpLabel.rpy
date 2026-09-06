init -1 python:
    ### jumps to label
    class BtnJumpLabel(ButtonBehaviour):
        def __init__(self, hoverTxt, label):
            super().__init__()
            self.hoverTxt = hoverTxt
            self.label = label

        def getHoverTxt(self):
            return self.hoverTxt

        def execute(self):
            TooltipClear()
            if self.clickSfx is not None:
                renpy.play(self.clickSfx, channel = "sound")
            renpy.with_statement(Dissolve(0.05))
            renpy.jump(self.label)
            
            return