label dros_firstmeet_bordello:
    $ QstComplete(EventBrothelAd)
    $ NoteLock("brothelAd1")
    $ NoteLock("brothelAd2")
    $ DrosInBordello().bordelloFirstMeet = False
    show dros at center
    DROS @lewd 'Why hello handsome, would you-'
    "Dros' face turned pale white when he realized who he was talking to."
    DROS @shock 'W-What are you doing here?!'
    MC @smile 'I could ask you the same thing.'
    DROS @talk 'I-'
    DROS @angry "What does it look like I'm doing?"
    menu:
        "Tailor by day, whore by night... Got anymore surprises?": 
            DROS @angry 'Grrhh!'
            DROS @angry 'I am not a whore! I-'
            DROS @angry "Urgh! You're infuriating!"
        "Do you work here?":
            DROS @angry 'No!'
            DROS @angry 'Well, {i}yes{/i} but not really!'
    MC @talk 'So what are you doing here then?'
    DROS @sad '...Do you know how hard it is for someone {i}like me{/i} to find some companionship around here?'
    MC @talk 'So you dress up at a brothel?'
    DROS @talk "Your lands aren't quite as 'open-minded' as Synmaria about these kind of things."
    DROS @sad "Men... {i}with other men,{/i} is punishable with imprisonment... {i}or worse here.{/i}"
    DROS @sad 'Guards turn a blind eye to me as an elf to avoid diplomatic issues with my kin.'
    DROS @sad "But the people who {i}are{/i} interested in me are either too afraid to act, or won't because I'm an elf."
    DROS @angry "{i}And as we all know, elves aren't to be trusted.{/i}"
    DROS @sad "I am an outsider amongst outsiders..."
    MC @talk "So you 'work' here to find someone interested?"
    DROS @talk '...The madam lets me work here as long as she takes a cut.'
    DROS @talk 'But in truth, I never even wanted to set a price.'
    DROS @talk "But she insists for the security and privacy to use their rooms, I have to charge some kind of rate."
    DROS @talk "Everyone has to earn their keep here."
    menu:
        "That sounds awfully lonely.":
            DROS @sad '...What does it matter to you?'
            DROS @talk 'Compared to many, I have it wonderful in this city.'
            DROS @sad "What's a little loneliness compared to have no bread on the table?"
            MC @talk "It still eats away at you being that alone all the time."
            'The comment seemed to cut somewhere deep inside of Dros, as he struggled to form his next sentence.'
        "That why you act like a total cunt?":
            DROS @angry "You fucking try being cheerful when you're surrounded by morons day in, day out."
            DROS @angry "At least some sex would take the edge off!"
    DROS @sad 'W-What do you even want from me?'
    DROS @angry "If you've come here to mock me, just get it over with."
    menu:
        "You're right, it {i}IS{/i} pretty funny.":
            DROS @angry 'Laugh it fucking up.'
            DROS @angry "You're a real fucking jester."
        "I'm not here to mock you, Dros.":
            DROS @talk 'Then what {i}do{/i} you want?'    
    MC @talk "Maybe there's a way I could help?"
    DROS @talk "How could you possibly help me?"
    MC @talk 'Come now, surely you can think of something.'
    DROS @sad 'Well... I did have one idea.'
    DROS @sad "But it's foolish."
    MC @talk 'Try me.'
    DROS @talk '...I was thinking maybe I could make myself more...'
    DROS @lewd "{i}Womanly.{/i}"
    MC @talk "Womanly?"
    DROS @sad "Come now, if I had some tits and looked the part a bit more, do you think I'd have half the trouble I do now?"
    DROS @smile "I mean, it's the worst kept secret how often the Mages of Palam get laid so..."
    DROS @talk "I guess I've been wondering if I maybe just looked and sounded more like a woman, I'd probably find more luck."
    DROS @talk "What do you think?"
    DROS @talk "I even have a plan if you're curious."
    DROS @talk "If you help me, I could see to it there's a discount at my store for you."
    menu:
        "I'll help you become more 'womanly,' Dros.":
            DROS @shock 'You will?'
            DROS @smile 'I mean, uh... Thank you.'
            DROS @talk "I wasn't actually expecting you to-"
            DROS @smile "Nevermind, the plan is pretty straightforward actually."
            MC @talk 'Go on?'
            DROS @sad "The Mages of Palam seemed reluctant to help me, even after I offered generous payment."
            DROS @talk "I don't know why, but they HAVE to know something."
            DROS @talk "Speak to them and start there if you're serious about helping me."
            jump startGracefulRebirth

        "I don't think this is something I'd be able to help you with.":
            'Dros was clearly wounded by the comment, but he once again built up his usual walls and distanced himself once again.'
            DROS @sad 'I see... Well, fine then.'
            DROS @sad 'We have nothing further to discuss.' 
            'Without another word, Dros turned and headed off to in the opposite direction to me.'
            MC '(Hm, perhaps I should re-consider helping him? His store discount could prove quite useful.)'
            $ QstStart(PrimerGracefulRebirth)
            $ LocEnter()