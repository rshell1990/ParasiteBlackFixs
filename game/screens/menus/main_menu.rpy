screen main_menu():
    tag menu
    modal True

    on "show" action TooltipClearUI()
    on "hide" action TooltipClearUI()

    if main_menu:
        add gui.main_menu_background
        if Build_Kind == "steam":
            use satyr_main_menu()
    else:
        add gui.game_menu_background

    if DEV_VARIABLES["MAIN_MENU_OPTS"] and main_menu:
        vbox:
            align (0.1,0.9)
            text "Dev mode"
            textbutton "(q) Quickstart" hovered TooltipSetUI("label: dev_quickstart") action Start("dev_quickstart") keysym "K_q"
            textbutton "(a) Quickstart (post-prologue)" hovered TooltipSetUI("label: dev_quickstart_postprologue") action Start("dev_quickstart_postprologue") keysym "K_a"
            textbutton "(w) Quickstart (Hamun, act 2 start)" hovered TooltipSetUI("label: dev_quickstart_hamun") action Start("dev_quickstart_hamun") keysym "K_w"
            textbutton "(d) Devroom" action Start("devroom") keysym "K_d"
    
    if Build_Kind == "nosteam":
        use socmedia()
    use display_version()
    vbox:
        style_prefix "main_menu"
        align (0.5,0.95)
        spacing 5
        if not main_menu:
            textbutton _("Return"):
                action Return()
                default_focus True
        if main_menu:
            textbutton _("New Game"):
                action Start()
                default_focus True
            textbutton _("Load") action ShowMenu("save_load")
        else:
            if IsPlayerInGalleryScene() == False:
                textbutton _("Save Menu") action ShowMenu("save_load")
        textbutton _("Options") action ShowMenu("options")
        if Build_Kind == "steam" or Build_Kind == "gog" or config.developer:
            textbutton _("DLC") action ShowMenu("main_menu_dlcs")
        if main_menu:
            textbutton _("Credits") action ShowMenu("credits")
        else:
            textbutton _("Main Menu") action MainMenu()
        if not renpy.variant("web"):
            textbutton _("Quit") action config.quit_action
    if Build_Kind == "nosteam":
        use steam_window()
    use satyrlauncher()
screen socmedia():
    vbox:
        spacing 20
        anchor (0.0, 0.0)
        pos (0.02, 0.02)
        imagebutton:
            idle Transform("images/gui/logos/discord.webp", matrixcolor = OpacityMatrix(0.5) * SaturationMatrix(0.5))
            hover "images/gui/logos/discord.webp"
            action OpenURL("https://discord.gg/cApAfqUdWK")
        imagebutton:
            idle Transform("images/gui/logos/subscribestar.webp", matrixcolor = OpacityMatrix(0.5) * SaturationMatrix(0.5))
            hover "images/gui/logos/subscribestar.webp"
            action OpenURL("https://subscribestar.adult/damned-studios")

screen display_version():
    if config.developer:
        if Build_Kind == "steam":
            text "DEVELOPMENT BUILD [config.version] (STEAM)":
                align (0.01, 1.0)
        elif Build_Kind == "gog":
            text "DEVELOPMENT BUILD [config.version] (GOG)":
                align (0.01, 1.0)
        else:
            text "DEVELOPMENT BUILD [config.version]":
                align (0.01, 1.0)
    else:
        if Build_Kind == "steam":
            text "EARLY ACCESS BUILD [config.version], [configBuildDate] (STEAM)":
                align (0.01, 1.0)
        elif Build_Kind == "gog":
            text "EARLY ACCESS BUILD [config.version], [configBuildDate] (GOG)":
                align (0.01, 1.0)
        else:
            text "EARLY ACCESS BUILD [config.version], [configBuildDate]":
                align (0.01, 1.0)