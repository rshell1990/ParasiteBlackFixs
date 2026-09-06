label rom_Ves_HaveSomeFun:
    VES @lewd_talk "Fun you say?"
    VES @lewd_talk "What do you have in mind?"
    menu:
        "Care to practice that position you like?":
            VES @lewd_talk "Oh, now we're talking!"
            if RomanceVes().lingerie == 4:
                VES @lewd_talk "Do you want me to wear that outfit you gave me?"
                menu:
                    "Sure.":
                        $ RomanceVes().wearsLing = True
                    "No, I prefer you naked.":
                        $ RomanceVes().wearsLing = False
            jump rom_Ves_HaveSomeFun2
        "Actually, something completely different.":
            VES @surp_talk "Huh?"
            return

label rom_Ves_HaveSomeFun2:
    VES @lewd 'Alright {i}human{/i}, just give me a moment...'
    scene black with dissolve
    "Minutes later..."
    if RomanceVes().wearsLing:
        $ CharSetClothes("ves", "ling")
    else:
        $ CharSetClothes("ves", "naked")
    VES @talk 'You can come in now!'
    $ LocFlush()
    show ves:
        xcenter 0.6
        xzoom -1.0
    with dissolve
    show mc:
        xcenter 0.2
    with dissolve
    'As I stepped back into the tent, Ves stood there more confidently now, waiting with her hand on her hip as she smirked at me.'
    VES @talk 'Are you ready?'
    "Ves’ eyes widened when she saw my hard-on standing to attention once again, my eyes hungrily looking her up and down."
    VES @talk 'Well... I guess that answers that.'
    VES @talk 'Come, lie down on the floor.'
    VES @talk "I bet you've been thinking about doing this again since last time!"
    scene black with dissolve
    VES @talk 'Hold still! Don’t move!'
    MC @talk 'Ves!—'
    MC @talk 'Mmmff!'
    $ CharSetClothes("mc", "naked")
    jump ves_sex69
