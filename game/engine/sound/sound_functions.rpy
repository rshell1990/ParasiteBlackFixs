init python:
    # plays music, avoids loops, takes *PATH* to a track
    def PlayMusic(MusPath):
        if renpy.music.get_playing(channel = "music") == MusPath:
            return
        else:
            StopSound("music", FadeOut = 0.25)
            PlaySound(MusPath, FadeIn = 0.25, FadeOut = 0.25, Loop = True, Channel = "music")
            return

    # plays music from a list. you can feed it a soundlib key for speed!
    def PlayMusicRandom(Value): 
        if isinstance(Value, str):
            MusicList = soundLib[Value]
        elif isinstance(Value, list):
            MusicList = Value
        PlayMusic(renpy.random.choice(MusicList))
        return

    # plays sex fx. takes file path or variable name (like audio.somefile).
    def PlaySexFx(Val, Loop = 0, Volume = 1.0, Channel = 1):
        if Channel == 1:
            ChannelID = "sexfx"
        elif Channel == 2:
            ChannelID = "sexfx2"
        ####
        if hasattr(audio, Val):
            PlayPath = getattr(audio, Val)
        else:
            PlayPath = Val
        ####
        PlaySound(PlayPath, Volume = Volume, Channel = ChannelID, Loop = (True if Loop == 1 else False))
        return

    # same as normal playsexfx but runs on 2nd channel to have parallel sounds
    def PlaySexFx2(Val, Loop = 0, Volume = 1.0):
        PlaySexFx(Val, Loop, Volume, Channel = 2)
        return

    # stops sexfx
    def StopSexFx(Channel = 1, FadeOut = 0.2):
        if Channel == 1:
            ChannelID = "sexfx"
        elif Channel == 2:
            ChannelID = "sexfx2"
        StopSound(ChannelID, FadeOut)
        return

    # stops sexfx playing on channel 2
    def StopSexFx2():
        StopSexFx(2)
        return

    # plays random sound from a list, Value can be a soundLib key to save time
    def PlaySoundRandom(Value, Volume = 1.0, Channel = "sound"):
        if isinstance(Value, str):
            Assert(Value in soundLib, "sound list %s not found in soundLib!" % Value)
            SoundList = soundLib[Value]
        elif isinstance(Value, list):
            SoundList = Value
        PlaySound(renpy.random.choice(SoundList), Volume = Volume, Channel = Channel)
        return

    # same as playsoundrandom but does channel roulette
    def PlaySoundRandomPara(Value, Volume = 1.0, Channel = "sound"):
        PlaySoundRandom(Value, Volume = Volume, Channel = GetNextSubChannel(Channel))
        return

    ##### shorthand for playsound(x, channel=ambience)
    def PlayAmbience(Sound, FadeIn = 0.0, FadeOut = 0.0, Volume = 1.0, Loop = True):
        PlaySound(Sound, FadeIn = FadeIn, FadeOut = FadeOut, Volume = Volume, Loop = Loop, Channel = "ambience")
        return
    def StopAmbience(Sound, FadeOut = 0.0):
        StopSound("ambience", FadeOut = FadeOut)
        return

    ##### parallel variant, for when you want overlapping sounds w/o thinking too much
    def PlaySoundPara(Sound, FadeIn = 0.0, FadeOut = 0.0, Volume = 1.0, Loop = False, Channel = "sound"):
        PlaySound(Sound, FadeIn = FadeIn, FadeOut = FadeOut, Volume = Volume, Loop = Loop, Channel = GetNextSubChannel(Channel))
        return
    # stops sound on ALL parallel channels
    def StopSoundPara(ChannelID, FadeOut = 0.0):
        StopSound(ChannelID, FadeOut)
        for i in (2, 12):
            StopSound("%s%s" % (ChannelID, i), FadeOut)
        return

    #### all sounds/mus we play *should* converge to this function, its a wrapper on a renpy call
    def PlaySound(Sound, FadeIn = 0.0, FadeOut = 0.0, Volume = 1.0, Loop = False, Channel = "sound"):
        renpy.music.play(Sound, channel = Channel, relative_volume = Volume, loop = Loop, fadein = FadeIn, fadeout = FadeOut)
        return
    #### all sounds/mus we stop *should* converge to this function, its a wrapper on a renpy call
    def StopSound(ChannelID, FadeOut = 0.0):
        renpy.music.stop(channel = ChannelID, fadeout = FadeOut)
        return

    # control whether music should automatically revert to location-defined
    def AutoMus(TrueOrFalse):
        store.autoMus = TrueOrFalse
        return
    # control whether ambience should automatically revert to location-defined
    def AutoAmb(TrueOrFalse):
        store.autoAmb = TrueOrFalse
        return
