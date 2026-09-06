label fortress_inn_lucy_firsttime:
    $ EventFortressInn().SeenFirstTimes[EventFortressInn().VariantID] = True
    show mc at left with easeinleft
    "As the doors swung open, a mousey-haired, fair maiden hurried over."
    show lucy at center with dissolve
    LUCY @happy "H-Hello!"
    LUCY @happy "Welcome to {i}The Cat at Sundown!{/i}"
    LUCY @happy "I'm Lucy, and this is Johan."
    LUCY @talk "Just take a seat and call me over if you need anything!"
    jump fortress_inn_lucy_talk_menu

####### Lucy
label fortress_inn_lucy_talk:
    show lucy at center
    LUCY @talk "Y-Yes?"
    menu fortress_inn_lucy_talk_menu:
        "I'd like to order something.":
            LUCY @shock "O-Of course!"
            LUCY @happy "What would you like?"
            menu:
                "I'd like an ale, please." (Req_Gold = 30):
                    $ PlayerRemItem("gold", 30)
                    LUCY @talk "A-Alright!"
                    "Lucy hurried away before returning with a frothing mug of ale, which she carefully placed in front of me."
                    $ EventFortressInn().GetDrink()
                    LUCY @happy "Here you go!"
                    LUCY @blush "L-Let me know if you need anything else!"
                "Any food?" (Req_Gold = 55):
                    $ PlayerRemItem("gold", 55)
                    LUCY @talk "T-There's some rabbit stew and vegetables today."
                    LUCY @talk "I-I'll bring it over now!"
                    scene black with dissolve
                    $ TimeAdvBy(TIME_1H)
                    "A short while later, Lucy returned with a loaf of bread and a steaming bowl of rabbit stew with vegetables."
                    $ EventFortressInn().GetFood()
                    $ LocFlush()
                    show lucy at center
                    with dissolve
                    LUCY @happy "E-Enjoy! It's really good! I promise!"
                    "Taking a spoonful, it was indeed very good."
                "Nothing for now.":
                    LUCY @talk "A-Alright! Umm, I have to tend to some other tables."
                    LUCY @blush "L-Let me know if you need anything!"
            jump fortress_inn_lucy_talk_menu
        "How does a girl end up working in a place like this?":
            LUCY @blush "T-The GTC usually offers these jobs to pretty girls from villages."
            LUCY @blush "I guess they thought I was pretty enough to work at this one."
            MC @sad "It must be tough being away from your family in a place like this."
            LUCY @talk "Y-Yes, but... Places like these pay really well!"
            LUCY @talk "I can m-make enough money to send back home and help my family!"
            LUCY @happy "F-Father may even be able to buy a second farm soon!"
            MC @think "When do you get to return home?"
            LUCY @talk "A-After six months, we return home and a new girl takes our place."
            LUCY @talk "S-Some girls choose to stay at the same inn, while others are offered coin to move somewhere else."
            LUCY @talk "It's a lot of coin... for a peasant, anyway."
            jump fortress_inn_lucy_talk_menu
        "How is the baby?"  (AppearIf = CharGetBirths("lucy") > 0):
            LUCY @happy "H-He's fine!"
            LUCY @happy "Growing up so fast!"
            LUCY @think "... Maybe a little too fast?"
            LUCY @shock "I've n-never seen a baby say his first words so quickly!"
            jump fortress_inn_lucy_talk_menu
        "Do you provide any... {i}'special services?'{/i}" (AppearIf = (EventFortressInn().ScheduledFuntime == False)):
            "Lucy's face burned bright red as she stuttered out her answer."
            LUCY @blush "Y-Yes! Uhh!"
            LUCY @blush "W-We d-do!"
            LUCY @blush "Umm... I-Is that something you'd l-like?"
            menu:
                "With you? Yes.":
                    LUCY @blush "I... If..."
                    LUCY @blush "If that's what you want, I can v-visit your room tonight."
                    LUCY @blush "S-Should you choose to stay here, that is."
                    $ EventFortressInn().ScheduledFuntime = True
                "No.":
                    LUCY @blush "A-Alright."
                    LUCY @blush "Let me know if there's anything else I can help you with."
            jump fortress_inn_lucy_talk_menu
        "I best get going...":
            LUCY @happy "S-Safe travels!"
            $ LocEnter()

###### Johan
label fortress_inn_johan_talk:
    show cg_johan at center with dissolve
    JOHAN @talk "Drinks and food, speak to Lucy."
    JOHAN @talk "Anything else, you talk to me."
    menu fortress_inn_johan_talk_menu:
        "I'd like a room for the night, please." (AppearIf = (EventFortressInn().BoughtKey == False)):
            JOHAN @talk "Two fifty."
            menu:
                "{i}*Pay the coin*{/i}" (Req_Gold = 250):
                    $ PlayerRemItem("gold", 250)
                    $ EventFortressInn().BoughtKey = True
                    "Johan reached over and handed me an old, worn key."
                    JOHAN @talk "Second door on the left."
                    $ LocEnter()
                "On second thought...":
                    JOHAN @think "Got something else you wish to discuss instead?"
                    jump fortress_inn_johan_talk_menu
        "Nothing for now.":
            JOHAN @talk "Enjoy your stay."
            $ LocEnter()

label fortress_inn_lucy_night:
    $ TimeAdvBy(TIME_05H)
    $ LocSet("fortress_inn_room")
    "{i}*Knock* *Knock*{/i}"
    $ PlaySound(audio.door_knock)
    $ Pause(0.5)
    $ LocFlush()
    show mc at right_f
    with dissolve
    LUCY @talk "H-Hello... Can I come in?"
    show lucy at cleft with easeinleft
    MC @talk "Enter."
    "The door creaked open as Lucy sheepishly stepped inside."
    LUCY @blush "Y-You asked me to join you, sir?"
    "Lucy hesitated for a moment, almost too embarrassed to tell me her prices."
    LUCY @blush "I-Um..."
    LUCY @blush "M-My mouth is two hundred. My... My..."
    LUCY @blush "W-Woman parts are four hundred."
    LUCY @blush "And... and..."
    MC @think "... Your ass?"
    LUCY @blush "S-Six fifty, sir."
    "Lucy's face burned bright red by the time she'd finished listing her prices."
    menu:
        "I'll take your mouth." (Req_Gold = 200):
            $ PlayerRemItem("gold", 200)
            label replay_lucy_bj:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            LUCY @shock "My mouth?!"
            LUCY @blush "I mean, umm... Yes. A-Alright."
            LUCY @blush "P-Please, um..."
            LUCY @blush "U-Undress and lie down on the bed, and I'll t-take care of you."
            $ PlaySexFx(audio.ves69_150, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_bj_preg_1
            else:
                scene lucy_bj_nopreg_1
            with dissolve
            $ Pause()
            "Lying on the bed, I watched as a naked Lucy carefully lowered herself beside me."
            "My hard cock stood proudly before her."
            LUCY "I-I'll begin now! A-Alright?"
            "Lucy hesitated for a moment before shyly parting her lips and carefully taking the head of my cock into her mouth."
            if CharIsVisiblyPreg("lucy"):
                scene lucy_bj_preg_2
            else:
                scene lucy_bj_nopreg_2
            with dissolve
            $ Pause()
            LUCY "Mmfghh..."
            "Her lips glided back and forth."
            "Slowly at first, but as she grew more comfortable, she took a few more inches."
            LUCY "{i}*Slurp* *Slurp*{/i}"
            LUCY "Ishhthishh ghoodhh?"
            MC "Ahh!"
            MC "Yes, you're doing well!"
            MC "Go on now, faster, girl!"
            if CharIsVisiblyPreg("lucy"):
                scene lucy_bj_preg_3
            else:
                scene lucy_bj_nopreg_3
            with dissolve
            $ Pause()
            "Encouraged by my words, Lucy tried to take a little more."
            "Her head bobbed on my cock as her warm saliva coated my member, her lips forming a tight seal."
            LUCY "Mmfghh! {i}*Slurp!*{/i} Y-Yheshhshirr! {i}*Slurp!*{/i}"
            "Lucy lacked experience. That much was clear from her apprehension."
            "But as her tongue twisted around my cock without any real technique,"
            "she more than made up for it with enthusiasm."
            "Eventually, I found myself drawing closer and closer to the edge until..."
            MC "C-Cumminggg!!"
            $ ReduceInfectionFromSex("lucy")
            if CharIsVisiblyPreg("lucy"):
                $ UnlockGalFlag("lucy", "bj", "var_preg")
            else:
                $ UnlockGalFlag("lucy", "bj", "var_nopreg")
            $ UnlockGalSceneAndGrantXp("lucy", "bj")
            $ PlaySexFx(audio.ves69_finish)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_bj_preg_cum
            else:
                scene lucy_bj_nopreg_cum
            with flash
            $ Pause()
            "Lucy's eyes widened as she squealed in surprise, letting out a little 'Mmfghh?!' sound."
            "As I fed her my thick load, she closed her eyes and dutifully swallowed as much of it as she could."
            "Gently, I stroked the back of her head, and once she finished swallowing the last of my seed,"
            "she pulled her lips free with a *PLOP* and took a deep breath."
            LUCY "D-Did I do good?"
            MC "You did— {i}*Huff*{/i} Very well, Lucy."
            "Wiping her mouth, Lucy climbed from the bed and gathered her clothes."
            "She gave me a small, polite bow."
            LUCY @blush "P-Please enjoy the rest of your time with us, sir."
            $ StopReplay()
            scene black with dissolve
            "Lucy scarpered out of the room, quietly closing the door behind her."
            MC @smile "(Cute.)"
        "I'll take your womanhood." (Req_Gold = 400):
            $ PlayerRemItem("gold", 400)
            label replay_lucy_sidefuck_vag:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            LUCY @shock "MY-"
            "She stopped herself, staring for a few moments before slowly... very slowly... beginning to strip off her clothes."
            "They slipped from her body and fell to the floor as she answered with a shaky breath."
            LUCY @blush "Y-Yes, sir."
            scene black with dissolve
            "... A few minutes later."
            $ PlaySexFx(audio.nijah_miss_1, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_vag_1
            else:
                scene lucy_sidefuck_nopreg_vag_1
            with dissolve
            $ Pause()
            LUCY "B-Be gentle..."
            LUCY "{i}Please?{/i}"
            "Rubbing my cock against her wet, tight pussy, Lucy let out a trembling, stifled moan in anticipation."
            MC "Are you ready?"
            "She nodded anxiously."
            LUCY "Y-Yes, please."
            $ PlaySexFx(audio.nijah_miss_2, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_vag_2
            else:
                scene lucy_sidefuck_nopreg_vag_2
            with dissolve
            $ Pause()
            "As I pushed against her entrance, Lucy let out a silent gasp, her body tensing as she felt my member slide inside her."
            "Her warm, tight wetness squeezed around me as I slowly began to fuck her."
            LUCY "A-Ahh..."
            LUCY "It feels so..."
            LUCY "Mhmm... {i}G-Good.{/i}"
            MC "Gods, girl... Are you sure you aren't a virgin?"
            LUCY "N-No, sir..."
            LUCY "J-Just tight."
            LUCY "Mmmfghh...!"
            LUCY "A-And you're very, {i}very,{/i} big."
            MC "Ahh! Are you ready for more?"
            LUCY "Y-Yes..."
            LUCY "G-Give me more, please!"
            $ PlaySexFx(audio.nijah_miss_3, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_vag_3
            else:
                scene lucy_sidefuck_nopreg_vag_3
            with dissolve
            $ Pause()
            "I moved faster, slamming into her tight hole as she moaned happily."
            "The bed creaked as the frame struck the wall, loud enough that I wondered if it might disturb the other guests."
            LUCY "Y-Yes! YES!"
            LUCY "P-Please! It f-feels so good!"
            LUCY "D-Don't stop!"
            LUCY "O-Oooh! You're s-so strong..."
            "She giggled softly as I continued to have my way with her."
            LUCY "I feel so small in your arms!"
            "Lucy's eyes began to roll back as I slammed into her."
            "She trembled and shook as time went on."
            LUCY "Ahh...!"
            LUCY "C-Cum in me, please!"
            LUCY "I want us to cum together!"
            LUCY "CUM WITH ME!"
            "Something about her desperate plea pushed me over the edge."
            "Burying my cock deep inside her, I held her tightly as I emptied my balls into her welcoming snatch."

            if not QstIsActive(PregFortressInnLucy):
                $ QstStart(PregFortressInnLucy)
            $ PregRoll("lucy")
            $ PlaySexFx(audio.nijah_miss_finish)
            $ ReduceInfectionFromSex("lucy")
            if CharIsVisiblyPreg("lucy"):
                $ UnlockGalFlag("lucy", "sidefuck", "var_preg_vag")
            else:
                $ UnlockGalFlag("lucy", "sidefuck", "var_nopreg_vag")
            $ UnlockGalSceneAndGrantXp("lucy", "sidefuck")

            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_vag_cum
            else:
                scene lucy_sidefuck_nopreg_vag_cum
            with flash
            $ Pause()

            MC "HRGHHHH!"
            LUCY "Y-Yes! Mmmfghh! That's it!"
            LUCY "S-Shhh...!"
            LUCY "L-Let it all out... It's alright!"
            "I could feel her hand stroking the back of my hair as I lay beside her, breathing heavily for a while."
            "After a while, she slowly climbed from the bed and gathered her clothes from the floor."
            LUCY @talk "G-Goodnight, sir."
            $ StopReplay()
            scene black with dissolve
            "With that, she quietly left my room, gently closing the door behind her."
        "I'll take your ass."  (Req_Gold = 650):
            $ PlayerRemItem("gold", 650)
            label replay_lucy_sidefuck_anal:
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            "Lucy's eyes widened as she gulped, her cheeks burning red as she whimpered."
            LUCY @blush "M-My butt?"
            "Lucy carefully and sheepishly undressed, letting her clothes fall to the floor as she stood naked before me."
            LUCY @blush "... A-Alright, umm... Just give me a few minutes."
            LUCY @blush "P-Please, get on the bed and prepare yourself."
            scene black with dissolve
            "{i}... A short while later.{/i}"
            $ PlaySexFx(audio.nijah_miss_1, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_anal_1
            else:
                scene lucy_sidefuck_nopreg_anal_1
            with dissolve
            $ Pause()
            "Lying on her back, with my cock teasingly prodding against her tight backdoor,"
            "Lucy let out cute little whimpers as I teased her endlessly."
            "Her pussy glistened in the dim light with excitement as she waited anxiously for what was to come."
            MC "Are you ready?"
            LUCY "Y-Yes... I'm ready for you down t-there."
            "Pushing against her sphincter, the tight rosebud slowly gave way as I eased a few inches into her ass."
            $ PlaySexFx(audio.nijah_miss_2, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_anal_2
            else:
                scene lucy_sidefuck_nopreg_anal_2
            with dissolve
            $ Pause()
            "She gasped, doing her best to relax as her ass squeezed around my cock."
            LUCY "G-GODSSS!"
            MC "Ahh! Relax, girl!"
            MC "Before you snap my cock off!"
            LUCY "{i}*Huff*{/i} I'm... {i}*Huff*{/i} trying!"
            "As I moved in and out of her ass, Lucy trembled with every shaky breath."
            "Her ass, though, was incredibly tight."
            LUCY "Y-You're in... You're in my butt."
            LUCY "W-With your— Eeeep!"
            LUCY "B-Big thingy!"
            "I couldn't help but laugh reassuringly, doing my best to soothe the girl as I had my way with her."
            LUCY "It's not-"
            LUCY "A-Ahh! F-Funny!"
            MC "Are you ready for more?"
            LUCY "Ooooh..."
            "Lucy nodded, sweat dripping from her brow as her body glistened in the dim light."
            LUCY "T-Thank you."
            LUCY "For being c-considerate."
            $ PlaySexFx(audio.nijah_miss_3, 1)
            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_anal_3
            else:
                scene lucy_sidefuck_nopreg_anal_3
            with dissolve
            $ Pause()
            "I began to move faster as her moans grew louder."
            "Her stretched ass still squeezed around me, but she had begun to relax and adjust to the invading member in her rear."
            MC "Mhmm... Have you— Ahh! Practised with-"
            LUCY "N-Nooo!"
            LUCY "I-It's too embarrassing!"
            LUCY "I already feel like I'm going to die knowing you're back there!"
            MC "Your moans say otherwise."
            LUCY "I-"
            LUCY "Ooooh..."
            LUCY "S-Sir, please... I would d-die if anyone knew I l-liked this."
            "I slammed my cock deeper, my heavy balls growing more desperate to flood her ass with my seed."
            MC "Oh, finally being honest, huh?"
            LUCY "T-The act itself is a-alright..."
            LUCY "B-But... Mmmfhh..."
            LUCY "I-It's just so..."
            LUCY "{i}N-Naughty.{/i}"
            "Something about her words stirred something inside me."
            "As I continued to pound her tight ass, Lucy's moans grew louder and more restless."
            MC "Grghh! I'm going to fill your ass up!"
            LUCY "A-Ahh!"
            LUCY "A-Alright! Mhhfghh! D-Do it!"
            LUCY "P-Please! Use me! USE ME TILL YOU'RE HAPPY!"
            "Burying my cock to the hilt,"
            $ PlaySexFx(audio.nijah_miss_finish)
            $ ReduceInfectionFromSex("lucy")

            if CharIsVisiblyPreg("lucy"):
                $ UnlockGalFlag("lucy", "sidefuck", "var_preg_anal")
            else:
                $ UnlockGalFlag("lucy", "sidefuck", "var_nopreg_anal")
            $ UnlockGalSceneAndGrantXp("lucy", "sidefuck")

            if CharIsVisiblyPreg("lucy"):
                scene lucy_sidefuck_preg_anal_cum
            else:
                scene lucy_sidefuck_nopreg_anal_cum
            with flash
            $ Pause()

            "I held Lucy tightly as I poured my thick load into her."
            MC "GRGHHHH!!"
            LUCY "AHHHH...!"
            "As our bodies relaxed, she soothingly stroked the back of my head."
            LUCY "That was... {i}*Huff*{/i}"
            "Lucy brushed a few strands of hair from her face as she slowly rose to her feet."
            "With shaky legs, she carefully gathered her clothes into her arms."
            LUCY "I-If that will be all, sir."
            LUCY "P-Please enjoy your stay."
            $ StopReplay()
            scene black with dissolve
            "As Lucy turned to leave, I playfully reached out and swatted her cute ass."
            LUCY @shock "EEEEEP!"
            "She hurried out the door as I laughed."
            MC @smile "(Far too cute to be working in a place like this.)"
        "On second thought...":
            $ AutoMus(False)
            stop music fadeout 0.1
            $ PlaySound(audio.scratch_stop)
            LUCY @sad "O-Oh... Y-You don't want me anymore?"
            LUCY @sad "A-Alright... I'll leave you be tonight."
            hide lucy with dissolve
            scene black with dissolve
    $ AutoMus(True)
    return

##############################
####### lucy
label fortress_inn_lucy_impreg:
#######Lucy impreg scene (first/rep)
    $ PregFortressInnLucy().ShareImpregNews = False
    show mc at cleft with easeinleft
    show lucy at cright_f with easeinright
    "No sooner had I entered than Lucy approached me sheepishly, her hands resting on her belly."
    "My eyes drifted down towards it as I almost instinctively sensed the change."
    LUCY @sad "U-Umm... Can we talk?"
    "Her eyes cautiously swept around the inn as she stepped closer."
    LUCY @sad "I-I'm pregnant."
    if PregFortressInnLucy().NumImpregs == 1:
        MC @surprised "And it's definitely mine?"
        "She nodded nervously."
        LUCY @sad "D-Definitely."
        LUCY @sad "I umm... W-wasn't with anyone after you for a while, a-and I noticed..."
        LUCY @blush "Y-You know..."
        "She squirmed on the spot for a moment."
        LUCY @blush "D-Don't worry. I umm... I don't want to make a fuss."
        LUCY @blush "Umm, I knew this sort of thing {i}might{/i} happen eventually."
        LUCY @happy "T-The Blood Moon must not have worked, h-ha..."
        "She scratched at her cheek."
        LUCY @blush "I-If you wanted to, though..."
        LUCY @blush "M-Maybe you'd like to visit my village sometime?"
        LUCY @blush "Umm..."
        LUCY @happy "I l-live at Locksworth!"
        LUCY @blush "I-It would be really nice if you could stop by sometime."
        LUCY @blush "T-That's all I had to say..."
    else:
        #Repeat variant
        LUCY @blush "{i}A-Again...{/i}"
        MC @surprised "... Mine?"
        "She nodded frantically."
        LUCY @blush "I-It feels too good with you."
        "Lucy buried her face in her hands."
        LUCY @blush "I know I should do better, but I keep letting you cum inside!"
        LUCY @blush "It's all my fault!"
        MC @sad "{i}*Sigh*{/i}"
        MC @think "Do you need anything?"
        LUCY @talk "I... I'll be alright."
        LUCY @blush "I know you still have lots of adventures and things to do."
        LUCY @blush "Y-You Guild types are always so busy, haha!"
        LUCY @happy "B-But, uhh! It would be really nice to see you at my village of Locksworth sometime!"
        LUCY @blush "I-If you can find the time, that is."
        LUCY @talk "A-Anyway, I better get back to cleaning tables."
        LUCY @talk "P-Please call me over if you need anything!"
        "Her hand tenderly brushed against mine as she slipped past."
    #Both continued
    hide lucy with easeoutleft
    "Without another word, Lucy returned to serving drinks at the other tables."
    show mc at center with ease
    MC "(Locksworth, huh?)"
    $ LocEnter()

####### After giving birth
label fortress_inn_lucy_postbirth:
    $ PregFortressInnLucy().DoBabyScene = False
    show mc at cleft with easeinleft
    show lucy at cright_f with easeinright
    LUCY @happy "I-IT'S YOU!"
    LUCY @happy "I mean, umm... L-Look!"
    LUCY @happy "Isn't he adorable?"
    "A small baby, wrapped snugly in cloth, gurgled in Lucy's arms, laughing cutely as she tickled his nose."
    LUCY @blush "Umm... S-Say, what do you think of the name..."
    $ PregFortressInnLucy().BabyName = renpy.input(_("What shall we call her?"), default = _("Viska"))
    LUCY @happy "A-Alright, I'll think on it!"
    LUCY @happy "I g-gotta feed this little one, umm... J-Just call me over in a minute if you need anything!"
    $ LocEnter()
