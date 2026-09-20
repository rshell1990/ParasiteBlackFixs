# Standalone native-style tooltip.
#
# Usage: on any button or displayable that supports focus, use the `tooltip`
# property, then `use NativeTooltip` inside the screen that contains it:
#
#     textbutton "Example":
#         action Return()
#         tooltip "Hello!"
#
#     screen my_screen():
#         use NativeTooltip
#
# This is fully self-contained and does not interfere with the existing
# TooltipSetUI/TooltipClearUI system in game/engine/tooltip/tooltip.rpy.
# Both can coexist during incremental migration.

screen NativeTooltip():
    zorder 100
    $ tt = GetTooltip()
    if tt:
        mouseAnchor (0, 0, 45, 50):
            frame:
                xmaximum 640
                padding (16, 12)
                if isinstance(tt, str):
                    text tt
                else:
                    add tt
