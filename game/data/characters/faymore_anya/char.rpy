define ANYA = Character(_("Anya"), image = "anya")

init python:
    CharDefs["anya"] = BuildCharTemplate(CharID = "anya",
        name = _("Anya"),
        RelTextIDs = {"initial"},
        portrait = "images/characters/anya/portrait.webp",
        ExtraData = {"clothes":"normal"},
    )

    RelText["anya"] = {}

    # initial
    RelText["anya"]["initial"] = {
        "order":0,
        "text":_("The wife of Chanyi Faymore and mother of Serafina... A merchant lord who seems particularly easy going.")}

    @AppendToAllQuests
    class DialogueAnya(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_faymore_manor":
                if IsInTimeFrame(TIME_DAY_START, TIME_DAY_END):
                    btnMods["hamun_faymore_manor_talk_anya"] = BtnJumpLabel(_("Talk to Anya"), "dialogue_anya_entry")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("anya_root", DNode(_("That's all."), "anya_bye", nextNode = "DNodeExit", order = -100))

    config.tag_layer["anya"] = "characters"

label dialogue_anya_entry:
    show anya at center with dissolve
    ANYA @talk "[player_name!t]."
    call processDialogue("anya_root") from _call_processDialogue_81
    $ LocEnter()

label anya_bye:
    ANYA @talk "Speak to Chanyi if you want to arrange... umm..."
    ANYA @lewd "Some 'evening entertainment' for us."
    $ LocEnter()
