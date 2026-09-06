define PRINCESS_CECILIA = Character("Princess Cecilia", image = "cecilia")

init python:
    CharDefs["cecilia"] = BuildCharTemplate(CharID = "cecilia",
        name = _("Princess Cecilia"),
        portrait = "images/characters/cecilia/portrait.webp",
        RelTextIDs = {"summary_initial"},
        ExtraData = {"clothes":"normal"}) # normal / naked

    config.tag_layer["cecilia"] = "characters"

    # initially present
    RelText["cecilia"] = {}
    RelText["cecilia"]["summary_initial"] = {
        "order":0,
        "text":_("The royal princess of Alderay, King Mesamor's daughter... I am her loyal subject.")}