init -1 python:
    class LocButtonMod(object):
        def __init__(self, blacklist = None, whitelist = None, directMods = None, priority = 0):
            self.priority = priority
            self.blacklist = blacklist
            self.whitelist = whitelist
            self.directMods = ({} if directMods is None else directMods)

        def modBtn(self, tag):
            if (self.blacklist is not None and tag in self.blacklist) or \
                (self.whitelist is not None and tag not in self.whitelist):
                return BtnDisabled()
            elif tag in self.directMods:
                return self.directMods[tag]
            else:
                return None