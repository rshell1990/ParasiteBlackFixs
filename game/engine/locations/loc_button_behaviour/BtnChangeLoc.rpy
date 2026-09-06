init -1 python:
    ### changes location
    # destTag is a single tag or a list of tags
    # If it's a list then the locations will be visited in auto-pilot mode
    class BtnChangeLoc(ButtonBehaviour):
        def __init__(self, hoverTxt, destTag):
            super().__init__()

            if not isinstance(destTag,list):
                destTag = [destTag]

            self.BtnLocTag = destTag[-1]
            self.movePath = destTag
            self.hoverTxt = hoverTxt

        def getHoverTxt(self):
            return self.hoverTxt

        def execute(self):
            TooltipClear()
            if self.clickSfx is not None:
                renpy.play(self.clickSfx, channel = "sound")
            # i dont really think any fo that shit is necessary
            LocSet(self.movePath[0])
            autoMoveQ = self.movePath[1:]
            return