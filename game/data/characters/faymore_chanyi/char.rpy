define CHANYI = Character(_("Chanyi"), image = "chanyi")

init python:
    CharDefs["chanyi"] = BuildCharTemplate(CharID = "chanyi",
        name = _("Chanyi"),
        RelTextIDs = {"initial"},
        portrait = "images/characters/chanyi/portrait.webp",
        ExtraData = {"clothes":"normal"},
    )

    RelText["chanyi"] = {}

    # initial
    RelText["chanyi"]["initial"] = {
        "order":0,
        "text":_("Chanyi Faymore, wife to Anya Faymore and stepmother to Serafina Faymore. She is a no-nonsense katai and a powerful merchant lord in her own right.")} 

    @AppendToAllQuests
    class DialogueChanyi(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_faymore_manor":
                if IsInTimeFrame(TIME_DAY_START, TIME_DAY_END):
                    btnMods["hamun_faymore_manor_talk_chanyi"] = BtnJumpLabel(_("Talk to Chanyi"), "dialogue_chanyi_entry")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("chanyi_root", DNode(_("That will be all."), "chanyi_bye", nextNode = "DNodeExit", order = -100))

    config.tag_layer["chanyi"] = "characters"

label dialogue_chanyi_entry:
    show chanyi at center with dissolve
    CHANYI @talk "Yes, can I help you?"
    call processDialogue("chanyi_root") from _call_processDialogue_82
    $ LocEnter()

label chanyi_bye:
    CHANYI @talk "Very well."
    $ LocEnter()

#chanyi
label dialogue_temp:
    menu:
        "How is Serafina progressing?":
            CHANYI @talk "Her training goes well."
            CHANYI @talk "The nightmares have ceased, and she's more confident than ever."
            "There was a pause."
            CHANYI @serious "That dark mage, though."
            CHANYI @serious "He seems amicable and civil."
            CHANYI @serious "{i}But I just can't trust him.{/i}"

# anya
label dialogue_temp_2:
    ANYA @happy "Oh, hello!"
    menu:
        "Have you heard from Davik at all?":
            ANYA @sad "No... And I don't suspect we will."
            ANYA @sad "I can't say I'm not furious at him for what he's done..."
            ANYA @sad "But I also understand {i}why{/i}, at least."
            ANYA @talk "I just hope he manages to find his own happiness."
    
        "Is Serafina well?":
            ANYA @happy "Serafina is doing {i}very{/i} well."
            ANYA @happy "She sleeps soundly now."
            ANYA @talk "And I don't think I've seen her this happy in a long time."
            "There was a long pause."
            ANYA @sad "I think... she is worried about her father, though."
            ANYA @sad "Even if she doesn't say it."