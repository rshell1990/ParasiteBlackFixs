default LUNA = Character(_("Luna"))

init python:
    CharDefs["luna"] = BuildCharTemplate(
        CharID = "luna",
        name = _("Luna"),
        portrait = "images/characters/luna/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"}) # naked, normal, ling

    config.tag_layer["luna"] = "characters"

    RelText["luna"] = {}
    RelText["luna"]["initial"] = {
        "order":0,
        "text":_("A thirty-something katai woman, the proud owner of the Princess' Dream bathhouse in Hamun... she seems a little lonely?")}
