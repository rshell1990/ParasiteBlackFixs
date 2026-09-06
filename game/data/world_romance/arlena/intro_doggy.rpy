label rom_ArlenaIntroDoggy:
    'The door opened inch by inch as Arlena’s face peeped surreptitiously through the gap.'
    'She averted her gaze as the air touched her rosy cheeks.'
    MC @talk 'Arlena? Is everything alright?'
    ARLENA 'Yes, just give me a moment...'
    $ CharSetClothes("arlena", "apron")
    show mc at cleft
    show arlena at cright_f
    with dissolve
    'She sealed the door shut for a moment before opening it fully to allow me to inspect what was on the other side.'
    'Arlena smiled, wrapped in a warm furry blanket that hung off her bare shoulders.'
    'I had to tear my eyes away from the cute little mole on her collar bone, wanting nothing more than to reach out and touch her.'
    'She had placed various candles around the room, illuminating it with a warm, soft kind of light.'
    'Placed on the floor was a small white blanket, keenly laid out with a few pieces of food she had managed to pull together in a wooden bowl.'
    'Sat beside it was a half empty bottle of wine with two glasses already poured out waiting for us.'
    ARLENA 'It isn’t much but...'
    ARLENA 'It’s all I could cobble together.'
    menu:
        'Hey, you should’ve asked me to bring something myself!':
            ARLENA 'And ruin the surprise? Please.'
            ARLENA 'You’re a guest, I didn’t want to trouble you with petty tasks after everything you’ve done for me already.'
            MC @talk 'Look at you being nice.'
        'It’ll do fine.':
            ARLENA 'Glad you think so.'
        'What’s with the blanket?':
            ARLENA 'It’s... It’s cold is all!'
    ARLENA 'Come on, let’s dig in...'
    scene black with dissolve
    'We split the food in the bowl between us and laughed over old stories as we made our way through the wine.'
    ARLENA 'Hahaha! Do you remember Viktor’s ‘Great Potato Scam’?'
    MC @talk 'Oh yes, he swore hands down he had figured out a way to grow them himself faster than all the farmers could combined.'
    MC @talk 'He was offering huge sacks of potatoes for practically nothing.'
    $ LocFlush()
    show mc at cleft
    show arlena at cright_f
    with dissolve
    'Between snorts of laughter, Arlena struggled to hold down her mouthful of wine as she reminisced.'
    ARLENA @smile 'The little shit only had the top layer be actual potatoes, beneath all that he’d just painted a load of rocks! '
    ARLENA @smile 'I still remember the mob chasing him now!'
    MC @talk 'He swore blind they were just funny shaped, hard, ‘exotic’ potatoes!'
    ARLENA 'Didn’t someone break his nose for that?'
    MC @talk 'Yes! When he caught up to him, he said something like ‘here’s something ‘exotic’ for you to try, boy!’ '
    'Arlena laughed once again as we remembered Viktor being dropped by the old farmer’s punch.'
    ARLENA 'As much of an ass he was, he was quite cute.'
    MC @talk 'Who? The old farmer?'
    ARLENA 'Noooo, Viktor of course!'
    ARLENA '{i}Dumbass.{/i}'
    MC @talk 'Oh no...'
    ARLENA 'He was! He had this little button nose!'
    MC @talk 'His voice sounded like a cat drowning.'
    ARLENA 'Well, I liked him.'
    MC @talk '... You liked Viktor?'
    ARLENA 'We went out once...'
    MC @talk 'Oh? Just the once?'
    ARLENA 'Yeah, but nothing happened or anything like that.'
    ARLENA 'Just didn’t feel right.'
    MC @talk 'How come?'
    'Arlena paused for a moment, choosing her words with care as she took a sip of her wine.'
    ARLENA 'Well...'
    ARLENA 'I had someone else on my mind at the time, so...'
    'As Arlena shyly looked away, it dawned on me exactly {i}who{/i} had been on her mind.'
    MC @talk '... Ah.'
    ARLENA 'It’s fine, it was a long time ago, my standards were extremely low.'
    ARLENA '... And you were an ass.'
    MC @talk '... But I’m likable now, huh?'
    'Arlena smiled alluringly before once again reaching to grab her wine.'
    ARLENA 'Yes...'
    ARLENA 'You are {i}tolerable{/i}.'
    MC @talk 'As are you, m’lady.'
    'I raised my drink.'
    MC @talk 'Here’s to being tolerable.'
    'Arlena playfully clinked her drink against mine, but after swigging the last of it down and reaching over for the bottle to refill it, she realised it was empty.'
    ARLENA 'Oh! We’re out of wine...'
    ARLENA 'Heh... Time flies, huh? '
    menu:
        "{image=[ICON.HEART]} Hey would you consider... 'escalating' things a little?":
            pass
        '{image=[ICON.HEART_CROSS]} Say nothing.':
            scene black with dissolve
            "Changing the subject, we spent the rest of the... date contentedly chatting about other things till finally, she waved me off into the cool night air to make my way home."
            'I couldn’t help but notice, despite the pleasantness of the evening, there was {i}a tinge of disappointment{/i} in her voice as I made my move to leave.'
            $ LocFlush()
            show mc at cleft
            show arlena at cright_f
            with dissolve
            ARLENA 'Thanks for a good time, turns out you CAN be a gentleman when you put your mind to it.'
            MC @talk "Yeah, thank you too!"
            MC @talk "I'll be going now."
            MC @talk "Take care, Arlena."
            "With a heavy heart, I left the smithy."
            $ LocSet("novaras_dist_farm")
            $ CharChangeRel("arlena", -1)
            $ QstComplete(RomanceArlena)
            $ LocEnter()

    ARLENA 'W-What do you mean?'
    MC @talk '... Well.'
    MC @talk 'It’s just, tell me if I’m reading this wrong but...'
    MC @talk 'You didn’t just invite me here tonight to reminisce about our time at school, did you?'
    'Arlena said nothing, her mouth hung slightly open as she stared wide eyed at me in waiting.'
    show mc at cleft
    with easeinleft
    'I inched towards Arlena, never breaking eye contact before placing a tender kiss onto her lips.'
    'For just a moment, Arlena hesitated, her breath hot and heavy on my face, before she sunk into the kiss and slipped her soft tongue into my mouth.'
    ARLENA '... Fuck it.'
    show arlena at nod
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Dropping the fur blanket to the floor, Arlena revealed the see-through night gown she wore beneath.'
    'It hung off her small frame, slipping over the curves of her body like silk.'
    'She took my hand and lead me over to her bed with another passionate kiss.'
    ARLENA 'Mmm...'
    ARLENA 'I’ve wanted this for a long time.'
    MC @talk 'How do you—'
    ARLENA 'Shut up and take me.'
    'She began stripping my clothes off with an animal like passion, ripping my shirt over my head and then tracing the lines of my muscles with her fingertips.'
    'As she took off my trousers, her eyes widened when she saw the size of my hardening member.'
    ARLENA 'That’s... {i}big.{/i}'
    MC @talk '... Do you—'
    ARLENA 'It’ll be fine, just start slow, okay?'
    scene arlena_doggy_slow with dissolve
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop.ogg",1)
    $ Pause()
    'Arlena spun around, grabbing and holding onto the rails of the bed while presenting me with her butt.'
    'As my hand caressed the soft flesh, I felt myself harden more than I thought possible as she pressed her head down onto the pillow in anticipation.'
    'With both hands gripping her waist, I aligned my cock against her and pushed the head into her, easing inside her slowly.'
    'With ever millimetre that I sunk into her I could feel the urge to plunge the entirety of myself in and relentlessly fuck her grow stronger and stronger.'
    'Arlena’s hands coiled around the quilts and she let out a small painful whimper as I felt her tighten around me.'
    'The parasite inside me responded like an animal, it took all my strength to not just slam away at her like some feral beast.'
    'Taking a deep breath to steady myself, I asked...'
    MC @talk 'Arlena? Are you—'
    ARLENA 'Yes, I’m fine...'
    'Slowly but surely, I pushed a few more inches into Arlena and listened out for any sign it was too much for her, I knew how much I might hurt her if I lost control.'
    'She whimpered once again and asked me to stop for a few moments while she adjusted herself.'
    'Satisfied, she told me to continue, and as I sunk deeper into her she sighed, half struggling against the size of me, half in pleasure.'
    MC @talk 'Ready?'
    'Biting her lower lip, Arlena nodded and I began to thrust in and out of her in a slow controlled rhythm, allowing myself nothing more.'
    'She soon cooed and moaned happily, and I felt her becoming wetter and wetter, allowing me to tentatively fuck her just a little harder.'
    ARLENA 'Yes... Mmmm!'
    ARLENA 'Fuck...'
    'Finally, I sunk myself fully into her, the beast inside me roared in satisfaction, urging me to let go.'
    'Arlena groaned happily, still struggling with my size but turned on enough that she didn’t move to stop me.'
    scene arlena_doggy_fast with dissolve
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop2.ogg",1)
    $ Pause()
    'I moved faster, thrusting in and out of her tight little hole.'
    'Arlena cried out for more, and soon I found myself unable to stop as the pleasure swept over me.'
    'With every thrust she’d moan a little harder, pushing back against me so that I could slam into her.'
    'I threw my weight forward, mounting her from behind, building up a ferocious speed.'
    'She felt incredible, and as the sweat rolled down from me onto the blanket, I felt her quiver and tremble beneath me as she climaxed.'
    'The walls of her pussy throbbed and pulsed around me, clinging to my cock as she squirmed beneath me in pleasure.'
    'Her mouth hung open breathlessly as she gasped for sweet air, her hands tangling in the sheets as she moaned.'
    'She writhed on the bed, exhausted but satisfied, allowing herself to collapse into her pillow.'
    'She reached behind herself, wrapping her hand around the back of my neck, pulling me down closer to her body as I pounded away at her still throbbing pussy.'
    'I knew I wouldn’t be able to last much longer.'
    MC @talk 'Arlena... I’m going to—'
    ARLENA 'Just do it! Please!'
    $ PlaySexFx("audio/sex_sounds/nijah_doggy_finish.ogg")
    scene arlena_doggy_finish with flash
    $ ReduceInfectionFromSex("arlena")
    $ UnlockGalSceneAndGrantXp("arlena","doggy")
    $ AutoMus(True)
    $ Pause()
    'Unable to hold back any longer, I pushed the length of myself as deep inside Arlena as I dared and watched as she gasped as the hot rush of my seed flooded into her.'
    'Spent, I rolled onto my side and sighed with relief.'
    'Arlena rolled over and flopped her head on my chest.'
    $ CharSetClothes("arlena", "naked")
    $ CharSetClothes("mc", "naked")
    $ LocFlush()
    show mc at cleft
    show arlena at cright_f
    with dissolve
    ARLENA 'That was...'
    MC @talk 'Not bad, huh?'
    ARLENA 'Not too bad at all.'
    ARLENA 'I’ve got to try walk around after this and hope Father doesn’t notice you know!'
    MC @talk 'Haha! Sorry, I’ll try being more gentle next time.'
    'Arlena gave me an exaggerated pout.'
    ARLENA 'I didn’t say that...'
    'We both sat in silence for a moment before Arlena rolled over to grab a small vial of {i}‘Red Moon’{/i}, known for its anti-pregnancy properties.'
    ARLENA '... What?'
    ARLENA 'Can’t have your little ones running around the place now, can I?'
    BLACK "{b}USELESS{/b}"
    "Ouch!"
    'I re-focused, trying to ignore a gnawing mixture of dissapointment and anger the {i}thing{/i} within me stirred.'
    MC @talk 'No, of course.'
    ARLENA 'Besides, {i}you’re an Adventurer{/i} now, remember?'
    ARLENA 'Let’s not kid ourselves, you’re not going to just stay with me so...'
    ARLENA 'It’s better this way.'
    'I nodded, only half convinced.'
    ARLENA 'Anyway, you better get out of here.'
    ARLENA 'If father catches us two together, hell...'
    ARLENA 'If he knew half of what I got up to, he’d flip his lid.'
    'Getting dressed, Arlena soon saw me out the smithy.'
    "Waving me off, she reminding me to come back for ‘more work’ soon..."
    hide mc
    hide arlena
    with dissolve
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("arlena", "normal")
    $ LocSet("novaras_dist_farm")
    return
