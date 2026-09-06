default LUCIUSMAL = Character(_("Lucius Mal"), image = "luciusmal")

init python:
    CharDefs["luciusmal"] = BuildCharTemplate(CharID = "luciusmal",
                                                        name = _("Lucius Mal"), 
                                                        portrait = "images/characters/luciusmal/portrait.webp", 
                                                        RelTextIDs = {"initial"},
                                                        ExtraData = {"pose":"base_1"})
    config.tag_layer["luciusmal"] = "characters"

    RelText["luciusmal"] = {}
    RelText["luciusmal"]["initial"] = {
        "order":0,
        "text":_("A lucrative businessman who runs a shop in Novaras, he seems to have his fingers in many pies...")}