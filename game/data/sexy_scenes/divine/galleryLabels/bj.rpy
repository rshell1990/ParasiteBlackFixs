label gallery_divine_bj:
    if GalFlag("divine", "bj", "var_first") and (GalFlagCount("divine", "bj") > 1):
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["first_time"] = True
            "No":
                $ tmpvar["first_time"] = False
    else:
        $ tmpvar["first_time"] = True
####################
    if not tmpvar["first_time"]:
        if (GalFlag("divine", "bj", "ling_preg") or GalFlag("divine", "bj", "ling_nopreg")) and (GalFlag("divine", "bj", "naked_nopreg") or GalFlag("divine", "bj", "naked_preg")):
            "Was she wearing her lingerie?"
            menu:
                "Yes":
                    $ tmpvar["ling"] = True
                "No":
                    $ tmpvar["ling"] = False
        else:
            if GalFlag("divine", "bj", "ling_preg") or GalFlag("divine", "bj", "ling_nopreg"):
                $ tmpvar["ling"] = True
            else:
                $ tmpvar["ling"] = False
####################
        if (GalFlag("divine", "bj", "ling_preg") or GalFlag("divine", "bj", "naked_preg")) and (GalFlag("divine", "bj", "ling_nopreg") or GalFlag("divine", "bj", "naked_nopreg")):
            "Was she pregnant at the time?"
            menu:
                "Yes":
                    $ tmpvar["preg"] = True
                "No":
                    $ tmpvar["preg"] = False
        else:
            if (GalFlag("divine", "bj", "ling_preg") or GalFlag("divine", "bj", "naked_preg")):
                $ tmpvar["preg"] = True
            else:
                $ tmpvar["preg"] = False
    else:
        $ tmpvar["preg"] = False
        $ tmpvar["ling"] = True
####################
    jump gallery_divine_bj_scene

label gallery_divine_bj_scene:
    $ PlayMusicRandom("mus_sex")
    if tmpvar["first_time"]:
        scene divine_bj_ling_idle_nopreg_notent with dissolve
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_idle_preg_notent with dissolve
            else:
                scene divine_bj_ling_idle_nopreg_notent with dissolve
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_idle_preg_notent with dissolve
            else:
                scene divine_bj_naked_idle_nopreg_notent with dissolve
    $ Pause()
    "From my back, two of the tentacles emerged and coiled around Sister Divine, her shock quickly made way to giggles as the tentacles lifted her off her feet and dangled her in front of my hardened cock."
    DIVINE "Oh...!"
    "My rock hard, ribbed cock pressed up and rubbed against her cheek."
    DIVINE "Well, I suppose that’s one way to tell me you want me to suck your cock."
    "The tentacles suspending her in the air gently rocked her back and forward, tapping the head of my cock against her face playfully."
    "Sister Divine laughed once again,"
    DIVINE "Keen... Aren’t we?"
    "I let out a low rumble."
    DIVINE "Such an impatient lover!"
    DIVINE "Very well~"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    if tmpvar["first_time"]:
        scene divine_bj_ling_bj_nopreg_notent with dissolve
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_bj_preg_notent with dissolve
            else:
                scene divine_bj_ling_bj_nopreg_notent with dissolve
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_bj_preg_notent with dissolve
            else:
                scene divine_bj_naked_bj_nopreg_notent with dissolve
    $ Pause()
    "Opening her mouth, Sister Divine gently wrapped her lips over the head as she slowly rocked her head as far forward as she could."
    "Her tongue flicking and dancing over the sensitive head sent sparks of pleasure coursing through me."
    DIVINE "{i}*Slurp!*{/i} mmmfghh...! {image=[ICON.HEART]}"
    "Sister Divine continued to coo and moan as she worked her wet mouth over my cock."
    "Letting out heavy, animal like breaths, I let her continue to pleasure me obediently, gently rocking her forward to try and force her face deeper onto my cock."
    "She grunted and slurped on it, devouring it eagerly."
    DIVINE "(Mfghh...I feel like I can barely wrap my lips around it.)"
    DIVINE "(Fufu, doesn't mean I won't give it a good try! {image=[ICON.HEART]})"
    DIVINE "{i}Slurp!{/i} Mfghhh!"
    "I let out another low rumble of approval, gently rocking her suspended body back and forth further as I tried to get her to swallow my cock more deeply."
    DIVINE "(Ooh! So you want me to shove this cock even deeper into me, huh?)"
    DIVINE "(Such a naughty creature... Come then, let's see what you've got!)"
    if tmpvar["first_time"]:
        scene divine_bj_ling_dt_nopreg_notent with dissolve
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_dt_preg_notent with dissolve
            else:
                scene divine_bj_ling_dt_nopreg_notent with dissolve
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_dt_preg_notent with dissolve
            else:
                scene divine_bj_naked_dt_nopreg_notent with dissolve
    $ Pause()
    "Divine's mouth opened wider as she swallowed a few more inches of my cock, slightly gagging in the process." # - DEEP THROAT BJ
    "My cock was secreting the sensation-enhancing chemicals and pretty soon, Sister Divine was dripping sweat as she hungrily sucked on it, forcing it as deeply down her throat as she could go."
    DIVINE "Mmmfghh!!"
    DIVINE "(Incredible... My whole body feels like it’s burning up!)"
    DIVINE "(I just don’t want to stop!)"
    "As I watched Sister Divine’s breasts swing back and forth, her lips glided over my cock coating it in silvery saliva."
    "I felt the animalistic urge to use the rest of my tentacles..."
    "From over my shoulders, two more tentacles slid down, their teeth retracted as they snaked their way up past Sister Divine’s stomach towards her breasts."
    DIVINE "(W-What are you-)"
    if tmpvar["first_time"]:
        scene divine_bj_ling_dt_nopreg_tent with hpunch
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_dt_preg_tent with hpunch
            else:
                scene divine_bj_ling_dt_nopreg_tent with hpunch
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_dt_preg_tent with hpunch
            else:
                scene divine_bj_naked_dt_nopreg_tent with hpunch
    $ Pause()
    "Suddenly, the two tentacles attached to her breasts and began to suckle at them." 
    DIVINE "Mmmfgh?!"
    DIVINE "(They’re... They’re sucking me like... like...)"
    DIVINE "(Ooooh! They’re a little rough but it feels so nice!)"
    DIVINE "(Hungry... aren’t they? Ah! {image=[ICON.HEART]})"
    DIVINE "{i}*Glug!* *Slurp!*{/i} mmmffgh!!"
    "Sister Divine grunted in pleasure as the two tentacles did their best to milk her large dangling breasts."
    "Her rock-hard cock twitched in excitement, helpless as I continued to plunge my own past her soft lips."
    DIVINE "Mhmm! MHHH!"
    "Sister Divine's body began to drip with sweat, the aphrodisiac omitting from my skin drove her deeper and deeper into a fever of lust."
    DIVINE "(Gods... What's happening to me?)"
    if tmpvar["first_time"]:
        DIVINE "(I didn't understand why I was so drawn to him but-)"
        DIVINE "(Mmmfghh! It's so clear now!)"
    else:
        DIVINE "(I didn't understand at first but-)"
        DIVINE "(Mmmfghh! Every time we fuck it becomes more and more clear to me!)"
    DIVINE "(It's so good!)"
    "I continued to thrust my cock into Sister Divine's warm, wet mouth for some time, listening to her hot wet slurps and moans as she tried to take my cock as deeply as she could down her throat."
    if tmpvar["first_time"]:
        scene divine_bj_ling_idle_nopreg_tent with dissolve
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_idle_preg_tent with dissolve
            else:
                scene divine_bj_ling_idle_nopreg_tent with dissolve
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_idle_preg_tent with dissolve
            else:
                scene divine_bj_naked_idle_nopreg_tent with dissolve
    $ Pause()
    "For a brief moment, I unsheathed my cock from Sister Divine's mouth." #idle + tit milking
    DIVINE "What - {i}*Huff*{/i} are you doing?"
    DIVINE "Give it back! Give me your cock!"
    "I let out another low rumble and Divine laughed."
    DIVINE "Haha! You want me to beg?"
    "I nodded, rumbling once more in acknowledgment."
    DIVINE "Ooooh! They feel so good milking me! Mmfhh! "
    DIVINE "F-Fine you petulant beast, ram that fucking cock down my throat!"
    DIVINE "Make me your bitch!"
    play sound2 "audio/cfx/transform.ogg"
    if tmpvar["first_time"]:
        scene divine_bj_ling_dt_nopreg_tent with hpunch
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_dt_preg_tent with hpunch
            else:
                scene divine_bj_ling_dt_nopreg_tent with hpunch
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_dt_preg_tent with hpunch
            else:
                scene divine_bj_naked_dt_nopreg_tent with hpunch
    $ Pause()
    "I roared as I slammed my cock down into her throat once more." #DEEP THROAT BJ 
    DIVINE "Mmfghh!! {i}Slurp!{/i}"
    DIVINE "(Yes! Yes! More!)"
    DIVINE "(I'm so ... I'm so...!)"
    "Between Divine's legs, a small pool was growing as her wet juices trickled down her leg onto the floor in little drops."
    "Her tongue thrashed desperately to please me as she let out muffled moaned so very sweetly for me."
    DIVINE "Mmfghhhhhhh...!! {i}Slurp!{/i}"
    "Eventually, after body continued to shudder time and time again with orgasms rippling through her, I felt my own climax finally drawing close."
    DIVINE "{i}*Slurp!* *Slurp!* Mhmfghh!{/i} {image=[ICON.HEART]}"
    DIVINE "(Mhff! He's close! I c-can feel him throbbing in my mouth!)"
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    play sound2 "audio/cfx/transform.ogg"
    if tmpvar["first_time"]:
        scene divine_bj_ling_nopreg_finish with flash
    else:
        if tmpvar["ling"]:
            if tmpvar["preg"]:
                scene divine_bj_ling_preg_finish with dissolve
            else:
                scene divine_bj_ling_nopreg_finish with dissolve
        else:
            if tmpvar["preg"]:
                scene divine_bj_naked_preg_finish with dissolve
            else:
                scene divine_bj_naked_nopreg_finish with dissolve
    $ Pause()
    "Unable to hold back any longer, I gripped Sister Divine's head and pulled her forward towards me, forcing every inch of my cock down her throat as I roared and flooded her belly with my seed."
    DIVINE "{i}*Glughhh!*{/i} Mmmfghhhh...! {image=[ICON.HEART]}"
    "Sister Divine shuddered as she desperately tried to swallow the overflowing seed that seeped out of her mouth onto the floor."
    "Her stomach began to bloat slightly as I continued pouring into her, till finally, I slowly unsheathed my cock, letting her gasp for air as she coughed and spluttered."
    DIVINE "*Cough!* Gods...!"
    DIVINE "{i}*Huff*{/i} {i}*Huff*{/i}"
    "With two loud *plops* my tentacles unshackled themselves from her now sore, over-stimulated breasts, and I gently pulled and laid her down to rest on her bed."
    return