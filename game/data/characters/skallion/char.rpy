default SKALLION = Character(_("Skallion"), image = "skallion")

init python:
    CharDefs["skallion"] = BuildCharTemplate(CharID = "skallion",
                                                    name = _("Skallion"), 
                                                    portrait = "images/characters/skallion/portrait.webp",
                                                    RelTextIDs = {"initial"})
    config.tag_layer["skallion"] = "characters"


    RelText["skallion"] = {}
    RelText["skallion"]["initial"] = {
        "order":0,
        "text":_("Markus' brother, a somewhat withered individual, his years working in the mines have done irreparable damage to his body.")
    }