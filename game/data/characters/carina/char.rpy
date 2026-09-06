default CARINA = Character(_("Carina"), image = "carina")
init python:
    CharDefs["carina"] = BuildCharTemplate(CharID = "carina",
        name = _("Carina"),
        portrait = "images/characters/carina/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})

    config.tag_layer["carina"] = "characters"

    config.tag_layer["cg_carina_smoke_ling"] = "characters"
    config.tag_layer["cg_carina_smoke_normal"] = "characters"
    config.tag_layer["cg_carina_smoke_naked"] = "characters"
    
    RelText["carina"] = {}
    RelText["carina"]["initial"] = {
        "order":0,
        "text":_("The calculating owner of the Weeping Heart bordello. A dangerous, resourceful woman, she is a prominent figure in the city's underworld.")}
