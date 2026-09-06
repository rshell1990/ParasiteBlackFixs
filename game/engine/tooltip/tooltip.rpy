screen tooltip():
    zorder 100
    mouseAnchor (0, 0, 45, 50):
        if not (isinstance(mtt.value, Text) and mtt.value.get_all_text() == ""):
            frame:
                xmaximum 640
                padding (16, 12)
                text mtt.value

init python:
    class TooltipValueHolder(Tooltip):
        def __init__(self):
            self.default = Text("")
            self.value = self.default

    # for screens
    def TooltipSetUI(NewVal):
        return Tooltip.Action(store.mtt, NewVal)
    def TooltipClearUI():
        return Tooltip.Action(store.mtt, Text(""))
    
    # for non-screens
    def TooltipSet(NewVal):
        store.mtt.value = NewVal
        return
    def TooltipClear():
        store.mtt.value = Text("")
        return

    store.mtt = TooltipValueHolder()
