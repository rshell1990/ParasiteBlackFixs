default VIZURA = Character(_("Vizura"), image = "vizura")

init python:
    CharDefs["vizura"] = BuildCharTemplate(CharID = "vizura",
        name = _("Vizura"),
        portrait = "images/characters/vizura/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes" : "normal"})
    config.tag_layer["vizura"] = "characters"

    RelText["vizura"] = {}
    RelText["vizura"]["initial"] = {
        "order":0,
        "text":_("A goblin merchant I've encountered on my travels.")}

    RelText["vizura"]["post_sex"] = {
        "order":1,
        "text":_("The two of us have reached an {i}agreement.{/i} Whilst I wouldn't call it love, having someone so eager to jump into bed with me is certainly a pleasant distraction on my travels...")}