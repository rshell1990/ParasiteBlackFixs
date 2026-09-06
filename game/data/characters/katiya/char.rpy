default KATIYA = Character(_("Katiya"), image = "katiya")

init python:
    CharDefs["katiya"] = BuildCharTemplate(CharID = "katiya",
                                            name = _("Katiya"), 
                                            portrait = "images/characters/katiya/portrait.webp", 
                                            RelTextIDs = {"initial"})
    config.tag_layer["katiya"] = "characters"
    config.tag_layer["cg_katiya_flash"] = "characters"

    RelText["katiya"] = {}
    RelText["katiya"]["initial"] = {
        "order":0,
        "text":_("A shrewd store owner in Hamun... She seems open to offers for more than just her wares.")}