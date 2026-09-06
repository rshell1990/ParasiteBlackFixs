label dros_preTf_payMenu:
    DROS @talk "Oh sure, I... Need to charge you for the room."
    DROS @talk "Madam's rules still apply even though I'm paying for the room myself."
    DROS @talk "Four hundred."
    menu:
        'Here.' (Req_Gold = 400): #If coin available 
            $ PlayerRemItem("gold",400)
            'I handed over the coins.'
            DROS @smile 'Okay then.'
            jump dros_bordello_sex_preTf_root
        "I can't afford that.":
            DROS @sad 'Oh, I see...'
            DROS @talk "I'll be here."
            return

label dros_bordello_sex_preTf_root:
    DROS @lewd 'Follow me, [dros_player_ref!t].'
    scene black with dissolve
    #Fade to black - Cut to brothel room
    DROS @smile 'Soooo...'
    scene bg_weeping_heart_brothel_room
    $ CharSetClothes("dros", "dress")
    $ LocNameSetTemp(_("Brothel Room"))
    show dros at center
    with dissolve
    DROS @talk "Do you like my clothes?"
    menu:
        'Keep your clothes as is.':
            DROS @smile  "Whatever turns you on more..."
            pass
        'Undress.':
            DROS @shock 'Oooh...!'
            DROS @lewd 'As you wish, [dros_player_ref!t].'
            $ CharSetClothes("dros", "naked")
            show dros at nod
            DROS @lewd 'Better?'
            MC "Indeed."
    DROS @talk 'What next?'
    menu:
        'Get on your knees, I want those lips wrapped around my cock.':
            jump dros_brothel_bj_preTf
        "Get onto the bed...{i}I need you now.{/i}":
            jump dros_brothel_missionary_preTf

label dros_brothel_bj_preTf:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Dros did as he was told, obediently dropping to his knees as my member pressed against his warm cheek.'
    'His soft, warm hands gently stroked at my cock rhythmically.'
    "Dros' hot breathe touched my cock as he breathed excitedly for what was to come."
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    if CharGetClothes("dros") == "dress":
        scene dros_bj_dress
        $ UnlockGalFlag("dros","bj","var_pretf_dress")
    if CharGetClothes("dros") == "naked":
        scene dros_bj_naked
        $ UnlockGalFlag("dros","bj","var_pretf_naked")
    with dissolve
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
    menu:
        'Make him swallow it.':
            if CharGetClothes("dros") == "dress":
                scene dros_bj_dress_finish_in
                $ UnlockGalFlag("dros","bj","var_pretf_dress_fin_in")
            if CharGetClothes("dros") == "naked":
                scene dros_bj_naked_finish_in
                $ UnlockGalFlag("dros","bj","var_pretf_naked_fin_in")
            with flash
            $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
            $ ReduceInfectionFromSex("dros")
            $ Pause()
            'Unable to hold back anymore, I released my hot seed down his throat.'
            'Dros let out some hot moans as he desperately tried to swallow down every drop of my overflowing load.'
            DROS 'Mmmfghh...!!'
            MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
            "Pulling my cock out of his mouth, Dros' cheeks puffed out as he gulped and swallowed down the last of my load and presented his open empty mouth to me." 
            DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
        'Cover his face.':
            if CharGetClothes("dros") == "dress":
                scene dros_bj_dress_finish_out
                $ UnlockGalFlag("dros","bj","var_pretf_dress_fin_out")
            if CharGetClothes("dros") == "naked":
                scene dros_bj_naked_finish_out
                $ UnlockGalFlag("dros","bj","var_pretf_naked_fin_out")
            with flash
            $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
            $ ReduceInfectionFromSex("dros")
            $ Pause()
            "Pulling my cock out of his mouth, I grunted loudly as I glazed Dros' face with my load." 
            "Dros opened his mouth as I came, catching what he could onto his tongue as the rest dripped down off from him."
            DROS '(G-Gods... Does he ever stop cumming?)'
            MC "{i}*Huff*{/i} Oh fuck..."
            MC "You drained me dry!"
    $ UnlockGalSceneAndGrantXp("dros","bj")
    scene black with dissolve
    $ AutoMus(True)
    if DrosInBordello().bordelloFirstFuck:
        jump dros_preTf_firstSex
    else:
        jump dros_brothel_aftersex_preTf

label dros_brothel_missionary_preTf:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Dros blushed at the comment, but he quickly did as he was told and crawled over onto the bed.'
    'Laying on his back, he spread his legs as he waited for me to join him.'
    DROS "I'm... {i}I'm ready.{/i}"
    $ PlaySexFx("audio/sex_sounds/no_voice.ogg",1)
    if CharGetClothes("dros") == "dress":
        scene dros_miss_dress
    if CharGetClothes("dros") == "naked":
        scene dros_miss_naked
    with dissolve
    $ Pause()
    'As my cock prodded against the tight rosebud hole he had lubed in preparation for me, his chest rose and dropped in excitement.'
    DROS "Gods... You're so-"
    'His asshole spread and widened as it swallowed my cock.'
    DROS 'BIGGGG!'
    'Dros flushed red from arousal as I began to thrust into his tight, warm ass.'
    'Inch by inch his butt swallowed me as he squeezed me tightly.'
    DROS 'F-Fuck...!'
    DROS "Fuck me! You f-feel i-incredibleee!"
    MC 'Ah! Your ass feels so tight!'
    'Dros briefly flashed a smile as his eyes watered slightly.'
    DROS 'E-Elvish ass is always tighter!'
    "Whether that was true or not didn't matter, what did matter was the sensation right now was extraordinary."
    "Soon, the two of us were dripping with sweat as his body welcomed me greedily, swallowing every inch as he tried to milk me dry."
    'Dros went wild as his body seemed to squeeze and release around me.'
    DROS '{i}F-Fuck me! Make me your elvish bitch!{/i}'
    DROS 'C-Cum! Please! I NEED to m-make you cum!'
    'The incredible intoxicating feeling was too much, and soon, my balls were rising as I could hold on no longer.'
    MC "Grghh! I'm cumming you little whore!"
    DROS "Oh fuck yes, [dros_player_ref!t]! I'm cumming too! I'm cumming so hard!"
    if CharGetClothes("dros") == "dress":
        $ UnlockGalFlag("dros","miss","var_pretf_dress")
        scene dros_miss_dress_finish
    if CharGetClothes("dros") == "naked":
        $ UnlockGalFlag("dros","miss","var_pretf_naked")
        scene dros_miss_naked_finish
    with flash
    $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
    $ ReduceInfectionFromSex("dros")
    $ UnlockGalSceneAndGrantXp("dros","miss")
    $ Pause()
    'Bottoming out into him, I grunted as I pumped his ass full of my seed.'
    DROS '{i}*Gasp!*{/i}'
    'Dros whimpered as his mouth hung open, feeling the seed pour into him.'
    DROS 'S-Soo... {i}much...{/i}'
    MC '{i}*Huff*{/i} Are you okay?'
    'Dros giggled weakly.'
    DROS 'S-Soo... full... and...'
    DROS "{i}Good.{/i}"
    MC '{i}*Huff*{/i} Your tight ass drained me dry.'
    DROS "(My legs feel so weak, gods only know if I'll be able to walk home after that monster!)"
    scene black with dissolve
    $ AutoMus(True)
    if DrosInBordello().bordelloFirstFuck:
        jump dros_preTf_firstSex
    else:
        jump dros_brothel_aftersex_preTf

label dros_brothel_aftersex_preTf:
    $ CharSetClothes("dros", "dress")
    scene bg_weeping_heart_brothel_room
    show dros at center
    with dissolve
    DROS @smile 'That was amazing!'
    DROS @smile 'You have no idea how much I needed that.'
    DROS "(Gods, I'm shaking!)"
    'Dros leaned forward to kiss me and I squeezed his soft ass.'
    DROS @lewd 'U-Until next time!'
    $ CharChangeRel("dros", 1)
    $ LocNameReset()
    $ LocEnter()