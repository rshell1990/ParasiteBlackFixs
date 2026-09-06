label jurgen_2_get_amira_nijah:
    #Player speaks to Nijah - new dialogue option to 'ask about Amira's tears' 
    NIJAH 'Eh?'
    NIJAH "What do you want zat for?"
    MC @talk "Could you get me some?"
    'Nijah seemed slightly uncomfortable with the question, but she nodded and left the room briefly before returning with a vial.'
    NIJAH 'Be careful with zis!'
    MC @talk 'I will Nijah, thank you.'
    $ PlayerAddItem("qst_amiras_tears")
    $ QstGracefulRebirth().tookAmirasFromNijah = True
    return
    # adds item

label jurgen_2_get_raza_fawha:
    #Player speaks to Fawha - New dialogue option to 'ask about Raza'
    FAWHA @talk 'Raza?'
    FAWHA @talk "I hope you aren't planning on using it... Be a shame to waste such a pretty face as yours."
    MC @talk 'No... But I need some that I could slip into a drink.'
    'Fawha raised a curious eyebrow.'
    FAWHA @talk "...Should I even ask?"
    MC @talk "Probably best you don't."
    'Fawha produced a small crystalized ball no bigger than a fingernail.'
    FAWHA @talk "They've been testing with this... It should dissolve quickly in whatever drink you put it into."
    MC @talk 'Thank you.'
    FAWHA @talk 'You owe me one, handsome.'
    $ PlayerAddItem("qst_raza_bottle")
    $ QstGracefulRebirth().tookRazaFromFawha = True
    return
    # adds item

label jurgen_1_tavern_poison:
    #Slipping poison into Jurgen's drink 
    MC "(What should I use?)"
    menu:
        "Amira's tears" if PlayerItemQty("qst_amiras_tears") > 0:
            jump jurgen_1_tavern_poison_amira
        "Raza" if PlayerItemQty("qst_raza_bottle") > 0:
            jump jurgen_1_tavern_poison_raza

label jurgen_1_tavern_poison_amira:
    MC @talk "There's a man outside calling for a guard named Jurgen, just thought you should know."
    JURGEN 'What?'
    JURGEN "Wait here while I see what's going on!"
    hide cg_guard with easeoutright
    'Once Jurgen left to investigate my lie, I subtly pressed the poison into his drink.'
    $ PlayerRemItem("qst_amiras_tears")
    show cg_guard:
        xalign 0.85
        xoffset -1.0
    with easeinright
    JURGEN 'There was no one there.'
    MC @talk 'Hm? Strange... He must have left.'
    'Jurgen grabbed his mug and began taking a sip.'
    JURGEN 'Hm, what did he look like?'
    MC @talk "Well, I didn't get much of a good look at him, but he was tall with dark short hair."
    'Jurgen continued to sip at his drink.'
    JURGEN 'Did he-'
    'Jurgen suddenly stopped speaking, the poison already kicking in.'
    MC @talk 'Everything alright?'
    'Jurgen said nothing, he stumbled his way towards the door knocking over various drinks and bottles in his way.'
    'A few people gasped as I shouted behind him,'
    MC @talk "I think you've drank too much tonight friend!"
    'A few people laughed, blissfully unaware of what was truly happening.'
    scene black with dissolve
    $ LocSet("novaras_dist_market")
    'I waited a short while later before heading outside."
    "Following the stench of death to find Jurgen, I saw he had crawled his way up some Alleyway, no doubt believing he could throw up whatever was wrong.'
    'He laid dead in a pool of his own blood that bled from his eyes.'
    $ LocFlush()
    show mc:
        xcenter 0.15
    with dissolve
    BLACK '(Fascinating.)'
    MC '(What is?)'
    BLACK '(I did not appreciate how calculating your dark side could be.)'
    BLACK '(...You would have made a good one of us.)'
    "Something about my dark passenger's comment I found unsettling, I justified in my head I did what I had to but..."
    "Did I really believe that?"
    hide mc with dissolve
    "I quickly fled the scene before someone else stumbled upon Jurgen's body."
    $ QstGracefulRebirth().jurgenGone = True
    $ QstGracefulRebirth().jurgenActive = False
    $ GoalComplete(QstGracefulRebirth, 1.5)
    $ LocEnterQ()

label jurgen_1_tavern_poison_raza:
    #Slipping Raza in his drink 
    MC @talk "There's a man outside calling for a guard named Jurgen, just thought you should know."
    JURGEN 'What?'
    JURGEN "Wait here while I see what's going on!"
    'Once Jurgen left to investigate my lie, I subtly pressed the Raza into his drink.'
    $ PlayerRemItem("qst_raza_bottle")
    JURGEN 'There was no one there.'
    MC @talk 'Hm? Strange... He must have left.'
    'Jurgen grabbed his mug and began taking a sip.'
    JURGEN 'Hm, what did he look like?'
    MC @talk "Well, I didn't get much of a good look at him, but he was tall with dark short hair."
    'Jurgen continued to sip at his drink.'
    JURGEN 'Did he-'
    'Jurgen suddenly stopped speaking, the raza already beginning to kick in.'
    MC @talk 'Everything alright?'
    "Jurgen's legs gave out beneath him as he dragged his mug and a couple bottles down with him crashing onto the floor."
    'A few people gasped and hurried over to help him as I leant down to offer my faux support.'
    MC @talk 'Someone call the guard! Get a doctor!'
    scene black with dissolve
    'A short while later, a doctor came to see to Jurgen as some other guards appeared and dispered the small crowd that was gathering and Jurgen.'
    'When Officer Lukkan entered, his eyes lit up when he saw me.'
    $ LocFlush()
    show mc at left
    show lukkan at cright_f
    with dissolve
    LUKKAN @talk "{i}You?{/i}"
    MC @talk 'Sir...'
    LUKKAN @talk "What's going on here?"
    MC @talk 'This guard was trying to sell Raza to me, but I think he must have taken some himself.'
    MC @talk 'Looks like he might have taken a little too much.'
    "The guard looked down at Jurgen's unconscious body before looking back up towards me."
    LUKKAN @talk '{i}Fuck.{/i}'
    LUKKAN @talk 'Listen, none of this happened.'
    LUKKAN @talk "He just got a little too drunk and that's all, understand?"
    "The doctor briefly looked up to object but Lukkan's glare shot him down quickly."
    MC @talk "But, what will happen-"
    LUKKAN @talk "He'll be fine..."
    LUKKAN @talk "He's going to enjoy a nice new promotion... In NewYark, working the sewerage systems there."
    'Lukkan gritted his teeth.'
    LUKKAN @talk '{i}But you keep your mouth shut about this, understand?{/i}'
    'I nodded.'
    MC @talk 'Yes sir.'
    LUKKAN @talk "Show's over people! Move on!"
    hide lukkan
    with dissolve
    'The crowds grumbled as the doctor had a couple guards lift up Jurgen onto a stretcher before he was carried out.'
    'Lukkan shot me once last warning look to keep this quiet before he himself left as well.'
    MC "(Well... That's the Jurgen problem solved.)"
    BLACK '(Very clever, human.)'
    $ QstGracefulRebirth().jurgenGone = True
    $ QstGracefulRebirth().jurgenActive = False
    $ GoalComplete(QstGracefulRebirth, 1.5)
    $ LocEnter()