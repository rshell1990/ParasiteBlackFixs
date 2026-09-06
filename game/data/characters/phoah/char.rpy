default PHOAH = Character(_("Goddess Phoah"), image = "phoah")
init python:
    CharDefs["phoah"] = BuildCharTemplate(CharID = "phoah", 
                                            name = _("Goddess Phoah"),
                                            portrait = "images/characters/phoah/portrait.webp",
                                            ExtraData = {"clothes":"normal",
                                                "wings":False,
                                                "location":tra(STR_LOC.NOV_CITY)})
    config.tag_layer["phoah"] = "characters"