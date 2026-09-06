label rom_Ves_61_PostDrunk:
    'The next morning I awoke to the unsettling feeling of Ves towering over me, blocking out the diminishing sunlight that had managed to break its way through the fabric of the tent.'
    $ LocFlush()
    show mc:
        xcenter 0.15
    show ves:
        xcenter 0.6
        xzoom -1.0
    with dissolve
    MC @talk 'Mm? Ves?'
    VES @talk '... We have unfinished business.'
    'Half drowsy and barely awake, I rubbed my eyes and sat up yawning.'
    MC @talk 'We do?'
    VES @talk 'Yes...'
    VES @talk 'It has bothered me for some time now.'
    MC @talk 'What has?'
    VES @talk 'I have not brought you to finish.'
    MC @talk 'Huh? What are you talking about?'
    VES @talk '{i}I did not{/i} bring you to finish.'
    MC @talk 'You have not—'
    'My eyes widened as I realised what she was saying.'
    MC @talk 'Oh... OH!'
    VES @talk 'I am not ready to... go further with you yet, but...'
    VES @talk 'I... have heard from some of the other orcs about an act that male orcs sometimes request that their mates do...'
    VES @talk 'Involving their breasts.'
    'Ves prompted me to once again strip down naked. Now standing confidently in front of me as my eyes revelled in the strength of her body, already hard and throbbing I stared at her round tits and pussy nestled beneath the thick black bush.'
    MC @smile 'Y-Yeah... It’s true alright!'
    'Crouching down, Ves proceeded to wrestle with me and pull off my clothes, smiling as she pulled out my member with both of her hands.'
    VES @smile_talk 'I... haven’t done this before...'
    'With a determined look, Ves seemed to take this as some kind of ‘warrior’s challenge’, proudly declaring...'
    VES @talk 'But I will make sure this is good for you!'
    hide mc
    hide ves
    with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    scene ves_titjob_naked_slow with dissolve
    $ Pause()
    'Ves wrapped her soft, ample breasts around my cock, shyly looking for approval as she began to massage my cock between her tits.'
    'Grunting in approval, Ves smiled as she pressed her breasts together, enveloping my cock as she began to move up and down, softly massaging me.'
    'Ves continued happily for a while, her eyes looking up to me inquisitively for any approving grunts and moans.'
    'Each time I showed my pleasure, she made sure to double down on whatever she was doing.'
    VES 'Hearing you moan like this is...'
    VES '... {i}Making me more excited.{/i}'
    MC 'Ves, you’re... Ahhhh.'
    VES 'That’s right... Moan more for me.'
    VES 'Tell me you like it.'
    MC 'Mmm, I like it, Ves... I like it alright! I like it a lot!'
    VES 'This is {i}*huff*{/i} quite the workout!'
    MC 'Mmm... Yeah just...'
    MC 'Ahh...'
    scene ves_titjob_naked_finish with flash
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg",0)
    $ Pause()
    $ UnlockGalSceneAndGrantXp("ves","tj")
    $ UnlockGalFlag("ves","tj","var_naked")
    VES '{i}*Gulp*{/i}'
    VES  '{i}*Huff* *Cough!* *Cough!*{/i}'
    MC  'Ves, are you alright?'
    VES  'Urgh... Yes.'
    VES 'I guess I can skip my next meal now...'
    $ ReduceInfectionFromSex("ves")
    $ AutoMus(True)
    $ LocFlush()
    with dissolve
    show mc:
        xcenter 0.15
    show ves:
        xcenter 0.55
        xzoom -1.0
    with dissolve
    MC @smile '...'
    VES @talk '... Stop grinning and just get me something to wipe my face.'
    'Ves pouted, grumbling beneath her breath.'
    VES @talk '{i}You better not have gotten anything in my hair...{/i}'
    #BOTH ROUTES CONTINUED
    VES @smile_talk 'That was... {i}fun.{/i}'
    $ CharChangeRel("ves", 1)
    MC @smile 'That’s one word for it.'
    VES @talk 'You can think of another?'
    MC @talk 'I can think of a few words, but they all involve us not leaving your tent today.'
    'Ves smiled, her cheeks once again flushed a shade of pink as she averted her gaze.'
    VES @talk 'That sounds nice...'
    VES @talk 'But... {i}another time.{/i}'
    MC @talk 'Yes, ma’am.'
    $ CharSetClothes("ves", "normal")
    show ves at nod
    VES @talk 'I have to go scavenge for a while... Come back later if you want some food or...'
    VES @talk 'Uhh, maybe some more... fun.'
    MC @talk 'You don’t have to tell me twice!'
    hide ves with dissolve
    MC '(Hmm... I wonder if I could buy Ves a gift somewhere?)'
    MC '(Maybe some new clothes?)'
    $ NoteUnlock("VesLingerie")
    #New quest: I should find Ves some clothes... But what?
    $ DialogueVes().outHunting = True
    $ QstSetProgress(RomanceVes, 12)
    hide mc with dissolve
    $ CharSetClothes("mc", "normal")
    $ LocSet("ves_camp")
    $ TimeAdvBy(TIME_05H)
    $ LocEnter()
