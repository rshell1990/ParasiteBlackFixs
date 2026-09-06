label qst_the_mages_path_meet_1:
    show mika at center with dissolve
    MIKA @talk "I-I'm ready to train when you are!"
    "Mika sterns herself with new determination for the lesson ahead!"
    menu:
        "{image=[ICON.SWORDS]} Let's begin!":
            $ tmpvar = renpy.random.randint(0, 1)
            # 50/50
            scene black with dissolve
            if tmpvar == 0:
                "Despite her best efforts, Mika was overcome by her fear."
                "Reduced to a shivering ball, she could not continue this time."
                $ LocFlush(dissolve)
                show mika sad at center with dissolve
                MIKA @sad "S-Sorry."
                MIKA @cry "I didn't mean to-"
                MC @talk "It's fine, Mika."
                MC @talk "We'll try again another day."
                MIKA @sad "O-Okay..."
                $ QstSetDelay(QstTheMagesPath, 1)
                $ LocEnter()

            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            scene black with dissolve
            $ AutoMus(True)
            "The sparring session went well,"
            "Mika was terrified, but with some gentle encouragement, she managed to steer herself enough to actually at least dodge my attacks and cast some basic magecraft defence."
            "While there was still a long way to go, there had been remarkable progress."
            $ TimeAdvBy(TIME_2H)
            $ LocFlush()
            show mika at center
            show mc at left
            with dissolve
            MIKA @smile "I - {i}*Huff*{/i} did it!"
            MC @smile "Well done, Mika."
            MC @smile "That was much better than before."
            MIKA @talk "Mhmm!"
            DIVINE "I see things are going well?"
            "Unaware at her observantly watching us this whole time, Sister Divine stepped closer towards us, seemingly pleased."
            show divine:
                right 
                xzoom -1.0
            with dissolve
            MIKA @shock "S-Sister Divine!"
            DIVINE @happy "It's good to see you making such progress, Mika."
            MC @talk "We still have some ways to go..."
            DIVINE @happy "I just wanted to check in on your progress."
            DIVINE @talk "Good work, Mika."
            MIKA @shock "T-Thank you! Sister!"
            DIVINE @talk "Well, don't let me get in the way."
            DIVINE @talk "Carry on both."
            hide divine with dissolve
            "As Sister Divine left with a pleased expression, Mika sighed with relief."
            MC @talk "... Are you going to tell her what happened to you?"
            MIKA @scared "N-No, definitely not."
            MIKA @sad "I couldn't bear the thought of her knowing."
            MIKA @sad "Would she think I was a coward? Even more useless than she already thinks?"
            MIKA @sad "I ... I don't want to be an even bigger disappointment to her."
            MC @talk "I doubt she would think that way about you."
            MIKA @sad "But-"
            MIKA @scared "I'll tell her when I'm ready!"
            MC @talk "As you wish, Mika."
            MIKA @sad "... You won't tell her, right?"
            MC @talk "No, Mika."
            MC @talk "It's up to you to tell her when you're ready."
            "Mika's whole body seemed to relax once more."
            MIKA @smile "Ahh, that's good to hear."
            MIKA @talk "I was wondering if we could-"
            MIKA "{i}Ahh!{/i}"
            hide mika with hpunch
            play sound2 "audio/cfx/body_falling.ogg"
            "Suddenly, tripping up on herself, Mika came crashing to the ground abruptly."
            scene black with dissolve
            MC @surprised "Mika!"
            menu:
                "Look away for Mika's sake":
                    "I averted my gaze before catching sight of something undignified."
                    $ QstTheMagesPath().AvertedGazeDuringBPScene = True
                "Look.":
                    scene mika_on_ground_buttplug with dissolve
                    $ Pause()
                    "As she tumbled forward, with a gust of passing wind, her dress flipped up entirely, revealing her bare butt and the lewd toy pressed into her ass." #Mika Ass flash - buttplug CG
                    MIKA "Ow ow ow!"
                    MC "..M-Miss Mika, you're-"
                    MIKA "H-Huh?"
                    "Realizing what I was looking at, Mika's face contorted in horror."
                    MIKA "{i}*Gasp!*{/i}"
                    scene black with dissolve
            "Frantically, with her cheeks burning red, Mika rose back to her feet, pale as a ghost in a complete panic."
            $ LocFlush(dissolve)
            show mika sad at center
            with dissolve
            MIKA @scared "I - I - I can explain!"
            MIKA @scared "I-It was just a silly idea I had to help me focus! That's all!"
            MC @surprised "M-Mika, uhh..."
            if QstTheMagesPath().AvertedGazeDuringBPScene == True:
                MC @think "Mika, I didn't see any-"
                MIKA @scared "I just like to wear it sometimes, okay!?"
                MC @think "... Uhh, right."
                MIKA @sad "W-Wait, you didn't see it?"
                MIKA @sad "Oh gods, uhh... Forget I said anything!"
            "Before I could finish my sentence, a deeply embarrassed Mika hurried off."
            hide mika with moveoutright
            MC @surprised "Mika! Wait!"
            MIKA "I'LL SEE YOU FOR THE NEXT SESSION TOMORROW!"
            if QstTheMagesPath().AvertedGazeDuringBPScene == True:
                MC @sad "{i}Sigh{/i}"
                MC @talk "What a nuisance this is."
            else:
                MC "(Help her focus, huh?)"
                "I smirked at the thought; our next sparring match was going to be an {i}interesting{/i} one."
                $ UnlockGalSceneAndGrantXp("mika", "mika_on_ground_buttplug")
            $ QstSetProgress(QstTheMagesPath, 1)
            $ QstSetDelay(QstTheMagesPath, 1)
            $ LocEnterQ()
        "I have some other business I need to attend to first.":
            MIKA @shock "O-Oh, alright then."
            MIKA @talk "I'll be here when you're ready."
            $ LocEnter()

label qst_the_mages_path_meet_2:
    if not QstTheMagesPath().mcTalkedAboutTheButtplug:
        show mika sad at left with dissolve
        "As soon as she saw me approaching, very sheepishly, Mika took a few timid steps towards me."
        show mika sad at center with dissolve
        "Her cheeks burning red, her eyes shyly averted to the ground as she spoke."
        MIKA @sad "A-About the other day-"
        MC @talk "Think nothing of it, Mika."
        MIKA @shock "But-"
        if QstTheMagesPath().AvertedGazeDuringBPScene == True:
            MIKA @sad "About what I s-said... I was-"
            MC @talk "It's fine, Mika, let's move on."
            MIKA @sad "R-Right..."
        else:
            MIKA @sad "You saw my...{i}You know.{/i}"
            menu qst_the_mages_path_meet_2_menu:
                "And what a nice ass it was.":
                    "Mika's expression perked up with surprise at the comment."
                    MIKA @shock "You ... {i}liked what you saw?{/i}"
                    MC @smile "I did."
                    "Mika's cheeks once again blushed red as she stuttered, thinking about what to say."
                    MIKA @scared "W-Well, u-uh! But I'm a-"
                    MC @smile "Mika, we're here for a sparring session, remember?"
                    "A flustered Mika gulped, nodding as she tried to regain some focus."
                    MIKA @shock "Y-Yes, of course!"
                    MIKA "(He ... He likes my butt?)"
                    MIKA "(Gods, why is that making me feel all tingly inside?)"
                "Just remember to not forget to wear your undergarments next time.":
                    MIKA @sad "Y-Yes sir."
                    MIKA @sad "I won't forget."
        show mika sad at center with dissolve
        MIKA @talk "With that out of the way, are you ready for our next sparring session?"
        $ QstTheMagesPath().mcTalkedAboutTheButtplug = True
    else:
        show mika at center with dissolve
        MIKA @talk "Are you ready for our next sparring session?"

    menu qst_the_mages_path_meet_2_menu_2:
        "{image=[ICON.SWORDS]} Let's begin!":
            $ tmpvar = renpy.random.randint(0, 1)
            #random 50/50
            scene black with dissolve
            if tmpvar == 0:
                "Despite her best efforts, Mika was overcome by her fear."
                "Reduced to a shivering ball, she could not continue this time."
                $ LocFlush()
                show mika sad at center 
                with dissolve
                MIKA @sad "S-Sorry."
                MIKA @cry "I didn't mean to-"
                MC @talk "It's fine, Mika."
                MC @talk "We'll try again another day."
                MIKA @sad "O-Okay..."
                $ tmpvar = {}
                $ QstSetDelay(QstTheMagesPath, 1)
                $ LocEnter()

            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_magearena", CharIDList_Left = ["mc"], CharIDList_Right = ["mika"], CanTransform = False, ContinueOnDefeat = True))
            scene black with dissolve
            $ AutoMus(True)
            "Mika, managing to build on the success of last time, not only dodged my strikes but managed to effectively counter-strike with light blasts and keep me at bay."
            "She still lacked the confidence to go on the offensive, and even though her hands still shook with fear, it was another vast improvement."
            play sound2 "audio/cfx/mika_spell.ogg"
            "One of her blasts of energy, however, was far stronger than the others, and accidentally, she sent me slamming into the ground painfully."
            $ CharSetVar("mc", "default_look", "father_armor_ash")
            $ TimeAdvBy(TIME_2H)
            $ LocFlush(dissolve)
            show mika scared at center_f
            with dissolve
            MIKA @scared "[player_name!t]!"
            show mc at left with dissolve
            MC "(...Ow)."
            "I dragged myself up back to my feet."
            MC @talk "{i}*Huff*{/i} I'm alright!"
            MC @talk "That'll do for now, Mika."
            MC @talk "Well done."
            MIKA @scared "I-I'm so sorry! I didn't mean to!"
            MC @talk "Mika, it's fine; injuries happen during sparring."
            "Mika pouted sadly, her lips trembling."
            MIKA @sad "T-Then let me heal you at least!"
            MIKA @sad "You're bleeding!"
            "I wiped the trail of blood from my face and looked down to see, indeed, she had injured me more than I initially suspected."
            MIKA "(How is he even still standing? A blast like that should have ... Should have...)"
            MIKA "(No, push the thought aside!)"
            MC @talk "Hm, very well then."
            MIKA @blush "P-Please remove your clothes!"
            MIKA @blush "I - I need to ensure I heal you fully."
            $ CharSetVar("mc", "default_look", "father_armor")
            $ CharSetClothes("mc", "pants")
            show mc at blurin, nod
            "Accepting her advice, I removed the top of my armour and let it slide onto the floor."
            "As I waited for Mika to heal me, though, she chose to stand there and ... {i}stare.{/i}"
            MIKA @blush "..."
            MC @talk "Mika."
            MIKA "(Gods ... How does a man even sculpt a body like that?)"
            MC @serious "MIKA!"
            MIKA @shock "H-HUH?!"
            MIKA @blush "O-Oh! Sorry!"
            "Mika waved her hands in a circular motion towards me, and as she did so, I felt a sudden warmth as my wounds and injuries began to heal."
            "As the gash closed its wound, there was still some ache but it was a remarkable improvement."
            MIKA @sad "{i}*Phew!*{/i}"
            MIKA @blush "S-Sorry about that."
            MC @smile "There's no need to apologize, Mika."
            show mc:
                left
                linear 0.2:
                    xoffset 300
                nod
            "Reaching out, I gently patted Mika on the head in appreciation, and as I did so, her whole face lit up red once more."
            hide mc
            show mc at left 
            with dissolve
            MIKA @blush "I - I need to get going!"
            "Once again, Mika, without saying another word, hurried away before I could stop her."
            MIKA @blush "L-Let me know when you want to spar again!"
            show mika at center
            with dissolve
            hide mika with moveoutright

            $ CharSetClothes("mc", "normal")
            $ QstSetProgress(QstTheMagesPath, 2)
            $ QstSetDelay(QstTheMagesPath, 1)
            $ LocEnter()

        "I have some other business to attend to first.":
            MIKA @talk "Mm, alright."
            MIKA @talk "Just let me know when you're ready, then, I suppose..."
            $ LocEnter()

label qst_the_mages_path_meet_3:
    show mika at center with dissolve
    MIKA @sad "A-Ah, can we, um..."
    MIKA @sad "Skip sparring today, perhaps?"
    MC @think "Why? What's the matter?"
    MIKA @sad "N-Nothing."
    MC @talk "Doesn't exactly sound like nothing."
    "Mika paused, hesitating to answer."
    MIKA @sad "...It's just-"
    MIKA @sad "{i}*Sigh*{/i}"
    MIKA @sad "Today's a special day for Mages everywhere."
    MIKA @sad "It's called {i}Roses night.{/i}"
    MIKA @sad "You send out an enchanted rose to someone you like, and it lets them know you're interested."
    MC @think "Enchanted roses?"
    MIKA @smile "They're beautiful... They tend to glitter thanks to the enchantment."
    MIKA @smile "When you touch them, the person's face comes to your mind immediately."
    MIKA @sad "...Guess how many I got?"
    MIKA @smile "Zero! Ta da! Haha!"
    MIKA @sad "Ha...Ha..."
    MC @sad "Mika..."
    MIKA @smile "It's fine. We mages of Palam usually end up giving roses to each other more than anything."
    MIKA @sad "Still... It would have been nice to know {i}someone{/i} liked me that way."
    MC @talk "I'm sure, Mika, whoever you end up with, be a fortunate person."
    "Mika's eyes seemed to light up at my comment."
    MIKA @blush "C-Can I ask you something?"
    MC @smile "Of course."
    MIKA @think "Have you ever been in love?"
    $ TimeAdvBy(TIME_2H)
    scene black with dissolve
    "What felt like ancient memories now sprung back of a girl's face I'd longed to forget."
    "Back before the dark passenger, {i}back before everything.{/i}"
    $ LocFlush()
    show mika at center
    with dissolve
    MC @talk "... Well, I'm not sure I'd call it love."
    MC @talk "But, it was {i}more{/i} than just a fling."
    MIKA @blush "W-What was it like?"
    menu:
        "You'll find out yourself one day.":
            MIKA @sad "I - I hope so."
        "The sex was great, but she turned out to be a bitch in the end.":
            MIKA @sad "I - I see."
            MIKA @sad "That's unfortunate."
    #Both choices continued 
    MIKA @blush "I ... I think any lady would be fortunate to have you."
    MC @surprised "That's kind of you to say, Mika."
    "Mika waited expectantly."
    MIKA @sad "So, can we train another day, please?"
    MC @talk "Very well, Mika."
    hide mika with moveoutright
    "Mika smiled faintly, offering a curt bow as she hurried off."
    MC "(...Enchanted roses, huh?)"
    $ QstSetProgress(QstTheMagesPath, 3)
    $ LocEnterQ()

label qst_the_mages_path_meet_4:
    show mc at left with moveinleft
    show cg_dealer at right_f
    with dissolve
    hide cg_dealer with moveoutleft
    show mc angry
    "As I made my way through the streets of Novaras, a robbed, hooded figure passing by pressed a small wooden box against my chest before disappearing into the crowds before I could stop them."
    MC @angry "What in the-"
    scene black with dissolve
    "The box itself was simple but carved well, with some light ornate engravings on the side."
    if IsDaytime():
        scene bg_alleyway
    else:
        scene bg_alleyway_night
    with dissolve
    "Deciding to open such a thing out in the open was probably not the best idea; I headed towards one of many darkened alleys to inspect the box closer." #Cut to alley BG
    "As people passed by on the main street obliviously, I ran my hands carefully over the box."
    "It was light, and as I gently shook it, there was definitely something inside, though."
    "Gently, as I slid off the lid from the box, inside was a glittering dark rose."
    MC "(...A rose?)"
    "Remembering Mika's words about enchanted roses, I gently reached down to touch the rose, and as I did so, I was assaulted by a glimpse of Mika's alluring face before my thoughts became pitch black."
    BLACK "{i}I have detected and blocked a potential psychic attack.{/i}"
    BLACK "It appears to be attempting to implant images into your mind."
    BLACK "Should you wish, I can allow you to safely view whatever the person was trying to send..."
    menu:
        "Show me.":
            BLACK "Very well."
            scene mika_wet_dream_slow with slowflash
            $ AutoMus(False)
            $ AutoAmb(False)
            stop ambience
            stop ambience2
            $ PlayMusicRandom("mus_sex")
            $ Pause()
            "Suddenly, lewd images of Mika sprawled out on a bed came surging through my mind." #Lewd CGs com roupa
            $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
            "Like watching a vision, she ran her hands up her body and smiled alluringly, leaving nothing to the imagination."
            scene mika_wet_dream_fast with dissolve
            "Overwhelmingly so, not only could I see her, I could {i}feel{/i} her desires and intent as though they were my own."
            scene mika_wet_dream_fast_nude with flash
            "In a moment, there was a second image of her, now naked on the bed as she continued to rub her body teasingly with her hands." # cg sem roupa
            MIKA "{i}I want you ... I want you so much.{/i}"
            MIKA "{i}Like I've never wanted anyone before.{/i}"
            if IsDaytime():
                $ UnlockGalFlag("mika","mika_wet_dream","day")
                scene bg_alleyway
            else:
                $ UnlockGalFlag("mika","mika_wet_dream","night")
                scene bg_alleyway_night
            with slowflash
            $ AutoMus(True)
            $ AutoAmb(True)
            $ StopSexFx()
            "As soon as the vision began, it ended, and I stood once more in the same alleyway."
            MC "(Gods ... It felt like I was {i}there{/i} with her just now.)"
            $ UnlockGalSceneAndGrantXp("mika", "mika_wet_dream")
            $ QstTheMagesPath().mikaWetDreamSkipped = False
        "No ... I don't want to see it.":
            BLACK "Very well, I shall safely discard these implanted images."
            BLACK "...Done."
            $ QstTheMagesPath().mikaWetDreamSkipped = True
    #Both choices continued
    MC "(Did Mika really mean to send this to me?)"
    "I pondered my own mixed feelings... {i}How did I feel about this?{/i}"
    MC "(I should speak to Mika tomorrow about it.)"
    MC "(Well, this could be awkward...)"
    $ QstSetProgress(QstTheMagesPath, 4)
    $ LocEnter()

label qst_the_mages_path_meet_5:
    $ TimeAdvBy(TIME_2H)
    show mika at center with dissolve
    "When she saw me, Mika, trembling and blushing, took a few nervous steps to meet me halfway."
    MIKA @blush "H-Hello."
    MC @think "I uhh...{i}I got your rose.{/i}"
    MIKA @blush "Y-Yes..."
    "With a deep breath, Mika began."
    MC @embarr "I - I hope this hasn't come as too much of a surprise."
    MIKA @blush "I understand we haven't exactly known each other very long."
    MIKA @blush "We Palam girls don't get m-many opportunities, so, especially when some fucking handsome-"
    "Mika's eyes widened."
    MIKA @shock "Oh gods, did I just say that?"
    MC @smile "You did."
    "Mika's cheeks burned red."
    MIKA @blush "(Stay focused Mika! Don't get flustered now!)"
    MIKA @blush "... W-We don't like to wait around long and miss our chance, is what I meant to say."
    MIKA @blush "And, since you've been so patient and kind with me ... I don't think I've ever met another man quite like you."
    "Her eyes nervously look towards me for a reply."
    MIKA @blush "S-So, how about it?"
    MIKA @sad "I- I understand if you didn't just want to be with me, w-we're not usually people's first picks..."
    MIKA @sad "W-We're used to playing the role of {i}mistress{/i} more than the role of wife."
    "Mika declared defiantly, her heart no doubt racing as she did so."
    MIKA @blush "B-But I'd like to be with you all the same!"
    "Hmm, this is a difficult matter... {i}Do I like Mika this way? Or should I let her down gently and keep things as they are between us?{/i}"
    "Or, perhaps Markus may be interested in her if I'm not?"
    "He {i}did{/i} mention he found them attractive once before."
    "What should I do?"
    menu:
        "{image=[ICON.HEART]} Agree to become Mika's lover":
            $ CharSetLover("mika")
            $ CharChangeRel("mika", 1)
            MC @lewd "I hope you're as bold in bed as you are outside it."
            MIKA @sad "Oh, I under-"
            MIKA @shock "Wait, what?!"
            MIKA @blush "Y-You mean it? You'll be my-"
            MC @smile "Is it that surprising I said yes?"
            MIKA @shock "I...!"
            MIKA @lewd "Gods, I think I might need to sit down, haha!"
            MIKA @lewd "I'm shaking!"
            MC @lewd "{i}You will be soon.{/i}"
            "Mika's cheeks burned as she giggled nervously, pressing her burning cheeks together in her palms."
            MIKA @lewd "J-just hearing you talk like that is embarrassing me."
            MC @smile "But ..."
            MIKA @think "{i}...But?{/i}"
            MC @talk "First, we need to finish what we started."
            MC @talk "You're sparring sessions; are you ready to continue them?"
            "Mika nodded defiantly."
            MIKA @smile "Mhmm!"
            MIKA "(Now, I don't just want to succeed for myself anymore.)"
            MIKA "(I want {i}you{/i} to know I'll be alright out there on my own!)"
            "Mika yawned."
            MIKA @talk "Sister Divine has asked me to help her with some paperwork and things today."
            MIKA @talk "I - I'll definitely be here tomorrow for training, though!"
            MC @smile "That's good to hear, Mika."
            hide mika with moveoutright
            "Smiling, Mika hurried off with some bounce in her step."
            "It was a pleasant feeling, seeing her become more confident."
            $ CharAddRelEntry("mika", "love")
            $ QstStart(QstTheLoversPath)

        "{image=[ICON.HEART_CROSS]} See if Markus would be interested in her instead.":
            MC @talk "I'm sorry, Mika, I don't think that would be appropriate."
            $ QstComplete(QstTheMagesPath)
            "Mika sighed expectantly."
            MIKA @sad "{i}*Sigh*{/i}"
            MIKA @sad "Can't exactly say I didn't see that one coming..."
            "A deflated Mika offered a weak smile, but it was clear her hopes were never high."
            MC @think "...But perhaps I know someone who {i}would{/i} be interested."
            "Mika perked up in surprise at the comment."
            MIKA @shock "Huh?"
            MIKA @blush "I ... I'm not sure."
            MIKA @blush "Does he know I'm, you know, a mage of Palam?"
            MC @talk "Why don't you let me speak to him first, and then, if he agrees, introduce you afterwards?"
            MIKA @blush "...A-Alright then, I trust you."
            "Mika pouted."
            MIKA @angry "He better be good lookin'! Just because we're always on the lookout for a good catch doesn't mean {i}every{/i} man is a good fit, you know!"
            MC @smile "Don't worry, he's {i}almost{/i} as good-looking as me."
            "Mika playfully puckered her lips to the side."
            MIKA @smile "Mmmm, okay then."
            MIKA @smile "I trust you."
            $ QstStart(QstABestFriendsPath)
            MC @smile "But ..."
            MIKA @think "{i}...But?{/i}"
            MC @talk "First, we need to finish what we started."
            MC @talk "Your sparring sessions; are you ready to continue them?"
            "Mika nodded defiantly."
            MIKA @smile "Mhmm!"
            "Mika yawned."
            MIKA @talk "Sister Divine has asked me to help her with some paperwork and things today."
            MIKA @talk "I - I'll definitely be here tomorrow for training, though!"
            MC @smile "That's good to hear, Mika."
            hide mika with moveoutright
            "Smiling, Mika hurried off with some bounce in her step."
            "It was a pleasant feeling, seeing her become more confident."
            scene black with dissolve
            jump qst_a_best_friends_path_1

    $ QstComplete(QstTheMagesPath)
    $ LocEnter()