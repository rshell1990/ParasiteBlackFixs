label ves_bjRepeat:
    $ CharSetClothes("mc", "naked")
    $ CharSetClothes("ves", "naked")
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    'The next morning I awoke to the unsettling feeling of Ves towering over me, blocking out the diminishing sunlight that had managed to break its way through the fabric of the tent.'
    MC @surprised 'Mm? Ves?'
    VES @talk '...Good morning lover.'
    'I smirked at the comment.'
    MC @smile '{i}Lover{/i} is now?'
    'Ves blushed at the remark, caught off guard.'
    VES @surprised "D-Don't make it strange human!"
    VES @lewd 'I am just trying to set the mood.'
    MC @talk 'Set the mood? You mean-'
    VES @lewd "Come [player_name!t], I want to 'finish' you again!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Ves prompted me to once again strip down naked.'
    'Now standing confidently in front of me as my eyes revelled in the strength of her body, already hard and throbbing I stared at her round tits and pussy nestled beneath the thick black bush.'
    MC @smile 'Y-Yeah... It’s true alright!'
    'Crouching down, Ves proceeded to wrestle with me and pull off my clothes, smiling as she pulled out my member with both of her hands.'
    VES @smile 'Are you ready?'
    'With a determined look, Ves once again took this as some kind of ‘warrior’s challenge’, proudly declaring...'
    VES @talk 'This time I shall make it feel even better for you!'
    if RomanceVes().lingerie == 4:
        VES @talk 'Say, would you like me to wear that nice outfit for you?'
        menu:
            'Oh yes, please do.':
                scene ves_titjob_ling_slow with dissolve
                $ RomanceVes().wearsLing = True
            "Nah, I'd like you naked instead.":
                scene ves_titjob_naked_slow with dissolve
    else:
        scene ves_titjob_naked_slow with dissolve
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

    menu:
        "Ask Ves to use her mouth as well.":
            if RomanceVes().wearsLing:
                scene ves_titjob_ling_fast with dissolve
            else:
                scene ves_titjob_naked_fast with dissolve
            $ Pause()
            VES @talk 'You want me to...'
            VES @talk 'Put my mouth on it again?'
            MC @talk '{i}*Huff*{/i} Y-Yeah, but you—'
            "Ves' mouth warmly wrapped around my cock as her head began to bop up and down keenly."
            $ UnlockGalFlag("ves","tj","var_usemouth")
            'I sighed happily, watching as she continued to push her soft tits together enveloping my cock while her tongue thrashed and beat against my cock.'
            VES @talk '{i}*Slurp!* *Slurp!* Mmffghh!{/i} {image=[ICON.HEART]}'
            VES @talk "(I can feel his spear stretching out my mouth, it's so... {i}powerful{/i})"
            VES @talk "(There's something about it, some taste or scent to it.)"
            VES @talk "(It's... It's...)"
            VES @talk '({i}addictive.{/i})'
            VES @talk '(I need more! MORE! I want to feel to taste his seed and give it all to me!)'
            'Ves continued to lewdly work my cock with a determined lewd look, her eyes locked onto me as she drove me to the edge.'
            'Finally, I was unable to hold back from the intense pleasure, and I felt myself grunt as I unleashed my seed into her warm, wet mouth.'
        "Tell Ves she’s doing great.":
            if RomanceVes().wearsLing:
                scene ves_titjob_ling_fast with dissolve
            else:
                scene ves_titjob_naked_fast with dissolve
            $ Pause()
            VES @talk 'Yes! Now finish for me!'
            VES @talk 'Give me that seed!'
            VES @talk 'Your c-cock feels so good between my tits!'
            MC @talk 'Ahhh! Ves! I am-'
            VES @talk 'Do it!'
            VES @talk 'Claim me and cover me in your seed!'
            $ UnlockGalFlag("ves","tj","var_doinggreat")
            MC @talk '...!'

    if RomanceVes().wearsLing:
        scene ves_titjob_ling_finish
        $ UnlockGalFlag("ves","tj","var_ling")
    else:
        scene ves_titjob_naked_finish
        $ UnlockGalFlag("ves","tj","var_naked")
    with flash
    $ ReduceInfectionFromSex("ves")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg",0)
    $ Pause()
    $ UnlockGalSceneAndGrantXp("ves","tj")
    VES @surprised 'Gah! There’s so much of it!'
    MC @smile '...'
    VES "... Stop grinning and just get me something to wipe my face."
    'Ves pouted, grumbling beneath her breath.'
    'Ves pouted cutely.'
    VES @talk '{i}You better not have gotten anything in my hair...{/i}'
    VES @smile 'That was... {i}fun.{/i}'
    MC @smile 'That’s one word for it.'
    $ AutoMus(True)
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    VES @talk 'You can think of another?'
    MC @talk 'I can think of a few words, but they all involve us not leaving your tent today.'
    'Ves smiled, her cheeks once again flushed a shade of pink as she averted her gaze.'
    VES @lewd 'That sounds nice...'
    VES @talk 'But... {i}another time.{/i}'
    $ CharChangeRel("ves", 1)
    MC @talk 'Yes, ma’am.'
    VES @talk 'I have to go scavenge for a while... Come back later if you want some food or...'
    VES @lewd 'Uhh, maybe some more... fun.'
    hide ves with dissolve
    MC @talk 'You don’t have to tell me twice!'
    hide mc with dissolve
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("ves", "normal")
    $ DialogueVes().outHunting = True
    $ RomanceVes().wearsLing = False
    $ LocSet("ves_camp")
    $ LocEnter()
