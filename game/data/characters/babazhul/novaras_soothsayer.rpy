init python:
    # a list of label names you can find at the end of this file listing random "tell a fortune" dialogue bits.
    # to add more, add a label, its text & an entry into this list.
    NovarasSoothsayerFortuneList = [
        "nov_soothsayer_future0",
        "nov_soothsayer_future1",
        "nov_soothsayer_future2",
        "nov_soothsayer_future3",
        "nov_soothsayer_future4",
        "nov_soothsayer_future5",
        "nov_soothsayer_future6"]

    @AppendToAllQuests
    class NovarasSoothsayer(LogicModule):
        def __init__(self):
            super().__init__()

            self.seen_fortune = []

        def getUnseenFortunes(self):
            return [x for x in NovarasSoothsayerFortuneList if x not in self.seen_fortune]

        def locationMod(self):
            btnMods = {}
            if self.progress == 1:
                if (GetLocID() == "novaras_soothsayer_cabin" or 
                    GetLocID() == "hamun_witch_house"):
                    # TRIPPY RIGHT? WE MOD 2 DIFF PLACES
                    btnMods["btn_novaras_talk_to_babazhul"] =   BtnJumpLabel(_("Talk to Babazhul"), "nov_soothsayer_talk")
                    btnMods["btn_hamun_talk_to_babazhul"] =     BtnJumpLabel(_("Talk to Babazhul"), "nov_soothsayer_talk")
            return LocButtonMod(directMods = btnMods)

        def onEnter(self):  
            if (GetLocID() == "novaras_soothsayer_cabin" or 
                    GetLocID() == "hamun_witch_house"):
                if self.progress == 0:
                    return TriggeredEvent("nov_soothsayer_firstmeet")

        def extraDialogue(self):
            yield ("babazhul_root", DNode(_("Speak to me of the future, soothsayer."), "nov_soothsayer_future"))
            yield ("babazhul_root", DNode(_("I long to walk through my past once again."), "nov_soothsayer_gallery"))
            yield ("babazhul_root", DNode(_("I will return in time."), "nov_soothsayer_goodbye", nextNode = "DNodeExit", order = -100))

### firstmeet
label nov_soothsayer_firstmeet:
    show babazhul:
        pos (0.0,0.0)
    with dissolve
    "Entering into the darkened room of the soothsayer I looked around."
    "The room was dimly lit only by pale candle light, with strange trinkets from faraway lands adorning every corner of the room, strange skulls and books in ancient tongues long since dead."
    "Here and there was a stuffed bird or some scroll with strange markings on it littered around on the floor amongst the pile of many books."
    "The old hag was sat down at her seat, hunched over her desk looming over a crystal ball as she looked towards me expectantly."
    if QstIsActive(QstTerminus):
        BABAZHUL "Greetings, child of tooth and claw."
        BABAZHUL "How may Babazhul help you?"
        MC "Hm? Child of what?"
        MC "What are you talking about?"
        hide babazhul with Dissolve(0.25)
        $ PlaySound("audio/cfx/detect_magic.ogg")
        $ CharSetVar("babazhul", "lit", "yes")
        show babazhul with dissolve
        BABAZHUL "{i}The old gods stir with the new, the great games' next chapter shall soon begin.{/i}"
        BABAZHUL "{i}A great warrior shall join you, the great tooth and claw, a forgotten lord from a time lost beyond the stars.{/i}"
        BABAZHUL "{i}To battle the dreaming king, whose restless fury shall scorch these lands.{/i}"
        MC "What the~"
        MC "Gods? A Dreaming king? Great warriors?"
        hide babazhul with dissolve
        $ CharSetVar("babazhul", "lit", "no")
        "The soothsayer went silent for a moment, before continuing in her raspy voice:"
        BABAZHUL "In time ... All will be clear, [player_name!t]."
        MC "...How did you know my-"
        BABAZHUL "Hahahaha!"
    else:
        $ BABAZHUL = Character("???", image = "babazhul")
        BABAZHUL @talk "{i}I knew you would come,{/i} [player_name!t]."
        MC "How did you know my name?"
        BABAZHUL @talk "Babazhul knows many names, many things that have passed and are yet to pass."
        $ BABAZHUL = Character (_("Babazhul"), image = "babazhul")
    $ CharMeet("babazhul")
    BABAZHUL @talk "Now tell me child of tooth and claw, do you seek your past... {i}or your future?{/i}"
    BABAZHUL @talk "For but five gold, it can be yours..."
    $ QstSetProgress(NovarasSoothsayer, 1)
    call processDialogue("babazhul_root") from _call_processDialogue_11
    hide babazhul with dissolve

### re-entry
label nov_soothsayer_talk:
    show babazhul:
        pos (0.0,0.0)
    with dissolve
    BABAZHUL @talk "Welcome back, child of tooth and claw."
    BABAZHUL @talk "Make your choice."
    call processDialogue("babazhul_root") from _call_processDialogue_12
    $ LocEnter()

# future lines
label nov_soothsayer_future:
    if PlayerItemQty("gold") >= 5:
        # for some reason, just going "if list" (or a bool check) doesnt work
        if len(NovarasSoothsayer().getUnseenFortunes()) > 0:
            show babazhul with dissolve
            BABAZHUL @talk "So be it."
            $ PlayerRemItem("gold", 5)
            hide babazhul with dissolve
            "Babazhul hands lightly touched over her crystal ball, which brightly began to glow and illuminate as she stared deeply into it with her half blind eyes."
            play sound "audio/cfx/detect_magic.ogg"
            #show cg_nov_witch_glow with dissolve

            $ tmpvar = {}
            $ tmpvar["fortune_label"] = renpy.random.choice(NovarasSoothsayer().getUnseenFortunes())
            $ NovarasSoothsayer().seen_fortune.append(tmpvar["fortune_label"])
            $ CharSetVar("babazhul", "lit", "yes")
            $ renpy.call(tmpvar["fortune_label"])
            call processDialogue("babazhul_root") from _call_processDialogue_13
        else:
            show babazhul with dissolve
            BABAZHUL @talk "In time, perhaps, there might be clarity..."
            BABAZHUL @talk "For now, I can see no more."
            call processDialogue("babazhul_root") from _call_processDialogue_14
    else:
        show babazhul with dissolve
        BABAZHUL @talk "You do not possess enough coin, child, return when you do."
        $ LocEnter()

# goodbye
label nov_soothsayer_goodbye:
    show babazhul with dissolve
    BABAZHUL @talk "{i}*Laughs*{/i} Of course you will return... I've already foreseen it."
    $ CharSetVar("babazhul", "lit", "no")
    $ LocEnter()

###############################
# tell-a-future lines list
label nov_soothsayer_future0:
    show babazhul with dissolve
    BABAZHUL @talk "I see a great shadow following you, a warrior of a thousand worlds."
    BABAZHUL @talk "Sitting on a throne of bones, so alone and so cold."
    BABAZHUL @talk "He would sit forever... Enjoy the silence, if not for his master's call."
    #hide cg_nov_witch_glow with dissolve
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_15

label nov_soothsayer_future1:
    show babazhul with dissolve
    BABAZHUL @talk "Hahaha! I see her fire, Princess raised by shadows and knives, born into a lie."
    BABAZHUL @talk "The great stars lay before her, and perhaps you at her side."
    BABAZHUL @talk "Oh child of tooth and claw, we shall see if love can truly conquer all!"
    #hide cg_nov_witch_glow with dissolve
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_16

label nov_soothsayer_future2:
    show babazhul with dissolve
    BABAZHUL @talk "The imitation stalks these lands, a beautiful souless beast."
    BABAZHUL @talk "Nothing but death awaits, yet how sweet will she be when she poisons your soul with honey."
    BABAZHUL @talk "See past the lies and beware, beware child of tooth and claw:"
    BABAZHUL @talk "The beautiful souless beast may be your demise."
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_17

label nov_soothsayer_future3:
    show babazhul with dissolve
    BABAZHUL @talk "My my, child! Such sweet fruits await! One in green, one in blue, one with scales, one so small, you could carry four! Hahaha!"
    BABAZHUL @talk "Their love will guide you through the darkness to come, cling to it, embrace it, hold them dear and close."
    BABAZHUL @talk "For when the time comes, you must face the darkness alone..."
    #hide cg_nov_witch_glow with dissolve
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_18

label nov_soothsayer_future4:
    show babazhul with dissolve
    BABAZHUL @talk "He sits at the helm of ultimate destruction, more ghost than man but he will return home."
    BABAZHUL @talk "Oh child of tooth and claw, to forever be reaching for the past is a terrible thing."
    BABAZHUL @talk "It may make monsters of us all..."
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_19

label nov_soothsayer_future5:
    show babazhul with dissolve
    BABAZHUL @talk "I see two brothers, stood on opposite cliffs."
    BABAZHUL @talk "A terrible storm rages, the black waves thrashing beneath their feet."
    BABAZHUL @talk "Both weep... But the fire inside makes them scream."
    BABAZHUL @talk "How the ones we love cut so deep."
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_20

label nov_soothsayer_future6:
    show babazhul with dissolve
    BABAZHUL @talk "Grief... I feel his grief."
    BABAZHUL @talk "It has made a monster of him, and it drives him to do terrible things."
    BABAZHUL @talk "But his fate is not yet sealed."
    BABAZHUL @talk "What will become of him?"
    hide babazhul with dissolve
    $ CharSetVar("babazhul", "lit", "no")
    call processDialogue("babazhul_root") from _call_processDialogue_21
