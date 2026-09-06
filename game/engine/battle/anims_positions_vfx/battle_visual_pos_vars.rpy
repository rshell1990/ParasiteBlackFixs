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

    BattleChar_SpriteZorder = {} # spritezorder:hudzorder
    BattleChar_SpriteZorder[0] = (5, 6)

    BattleChar_SpriteZorder[1] = (1, 2)

    BattleChar_SpriteZorder[2] = (7, 8)

    BattleChar_SpriteZorder[3] = (3, 4)
