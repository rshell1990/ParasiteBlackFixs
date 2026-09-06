default SHAY = Character(_("Shay"), image = "shay")

init python:
    CharDefs["shay"] = BuildCharTemplate(
        CharID = "shay", 
        name = _("Shay"), 
        portrait = "images/characters/shay/portrait.webp", 
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"}, # normal / naked / ling
    )
    config.tag_layer["shay"] = "characters"

    RelText["shay"] = {}
    RelText["shay"]["initial"] = {
        "order":0,
        "text":_("The co-owner of the {i}Iron Unicorn{/i}, a beautiful, buxom barmaid. Despite being married, she seems readily happy to tease the clientele if it means more coin...")}
