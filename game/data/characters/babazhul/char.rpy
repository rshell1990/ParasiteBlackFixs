default BABAZHUL = Character(_("Babazhul"), image = "babazhul")
default BABAZHUL_MAD = Character(_("Babazhul"), what_color = "#69ffe3", what_style = "babazhul_mad_text", image = "babazhul")

init python:
    CharDefs["babazhul"] = BuildCharTemplate(CharID = "babazhul",
        name = _("Babazhul"),
        portrait = "images/characters/babazhul/portrait.webp", 
        RelTextIDs = {"initial"},
        ExtraData = {"lit":"no"}) #<- for her crystal ball

    config.tag_layer["babazhul"] = "characters"

    RelText["babazhul"] = {}
    RelText["babazhul"]["initial"] = {
        "order":0,
        "text":_("A mysterious soothsayer who offers a glimpse at her powers in return for coin...")}

