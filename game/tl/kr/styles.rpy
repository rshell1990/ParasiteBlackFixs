translate kr style default:
    font "tl/kr/font_standard.ttf"
    color "#fdf2f0"
    size (LARGE_TEXT_SIZE if persistent.large_font else NORMAL_TEXT_SIZE)

translate kr style label_text:
    font "tl/kr/font_label.ttf"
    color "#f59a84"
    size (LARGE_LABEL_TEXT_SIZE if persistent.large_font else NORMAL_LABEL_TEXT_SIZE)

translate kr style prologue_letter_label_text is label_text:
    font "tl/kr/font_label.ttf"
    color "#1b1414ff"

translate kr style prologue_letter_text is text:
    font "tl/kr/font_standard.ttf"
    color "#1b1414ff"
