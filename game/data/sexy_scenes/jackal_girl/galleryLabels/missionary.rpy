label gallery_jackal_girl_missionary:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    ## warning, there's some string processing involved! be careful entering

    # if there is both anal and vag flags of ANY kind, show menu
    # else, set to which kind is the only one
    if len(GalFlagsWithSubstring("jackal_girl", "missionary", "_vag")) > 0 and len(GalFlagsWithSubstring("jackal_girl", "missionary", "_anal")) > 0:
        "Which was it?"
        menu:
            "Vaginal":
                $ tmpvar["kind"] = "vag"
            "Anal":
                $ tmpvar["kind"] = "anal"

    elif len(GalFlagsWithSubstring("jackal_girl", "missionary", "_vag")) > 0:
        $ tmpvar["kind"] = "vag"

    elif len(GalFlagsWithSubstring("jackal_girl", "missionary", "_anal")) > 0:
        $ tmpvar["kind"] = "anal"
    else:
        $ raise Exception("What the fuck!")

    ### preg status
    if len(GalFlagsWithSubstring("jackal_girl", "missionary", "_preg" + "_" + tmpvar["kind"])) > 0 and len(GalFlagsWithSubstring("jackal_girl", "missionary", "_nopreg" + "_" + tmpvar["kind"])) > 0:
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["preg"] = True
            "No":
                $ tmpvar["preg"] = False
    elif len(GalFlagsWithSubstring("jackal_girl", "missionary", "_preg" + "_" + tmpvar["kind"])) > 0:
        $ tmpvar["preg"] = True
    elif len(GalFlagsWithSubstring("jackal_girl", "missionary", "_nopreg" + "_" + tmpvar["kind"])) > 0:
        $ tmpvar["preg"] = False
    else:
        $ raise Exception("What the fuck!")


    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_idle with dissolve
    else:
        scene jackal_girl_missionary_nopreg_idle with dissolve
    $ Pause()

    if tmpvar["kind"] == "anal":
        jump gallery_jackal_girl_missionary_ass
    elif tmpvar["kind"] == "vag":
        jump gallery_jackal_girl_missionary_puss
    return

label gallery_jackal_girl_missionary_puss:
    "On the floor, I rubbed my member against the creature's wet opening."
    "She let out soft, happy pants as her juices coated my cock."
    "Holding one of her legs in my arms, her soft tail swishes and brushes against me as her tight slit glistened in the light."
    MC "Are you ready for this?"
    JACKAL_GIRL "{i}*Pant* *Pant!*{/i}"
    "She said nothing, but her sultry eyes refused to look away as she looked up expectantly for her {i}mate{/i} to take charge."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_slow with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_slow with dissolve
    $ Pause()
    "I carefully aligned my cock against her tight slit, pushing it slowly into her."
    "Her insides felt different than a humans... Ribbed with tiny bumps, less pronounced than mine, but incredible all the same."
    "She let out a sudden, soft rumble that sounded an awful lot like a moan."
    "She squeezed tightly around me, her tail swishing happily as I slid deeper into her."
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_fast with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_fast with dissolve
    $ Pause()
    "Somehow, even without words, like two rutting beasts, I understood her perfectly."
    "She panted hotly, and as I thrust faster into her eager hole, she howled with delight."
    "She trembled beneath my hands as I stroke her soft, sweaty fur."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_tentacle_head_slow with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_tentacle_head_slow with dissolve
    $ Pause()
    "Her eyes widen as the first of my tentacles slithered toward her."
    "She tilted her head, watching as it pushed into her throat."
    "She let out a startled yelp, but once the aphrodisiac kicked in, she rumbles with pleasure."
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_tentacle_head_fast with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_tentacle_head_fast with dissolve
    $ Pause()
    "I smiled, slamming my cock deep into her as if in a trance, her paws curling in pleasure."
    JACKAL_GIRL "{i}*Slurp!* *Pant!* *Slurp!* *Pant!*{/i} ❤️"
    JACKAL_GIRL "{i}Arrfff!{/i}"
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_tentacle_faceful_slow with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_tentacle_faceful_slow with dissolve
    $ Pause()
    "The tentacle cupped her face as it latched on. She didn't resist — just moaned."
    "Her cunt tightened and squeezed me as she drew closer to her own climax."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_tentacle_faceful_fast with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_tentacle_faceful_fast with dissolve
    $ Pause()
    "By now, I was slamming into her greedy hole, her squeals muffled by the tentacle down her throat."
    "Her tail swished erratically, and I could feel her heart racing."
    "She was close. But I was not done yet..."
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_tentacle_booba_face with dissolve
    else:
        scene jackal_girl_missionary_nopreg_vag_tentacle_booba_face with dissolve
    $ Pause()
    "Two more tentacles slithered around her, latching onto her breasts and suckling eagerly."
    "Her entire body trembled as I continued thrusting into her drenched pussy."
    "Even as she squirmed beneath me, I held her tight, rutting her without pause."
    "In this moment, she was mine. Mine to {i}devour{/i} completely."
    "She let out a howl-like moan, shaking as a powerful orgasm overtook her."
    "So caught up in the moment, I didn't realize how close I was."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_vag_finish with flash
    else:
        scene jackal_girl_missionary_nopreg_vag_finish with flash
    $ Pause()
    "With a final series of thrusts, I buried myself deep and flooded her womb with my seed."
    "She clenched tight around me, but by now she was exhausted."
    "As I pulled out, she let out a soft whimper, and my cock freed itself with a slick sound."
    "Her tail still wagged gently as she panted in the afterglow."
    scene black with dissolve
    "I knew she wouldn't be moving for a while... but I also knew I had to return to the path at once."
    "As I left, I swear I caught a glimpse of her silhouette trailing me for a few more miles before she finally vanished altogether..."
    return

label gallery_jackal_girl_missionary_ass:
    "On the ground, I pressed the head of my cock against her tight rosebud."
    "She twisted her head to look towards me, panting and confused."
    "Holding her leg up, her tail swished as her asshole twitched under my touch."
    MC "Are you ready for this?"
    JACKAL_GIRL "{i}A-Aroo?{/i}"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_slow with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_slow with dissolve
    $ Pause()
    "She didn't speak, but watched intently as I pressed into her tight ring."
    "Her mouth opened with a sharp howl as I pushed the head inside."
    "Her ass squeezed around me, resisting at first, but as I slid in deeper with practiced ease,"
    "Her eyes at first showed confusion — but she didn't resist, and soon, her body started to relax."
    "Still though, I felt like I could almost read her thoughts as she looked up to me, cock rammed firmly in her ass."
    "{i}'You put it THERE instead of where it belongs... now what?'{/i}"
    "Her asshole pulsed around my shaft as she looked back at me."
    "I moved slowly, letting her adjust. As I went deeper, she began to pant once more."
    "Soft rumbles escaped her lips. She was starting to enjoy it."
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_fast with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_fast with dissolve
    $ Pause()
    "Her ass gripped me like a vice, her tail brushing up along my side."
    "Again, like rutting beasts, we didn't need words to understand each other."
    "I thrust harder, and her moans only grew louder."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_tentacle_head_slow with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_tentacle_head_slow with dissolve
    $ Pause()
    "Her eyes widened as the first tentacle crept forward and pushed into her throat."
    "She gagged, then moaned, the aphrodisiac having done it's work."
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_tentacle_head_fast with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_tentacle_head_fast with dissolve
    $ Pause()
    "Her paws curled, overcome with pleasure."
    JACKAL_GIRL "{i}*Slurp!* *Pant!* *Slurp!* *Pant!*{/i} ❤️"
    JACKAL_GIRL "{i}Arrfff!{/i}"
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_tentacle_faceful_slow with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_tentacle_faceful_slow with dissolve
    $ Pause()
    "The tentacle cupped her face, pulsing steadily."
    "She didn't resist, her ass tightening involuntarily."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_tentacle_faceful_fast with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_tentacle_faceful_fast with dissolve
    $ Pause()
    "I pounded into her greedy ass, her muffled squeals pushing me further toward the edge."
    "Her tail thrashed wildly, her body trembling from the stimulation."
    "But I was not finished."
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_tentacle_booba_face with dissolve
    else:
        scene jackal_girl_missionary_nopreg_anal_tentacle_booba_face with dissolve
    $ Pause()
    "Two more tentacles latched onto her breasts, suckling greedily."
    "She spasmed beneath me, unable to handle the overload of pleasure."
    "Even as she writhed, I held her firm, thrusting into her tight, stretched rear."
    "She was mine. Mine to {i}devour{/i} completely."
    "She howled into the tentacle as a powerful orgasm wracked her body."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_anal_finish with flash
    else:
        scene jackal_girl_missionary_nopreg_anal_finish with flash
    $ Pause()
    "I was too far gone. With a final thrust, I slammed deep and empty myself into her bowels."
    "She clenched tightly as I pulled out, her body now limp, but her tail still wagged weakly."
    "My seed seeped from her ass as she panted softly."
    scene black with dissolve
    "I knew she wouldn't be moving for a while... but I also knew I had to return to the path at once."
    "As I left, I swear I caught a glimpse of her silhouette trailing me for a few more miles before she finally vanished altogether..."
    return