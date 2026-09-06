screen enterCheatCode():
    modal True
    default cheat_code = ""
    frame:
        style "frame_outer"
        align (0.5,0.5)
        vbox:
            null width 200
            spacing 20
            text _("Enter cheat code"):
                align (0.5,0.5)
            text "{i}"+_("Some cheat codes will permanently disable achievements in the current savefile,\nuse with caution")+"{/i}":
                align (0.5,0.5)
                text_align 0.5
                color "#ff0000"
                size 24
            input:
                xalign 0.5
                default ""
                value ScreenVariableInputValue("cheat_code")
            hbox:
                align (0.5,0.5)
                spacing 20
                textbutton _("Ok"):
                    style "confirm_button"
                    action [Hide("enterCheatCode"), Function(processCheatCode,cheat_code)]
                    keysym "K_RETURN"

                textbutton _("Cancel"):
                    style "confirm_button"
                    action Hide("enterCheatCode")
                    keysym "K_ESCAPE"

init python:
    def processCheatCode(cheatString):
        isCheatOn = None

        if cheatString == ch_enablecheatmenu: # toggle cheat menu
            store.cheat_menu_bool = not store.cheat_menu_bool
            if store.cheat_menu_bool:
                isCheatOn = True

                if not main_menu:
                    store._enable_achievements = False

            if not store.cheat_menu_bool:
                isCheatOn = False

        if cheatString == ch_unlockallgallery: # unlock all gallery
            GalUnlockAllScenes()

        if cheatString == ch_lockallgallery: # lock all gallery (for w/e reason)
            GalLockAllScenes()

        if isCheatOn == True:
            renpy.music.play("audio/interface/cheat_on.ogg", channel=u'sound2', loop=None, relative_volume=1.0)
        if isCheatOn == False:
            renpy.music.play("audio/interface/cheat_off.ogg", channel=u'sound2', loop=None, relative_volume=1.0)

    def CHEAT_NakedParty():
        for CharID in list(worldChars.keys()):
            if CharHasVar(CharID, "clothes"):
                CharSetClothes(CharID, "naked")
    def CHEAT_NakedPartyUndo():
        for CharID in list(worldChars.keys()):
            if CharHasVar(CharID, "clothes"):
                CharSetClothes(CharID, "normal")