init python:
    @AppendToAllQuests
    # off by default, enabled as a reward for TwoEmperors
    # it's a button that lets you leave the location
    class TravelButtonDemoraiTemple(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "demorai_temple":
                btnMods["btn_demorai_temple_travel"] = BtnTravel()
            return LocButtonMod(directMods=btnMods)

    WorldLocation("demorai_temple", STR_LOC.DEMORAI_TEMPLE_OUT, "bg_demorai_temple", WorldMapRootLocTag = "demorai_temple")
    LocDef = wLocs["demorai_temple"]
    LocDef.withBtn("btn_demorai_temple_travel", BtnDisabled())
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/desert_day.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/desert_night.ogg")
    # music
    LocDef.withDayMusic("audio/music/8_ValleyofDeath.ogg")
    LocDef.withNightMusic("audio/music/8_ValleyofDeath.ogg")
    # to int
    LocDef.withBtn("demoraiTempleEnter", 
        BtnChangeLoc(STR_NAV.ENTER, "demorai_temple_interior"))
    # travel
    LocDef.withWorldMap(STR_LOC.DEMORAI_TEMPLE_OUT,
        ["valley_of_death", "hamun_gates"],
        "images/world_map/demorai_temple.webp", (1784, 1239))
    LocDef.SetDayNightMatrixClass(MxDayNight_Desert)

    #LocDef.withRouteNavigation("hamun_gates", demorai_temple_to_hamun_gates_route)
    #LocDef.withRouteNavigation("valley_of_death", demorai_temple_to_valley_of_death_route)

screen loc_demorai_temple():
    default locTag = "demorai_temple"

    if QstIsActive(TravelButtonDemoraiTemple):
        use locBtn_basic(locTag,"btn_demorai_temple_travel",
            "images/gui/buttons_loc/travel.webp",
            Transform(pos = (0.5, 0.85)), 
            key = config.keymap["nav_down"])

    use locBtn_basic(locTag,"demoraiTempleEnter",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.32, 0.53)), 
        key = config.keymap["nav_up"])