default SoundUpdate_LastAt = 0
define SoundUpdate_Every = 1.0

init python:
    # Initialize the variable in store immediately at init time
    if not hasattr(store, "SoundUpdate_LastAt"):
        store.SoundUpdate_LastAt = 0

    PeriodicTickCallbacks = []
    def PeriodicTick():
        for callbackF in PeriodicTickCallbacks:
            callbackF()
    config.periodic_callback = PeriodicTick

    def soundUpdate():
        store.SoundUpdate_LastAt = renpy.time.time()
        if getattr(store, "autoAmb", False) and getattr(store, "dynamicAmbience", None) is not None:
            store.dynamicAmbience.update()
        if getattr(store, "autoMus", False) and getattr(store, "dynamicMusic", None) is not None:
            store.dynamicMusic.update()

    def SoundTick():
        last_at = getattr(store, "SoundUpdate_LastAt", 0)
        if renpy.time.time() - last_at > SoundUpdate_Every:
            soundUpdate()

    PeriodicTickCallbacks.append(SoundTick)