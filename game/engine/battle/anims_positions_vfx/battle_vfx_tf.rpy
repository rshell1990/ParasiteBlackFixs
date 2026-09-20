init python:
    def Battle_RunCharAnim(BattleChar, AnimID):
        if not hasattr(BattleChar, "SpriteTag"):
            BattleChar.SpriteTag = "battle_char_%s_%s_%s" % (BattleChar.BattleSide, BattleChar.CharID, id(BattleChar))
        renpy.hide(BattleChar.SpriteTag)

        # Fall back to idle animation if requested animation key is missing
        anims_dict = getattr(BattleChar.BattleSkin, "AnimsDict", {})
        target_anim = anims_dict.get(AnimID, anims_dict.get("idle"))

        if isinstance(target_anim, list):
            AnimObj = renpy.random.choice(target_anim)
        else:    
            AnimObj = target_anim

        if getattr(AnimObj, "AnimLoop", False):
            ShowWhat = AnimObj.Displayable
        else:
            IdleAnimObj = anims_dict.get("idle")
            idle_disp = getattr(IdleAnimObj, "Displayable", None) if IdleAnimObj else None
            ShowWhat = At(AnimObj.Displayable, Battle_TransformRevertToIdleAnim(AnimObj.LengthInSeconds, idle_disp))

        renpy.show(
            BattleChar.SpriteTag, 
            what = ShowWhat, 
            at_list = [Battle_TransformCharPosition(BattleChar)], 
            zorder = getattr(BattleChar, "SpriteZorder", 1)
        )
        return AnimObj

    def Battle_SpawnVfxOnChar(BattleChar, ImageID, RandomRotation = False, AutoXFlip = True):
        if RandomRotation:
            Rotation = renpy.random.uniform(0, 360)
        else:
            Rotation = 0

        tag_name = str(ImageID) + "_" + str(id(BattleChar))
        renpy.hide(tag_name)
        renpy.show(
            ImageID,
            at_list = [Battle_TransformVFXPosition(BattleChar, Rotation, AutoXFlip)],
            zorder = getattr(BattleChar, "SpriteZorder", 1) + 8,
            tag = tag_name
        )


# char sprites root tf
transform Battle_TransformCharPosition(BattleChar):
    anchor (0.5, 1.0)
    pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
    xoffset getattr(BattleChar.BattleSkin, "SpriteOffset", (0, 0))[0]
    yoffset getattr(BattleChar.BattleSkin, "SpriteOffset", (0, 0))[1] - 60
    
    xzoom (1.0 if BattleChar.BattleSide == 0 else -1.0)
    zoom (0.9 if BattleChar.PositionSlotIndex in [0, 1] else 1.0)

# helper tf that reverts to "idle" anim reliably
transform Battle_TransformRevertToIdleAnim(Delay, IdleDisplayable):
    pause Delay
    IdleDisplayable

# spot at which vfx sprites appear
transform Battle_TransformVFXPosition(BattleChar, Rotation = 0, AutoXFlip = True):
    anchor (0.5, 0.5)
    rotate Rotation
    pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
    offset getattr(BattleChar.BattleSkin, "SpriteVFXOffset", (0, 0))
    xzoom (-1.0 if BattleChar.BattleSide == 0 and AutoXFlip else 1.0)

######### default impact image on all skills and attacks
image Battle_VfxImpact:
    "images/battle_fx/impact.webp"
    Battle_TransformVfxImpact

transform Battle_TransformVfxImpact:
    subpixel True
    zoom 2.0
    ease 1.0:
        zoom 1.5
        alpha 0.0

############### "nod and bop (tm)" anims
# 0.45
transform Battle_TransformAttack(Char, Delay = 0.0, InLen = 0.05, OutLen = 0.4):
    subpixel True
    pause Delay
    ease InLen:
        xoffset (-60 if Char.BattleSide == 1 else 60)
    ease OutLen:
        xoffset 0

# 0.95
transform Battle_TransformIdle(Char):
    subpixel True
    ease 0.35:
        yzoom 1.01
    ease 0.6:
        yzoom 1.0
    repeat

# 0.45
transform Battle_TransformCast(Char):
    subpixel True
    ease 0.05:
        yoffset 5
        yzoom 0.97
    ease 0.4:
        yoffset 0
        yzoom 1.0

# 0.25
transform Battle_TransformHit(Char):
    subpixel True
    ease .05 xoffset 8
    ease .05 xoffset -8
    ease .05 xoffset 5
    ease .05 xoffset -5
    ease .05 xoffset 0