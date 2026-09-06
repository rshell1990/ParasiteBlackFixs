label gallery_ves_titjob:
    scene black with dissolve
    if GalFlag("ves","tj",["var_ling","var_naked"]):
        "Was she wearing lingerie?"
        menu:
            "Yes":
                jump gallery_ves_titjob_ling
            "No, she was naked":
                jump gallery_ves_titjob_naked
    elif GalFlag("ves","tj","var_ling"):
        jump gallery_ves_titjob_ling
    elif GalFlag("ves","tj","var_naked"):
        jump gallery_ves_titjob_naked

label gallery_ves_titjob_naked:
    scene ves_titjob_naked_slow
    with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    $ Pause()
    'Ves wrapped her soft, ample breasts around my cock, shyly looking for approval as she began to massage my cock between her tits.'
    'Grunting in approval, Ves smiled as she pressed her breasts together, enveloping my cock as she began to move up and down, softly massaging me.'
    'Ves continued happily for a while, her eyes looking up to me inquisitively for any approving grunts and moans.'
    'Each time I showed my pleasure, she made sure to double down on whatever she was doing.'
    VES @talk 'Hearing you moan like this is...'
    VES @talk '... {i}Making me more excited.{/i}'
    MC @smile 'Ves, you’re... Ahhhh.'
    VES @talk 'That’s right... Moan more for me.'
    VES @talk 'Tell me you like it.'
    MC @talk 'Mmm, I like it, Ves... I like it alright! I like it a lot!'
    VES @talk 'This is {i}*huff*{/i} quite the workout!'
    MC @talk 'Mmm... Yeah just...'
    MC @talk 'Ahh...'
    if GalFlag("ves","tj",["var_usemouth","var_doinggreat"]):
        "Did I..."
        menu:
            "Ask Ves to use her mouth as well?":
                VES @talk 'You want me to...'
                VES @talk 'Put my mouth on it again?'
                MC @talk '{i}*Huff*{/i} Y-Yeah, but you—'
                "Ves' mouth warmly wrapped around my cock as her head began to bop up and down keenly."
                scene ves_titjob_naked_fast with dissolve
                $ Pause()
                'I sighed happily, watching as she continued to push her soft tits together enveloping my cock while her tongue thrashed and beat against my cock.'
                VES @talk '{i}*Slurp!* *Slurp!* Mmffghh!{/i} {image=[ICON.HEART]}'
                VES @talk "(I can feel his spear stretching out my mouth, it's so... {i}powerful{/i})"
                VES @talk "(There's something about it, some taste or scent to it.)"
                VES @talk "(It's... It's...)"
                VES @talk '({i}addictive.{/i})'
                VES @talk '(I need more! MORE! I want to feel to taste his seed and give it all to me!)'
                'Ves continued to lewdly work my cock with a determined lewd look, her eyes locked onto me as she drove me to the edge.'
                'Finally, I was unable to hold back from the intense pleasure, and I felt myself grunt as I unleashed my seed into her warm, wet mouth.'
            "Tell Ves she’s doing great?":
                VES @talk 'Yes! Now finish for me!'
                scene ves_titjob_naked_fast with dissolve
                $ Pause()
                VES @talk 'Give me that seed!'
                VES @talk 'Your c-cock feels so good between my tits!'
                MC @talk 'Ahhh! Ves! I am-'
                VES @talk 'Do it!'
                VES @talk 'Claim me and cover me in your seed!'
                MC @talk '...!'
    elif GalFlag("ves","tj","var_usemouth"):
        VES @talk 'You want me to...'
        VES @talk 'Put my mouth on it again?'
        MC @talk '{i}*Huff*{/i} Y-Yeah, but you—'
        "Ves' mouth warmly wrapped around my cock as her head began to bop up and down keenly."
        scene ves_titjob_naked_fast with dissolve
        $ Pause()
        'I sighed happily, watching as she continued to push her soft tits together enveloping my cock while her tongue thrashed and beat against my cock.'
        VES @talk '{i}*Slurp!* *Slurp!* Mmffghh!{/i} {image=[ICON.HEART]}'
        VES @talk "(I can feel his spear stretching out my mouth, it's so... {i}powerful{/i})"
        VES @talk "(There's something about it, some taste or scent to it.)"
        VES @talk "(It's... It's...)"
        VES @talk '({i}addictive.{/i})'
        VES @talk '(I need more! MORE! I want to feel to taste his seed and give it all to me!)'
        'Ves continued to lewdly work my cock with a determined lewd look, her eyes locked onto me as she drove me to the edge.'
        'Finally, I was unable to hold back from the intense pleasure, and I felt myself grunt as I unleashed my seed into her warm, wet mouth.'
    elif GalFlag("ves","tj","var_doinggreat"):
        VES @talk 'Yes! Now finish for me!'
        scene ves_titjob_naked_fast with dissolve
        $ Pause()
        VES @talk 'Give me that seed!'
        VES @talk 'Your c-cock feels so good between my tits!'
        MC @talk 'Ahhh! Ves! I am-'
        VES @talk 'Do it!'
        VES @talk 'Claim me and cover me in your seed!'
        MC @talk '...!'
    else:
        pass
    scene ves_titjob_naked_finish
    with flash
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg",0)
    $ Pause()
    VES @surprised 'Gah! There’s so much of it!'
    MC @smile '...'
    VES "... Stop grinning and just get me something to wipe my face."
    'Ves pouted, grumbling beneath her breath.'
    'Ves pouted cutely,'
    VES @talk '{i}You better not have gotten anything in my hair...{/i}'
    $ AutoMus(True)
    return

label gallery_ves_titjob_ling:
    scene ves_titjob_ling_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    $ Pause()
    'Ves wrapped her soft, ample breasts around my cock, shyly looking for approval as she began to massage my cock between her tits.'
    'Grunting in approval, Ves smiled as she pressed her breasts together, enveloping my cock as she began to move up and down, softly massaging me.'
    'Ves continued happily for a while, her eyes looking up to me inquisitively for any approving grunts and moans.'
    'Each time I showed my pleasure, she made sure to double down on whatever she was doing.'
    VES @talk 'Hearing you moan like this is...'
    VES @talk '... {i}Making me more excited.{/i}'
    MC @smile 'Ves, you’re... Ahhhh.'
    VES @talk 'That’s right... Moan more for me.'
    VES @talk 'Tell me you like it.'
    MC @talk 'Mmm, I like it, Ves... I like it alright! I like it a lot!'
    VES @talk 'This is {i}*huff*{/i} quite the workout!'
    MC @talk 'Mmm... Yeah just...'
    MC @talk 'Ahh...'
    if GalFlag("ves","tj",["var_usemouth","var_doinggreat"]):
        "Did I..."
        menu:
            "Ask Ves to use her mouth as well?":
                VES @talk 'You want me to...'
                VES @talk 'Put my mouth on it again?'
                MC @talk '{i}*Huff*{/i} Y-Yeah, but you—'
                "Ves' mouth warmly wrapped around my cock as her head began to bop up and down keenly."
                scene ves_titjob_ling_fast with dissolve
                $ Pause()
                'I sighed happily, watching as she continued to push her soft tits together enveloping my cock while her tongue thrashed and beat against my cock.'
                VES @talk '{i}*Slurp!* *Slurp!* Mmffghh!{/i} {image=[ICON.HEART]}'
                VES @talk "(I can feel his spear stretching out my mouth, it's so... {i}powerful{/i})"
                VES @talk "(There's something about it, some taste or scent to it.)"
                VES @talk "(It's... It's...)"
                VES @talk '({i}addictive.{/i})'
                VES @talk '(I need more! MORE! I want to feel to taste his seed and give it all to me!)'
                'Ves continued to lewdly work my cock with a determined lewd look, her eyes locked onto me as she drove me to the edge.'
                'Finally, I was unable to hold back from the intense pleasure, and I felt myself grunt as I unleashed my seed into her warm, wet mouth.'
            "Tell Ves she’s doing great?":
                VES @talk 'Yes! Now finish for me!'
                scene ves_titjob_ling_fast with dissolve
                $ Pause()
                VES @talk 'Give me that seed!'
                VES @talk 'Your c-cock feels so good between my tits!'
                MC @talk 'Ahhh! Ves! I am-'
                VES @talk 'Do it!'
                VES @talk 'Claim me and cover me in your seed!'
                MC @talk '...!'
    elif GalFlag("ves","tj","var_usemouth"):
        VES @talk 'You want me to...'
        VES @talk 'Put my mouth on it again?'
        MC @talk '{i}*Huff*{/i} Y-Yeah, but you—'
        "Ves' mouth warmly wrapped around my cock as her head began to bop up and down keenly."
        scene ves_titjob_ling_fast with dissolve
        $ Pause()
        'I sighed happily, watching as she continued to push her soft tits together enveloping my cock while her tongue thrashed and beat against my cock.'
        VES @talk '{i}*Slurp!* *Slurp!* Mmffghh!{/i} {image=[ICON.HEART]}'
        VES @talk "(I can feel his spear stretching out my mouth, it's so... {i}powerful{/i})"
        VES @talk "(There's something about it, some taste or scent to it.)"
        VES @talk "(It's... It's...)"
        VES @talk '({i}addictive.{/i})'
        VES @talk '(I need more! MORE! I want to feel to taste his seed and give it all to me!)'
        'Ves continued to lewdly work my cock with a determined lewd look, her eyes locked onto me as she drove me to the edge.'
        'Finally, I was unable to hold back from the intense pleasure, and I felt myself grunt as I unleashed my seed into her warm, wet mouth.'
    elif GalFlag("ves","tj","var_doinggreat"):
        VES @talk 'Yes! Now finish for me!'
        scene ves_titjob_ling_fast with dissolve
        $ Pause()
        VES @talk 'Give me that seed!'
        VES @talk 'Your c-cock feels so good between my tits!'
        MC @talk 'Ahhh! Ves! I am-'
        VES @talk 'Do it!'
        VES @talk 'Claim me and cover me in your seed!'
        MC @talk '...!'
    else:
        pass
    scene ves_titjob_ling_finish with flash
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg",0)
    $ Pause()
    VES @surprised 'Gah! There’s so much of it!'
    MC @smile '...'
    VES "... Stop grinning and just get me something to wipe my face."
    'Ves pouted, grumbling beneath her breath.'
    'Ves pouted cutely,'
    VES @talk '{i}You better not have gotten anything in my hair...{/i}'
    VES @smile 'That was... {i}fun.{/i}'
    MC @smile 'That’s one word for it.'
    $ AutoMus(True)
    return
