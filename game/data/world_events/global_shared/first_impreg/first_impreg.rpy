init python:
    # this gets 'started' and 'started again' MANUALLY by each "you got me pregnant" scene
    # works only becaue qststart is soft
    @AppendToAllQuests
    class EventFirstImpreg(LogicModule):
        def __init__(self):
            super().__init__()

        def onEnter(self):  
            if not IsPlayerTraveling(): # not sure if necessary really
                return TriggeredEvent("ev_first_impreg")

label ev_first_impreg:
    $ QstComplete(EventFirstImpreg)
    show mc with easeinleft:
        xcenter 0.15
    MC '(Fuck! FUCK!)'
    MC '(What do I do now?)'
    BLACK '{i}(Relax){/i}'
    MC '(My child... Will it have the same affliction as I do?)'
    MC "(Will it have it's own {i}dark passenger?{/i})"
    BLACK '{i}(No).{/i}'
    BLACK '{i}(Our sired seed will have enhanced strength, speed, and other enhanced traits due to the genetic mutations).{/i}'
    BLACK '{i}(But they will not be parasites).{/i}'
    MC "(I don't understand, why not?)"
    BLACK '{i}(The genetic change is too drastic, trying to convert a species into one of us without any prior genetic code mutation can result in massive organ failure).{/i}'
    BLACK '{i}(Therefore, our species prefers to breed during the first wave, then, the sired offspring will be mated with to produce Parasites).{/i}'
    BLACK '{i}(It is far safer to produce our kind with the sired offsprings genetic code as a foundation).{/i}'
    MC '(So... They will be okay?)'
    BLACK '{i}(Yes){/i}'
    BLACK '{i}(Our species are designed to breed, I expect you will be driven to sire more young){/i}.'
    MC "(I'm not so sure about that, but... At least I know the children won't be cursed as I am.)"
    BLACK '{i}(Curses... Blessings... These concepts hold little meaning to me, we are as our nature intended, nothing more).{/i}'
    MC '(Yeah... I thought you might say something like that.)'
    $ LocEnter()