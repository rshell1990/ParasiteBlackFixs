define LADY_TARBECK =   Character(_("Lady Tarbeck"), image = "lady_tarbeck")

init python:
    CharDefs["lady_tarbeck"] = BuildCharTemplate(CharID = "lady_tarbeck",
        name = _("Lady Tarbeck"),
        portrait = "images/characters/lady_tarbeck/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {
            "clothes":"normal", # normal naked ling
            "variant":"normal", # darkmage, bimbo
            "darkmage_mask":False,
        },
    )

    config.tag_layer["lady_tarbeck"] = "characters"
    config.tag_layer["cg_lady_tarbeck_darkmage_kiss_normal"] = "characters"

    RelText["lady_tarbeck"] = {}
    RelText["lady_tarbeck"]["initial"] = {
        "order":0,
        "text":_("The wife of Lord Tarbeck, quiet and reserved, she seems deeply saddened by what has become of her marriage...")
    }
image cg_lady_tarbeck_darkmage_kiss_normal:
    "cg_lady_tarbeck_darkmage_kiss_normal_base"
    offset (0, 100)
image cg_lady_tarbeck_bimbo_kiss_normal:
    "cg_lady_tarbeck_bimbo_kiss_normal_base"
    offset (0, 100)