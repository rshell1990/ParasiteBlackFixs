default LUCY = Character(_("Lucy"), image = "lucy")

init python:
    CharDefs["lucy"] = BuildCharTemplate(CharID = "lucy",
        name = _("Lucy"),
        portrait = "images/characters/lucy/portrait.webp",
        RelTextIDs = {"summary_initial"},
        ExtraData = {"clothes":"normal"}) # naked, normal

    config.tag_layer["lucy"] = "characters"

    RelText["lucy"] = {}
    RelText["lucy"]["summary_initial"] = {
        "order":0,
        "text":_("The beautiful but nervous barmaid at {i}The Cat at sundown.{/i} She seems open to earning coins in ways other than just pouring drinks...")}