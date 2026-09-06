label rom_Nijah_stage2_afterInvest:
    $ LocSet("nijah_house_broom")
    $ LocFlush()
    show mc:
        xcenter 0.15
    show nijah:
        xcenter 0.4
        xzoom -1.0
    with dissolve
    NIJAH '... Come.'
    'Nijah took my hand.'
    MC 'Nijah? Where are you taking me?'
    'Leading me into her bedroom, she smiled.'
    NIJAH @smile '...'
    $ CharSetClothes("nijah", "naked")
    'Slipping off her robes, Nijah smiled softly as she stood naked before me.'
    show nijah:
        xcenter 0.4
        xzoom -1.0
    with dissolve
    'Nijah dropped to her knees, waiting patiently.'
    NIJAH 'How do you want me, {i}master?{/i}'
    'With my cheeks slightly red at the comment, I did my best to try reassure her that I didn’t {i}buy{/i} her.'
    MC @talk 'N-Nijah, I didn’t-'
    MC @talk  'I didn’t give you the money so that-'
    hide mc
    hide nijah
    with dissolve
    show cg_nijah_kiss_naked:
        xcenter 0.5
    with dissolve
    'Nijah pressed her soft lips passionately into mine, silencing me.'
    NIJAH 'I know zis.'
    MC @talk '...'
    NIJAH 'But you are good...'
    '...Nijah added sadly.'
    NIJAH 'And I know I am not fit to be a wife anymore... Perhaps in Ramon, but here...'
    NIJAH 'Too tainted.'
    MC @talk 'Nijah... I don’t think-'
    NIJAH 'It iz okay, Alderians could never marry Ramonian whores...'
    NIJAH '{i}But zis does not mean I cannot be yours still!{/i}'
    "Nijah’s cheeks flushed red as she nervously looked to the ground."
    NIJAH 'B-But... Zis is okay... I... I can live with this...'
    NIJAH 'As long as you are my master, {i}master.{/i}'
    'Despite my mild anxieties around feeling that I was taking advantage of her, I found myself quickly becoming excited as I stared at her naked kneeling before me.'
    NIJAH 'S-So please... {i}Master...{/i} Do vat you will~'
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    menu nijah_bed_sexmenu:
        'Tell Nijah to suck your cock':
            # 1 Continued – Non-pregnancy
            hide cg_nijah_kiss_naked
            with dissolve
            $ CharSetClothes("mc", "naked")
            show mc:
                xcenter 0.15
            show nijah:
                xcenter 0.4
                xzoom -1.0
            with dissolve
            "Dropping to her knees, Nijah's hands reached to fumblingly undo my belt as she pulled down my clothes to reveal my hard cock."
            'Smiling, and her eyes darting between mine and the large cock in front of her, she quickly went to work, kissing the head of my cock with her soft, sweet lips.'
            NIJAH 'Your cock iz wonderful~'
            NIJAH 'Mmmfghh~'
            MC @talk 'Ahh~ Tease.'
            $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
            scene nijah_house_bj with dissolve
            $ Pause()
            'Nijah giggled to my comment, looking up to me with sultry eyes as she leaned forward, wrapping her lips fully around the head of my cock and slowly gliding forward, moaning softly as she took a few inches.'
            MC @talk 'Ahh! NIJAH!'
            "Nijah's head slowly began to bop back and forth, her tongue thrashing and beating against my member as she cooed and moaned happily."
            NIJAH '(Zo big...)'
            NIJAH '(He puts others to shame.)'
            'Running my hand through her soft black hair, Nijah continued to bop her head back and forth, slowly picking up speed as she tried to take my cock deeper down her throat.'
            MC @talk '(This feels amazing... She’s so good at it!)'
            MC @talk '...Nijah... Ahh...'
            NIJAH 'Mmmhm?'
            MC @talk 'Can you try take it all?'
            NIJAH 'Mmmhmm!!'
            'Nijah, after much struggle inched more and more forward, coating my cock in saliva till finally, she managed to press her nose up against my pubic hairs, her eyes watering as she held my cock down her throat.'
            MC @talk 'Oh shit! Nijah! I’m so close!'
            'Nijah threw her head back and forth furiously, lewd wet sounds escaping her tight sealed lips as I felt my body tighten.'
            "Grunting, unable to hold back any longer, I grabbed Nijah's head and once again slammed her forward, holding her in place as she whimpered."
            $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
            scene nijah_house_bj_finish with flash
            $ ReduceInfectionFromSex("nijah")
            $ UnlockGalSceneAndGrantXp("nijah","house_bj")
            NIJAH 'Mmfghh?!'
            MC @talk 'Swallow! Swallow it all!'
            'Nijah did as she was told, pulling back once she was done to desperately gasp for air before opening her mouth to show me she had done it.'
            NIJAH '{i}*Huff*{/i} Are you pleased {i}*Huff*{/i} Master?'
            MC @talk 'I think from the way my legs are shaking, I might just need to lay down for a bit!'
            NIJAH '{i}*Giggles*{/i} Good~'

        'Tell Nijah to get on the bed': #(doggy style = Vaginal and anal variants)
            #2.) Continued – Non pregnancy
            hide cg_nijah_kiss_naked
            with dissolve
            $ CharSetClothes("mc", "naked")
            show mc:
                xcenter 0.15
            show nijah:
                xcenter 0.3
                xzoom -1.0
            with dissolve
            'Getting on the bed on all fours, Nijah stuck out her butt lewdly and lightly swayed it back and forth enticingly as she looked over her shoulder nervously.'
            NIJAH 'M-Master please... Claim me.'
            'With my hands on her soft cheeks, I slapped my cock a few times on her before gently pressing my cock against...'

            menu nijah_v_or_a:
                'Her pussy.':
                    #2a Continued
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg",1)
                    scene nijah_house_doggy_vag with dissolve
                    $ Pause()
                    'Gently, I pressed the head of my cock against the already wet hole, and Nijah gasped as she felt my cock slowly enter into her.'
                    NIJAH 'Ooooh! S-So good!'
                    NIJAH 'M-Mmmm...!'
                    MC @talk 'Are you okay Nijah?'
                    "Nijah's hands coiled around the bed quilts as she bit her lower lip, but after a deep breath she nodded."
                    NIJAH 'Y-Yes, you are just very big.'
                    NIJAH 'P-Please continue m-master.'
                    'With my hands on her hips, I continued to press the rest of my cock into her, feeling her body tighten around me as she struggled to take me deeply.'
                    NIJAH 'Ahh!'
                    'After a few minutes, Nijah slowly began to rock her butt back with the motions, and we soon began to build a steady rhythm as she felt more comfortable with me moving faster.'
                    NIJAH 'Yes! Fuck me master! Make me your little Ramonian whore! Ah!'
                    'Throwing herself back wildly onto me, Nijah continued to moan and grunt as she slammed herself back onto me, our flesh slapping against each other making sounds as sweat began to drip down from the two of us as passion overtook.'
                    NIJAH 'So... close!'
                    NIJAH 'Finish Master! Don’t stop till you finish!'
                    "Slamming into Nijah’s ass, she wailed like an animal as I took and used her body for my pleasure, uncontrollably moaning till I suddenly felt myself unable to hold back any longer..."
                    "Unable to hold back any longer, I pulled Nijah's ass back to fully take my cock, and as she quivered and moaned, a guttural sound escaped her lips as she felt the hot rush of my load pouring deeply into her."
                    scene nijah_house_doggy_vag_finish with flash
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                    $ ReduceInfectionFromSex("nijah")
                    $ PregRoll("nijah")
                    $ UnlockGalFlag("nijah", "house_doggy", "var_vag")
                    $ UnlockGalSceneAndGrantXp("nijah","house_doggy")
                    $ Pause()
                    NIJAH 'Ooooh~ Master...'
                    NIJAH '{i}Zo much...{/i}'
                    NIJAH 'I feel so full now!'
                    'Nijah giggled, sweaty and breathing heavily from exhaustion as she looked over her shoulder towards me while she fluttered her eyes.'

                'Her asshole.':
                    "As I pressed my cock against Nijah’s tight, dark rosebud, she suddenly gasped and reached back to cover her asshole with her hand."
                    NIJAH 'N-Not that hole!'
                    MC @talk 'I want to fuck your ass.'
                    'Nijah blushed profusely at the comment.'
                    NIJAH 'You are very big...'
                    'Nijah whimpered but nodded.'
                    scene nijah_house_doggy_anal with dissolve
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg", 1)
                    $ Pause()
                    "Once I was confident she was ready, I once again pressed the head of my cock against Nijah’s tight ass, and her hands coiled as she whimpered nervously, squealing when the head of my cock forced open her tight asshole and pressed it’s way forward."
                    NIJAH 'AHHH!'
                    MC @talk 'Are you okay?'
                    NIJAH 'J-Just hold for a moment...'
                    'After taking a few anxious breathes, Nijah did her best to try and relax as she nervously signalled for me to continue fucking her ass.'
                    'Slowly, as Nijah’s tight ass ring stretched around my cock while she took me deeper into her, the winces of pain slowly died down, and soon, she moaned softly beneath her hot breath, gently rocking her round butt back and forth onto my member with no prompt.'
                    NIJAH 'Mmmhmm... Iz starting to feel g-good...'
                    NIJAH 'But it still burns a little!'
                    'After a few more minutes of her ass tightening and flexing around my cock, I with my hands pressed greedily into her ass began to thrust back and forth faster.'
                    'Soon, I was slamming to the hilt of her tight ass while Nijah squealed in pleasure, moaning as her tight ass worked tirelessly to try and force me to finish inside of her.'
                    MC @talk 'NIJAH! {i}*Huff!*{/i} Your ass feels incredible!'
                    NIJAH 'Yes! Fuck my butt! So good! Yes!~'
                    'Excitedly, Nijah’s pussy dripped onto the bed quilts while I continued to pound her ass from behind, and soon, as her body convulsed in tight waves, I could sense her orgasm drawing near.'
                    NIJAH 'Yes! YES! Take my ass master!'
                    NIJAH 'YES!~'
                    'As her body convulsed and tightened around me, her mouth hung agape as she seemed to choke on her own words, a powerful orgasm ripping through her body as I found myself drawing almost painfully near to finishing as well...'
                    
                    'Unable to hold back any longer, I pulled Nijah’s tight ass back to fully take my cock, and as she quivered and moaned, a guttural sound escaped her lips as she felt the hot rush of my load pouring deeply into her asshole.'
                    scene nijah_house_doggy_anal_finish with dissolve
                    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
                    $ ReduceInfectionFromSex("nijah")
                    $ UnlockGalFlag("nijah","house_doggy","var_anal")
                    $ UnlockGalSceneAndGrantXp("nijah","house_doggy")
                    $ Pause()
                    NIJAH 'Ooooh~ Master...!'
                    NIJAH '{i}Zo much...{/i}'
                    NIJAH 'My poor butt iz on fire!'
                    'Nijah dropped down onto the bed face first, her body twitching involuntarily as some of my excess seed poured from her stretched asshole.'
                    NIJAH 'G-Grghhh~'

        'Tell Nijah to ride you':
            hide cg_nijah_kiss_naked
            with dissolve
            'Taking my hand, Nijah lead me towards the bed before both her hands rested on my chest, shoving me forward and down onto the quilts as she climbed on top.'
            NIJAH '{i}Clothes off.{/i}'
            $ CharSetClothes("mc", "naked")
            show mc:
                xcenter 0.15
            show nijah:
                xcenter 0.3
                xzoom -1.0
            with dissolve
            'She ordered hungrily, and obliging her, I stripped down as Nijah smiled, rubbing her already wet pussy against my cock, moaning sweetly as she did so.'
            NIJAH 'Zo good...~'
            NIJAH 'O-Oooh...!'
            if CharIsVisiblyPreg("nijah"):
                scene nijah_house_cowgirl_preg with dissolve
            else:
                scene nijah_house_cowgirl_nopreg with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg",1)
            $ Pause()
            'Gently taking a hold of my cock in her warm hand, Nijah aligned it against her opening and slowly side down onto it, sighing happily as I slowly entered her tight, hot body.'
            NIJAH 'Mmmfgh...'
            NIJAH 'Master, you feel wonderful.'
            MC @talk 'Ah! Nijah, you feel incredible...'
            'Smiling mischievously, Nijah sighed happily as she lifted herself and dropped down slowly, steadily building speed as she rode my cock.'
            NIJAH 'Mmm, my love~ Yes!'
            NIJAH 'Such a big cock! Ah!'
            'Nijah began to slam herself down onto me, her tight body squeezing and milking my cock as she rode me furiously, guttural moans escaping her lips as her hands trailed down my chest.'
            NIJAH 'Yes! YES!'
            NIJAH 'I’m so close!'
            'Nijah suddenly began to tighten up, her body convulsing in short waves as she trembled and squeezed around me, her eyes slightly rolling back as she struggled to form some type of words, choking on air as she let out a squeal like moan of pleasure.'
            NIJAH 'OOOOH!~'
            if CharIsVisiblyPreg("nijah"):
                scene nijah_house_cowgirl_preg_finish with dissolve
                $ UnlockGalFlag("nijah","house_cowgirl","var_preg")
            else:
                scene nijah_house_cowgirl_nopreg_finish with dissolve
                $ UnlockGalFlag("nijah","house_cowgirl","var_nopreg")
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            $ ReduceInfectionFromSex("nijah")
            $ UnlockGalSceneAndGrantXp("nijah","house_cowgirl")
            $ Pause()
            'Unable to hold back much longer myself, I reached forward to grab her hips, forcing myself to fuck her as quickly as I could like a wild animal in heat.'
            'As she became overwhelmed from the pleasure, she threw her head back.'
            'I gritted my teeth and grunted that I was about to finish.'
            'Pouring my hot load into her, Nijah flung herself forward to steal a kiss, grinding her pussy down on me before she pulled back and smiled.'
            NIJAH 'Zat good for you?'
            MC @talk '{i}Very.{/i}'
            'Nijah smiled, her sultry eyes locked onto mine as she greedily stole another kiss.'

        'Ask Nijah if you can fuck her in your parasite form':
            hide cg_nijah_kiss_naked
            with dissolve
            show mc:
                xcenter 0.15
            show nijah:
                xcenter 0.3
                xzoom -1.0
            with dissolve
            'Nijah blinked at the request.'
            NIJAH 'Y-You want vat?'
            MC @talk 'In my other form...'
            'Nijah flushed red, biting at her nail nervously while she pondered the idea.'
            NIJAH 'Your other form... maybe too much for me without lube.'
            MC @talk 'Here Nijah, I already have some.'
            NIJAH 'O-Oh?'
            'Nijah took the vial of lube.'
            NIJAH '...G-Give me a few minutes.'
            NIJAH 'Need to make sure everything is ready.'
            scene black with dissolve
            'Nijah made sure to anxiously apply the lube not only to her pussy, but her asshole as well, perhaps unsure of what my ‘other’ form would be like.'
            'Finally satisfied, she took a deep breath and approached me once again.'
            $ LocFlush()
            show mc_transformed:
                xcenter 0.3
            show nijah:
                xcenter 0.7
                xzoom -1.0
            NIJAH 'Okay... I iz ready.'
            "Changing into my other form, I could sense Nijah’s tense nervousness as she saw the flesh tear away from me, and pale white with fear, I thought she might bolt for the door before I called to her in my raspy voice."
            MC @talk 'Wait! It’s still me! It’s okay!'
            NIJAH 'Y-Yes... I sorry.'
            NIJAH 'Just... Not used to you like that.'
            show nijah:
                ease 1.0 xcenter 0.5
                xzoom -1.0
            'Doing her best to feign a confident smile, she sheepishly stepped towards me.'
            NIJAH 'S-So... How we do this my love?'
            'With both hands  wrapped around her, I lifted Nijah up with ease and she squealed with mild panic as I held her body up with ease.'
            NIJAH 'Y-You is strong!'
            'Lewdly, I leaned forward and pressed my tongue into her mouth before sliding it down her throat.'
            'At first, she pulled back, perhaps in initial revulsion or shock, but as the pheromones released, she soon relaxed and lewdly began to moan, entwining her tongue with mine.'
            NIJAH '(Ooooh~ What is zis feeling?)'
            NIJAH '(Everything feels so...so hot and dizzy now.)'
            NIJAH 'A-Ahh...!~'
            NIJAH 'Mmmfghh...!'
            'With her fear and anxieties seemingly drifting away, Nijah began to drip in anticipation of what was to come...'
            'With her body little more than a plaything to me, my ribbed bulbous cock slowly unsheathed itself.'
            'I began to prod teasingly and press my cock against...'
            menu:
                'Her pussy':
                    if CharIsVisiblyPreg("nijah"):
                        scene nijah_house_para_preg_vag with dissolve
                    else:
                        scene nijah_house_para_nopreg_vag with dissolve
                    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg",1)
                    $ Pause()
                    'As the bulbous red cock pressed against her wet hole, Nijah moaned softly with every prod, and soon, with her feet dangling in the air, her toes curled as she felt my member press and force its way into her hot body.'
                    NIJAH 'A-Ahhh...!'
                    "I felt the instant gratification of Nijah’s body tightening around me, and as I rumbled in approval, Nijah’s mouth hung open as I slowly slid her down onto my cock."
                    NIJAH 'M-Mmfghh!'
                    'I soothingly leaned closer, nuzzling at her neck as I gave her a few moments to relax.'
                    NIJAH 'I... I iz fine, j-just...'
                    NIJAH 'C-Careful.'
                    'Gently, with my hands softly gripped beneath her legs, I began to lift and drop her onto my cock, and each time, Nijah slowly became wetter as soft moans began to escape her lips.'
                    NIJAH 'O-Oooh~'
                    NIJAH 'My love, p-please...!'
                    'Encouraged by her words, I began to pick up the pace, grunting hot breathes as I continued to fuck Nijah, driven by that animalistic desire as my hands light squeezed at her flesh while forcing her down onto my cock.'
                    'Nijah, now sweaty and overcome by the pleasure, began to try and help throw herself back down onto me, moaning with each thrust.'
                    NIJAH 'Ahh! Ahh! Oooh!'
                    NIJAH 'P-Please! Iz so good!'
                    NIJAH 'F-Finish inside of me my love! Don’t stop!'
                    NIJAH 'Iz wonderful!'
                    if CharIsVisiblyPreg("nijah"):
                        scene nijah_house_para_preg_vag_finish with flash
                        $ UnlockGalFlag("nijah", "house_para", "var_preg_vag")
                    else:
                        scene nijah_house_para_nopreg_vag_finish with flash
                        $ UnlockGalFlag("nijah", "house_para", "var_nopreg_vag")
                    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
                    $ ReduceInfectionFromSex("nijah")
                    $ PregRoll("nijah")
                    $ UnlockGalSceneAndGrantXp("nijah", "house_para")
                    $ Pause()
                    "Unable to hold on any longer, I growled loudly as I forced Nijah’s soft ass down onto my member, pressing her to the hilt as her eyes widened in shock as she felt the hot seed pouring into."
                    'Her body shook and trembled as her hands coiled in pleasure, her mouth hung agape as she choked on the air in pleasurable ecstasy.'
                    'As I felt Nijah begin to go limp, I placed her gently down onto the bed, an exhausted look etched onto her face as she tried to catch her breath, my seed pouring out of her pussy the whole time.'
                    NIJAH 'Iz... Zo good~'

                'Her asshole':
                    if CharIsVisiblyPreg("nijah"):
                        scene nijah_house_para_preg_anal with dissolve
                    else:
                        scene nijah_house_para_nopreg_anal with dissolve
                    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg",1)
                    $ Pause()
                    'When Nijah felt my cock prod against her tight backdoor, her face whitened as she sheepishly looked into my eyes, stuttering over her words.'
                    NIJAH 'Z-Zat is-'
                    'I grumbled soothingly, but as I prodded gently against her hole, Nijah understood what I wanted to take, and flushed red from embarrassment.'
                    NIJAH '{i}...Be gentle.{/i}'
                    'Gently, as I continued to press against her tight rosebud, Nijah’s ass spread and opened as the head pushed through into her tight backdoor.'
                    'With her eyes wide, she gritted her teeth while toes curled, shaking slightly as she felt my cock slowly push its way deeper into her.'
                    NIJAH 'AHHH!'
                    NIJAH 'Too big! TOO BIG!'
                    NIJAH 'Burning!'
                    'As Nijah closed her eyes painfully whimpering, I stopped for a moment, and pulled her head towards mine,'
                    NIJAH 'Hurts! Please! You are-'
                    "Suddenly, I pressed my long tongue into Nijah’s mouth, catching her off guard briefly as I began to feed her body more endorphins, twisting my tongue around hers."
                    NIJAH 'M-Mmmfghh...'
                    'Nijah closed her eyes as I continued, and without even realizing, she was now beginning to gently bounce on my cock, the tight ring of her ass squeezing and milking me while soft moans escaped her lips.'
                    NIJAH 'Iz... Wonderful...'
                    NIJAH 'Never... Mmm... Enjoyed this so much...!'
                    'With her body now burning with arousal, I began to pick up the pace, lifting up her plump fleshy ass and dropping her back down onto me as Nijah, now dripping with sweat moaned loudly.'
                    NIJAH 'Yes! Mmmfgh!'
                    NIJAH 'D-Do not stop! F-Fuck me!'
                    NIJAH 'Fuck my ass!'
                    if CharIsVisiblyPreg("nijah"):
                        scene nijah_house_para_preg_anal_finish with dissolve
                        $ UnlockGalFlag("nijah","house_para","var_preg_anal")
                    else:
                        scene nijah_house_para_nopreg_anal_finish with dissolve
                        $ UnlockGalFlag("nijah","house_para","var_nopreg_anal")
                    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
                    $ ReduceInfectionFromSex("nijah")
                    $ UnlockGalSceneAndGrantXp("nijah","house_para")
                    $ Pause()
                    'Unable to hold on any longer, I growled loudly as I forced Nijah’s soft ass down onto my member, pressing her to the hilt as her eyes widened in shock as she felt the hot seed pouring into her tight backdoor.'
                    'Her body shook and trembled as her hands coiled in pleasure, her mouth hung agape as she choked on the air in pleasurable ecstasy.'
                    NIJAH 'M-My poor ass!'
                    'As I felt Nijah begin to go limp, I placed her gently down onto the bed, an exhausted look etched onto her face as she tried to catch her breath, my seed pouring out of her backdoor the whole time.'
                    NIJAH '{i}*Huff*{/i} My poor... {i}*Huff*{/i} ass...'
                    'Nijah laughed as she looked up to me half-deliriously,'
                    NIJAH 'I may not walk straight for few days now!'
    $ LocFlush()
    $ AutoMus(True)
    show mc:
        xcenter 0.15
    show nijah:
        xcenter 0.4
        xzoom -1.0
    with dissolve
    NIJAH 'Would you cuddle with me, my love?'
    $ QstSetProgress(RomanceNijah, 2)
    $ RomanceNijah().investBusiness = True
    $ QstStart(ShopNijahStall)
    menu:
        'Yes.':
            scene black with dissolve
            NIJAH 'Come to bed my love~'
            $ CharSetClothes("mc", "normal")
            $ CharSetClothes("nijah", "normal")
            $ LocSet("novaras_dist_house")
            $ CharChangeRel("nijah", 1)
            $ NoteUnlock("NijahRomanceInvested")
            $ LocEnter()

        'I have other business to attend to.':
            'Nijah sighed dejectedly.'
            NIJAH 'I zee.'
            NIJAH 'Do not leave me too long, iz lonely without you...'
            $ CharSetClothes("mc", "normal")
            $ CharSetClothes("nijah", "normal")
            $ LocSet("novaras_dist_house")
            $ NoteUnlock("NijahRomanceInvested")
            $ LocEnter()