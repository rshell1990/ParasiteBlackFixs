default THEA = Character(_("Thea"), image = "thea")

init python:
    CharDefs["thea"] = BuildCharTemplate(CharID = "thea",
        name = _("Thea"),
        portrait = "images/characters/thea/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})
    config.tag_layer["thea"] = "characters"

    RelText["thea"] = {}
    # initially visible
    RelText["thea"]["initial"] = {
        "order":0,
        "text":_("A girl who helps manage the Adventurer's guild in Novaras... She's quite beautiful!")}

    # add after had sex
    RelText["thea"]["after_sex"] = {
        "order":1,
        "text":_("It seems she has a fetish for 'adventurers,' especially successful ones. It's a good thing I'm planning on continuing to rise the ranks of the guild, isn't it?")}