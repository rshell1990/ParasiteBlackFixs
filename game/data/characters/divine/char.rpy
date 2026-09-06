default DIVINE = Character(_("Sister Divine"), image = "divine")
init python:
    CharDefs["divine"] = BuildCharTemplate(CharID = "divine",
        name = _("Sister Divine"),
        portrait = "images/characters/divine/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})

    config.tag_layer["divine"] = "characters"
    config.tag_layer["cg_mc_divine_kiss"] = "characters"
    config.tag_layer["cg_mc_divine_kiss_naked"] = "characters"

    RelText["divine"] = {}
    RelText["divine"]["initial"] = {
        "order":0,
        "text":_("The head Mage of Palam at the tower of Palam in Novaras. She is responsible for all the fledgling Palam mages.")}
    # add if romance
    RelText["divine"]["romance"] = {
        "order":1,
        "text":_("The two of us have now shared a bed, though between the risks for both of us, our affair shall be a secret, passionate one no doubt.")}