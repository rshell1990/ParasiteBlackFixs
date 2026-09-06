label rom_Myu_initial:
    $ CharChangeRel("myu", 1)
    $ CharSetLover("myu")
    $ CharReplaceRelEntry("myu", "initial_no_romance", "initial_romance")
    $ QstStart(RomanceMyu)
    MYU @blush "R-Really?"
    MYU @blush "You want Myu?"
    MC @lewd "I uh, I do."
    MC @smile "That is, if you still want me to-"
    'Myu suddenly leapt onto me for another hug.'
    MYU 'Myu will be best wife!'
    MC 'Haha... You know, we have to actually get married to be husband and wife, right?'
    "Myu didn't listen, snuggling in closer to my chest."
    MYU 'Touch butt please.'
    hide mc
    hide myu
    show cg_myu_hug_grab at center
    with dissolve
    'I did as Myu asked, fondling her butt a little as she moaned softly.'
    'Myu pushed herself away, still grinning from ear to ear.'
    MYU @smile "Myu has plan to learn how to be good wife."
    MC @talk "Huh?"
    MYU @blush "Myu has been... spying on people in Pleasure District."
    MYU @blush "Learning things... {i}Lots of things.{/i}"
    hide cg_myu_hug_grab
    show mc at cleft
    show myu at cright_f
    with dissolve
    MC @lewd "Myu!"
    MYU @blush "C-Can Myu try something?"
    MYU @blush "Wanted to try for a while now... But, was too worried with everything going on."
    menu:
        "Go for it.":
            jump rom_myu_titjob
        "Another time, Myu.":
            MYU @talk "Aw, okay!"
            MYU @talk "Just let Myu know when you want to try!"
            $ LocEnter()

label rom_myu_somefun:
    if RomanceMyu().tumbleMood:
        MYU @blush "Fufu~ What did you want to try?"
        menu:
            "Can you use your tits again?":
                MYU @blush "Anything you want, husband."
                jump rom_myu_titjob
            "How about you get on top of me?":
                MYU @joy "Oooh!"
                MYU @blush "Lay down..."
                if CharGetPreg("myu") >= 2:
                    jump rom_myu_cowgirl_preg
                else:
                    jump rom_myu_cowgirl_nopreg
            "Myu, would you like to have 'fun' while I'm in my other form?":
                MYU @blush "Yes husband ~"
                MYU @blush "Myu would like that a lot."
                jump rom_myu_para_doggy
            "Nevermind.":
                MYU @sad "Okay..."
                return
    else:
        MYU @talk "Mmmm, not today, husband."
        MYU @talk "Myu too tired..."
        return

label rom_myu_hug:
    MYU @blush "Y-Yes please... Myu likes hugs."
    hide mc
    hide myu
    with dissolve
    show cg_myu_hug_grab at center
    with dissolve
    'Myu came forward to hug me, blushing profusely as she let me fondle her ass.'
    MYU "Mmm, your hands feel so nice."
    "Myu pulled away, still blushing like a young bride."
    MYU @blush "T-That was nice, h-husband."
    hide cg_myu_hug_grab
    with dissolve
    show mc at cleft
    show myu at cright_f
    with dissolve
    return