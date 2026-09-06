label qst_BiteBark_1_TalkToKennelMaster:
    show kennelmaster with dissolve:
        xcenter 0.75
        xzoom -1.0
    show mc with easeinleft:
        xcenter 0.15
    KENNELMASTER"Ah! You're new!"
    MC @talk 'Hm? Are you used to repeat visitors or something?'
    KENNELMASTER"Something like that, usually, half of these wannabe 'adventurers' come to me for the perfect companion for their latest quest but usually get the thing killed."
    KENNELMASTER"{i}OoOoh! How was I supposed to know that my mutt that's only just come out of training couldn't fight a fucking hydra?{/i}"
    KENNELMASTER'Fucking idiots.'
    MC @talk "I suppose now would be a bad time to say I'm an adventurer looking for a companion then?"
    KENNELMASTER"Not at all, I'll happily take your coin."
    KENNELMASTER"Just don't come crying to me if you get the thing killed because you decided to attack a battalion of Demorai or something."
    MC @talk "I'll try to keep that in mind."
    KENNELMASTER'So, which one would you like?'
    MC @talk "Show me what you've got."
    KENNELMASTER'Have you ever had one before?'
    MC @talk 'No.'
    KENNELMASTER'Hm... I recommend something simple then.'
    KENNELMASTER"It'll cost you a bit more, but our ones pre-trained are great for-"
    'In that moment as the man continued to prattle on, I had the distinct sense that someone, no, {i}something{/i} was watching me.'
    'Following the instinct of that feeling, I moved through the packs of dogs that stared at me from behind there bars, and arrived upon a blue wolf, sat silently and observing me from its cell.'
    KENNELMASTER'Hey! Are you even listening to me?'
    MC @talk 'That one, tell me about that one.'
    'The man looked over at the blue wolf.'
    KENNELMASTER'Oh no no no, not that one.'
    MC @talk "What? What's wrong with it?"
    KENNELMASTER'She refuses to break.'
    MC @surprised 'Huh?'
    KENNELMASTER"This one has refused everything we've tried, we even palmed her off to some of the more experienced Adventurers and she just keeps fucking off."
    MC @talk "Why is she blue? I've never seen a wolf like that."
    KENNELMASTER'Dunno mate, funniest thing though, so this old lord, Lord Vront of Thornfall dies and leaves her in our care, right?'
    KENNELMASTER'Leaves strict instructions that apparently she was supposed to go to his daughter or something but she just up and vanished, so, naturally, the wolf lands on our doorstep.'
    MC @surprised 'The daughter just vanished?'
    KENNELMASTER'Yep, not a clue where she went, and because of that, we got saddled with this one.'
    KENNELMASTER"Hardly makes a fucking sound, weirdest animal I've ever had to deal with."
    KENNELMASTER"Like she screws with us too, ever seen an animal turn its nose up to food and literally throw it back at us?"
    KENNELMASTER'Me neither, till this fucker shows up.'
    BLACK 'This pet is {b}different{/b}, host.'
    MC '(Yes... I can sense it.)'
    KENNELMASTER'Oi! Stop staring off all weird like that would ya?'
    KENNELMASTER"Now come this way, I think you'll find these ones over here much more-"
    MC @talk 'I want this one.'
    KENNELMASTER"{i}*Sigh*{/i} You just got to be fucking difficult, don't you?"
    KENNELMASTER"Fine, for seven hundred and fifty she's yours."
    MC @angry 'What? You just said you gave her away to free to the last adventurers!'
    KENNELMASTER"They've made a name for themselves... You're a nobody."
    KENNELMASTER"And that's still a steal price! We'd normally charge double that!"
    menu:
        'Here.' (Req_Gold = 750): #(Only available if player has gold available)
            $ PlayerRemItem('gold', 750) #If coin amount is available (750)
            KENNELMASTER"Alright, she's your problem now."
            'The man moved to open the cell up and allow the wolf out.'
            KENNELMASTER"Come on then bitch! Looks like you get another chance!"
            KENNELMASTER"Try not to fuck this one up would ya, {i}please?{/i}"
            hide kennelmaster with easeoutright
            ELENA_W "..."
            show mc with easeinleft:
                xcenter 0.15
            show elena_w with dissolve:
                xcenter 0.45
                xzoom -1.0
            'I crouched down towards the wolf.'
            MC @smile 'Hello, my name is [player_name!t], and-'
            'The wolf trotted off, seemingly uninterested in what I had to say.'
            hide elena_w with dissolve
            'Waiting by the door for us to leave, it stared at me with disinterest.'
            KENNELMASTER'Heh heh! Told you!'
            KENNELMASTER"Oh... by the way, no collar... She'll rip your fucking head off if you try."
            MC @angry 'You could have mentioned that before.'
            KENNELMASTER"Oh don't worry! She'll follow you alright!"
            KENNELMASTER"No problems there, till she just decides 'fuck it' and decides to stroll off and leave you eventually."
            KENNELMASTER"Anyway, she's {i}your{/i} problem now! Hahaha!"
            MC @sad '(This... could be more difficult than I hoped.)'
            hide mc with dissolve
            MC @talk 'Come on then girl, let me show you your new home.'
            ELENA_W "..."
            $ QstSetProgress(QstBiteBark, 2)
            $ LocSet("novaras_dist_army")
            $ LocEnterQ()

        "I don't have the money yet...":
            KENNELMASTER"She ain't going anywhere mate, come back when you have the coin."
            $ LocSet("novaras_dist_army")
            $ QstSetProgress(QstBiteBark, 1)
            $ LocEnterQ()