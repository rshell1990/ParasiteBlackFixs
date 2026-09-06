default ADARA = Character(_("Adara"), image = "adara")
init python:
    CharDefs["adara"] = BuildCharTemplate(CharID = "adara",
        name = _("Adara"),
        portrait = "images/characters/adara/portrait.webp",
        RelTextIDs = {"summary_initial", "append"},
        ExtraData = {"clothes":"normal", # naked, normal, normal_ash, ling
                    "blush":False})

    config.tag_layer["adara"] = "characters"
    config.tag_layer["cg_adara_dead_dad"] = "characters"
    
    config.tag_layer["cg_adara_hug_1"] = "characters"
    config.tag_layer["cg_adara_hug_2"] = "characters"
    config.tag_layer["cg_adara_hug_armor_2"] = "characters"

    # initially present, replaced after tj
    RelText["adara"] = {}
    RelText["adara"]["summary_initial"] = {
        "order":0,
        "text":_("My childhood friend, there has long been unspoken feelings shared between the two of us.")}

    # always present, appended to the end
    RelText["adara"]["append"] = {
        "order":1,
        "text":_("Sweet and protective, Adara has always been the one to help get me out of the trouble Markus led me into.")}

    # replaces initial line after tj
    RelText["adara"]["summary_post_titjob"] = {
        "order":0,
        "text":_("My childhood friend, our friendship has become something else, yet, neither of us can put into words what we are yet.")}