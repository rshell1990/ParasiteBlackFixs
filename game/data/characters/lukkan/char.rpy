default LUKKAN = Character(_("Lukkan"), image = "lukkan")
init python:
    CharDefs["lukkan"] = BuildCharTemplate(CharID = "lukkan",
                                                    name = _("Lukkan"), 
                                                    portrait = "images/characters/lukkan/portrait.webp",
                                                    RelTextIDs = {"initial"})
    config.tag_layer["lukkan"] = "characters"
    config.tag_layer["lukkan_base"] = "characters"

    RelText["lukkan"] = {}
    RelText["lukkan"]["initial"] = {
        "order":0,
        "text":_("A high-ranking officer who seems to handle various bureaucratic jobs. He sided with Alcott during the rebellion.")}