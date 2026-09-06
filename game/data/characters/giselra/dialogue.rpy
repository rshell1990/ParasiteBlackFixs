init python:
    @AppendToAllQuests
    class DialogueGiselra(LogicModule):
        def __init__(self):
            super().__init__()

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_giselra_store":
                if IsDaytime():
                    if self.progress == 0:
                        btnMods["btn_talk_giselra_store"] = BtnJumpLabel(_("Talk to Giselra"), "giselra_talk_firstmeet")
                    else:
                        btnMods["btn_talk_giselra_store"] = BtnJumpLabel(_("Talk to Giselra"), "giselra_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("giselra_root", DNode(_("I should go."), "giselra_bye", nextNode = "DNodeExit", order = -100))

label giselra_talk_firstmeet:
    $ QstSetProgress(DialogueGiselra, 1)
    "The tailor's voice called from the back of the store."
    GISELRA "One moment please!"
    "I turned slowly, looking at the many intricately crafted dresses on display."
    "Whoever this tailor was, she was indeed of exceptional skill."
    "I heard soft footsteps, turning my head as an older, black woman stepped forward,"
    "With an infectiously warm smile, she greeted me."
    show giselra at center with dissolve
    GISELRA @smile "Welcome to Giselra's handsome."
    GISELRA @smile "The finest tailor in ALL of Hamun."
    MC @smile "The finest you say?"
    GISELRA @talk "Of course, whatever clothes you desire, I can see them crafted."
    GISELRA @smile "{i}For a price, of course...{/i}"
    GISELRA @talk "Let me know if my services are of used."
    MC @talk "Will do."
    $ CharMeet("giselra")
    MC "(Always handy to know a good tailor.)"
    call processDialogue("giselra_root") from _call_processDialogue_79
    $ LocEnter()

label giselra_talk:
    show giselra at center with dissolve
    $ CharMeet("giselra")
    GISELRA @shock "Welcome to Giselra’s!"
    GISELRA @smile "Looking for something tailored, perhaps?"
    call processDialogue("giselra_root") from _call_processDialogue_74
    $ LocEnter()

label giselra_bye:
    GISELRA @smile "Bye, lovely."
    $ LocEnter()