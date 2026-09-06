init python:
    @AppendToAllQuests
    class EventElenaWhoIsNijah(LogicModule):
        def onExit(self):  
            if GetLocID() == "novaras_dist_house":
                if PlayerPos.lastTag == "mc_house_kitchen":
                    if QstIsActive(EventNijahRescue):
                        if QstGetProgress(EventNijahRescue) >= 2:
                            if QstIsActive(QstBiteBark):
                                if QstGetProgress(QstBiteBark) >= 6:
                                    if not CharInParty("elena"):
                                        return TriggeredEvent("ev_elenaAsksAboutNijah")
                                            # fucking kill me
                                                # someone


label ev_elenaAsksAboutNijah:
    $ QstComplete(EventElenaWhoIsNijah)
    $ LocSet("mc_house_kitchen")
    $ LocFlush()
    with dissolve
    show mc:
        xcenter 0.55
    with dissolve
    "As I was about to leave, I felt someone stop me."
    MC @talk "Wha~"
    show elena with dissolve:
        xcenter 0.35
        xzoom -1.0
    ELENA @talk 'Who is she?'
    MC @talk "Elena! Change back! You could be-"
    ELENA @angry "I sneaked past [regina_ref!t], now who is the girl?"
    menu:
        'Someone who needs my help.':
            ELENA @sad '{i}*Sigh*{/i} I see.'
            ELENA @grumpy "Just be careful please? You can't just go helping every pretty face you see."
            ELENA @grumpy 'If the wrong person talks to the inquisitors about us, things will not be pleasant.'
            MC @talk 'Relax Elena, I have things under control.'
            MC @talk 'She will be gone soon enough.'
            ELENA @grumpy "Good... People like us can't go relying on others."
            #Nijah calling from bedroom
            NIJAH '[player_name!t]? Iz someone there?'
            'Elena transformed back into a wolf once again, trotting off once again.'
            MC @talk 'N-No Nijah! Just a neighbour of mine!'
            NIJAH 'O-Okay!'
        'Someone I want to fuck.':
            ELENA @angry 'Damn it [player_name!t], you need to take things more seriously!'
            ELENA @grumpy 'What if she uncovered the two of us?'
            ELENA @grumpy 'Things could go very badly...'
            ELENA @grumpy 'If the wrong person talks to the inquisitors about us, things will not be pleasant.'
            MC @talk 'Relax Elena, I have things under control.'
            MC @talk 'She will be gone soon enough.'
            ELENA @sad "Good... People like us can't go relying on others."
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    $ LocEnter()