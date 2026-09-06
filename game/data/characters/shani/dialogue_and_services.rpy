init python:
    @AppendToAllQuests
    class DialogueShani(LogicModule):
        def __init__(self):
            super().__init__()

            self.knowName = False
            self.paidAmount = 0
            self.analPrice = 350

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_bordello_ext":
                if not IsDaytime():
                    btnMods["shani_talk_btn"] = BtnJumpLabel(_("Talk to the working girl"), "shani_talk")
            return LocButtonMod(directMods=btnMods)

        def extraDialogue(self):
            yield ("shani_root", DNode(_("Let's have some fun."), "shani_sexmenu"))
            yield ("shani_root", DNode(_("I wanted to ask you a few questions."), "shani_questions"))
            yield ("shani_root", DNode(_("I should go."), "shani_bye", nextNode = "DNodeExit", order = -100))
            if self.knowName == False:
                yield ("shani_questions", DNode(_("What's your name?"), "shani_name"))
            yield ("shani_questions", DNode(_("How did you end up becoming... well... a 'lady of the night'?"), "shani_prof"))
            yield ("shani_questions", DNode(_("Have you heard any rumours about goings on around the city?"), "shani_rumours"))
            yield ("shani_questions", DNode(_("Forget it."), "shani_stopquestions", nextNode = "shani_root"))

            yield ("shani_sex", DNode(_("Getting my cock sucked."), "shani_bj"))
            yield ("shani_sex", DNode(_("I don't know, sex?"), "shani_vag"))
            yield ("shani_sex", DNode(_("Your sweet backdoor."), "shani_anal"))
            yield ("shani_sex", DNode(_("Let's talk about something else instead."), "shani_sexmenu_leave", nextNode = "shani_root"))
### shani talk label(s)
# intro/menu
label shani_talk:
    show shani at center
    with dissolve
    $ rng = RngInt(1,3)
    if rng == 1:
        SHANI "Hey handsome, looking for some action?"
    if rng == 2:
        SHANI "Do you like what you see?"
    if rng == 3:
        SHANI "Care to please a lady in need?"
    call processDialogue("shani_root") from _call_processDialogue_7
    $ LocEnter()

# questions main
label shani_questions:
    show shani angry
    'This one she did not like...'
    SHANI @angry "You're not working for one of them inquisitors, are you?"
    MC @talk 'No, I just have a few questions.'
    show shani
    SHANI 'Well that depends, my time is money so...'
    menu:
        "Give her some coin" (Req_Gold = 10):
            $ PlayerRemItem("gold", 10)
            SHANI "What do you want to know?"
            SHANI "Can't promise I'll answer everything though..."
            call processDialogue("shani_questions") from _call_processDialogue_8
            return
        "So is everyone else's.":
            SHANI "You don't value knowledge much, do you..."
            SHANI "Wanna have some fun instead?"
            return

# name question
label shani_name:
    SHANI "Why'd you want to know that?"
    MC @talk 'Most conversations with new people usually start with names.'
    SHANI 'Fine, then what’s yours?'
    MC @talk 'You can call me [player_name!t].'
    'The girl seemed uncomfortable answering my question, her eyes nervously averting away.'
    SHANI '...Shani.'
    $ CharMeet("shani")
    $ DialogueShani().knowName = True
    $ SHANI = Character(_("Shani"), image = "shani")
    MC @talk 'Is that your {i}real{/i} name?'
    SHANI 'It’s the only name I’m willing to give.'
    MC @talk 'Alright, well, pleased to meet you, Shani.'
    SHANI "Oh the pleasure's all mine."
    return

# prof question
label shani_prof:
    show shani angry
    SHANI @angry 'Is this some kind of trick question?'
    SHANI @angry 'I’m not stupid you know!'
    MC @talk 'No, I... I mean, doesn’t the government give everyone jobs assigned?'
    MC @talk 'Were you really assigned to be-'
    SHANI @angry 'Of course bloody not!'
    SHANI @angry 'Gods, you aren’t the sharpest tool are you?'
    MC @talk 'Hey! I scored very well and-'
    SHANI @angry 'And ended up becoming a scout?'
    MC @talk '...'
    SHANI @angry 'Yeah, I can always tell.'
    SHANI @angry 'It’s all a load of shite, they manipulate who goes into what job, they’ve done it for years.'
    MC @talk  'How do you know that?'
    SHANI @angry 'You know, you might be book smart but you ain’t much common sense, are you?'
    SHANI @angry 'Bah, all of you lot are the same, eating up whatever nonsense those cunts conjure up as an excuse for you all.'
    show shani
    'Shani looked around for anyone who might be listening in before she leaned forward to whisper to me.'
    SHANI 'They look for the pretty ones without family, the ‘problem’ girls so to speak.'
    SHANI 'Either a lot of those refugees from Ramon or girls who maybe are just doing average on the scores, the ones no one will miss.'
    SHANI 'Then they give them jobs that don’t pay enough to even get by because they KNOW the girls will have to turn tricks to make ends meet.'
    MC @talk 'Is that what happened to you?'
    SHANI '...I wasn’t the best in School, I’ll be honest.'
    SHANI 'But I was good with nursing and they said I might be able to help with some basic treatments of the wounded.'
    SHANI 'Next thing I know, I’m shafted with street sweeping suddenly, not even enough to cover half my rent.'
    SHANI 'And with everyone’s work already decided, what else is a girl supposed to do?'
    SHANI 'Oh that’s right, they know EXACTLY what they’re doing.'
    SHANI 'One of my friends was set on course to being a kitchen assistant, the same bloody thing happened to her.'
    SHANI "Now she's taking cock up the ass like the rest of us."
    SHANI 'Bastards probably fucked with your scores too if you were unlucky enough to get shafted into the Scouts.'
    SHANI 'You piss someone off you shouldn’t have by any chance?'
    'I dwelled on the thought for a moment, but quickly dismissed it.'
    MC @talk "No, I rely on my innate luck getting what I want."
    show shani smile
    'Shani laughed, rolling her eyes at this one.'
    SHANI @smile 'Okay, lucky one...'
    show shani
    return

# question rumors
label shani_rumours:
    SHANI 'Rumours? What kind of rumours are you asking about?'
    SHANI "I know half the men in this city can’t stay faithful to their wives if that’s what you're asking, but I’m not privy to court gossip."
    MC @talk 'Something a sellsword could use...'
    'Shani once again looked around nervously for anyone who might be listening in.'
    SHANI "Yeah... There is, but you didn’t hear it from me."
    MC @talk 'Go on...'
    SHANI 'Lots of girls have been going missing recently.'
    MC @talk 'Missing?'
    SHANI 'Yeah, vanished into thin air.'
    SHANI 'Girls who wouldn’t vanish without saying something to one of us first.'
    MC @talk 'Have you tried speaking to the guards about it?'
    SHANI 'Those wankers aren’t interested.'
    SHANI 'No ones interested in us lot, we’re replaceable and forgotten once they’re done with us.'
    MC @talk 'So you want me to find what’s happening to the girls?'
    SHANI "You'll soon be able to speak to Madam Carina inside about it, I don’t know much else."
    return

# leave questions
label shani_stopquestions:
    SHANI "Suit yourself, now you're looking to do business or not?"
    return

# shani sex options
label shani_sexmenu:
    SHANI @lewd 'Now we’re talking my language handsome, what are you interested in?'
    call processDialogue("shani_sex") from _call_processDialogue_9
    return

# bj scene
label shani_bj:
    SHANI 'That’ll be fifty coins.'
    menu:
        'Hand them over.' (Req_Gold = 50):
            $ PlayerRemItem("gold", 50)
            $ DialogueShani().paidAmount += 50
            SHANI 'Right this way stranger~'
            scene black with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            'Following Shani, she led me behind some darkened alleyway before shoving me against the wall.'
            SHANI 'Now, let’s see what we’re working with here.'
            'As Shani crouched down, she unbuckled my clothes, and as she pulled out my cock her eyes widened as she grinned,'
            SHANI 'Fuckin’ hell! You’re a hung one, aren’t ya?'
            MC @talk 'That going to be a problem?'
            SHANI 'Not at all my love, just more for me to play with~'
            $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
            scene shani_bj with dissolve
            $ Pause()
            'Licking her lips, Shani laughed to herself slightly as her hands wrapped around my member, stroking it a few times before she leaned forward.'
            'Planting a warm kiss onto the head of my cock, her lips rolled over and enveloped the head.'
            SHANI 'Mmm~'
            MC @talk 'Ahhh... That’s it.'
            'Shani began to slide her lips forward, enveloping my cock in her warm mouth as lewd wet sounds escaped from her lips.'
            'Quickly, she began to bop her head back and forth, her tongue bashing against my cock as she took an impressive amount of it.'
            'Shani began to glide her head back and forth faster, her sultry eyes looking up to me as I felt her warm mouth begin driving me crazy as her tongue twisted and curled around me.'
            scene shani_bj_alt with dissolve
            $ Pause()
            MC @talk 'F-Fuck...'
            MC @talk 'I don’t know how much longer at this rate I can-'
            MC @talk 'AHHH!'
            'Sensing my cock was beginning to throb in anticipation, Shani continued to throw herself onto me, now taking my cock as deeply as she could gagging on the large member in her mouth.'
            'Unable to hold on any longer, I grunted loudly, my teeth gritted as I pushed Shani’s head forward, forcing her to swallow my load,'
            scene shani_bj_finish with flash
            $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
            $ ReduceInfectionFromSex("shani")
            $ UnlockGalSceneAndGrantXp("shani","bj")
            $ Pause()
            'Her eyes widened in surprise at how much seed there was, and as she struggled against my hand, I finally released her once she was fully spent.'
            'She pulled her head back, coughing and spluttering as she tried to swallow down the rest of the load.'
            SHANI '*Cough* Fuckin’ hell!'
            SHANI 'You half horse or something?!'
            MC @talk 'Not exactly...'
            BLACK 'Half-deity.'
            SHANI 'Gods, that was a lot.'
            SHANI 'And what in the seven hells?'
            SHANI "Why’s this seed taste so good?"
            SHANI 'Alright well, pleasure doing business with you...'
            $ AutoMus(True)
            $ store.curDialogue = "DNodeExit"
            $ LocFlush()
            return
        'On second thought...':
            SHANI @angry "What? I don't bite you know."
            SHANI "What's on your mind?"
            return

# vag scene
label shani_vag:
    SHANI 'Now we’re talkin’.'
    SHANI 'That’ll be a hundred and fifty.'
    menu:
        'Hand them over.' (Req_Gold = 150):
            $ PlayerRemItem("gold", 150)
            $ DialogueShani().paidAmount += 150
            scene black with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            'Shani led me around some back alley away from prying eyes, quickly hiking up her skirt to reveal her bare ass as she pressed her hands against the cold stone wall.'
            SHANI 'Well don’t keep me waiting, be quick lover~'
            'Wasting no time, I unbuckled my clothes and pressed my hard-on against her tight, warm hole.'
            SHANI 'Alright, now just-'
            scene shani_doggy_vag with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg",1)
            $ Pause()
            'I forced my cock deeply into her and she gasped in shock, her tight warm body squeezing effortless around me.'
            SHANI 'FUCK!'
            SHANI '*Huff* T-There’s a lot of you!'
            MC @talk 'Everything okay?'
            SHANI 'Just, start slow, okay love?'
            SHANI 'F-Fuck, it’s like being screwed by a horse...!'
            'I begin to glide my cock in and out of her tight body, and with each thrust, she let out a hot moan or grunt as my cock pushed its way into her.'
            'She was tight, her pussy squeezing and gripping around me as I thrust into her wet hole.'
            SHANI 'Oh fuck... *Huff* G-Gods! How much longer can you last? I’m not gonna be able to walk after this!'
            'Shani’s legs began to tremble as I had to hold up her hips while I thrust into her.'
            'I felt her body tighten in waves as she closed her eyes, mouth hung open as she quivered in place.'
            SHANI 'Ah! Ah! Mmmfgh!'
            SHANI 'Fuckkk!'
            SHANI 'F-Finish! Finish please! I can’t take it any longer!'
            'Unable to hold back any longer, feeling my own pleasure reach its peak, I dug my hands into her soft ass as I thrust forward, grunting as I released deep inside of Shani.'
            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            $ ReduceInfectionFromSex("shani")
            scene shani_doggy_vag_finish with flash
            $ UnlockGalSceneAndGrantXp("shani","doggy")
            $ UnlockGalFlag("shani","doggy","var_vag")
            $ Pause()
            SHANI '{i}F-Fuck! There’s so much of it! I’m gonna walk around looking pregnant at this rate!{/i}'
            SHANI '{i}It’s so... hot, Oh gods, my body just feels so alive!{/i}'
            'Finally finished, I sighed with relief and unsheathed my cock from Shani, watching as some of my seed poured out from her onto the ground as she shakily got back to her feet.'
            SHANI 'That was...'
            SHANI 'You really know how to show a girl a good time, don’t you?'
            SHANI 'Come on, let’s get back before someone sees us down here.'
            SHANI '...And before my legs give out.'
            $ AutoMus(True)
            $ store.curDialogue = "DNodeExit"
            $ LocFlush()
            return
        "Actually, I have something else in mind.":
            SHANI "Yeah, whatever..."
            return

# anal scene
label shani_anal:
    if DialogueShani().paidAmount < 200:
        SHANI 'Sorry love, but uh, that hole’s reserved only for regulars I can trust.'
        'Regulars, huh?'
        'Guess this relationship needs a little more {i}investment.{/i}'
        return
    if QstIsComplete(QstADazzlingTail):
        SHANI 'Funny you mention about anal...'
        SHANI 'This girls been selling these things to help keep our asses stretched a little would you believe it or not!'
        SHANI 'The girls are going crazy for them and well...'
        SHANI 'Let’s just say I’m only charging three hundred coins now.'
        $ DialogueShani().analPrice = 300
    else:
        'Shani took a deep breath...'
        SHANI '...Three hundred and fifty coins.'
        MC @surprised 'You want three hundred coins for anal?'
        MC @surprised 'Are you serious?'
        SHANI 'Listen love, I’ve seen that thing dangling between your legs.'
        SHANI 'If you smash in my backdoors with that, I am probably going to need to take the rest of the night off.'
        SHANI 'So, what will it be?'
    menu:
        'Hand them over.' (Req_Gold = DialogueShani().analPrice):
            $ PlayerRemItem("gold", DialogueShani().analPrice)
            $ DialogueShani().paidAmount += DialogueShani().analPrice
            scene black with dissolve
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            SHANI 'A-Alright, come this way...'
            'Shani led me down a quiet, darkened black alley, where she nervously hiked up her dress and bent forward against the wall, her tight darkened asshole winking at me.'
            SHANI 'I uh, p-put some lube there so...'
            'Wasting little time, I moved behind Shani and pressed the head of my cock against her tight backdoor.'
            scene shani_doggy_anal with dissolve
            $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg",1)
            $ Pause()
            'Shani winced slightly as she felt my push against her rosebud, and after some initial resistance, her asshole spread around my cock and I managed to push my member forward deep into her ass.'
            SHANI 'F-Fuckkkk!'
            SHANI 'Fuck! It burns!'
            SHANI 'S-Start slow! Gods! My poor fucking ass!'
            'Uh, could use some help here.'
            BLACK 'Releasing pheromones.'
            'After a minute or two, I suddenly began to notice Shani slowly pushing herself to slide back and forth onto my cock, and despite spluttering with some discomfort, she shakily began to slowly build up speed.'
            SHANI 'T-Things are starting to feel a little b-better.'
            SHANI 'It’s - Ah... Starting to feel kinda nice~'
            BLACK 'Her body is adapting well, now to push the dopamine.'
            SHANI 'Oh fuck! Ah! Mmmfgh!'
            SHANI 'M-Move faster, this is - Oooh!'
            SHANI 'F-Fuck! It still burns but... But it’s starting to feel... amazing!'
            'Wasting no time, I began to thrust deeply into Shani tight ass, listening to her grunt and moan in pleasure as she threw her soft round butt back onto me.'
            'As I dug my hands into the soft flesh of her ass, she cried out in pleasure, moaning while I took her more and more like a wild animal.'
            BLACK 'Good... Feel me coursing through you.'
            SHANI 'Fuck me! Fuck my ass like a slut!'
            SHANI 'I fucking love it!'
            'Shani’s body felt like it was burning up and so did mine, as she shivered and tightened around my cock, I lost track of the orgasms I had given her.'
            SHANI 'F-Finish in my ass! I want to feel you fill up my ass!'
            "Hearing Shani's depraved words, I could hold back no longer, and pulling her to the hilt of my cock I held her there while I gritted my teeth and flooded her bowels with my hot seed."
            $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
            scene shani_doggy_anal_finish with flash
            $ ReduceInfectionFromSex("shani")
            $ UnlockGalSceneAndGrantXp("shani", "doggy")
            $ UnlockGalFlag("shani", "doggy", "var_anal")
            $ Pause()
            MC @talk 'A-Ahh! Fuck!'
            SHANI 'So hot... So much of it... Gods...'
            SHANI 'My head feels like it’s spinning!'
            "As Shani's legs began to buckle, I had to catch from falling as she tried to stand back up and compose herself."
            SHANI 'I haven’t been fucked like that in years...'
            SHANI 'Phew... Come on, we need to get back before *huff* someone sees us.'
            SHANI '...Or I collapse.'
            $ AutoMus(True)
            $ store.curDialogue = "DNodeExit"
            $ LocFlush()
            return
        "There was something else...":
            SHANI @angry "Oh, thank god."
            return

label shani_sexmenu_leave:
    SHANI 'As you wish...'
    return

# bye
label shani_bye:
    $ rng = RngInt(1,3)
    if rng == 1:
        SHANI "Suit yourself, honey."
    if rng == 2:
        SHANI "Hmph, your loss."
    if rng == 3:
        SHANI "I'll be waiting for you."
    return
