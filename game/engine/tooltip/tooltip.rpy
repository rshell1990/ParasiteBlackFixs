screen tooltip():
    zorder 100
    mouseAnchor (0, 0, 45, 50):
        if is_tooltip_visible(mtt.value):
            frame:
                xmaximum 640
                padding (16, 12)
                text mtt.value

init python:
    EMPTY_TOOLTIP = Text("")

    def _as_text(val):
        """Coerce plain strings to Text displayables so the tooltip screen
        always receives a Text value (matching its visibility guard)."""
        if isinstance(val, Text):
            return val
        return Text(val)

    def is_tooltip_visible(value):
        """True when the tooltip has content to show (not an empty Text)."""
        return not (isinstance(value, Text) and value.get_all_text() == "")

    class TooltipValueHolder(object):
        """Simple holder for the current tooltip value (no legacy Tooltip class)."""
        def __init__(self):
            self.default = EMPTY_TOOLTIP
            self.value = self.default

    # for screens (usable as hovered/unhovered actions)
    def TooltipSetUI(NewVal):
        return Function(_TooltipSetUIImpl, NewVal)
    def _TooltipSetUIImpl(NewVal):
        store.mtt.value = _as_text(NewVal)
    def TooltipClearUI():
        return TooltipSetUI(EMPTY_TOOLTIP)

    # for non-screens
    def TooltipSet(NewVal):
        store.mtt.value = _as_text(NewVal)
        return
    def TooltipClear():
        store.mtt.value = EMPTY_TOOLTIP
        return

    store.mtt = TooltipValueHolder()
