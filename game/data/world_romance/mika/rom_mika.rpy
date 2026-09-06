init python:
    notesLib["visit_mika_post_celebration"] = Note(
        _("Visit Mika at the dorms"), 
        _("Mika and I have agreed to meet up at the Palam Tower student dorms, after dark."))
    @AppendToAllQuests
    # mika romance logic,
    # the module is turned on by finishing QstLetsCelebrate
    # progress 0 is her catching up with you in the mainhall at night (intro scene), 
    # 1 her hanging out in her quarters greeting you at night
    # 2 is afterwards
    class RomanceMika(LogicModule):
        def __init__(self):
            super().__init__()

            self._doMikaWantSexToday = None
            self._doMikaWantSexTodayDayCheck = None

        def onEnter(self):  
            if GetLocID() == "novaras_palam_dorm":
                if IsEvening():
                    if self.progress == 0:
                        return TriggeredEvent("rom_mika_after_celebration_event")

            elif GetLocID() == "novaras_palam_bath":
                if IsEvening():
                    if self.progress == 2:
                        return TriggeredEvent("mika_rom_divine_bath_repeat")

        def doMikaWantSexToday(self):
            if self._doMikaWantSexTodayDayCheck != GetGameDay():
                self._doMikaWantSexTodayDayCheck = GetGameDay()
                self._doMikaWantSexToday = renpy.random.randint(1, 10) <= 6
            return self._doMikaWantSexToday

        def mikaHadSexToday(self):
            self._doMikaWantSexToday = False

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_dorm":
                if IsEvening():
                    if self.progress >= 1:
                        btnMods["btn_palam_dorm_mika_talk_btn"] = BtnJumpLabel(_("Talk to Mika"), "mika_rom_meet_loop")
            return LocButtonMod(directMods = btnMods)

        def onStart(self):
            NoteUnlock("visit_mika_post_celebration")
            return


label mika_rom_meet_loop:
    show mika at center with dissolve
    MIKA @smile "[player_name!t]!"
    menu mika_rom_meet_loop_1:
        "How are you, Mika?":
            if GetGameDay() % 4 == 0:
                MIKA @smile "Mhmm! I- I've been training really hard!" #Response 1
                MIKA @smile "Don't worry, I won't let you down when I'm finally sent to wherever!" 
            elif GetGameDay() % 4 == 1:
                MIKA @sad "Z-Zara keeps telling me to try to reach more books and things." #Response 2
                MIKA @angry "{i}YoU'Ll OnLy bEcOmE a beTtEr MagE iF YoU rEaD mORe MiKa!{/i}"
                MIKA @angry "Hmph! S-She just doesn't get reading some dull book; that is how I learn best!"
                MIKA @sad "You understand me... {i}Right?{/i}"
            elif GetGameDay() % 4 == 2:
                MIKA @blush "Ummm... What's a sixty-nine?" #Response 3
                MIKA @blush "J-Jana says she's done some weird stuff with the other girls before."
                MIKA @shock "Do you kiss each other sixty-nine times in a row!?"
                MIKA @think "That kinda seems like a lot..."
            elif GetGameDay() % 4 == 3:
                MIKA @smile "Recently, I managed to grow some strawberries!" #Response 4
                MIKA @think "Sister Divine keeps telling me to be careful about the potatoes I'm growing, though."
                MIKA @smile "I think she thinks Jana might try and make something with them."
                MIKA @think "I wonder what though?"
            jump mika_rom_meet_loop_1

        "How is the child?" if PregMika().NumBirths > 0:
            if GetGameDay() % 4 == 0:
                MIKA @smile "They've been hungry recently."
                MIKA @smile "My poor boobs are so sore!"
                MIKA @blush "...Reminds me of someone else's appetite for them."
                jump mika_rom_meet_loop_1
            elif GetGameDay() % 4 == 1:
                MIKA @sad "They've been a bit restless in the nights recently."
                MIKA @sad "Bad dreams, maybe?"
                jump mika_rom_meet_loop_1
            elif GetGameDay() % 4 == 2:
                MIKA @smile "They've just been so energetic today!"
                MIKA @smile "Gods... I wonder what they'll be like when they grow up?"
                jump mika_rom_meet_loop_1
            elif GetGameDay() % 4 == 3:
                MIKA @smile "Mmmm... They've been pretty sleepy today."
                MIKA @smile "I think they wore themselves out earlier."
                MIKA @smile "You wanna hold them, maybe?"
                jump mika_rom_meet_loop_1

        "Are you free for some... {i}entertainment?{/i}":
            if not RomanceMika().doMikaWantSexToday():
                MIKA @talk "Mmmm, s-some other time." #Fail
                MIKA @talk "I have a couple of things I need to attend to today."
                jump mika_rom_meet_loop_1
            else:
                MIKA @blush "W-What was you thinking?" #Success 
                menu:
                    "I was thinking about how much I wanted to kiss you...":
                        call mika_rom_kiss_repeat from _call_mika_rom_kiss_repeat
                    "I was thinking about you doing that thing with your mouth again...":
                        MIKA @think "That thing with my-"
                        MIKA @shock "O-Oh...!"
                        MIKA @blush "W-Well, y-yes but..."
                        MIKA @blush "Come on, before someone sees us."
                        MIKA @blush "G- Get it out for me, please?"
                        call mika_rom_bj_repeat from _call_mika_rom_bj_repeat
                    "Let's lay down on your bed for a while...":
                        MIKA @blush "M-Mhmm... Y-Yes."
                        call mika_rom_missionary_repeat from _call_mika_rom_missionary_repeat
                    "Feel like doing something... {i}risky{/i} again?":
                        MIKA @blush "Y-Yes..."
                        MIKA @blush "H-Hold on though, let me just make sure no one's there..."
                        MIKA @blush "Should I wear something?"
                        menu:
                            "No clothes... Now move your cute blue ass.":
                                MIKA @shock "Y-Yes sir!"
                                scene black with dissolve
                                $ PlaySoundRandom("tentFlap")
                                $ CharSetClothes("mika", "naked")
                                $ LocFlush()
                                show mika at center 
                                with dissolve
                                call mika_rom_hallway_repeat from _call_mika_rom_hallway_repeat
                            "Put your lingerie on.":
                                MIKA @blush "M-Mmm... Give me a moment to change then."
                                scene black with dissolve
                                $ PlaySoundRandom("tentFlap")
                                $ CharSetClothes("mika", "ling2")
                                $ LocFlush()
                                show mika at center 
                                with dissolve
                                call mika_rom_hallway_repeat from _call_mika_rom_hallway_repeat_2
                    # Available if the player got them to have sex
                    "Are you going to go revisit Sister Divine soon?" if not QstLittleLies().mikaXDivineSceneSkipped: 
                        MIKA @blush "I - I can ask her to meet me again tonight."
                        MIKA @blush "I- If that's what you want?"
                        MIKA @blush "O-Okay... I'll tell her to meet me in the same place."
                        $ QstSetProgress(RomanceMika, 2)
                    "On second thought...":
                        MIKA @talk "What is it?"
                        jump mika_rom_meet_loop_1
                $ RomanceMika().mikaHadSexToday()
                $ LocEnter()

        "I must go...":
            MIKA @shock "S-So soon?"
            MIKA @sad "O-Oh, well..."
            MIKA @smile "I can't wait to see you again!"
            $ LocEnter()