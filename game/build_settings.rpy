init python hide:
    ## -------------------------------------------------------------------------
    ## ARCHIVE DEFINITIONS
    ## -------------------------------------------------------------------------
    # Core archives
    packs = ["engine", "images", "audio", "video", "data", "tl"]
    for pack in packs:
        build.archive(pack, "all")

    # Scene archives
    scene_packs = ["scenes1", "scenes2", "scenes3", "scenes4"]
    for scene_pack in scene_packs:
        build.archive(scene_pack, "all")


    ## -------------------------------------------------------------------------
    ## FILES TO EXCLUDE (Processed first; matching files are ignored)
    ## -------------------------------------------------------------------------
    build.classify("**/Thumbs.db", None)            # Windows thumbnail cache
    build.classify("game/**.rpy", None)             # Source scripts
    build.classify("game/**.pyc", None)             # Uncompiled python cache
    build.classify("game/**.bak", None)             # Backup files

    build.classify("game/**.mp3", None)             # Non-OGG audio
    build.classify("game/**.wav", None)             # Non-OGG audio
    build.classify("game/**.mp4", None)             # Non-WebM video
    build.classify("game/**.avi", None)             # Non-WebM video

    build.classify("game/build_excluded/**", None)  # Build exclusion directory
    build.classify("**/.vscode/**", None)           # VSCode settings
    build.classify("README.md", None)               # Git readme
    build.classify("debugLog.txt", None)            # Local debug log
    build.classify("game/cache/**", None)           # Local cache
    build.classify("game/saves/**", None)           # Local saves
    build.classify("**/DOC_**.txt", None)           # Documentation files
    build.classify("game/dlc/**", None)             # DLC files

    # Dev tools & config utilities
    build.classify("game/devtools/*.exe", None)
    build.classify("game/devtools/*.json", None)


    ## -------------------------------------------------------------------------
    ## SPECIFIC ASSET CLASSIFICATIONS (Must precede generic asset rules)
    ## -------------------------------------------------------------------------
    # Scene Assets (Partitioned alphabetically)
    build.classify("game/images/sexy_scenes/[a-f]**.webp", "scenes1")
    build.classify("game/images/sexy_scenes/[a-f]**.webm", "scenes1")

    build.classify("game/images/sexy_scenes/[g-l]**.webp", "scenes2")
    build.classify("game/images/sexy_scenes/[g-l]**.webm", "scenes2")

    build.classify("game/images/sexy_scenes/[m-r]**.webp", "scenes3")
    build.classify("game/images/sexy_scenes/[m-r]**.webm", "scenes3")

    build.classify("game/images/sexy_scenes/[s-z]**.webp", "scenes4")
    build.classify("game/images/sexy_scenes/[s-z]**.webm", "scenes4")


    ## -------------------------------------------------------------------------
    ## GENERAL ASSET & DATA CLASSIFICATIONS
    ## -------------------------------------------------------------------------
    # Engine & Scripts
    build.classify("game/engine/**.rpyc",                   "engine")
    build.classify("game/screens/**.rpyc",                  "engine")
    build.classify("game/options.rpyc",                     "engine")
    build.classify("game/gui.rpyc",                         "engine")
    build.classify("game/styles.rpyc",                      "engine")
    build.classify("game/devtools/**.rpyc",                 "engine")
    build.classify("game/build_settings.rpyc",             "engine")
    build.classify("game/publisher_launcher/satyrlauncher.rpyc", "engine")
    build.classify("game/**.ttf",                           "engine")

    # Data & Translations
    build.classify("game/data/**.rpyc",                     "data")
    build.classify("game/strings/**.rpyc",                  "data")
    build.classify("game/tl/**.rpyc",                       "tl")

    # Fallback rule for any root or unclassified .rpyc files
    build.classify("game/**.rpyc",                          "engine")

    # Images & Multimedia
    build.classify("game/images/**.webp",                   "images")
    build.classify("game/images/**.webm",                   "images")
    build.classify("game/gui/**.webp",                      "images")

    # Launcher Assets
    build.classify("game/publisher_launcher/**.png",        "images")
    build.classify("game/publisher_launcher/**.jpg",        "images")
    build.classify("game/publisher_launcher/**.otf",        "images")
    build.classify("game/publisher_launcher/**.webp",       "images")

    # Audio & Video
    build.classify("game/audio/**.ogg",                     "audio")
    build.classify("game/video/**.webm",                    "video")

    # Android specific distribution files
    build.classify("res/**.**",                             "android")