default VALA = Character(_("Vala"), image = "vala")

init python:
    CharDefs["vala"] = BuildCharTemplate(CharID = "vala",
        portrait = "images/characters/vala/portrait.webp",
        name = _("Vala"),
        RelTextIDs = {"initial"},
        ExtraData = {
            "clothes":"normal", # normal / naked
            "glasses":"on"})
    config.tag_layer["vala"] = "characters"
    config.tag_layer["cg_vala_books_1"] = "characters"
    config.tag_layer["cg_vala_books_2"] = "characters"

    RelText["vala"] = {}
    RelText["vala"]["initial"] = {
        "order":0,
        "text":_("A librarian who works within the capital's library. She seems clumsy, but she's cute and friendly enough.")}