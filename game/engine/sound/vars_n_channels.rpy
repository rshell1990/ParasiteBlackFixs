define config.main_menu_music = "audio/music/1_Menu.ogg"

# to make activate_sound and hover_sound play on proper ui channel
define config.play_channel = "guisfx" 

init python:
    # on first-start, sets main mixer to 50%
    if not persistent._set_preferences:
        preferences.set_volume("main", 0.5)

    # ref: music, sound, voice - default channels connected to corresp. mixers.
    # music, sfx, and voice - default mixers.


    # creates more channels like chan chan2 chan3 ... chan10
    for ChannelID, Mixer in zip(["ambience", "sound", "sexfx", "guisfx"], 
                                ["ambience", "sfx",   "sexfx", "guisfx"]):
        Loop = (True if ChannelID == "ambience" else False)
        renpy.music.register_channel(ChannelID, mixer = Mixer, loop = Loop)
        for i in range(2, 11):
            renpy.music.register_channel("%s%s" % (ChannelID, i), mixer = Mixer, loop = Loop)

    SubChannelIndexes = {
        "sound"     : 1,
        "ambience"  : 1,
        "sexfx"     : 1,
        "guisfx"    : 1,
    }

    def GetNextSubChannel(Channel):
        Assert(Channel in SubChannelIndexes)

        NextIndex = SubChannelIndexes[Channel]
        if NextIndex == 1:
            SubChannelID = Channel
        else:
            SubChannelID = "%s%s" % (Channel, NextIndex)

        SubChannelIndexes[Channel] += 1
        if SubChannelIndexes[Channel] >= 11:
            SubChannelIndexes[Channel] = 1
        return SubChannelID

    # get a list of all channel & mixer names printed out, debug purposes
    # warning, seems to be lying doesnt list 'audio' channel/mixer
    def DEBUG_PrintAllChannelsAndMixers():
        for ChannelObject in renpy.audio.audio.all_channels:
            print("DEBUG: channel: " + str(ChannelObject.name) + "-> mixer: " + str(ChannelObject.mixer))
        return
