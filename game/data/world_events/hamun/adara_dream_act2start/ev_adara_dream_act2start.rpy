init python:
    @AppendToAllQuests
    class EventAdaraDreamAct2Start(LogicModule):
        def onPreSleepHamunHookahBar(self):
            if RngInt(1, 5) == 1:
                return TriggeredEvent("event_AdaraDreamAct2Start")

label event_AdaraDreamAct2Start:
    $ QstComplete(EventAdaraDreamAct2Start)
    scene black with dissolve
    "As I drifted off to sleep, pleasant memories came rushing back to me."

    $ AutoMus(False)
    $ PlayMusic("audio/music/47_Bubbles.ogg")
    scene cg_adara_on_top_nude with flash
    $ Pause()

    "Adara's naked body on top of mine, her eyes filled with love and adoration as she looks down at me."
    "She's beautiful... Simply beautiful."
    ADARA "[player_name!t]... I've missed you so much."
    ADARA "I know you did your best."
    MC "Adara, I—"

    scene cg_adara_kissing_nude with dissolve
    $ Pause()

    ADARA "{i}I love you...{/i} [player_name!t]."
    ADARA "{i}Come back to me.{/i}"
    ADARA "{i}Come home...{/i}"

    call shared_bed_sleep_logic from _call_shared_bed_sleep_logic
    $ LocFlush()
    $ CharSetClothes("mc", "pants")
    show mc at cright_f
    with flash
    show mc at shake
    
    MC @surprised "...!"
    $ AutoMus(True)
    MC @sad "...Adara."
    MC @serious "{i}I'll come home one day. I promise.{/i}"
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ LocEnter()

