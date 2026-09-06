label splashscreen:    
    if config.developer and (persistent.first_time_language_selection == False):
        return
    scene black with dissolve
    if persistent.first_time_language_selection == True:
        call screen LanguageSelection(FromFirstLaunch = True)
        with dissolve
        $ persistent.first_time_language_selection = False
    $ Pause(0.1)
    $ renpy.movie_cutscene("video/dev_logo.webm", stop_music = False)
    return