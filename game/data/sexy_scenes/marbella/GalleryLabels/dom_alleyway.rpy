# for some reason rmb in replay explodes if we dont have it
label preferences:
    call screen main_menu()
    #return

label gallery_marbella_dom_alleyway:
    scene black with dissolve
    # only first
    if GalFlagCount("marbella", "dom_alleyway") == 0:
        $ StartReplay("replay_marbella_dom_alleyway_first")
        scene black with dissolve
        return
    else:
        "Was it our first time?"
        menu:
            "Yes":
                $ StartReplay("replay_marbella_dom_alleyway_first")
                scene black with dissolve
                return
            "No":
                pass

    # locked in to rep scenes
    
    if GalFlag("marbella", "dom_alleyway", ["rep_preg_vag", "rep_preg_anal"], anymatch = True) and GalFlag("marbella", "dom_alleyway", ["rep_nopreg_vag", "rep_nopreg_anal"], anymatch = True):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False
    else:
        if GalFlag("marbella", "dom_alleyway", ["rep_preg_vag", "rep_preg_anal"], anymatch = True):
            $ tmpvar["preg"] = True
        else:
            $ tmpvar["preg"] = False

    if GalFlag("marbella", "dom_alleyway", ["rep_preg_vag", "rep_nopreg_vag"], anymatch = True) and GalFlag("marbella", "dom_alleyway", ["rep_preg_anal", "rep_nopreg_anal"], anymatch = True): 
        "Was it anal or vaginal?"
        menu:
            "Vaginal":
                $ tmpvar["variant"] = "vag"
            "Anal":
                $ tmpvar["variant"] = "anal"
    scene black with dissolve
    # rep
    $ PlaySound("audio/cfx/transform.ogg")
    MC @smile "So, are you ready?"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MARBELLA_ROBE @smile "Always..."
    MARBELLA_ROBE @emb "Buttttt..."
    MC "But what?"
    MARBELLA_ROBE @lewd "Wouldn't you rather put it in my ass this time?"

    if tmpvar["variant"] == "anal":
        MC "You think I'd pass up the opportunity to stretch out your fat ass?"
        MARBELLA_ROBE @lewd "Mhmm... Let's do it!"
        scene black with dissolve
        "{i}A few minutes later...{/i}"
        MARBELLA "{i}*Huff!*{/i} G-Gentle! GENTLE!"
        MARBELLA "My ass still needs a few seconds to-"
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_1 with dissolve
        else:    
            scene marbella_dom_alleyway_nopreg_1 with dissolve
        $ Pause()

        "Her body strapped and pinned to mine, she groaned as I pushed my cock against her tight rosebud."
        "After some resistance, her ass spread and gave way, her eyes widening in shock."
        MARBELLA "ADJUSTTTTTTTT...!!"
        $ PlaySexFx(audio.nijah_miss_1, 1)
    
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_2 with dissolve
        else:    
            scene marbella_dom_alleyway_nopreg_2 with dissolve
        $ Pause()
        "Her tight asshole squeezed around me as we moved through the alleyways."
        MARBELLA "Mmfghhh!"
        MARBELLA "M-My ASS!"
        MARBELLA "You're gonna- Hrghh! B-Break it!"
        MC "You're the one who asked for it!"
        MC "Now you have to take responsibility!"
        "Marbella quivered on the end of my cock, her tight ass pulsing around me."
        MARBELLA "{i}*Huff*{/i} I w-will! {i}*Huff!*{/i}"
        MARBELLA "I'll take responsibility and milk your cock dry with my ass!"
        "I could hear her heart racing as we moved from alleyway to alleyway."
        MC "Ready to find your audience?"
        MARBELLA "MMFGHHH!"
        "Up ahead, I saw a couple locked in an embrace against a wall."
        MC "Perfect!"
        MARBELLA "(T-They'll see me- Ahh!)"
        MARBELLA "(THEY'RE GONNA SEE ME WITH HIS COCK IN MY ARSE!)"
        "I approached them, grinning as Marbella bounced on my cock."
        WOMAN "W-WHAT IN THE WORLD?!"
        MAN "Huh?"
        MC "Don't mind me, just taking my dwarf for a fuck-walk."
        "Marbella moaned, drool slipping from her lips."
        MARBELLA "(Oh gods... They've seen me...)"
        MARBELLA "(PEOPLE HAVE SEEN ME!)"
        "She climaxed on the spot, her asshole convulsing around me."
        MARBELLA "MMMFGHHH...!!"
        MAN "I told you the rumors were true! See?"
        MAN "They said there was a monster walking around here at night fucking some girl!"
        WOMAN "I... I don't believe it!"
        WOMAN "(What's wrong with me? Why is this... {i}thing{/i} so strangely atttractive?)"
        WOMAN "(Oh gods, I best not say anything, my husband will think I'm some kind of pervert!)"
        MAN "I've seen some crazy things in this city, but this might be the craziest!"
        WOMAN "H-Her rear... That monster is putting it in her rear!"
        MAN "Better that than the thing wants to kill us!"
        MAN "See? I told you that you should let me put it there sometimes too!"
        WOMAN "S-She can't possibly be enjoying that..."
        MC "Why don't you tell them how you feel, Marbella?"
        MC "{i}Do you like being my private cock-milker?{/i}"
        MARBELLA "(I can't... I CAN'T!)"
        $ PlaySexFx(audio.nijah_miss_3, 1)
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_3 with dissolve
        else:    
            scene marbella_dom_alleyway_nopreg_3 with dissolve
        $ Pause()
        "Something snapped within her."
        MARBELLA "I love it!"
        MARBELLA "L-LET THEM SEE!"
        MARBELLA "D-Don't stop! Keep filling me up!"
        WOMAN "W-We should go!"
        MC "Thanks for saying hello!"
        "The couple hurried off."
        MARBELLA "HAHAHAHA!"
        MARBELLA "I did it! I let them see!"
        MARBELLA "I'm such a fuckin' whore for you!"
        MC "{i}You love it.{/i}"
        MARBELLA "YES I FUCKING LOVE IT!"
        MARBELLA "LET THEM HEAR!"
        MC "I'm getting close!"
        MARBELLA "Fill me up!"
        "Her asshole squeezed tighter than ever."
        "I buried myself deep and filled her ass with a thick burst of seed."
        MC "HRGHHHHHHH...!"
        MARBELLA "YESSSSSSSS...!!!"
        $ PlaySexFx(audio.nijah_miss_finish)
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_finish with flash
        else:    
            scene marbella_dom_alleyway_nopreg_finish with flash
        $ Pause()
        "She shuddered as I pumped her full."
        MC "Marbella?"
        MARBELLA "... Zzzz."
        "Fucked unconscious. A new one."
        scene black with dissolve
        return
    elif tmpvar["variant"] == "vag":
        MC "Another time. Your tight cunt is mine tonight."
        MARBELLA_ROBE @lewd "Mmm, yesss...!"
        scene black with dissolve
        "{i}A few minutes later...{/i}"

        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_1 with dissolve
        else:    
            scene marbella_dom_alleyway_nopreg_1 with dissolve
        $ Pause()

        "Tied and strapped to my body, Marbella wiggled beneath the restraint as she looked back towards me."
        MARBELLA "{i}*Quiet*{/i} Want me to play it up like I'm still resisting your wonderful cock?"
        MC "Haha... If it pleases you."
        MARBELLA "A-Ahh...! Y-You won't break me!"
        MARBELLA "Y-You think you can just shove that cock in me anytime you want and I'll just-"

        $ PlaySexFx(audio.nijah_miss_1, 1)
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_2 with dissolve
        else:    
            scene marbella_dom_alleyway_nopreg_2 with dissolve
        $ Pause()

        "Tied and strapped, she groaned as I thrust into her."
        MARBELLA "H-HRGHHH...!"
        MARBELLA "T-That's it! Mmfghh!"
        MARBELLA "Break me! BREAK ME AGAIN!"
        "Her round, fat ass slammed against my cock,"
        "her tight pussy squeezing as it dragged to the hilt."
        MC "Haha... So eager to give up being a silly dwarf with all your paperwork and worries."
        MC "Isn't it so much better just being my cocksleeve?"
        MARBELLA "Mmmfghh...!! {image=[ICON.HEART]}"
        MC "... Ah! Look, some people coming our way!"
        MC "Ready for another audience?"
        MARBELLA "Nooooo...!"
        MARBELLA "(Yes! Yes! YES!)"
        MARBELLA "(I'm gonna cum! I'll CUM IF THEY SEE ME!)"
        "The couple approached, at first, their faces ones of shock."
        "But then, the couple smiled at the perverted scene before them."
        MARBELLA "Urghhhh....ffghhh!!"
        MAN "See? I told you the rumors were true!"
        WOMAN "It's... It's fucking her."
        WOMAN "That monster is actually fucking her!"
        WOMAN "S-Should we do something?!"
        MAN "She seems happy to me."
        MC "Don't mind me."
        MC "My breeding sow here just needs her nightly filling."
        "Marbella could only quiver in shameful delight at my words."
        "Marbella climaxed as they watched."
        MARBELLA "MMMFGHHH...!!"
        WOMAN "It SPEAKS!"
        MARBELLA "P-Pweaseee! Mmfghh!"
        MARBELLA "L-Let himhh carryhhh onhhh!"
        WOMAN "W-What?"
        WOMAN "Do you really... {i}enjoy this?{/i}"
        MC "Yes, slut... {i}Tell them.{/i}"
        MC "Do you like being my private cock-milker?"
        MARBELLA "I LOVE IT!"
        MARBELLA "LET THEM SEE!"

        $ PlaySexFx(audio.nijah_miss_3, 1)
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_3 with dissolve
        else:    
            scene marbella_dom_alleyway_nopreg_3 with dissolve
        $ Pause()

        "I began to move faster, slamming into my personal fucktoy as her cunt quivered and tightened around me."
        MARBELLA "F-FUCKKHHH!"
        MARBELLA "It'sh shoooo fuckin' goodhhhh!"
        MC "Not so shy anymore, huh?"
        MARBELLA "F-FUCKK MHEEE! FUCK MHEEE SHOOO HARD!"
        MARBELLA "I whuvhhh him! I WHUVHH HIM AND HISHH HUGE COCKHHH!"
        "The woman's cheeks burned red as she tightened her hands around her dress."
        "The man watched mesmerised, grinning as the blood rushed to his groin."
        WOMAN "Oh... {i}Oh my...{/i}"
        MARBELLA "Break me! Break my tight little pussy!"
        MARBELLA "DON'T STOPHH TILL YOU FILL ME UP YOU FUCKKK!"
        MARBELLA "MMFGHHH!"
        "Marbella quivered, trembling with another orgasm."
        "Fucked into oblivion, her mind completely gone,"
        "Marbella could only slur out increasingly lewd and incomprehensible words and moans as my balls slapped against her clit."
        "Finally, I found myself drawing close."
        MC "I'm getting close!"
        MARBELLA "Fill me up!"
        "Her pussy clenched tight."

        $ PlaySexFx(audio.nijah_miss_finish)
        if tmpvar["preg"] == True:
            scene marbella_dom_alleyway_preg_finish with flash
        else:    
            scene marbella_dom_alleyway_nopreg_finish with flash

        $ Pause()

        "She shuddered as I pumped her full of my heavy load."
        "Her eyes rolling white as she let out a desperate, breathless moan."
        MC "HRGHHHHHHH...!"
        MARBELLA "YESSSSSSSS...!!!"
        MARBELLA "{i}SHOOO GHODHHH!{/i} {image=[ICON.HEART]} {image=[ICON.HEART]}"
        "Änd just like that, Marbella went limp, her cunt relaxing."
        MC "Marbella?"
        MARBELLA "... Zzzz."
        "Fucked unconscious. A new one."
        "I gently and soothing petted Marbella."
        MC "Heh... looks like you're all worn out."
        "I gently gave her butt a slap, and looking up, I realized the couple from before had left."
        "Instead, I could only hear soft moans from a side alleyway... It seems our little show left them too frustrated."
        MC "Time to take you to bed, Marbella."
        MARBELLA "{i}*Grumbles*{/i}"
        scene black with dissolve
        return