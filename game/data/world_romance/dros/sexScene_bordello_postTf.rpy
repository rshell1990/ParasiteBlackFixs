label dros_postTf_payMenu:
    DROS @talk "Oh sure, I... Need to charge you for the room."
    DROS @talk "Four hundred."
    menu:
        'Here.' (Req_Gold = 400): #If coin available 
            $ PlayerRemItem("gold",400)
            'I handed over the coins.'
            DROS @talk 'Okay then.'
            jump dros_bordello_sex_postTf_root
        "I can't afford that.":
            DROS @talk 'Oh, I see...'
            DROS @talk "I'll be here."
            return


label dros_bordello_sex_postTf_root:
    DROS @lewd 'Follow me, [dros_player_ref!t].'
    scene black with dissolve
    scene bg_weeping_heart_brothel_room
    show dros at center
    with dissolve
    #Fade to black - Cut to brothel room
    DROS @smile 'Soooo...'
    DROS @lewd "Do you like my clothes?"
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
    #Any choice continued 
    DROS @lewd 'What next?'
    menu:
        'Get on your knees, I want those lips wrapped around my cock.':
            jump dros_brothel_bj_postTf
        "Get onto the bed...{i}I need you now.{/i}":
            jump dros_brothel_missionary_postTf

label dros_brothel_bj_postTf:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Draya did as she was told, obediently dropping to her knees as my member pressed against her warm cheek.'
    'Her soft, warm hands gently stroked at my cock rhythmically.'
    "Draya's hot breathe touched my cock as she breathed excitedly for what was to come."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    if CharGetClothes("dros") == "dress":
        scene draya_bj_dress
        $ UnlockGalFlag("dros","bj","var_posttf_dress")
    if CharGetClothes("dros") == "naked":
        scene draya_bj_naked
        $ UnlockGalFlag("dros","bj","var_posttf_naked")
    with dissolve
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
    menu:
        'Make them swallow it.':
            if CharGetClothes("dros") == "dress":
                scene draya_bj_dress_finish_in
                $ UnlockGalFlag("dros","bj","var_posttf_dress_fin_in")
            if CharGetClothes("dros") == "naked":
                scene draya_bj_naked_finish_in
                $ UnlockGalFlag("dros","bj","var_posttf_naked_fin_in")
            with flash
            $ PlaySexFx("audio/sex_sounds/no_voice_finish.ogg")
            $ ReduceInfectionFromSex("dros")
            'Unable to hold back anymore, I released my hot seed down their throat.'
            'Draya let out some hot moans as she desperately tried to swallow down every drop of my overflowing load.'
            DROS 'Mmmfghh...!!'
            MC '{i}*Huff*{/i} Oh fuck... {i}*Huff*{/i}'
            "Pulling my cock out of her mouth, Draya's cheeks puffed out as she gulped and swallowed down the last of my load and presented her open empty mouth to me." 
            DROS "{i}*Huff*{/i} So... {i}*Huff*{/i} much..."
        'Cover them.':
            if CharGetClothes("dros") == "dress":
                scene draya_bj_dress_finish_out
                $ UnlockGalFlag("dros","bj","var_posttf_dress_fin_out")
            if CharGetClothes("dros") == "naked":
                scene draya_bj_naked_finish_out
                $ UnlockGalFlag("dros","bj","var_posttf_naked_fin_out")
            with flash
            $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
            $ ReduceInfectionFromSex("dros")
            $ Pause()
            "Pulling my cock out of her mouth, I grunted loudly as I glazed Draya's face and tits in my load." 
            "Draya opened her mouth as I came, catching what she could onto her tongue as the rest dripped down off from her."
            DROS '(G-Gods... Does he ever stop cumming?)'
            MC "{i}*Huff*{/i} Oh fuck..."
            MC "You drained me dry!"
    $ UnlockGalSceneAndGrantXp("dros","bj")
    scene black with dissolve
    jump dros_bordello_sex_postTf_aftersex

label dros_brothel_missionary_postTf:
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Draya blushed at the comment, but she quickly did as she was told and crawled over onto the bed.'
    'Laying on her back, she spread her legs as she waited for me to join her.'
    DROS "I'm... {i}I'm ready.{/i}"
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg",1)
    if CharGetClothes("dros") == "dress":
        scene draya_miss_dress
    if CharGetClothes("dros") == "naked":
        scene draya_miss_naked
    with dissolve
    $ Pause()
    'As my cock prodded against the tight rosebud hole she had lubed in preparation for me, her chest rose and dropped in excitement.'
    DROS "Gods... You're so-"
    'Her asshole spread and widened as it swallowed my cock.'
    DROS 'BIGGGG!'
    'Draya flushed red from arousal as I began to thrust into their tight, warm ass.'
    'Inch by inch her butt swallowed me as she squeezed me tightly.'
    DROS 'F-Fuck...!'
    DROS "Fuck me! You f-feel i-incredibleee!"
    MC 'Ah! Your ass feels so tight!'
    'Draya briefly flashed a smile as her eyes watered slightly.'
    DROS 'E-Elvish ass is always tighter!'
    "Whether that was true or not didn't matter, what did matter was the sensation right now was extraordinary."
    "Soon, the two of us were dripping with sweat as her body welcomed me greedily, swallowing every inch as she tried to milk me dry."
    'Draya went wild as her body seemed to squeeze and release around me.'
    DROS '{i}F-Fuck me! Make me your elvish bitch!{/i}'
    DROS 'C-Cum! Please! I NEED to m-make you cum!'
    'The incredible intoxicating feeling was too much, and soon, my balls were rising as I could hold on no longer.'
    MC "Grghh! I'm cumming you little whore!"
    DROS "Oh fuck yes, [dros_player_ref!t]! I'm cumming too! I'm cumming so hard!"
    if CharGetClothes("dros") == "dress":
        $ UnlockGalFlag("dros","miss","var_posttf_dress")
        scene draya_miss_dress_finish
    if CharGetClothes("dros") == "naked":
        $ UnlockGalFlag("dros","miss","var_posttf_naked")
        scene draya_miss_naked_finish
    with flash
    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ ReduceInfectionFromSex("dros")
    $ UnlockGalSceneAndGrantXp("dros","miss")
    $ Pause()
    'Bottoming out into her, I grunted as I pumped her ass full of my seed.'
    DROS '{i}*Gasp!*{/i}'
    'Draya whimpered as her mouth hung open, feeling the seed pour into her.'
    DROS 'S-Soo... {i}much...{/i}'
    MC '{i}*Huff*{/i} Are you okay?'
    'Draya giggled weakly.'
    DROS 'S-Soo... full... and...'
    DROS "{i}Good.{/i}"
    MC '{i}*Huff*{/i} Your tight ass drained me dry.'
    DROS "(My legs feel so weak, gods only know if I'll be able to walk home after that monster!)"
    scene black with dissolve
    jump dros_bordello_sex_postTf_aftersex

label dros_bordello_sex_postTf_aftersex:
    $ AutoMus(True)
    $ CharSetClothes("dros", "dress")
    scene bg_weeping_heart_brothel_room
    show dros at center
    with dissolve
    DROS @lewd 'That was amazing!'
    DROS @smile 'You have no idea how much I needed that, [dros_player_ref!t].'
    DROS @lewd "(Gods, I'm shaking!)"
    'Draya leaned forward to kiss me and I squeezed her soft ass.'
    DROS @lewd 'U-Until next time!'
    $ CharChangeRel("dros", 1)
    $ LocNameReset()
    $ LocEnter()