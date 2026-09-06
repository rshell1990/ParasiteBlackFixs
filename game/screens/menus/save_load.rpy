
screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "save_name"

    add "images/gui/unsorted/black_under.webp"

    frame:
        style "frame_outer"
        align (0.5, 0.5)
        xminimum 700

        has vbox:
            spacing 20
            xalign 0.5

        if FileLoadable(slot):
            label _("SAVE NAME ({color=#f00}overwrite{/color})") xalign 0.5
        else:
            label _("SAVE NAME ({color=#d95411}new{/color})") xalign 0.5

        input:
            value VariableInputValue("save_name")
            length 40
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 75

            textbutton _("ACCEPT"):
                keysym [ "K_RETURN", "K_KP_ENTER" ]
                action [ FileAction(slot, confirm = False), SetVariable("save_name", ""), Hide("screen_save_name") ]

            textbutton _("CANCEL"):
                keysym "game_menu"
                action [ SetVariable("save_name", ""), Hide("screen_save_name") ]


screen save_load(HideOnReturnBtn = False, BlockSave = False):
    tag menu
    modal True

    default PageInputMode = False
    default ManualPage = "1"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    add "images/gui/unsorted/black_under.webp"
    label _("Save Menu") style "menu_header"

    
    vbox:
        align (0.5, 0.54)
        spacing 15
        grid 4 2:
            align (0.5, 0.5)
            spacing 15
            for i in range(8):
                $ slot = i + 1
                button:
                    #maximum (400,300)
                    vbox:
                        spacing 3
                        null height 10
                        fixed:
                            align (0.5, 0.5)
                            maximum (config.thumbnail_width, config.thumbnail_height)
                            add FileScreenshot(slot):
                                align (0.5, 0.5)
                                size (config.thumbnail_width, config.thumbnail_height)
                            add "images/gui/blank.webp":
                                align (0.5, 0.5)
                                size (config.thumbnail_width, config.thumbnail_height)
                        frame:
                            style "empty"
                            ysize 30
                            xalign 0.5
                            add Text(FileSaveName(slot).replace("[","[[").replace("{","{{")):
                                align (0.5, 0.5)
                                zoom (370.0 / max(370.0, Text(FileSaveName(slot).replace("[","[[").replace("{","{{")).size()[0]))
                        text FileTime(slot, format=_("{#file_time}%c")):
                            xalign 0.5
                            size 25
                            color "#ffffff80" 
                            #if persistent.save_naming and FilePageName() not in ("a","q"):
                            #    color "#ffffff80" 

                        hbox:
                            textbutton _("Save"):
                                style "save_button"
                                sensitive not (BlockSave or _in_replay or main_menu or FilePageName() == "a" or IsPlayerInBattle() or IsPlayerInBaratiGame() or IsPlayerInGalleryScene())
                                if persistent.save_naming:
                                    action [SetVariable("save_name", FileSaveName(slot)), Show("screen_save_name", slot = slot)]
                                else:
                                    action FileAction(slot, confirm = True)
                            textbutton _("Load"):
                                style "save_button"
                                action FileLoad(slot)
                            textbutton _("Delete"):
                                style "save_button"
                                action FileDelete(slot)
                                keysym "save_delete"
                        null height 10
        null height 10
        hbox:
            xalign 0.7
            textbutton "<":
                style "save_page_button"
                action FilePagePrevious()
                if PageInputMode == False:
                    keysym "K_s"
            textbutton _("{#auto_page}Auto"):
                style "save_page_button"
                action FilePage("auto")
                if PageInputMode == False:
                    keysym "K_a"
            textbutton _("{#quick_page}Quick"):
                style "save_page_button"
                action FilePage("quick")
                if PageInputMode == False:
                    keysym "K_q"
            for page in range(1, 9):
                textbutton "[page]":
                    style "save_page_button"
                    action FilePage(page)
                    if PageInputMode == False:
                        keysym str(page)

            textbutton ">":
                style "save_page_button"
                action FilePageNext()
                if PageInputMode == False:
                    keysym "K_w"
            null width 30
            fixed:
                yalign 0.5
                xsize 300
                ysize 1
                hbox:
                    yalign 0.5
                    textbutton _("(j) Jump to"):
                        yalign 0.5
                        action SetLocalVariable("PageInputMode", True)
                        keysym ["K_j"]
                    if PageInputMode == True:
                        fixed:
                            yalign 0.5
                            xsize 80
                            ysize 1
                            input:
                                xanchor 0.0
                                xpos 0.1
                                yalign 0.5
                                allow "0123456789"
                                length 1
                                value LocalVariableInputValue("ManualPage")
                        if len(ManualPage) > 0 and ManualPage != "0":
                            textbutton _("Confirm"):
                                yalign (0.5)
                                xalign 1.0
                                action [FilePage(ManualPage), SetLocalVariable("PageInputMode", False)]
                                keysym ["K_RETURN"]

    frame:
        align (0.5, 0.095)
        ysize 50
        style "empty"
        if FilePageName() != "a":
            if FilePageName() != "q":
                if int(FilePageName()) > 9:
                    text tra(_("Page %s")) % FilePageName()
            else:
                text tra(_("You can quicksave and quickload using F5 and F9 keys."))

    textbutton _("Return"):
        style "menu_return"
        yoffset 10
        if HideOnReturnBtn:
            action [Hide("save_load"), Return()]
        else:
            action ShowMenu("main_menu")
        if main_menu:
            keysym "K_ESCAPE"
        default_focus True
