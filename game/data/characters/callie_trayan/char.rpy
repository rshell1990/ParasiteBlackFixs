default CALLIE = Character(_("Callie"), image = "callie")
default TRAYAN = Character(_("Trayan"), image = "trayan")

init python:
    CharDefs["callie"] = BuildCharTemplate(CharID = "callie",
        name = _("Callie"),
        portrait = "images/characters/callie/portrait.webp", 
        RelTextIDs = {"initial"},
        ExtraData = {"clothes": "normal"})

    config.tag_layer["callie"] = "characters"
    config.tag_layer["cg_callie_cage"] = "characters"

    RelText["callie"] = {}
    # initially present
    RelText["callie"]["initial"] = {
        "order":0,
        "text":_("A katai daughter of a wealthy merchant I rescued.")}
    # unlocked after sex
    RelText["callie"]["had_sex"] = {
        "order":1,
        "text":_("The girl and I shared a passionate night at a inn on the way back... Perhaps should I ever visit the city of Hamun, I should ask for her?")}

    CharDefs["trayan"] = BuildCharTemplate(CharID = "trayan",
        name = _("Trayan"),
        portrait = "images/characters/trayan/portrait.webp", 
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})

    config.tag_layer["trayan"] = "characters"
    config.tag_layer["cg_trayan_cage"] = "characters"

    RelText["trayan"] = {}
    # initially present
    RelText["trayan"]["initial"] = {
        "order":0,
        "text":_("A katai son of a wealthy merchant I rescued.")}
    # unlocked after sex
    RelText["trayan"]["had_sex"] = {
        "order":1,
        "text":_("The boy and I shared a passionate night at a inn on the way back... Perhaps should I ever visit the city of Hamun, I should ask for him?")}