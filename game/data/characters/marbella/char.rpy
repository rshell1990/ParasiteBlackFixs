default MARBELLA = Character(_("Marbella"), image = "marbella")
default MARBELLA_ROBE = Character(_("Marbella"), image = "marbella_robe")

init python:
    CharDefs["marbella"] = BuildCharTemplate(
        CharID = "marbella",
        name = _("Marbella"),
        portrait = "images/characters/marbella/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"},
    )

    config.tag_layer["marbella"] = "characters"
    config.tag_layer["marbella_robe"] = "characters"

    config.tag_layer["cg_marbella_back_naked"] = "characters"
    config.tag_layer["cg_marbella_back_goggles"] = "characters"
    config.tag_layer["cg_marbella_mc_kiss"] = "characters"
    
    config.tag_layer["cg_marbella_back_ling"] = "characters"
    config.tag_layer["cg_marbella_back_maid"] = "characters"
    config.tag_layer["cg_marbella_back_wedding"] = "characters"
    config.tag_layer["cg_marbella_back_robe_naked"] = "characters"

    config.tag_layer["cg_marbella_beer_ling"] = "characters"
    config.tag_layer["cg_marbella_beer_naked"] = "characters"
    config.tag_layer["cg_marbella_beer_normal"] = "characters"
    

    RelText["marbella"] = {}
    RelText["marbella"]["initial"] = {
        "order":0,
        "text":_("The passionate owner of 'The Crooked Shaft Mining Co' She seems to have taken a liking to me... Or my coin for funding her business ventures.")}

image cg_marbella_back_robe_naked:
    "cg_marbella_robe_naked_back_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_beer_normal:
    "cg_marbella_beer_normal_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_beer_ling:
    "cg_marbella_beer_ling_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_beer_naked:
    "cg_marbella_beer_naked_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_back_wedding:
    "cg_marbella_back_wedding_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_back_maid:
    "cg_marbella_back_maid_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_back_ling:
    "cg_marbella_back_ling_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_back_naked:
    "cg_marbella_back_naked_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_back_goggles:
    "cg_marbella_back_goggles_base"
    offset CHAR_OFFSET.MARBELLA
image cg_marbella_mc_kiss:
    "cg_marbella_mc_kiss_base"
    yoffset 200
