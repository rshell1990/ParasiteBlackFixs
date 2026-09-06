translate ja style default:
    font "tl/ja/font_standard.ttf"
    color "#fdf2f0"
    # you can set this to any integer value, like 30 or w/e
    size (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE)

translate ja style label_text:
    font "tl/ja/font_label.ttf"
    color "#f59a84"
    # or you can add/subtract even.
    # (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE) -10 should work
    size (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE)

################# prologue letter ############
translate ja style prologue_letter_label_text is label_text:
    font "tl/ja/font_label.ttf"
    color "#1b1414ff"

translate ja style prologue_letter_text is text:
    font "tl/ja/font_standard.ttf"
    color "#1b1414ff"