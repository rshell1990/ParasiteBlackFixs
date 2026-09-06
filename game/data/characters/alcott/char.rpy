default ALCOTT = Character(_("Emperor Alcott"), image = "alcott")
init python:
    CharDefs["alcott"] = BuildCharTemplate(CharID = "alcott",
        name = _("Emperor Alcott"),
        RelTextIDs = {"initial"},
        portrait = "images/characters/alcott/portrait.webp")
    config.tag_layer["alcott"] = "characters"

    RelText["alcott"] = {}
    RelText["alcott"]["initial"] = {
        "order":0,
        "text":_("The defacto leader of Alderay, a once former general under king Mesamore who led Novaras' defence during the great siege. Turned usurper, he overthrew Mesamore and now rules with an iron fist over all of us.")}