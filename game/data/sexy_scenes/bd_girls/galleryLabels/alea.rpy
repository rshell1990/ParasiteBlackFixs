label gallery_alea_tj:
    scene black with dissolve
    if GalFlag("bd_girls","alea_tj",["var_mask","var_nomask"]):
        "Was she wearing a mask?"
        menu:
            "Yes":
                jump gallery_alea_tj_mask
            "No":
                jump gallery_alea_tj_nomask
    elif GalFlag("bd_girls","alea_tj","var_mask"):
        jump gallery_alea_tj_mask
    elif GalFlag("bd_girls","alea_tj","var_nomask"):
        jump gallery_alea_tj_nomask

label gallery_alea_tj_mask:
    $ PlayMusicRandom("mus_sex")
    ALEA 'Mmm, if only they all came here like you.'
    'Beside me, I could see the girl wrapping her tits around [player_name!t], rhythmically bouncing them as she spoke something to him.'
    ALEA 'Ah ah...! Eyes on me now.'
    ALEA "Now, let's have some fun with this!"
    scene alea_tj_mask with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
    $ Pause()
    "Alea's soft breasts wrapped around my cock as she began to rhythmically motion up and down teasingly."
    "She kept glancing towards [player_name!t]'s girl, and I got the distinct impression there was some kind of small competition between them that neither of spoke openly about."
    ALEA 'How do they feel my lord? Are my tits not better at stroking your cock than your little wife?'
    MARKUS 'Ahh! I have no wife.'
    ALEA 'What? No lovers? Mistress at least?'
    MARKUS 'Mhhmm... N-Not yet.'
    MARKUS 'Though I have familiarized myself with a few of the brothels now!'
    ALEA "Mmm... No matter, I'm going to make this unforgettable for you anyway!"
    "Alea's tits bounced up and down faster as she pressed them together tightly with her hands, there was a wild glint in her eyes as she grinned watching me writhe and squirm in her grip."
    MARKUS "{i}*Huff!*{/i} I don't know how much longer I can hold like this!"
    MARKUS 'Gods woman! Where did you learn to do this?'
    ALEA 'Hush my lord, focus on covering this poor, depraved, Ramonian whores tits.'
    ALEA 'A-Ah...! I can feel your cock twitching!'
    ALEA 'Are you close?'
    MARKUS "Yes! Grgh! I can't hold it much longer!"
    ALEA "Don't, cover me in your hot seed! Come on! Do it! DO IT!"
    scene alea_tj_mask_finish with flash
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ Pause()
    ALEA 'Oooh!'
    MARKUS 'Gods...'
    ALEA '{i}*Giggles*{/i} Well... That was a lot.'
    return

label gallery_alea_tj_nomask:
    $ PlayMusicRandom("mus_sex")
    ALEA 'Mmm, if only they all came here like you.'
    'Beside me, I could see the girl wrapping her tits around [player_name!t], rhythmically bouncing them as she spoke something to him.'
    ALEA 'Ah ah...! Eyes on me now.'
    ALEA "Now, let's have some fun with this!"
    scene alea_tj_nomask with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
    $ Pause()
    "Alea's soft breasts wrapped around my cock as she began to rhythmically motion up and down teasingly."
    "She kept glancing towards [player_name!t]'s girl, and I got the distinct impression there was some kind of small competition between them that neither of spoke openly about."
    ALEA 'How do they feel my lord? Are my tits not better at stroking your cock than your little wife?'
    MARKUS 'Ahh! I have no wife.'
    ALEA 'What? No lovers? Mistress at least?'
    MARKUS 'Mhhmm... N-Not yet.'
    MARKUS 'Though I have familiarized myself with a few of the brothels now!'
    ALEA "Mmm... No matter, I'm going to make this unforgettable for you anyway!"
    "Alea's tits bounced up and down faster as she pressed them together tightly with her hands, there was a wild glint in her eyes as she grinned watching me writhe and squirm in her grip."
    MARKUS "{i}*Huff!*{/i} I don't know how much longer I can hold like this!"
    MARKUS 'Gods woman! Where did you learn to do this?'
    ALEA 'Hush my lord, focus on covering this poor, depraved, Ramonian whores tits.'
    ALEA 'A-Ah...! I can feel your cock twitching!'
    ALEA 'Are you close?'
    MARKUS "Yes! Grgh! I can't hold it much longer!"
    ALEA "Don't, cover me in your hot seed! Come on! Do it! DO IT!"
    scene alea_tj_nomask_finish with flash
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ Pause()
    ALEA 'Oooh!'
    MARKUS 'Gods...'
    ALEA '{i}*Giggles*{/i} Well... That was a lot.'
    return