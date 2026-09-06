default REGINA = Character("[regina_ref_cap!t]", image = "regina")
init python:
    CharDefs["regina"] = BuildCharTemplate(CharID = "regina",
        name = _("Regina"),
        portrait = "images/characters/regina/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData ={"clothes":"normal", # towel, normal, robe, witch, naked
            "hood":False, # for robe, not seen with other outfits
            "hide":False})

    config.tag_layer["regina"] = "characters"

    config.tag_layer["cg_regina_raven"] = "characters"
    config.tag_layer["cg_regina_cooking_back"] = "characters"
    config.tag_layer["cg_regina_masked"] = "characters"
    config.tag_layer["cg_regina_robe_open"] = "characters"
    config.tag_layer["cg_regina_witch"] = "characters"

    RelText["regina"] = {}
    # unlocked at start
    RelText["regina"]["initial"] = {
        "order":0,
        "text":_("Regina, a close family friend who took me in whilst father was sent off to war. I trust her with my life, though I can't help but feel she's hiding something from me...")}

    # unlocked after that alley hump scene
    RelText["regina"]["post_alley"] = {
        "order":1,
        "text":_("Since that strange dream, the sexual tension between the two of us continues to grow... along with my uncertainty towards her.")}

image cg_regina_cooking_back:
    "cg_regina_cooking_back_base"
    yoffset 100