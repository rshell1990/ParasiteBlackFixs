default MRS_WINWARD = Character(_("Mrs. Winward"), image = "mrs_winward")
init python:
    CharDefs["mrs_winward"] = BuildCharTemplate(CharID = "mrs_winward",
        name = _("Mrs. Winward"),
        portrait = "images/characters/winward_mrs/portrait.webp",
        RelTextIDs = {"summary_initial"},
        ExtraData = {"clothes":"normal"}) # normal, cowl, naked, funeral

    config.tag_layer["mrs_winward"] = "characters"

    config.tag_layer["cg_winward_ass"] = "characters"
    config.tag_layer["cg_winward_tits"] = "characters"
    config.tag_layer["cg_winward_kiss"] = "characters"
    config.tag_layer["cg_winward_kiss_cowl"] = "characters"
    config.tag_layer["cg_winward_funeral_tits"] = "characters"

    RelText["mrs_winward"] = {}
    RelText["mrs_winward"]["summary_initial"] = {
        "order":0,
        "text":_("Mrs. Winward, a tanner lady.")}