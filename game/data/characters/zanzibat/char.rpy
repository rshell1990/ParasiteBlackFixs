default ZANZIBAT = Character(_("Zanzibat"), image = "zanzibat")

init python:
    CharDefs["zanzibat"] = BuildCharTemplate(CharID = "zanzibat",
                                name = _("Zanzibat"),
                                portrait = "images/characters/zanzibat/portrait.webp",
                                RelTextIDs = {"summary_initial"},
                                ExtraData = {"clothes":"normal"}) # none actually, just normal
    config.tag_layer["zanzibat"] = "characters"

    RelText["zanzibat"] = {}
    RelText["zanzibat"]["summary_initial"] = {
        "order":0,
        "text":_("A powerful and aloof merchant lord in Hamun")}