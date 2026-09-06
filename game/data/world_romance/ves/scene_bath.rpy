label ves_bathRepeat:
    scene ves_bath with dissolve
    'My cock once again throbbed and now forced and pressed itself between Ves’ legs, impossible to contain. Ves stared down at the hard member between her legs as it nestled beneath her pussy.'
    VES @talk '{i}*Heavy breathing*{/i}'
    VES @talk 'I see my mate is in need of servicing again...'
    MC @talk '{i}*Huff*{/i} Ves—'
    'Ves’ hands softly wrapped around my cock, gently and curiously feeling along the shaft, her breath heavy as she did so. As my cock rubbed up against her clit and soft bush, she shuddered slightly, biting her lower lip.'
    VES @talk 'It’s... {i}very big...{/i}'
    MC @talk '{i}*Huff*{/i} Ves... I need relief...'
    'Ves breathed excitedly as she whispered sultrily'
    VES @talk 'T-Touch me...'
    VES @talk 'I want to feel your hands on me again.'
    'As my hands reached around, I gently fondled at her soft breasts, resting my thumb over her dark areola, feeling the nipples harden as I lightly squeezed and twirled them between my finger and my thumb.'
    'My other hand glided past her soft stomach towards the smooth black bush. Ves moaned softly as my fingers rubbed against her clit before they softly pushed inside of her.'
    'Ves’ head rested back on my shoulder as her hands continued to stroke my cock. Finally, I stopped fondling at her breasts and reached up to raise her chin towards me and placed a soft kiss onto her lips.'
    'She seemed more taken by surprise at this than anything else, her eyes widened in shock before she slowly closed them and sunk into the kiss. As my tongue slipped into her mouth, I felt myself curiously pass by her fangs before her tongue met mine.'
    'She moaned softly, now gently trembling in my arms, Ves reluctantly pulled away from me, breathing heavily as she leaned her head forward.'
    MC @talk "Ahhh... Ves, that felt great."
    VES @talk  '{i}*Huff*{/i} Yes...'
    VES @talk "Mmm, we b-best stop here before I can't control-"
    VES @talk 'I mean...'
    VES @talk 'Before things get out of hand.'
    $ StopSexFx()
    $ CharSetClothes("mc", "naked")
    $ CharSetClothes("ves", "naked")
    $ LocFlush()
    with dissolve
    show mc at cleft
    show ves at cright_f
    with dissolve
    VES @smile 'I...'
    VES @smile_talk "I think that's enough bathing for now."
    'Disappointed, I nodded as Ves slipped away.'
    hide ves with dissolve
    scene black with dissolve
    MC '(... Damn it.)'
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("ves", "normal")
    $ UnlockGalSceneAndGrantXp("ves","bath")
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    while IsInTimeFrame(TIME_AFTERNOON,TIME_DAY_START):
        $ TimeAdvBy(TIME_1H)
        $ Pause(0.1)
    jump ves_bjRepeat
