label gallery_nijah_missionary:
    $ CharSetClothes("nijah", "jewelry")
    scene bg_weeping_heart_brothel_room
    show mcprologue:
        xcenter 0.3
    show nijah:
        xcenter 0.7
        xzoom -1.0
    with dissolve
    NIJAH '... {i}Come.{/i}'
    'Taking my hand, Nijah pulled me in closer and pressed a delicate kiss onto my neck.'
    'As I explored her body, reaching around to grab handfuls of her ass, she pulled me down onto the bed on top of her.'
    NIJAH 'How do you want me?'
    $ PlayMusicRandom("mus_sex")
    'Nervously, the words stumbled out of me:'
    MC 'L-Like this is fine, thank you.'
    'Nijah smiled, feeling my member hardening as it prodded between her thighs.'
    NIJAH 'Come zen.'
    NIJAH 'Let me help you with zis.'
    'Taking my cock softly in her hand, Nijah positioned the angle carefully so that when I moved clumsily forward, I thrusted inside her...'

    scene nijah_brothel_miss_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg",1)
    $ Pause()

    'Enveloped by her, wet and tight, we both gasped a little as she grabbed me by my ass, pulling me all the way inside her.'
    NIJAH 'Mmm! Yis...'
    MC 'Ahh... You’re really tight...'
    NIJAH 'Take me!'
    'She {b}was{/b} tight, yet I felt her immense passion, a craving for more of me inside her...'
    'So I gave it to her.'
    'The sound of our flesh colliding amped up as I began to steadily thrust into her.'
    NIJAH 'Yi-i-is! Don\'t you zlow down...'
    'Nijah soon wrapped her legs around me, pulling me deeper inside her as she began to moan under her breath.'
    NIJAH 'Mmm! Zis is... g-good!'
    MC '{i}*Huff* *Huff*{/i} Y-Yeah...!'
    NIJAH 'Fazter! Harder! Fuck me!'

    scene nijah_brothel_miss_fast with dissolve
    $ PlaySexFx("audio/sex_sounds/nijah_miss_3.ogg",1)
    $ Pause()

    'I slammed myself ferociously into her, Nijah grunted happily, the two of us now drenched in sweat...'
    NIJAH 'Yis, more, pound me like you mean it, my ztallion!'
    'My hands clambered over her body, groping and gnawing desperately at her breasts and soft round butt.'
    NIJAH 'Mmm! I am c-close!'
    'She cried out in ecstasy, and upon feeling her pussy squeeze the length of me in tight convoluted motions, I began to feel my body tense up as I thrusted into her faster and faster, pushing myself over the edge.'
    NIJAH 'Yis! Yis zis is it! I can feel—'
    NIJAH 'Mmmm!'
    'Feeling her body tighten once again around my member, my aching balls could finally take no more as I grunted loudly, about to cum...'
    if GalFlag("nijah", "brothel_miss", ["var_in","var_out"]):
        "Did I..."
        menu:
            'Finish inside of Nijah?':
                $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                scene nijah_brothel_miss_finish_in with flash
                $ Pause()
                'Instinctively, Nijah pulled me in closer and I released deeply into her...'
                'A hot moan escaped her lips as my warm seed poured into her and I slowly began to soften inside of her.'
            "Cum on Nijah?":
                $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                scene nijah_brothel_miss_finish_out with flash
                $ Pause()
                "Pulling out of Nijah's tight pussy, I stroked my cock for a few moments as I covered her in my hot load."
                "Nijah moaned as she felt the hot splash on her skin, giggling as she scopped up a little and pressed it into her mouth."
    elif GalFlag("nijah", "brothel_miss", "var_in"):
        'Instinctively, Nijah pulled me in closer and I released deeply into her...'
        'A hot moan escaped her lips as my warm seed poured into her and I slowly began to soften inside of her.'
        scene nijah_brothel_miss_finish_in with flash
        $ PlaySexFx('audio/sex_sounds/kiara_tent_finish.ogg')
        $ Pause()

    elif GalFlag("nijah", "brothel_miss", "var_out"):
        "Pulling out of Nijah's tight pussy, I stroked my cock for a few moments as I covered her in my hot load."
        "Nijah moaned as she felt the hot splash on her skin, giggling as she scopped up a little and pressed it into her mouth."
        scene nijah_brothel_miss_finish_out with flash
        $ PlaySexFx('audio/sex_sounds/kiara_tent_finish.ogg')
        $ Pause()

    MC '{i}*Huff*... *Huff*...{/i}'
    'Trembling with subsiding waves of pleasure I pulled out and rolled over besides her.'
    $ CharSetClothes("nijah", "normal")
    return
