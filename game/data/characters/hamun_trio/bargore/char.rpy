define LADY_BARGORE = Character(_("Lady Bargore"), image = "lady_bargore")

init python:
    CharDefs["lady_bargore"] = BuildCharTemplate(CharID = "lady_bargore",
        name = _("Lady Bargore"),
        portrait = "images/characters/lady_bargore/portrait.webp",
        #RelTextIDs = {"summary_initial", "append"},
        ExtraData = {"clothes":"normal", # naked, normal
        }
    )

    config.tag_layer["lady_bargore"] = "characters"