define VIVIAN = Character(_("Vivian"), image = "vivian")

init python:
    CharDefs["vivian"] = BuildCharTemplate(CharID = "vivian",
        portrait = "images/characters/vivian/portrait.webp",
        name = _("Vivian"),
        RelTextIDs = {"initial"},
        ExtraData = {
            "clothes": "normal",   # normal / naked / ling / normal_mug
        },
    )
    config.tag_layer["vivian"] = "characters"
    
    RelText["vivian"] = {}
    RelText["vivian"]["initial"] = {
        "order":0,
        "text":_("A barmaid at {i}The Dancing Frog{/i}, a fortress inn. She takes great pride in her professionalism.")
        }