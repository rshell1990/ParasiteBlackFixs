default NIJAH = Character(_("Nijah"), image = "nijah")
init python:
    CharDefs["nijah"] = BuildCharTemplate(CharID = "nijah",
        name = _("Nijah"),
        portrait = "images/characters/nijah/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal", # normal, naked, jewelry
            "pose":1, # 1, 2
            "prologueMet":False, # set True in prologue if you visit bordello
            "fledNovaras":False})
    config.tag_layer["nijah"] = "characters"
    config.tag_layer["cg_nijah_kiss_naked"] = "characters"
    config.tag_layer["cg_nijah_kiss_clothed"] = "characters"
    config.tag_layer["nijah_baby"] = "characters"

    RelText["nijah"] = {}
    # initially unlocked
    RelText["nijah"]["initial"] = {
        "order":0,
        "text":_("A Ramonian prostitute - Life is hard for her and her people here in Novaras.")}
    # add if sold to tarek
    RelText["nijah"]["sold_to_tarek"] = {
        "order":1,
        "text":_("...But alas, I can't afford to play hero. I betrayed her and sold her for some coin.")}
    # add if killed by tarek during damzel in diztrezz quest
    RelText["nijah"]["killed_by_tarek"] = {
        "order":1,
        "text":_("She was killed by Tarek, a criminal boss who had loaned her a hefty sum of money. So much for trying to help her...")}
    # add if market route
    RelText["nijah"]["market_stall"] = {
        "order":1,
        "text":_("Funding her food stall, Nijah has appointed herself my... quasi-wife? {i}Not that I'm complaining.{/i}")}
    # add if pimp route
    RelText["nijah"]["pimped_out"] = {
        "order":1,
        "text":_("Under my protection, Nijah has returned to her life as a prostitute. She seems to wish our relationship was more than just sex and protection though...")}

    RelText["nijah"]["died_during_siege"] = {
        "order":2,
        "text":_("She was killed by the Demorai during the siege of Novaras.")}
