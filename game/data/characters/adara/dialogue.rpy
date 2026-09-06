init python:
    @AppendToAllQuests
    class DialogueAdara(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "adara_house_bedroom":
                if IsDaytime():
                    btnMods["btn_talk_adara"] = BtnJumpLabel(_("Talk to Adara"), "adara_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("adara_root", DNode(_("I have to go."), "adara_bye", nextNode = "DNodeExit", order = -100))
            yield ("adara_root", DNode(_("How are you?"), "adara_talk_howareyou"))

label adara_talk:
    show adara at center_f with dissolve
    ADARA @talk "[player_name!t]?"
    call processDialogue("adara_root") from _call_processDialogue_47
    $ LocEnter()

label adara_bye:
    ADARA @shock "Ah, so soon?"
    ADARA @sad "Well ... alright then, I'll see you soon I guess."
    $ LocEnter()

label adara_talk_howareyou:
    $ TmpFlush()
    $ TmpSet("random_topics", ["gen_1", "gen_2", "gen_3"])
    if BlackDiamondLogic().tarekFate != "walked":
        $ TmpGet("random_topics").append("diamond_massacre")
    if RomanceNijah().investBusiness:
        $ TmpGet("random_topics").append("nijah_stall")
    if QstIsComplete(QstGuildBehemoth):
        $ TmpGet("random_topics").append("white_rat")
    $ TmpSet("rng", renpy.random.choice(TmpGet("random_topics")))
    if TmpGet("rng") == "gen_1":
        ADARA @sad "Father has been a little more unwell than usual today, so I've been quite busy tending to his health." #Variant 1 
    if TmpGet("rng") == "gen_2":
        ADARA @talk "Hm? Same as always I suppose..." #variant 2 
    if TmpGet("rng") == "gen_3":
        ADARA @smile "I am well, [player_name!t], thank you for asking." #variant 3 
    if TmpGet("rng") == "diamond_massacre":
        ADARA @talk "Did you hear about the commotion in the pleasure district? Some kind of ... {i}monster{/i} attacked one of the gangs, at least, that's the rumour." #variant 4 - if player killed the gang members in the black diamond
    if TmpGet("rng") == "nijah_stall":
        ADARA @smile "I am well thank you! Have you seen that new market stall selling Ramonian food? It's very popular!" #Varaint 5 - If player has Nijah's stall set up
    if TmpGet("rng") == "white_rat":
        ADARA @smile "You're making quite a name for yourself, aren't you? Congratulations on moving up ranks in the adventurers guild!" #Variant 6 - If player has slain the white rat
    $ TmpFlush()
    return
