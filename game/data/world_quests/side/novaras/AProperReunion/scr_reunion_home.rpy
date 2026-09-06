label qst_reunion_home:
    $ QstComplete(PrimerQstProperReunion)
    show mc at cleft
    show regina at cright_f
    with dissolve
    MC @talk "[regina_ref_cap!t]."
    REGINA @talk 'Hey dear, I have just made some food.'
    MC @talk'Oh? Are these fresh eggs?'
    REGINA @talk 'Yes, I decided to treat you a little.'
    REGINA @talk 'I figured you might appreciate something a little tastier after six months of just Scout rations.'
    MC @talk'I won’t complain about that.'
    play sound "audio/cfx/door_knock.ogg"
    MC @talk'Hmm?'
    REGINA @talk '...Were you expecting a guest?'
    MC @talk'Not that I’m aware of.'
    MC @talk'Who could be knocking this early?'
    show regina shock
    "[regina_ref_cap!t]'s eyes widened for a moment as she seemed to realize who was at the door, but by then, my hand was already reaching for the handle."
    REGINA @shock_talk"Oh gods! Wait! I forgot to tell you-"
    "As soon as I opened the door, a hand reached out sharply to push the door wide open. Adara stood before me, breathing heavily as she glared at me."
    show adara angry at center_f
    with easeinright
    ADARA @angry "{i}...You!{/i}"
    "She finally blurted out, her voice breaking slightly from the strain."
    "I pulled back slightly, it had felt like a lifetime since I last saw her, and here she was stood before me."
    MC @talk "Adara?"
    "Suddenly, a felt the sharp and sudden pain of her open palm collide against my face, knocking my head towards the side before I turned to look back at her, cheek burning and slightly dazed and confused."
    play sound "audio/cfx/slap.ogg"
    MC @talk "What the hell was that for?!"
    ADARA @angry "How long have you been back?"
    MC @talk "Adara!"
    ADARA @angry "Why didn’t you tell me!"
    ADARA @angry "You should have told me you idiot!"
    MC @talk "Adara! I-"
    $ QstStart(QstProperReunion)
    $ AutoMus(False)
    $ PlayMusic("audio/music/23_Reunification.ogg")
    hide mc
    hide adara
    show cg_adara_hug_1 at cleft
    with flash
    "Suddenly, Adara flung herself forward, wrapping her arms around me as she rested her head onto my chest, lightly sobbing as she tried to hold back her tears."
    "..."
    "As she held me tightly, I could feel her heart race beneath her dress."
    ADARA @sad "You’re a fool... {i}You’re such a fool...{/i}"
    menu:
        'Hug Adara back':
            hide cg_adara_hug_1
            show cg_adara_hug_2 at cleft
            with dissolve
            "I gently motioned to wrap my arms around Adara and held her for a few moments."
            MC @talk "Adara..."
            MC"{i}I’m fine, can’t you see?{/i}"
            "Slowly, she pulled back, her eyes filled with water as she struggled to hold herself, her voice breaking on each word."
            ADARA @sad "Y-Yes... I can see that."
            hide cg_adara_hug_2
        'Pull Adara off':
            hide cg_adara_hug_1
            show mc at cleft
            show adara at center_f
            show regina at cright_f
            with dissolve
            "Abruptly, I pulled Adara back, lightly shaking her to snap some sense into her."
            MC @angry "Adara, get a hold of yourself!"
            "Adara swallowed hard, wiping her eyes quickly with her hands as she tried to re-compose herself."
            ADARA @sad "R-Right... Sorry."
    hide cg_adara_hug_1
    show mc at cleft
    show adara at center_f
    show regina at cright_f
    with dissolve
    ADARA @sad "Did you not receive my letters?"
    ADARA @sad "You stopped writing back so suddenly."
    MC @talk "Only while in training."
    MC @talk "After we headed off south, we heard nothing from Novaras."
    ADARA @sad "Y-Yes, they did say letters would take a lot longer to reach you... if at all."
    ADARA @sad "Still, I guess I still hoped they’d find their way to you still somehow."
    show adara lewd
    "Now that she had calmed somewhat, Adara took a moment to collect and truly comprehend the vast physical changes to myself since we last met, her eyes wandering over me as she blushed slightly."
    show adara
    ADARA @shock "Gods... [player_name!t]..."
    ADARA @shock "You look... {i}Different.{/i}"
    MC @talk "Uhh, yes... a lot has changed since I joined the scouts."
    ADARA @sad "Is it true?"
    MC @talk "What is?"
    ADARA @sad "Everyone’s been saying how you and Markus were the lone survivors of some perilous mission!"
    ADARA @sad "They say you’re both some kind of heroes or something!"
    MC @talk "Well... We made it home, that’s true."
    ADARA @sad "What happened beyond the wall?"
    MC @talk "Well-"
    ADARA @talk "Are you hurt? People are saying all sorts of strange things!"
    ADARA @talk "Some are saying a dragon brought you to the castle gates on his back!"
    ADARA @talk "Others are saying you found some type of ‘portal’ or something?"
    MC @talk "Adara, it’s a long story and too much to tell all at once."
    ADARA @talk "...Yes, sorry... I don’t mean to ask so much at once."
    REGINA @talk"Adara, would you like something to eat or drink?"
    ADARA @talk "I am fine, thank you..."
    REGINA @talk"Then come, try not to bother [player_name!t] too much with all of your questions at once."
    REGINA @talk"There is plenty of time to talk through everything, Adara."
    ADARA @talk "I-"
    ADARA @talk "Yes, of course..."
    ADARA @talk "...But, I must know... are you back to stay now?"
    menu:
        'Yes, I’m back to stay.':
            ADARA @talk "That’s good to hear."
            ADARA @talk "We’ve all been so worried."
        'I’m not sure...':
            show adara sad
            show mc sad
            ADARA @sad "I... I see..."
            MC @sad "But {i}for now, {/i} I am home."
    show mc
    show adara
    ADARA @talk "Yes, it’s good to have you back."
    menu:
        'Invite Adara out to the {i}’Iron Unicorn’{/i} in the Evening.':
            MC @talk "Adara, why don’t we meet at the {i}Iron Unicorn{/i} later? We can talk over a few drinks..."
            ADARA @talk "You... Uhh, of course!"
            ADARA @talk "That sounds nice, [player_name!t]."
            $ QstSetProgress(QstProperReunion, 1)
        '{image=[ICON.HEART_CROSS]} Tell Adara it’s good to see her and you’ll need to catch up with her soon...':
            MC @talk "We’ll speak soon and talk about everything that’s passed these past few months."
            ADARA @talk "Y-Yes, that would be good."
            show adara joy
            "Adara smiled brightly, struggling to hold back her emotion."
            ADARA @joy "I’m glad you’re home [player_name!t]..."
            $ QstComplete(QstProperReunion)
            $ QstProperReunion().friendZoned = True
    show mc
    show adara
    REGINA @talk"Adara dear, won’t you stay a little longer?"
    show adara sad
    ADARA @sad "No... I..."
    ADARA @sad "I best head home, father is unwell."
    MC @talk "What’s wrong with your father?"
    ADARA @sad "He continues to cough up something foul..."
    ADARA @sad "He has been unwell these last few days, the coin I earn from working at the castle helps pay for his medicine but..."
    ADARA @sad "His recovery is slow."
    menu:
        'Offer Adara some coin to pay for her father’s medicine.' if PlayerItemQty("gold") > 0:
            if PlayerItemQty("gold") >= 100:
                $ PlayerRemItem("gold", 100)
            else: 
                $ PlayerRemItem("gold", PlayerItemQty("gold"))
            $ QstProperReunion().paidForMedicine = True
            ADARA @talk "[player_name!t]! No, I can’t accept this...!"
            MC @talk "Adara, I have earned more than enough coin these last few days."
            MC @talk "Take it."
            "Adara smiled brightly as I handed over the small pouch of coins into her hand."
            ADARA @talk "[player_name!t]... This is-"
            MC @talk "Adara, {i}please,{/i} just take it."
            ADARA @talk "...Alright, if that’s what you really want."
            show adara at kissandleave
            "Adara quickly sprung forward once again to give another hug, planting a soft kiss onto my cheek before she hurried off home, waving ‘bye’ over her shoulder as she went."
            hide adara
        'Wish Adara well.':
            MC @talk "Keep me informed on your father’s health Adara, ask if you need anything."
            ADARA @talk "Mmm, I will do."
            ADARA @talk "Well, I best get going now..."
            ADARA @talk "It’s good to see you [player_name!t]."
            MC @talk "It’s good to see you too, Adara."
            hide adara with easeoutright
            "With that, I watched as Adara waved me goodbye, slowly making her way home."
    show mc
    show regina
    REGINA @talk"...You do know that girl is madly in love with you, right?"
    show mc surprised
    MC "[regina_ref_cap!t]!"
    REGINA @talk"Urgh, I hardly understand you pair."
    REGINA @talk"I know full well you’ve had your hands on other girls before."
    MC talk "Yes but... Adara and I have known each other for so long."
    MC @talk "It’s strange to think about her like that."
    "[regina_ref_cap!t] smirked."
    REGINA @talk"Oh, but you have thought about her like that?"
    show mc surprised
    MC "[regina_ref_cap!t]!"
    REGINA @talk"I’m just saying, you could do a lot worse than her..."
    REGINA @talk"I certainly preferred her to that other harpy you used to fool around with? What was her name?"
    "...{i}Elia{/i}."
    MC talk "I’d rather not be reminded."
    MC @talk "That feels like a lifetime ago now anyway."
    REGINA @talk"Hmph... It matters not."
    REGINA @talk"Anyway, come finish your meal before it goes cold!"
    MC @talk "Yes, [regina_ref!t]."
    $ AutoMus(True)
    if QstProperReunion().friendZoned:
        jump ev_AdaraDream_KO_friendzone
    else:
        $ LocEnter()