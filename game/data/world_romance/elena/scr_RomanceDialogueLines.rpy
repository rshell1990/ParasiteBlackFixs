label rom_ElenaHowYOuFeelin:
    ELENA @talk "I'm fine, {i}better{/i} now I have you around."
    ELENA @grumpy "It's funny... I was always surrounded by people, but I always felt so alone."
    ELENA @lewd '...Till I met {i}you.{/i}'
    ELENA @talk "Gods, you're making me sound like some maidens first crush, Shoo! Go bother someone else!"
    MC @talk 'As you wish, {i}fair maiden.{/i}'
    ELENA @lewd 'Very funny.'
    return

label rom_ElenaComeCloseer:
    ELENA @talk 'Hm? What are you-'
    #MC and Elena kiss
    hide elena
    hide mc
    show cg_mc_elena_kiss_armor at center
    with dissolve
    ELENA 'Mhmmm...'
    ELENA '(My heart races so fast when he does this.)'
    #Stop kiss art
    hide cg_mc_elena_kiss_armor with dissolve
    show elena at center_f
    ELENA @lewd 'Ahh... Warn me next time!'
    MC @talk "Couldn't resist."
    ELENA @talk 'Hmmm...'
    if CharGetRel("elena") < 5:
        $ CharChangeRel("elena", 1)
    return
