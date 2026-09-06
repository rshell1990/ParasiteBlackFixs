default CELESTE = Character(_("Celeste"), image = "celeste")
init python:
    CharDefs["celeste"] = BuildCharTemplate(CharID = "celeste",
        name = _("Celeste"),
        portrait = "images/characters/celeste/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})
    
    config.tag_layer["celeste"] = "characters"
    config.tag_layer["cg_celeste_return_party"] = "characters"
    config.tag_layer["cg_celeste_return_kid"] = "characters"

    RelText["celeste"] = {}
    RelText["celeste"]["initial"] = {
        "order":0,
        "text":_("A living legend. Not since the death of Newheart has a hero with such potential and hope swept across Novaras. Her powerful abilities are only matched by her beauty.")}