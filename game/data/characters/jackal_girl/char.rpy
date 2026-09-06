default JACKAL_GIRL = Character(_("Jackal girl"), image = "jackal_girl")
init python:
    CharDefs["jackal_girl"] = BuildCharTemplate(CharID = "jackal_girl",
                                name = _("Jackal girl"),
                                portrait = "images/characters/jackal_girl/portrait.webp",
                                ExtraData = {"clothes":"normal"}) # naked / normal
    config.tag_layer["jackal_girl"] = "characters"

    # this only exists because player can kill her, so its like a flag
    @AppendToAllQuests
    class EventJackalGirlEncounter(LogicModule):
        def __init__(self):
            super().__init__()
