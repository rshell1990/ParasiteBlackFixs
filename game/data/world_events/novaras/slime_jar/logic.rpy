init python:
    notesLib["slimeJarInspect"] = Note(
        _("Inspect the Slimelark"),
        _("I should find someplace private to take a look at what's going on with the baby Slimelark.\nIn this city, my bedroom seems like the only adequate spot."))
    @AppendToAllQuests
    class PrimerSlimeJar(LogicModule):
        def onEnter(self):  
            if self.progress == 0:
                return TriggeredEvent("ev_slime_jar")
            if GetLocID() == "mc_house_bedroom":
                if self.progress == 1:
                    return TriggeredEvent("ev_slime_jar_2")

        def onComplete(self):
            QstStart(QstRavenousJelly)
            return

label ev_slime_jar:
    show mc at left with easeinleft
    "I could feel the slimelark shifting and moving around in the container as it bashed against the walls."
    MC "(Hm... Maybe this wasn't such a good idea.)"
    MC "(I should inspect it somewhere private.)"
    MC "(My bedroom?)"
    $ QstSetProgress(PrimerSlimeJar, 1)
    $ NoteUnlock("slimeJarInspect")
    $ LocEnter()

label ev_slime_jar_2:
    show mc at center with dissolve
    $ NoteLock("slimeJarInspect")
    "As I gently opened up the container to peer inside, the young slime slithered and moved around slowly in there, but it was clearly curious about my presence."
    MC "(Hmm... Maybe it's hungry?)"
    "I considered for a moment that maybe taking this creature in was a bad idea, but I had already gone this far now, and felt some responsibility for it."
    $ PlayerRemItem("qst_slime_jar")
    $ QstComplete(PrimerSlimeJar)
    MC "(Knowing what these things eat...)"
    MC "(Perhaps some meat?)"
    if PlayerItemQty("red_meat") > 0:
        MC "(Should I just try feed it some?)"
        $ QstSetProgress(QstRavenousJelly, 1)
    else:
        "I have stashed the container under my bed and set out to get some meat."
        hide mc with dissolve
    $ LocEnter()