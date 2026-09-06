default DROS = Character(_("Dros Ulvrak"), image = "dros")

init python:
    CharDefs["dros"] = BuildCharTemplate(CharID = "dros",
        name = _("Dros Ulvrak"),
        portrait = "images/characters/dros/portrait.webp", 
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})
    config.tag_layer["dros"] = "characters"

    RelText["dros"] = {}
    # initially present
    RelText["dros"]["initial"] = {
        "order":0,
        "text":_("An unfriendly, slightly pretentious elven tailor.")}
    
    # replace initial when romanced
    RelText["dros"]["romanced"] = {
        "order":0,
        "text":_("A slightly pretentious elven tailor, secretly nice once they warm up to you.")}
    
    # add when tf happens
    RelText["dros"]["transformed"] = {
        "order":1,
        "text":_("Having made some alterations to their body to become more feminine, they now ask me to call them {i}Draya.{/i}")}

    # add corresponding one on romance, depending on their sex
    RelText["dros"]["romance_male"] = {
        "order":2,
        "text":_("The two of us have agreed to secret romance to help deal with his {i}needs.{/i}")}

    RelText["dros"]["romance_female"] = {
        "order":2,
        "text":_("The two of us have agreed to secret romance to help deal with her {i}needs.{/i}")}