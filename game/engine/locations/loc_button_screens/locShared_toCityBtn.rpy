# Location sub-screens that define multiple buttons should use the "locShared_" prefix
# this button's purpose is to have same placement position & same hotkey
screen locShared_toCityBtn(locTag, ButtonTag):
    use locBtn_basic(locTag, ButtonTag, "images/gui/buttons_loc/door.webp", Transform(pos = (0.5, 0.85)), key = config.keymap["nav_down"])
