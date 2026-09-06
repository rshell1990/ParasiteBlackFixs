init -1 python:
    class DaynightSound(object):
        def __init__(self, channel, dayTrack, nightTrack):
            self.channel = channel
            self.dayTrack = dayTrack
            self.nightTrack = nightTrack

        def update(self):
            if IsDaytime():
                targetTrack = self.dayTrack
            else:
                targetTrack = self.nightTrack

            if renpy.music.is_playing(channel = self.channel) != targetTrack:
                if targetTrack is None:
                    renpy.music.stop(channel = self.channel, fadeout = 1.0)
                else:
                    renpy.music.play(targetTrack,
                                channel = self.channel,
                                loop = True,
                                fadeout = 0.5,
                                fadein = 0.5,
                                if_changed = True)
