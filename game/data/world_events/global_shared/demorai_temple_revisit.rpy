init python:
    @AppendToAllQuests
    class DemoraiTempleRevisit(LogicModule):
        def onEnter(self):  
            if GetLocID() == "demorai_temple_interior":
                return TriggeredEvent("ev_demorai_temple_reenter")

label ev_demorai_temple_reenter:
    $ QstComplete(DemoraiTempleRevisit)
    'As I entered the Ruins once again, I realized how deathly quiet it was.'
    MC "(Abandoned... Looks like they've all left.)"
    $ LocEnterQ()