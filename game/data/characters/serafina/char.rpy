default SERAFINA = Character(_("Serafina"), image = "serafina")

init python:
    CharDefs["serafina"] = BuildCharTemplate(CharID = "serafina",
        name = _("Serafina"),
        portrait = "images/characters/serafina/portrait.webp",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal", # (inq)uisitor, mage, naked, normal
            "hat":True, # for inquisitor outfit
        }
    )

    config.tag_layer["serafina"] = "characters"

    RelText["serafina"] = {}
    # unlocked at start
    RelText["serafina"]["initial"] = {
        "order":0,
        "text":_("The daughter of Chanyi and Anya Faymore. A beautiful, adventurous girl of incredible magecraft who has the strange and deadly power of making her dreams... or nightmares... a reality.")}