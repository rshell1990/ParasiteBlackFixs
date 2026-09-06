default MR_WINWARD = Character(_("Mr. Winward"), image = "mr_winward")

init python:
    CharDefs["mr_winward"] = BuildCharTemplate(CharID = "mr_winward",
                                                name = _("Mr. Winward"),
                                                portrait = "images/characters/winward_mr/portrait.webp",
                                                RelTextIDs = {"summary_initial"})

    config.tag_layer["mr_winward"] = "characters"

    RelText["mr_winward"] = {}
    RelText["mr_winward"]["summary_initial"] = {
        "order":0,
        "text":_("Mrs. Winward's husband.")}
    RelText["mr_winward"]["killed_by_mc_jackpot"] = {
        "order":1,
        "text":_("As the Dark Passenger put it, there was an eighty-four-point-six percent chance of him getting killed if he continued on his path. Tough luck.")}