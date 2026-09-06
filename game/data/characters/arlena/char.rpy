default ARLENA = Character(_("Arlena"), image = "arlena")
init python:
    CharDefs["arlena"] = BuildCharTemplate(CharID = "arlena",
        portrait = "images/characters/arlena/portrait.webp",
        name = _("Arlena"),
        RelTextIDs = {"summary", "relation_initial"},
        ExtraData = {"clothes":"normal"}) # normal, naked, apron, normal_ash
    config.tag_layer["arlena"] = "characters"

    RelText["arlena"] = {}
    # always present
    RelText["arlena"]["summary"] = {
        "order":0,
        "text":_("A popular blacksmith's daughter, she studied alongside me when I was younger.")}

    # present at start, replaced after they become lovers
    RelText["arlena"]["relation_initial"] = {
        "order":1,
        "text":_("I get the impression she doesn't like me very much...")}

    # replaces the above after lovers
    RelText["arlena"]["relation_lovers"] = {
        "order":1,
        "text":_("The two of us have become lovers, not that she'd ever admit it without kicking me first!")}

    # if died during novaras siege
    RelText["arlena"]["died_during_siege"] = {
        "order":2,
        "text":_("She was killed by the Demorai during the siege. Her memory will live on in my heart.")}