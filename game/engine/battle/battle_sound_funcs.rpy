init python:
    def Battle_RegisterBattleSfxChannels():
        # for sounds
        for Side in range(2): # 0-1 side
            for PosIndex in range(4): # 0-3 char slot
                for ChannelIndex in range(3): # 0-2 fx channels per char
                    NewFXChannelName = "BattleSFX_%s_%s_%s" % (Side, PosIndex, ChannelIndex)
                    renpy.music.register_channel(NewFXChannelName, mixer = "sfx", loop = False)
                NewVoiceChannelName = "BattleSFX_%s_%s_voice" % (Side, PosIndex)
                renpy.music.register_channel(NewVoiceChannelName, mixer = "voice", loop = False)

    Battle_RegisterBattleSfxChannels()
    
    def Battle_GetNextCharFXChannel(BattleChar):
        channels = getattr(BattleChar, "AudioChannelsFX", [])
        if not channels:
            return "sfx"

        next_idx = getattr(BattleChar, "AudioChannelsFX_NextIndex", 0)
        if next_idx < (len(channels) - 1):
            next_idx += 1
        else:
            next_idx = 0

        BattleChar.AudioChannelsFX_NextIndex = next_idx
        return channels[next_idx]

    def Battle_PlayCharSkinSound(SoundID, CallingBattleChar, AudioSourceOverride = None, Chance = 1.0, Voice = False):
        if not CallingBattleChar or not hasattr(CallingBattleChar, "BattleSkin"):
            return

        skin = CallingBattleChar.BattleSkin
        sounds_dict = getattr(skin, "SoundsDict", {})
        
        if SoundID not in sounds_dict:
            return

        SoundList = sounds_dict.get(SoundID, [])
        if not SoundList:
            return

        rng_val = store.RngFloat(0.0, 1.0) if hasattr(store, "RngFloat") else renpy.random.random()
        DoSoundRoll = (rng_val <= Chance)

        if DoSoundRoll:
            TargetChar = (CallingBattleChar if AudioSourceOverride is None else AudioSourceOverride)
            ChosenSound = renpy.random.choice(SoundList)

            silence_dict = getattr(TargetChar.BattleSkin, "SoundsExtraSilence", {})
            vol_dict = getattr(TargetChar.BattleSkin, "SoundsVolCorrection", {})

            SilenceTime = silence_dict.get(SoundID, 0.0)
            RelVolume = vol_dict.get(SoundID, 1.0)

            Battle_PlaySoundOnBattleChar(ChosenSound, TargetChar, Voice = Voice, ExtraSilence = SilenceTime, RelVolume = RelVolume)
        return

    def Battle_PlaySoundOnBattleChar(Sound, TargetChar, Voice = False, ExtraSilence = 0.0, RelVolume = 1.0):
        if not TargetChar:
            return

        if Voice:
            TargetChannel = getattr(TargetChar, "AudioChannelVoice", "voice")
        else:
            TargetChannel = Battle_GetNextCharFXChannel(TargetChar)

        if ExtraSilence > 0:
            renpy.music.play(["<silence %s>" % ExtraSilence, Sound], channel = TargetChannel, relative_volume = RelVolume)
        else:
            renpy.music.play(Sound, channel = TargetChannel, relative_volume = RelVolume)
        return

    def Battle_StopSoundOnBattleChar(BattleChar, Fadeout = 0.0, Voice = False):
        if not BattleChar:
            return

        if Voice:
            voice_channel = getattr(BattleChar, "AudioChannelVoice", None)
            if voice_channel:
                renpy.music.stop(channel = voice_channel, fadeout = Fadeout)
        else:
            for ChannelName in getattr(BattleChar, "AudioChannelsFX", []):
                renpy.music.stop(channel = ChannelName, fadeout = Fadeout)
        return