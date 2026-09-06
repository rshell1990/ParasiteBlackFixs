## (bot floor)
# hallway
# dining room
# library
# kitchen
# study
# cellar

## (top floor)
# hallway, upstairs
# bathroom
# hallway 2 (name)
# nursery
# master bedroom


init python:    
    # The dream house can be found right at the entrance to the "ancient forest" location. It is the first map/location available on clicking the ancient forest. The deeper parts of the forest will be expanded later.
    # so player arrives to Ancient Forest location and they can straight up see the clickable house
    # this "unlocks" (enables) clickey house
    @AppendToAllQuests
    class HouseLockDreamhouse(LogicModule):
        def __init__(self):
            super().__init__()

            # prog 0 is "can enter" (the quest trigger/interrupt whatever is handled by the dreamhouse quest)
            # prog 1 is "cant enter,strange force"
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "ancient_forest":
                if self.progress == 0:
                    btnMods["ancient_forest_dreamhouse"] = BtnChangeLoc(STR_LOC.DREAMHOUSE, "dreamhouse_hallway")
                elif self.progress == 1:
                    btnMods["ancient_forest_dreamhouse"] = BtnJumpLabel(STR_LOC.DREAMHOUSE, "dreamhouse_cant_enter")
            return LocButtonMod(directMods = btnMods)

label dreamhouse_cant_enter:
    MC "(I feel a strange force push against me when trying to enter this place...)"
    $ LocEnterQ()

init python:
################## main hallway/entrance
    WorldLocation("dreamhouse_hallway", STR_LOC.DREAMHOUSE_HALLWAY, "bg_dreamhouse_l1_entrance", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_hallway"]
    LocDef.CanWait = False
    
    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_hallway_to_outside", BtnChangeLoc(STR_LOC.ANCIENT_FOREST, "ancient_forest")) 
    LocDef.withBtn("dreamhouse_hallway_to_upstairs", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY_UPSTAIRS, "dreamhouse_hallway_upstairs")) 
    LocDef.withBtn("dreamhouse_hallway_to_diningroom", BtnChangeLoc(STR_LOC.DREAMHOUSE_DININGROOM, "dreamhouse_diningroom")) 
    LocDef.withBtn("dreamhouse_hallway_candle", BtnDisabled()) 

    # vfx
    #vfxLibLights["dreamhouse_hallway"] = {
    #    "lightpost_big":   [(1175, 540)], 
    #}
    #vfxLibLights["dreamhouse_hallway_night"] = vfxLibLights["dreamhouse_hallway"]


################## dining room
    WorldLocation("dreamhouse_diningroom", STR_LOC.DREAMHOUSE_DININGROOM, "bg_dreamhouse_l1_diningroom", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_diningroom"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_diningroom_to_hallway", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY, "dreamhouse_hallway")) 
    LocDef.withBtn("dreamhouse_diningroom_to_library", BtnChangeLoc(STR_LOC.DREAMHOUSE_LIBRARY, "dreamhouse_library")) 
    LocDef.withBtn("dreamhouse_diningroom_to_kitchen", BtnChangeLoc(STR_LOC.DREAMHOUSE_KITCHEN, "dreamhouse_kitchen")) 
    LocDef.withBtn("dreamhouse_diningroom_table", BtnDisabled()) 
    LocDef.withBtn("dreamhouse_diningroom_wolfhead", BtnDisabled()) 
    LocDef.withBtn("dreamhouse_diningroom_portrait", BtnDisabled()) 



################## library 
    WorldLocation("dreamhouse_library", STR_LOC.DREAMHOUSE_LIBRARY, "bg_dreamhouse_l1_library", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_library"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_library_to_study", BtnDisabled())
    LocDef.withBtn("dreamhouse_library_to_diningroom", BtnChangeLoc(STR_LOC.DREAMHOUSE_DININGROOM, "dreamhouse_diningroom")) 

    LocDef.withBtn("dreamhouse_library_portrait", BtnDisabled())
    LocDef.withBtn("dreamhouse_library_books_1", BtnDisabled())
    LocDef.withBtn("dreamhouse_library_books_2", BtnDisabled())
    LocDef.withBtn("dreamhouse_library_fireplace", BtnDisabled())

    LocDef.withBtn("dreamhouse_library_floorstuff", BtnDisabled())


################## kitchen 
    WorldLocation("dreamhouse_kitchen", STR_LOC.DREAMHOUSE_KITCHEN, "bg_dreamhouse_l1_kitchen", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_kitchen"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_kitchen_to_cellar", BtnChangeLoc(STR_LOC.DREAMHOUSE_CELLAR, "dreamhouse_cellar")) 
    LocDef.withBtn("dreamhouse_kitchen_to_diningroom", BtnChangeLoc(STR_LOC.DREAMHOUSE_DININGROOM, "dreamhouse_diningroom")) 

    LocDef.withBtn("dreamhouse_kitchen_cupboards", BtnDisabled()) 
    LocDef.withBtn("dreamhouse_kitchen_pot", BtnDisabled())
    LocDef.withBtn("dreamhouse_kitchen_table", BtnDisabled()) 

################## cellar 
    WorldLocation("dreamhouse_cellar", STR_LOC.DREAMHOUSE_CELLAR, "bg_dreamhouse_l1_cellar", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_cellar"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_cellar_to_kitchen", BtnChangeLoc(STR_LOC.DREAMHOUSE_KITCHEN, "dreamhouse_kitchen")) 
    LocDef.withBtn("dreamhouse_cellar_barrel", BtnDisabled())
    LocDef.withBtn("dreamhouse_cellar_papers", BtnDisabled())
    # for l2 specifically
    LocDef.withBtn("dreamhouse_cellar_mercenary", BtnDisabled())

   
################## study
    WorldLocation("dreamhouse_study", STR_LOC.DREAMHOUSE_STUDY, "bg_dreamhouse_l1_study", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_study"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_study_to_library", BtnChangeLoc(STR_LOC.DREAMHOUSE_LIBRARY, "dreamhouse_library")) 
    LocDef.withBtn("dreamhouse_study_desk", BtnDisabled()) 

################## hallway upstairs
    WorldLocation("dreamhouse_hallway_upstairs", STR_LOC.DREAMHOUSE_HALLWAY_UPSTAIRS, "bg_dreamhouse_l1_hallway_upstairs", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_hallway_upstairs"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_upstairs_to_entrance", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY, "dreamhouse_hallway")) 
    LocDef.withBtn("dreamhouse_upstairs_to_bathroom", BtnChangeLoc(STR_LOC.DREAMHOUSE_BATHROOM, "dreamhouse_bathroom")) 
    LocDef.withBtn("dreamhouse_upstairs_to_hallway2", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY2, "dreamhouse_hallway2")) 

################## bathroom
    WorldLocation("dreamhouse_bathroom", STR_LOC.DREAMHOUSE_BATHROOM, "bg_dreamhouse_l1_bathroom", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_bathroom"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_bathroom_to_hallway_upstairs", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY_UPSTAIRS, "dreamhouse_hallway_upstairs")) 
    LocDef.withBtn("dreamhouse_bathroom_bathtub", BtnDisabled())
    LocDef.withBtn("dreamhouse_bathroom_mirror", BtnDisabled())


################## hallway2
    WorldLocation("dreamhouse_hallway2", STR_LOC.DREAMHOUSE_HALLWAY2, "bg_dreamhouse_l1_hallway2", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_hallway2"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_hallway2_to_upstairs", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY_UPSTAIRS, "dreamhouse_hallway_upstairs")) 
    LocDef.withBtn("dreamhouse_hallway2_to_nursery", BtnChangeLoc(STR_LOC.DREAMHOUSE_NURSERY, "dreamhouse_nursery")) 
    LocDef.withBtn("dreamhouse_hallway2_to_bedroom", BtnDisabled()) 

################## nursery
    WorldLocation("dreamhouse_nursery", STR_LOC.DREAMHOUSE_NURSERY, "bg_dreamhouse_l1_nursery", WorldMapRootLocTag = "ancient_forest")
    LocDef = wLocs["dreamhouse_nursery"]
    LocDef.CanWait = False

    # music
    LocDef.withDayMusic("audio/music/57_enter_the_dream_house.ogg")
    LocDef.withNightMusic("audio/music/57_enter_the_dream_house.ogg")

    # clickables
    LocDef.withBtn("dreamhouse_nursery_to_hallway2", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY2, "dreamhouse_hallway2")) 
    LocDef.withBtn("dreamhouse_nursery_toys", BtnDisabled()) 
    LocDef.withBtn("dreamhouse_nursery_crib", BtnDisabled())

# ################## bedroom
#     WorldLocation("dreamhouse_bedroom", STR_LOC.DREAMHOUSE_BEDROOM, "bg_dreamhouse_l1_entrance", WorldMapRootLocTag = "ancient_forest")
#     LocDef = wLocs["dreamhouse_bedroom"]
#     LocDef.CanWait = False

#     # clickables
#     LocDef.withBtn("dreamhouse_bedroom_to_hallway2", BtnChangeLoc(STR_LOC.DREAMHOUSE_HALLWAY2, "dreamhouse_hallway2")) 





################ screens for all locs
screen loc_dreamhouse_hallway():
    default locTag = "dreamhouse_hallway"

    # exit outside
    use locBtn_basic(locTag, "dreamhouse_hallway_to_outside",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # to upstairs
    use locBtn_basic(locTag, "dreamhouse_hallway_to_upstairs",
        "images/gui/buttons_loc/arrow_u.webp",
        Transform(pos = (0.08, 0.5)),
        key = config.keymap["nav_left"])

    # to diningroom
    use locBtn_basic(locTag, "dreamhouse_hallway_to_diningroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.85, 0.5)),
        key = config.keymap["nav_right"])

    # candle
    use locBtn_basic(locTag, "dreamhouse_hallway_candle",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.61, 0.54)),
        )


screen loc_dreamhouse_diningroom():
    default locTag = "dreamhouse_diningroom"

    # to library
    use locBtn_basic(locTag, "dreamhouse_diningroom_to_library",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.056, 0.481)),
        key = config.keymap["nav_left"])

    # to kitchen
    use locBtn_basic(locTag, "dreamhouse_diningroom_to_kitchen",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.321, 0.481)),
        key = config.keymap["nav_up"])

    # to hallway
    use locBtn_basic(locTag, "dreamhouse_diningroom_to_hallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.901, 0.46)),
        key = config.keymap["nav_right"])

    # table
    use locBtn_basic(locTag, "dreamhouse_diningroom_table",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.509, 0.549)),
        )
    # wolfhead
    use locBtn_basic(locTag, "dreamhouse_diningroom_wolfhead",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.559, 0.313)),
        )
    # protrait
    use locBtn_basic(locTag, "dreamhouse_diningroom_portrait",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.195, 0.356)),
        )



screen loc_dreamhouse_library():
    default locTag = "dreamhouse_library"

    # to study
    use locBtn_basic(locTag, "dreamhouse_library_to_study",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.636, 0.459)),
        key = config.keymap["nav_up"])

    # to dining
    use locBtn_basic(locTag, "dreamhouse_library_to_diningroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # portrait
    use locBtn_basic(locTag, "dreamhouse_library_portrait",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.21, 0.337)))
    # book l
    use locBtn_basic(locTag, "dreamhouse_library_books_1",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.372, 0.403)))
    # book r
    use locBtn_basic(locTag, "dreamhouse_library_books_2",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.534, 0.397)))
    # firep;lace
    use locBtn_basic(locTag, "dreamhouse_library_fireplace",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.847, 0.531)))
    # aka human sacrificies 
    use locBtn_basic(locTag, "dreamhouse_library_floorstuff",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.67, 0.74)))



screen loc_dreamhouse_kitchen():
    default locTag = "dreamhouse_kitchen"

    # to cellar
    use locBtn_basic(locTag, "dreamhouse_kitchen_to_cellar",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.544, 0.578)),
        key = config.keymap["nav_right"])

    # to dining
    use locBtn_basic(locTag, "dreamhouse_kitchen_to_diningroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.964, 0.552)),
        key = config.keymap["nav_left"])

    # cupboards
    use locBtn_basic(locTag, "dreamhouse_kitchen_cupboards",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.13, 0.478)),
        )
    # pot
    use locBtn_basic(locTag, "dreamhouse_kitchen_pot",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.344, 0.522)),
        )
    # table
    use locBtn_basic(locTag, "dreamhouse_kitchen_table",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.466, 0.639)),
        )


screen loc_dreamhouse_cellar():
    default locTag = "dreamhouse_cellar"

    # to kitchen
    use locBtn_basic(locTag, "dreamhouse_cellar_to_kitchen",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])
    # barrel
    use locBtn_basic(locTag, "dreamhouse_cellar_barrel",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.713, 0.502)),
        )
    # papers
    use locBtn_basic(locTag, "dreamhouse_cellar_papers",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.507, 0.499)),
        )
    # merc (l2)
    use locBtn_basic(locTag, "dreamhouse_cellar_mercenary",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.31, 0.69)),
        )



screen loc_dreamhouse_hallway_upstairs():
    default locTag = "dreamhouse_hallway_upstairs"

    # to entrance
    use locBtn_basic(locTag, "dreamhouse_upstairs_to_hallway",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.85, 0.5)),
        key = config.keymap["nav_right"])

    # to hallway2
    use locBtn_basic(locTag, "dreamhouse_upstairs_to_hallway2",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.55, 0.5)),
        key = config.keymap["nav_up"])

    # to bathroom
    use locBtn_basic(locTag, "dreamhouse_upstairs_to_bathroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.15, 0.5)),
        key = config.keymap["nav_left"])



screen loc_dreamhouse_hallway_upstairs():
    default locTag = "dreamhouse_hallway_upstairs"

    # to entrance
    use locBtn_basic(locTag, "dreamhouse_upstairs_to_entrance",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.91, 0.62)),
        key = config.keymap["nav_right"])

    # to hallway2
    use locBtn_basic(locTag, "dreamhouse_upstairs_to_hallway2",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.723, 0.494)),
        key = config.keymap["nav_up"])

    # to bathroom
    use locBtn_basic(locTag, "dreamhouse_upstairs_to_bathroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.207, 0.501)),
        key = config.keymap["nav_left"])



screen loc_dreamhouse_hallway2():
    default locTag = "dreamhouse_hallway2"

    # to upstairs stairs
    use locBtn_basic(locTag, "dreamhouse_hallway2_to_upstairs",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # to nursery
    use locBtn_basic(locTag, "dreamhouse_hallway2_to_nursery",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.34, 0.506)),
        key = config.keymap["nav_left"])

    # to bedroom
    use locBtn_basic(locTag, "dreamhouse_hallway2_to_bedroom",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.878, 0.57)),
        key = config.keymap["nav_right"])



screen loc_dreamhouse_nursery():
    default locTag = "dreamhouse_nursery"

    # to hallway2
    use locBtn_basic(locTag, "dreamhouse_nursery_to_hallway2",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # toys
    use locBtn_basic(locTag, "dreamhouse_nursery_toys",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.24, 0.581)),
        )
    # crib
    use locBtn_basic(locTag, "dreamhouse_nursery_crib",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.595, 0.484)),
        )

# screen loc_dreamhouse_bedroom():
#     default locTag = "dreamhouse_bedroom"

#     # to hallway2
#     use locBtn_basic(locTag, "dreamhouse_bedroom_to_hallway2",
#         "images/gui/buttons_loc/door.webp",
#         Transform(pos = (0.5, 0.85)),
#         key = config.keymap["nav_down"])


screen loc_dreamhouse_study():
    default locTag = "dreamhouse_study"

    # to library
    use locBtn_basic(locTag, "dreamhouse_study_to_library",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # desk
    use locBtn_basic(locTag, "dreamhouse_study_desk",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.75, 0.53)),
        )



screen loc_dreamhouse_bathroom():
    default locTag = "dreamhouse_bathroom"

    # to hallway upstairs
    use locBtn_basic(locTag, "dreamhouse_bathroom_to_hallway_upstairs",
        "images/gui/buttons_loc/door.webp",
        Transform(pos = (0.5, 0.85)),
        key = config.keymap["nav_down"])

    # bathtub
    use locBtn_basic(locTag, "dreamhouse_bathroom_bathtub",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.642, 0.573)),
        )
    
    # mirror
    use locBtn_basic(locTag, "dreamhouse_bathroom_mirror",
        "images/gui/buttons_loc/question.webp",
        Transform(pos = (0.184, 0.476)),
        )

