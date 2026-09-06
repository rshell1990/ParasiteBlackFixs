default NYX = Character(_("Nyx"), image = "nyx")
default NYXP = Character(_("Nyx"), image = "nyx", what_color = "#ff5ed1")
init python:
    
    CharDefs["nyx"] = BuildCharTemplate(CharID = "nyx",
                portrait = "images/characters/nyx/portrait.webp",
                name = _("Nyx"),
                RelTextIDs = {"initial"},
                ExtraData = {"clothes":"normal", 
                            "fold":False})
    config.tag_layer["nyx"] = "characters"
    config.tag_layer["cg_nyx_slave_back"] = "characters"
    config.tag_layer["cg_nyx_kiss_armor_relaxed"] = "characters"
    config.tag_layer["cg_nyx_kiss_armor_surprised"] = "characters"
    config.tag_layer["cg_nyx_kiss_naked"] = "characters"
    config.tag_layer["cg_nyx_halfnaked"] = "characters"

    RelText["nyx"] = {}
    # unlocked initially
    RelText["nyx"]["initial"] = {
        "order":0,
        "text":_("The Captain of the city guard of Novaras, strong-willed and resourceful, she's managed to hold this city together despite the odds... for now.")}
    # add if romance route
    RelText["nyx"]["romance"] = {
        "order":1,
        "text":_("In our time together, the two of us have become secret lovers. Whether it be from the loneliness and stress of the job, the captain needs someone she doesn't always have to be so strong around all the time... I guess that's me.")}
    # add if romance route dom
    RelText["nyx"]["romance_dom"] = {
        "order":1,
        "text":_("To the eyes of the world, she's a respectable, highly ranked captain who gives me and dozens like me orders to follow everyday. In private, {i}I{/i} order her around, my willing, secretly eager sex slave who needs to find some release from the crushing responsibilities of her job. If it's just sex, or something more, I guess we'll see...")}