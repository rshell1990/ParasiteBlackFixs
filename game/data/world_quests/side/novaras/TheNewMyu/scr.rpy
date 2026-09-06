label qst_NewMyu_0_gotRolls:
    MC "(Alright, I should be able to buy a bottle of wine from the {i}Iron Unicorn{/i}.)"
    $ QstSetProgress(QstNewMyu, 1)
    $ LocEnterQ()

label qst_NewMyu_1_buyWineShay:
    SHAY @smile "A bottle of wine huh?"
    SHAY @smile "What are you celebrating?"
    MC @talk "Not sure yet, a uh, {i}'friend'{/i} of mine wants some."
    SHAY @smile "Well, look at you!"
    SHAY @talk "Don't wanna keep the lucky girl waiting, do we?"
    SHAY @smile2 "Two hundred-fifty coins for the wine and its all yours."
    menu qst_NewMyu_1_buyWineShay_menu:
        "I'd be eternally grateful if you could sell me that wine a little cheaper." (Req_Charm = 6) if not QstNewMyu().haggledWine:
            $ QstNewMyu().haggledWine = True
            $ QstNewMyu().winePrice = 200
            SHAY @talk "... Fine."
            SHAY @talk "You're lucky you're so good looking, you know that?"
            SHAY @talk "Two hundred coins, and not one less!"
            jump qst_NewMyu_1_buyWineShay_menu

        "Here you go." (Req_Gold = QstNewMyu().winePrice): # swap with wine-price quest-tied var
            $ PlayerRemItem("gold", QstNewMyu().winePrice)
            $ PlayerAddItem("qst_wine_bottle")
            SHAY @smile "Hope she's worth it!"
            $ QstSetProgress(QstNewMyu, 2)
            $ LocEnter()
        
        "I'll be back.":
            $ QstNewMyu().shayWineRevisit = True
            SHAY @talk "No problem, I'll keep it back here for you."
            $ LocEnter()

label qst_NewMyu_1_buyWineShay_revisit:
    SHAY @talk "Don't wanna keep the lucky girl waiting, do we?"
    if QstNewMyu().haggledWine:
        SHAY @smile2 "Two hundred coins for the wine and its all yours."
    else:
        SHAY @smile2 "Two hundred-fifty coins for the wine and its all yours."
    menu qst_NewMyu_1_buyWineShay_revisit_menu:
        "I'd be eternally grateful if you could sell me that wine a little cheaper."  (Req_Charm = 6) if not QstNewMyu().haggledWine:
            $ QstNewMyu().haggledWine = True
            $ QstNewMyu().winePrice = 200
            SHAY @talk "... Fine."
            SHAY @talk "You're lucky you're so good looking, you know that?"
            SHAY @talk "Two hundred coins, and not one less!"
            jump qst_NewMyu_1_buyWineShay_revisit_menu

        "Here you go." (Req_Gold = QstNewMyu().winePrice):
            $ PlayerRemItem("gold", QstNewMyu().winePrice)
            $ PlayerAddItem("qst_wine_bottle")
            SHAY @smile "Hope she's worth it!"
            $ QstSetProgress(QstNewMyu, 2)
            $ LocEnter()

        "I'll be back.":
            SHAY @talk "No problem, I'll keep it back here for you."
            $ LocEnter()

label qst_NewMyu_2_returnMyu:
    MYU @joy "Great!"
    $ PlayerRemItem("qst_sweet_roll")
    MYU @talk "Myu try now?"
    $ PlayerRemItem("qst_sweet_roll")
    MC @smile "Sure, Myu, just don't-"
    if PlayerItemQty("qst_sweet_roll") > 0:
        $ PlayerRemItem("qst_sweet_roll")
    'Myu snatched one of the sweet rolls from me and began to shovel it into her mouth.'
    MYU @joy "Mmm! So much sugar!"
    MC @smile "You like it?"
    MYU @smile "Uhuh, Myu try wine?"
    $ PlayerRemItem("qst_wine_bottle")
    'I handed Myu the wine and she began to gulp at the bottle.'
    'I could see the red fluid inside of her pouring into her semi-translucent body.'
    'I had to snatch the bottle back off her to stop her trying to gulp the whole thing.'
    MC @surprised "Easy, Myu, easy!"
    MYU @blush "Ahh! It tastes {i}weird!{/i}"
    MC @talk "Well, what do you think?"
    MYU @blush "Myu... Not sure."
    MYU @blush "Feel kinda, {i}funny.{/i}"
    MYU @blush "{i}*Giggles*{/i} Hehehe!"
    MC @talk "I think you might be a little drunk, Myu."
    MYU @joy "Whaaaaa...?!"
    MYU @blush "Myu only had a little!"
    MC @talk "Myu, has never drunk alcohol before."
    'Myu pouted at the comment, but quickly, she was stumbling around the room struggling to stand.'
    'Soon after, she tripped herself up, and I had to catch her quickly from falling.'
    MC @surprised "Myu!"
    MYU @blush "Hehe! Everything is spinning!"
    MC @talk "Just relax for a moment."
    "Myu's expression suddenly changed as she stared wide-eyed at me, reaching to cover her mouth."
    MC @sad "Myu? What's-"
    'Myu began to hurl violently, purging the sweet roll and wine from her body.'
    MC @surprised "Myu!"
    MYU @sad "Urghh..."
    MC @sad "Myu, are you okay?"
    MYU @smile "M-Myu is fine!"
    MYU @sad "J-Just drank a little-"
    'Myu hurled once again.'
    MC @sad "Myu, when was the last time you ate?"
    MYU @sad "Myu, {i}*Huff*{/i} is fine."
    MC @talk "We should take you hunting again soon, we can-"
    MYU @angry "MYU IS FINE!"
    MYU @scared "...Myu, doesn't want to hunt."
    show myu at center_f with ease
    MC @sad "Myu, what's-"
    MYU @angry "Leave Myu alone! MYU IS FINE!"
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    $ LocSet("azul_safehouse")
    'Myu violently shoved me out of her room.'
    $ LocFlush()
    show mc at cright
    with dissolve
    MC @angry "Myu!"
    show mc at blurin, cright_f
    MC '(...Shit!)'
    MC "(I should check on her later when I have a chance, find out what's going on here.)"
    $ QstSetProgress(QstNewMyu, 3)
    $ QstNewMyu().letMyuCoolDown = True
    $ LocEnter()

label qst_NewMyu_3_afterCoolDown:
    scene black with dissolve
    MC @talk "Myu, are you here?"
    MC @talk "We need to-"
    $ AutoMus(False)
    scene cg_slime_dinner with flash
    $ PlayMusic("audio/ambience_scenes/obelisks.ogg")
    "I stopped dead in my tracks, staring down at the pool of blood and some half torn apart man laid motionless on the floor."
    "Myu's tendrils worked to drain the blood as his raw wet flesh was dissolving inside of her."
    'When she finally looked up to see me, in a panic she changed her form once again.'
    $ LocFlush()
    show mc at cleft
    with dissolve
    show myu at cright_f with easeinright
    MYU @scared "N-Not what it looks like!"
    MYU @scared "He was trying to steal! Said he would hurt Myu!"
    MC @surprised "Myu... Where the fuck did you-"
    MYU @scared "M-Myu found outside!"
    MYU @scared "Don't be mad! Don't be mad at Myu!"
    MYU @scared "Myu's not bad! MYU ISN'T MONSTER!"
    MC @sad "Myu, what are you-"
    hide myu with easeoutleft
    "In a complete panic, Myu barged past me, dissolving away into a pool of liquid again as she slide under the door and made her way outside..."
    show mc at cleft_f, blurin
    MC @surprised "MYU!"
    scene black with dissolve
    $ LocSet("azul_safehouse")
    $ LocFlush()
    with dissolve
    show mc at center_f with easeinright
    MC '(Fuck! FUCK!)'
    MC '(Where could she have gone?)'
    $ CharSetVar("myu", "hide", True)
    $ AutoMus(True)
    $ QstSetProgress(QstNewMyu, 4)
    $ LocEnter()

label qst_NewMyu_4_findMyuChurch:
    show mc at cleft with easeinleft
    if QstNewMyu().churchFirstTime:
        MC '(Huh? What is this?)'
        show mc at nod
        'I picked up the note on the door.'
        '{i}All services have been suspended for the day. Thank you.{/i}'
        MC '(I wonder if...)'
    else:
        'The note said, {i}all services have been suspended for the day. Thank you.{/i}'
        MC '(I wonder if...)'
    menu:
        'Knock on the door':
            pass
        'Step away from the Church':
            MC "(I should check on this place later.)"
            $ QstNewMyu().churchFirstTime = False
            $ LocEnter()
    show mc at center with easeinleft
    play sound "audio/cfx/door_knock.ogg"
    MC @talk "Hello! Is anyone there?"
    show mc at cleft with easeoutleft
    show kylisa at cright with easeinright
    if QstGetProgress(DialogueKylisa) == 0:
        KYLISA @smile "We meet again, [player_name!t]."
        MC @surprised "Wait, I know you, you're-"
        KYLISA @talk "Kylisa, the royal mage."
        KYLISA @talk "I was there when you were brought into the Hospital to check you for any Demorai taint."
        $ QstSetProgress(DialogueKylisa, 1)
    else:
        KYLISA @talk "Can I help you with something?"
        KYLISA @talk "There're no services today."
        MC @talk "I... No."
        KYLISA @talk "Then you should-"
    ################# cont
    'I heard a soft voice calling from inside the Church hall.'
    MYU "It's okay..{i}*Sniff*{/i} It's him."
    KYLISA @sad "Ah..."
    KYLISA @talk "Your {i}friend{/i} said you would look for her."
    MC @sad "What is Myu doing in there?"
    KYLISA @sad "I found the poor thing sobbing in the pews telling me she was a monster over and over again."
    KYLISA @sad "So, I canceled the services for today."
    $ choicemenu = ["a"]
    menu qst_NewMyu_4_findMyuChurch_menu:
        "Why did you help Myu?" if "a" in choicemenu:
            $ choicemenu.remove("a")
            KYLISA @angry "Because some of us can still remember when times were better and we fought back against the over-reach of the inquisitors."
            KYLISA @talk "The inquisitors destroy whatever they fear, but there was a time we strived to understand different races."
            KYLISA @talk "I must admit, I was a little taken aback at first by a slimelark, but our faith is not one to turn away the weary, whoever or whatever they may be."
            jump qst_NewMyu_4_findMyuChurch_menu
        "May I enter to see her?":
            KYLISA @talk "Of course, but be gentle with her."
            KYLISA @talk "She's quite... fragile."
    #######################################################
    hide mc with easeoutright
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/37_Rooftops.ogg")
    $ LocSet("novaras_church")
    $ LocFlush()
    show myu at right_f
    with dissolve
    show mc at center with easeinleft
    "When I entered the Church, Myu continued to cry softly, and when she saw me she stood up and slowly approached anxiously."
    show myu at cright_f with easeinright
    MYU @sad "...Myu feels like such a fool."
    MC @sad "Myu, what happened back there?"
    MC @talk "Why were you feeding on someone in your room?"
    MC @talk "Why didn't you just tell me you wanted to hunt?"
    'Myu fumbled on her words, struggling to get out what she wanted to say.'
    MYU @sad "{i}...Myu wanted to show you she could be normal.{/i}"
    MYU @sad "{i}Myu wanted to prove she wasn't a monster...{/i}" 
    MYU @sad "So Myu tried eating like everyone else."
    MYU @sad "But it just kept making Myu more and more sick."
    MYU sad "Till Myu was soooo hungry."
    MYU @sad "Myu couldn't stop herself anymore... All Myu could think about was food."
    MYU @sad "Myu saw the way you looked at her last time, Myu  so... {i}dirty.{/i}"
    MYU @sad "Myu didn't want you to feel dirty again, no matter how hungry she got."
    MYU @sad "So, Myu hunted alone, wanted to hide it from you so you wouldn't see Myu like that again."
    'Myu began to sob.'
    MC @sad "...Oh, Myu."
    'I gently wiped away one of her tears.'
    MC @sad "Listen to me, Myu."
    MC @think "Everyone has... {i}darkness{/i} inside of them."
    MC @talk "And sometimes, that darkness can be a little scary."
    MC @serious "But you're not defined by what you are, but {i}who{/i} you are."
    MYU @sad "...Is [player_name!t] scared of Myu?"
    MC @talk "...No, Myu."
    MYU @sad "W-Why?"
    MYU @sad "{i}You said Myu was a monster.{/i}"
    MYU @sad "Monsters are bad, monsters are the worst..."
    MC @talk "You're not a monster Myu... You're just a scared girl trying to understand a scary world."
    MC @talk "I'm sorry I made you feel the way you did, and truth is, you {i}did{/i} scare me a little."
    "Myu's eyes dropped to the floor dejectedly."
    MC @talk "But... That's okay."
    MC @smile "{i}Because I guess I'm kinda scary too sometimes.{/i}"
    MC @smile "And just because you're a little different, it doesn't make you a monster."
    MYU '...'
    hide mc
    hide myu
    show cg_myu_hug at center
    with dissolve
    "Myu leapt forward to hug me." #Myu hug art
    MC 'Whoa, easy now!'
    MYU '{i}*Sniff*{/i} Myu is ready to go home now.'
    MC "Come then, Myu, let's get you home."
    show kylisa at left with easeinleft
    KYLISA @talk "I take it all is resolved?"
    hide cg_myu_hug
    show mc at center_f
    show myu at cright_f
    with dissolve
    MC @smile "I think so."
    KYLISA @smile "Good."
    MC @talk "Thank you for helping her."
    MC @talk "I know many wouldn't."
    KYLISA @talk "I am sure one day in the future, you may return this act of kindness."
    KYLISA @talk "...Tell me something though."
    KYLISA @talk "Why are {i}you{/i} helping this slimelark?"
    menu:
        "I guess because it's the right thing to do?":
            KYLISA @talk "...Very well, as good an answer as any I suppose."
        "She is my companion.":
            KYLISA @talk "...I see."
            KYLISA @talk "Well I hope you and your companion chose wisely in this war and the wars to come."
        "{i}I intend to breed her well, she shall sire me great warriors.{/i}":
            "...The phrase jumped out of me in a tone so... {i}alien{/i}."
            KYLISA @blush "I... Right, well, as long as {i}she's{/i} happy with that as well I suppose."
            KYLISA @talk "Perhaps you might want to consider leaving Novaras if that's your long term-plan with her."
            KYLISA @talk "The inquisition have punished many... With child or not."
    KYLISA @talk "Anyway, you two should leave now, before someone else comes inquiring."
    MC @talk "Thank you, Kylisa."
    scene black with dissolve
    'After that, the two of us slipped away back home safely.'
    $ AutoMus(True)
    $ LocSet("azul_safehouse_bedroom")
    $ TimeAdvBy(TIME_05H)
    $ LocFlush()
    show mc at cleft
    show myu at cright_f
    with dissolve
    MYU @talk "Myu tired, can... can we talk more soon?"
    MC @talk "Of course, Myu."
    $ CharSetVar("myu", "hide", False)
    $ QstComplete(QstNewMyu)

    'Before she dissolved, Myu turned to face me once more.'
    MYU @talk "Do... [player_name!t] not want to be Myu husband?"
    MC @surprised "What?"
    MYU @sad "Myu... Understand now, things not as she thought."
    MYU @sad "Even though Myu wants [player_name!t], not fair to force someone to love who doesn't love back."
    MYU @sad "So, what does [player_name!t] want?"
    menu:
        "{image=[ICON.HEART]} You're mine, Myu.":
            jump rom_Myu_initial # down at world_romance/myu

        "{image=[ICON.HEART_CROSS]} Myu, I think it's best we just stay friends.":
            MYU @sad "Myu... Myu understand."
            MYU @sad "Myu is sorry for trying to force what cannot be."
            MC @talk "I will still keep you safe and look after you Myu, I promise."
            MC @talk "I just can't be what you {i}want{/i} me to be."
            MYU @sad "...Very well, Myu will help when she can."
            MYU @smile "And maybe, along the way, Myu will find someone who {i}does{/i} want her that way."
            MC @talk "Maybe Myu, maybe."
            MC '(I hope I have made the right choice with this.)'
            $ LocEnter()