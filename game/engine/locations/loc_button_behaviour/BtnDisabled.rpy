init -1 python:
    # does nothing, used as nil value quite often
    class BtnDisabled(ButtonBehaviour):
        def isEnabled(self):
            return False
