init python:
    def Battle_RunCharAnim(BattleChar, AnimID):
        """
        Executes a character pose animation safely without crashing if the key is missing.
        """
        if not hasattr(BattleChar, "BattleSkin") or not hasattr(BattleChar.BattleSkin, "AnimsDict"):
            return None

        # Check if the requested pose key exists in the character's skin
        if AnimID not in BattleChar.BattleSkin.AnimsDict:
            renpy.log(f"WARNING: Animation '{AnimID}' missing for skin '{BattleChar.BattleSkin}'.")
            return None

        # Retrieve the animation sequence/data and assign to AnimObj
        AnimObj = BattleChar.BattleSkin.AnimsDict[AnimID]

        # Check if the object is a container/list vs a direct displayable anim object
        if isinstance(AnimObj, list):
            # If the animation data is a list of steps/images
            pass

        # Safely evaluate looping and displayable properties
        if getattr(AnimObj, "AnimLoop", False):
            ShowWhat = getattr(AnimObj, "Displayable", AnimObj)
        else:
            IdleAnimObj = BattleChar.BattleSkin.AnimsDict.get("idle", None)
            IdleDisplayable = getattr(IdleAnimObj, "Displayable", IdleAnimObj)
            AnimDisplayable = getattr(AnimObj, "Displayable", AnimObj)
            AnimLength = getattr(AnimObj, "LengthInSeconds", 0.5)

            if IdleAnimObj:
                ShowWhat = At(AnimDisplayable, Battle_TransformRevertToIdleAnim(AnimLength, IdleDisplayable))
            else:
                ShowWhat = AnimDisplayable

        renpy.show(
            BattleChar.SpriteTag, 
            what = ShowWhat, 
            at_list = [Battle_TransformCharPosition(BattleChar)], 
            zorder = BattleChar.SpriteZorder
        )
        return AnimObj

    def Battle_SpawnVfxOnChar(BattleChar, ImageID, RandomRotation = False, AutoXFlip = True):
        if RandomRotation:
            Rotation = RngFloat(0, 360)
        else:
            Rotation = 0
        renpy.hide(ImageID + str(id(BattleChar)))
        renpy.show(ImageID,
            at_list = [Battle_TransformVFXPosition(BattleChar, Rotation, AutoXFlip)],
            zorder = BattleChar.SpriteZorder + 8,
            tag = ImageID + str(id(BattleChar)))
        return
    def Battle_ShowChargeVFX(BattleChar):
        """
        Displays the particle/visual effect overlay when charging a skill.
        """
        # Determine target displayable tag or character position
        char_tag = getattr(BattleChar, "SpriteTag", None) or getattr(BattleChar, "CharID", None)
        
        # Check if the charge VFX image exists in Ren'Py's image registry
        if renpy.has_image("vfx_charge"):
            renpy.show("vfx_charge", at_list=[Transform(center)])
        elif char_tag and renpy.has_image(f"vfx_charge_{char_tag}"):
            renpy.show(f"vfx_charge_{char_tag}")
        else:
            # Fallback log if no explicit charge VFX graphic is defined
            renpy.log(f"VFX Warning: 'Battle_ShowChargeVFX' triggered for '{char_tag}', but no VFX asset was found.")

# char sprites root tf
transform Battle_TransformCharPosition(BattleChar):
    anchor (0.5, 1.0)
    pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
    xoffset BattleChar.BattleSkin.SpriteOffset[0]
    yoffset BattleChar.BattleSkin.SpriteOffset[1] - 60
    
    xzoom (1.0 if BattleChar.BattleSide == 0 else -1.0)
    zoom (0.9 if BattleChar.PositionSlotIndex in [0, 1] else 1.0)

# helper tf that reverts to "idle" anim reliably
transform Battle_TransformRevertToIdleAnim(Delay, IdleDisplayable):
    Delay
    IdleDisplayable

# spot at which vfx sprites appear
transform Battle_TransformVFXPosition(BattleChar, Rotation = 0, AutoXFlip = True):
    anchor (0.5, 0.5)
    rotate Rotation
    pos BattleChar_ScreenPositions[BattleChar.BattleSide][BattleChar.PositionSlotIndex]
    offset BattleChar.BattleSkin.SpriteVFXOffset
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

############### "nod and bop (tm)" anims "
# 0.45
transform Battle_TransformAttack(Char, Delay = 0.0, InLen = 0.05, OutLen = 0.4):
    subpixel True
    Delay
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
    ease .05 xoffset -8 # 0.05
    ease .05 xoffset 5
    ease .05 xoffset -5 # 0.1
    ease .05 xoffset 0
##############
