label ev_Markus_tavern_postTwoEmps_2:
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    show mc:
        xcenter 0.5
    with dissolve
    MC '(Where did they go?)'
    MC '(...There!)'
    'The robed figure was stood wand watching me at the entrance to some Alleyway.'
    hide mc with easeoutright
    'When I saw them, and made my way towards them, they turned and ran.'
    'As I gave chase, the robed figure was clambering her way up onto the many low rooftops of Novaras.'
    scene black with dissolve
    MC "(She's fast!)"
    BLACK '({i}We are faster{/i}.)'
    'Giving chase, I clambered up onto the rooftops behind them.'
    'Thanks to the changes to my body, I could leap higher than I ever could before, and quickly, I sprinted along the moonlit stone rooftops after the elusive figure.'
    'The figure glanced over their shoulder to know I was still giving chase, and as we leapt from rooftop to rooftop, ever rising higher above the city, finally, the figure reached a dead end and was cornered.'
    scene cg_rooftops
    show mc:
        xcenter 0.5
    with dissolve
    MC @angry "Show yourself! Whoever you are!"
    $ AutoMus(False)
    $ PlayMusic("audio/music/37_Rooftops.ogg")
    UNKNOWN @talk "Is that any way to greet an old friend?"
    'That voice... So indistinguishable.'
    show mc at blurin:
        xzoom -1.0
    "...But it couldn't be."
    show mc with easeoutright:
        xcenter 0.7
    'As she pulled back the hood and lowered the mask, I stared in disbelief.'
    $ CharSetClothes("kiara", "normal")
    $ CharSetVar("kiara", "default_look", "hooded")
    $ CharSetPortrait("kiara", "images/characters/kiara/portrait_hooded.webp")
    show kiara at cleft with easeinleft
    MC @talk "{i}...Kiara?{/i}"
    $ CharUnKill("kiara")
    if CharGetVar("kiara", "romanced") == True:
        $ CharAddRelEntry("kiara", "revive_romance")
        jump ev_Markus_tavern_postTwoEmps_kiaraReunion
    else:
        $ CharAddRelEntry("kiara", "revive_no_romance")
        jump ev_Markus_tavern_postTwoEmps_kiaraMessage

label ev_Markus_tavern_postTwoEmps_kiaraReunion:
    "As tears welled up in Kiara's eyes, the moonlight lit up her face beautifully."
    KIARA @happy "{i}...I've fucking missed you so much.{/i}"
    'Kiara leapt forward, her lips pressed against mine as she hugged me tight.'
    hide mc
    hide kiara
    with dissolve
    show cg_kiara_hug with dissolve:
        xcenter 0.5
        xzoom -1.0
    #play sound "audio/cfx/dark_chime.ogg"
    $ Pause()
    'When she pulled herself away, she wiped her tearful eyes as she laughed.'
    hide cg_kiara_hug with dissolve
    show mc at cright_f
    show kiara at cleft
    with dissolve
    MC @surprised "Kiara... You're... {i}You're alive!{/i}"
    KIARA "Looks like it, don't it?"
    MC @talk "I don't understand, you... The battle... You were-"
    KIARA "Believe me, I'm just as surprised as you are that I'm here now."
    MC @surprised "What happened to you?"
    KIARA "It's... A long story."
    KIARA "I'll explain everything soon, okay?"
    KIARA "But first..."
    'Kiara stripped down her clothes till she was stood naked before me.'
    MC @surprised "K-Kiara?!"
    KIARA "...Well don't just stand there!"
    KIARA "Take your bloody clothes off as well already!"
    menu:
        '{image=[ICON.HEART]} Take off your clothes!':
            pass
        'Hold on a minute!':
            MC @talk "Wait a minute, Kiara, we need to talk about this!"
            KIARA @angry "...Urghhh... Really?"
            KIARA @angry "Do you have any idea how much I've been wanting a good shag?"
            KIARA "Not to mention how fucking gorgeous you've become since we last met!"
            'Kiara moved forward enticingly once again before I stopped her.'
            MC @talk "Kiara... {i}Why are you here?{/i}"
            KIARA @sad "...Damn it, [player_name!t]."
            KIARA @sad "Why we gotta cut straight to business and miss out all the fun?"
            KIARA @sad "{i}*Sigh*{/i}"
            KIARA "Fine... Listen well, [player_name!t]."
            jump ev_Markus_tavern_postTwoEmps_kiaraMessage

    MC "(...Fuck it!)"
    "Stripping down my clothes, Kiara leapt onto me and giggled as the two of us passionately kissed once again."
    scene black with dissolve
    "Squeezing her soft little ass, I gently dropped her down onto the floor and rested on top of her."
    "Kiara breathed heavily as she hungrily looked down at my new muscular frame and the now larger than she remembered dangling appendage between her legs."
    $ PlayMusicRandom("mus_sex")
    scene kiara_rooftop_idle with dissolve
    $ Pause()
    KIARA "Oh gods... You really are different now, aren't you?"
    "After briefly running her hands down my chest, she wrapped her hands around the back of my neck."
    "There was a soft, desperate quality to her voice."
    KIARA "I haven't felt the same since that night..."
    "Gently, I rubbed my member up against her body as she let out a trembling, hot breath."
    MC "Kiara..."
    MC "I can't believe you're actually alive..."
    "Coating my cock in her wetness as I glided back and forth, she smiled softly from down below."
    KIARA "Then... {i}*huff*{/i} Show me..."
    KIARA "{i}Show me I'm still alive.{/i}"
    "Still in disbelief that she was back in my arms, I slowly pulled my cock back, aligning it against her hole."
    KIARA "T-Take me however you want. It's alright."
    KIARA "{i}I just need to feel you inside of me.{/i}"
    menu:
        "Put it in her pussy.":
            KIARA "G-Go on now..."
            KIARA "{i}Show me how you make love to them soft Southern girls.{/i}"
            scene kiara_rooftop_vag_slow with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            $ Pause()
            KIARA "A-AHH!"
            KIARA "Mmmmfghh! F-Fuck! [player_name!t]!"
            KIARA "You're - Ahh! B-Bigger than last time!"
            "Kiara clung to me as I continued to press myself in and out of her warm womanhood."
            "She squeezed me tightly, and her hot moans filed the night air as she drew me in deeper."
            "Kiara's eyes seemed to shimmer in the moonlight as her mouth hung open."
            KIARA "Did - {i}*Huff*{/i} Did you miss me love?"
            MC "Hrghh! Y-Yes..."
            MC "Of course I missed you!"
            KIARA "M-Mmfghh! Go on... {i}*Huff*{/i} It's alright now."
            KIARA "I'm back - Mmfgh! W-We can - Ah!"
            KIARA "Be t-together like we were - Mmmhh! S-Supposed to be!"
            "The pleasure was almost unbearable, the sex had been good before, but this was unlike anything I'd experienced."
            MC "Ahh! K-Kiara!"
            scene kiara_rooftop_vag_fast with dissolve
            $ Pause()
            KIARA "Can't you - Mmhm! See?"
            KIARA "{i}It's fate... The gods have - Ah! Brought us back together!{/i}"
            "I couldn't focus anymore, not on her words, not on my fears... Nothing."
            "As I pushed myself deep into Kiara's tight, welcoming body, Kiara would lean forward occasionally to snatch a kiss and giggle."
            "Soon, the two of us were drowning in... Lust? Regret? Some strange mixture of emotions not easily described but oh so intoxicating."
            KIARA "F-Finish in me."
            "Kiara said breathlessly, her body convulsing and tightening."
            KIARA "I can f-feel how close you are love."
            KIARA "L-Let's finish together, okay?"
            MC "Urghh! K-Kiara!"
            KIARA "Yes! That's it! Give it to me!"
            KIARA "Don't stop! D-Don't-"
            "Finally, I could hold back no more."
            $ UnlockGalFlag("kiara", "rooftop", "vag")
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            scene kiara_rooftop_vag_finish with flash
            $ ReduceInfectionFromSex("kiara")
            $ UnlockGalSceneAndGrantXp("kiara", "rooftop")
            $ Pause()
            "As I forced myself deeply to the hilt inside of Kiara's tight body once more, I grunted loudly as I poured my hot, thick seed deep into her."
            "Kiara in turn, upon feeling the hot rush of warmth inside of her, tightened and spasmed around me as she gasped breathlessly in climax."
        "Put it in her ass.":
            "As she felt the head of my cock press against her tight ass, she winced for a moment, letting out a soft moan as she chewed her bottom lip."
            KIARA "D-Do it..."
            KIARA "{i}Take me.{/i}"
            scene kiara_rooftop_anal_slow with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            $ Pause()
            "As she felt the head of my cock push into her tight ass, it opened and stretched to squeeze around my member as she cried out."
            KIARA "Mmmfghhh!!"
            MC "Am I hurting you?"
            KIARA "A - A little..."
            KIARA "But it's okay - Mhmm..."
            KIARA "{i}I'm stronger now... I can t-take you.{/i}"
            "I wondered for a moment what she meant by those words, but as her tightness squeezed around me, I could only focus on the pleasure as I began to move in and out of her."
            KIARA "Ahhh!!"
            KIARA "Y-Yes! Mmfghh! D-Do you feel it too?"
            KIARA "W-We're - Ahh! Meant to be together!"
            "Kiara's ass tigthly squeezed around me as I began to move faster."
            MC "Kiara... You feel - {i}*Huff*{/i} incredible!"
            KIARA "H-Harder!"
            KIARA "F-Fate has bought us back together! Mhmm!"
            KIARA "T-Take me! Take me however you fucking want!"
            "Taken over with the pleasure, I couldn't focus on anything else, reduced to a grunting animal as I had my way with her."
            scene kiara_rooftop_anal_fast with dissolve
            $ Pause()
            "Kiara would giggle and laugh between her coos and sharp moans of pleasure, leaning forward to snatch a kiss as she did her best to pull me in deeper."
            KIARA "M-My ass... Mhmm!"
            KIARA "Y-You feel so good in my ass!"
            MC "Kiara, how are you handling-"
            KIARA "Shhh, my love..."
            KIARA "{i}I've been remade so we're perfect for each other.{/i}"
            "I wanted to ask her what she meant, I wanted to ask her how she was back here with me now."
            "As she tightened and squeezed around me though, the hot seeping lust... regret... whatever we were feeling and taking out on each other, was all consuming."
            KIARA "I can f-feel you throbbing..."
            "...Kiara said breathlessly, her body convulsing and tightening."
            KIARA "F-Finish in me, {i}I want to feel your warmth inside of me.{/i}"
            MC "Urghh! K-Kiara!"
            KIARA "Yes! That's it! Give it to me!"
            KIARA "P-Pour it into me!"
            KIARA "F-Finish in my ass!"
            KIARA "Don't stop! D-Don't-"
            "Finally, I could hold back no more."
            $ UnlockGalFlag("kiara", "rooftop", "anal")
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            scene kiara_rooftop_anal_finish with flash
            $ ReduceInfectionFromSex("kiara")
            $ UnlockGalSceneAndGrantXp("kiara", "rooftop")
            $ Pause()
            "As I forced myself deeply to the hilt inside of Kiara's tight body once more, I grunted loudly as I poured my hot, thick seed deep into her."
            "Kiara in turn, upon feeling the hot rush of warmth inside of her, tightened and spasmed around me as she gasped breathlessly in climax."
    scene black with dissolve
    "The two of us laid there for a moment, breathless and spent before Kiara pressed a weak kiss onto my lips before I rolled down naked beside her."
    "Kiara rolled over, her hands resting on my chest."
    $ CharSetClothes("kiara", "naked")
    $ CharSetClothes("mc", "pants")
    $ CharChangeRel("kiara", 1)
    scene cg_rooftops
    show mc at cleft
    show kiara at cright_f
    with dissolve
    $ PlayMusic("audio/music/37_Rooftops.ogg")
    KIARA "Gods... I needed that."
    MC "Kiara, we still need to talk about-"
    KIARA "What a beautiful night..."
    KIARA "You really see all the stars up here, don't you?"
    'Kiara gently balled her hand on my chest as she looked up at the glittering sea of stars.'
    MC "...Mmm, I suppose it is a beautiful night."
    KIARA "I wish I could just lay here with you like this forever."
    MC "What does that mean? Are you not staying?"
    KIARA "I... I can't stay."
    MC "What? Kiara..."
    KIARA "...I was looking forward to seeing you so much, I kept pushing the actual {i}job{/i} part of this trip aside."
    MC 'What are you talking about, Kiara?'
    KIARA '...'
    'Reluctantly, Kiara rose up and began to re-dress herself.' #MC is half naked,  Kiara is now dressed 
    $ CharSetClothes("kiara", "normal")
    show kiara at blurin, nod
    jump ev_Markus_tavern_postTwoEmps_kiaraMessage

label ev_Markus_tavern_postTwoEmps_kiaraMessage:
    KIARA "I'm here to bring you a message from the Mistress."
    MC @talk "The... {i}Mistress?{/i}"
    KIARA "Mistress Sypha."
    KIARA "She said you two had already met."
    'I felt the blood drain from my body.'
    MC @surprised "You... {i}You're the agent?{/i}"
    KIARA @sad "I'm sorry [player_name!t], there's so much I have to tell you, but..."
    KIARA @sad "She's told me only to pass on her message."
    MC @talk "Who is she? What is the message?"
    KIARA "She is a member of {i}The Order of Xeriya'.{/i}"
    KIARA "They're..."
    'Kiara looked down briefly at the note wrote for her in some strange language I could not decipher.'
    KIARA "...A semi-autonomous sect... Whatever that means."
    KIARA "The mistress still won't explain {i}everything{/i} to me either yet, but they want to help."
    MC @talk '{i}...Help?{/i}'
    KIARA @sad "Trust me, I know it seems crazy and you have no reason to believe them."
    KIARA "But the Mistress is the reason I'm back now and she's told me stuff that's going to have your head spinning when you hear it!"
    MC @talk "Well... What does she want?"
    KIARA @sad "She... She said not to tell you yet, till you could be trusted."
    KIARA "But to prove that she's a friend and not a foe, she wanted me to tell you..."
    KIARA "{i}There are spies within Novaras waiting for the signal.{/i}"
    KIARA "{i}When the second siege begins, the attack will come from both the outside and from within.{/i}"
    MC @talk "Within? But-"
    KIARA "I'm sorry, that's all she told me to say."
    'Kiara bit her lip.'
    KIARA @sad "...I can't stay much longer; I have to go now."
    show kiara at right_f with ease
    KIARA @sad "Time is running out [player_name!t], they're coming... They're coming, and you have to be ready for them."
    KIARA @sad "You have to survive, okay?"
    KIARA @sad "You could change everything!"
    MC @sad "Kiara... What are you saying?"
    KIARA @sad "We'll see each other soon! I promise!"
    hide kiara with easeoutright
    'Kiara suddenly turned and leapt off the building as I reached out to stop her.'
    show mc with easeinleft:
        xcenter 0.65
    MC @surprised "Kiara! WAIT!"
    'As I looked over the edge to grab her, she had vanished...'
    'I took a few steps back, thinking on her words.'
    show mc with easeoutleft:
        xcenter 0.5
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    MC "(...Second siege.)"
    MC "(Oh gods... I have to do something before it's too late!)"
    $ AutoMus(True)
    $ QstComplete(EventNovarasMarkusTavernTwoEmps)
    $ LocEnter()
