init python:
    notesLib["brothelAd1"] = Note(
        _("Elves at the bordello?"),
        _("A young boy bumped into me as I was wandering around Novaras. The flyer he shoved in my hands mentioned Elves working in the Brothels, night time...\nPerhaps I should swing by one night and see what I can see?"))
    notesLib["brothelAd2"] = Note(
        _("An elf at the bordello?"),
        _("This mysterious elven 'worker' seems to only show up once in a few nights. I wonder if I'd bump into {i}him{/i}."))

    @AppendToAllQuests
    class EventBrothelAd(LogicModule):
        def __init__(self):
            super().__init__()

            self.startSpamDay = -1

        def onEnter(self):  
            if self.progress == 0:
                if self.startSpamDay == GetGameDay():
                    if IsDaytime():
                        if GetLocID() == renpy.random.choice(LocIDList_NovarasCityStreets):
                            if RngInt(1, 3) == 3:
                                return TriggeredEvent("event_brothel_ad_1")
            elif self.progress == 1:
                if GetLocID() == "novaras_bordello_interior":
                    if not DrosInBordello().bordelloNight:
                        return TriggeredEvent("event_brothel_ad_2")

        def onStart(self):
            self.startSpamDay = GetGameDay() + 1 # so that a day passes till we get the memo
            return

label event_brothel_ad_1:
    show mc with dissolve:
        xalign 0.65
        xzoom -1.0
    'While wandering the streets of Novaras, a young boy came hurtling towards me with a flyer in his hand.'
    show mcprologue with easeinleft:
        xalign 0.3
        yoffset 150
        #xzoom -1.0
        zoom 0.9
        matrixcolor BrightnessMatrix(-1.0)

    YOUNG_BOY 'Hey! We got the best pussy! We got the best ass in Novaras!'
    YOUNG_BOY 'We even got elven sluts and more!'
    YOUNG_BOY 'Come to see us if you want the best time in Novaras!'
    'The boy was already hurrying off to hand off his flyers to other potential patrons before I could even answer him.'
    hide mcprologue with easeoutright
    'The thought bemused, but as I looked down to the sheet, I could see it was advertising the brothel {i}I{/i} knew of.'
    MC '(Hm... Elves are working there now?)'
    MC "(I've never seen an elf there... Perhaps I should check it out sometime?)"
    $ NoteUnlock("brothelAd1")
    $ QstSetProgress(EventBrothelAd, 1)
    $ LocEnter()

label event_brothel_ad_2:
    show mc:
        xalign 0.2
    MC "(I don't see any elves around here.)"
    'As Helena was passing by, I called over to her.'
    show helena:
        xalign 0.8
    MC @talk 'Hey, are there any elves working here?'
    HELENA @talk 'Elves?'
    HELENA @talk 'Well, there is one.'
    HELENA @talk "Though saying they work here is quite a stretch..."
    MC @think 'What does that mean?'
    HELENA @talk "Never mind, he's not in today anyway."
    'Helena continued to stroll off in the direction she was heading before.'
    'Looking over her shoulder, she cried out to me,'
    HELENA @talk 'Try again tomorrow maybe!'
    hide helena with dissolve
    $ NoteLock("brothelAd1")
    $ NoteUnlock("brothelAd2")
    $ QstComplete(EventBrothelAd)
    MC '(...{i}He?{/i})'
    $ LocEnter()