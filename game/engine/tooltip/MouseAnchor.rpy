python early:
    # Fixed-like element that is positioned relative to the mouse
    # ex:
    #    mouseAnchor (0.5,0):
    #        text "This is centered below the mouse"
    class MouseAnchor(renpy.display.layout.Container):
        def __init__(self, posData, **properties):
            super(MouseAnchor,self).__init__(**properties)
            self.anchor =       (posData[0], posData[1])
            self.absOffset =    (posData[2], posData[3])

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            maxWidth, maxHeight = (0,0)
            childRenders = []
            for c in self.children:
                cr = renpy.render(c, width, height, st, at)
                maxWidth = max(cr.width,maxWidth)
                maxHeight = max(cr.height,maxHeight)
                childRenders.append(cr)

            mX, mY = renpy.get_mouse_pos()
            offset = [mX - self.anchor[0] * maxWidth + self.absOffset[0], mY - self.anchor[1] * maxHeight + self.absOffset[1]]

            # tooltip is repositioned when too close to edge
            # otherwise mouse partially covers text
            if offset[0] > config.screen_width - maxWidth:
                offset[0] = offset[0] - maxWidth - self.absOffset[0]

            # prevent child element from going beyond screen
            maxOffset = (config.screen_width - maxWidth, config.screen_height - maxHeight)
            minOffset = (0, 0)
            offset2 = (min(maxOffset[0], max(0, offset[0])) , min(maxOffset[1], max(0, offset[1])))

            for cr in childRenders:
                rv.subpixel_blit(cr,offset2)

            renpy.redraw(self,0)

            return rv

    obj = renpy.register_sl_displayable("mouseAnchor",MouseAnchor,"fixed","many")
    obj.add_positional("posData")
