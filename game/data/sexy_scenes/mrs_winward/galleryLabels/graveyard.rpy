label gallery_winward_grave: 
    if GalFlag("mrs_winward", "grave", ["preg", "nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False

    elif GalFlag("mrs_winward", "grave", "preg"):
        $ tmpvar["preg"] = True
    elif GalFlag("mrs_winward", "grave", "nopreg"):
        $ tmpvar["preg"] = False
    
#######
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if tmpvar["preg"] == True:
        scene mrs_winward_grave_preg_idle with dissolve
    else:
        scene mrs_winward_grave_nopreg_idle with dissolve
    $ Pause()

    MRS_WINWARD "Mhmmm..."
    MRS_WINWARD "I hope you're watching this, dear... Wherever you are."
    MRS_WINWARD "I want you to {i}see{/i} why I won't be crying over you anymore..."
    "As Mrs Winward lightly wiggled and pushed her immense ass up against me, swallowing my cock briefly in the crack, I could feel rubbed up against her just how wet she was becoming."
    "She tilted her head to look back towards me as she muttered,"
    MRS_WINWARD "I - I'm ready."
    MRS_WINWARD "{i}Put it in.{/i}"
    
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    if tmpvar["preg"] == True:
        scene mrs_winward_grave_preg_slow with dissolve
    else:
        scene mrs_winward_grave_nopreg_slow with dissolve
    $ Pause()

    "Doing as she asked, I first pressed the head of my cock against her wet slit, and as I pushed against her, she moaned softly as her lips spread and wrapped around my cock."
    MRS_WINWARD "Mhfghhh...!"
    MC "Are you okay?"
    MRS_WINWARD "I'm fine - {i}*Huff*{/i} Just... Put it in!"
    "Inch by inch, I pushed the rest of my cock into her warm insides."
    "At first, she gasped in a mixture of shock and surprise as she felt the large member push its way up into her."
    "She winced with pain, but as she squeezed around me, I slowly began to rock back and forth, gently fucking her."
    MRS_WINWARD "Oooooh!!"
    MRS_WINWARD "H-He's so big dear... Mfghh!"
    MRS_WINWARD "{i}So big.{/i}"
    "Gently, flesh collided as I slapped up against her butt, her ass jiggling with every thrust and impact."
    "She moaned softly, her huge breasts swinging like two huge church bells with every motion."
    MRS_WINWARD "Ahhh! Ahhh! Mmfghh!! {image=[ICON.HEART]}"
    MRS_WINWARD "H-Harder! Harder deary!"
    MRS_WINWARD "Mmfghhh! So good!"

    if tmpvar["preg"] == True:
        scene mrs_winward_grave_preg_fast with dissolve
    else:
        scene mrs_winward_grave_nopreg_fast with dissolve
    $ Pause()

    "Picking up the pace, I began to slam against her fat ass as she groaned hotly."
    "Had the air warmed up suddenly? Or did her body feel so good that I no longer noticed the cool breeze?"
    "Her ass rippled with every thrust as I kneaded the fat between my fingertips as I squeezed her round butt."
    MRS_WINWARD "OOOOOOOOOH!! Y-Yes! That's it! Mhfghh! Just like that!"
    MRS_WINWARD "S-See dear? I'm going to - Ahh!"
    MRS_WINWARD "B-Be just fine without you!"
    MRS_WINWARD "F-Fuckkk! Ooooh!!"
    MC "Mrs Winward - {i}*Huff*{/i} We should - Ahh!"
    MC "Hurry up before someone sees us!"
    MRS_WINWARD "Ahh! Just - Mhhfghh! F-Fill me up whenever you're ready, dear!"
    MRS_WINWARD "F-Filling me up is {i}your{/i} job now, dear!"
    "Mrs Winward continued to sickly moan in pleasure, her knees trembling as I continued to thrust into her slick, wet, tight hole."
    "As our sweat glistened in the moonlight, I began to feel my balls rise as my cock tightened,"
    "The inevitable building sensation for release becoming increasingly unbearable with each passing thrust."
    MRS_WINWARD "Yes... Mhfghh! J-Just like that! Just like-"
    MRS_WINWARD "MMMFGHHHHH!! {image=[ICON.HEART]}"
    "As Mrs Winward's whole body shuddered and tightened around me, the sudden sensation was too much."
    "I grunted loudly as I spilled my load into her body; her mouth hung open as she gasped, feeling the thick seed fill her up."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    if tmpvar["preg"] == True:
        scene mrs_winward_grave_preg_finish with flash
    else:
        scene mrs_winward_grave_nopreg_finish with flash
    $ Pause()

    MC "H-HRGHHHH!"
    MRS_WINWARD "O-Oooooooooooooooooh!!"
    "As I poured out the last of my seed into her willing, eager body, I held her in my grasp tightly for a moment, letting the waves of pleasure pass by."
    "After a few moments, I slowly stumbled back, pulling my cock outside of her now well fucked hole."
    return