define LADY_BELAMORE = Character(_("Lady Belamore"), image = "lady_belamore")

init python:
    CharDefs["lady_belamore"] = BuildCharTemplate(CharID = "lady_belamore",
        name = _("Lady Belamore"),
        portrait = "images/characters/lady_belamore/portrait.webp",
        #RelTextIDs = {"summary_initial", "append"},
        ExtraData = {"clothes":"normal", # naked, normal
        }
    )

    config.tag_layer["lady_belamore"] = "characters"