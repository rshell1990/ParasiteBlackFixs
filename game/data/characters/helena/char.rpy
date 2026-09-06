default HELENA = Character(_("Helena"), image = "helena")
init python:
    CharDefs["helena"] = BuildCharTemplate(CharID = "helena",
                                                    name = _("Helena"),
                                                    portrait = "images/characters/helena/portrait.webp", 
                                                    RelTextIDs = {"initial"},
                                                    ExtraData = {"clothes":"normal"})
    config.tag_layer["helena"] = "characters"


    RelText["helena"] = {}
    RelText["helena"]["initial"] = {
        "order":0,
        "text":_("A {i}highly{/i} sought after and respected courtesan.")}