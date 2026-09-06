init python:
    DLC_All = {}
    DLC_All["dlc1_premium_pack"] = {
        "name":_("Premium Supporter Pack + Cheats"),
        "img_path":"images/gui/dlc/dlc1.webp",
        "dlc_location":"dlc/dlc1_supporter_pack",
        "buy_link_steam":"https://store.steampowered.com/app/3404970/Parasite_Black__Premium_Supporter_Pack__Cheats/",
        "buy_link_gog":"https://www.gog.com/game/parasite_black_premium_supporter_pack_cheats",
        "desc":_("Supporter's Premium Pack with a guide, cheat codes and posters"),
    }
    if config.developer == True:
        DLC_All["dlc2_grim_days_manga"] = {
            "name":_("Grim Days Manga Series"),
            "img_path":"images/gui/dlc/dlc2.webp",
            "dlc_location":"dlc/dlc2_grim_days_manga",
            "buy_link_steam":None,
            "buy_link_gog":"https://www.gog.com/game/parasite_black_grim_days_manga_series",
            "desc":_("Follow Renia Lupinegar's descent into madness on a vengeful quest to reclaim what was lost... At the expense of everyone else."),
        }

    # a set of active dlc IDs
    DLC_Active = set()

init python:
    import pathlib

    def _to_file_uri(path):
        if not path:
            return None
        try:
            return pathlib.Path(path).resolve().as_uri()
        except Exception:
            return None

    def PlayerHasDLC(DLCID):
        return DLCID in store.DLC_Active

screen main_menu_dlcs():
    tag menu
    modal True
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    add "images/gui/unsorted/black_under.webp"
    label _("Downloadable Content") style "menu_header"
    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_spacing 10
        xsize 1200
        ysize 750
        align (0.5, 0.5)
        vbox:
            xalign 0.5
            spacing 10
            for DLC_ID, DLC_Data in DLC_All.items():
                fixed:
                    fit_first True
                    button:
                        padding (18, 18)
                        hbox:
                            xfill True
                            spacing 20
                            add DLC_Data["img_path"] align (0.5, 0.5) zoom 0.3    
                            vbox:
                                xalign 0.0
                                xfill True
                                spacing 8
                                text tra(DLC_Data["name"]):
                                    style "label_text"
                                    xanchor 0.0
                                text tra(DLC_Data["desc"])
                        if PlayerHasDLC(DLC_ID):
                            if _to_file_uri(config.gamedir + "/" + DLC_Data["dlc_location"]):
                                hovered TooltipSetUI(_("Click to open DLC folder"))
                                action OpenURL(config.gamedir + "/" + DLC_Data["dlc_location"])
                        else:
                            hovered TooltipSetUI(_("Click to open store page"))
                            if Build_Kind == "steam":    
                                action OpenURL(DLC_Data["buy_link_steam"])
                            elif Build_Kind == "gog":
                                action OpenURL(DLC_Data["buy_link_gog"])
                        
                        unhovered TooltipClearUI()
                    if PlayerHasDLC(DLC_ID):
                        add "images/gui/dlc/owned.webp" align (1.0, 1.0)

    textbutton _("Return"):
        style "menu_return"
        action ShowMenu("main_menu")
        default_focus True
        if main_menu:
            keysym "K_ESCAPE"

