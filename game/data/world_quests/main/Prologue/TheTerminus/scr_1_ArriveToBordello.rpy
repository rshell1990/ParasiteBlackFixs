label qst_Terminus_ArriveToBordello:
    $ TimeAdvBy(TIME_1H)
    show mcprologue at cleft with easeinleft
    'I have made my way down to the Pleasure District.'
    'Semi-delirious with the realisation that my life expectancy had dropped so dramatically in just a few hours, all of my hopes and dreams along with it, I have made my way through the narrow streets.'
    'The Pleasure District glittered beguilingly from the enchanted lanterns and beautiful girls enticing us into their brothels, offering some solace of fun.'
    'It was a strange little world, entirely its own, a place where anyone could forget their troubles for a few hours.'
    'Folk went about merrily, semi-drunk as the sweet air was filled with the scents of seduction and desire.'
    "I saw Markus leaning expectantly on one of the houses' walls, his arms crossed."
    show markusprologue at cright_f
    with easeinright
    MARKUS "You came, huh?"
    'Markus, despite all his gusto wanting to come down here, was as nervous as me.'
    MARKUS 'W-Well... I’m gonna go grab myself a girl, have fun, [player_name!t].'
    MARKUS '... {i}G-Guess I’ll see you tomorrow.{/i}'
    'I felt knots in my stomach just hearing the words. '
    MC '... Yeah... See you then.'
    show markusprologue at cright, blurin
    hide markusprologue with easeoutright
    'Markus shuffled away nervously, heading for a nearby building before a hand appeared and he was abruptly dragged in by the collar.'
    'The woman who’d claimed him was particularly dominant but had an attractive quality in the way she handled herself.'
    MC '{i}*Sigh*{/i}'
    'Well... Let’s do this, not like I’m gonna get another chance for a while.'
    'Wandering through the sparkling maze of streets, I must have passed by a few dozen ladies trying to entice me into their private quarters.'
    'I had to admit, as depressed as I was, the chance to spend at least a couple of hours with any one of them was incredibly appealing.'
    $ CharSetClothes("nijah", "normal")
    show nijah at cright_f with dissolve
    'Eventually, I found myself gazing at a beautiful woman waving me in with long delicate fingers.'
    'Her skin had a warm olive complexion, her hair hung thick and long, her eyes dark and hooded.'
    'She was dressed in clothes that seemed to be from some far-flung land, her face full of foreign allure.'
    'She smiled coyly at me when she could tell I was interested.'
    UNKNOWN 'Hello, stranger!'
    MC 'H-Hi...'
    UNKNOWN 'Wouldz you like to come in?'
    MC 'Y-Yes, please.'
    scene black with dissolve
    'As I entered the small room, I was overcome by the sweet smell of the incense she had been burning.'
    $ LocNameSetTemp("Bordello room")
    $ AutoAmb(False)
    stop ambience fadeout 3.0
    scene bg_weeping_heart_brothel_room
    show nijah at cright_f
    with dissolve
    'In the centre of the room was a bed, piled high with luxurious red quilts.'
    show mcprologue at cleft with easeinleft
    'Unusual pieces of furniture complemented the room which seemed so out of place in the capital of Novaras.'
    'Noticing her accent, I asked:'
    MC 'Umm... Are you from {i}Farah’Sand?{/i}'
    'She paused and folded her arms as she looked me up and down.'
    UNKNOWN '... Zis a problem if I am?'
    MC 'Um! No! Of course not! Uh...'
    UNKNOWN 'Good! But yis, I am from Farah’Sand.'
    UNKNOWN 'Tis strange one zo young as yourself to know zis!'
    MC 'Well... I just came back from my Terminus.'
    UNKNOWN 'Ah! You iz student? Zis iz good!'
    UNKNOWN 'You haz come to celebrate, yes?'
    MC 'Uh... Not really.'
    UNKNOWN 'Hmm?'
    MC 'Uh... {i}I’ve been put in the Scouts.{/i}'
    'For a moment, the woman’s eyes widened, her mouth opened as if she wished to say something, before she decided against it and relaxed her features.'
    UNKNOWN '... I zee.'
    UNKNOWN 'Zo, you wish to have fuck, yes?'
    'Flustered by the bluntness of her answer, I nodded.'
    UNKNOWN 'Fifty gold, please...'
    if PlayerItemQty("gold") < 50:
        'Counting the gold in my hand, I realised I was short.'
        MC 'I... I only have this much...'
        $ PlayerRemItem("gold", PlayerItemQty("gold"))
        'The woman leaned forward to count my gold, then looked up at me with a sympathetic smile.'    
        UNKNOWN 'Iz no matter... {i}You do very brave thing for all of us{/i}'
        MC 'You mean—'
    else:
        MC "Okay..."
        $ PlayerRemItem("gold", 50)
        'The woman leaned forward to count my gold, then looked up at me with a smile.'
    UNKNOWN '{i}Come.{/i}'
    'In that moment, the woman allowed her robes to drop to the floor, revealing her lush naked body beneath.'
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("nijah", "jewelry")
    show nijah at blurin, nod 
    'Her breasts were full, soft and round, her brown nipples already erect, two piercings and a delicate chain linking them.'
    show nijah at center_f with easeinright
    MC '... W-What do I call you?'
    UNKNOWN 'You may call me Nijah.'
    $ CharMeet("nijah")
    $ CharSetVar("nijah", "prologueMet", True)
    MC 'N-Nice to meet you, Nijah, I’m [player_name!t].'
    NIJAH '... {i}Come.{/i}'
    'Taking my hand, Nijah pulled me in closer and pressed a delicate kiss onto my neck.'
    'As I explored her body, reaching around to grab handfuls of her ass, she pulled me down onto the bed on top of her.'
    NIJAH 'How do you want me?'
    menu:
        "Missionary":
            'Nervously, the words stumbled out of me:'
            MC 'L-Like this is fine, thank you.'
            'Nijah smiled, feeling my member hardening as it prodded between her thighs.'
            NIJAH 'Come zen.'
            NIJAH 'Let me help you with zis.'
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            'Taking my cock softly in her hand, Nijah positioned the angle carefully so that when I moved clumsily forward, I thrusted inside her...'

            scene nijah_brothel_miss_slow with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
            $ Pause()

            'Enveloped by her, wet and tight, we both gasped a little as she grabbed me by my ass, pulling me all the way inside her.'
            NIJAH 'Mmm! Yis...'
            MC "Ahh... You're really tight..."
            NIJAH 'Take me!'
            'She {b}was{/b} tight, yet I felt her immense passion, a craving for more of me inside her...'
            'So I gave it to her.'

            'The sound of our flesh colliding amped up as I began to steadily thrust into her.'
            NIJAH "Yi-i-is! Don't you zlow down..."
            'Nijah soon wrapped her legs around me, pulling me deeper inside her as she began to moan under her breath.'
            NIJAH 'Mmm! Zis is... g-good!'
            MC '{i}*Huff* *Huff*{/i} Y-Yeah...!'
            NIJAH 'Fazter! Harder! Fuck me!'

            scene nijah_brothel_miss_fast with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_miss_3.ogg", 1)
            $ Pause()

            'I slammed myself ferociously into her, Nijah grunted happily, the two of us now drenched in sweat...'
            NIJAH 'Yis, more, pound me like you mean it, my ztallion!'
            'My hands clambered over her body, groping and gnawing desperately at her breasts and soft round butt.'
            NIJAH 'Mmm! I am c-close!'
            'She cried out in ecstasy, and upon feeling her pussy squeeze the length of me in tight convoluted motions, I began to feel my body tense up as I thrusted into her faster and faster, pushing myself over the edge.'
            NIJAH 'Yis! Yis zis is it! I can feel—'
            NIJAH 'Mmmm!'
            'Feeling her body tighten once again around my member, my aching balls could finally take no more as I grunted loudly, about to cum...'
            menu:
                'Finish inside of Nijah.':

                    $ UnlockGalFlag("nijah", "brothel_miss", "var_in")
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                    scene nijah_brothel_miss_finish_in with flash
                    $ Pause()

                    'Instinctively, Nijah pulled me in closer and I released deeply into her...'
                    'A hot moan escaped her lips as my warm seed poured into her and I slowly began to soften inside of her.'
                "Cum on Nijah.":

                    $ UnlockGalFlag("nijah", "brothel_miss", "var_out")
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                    scene nijah_brothel_miss_finish_out with flash
                    $ Pause()

                    "Pulling out of Nijah's tight pussy, I stroked my cock for a few moments as I covered her in my hot load."
                    "Nijah moaned as she felt the hot splash on her skin, giggling as she scopped up a little and pressed it into her mouth."
            MC '{i}*Huff*... *Huff*...{/i}'
            'Trembling with subsiding waves of pleasure I pulled out and rolled over besides her.'
            $ UnlockGalSceneAndGrantXp("nijah", "brothel_miss")

        'Doggystyle':
            MC 'Could... Could we do doggystyle?'
            NIJAH 'You want do like ze dog?'
            MC 'Uh... Y-Yes...'
            'Nijah rolled over onto her hands and knees, she bit down on her bottom lip with a smile and wiggled her butt playfully.'
            NIJAH 'Come... {i}Take me like animal.{/i}'
            $ PlayMusicRandom("mus_sex")
            $ AutoMus(False)
            'I nervously did as I was told, positing myself behind her as I grabbed her ass and held her still then thrust myself into her awkwardly.'
            'Nijah shuddered a little as I filled her up and I gasped at how tight and warm she was.'
            MC 'Is this okay?'
            NIJAH 'Mmm... Y-Yis, continue for me, please.'

            scene nijah_brothel_doggy_slow with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop.ogg", 1)
            $ Pause()

            'With both hands on her soft round rump, I thrusted into her with maddening lust. Each stroke inside her felt warmer and wetter than the previous.'
            'Fuelled on by the thoughts of death, of love that wouldn’t be, of anger at where {i}I should{/i} be, I grunted harder as I filled her tender hole.'
            NIJAH 'Mmm! Mmm! Z-Zomeone is v-very p-passionate!'
            NIJAH 'Ah!'
            MC '{i}*Huff* *Huff*{/i}'
            MC 'Is it okay to carry on like this? D’you like it?'
            'Nijah looked back at me, flushed with arousal as she nodded.'
            NIJAH 'Yis, I like ze man who knows how to fuck woman properly!'
            'Encouraged by her words I continued, pushing deeper and harder into Nijah, my hands gripping her ass to steady myself as I slammed inside her.'
            'The air hung heavy with the scent of fucking and was soon filled with a series of happy lustful grunts and moans from the both of us.'
            
            scene nijah_brothel_doggy_normal with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop2.ogg", 1)
            $ Pause()

            MC 'You’re so fucking wet... Ahhh!'
            NIJAH 'Mm! Fuck me harder! Please, I love ze feel of you...'
            'We soon became a hot sweaty mess as our heavy fuck session continued. '
            'My nails dug deep into the flesh of her butt making her squeal with masochistic delight as I plunged my cock deeper into her tight, loving hole.'
            'Soon, Nijah’s body began to tighten around me as her breathless moans became high pitched squeals and grunts.'
            'I could see her hands clasping the quilt as she bit down on the pillow she had buried her face into in ecstasy.'

            scene nijah_brothel_doggy_fast with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_doggy_loop5.ogg", 1)
            $ Pause()

            MC '{i}*Huff*{/i} I’m gonna... cum soon...'
            NIJAH 'Mmm! Yis! Cum! Finish! I want to feel you fill me!'
            MC 'Oh fuck!'
            'Feeling her body squeeze around me, Nijah began to choke on her words as I felt her tremble.'
            'Her legs began to shake as her body was overcome by an orgasm and I felt my own balls tighten, ready to explode inside her.'
            MC 'G-Gonna c—'

            $ PlaySexFx("audio/sex_sounds/nijah_doggy_finish.ogg")
            scene nijah_brothel_doggy_finish with flash
            $ Pause()

            'I didn’t even get to finish my sentence before I grunted loudly, bursts of my hot seed covering her thick ass.'
            NIJAH 'Ooooh! I can feel your cum on me! Iz zo good!'
            'Breathlessly rolling to the side, I sprawled my arms out on the soft bed, satisfied.'
            $ UnlockGalSceneAndGrantXp("nijah","brothel_doggy")

    ### achievement
    if "nijah" not in _total_cummed_characters:
        $ _total_cummed_characters.append("nijah")
    scene black with dissolve
    $ Pause(0.25)
    scene bg_weeping_heart_brothel_room
    show mcprologue at cleft
    show nijah at cright_f
    with dissolve
    'Laying on her side playfully, Nijah giggled:'
    NIJAH 'So, how was zat, {i}lover?{/i}'
    MC 'It was... {i}*huff*{/i} pretty great...'
    NIJAH 'I iz glad!'
    scene nijah_brothel_bj_idle
    with dissolve
    $ Pause()
    NIJAH 'You haz little more time before we finish.'
    NIJAH 'I suck your cock for bit, if you like?'
    MC 'S-Sure...'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene nijah_brothel_bj_suck
    with dissolve
    $ Pause()
    'Nijah stuck out her tongue, slid it under the head of my cock, and then pulled the rest of me inside her warm, wet mouth.'
    NIJAH '{i}*Slurp!*{/i} Mmm~'
    MC 'Ah... So... how did you end up in the Capital?'
    $ StopSexFx()
    scene nijah_brothel_bj_stroke
    with dissolve
    $ Pause()
    NIJAH '{i}*PLOP*{/i} Many of my people, zey were stranded during ze first outbreak.'
    NIJAH 'We came here when trade was good, zer was many talks of new, more relaxed trade routes at time between our lands...'
    NIJAH 'But zen ze ports were closed suddenly and many of us fled {i}here.{/i}'
    NIJAH @sad '{i}*Sigh*{/i} I miss my home greatly...'
    'For a moment, Nijah looked painfully sad, wistful for a land so far out of her reach now. Upon realising that I had noticed, she feigned a smile.'
    NIJAH 'I am sorry, a sad face iz no good for a whore...'
    NIJAH 'Let me make you smile instead!'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene nijah_brothel_bj_suck
    with dissolve
    $ Pause()
    'Nijah quickly brought her mouth back down onto my cock.'
    'She ran her tongue up the length of me before gently licking at the head, teasing me with little flicks.'
    'Then she brought her mouth down around the rest, pushing me deep into her throat.'
    NIJAH 'Mmmm... {i}*Slurp!* *Slurp!*{/i}'
    MC 'A-Ahh...'
    'As I began to feel myself slowly building towards an orgasm once again, I asked.'
    MC 'S-So, do you get many customers?'
    $ StopSexFx()
    scene nijah_brothel_bj_stroke
    with dissolve
    $ Pause()
    NIJAH '{i}*PLOP*{/i} Hmm? Oh, Not really...'
    MC 'Huh? But you’re so beautiful!'
    NIJAH 'Ah! Thank you!'
    NIJAH 'But no, many are wary of my people.'
    NIJAH 'We are not trusted by ze common folk.'
    NIJAH 'Many think we are like, uhh, how you say, ‘leeches’?'
    NIJAH 'But zis is not fair! Because we would go home if we could!'
    MC '... I see.'
    'Suddenly, Nijah stopped.'
    NIJAH 'Oh no... I thinkz we are out of time, [player_name!t]!'
    MC 'Huh? So soon?'
    NIJAH 'You haz been here nearly an hour...'
    MC 'Oh shit! I didn’t even realise!'
    NIJAH 'Iz okay!'
    'As I started to gather up my clothes, Nijah reached out to take my hand.'
    NIJAH '... Wait moment!'
    MC 'Huh?'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene nijah_brothel_bj_suck
    with dissolve
    $ Pause()
    'Suddenly, Nijah lunged forward, sucking on my cock furiously, her lips tight around me as she slammed her mouth up and down.'
    'I gasped as my already sensitive cock was suddenly and quickly overwhelmed by the hot, wet sensation.'
    MC 'F-Fuck!'
    NIJAH '{i}*Slurp!* *Slurp!*{/i} Mmm...'
    MC 'S-Shit! Nijah! I’m gonna cum again! I’m gonna—'
    'With both hands wrapped around me, Nijah made sure to push me in as deeply as possible, moaning with anticipation.'
    'I gasped, overwhelmed with pleasure as I felt my cock convulse in her mouth and poured myself hot and sticky down her throat.'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene nijah_brothel_bj_finish
    with dissolve
    $ Pause()
    'Exhausted, I unsheathed my cock from her mouth, she looked up at me and swallowed the load.'
    'She then took me gently in her hands and very softly ran her tongue from my balls to the head again, making certain to have licked up every last drop.'
    $ UnlockGalSceneAndGrantXp("nijah", "brothel_bj")
    MC '{i}*Huff*{/i} But I thought we... {i}*huff*{/i} were out of...'
    scene bg_weeping_heart_brothel_room
    show mcprologue at cleft
    show nijah at center_f
    with dissolve
    NIJAH 'You iz cute boy.'
    NIJAH '{i}I like you...{/i}'
    'I became almost bashful at her words and couldn’t stop myself from smiling.'
    MC 'T-Thanks...'
    NIJAH 'Now you must shoo!'
    MC 'Oh, uh, okay!'
    NIJAH 'When come back, you will see me again, yes? I would like zat a lot.'
    MC 'Umm, well, {i}if{/i} I come back...'
    NIJAH 'You will be fine! Nijah know these things...'
    'Noticing a painful look of ‘yeah, right’ on my face, Nijah smiled flirtatiously and added...'
    NIJAH 'Zen once you do, I let you put in my butt! Yes?'
    MC 'W-What?!'
    NIJAH 'Good! Zee? Now you have extra reason to come back!'
    'I couldn’t help but laugh at what I presumed was at least a semi-serious offer.'    
    'However, it had finally come for us to say our goodbyes, so she blew me a kiss, closing the door to shut me off from the evening’s antics, ready to prepare herself for the next client of the night.'
    show mcprologue at cleft_f, blurin
    hide mcprologue with easeoutleft
    $ LocNameReset()
    $ LocFlush()
    $ AutoAmb(True)
    $ AutoMus(True)
    with dissolve
    show mcprologue at cright_f
    with easeinright
    'Heh... Well... that was a hell of a way to spend my last night of freedom.'
    'My mind once again turned to dread as the bubbly happy-go-lucky feelings I had felt with Nijah began to dissolve away, to reveal the horrifying reality of what was coming my way.'
    '...My last night.'
    $ CharSetClothes("nijah", "normal")
    $ QstTerminus().AdaraOrNijah = "nijah"
    $ QstSetProgress(QstTerminus, 4)
    $ LocEnter()
