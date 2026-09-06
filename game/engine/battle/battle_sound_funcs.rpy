init python:
    def Battle_RegisterBattleSfxChannels():
        # for sounds
        for Side in range(2): # 0-1 side
            for PosIndex in range(4): # 0-3 char slot
                for ChannelIndex in range(3): # 0-2 fx channels per char
                    NewFXChannelName = "BattleSFX_%s_%s_%s" % (Side, PosIndex, ChannelIndex)
                    renpy.music.register_channel(NewFXChannelName, mixer = "sfx", loop = False)
                NewVoiceChannelName = "BattleSFX_%s_%s_voice" % (Side, PosIndex)
                renpy.music.register_channel(NewVoiceChannelName, mixer = "sfx", loop = False)
    Battle_RegisterBattleSfxChannels()
    
    def Battle_GetNextCharFXChannel(BattleChar):
        if BattleChar.AudioChannelsFX_NextIndex < (len(BattleChar.AudioChannelsFX) - 1):
            BattleChar.AudioChannelsFX_NextIndex += 1
        else:
            BattleChar.AudioChannelsFX_NextIndex = 0
        return BattleChar.AudioChannelsFX[BattleChar.AudioChannelsFX_NextIndex]

    def Battle_PlayCharSkinSound(SoundID, CallingBattleChar, AudioSourceOverride = None, Chance = 1.0, Voice = False):
        if SoundID not in CallingBattleChar.BattleSkin.SoundsDict:
            return
        SoundList = CallingBattleChar.BattleSkin.SoundsDict[SoundID]
        if len(SoundList) == 0:
            return

        DoSoundRoll = (True if RngFloat(0.0, 1.0) <= Chance else False)
        if DoSoundRoll:
            TargetChar = (CallingBattleChar if AudioSourceOverride is None else AudioSourceOverride)
            ChosenSound = renpy.random.choice(SoundList)
            SilenceTime = TargetChar.BattleSkin.SoundsExtraSilence[SoundID]
            RelVolume = TargetChar.BattleSkin.SoundsVolCorrection[SoundID]
            Battle_PlaySoundOnBattleChar(ChosenSound, TargetChar, Voice = Voice, ExtraSilence = SilenceTime, RelVolume = RelVolume)
        return

    def Battle_PlaySoundOnBattleChar(Sound, TargetChar, Voice = False, ExtraSilence = 0.0, RelVolume = 1.0):
        TargetChannel = (Battle_GetNextCharFXChannel(TargetChar) if Voice == False else TargetChar.AudioChannelVoice)
        renpy.music.play(["<silence %s>" % ExtraSilence, Sound], channel = TargetChannel, relative_volume = RelVolume)
        return

    def Battle_StopSoundOnBattleChar(BattleChar, Fadeout = 0.0, Voice = False):
        if Voice:
            renpy.music.stop(channel = BattleChar.AudioChannelVoice, fadeout = Fadeout)
        else:
            for ChannelName in BattleChar.AudioChannelsFX:
                renpy.music.stop(channel = ChannelName, fadeout = Fadeout)
        return