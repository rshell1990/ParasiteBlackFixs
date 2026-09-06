init python:
    @AppendToAllQuests
    class EventMcNewArmor(LogicModule):
        def onEnter(self):  
            if GetLocID() == "mc_house_kitchen":
                if IsDaytime():    
                    return TriggeredEvent("event_mc_newarmor", priority = 1)

        def onComplete(self):
            PlayerAddItem("father_armor_item")
            if CharGetVar("mc", "eqp_chest") is not None:
                UnequipItem_CharIndex(0, EQP_SLOTS.CHEST[0])
            EquipItem(0, "father_armor_item", EQP_SLOTS.CHEST[0])
            TooltipClear()
            
            CharSetVar("mc", "default_look", "father_armor")
            CharSetBattleSkinID("mc", "mc_na")
            return

label event_mc_newarmor:
    show regina at cleft
    show mc at cright_f
    with dissolve
    REGINA @sad '[player_name!t]!'
    '[regina_ref_cap!t] leapt onto me hugging me tightly when she saw me.'
    'I struggled to pull away from her tight grip as I tried to calm her.'
    MC @talk "Ahh! Careful!"
    REGINA @sad "What happened?"
    REGINA @sad 'I heard you were seen being carried off towards the doctors, then the next thing I knew, I was told you were fighting for your life!'
    menu:
        'I was attacked by... {i}something.{/i}':
            REGINA @sad 'I told you to be careful.'
            REGINA @angry 'You need to listen to me more!'
            REGINA @sad 'Being an Adventurer is dangerous [player_name!t].'
        "I'm fine... They're over-exaggerating.":
            REGINA @sad '{i}*Sigh*{/i} Please be more careful.'
            REGINA @sad "I don't know what I would do with myself if something happened to you."
    'The thought lingered for a moment on how close to death once again I truly had come.'
    "I had become perhaps too arrogant with my newfound powers."
    "Death as a prospect seemed to have slipped further and further away since I merged with the dark passenger." 
    'But now... Now I remembered I {i}was{/i} still vulnerable, and should I meet my end, those most precious to me would be left to fend for themselves without me.'
    MC @sad '...I promise I will be more careful.'
    "I gently caressed [regina_ref!t]'s face and brought her into an embrace."
    'She smelt good, like freshly cut wildflowers.'
    'She reluctantly pulled away and said,'
    REGINA @talk 'There is some good news.'
    REGINA @talk 'Your father has sent word and had delivered a gift for you.'
    MC @surprised "Father?"
    REGINA @talk 'Yes... Some new armour and a letter for us each.'
    REGINA @talk 'I brought it into your room for when you want to read it.'
    MC @talk 'Thank you.'
    REGINA @sad 'How are your wounds? Are they-'
    MC @talk 'I am still sore but, I am fine.'
    MC @talk 'I promise you.'
    'Reluctantly, [regina_ref!t] relented, pulling back as she remarked she would put some food on for later, no doubt distracting herself with regards to her worries for me.'
    show regina at blurin, cleft_f
    $ Pause(0.15)
    hide regina with easeoutleft
    MC '{i}*Sigh*{/i}'
    scene black with dissolve
    MC '(I should see what father has brought me.)'
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    show mc:
        xalign 0.5
    with dissolve
    'The armour was laid out for me on the bed with the note held down beneath one of the gauntlet.'
    'I held up the note and began to read it.'
    '{i}My son,{/i}'
    '{i}I am both troubled and proud to hear of your services to the Scouts corps.{/i}'
    '{i}I am angered as to why you were sent there to begin with, despite the assurances of those of higher stations than mine, that you and your friends places were secured with administrative roles only.{/i}'
    "{i}Despite what I can only assume to be the result of clerical errors, I have heard of you and Markus' bravery, and how you both were the sole survivors of a mission gone awry.{/i}"
    "{i}There is no greater fear for a father, than to lose his only son, and it pleases me greatly to know you are still hopefully well by the time this letter reaches you.{/i}"
    "{i}My work here is important, but it is so far mostly safe, despite the days dragging long tediously.{/i}"
    '{i}I look forward to seeing you, Erika, and everyone soon in the next few months.{/i}'
    '{i}In the last letter I received, it mentioned you and that Adara girl were still close.{/i}'
    '{i}Perhaps when I am back, I could speak to her father to arrange your betrothal if you wish?{/i}'
    '{i}It would be good for some good to come from all this darkness recently...{/i}'
    '{i}Now, I have sent to you a gift as I am sure you have received with this letter.{/i}'
    "{i}I have been told that you have been entered involuntarily into the Adventurers Guild as per the Emperor's will.{/i}"
    "{i}Despite my complete displeasure at the events that have unfolded, we must do the best we can with the cards dealt.{/i}"
    "{i}Therefore, I cannot bear the thought of you running around in whatever scrap metal they have given you and called 'armour' for your line of work.{/i}"
    "{i}I have spent of my own coin to have fashioned for your armour that may actually protect you.{/i}"
    "{i}I have heard you are far larger now since I last saw you, and I hope given the reports I received that I have gotten the right size.{/i}"
    '{i}I hope it serves and protects you well my son, I will pray for your safety along with my own.{/i}'
    '{i}Love, your father.{/i}'
    MC '(...Father.)'
    scene black with dissolve
    'Placing down the letter, I looked over towards the armour and after stripping down, placed it on piece by piece.'
    $ QstComplete(EventMcNewArmor)
    "It was certainly heavier than the old armour, yet not by much, and it fit my frame surprisingly well."
    $ LocFlush()
    show mc:
        xalign 0.5
    with dissolve
    'As I looked down towards my hand, I crunched it tightly into a ball.'
    MC '(Next time.)'
    MC "(Next time I'll be ready for whatever comes.)"
    $ LocEnter()