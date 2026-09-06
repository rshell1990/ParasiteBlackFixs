label scr_SharedInThorns_luciusClue:
    LUCIUSMAL "Hmm?"
    LUCIUSMAL "The Thornfalls you say? As in the now deceased Lord Vront's line?"
    LUCIUSMAL 'Hmmmm... Yes, I know one or two things told to me by some little birds through the grape vine.'
    LUCIUSMAL 'But tell me, what is this information worth to you?'
    MC @angry 'Let me guess, your pouch is awfully light of coin today, right?'
    LUCIUSMAL 'How wise you are!'
    LUCIUSMAL 'I should think... Two hundred coins should suffice!'
    ELENA "{i}*Growls*{/i}"
    'As Elena stepped forward snarling, the Merchant pulled back, his face quite afraid.'
    LUCIUSMAL 'Y-Your pet is snarling at me!'
    MC @talk "Oooh, she definitely doesn't like to be called that."
    LUCIUSMAL 'B-Back! Back you animal!'
    menu:
        'Let Elena threaten the Merchant':
            'Elena continue to snarl as she stepped forward, jumping forward to knock the startled Merchant down where she barked in front of his petrified face.'
            LUCIUSMAL 'Get her off me! GET HER OFF ME!'
            MC @talk 'Will you tell us what we want to know?'
            LUCIUSMAL 'Yes! YES! ANYTHING!'
            MC @talk 'Elena!'
            "Elena leapt off from the Merchant's chest and returned to my side."
            'The sheepishly white Merchant rose to his feet, shaking with fear.'
            LUCIUSMAL 'That mutt should be put down!'
            MC @talk 'Do not speak ill of Elena again Merchant.'
            MC @talk "I can assure you, {i}she{/i} won't be the one put down."
            LUCIUSMAL 'I... I will tell you what you want! Please!'
            MC @talk 'Speak Merchant.'
            $ QstSharedInThorns().threatenedLucius = True
            jump scr_SharedInThorns_luciusTellMe
        'Pull Elena back':
            'Deciding it was best not to let Elena continue to threaten the Merchant, I pulled her back.'
            LUCIUSMAL "So, what say you? Fifty gold and I'll tell you what I know."
            menu:
                'I shall return later.':
                    LUCIUSMAL "Of course... My information isn't going anywhere."
                    $ LocEnter()
                'Here is your coin Merchant.' (Req_Gold = 50):
                    $ PlayerRemItem('gold', 50)
                    jump scr_SharedInThorns_luciusTellMe


label scr_SharedInThorns_luciusTellMe:
    MC @talk 'Now, tell me what I want to know.'
    LUCIUSMAL "For many years, the Lord of Thornfall has privately funded various archaeological sites in Ramon."
    MC @talk '{i}Yes, Ramon.{/i}'
    LUCIUSMAL 'Very secretive, many speculate he is, or rather, {i}was{/i} digging up old buried temples for their treasures, but no one involved is willing to talk.'
    LUCIUSMAL "Those who have muttered strange things about what they've seen... Well, let's just say many of them vanish under very mysterious circumstances."
    LUCIUSMAL "Lord Vront's daughter was last seen around Ramon not long ago before she vanished."
    $ choicemenu = ['a']
    menu scr_SharedInThorns_luciusTellMe_menu:
        'What kind of strange things do they speak of?' if 'a' in choicemenu:
            LUCIUSMAL 'I only hear rumours... Strange underground temples, things glowing... Monsters.'
            LUCIUSMAL 'The ravings of mad men.'
            $ choicemenu.remove('a')
            jump scr_SharedInThorns_luciusTellMe_menu
        'What of the Lady Grace Thornfall and her recent travels to Ramon?': #Continues plot
            LUCIUSMAL 'I know nothing!'
            LUCIUSMAL 'The lady travelled to Ramon some years ago now, her business affair are even more secretive than her fathers!'
            MC @talk 'Hm... I see.'
            #If player threatened the Merchant
            if QstSharedInThorns().threatenedLucius == True:
                LUCIUSMAL "That's all I know! Now get out of my damn store!"
                MC @talk 'Thank you for your help.'
                LUCIUSMAL 'Tsch!'
                hide luciusmal with dissolve
                if 'a' not in choicemenu:
                    MC '(Hm... {i}Buried temples...{/i} Perhaps he was seeking some kind of enchantment or artefact?)'
                    'Elena looked up towards me, her eyes troubled by what she heard.'
                    MC @talk "Don't worry."
                    MC @talk "We'll talk about it when we get home."
                $ QstSharedInThorns().cluesCollected.append("trade")
                $ GoalComplete(QstSharedInThorns, 3)
                $ GoalShow(QstSharedInThorns, 6)
                $ LocSet("novaras_dist_market")
                $ LocEnterQ()
            else:
                #If player paid Merchant/bartered
                LUCIUSMAL 'A pleasure doing business with you as always.'
                MC @talk 'Goodbye Lucius.'
                hide luciusmal with dissolve
                if 'a' not in choicemenu:
                    MC '(Hm... {i}Buried temples...{/i} Perhaps he was seeking some kind of enchantment or artefact?)'
                    'Elena looked up towards me, her eyes troubled by what she heard.'
                    MC @talk "Don't worry."
                    MC @talk "We'll talk about it when we get home."
                $ QstSharedInThorns().cluesCollected.append("trade")
                $ GoalComplete(QstSharedInThorns, 3)
                $ GoalShow(QstSharedInThorns, 6)
                $ LocSet("novaras_dist_market")
                $ LocEnterQ()
