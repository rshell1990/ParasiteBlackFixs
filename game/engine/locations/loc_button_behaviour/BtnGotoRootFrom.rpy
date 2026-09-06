init -1 python:
    ### (supposedly) returns to 'parent' location until there's no 'parent' locs left
    class BtnGotoRootFrom(ButtonBehaviour):
        def __init__(self, hoverTxt, FromLoc, goDirect = False):
            super().__init__()

            self.FromLoc = FromLoc
            self.hoverTxt = hoverTxt
            self.goDirect = goDirect # If true, go directly to root location ignoring any parent links in-between. Not recommended since it may avoid triggers

        def getHoverTxt(self):
            return self.hoverTxt

        def execute(self):
            TooltipClear()
            if self.clickSfx is not None:
                renpy.play(self.clickSfx, channel = "sound")
            tmpLoc = self.FromLoc
            route = []
            timeout = 20
            while tmpLoc.parent is not None:
                tmpLoc = tmpLoc.parent
                route.append(tmpLoc.tag)
                timeout -= 1
                if timeout <= 0:
                    break

            if len(route) > 0:
                if self.goDirect:
                    LocSet(route[-1])
                else:
                    LocSet(route[0])
                    autoMoveQ = route[1:]
