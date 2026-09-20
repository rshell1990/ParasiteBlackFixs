transform show_hide_dissolve:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.25 alpha .0

screen book(book_dict):
    modal True

    on "show" action Play("sound", renpy.random.choice(soundLib["flip_pages"]))
    default paged_text = GetPageList(book_dict) # a list of [page,page,page]

    default page = 0 # inc by 2: 0-2-4-6-8-10

    if (len(paged_text) % 2) == 0:
        default max_page = len(paged_text) + 2
        default last_page_empty = True
    else:
        default max_page = len(paged_text) + 1
        default last_page_empty = False
    #default max_page = len(paged_text) # here we must get 2-4-6 even num
    add "images/gui/unsorted/black_under.webp":
        at show_hide_dissolve
        matrixcolor OpacityMatrix(0.8)
    frame:
        at show_hide_dissolve
        xysize (1250, 840)
        align (0.5, 0.4)
        hbox:
            xfill True
            # left page
            frame:
                xoffset 2
                background Frame("images/gui/frames/paper.webp", Borders(0, 0, 0, 0))
                padding (55, 55)
                xysize (615, 820)

                if page >= 4:
                    text paged_text[page - 3]:
                        color "#161616"
                        style "book_text"

                    text str(page - 2):
                        align (0.0, 1.03)
                        color "#161616"
                        size 35

            # right page
            frame:
                xoffset -2
                background Frame("images/gui/frames/paper.webp", Borders(0, 0, 0, 0))
                padding (55, 55)
                xysize (615, 820)
                xalign 1.0
                if page == 0:
                    text book_dict["title_page"]:
                        style "book_title_page"
                
                if page == 2:
                    text paged_text[0]:
                        color "#161616"
                        style "book_text"

                if 4 <= page: # 4-6-8-10 I don't even know what I'm doing anymore
                    if page == max_page:
                        if not last_page_empty:
                            text paged_text[page - 2]: # 0-2-4-6-8
                                color "#161616"
                                style "book_text"
                    else:
                        text paged_text[page - 2]: # 0-2-4-6-8
                            color "#161616"
                            style "book_text"
                
                if page >= 2:
                    if page == max_page:
                        if not last_page_empty:
                            text str(page - 1):
                                align (1.0, 1.03)
                                color "#161616"
                                size 35
                    else:
                        text str(page - 1):
                            align (1.0, 1.03)
                            color "#161616"
                            size 35

    hbox:
        align (0.5, 0.91)
        spacing 20
        textbutton tra(_("(%s) Prev. page")) % GetHotkeyStr("nav_left", Parens = False, Space = False):
            if page > 1:
                action [SetLocalVariable("page", page - 2), Play("sound", renpy.random.choice(soundLib["flip_pages"]))]
            keysym config.keymap["nav_left"]
        textbutton tra(_("(%s) Close")) % GetHotkeyStr("nav_down", Parens = False, Space = False):
            action [Hide("book"), Play("sound", "audio/items/book/close.ogg")]
            keysym config.keymap["nav_down"]
        textbutton tra(_("(%s) Next page")) % GetHotkeyStr("nav_right", Parens = False, Space = False):
            if page < max_page:
                action [SetLocalVariable("page", page + 2), Play("sound", renpy.random.choice(soundLib["flip_pages"]))]
            keysym config.keymap["nav_right"]

init -1 python:
    def ItemOpenBook(ItemID, char_ID, book_dict):
        renpy.show_screen("book", book_dict)
        return
    
    # splits text by symbols-per-page + first occuring space
    def GetPageList(book_dict): 
        # adding one space so that non-translated books dont crash
        remaining_text = tra(book_dict["full_text"]) + " " 
        return_page_list = []
        symbols_per_page = 765
        bail = False
        while True:
            BoldTagOpen = False
            ItalicsTagOpen = False
            SizeTag = None

            if len(remaining_text) == 0:
                break

            slice_at = symbols_per_page
            if len(remaining_text) <= slice_at:
                return_page_list.append(remaining_text)
                break

            while remaining_text[slice_at] != " ":
                slice_at += 1
                if len(remaining_text) <= slice_at:
                    remaining_text = "{b}" + remaining_text
                    remaining_text = "{i}" + remaining_text
                    return_page_list.append(remaining_text)
                    bail = True
                    break
            if bail:
                break

            page_text = remaining_text[:slice_at]

            ParsingCursor = 0

            max_pos = len(page_text)
            while ParsingCursor < max_pos:
                rest = page_text[ParsingCursor:]
                if rest.startswith("{b}"):
                    BoldTagOpen = True
                    ParsingCursor += 3
                    continue
                elif rest.startswith("{/b}"):
                    BoldTagOpen = False
                    ParsingCursor += 4
                    continue
                elif rest.startswith("{i}"):
                    ItalicsTagOpen = True
                    ParsingCursor += 3
                    continue
                elif rest.startswith("{/i}"):
                    ItalicsTagOpen = False
                    ParsingCursor += 4
                    continue
                elif rest.startswith("{size="):
                    value, NextCursorPos = BookUI_BookGrabValueBeforeClosingCurly(page_text, ParsingCursor + 5)
                    SizeTag = value
                    # the outer loop will ++ it
                    ParsingCursor = NextCursorPos
                    continue
                elif rest.startswith("{/size}"):
                    SizeTag = None
                    ParsingCursor += 7
                    continue
                # nothing matched – advance by one char
                ParsingCursor += 1

            if BoldTagOpen:
                page_text = page_text + "{/b}"
            if ItalicsTagOpen:
                page_text = page_text + "{/i}"
            if SizeTag is not None:
                page_text = page_text + "{/size}"
            
            return_page_list.append(page_text)
            remaining_text = remaining_text[slice_at:]
            
            if BoldTagOpen:
                remaining_text = "{b}" + remaining_text
            if ItalicsTagOpen:
                remaining_text = "{i}" + remaining_text
            if SizeTag is not None:
                remaining_text = "{size=" + str(SizeTag) + "}" + remaining_text

        return return_page_list

    def BookUI_BookGrabValueBeforeClosingCurly(text, start):
        i = start + 1
        Buffer = []
        while i < len(text) and text[i] != '}':
            Buffer.append(text[i])
            i += 1
        ReturnVal = ''.join(Buffer)
        try:
            return int(ReturnVal), i + 1          # +1 to skip the closing '}'
        except ValueError:
            return 0, i + 1                 # fallback if somebody wrote garbage