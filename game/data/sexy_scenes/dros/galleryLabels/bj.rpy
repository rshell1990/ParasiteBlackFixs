label gallery_dros_bj:
    scene black with dissolve
    if ((GalFlag("dros", "bj", "var_pretf_naked") or 
        GalFlag("dros", "bj", "var_pretf_dress")) and 
        (GalFlag("dros", "bj", "var_posttf_naked") or 
        GalFlag("dros", "bj", "var_posttf_dress"))):
            "Was it Dros or Draya?"
            menu:
                "Dros":
                    jump gallery_dros_bj_preTf
                "Draya":
                    jump gallery_dros_bj_postTf
    elif GalFlag("dros", "bj", ["var_pretf_naked", "var_pretf_dress"]):
        jump gallery_dros_bj_preTf
    elif GalFlag("dros", "bj", ["var_prostf_naked", "var_posttf_dress"]):
        jump gallery_dros_bj_postTf
    
    elif GalFlag("dros", "bj", "var_pretf_naked"):
        jump gallery_dros_bj_preTf_naked
    elif GalFlag("dros", "bj", "var_pretf_dress"):
        jump gallery_dros_bj_preTf_dress
    elif GalFlag("dros", "bj", "var_posttf_naked"):
        jump gallery_dros_bj_postTf_naked
    elif GalFlag("dros", "bj", "var_posttf_dress"):
        jump gallery_dros_bj_postTf_dress

label gallery_dros_bj_preTf:
    if GalFlag("dros","bj",["var_pretf_naked","var_pretf_dress"]):
        "What was he wearing?"
        menu:
            "Not much.":
                jump gallery_dros_bj_preTf_naked
            "That slutty outfit of his.":
                jump gallery_dros_bj_preTf_dress
    elif GalFlag("dros","bj","var_pretf_naked"):
        jump gallery_dros_bj_preTf_naked
    elif GalFlag("dros","bj","var_pretf_dress"):
        jump gallery_dros_bj_preTf_dress

label gallery_dros_bj_postTf:
    if GalFlag("dros","bj",["var_posttf_naked","var_posttf_dress"]):
        "What was she wearing?"
        menu:
            "Not much.":
                jump gallery_dros_bj_postTf_naked
            "That slutty outfit of hers.":
                jump gallery_dros_bj_postTf_dress
    elif GalFlag("dros","bj","var_posttf_naked"):
        jump gallery_dros_bj_postTf_naked
    elif GalFlag("dros","bj","var_posttf_dress"):
        jump gallery_dros_bj_postTf_dress

label gallery_dros_bj_preTf_naked:
    MC 'Get on your knees, I want those lips wrapped around my cock.'
    $ PlayMusicRandom("mus_sex")
    'Dros did as he was told, obediently dropping to his knees as my member pressed against his warm cheek.'
    'His soft, warm hands gently stroked at my cock rhythmically.'
    "Dros' hot breathe touched my cock as he breathed excitedly for what was to come."
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    scene dros_bj_naked with dissolve
    $ Pause()
    DROS "Gods..." 
    DROS "You really are blessed with a great spear, aren't you?"
    "Dros trembled slightly with excitement as he gently kissed the tip with his warm, soft lips."
    DROS 'W-Would you perhaps, um... {i}Be a little mean to me please?{/i}'
    'I raised a curious eyebrow.'
    DROS 'H-Hey...'
    DROS 'It turns me on.'
    MC '...Are you still talking? You should be worshipping my cock slut.'
    DROS 'A-Ah! Yes, [dros_player_ref!t].'
    "Dros' lips wrapped around my cock as he began to gently bop his head forward and back."
    'His hot warm mouth tenderly wrapped around me as his wet tongue wrapped around my cock.'
    MC "Ahhh... That's it."
    MC "Good little elvish slut."
    DROS '{i}*Slurp!*{/i} Mmfghh...! {i}*Slurp!*{/i}'
    'Dros continued to coo and moan softly as his head glided back and forth over my cock.'
    'His lips struggled to wrapped around the thick member, but as his eyes looked into mine I could see the desperation to please me.'
    DROS 'Mmmfghh...!'
    MC 'Ahh! This is all you elven bitches are good for, draining balls dry and taking cock!'
    MC "But I'm sure you knew that already, right?"
    "Dros' hard cock twitched with excitement as he threw his head forward desperately."
    'As his warm mouth coated my cock in saliva, I began to feel myself struggling to hold back.'
    "The intense, hot sensation of Dros' lips as he sucked my cock as though his life depended on it, was driving me wild."
    DROS 'Mmm!! {i}*Slurp!*{/i}'
    'Dros must have sensed it too, because he began to slide his mouth deeper, taking as much of my cock as he could down into his throat.'
    MC 'G-Grghh! You little elvish w-whore!'
    MC "I'm so close!"
    DROS 'Mmmfghhh!!'
    'Finally, I could take no more of his tender, loving mouth.'
    MC "I'm going to cum!"
    if GalFlag("dros","bj",["var_pretf_naked_fin_in","var_pretf_naked_fin_out"]):
        "Did I..."
        menu:
            'Make him swallow it?':
                scene dros_bj_naked_finish_in
                with flash
                $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
                $ Pause()
                'Unable to hold back anymore, I released my hot seed down his throat.'
                'Dros let out some hot moans as he desperately tried to swallow down every drop of my overflowing load.'
                DROS 'Mmmfghh...!!'
                MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
                "Pulling my cock out of his mouth, Dros' cheeks puffed out as he gulped and swallowed down the last of my load and presented his open empty mouth to me." 
                DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
            'Cover his face?':
                scene dros_bj_naked_finish_out
                with flash
                $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
                $ Pause()
                "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
                "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
                DROS '(G-Gods... Does he ever stop cumming?)'
                MC "{i}*Huff*{/i} Oh fuck..."
                MC "You drained me dry!"
    elif GalFlag("dros","bj","var_pretf_naked_fin_in"):
        scene dros_bj_naked_finish_in
        with flash
        $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
        $ Pause()
        'Unable to hold back anymore, I released my hot seed down his throat.'
        'Dros let out some hot moans as he desperately tried to swallow down every drop of my overflowing load.'
        DROS 'Mmmfghh...!!'
        MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
        "Pulling my cock out of his mouth, Dros' cheeks puffed out as he gulped and swallowed down the last of my load and presented his open empty mouth to me." 
        DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
    elif GalFlag("dros","bj","var_pretf_naked_fin_out"):
        scene dros_bj_naked_finish_out
        with flash
        $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
        $ Pause()
        "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
        "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
        DROS '(G-Gods... Does he ever stop cumming?)'
        MC "{i}*Huff*{/i} Oh fuck..."
        MC "You drained me dry!"
    "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
    "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
    DROS '(G-Gods... Does he ever stop cumming?)'
    MC "{i}*Huff*{/i} Oh fuck..."
    MC "You drained me dry!"
    return
label gallery_dros_bj_preTf_dress:
    MC 'Get on your knees, I want those lips wrapped around my cock.'
    $ PlayMusicRandom("mus_sex")
    'Dros did as he was told, obediently dropping to his knees as my member pressed against his warm cheek.'
    'His soft, warm hands gently stroked at my cock rhythmically.'
    "Dros' hot breathe touched my cock as he breathed excitedly for what was to come."
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    scene dros_bj_dress with dissolve
    $ Pause()
    DROS "Gods..." 
    DROS "You really are blessed with a great spear, aren't you?"
    "Dros trembled slightly with excitement as he gently kissed the tip with his warm, soft lips."
    DROS 'W-Would you perhaps, um... {i}Be a little mean to me please?{/i}'
    'I raised a curious eyebrow.'
    DROS 'H-Hey...'
    DROS 'It turns me on.'
    MC '...Are you still talking? You should be worshipping my cock slut.'
    DROS 'A-Ah! Yes, [dros_player_ref!t].'
    "Dros' lips wrapped around my cock as he began to gently bop his head forward and back."
    'His hot warm mouth tenderly wrapped around me as his wet tongue wrapped around my cock.'
    MC "Ahhh... That's it."
    MC "Good little elvish slut."
    DROS '{i}*Slurp!*{/i} Mmfghh...! {i}*Slurp!*{/i}'
    'Dros continued to coo and moan softly as his head glided back and forth over my cock.'
    'His lips struggled to wrapped around the thick member, but as his eyes looked into mine I could see the desperation to please me.'
    DROS 'Mmmfghh...!'
    MC 'Ahh! This is all you elven bitches are good for, draining balls dry and taking cock!'
    MC "But I'm sure you knew that already, right?"
    "Dros' hard cock twitched with excitement as he threw his head forward desperately."
    'As his warm mouth coated my cock in saliva, I began to feel myself struggling to hold back.'
    "The intense, hot sensation of Dros' lips as he sucked my cock as though his life depended on it, was driving me wild."
    DROS 'Mmm!! {i}*Slurp!*{/i}'
    'Dros must have sensed it too, because he began to slide his mouth deeper, taking as much of my cock as he could down into his throat.'
    MC 'G-Grghh! You little elvish w-whore!'
    MC "I'm so close!"
    DROS 'Mmmfghhh!!'
    'Finally, I could take no more of his tender, loving mouth.'
    MC "I'm going to cum!"
    if GalFlag("dros","bj",["var_pretf_dress_fin_in","var_pretf_dress_fin_out"]):
        "Did I..."
        menu:
            'Make him swallow it?':
                $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
                scene dros_bj_dress_finish_in with flash
                $ Pause()
                'Unable to hold back anymore, I released my hot seed down his throat.'
                'Dros let out some hot moans as he desperately tried to swallow down every drop of my overflowing load.'
                DROS 'Mmmfghh...!!'
                MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
                "Pulling my cock out of his mouth, Dros' cheeks puffed out as he gulped and swallowed down the last of my load and presented his open empty mouth to me." 
                DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
            'Cover his face?':
                $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
                scene dros_bj_dress_finish_out with flash
                $ Pause()
                "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
                "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
                DROS '(G-Gods... Does he ever stop cumming?)'
                MC "{i}*Huff*{/i} Oh fuck..."
                MC "You drained me dry!"
    elif GalFlag("dros","bj","var_pretf_dress_fin_in"):
        $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
        scene dros_bj_dress_finish_in with flash
        $ Pause()
        'Unable to hold back anymore, I released my hot seed down his throat.'
        'Dros let out some hot moans as he desperately tried to swallow down every drop of my overflowing load.'
        DROS 'Mmmfghh...!!'
        MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
        "Pulling my cock out of his mouth, Dros' cheeks puffed out as he gulped and swallowed down the last of my load and presented his open empty mouth to me." 
        DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
    elif GalFlag("dros","bj","var_pretf_dress_fin_out"):
        $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
        scene dros_bj_dress_finish_out with flash
        $ Pause()
        "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
        "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
        DROS '(G-Gods... Does he ever stop cumming?)'
        MC "{i}*Huff*{/i} Oh fuck..."
        MC "You drained me dry!"
    "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
    "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
    DROS '(G-Gods... Does he ever stop cumming?)'
    MC "{i}*Huff*{/i} Oh fuck..."
    MC "You drained me dry!"
    return

label gallery_dros_bj_postTf_naked:
    MC 'Get on your knees, I want those lips wrapped around my cock.'
    $ PlayMusicRandom("mus_sex")
    'Draya did as she was told, obediently dropping to her knees as my member pressed against her warm cheek.'
    'Her soft, warm hands gently stroked at my cock rhythmically.'
    "Draya's hot breathe touched my cock as she breathed excitedly for what was to come."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    scene draya_bj_naked with dissolve
    $ Pause()
    DROS "Gods..." 
    'Draya began.'
    DROS "You really was blessed with a great spear, weren't you?"
    "Draya trembled slightly with excitement as the gently kissed the tip with her warm, soft lips."
    DROS 'W-Would you perhaps, um... {i}Be a little mean to me please?{/i}'
    'I raised a curious eyebrow.'
    DROS 'H-Hey...'
    DROS 'It turns me on.'
    MC '...Are you still talking? You should be worshipping my cock slut.'
    DROS 'A-Ah! Yes, [dros_player_ref!t].'
    "Draya's lips wrapped around my cock as she began to gently bop her head forward and back."
    'Her hot warm mouth tenderly wrapped around me as her wet tongue wrapped around my cock.'
    MC "Ahhh... That's it."
    MC "Good little elvish slut."
    DROS '{i}*Slurp!*{/i} Mmfghh...! {i}*Slurp!*{/i}'
    'Draya continued to coo and moan softly as her head glided back and forth over my cock.'
    'Her lips struggled to wrapped around the thick member, but as her eyes looked into mine I could see the desperation to please me.'
    DROS 'Mmmfghh...!'
    MC 'Ahh! This is all you elven bitches are good for, draining balls dry and taking cock!'
    MC "But I'm sure you knew that already, right?"
    "Draya's hard cock twitched with excitement as she threw her head forward desperately."
    'As her warm mouth coated my cock in saliva, I began to feel myself struggling to hold back.'
    "The intense, hot sensation of Draya's lips as she sucked my cock as though her life depended on her, was driving me wild."
    DROS 'Mmm!! {i}*Slurp!*{/i}'
    'Draya must have sensed it too, because she began to slide her mouth deeper, taking as much of my cock as she could down into her throat.'
    MC 'G-Grghh! You little elvish w-whore!'
    MC "I'm so close!"
    DROS 'Mmmfghhh!!'
    'Finally, I could take no more of their tender, loving mouth.'
    MC "I'm going to cum!"
    if GalFlag("dros","bj",["var_posttf_naked_fin_in","var_posttf_naked_fin_out"]):
        "Did I..."
        menu:
            'Make them swallow it?':
                $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
                scene draya_bj_naked_finish_in with flash
                $ Pause()
                'Unable to hold back anymore, I released my hot seed down their throat.'
                'Draya let out some hot moans as she desperately tried to swallow down every drop of my overflowing load.'
                DROS 'Mmmfghh...!!'
                MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
                "Pulling my cock out of her mouth, Draya's cheeks puffed out as she gulped and swallowed down the last of my load and presented her open empty mouth to me." 
                DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
            'Cover them?':
                $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
                scene draya_bj_naked_finish_out with flash
                $ Pause()
                "Pulling my cock out of her mouth, I grunted loudly as I glazed Draya's face and tits in my load." 
                "Draya opened her mouth as I came, catching what she could onto her tongue as the rest dripped down off from her."
                DROS '(G-Gods... Does he ever stop cumming?)'
                MC "{i}*Huff*{/i} Oh fuck..."
                MC "You drained me dry!"
    elif GalFlag("dros","bj","var_posttf_naked_fin_in"):
        $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
        scene draya_bj_naked_finish_in with flash
        $ Pause()
        'Unable to hold back anymore, I released my hot seed down their throat.'
        'Draya let out some hot moans as she desperately tried to swallow down every drop of my overflowing load.'
        DROS 'Mmmfghh...!!'
        MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
        "Pulling my cock out of her mouth, Draya's cheeks puffed out as she gulped and swallowed down the last of my load and presented her open empty mouth to me." 
        DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
    elif GalFlag("dros","bj","var_posttf_naked_fin_out"):
        $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
        scene draya_bj_naked_finish_out with flash
        $ Pause()
        "Pulling my cock out of her mouth, I grunted loudly as I glazed Draya's face and tits in my load." 
        "Draya opened her mouth as I came, catching what she could onto her tongue as the rest dripped down off from her."
        DROS '(G-Gods... Does he ever stop cumming?)'
        MC "{i}*Huff*{/i} Oh fuck..."
        MC "You drained me dry!"
    return
label gallery_dros_bj_postTf_dress:
    MC 'Get on your knees, I want those lips wrapped around my cock.'
    $ PlayMusicRandom("mus_sex")
    'Draya did as she was told, obediently dropping to her knees as my member pressed against her warm cheek.'
    'Her soft, warm hands gently stroked at my cock rhythmically.'
    "Draya's hot breathe touched my cock as she breathed excitedly for what was to come."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    scene draya_bj_dress with dissolve
    $ Pause()
    DROS "Gods..." 
    'Draya began.'
    DROS "You really was blessed with a great spear, weren't you?"
    "Draya trembled slightly with excitement as the gently kissed the tip with her warm, soft lips."
    DROS 'W-Would you perhaps, um... {i}Be a little mean to me please?{/i}'
    'I raised a curious eyebrow.'
    DROS 'H-Hey...'
    DROS 'It turns me on.'
    MC '...Are you still talking? You should be worshipping my cock slut.'
    DROS 'A-Ah! Yes, [dros_player_ref!t].'
    "Draya's lips wrapped around my cock as she began to gently bop her head forward and back."
    'Her hot warm mouth tenderly wrapped around me as her wet tongue wrapped around my cock.'
    MC "Ahhh... That's it."
    MC "Good little elvish slut."
    DROS '{i}*Slurp!*{/i} Mmfghh...! {i}*Slurp!*{/i}'
    'Draya continued to coo and moan softly as her head glided back and forth over my cock.'
    'Her lips struggled to wrapped around the thick member, but as her eyes looked into mine I could see the desperation to please me.'
    DROS 'Mmmfghh...!'
    MC 'Ahh! This is all you elven bitches are good for, draining balls dry and taking cock!'
    MC "But I'm sure you knew that already, right?"
    "Draya's hard cock twitched with excitement as she threw her head forward desperately."
    'As her warm mouth coated my cock in saliva, I began to feel myself struggling to hold back.'
    "The intense, hot sensation of Draya's lips as she sucked my cock as though her life depended on her, was driving me wild."
    DROS 'Mmm!! {i}*Slurp!*{/i}'
    'Draya must have sensed it too, because she began to slide her mouth deeper, taking as much of my cock as she could down into her throat.'
    MC 'G-Grghh! You little elvish w-whore!'
    MC "I'm so close!"
    DROS 'Mmmfghhh!!'
    'Finally, I could take no more of their tender, loving mouth.'
    MC "I'm going to cum!"
    if GalFlag("dros","bj",["var_posttf_dress_fin_in","var_posttf_dress_fin_out"]):
        "Did I..."
        menu:
            'Make them swallow it?':
                $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
                scene draya_bj_dress_finish_in with flash
                $ Pause()
                'Unable to hold back anymore, I released my hot seed down their throat.'
                'Draya let out some hot moans as she desperately tried to swallow down every drop of my overflowing load.'
                DROS 'Mmmfghh...!!'
                MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
                "Pulling my cock out of her mouth, Draya's cheeks puffed out as she gulped and swallowed down the last of my load and presented her open empty mouth to me." 
                DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
            'Cover them?':
                $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
                scene draya_bj_dress_finish_out with flash
                $ Pause()
                "Pulling my cock out of her mouth, I grunted loudly as I glazed Draya's face and tits in my load." 
                "Draya opened her mouth as I came, catching what she could onto her tongue as the rest dripped down off from her."
                DROS '(G-Gods... Does he ever stop cumming?)'
                MC "{i}*Huff*{/i} Oh fuck..."
                MC "You drained me dry!"
    if GalFlag("dros","bj","var_posttf_dress_fin_in"):
        $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
        scene draya_bj_dress_finish_in with flash
        $ Pause()
        'Unable to hold back anymore, I released my hot seed down their throat.'
        'Draya let out some hot moans as she desperately tried to swallow down every drop of my overflowing load.'
        DROS 'Mmmfghh...!!'
        MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
        "Pulling my cock out of her mouth, Draya's cheeks puffed out as she gulped and swallowed down the last of my load and presented her open empty mouth to me." 
        DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
    if GalFlag("dros","bj","var_posttf_dress_fin_out"):
        $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
        scene draya_bj_dress_finish_out with flash
        $ Pause()
        "Pulling my cock out of her mouth, I grunted loudly as I glazed Draya's face and tits in my load." 
        "Draya opened her mouth as I came, catching what she could onto her tongue as the rest dripped down off from her."
        DROS '(G-Gods... Does he ever stop cumming?)'
        MC "{i}*Huff*{/i} Oh fuck..."
        MC "You drained me dry!"
    return