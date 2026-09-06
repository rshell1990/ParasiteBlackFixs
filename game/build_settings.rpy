init python hide:
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ## / is the directory separator.
    ## * matches all characters, except the directory separator.
    ## ** matches all characters, including the directory separator.
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.    
    ### FILES TO SKIP ###
    build.classify("**/Thumbs.db", None)            # windows thumbnails file
    build.classify("game/**.rpy", None)             # source files
    build.classify("game/**.bak", None)             # backup files

    build.classify("game/**.mp3", None)             # non-ogg audio
    build.classify("game/**.wav", None)             # non-ogg audio

    build.classify("game/**.mp4", None)             # non-webm video
    build.classify("game/**.avi", None)             # non-webm video

    build.classify("game/build_excluded/**", None)  # only for buildsettings
    build.classify("**/.vscode/**", None)           # for vscode .json stuff 

    build.classify("README.md", None)               # git readme

    build.classify("debugLog.txt", None)            # your local debuglog.txt

    build.classify("game/cache/**", None)           # local cache folder
    build.classify("game/saves/**", None)           # local saves folder

    build.classify("**/DOC_**.txt", None)           # txt docs (any)

    build.classify("game/dlc/**", None)             # any and all dlc files

    build.classify("game/devtools/RenParse.exe", None)           # renparse & config
    build.classify("game/devtools/RenParseConfig.json", None)
    build.classify("game/devtools/RenPurge.exe", None)           # renpurge & config
    build.classify("game/devtools/RenPurgeConfig.json", None)
    build.classify("game/devtools/OrphanRadar.exe", None)           # OR & config
    build.classify("game/devtools/OrphanRadarConfig.json", None)
    build.classify("game/devtools/QuoteSeeker.exe", None)           # QS & config (exclusively for nested "" unescaped quotes)
    build.classify("game/devtools/QuoteSeekerConfig.json", None)

    ### ARCHIVES ###
    packs = ["engine", "images", "audio", "video", "data", "tl"]
    for pack in packs:
        # Include all archives under "all"
        build.archive(pack, "all")

    ### FILES TO ARCHIVE ###
    # engine.rpa
    build.classify("game/engine/**.rpyc",   "engine")
    build.classify("game/screens/**.rpyc",  "engine")

    build.classify("game/**.ttf", "engine")

    # other engine/dev-related files
    build.classify("game/options.rpyc",     "engine")
    build.classify("game/gui.rpyc",         "engine")
    build.classify("game/styles.rpyc",      "engine")
    build.classify("game/devtools/**.rpyc", "engine") # drop in devroom and devmenu
    build.classify("game/build_settings.rpyc", "engine")
    build.classify("game/publisher_launcher/satyrlauncher.rpyc", "engine")

    ##### assets section #####
    # sex scenes
    build.archive("scenes1", "all")
    build.archive("scenes2", "all")
    build.archive("scenes3", "all")
    build.archive("scenes4", "all")
    # a-f
    build.classify("game/images/sexy_scenes/[a-f]**.webp",   "scenes1")
    build.classify("game/images/sexy_scenes/[A-F]**.webp",   "scenes1")
    build.classify("game/images/sexy_scenes/[a-f]**.webm",   "scenes1")
    build.classify("game/images/sexy_scenes/[A-F]**.webm",   "scenes1")
    # g-l
    build.classify("game/images/sexy_scenes/[g-l]**.webp",   "scenes2")
    build.classify("game/images/sexy_scenes/[G-L]**.webp",   "scenes2")
    build.classify("game/images/sexy_scenes/[g-l]**.webm",   "scenes2")
    build.classify("game/images/sexy_scenes/[G-L]**.webm",   "scenes2")
    # m-r
    build.classify("game/images/sexy_scenes/[m-r]**.webp",   "scenes3")
    build.classify("game/images/sexy_scenes/[M-R]**.webp",   "scenes3")
    build.classify("game/images/sexy_scenes/[m-r]**.webm",   "scenes3")
    build.classify("game/images/sexy_scenes/[M-R]**.webm",   "scenes3")
    # s-z
    build.classify("game/images/sexy_scenes/[s-z]**.webp",   "scenes4")
    build.classify("game/images/sexy_scenes/[S-Z]**.webp",   "scenes4")
    build.classify("game/images/sexy_scenes/[s-z]**.webm",   "scenes4")
    build.classify("game/images/sexy_scenes/[S-Z]**.webm",   "scenes4")

    # images.rpa
    build.classify("game/images/**.webp",   "images")
    build.classify("game/images/**.webm",   "images") # anim webms be images too
    build.classify("game/gui/**.webp",      "images")
    # launcher-related images(and a font)
    build.classify("game/publisher_launcher/**.png", "images")
    build.classify("game/publisher_launcher/**.jpg", "images")
    build.classify("game/publisher_launcher/**.otf", "images")
    build.classify("game/publisher_launcher/**.webp", "images")
    
    # audio.rpa
    build.classify("game/audio/**.ogg",     "audio")

    # video.rpa
    build.classify("game/video/**.webm",    "video")

    # data.rpa
    build.classify("game/data/**.rpyc",     "data")
    build.classify("game/strings/**.rpyc",  "data")

    # tl.rpa
    build.classify("game/tl/**.rpyc",       "tl")

    build.classify("res/**.**",             "android")
