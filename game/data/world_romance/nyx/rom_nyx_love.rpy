######### LOVE ROUTE
label rom_nyx_love_1:
    if day < QstGetDelayVal(RomanceNyx):
        MC "Nyx isn't here. I'll try tomorrow."
        $ LocSet("novaras_fort_seb_barracks")
        $ LocEnterQ()

    $ NoteLock("romanceNyxLove1")

    #Player returns to speak to Captain Nyx
    show nyx angry at center_f with dissolve
    "Upon entering into her Office, Nyx stormed over angrily towards me, hands balled up into fists."
    NYX @angry "Was I not clear before?"
    NYX @angry "What in the seven hells are you doing here?"
    MC @talk "I came here to speak to you."
    NYX @think "About what? There is nothing to discuss."
    menu:
        "Come with me tonight to the {i}Iron Unicorn.{/i}":
            show nyx shock
            NYX @shock "E-Excuse me?"
            MC @talk "You can't work all the time; you need a break every once in a while."
            NYX @angry "Are you even hearing yourself?!"
            show nyx arrogant
            NYX @arrogant "I'm the captain of the city guard ... Not some peasant girl you're courting!"
            MC @smile "And does the captain of the city guard never take a day-off?"
            NYX @arrogant "My duties and responsibilities come first."
            MC @talk "Surely you can't fulfil those duties as well without taking a break every now and then?"
            show nyx angry
            NYX @angry "Must you persist in this matter?"
            MC @smile "Because I care about you."
            show nyx blush
            "Nyx blushed at the comment, grumbling beneath her breath how 'stupid' I was being while averting her gaze."
            NYX @think "{i}*Sigh*{/i}"
            show nyx angry
            NYX @angry "What if someone sees me, hm? How do you propose I explain that one?"
            MC @talk "Am I supposed to believe you're incapable of disguising yourself?"
            MC @talk "Outside of that armor, how many are honestly going to recognize you?"
            show nyx think
            NYX @think "...Fine, FINE!"
            NYX @angry "But push aside silly notions of this being anything more than a chance for me to take a break from work."
            NYX @think "What happened last time {i}won't{/i} happen again."
            MC @smile "If you say so."
            NYX @angry "Don't be so-"
            NYX @think "You know what? Forget it, I will see you at the {i}Iron Unicorn{/i} this Evening."
            MC @smile "I shall see you then."

            scene black with dissolve
            $ LocSet("novaras_fort_seb_barracks")
            $ QstSetProgress(RomanceNyx, 2)
            $ NoteUnlock("romanceNyxLoveUnicorn")
            $ LocEnter()

        "You're right, we should keep things professional. {image=[ICON.HEART_CROSS]}":
            show nyx shock
            "Nyx seemed surprised at the comment, but quickly returned to her usual self."
            NYX @think "Y-You agree?"
            show nyx sad
            NYX @sad "Right, well, yes ... It's for the best."
            MC @talk "Are you alright?"
            NYX @sad "I'm fine, now, if that's all you came to say you can go."
            NYX @think "And the two of us can forget this little 'incident' ever happened..." #Ends romance

            scene black with dissolve
            $ LocSet("novaras_fort_seb_barracks")
            $ QstFail(RomanceNyx)
            $ LocEnter()


label rom_nyx_love_unicorn_date:
    $ NoteLock("romanceNyxLoveUnicorn")

    $ LocFlush()
    show mc think at cleft:
        xzoom -1.0
    with dissolve

    #Player enters the Iron unicorn - Option appears on screen to click 'Wait for Captain Nyx to join you...'
    "I looked around for any sign of Captain Nyx, to no-avail."
    MC "(Hm ...Maybe she really isn't coming.)"
    $ CharSetClothes("nyx", "robe")
    show mc think at cleft
    show nyx at cright_f
    with dissolve
    "In that moment I felt someone nudge up against me, and as I turned, I looked to see a robbed figure stood before me."
    show mc smile
    "As she tilted her head up, I could see clearly through the hood it was Captain Nyx."
    MC @smile "Ah! Captain-"
    NYX @angry "Shh! Not so loud!"
    MC @smile "Ahh ... That explains the disguise then."
    "Nyx sighed uneasily, looking around the tavern for signs of anyone she recognized."
    NYX @think "Why did you choose to bring me here?"
    NYX @think "There are too many people."
    MC @talk "Relax, Nyx."
    MC @talk "We're here to have some fun, remember?"
    NYX @talk "Right, yes ...'fun.'"
    MC @talk "What are you drinking?"
    NYX @talk "Ale."
    MC @talk "Two ales, coming up..."

    #Fade to black - text appears on screen - 'a short while later...'
    call center_text(_("A short while later...")) from _call_center_text_4

    #MC and Nyx are holding drinks 
    $ CharSetClothes("nyx", "robe_mug")
    $ CharSetClothes("mc", "mug")
    $ LocFlush()
    show mc at cleft
    show nyx at cright_f
    'Nyx took a sip of the ale in her cup and smiled.'
    NYX @laugh "Have to admit, I can't remember the last time I drank this much..."
    MC @smile "Are you trying to tell me the great Captain Nyx can't handle her drink?"
    show nyx blush
    'Nyx seemed flustered at my comment.'
    NYX @blush "I enjoy a glass of wine sometimes alone in my chambers..."
    show nyx
    NYX @talk "If any of the men actually saw me drunk and in disarray, they'd-"
    MC @talk "Nyx, don't you think that perhaps you're holding yourself to an unreasonable standard?"
    MC @talk "The men would have seen their own commanders drunk at least a thousand times."
    NYX @angry "Their {i}male{/i} commanders."
    NYX @angry "For them, such a thing is fine, but for me? One of the first female Captains? My enemies would just use it against me..."
    'Nyx paused for a moment, looking around uneasily for anyone she might recognise.'
    MC @sad "...It must get tiresome, being paranoid all the time."
    MC @think "Always having to keep your guard up like that."
    NYX @talk "Mmm, it's difficult."
    MC @talk "...And lonely."
    NYX @sad "..."
    NYX @talk "Enough dwelling on me, tell me about you."
    MC @talk "Me?"
    NYX @talk "Yes, {i}you.{/i}"
    NYX @talk "Not only are you a curiosity given your 'gift,' you've successfully dragged me out here on a night out."
    NYX @talk "Can't a girl at least be a little curious?"
    MC @smile "You weren't curious before."
    NYX @talk "That was business, this is supposed to be leisure ... Now, I'm curious."
    MC @talk "What do you want to know?"
    NYX @talk "First, tell me a little about yourself."
    NYX @talk "I take it you didn't plan to go into the Scouts, hardly anyone ever does ... So, what did you want to be?"
    menu:
        'In truth, I just wanted a paperwork job within the royal Palace.':
            NYX @shock "Really?"
            NYX @talk "That's... surprising."
            MC @talk "How so?"
            NYX @talk "You carry yourself as an Adventurer so well, I just thought you'd have wanted a more ..."
            NYX @talk "Never mind, it's not like I can hardly blame you for wanting a job like that."
            MC @talk "I figured you'd be disappointed by that answer."
            NYX @laugh "Not at all, if anything, we could do with more {i}effective{/i} people running administration."
            "Nyx's face became solemn."
            NYX @talk "Besides ... You and I both know what it's really like out there."
            NYX @talk "I could hardly blame anyone for wanting to stay as far away as possible from that."
            NYX @talk "Well, onto my next question!"

        'I wanted to be an Adventurer.':
            NYX @talk "Ahhh ... That fits."
            NYX @talk "Well, you've certainly taken well to the role it seems."
            MC @talk "Growing up, we'd all heard about the greats, {i}Sir Gregor Iron hands, Marcella the wise,{/i}I guess I couldn't help but be a little inspired."
            "Nyx laughed."
            NYX @talk "I used to beg my father to read me stories about the golden age of heroes."
            NYX @talk "{i}Eris of the Golden Dawn, Viletta the charmer.{/i}"
            MC @talk "Are they the reason you became Captain of the city guard?"
            'Nyx laughed once more.'
            NYX @talk "I can't say they were the {i}only{/i} reason, but ... They certainly had an impact on me."
            NYX @talk "Anyway, onto my next question then!"

        'I wanted to work at the brothels.':
            show nyx think
            'Captain Nyx nearly spat up her drunk.'
            NYX @think "Oh be serious!"
            MC @smile "What? It's true!"
            show nyx
            MC @talk "I'm much more of a lover than a fighter I think."
            NYX @talk "But working in a brothel? Seriously?"
            NYX @talk "Don't all boys growing up usually dream about adventure and how they're gonna be the next Newheart?"
            MC @smile "I was content with the idea I could prove my mettle enough in the bedroom rather than the battlefield."
            show nyx blush
            "Nyx took a sip of her drink, her cheeks flushed red at the comment."
            NYX @blush "A-Anyway, moving on..."
            show nyx

    #All choices continued 
    NYX @talk "Okay, here's one."
    NYX @talk "What do you wanna be now?"
    NYX @talk "I mean, some would already say you've done the impossible..."
    NYX @talk "But you tell me."
    menu:
        "I'd like to just settle down, hopefully comfortably, with someone I love I think.":
            NYX @blush "That sounds nice..."
            NYX @talk "I mean, dreadfully boring, but nice."

        "I'm not sure ... I guess I'll just see how things play out.":
            NYX @talk "Ah, well..."
            NYX @talk "I suppose I should have expected that answer."
            NYX @talk "Your whole world has pretty much been flipped in the last few months since the scouts."
            NYX @talk "Can't expect too much, I suppose."

        "Power is everything ... And I intend to grab as much of it as I can.":
            NYX @talk "Ambitious, aren't we?"
            NYX @talk "Just try and remember a lot of people have been in that game a lot longer than you."
            NYX @angry "Fuck around, and one of them will soon push you down into the shit."

    #All choices continued 
    MC @smile "Why do I feel like I'm being interrogated?"
    NYX @blush "I have no idea what you're talking about, anyway, answer the next question."
    NYX @talk "... Why um ... Why me?"
    MC @surprised "Why you?"
    NYX @talk "I mean, there are other women..."
    NYX @talk "Most men think I'm about as friendly as having the sharp end of a blade shoved up your arse."
    menu:
        "I think you're funny.":
            show nyx think
            "Nyx became wide-eyed in disbelief."
            NYX @think "Funny? FUNNY?"
            NYX @angry "In what world am I funny?"
            NYX @think "The last time I tried to tell a joke, it ended with twenty recruit guards stark-bollock naked training in the rain and mud!"
            "I couldn't help but laugh, and a befuddled Nyx nervously smiled as she took another sip of her drunk."     
            show nyx
            MC @surprised "How did that happen?"
            NYX @talk "One of those fools complained to me that his armour was too heavy, so he asked if he could train with something lighter on."
            NYX @talk "So I told him, the only alternative was to strip and fight naked as part of our 'lightning speed' strike division."
            NYX @talk "Next thing I know, I come back, and ALL the silly bastards are training naked!"
            NYX @talk "I'd never seen so much cock and balls in my life!"
            "I couldn't help but laugh again."
            MC @smile "See? You're funny."
            NYX @blush "Gods, you're a strange one."

        "That's why I like you, you're unlike any woman I've ever met before.":
            NYX @blush "Gods ... Stop."
            NYX @angry "You use that line all the time, don't you?"
            MC @smile "All the time."
            show nyx smile
            "Nyx pouts cutely."
            show nyx
            MC @talk "But I think I mean it this time; you really are different."
            MC @talk "Most women-"
            NYX @laugh "Don't make half the men you meet look like spineless cunts?"
            MC @talk "I was going to say don't have quite such a foul mouth, but that too."
            NYX @talk "Thanks, but also fuck you, my mouth isn't foul!"

    #Either choice continued 
    NYX @talk "{i}*Sigh*{/i} Well, I guess it's fair you get to ask me some questions back."
    NYX @talk "So ... What do you want to know?"
    $ choicemenu = set()
    menu nyx_love_unicorn_date_menu:
        "Have you ever been in love before?" if 'love' not in choicemenu:
            $ choicemenu.add('love')
            NYX @talk "... Fuck, you always come out swinging like that?"
            'Nyx paused for a moment to take a sip of her drink.'
            NYX @talk "No, can't say I have."
            NYX @think "Came close once though."
            NYX @talk "My father tried to marry me off when I was young once, the engagement was quickly called off when I broke my supposed fiancé-to-be's nose."
            MC @talk "What did he do?"
            NYX @angry "When I didn't put out, I caught him balls deep in the town slut one night."
            NYX @think "Well, it wasn't a pretty sight."

            jump nyx_love_unicorn_date_menu

        "Do you like your job?" if 'job' not in choicemenu:
            $ choicemenu.add('job')
            NYX @talk "Do I like it?"
            show nyx think
            'Nyx seemed perplexed by the question.'
            show nyx
            NYX @talk "...Yes, I think I do."
            NYX @think "Even if I complain about the sheer volume of incompetence all the time."
            NYX @sad "Truth is, I've never made a very good {i}girl.{/i}"
            NYX @sad "Always in fights, always getting up to trouble, always ..."
            'Captain Nyx sighed.'
            NYX @sad "Always being trouble for my parents."
            NYX @talk "So, when the chance finally came to do something that I was good at, I just threw myself into it."
            MC @talk "Must have been hard ... Earning respect I mean."
            NYX @think "Mmm, you have no idea."

            jump nyx_love_unicorn_date_menu

        "Where are you parents now?" if 'parents' not in choicemenu:
            $ choicemenu.add('parents')
            NYX @think "Hm? They're fine, they live in Newyark."
            NYX @talk "Father makes his living fixing up the boats in the dock."
            NYX @talk "Mother mostly stays at home, but she writes to me often."
            MC @talk "Sounds like you get on well with them."
            NYX @think "Ha ... Well, kind of."
            MC @talk "Kind of?"
            NYX @think "They've never really fully accepted what I do."
            NYX @think "In their eyes, I should be married and bringing them a couple grandchildren."
            MC @talk "Who's to say you can't do both?"
            show nyx laugh
            'Nyx laughed.'
            NYX @laugh "Can you really imagine me as a mother? Gods ... I'd be terrible."
            show nyx
            MC @talk "Really? I think you'd be pretty good myself."
            show nyx blush
            'Nyx blushed slightly as she brushed her hair back with her hand.'
            NYX @blush "Umm, if you say so..."
            show nyx

            jump nyx_love_unicorn_date_menu

        "I think I've asked enough questions.": #continues on
            NYX @talk "Well then, what should we do now?"
            MC @smile "How about another round?"
            NYX @laugh "Are you trying to get me drunk to seduce me?"
            NYX @laugh "I won't fall for such tricks!"

    #Cut to black - text appears on screen - a couple hours later...
    call center_text(_("A couple hours later...")) from _call_center_text_5

    $ LocFlush()
    show mc at cleft
    show nyx drunk at cright_f

    NYX @drunk "Zhoo ... Whatdya mean you don't exphect me to mhake the fhirst move?"
    NYX @angry "ARE YHUU TRYNAA SAY SOMETHIN?"
    MC @smile "Haha, no, Nyx."
    NYX @drunk "Zhat's Chapthain to yhuu!"
    MC @smile "No, {i}Captain Nyx.{/i}"
    MC @smile "Just I know you have a lot of reservations, so I don't expect you to try something crazy."
    "Nyx stared drunkenly towards me. her eyes blinking slowly as she places her half empty drink down onto the table."
    NYX @drunk "G-Give me a moment...Mhm!"
    "Nyx stumbled off for a moment, nearly crashing into one of the tables before she managed to make her way successfully towards one of the privies."
    "A short while, she returned with a contently smug expression."
    MC @think "Is everything okay?"
    NYX @drunk "Mhmm! Lhet's go, it's thime I went home."
    MC @talk "Alright, I'll walk you back as far as you want."

    #Cut to black 
    scene black with dissolve

    $ LocSet("novaras_dist_market")

    'Walking Nyx back, she clinged unusually tight to my arm, pressing her breasts up against me as she kept looking up towards me.'
    "As we were passing through one of the City's darkened alleyways, Nyx suddenly stopped."

    #Cut to alleyway 
    $ CharSetClothes("nyx", "robe")
    $ CharSetClothes("mc", "normal")
    scene bg_alleyway_night
    show mc at cleft
    show nyx drunk at cright_f
    with dissolve

    NYX @drunk "W-Wait a minute."
    MC @talk "Nyx? What is it?"
    NYX @drunk "Yhuu shaid, I whouldn't dhuu nothin' chrazy."
    NYX @drunk "S-Shuu, I umm ..."
    NYX @drunk "{i}Did somethin' chrazy.{/i}"
    MC @think "Nyx? What did you do?"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ HideUI(True)

    scene ss_nyx_alleyway_show_everything with dissolve
    $ Pause()
    "With a drunken smile, Nyx undid her robes to reveal her luscious naked body beneath."
    NYX "Fufu~ ??"
    MC "N-Nyx! You're-"
    NYX "Shhhhh! Dhon't shay my nhame shoo lhoud."
    MC "Uhh, r-right, of course."

    scene ss_nyx_alleyway_looking with dissolve
    $ Pause()
    "Down on her knees, Nyx greedily tugged at my belt with her fumbling." #Cut to animation(s)
    NYX "Mhm! G-Ghive it to me alhready!"
    NYX "I want your cock!"
    NYX "That'sha order!"
    MC "You're ordering me to get my cock out for you?"
    NYX "Yeshh!"
    MC "...Alright then, as you wish, {i}Captain.{/i}"

    scene ss_nyx_alleyway_looking_dick with dissolve
    $ Pause()
    "With my hard cock pulled out in front of her, Nyx stared wide-eyed with her mouth hung open before her mouth curved into a perverse smile."
    NYX "Ghohds itshh evhen bhigger than I rhemember."
    MC "You’ve had quite a lot to drink..."
    MC "Are you sure you want to do this?"
    NYX "Shhhhh, Ivhve whanted thisss ALLLLL nhightt!"

    scene ss_nyx_alleyway_kiss with dissolve
    $ Pause()
    "Grabbing a hold of my cock Nyx playfully slapped it against her cheek before giving the head a soft kiss."
    NYX "It thastess salty!"
    MC "Well, I wasn’t expecting you to-"

    scene ss_nyx_alleyway_slap with dissolve
    $ Pause()
    "With her tongue out, Nyx slapped my cock against her wet tongue and giggled."
    "I groaned in pleasure at the sudden sensation, and Nyx remarked playfully,"
    NYX "Lemme chlean it."

    scene ss_nyx_alleyway_bj with dissolve
    $ Pause()
    "Before I could say another word, Nyx's mouth was wrapped around the head of my cock as she gently swrirled her tongue around the head."
    MC "Ahh...!"
    MC "{i}*Huff*{/i} N-Nyx..."
    NYX "{i}*Slurp!*{/i} Mmfghh! {i}*Slurp!*{/i}"
    "Inch by inch, Nyx takes my cock deeper into her mouth."
    "Her eyes under the dim moonlight look up towards me with neediness as her mouth coats my cock in her saliva."
    NYX "(My head ishh spinning so much.)"
    NYX "(Mhmmm, Heshh shooo bhigg.)"
    NYX "(Fufu, thishh BIG chockkk bhelongss to meee now. {image=[ICON.HEART]})"
    NYX "(NONE OF YOUU BHITCHESS CHAN HAVE ITHH!)"
    NYX "(Urghhh, but I whanttt ithh shooo bhaddd!)"
    MC "{i}*Huff*{/i} Fuck ... Nyx!"
    "Nyx's head continued to bop back and forward as her lips glided across my cock."
    "The hot sensation of her mouth was intoxicating, her tongue continued to clumsily bash and wrap itself around my cock as she moaned hotly."
    NYX "Mhmm...??"
    MC "Ahh! Wasn't expecting - Mhmm! This tonight!"
    NYX "{i}*Slurp!*{/i} Mhmm!"
    "Nyx's teeth lightly grazed me occasionally as she drunkenly pushed herself too far and too deeply, but her enthusiasm overcame any lack of experience."
    NYX "(I chanttt bhelieve I'm dhoingg thisshh.)"
    NYX "(Mhmmm, why'd he hashh to be sooo cute thoughh?)"
    NYX "(I can't sthoop thinkin' abhout lhasst thime.)"
    NYX "(What's happeningh to mee?)"
    'As Nyx continued, her head now rhythmically bouncing as she swallowed my cock as deeply as she could,'
    "I soon began to feel the overwhelming urge to finish quickly building, and I knew I couldn't hold on much longer."
    MC "{i}*Huff*{/i} I'm c-close..."
    "I said with gritted teeth, my hands coiling into fists as my member became increasingly sensitive and my balls felt like they were tightening."
    "As Nyx continued her lewd, drunken, loving blowjob, I heard the sounds of movement coming from behind."
    scene ss_nyx_alleyway_bj_guards with dissolve
    $ Pause()
    GUARD "I can't believe the rota assigned us night patrol for the THIRD night in a row!"
    SECOND_GUARD "You heard the captain's orders, with the chaos going on with the Vulshan and the Khazahs, everyone's having to do more patrols than before."
    SECOND_GUARD "Everyone does at least two night shifts in a row now."
    MC "(Shit shit! The guards!)"
    NYX "Mhmm?"
    NYX "(Thoshh vhoicesss shound familiarr?)"
    NYX "{i}*Slurp!* *Slurp!*{/i}"
    GUARD "That's all well and good, but my fucking balls feel like they're going to explode if I don't find some whore soon to deal with them!"
    SECOND_GUARD "Aren't you married? Get your wife to suck your cock when you're home and stop whining!"
    GUARD "Bah, she's never in the mood..."
    GUARD "Besides, I'm in the mood for a long-haired blonde with a fat ass."
    SECOND_GUARD "...Like the Captain?"
    GUARD "Course! What I wouldn't give to bend her over that desk and ram that fucking ass! Haha!"
    NYX "{i}*Slurp!*{/i} Mhmm?"
    NYX "(Are theyyy thalkinggg about myy arse?)"
    NYX "(Thoseeee FUCKS! I'll have them bhothhh do an extrah shift for thattt!)"
    MC "(Fuck! FUCK! They're so close! They're gonna see her!)"
    "As the guards drew closer and closer, one of them no doubt finally noticed our silhouettes."
    GUARD "OI! WHO GOES THERE?!"
    MC "(Shit!)"
    "Nyx almost obliviously continued to suck on my cock, her glossy eyes looking up to me in drunken adoration and lust."
    "Deciding there was only one thing to do, I reached around to grab the back of her head."
    "Nyx's eyes widened in surprise as I pulled her head forward."
    "Her cold nose pressed up against my pubic hairs as she let out a little surprised 'Mhmm!' taking my cock suddenly to the hilt."
    "As she squirmed and gagged, the sudden sensation was too much."

    scene ss_nyx_alleyway_finish with flash
    $ ReduceInfectionFromSex("nyx")
    $ Pause()
    "Gripping her hair, I flooded her mouth with the hot, heavy load which she desperately tried to swallow down."
    "The two guards approached, unable to see Captain Nyx's face as she tapped against my leg for air."
    MC "Uhh, we'll just be finishing - ahh! Up now..."
    MC "(Go away, go away, go away!)"
    "The two guards smirked and looked at each other before passing by and laughing."
    SECOND_GUARD "Be gone by the time we get back!"
    "Feeling Nyx's taps against my leg become weaker and weaker, I quickly pulled her off from me, allowing her to gasp for air."
    "She coughed up some of my warm seed onto the floor, shaking as she looking up weakly towards me."
    NYX "You - {i}*Cough!*{/i} Couldha khiled meee! {i}*Cough!*{/i}"

    $ UnlockGalSceneAndGrantXp("nyx", "alleyway")
    $ HideUI(False)
    $ AutoMus(True)

    scene bg_alleyway_night
    show nyx drunk at cright_f
    show mc at cleft
    with dissolve
    "I helped the drunk Nyx back to her feet."
    MC @surprised "Sorry, I had to make sure the guards didn't see you."

    show mc at center with easeinleft
    "Nyx wiped her mouth clean, and nearly stumbling over, I reached out to quickly grab her."
    MC @talk "Easy!"
    NYX @drunk_sad "Mmmm, I t-think that'sh enough for one nightt."
    NYX @drunk "T-Take me back to my room."

    scene black with dissolve
    "Making sure to hold on and lead Nyx safely, she followed clumsily from behind as I lead her back to the fort." #Cut to black
    MC "Which way is your room, Nyx?"
    NYX "Mhmm, thish whayy."
    "Leading Nyx to her room, she reached into her pocket and with a fumbling hand pulled out a key which she failed several times to put into the lock."

    play sound wooden_door_open_3
    $ LocSet("novaras_fort_seb_captains_bedroom")
    "Taking the key, I opened the door for her."

    $ LocFlush()
    show mc at cleft
    show nyx drunk at cright_f
    with dissolve
    NYX @drunk "Thankshh." #Cut to Nyx room 
    $ CharSetClothes("nyx", "naked")
    show nyx at blurin, nod
    "In an instant, Nyx threw off her robes as she laid down onto her bed."
    hide nyx with dissolve
    "Her room was unsurprisingly minimalist, with very little beyond the bare essentials."
    "A desk with a quilt overflowing with paperwork by the window, a wardrobe to the side with a hulking chest in front of her bed."
    "Some armor perched up on a stand and a few weapons kept nearby."
    show mc at left with easeinleft:
        xzoom -1.0
    show mc at nod
    "As I turned to leave, Nyx drunkenly called out."
    show mc:
        xzoom 1.0
    NYX "Nhhuuu."
    MC @talk "What?"
    NYX "S-Stahyy."
    NYX "I want chuddles."
    "Nyx waits with drunken impatience in her bed for me to join her, patting at the bed alongside her."
    MC @talk "Is that an order too?"
    NYX "Yeshhh!"
    $ CharSetClothes("mc", "naked")
    show mc at blurin, nod
    "I sighed, smiling towards her as I began to take off my armor."
    "She was a demanding drunk, but a surprisingly adorable one."
    show mc at cleft with easeinleft
    scene black with dissolve
    "Slipping into the bed alongside her, Nyx rested her head on my chest before dreamily begining to drift off to sleep." #Cut to black
    NYX "Pleasheee ... Stahyyy from nowh on."
    NYX "I feelshsoo, {i}lonely...{/i}"
    "And like that, Nyx was asleep."
    "Gently, I stroked her hair softly till I too, began to drift off."

    scene black with Dissolve(1.0)
    $ Pause(0.5)
    $ TimeAdvTo(TIME_MORNING)
    $ CharSetClothes("mc", "pants")
    $ LocFlush()
    show mc at center
    with Dissolve(1.0)

    #Cut to morning
    "As I open my eyes, I sit-upright to find I'm alone in Captain Nyx's bed."
    MC @talk "Nyx?"
    $ PlayerAddItem("qst_nyx_room_key", 1)
    "Beside the bed, a small note is left with a key beside it."

    "{i}I didn't want to wake you, I've been called to deal with some urgent work at once.{/i}"
    "{i}Thank you for last night, I didn't realise how much I needed it.{/i}"
    "{i}...And thanks for the worst hangover I've had in years.{/i}"
    "{i}Come see me soon, please... We have much to discuss.{/i}"
    "{i}-Nyx{/i}"

    MC "(I should give it a day or so before trying to visit Nyx again.)"
    MC "(Give her time to deal with her work and think about what happened.)"
    MC "(Damn, what a night!)"

    scene black with Dissolve(1.0)
    $ Pause(0.5)

    $ QstSetProgress(RomanceNyx, 3)

    $ CharSetClothes("nyx", "normal")
    $ CharSetClothes("mc", "normal")

    $ LocSet("novaras_fort_seb_barracks")
    $ LocEnter()
