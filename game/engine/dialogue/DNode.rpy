init python:
    class DNode(object):
        def __init__(self, txtLabel, label, nextNode = None, order = 0):
            self.order = order
            self.label = label
            self.txtLabel = txtLabel
            self.nextNode = nextNode

        def getId(self):
            return "%s|%s" % (self.txtLabel, self.label)

    debugNode = DNode("...", "dialogue_nothing", nextNode = "DNodeExit")
