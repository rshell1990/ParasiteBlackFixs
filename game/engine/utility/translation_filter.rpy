init python:  
    translate_exclude_files = [
        "test_script.rpy",
        "test_script2.rpy",
        "test_script3.rpy",
        "test_script4.rpy",
        "battle_setup.rpy",
        "dev_menu.rpy",
        "devroom.rpy",
    ]
    translate_list_files_ORIG = renpy.translation.generation.translate_list_files
    def _filtered_translate_list_files():  
        return [
            f for f in translate_list_files_ORIG() if not any(excl in f for excl in translate_exclude_files)
        ]
    renpy.translation.generation.translate_list_files = _filtered_translate_list_files