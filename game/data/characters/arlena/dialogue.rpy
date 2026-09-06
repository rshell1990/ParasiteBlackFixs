init python:
    @AppendToAllQuests
    class DialogueArlena(LogicModule):
        def __init__(self):
            super().__init__()

            self.canEnterRoom = False
            self.dayUnlocked = 0

        def locationMod(self):
            btnMods = {}
            if IsDaytime():
                if self.canEnterRoom == True:
                    btnMods["visitArlena"] =    BtnChangeLoc(_("Visit Arlena"), "arlena_room")
                    btnMods["talkArlena"] =     BtnJumpLabel(_("Talk to Arlena"), "arlena_talk")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if GetLocID() == "arlena_room":
                if self.progress == 0:
                    return TriggeredEvent("arlena_room_first_entry")

        def extraDialogue(self):
            yield ("arlena_root", DNode(_("I should go."), "arlena_bye", nextNode = "DNodeExit", order = -100))
            if QstIsComplete(QstADazzlingTail):
                if PlayerItemQty("gems") >= 20:
                    yield ("arlena_root", DNode(_("I brought some more gems!"), "arlena_gems_for_gold"))
                else:
                    yield ("arlena_root", DNode(_("I brought some more gems!"), "arlena_gems_for_gold_not_enough"))

label arlena_room_first_entry:
    "Arlena's boxed room was compact but filled with drawings of schematics littered all about the place."
    'Here and there were the essentials, a single soft straw bed, a draw for some clothes and a workbench for her to sit at.'
    show arlena angry with flash:
        xcenter 0.35
        zoom 1.1
    MC "{b}OUCH!{/b}"
    ARLENA @angry "[player_name!t]?! Fucking idiot, what's wrong with you sneaking around like that?!"
    MC "Sorry! The door was unlocked..."
    MC "Did you just hit me with a-"
    ARLENA @angry "YES! A stool!"
    "Surprisingly, Arlena seemed to cool down right before my eyes."
    "Perhaps I really {i}did{/i} sneak up on her."
    ARLENA "Anyway, welcome to my High Castle."
    ARLENA 'I sketch out some of the more unique designs for armour and weapons here.'
    ARLENA 'There is something else I’ve been working on too...'
    ARLENA "Now if you don't mind, I'd rather get back to work."
    hide arlena with easeoutright
    ARLENA '...idiot.'
    $ QstSetProgress(DialogueArlena, 1)
    $ LocEnterQ()

# general talk label
label arlena_talk:
    show arlena at center
    with dissolve
    ARLENA 'Yes? What is it?'
    call processDialogue("arlena_root") from _call_processDialogue_10
    $ LocEnter()

label arlena_bye:
    ARLENA "Alright, see ya 'round."
    return

# gems for gold, called from arlena char dialogue
label arlena_gems_for_gold:
    ARLENA @smile "Oh did you now?"
    MC "Yeah!"
    MC 'Here you go...'
    $ PlayerRemItem("gems", 20)
    if CharGetRel("arlena") < 6:
        $ CharAddRel("arlena", 1)
    "I handed over a hefty pouch of gems, as Arlena's eyes began to glow with passion."
    ARLENA 'This is... Great!'
    ARLENA "Here's your cut."
    $ PlayerAddItem("gold", QstADazzlingTail().gemPay * 10)
    ARLENA "Pleasure doing business with ya!"
    return

label arlena_gems_for_gold_not_enough:
    MC "(She needs at least 20.)"
    return
