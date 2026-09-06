label hamun_spa_use_main:
    show luna at right_f with ease
    show mc at cleft with easeinleft
    LUNA @smile "Wonderful!"
    LUNA @smile "The male baths is through the blue curtain."
    show markus at left with easeinleft
    MARKUS @smile "Given this desert heat, a bath is most welcome."
    MARKUS @smile "You ladies have fun now."
    hide markus with easeoutright
    if CharInParty("ves"):
        show ves at left with easeinleft
        VES @angry "If I catch you trying to peek, I will poke your eyes out."
        hide ves with easeoutright
    if CharInParty("sypha") and CharInParty("kiara"):
        show sypha at center with easeinleft
        show kiara at left with easeinleft
        SYPHA @happy "Mmm... A bath sounds pleasant."
        SYPHA @happy "Does it come with servants to fan us?"
        KIARA @talk "Mistress, I fear you still have much to learn about Alderay..."
        SYPHA @sad "Hm, shame."
        hide sypha 
        hide kiara
        with easeoutright
    scene black with dissolve
    $ LocSet("hamun_spa_male")
    $ PlaySoundRandom("tentFlap")
    $ Pause(0.5)
    play sound "audio/cfx/water_splash_bath.ogg"
    "... Retreating to our separated baths, I sank deeper into the water as I began to relax with Markus."
    $ LocFlush()
    $ CharSetClothes("mc", "towel_wet")
    $ CharSetClothes("markus", "towel_wet")
    show mc at cleft
    show markus at cright_f
    with dissolve
    MARKUS "Ahh..."
    MARKUS "So then, what's been on your mind as of late?"
    menu:
        "{i}Talk about anything.{/i}":
            jump hamun_spa_markus_talk
        "Suggest you both transform into women and switch to their baths." (Req_Perk = "fem_charm"):
            jump hamun_spa_tf_both
        "{i}*Sneak out to peek on the girls.*{/i}" (Req_Perk = "chameleon"):
            jump hamun_spa_tf_solo

label hamun_spa_markus_talk:
    $ tmpvar = RngInt(1, 2)
    if tmpvar == 1:
        MC "Tell me Markus, do you... keep count?"
        MC "Since the change I mean."
        "Markus grinned."
        MARKUS "I don't think there isn't a whore in a brothel in Novaras who doesn't know my name by now."
        MC "Just whores?"
        MARKUS "There are a few I keep steady."
        MARKUS "One or two of which who may or may not already be married."
        MARKUS "In fact, this one time..."
        scene black with dissolve
        "Markus shares some of the stories of his {i}conquests{/i} as the two of us relax and talk."
    elif tmpvar == 2:
        MARKUS "... Do you think elven women are sex starved, or sex mad?"
        MC "{i}What?{/i}"
        MARKUS "Well, they live something like two, maybe three lifetimes longer than us, don't they?"
        MARKUS "Do you think, either they have so much sex over the years, that it messes with their heads and only the most crazy stuff can get them off."
        MARKUS "OR, do you think with how prudish they can be about things, they're all insanely repressed for some cock?"
        MC "Is this just your pitch on why we should go and fuck a load of elves?"
        MARKUS "{i}You should know by now I am a pointy-ear connoisseur.{/i}"
        scene black with dissolve
        "Markus and I continued to talk and laugh about the most random of topics." 
    jump hamun_spa_over

label hamun_spa_tf_both:
    MC "Say... Do you remember that little trick of yours with Krishana night?"
    MARKUS "Hm?"
    MARKUS "... Oh!"
    MARKUS "{i}That{/i} trick."
    MARKUS "What of it?"
    MC "Given I can do the same, what's say you and I change and switch baths to join the girls?"
    MARKUS "Now THAT's an idea!"
    MARKUS "Let's do it!"
    scene black with dissolve
    $ LocSet("hamun_spa_female")
    $ LocFlush(dissolve)
    $ SetMCFemOutfit("towel")
    show mcfem at cleft with easeinleft
    show markus_fem at cright_f with easeinright
    "Our bodies twisting into that of women, we managed to sneak past Luna into the girl's baths with little issue."
    "Inside, the dozens of women were chatting and laughing away, and I caught sight of a few of the girl's from our party."
    MARKUS "Well... Should we go over there and try and talk to them? Or..."
    menu:
        "Just relax with Markus.":
            MC "I think it's best we just relax here for a while."
            MARKUS "M-Mmm... It might be a little awkward if the girls realize it's us."
            MARKUS "Alright then, let's just... {i}enjoy the views I guess.{/i}"
            $ PlaySoundRandom("tentFlap")
            $ SetMCFemOutfit("wet")
            show mcfem at blurin, nod
            $ PlaySoundRandom("tentFlap")
            $ CharSetClothes("markus", "wet")
            show markus_fem at blurin, nod
            "The two of us sat back and watched, enjoy as the girls splashed around in the water."
            "... The more I did my best to watch the different girls though, the more I did feel my eyes pull towards Markus."
            "Markus' gaze turned to meet mine as well occasionally, their cheeks flushing red."
            MARKUS "... Y-You know."
            MARKUS "Have you perhaps, ever wondered what it's like to kiss {i}as{/i} a girl?"
            "Markus' eyes look towards me expectently."
            menu:
                "M-Maybe?":
                    MARKUS "... M-Maybe wanna find out?"
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_sex")
                    "My own cheeks flushed red, what was this body doing to me?"
                    "The changes in this womanly body were not just superficial."
                    "Everything felt... {i}different.{/i}"
                    if IsDaytime():
                        scene markus_fem_spa_wmc_day_slow
                    else:
                        scene markus_fem_spa_wmc_night_slow
                    with dissolve
                    $ Pause()
                    "A nervous Markus clambered into my lap, her heavy breasts pressing against my face as my hands reached back to cup and squeeze at her soft ass."
                    "Her hot breath touched my face as she nervously tilted her head forward."
                    MARKUS "R-Ready?"
                    "I nodded, and her soft lips pressed against mine."
                    MARKUS "M-Mmmm...❤️"
                    "The two of us sank into the kiss, panic and nervousness giving way to soft pleasure as our tongues entwined."
                    if IsDaytime():
                        scene markus_fem_spa_wmc_day_fast
                    else:
                        scene markus_fem_spa_wmc_night_fast
                    with dissolve
                    $ Pause()
                    MC "(W-What in the hells are we doing?!)"
                    MC "(G-Gods... Why does it feel so nice?)"
                    "Our hands explored each other's body, cupping and feeling each other as soft moans escapted our lips."
                    "Between kisses, Markus mumbled unconvincingly,"
                    MARKUS "T-This is just us - Mhmm... Fooling around, alright?"
                    "I nod between kisses, and a few of the women nearby notice and giggle, but say nothing."
                    scene black with dissolve
                    if IsDaytime():
                        $ UnlockGalFlag("markus", "fem_spa_wmc", "flag_day")
                    else:
                        $ UnlockGalFlag("markus", "fem_spa_wmc", "flag_night")
                    $ UnlockGalSceneAndGrantXp("markus", "fem_spa_wmc")
                    "For the next half an hour, the two of us are too pre-occupied with each other to really pay any of the other women much attention."
                    "When Markus finally managed to pull herself away from me, the two of us were now suddenly unable to look each other in the eyes."
                    $ LocFlush()
                    show mcfem at cleft
                    show markus_fem at cright_f
                    with dissolve
                    MARKUS "I... I think I'm gonna go get dressed."
                    MARKUS "I-I'll see you outside when you're done!"
                    hide markus_fem with easeoutleft
                    MC "Wait!"
                    "Before I could stop them, they were gone."
                    show mcfem at blurin, center_f with ease
                    MC "(... Damn it.)"
                    MC "(What in the hells are we doing?)"
                    "Well, that didn't exactly go as planned, did it?"
                    "... Within the next ten minutes, I awkwardly left as well."
                    hide mcfem with easeoutleft
                    $ AutoMus(True)
                    scene black with dissolve
                "No... Not really.":
                    MARKUS "A-Ahh... Right."
                    "They forced a laugh."
                    MARKUS "That would be weird, right?"
                    scene black with dissolve
                    "For the next hour, we sat together watching the girls before leaving and heading back towards the mens."

        "Go speak to the girls.":
            MC "This will be fun."
            MC "Let's see if the girls can figure out if it's us."
            hide mcfem
            hide markus_fem
            with dissolve
            $ CharSetClothes("sypha", "wet")
            $ CharSetClothes("kiara", "naked")
            show sypha at cright_f
            show kiara at right_f
            with dissolve
            $ SetMCFemOutfit("towel_wet")
            $ CharSetClothes("markus", "towel_wet")
            show mcfem at cleft with easeinleft
            show markus_fem at left with easeinleft
            "Kiara was sat across the way from Sypha as the two spoke candily about something."
            if CharInParty("ves"):
                "Ves, curiously was surrounded by a group of girls who seemed fascinated by her muscles."
                "A slightly smug Ves posed with her arms, letting the giggling women feel her arms' muscles."
            MARKUS "Hello, ladies!"
            MARKUS "Mind if we join you?"
            "Sypha blinked for a moment as her eyes looked back and forth between me and Markus."
            "{i}Did she realize already?{/i}"
            "A soft smile appeared on her lips."
            SYPHA "Of course, join us."
            $ PlaySoundRandom("tentFlap")
            $ SetMCFemOutfit("wet")
            show mcfem at blurin, nod
            $ PlaySoundRandom("tentFlap")
            $ CharSetClothes("markus", "wet")
            show markus_fem at blurin, nod
            KIARA "But... Mistress!"
            SYPHA "Relax, pet."
            SYPHA "So, {i}'ladies'{/i} what brings you here today?"
            MC "U-Uhh, we just wanted to enjoy the baths."
            MARKUS "Right! We've heard so much about them!"
            KIARA "What brings you to Hamun?"
            MARKUS "Oh, uhhh, our husbands are on business here."
            MARKUS "So we're doing a little sight-seeing around the city."
            SYPHA "Hmm, is that so?"
            SYPHA "Kiara, go fetch some bottles of wine."
            SYPHA "Our new friends here are probably thirsty!"
            KIARA "R-Right away, mistress!"
            "With a skip in her step, Kiara hurried out of the pool, rushing to order the wine."
            SYPHA "Now then..."
            "Sypha's eyes met mine."
            SYPHA "Why don't you both come a little closer?"
            MC "U-Uh?"
            SYPHA "Come, I can hardly hear the two of you all the way over there."
            "Markus and I shared a knowing look before moving closer."
            "As we did so, Kiara returned with two bottles of wine in hand."
            KIARA "Here Mistress!"
            SYPHA "Wonderful!"
            SYPHA "Come, let's have ourselves a drink or two..."
            scene black with dissolve
            $ Pause(0.25)
            $ TimeAdvBy(TIME_1H)
            "An hour later..."
            $ LocFlush()
            show mcfem at cleft
            show sypha at cright_f
            show markus_fem at left
            show kiara at right_f
            with dissolve
            KIARA "Haha! And then what happened?"
            MARKUS "And then - {i}*Hiccup!*{/i}"
            MARKUS "We hid on the back of wagon as fast as we could out of here!"
            "As the four of us laughed whilst the wine poured easily, I felt the soft hand of Sypha kneading at one of my breasts."
            MC "H-Huh?"
            SYPHA "You know."
            SYPHA "{i}You just happen to be my type...{/i}"
            "Sypha's hand reached down the water to touch at my thigh as Markus and Kiara seemed oblivious as to what was happening."
            "Sypha leaned closer to whisper into my ear as her hand trailed."
            SYPHA "{i}Quite the cute trick you have... [player_name!t].{/i}"
            MC "{i}Y-You knew?{/i}"
            SYPHA "So... As you're so curious about being a woman."
            SYPHA "Why don't you relax for a moment and let me show you?"
            menu:
                "Let Sypha continue.":
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_sex")
                    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg", 1)
                    if IsDaytime():
                        scene sypha_hamun_spa_femmc_day_slow
                    else:
                        scene sypha_hamun_spa_femmc_night_slow
                    with dissolve
                    $ Pause()
                    "I gulp, letting Sypha continue as her hand presses itself between my legs."
                    "Her soft fingers press and rub against the opening between my legs as her other hand continues to knead at one of my breasts."
                    "I let out a soft sigh as she gently kisses and rubs her tongue along my neck, the strange sensations I felt were so different to being a man..."
                    "Wet, my body hot and flushed from the teasing, she carefully pushed one, and thjen two, of her fingers into my hole."
                    "I let out a gasp that I desperately tried to muffle."
                    "By some miracle, Kiara and Markus remained obvious to what was going on as Sypha's fingers slipped deeper inside."
                    SYPHA "{i}Are you enjoying your new 'experiences?'{/i}"
                    MC "M-Mhmm..."
                    MC "It's so strange."
                    SYPHA "I'll take that as a yes then."
                    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
                    if IsDaytime():
                        scene sypha_hamun_spa_femmc_day_fast
                    else:
                        scene sypha_hamun_spa_femmc_night_fast
                    with dissolve
                    $ Pause()
                    "As Sypha continued to toy with my body, I felt something inside of, a budding, overwhelming sensation."
                    "As though my whole body was twisting itself up from the inside."
                    MC "S-Sypha."
                    MC "I think I'm gonna-"
                    SYPHA "Just relax and let it happen."
                    SYPHA "And remember... {i}You can indulge me next time.{/i}"
                    "The hot, intense sensation suddenly came all at once, as though my whole body erupted into exstacy."
                    "To stop myself from moaning too loudly, Sypha's hand reached aroud to grab my mouth as my eyes rolled to the back of my head."
                    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
                    if IsDaytime():
                        scene sypha_hamun_spa_femmc_day_idle
                    else:
                        scene sypha_hamun_spa_femmc_night_idle
                    with flash
                    if IsDaytime():
                        $ UnlockGalFlag("sypha", "hamun_spa_femmc", "flag_day")
                    else:
                        $ UnlockGalFlag("sypha", "hamun_spa_femmc", "flag_night")
                    $ UnlockGalSceneAndGrantXp("sypha", "hamun_spa_femmc")
                    $ Pause()
                    MC "Mmfmfghhh!! ❤️"
                    "The pleasure lasted longer than it did as a man, and it was so much more intense..."
                    "As the wave of pleasure slowly began to simmer down, Sypha released her grip as I caught my breath."
                    MARKUS "Are you - {i}*Hiccup!*{/i} Alright?"
                    MC "Y-Yes..."
                    "I say flustered, Sypha grinned at me like a cat that just managed to catch a mouse, saying nothing as she reaches over to sip once more at her wine."
                    "With shaky legs, I rise to my feet."
                    MC "W-We should go now. Mmm..."
                    MARKUS "H-Huhh? So suddenly?"
                    MC "Yes, come on."
                    scene black with dissolve
                    $ LocFlush(dissolve)
                    show mcfem at cright 
                    show markus_fem at cleft
                    with easeinleft
                    "Climbing out of the pool, a bewildered Markus followed from behind, slightly confused as to what just happened."
                    hide mcfem 
                    hide markus_fem 
                    with easeoutright
                    show sypha at cright
                    show kiara at cleft
                    with easeinleft
                    SYPHA @laugh "Hahahahahaha!"
                    KIARA @think "Mistress? Did I miss something?"
                    show sypha at blurin, cright_f
                    SYPHA @happy "Oh, don't you worry your pretty little head about it."
                    scene black with dissolve

                "Pull away to leave.":
                    MC "E-Excuse me, I think I better get going."
                    MARKUS "Huh? So soon?"
                    hide mcfem
                    hide markus_fem
                    with easeoutright
                    "As I climbed out of the pool, Sypha chuckled softly as a confused Markus followed from behind asking what happened."
                    KIARA "Mistress? What happened?"
                    SYPHA "She just felt a little lightheaded from the wine is all... She'll be fine, I'm sure."
                    scene black with dissolve

            "With my cheeks flushed red, I quickly retreated to gather my clothes."
            "Eventually, having changed back into a man, Markus continued to quiz me over what had happened,"
            "but I handwaved off his questions that I was just tired."
    jump hamun_spa_over

label hamun_spa_tf_solo:
    MC "There's something I need to take care of."
    MC "I'll be back shortly."
    MARKUS "Alright."
    MARKUS "I'll order us some mead in the meanwhile."
    scene black with dissolve
    $ LocSet("hamun_spa_female")
    $ LocFlush(dissolve)
    "Carefully, invisible to all but the keenest eyes noticing slight inflections as I moved, I made our way towards the girls side of the baths."
    "Luna remained oblivious, as I slipped through to peer on the women's side."
    $ tmpvar = [1, 2]
    if CharIsMet("katiya"):
        $ tmpvar.append(3)
    $ tmpvar = renpy.random.choice(tmpvar)
    if tmpvar == 1:
        if IsDaytime():
            scene numa_marbella_spa_day with dissolve
        else:
            scene numa_marbella_spa_night with dissolve
        $ Pause()
        MARBELLA "Oi, thanks for inviting me out by the way."
        MARBELLA "All that work in the mines... Bloody can't remember a time I DON'T feel like I'm dripping sweat!"
        NUMA "It's fine."
        NUMA "I prefer some companionship when in the pools here."
        MARBELLA "Why {i}do{/i} ya invite me instead of one of ya fishy friends?"
        MARBELLA "No offence, of course."
        NUMA "It's... complicated."
        NUMA "Females of my species can be quite... {i}territorial.{/i}"
        NUMA "There are all sorts of politics and things."
        NUMA "Me inviting another female to a {i}human{/i} bathhouse could be taken the wrong way."
        MARBELLA "So they're a bunch of bitches then?"
        "Numa laughed."
        NUMA "I suppose they can be."
        MARBELLA "Ite' but then, {i}why me?{/i}"
        NUMA "You are different, are you not?"
        MARBELLA "You mean, because I'm a dwarf?"
        MARBELLA "This better not be no pity party fin girl!"
        NUMA "No."
        NUMA "You just understand better than the rest of them."
        NUMA "{i}... And you make me laugh.{/i}"
        MARBELLA "Too-fucking right I do!"
        MARBELLA "...Quick question though."
        NUMA "What's that?"
        MARBELLA "Whose cock is better, yer fishy men, or human?"
        "Once more Numa laughed."
        NUMA "I'll tell you the answer if you buy the food later."
        MARBELLA "Bloody cheapskate!"
        scene black with dissolve
        "Reluctantly, I slipped away from the scene, careful to return back before anyone noticed I was gone."
    elif tmpvar == 2:
        if IsDaytime():
            scene kiara_spa_day with dissolve
        else:
            scene kiara_spa_night with dissolve
        $ Pause()
        "Kiara hummed happilly to herself as she sat, her feet in the water as she bathed herself."
        KIARA "{i}O love, I swear, when the night is through,{/i}"
        KIARA "{i}My weary heart will return to you.{/i}"
        KIARA "{i}Though fate may call, I’ll fight, I’ll strive,{/i}"
        KIARA "{i}For your embrace, I long to live.{/i}"
        "Her voice is strangely hypnotic, I feel as though I could listen to her sing day and night."
        "My eyes wander over her lovely body, hypnotic in the light, and reluctantly, I pull myself away from her before anyone notices I've been gone too long already."
        scene black with dissolve
    elif tmpvar == 3:
        if IsDaytime():
            scene katiya_spa_day with dissolve
        else:
            scene katiya_spa_night with dissolve
        $ Pause()
        "Three naked, lush bodies sat around the pool, laughing and talking as I swore I recognised one of the women."
        KATIYA "So, Kala, Venya, how fares things with your husbands?"
        KALA "Really? You invite us out here and want to talk about those bores?"
        FAYE "Speak for yourself, Kala!"
        FAYE "Just last week, my husband took me to this lord's party, and-"
        KALA "We both know what you and your husband get up to."
        KALA "But if I recall, you two aren't exactly spending much time {i}together.{/i}"
        KATIYA "Kala!"
        FAYE "So what?"
        FAYE "He get's what he wants and I get what I want."
        FAYE "What's wrong with that?"
        FAYE "And you can hardly talk, when was the last time you and your husband... {i}you know.{/i}"
        KALA "Don't remind me."
        KALA "I think soon I might need to... {i}find other solutions,{/i} if he doesn't do SOMETHING soon."
        KALA "How long is someone supposed to suffer?"
        KATIYA "Wait, you're thinking about having an affair?!"
        KALA "What else am I supposed to do at this point?"
        KALA "Divorce is out of the question, our families would kill us..."
        FAYE "What about you, Katiya?"
        FAYE "Is there a special someone in your life?"
        KATIYA "Haha, I am far too busy for such things."
        FAYE "Booo.... BOOOO!"
        KALA "There must be one man in this city who catches your eye."
        KATIYA "W-Well..."
        KATIYA "I did see one man recently."
        FAYE "Ooooh! Tell us everything!"
        KATIYA "Haha, there's not much to tell... He came into my store and he was just very handsome."
        KALA "And you're hoping he comes back?"
        KATIYA "I... {i}wouldn't say no to seeing him again.{/i}"
        scene black with dissolve
        "The women continued to giggle and chatter."

    "Deciding I had seen enough, I turned to leave before anyone realized I'd been away for too long."
    jump hamun_spa_over

label hamun_spa_over:
    $ AutoMus(True)
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("markus", "normal")

    $ CharSetClothes("sypha", "normal")
    $ CharSetClothes("kiara", "normal")

    $ SetMCFemOutfit("normal")

    $ HealParty()
    $ TimeAdvBy(TIME_1H)
    $ Pause(0.25)
    $ LocSet("hamun_spa")
    $ Pause(0.1)
    $ LocEnter()