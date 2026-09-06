label qst_the_lovers_path_meet_1:
    show mika at center with dissolve
    MIKA @smile "N-No more light sparring!"
    "Mika clenched her fists and raised them confidently to her chest."
    MIKA @smile "I can do this!"
    menu:
        "{image=[ICON.SWORDS]} Let's do this!": #Player battles Mika
            "L-Let's go!"
            #player battles Mika - if player loses 
            $ TimeAdvBy(TIME_2H)
            hide mika 
            with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            $ AutoMus(True)
            $ LocFlush()
            show mc at left
            with dissolve
            show mika at center_f
            with dissolve
            if LastBattleOutcome == "defeat":
                MIKA @smile "I did it! I won!"
                MIKA @smile "I can't believe I actually won!"
                MC @smile "Ahh... Well done, Mika."
            else:
                #If player wins 
                MIKA @scared "{i}*Huff* ...*Huff*{/i} "
                MIKA @scared "So ... {i}*Huff*{/i} close!"
                MC @smile "You did very well, Mika."
            #Both variants continued 
            MIKA @blush "Sooooo..." 
            show mika:
                linear 0.2:
                    xoffset -350
                nod
            "Mika, with a bounce in her step, moved closer towards me, her hands gently resting on my chest."
            MIKA @blush "B-Because I did so well."
            MIKA @blush "H-How about a reward?"
            MC @smile "A reward?"
            MC @smile "What would you like?"
            MIKA @blush "M-Maybe we could start with a kiss?"
            "Mika nervously twirled her hair."
            MIKA @blush "Around here, I've only ever kissed other Mages; I wanna know if it feels different to kiss a man."
            hide mc
            show mc at left
            with dissolve
            "Leaning closer towards Mika, her breathing became heavier as she nervously tilted her lips towards mine."
            MIKA @blush "Do ... Do you want me to-"
            $ LocFlush()
            show cg_mc_mika_kiss:
                left
                yoffset 60
            with dissolve
            "Pulling her in, Mika let out a soft moan in surprise before sinking into the kiss." #Mika MC kiss 
            "Her soft lips pressed against mine, her tongue entwining with mine as my hands fondled at her soft, cute ass."
            "After a few moments of enjoying her warm body pressed up against mine, Mika reluctantly pulled herself away."
            "She looked breathlessly towards me."
            $ LocFlush()
            show mc at left
            show mika:
                center
                xzoom -1.0
            with dissolve
            MC @lewd "Was it different?"
            MIKA @lewd "Mhmm..."
            MIKA @lewd "Your hands are ... {i}bigger{/i} than a girl's hands."
            hide mika
            show cg_mika_boner:
                yoffset 30
                center
                xzoom -1.0
            with dissolve
            "Noticeably, something was pushing against the fabric of Mika's dress." #Mika hard-on wearing a dress 
            $ CharSetClothes("mika", "boner")
            hide cg_mika_boner
            show mika:
                center
                xzoom -1.0
            "Upon looking down to realise what I was looking at, Mika blushed once again, turning her back to me."
            MIKA @shock "I- I'm sorry! I didn't mean for it to-"
            MC @talk "Mika, it's fine. I have one myself; I understand how it works."
            MIKA @blush "I - I need to go!"
            show mika:
                center
                xzoom 1.0
            with dissolve
            hide mika with moveoutright
            show mc:
                linear 0.2:
                    xoffset 400
            MC @surprised "Mika! Wait!"
            "I reached out to grab her, but Mika was already gone."
            MC "(Hm ... Perhaps next time she'll be more bold?)"
            $ CharSetClothes("mika", "dress")
            $ QstSetProgress(QstTheLoversPath, 1)
            $ QstSetDelay(QstTheLoversPath, 1)
            $ LocEnter()
        "I have some other business I need to attend to first.":
            MIKA @talk "I see; well, let me know when you are free." #Ends convo
            $ LocEnter()

label qst_the_lovers_path_meet_2:
    show mika at center with dissolve
    MIKA @blush "H-Hello."
    MC @talk "Good morning, Mika. Ready to continue?"
    MIKA @blush "Um, before we do."
    MIKA @blush "I just wanted to say sorry about running off the other day like that."
    MC @smile "It's fine, honestly."
    MIKA @blush "You kinda made me feel all funny..."
    MIKA @shock "Don't get me wrong!"
    "Mika added hastily." 
    MIKA @blush "Messing around with other mages is one thing, but I've never felt like that."
    "Smiling at Mika only made her blush more; nervously, she coughed and tried to change the subject."
    MIKA @blush "So, um, are we to spar again?"
    menu:
        "{image=[ICON.SWORDS]} Let's spar.":
            MIKA @blush "B-Before we do that!"
            MIKA @smile "How about we make it a little more {i}interesting?{/i}"
            MC @think "Go on?"
            "Mika shyly rubbed her hands together."
            MIKA @blush "I-If I win."
            MIKA @blush "You have to let me..."
            "Mika brushed her hair over her shoulder as her blush deepened."
            MIKA @blush "L-Let me do something to you."
            "Mika's eyes kept glancing back and forth from the floor towards me."
            MC @think "And if I win?"
            MIKA @blush "Y-You can do whatever you want {i}to me.{/i}"
            MC @smile "...Very well."
            "Mika politely bowed, taking her position for the sparring match to begin again."
            MIKA @angry "{i}Have at you then!{/i}"
            $ TimeAdvBy(TIME_2H)
            hide mika 
            with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            $ AutoMus(True)
            $ LocFlush()
            show mc at left
            show mika:
                center
                xzoom -1.0
            with dissolve
            if LastBattleOutcome == "defeat":
                #Mika successfully wins 
                MIKA @shock "I ... {i}*Huff*{/i} I did it!"
                "I clambered back to my feet, brushing myself off."
                MC @smile "Ah, nicely done, Mika."
                show mika:
                    center
                    xzoom -1.0
                    linear 0.2:
                        xoffset -340
                $ Pause(0.2)
                show mc at shake
                MC @smile "Now, what reward was you-"
                hide mc
                hide mika
                show cg_mc_mika_kiss:
                    left
                    yoffset 60
                with dissolve
                "Mika leapt into my arms, passionately pressing her lips against me as I reached around to grab hold of her ass, holding her up in my arms."
                MIKA "Mhmm..."
                "She slipped her hot tongue into my mouth without a moment's hesitation, twisting and joining it with mine as her hot breath touched my cheek."
                "Slowly, she lowered herself from my arms back onto the ground."
                show mc:
                    left
                show mika:
                    center
                    xzoom -1.0
                    xoffset -340
                hide cg_mc_mika_kiss
                with dissolve
                MIKA @blush "You have no idea how long I've wanted to do that."
                MC @surprised "Well, that was quite a pleasant surprise."
                hide mika
                show mika:
                    center 
                    xzoom -1.0
                with dissolve
            else:
                #Player successfully wins 
                MIKA @shock "Ah!"
                MIKA @sad "So close!"
                MC @smile "You did well, Mika."
                "Unsure of herself, Mika took a few shaky steps closer towards me, placing her hands on my chest."
                MIKA @blush "W-Well, a bet's a bet."
                MIKA @blush "What do you want me to do?"
                menu:
                    "Ask for a kiss.":
                        MIKA @shock "W-What are you-"
                        show mc:
                            left
                            linear 0.2:
                                xoffset 340
                        $ Pause(0.2)
                        show mika at shake
                        MIKA @shock "{i}...Oh!{/i}"
                        hide mc
                        hide mika
                        show cg_mc_mika_kiss:
                            center
                            yoffset 60
                        with dissolve
                        "Gently, I reached around Mika's waist and pulled her closer to me, pressing a sweet kiss against her tender lips."
                        "I fondled and played with her soft bubbly ass as I slipped my tongue into her hot mouth."
                        "Like a plaything for me, she moaned sweetly as her tongue thrashed and entwined with mine."
                        "She let out a soft moan as she pulled back, her hot breath touching my face as she reluctantly pulled away."
                        show mc:
                            left
                            xoffset 340
                        show mika:
                            center
                            xzoom -1.0
                        hide cg_mc_mika_kiss
                        with dissolve
                        MIKA @blush "T-That was very nice..."
                        hide mc with dissolve
                        show mc at left with dissolve
                    "Ask Mika to show you her tits.":
                        "Mika blinked in surprise."
                        MIKA @shock "H-Here?"
                        MIKA @shock "{i}Now?{/i}"
                        MIKA @sad "B-But, someone might see!"
                        MC @smile "That's part of the fun."
                        "Blushing, Mika sheepishly looked around for anyone who might be watching before she undid her mage robes, presenting her bare tits to me."
                        hide mika
                        show cg_mika_bare_tits:
                            center
                            xzoom -1.0
                        show mc at left
                        with dissolve
                        $ CharSetClothes("mika", "bare_tits")
                        hide cg_mika_bare_tits
                        show mika blush at center:
                            center
                            xzoom -1.0
                        show mika blush:
                            center
                            xzoom -1.0
                            linear 0.2:
                                xoffset -200
                        $ Pause(0.2)
                        "As my eyes wandered over her chest, Mika's cheeks flushed red as she stepped closer towards me."
                        MIKA @blush "{i}D-Do you like them?{/i}"
                        MC @smile "Very much so."
                        "My comment brought a shy, blushing smile across Mika's face."
                        MIKA @blush "Really?"
                        MIKA @blush "That's ... {i}good to know.{/i}"
                        "After letting me stare for a few more moments, Mika covered herself again."
                        show mika blush:
                            center
                            xoffset -200
                            xzoom -1.0
                            linear 0.2:
                                xoffset 0
                        $ Pause(0.2)
                        show cg_mika_bare_tits:
                            center
                            xzoom -1.0
                        hide mika
                        with None
                        $ CharSetClothes("mika", "dress")
                        show mika:
                            center
                            xzoom -1.0
                        hide cg_mika_bare_tits 
                        with dissolve
                        MIKA @blush "T-That'll do for now, I think."
                    "Ask Mika to show you her ass.":
                        "Mika's whole face seemed to turn bright red at the suggestion."
                        MIKA @shock "M-My butt?"
                        MIKA @shock "B-But-!"
                        MC @smile "Why wouldn't I want to look at your ass?"
                        MIKA @shock "I-"
                        MIKA @sad "Do you really want that?"
                        MIKA @sad "I mean, you'll see my..."
                        "Mika paused, staring into my expectant eyes."
                        MIKA @sad "No... I trust you."
                        "Letting out a nervous sigh, Mika turned around, gripping the sides of her mage dress."
                        MIKA @sad "A-Alright, here I go..."
                        hide mika
                        show cg_mika_ass:
                            yoffset 15
                            center
                        with dissolve
                        "Closing her eyes, Mika crunched her face as though awaiting some terrible, cruel rejection."
                        "She rolled up the dress and bent forward, presenting me her cute, round ass."
                        MC @surprised "Well, {i}I hope I have a chance to see that more often.{/i}"
                        "My comment made Mika open her eyes as she looked back over her shoulder towards me in surprise."
                        MIKA "Y-You really like it?"
                        MC @smile "I do."
                        MC @smile "{i}But those panties are in the way.{/i}"
                        "Mika's cheeks once again flushed red, and with slightly shaking hands, she hooked her fingers into her panties and ever so slowly pulled them down."
                        "As her panties dropped down to her ankles, she spread her legs slightly, giving me a clear view of both her tight, womanly holes and the dangling cock between her legs."
                        $ AutoMus(False)
                        $ PlayMusicRandom("mus_sex")
                        scene mika_on_ground with dissolve
                        MIKA "H-Here you go."
                        "Flustered, Mika continued to watch and stare in a mix of curiosity and excitement as she felt my eyes carry across her most intimate parts."
                        "After a few moments, she slowly pulled her panties back up and turned to face me once more."
                        $ AutoMus(True)
                        $ LocFlush()
                        show mc at left
                        show mika at center
                        with dissolve
                        MIKA @blush "There, you've um... {i}Seen me{/i} now."
                        $ UnlockGalSceneAndGrantXp("mika", "mika_on_ground")
            #All choices/routes continued 
            MIKA @blush "...When you're free, can you stop by the girls' dorm tomorrow?"
            MIKA @blush "I have a little gift for you..."
            MC @think "A gift?"
            MIKA @blush "M-Mhmm."
            MIKA @smile "Just promise me you'll come."
            MC @smile "I'll see you there."
            "Mika smiled as she playfully spun, taking a couple slow steps away from me and happily hummed to herself."
            MC "(I wonder what she has planned?)"
            $ QstSetProgress(QstTheLoversPath, 2)
            $ LocEnter()
        "Not right now.":
            MIKA @talk "Alright, let me know, I guess..."
            $ LocEnter()

label qst_the_lovers_path_meet_3:
    show mika:
        center
        xzoom -1.0
    with dissolve
    show mc at left with dissolve
    MIKA @blush "Ah, you came..."
    MC @talk "What is this about, Mika?"
    show mika:
        center
        xzoom -1.0
        linear 0.3:
            xoffset -340
    $ Pause(0.3)
    hide mika
    hide mc
    show cg_mc_mika_kiss:
        left
        yoffset 60
    with dissolve
    "Mika stepped towards me again, pressing her lips against mine."
    "After a tender, passionate kiss, she pulled back to look into my eyes."
    hide cg_mc_mika_kiss
    show mc at left
    show mika:
        center
        xzoom -1.0
        xoffset -340
    with dissolve
    MIKA @blush "R-Relax."
    scene black with dissolve
    "With a sharp shove, Mika pushed me down back onto the edge of a bed as she dropped to her knees and began to unbuckle my clothes." #Mika on knees
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    scene mika_bj_nopreg_dress_idle with dissolve
    $ Pause()
    MIKA "D-Don't think I'm like this with everyone!"
    MIKA "There's something so... {i}different{/i} about you."
    MIKA "It's like it drives me crazy just being near you!"
    BLACK "({i}Interesting ... Her magecraft sensitivity has allowed her to mildly detect my pheromones.{/i})"
    MC "(Is that a bad thing?)"
    BLACK "({i}No ... But against potential threats it will be worth remembering they may be able to detect it.{/i})"
    MIKA "Is something the matter?"
    MC "Oh, sorry, just uh, got lost in thought a moment there."
    MIKA "A-Ah! Don't worry! You won't be able to focus on anything else soon!"
    scene mika_bj_nopreg_dress_face with dissolve
    $ Pause()
    "With my cock flopped out onto her face, Mika, flushed with nervous excitement, gently licked at the shaft." #Cock resting on Mika's face
    MIKA "It's so - {i}*Huff*{/i} heavy!"
    MIKA "And..."
    "I groaned happily as I felt her tongue continue to prod and glide up and down."
    MIKA "{i}B-Big.{/i}"
    MIKA "You sure you're human and not part horse?"
    "I laughed, but as I did so, Mika dragged her tongue towards the tip, wrapping her lips around the head of my cock finally." #BJ
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene mika_bj_nopreg_dress_suck with dissolve
    $ Pause()
    MC "Ahh!"
    MIKA "Mhmm..."
    MIKA "(This thing's gonna give my jaw one hell of a workout!)" 
    "Mika glided her head back and forth, moaning softly as she did so."
    MIKA "{i}*Slurp*{/i} Mhfhhh..."
    "It was clear she lacked experience but didn't lack enthusiasm."
    "Clumsily, she beat and wrapped her tongue around my member, groaning hotly as she did her best to please me."
    "Mika's head rocked back and forth as she did her best to swallow down inch after inch of the cock in front of her."
    MIKA "(Gods... And I thought some of the other sisters were big!)"
    MIKA "(I wonder if the others know how {i}'equipped'{/i} he is?)"
    MC "Ahh... K-Keep doing that."
    "I reached around to grab the back of Mika's head, gently pulling her head forward."
    MIKA "Mhhfh! {i}*Slurp!*{/i}"
    "Mika's mouth widened and stretched to take another inch, her watering eyes looking up towards me as she continued to try and force my cock deeper into her throat."
    "Occasionally, small choking sounds would escape her lips as she dipped her head slightly too far down."
    MIKA "{i}*Glughh!*{/i} Mhhfhh!"
    "As Mika found herself in a more steady rhythm, her eyes, dazed and full with a mixture of love and lust, met mine as she pressed her tongue against the bottom of my cock and continued to throw her head forward."
    MIKA "Mhfhhh! D-Dhhadhyy! ❤️"
    MC "{i}*Huff*{/i} Mika... That's... Mhmmff!"
    "As Mika continued this steady pattern of back, forth, back, forth with her head and gliding, silk-wet lips, the intense sensation continued to build inside of me."
    "The seal around her mouth tightened as she began to feel my member swell and throb in her mouth."
    MIKA "{i}H-He's close! He's so close! I can feel it!{/i}"
    "My hands tightened their grip around Mika's soft hair; the throbbing, building sensation was now painful, desperate for release."
    MC "M-Mika!"
    MC "I'm going to-"
    "Mika, sensing I was on the edge, threw her head forward and held it there in place, choking as deeply as she could on my cock as she thrashed and beat her tongue around my cock."
    "The sudden, sharp sensation was too much, too hot, and grunting loudly, I began to pour my hot load into Mika's warm mouth."
    MC "H-Hrghhhh!!"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    show mika_bj_nopreg_dress_suck with flash
    show mika_bj_nopreg_dress_suck with flash
    scene mika_bj_nopreg_dress_finish_in with flash
    $ ReduceInfectionFromSex("mika")
    $ UnlockGalFlag("mika", "mika_bj_suck", "var_nopreg_dress")
    $ UnlockGalSceneAndGrantXp("mika", "mika_bj_suck")
    $ Pause()
    MIKA "Mmfghh...!?"
    "As Mika swallowed down the hot load pouring into her body, her sultry eyes looked up to me, loving feeding her my seed, and slowly, once the last drop of my load was spent, she slowly dragged her lips back."
    "With a loud *PLOP,* her lips pulled away from the head of my cock, and with a gentle kiss on the head, she looked up and smiled towards me."
    scene mika_bj_nopreg_dress_finish_out with dissolve
    $ Pause()
    MIKA "W-Was that good?"
    "Mika rose back to her feet, wiping her wet lips with her sleeve as she smiled sheepishly towards me." #Sex scene end 
    $ AutoMus(True)
    $ LocFlush()
    show mika at center
    with dissolve
    MC @embarr "That was ..."
    MC @smile "{i}Very impressive.{/i}"
    "Mika's eyes widened at the answer before settling alluringly as a coy smile appeared on her once nervous face."
    MIKA @smile "I-I see."
    MIKA @blush "I guess you won't mind letting me keep practicing on you?"
    MC @embarr "Do you even need to ask?"
    "Mika, gently pressing and rubbing her two index fingers together as she bowed her head lightly, lifted her eyes up towards me."
    MIKA @blush "Umm... I was wondering if perhaps y-you'd wanted to some time-"
    "She paused, reluctant to finish her sentence."
    MIKA @blush "...N-Nevermind."
    MIKA @smile "I'll see you tomorrow, yes?"
    MC @smile "I hope you're ready."
    "Mika nodded defiantly."
    MIKA @talk "This time, I'm gonna show you what I'm made of!"
    MC @talk "I look forward to seeing you try!"
    $ CharChangeRel("mika", 1)
    $ QstSetProgress(QstTheLoversPath, 3)
    $ QstSetDelay(QstTheLoversPath, 1)
    $ LocEnter()

label qst_the_lovers_path_meet_4:
    show mika at center with dissolve
    MIKA @talk "I hope you're ready!"
    menu:
        "{image=[ICON.SWORDS]} Let's do this!": #Battle begins
            $ TimeAdvBy(TIME_2H)
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            $ AutoMus(True)
            $ LocFlush()
            show mika:
                center
                xzoom -1.0
            with dissolve
            show mc at left with dissolve
            if LastBattleOutcome == "defeat":
                MIKA @smile "I - {i}*Huff*{/i} did it!"
                MC @smile "Well - {i}*Huff*{/i} done, Mika."
            elif LastBattleOutcome == "victory":
                MIKA @talk "{i}*Huff!* *Huff!*{/i} How did you - {i}*Huff*{/i} move so fast?"
                MC @smile "{i}Training.{/i}"
                MIKA @talk "{i}*Huff*{/i} Figures..."
            MIKA @talk "...I was thinking we could celebrate."
            MC @smile "Celebrate?"
            MIKA @smile "You're nearly done training me, right?"
            MIKA @smile "I feel so much more alive now, and-"
            "Mika paused, blushing as she grabbed a hold of both of her arms."
            MIKA @smile "I just haven't been this happy in a long t-time and-"
            MIKA @smile "{i}I wanna spend that time with you.{/i}"
            MC @smile "Very well, Mika."
            MIKA @smile "What did you have in mind?"
            "Mika pondered the thought for a moment."
            MIKA @smile "T-Tomorrow, meet me at the market! Let's make a day of it!"
            MC @smile "As you wish, Mika."
            show mika:
                center
                xzoom -1.0
                linear 0.3:
                    xoffset -340
            $ Pause(0.3)
            "With a light bounce in her step, Mika leapt forward to kiss me on the cheek before hurrying off."
            MIKA "I'll be waiting for you!"
            show mika:
                center
                xzoom 1.0
                xoffset -340
            with dissolve
            hide mika with moveoutright
            MC @smile "(That girl...)"
            $ QstComplete(QstTheLoversPath)
            $ LocEnter()

        "Not yet; I have some things I need to take care of first.":
            MIKA @talk "Mmm, stalling huh?"
            MIKA @talk "Fine, I can wait!"
            $ LocEnter()