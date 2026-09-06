label rom_marbella_gang_supplies:
    if RomanceMarbella().Gang_SuppliesDaysLeft == 0:
        KHAZAH_LEADER "Ahh, yes! I have one here for you."
        $ tmpvar = RngInt(1, 3)
        if tmpvar == 1:
            $ PlayerAddItem("potion_heal_minor", 4)
            $ PlayerAddItem("potion_heal_vlarge", 1)
            $ PlayerAddItem("potion_heal_large", 3)
            $ PlayerAddItem("gold", 350)
        elif tmpvar == 2:
            $ PlayerAddItem("goblin_stims", 6)
            $ PlayerAddItem("potion_antidote", 5)
            $ PlayerAddItem("gold", 550)
        elif tmpvar == 3:
            $ PlayerAddItem("gold", 900)
        $ tmpvar = {}
        $ RomanceMarbella().Gang_SuppliesDaysLeft = RomanceMarbella().Gang_SuppliesDelay
    else:
        KHAZAH_LEADER "Not yet. Come again in a few days."
    return

#####################################################################################################################################################
# from here – there is a 50% chance of triggering one of the sex scenes 
# (BJ - 
# anal slave - 
# Negotiation toy)
label rom_marbella_gang_rep_scene_main:
    $ RomanceMarbella().Gang_SeenMarbellaSceneTonight = True
    # cycle scenes
    $ RomanceMarbella().Gang_NextRepScene += 1
    if RomanceMarbella().Gang_NextRepScene == 3:
        $ RomanceMarbella().Gang_NextRepScene = 0
    # jump to
    if RomanceMarbella().Gang_NextRepScene == 0:
        jump rom_marbella_gang_rep_bj
    elif RomanceMarbella().Gang_NextRepScene == 1:
        jump rom_marbella_gang_rep_anal
    elif RomanceMarbella().Gang_NextRepScene == 2:
        jump rom_marbella_gang_rep_neg

# BJ repeat
label rom_marbella_gang_rep_bj:
    # marbella_gang_bj_nopreg/preg 1-5 & finish
    show mc at cright_f with easeinright
    "As I entered the Khazah's base, lewd slurping sounds filled my ears as I saw Marbella already eagerly pleasing one of the Khazah."
    "She briefly pulled away to glance at me, lewdly motioning for me to join them."
    menu:
        "*Pull out your cock for Marbella*":
            $ AutoMus(False)
            $ AutoAmb(False)
            stop ambience fadeout 0.5
            $ PlayMusicRandom("mus_sex")
            if CharIsVisiblyPreg("marbella"):
                scene marbella_gang_bj_preg_1 with dissolve
            else:
                scene marbella_gang_bj_nopreg_1 with dissolve
            $ Pause()
            "Marbella's eyes widened as she stared at the cock hanging in front of her."
            MARBELLA "Gods... You're hung like a fuckin' horse."
            KHAZAH "What iz hold up?"
            MARBELLA "In a minute!"
            MARBELLA "A girl's just appreciating the goods, is all."
            KHAZAH "Appreciate while sucking!"
            $ PlaySexFx(audio.ves69_100, 1)
            if CharIsVisiblyPreg("marbella"):
                scene marbella_gang_bj_preg_2 with dissolve
            else:
                scene marbella_gang_bj_nopreg_2 with dissolve
            $ Pause()
            "Eagerly, Marbella leaned forward, wrapping her soft lips around my cock as she stroked the Khazah's cock."
            "I groaned as her tongue worked against the head."
            MC "Ahhh... Mfghh!"
            MARBELLA "{i}*Slurp... Slurp*{/i}"
            "Her mouth inched forward, taking more as she sucked."
            MARBELLA "Mmfghh..."
            MARBELLA "Yhourhh rheallhy bhighh! {i}*Slurp!*{/i}"
            "I smirked at the comment, her mouth still working."
            KHAZAH "Over here, girl."
            KHAZAH "Before I get lonely."
            $ PlaySexFx(audio.ves69_100, 1)
            if CharIsVisiblyPreg("marbella"):
                scene marbella_gang_bj_preg_3 with dissolve
            else:
                scene marbella_gang_bj_nopreg_3 with dissolve
            $ Pause()
            "Marbella pulled away with a soft *plop* before wrapping her lips around the Khazah's cock."
            "He groaned as she moved her head back and forth."
            KHAZAH "Ahhh! That's it, girl!"
            $ PlaySexFx(audio.ves69_150, 1)
            if CharIsVisiblyPreg("marbella"):
                scene marbella_gang_bj_preg_5 with dissolve
            else:
                scene marbella_gang_bj_nopreg_5 with dissolve
            $ Pause()
            "Marbella moved faster, swallowing a few more inches of the Khazah's cock greedily."
            KHAZAH "Ooh! That's it!"
            "Her hand stroked furiously at my cock as her lips glided back and forth servicing the Khazah."
            KHAZAH "You know how to pleasure cock."
            KHAZAH "I'm sure the other Khazah are going to love you, heh..."
            "After a few moments, she pulled away once more,"
            $ PlaySexFx(audio.ves69_150, 1)
            if CharIsVisiblyPreg("marbella"):
                scene marbella_gang_bj_preg_4 with dissolve
            else:
                scene marbella_gang_bj_nopreg_4 with dissolve
            $ Pause()
            "pressing her lips back onto me as her pace quickened."
            "As she stroked the other faster, her eyes lifted pleadingly toward me."
            "There was a shy, desperate need for approval as she continued,"
            "and every soft moan I gave only encouraged her further."
            MARBELLA "(Oh gods, I'm far too comfortable being— ahh! —their plaything!)"
            MARBELLA "(Fuck... Was I really this desperate all along?)"
            MARBELLA "(I just hope Gavkat or the others never find out.)"
            MARBELLA "(... At least as long as I keep this part of my life separate.)"
            MARBELLA "(Mhmm... It could be worse.)"
            MARBELLA "(Mmmfghh... This could...)"
            MC "Ahh! Marbella!"
            MC "I'm getting close!"
            MARBELLA "(G-Get a little addictive!)"
            KHAZAH "Ahh! Me too!"
            KHAZAH "Come on!"
            "Marbella lips remained firmly on my cock."
            MARBELLA "(Come on, come on!)"
            MARBELLA "(GIVE ME THAT THICK LOAD!)"
            $ PlaySexFx(audio.kiara_bj_finish)
            if CharIsVisiblyPreg("marbella"):
                scene marbella_gang_bj_preg_finish with flash
                $ UnlockGalFlag("marbella", "gang_bj", "var_rep_preg")
            else:
                scene marbella_gang_bj_nopreg_finish with flash
                $ UnlockGalFlag("marbella", "gang_bj", "var_rep_nopreg")
            $ UnlockGalSceneAndGrantXp("marbella", "gang_bj")
            $ ReduceInfectionFromSex("marbella")
            $ Pause()
            "I finished first, shortly followed by the Khazah who plastered her tits and face in his seed."
            "Marbella gasped slightly in surprise,"
            "swallowing down as much of the thick load as possible that spilled from the sides of her mouth,"
            "Marbella could only groan in appreciation, stroking out the last drops of the Khazah's cum with her hand."
            "And then, once she was satisfied our balls were drained she dragged her lips forward, cleaning up my cock submissively before pulling her lips away with a loud *PLOP* sound."
            scene black with dissolve
            $ AutoMus(True)
            $ AutoAmb(True)
            $ LocFlush()
            $ CharSetClothes("marbella", "maid")
            show marbella at left
            show cg_bandit at center
            with dissolve
            "Standing back to her feet, Marbella wiped her face clean with her arm."
            "Her mouth curved into a sheepish smile as her cheeks burned red."
            MARBELLA @lewd "I'm, uhhh... better at this than I thought!"
            KHAZAH "You were built for this, little dwarf."
            MARBELLA @angry "Call me little and dwarf in the same sentence again, and next time I'll bite it off."
            KHAZAH "Uhhh... our Queen?"
            MARBELLA @lewd "Much fuckin' better."
            MARBELLA @lewd "Anyway, want me to get you your drinks?"
            KHAZAH_LEADER "If you would be so kind."

            hide marbella
            show cg_marbella_back_maid at left_f 
            with dissolve
            $ PlaySound("audio/cfx/spank.ogg")
            "Marbella hummed happily to herself as she wandered past."
            "Each man she walked past taking a swip at her ass."
            hide cg_marbella_back_maid with easeoutleft
            "It jiggled with each impact, quickly turning pink."
            $ PlaySound("audio/cfx/spank.ogg")
            MARBELLA "{i}*Giggles*{/i}"
            MARBELLA "Boys, please..."
            MARBELLA "No need to be so rough, just grab me when you want a go."
            MARBELLA "{i}This ass belongs to the Khazah...{/i}{image=[ICON.HEART]}"
            "The men whistled as she went by, and Marbella, strangely accustomed, lapped up being their object of desire..."
            hide marbella with easeoutleft
            hide cg_bandit with dissolve
            "I pulled away as Marbella wiped herself clean with a rag and some water before heading off to fetch drinks for the other Khazah."
            show mc at center_f with ease
            MC "(Well, looks like Marbella's adapted to this place pretty well...)"
            $ CharSetClothes("marbella", "normal")
        "Perhaps another time.":
            "Marbella shrugged and went back to happily sucking the cock in front of her."
            $ CharSetClothes("marbella", "normal")
    $ LocEnter()

#######################################################################################################################################################
label rom_marbella_gang_rep_anal:
    #anal slave.
    show mc at cright_f with easeinright
    "As I swung open the door, I was greeted by the sight of Marbella — naked, blindfolded, and gagged."
    "She was bent over a device with her pussy sealed away, the words ANAL ONLY boldly scrawled across her cheeks."
    "She lifted her head slightly as she heard me step inside."
    show cg_bandit at cleft with easeinleft
    KHAZAH_LEADER "Ah, just in time, friend!"
    KHAZAH_LEADER "Want to use her ass?"
    KHAZAH_LEADER "The others will be stretching her hole shortly."
    menu:
        "*Use her ass*":
            label replay_marbella_gang_analonly:
            $ AutoMus(False)
            $ AutoAmb(False)
            stop ambience fadeout 0.5
            $ PlayMusicRandom("mus_sex")
            scene marbella_gang_analonly_1 with dissolve
            $ Pause()
            "As I stepped up to Marbella, she squirmed slightly, kicking her feet as she felt the head of my cock press against her tight backdoor."
            $ PlaySexFx(audio.forgean_075, 1)
            scene marbella_gang_analonly_2 with dissolve
            $ Pause()
            MARBELLA "MMFGHH!"
            "Her ass was already generously lubed and lightly stretched from toys."
            "As I pushed against her, she let out a small whimper when I met resistance,"
            "but with more pressure, her ass gave way and stretched around the head of my cock."
            "She squealed into the gag as I buried myself deeper inside her tight, squeezing ass."
            MARBELLA "Mhyhhh ASHHH! MMFHGH!"
            $ PlaySexFx(audio.forgean_100, 1)
            scene marbella_gang_analonly_3 with dissolve
            $ Pause()
            "I grunted in response to her muffled pleas, beginning to move faster as I fucked her."
            MARBELLA "Mfghh! {i}*Grunt*{/i} Ahhh! {i}*Grunt*{/i}"
            "Her soft ass pushed back against me as the sound of flesh colliding filled the room."
            "Her moans grew louder as I gripped her tighter,"
            "hot sweat dripping from her as I used her body."
            "The men around us roared and cheered as I fucked the dwarven slut's tight ass without mercy,"
            "her cries a mixture of pleasure and pain."
            MARBELLA "M-MMFMGHHHHH...!"
            "Between heavy breaths, her sudden cry caught me by surprise as her whole body tightened and shook."
            "The intense sensation of her ring convulsing around my cock like a vice pushed me over the edge."
            $ PlaySexFx(audio.forgean_finish)
            scene marbella_gang_analonly_finish with flash
            $ Pause()
            "Slamming myself to the hilt, I gritted my teeth as I finished inside her."
            MC "G-GRGHHHH!!"
            "She shuddered again, feeling the load fill her."
            scene marbella_gang_analonly_finish2 with flash
            $ UnlockGalSceneAndGrantXp("marbella", "gang_analonly")
            $ ReduceInfectionFromSex("marbella")
            $ Pause()
            "Satisfied, I slowly pulled free."
            "With a *PLOP* sound, I slipped out as she twitched, feeling the seed seep from her ass."
            scene marbella_gang_analonly_4 with dissolve
            $ Pause()
            "No sooner had I finished than one of the Khazah approached from behind, pressing himself against her."
            "Her hands clenched into fists as her toes curled."
            $ PlaySexFx(audio.forgean_100, 1)
            scene marbella_gang_analonly_5 with dissolve
            $ Pause()
            "She grunted as the man took his turn, the rest of the Khazah waiting behind him."
            $ StopReplay()
            $ LocFlush(dissolve)
            $ StopSexFx(FadeOut = 0.5)
            $ CharSetClothes("marbella", "maid")
            show cg_bandit at center
            show marbella at left
            MARBELLA @emb "Ow ow ow...!"
            MARBELLA @emb "My poor ass!"
            KHAZAH_LEADER "Good girl... Now go fetch everyone their drinks."
            hide marbella
            show cg_marbella_back_maid at left_f 
            with dissolve
            MARBELLA "Gods, you all fuck me in the ass and don't even let me sit down after!"
            hide cg_marbella_back_maid with easeoutleft
            $ PlaySound("audio/cfx/spank.ogg")
            MARBELLA "N-Not today you fucks! You've abused my ass enough as it is!"
            "The men chuckled in amusement as she wobbled about with an awkward gait to fetch their drinks."
            with dissolve
            $ AutoMus(True)
            $ AutoAmb(True)
            $ CharSetClothes("marbella", "normal")
            KHAZAH_LEADER "So, did you come here just for a fuck, or do you have some business?"
        "I'll pass.":
            KHAZAH_LEADER "Hm... As you desire."
            KHAZAH_LEADER "What business brings you here then?"
    call processDialogue("hamun_khazah_leader_root") from _call_processDialogue_77
    $ LocEnter()

###########################################################################################################################################################
label rom_marbella_gang_rep_neg:
    show mc at cright_f with easeinright
    "Opening the door, I was greeted by the curious sight of Marbella strapped to a table, hog-tied and blindfolded, with a device prying her mouth open."
    show cg_bandit at cleft with easeinleft
    KHAZAH_LEADER "Ahh, good to see you, friend."
    KHAZAH_LEADER "Marbella here has made herself available to assist some friends of the Khazah with negotiations."
    KHAZAH_LEADER "Feel free to use her, should you wish."
    menu:
        "*Use her*":
            label replay_marbella_gang_tied:
            $ AutoMus(False)
            $ AutoAmb(False)
            stop ambience fadeout 0.5
            $ PlayMusicRandom("mus_sex")
            $ PlaySexFx(audio.moans_breaths_loop, 1)
            scene marbella_gang_tied_1 with dissolve
            $ Pause()
            "Stepping behind her, I slapped my cock onto her soft ass as she jumped at the sudden feeling."
            "Sliding back and forth between her crack, Marbella's breathing became heavier as another Khazah began to rub his cock agaisnt her face."
            "Drool rolled from her pried open mouth as she desperately tried to speak."
            MARBELLA "Whoshhtherehh behindhhh mheee?"
            MC "Shh, be a a good girl now, Marbella."
            "I gave her ass a playful slap, watching the fat jiggle as she groaned."
            MC "You have cocks to serve."
            MARBELLA "Mmfghghh...!"
            "Her tongue slithered out of her mouth to lick teasingly at the cock in front of her."
            "More and more, as we continued to tease her, her pussy glistened with excitement and anticipation of what was to come."
            $ PlaySexFx(audio.ves69_125, 1)
            scene marbella_gang_tied_2 with dissolve
            $ Pause()
            "I aligned myself against her wet slit as another Khazah pressed himself to her mouth."
            "She groaned in surprise as she felt me enter her, but the shock soon turned to soft whimpers and moans."
            "As the Khazah pushed into her mouth, her tongue worked around him as he grunted approvingly."
            MARBELLA "{i}*Slurp!*{/i} Mmfghhh!! {i}*Slurp!*{/i}"
            "Her tight cunt swallowed me eagerly,"
            "squeezing around me as I fucked her from behind."
            "With every thrust, she grunted in approval, her ass jiggling with each impact."
            $ PlaySexFx(audio.kiara_bj_loop, 1)
            $ PlaySexFx2(audio.no_voice, 1)
            scene marbella_gang_tied_3 with dissolve
            $ Pause()
            "The Khazah pushed deeper into her mouth as I continued to thrust into her."
            "The table shook as the sound of flesh slapping filled the room, mixing with drinking and chatter."
            "{i}*Plap!* *Plap!* *Plap!*{/i}"
            "Marbella wasn't a person to me in that moment."
            "She was nothing more than a toy to relieve myself with,"
            "and she seemed to sense that too, her moans growing louder as she choked."
            "She knew what she was to these men, and as her pussy tightened around me, I had my answer."
            "{i}She liked it.{/i}"
            MARBELLA "MMMMFGHHH...!"
            "She squealed around the cock in her mouth,"
            "her body trembling as her pussy convulsed."
            "The Khazah grunted, throwing his head back as he pushed deeper."
            "The sudden tightness caught me off guard as well."
            "Slamming into her, I grunted, squeezing her ass as I finished inside her."
            $ PlaySexFx(audio.kiara_bj_finish)
            $ StopSexFx2()
            scene marbella_gang_tied_finish with flash
            $ UnlockGalSceneAndGrantXp("marbella", "gang_tied")
            $ PregRoll("marbella")
            $ ReduceInfectionFromSex("marbella")
            $ Pause()
            MC "HRGHHHH...!!"
            "She shuddered, her toes curling as she felt me empty inside her."
            "The Khazah too, unloaded into her throat with a groan, muttering something about 'swallowing it all' to Marbella."
            "When I pulled out, I watched the seed spill from her used pussy and smirked."
            "Giving her ass a sharp slap, it jiggled and left a red handprint as I stepped aside."
            "Another Khazah took my place, wasting no time before thrusting into her."
            "Marbella responded only with soft moans, letting the men use her as they pleased."
            $ StopReplay()
            $ LocFlush(dissolve)
            $ AutoMus(True)
            $ AutoAmb(True)
            $ CharSetClothes("marbella", "maid")
            show cg_bandit at center
            show marbella at left
            MARBELLA @emb "You boys really went to town on me tonight..."
            KHAZAH_LEADER "It was your idea to let us tie you up like that."
            MARBELLA @lewd "It helped you secure the deal, didn't it?"
            MARBELLA @smile "Anyway, I'm off to do my rounds now my pussy's sore."
            hide marbella
            show cg_marbella_back_maid at left_f 
            with dissolve
            $ PlaySound("audio/cfx/spank.ogg")
            MARBELLA "{i}Eeeep!{/i}"
            MARBELLA "Careful with the butt!"
            hide cg_marbella_back_maid with easeoutleft
            $ PlaySound("audio/cfx/spank.ogg")
            MARBELLA "Boysssss..."
            MARBELLA "{i}I might be small, but there's enough of me to go around!{/i}"
            MARBELLA "Fufu~ {image=[ICON.HEART]}"
            "Marbella continued to tease the Khazah who groped her freely as she fetched them their drinks."
            KHAZAH_LEADER "So, did you come here just for a fuck, or do you have some business?"       
            $ CharSetClothes("marbella", "normal") 
        "Not now.":
            KHAZAH_LEADER "Hmm?"
            KHAZAH_LEADER "Then have you come here for some other reason, perhaps?"
    call processDialogue("hamun_khazah_leader_root") from _call_processDialogue_78 
    $ LocEnter()
