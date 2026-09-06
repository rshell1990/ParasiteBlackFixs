
label qst_Terminus_ArriveToAdaraTavern:
    $ TimeAdvBy(TIME_1H)
    show mcprologue at cleft with easeinleft
    'As I slouched my way into the tavern, a tipsy Adara, holding a bottle of wine in her hand, leapt up to wrap her arms around me.'
    $ CharSetVar("adara", "blush", True)
    show adara at center_f with easeinright
    ADARA @talk 'YOU CAME!!'
    MC 'H-Hey... Yeah, I came.'
    'Adara, leaned back somewhat unsteadily, her face flushed endearingly red from the drink as she giggled.'
    show adara at cright_f with easeoutright
    ADARA @talk'Don’t mind me! Just a little tipsy!'
    'I did my best to feign a smile, it was nice to see her have such a good time.'
    MC '... Well, what job did you get?'
    ADARA @talk 'Well, you won’t believe it but...'
    ADARA @talk 'I’m going to work as part of the Economic Administration Division!'
    MC '... No way.'
    ADARA @smile 'Which means...'
    ADARA @talk 'I also have to manage the {i}royal{/i} budget! Soooo...'
    ADARA @talk '{i}I also get to spend some time at the palace!{/i} Isn’t that cool?'
    ADARA @talk 'We could totally run into each other as we’re going about our business there!'
    MC @sad '...'
    'Adara must have noticed my smile crack as the painful truth of the situation slowly swept over me.'
    ADARA @talk '... [player_name!t]? What’s wrong?'
    ADARA @talk 'You {i}did{/i} get in, right?'
    MC '... Y-Yeah, of course I did!'
    show adara smile
    'Adara beamed as she squealed, giving me a hug once again.'
    ADARA @smile 'I KNEW you and Markus would get in! Come on! Let me get you a drink!'
    'Before I could say anything, Adara darted off towards the counter to order me a cup.'
    show adara at cright, blurin
    hide adara with easeoutright
    'Here and there were other students scattered about, merrily clanking their drinks as they talked about what role they had been given and of the promise of a future I was to be denied.'
    show mcprologue at left_f, blurin with easeoutleft
    'Miserably, I decided I could no longer bear to stick around and did my best to try and slither away before I felt Adara’s delicate hand find the hem of my shirt and pull me back.'
    show adara at cleft_f with easeinright
    ADARA @talk 'Hey! Wait a minute!'
    ADARA @talk 'Where are you going?'
    show mcprologue at left, blurin
    MC 'Oh uh, I’m just not feeling very well...'
    show adara at cright_f with easeoutright
    show mcprologue at cleft with easeinleft
    ADARA @talk'What? Have you got a fever?'
    MC 'No, uh...'
    ADARA @talk'Where’s Markus? I thought he’d be here celebrating with you.'
    MC 'He’s... {i}elsewhere.{/i}'
    ADARA @talk'Oh...'
    'Before Adara could read any of the pain I was trying so hard to conceal on my face, I tried once again to slink towards the exit.'
    MC @sad'Enjoy your night, Adara.'
    show mcprologue at cleft_f, blurin
    hide mcprologue with easeoutleft
    ADARA @talk 'Hey!'
    hide adara with easeoutleft
    scene black with dissolve
    $ LocSet("novaras_dist_market")
    $ LocUpdateDynSound()
    $ CharSetVar("adara", "blush", False)
    scene adara_alley_hj_bg
    show mcprologue at cleft_f
    with dissolve
    show adara at cright_f with easeinright
    'Making my way out onto the street, a tipsy Adara hastened after me.'
    ADARA @talk'Wait! Stop!'
    show mcprologue at blurin, cleft
    'With a heavy sigh, I slowly turned around to face Adara, my mask of pretence slipping off more and more with every passing second.'
    ADARA @talk'What’s going on? ... Are you telling me the truth?'
    MC 'What?'
    ADARA @talk'[player_name!t], please... Are you telling me the truth?'
    show adara at center_f with easeinright
    MC 'Yes! Now go back in and enjoy yourself, okay?'
    show mcprologue at cleft_f, blurin
    "I turned angrily to leave, my emotions frothing to the surface, but Adara grabbed me."
    show mcprologue at cleft, blurin
    "I spun round and knocked her hand away from me."
    MC @angry 'LEAVE ME ALONE, ADARA!'
    show adara at shake
    show adara shock
    'Somewhat taken back, Adara looked at me in confusion.'
    show adara at cright_f with easeoutright
    'The guilt of what I’d just done stung through me.'
    show adara at center_f with easeinright
    'I tried to fumble out some sort of apology, but Adara, with a new-found look of determination, once again grabbed my hand and dragged me into the darkness of one of the nearby alleys.'
    show adara at nod
    MC @angry 'Hey! Let go!'
    ADARA @angry 'No, not until you tell me the truth, damn it!'
    'In the depths of the alley, dark and dingy, with just a trickle of light allowing me to see her, Adara folded her arms and waited impatiently.'
    MC '...'
    'Suddenly, her gaze dropped to the floor as she spoke with tender realisation.'
    show adara sad
    ADARA @talk'...You didn’t get into the palace, {i}did you?{/i}'
    MC '... No.'
    'Her eyes looked up to meet mine.'
    ADARA @talk'[player_name!t]... I’m so sorry, I know how much you and Markus both wanted to go.'
    show adara smile
    'She smiled encouragingly.'
    ADARA @talk'But just because you didn’t get what you wanted doesn’t mean—'
    MC 'I’m joining the Scouts.'
    show adara shock
    'Adara’s eyes widened as the words sunk in, she turned ghostly white and trembled when she spoke.'
    ADARA @shock'{i}... W-What?{/i}'
    MC 'Both me and Markus... We’ve been put in the Scouts.'
    'Adara said nothing, she just stared at me in shock as the moments crawled by.'
    'Finally, her eyes darkened as she relaxed, her words now solemn in acceptance.'
    ADARA @talk'... When do you leave?'
    MC 'Training starts tomorrow.'
    ADARA @talk'So soon?'
    MC 'Yeah... Tonight is my last night...'
    show adara lewd
    'Adara’s eyes started to mist up, but she quickly averted her gaze from me so I wouldn’t see before she bit down on her lower lip.'
    show adara
    ADARA @talk'{i}... Fine.{/i}'
    MC 'Fine?'
    MC 'Adara, you know as well as I do what—'
    ADARA @angry 'You’re coming home.'
    MC 'No one can promise that.'
    ADARA @angry 'Yes! Yes, I can!'
    ADARA @angry 'Because {i}you will!{/i} You will come home!'
    ADARA @angry 'You’re not allowed to die! Do you understand?!'
    MC '... Adara...'
    ADARA @angry 'Say it!'
    MC '...'
    ADARA @talk'{i}P-Please say it...{/i}'
    MC '...'
    MC 'I’m not allowed to die.'
    $ CharChangeRel("adara", 1)
    MC 'I’m going to come back.'
    show adara with easeinright:
        xcenter 0.4
        xzoom -1.0
    'Overcome with emotion, Adara leapt forward to hug me as she sobbed, tears leaving lonely trails as they swept down her cheeks.'
    'When she pulled back to look at me, she pressed a desperate, {i}needy{/i} kiss onto my mouth. At first, I was surprised, but I soon allowed myself to sink into her warm, comforting embrace.'
    ADARA @talk'Come home... {i}to me...{/i}'
    MC 'Adara... I...'
    'Adara raised a finger to my lips, silencing me.'
    ADARA @talk'{i}No...{/i} Come home, then say what you need to say.'
    'I shuffled away from her, embarrassed. The solemn sultry look Adara had given me, combined with a kiss, had left me hard, aching for more.'
    'As Adara leaned clumsily in again, she must have felt it because her eyes widened in innocent surprise.'
    ADARA @talk'[player_name!t]? Why are you—'
    ADARA @talk'... Oh... I see.'
    MC '... S-Sorry, uh...'
    ADARA 'N-No...'
    ADARA @talk'I, um, {i}I like it.{/i}'
    'Perhaps it was because she was a little tipsy, perhaps it was because hidden in that alley the tension between us had been charged to almost electric...'
    'Or perhaps it was simply the looming thought we may never see each other again, but Adara leaned in and reached down to grab my member in her small, silky hands.'
    MC 'Adara!'
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    window hide
    hide mcprologue
    hide adara
    show adara_alley_hj_slow
    with dissolve
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
    $ Pause()
    'Adara blushed as she began to gently stroke my cock, her fingers dancing over the head.'
    ADARA 'I’m not ready for the full thing...'
    ADARA '...And I haven’t done stuff like this before...'
    ADARA '{i}B-but...{/i}'
    ADARA 'I want this...'
    'Our eyes constantly darted back towards the light at the opening of the street where the rest of the world continued to celebrate.'
    'Shielded by the intimacy of darkness, our breathing became heavier and heavier as Adara’s puppy like eyes looked longingly into mine.'
    MC '...Ahh'
    MC 'Adara, that feels so good...'
    ADARA 'Good... {i}I want it to feel good.{/i}'
    window hide
    hide adara_alley_hj_slow
    show adara_alley_hj_normal
    with dissolve
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg",1)
    $ Pause()
    'Breathing heavily, she began to stroke me faster, her hand gripped me harder as she shyly looked away, biting her lower lip.'
    ADARA 'You have no idea how long I’ve wanted you like this...'
    MC 'Adara... {i}*Huff*{/i} You never-Ah-said...'
    ADARA 'Well I’m saying it now!'
    MC 'Shhh! We might get heard...'
    ADARA 'We-... Oh yes, I {b}know{/b} that.'
    'I felt her coyness erupt into determination...'
    MC 'Ah...~ If you keep that up I’ll-'
    ADARA 'Yes, {b}you will{/b}...'
    'With that, she picked up the pace even further, squeezing my pulsating cock hard as she continued:'
    window hide
    hide adara_alley_hj_normal
    show adara_alley_hj_fast
    with dissolve
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x3.ogg",1)
    $ Pause()
    ADARA 'Cum for me, [player_name!t]...'
    MC '{i}*Huff*{/i} Fuck... Adara...'
    ADARA 'I {b}want{/b} you to finish, [player_name!t].'
    MC "...I'm getting so close..."
    ADARA 'I want to be the one to {b}make you cum!{/b}'
    'Her passionate talking finally tipped me over the edge...'
    MC 'Oh fuck! ADARA!'
    'I felt myself {b}explode{/b} with an animal-like grunt, orgasmic warmth engulfing my entire body, my eyes shut...'
    window hide
    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    $ UnlockGalSceneAndGrantXp("adara","alley_hj")

    ### achievement
    if "adara" not in _total_cummed_characters:
        $ _total_cummed_characters.append("adara")

    stop music fadeout 3.0
    hide adara_alley_hj_fast
    show adara_alley_hj_finish
    with flash
    $ Pause()
    'Exhaling deeply, I saw Adara still holding onto my yet erect member, cum dripping down her hand.'
    'Cooling off back into her usual self, she asked sweetly:'
    ADARA 'Was... Was that good for you?'
    MC '{i}*Huff* *Huff*{/i}'
    MC 'Y-Yes... Thank you.'
    'Adara smiled as she looked around timidly, perhaps realising that at any moment we could be arrested for indecency.'
    ADARA 'I... I must go, before the others wonder where I am...'
    MC 'Alright...'
    ADARA 'And [player_name!t]...'
    MC 'Yeah?'
    ADARA 'Please... Be safe.'
    'I nodded clumsily as she freed herself from our profound embrace, waving meekly at me before disappearing around the corner.'
    hide adara_alley_hj_finish
    show mcprologue at center
    show adara at cright_f
    with dissolve
    show adara at blurin, cright
    hide adara with easeoutright
    MC '...'
    $ CharSetLover("adara")
    $ QstTerminus().AdaraOrNijah = "adara"
    MC '{i}Phew!{/i}'
    $ QstStart(RomanceAdara)
    scene black with dissolve
    $ AutoMus(True)
    $ QstSetProgress(QstTerminus, 4)
    $ LocEnter()