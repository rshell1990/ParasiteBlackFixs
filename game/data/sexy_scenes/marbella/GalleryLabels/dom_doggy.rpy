label gallery_marbella_dom_doggy:
    scene black with dissolve
    # choose first or rep
#########
    if GalFlagsWithSubstring("marbella", "dom_doggy", "_first") and GalFlagsWithSubstring("marbella", "dom_doggy", "_rep"):
        "Was it our first time?"
        menu:
            "Yes":
                $ tmpvar["first"] = True
            "No":
                $ tmpvar["first"] = False
    elif GalFlagsWithSubstring("marbella", "dom_doggy", "_first"):
        $ tmpvar["first"] = True
    else:
        $ tmpvar["first"] = False
#########
    if GalFlagsWithSubstring("marbella", "dom_doggy", "preg_") and GalFlagsWithSubstring("marbella", "dom_doggy", "nopreg_"):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False
    elif GalFlagsWithSubstring("marbella", "dom_doggy", "preg_"):
        $ tmpvar["preg"] = True
    else:
        $ tmpvar["preg"] = False
#########
    if GalFlagsWithSubstring("marbella", "dom_doggy", "_ling_") and GalFlagsWithSubstring("marbella", "dom_doggy", "_naked_"):
        "Was she naked or wearing her lingerie?"
        menu:
            "Naked":
                $ tmpvar["cloth"] = "naked"
            "Lingerie":
                $ tmpvar["cloth"] = "ling"
    elif GalFlagsWithSubstring("marbella", "dom_doggy", "_ling_"):
        $ tmpvar["cloth"] = "ling"
    else:
        $ tmpvar["cloth"] = "naked"
############
    if GalFlagsWithSubstring("marbella", "dom_doggy", "_vag_") and GalFlagsWithSubstring("marbella", "dom_doggy", "_anal_"):
        "Was it vaginal or anal?"
        menu:
            "Vaginal":
                $ tmpvar["variant"] = "vag"
            "Anal":
                $ tmpvar["variant"] = "anal"
    elif GalFlagsWithSubstring("marbella", "dom_doggy", "_vag_"):
        $ tmpvar["variant"] = "vag"
    else:
        $ tmpvar["variant"] = "anal"

    # "nopreg_ling_vag_first",  "nopreg_naked_vag_first", 
    # "nopreg_ling_anal_first", "nopreg_naked_anal_first",

    # "nopreg_ling_vag_rep",  "nopreg_naked_vag_rep", 
    # "nopreg_ling_anal_rep", "nopreg_naked_anal_rep",

    # "preg_ling_vag_rep",  "preg_naked_vag_rep", 
    # "preg_ling_anal_rep", "preg_naked_anal_rep",

    $ tmpvar["stored_marbella_clothes"] = CharGetClothes("marbella")

    if tmpvar["cloth"] == "naked":
        $ CharSetClothes("marbella", "naked")
    elif tmpvar["cloth"] == "ling":
        $ CharSetClothes("marbella", "ling")

    if tmpvar["first"] == True:
        jump gallery_marbella_dom_doggy_first
    else:
        jump gallery_marbella_dom_doggy_rep

label gallery_marbella_dom_doggy_first:
    MC @smile "Marbella..."
    MC @smile "You and I are going on a date."
    MARBELLA @shock "W-What?!"

    "One hour later..."
    $ AutoMus(False)
    $ AutoAmb(False)
    stop ambience fadeout 0.5
    $ PlayMusicRandom("mus_sex")

    scene marbella_dom_date_nopreg_1 with dissolve
    $ Pause()

    "... Marbella sat sheepishly across from me, her body tucked tightly into the dress as I ate the small banquet laid out before us."
    MC "Mm, the food's great, isn't it?"
    "Marbella's cheeks burned red, her eyes heavy as she struggled to control her wavering, shaky breath."
    MC "Darlingggg..."
    "I waved my fork playfully in front of her."
    MARBELLA "H-Huh?"
    MC "The food is good, right?"
    MARBELLA "Y-Yes."
    MARBELLA "{i}*Gasp!*{/i}"

    $ PlaySexFx(audio.no_voice, 1)
    scene marbella_dom_date_nopreg_2 with dissolve
    $ Pause()

    MC "... Something the matter, love?"
    MARBELLA "{i}*Whispering* Y-You know damn well what's the matter!{/i}"
    "She moaned softly and quickly moved to cover her mouth."
    "I chuckled, grinning as I knew what was going on beneath that dress."
    "Marbella squirmed in her seat; she had hardly touched her food."
    "Grinning, I could feel my thrall, like a limb I still controlled, greedily push its tendrils deeper."
    MARBELLA "M-Mmhhhf...!"
    MC "How do you like my trick?"
    MARBELLA "{i}*Huff*{/i} Your 'trick' is going to -"
    
    scene marbella_dom_date_nopreg_3 with dissolve
    $ Pause()

    MARBELLA "Mhmmffhh..."
    MARBELLA "G-Gods... Was letting it slip one up my cunt not enough?"
    MARBELLA "D-Did you really need to let it put itself in my arse too?"
    MC "Feeling a little... {i}full,{/i} are we?"
    MARBELLA "F-Fuck... {i}*Huff*{/i}"
    MARBELLA "You... {i}*Huff*{/i}"
    MC "Feisty."
    MARBELLA "{i}*Huff*{/i} P-Please..."
    MARBELLA "I can't take much more of this!"
    MC "Then come back to my room for the evening."
    MARBELLA "N-Now?"
    MARBELLA "Mmfghh!!"
    MC "It's either that... or I make you walk around this city with my thrall all night and we find out how many times you can cum before falling unconscious."
    MARBELLA "...You!"
    MARBELLA "{i}*Huff*{/i}... Oh fuck it."
    MARBELLA "My cunt's on fire and you've got me all worked up."
    MARBELLA "L-Let's go back to yours."
    MARBELLA "J-Just make sure none of the others see me, alright?"
    
    $ StopSexFx()
    scene black with dissolve
    "Later at The Pale Dragon..."
    MARBELLA @emb "S-Should I just lay on the bed?"
    MARBELLA @emb "Or-"

    if CharGetClothes("marbella") == "ling":
        scene marbella_dom_doggy_nopreg_ling_alt_idle with dissolve
    elif CharGetClothes("marbella") == "naked":
        scene marbella_dom_doggy_nopreg_naked_alt_idle with dissolve
    $ Pause()

    "Marbella squealed as I pushed her down onto the bed, tendrils from my hand holding her in place."
    MARBELLA "F-Fuck! Let me know when you're just gonna throw me around like that?!"
    "I moved behind her round ass, kneading the soft flesh with both hands as I rubbed my cock against her glistening womanhood."
    "She cooed softly as I slapped her ass, watching her cheeks jiggle as the sound rang out through the room."
    MARBELLA "Eeep!"
    MARBELLA "C-Careful!"
    MARBELLA "If the boys see a red handprint on my arse, they'll know what we've been up to for sure!"

    if CharGetClothes("marbella") == "ling":
        scene marbella_dom_doggy_nopreg_ling_idle with dissolve
    elif CharGetClothes("marbella") == "naked":
        scene marbella_dom_doggy_nopreg_naked_idle with dissolve
    $ Pause()

    "Her hands squeezed at the bed quilts as she waited nervously for what was to come."
    MC "So... tell me, when my thrall was playing with your cunt and asshole, which did you prefer?"
    "Marbella's cheeks turned an even brighter shade of red. If she could have hidden her face beneath a pillow, she would have."
    MARBELLA "Y-You can't be seriously asking me that!"
    MARBELLA "Not when I'm waving my fat ass in your face right now!"
    MC "Stop thinking about being embarrassed."
    "I gently traced my finger upward."
    MC "Be honest."
    "My finger pressed against her pussy, scooping up some of her juices before I lightly prodded my thumb against her asshole."
    "She let out a little gasp, followed by a breathless, quiet moan."
    MARBELLA "... Gods, I'll kill you if you ever talk to anyone about this."
    MC "Where do you want me to shove my cock, Marbella?"
    "She shuddered, breathing heavily."
    MARBELLA "... P-Pick whatever hole you like, you big-dicked bastard."
    
    if tmpvar["variant"] == "vag":

        $ PlaySexFx(audio.nijah_miss_1, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_vag_1 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_vag_1 with dissolve
        $ Pause()

        "As I pushed my cock against her wet slit, Marbella let out a guttural moan as she felt my member enter her."
        MARBELLA "F-FUCKKK!"
        MARBELLA "{i}*Huff*{/i} Oh fuck! Fuck! Fuck!"
        
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_2 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_1 with dissolve
        $ Pause()

        MARBELLA "Y-You're stretching me good back there! Mmffghh!"
        "As I began to slowly move my cock in and out of her, Marbella gently bounced her ass back and forth, matching my pace."
        MC "Enjoying yourself?"
        MARBELLA "S-Shut up!"
        MARBELLA "You could at least tell me how tight my cunt is or something! Ahh!"

        $ PlaySexFx(audio.nijah_miss_2, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_vag_2 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_vag_2 with dissolve
        $ Pause()

        "I slammed my cock deeper into her, moving faster as she moaned louder."
        "The bedframe hit against the wall as she gasped, her round ass shaking with every thrust as the sounds of flesh colliding filled the room."
        "*Phap!* *Phap!* *Phap!*"
        MARBELLA "OH GODSSSS...!"
        MC "Does that answer your question about how much I love your {i}tight{/i} cunt?"
        MARBELLA "{i}*Huff*{/i} F-Fuck... More..."
        MARBELLA "More, you fuck!"
        MARBELLA "Ahhh! S-Slam that cock into me!"
        MARBELLA "And use those fucking things of yours to fuck me up!"
        MC "Heh heh, whatever you wish, slut!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_vag_3 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_vag_3 with dissolve
        $ Pause()

        "Two tendrils protruded from my back, slithering around to latch onto her breasts and suckle at them."
        MARBELLA "Oooooh f-fuckkk!"
        MARBELLA "Yer tryna milk me or— Mmfghh! Somethin'?!"
        MC "Haha!"
        MC "I doubt any man could resist a chance to suckle on your tits!"

        $ PlaySexFx(audio.nijah_miss_3, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_4 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_3 with dissolve
        $ Pause()

        MARBELLA "Mmfghh!"
        "Marbella bit down on her lower lip, her tight pussy squeezing around me with every thrust."
        MARBELLA "M-More!"
        MC "More?"
        MARBELLA "AHHHHH! Yes! MORE!"
        MARBELLA "Mmmfghh! Fuck!"
        MARBELLA "You said you'd— Mmfghh! Fuck me up and handle all my needs, right?!"
        MARBELLA "{i}*Huff*{/i} F-Fuck! I'm so pent up and stressed!"
        MARBELLA "Ooooh! This is so good!"
        MARBELLA "M-More! I need just a little more to push me over the edge!"
        MC "I had just the thing!"
        MARBELLA "What do you—"

        $ PlaySexFx(audio.ves69_150, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_vag_4 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_vag_4 with dissolve
        $ Pause()

        "A third tendril appeared, latching onto her face as it pushed its tip into her mouth."
        MARBELLA "Mmmfghh?!"
        "The small dwarf let out a muffled moan as her eyes rolled back."
        MC "There you— Ahh! Go!"
        MC "See? Isn't that better?"
        MC "Instead of running your mouth so much, we just—"
        MC "AHH! Stuff you full of cock!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_5 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_4 with dissolve
        $ Pause()

        MARBELLA "Ooofghhh!"
        MARBELLA "Yhourghh fhillighh mheee uphh!"
        MARBELLA "Mmfghh!"
        "Her guttural moans grew louder, more animal-like as she slammed her ass back against me."
        "She took every inch of my cock, and I smirked watching it press against her stomach."
        MC "Greedy little— Ahh!"
        MC "Dwarven cocksleeve!"
        "Marbella shuddered, her whole body shaking as I felt her wet hole tighten and squeeze around me."
        MARBELLA "MMMMFGHHHHH...!"
        "As she climaxed, I pulled her flesh against me, holding her there."
        "The tight, hot sensation of her pussy pulsing around my cock was more than enough to push me over the edge as well."

        $ PlaySexFx(audio.ves69_finish)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_finish with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_finish with dissolve
        $ Pause()

        MC "GRGHHHH!"
        "I flooded her womb with my seed."

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_vag_finish with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_vag_finish with dissolve
        $ Pause()

        "Marbella could only gasp as she felt the rush of warmth inside of her."
        "After a few moments, I slowly withdrew, grinning in satisfaction."
        "As I pulled out, she let out a soft, shocked shudder."
        "Released from my tendrils' grip, she collapsed face-forward onto the bed, exhausted."
        "She let out small 'ahhh...' sounds, nearly completely out of it."

    elif tmpvar["variant"] == "anal":

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_idle with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_idle with dissolve
        $ Pause()

        "With a mischievous smirk, I pressed the head of my cock against her tight rosebud."
        MARBELLA "W-Wait a second! Uhh! I didn't think you'd actually—"
        
        $ PlaySexFx(audio.nijah_miss_1, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_anal_1 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_anal_1 with dissolve
        $ Pause()

        "The head of my cock stretched her open as her eyes widened in shock."
        MARBELLA "F-FUCKKK!"
        MARBELLA "{i}*Huff*{/i} Oh fuck! Fuck! Fuck!"
        MARBELLA "Y-YER PRICK IS IN MY ARSE, BASTARD!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_2 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_1 with dissolve
        $ Pause()

        MC "Never offer up 'any hole' if you aren't prepared for the consequences, my little slut."
        MARBELLA "Ooophh!"
        "Slowly, I began to thrust back and forth, her tight ass gripping me like a vice."
        
        $ PlaySexFx(audio.nijah_miss_2, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_anal_2 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_anal_2 with dissolve
        $ Pause()

        MC "Gods, you're tight!"
        MARBELLA "{i}*Huff*{/i} F-Fuckin' hells!"
        MARBELLA "It hurts!"
        MC "Shall I stop?"
        MARBELLA "N-No...!"
        MARBELLA "... Just spit on the bloody thing at least!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_3 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_2 with dissolve
        $ Pause()

        "Grinning, I coated myself in saliva."
        "With the added slickness, she began pushing back against me with muffled, heated breaths."
        MARBELLA "Hrghhh! You could at least tell me how tight I am or something!"
        MC "Fishing for compliments?"
        MARBELLA "I'VE EARNED SOME BLOODY COMPLIMENTS!"
        "I thrust deeper, picking up speed as she gasped."
        MC "{b}Your ass is the tightest I've ever fucked.{/b}"
        MARBELLA "Ooooooh ffffuckkkkk...!"
        "*Phap!* *Phap!* *Phap!*"
        MARBELLA "OH GODS MY ASSS!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_anal_2 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_anal_2 with dissolve
        $ Pause()

        MC "Quite the little sadomasochistic anal slut, aren't we?"
        MARBELLA "{i}*Huff*{/i} F-Fuck... More..."
        MARBELLA "M-More...!"

        $ PlaySexFx(audio.nijah_miss_3, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_4 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_3 with dissolve
        $ Pause()

        "Two tendrils slithered forward, latching onto her breasts."
        MARBELLA "Oooooh f-fuckkk!"
        MARBELLA "Least it distracts from the— Ahh!"
        MARBELLA "Pain of you stretchin' me so much!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_anal_3 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_anal_3 with dissolve
        $ Pause()

        MC "Still hurting?"
        MARBELLA "F-Fucking yes!"
        MARBELLA "But don't you dare stop!"
        MC "Say it then."
        MC "Say you like me fucking your ass."
        MARBELLA "AHHHH! YES!"
        MARBELLA "I LIKE YOU FUCKING MY ASS, DAMN IT!"
        "Her body trembled violently as she climaxed around me."

        $ PlaySexFx(audio.ves69_150, 1)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_5 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_4 with dissolve
        $ Pause()

        "A third tendril appeared, latching onto her face as it pushed its tip into her mouth."
        MARBELLA "Mmmfghh?!"
        "The small dwarf let out a muffled moan as her eyes rolled back."
        MC "There you- Ahh! Go!"
        MC "See? Isn't that better?"
        MC "Instead of running your mouth so much! We just-"
        MC "AHH! Stuff you full of cock!"
        MARBELLA "Ooofghhh!"
        MARBELLA "Yhourghh fhillighh mheee uphh!"
        MARBELLA "Mmfghh!"

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_anal_4 with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_anal_4 with dissolve
        $ Pause()

        "My words seemed to trigger something in Marbella."
        "Her guttural moans grew louder, more animal-like as she slammed her fat ass back onto me."
        "She took every inch of my cock, and I smirked as it bulged against her stomach."
        MC "Greedy little- Ahh!"
        MC "Dwarven cocksleeve!"
        "Marbella shuddered, her whole body shaking as her tight asshole squeezed around me."
        MARBELLA "MMMMFGHHHHH...!"
        "As she climaxed, I pulled her flush against me and held her there."
        "The tight, hot sensation of her ass pulsing around my cock was more than enough to push me over the edge as well."

        $ PlaySexFx(audio.ves69_finish)
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_anal_finish with flash
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_anal_finish with flash
        $ Pause()

        "I grunted, holding her folded body against mine as I filled her with my load."
        MC "GRGHHHH!"
        "Marbella let out another muffled moan as she felt the hot seed spill into her."
        MARBELLA "Y-You're filling my ass!"
        "After a few moments, I slowly unsheathed my cock, grinning in satisfaction."

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_finish with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_finish with dissolve
        $ Pause()

        "As I pulled free, she let out a small shudder as my cum poured from her stretched ass onto the bed."
        "Releasing her from my tendrils' grip, she dropped face-first onto the bed, well fucked and exhausted."
        "She let out small 'ahhh...' sounds, barely conscious, as more of my cum occasionally seeped from her tight backdoor."

    scene black with dissolve
    "Afterward, I slowly withdrew."
    "Released from my tendrils, she collapsed forward, trembling and exhausted."
    jump gallery_marbella_dom_doggy_end

label gallery_marbella_dom_doggy_rep:
    MARBELLA @smile "A date, huh?"
    MARBELLA @smile "Will I just be wearing a dress this time?"
    MARBELLA @lewd "Or uhh, will your little 'friend' be hiding under me dress again?"
    MC @smile "You already know the answer."
    MARBELLA @lewd "Mmm... Sounds like fun!"
    MARBELLA @lewd "I'll see you this evening!"

    $ AutoMus(False)
    $ AutoAmb(False)
    stop ambience fadeout 0.5
    "Later that evening..."
    $ Pause(0.5)
    $ PlayMusicRandom("mus_sex")

    if tmpvar["preg"] == True:
        scene marbella_dom_date_preg_1 with dissolve
    else:
        scene marbella_dom_date_nopreg_1 with dissolve
    $ Pause()

    "... Marbella sat sheepishly across from me, her body tucked tightly into the dress as I ate the small banquet laid out before us."
    MC "I do love eating here, don't you?"
    "Marbella's cheeks burned red, her eyes heavy as she struggled to control her wavering breath."
    MARBELLA "Y-Yes..."
    MARBELLA "Coming here is- Mmhhfhh!"
    MARBELLA "THE BEST!"
    MC "The food that good, huh?"
    "I waved my fork playfully in front of her."
    MARBELLA "H-Huh?"
    MARBELLA "O-Oh y-yes..."
    MARBELLA "The food is- Mmfghh!"
    MARBELLA "{i}Sooo good!{/i}"
    MARBELLA "{i}*Gasp!*{/i}"
    MC "... Something the matter, love?"

    $ PlaySexFx(audio.no_voice, 1)
    if tmpvar["preg"] == True:
        scene marbella_dom_date_preg_2 with dissolve
    else:
        scene marbella_dom_date_nopreg_2 with dissolve
    $ Pause()

    MARBELLA "{i}*Whispering* Y-Your little friend is very enthusiastic tonight!{/i}"
    "She moaned softly and, as it slipped from her lips so casually, quickly moved to cover her mouth."
    "I chuckled, grinning as I knew what was going on beneath that dress..."
    "Marbella squirmed in her seat. She had hardly touched her food."
    "Grinning, I felt my thrall, like a limb I could still control, greedily push its tendrils deeper."
    "Beneath the dress, latched onto her skin, the thrall suckled at her breasts with two tendrils as it secretly worked its way into her."
    MARBELLA "M-Mmhhhf...!"
    MC "How do you like my trick?"
    MARBELLA "{i}*Huff*{/i} Your 'trick' is going to-"
    MARBELLA "Mhmmffhh..."

    if tmpvar["preg"] == True:
        scene marbella_dom_date_preg_3 with dissolve
    else:
        scene marbella_dom_date_nopreg_3 with dissolve
    $ Pause()

    MARBELLA "G-Gods... N-Now he's also in my-"
    "Marbella squirmed in her seat."
    MARBELLA "Ooooh...!"
    "I smirked."
    MC "Feeling a little... {i}full{/i}, are we?"
    MARBELLA "I'm gonna... {i}*Huff*{/i}"
    MARBELLA "Make you pay tonight for this! {i}*Huff*{/i}"
    MC "Feisty."
    "Marbella squirmed as I made the creature suckle and move faster, her eyes rolling back."
    MARBELLA "Oh gods..."
    MARBELLA "M-Mfghh!"
    MARBELLA "{i}*Huff*{/i} P-Please..."
    MARBELLA "I can't take much more of this!"
    MC "Ready to get out of here?"
    MARBELLA "Oh gods, yes!"
    MARBELLA "Let's go alreadyyyy!"

    $ StopSexFx()
    scene black with dissolve

    "Later at The Pale Dragon..."

    MARBELLA @lewd "Soooo... How should we-"

    if tmpvar["preg"] == True:
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_preg_ling_alt_idle with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_preg_naked_alt_idle with dissolve
    else:
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_idle with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_idle with dissolve
    $ Pause()

    "Marbella squealed as I pushed her down onto the bed, the tendrils from my hand holding her in place as she stuck out her round, fat ass."
    MARBELLA "{i}*Giggles*{/i} Easy now, boy, we got alllll night, love!"
    "I moved behind her, kneading the soft flesh of her ass with both hands as I rubbed my cock against her glistening womanhood."
    "She cooed softly as I slapped her ass, watching her cheeks jiggle as the sound rang out through the room."
    MARBELLA "Ahh!"
    MARBELLA "Naughty little...!"
    MARBELLA "{i}*Giggles*{/i} You tryna mark me for Gavkat and all the others to see, hm?"

    if tmpvar["preg"] == True:
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_preg_ling_idle with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_preg_naked_idle with dissolve
    else:
        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_idle with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_idle with dissolve
    $ Pause()

    "Her hands squeezed at the bed quilts as she waited nervously for what was to come."
    MC "So... Tell me, when my thrall was playing with your cunt and asshole, which did you prefer?"
    "Marbella's cheeks turned an even brighter shade of red as she squirmed."
    MARBELLA "Your big hard cock in this fat ass waving in your face is what I prefer!"
    MC "Correct answer."
    "I gently traced my finger up."
    "My finger pressed against her pussy, scooping up some of her juices before I lightly prodded my thumb against her asshole."
    "She let out a small gasp, followed by a breathless moan."
    MARBELLA "... Ooooh."
    MARBELLA "Fuckin' tease!"
    MC "Where do you want me to shove my cock, Marbella?"
    "She shuddered, breathing heavily."
    MARBELLA "... P-Pick whatever hole you like, you big-dicked bastard."

    if tmpvar["variant"] == "vag":
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_idle with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_idle with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_idle with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_idle with dissolve
        $ Pause()

        "As I gently rubbed my cock against her glistening, wet hole, Marbella cooed with excitement."
        MARBELLA "F-Fuck... it's like you're rubbing me with a club back there."
        MC "Ready?"
        "Marbella sheepishly nodded."

        $ PlaySexFx(audio.nijah_miss_1, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_vag_1 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_vag_1 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_vag_1 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_vag_1 with dissolve
        $ Pause()

        "As I pushed my cock against her wet slit, Marbella let out a guttural moan as she felt my member enter her."
        MARBELLA "F-FUCKKK!"
        MARBELLA "{i}*Huff*{/i} Oh fuck! Fuck! Fuck!"
        MARBELLA "Y-You're stretching me good back there! Mmffghh!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_1 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_1 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_1 with dissolve
        $ Pause()

        "As I began to move in and out of her slowly, Marbella started to bounce her ass back and forth, matching my pace."
        MC "Enjoying yourself?"
        MARBELLA "S-Shut up!"
        MARBELLA "You could at least tell me how tight my cunt is or something! Ahh!"

        $ PlaySexFx(audio.nijah_miss_2, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_vag_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_vag_2 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_vag_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_vag_2 with dissolve
        $ Pause()

        "I slammed deeper into her, moving faster as she moaned louder."
        "The bedframe hit against the wall as she gasped, her round ass shaking with every thrust as the sounds of flesh colliding filled the room."
        "*Phap!* *Phap!* *Phap!*"
        MARBELLA "OH GODSSSS...!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_2 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_2 with dissolve
        $ Pause()

        MC "Does that answer your question on how much I love your {i}tight{/i} cunt?"
        MARBELLA "{i}*Huff*{/i} F-Fuck... More..."
        MARBELLA "More, you fuck!"
        MARBELLA "Ahhh! S-Slam that cock into me!"
        MARBELLA "And use those fucking things of yours to fuck me up!"
        MC "Heh heh, whatever you wish, slut!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_vag_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_vag_3 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_vag_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_vag_3 with dissolve
        $ Pause()

        "Two tendrils protruded from my back, slithering around to latch onto her breasts and suckle at them."
        MARBELLA "Oooooh f-fuckkk!"
        MARBELLA "Yer tryna milk me or- Mmfghh! Somethin'?!"
        MC "Haha!"
        MC "I doubt any man could resist a chance to suckle on your tits!"
        MARBELLA "Mmfghh!"
        "Marbella bit down on her lower lip."
        "Her tight pussy squeezed around me with every thrust."

        $ PlaySexFx(audio.nijah_miss_3, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_3 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_3 with dissolve
        $ Pause()

        MARBELLA "M-More!"
        MC "More?"
        MARBELLA "AHHHHH! Yes! MORE!"
        MARBELLA "Mmmfghh! Fuck!"
        MARBELLA "You said you'd- Mmfghh! Fuck me up and handle all my needs, right?!"
        MARBELLA "{i}*Huff*{/i} F-Fuck! I'm so pent up and stressed!"
        MARBELLA "Ooooh! This is so good!"
        MARBELLA "M-More! I just need a little more to push me over the edge!"
        MC "I have just the thing!"
        MARBELLA "What do you-"

        $ PlaySexFx(audio.ves69_150, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_vag_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_vag_4 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_vag_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_vag_4 with dissolve
        $ Pause()

        "A third tendril appeared, latching onto her face as it pushed its tip into her mouth."
        MARBELLA "Mmmfghh?!"
        "The small dwarf let out a muffled moan as her eyes rolled back."
        MC "There you- Ahh! Go!"
        MC "See? Isn't that better?"
        MC "Instead of running your mouth so much! We just-"
        MC "AHH! Stuff you full of cock!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_4 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_5 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_4 with dissolve
        $ Pause()

        MARBELLA "Ooofghhh!"
        MARBELLA "Yhourghh fhillighh mheee uphh!"
        MARBELLA "Mmfghh!"
        "My words seemed to trigger something in Marbella."
        "Her guttural moans grew louder, more animal-like as she slammed her fat ass back onto me."
        "She took every inch of my cock, and I smirked as it bulged against her stomach."
        MC "Greedy little- Ahh!"
        MC "Dwarven cocksleeve!"
        "Marbella shuddered, her whole body shaking as her wet hole tightened and squeezed around me."
        MARBELLA "MMMMFGHHHHH...!"
        "As she climaxed, I pulled the little dwarf to the hilt of my cock and held her there."
        "The tight, hot sensation of her pussy pulsing around me was more than enough to push me over the edge as well."
        "I grunted, holding her against me as I filled her with my load."

        $ PlaySexFx(audio.ves69_finish)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_finish with flash
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_finish with flash
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_finish with flash
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_finish with flash

        MC "GRGHHHH!"
        "Marbella let out another muffled moan as she felt the hot seed spill into her."
        "Marbella laid there, quietly, wiggling her butt lightly to make sure every drop was poured into her."
        MARBELLA "{i}*Huff*{/i} I love you..." 

        if CharGetClothes("marbella") == "ling":
            scene marbella_dom_doggy_nopreg_ling_alt_vag_finish with dissolve
        elif CharGetClothes("marbella") == "naked":
            scene marbella_dom_doggy_nopreg_naked_alt_vag_finish with dissolve
        $ Pause()

        "After a few moments, I slowly unsheathed my cock, grinning in satisfaction."
        "As I pulled free, she let out a small shudder as my cum poured from her well-fucked hole onto the bed."
        "Releasing her from my tendrils' grip, she dropped face-first onto the bed, well fucked and exhausted."
        "She let out small 'ahhh...' sounds, barely conscious, as more of my cum occasionally leaked from her."

    if tmpvar["variant"] == "anal":
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_idle with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_idle with dissolve
        else:

            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_idle with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_idle with dissolve
        $ Pause()

        "With a mischievous smirk, I began to prod and push the head of my cock against her tight little rosebud."
        MARBELLA "W-Wait a second! Uhh! I didn't think you'd actually-"

        $ PlaySexFx(audio.nijah_miss_1, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_anal_1 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_anal_1 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_anal_1 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_anal_1 with dissolve
        $ Pause()

        "The head of my cock stretched her asshole as her eyes opened wide in shock."
        "Her hands clenched tightly to the bed quilts as she hissed."
        MARBELLA "F-FUCKKK!"
        MARBELLA "{i}*Huff*{/i} Oh fuck! Fuck! Fuck!"
        MARBELLA "Y-YER PRICK IS IN MY ARSE, BASTARD!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_1 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_1 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_1 with dissolve
        $ Pause()

        MC "Never offer up 'any hole' if you aren't prepared for the consequences, my little slutty pet."
        MARBELLA "Ooophh!"
        MARBELLA "B-Bloody bastard!"

        $ PlaySexFx(audio.nijah_miss_2, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_anal_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_anal_2 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_anal_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_anal_2 with dissolve
        $ Pause()

        "Slowly, I began to push my cock back and forth into her, her tight ass gripping me like a vice."
        MC "Gods, are you tight!"
        MARBELLA "{i}*Huff*{/i} F-Fuckin' hells!"
        MARBELLA "It hurts!"
        MC "Shall I stop?"
        MARBELLA "N-No...!"
        "Marbella paused for a moment, her cheeks flushed red."
        MARBELLA "... Just spit on the bloody thing some more at least!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_2 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_2 with dissolve
        $ Pause()

        "Grinning, I did as she asked, coating my cock in more saliva."
        "Slowly, with the extra slickness, Marbella began to push her fat ass back onto me with muffled, heated breaths."
        MARBELLA "{i}*Huff*{/i} Fuck... Oh fuck..."
        MARBELLA "Hrghhh! You could at least tell me how tight I am or something! Ahh!"
        MC "Fishin' for compliments!"
        MARBELLA "By the gods, man! Mhfhh! I'm taking your huge cock up my brown hole!"
        MARBELLA "I'VE EARNED SOME BLOODY COMPLIMENTS!"
        "I slammed deeper into her, thrusting faster as she gasped."
        MC "{b}Your ass is the tightest I've ever fucked.{/b}"
        MARBELLA "Ooooooh ffffuckkkkk...!"
        "The bedframe hit against the wall as her round ass shook with every thrust, the sounds of flesh colliding filling the room."

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_anal_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_anal_2 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_anal_2 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_anal_2 with dissolve
        $ Pause()

        "*Phap!* *Phap!* *Phap!*"
        MARBELLA "M-MYHH AHHSSS...!"
        MARBELLA "OH GODSHHH MYHHH ASHHHH!"
        MC "Quite the little sadomasochistic anal slut, aren't we?"
        MARBELLA "{i}*Huff*{/i} F-Fuck... More..."
        MARBELLA "My ashhh!"
        MARBELLA "Y-You're ruining my ashhh!"
        MC "From the way your ass is gripping me, I think that's turning you on even more!"
        MARBELLA "Mfghh!"
        MARBELLA "M-More... Use those fucking things of yours to fuck me up!"
        MC "Heh heh, whatever you wish, slut!"

        $ PlaySexFx(audio.nijah_miss_3, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_3 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_3 with dissolve
        $ Pause()

        "Two tendrils protruded from my back, slithering around to latch onto her breasts and suckle at them."
        MARBELLA "Oooooh f-fuckkk!"
        MARBELLA "Yer tryna milk me or- Mmfghh! Somethin'?!"
        MC "Haha!"
        MC "I doubt any man could resist a chance to suckle on your tits!"
        MARBELLA "Mmfghh!"
        "Marbella bit down on her lower lip."
        MARBELLA "L-Least it distracts a bit from the- Ahh!"
        MARBELLA "Pain of you stretchin' out this ass so much!"

        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_anal_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_anal_3 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_anal_3 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_anal_3 with dissolve
        $ Pause()

        MC "Still hurting?"
        MARBELLA "F-Fucking yes!"
        MARBELLA "B-But don't you dare stop! Mmfghh!"
        MC "Say it then!"
        MC "Say you like me fucking your ass!"
        MARBELLA "AHHHH! Yes!"
        MARBELLA "I LIKE YOU FUCKING MY ASS, DAMN IT!"
        MARBELLA "Mmmfghh! M-More!"
        MARBELLA "You said you'd- Mmfghh! Fuck me up and handle all my needs, right?!"
        MARBELLA "{i}*Huff*{/i} F-Fuck! I'm so pent up and stressed!"
        MARBELLA "Ooooh! This is so good!"
        MARBELLA "M-More! I just need a little more to push me over the edge!"
        MC "I have just the thing!"
        MARBELLA "What do you-"

        $ PlaySexFx(audio.ves69_150, 1)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_4 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_5 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_4 with dissolve
        $ Pause()
    
        "A third tendril appeared, latching onto her face as it pushed its tip into her mouth."
        MARBELLA "Mmmfghh?!"
        "The small dwarf let out a muffled moan as her eyes rolled back."
        MC "There you- Ahh! Go!"
        MC "See? Isn't that better?"
        MC "Instead of running your mouth so much! We just-"
        MC "AHH! Stuff you full of cock!"
        MARBELLA "Ooofghhh!"
        MARBELLA "Yhourghh fhillighh mheee uphh!"
        MARBELLA "Mmfghh!"
        
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_anal_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_anal_4 with dissolve
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_anal_4 with dissolve
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_anal_4 with dissolve
        $ Pause()

        "My words seemed to trigger something in Marbella."
        "Her guttural moans grew louder, more animal-like as she slammed her fat ass back onto me."
        "She took every inch of my cock, and I smirked as it bulged against her stomach."
        MC "Greedy little- Ahh!"
        MC "Dwarven cocksleeve!"
        "Marbella shuddered, her whole body shaking as her tight asshole squeezed around me."
        MARBELLA "MMMMFGHHHHH...!"
        "As she climaxed, I pulled her flush against me and held her there."
        "The tight, hot sensation of her ass pulsing around my cock was more than enough to push me over the edge as well."

        $ PlaySexFx(audio.ves69_finish)
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_alt_anal_finish with flash
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_alt_anal_finish with flash
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_alt_anal_finish with flash
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_alt_anal_finish with flash
        $ Pause()

        "I grunted, holding her folded body against mine as I filled her with my load."
        MC "GRGHHHH!"
        "Marbella let out another muffled moan as she felt the hot seed spill into her."
        MARBELLA "Y-You're filling my ass!"
        "After a few moments, I slowly unsheathed my cock, grinning in satisfaction."
        
        if tmpvar["preg"] == True:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_preg_ling_finish with flash
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_preg_naked_finish with flash
        else:
            if CharGetClothes("marbella") == "ling":
                scene marbella_dom_doggy_nopreg_ling_finish with flash
            elif CharGetClothes("marbella") == "naked":
                scene marbella_dom_doggy_nopreg_naked_finish with flash
        $ Pause()

        "As I pulled free, she let out a small shudder as my cum poured from her stretched ass onto the bed."
        "Releasing her from my tendrils' grip, she dropped face-first onto the bed, well fucked and exhausted."
        "She let out small 'ahhh...' sounds, barely conscious, as more of my cum occasionally seeped from her tight backdoor."

    scene black with dissolve
    "Satisfied and content, I dropped down onto the bed beside her."
    jump gallery_marbella_dom_doggy_end

label gallery_marbella_dom_doggy_end:
    $ CharSetClothes("marbella", tmpvar["stored_marbella_clothes"])
    return