# haaaax!
screen QuickSaveLoadCaller():
    if not main_menu:
        if not IsPlayerInBattle():
            if not IsPlayerInBaratiGame():
                if not IsPlayerInGalleryScene():
                    key config.keymap["quick_save"] action [Function(AddNotif, _("Game saved!")), QuickSave(message = "")]
                    key config.keymap["quick_load"] action QuickLoad()
                        
init python:
    config.always_shown_screens.append("QuickSaveLoadCaller")