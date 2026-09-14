# haaaax!
screen QuickSaveLoadCaller():
    if not main_menu:
        if not IsPlayerInBattle():
            if not IsPlayerInBaratiGame():
                if not IsPlayerInGalleryScene():
                    key config.keymap.get("quick_save", "K_s") action [Function(AddNotif, _("Game saved!")), QuickSave(message = "")]
                    key config.keymap.get("quick_load", "K_l") action QuickLoad()
                        
init python:
    config.always_shown_screens.append("QuickSaveLoadCaller")