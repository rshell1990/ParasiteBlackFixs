label gallery_adara_alley_fing:
    scene adara_alley_hj_bg
    show mc at left
    show adara at cleft_f
    with dissolve
    stop music fadeout 1.0
    play ambience "audio/ambience_loc/citynight.ogg"
    ADARA @talk "Would... Would you maybe follow me?"
    MC @talk "What?"
    $ CharSetVar("adara", "blush", True)
    "Adara’s cheeks burned red."
    ADARA @talk "{i}...Somewhere more private.{/i}"
    MC @talk "Oh... OH!"
    MC @talk "Well, what did you have in mind?"
    $ CharSetVar("adara", "blush", False)
    "Taking a hold of my hand, Adara led me off down to one of the darkened winding back alleyways, where she promptly shoved me against a wall and pressed another kiss onto me."
    $ PlayMusicRandom("mus_sex")
    ADARA @talk "{i}T-Touch me...{/i}"
    ADARA @talk "Please touch me."
    ADARA @talk "I want to feel your hands on me..."
    hide mc
    hide adara
    show adara_alley_fing
    with dissolve
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg", 1)
    $ Pause()
    "As Adara turned around, my hands trailed up her body and reached up her dress, pressing my fingers against her wet honeypot."
    ADARA @talk "Ahh! [player_name!t]!"
    ADARA @talk "Y-Yes...~"
    ADARA @talk "Just like that, t-touch me however you want."
    "My other hand greedily moved to reach into her dress and fondle at one of her large breasts while I kissed at her soft neck."
    "Adara closed her eyes and let out soft moans as I pushed my fingers deeper into her wet, tight crevices."
    ADARA @talk "{i}Mmmfgh...{/i}"
    ADARA @talk "Your hands are so rough..."
    ADARA @talk "L-Like an animals..."
    MC @talk "{i}*Huff*{/i} Do you need me to slow down?"
    ADARA @talk "N-No...{i}I like it.{/i}"
    "Beneath my skin, I felt the Parasite searing beneath my flesh."
    "I envisioned turning Adara around, throwing up her skirt and having my way with her here and now."
    "The thought became maddening, all consuming as her grunts and soft moans left me shaking, desperate to go further and take her as my mate."
    "...But this was Adara... One of my oldest friends."
    "Biting hard down onto myself, I felt myself twisting my stomach into knots as I resisted my dark impulses."
    ADARA @talk "[player_name!t]... What’s wrong?"
    MC @talk "Nothing {i}*huff*{/i} Just... {i}hard{/i} not to try go further..."
    ADARA @talk "...S-Soon... soon I’ll be ready for you."
    ADARA @talk "If you w-want me like that still."
    "Adara added nervously..."
    ADARA '{i}He... He wants me like that...{/i}'
    ADARA '{i}He wants me!{/i}'
    ADARA @talk "[player_name!t], I-"
    ADARA @talk "Mmhmm!"
    ADARA @talk "I’m cumming! Yes! YES!"
    "Adara’s head moved back onto my shoulder as I felt her tighten around my fingers."
    "her eyes widened as her mouth hung slightly agape, seemingly choking on air as she trembled slightly."
    "As Adara’s head slumped forward and her body began to relax, she breathed in heavily as I loosened my grip on her."
    $ StopSexFx()
    stop music fadeout 1.0
    scene adara_alley_hj_bg
    show mc at cleft
    show adara at cright_f
    with dissolve
    ADARA @talk "...Thank you."
    ADARA @talk "I... I know I shouldn’t have thrown all this on you like that but-"
    MC @talk "Adara, it’s alright."
    "Adara smiled, and moved forward once again to press a quick kiss onto my lips, as though she was re-affirming whatever was going on between us was still real."
    return