default MIKA = Character(_("Mika"), image = "mika")
init python:
    CharDefs["mika"] = BuildCharTemplate(CharID = "mika",
                                name = _("Mika"),
                                portrait = "images/characters/mika/portrait.webp",
                                BattleSkin = "mika",

                                BattleClass = "warrior",

                                Strength = 4,
                                Endurance = 6,
                                Willpower = 5,
                                Agility = 6,
                                Dexterity = 6,
                                Luck = 3,

                                CharSkills = {"NeutralASmallBlessingMageVariant":1, "NeutralColdWeather":1},
                                is_mage = True,
                                ExtraData = {"clothes":"dress"}, # naked / ling1 / ling2 / dress
                                RelTextIDs = {"initial", "append"},
    )
    config.tag_layer["mika"] = "characters"

    config.tag_layer["cg_mika_backstory_1"] = "characters"
    config.tag_layer["cg_mika_backstory_2"] = "characters"
    config.tag_layer["cg_mc_mika_kiss"] = "characters"
    config.tag_layer["cg_mc_mika_hug"] = "characters"
    config.tag_layer["cg_mc_mika_hug_cry"] = "characters"
    config.tag_layer["cg_mc_mika_kiss_naked"] = "characters"
    config.tag_layer["cg_mika_boner"] = "characters"
    config.tag_layer["cg_mika_bare_tits"] = "characters"
    config.tag_layer["cg_mika_ass"] = "characters"
    config.tag_layer["cg_mika_baby"] = "characters"

    # initially present, replaced after tj
    RelText["mika"] = {}
    RelText["mika"]["append"] = {
        "order":0,
        "text":_("An insecure mage of Palam with a fear of fighting.")}
    # always present, appended to the end
    RelText["mika"]["append_2"] = {
        "order":0,
        "text":_("After much hard work, she's now capable of defending herself!")}
    # replaces initial line after tj
    RelText["mika"]["love"] = {
        "order":1,
        "text":_("During our time training together we became close and I took her as my lover.")}