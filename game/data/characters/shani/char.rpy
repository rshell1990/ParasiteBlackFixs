default SHANI = Character("???", image = "shani")
init python:
    CharDefs["shani"] = BuildCharTemplate(CharID = "shani",
                                                name = _("Shani"),
                                                portrait = "images/characters/shani/portrait.webp",
                                                RelTextIDs = {"initial"},
                                                ExtraData = {"clothes":"normal", # normal / naked
                                                            "pose":"normal"}) # normal / alt

    config.tag_layer["shani"] = "characters"
    config.tag_layer["cg_shani_bdsm"] = "characters"

    RelText["shani"] = {}
    RelText["shani"]["initial"] = {
        "order":0,
        "text":_("A prostitute who works outside of one of the many brothels of Novaras.")}

    RelText["shani"]["died_during_siege"] = {
        "order":2,
        "text":_("The Demorai took her life during the siege.")}

image cg_shani_bdsm:
    "cg_shani_bdsm_sprite"
    offset CHAR_OFFSET.SHANI