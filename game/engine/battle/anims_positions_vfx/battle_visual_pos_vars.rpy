init python:
    # position of left slots,
    BattleChar_ScreenPositions = {}
    BattleChar_ScreenPositions[0] = [(720, 730), (560, 440), (340, 740), (230, 455)]
    #BattleChar_ScreenPositions[0] = [(230, 455), (560, 440), (720, 730), (340, 740)]

    

    # order is based on *distance from center*

    # right slots are mirrored
    BattleChar_ScreenPositions[1] = []
    for Coords in BattleChar_ScreenPositions[0]:
        BattleChar_ScreenPositions[1].append((1920 - Coords[0], Coords[1]))

    # Keep the same side -> slot structure used by the battle loop. Slots 0 and
    # 2 are in front of slots 1 and 3, matching the overlapping formation.
    BattleChar_SpriteZorder = {
        0: {0: (5, 6), 1: (1, 2), 2: (7, 8), 3: (3, 4)},
        1: {0: (5, 6), 1: (1, 2), 2: (7, 8), 3: (3, 4)},
        }
