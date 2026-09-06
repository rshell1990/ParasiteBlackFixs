init python:
    WorldLocation("travel_node_mine", STR_LOC.ABANDONED_MINE, "black")
    LocDef = wLocs["travel_node_mine"]
    LocDef.CanWait = False
    # ambience
    LocDef.withDayAmbience("audio/ambience_loc/cave.ogg")
    LocDef.withNightAmbience("audio/ambience_loc/cave.ogg")
    # music
    LocDef.withDayMusic("audio/music/40_Wander.ogg")
    LocDef.withNightMusic("audio/music/40_Wander.ogg")

    LocDef.withBtn("btn_leave", BtnJumpLabel(STR_NAV.LEAVE, "travel_node_mine_leave"))
    LocDef.withBtn("btn_mine", BtnDisabled())

    @AppendToAllQuests
    class TravelMine(LogicModule):
        def __init__(self):
            super().__init__()

            self.MineKind = None # rolls "iron", "gem", "copper", "syax". changes some stuff accordingly
            self.HasBeenMined = True # set to False on enter. as player "clicks" mine, turns True

        def OverrideLocBg(self):
            Result = {}            
            if TravelMine().MineKind == "iron":
                Result["travel_node_mine"] = "bg_mine_iron"
            elif TravelMine().MineKind == "syax":
                Result["travel_node_mine"] = "bg_mine_syax"
            elif TravelMine().MineKind == "gems":
                Result["travel_node_mine"] = "bg_mine_gems"
            elif TravelMine().MineKind == "copper":
                Result["travel_node_mine"] = "bg_mine_copper"
            return Result

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "travel_node_mine":
                if self.HasBeenMined:   
                    btnMods["btn_mine"] = BtnJumpLabel(_("Get mining"), "travel_event_mine_dig_empty")
                else:
                    btnMods["btn_mine"] = BtnJumpLabel(_("Get mining"), "travel_event_mine_dig")
            return LocButtonMod(directMods = btnMods)

screen loc_travel_node_mine():
    default locTag = "travel_node_mine"

    use locBtn_basic(locTag, "btn_mine",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.15, 0.55)))

    use locBtn_basic(locTag, "btn_leave",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)))

# for loc-button leaving
label travel_node_mine_leave:
    MC "(Should I go?)"
    menu:
        "Leave":
            $ GetOutToWorldMap()
        "Stay":
            $ LocEnterQ()

label travel_event_mine:
    $ TravelMine().MineKind = renpy.random.choice(["iron", "copper", "syax", "gems"])
    $ TravelMine().HasBeenMined = False

    show mc at left with easeinleft
    if TravelMine().MineKind == "iron":
        MC "(Hm... Looks like an abandoned iron mine.)"
        if PlayerItemQty("syax_pickaxe") > 0 or PlayerItemQty("iron_pickaxe") > 0:
            jump travel_event_mine_ask_enter
        else:
            MC "(It would make sense to explore it if I had a fitting pickaxe.)"
            MC "(I should move on.)"

    if TravelMine().MineKind == "gems":
        MC "(Hm... Looks like an abandoned gem mine.)"
        if PlayerItemQty("bronze_pickaxe") > 0 or PlayerItemQty("syax_pickaxe") > 0 or PlayerItemQty("iron_pickaxe") > 0:
            jump travel_event_mine_ask_enter
        else:
            MC "(It would make sense to explore it if I had a pickaxe.)"
            MC "(I should move on.)"

    if TravelMine().MineKind == "copper":
        MC "(Hm... Looks like an abandoned copper mine.)"
        if PlayerItemQty("bronze_pickaxe") > 0 or PlayerItemQty("syax_pickaxe") > 0 or PlayerItemQty("iron_pickaxe") > 0:
            jump travel_event_mine_ask_enter
        else:
            MC "(It would make sense to explore it if I had a fitting pickaxe.)"
            MC "(I should move on.)"

    if TravelMine().MineKind == "syax":
        MC "(Hm... Looks like an abandoned syax mine.)"
        MC "(Without royal decree, I can't even touch this stuff.)"
        MC "(Nor would any blacksmith even if I did...)"

    return

label travel_event_mine_ask_enter:
    MC "(Should I check inside?)"
    menu:
        "Enter the mine":
            scene black with dissolve
            "Heading into the darkened cavern alongside the railway lines, I found myself stood in the middle of an old mine."
            $ LocSet("travel_node_mine")
            $ LocEnter()

        "Move on":
            MC "(Perhaps another time.)"
            return

label travel_event_mine_dig:
    "Slamming my pickaxe against the rocks for some time, I managed to gather and chip away at the material I wanted."
    if renpy.random.randint(0, 2) == 0:
        $ TravelMine().HasBeenMined = True
    if TravelMine().MineKind == "iron":
        $ PlayerAddItem("iron_ore")
    if TravelMine().MineKind == "syax":
        $ PlayerAddItem("syax_ore")
    if TravelMine().MineKind == "gems":
        $ PlayerAddItem("raw_gems")
    if TravelMine().MineKind == "copper":
        $ PlayerAddItem("copper_ore")
    $ LocEnterQ()

label travel_event_mine_dig_empty:
    MC "(I can't see any more exposed material.)"
    MC "(It's time to move on.)"
    $ GetOutToWorldMap()