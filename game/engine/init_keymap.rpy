init -1 python:
    ### CUSTOM ###
    config.keymap["quick_save"] = ["K_F5"]
    config.keymap["quick_load"] = ["K_F9"]
    config.keymap["inventory"] = ["K_e"]
    config.keymap["characters"] = ["K_c"]
    # dev override to not overlap hotreload
    if config.developer:
        config.keymap["relations"] = ["K_y"]
    else: 
        config.keymap["relations"] = ["K_r"]
    config.keymap["map"] = ["K_x"]
    config.keymap["journal"] = ["K_q"]
    config.keymap["gui_rest_menu"] = ["K_t"]
    config.keymap["dialogue_history"] = ["K_b"]

    config.keymap["nav_up"] = ["K_w"]
    config.keymap["nav_down"] = ["K_s"]
    config.keymap["nav_right"] = ["K_d"]
    config.keymap["nav_left"] = ["K_a"]

    ### NATIVE MAINTAINED ###
    config.keymap["save_delete"] = ["K_DELETE"]
    config.keymap["iconify"] = ["alt_K_F1"]
    
    if config.developer:
        config.keymap["toggle_skip"] = ["K_F7"]
    else:
        config.keymap["toggle_skip"] = ["K_TAB"]

    # during development i sometimes need to press ctrl w/o weird shit happening so I just freed right ctrl -tmm
    if config.developer:
        config.keymap["skip"] = ["K_LCTRL"]
    else:
        config.keymap["skip"] = ["K_LCTRL", "K_RCTRL"]
    config.keymap["fast_skip"] = [">", "shift_K_PERIOD"]
    config.keymap["full_inspector"] = ["alt_shift_K_i"]
    config.keymap["developer"] = ["shift_K_d"]
    config.keymap["hide_windows"] = ["h","mouseup_2"]
    config.keymap["choose_renderer"] = ["G","shift_K_g"]
    config.keymap["self_voicing"] = ["v"]
    config.keymap["accessibility"] = ["A"]
    config.keymap["rollforward"] = ["mousedown_5"]
    config.keymap["rollback"] = ["mousedown_4"]
    config.keymap["drag_activate"] = ["mousedown_1"]
    config.keymap["drag_deactivate"] = ["mouseup_1"]
    config.keymap["input_left"] = ["K_LEFT","repeat_K_LEFT"]
    config.keymap["input_right"] = ["K_RIGHT","repeat_K_RIGHT"]
    config.keymap["input_delete"] = ["K_DELETE","repeat_K_DELETE"]
    config.keymap["input_paste"] = ["ctrl_noshift_K_v","meta_noshift_K_v"]
    config.keymap["input_jump_word_left"] = ["osctrl_K_LEFT"]
    config.keymap["input_jump_word_right"] = ["osctrl_K_RIGHT"]
    config.keymap["input_delete_word"] = ["osctrl_K_BACKSPACE"]
    config.keymap["input_home"] = ["K_HOME", "meta_K_LEFT"]
    config.keymap["input_end"] = ["K_END", "meta_K_RIGHT"]
    config.keymap["input_copy"] = ["ctrl_noshift_K_INSERT","ctrl_noshift_K_c","meta_noshift_K_c"]
    config.keymap["screenshot"] = ["K_F12"]
    config.keymap["dismiss"] = ["mouseup_1","K_RETURN","K_SPACE","K_KP_ENTER"]
    config.keymap["help"] = ["K_F1"]
    config.keymap["reload_game"] = ["R", "alt_shift_K_r", "shift_K_r"]
    config.keymap["game_menu"] = ["K_ESCAPE","K_MENU","K_PAUSE","mouseup_3"]
    config.keymap["console"] = ["K_BACKQUOTE", "alt_K_c", "shift_K_o"]
    config.keymap["toggle_fullscreen"] = ["alt_K_RETURN","K_F11"]
    config.keymap["button_select"] = ["mouseup_1","K_RETURN","K_KP_ENTER"]
    config.keymap["bar_activate"] = ["mousedown_1","K_RETURN"]
    config.keymap["bar_deactivate"] = ["mouseup_1","K_RETURN"]
    config.keymap["input_backspace"] = ["K_BACKSPACE","repeat_K_BACKSPACE"]
    config.keymap["input_enter"] = ["K_RETURN","K_KP_ENTER"]
    config.keymap["viewport_wheelup"] = ["mousedown_4"]
    config.keymap["viewport_wheeldown"] = ["mousedown_5"]
    config.keymap["viewport_drag_start"] = ["mousedown_1"]
    config.keymap["viewport_drag_end"] = ["mouseup_1"]
    config.keymap["focus_left"] = ["K_LEFT", "repeat_K_UP"]
    config.keymap["focus_right"] = ["K_RIGHT", "repeat_K_RIGHT"]
    config.keymap["focus_up"] = ["K_UP", "repeat_K_UP"]
    config.keymap["focus_down"] = ["K_DOWN", "repeat_K_DOWN"]
    config.keymap["bar_left"] = ["K_LEFT", "repeat_K_LEFT"]
    config.keymap["bar_right"] = ["K_RIGHT", "repeat_K_RIGHT"]
    config.keymap["bar_up"] = ["K_UP", "repeat_K_UP"]
    config.keymap["bar_down"] = ["K_DOWN", "repeat_K_DOWN"]
    config.keymap["viewport_pageup"] = ["K_PAGEUP","repeat_K_PAGEUP"]
    config.keymap["viewport_pagedown"] = ["K_PAGEDOWN","repeat_K_PAGEDOWN"]
    config.keymap["viewport_up"] = ["mousedown_4"]
    config.keymap["viewport_down"] = ["mousedown_5"]
    config.keymap["button_alternate"] = ["mouseup_3"]
    config.keymap["button_alternate_ignore"] = ["mousedown_3"]

    ### NATIVE THAT MIGHT COME IN HANDY
    config.keymap["button_ignore"] = None
    config.keymap["input_up"] = None
    config.keymap["input_down"] = None
    config.keymap["viewport_leftarrow"] = None
    config.keymap["viewport_rightarrow"] = None
    config.keymap["viewport_downarrow"] = None
    config.keymap["viewport_uparrow"] = None
    config.keymap["toggle_music"] = None
    config.keymap["profile_once"] = None
    config.keymap["memory_profile"] = None

    ### NATIVE CLEANUP
    config.keymap["toggle_afm"] = None
    config.keymap["clipboard_voicing"] = None
    config.keymap["debug_voicing"] = None
    config.keymap["stop_skipping"] = None
    config.keymap["director"] = None
    config.keymap["launch_editor"] = None
    config.keymap["dump_styles"] = None
    #config.keymap["inspector"] = None    
    config.keymap["quit"] = None # alt+f4 still works btw
    config.keymap["progress_screen"] = None
    config.keymap["dismiss_unfocused"] = None
    config.keymap["dismiss_hard_pause"] = None

    # following section cleans up conf.keymap of None entries
    # and purges default_keymap so there's no unwanted functionality at all
    def keymapOverride():
        keymapOverrideDict = {}
        for k,v in config.keymap.items():
            if v == None:
                continue
            keymapOverrideDict[k] = v
        config.keymap = keymapOverrideDict
        for key in config.default_keymap:
            config.default_keymap[key] = None
    
    keymapOverride()