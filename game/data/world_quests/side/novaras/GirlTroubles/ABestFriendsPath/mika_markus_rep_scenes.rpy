init python:
    @AppendToAllQuests
    class EventMikaMarkusRepScenes(LogicModule):
        def __init__(self):
            super().__init__()

            # aka "whether this night the sex will happen at all"
            self.EventShowTonight = False

            # aka "whether player had seen the sex scene unfold tonight"
            # while its false, player can click-into a scene
            self.EventSeenTonight = False

            # 0 is dbj, 1 is 3some
            self.EventKind = 0 

            self.CutInsForScenes = {0, 1}


        # the scenes are only seeable every other night
        def onNoon(self):
            self.EventShowTonight = not self.EventShowTonight

            if self.EventShowTonight:
                self.EventSeenTonight = False

                if self.EventKind == 0:
                    self.EventKind = 1
                elif self.EventKind == 1:
                    self.EventKind = 0
            return

        ### fire off the cut-in once for either scene
        def onEnter(self):  
            if len(self.CutInsForScenes) == 0:
                return

            if self.EventShowTonight:
                if GetLocID() in ["novaras_palam_e_wing"]:
                    if IsInTimeFrame(TIME_DAY_END, TIME_LATENIGHT):
                        if not self.EventSeenTonight:
                            if self.EventKind == 0:
                                PlaySexFx("audio/sex_sounds/reginamasturbate_loop_fade.ogg", 1)
                            elif self.EventKind == 1:
                                PlaySexFx("audio/sex_sounds/forgean_100_muffled.ogg", 1)

                        if self.EventKind in self.CutInsForScenes:
                            self.CutInsForScenes.remove(self.EventKind)
                            if self.EventKind == 0:
                                return TriggeredEvent("event_markus_mika_rep_dbj_click")
                            elif self.EventKind == 1:
                                return TriggeredEvent("event_markus_mika_rep_threesome_click")

        def onExit(self):
            StopSexFx()
            return

        # clickey
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_palam_e_wing":
                if IsInTimeFrame(TIME_DAY_END, TIME_LATENIGHT):
                    if self.EventShowTonight:
                        if not self.EventSeenTonight:
                            if self.EventKind == 0:
                                btnMods["btn_palam_e_wing_investigate_sounds"] = BtnJumpLabel(_("Investigate the sounds"), "event_markus_mika_rep_dbj_click")
                            elif self.EventKind == 1:
                                btnMods["btn_palam_e_wing_investigate_sounds"] = BtnJumpLabel(_("Investigate the sounds"), "event_markus_mika_rep_threesome_click")
                        return LocButtonMod(directMods = btnMods)
            else:
                return None

####################################################################
###### double blowjob
### dbj click-in
label event_markus_mika_rep_dbj_click:
    MIKA "Mhmm...! ❤️"
    MARKUS "{i}*Groans*{/i}"
    show mc at cleft with easeinleft
    "I could hear the sounds of Mika and Markus' moans and grunts from the other side of the women's living quarters."
    MC "(Looks like the two of them are at it again...)"
    MC "({i}...Hmmm.{/i})"
    MC "(Should I?)"
    menu:
        "Peek through the door.":
            scene black with dissolve
            $ StopSexFx()
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            scene mika_markus_bj_stroke_slow
            with dissolve
            $ Pause()
            "Gently pushing open the door to the girls' dorm, Markus is sat naked on a chair, a nearly empty bottle at his side as Mika kneels naked between his legs."
            $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
            scene mika_markus_bj_loop_slow
            with dissolve
            $ Pause()
            "Her head bopped up and down as he grabbed a hold of her pigtails with his fist, guiding her head."
            "Lewd slurping sounds escaped from Mika's mouth as she undoubtedly pleasured his member, obscured from my view."
            MIKA "{i}*Slurp!* *Slurp!*{/i}"
            MIKA "Mhmmmm...{i}*Slurp*{/i}"
            scene mika_markus_bj_loop_fast
            with dissolve
            $ Pause()
            MARKUS "Ahhh!!"
            MARKUS "That's it, Mika!"
            MARKUS "Tell me how you love that cock, girl!"
            scene mika_markus_bj_stroke_fast
            with dissolve
            $ Pause()
            MIKA "Mhmm! Ilhuvv yhourrr bhiggh chockk! {i}*Slurp!*{/i} ❤️"
            scene mika_markus_bj_loop_fast
            with dissolve
            $ Pause()
            MARKUS "Oooh! That's it!"
            MARKUS "My - Ahh! slutty little mage! Hrghhh!"
            "As he continued to push Mika's head down, his eyes briefly glanced over to meet mine, and he smirked."
            "With a wave of his other hand, it seemed like he was inviting me in..."
            menu:
                "Enter.":
                    call event_markus_mika_rep_dbj_sexscene from _call_event_markus_mika_rep_dbj_sexscene
                "Refuse Markus' offer.":
                    "With a shake of my head and wave of my hands, Markus returned to focusing solely on Mika as I slipped back out into the hallway."
                    MC @smile "(Well... Looks like Mika had nothing to worry about.)"
                    pass
        "Don't peek through the door.":
            "I decided it was probably best to give the two of them their privacy."
            pass
    jump event_markus_mika_rep_shared_jmr

### dbj sex scene
label event_markus_mika_rep_dbj_sexscene:
    $ EventMikaMarkusRepScenes().EventSeenTonight = True
    #######
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    $ LocSet("novaras_palam_dorm")
    $ StopSexFx()
    $ CharSetClothes("mika", "naked")
    $ CharSetClothes("markus", "naked")
    $ LocFlush()
    show mika at center
    show markus at cright_f
    with dissolve
    show mc at cleft with easeinleft
    
    "As I opened the door and entered inside, Mika abruptly stopped what she was doing upon hearing the door swinging open."

    hide mika
    show mika at blurin, center_f, shake

    MIKA @shock "[player_name!t]!"
    MIKA @lewd "Have you c-come to have some fun with me and Daddy again?"
    MARKUS @smile "I told you he couldn't resist your ass, girl."
    hide mika
    show mika at blurin, center
    MIKA @lewd "{i}*Giggles*{/i}"
    MIKA @lewd "...T-Take off your clothes."
    hide mika
    show mika at blurin, center_f
    MIKA @lewd "I've missed your cocks. ❤️"
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("mc", "naked")
    show mc at nod
    "Smirking, I stripped down naked and stood beside Markus."
    "Mika, eyes wide and cheeks burning red, twirled one of her pigtails with her finger as her eyes darted between us."
    MIKA @shock "...{i}Oh my.{/i}"
    "Mika gently bit down on her lower lip."
    MIKA @blush "T-Take a seat."
    hide mika
    show mika at blurin, center
    "Mika licked at her lips as she stared at the two dangling cocks in front of her."
    MIKA @lewd "I wanna d-drain you both dry!"
    scene black with dissolve
    "...On her knees, with our cocks in both of her hands Mika was trembling with burning lust."
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mika_double_bj_left_stroke_slow 
    with dissolve
    $ Pause()

    MIKA "S-So thick..."
    MIKA "So big..."
    MIKA "Mhmmm!"
    MARKUS "Ahhh! That's it, girl! Hrghh! Stroke our cocks!"
    MC "{i}*Grunts*{/i} Good girl, Mika..."

    scene mika_double_bj_right_stroke_slow 
    with dissolve
    $ Pause()

    "Mika's eyes briefly pulled away from the thick cocks in front of her to meet my eyes."
    MIKA "Mmm, will you review my progress here, too?"
    MC "That depends..."
    MC "{i}On how much you please us.{/i}"
    "Mika smiled before dipping her head forward onto my cock, wrapping her lips around it whilst she continued to stroke Markus."

    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
    scene mika_double_bj_right_suck_slow 
    with dissolve
    $ Pause()

    MC "Ahhh...!"
    MIKA "{i}*Slurp* *Slurp...*{/i}"
    MIKA "Mmmm, shoo bhigghh...❤️"
    MIKA "I chann bharleyhh fhithh ithhh inhh mhyhh mhouthh! {i}*Slurp!*{/i}"
    "Mika's head continued to gently move back and forth as she tried to take as much of my cock as she could."
    "Her head rocked forward, her sweet, wet lips gliding over my now glistening cock thanks to her saliva, her tongue nervously explored my cock, rubbing and wrapping against it."
    "With a loud *PLOP* sound, she smiled as she pulled her lips away from my member."
    
    scene mika_double_bj_right_suck_slow 
    with dissolve
    $ Pause()

    MIKA "{i}*Huff*{/i} Did I - {i}*Huff*{/i} pass your review?"
    MC "Mmm, a great start."
    MC "But I'm going to need to see more before I can tell you if your cock sucking skills are to my standards!"
    MARKUS "Allow me to assist!"
    "With a light pulling of Mika's head, she giggled as she wrapped her lips now around Markus' cock, sucking and dragging her lips down as she stroked my member."

    scene mika_double_bj_left_suck_slow
    with dissolve
    $ Pause()

    MIKA "{i}*Slurp!* *Slurp!*{/i} Mhhfhh!"
    MARKUS "Ahh! That's it, Mika!"
    MARKUS "Tell us how you love sucking our big cocks!"
    MIKA "Mhhfhh! Ihh Lhuvhhh {i}*Slurp!*{/i} shuckinghhh yhourhhh - Mhmmm! - bhighhh chockhhs! {i}*Slurp!*{/i} ❤️"
    "Mika's lips continued to glide over Markus's cock, coating it in her saliva as she tried to swallow as much of his {i}sword{/i} as she could."
    "Her hand continued to stroke at my cock whilst Markus groaned happily as her sweet mouth worked its magic on him."
    "After a few moments passed though, Mika's lips pulled away from Markus' cock, and she was giggling as she continued to stroke both of us once more."

    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mika_double_bj_right_stroke_slow
    with dissolve
    $ Pause()

    MIKA "{i}*Huff*{/i} W-what's a Palam mage to do?"
    MIKA "I'm - {i}*huff*{/i} s-sure Palam will understand! Fufu! ❤️"

    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
    scene mika_double_bj_left_suck_fast
    with dissolve
    $ Pause()

    "Mika's head moved from cock to cock, sliding down our members as she gagged and lightly choked on each one."

    scene mika_double_bj_right_suck_fast
    with dissolve
    $ Pause()

    "Her tongue thrashed and beat against each member as she fully became absorbed in her lust, her nervous nature seemingly numbed and vanished into nothing."
    "Instead, me and Markus were being serviced by a ferocious succubus, determined to suck us dry."

    scene mika_double_bj_left_suck_fast
    with dissolve
    $ Pause()

    MIKA "Ahhh! It's shooo ghood! Mhhhfh! I love it!"
    MIKA "I lhuvvhh yhourhhh chockkkss sliding dhownn my throattt shoo much!! ❤️"
    MIKA "Ghivhhh ithh to mheee!"

    scene mika_double_bj_right_suck_fast
    with dissolve
    $ Pause()

    MIKA "Cover yourhh little mage whore in all your seed!"
    MIKA "Make me beg for itthhh! ❤️"
    MARKUS "Oh godsss! Hrghhh! I'm... I'm going to finish!"
    "As I felt my balls begin to tighten and rise, I knew from my aching, now desperately sensitive cock, I was close to finishing as well."
    MC "M-Me too!"
    "Mika pulled back, opening out her mouth and letting her tongue flop out as she stroked the two of us enthusiastically."
    MARKUS "O-OOOH! FUCK!"
    MC "H-HRGHHHH!"
    "Unable to hold back any longer, I grunted loudly as I unleashed my hot load onto Mika's face and tongue."

    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")

    scene mika_double_bj_finish
    with flash
    $ Pause()

    $ ReduceInfectionFromSex("mika")
    $ UnlockGalSceneAndGrantXp("mika", "mika_double_bj")

    "Markus finished only a moment or two later, plastering Mika with another burst of his seed."
    "Mika, drunk on lust, continued to giggle and stroke us, making sure she'd thoroughly drained us for every last drop."
    "As the seed dripped down from her face onto her tits, her tongue swirled around her mouth to swallow as much of the seed as she could."
    MIKA "Mmm... You both taste so..."
    MIKA "Delicious. ❤️"
    MARKUS "Ahh... Mika and I are going to head to the baths and clean ourselves."
    MARKUS "I'll re-join you shortly once I'm clean."

    scene black with dissolve
    "As Mika rose to her feet, Markus playfully reached out to slap her butt."
    $ LocFlush()
    show mc at cleft
    show mika at center_f
    show markus at cright_f
    with dissolve

    MIKA "Eeeep!"
    MARKUS "Move your cute ass, girl!"
    MIKA "Mhmm, y-yes sir..."
    hide mika 
    hide markus
    with easeoutleft
    show mc at blurin, cleft
    show mc at center_f
    with ease
    show mc at blurin, center_f
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("mika", "dress")
    $ CharSetClothes("markus", "normal")
    show mc at nod
    scene black with dissolve
    "As the two of them left to head towards the baths, I re-dressed myself, heading out to carry on with the remainder of my evening."
    $ LocSet("novaras_palam_e_wing")
    return

####################################################################
###### threesome
### threesome click-in
label event_markus_mika_rep_threesome_click:
    MIKA "Ahhhh...! ❤️"
    "{i}*Plap!* *Plap!* *Plap!*{/i}"
    MARKUS "{i}*Groans*{/i}"
    MARKUS "Gods girl, are you tight!"
    show mc at cleft with easeinleft
    MC "(Those two are at it like rabbits again...)"
    MC "({i}...Hmmm.{/i})"
    MC "(Should I?)"
    menu:
        "Peek through the door.":
            scene black with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)
            scene mika_missionary_nopreg_vag_fast with dissolve
            $ Pause()
            "Peeking through the door, I found Mika in Markus' powerful arms, being raised and dropped onto his cock."
            MIKA "Hrhghh! Y-Yesshh! Mhmm!"
            MIKA "You're messing up m-my insides so much!"
            "Markus squeezed her bubbly blue ass as she continued to cry out euphorically."
            "Her tight pussy swallowed up Markus' large cock as the two of them were locked in their intense, passionate embrace."
            "Mika clawed at Markus' back, her legs tightly wrapped around him as he treated her body like a toy."
            MARKUS "F-Fuck! Are all mages of Palam like you!?"
            MIKA "Nghhhh! Mhmm! W-We're all so f-fucking horny all the time!"
            MIKA "Slam your cock into me, Daddy!"
            MIKA "M-Make me your little mage bitch!"
            "Markus, glancing over, could see me watching from the doorway."
            "Mika was far too preoccupied bouncing on his cock to notice much of anything, but Markus, smirking, waved to invite me in."
            menu:
                "Head inside.":
                    call event_markus_mika_rep_threesome_sexscene from _call_event_markus_mika_rep_threesome_sexscene
                "Shake your head.":
                    "Refusing Markus' offer, he nodded in acknowledgement, before turning his focus entirely back onto Mika."
                    MIKA "Oooooh! D-Daddy... Mhmm..."
                    MIKA "Don't stop! ❤️"
                    pass
        "Don't peek through the door.":
            "I decided it was probably best to give the two of them their privacy."
            pass
    jump event_markus_mika_rep_shared_jmr

### threesome sex scene
label event_markus_mika_rep_threesome_sexscene:
    $ EventMikaMarkusRepScenes().EventSeenTonight = True
    ##########
    $ PlaySoundRandom("woodenDoor")
    $ LocSet("novaras_palam_dorm")
    "At Markus' invite, I stepped into the room and closed the door behind me."
    "Mika, startled, still in Markus' arms, slightly squirmed when she noticed me entering."
    $ StopSexFx()
    $ CharSetClothes("mika", "naked")
    $ CharSetClothes("markus", "naked")
    $ LocFlush()
    show markus at cright_f
    show mika at center
    with dissolve
    show mc at left with easeinleft
    MIKA "A-Ahh! Have you come t-to join us again?"
    "Mika laughed as she licked her lips enticingly."
    MARKUS "Will that be a problem?"
    MIKA "N-Not at all! I love it when you both share me!"
    
    $ CharSetClothes("mc", "naked")
    $ PlaySoundRandom("tentFlap")
    show mc at blurin, nod

    "Markus flashed a bright grin as Mika's cheeks burned red as she watched me strip."
    MIKA "Mhmm! C-Careful though, l-last time was really intense!"
    MIKA "B-But I've trained my butt to handle you better now with some toys!"

    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene mika_threesome_dp_loop_slow 
    with dissolve
    $ Pause()

    "As I pushed the head of my cock against her tight rosebud, Mika's ass quickly gave way as she felt my cock stretch it out."
    MIKA "M-MY ASSSSSSHHH!!"
    ####
    "Mika howled in a mixture of pleasure and pain as she felt the two huge cocks stuff both of her holes."
    "Her tight, back tunnel squeezed my cock desperately."
    "Her body was immediately overwhelmed by the two huge cocks now sliding in and out of her stretched, defiled holes."
    MIKA "{i}*Huff*{/i} I luhvhh yhouuu! I lhuvvv yourhh chockkhhss!! {i}*huff*{/i}"
    "Mika's insides felt amazing, wedged between me and Markus; we treated her body like some kind of toy, mercilessly ramming our cocks into her drenched holes."
    MARKUS "Hrghh! Your pussy feels like it was built for my - Ahh! Cock!"
    MARKUS "How's her ass feel, [player_name!t]?"
    MC "H-Hrghh! She's - Mhmm! T-Tight!"
    MC "Her ass feels like it's - Ahh! Moulding around my cock!"
    MARKUS "Haha! Hear that slut?"
    MARKUS "Keep shaking that ass!"

    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)
    scene mika_threesome_dp_loop_fast 
    with dissolve
    $ Pause()

    MIKA "Mhhfhhhhhhhh....!! ❤️"
    "Mika seemed almost delirious, her eyes rolling to the back of her skull as she did as she was told, shaking her little blue ass on command."
    MIKA "F-Feel so - Mhhfhhh!"
    MIKA "S-Stuffed! ❤️"
    "Mika's tongue flopped out of her mouth as the two of us continued slamming our cocks into her."
    "Her tight holes squeezed and convulsed, seemingly as Mika experienced wave after wave of her own climaxes."
    "Her toes curled as she slurred out her lewd, desperate moans."
    MIKA "C-Cummmhh inhhh mheee!"
    MIKA "F-Fhill mheee uphh likeee ahhh whoreee!! ❤️"
    MARKUS "Grghh! You heard her! Ahh!"
    MARKUS "I-I'm close! I'm gonna..."
    "Markus grunted, tightening his grip around Mika as he flooded her womanhood with his load."
    "Mika's sudden gasp and tightening around me as she shook with a powerful orgasm was enough to tip me over the scales as well."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    scene mika_threesome_dp_finish
    with flash
    $ Pause()

    $ ReduceInfectionFromSex("mika")
    $ UnlockGalSceneAndGrantXp("mika", "mika_threesome")

    "With a grunting, animal-like 'Hrghhh!' sound, I poured my own thick, hot load into Mika's rectum."
    MIKA "A-Ahhhhhhh...! ❤️"
    "Mika shivered and trembled as we did so, her stomach lightly bulging from the sheer volume of cum being pumped into her."
    MIKA "G-Ghhhh!!"
    MC "Hrghh! T-Take it all, Mika!"
    "Eventually, with every last drop pumped into Mika, drenched in sweat, we slowly lowered Mika back onto the floor." 

    scene black with dissolve
    "Her feet touched the ground, but in a moment, she collapsed onto her back, our cum seeping from both her holes. "
    MC "Mika!"

    $ CharSetClothes("mc", "naked")
    $ CharSetClothes("markus", "naked")

    $ LocFlush()
    show mc at cleft
    show markus at cright_f
    with dissolve

    MIKA "F-Fine... {i}*Huff*{/i} Just n-need... {i}*Huff*{/i}"
    MIKA "...Rest."
    "Markus' eyes looked up to meet mine."
    MARKUS "...Wanna grab some ale over at the Iron Unicorn?"
    MC "Sure."
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("markus", "normal")
    $ CharSetClothes("mika", "dress")
    "The two of us got dressed and left a quivering, content Mika on the floor."
    MIKA "M-Mmm... ❤️"
    $ LocSet("novaras_palam_e_wing")
    return

### all paths jmr?
label event_markus_mika_rep_shared_jmr:
    $ AutoMus(True)
    $ LocEnter()

