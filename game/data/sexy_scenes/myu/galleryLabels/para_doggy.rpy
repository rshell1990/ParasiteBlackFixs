label gallery_myu_para_doggy:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    if GalFlag("myu", "para_doggy", ["var_vag","var_anal"]):
        "Was it vaginal or anal?"
        menu:
            "Vaginal":
                jump gallery_myu_para_doggy_vag
            "Anal":
                jump gallery_myu_para_doggy_anal
    elif GalFlag("myu", "para_doggy", "var_vag"):
        jump gallery_myu_para_doggy_vag
    elif GalFlag("myu", "para_doggy", "var_anal"):
        jump gallery_myu_para_doggy_anal

label gallery_myu_para_doggy_vag:
    if GalFlag("myu", "para_doggy", ["var_vag_preg", "var_vag_nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["myu_preg_alt"] = True
            "No":
                $ tmpvar["myu_preg_alt"] = False
    elif GalFlag("myu", "para_doggy", "var_vag_preg"):
        $ tmpvar["myu_preg_alt"] = True
    elif GalFlag("myu", "para_doggy", "var_vag_nopreg"):
        $ tmpvar["myu_preg_alt"] = False

    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg",1)
    scene myu_para_doggy_vag with dissolve
    $ Pause()
    "I pressed my ribbed cock into Myu's pussy and she gasped as I filled her up."
    "I watched my cock glide in and out of her translucent body as Myu's mouth hung open as she moaned, feeling it slide in and out of her."
    MYU "H-Husband..."
    MYU "Myu feels so full {image=[ICON.HEART]}~"
    "My talon hands dug into the cool flesh of her soft ass, but Myu didn't mind as my claw pressed inside of her."
    "Instead, with her jelly like substance, she simply gripped onto me tighter as she gently rocked her butt back into me as I took her."
    "The dark impulses of my 'dark passenger' coursed through me as I rammed into Myu's welcoming cunt."
    "Myu tightly squeezed me as I pulled her ass deeper into me."
    MYU "Ah! Ah! H-Husband!"
    MYU "OOoooh!"
    MYU "{i}*Huff*{/i} S-So firm with Myu!"
    'I grunted and growled once again, continuing to fuck Myu with hot-blooded, reckless abandon.'
    "The '{i}dark passenger{/i}' wanted to remind her she was {i}our{/i} mate, OUR breeding sow."
    "As Myu moaned sweetly, I roared as I fucked her furiously. She was mine... Mine..."
    if tmpvar["myu_preg_alt"] == True:
        scene myu_para_doggy_alt_preg_notent with dissolve
    if tmpvar["myu_preg_alt"] == False:
        scene myu_para_doggy_alt_nopreg_notent with dissolve
    $ Pause()
    BLACK "Mine."
    MYU "Ah! D-Darling!"
    MYU "Mmmfghh!!"

    if GalFlag("myu", "para_doggy", ["var_vag_finish","var_vag_tent"]):
        "Did I use my tentacles?"
        menu:
            "Yes":
                jump gallery_myu_para_doggy_vag_tent
            "No":
                pass
    elif GalFlag("myu", "para_doggy", "var_vag_tent"):
        jump gallery_myu_para_doggy_vag_tent
    elif GalFlag("myu", "para_doggy", "var_vag_finish"):
        pass

    'Deciding not to push Myu any further, I gripped her ass tightly as I fucked her from behind.'
    "Myu's whole body trembled and shook as she cried out in a high-pitched moan,"
    MYU "C-CUMMING!"
    "Grunting and snarling, I flooded Myu's cunt with my hot, beastly seed as she quivered, feeling me flooding her womb."
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene myu_para_doggy_vag_notent_finish with flash
    $ Pause()
    "Myu let out a long happy sigh as she giggled to herself."
    MYU "Fufu~ Myu happy, Myu full. {image=[ICON.HEART]}"
    return

label gallery_myu_para_doggy_vag_tent:
    scene myu_para_doggy_vag_tent_1 with dissolve
    $ Pause()
    'As my tentacles protruded from my back, with a mind of their own, they wrapped around Myu.'
    "Two of my tentacles latched onto Myu's breasts and began to suckle at her tits as the others toyed with her body."
    MYU "Mmmfghh! W-What are you doing to Myu?!"
    "I didn't answer her, watching as the two tentacles pumped Myu's breasts while the others slithered around her body, toying with her."
    MYU "Oooooh...! {image=[ICON.HEART]}"
    MYU "M-Myu's breasts f-feel s-so sensitive!"
    "A protruding tongue from one of the many tentacles gently pressed its way into Myu's mouth."
    MYU "M-Mmfghh!"
    if tmpvar["myu_preg_alt"] == True:
        scene myu_para_doggy_alt_preg_tent with dissolve
    if tmpvar["myu_preg_alt"] == False:
        scene myu_para_doggy_alt_nopreg_tent with dissolve
    $ Pause()
    "Myu's body was nothing more than something for me to play with now, overcome with pleasure, she simply continued to writhe hotly as she moaned uncontrollably."
    MYU "{i}H-Husband! Myu loves you! Myu loves you so much!!{/i} {image=[ICON.HEART]}"
    MYU 'Myu feels incredible!'
    MYU "Give M-Myu stuff! Myu w-want baby!"
    "I grunted in approval, as one tentacle slide around towards Myu's mouth."
    MYU "Huh? What this one-"
    "The tentacle slammed against Myu's face, forcing the soft tube like tongue down her throat."
    MYU "Mmmfghh?!"
    "Myu's eyes widened in shock as I poured the warm chemicals down into her body."
    "Through opening pores, I could allow Myu to breathe as I pumped her full of the sweet nectar that triggered and overloaded her mind and body with pleasure."
    scene myu_para_doggy_vag_tent_2 with dissolve
    $ Pause()
    MYU "Mmfghhh...! {image=[ICON.HEART]}"
    MYU "(W-What is this?!)"
    MYU "(What are you feeding Myu!!)"
    MYU "(Myu... f-feels...)"
    MYU "({i}Amazing!{/i})"
    MYU "(More! {i}Give Myu more!{/i})"
    MYU "Mmmfhghh...!"
    "Myu's body was in sync with me now. I could feel every intense over-sensation emitting from her as I fucked her."
    "Instinctively, I knew how potent and powerful the chemical I was releasing into her was."
    "In short bursts, a mate would simply become addicted."
    "Long term? {i}Their minds could be completely broken.{/i}"
    "As Myu's eyes rolled back, she continued her guttural moans as I continued to feed her my love."
    scene myu_para_doggy_vag_tent_3 with dissolve
    $ Pause()
    MYU "MMmfghh! Shhwww ghwwddd!"
    MYU "Lhuv yhuu! Lhuv yhuu! Lhuv yhuu!!! {image=[ICON.HEART]} {image=[ICON.HEART]}"    
    'Myu trembled and shook as orgasm after orgasm wrecked through her body.'
    "If I wasn't careful, I'd soon be leaving her completely broken, as she did her best to throw her ass back onto me with every thrust into her."
    "I grunted and snarled in approval. Every dark impulse inside of the dark passenger burned with glee."
    MYU "(Cumming! Can't stop cumming!)"
    MYU "Mmmfghh! Thinking no good! More, more, {i}more!{/i}"  
    "Feeling the end finally drawing near as the hot pleasure became too much for even me, I could no longer hold back."
    "Myu's whole body trembled and shook as she cried out in a high-pitched moan,"
    MYU "C-CUMMING!"
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene myu_para_doggy_vag_tent_finish with flash
    $ Pause()
    "Grunting and snarling, I flooded Myu's cunt with my hot, beastly seed as she quivered, feeling me flooding her womb."
    "Watching my seed flood into her semi-translucent body, she shook with pleasure before feeling heavy and limp under my claws."
    MYU "{i}*Huff* *Huff*{/i}"
    "Myu let out a long happy sigh as she giggled to herself."
    MYU "Fufu~ Myu happy, Myu full. {image=[ICON.HEART]}"
    return

label gallery_myu_para_doggy_anal:
    if GalFlag("myu", "para_doggy", ["var_anal_preg", "var_anal_nopreg"]):
        "Was she pregnant at the time?"
        menu:
            "Yes":
                $ tmpvar["myu_preg_alt"] = True
            "No":
                $ tmpvar["myu_preg_alt"] = False
    elif GalFlag("myu", "para_doggy", "var_anal_preg"):
        $ tmpvar["myu_preg_alt"] = True
    elif GalFlag("myu", "para_doggy", "var_anal_nopreg"):
        $ tmpvar["myu_preg_alt"] = False

    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg",1)
    scene myu_para_doggy_anal with dissolve
    $ Pause()
    "I moved my dick up and pressed it against the tight rosebud backdoor of Myu's asshole."
    "As I pressed and slide it into the tight hole, Myu let out a little squeal as she felt me fill her up back there."
    "Of course, she had simply crafted all this for my pleasure. Her whole body was a mimic of what a woman {i}should{/i} feel like after all."
    "But it didn't matter. Her tight welcoming hole squeezed me all the same, and as the dripping fluids of her slime seeped their way in through the skin, it acted as an aphrodisiac, driving me wild with unbound lust."
    MYU "G-Gahhhhhfhhh...!"
    MYU "M-Myu butt... D-Does it feel g-good?"
    "I growled and snarled in approval as I continued to fuck Myu's tight ass."
    "I watched with glee as the ring of her asshole formed and stretched around my cock, and I could see my cock working its way in and out of her semi-translucent body."
    MYU "Mmfgghh...!"
    MYU "{i}So full!{/i}"
    MYU "F-Fuck Myu butt harder! FUCK MYU HARDER! {image=[ICON.HEART]}~ "
    'I grunted and growled once again, continuing to fuck Myu with hot-blooded reckless abandon.'
    "The '{i}dark passenger{/i}' wanted to remind her she was {i}our{/i} mate, OUR breeding sow."
    "As Myu moaned sweetly, I roared as I fucked her furiously, she was mine... Mine..."
    if tmpvar["myu_preg_alt"] == True:
        scene myu_para_doggy_alt_preg_notent with dissolve
    if tmpvar["myu_preg_alt"] == False:
        scene myu_para_doggy_alt_nopreg_notent with dissolve
    $ Pause()
    BLACK "Mine."
    MYU "Ah! D-Darling!"
    MYU "M-Myu ass! So full! {image=[ICON.HEART]}"
    MYU "Mmmfghh!!"

    if GalFlag("myu", "para_doggy", ["var_anal_finish","var_anal_tent"]):
        "Did I use my tentacles?"
        menu:
            "Yes":
                jump gallery_myu_para_doggy_anal_tent
            "No":
                pass
    elif GalFlag("myu", "para_doggy", "var_anal_tent"):
        jump gallery_myu_para_doggy_anal_tent
    elif GalFlag("myu", "para_doggy", "var_anal_finish"):
        pass

    'Deciding not to push Myu any further, I gripped her ass tightly as I fucked her from behind.'
    "Myu's whole body trembled and shook as she cried out in a high-pitched moan,"
    MYU "C-CUMMING!"
    "Grunting and snarling, I flooded Myu's tight back door with my hot, beastly seed as she quivered, feeling me flood her ass."
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene myu_para_doggy_anal_notent_finish with flash
    $ Pause()
    "Myu let out a long happy sigh as she giggled to herself."
    MYU "Fufu~ Myu happy, Myu full. {image=[ICON.HEART]}"
    return

label gallery_myu_para_doggy_anal_tent:
    'As my tentacles protruded from my back, with a mind of their own they wrapped around Myu.'
    "Two of my tentacles latched onto Myu's breasts and suckled at her tits as the others toyed with her body."
    MYU "Mmmfghh! W-What are you doing to Myu?!"
    "I didn't answer her, watching as the two tentacles pumped Myu's breasts while the others slithered around her body, toying with her."
    MYU "Oooooh...! {image=[ICON.HEART]}"
    MYU "M-Myu's breasts f-feel s-so sensitive!"
    "A protruding tongue from one of the tentacles gently pressed its way into Myu's mouth."
    MYU "M-Mmfghh!"
    "Myu's body was nothing more than something for me to play with now, overcome with pleasure, she simply continued to writhe hotly as she moaned uncontrollably."
    MYU "{i}H-Husband! Myu loves you! Myu loves you so much!!{/i} {image=[ICON.HEART]}"
    MYU 'Myu feels incredible!'
    MYU "F-Fuck Myu butt! Don't stop!"
    MYU "Myu butt yours!"
    "I grunted in approval, as one tentacle slide around towards Myu's mouth."
    MYU "Huh? What this one-"
    "The tentacle slammed against Myu's face, forcing the soft tube like tongue down her throat."
    MYU "Mmmfghh?!"
    scene myu_para_doggy_anal_tent_2 with dissolve
    $ Pause()
    "Myu's eyes widened in shock as I poured the warm chemicals down into her body."
    "Through opening pores, I could allow Myu to breathe as I pumped her full of the sweet nectar that triggered and overloaded her mind and body with pleasure."
    MYU "Mmfghhh...! {image=[ICON.HEART]}"
    MYU "(W-What is this?!)"
    MYU "(What are you feeding Myu!!)"
    MYU "(Myu... f-feels...)"
    MYU "({i}Amazing!{/i})"
    MYU "(More! {i}Give Myu more!{/i})"
    MYU "Mmmfhghh...!"
    "Myu's body was in sync with me now. I could feel every intense over-sensation emitting from her as I fucked her."
    "Instinctively, I knew how potent and powerful the chemical I was releasing into her was."
    "In short bursts, a mate would simply become addicted."
    "Long term? {i}Their minds could be completely broken.{/i}"
    if tmpvar["myu_preg_alt"] == True:
        scene myu_para_doggy_alt_preg_tent with dissolve
    if tmpvar["myu_preg_alt"] == False:
        scene myu_para_doggy_alt_nopreg_tent with dissolve
    $ Pause()
    "As Myu's eyes rolled back, she continued her guttural moans as I continued to feed her my love."
    MYU "MMmfghh! Shhwww ghwwddd!"
    MYU "Lhuv yhuu! Lhuv yhuu! Lhuv yhuu!!! {image=[ICON.HEART]} {image=[ICON.HEART]}"    
    'Myu trembled and shook as orgasm after orgasm wrecked through her body.'
    "If I wasn't careful, I'd soon be leaving her completely broken, as she did her best to throw her ass back onto me with every thrust into her."
    "I grunted and snarled in approval. Every dark impulse inside of the dark passenger burned with glee."
    MYU "(Cumming! Can't stop cumming!)"
    MYU "Mmmfghh! Thinking no good! More, more, {i}more!{/i}"  
    "Feeling the end finally drawing near as the hot pleasure became too much for even me, I could no longer hold back."
    "It was time to flood her tight ass, and claim her body and mind as mine."
    "Grunting and snarling, I flooded Myu's ass with my hot, beastly seed as she quivered feeling me flooding into her."                   
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene myu_para_doggy_anal_tent_finish with flash
    $ Pause()
    MYU "{i}Mhhhfhhh...!!{/i}"
    "Watching my seed flood into her semi-translucent body, she shook with pleasure before feeling heavy and limp under my claws."
    MYU "{i}*Huff* *Huff....*{/i}"
    MYU "(Myu... butt... So full. {image=[ICON.HEART]})"
    return