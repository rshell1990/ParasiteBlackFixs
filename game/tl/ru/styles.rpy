translate ru style default:
    font "tl/ru/font_standard.ttf"
    color "#fdf2f0"
    # you can set this to any integer value, like 30 or w/e
    size (LARGE_TEXT_SIZE if persistent.large_font else NORMAL_TEXT_SIZE) -5# - 20

translate ru style book_text is default:
    size 22

translate ru style battle_itemskills_button_text is button_text:
    size 26

translate ru style quest_board_desc_text is default:
    size 22
translate ru style quest_board_title_text is default:
    size 27
translate ru style prologue_letter_title_text is prologue_letter_label_text:
    size 80
translate ru style prologue_letter_text_main is prologue_letter_text:
    size 30
translate ru style prologue_letter_text_sub is prologue_letter_text:
    size 20



translate ru style label_text:
    font "tl/ru/font_label.ttf"
    color "#f59a84"
    # or you can add/subtract even.
    # (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE) -10 should work
    size (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE) -5# - 20

################# prologue letter ############
translate ru style prologue_letter_label_text is label_text:
    font "tl/ru/font_label.ttf"
    color "#1b1414ff"

translate ru style prologue_letter_text is text:
    font "tl/ru/font_standard.ttf"
    color "#1b1414ff"

########## babazhul
translate ru style babazhul_mad_text is default:
    font "tl/ru/font_standard.ttf"