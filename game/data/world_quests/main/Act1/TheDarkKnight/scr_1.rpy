label qst_DarkKnight_1_GoToCaptainNyxOffice:
    show cg_guard with dissolve:
        xcenter 0.7
        xzoom -1.0
    show mc with easeinleft:
        xcenter 0.15
    show cg_guard at shake:
        xcenter 0.7
        xzoom -1.0

    GUARD 'Halt!'
    GUARD 'What business have you here?'
    menu:
        'Officer Lukkan has sent me, here, see the sigil?':
            'The guard snatched the paper and looked it over for a moment before nodding.'
            GUARD 'Apologises for the zealousness, there have been some... {i}Issues{/i} recently.'
            MC @talk 'Issues?'
            GUARD "Captain Nyx will explain everything, I'm sure."
            GUARD "You can find her in the Captains' office."
            scene black with dissolve
            $ LocSet("novaras_fort_seb_captains_office")
            $ LocFlush()
            show nyx at center
            with dissolve
            NYX @talk 'Ah, you must be on the one Officer Lukkan sent.'
            MC @talk 'What gave it away?'
            NYX @laugh 'Because people who know me are usually already pissing themselves.'
            NYX @talk "Which tells me you don't know me, which tells me Lukkan sent you."
        "Point that thing at me and I'll shove it up your ass.":
            'The guard gritted his teeth.'
            GUARD 'Not before I run you through...!'
            show nyx at center_f with dissolve
            #Captain Nyx appears
            NYX @angry 'Stop! What is all this commotion?'
            GUARD 'This man wishes to speak to you, Captain.'
            NYX @talk 'Hm? Oh, you must be the one Lukkan sent.'
            NYX @talk 'Stand down and let him through.'
            GUARD 'But-'
            NYX @angry "That was an order, not a request."
            GUARD "...Yes ma'am."
            GUARD 'You may proceed.'
            scene black with dissolve
            $ LocSet("novaras_fort_seb_captains_office")
            $ LocFlush()
            show nyx at center
            with dissolve
            NYX @angry 'You do know I can have you thrown in a cell for threatening guards like that.'
            MC @talk "I don't really like being told what to do."
            NYX @angry 'Hmph, well you better get used to it.'
            NYX @angry 'The only way to get anywhere here is to learn when to kiss ass and shut up.'
    menu:
        "Oh, I'm looking forward to getting to know you...":
            NYX @shock 'Oh, {i}really?{/i} Would you like to get to know me better with my boot up your fucking ass?'
            NYX @angry "Pay attention, I'm not one of your sluts, nor am I here to fuck around with some happy go lucky {i}'Adventurer'{/i}..."
            NYX @angry "...whose probably gonna get skullfucked to death by a pissed off Demorai soon anyway."
        'Why am I here, Captain?':
            pass
    $ CharMeet("nyx")
    NYX @talk 'Your services are called upon to serve the Kingdom once again.'
    NYX @talk "I don't know how aware you are with how 'fragile' things can be in this city, but suffice to say, I'm in need of a sellsword like yourself."
    NYX @talk "You'll be well compensated for your services."
    MC @talk 'Depends on the job.'
    NYX @talk "These last few months, we've seen an explosion in banditry around the city."
    NYX @talk 'It seems some of the smaller crime factions inside the city have splintered, and the ensuing chaos is spilling out onto the street.'
    NYX @angry "Soon the fuckers will be trying to rob people in bloody daylight if we don't stomp it out now."
    NYX @talk 'I want you to go out and send a message.'
    NYX @talk 'Find them, and take them out.'
    NYX @angry "I'll string up a few of the bodies when you're done, then they'll know not to fuck around."
    $ choicemenu = ['a','b','c','d']
    menu qst_DarkKnight_1_atCaptainNyxOffice_menu:
        'Why me? Why not have the guards do it?' if 'a' in choicemenu:
            NYX @angry "Because we're stretched thin enough as it is, Alcott keeps pulling my men into whatever division he thinks is most important for the day and he's leaving me severely short-handed."
            NYX @angry "The fucker's so busy worrying about the enemy beyond the wall, he forgets about the threats from within."
            MC @talk "I take it you don't approve of his leadership?"
            NYX @talk "Better than Mesamor, but even the best fruit is doomed to fall if the tree's rotten."
            MC @talk "That's... quite the metaphor."
            NYX @talk "We can discuss politics all you want when you're done."
            $ choicemenu.remove('a')
            jump qst_DarkKnight_1_atCaptainNyxOffice_menu
            # loops back to root
        'Why is this {i}my{/i} problem? We pay our taxes so you can deal with bandits.' if 'b' in choicemenu:
            NYX @angry 'In case you really are this stupid, let me spell it out for you.'
            NYX @angry '{i}We. Do. Not. Have. The. Men.{/i}'
            NYX @angry "What do you expect me to do? Kill all the bandits by myself?"
            NYX @talk "Not to mention the fact they've actively started laying traps for us now."
            MC @talk 'Laying traps?'
            NYX @talk 'Yep, baiting us into tight alleyways or feeding us false information.'
            NYX @angry "They've managed to ambush and take out a few of us like that, sneaky bastards, the lot of them."
            NYX @talk 'Something drastic needs to be done, something that will bring them back into line.'
            $ choicemenu.remove('b')
            jump qst_DarkKnight_1_atCaptainNyxOffice_menu
            # loops back to root
        "Ah finally, my week isn't complete without cutting a few bandits down." if 'c' in choicemenu:
            NYX @smile "Feeling a little bloodthirsty today, aren't we?"
            NYX @laugh 'Never mind, I just wish the rest of my men shared your enthusiasm.'
            NYX @angry "Half of them act like they've just had their balls cut off." 
            $ choicemenu.remove('c')
            jump qst_DarkKnight_1_atCaptainNyxOffice_menu
            # loops back to root
        'Have things really gotten that bad?' if 'd' in choicemenu:
            NYX @angry "Do you really think if things weren't that bad, Lukkan would be calling upon someone from the fucking Adventurers Guild of all things to help me out?"
            MC @angry "What's wrong with the Adventurers Guild?"
            NYX @smile "Haha! Wow, you are new to all this, aren't you?"
            NYX @angry "I'll tell you what, do your job, and maybe I'll tell you my 'opinions' on the Adventure Guild afterwards."
            $ choicemenu.remove('d')
            jump qst_DarkKnight_1_atCaptainNyxOffice_menu
            # loops back to root
        # appears if we asked 2 or more above questions
        "I think I got the idea..." if len(choicemenu)<3: 
            NYX @talk 'Finally.' #Dialogue continues
    NYX @talk 'So... Can I count on you with this?'
    menu:
        'I will do as you asked.':
            NYX @smile 'Finally, someone useful around here.'
            NYX @talk 'Good, I look forward to hearing your progress.'
            NYX @talk 'Remember, I need at least three groups of them slain, try wandering around at night and seeing what you find.'
            $ QstSetProgress(QstDarkKnight, 1)
            $ LocEnter()
        'I need some time to think.':
            $ QstDarkKnight().wasBriefed = True
            NYX @angry "Well, don't think too long, either you do it, or I have to find some other idiot to fill in for you." #Exits conversation.
            $ LocEnter()

label qst_DarkKnight_1_atCaptainNyxOfficeRevisit:
    NYX @talk 'Yeah, I need you to patrol the streets at night.'
    NYX @talk "Deal with at least three bandit groups."
    NYX @talk "So... Can I count on you with this?"
    menu:
        'I will do as you asked.':
            NYX @laugh 'Finally, someone useful around here.'
            NYX @talk 'Good, I look forward to hearing your progress.'
            $ QstSetProgress(QstDarkKnight, 1)
            $ LocEnter()
        'I need some time to think.':
            NYX @angry "Well don't think too long, either you do it, or I have to find some other idiot to fill in for you." #Exits conversation.
            $ LocEnter()

label qst_DarkKnight_1_atCaptainNyxOfficeInProg:
    NYX @talk "Yes? Did you do as I asked?"
    MC @talk 'Not yet.'
    NYX @angry 'Then what are you doing still stood here?'
    NYX @angry 'Go out and deal with them already!'
    $ LocEnter()