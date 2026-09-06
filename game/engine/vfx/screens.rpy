screen location_light_overlay(locTag):
    # if called via script with 'show screen', renpy seems to opt to pay attention to this layer definition.
    # if called via python, with renpy.show_screen, renpy seems to actually pay attention to _layer = X argument.
    # therefore, we need both.
    layer "vfx"
    default adjTag = (locTag + "_night"  if IsInTimeFrame(TIME_VISUAL_DUSK, TIME_VISUAL_DAWN) else locTag)
    if adjTag in vfxLibLights:
        for sprite, coords in vfxLibLights[adjTag].items():
            for item in coords:
                add sprite at flicker(item)
