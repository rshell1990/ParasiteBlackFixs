init python:
    # this is used by locnav to return certain events when conditions are met
    # ex: on entering house if its not daytime, makes it call label 'door_locked'
    class TriggeredEvent(object):
        def __init__(self, label, priority = 0):
            # Higher is the number, higher is the priority
            self.priority = priority
            self.label = label
