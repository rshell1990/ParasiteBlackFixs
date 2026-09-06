label scr_SharedInThorns_askForClues:
    ELENA @grumpy "Hm? Well, I'll try answer whatever questions you may have."
    menu scr_SharedInThorns_askForClues_menu:
        'How did one such as yourself in the company of the Thornfalls?' if 'book' not in QstSharedInThorns().cluesLearnedAbout: ### IF THIS CLUE IS UNKNOWN
            ELENA @grumpy 'I was found abandoned as a child by the then lord of the Thornfall Estate on the boundaries of their land.'
            ELENA @grumpy 'Lord Vront Thornfall.'
            MC @talk 'What happened to your parents?'
            ELENA @sad 'I do not know.'
            ELENA @sad 'I was found sick and alone.'
            ELENA @grumpy 'Lord Vront nursed me back to health, but made me swear to always protect his only heir, the lady Grace.'
            MC @talk 'Strange for a Lord to only have one daughter.'
            ELENA @sad 'Yes... Lord Vront was a complex man, he rarely opened up but as I understood it, much tragedy had befallen him in the past.'
            MC @talk 'Tragedy?'
            ELENA @grumpy "He wouldn't discuss such things with me, all that matters is that I kept his vow."
            MC "(It may be worth looking up to see if I can find anything about the Thornfall family's history, perhaps it may offer some clues as to the Lady Grace.)"
            $ GoalShow(QstSharedInThorns, 2)
            $ QstSharedInThorns().cluesLearnedAbout.append("book")
            if len(QstSharedInThorns().cluesLearnedAbout)==3:
                $ GoalComplete(QstSharedInThorns, 0)
                return
            else:
                jump scr_SharedInThorns_askForClues_menu
        'What does the lady Grace look like?' if any(['witch','trade']) not in QstSharedInThorns().cluesLearnedAbout: ### IF EITHER CLUE OF TRADE/WITCH UNKNOWN OR BOTH
            ELENA @talk 'She was blonde with long curly hair when I last saw her.'
            ELENA @talk '...It has been a few years.'
            MC @talk "You didn't keep in touch?"
            ELENA @sad 'We exchanged letters for a while but the war caused such long delays it became impossible.'
            MC @talk 'I see... No portraits of the lady remain?'
            ELENA @talk 'None in my possession, and those that littered the Estate were her as a child.'
            ELENA @grumpy 'Of little used to us now I am afraid.'
            menu scr_SharedInThorns_askForClues_menu_2:
                'Did she say anything that might helps us in those letters while they were still being exchanged?' if 'trade' not in QstSharedInThorns().cluesLearnedAbout:
                    ELENA @grumpy 'The lady Grace once mentioned she was funding some kind of expedition overseas, but she refused to elaborate on what it was she was looking for or where it was...'
                    MC @talk 'Did Lord Vront mention this expedition?'
                    ELENA @shock 'He said it was a matter of most urgency.'
                    ELENA @talk 'He said when the time came, he would explain everything...'
                    ELENA @sad 'But then one night, he cast himself off the cliffs onto the rocks below, let the tide take him out.'
                    MC @talk 'What? What possessed him to do such a thing?'
                    ELENA @sad 'I do not know... He was quieter than normal with the days leading up to his dead.'
                    MC '(Foreign expeditions... Perhaps someone might know something of this?)'
                    $ GoalShow(QstSharedInThorns, 3)
                    $ QstSharedInThorns().cluesLearnedAbout.append("trade")
                    if len(QstSharedInThorns().cluesLearnedAbout)==3:
                        $ GoalComplete(QstSharedInThorns, 0)
                    if 'witch' not in QstSharedInThorns().cluesLearnedAbout:
                        jump scr_SharedInThorns_askForClues_menu_2
                    else:
                        return
                'Was there anything strange about the Thornfalls?' if 'witch' not in QstSharedInThorns().cluesLearnedAbout:
                    ELENA @grumpy 'Strange?'
                    ELENA @grumpy 'You mean aside from humans willing to take in one such as myself?'
                    MC @talk 'Think... Was there anything you found strange in all your years there?'
                    'Elena seemed to ponder my question for a while before she answered sheepishly.'
                    ELENA @grumpy '...Lord Vront had various bolts and locks on his room door from the outside.'
                    MC @talk 'What?'
                    ELENA @grumpy 'The servants every night would lock the door and open it come morning.'
                    MC @talk 'Did you ever hear anything the other side of the door?'
                    ELENA @grumpy "I wasn't even allowed in that wing of the Estate come nightfall."
                    ELENA @grumpy 'The guards would patrol the Estate and kept me confined to my room.'
                    ELENA @grumpy 'I only saw the locks in passing during the day.'
                    MC @talk 'Did you ever hear any sounds or anything that might sound unnatural?'
                    ELENA @sad '...Once I sneaked passed the guards when I was still small.'
                    ELENA @sad 'Curiosity got the best of me.'
                    ELENA @shock 'I heard... {i}Scratching.{/i}'
                    ELENA @shock 'Frantic Scratching and then banging against the door when they heard me make the slightest sound.'
                    ELENA @sad 'That was the only time I sneaked out at night.'
                    MC @talk 'I see...'
                    MC '(Perhaps some kind of curse afflicted the family line? But what?)'
                    # ADD WITCH CLUE
                    #Clue update: Perhaps a witch of some kind might know about such a curse?
                    $ GoalShow(QstSharedInThorns, 1)
                    $ QstSharedInThorns().cluesLearnedAbout.append("witch")
                    if len(QstSharedInThorns().cluesLearnedAbout)==3:
                        $ GoalComplete(QstSharedInThorns, 0)
                    if "trade" not in QstSharedInThorns().cluesLearnedAbout:
                        jump scr_SharedInThorns_askForClues_menu_2
                    else:
                        return
                "Let's talk about something else.":
                    ELENA @talk 'Ask whatever you wish.' #Loops back to main
                    return
        'What brought you to Novaras?':
            ELENA @talk 'After Lord Vronts sudden death, I had to remain in hiding or risk exposure.'
            ELENA @talk 'The few servants who remained kept my secret as the Estate without any heir was re-absorbed back under the jurisdiction of the Alderian government.'
            ELENA @grumpy 'I was then taken to that oaf of a man who tried to sell me off to any party who would have me.'
            ELENA @talk '...Then in you walked.'
            jump scr_SharedInThorns_askForClues_menu
        'That is all I have to ask for now.':
            ELENA @talk 'Very well, I hope it was of use to you.'
            return
