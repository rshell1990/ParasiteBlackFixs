python early:
    # Fixed-like element that is positioned relative to the mouse.
    # ex:
    #    mouseAnchor (0.5, 0, 0, 10):
    #        text "This is centered below the mouse"
    class MouseAnchor(renpy.display.layout.Container):
        def __init__(self, pos_data, **properties):
            super(MouseAnchor, self).__init__(**properties)
            self.anchor = (pos_data[0], pos_data[1])
            self.abs_offset = (pos_data[2], pos_data[3])

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            max_width = max_height = 0
            child_renders = []
            for c in self.children:
                cr = renpy.render(c, width, height, st, at)
                max_width = max(cr.width, max_width)
                max_height = max(cr.height, max_height)
                child_renders.append(cr)

            mouse_x, mouse_y = renpy.get_mouse_pos()
            offset = [
                mouse_x - self.anchor[0] * max_width + self.abs_offset[0],
                mouse_y - self.anchor[1] * max_height + self.abs_offset[1],
            ]

            # Tooltip is repositioned when too close to the edge,
            # otherwise the mouse partially covers the text.
            if offset[0] > config.screen_width - max_width:
                offset[0] -= max_width + self.abs_offset[0]

            # Prevent the child element from going beyond the screen.
            offset = (
                min(config.screen_width - max_width, max(0, offset[0])),
                min(config.screen_height - max_height, max(0, offset[1])),
            )

            for cr in child_renders:
                rv.subpixel_blit(cr, offset)

            renpy.redraw(self, 0)

            return rv

    renpy.register_sl_displayable("mouseAnchor", MouseAnchor, "fixed", "many") \
        .add_positional("pos_data")
