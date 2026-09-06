define LORD_BELAMORE = Character(_("Lord Belamore"), image = "lord_belamore")
init python:
    CharDefs["lord_belamore"] = BuildCharTemplate(CharID = "lord_belamore",
        name = _("Lord Belamore"),
        #portrait = "images/characters/lord_belamore/portrait.webp",
        #RelTextIDs = {"initial"},
        #ExtraData = {"clothes":"normal"} # naked/ling/normal
    )
    
    config.tag_layer["lord_belamore"] = "characters"

