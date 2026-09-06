init python:
    @AppendToAllQuests
    ### enabled after completing prologue
    class DialogueKylisa(LogicModule):
        def __init__(self):
            super().__init__()

            self.FirstBless = True
            self.CanBless = True

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_church":
                if IsDaytime():
                    btnMods["btn_kylisa_talk"] = BtnJumpLabel(_("Talk to Kylisa"), "kylisa_talk")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "novaras_church":
                if IsDaytime():
                    if self.progress == 0:
                        return TriggeredEvent("nov_kylisa_firstmeet")

        def onMidnight(self):
            if not self.CanBless:
                self.CanBless = True

        def extraDialogue(self):
            yield ("kylisa_root", DNode(_("I've gotta go."), "kylisa_bye", nextNode = "DNodeExit", order = -100))
            yield ("kylisa_root", DNode(_("Who are you really?"), "kylisa_whoareyou"))
            yield ("kylisa_root", DNode(_("I have come to seek a blessing from the gods."), "kylisa_blessing"))
            yield ("kylisa_root", DNode(_("What can you teach me about the gods?"), "kylisa_teachmeaboutgods"))

label kylisa_talk:
    show kylisa at center 
    with dissolve
    KYLISA @talk "You have returned... How may I help you?"
    $ CharMeet("kylisa")
    call processDialogue("kylisa_root") from _call_processDialogue_39

label kylisa_bye:
    KYLISA @talk 'May the blessings of the gods be with you.'
    $ LocEnter()

label kylisa_whoareyou:
    KYLISA @talk 'I am the royal Mage, but given the... {i}change in leadership,{/i}'
    KYLISA @talk "I now serve at the Emperor's pleasure."
    menu:
        'Do you prefer serving under the Emperor than the king?':
            KYLISA @angry 'You should be careful asking such questions...'
            KYLISA @angry 'One could take that question the wrong way.'
            MC @talk 'Forgive me, I did not mean any ill with it.'
            KYLISA @sad '...He was kinder.'
            KYLISA @sad 'Most talk of how Alcott saved us all and Mesamore would have doomed us all.'
            KYLISA @sad "But many forget how we prospered under Mesamore before."
            KYLISA @sad "He was a kind king, one determined to tackle poverty in ways his predecessors never did, and life was good under him."
            KYLISA @sad "He may not he been the strongest military mind, but what king could have ever been prepared for the threat of the Demorai in such short notice?"
            KYLISA @talk 'Alcott tried time and time again to push for more control over the lives of the realms citizens, and each time, Mesamore pushed back.'
            KYLISA @talk 'Despite the war he faced, Mesamore always wanted us to see a future beyond it, he never wanted the realm to become nothing but the violent war machine it is today.'
            KYLISA @sad "Now? We are all just expendable pieces for a meat grinder as we fight inch by inch for every piece of land."
            KYLISA @talk "There are no names remembered anymore when it comes to the war council, just numbers... Numbers thrown against other numbers."
            MC @talk 'But did we have any other choice?'
            KYLISA @talk 'In stopping the war? No... I feel that it was inevitable.'
            KYLISA @angry "In what we've {i}become{/i} trying to win this war? Absolutely."
        'I see... I have other questions.':
            KYLISA @talk 'Speak your mind.'
    return

label kylisa_blessing:
    if InfectionModule().CurrentValue > 10:
        call kylisa_cleansing from _call_kylisa_cleansing
    else:
        "Kylisa paused for a moment, then replied calmly:"
        KYLISA @talk "The gods seem to already stand by your side, [player_name!t]."
        return
    return

label kylisa_cleansing:
    if DialogueKylisa().FirstBless:
        $ DialogueKylisa().FirstBless = False
        KYLISA @talk "The old or the new?"
        MC @talk "Whoever will listen."
        KYLISA @talk "I may grant you their blessing..."
        "She raised her head a bit, and from beneath her hood I saw a pair of glaring eyes, scanning into the very depths of my soul."
        "A gentle, barely-noticeable pulse of energy waved through my entire body, followed by a harsh, painful jitter:"
        BLACK "{b}THAT'S CLOSE ENOUGH.{/b}"
        "Kylisa took half-a step back and murmured to herself:"
        KYLISA @talk "That energy... It is not Demorai, yet so strong..."
        "She recomposed herself and concluded:"
        KYLISA @talk "I don't know what exactly you came in contact with, [player_name!t], but I might be able to help."
        KYLISA @talk "I believe I can douse this... black flame that is devouring your soul."
        "I gulped at the 'devouring' part."
        KYLISA @talk "I can only do so much as to set back it's {i}progress{/i}."
        KYLISA @talk "Five hundred coin."
    else:
        if DialogueKylisa().CanBless:
            KYLISA @talk "I can help you douse the black flame, [player_name!t]."
            KYLISA @talk "You should seek a more... permanent solution though, for I can see the flame leaving it's scorching marks on your soul as we speak."
            KYLISA @talk "Five hundred coin."
        else:
            KYLISA @talk "I cannot do this again, [player_name!t]."
            KYLISA @talk "I need to regain my strength."
            KYLISA @talk "Come find me tomorrow, I will help you with your... condition."
            MC @talk "I see."
            return
    menu:
        "Pay her." (Req_Gold = 500):
            $ DialogueKylisa().CanBless = False
            $ PlayerRemItem("gold", 500)
            "Pain began to quickly consume my body just as Kylisa raised her staff and pointed it at me:"
            play sound "audio/cfx/detect_magic.ogg"
            $ InfChangeBy(0, SetTo = True)
            show vfx_magick_glow with flash:
                anchor (0.5,0.5)
                pos (0.58,0.153)
                zoom 0.6
            hide vfx_magick_glow with dissolve
            KYLISA @talk "It is done."
            "Feeling refreshed and... in control again, I exhaled."
            MC @talk "Thanks, Kylisa."
            KYLISA @talk "It is my pleasure, [player_name!t]."
            return
        "Another time perhaps.":
            KYLISA @talk "Very well."
            return

label kylisa_teachmeaboutgods:
    KYLISA @talk 'One would hope your education would have taught you this already.'
    MC @talk 'It has been some time since I last read the holy text... I could do with a refresher.'
    KYLISA @talk 'Very well, what do you wish to know about?'
    menu kylisa_teachmeaboutgods_menu:
        'Ask about the first war of the gods.':
            KYLISA @talk "In the beginning, Al'Vazah, the great creator, formed the old gods and gave them dominion across the stars."
            KYLISA @talk "As life flourished, the old gods grew accustomed to their worship, and saw themselves as higher beings who became obsessed with their own power games against each other."
            KYLISA @talk 'The old gods would often toy with those they viewed as lesser beings, and could only be roused to help with the offer of bargains and sacrifices.'
            KYLISA @talk "Al'Vazah, displeased with what had become of the old gods, formed the new gods and also gave them powerful dominions to rule across the stars."
            KYLISA @talk "The new gods in contrast, believed it was their duty to guide the mortal races to a higher state of being."
            KYLISA @talk "They openly chose to walk amongst us, and pull back the veil of secrecy that the old gods always maintained."
            KYLISA @talk "Threatened, the old gods battled the new gods for supremacy in a great war we now know as the first war of the gods."
            KYLISA @talk "The new gods emerged victorious, led Al'Vazah's champion and the most powerful of all the gods, Tzenvachican."
            KYLISA @talk 'The old gods agreed to an uneasy truce talk, their dominion greatly reduced as the new gods triumphed over them.'
            KYLISA @talk "And thus began the longest long golden age of history till Malakai's war."
            jump kylisa_teachmeaboutgods_menu
        'Ask about the second war of the gods.':
            KYLISA @talk 'Over at least ten thousand years had passed since the end of the first War of the gods.'
            KYLISA @talk "It is said, the uneasy peace between the old gods and the new had become more strenuous than ever, as the old gods had begun to rally around their own Champion, Shal'krin who they saw might restore them to former glory."
            KYLISA @talk "But it was not Shal'Krin who bought about the second war of the gods."
            KYLISA @talk "Malakai the curious and kind, was decieved by the goddess of chaos, Gimera, that the only way to prevent the coming war was to open the Necronimis, a ancient box formed and sealed away by Al'Vazah at the start of his great creation."
            KYLISA @talk 'Malakai opened the box hoping to learn the knowledge inside and use it for good, but instead, he absorbed all the darkness and evils of life itself.'
            KYLISA @talk "Reborn as Malakai the deciever, the dark shifter, the prince of blood and the lord of darkness."
            KYLISA @talk "Malakai overthrew Shal'Krin and declared himself god of gods, declaring war against Al'Vazah and Tzenvachian."
            KYLISA @talk "Both old and new gods become factioned within themselves, taking sides either with Tzenvachian's forces or with Malakai's."
            KYLISA @talk "Brother slew brother, and old enemies now found themselves fighting shoulder to shoulder."
            KYLISA @talk 'Some followed Malakai out of fear, while others, genuinely believed in the warped vision of the mad god that he alone could bring about the {i}perfect{/i} world.'
            KYLISA @talk "While little is fully understood of what happened next, we know that thousands of mortal races joined the great war, and world upon world was engulfed in flames."
            KYLISA @talk "The gods that had once flourished, were decimated, until finally, Malakai himself faced off with Tzenvachian."
            KYLISA @talk "There battle, as it was written, is beyond our comprehension, but the result seems to be that Malakai's physical form was destroyed at the cost of both Tzenvachian sacrificing himself by trapping their souls in some eternal battle."
            KYLISA @talk "Thus ending the second war of the gods."
            jump kylisa_teachmeaboutgods_menu
        'What happened {i}after{/i} the war of the gods?':
            KYLISA @talk "Hmm, not much is written on this part."
            KYLISA @talk "Only the passing words of troubled surviving gods who have, throughout the ages, passed through our world and alluded to what happened."
            KYLISA @talk "But it's... difficult to always decipher their meaning."
            MC @talk "What do you mean?"
            KYLISA @talk "Do keep in mind, much of this is heavily debated by scholars and such, I cannot speak from official doctrine when I discuss it."
            KYLISA @talk "From the various legends and smaller texts I have gathered, some of the scarred surviving gods explained that the old wars were fought with 'mechanical dragons that surfed the stars' and other such strange things."
            KYLISA @talk "These dragons they struggled to feed in the aftermath of the war, and as food and other resources dwindled, they fought amongst each other for what very little remained."
            KYLISA @talk "Apparently it was the darkest of times..."
            'Kylisa smiled.'
            KYLISA @smile "We don't know for sure about that part."
            KYLISA @smile "Mechanical dragons flying through the stars... What a strange idea."
            KYLISA @smile "I do wonder sometimes what the gods could have meant by that."
            jump kylisa_teachmeaboutgods_menu
        "That's all I want to know.":
            KYLISA @talk "As you wish."
            KYLISA @talk "Anything else?"
            return

label nov_kylisa_firstmeet:
    $ QstSetProgress(DialogueKylisa, 1)
    show kylisa:
        xalign 0.5
    with dissolve
    KYLISA @talk 'Ah, it is good to see you walking.'
    MC @talk 'Huh? Have we met before?'
    KYLISA @smile 'Have you forgotten so quickly when I helped tend to your wounds?'
    'I remembered her now, the mage who arrived with Alcott.'
    MC @surprised "You're the Emperor's Mage!"
    KYLISA @talk 'Kylisa.'
    KYLISA @talk 'Tell me, what brings you here?'
    KYLISA @talk 'Have you come to pray to the gods?'
    call processDialogue("kylisa_root") from _call_processDialogue_40