default NUMA = Character(_("Numa"), image = "numa")
init python:
    CharDefs["numa"] = BuildCharTemplate(
        CharID = "numa", 
        name = _("Numa"),
        ExtraData = {"clothes":"normal"},
        portrait = "images/characters/numa/portrait.webp",
        RelTextIDs = {"initial"},
        ) # normal, naked
    config.tag_layer["numa"] = "characters"


    RelText["numa"] = {}
    # unlocked at start
    RelText["numa"]["initial"] = {
        "order":0,
        "text":_("A Thalay librarian working in the free city of Hamun, she seems slightly bored and lonely...")}