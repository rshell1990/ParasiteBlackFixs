label gallery_winward_stool:
    scene black with dissolve
    if GalFlag("mrs_winward", "stool", ["preg", "nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar = "preg"
            "No":
                $ tmpvar = "nopreg"
    elif GalFlag("mrs_winward", "stool", "preg"):
        $ tmpvar = "preg"
    elif GalFlag("mrs_winward", "stool", "nopreg"):
        $ tmpvar = "nopreg"

    "...As I approached the table, the two looked up and smiled from their food."
    MRS_WINWARD "Oh! [player_name!t], what brings you here?"
    MR_WINWARD "Would you like some food?"
    "As my eyes wandered towards Kionni's round ass, a perverse thought crossed my mind as she bit into her bread."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    MC "{i}I'm hungry for something alright.{/i}"
    if tmpvar == "preg":
        scene mrs_winward_stool_preg_idle with dissolve
    if tmpvar == "nopreg":
        scene mrs_winward_stool_nopreg_idle with dissolve
    $ Pause()
    "Hiking up her skirt, Mrs. Winward gasped as she looked behind to see me staring intently at her naked ass, with the small gemstone toy lodged into her tight asshole."
    MRS_WINWARD "W-Wait! I can explain-!"
    "A smile crept across Mr Winward's face as he waited in excitement."
    MC "What's there to explain?"
    MRS_WINWARD "I... I must wear it occasionally to ensure I can handle your b-back there..."
    MC "Then let's check in on your progress, shall we?"
    MR_WINWARD "Hoho! Yes! Absolutely!"
    MRS_WINWARD "B-But, the food-!"
    "Gently, I reached down and gripped the sides of the toy stuffed into her asshole, pulling out the toy."
    MRS_WINWARD "A-Ahhh...!"
    "As the jewelled toy popped out, Mrs. Winward's slightly gaping ass winked and tightened at me as her cheeks flushed red from embarrassment."
    MRS_WINWARD "...D-Don't just keep staring at it like that!"
    MRS_WINWARD "Oh gods, how shameful!"
    MR_WINWARD "You're absolutely right, honey!"
    MR_WINWARD "He definitely needs to close it up with {i}something!{/i}"
    "Smirking as I pulled out my hardened, excited cock and aligned it against her open hole, Mrs Winward's breath trembled as she felt the head prod against her."
    MRS_WINWARD "R-RIGHT NOW?!"
    MRS_WINWARD "Oh my, but I haven't even d-done my hair or-"
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    if tmpvar == "preg":
        scene mrs_winward_stool_preg_slow with dissolve
    if tmpvar == "nopreg":
        scene mrs_winward_stool_nopreg_slow with dissolve
    $ Pause()
    "As I slowly sunk my cock into Mrs Winward's ass, she gasped, feeling inch after inch fill up her fat butt."
    MRS_WINWARD "M-MMFGHHH!"
    MRS_WINWARD "S-Slowly! Ahh! It s-still burns a little! Mhmm!"
    MR_WINWARD "Don't worry, dear! I've seen all the work you've been putting into training that fat ass!"
    MR_WINWARD "You can definitely handle him!"
    "Mrs. Winward whimpered in response, letting out a guttural moan half in pain, half in pleasure as I felt my cock bury into her ass."
    MRS_WINWARD "G-GODSSSS...!"
    MRS_WINWARD "{i}*Huff*{/i} S-Slowly dear, please!"
    "Reaching to grab a fist full of her hair, I lightly tugged and pulled Mrs Winward's head back as another shocked but short gasp escaped her lips."
    "Slowly, in a steady motion, I fucked Mrs Winward's ass, watched as her stretched ring tightened and squeezed around me."
    "Her husband watched in a mixture of arousal and awe as he saw his wife's ass being stretched out in front of him."
    MR_WINWARD "How... How is it, dear?"
    MRS_WINWARD "G-Grghhhffhh!"
    MRS_WINWARD "{i}S-So full!{/i}"
    if tmpvar == "preg":
        scene mrs_winward_stool_preg_fast with dissolve
    if tmpvar == "nopreg":
        scene mrs_winward_stool_nopreg_fast with dissolve
    $ Pause()
    "Mrs Winward's cheeks flushed red as my cock sunk in and out of her ass deeper and faster."
    MRS_WINWARD "Mhfhh... Ahhh! G-Gods...!"
    MR_WINWARD "T-Tell me how it feels stretching you out, dear!"
    MRS_WINWARD "H-Hrghh! You're such a - Mhfhh! Old p-pervert!"
    MRS_WINWARD "Do you like this, dear? Do you like seeing me- Hrghh! Get my ass fucked by him instead of you?"
    "Like an obedient dog, Mr Winward nodded lightly, grinning as he watched the obscene scene before him."
    "Now moving faster, the loud sounds of flesh slapping and grunts filled the room as I slammed my cock into Kionni's ass."
    "As my cock sunk in and out of her tight backdoor, Mrs Winward hotly cooed and moaned as she let me continue to abuse her poor little hole."
    MRS_WINWARD "AH! Ah! Mhhfhh! F-Finish soon! Please! Mmhhh!!"
    MRS_WINWARD "My - {i}*Huff*{/i} poor little - {i}*Huff*{/i} asshhhh! {image=[ICON.HEART]}"
    MRS_WINWARD "F-Finish soon! Please! I can't take - Mhhh! Much more of this!"
    "After a few more minutes of slamming into Kionni's fat ass, watching with delight as the fat rippled with every thrust, I began to feel my own bubbling desire becoming more and more overwhelming."
    "My balls tightened and rose up, and finally, as I slammed and buried my cock up to the hilt of Mrs Winward's ass, I loudly grunted as I flooded Mrs Winward's bowels with my load."
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")

    if tmpvar == "preg":
        scene mrs_winward_stool_preg_finish with dissolve
    if tmpvar == "nopreg":
        scene mrs_winward_stool_nopreg_finish with dissolve
    $ Pause()

    MC "H-Hrghhhhhhhh...!!"
    "Mrs Winward shuddered, letting out a quivering moan when she finally realized we were done."
    "Unsheathing my cock from her ass, I watched as my overspilling seed spilt out onto the floor from her gaping hole."
    "Letting go of her hair, Kionni's head dropped down onto the table as she sat there, catching her breath exhaustedly."
    MR_WINWARD "...D-Dear?"
    MRS_WINWARD "{i}*Huff*{/i} I just need - {i}*Huff*{/i} time to rest."
    scene black with dissolve
    return