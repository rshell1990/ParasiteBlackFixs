init -1 python:
    ### tells a line of dialogue via narrator 
    class BtnFluffTxt(ButtonBehaviour):
        def __init__(self, hoverTxt, fullLine):
            super().__init__()

            self.hoverTxt = hoverTxt
            self.fullLine = fullLine

        def getHoverTxt(self):
            return self.hoverTxt

        def execute(self):
            TooltipClear()
            if isinstance(self.fullLine, list):
                for line in self.fullLine:
                    narrator(line)
            else:
                narrator(self.fullLine)
