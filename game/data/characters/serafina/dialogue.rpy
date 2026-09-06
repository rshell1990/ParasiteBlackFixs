# this ALSO handles virgo char (down below)
init python:
    @AppendToAllQuests
    class DialogueSerafina(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_faymore_manor_serafina_room":
                if IsDaytime():
                    btnMods["hamun_faymore_manor_talk_serafina"] = BtnJumpLabel(tra(_("Talk to Serafina")), "talk_serafina")
                    btnMods["hamun_faymore_manor_talk_virgo"] = BtnJumpLabel(tra(_("Talk to Virgo")), "talk_virgo")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("serafina_root",   DNode(_("How goes your training, Serafina?"), "talk_serafina_training"))
            yield ("serafina_root",   DNode(_("Have you heard anything from your father?"), "talk_serafina_father"))
            yield ("serafina_root",   DNode(_("Your mothers and I... How do you feel about that?"), "talk_serafina_wives"))
            yield ("serafina_root",   DNode(_("Nothing for now."), "talk_serafina_bye", nextNode = "DNodeExit", order = -100))

label talk_serafina:
    # SPEAKING TO SERAFINA
    show serafina at center with dissolve
    SERAFINA @smile "Oh, have you come to see me, or...?"
    call processDialogue("serafina_root") from _call_processDialogue_84
    $ LocEnter()

label talk_serafina_training:
    SERAFINA @talk "As well as it can, I suppose."
    SERAFINA @talk "Virgo is a strict instructor, but I know he means well."
    MC @think "And the magecraft he teaches you... is it—"
    SERAFINA @smile "{i}Powerful.{/i}"
    SERAFINA @talk "But it's also kind of terrifying."
    SERAFINA @talk "I have taken some private lessons before on magecraft."
    SERAFINA @surprised "But this is like a whole different world."
    MC @serious "Be careful, Serafina. Many a mage has said the same thing,"
    MC @serious "only to come undone by the madness of digging too deep."
    SERAFINA @smile "Don't worry, I'll be safe!"
    return

label talk_serafina_father:
    SERAFINA @sad "No..."
    SERAFINA @sad "But now I know where he might receive my letters, so I'm still going to try."
    SERAFINA @sad "I just hope he understands why I made the choice I did."
    return

label talk_serafina_wives:
    SERAFINA @sad "{i}*Sigh*{/i} I learned a long time ago about their... {i}tastes.{/i}"
    SERAFINA @talk "They aren't exactly subtle about it."
    SERAFINA @talk "But they do care for me a great deal."
    SERAFINA @talk "Just don't make things difficult for them, alright?"
    SERAFINA @talk "Chanyi may act strong, but she's more sensitive than she lets on."
    SERAFINA @think "And mother is just... well... mother."
    return

label talk_serafina_bye:
    SERAFINA @smile "Alright then."
    $ LocEnter()


############################################################################################################
default VIRGO = Character(_("Virgo"), image = "cg_virgo")
label talk_virgo:
    show cg_virgo at center with dissolve
    VIRGO "Greetings."
    menu talk_virgo_menu:
        "How goes Serafina's training?":
            VIRGO "The girl is a prodigy."
            VIRGO "Even if she doesn't understand it yet."
            VIRGO "She will make an excellent mage one day."
            MC @think "What kind of mage?"
            VIRGO "One where her talents are not wasted..."
            jump talk_virgo_menu
        "That's all.":
            VIRGO "Until we meet again then."
    $ LocEnter()