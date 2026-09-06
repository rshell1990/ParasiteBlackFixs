default BETTY = Character(_("Betty"), image = "betty")

init python:
    CharDefs["betty"] = BuildCharTemplate(CharID = "betty",
        name = _("Betty"),
        portrait = "images/characters/betty/portrait.webp",
        RelTextIDs = {"summary_initial"},
        ExtraData = {"clothes":"normal"}) # naked, normal, normal_tray

    config.tag_layer["betty"] = "characters"

    RelText["betty"] = {}
    RelText["betty"]["summary_initial"] = {
        "order":0,
        "text":_("The barmaid of {i}The Naughty Wench,{/i} married to the owner, but she seems particularly flirty and open...")}
