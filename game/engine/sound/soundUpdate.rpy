default SoundUpdate_LastAt = 0.0
define SoundUpdate_Every = 1.0
init python:
    PeriodicTickCallbacks = []
    def PeriodicTick():
        for callbackF in PeriodicTickCallbacks:
            callbackF()
    config.periodic_callback = PeriodicTick


    def soundUpdate():
        store.SoundUpdate_LastAt = renpy.time.time()
        if store.autoAmb == True and store.dynamicAmbience is not None:
            store.dynamicAmbience.update()
        if store.autoMus == True and store.dynamicMusic is not None:
            store.dynamicMusic.update()

    def SoundTick():
        last_at = getattr(store, "SoundUpdate_LastAt", 0.0)
        sound_every = getattr(store, "SoundUpdate_Every", 0.1)

    PeriodicTickCallbacks.append(SoundTick)
