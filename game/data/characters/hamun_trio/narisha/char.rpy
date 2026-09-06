define LADY_NARISHA = Character(_("Lady Narisha"), image = "lady_narisha")

init python:
    CharDefs["lady_narisha"] = BuildCharTemplate(CharID = "lady_narisha",
        name = _("Lady Narisha"),
        portrait = "images/characters/lady_narisha/portrait.webp",
        #RelTextIDs = {"summary_initial", "append"},
        ExtraData = {"clothes":"normal", # naked, normal
        }
    )

    config.tag_layer["lady_narisha"] = "characters"