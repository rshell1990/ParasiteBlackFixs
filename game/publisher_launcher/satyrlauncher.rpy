define satyrlauncher_screen_size = str(config.screen_width) + "x" + str(config.screen_height)
default has_internet = None
default launcher_cover_items = []
default launcher_feed_loading = False
default launcher_feed_error = None
default launcher_thumb_xpos = -config.screen_width * 7 // 8 - 50
default launcher_thumb_txpos = -config.screen_width * 7 // 8 - 50
default launcher_downloads_requested = False
default launcher_show = False
default launcher_show_bg = True
default launcher_cover_selected = 1
#For Steam Build = Set True if Steam Build, otherwise False.
default launcher_steam_build = True

init python:
    import hashlib
    import os
    import socket
    import threading
    import time
    from concurrent.futures import ThreadPoolExecutor

    import requests

    _internet_check_in_progress = False
    _launcher_feed_in_progress = False
    _launcher_feed_url = "https://satyr-launcher-default-rtdb.firebaseio.com/satyr_launcher_games.json"
    _launcher_download_executor = ThreadPoolExecutor(max_workers=8)
    _launcher_asset_states = {}
    _launcher_download_generation = 0
    _launcher_cache_dir = os.path.join(config.gamedir, "publisher_launcher", "cache")
    _launcher_loading_asset = "publisher_launcher/cover/loading.png"
    _launcher_failed_asset = "publisher_launcher/cover/failed.png"

    def _launcher_asset_key(item, field):
        return "{}:{}".format(item.get("title", "item"), field)

    def _launcher_cache_path(item, field, generation):
        asset_key = _launcher_asset_key(item, field)
        digest = hashlib.md5(asset_key.encode("utf-8")).hexdigest()
        return "publisher_launcher/cache/{}_{}_{}.jpg".format(field, digest, generation)

    def _clear_launcher_cache():
        if not os.path.isdir(_launcher_cache_dir):
            return
        for name in os.listdir(_launcher_cache_dir):
            path = os.path.join(_launcher_cache_dir, name)
            if os.path.isfile(path):
                try:
                    os.remove(path)
                except OSError:
                    pass

    def _set_launcher_asset_state(asset_key, state, path=None):
        _launcher_asset_states[asset_key] = {
            "state": state,
            "path": path,
        }

    def _flatten_platforms(value):
        if isinstance(value, dict):
            ordered = []
            for key in sorted(value.keys(), key=lambda k: str(k)):
                ordered.extend(_flatten_platforms(value[key]))
            return ordered
        if isinstance(value, (list, tuple)):
            ordered = []
            for item in value:
                ordered.extend(_flatten_platforms(item))
            return ordered
        if value in (None, ""):
            return []
        text = unicode(value).strip()
        if text.startswith(("(", "[", "{")) and text.endswith((")", "]", "}")) and "," in text:
            parts = []
            for part in text[1:-1].split(","):
                cleaned = part.strip().strip("'\"")
                if cleaned:
                    parts.append(cleaned)
            if parts:
                return parts
        return [text.strip("'\"")]

    def _normalize_launcher_item(raw_item):
        return {
            "title": raw_item.get("title", "Untitled"),
            "developer": raw_item.get("developer", ""),
            "image": raw_item.get("image", ""),
            "cover": raw_item.get("cover", ""),
            "about": raw_item.get("about", ""),
            "wishlist": raw_item.get("wishlist", ""),
            "patreon": raw_item.get("patreon", ""),
            "platforms": _flatten_platforms(raw_item.get("platforms", [])),
        }

    def _finish_launcher_feed_load(items, error=None):
        global _launcher_feed_in_progress
        store.launcher_cover_items = items
        store.launcher_feed_loading = False
        store.launcher_feed_error = error
        _launcher_feed_in_progress = False
        renpy.restart_interaction()

    def _load_launcher_feed_worker():
        items = []
        error = None

        try:
            response = requests.get(_launcher_feed_url, timeout=(5, 20))
            response.raise_for_status()
            payload = response.json() or {}
            if "satyr_launcher_games" in payload and isinstance(payload["satyr_launcher_games"], dict):
                payload = payload["satyr_launcher_games"]
            for key in sorted(payload.keys()):
                raw_item = payload.get(key) or {}
                item = _normalize_launcher_item(raw_item)
                if item["title"] and item["image"] and item["cover"]:
                    items.append(item)
            if not items:
                error = "empty"
        except Exception:
            error = "failed"

        renpy.invoke_in_main_thread(_finish_launcher_feed_load, items, error)

    def refresh_launcher_feed_async():
        global _launcher_feed_in_progress

        if _launcher_feed_in_progress:
            return

        _launcher_feed_in_progress = True
        store.launcher_cover_items = []
        store.launcher_feed_loading = True
        store.launcher_feed_error = None
        threading.Thread(target=_load_launcher_feed_worker, daemon=True).start()

    def _finish_launcher_asset_download(asset_key, success, path=None, generation=0):
        if generation != _launcher_download_generation:
            return

        if success:
            _set_launcher_asset_state(asset_key, "ready", path)
        else:
            _set_launcher_asset_state(asset_key, "failed", _launcher_failed_asset)
        renpy.restart_interaction()

    def _download_launcher_asset(item, field, generation):
        asset_key = _launcher_asset_key(item, field)
        rel_path = _launcher_cache_path(item, field, generation)
        abs_path = os.path.join(config.gamedir, rel_path)
        tmp_path = abs_path + ".tmp"

        try:
            response = requests.get(item[field], timeout=(5, 20), stream=True)
            response.raise_for_status()

            with open(tmp_path, "wb") as downloaded_file:
                for chunk in response.iter_content(65536):
                    if chunk:
                        downloaded_file.write(chunk)

            os.replace(tmp_path, abs_path)
            renpy.invoke_in_main_thread(_finish_launcher_asset_download, asset_key, True, rel_path, generation)
        except Exception:
            try:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
            except OSError:
                pass
            renpy.invoke_in_main_thread(_finish_launcher_asset_download, asset_key, False, None, generation)

    def queue_launcher_downloads(items):
        global _launcher_download_generation

        _launcher_download_generation += 1
        generation = _launcher_download_generation
        os.makedirs(_launcher_cache_dir, exist_ok=True)
        _clear_launcher_cache()

        for item in items:
            for field in ("image", "cover"):
                asset_key = _launcher_asset_key(item, field)
                _set_launcher_asset_state(asset_key, "loading", _launcher_loading_asset)
                _launcher_download_executor.submit(_download_launcher_asset, item, field, generation)

    def launcher_asset_path(item, field):
        state = _launcher_asset_states.get(_launcher_asset_key(item, field))
        if state is None:
            return _launcher_loading_asset
        if state["state"] == "ready" and state["path"]:
            return state["path"]
        if state["state"] == "failed":
            return _launcher_failed_asset
        return _launcher_loading_asset

    def _finish_internet_check(result):
        global _internet_check_in_progress
        store.has_internet = result
        _internet_check_in_progress = False
        if result:
            refresh_launcher_feed_async()
        else:
            store.launcher_cover_items = []
            store.launcher_feed_loading = False
            store.launcher_feed_error = "offline"
            renpy.restart_interaction()

    def _check_internet_worker():
        time.sleep(1.0)

        result = False
        conn = None
        try:
            conn = socket.create_connection(("8.8.8.8", 53), timeout=1.5)
            result = True
        except OSError:
            result = False
        finally:
            if conn is not None:
                conn.close()

        renpy.invoke_in_main_thread(_finish_internet_check, result)

    def check_internet_async():
        global _internet_check_in_progress

        if _internet_check_in_progress:
            return

        _internet_check_in_progress = True
        store.has_internet = None
        threading.Thread(target=_check_internet_worker, daemon=True).start()

    def refresh_launcher_session():
        global _launcher_feed_in_progress, _launcher_download_generation

        _launcher_feed_in_progress = False
        _launcher_download_generation += 1
        _launcher_asset_states.clear()
        store.has_internet = None
        store.launcher_cover_items = []
        store.launcher_feed_loading = False
        store.launcher_feed_error = None
        check_internet_async()

screen satyrlauncher():
    default launcher_font = "publisher_launcher/font_english/absans-regular.otf"
    default montserrat_font = "publisher_launcher/font_english/Montserrat/static/Montserrat-Regular.ttf"
    if launcher_thumb_xpos != launcher_thumb_txpos:
        timer 0.01 repeat True action [
            SetVariable(
                "launcher_thumb_xpos",
                launcher_thumb_txpos if abs(launcher_thumb_txpos - launcher_thumb_xpos) <= 1 else int(launcher_thumb_xpos + (launcher_thumb_txpos - launcher_thumb_xpos) * 0.2)
            ),
            If(
                abs(launcher_thumb_txpos - launcher_thumb_xpos) <= 1,
                true=[SetVariable("launcher_thumb_xpos", launcher_thumb_txpos), SetVariable("launcher_show_bg", True)],
            ),
        ]
    elif not launcher_show_bg:
        timer 0.01 action SetVariable("launcher_show_bg", True)

    $ cover_items = launcher_cover_items
    $ content_ready = launcher_show and has_internet == True and not launcher_feed_loading and len(cover_items) > 0
    $ selected_index = min(max(launcher_cover_selected - 1, 0), len(cover_items) - 1) if cover_items else 0

    if not getattr(renpy.variant, 'hide_satyrlauncher', False):
        if content_ready and not launcher_downloads_requested:
            timer 0.01 action [Function(queue_launcher_downloads, cover_items), SetVariable("launcher_downloads_requested", True)]

        frame:
            xysize (config.screen_width * 7 // 8, config.screen_height * 8 // 8)
            yalign 0.5
            xpos launcher_thumb_xpos
            background "#000000e6"
            if launcher_show:
                # Dynamically apply the slide transform only when connection succeeds
                if has_internet == True:
                    add "publisher_launcher/assets/satyrlogo.webp" at logo_checking, logo_slide_to_corner
                else:
                    add "publisher_launcher/assets/satyrlogo.webp" at logo_checking
                
                if has_internet is None:
                    text "Checking connection" style "launcher_status_text" at fade_in_item_main(0.1)
                elif has_internet is False:
                    text "Connection Offline" style "launcher_status_text" at fade_in_item_main(0.1)
                elif launcher_feed_loading:
                    text "Loading launcher content..." style "launcher_status_text" at fade_in_item_main(0.1)
                elif launcher_feed_error:
                    text "Failed to load launcher content." style "launcher_status_text" at fade_in_item_main(0.1)
                if content_ready:
                    viewport:
                        xpos 0.062 ypos 0.23 
                        xsize 350 ysize config.screen_height * 5 // 8
                        draggable True
                        mousewheel True
                        vbox:
                            spacing 40
                            for i, cover in enumerate(cover_items):
                                frame at fade_in_item(i):
                                    background None
                                    ysize 100
                                    button:
                                        background None
                                        xsize 317 ysize 183 xpadding 6 ypadding 6 selected (launcher_cover_selected == i+1)
                                        action [SetVariable("launcher_cover_selected", i+1), SetVariable("launcher_show_bg", False)]
                                        add AlphaMask(Transform(launcher_asset_path(cover, "image"), xoffset=0, yoffset=0, zoom=1.0), Transform("publisher_launcher/cover/overlay.png", size=(960, 310))) xsize 305 fit "contain" at zoom_hover_launcher
                                    text cover["title"] xpos 5 size 20 ypos 100 font launcher_font
                            frame at fade_in_item(i):
                                background None
                                ysize 30

            if content_ready:
                frame at fade_in_item(0.0):
                    xpos 0.26 ypos 0.23
                    xsize config.screen_width * 6 // 8 ysize config.screen_height * 5 // 8
                    background None
                    if launcher_show_bg:
                        $ selected = cover_items[selected_index]
                        frame at fade_in_item_main(0.0):
                            background None
                            vbox:
                                if satyrlauncher_screen_size == "2560x1440":
                                    spacing 8 ypos -230 
                                elif satyrlauncher_screen_size == "1920x1080":
                                    spacing 8 ypos -180
                                text selected["title"] size 62 at fade_in_item_main(0.1) font montserrat_font
                                text selected["developer"] size 32 at fade_in_item_main(0.15) font montserrat_font
                            vbox:
                                if satyrlauncher_screen_size == "2560x1440":
                                    add AlphaMask(Transform(launcher_asset_path(selected, "cover"), xoffset=0, yoffset=0, zoom=1.0), Transform("publisher_launcher/cover/overlay_2x.png", size=(1440, 465)))  ysize 420 fit "contain" ypos -20  at fade_in_item_main(0.2)
                                elif satyrlauncher_screen_size == "1920x1080":
                                    add AlphaMask(Transform(launcher_asset_path(selected, "cover"), xoffset=0, yoffset=0, zoom=1.0), Transform("publisher_launcher/cover/overlay_2x.png", size=(1440, 465))) ysize 320 fit "contain" ypos -20  at fade_in_item_main(0.2)
                                text selected["about"]:
                                    if satyrlauncher_screen_size == "2560x1440":
                                        size 25 
                                    elif satyrlauncher_screen_size == "1920x1080":
                                        size 20
                                    at fade_in_item_main(0.4) xsize config.screen_width * 4 // 8 ypos 20 font launcher_font
                        hbox at fade_in_item_main(0.25):
                            spacing 20
                            ypos 0.91
                            if selected["wishlist"] != "":
                                button at zoom_button_link:
                                    add "publisher_launcher/assets/steam_2.png"
                                    action If(has_internet, OpenURL(selected["wishlist"]), None)
                                    sensitive (has_internet == True)
                            if not launcher_steam_build:
                                if selected["patreon"] != "":
                                    button at zoom_button_link:
                                        add "publisher_launcher/assets/patreon.png"
                                        action If(has_internet, OpenURL(selected["patreon"]), None)
                                        sensitive (has_internet == True)
                            vbox:
                                yalign 0.5
                                hbox:
                                    spacing 20
                                    text "Platforms:" size 26 at fade_in_item_main(0.3) font launcher_font
                                    text ", ".join(selected["platforms"]) size 26 at fade_in_item_main(0.3) font launcher_font
            if content_ready:
                hbox at fade_in_item_main(0.9):
                    spacing 20
                    xpos 0.06
                    ypos config.screen_height * 9 // 10   
                    hbox:
                        yalign 0.5
                        add "publisher_launcher/assets/steam.png" fit "contain"  ysize 30
                        textbutton "satyrgames" action If(has_internet, OpenURL("https://store.steampowered.com/publisher/satyrgames"), None) sensitive (has_internet == True) background None text_color "#ffffff" text_size 22 xpos 5 ypos -8 text_font launcher_font
                    hbox:
                        yalign 0.5
                        add "publisher_launcher/assets/twitter.png" fit "contain"  ysize 30
                        textbutton "satyrgames" action If(has_internet, OpenURL("https://x.com/satyrgames"), None) sensitive (has_internet == True) background None text_color "#ffffff" text_size 22 xpos 5 ypos -8 text_font launcher_font
                    hbox:
                        yalign 0.5
                        add "publisher_launcher/assets/email.png" fit "contain" ysize 30
                        textbutton "contact@satyrgames.com" action If(has_internet, OpenURL("mailto:contact@satyrgames.com"), None) sensitive (has_internet == True) background None text_color "#ffffff" text_size 22 xpos 5 ypos -8 text_font launcher_font


transform fade_in_hover:
    alpha 1.0

# This handles the initial loading/flashing state at the center
transform logo_checking:
    xalign 0.5 yalign 0.5
    alpha 0.3
    ease 0.35 alpha 1.0
    ease 0.35 alpha 0.3
    ease 0.35 alpha 1.0

# This handles the slide-to-corner animation once connected
transform logo_slide_to_corner:
    xalign 0.5 yalign 0.5
    ease 0.25 xalign 0.07 yalign 0.07 zoom 0.6

transform fade_in_item(i):
    alpha 0.0 xoffset -100
    pause 0.95
    pause (i * 0.10)
    ease 0.45 alpha 1.0 xoffset 0

transform fade_in_item_main(i):
    alpha 0.0 xoffset -100
    pause i
    easein 0.25 alpha 1.0 xoffset 0

transform fade_in_up:
    alpha 0.0 yoffset 60
    pause 1.3
    ease 0.5 alpha 1.0 yoffset 0

transform blur_bg:
    xpos -300 zoom 0.9 alpha 0.0 blur 100
    easein 4.9 xpos -200 alpha 0.8

transform blur_bg_1:
    xpos -300 zoom 0.9 alpha 0.0 blur 100
    easein 4.9 xpos -200 alpha 0.6

transform zoom_hover_launcher:
    on hover:
        ease 0.2 zoom 1.0
    on idle:
        ease 0.2 zoom 0.9

transform zoom_button_link:
    zoom 0.5

default persistent.launcheroptimization = False

style launcher_status_text:
    font "publisher_launcher/font_english/Montserrat/static/Montserrat-Regular.ttf"
    size 30
    color "#ffffff"
    xpos 0.42
    ypos 0.64
