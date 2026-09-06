default ZARA = Character(_("Zara"), image = "zara")

init python:
    CharDefs["zara"] = BuildCharTemplate(CharID = "zara",
                                name = _("Zara"),
                                portrait = "images/characters/zara/portrait.webp",
                                RelTextIDs = {"summary_initial"},
                                ExtraData = {"clothes":"normal"}) # normal / naked / ling / dress
    config.tag_layer["zara"] = "characters"

    RelText["zara"] = {}
    RelText["zara"]["summary_initial"] = {
        "order":0,
        "text":_("A mage of Palam in training... I am expected to help discover what made her launch into a rampage.")}