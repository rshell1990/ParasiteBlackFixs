label gallery_winward_pimp_doublehj:
    if GalFlag("mrs_winward", "pimp_doublehj", ["cow", "nude"]):
        "Was she wearing her cow outfit?"
        menu:
            "Yes":
                $ tmpvar["cow"] = True
            "No":
                $ tmpvar["cow"] = False

    elif GalFlag("mrs_winward", "pimp_doublehj", "cow"):
        $ tmpvar["cow"] = True
    elif GalFlag("mrs_winward", "pimp_doublehj", "nude"):
        $ tmpvar["cow"] = False
##########    
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    
    if tmpvar["cow"] == True:
        scene mrs_winward_pimp_doublehj_cow_slow with dissolve
    else:
        scene mrs_winward_pimp_doublehj_nude_slow with dissolve
    $ Pause()

    "As I peered around the corner, Mrs Winward was on her knees grinning from ear to ear with her huge breasts exposed as she stroked at two cocks."
    "The third cock was all but consumed by her colossal tits, which the young man held and pressed together."
    YOUNG_MAN "Ahh! Gods! Your tits are so - Ahh! Soft but heavy!"
    MRS_WINWARD "Oooh, I'm sure a big, {i}strong{/i} young lad like yourself will be fine!"
    "Mrs Winward laughed as she continued to stroke the other two young men's cocks."
    TALL_YOUNG_MAN "Uhh, M-Mrs, when can we - Ahh!"
    TALL_YOUNG_MAN "Y-You know... {i}Go all the way?{/i}"
    MRS_WINWARD "Now, now, boys."
    MRS_WINWARD "We have to work up to that!"
    THIN_YOUNG_MAN "But - Ahh! We're all dying to"
    MRS_WINWARD "Shhh, just let me work my magic and drain your big, silly cocks, dry, boys."

    if tmpvar["cow"] == True:
        scene mrs_winward_pimp_doublehj_cow_fast with dissolve
    else:
        scene mrs_winward_pimp_doublehj_nude_fast with dissolve
    $ Pause()

    "Mrs. Winward continued to stroke the two boys' cocks, who groaned happily, whilst the third continued to lewdly thrust and fuck Mrs. Winward's huge tits, which glistened in the light thanks to some lube she must have used."
    YOUNG_MAN "A-Ahh! Your breasts feel so nice!"
    YOUNG_MAN "Mhhfhh! I-I'm really close, Mrs!"
    TALL_YOUNG_MAN "M-Me too!"
    THIN_YOUNG_MAN "Ahhh! L-Let me finish! Please!"
    MRS_WINWARD "Oooh? Already?"
    MRS_WINWARD "Fufu, you boys will need more practice if you're going to please your lady friends!"
    YOUNG_MAN "M-Mhhfhh! P-Please! D-Don't tell Kathryn about this!"
    TALL_YOUNG_MAN "A-Anya's noticed an improvement thanks to your training!"
    THIN_YOUNG_MAN "Venza s-says I last longer now..."
    MRS_WINWARD "Don't worry dearies, {i}My lips are sealed{/i}"
    MRS_WINWARD "Now cover me in your spunk."
    YOUNG_MAN "Y-Yes, ma'am!"
    TALL_YOUNG_MAN "H-Hrghhh!"
    THIN_YOUNG_MAN "S-So good! {i}*Huff*{/i}"

    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")

    if tmpvar["cow"] == True:
        scene mrs_winward_pimp_doublehj_cow_finish with dissolve
    else:
        scene mrs_winward_pimp_doublehj_nude_finish with dissolve
    $ Pause()

    "The three boys, on command, grunted quickly one after the other as they fired their loads, covering a very smug-looking Mrs. Winward, now plastered in their dripping seed."
    "Mrs. Winward scooped up some of the seed spilt onto her chest and pushed the finger into her mouth to taste."
    MRS_WINWARD "Mhmm!"
    MRS_WINWARD "Very good boys, don't forget, same time next week! Fufu! {image=[ICON.HEART]}"
    return