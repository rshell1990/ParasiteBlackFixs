label gallery_marbella_dom_tj:
    scene black with dissolve
    if GalFlagCount("marbella", "dom_titjob") == 0:
        $ StartReplay("replay_marbella_dom_titjob_first")
        scene black with dissolve
        return
    else:
        "Was it our first time?"
        menu:
            "Yes":
                $ StartReplay("replay_marbella_dom_titjob_first")
                scene black with dissolve
                return
            "No":
                pass

    "Was she pregnant at the time?"
    menu:
        "Yes":
            $ tmpvar["preg"] = True
        "No":
            $ tmpvar["preg"] = False

    MARBELLA @smile "I'm getting far, {i}far{/i} too comfortable letting you just tie me up with those things of yours."
    MC @think "Is that a no?"
    MARBELLA @lewd "Fuck no!"
    $ AutoMus(False)
    $ AutoAmb(False)
    stop ambience fadeout 0.5
    $ PlayMusicRandom("mus_sex")
    scene black with dissolve
    MARBELLA @lewd "Do your worst, big boy!"
    play sound2 "audio/cfx/transform.ogg"
    "From my back, two tentacles sprang, grabbing hold of Marbella as they tore and pulled off her clothes."
    $ PlaySexFx(audio.adara_hj_loop, 1)
    if tmpvar["preg"] == True:
        scene marbella_dom_titjob_preg_1 with dissolve
    else:
        scene marbella_dom_titjob_nopreg_1 with dissolve
    $ Pause()
    MARBELLA "Eeeeeeep!"            
    "Marbella giggled in delight, all her previous nerves a thing of the past."
    "Suspended in the air, my tentacles wrapping and restraining her, she wiggled as she looked back at me, eyes wide."
    if tmpvar["preg"] == True:
        scene marbella_dom_titjob_preg_2 with dissolve
    else:
        scene marbella_dom_titjob_nopreg_2 with dissolve
    $ Pause()
    "With a sharp swipe of my hand, I watched her ass jiggle with the impact as she yelped in shock."
    MARBELLA "Ahh!"
    MARBELLA "At least warm my arse up first before you swipe so-"
    "My hand struck again, colliding against the other cheek as she let out another startled gasp."
    MC "It's {i}my{/i} ass now."
    MARBELLA "Ahh!"
    MARBELLA "Do you get off or somethin' on me walking around with my butt red?"
    "A third tentacle appeared, slapping across Marbella's tits as she let out a sharp moan."
    MC "It sounds to me like someone's enjoying this more than they let on."
    MARBELLA "W-Well, you're just- Mmm..."
    MARBELLA "{i}M-Markin' yer territory, I s'pose...{/i}"
    MARBELLA "Can't be too mad about-"
    "As I spanked her ass once again, she gasped."
    "Before she could argue further, my tentacles whipped across her tits in a frenzy, leaving light pink marks in their wake."
    MARBELLA "F-Fuckkk...!"
    MC "That's right."
    MC "I'm marking you."
    MC "{i}I'm letting everyone know your ass belongs to me.{/i}"
    MARBELLA "{i}*Huff*{/i} You better- {i}*Huff*{/i} Mark me more- {i}*Huff*{/i} Because I'm-"
    MARBELLA "{i}*Huff*{/i} Not convinced!"
    "I slapped her ass once more, watching with delight as her fat cheeks turned a deeper shade of red."
    MC "I."
    "*{b}Smack!{/b}*"
    MC "OWN."
    "*{b}Smack!{/b}*"
    MC "THIS."
    "*{b}Smack!{/b}*"
    MC "FAT."
    "*{b}Smack!{/b}*"
    MC "ASS!"
    "*{b}Smack!{/b}*"
    "Marbella stopped arguing, her cunt glistening between her legs as she let out low, trembling breaths."
    MARBELLA "{i}*H-Huff!* *Huff!*{/i}"
    MC "Still going to argue who this fat butt belongs to?"
    "Marbella's breathing was heavy, her pussy wet with excitement, yet she remained silent."
    MARBELLA "..."
    MC "Still being disobedient, hm?"
    MC "No matter... I have just the solution!"
    scene marbella_dom_titjob_idle with dissolve
    $ Pause()
    "Marbella gasped as I pinned her onto the table, shoving my cock between her tits."
    MARBELLA "{i}*Giggles*{/i}"
    scene marbella_dom_titjob_3 with dissolve
    $ Pause()
    "With both hands, I pushed her tits together and began sliding my cock between her soft, heavy mounds."
    MC "Spit on it."
    MARBELLA "Spit on it yourself."
    "A soft moan escaped Marbella's lips as she squirmed beneath me."
    MARBELLA "M-Mmmhhhfff!"
    MC "Spit. On. It."
    MARBELLA "A-Ahh! {i}M-Make me!{/i}"
    "Her soft moans and grunts continued as I fucked her tits."
    "Every so often, her gaze would meet the head of my cock before she'd spit on it."
    MARBELLA "{i}*Spits!*{/i}"
    MARBELLA "T-There!"
    MARBELLA "I did as you asked!"
    scene marbella_dom_titjob_4 with dissolve
    $ Pause()
    "I squeezed her tits, the warm spit acting as a slick lubricant."
    MC "Good girl... And like we practiced, what are you?"
    MARBELLA "Mmfghhh!"
    "As her tits bounced with my cock thrusting between them, another hot moan escaped her lips."
    MARBELLA "{i}Y-Your little dwarven slut, sir...{/i}"
    "She bit her lower lip, her gaze heavy with anticipation of what would come next."
    "Her cheeks burned as her breathing grew heavier."
    "My balls tightened as the urge to paint her tits and face with my cum grew with each thrust."
    MC "{i}*Huff*{/i} You ready- {i}*Huff*{/i}"
    MC "To get marked, my little slut?"
    "Marbella nodded shakily."
    MARBELLA "D-Do your worst, you fu-"
    $ PlaySexFx(audio.adara_hj_finish)
    scene marbella_dom_titjob_finish with flash
    $ Pause()
    "I pressed her tits together tightly, ramming forward as I grunted, painting her face and tits in thick white seed."
    MC "HRGHHHHHH!"
    MARBELLA "{i}*Gasp!*{/i}"
    "As the last of my hot seed splashed across her face and chest, Marbella stared in stunned disbelief."
    MARBELLA "{i}Like a bloody horse every time...{/i}"
    MC "{i}*Huff*{/i} Your tits are amazing."
    scene black with dissolve
    return