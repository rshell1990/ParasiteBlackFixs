style frame: # default frame
    background Frame("images/gui/frames/frame1.webp", Borders(12, 12, 12, 12))
    padding (10, 10)

############# bars and sliders ################
style slider: # default h-slider
    ysize 40
    base_bar Frame("images/gui/sliders/horizontal_[prefix_]bar.webp", borders = (6, 6, 6, 6))
    thumb "images/gui/sliders/horizontal_[prefix_]thumb.webp"
    mouse "hover"
    #hover_sound "audio/interface/sound_hover.ogg"
    activate_sound "audio/interface/sound_click.ogg"

style scrollbar: # default h-scrollbar
    ysize 18
    base_bar Frame("images/gui/scrollbars/horizontal_[prefix_]bar.webp", borders =(6, 6, 6, 6))
    thumb Frame("images/gui/scrollbars/horizontal_[prefix_]thumb.webp",  borders =(6, 6, 6, 6))
    mouse "hover"
    unscrollable "hide"

style vscrollbar: # default v-scrollbar
    xsize 18
    base_bar Frame("images/gui/scrollbars/vertical_[prefix_]bar.webp", borders = (6, 6, 6, 6))
    thumb Frame("images/gui/scrollbars/vertical_[prefix_]thumb.webp",  borders = (6, 6, 6, 6))
    mouse "hover"
    unscrollable "hide"

style bar_red_256:
    xsize 256
    ysize 25
    left_bar Frame("images/gui/bars/bar2_fill_red.webp")
    right_bar Frame("images/gui/bars/bar2_under_red.webp")

style bar_green_256 is bar_red_256:
    left_bar Frame("images/gui/bars/bar2_fill_green.webp")
    right_bar Frame("images/gui/bars/bar2_under_green.webp")

style bar_brgreen_256 is bar_red_256:
    left_bar Frame("images/gui/bars/bar2_fill_brgreen.webp")
    right_bar Frame("images/gui/bars/bar2_under_brgreen.webp")

style bar_blue_256 is bar_red_256:
    left_bar Frame("images/gui/bars/bar2_fill_blue.webp")
    right_bar Frame("images/gui/bars/bar2_under_blue.webp")

style bar_teal_256 is bar_red_256:
    ysize 20
    left_bar Frame("images/gui/bars/bar2_fill_teal.webp")
    right_bar Frame("images/gui/bars/bar2_under_teal.webp")
############### root text styles ##########

default persistent.large_font = False

define NORMAL_TEXT_SIZE = 30
define LARGE_TEXT_SIZE = 40
define NORMAL_LABEL_TEXT_SIZE = 40
define LARGE_LABEL_TEXT_SIZE = 50

style default:
    font "en_fonts/gentium.ttf"
    color "#fdf2f0"
    size (LARGE_TEXT_SIZE if persistent.large_font else NORMAL_TEXT_SIZE)

style text is default



style label_text:
    font "en_fonts/algerian.ttf"
    color "#f59a84"
    size (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE)

init 999 python:
    def _refresh_font():
        style.text.size = (LARGE_TEXT_SIZE if persistent.large_font else NORMAL_TEXT_SIZE)
        style.label_text.size = (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE)
        return



################# root buttons ##############
style button:
    idle_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24,24,24,24)),matrixcolor=OpacityMatrix(0.45))
    hover_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24,24,24,24)),matrixcolor=IdentityMatrix())
    insensitive_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24,24,24,24)),matrixcolor=OpacityMatrix(0.45) * BrightnessMatrix(-0.1))

    #hover_sound "audio/interface/sound_hover.ogg"
    activate_sound "audio/interface/sound_click.ogg"
    mouse "hover"

    padding (12, 0)
    minimum (48, 48)

style button_text is text:
    yalign 0.5
    color "#fcc2b0"
    hover_color "#ff7d55"
    insensitive_color "#6d5555"
    outlines [ (2, "#1b1414ff", 0, 0) ]
    outline_scaling "step"

style image_button:
    #hover_sound "audio/interface/sound_hover.ogg"
    activate_sound "audio/interface/sound_click.ogg"
    mouse "hover"

style button_sneaky: # if ya want a textbutton that looks like plain text
    #hover_sound "audio/interface/sound_hover.ogg"
    activate_sound "audio/interface/sound_click.ogg"
    mouse "hover"

style button_sneaky_text is text:
    yalign 0.5

# shows "selected" state (glow if true) cant be used on a generic button, weird shit happens sometimes
style button_sel is button: 
    selected_idle_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24,24,24,24)),matrixcolor=TintMatrix((255,120,70))*BrightnessMatrix(0.2)*OpacityMatrix(0.9))
    selected_hover_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24,24,24,24)),matrixcolor=TintMatrix((255,120,70))*BrightnessMatrix(0.3))
style button_sel_text is button_text

# used by characters screen
style button_tab is button_sel: # fixed xsize, experimental
    xsize 350
    xalign 0.5
style button_tab_text is button_text:
    xalign 0.5

################# main menu #################
style main_menu_button: # nav buttons
    xalign 0.5
    padding (18,6)
style main_menu_button_text is label_text: # nav buttons
    yalign 0.5
    hover_color "#ff7d55"
    insensitive_color "#413636"
    outlines [ (2, "#1b1414ff", 0, 0) ]
    outline_scaling "step"

################# say window #################
style say_dialogue is text
style say_thought is text # empty "who" case
style say_label_text is label_text

################# choice menu #################
style choice_label_text is say_label_text
style choice_dialogue is say_dialogue
style choice_button is button:
    idle_background         Transform(Frame("images/gui/frames/frame3.webp", Borders(22, 22, 22, 22)), matrixcolor = IdentityMatrix())
    hover_background        Transform(Frame("images/gui/frames/frame3.webp", Borders(22, 22, 22, 22)), matrixcolor = MxMapHover())
    insensitive_background  Transform(Frame("images/gui/frames/frame3.webp", Borders(22, 22, 22, 22)), matrixcolor = OpacityMatrix(0.75))
    padding (15, 7)
style choice_button_text is button_text:
    text_align 0.5
    insensitive_color "#796363"

# for "already clicked" choice buttons
style choice_button_seen is choice_button
style choice_button_seen_text is choice_button_text:
    color "#cab7a7"
    hover_color "#ff7d55"
    insensitive_color "#555555"
    outlines [ (2, "#1b1414ff", 0, 0) ]
    outline_scaling "step"
################# options #################
style pref_cat_header:
    xalign 0.5
style pref_cat_header_text is label_text
##
style pref_slider:
    xfill True
##
style pref_button is button:
    xfill True
    xalign 0.5
style pref_button_text is button_text:
    align (0.5, 0.5)
##
style pref_toggle is button:
    xalign 0.5
    xfill True
    selected_idle_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24, 24, 24, 24)), matrixcolor = TintMatrix((255, 120, 70)) * BrightnessMatrix(0.2) * OpacityMatrix(0.9))
    selected_hover_background Transform(Frame("images/gui/frames/frame5.webp", Borders(24, 24, 24, 24)), matrixcolor = TintMatrix((255, 120, 70)) * BrightnessMatrix(0.3))
style pref_toggle_text is button_text:
    align (0.5,0.5)
##
style pref_vbox:
    xsize 400
################# journal #################
style quest_tab is pref_toggle:
    xfill False
style quest_tab_text is pref_toggle_text
style quest_entry is pref_toggle
style quest_entry_text is pref_toggle_text
style quest_stage_active is default:
    color "#f59a84"
    size 35
style quest_stage_completed is default:
    color "#967770"
################# inventory #################
style inv_itemSlot_qtyText is text: # item quantity text
    size 25
    xalign 1.0
    yalign 1.0
    xoffset -3
    yoffset -3

################# credits #################
style credits_label:
    xalign 1.0
style credits_label_text is label_text:
    size 30
style credits_text is text

################# confirm/popup #################
style confirm_button is main_menu_button
style confirm_button_text is main_menu_button_text

################# save/load #################
style save_button is pref_button:
    xsize 133
style save_button_text is pref_button_text

style save_page_button is pref_toggle:
    xfill False
style save_page_button_text is pref_toggle_text

################# prologue letter ############
style prologue_letter_label_text is label_text:
    font "en_fonts/handwritten_fancy.ttf"
    color "#1b1414ff"
style prologue_letter_text is text:
    font "en_fonts/handwritten_fancy.ttf"
    color "#1b1414ff"
################# world map #################
style wmap_loc_name_big_text is text:
    align (0.5,0.5)
    size 56
    color "#f1c2b6"
    outlines [ (3, "#1b1414ff", 0, 0) ]
    outline_scaling "step"
style wmap_loc_name_med_text is wmap_loc_name_big_text:
    outlines [ (2, "#1b1414ff", 0, 0) ]
    size 44
    #color "#f1dad3"
style wmap_loc_name_small_text is wmap_loc_name_med_text:
    size 32
    #color "#f1dad3"
style wmap_feature_label_text is label_text:
    align (0.5,0.50)
    size 50
    outlines [ (2, "#1b1414ff", 0, 0) ]
################ books ###################
style book_title_page is label_text:
    color "#161616"
    xalign 0.5
    yalign 0.4
    text_align 0.5

style book_text is default:
    size 27
############### steam-window-only ######
style frame_trans is frame: # seethru
    background Frame(Transform("images/gui/frames/frame1.webp", matrixcolor = OpacityMatrix(0.65)), Borders(12, 12, 12, 12))
    #padding (10,10)

################# shared by multiple #################
style frame_outer: # outside frame of ingame screens & confirm/cheat popups
    background Frame("images/gui/frames/frame2.webp", Borders(180, 180, 180, 180))
    padding (95, 95)
style frame_outer_smaller: # outside frame of ingame screens & confirm/cheat popups, smaller variant
    background Frame(Transform("images/gui/frames/frame2_smaller.webp", matrixcolor = OpacityMatrix(0.9)), Borders(150, 150, 150, 150))
    padding (72, 72)
##
style menu_header_text is label_text: # used by menu tabs such as "save", "options"
    size 80
style menu_header:
    align (0.5,0.02)
##
style menu_return is main_menu_button:
    align (0.5,0.95)
style menu_return_text is main_menu_button_text

###### dev-tools styles
style devmode_text is default:
    size 25

style devmode_label_text is default:
    size 34

style devmode_button is button:
    xalign 0.0
    background "frame_dev_idle"
    insensitive_background "frame_dev_insen"
    hover_background "frame_dev_hover"
    selected_background "frame_dev_sel"
    padding (3, 0)
    minimum (32, 32)

style devmode_button_text is button_text:
    xalign 0.5
    size 25
    color (255, 225, 225)
    hover_color (255, 150, 0)

style devmode_frame is frame:
    background "frame_dev_alpha"

image frame_dev_insen = Frame("images/gui/frames_dev/insen.webp", Borders(8, 8, 8, 8))
image frame_dev_alpha = Frame("images/gui/frames_dev/alpha.webp", Borders(8, 8, 8, 8))
image frame_dev_idle = Frame("images/gui/frames_dev/idle.webp", Borders(8, 8, 8, 8))
image frame_dev_hover = Frame("images/gui/frames_dev/hover.webp", Borders(8, 8, 8, 8))
image frame_dev_sel = Frame("images/gui/frames_dev/sel.webp", Borders(8, 8, 8, 8))

style devtab_button is button:
    xpadding 50
    selected_idle_background    Transform(Frame("images/gui/frames/frame5.webp", Borders(22, 22, 22, 22)), matrixcolor = TintMatrix((255, 120, 70)) * BrightnessMatrix(0.2) * OpacityMatrix(0.9))
    selected_hover_background   Transform(Frame("images/gui/frames/frame5.webp", Borders(22, 22, 22, 22)), matrixcolor = TintMatrix((255, 120, 70)) * BrightnessMatrix(0.3))



################# more text styles (for locale) ##############
style battle_itemskills_button is button
style battle_itemskills_button_text is button_text:
    size 40

style quest_board_desc_text is default:
    size 30
style quest_board_title_text is default:
    size 40

style prologue_letter_title is label
style prologue_letter_title_text is prologue_letter_label_text:
    size 100

style prologue_letter_text_main is prologue_letter_text:
    size 41

style prologue_letter_text_sub is prologue_letter_text:
    size 29

### for babazhul gallery stuff
style babazhul_mad_text is default:
    font "en_fonts/tegomin.ttf"