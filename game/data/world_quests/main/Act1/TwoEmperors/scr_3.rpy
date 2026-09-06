label qst_TwoEmperors_3:
    show mc at cleft
    show markus at cright_f
    with dissolve
    MARKUS 'I need to go do something.'
    MC @talk "What? {i}Now?{/i}"
    MC @talk "We need to speak to Officer Lukkan!"
    'Markus was unusually dripping with sweat, his face seemingly paler white than before.'
    MARKUS "I'm sorry, I just... I need to go, okay?"
    MC @talk "...Fine."
    MARKUS "Meet me after at the Iron Unicorn, we can talk more there!"
    hide markus with dissolve
    'Markus hurried off before I could stop him.'
    MC @talk "Markus!"
    MC "(...Damn it, what's gotten into him?)"
    MC '(I should head over to speak to Officer Lukkan as soon as possible.)'
    $ LocEnter()

label qst_TwoEmperors_3_guardDebrief:
    show mc with easeinleft:
        xcenter 0.5
    "Entering the city, I heard ringing of armour plates approaching from behind."

    show cg_guard with easeinleft:
        xcenter 0.15
    show mc at blurin:
        xzoom -1.0
    GUARD "The Emperor wishes to speak to you."
    GUARD "Right away."
    MC @think "The Emperor?"
    MC @talk "But, I'm supposed to report to-"
    GUARD "The Emperor wishes to hear your report directly."
    MC @talk "Where is he?"
    GUARD "He is waiting in Captain Nyx's Office."
    GUARD "He requests you come immediately."
    MC "Well, lead the way then."
    hide cg_guard with easeoutright
    scene black with dissolve
    $ LocSet("novaras_fort_seb_captains_office")
    "Upon entering Captain Nyx's Office, she was in a fierce mood as she argued with the stoic Emperor."
    $ LocFlush()
    show alcott:
        xcenter 0.25
    show nyx at cright_f
    with dissolve
    NYX @angry "I have no more men to pull! My resources are stretched thin as it is!"
    ALCOTT @talk "Did Lukkan not send you that someone from the Adventurers Guild?"
    ALCOTT @talk "Did he not succeed in his tasks as instructed?"
    NYX @angry "Y-Yes!"
    NYX @angry "But it was a band wrap solution to a gaping wound!"
    NYX @angry "I need {i}more{/i} men to keep this city under control! Not less!"
    ALCOTT @talk "Then I will pull some lower tier Adventurers from their quests to assist you for a few months till the situation settles."
    ALCOTT @talk "But for now, it's far more important some of your men are posted elsewhere."
    'Captain Nyx stared in disbelief.'
    NYX @shock '...{i}The Adventurers Guild?{/i}'
    NYX @angry "Emperor... Please, I need trained men."
    NYX @angry "Not a bunch of undisciplined mercenaries!"
    ALCOTT @angry "Captain Nyx, you will follow orders whether you like them or not, are we clear?"
    NYX  "...Yes... Emperor."
    NYX  "My apologies for my conduct."
    'The Emperor finally turned to notice me stood waiting in the doorway.'
    ALCOTT @talk "Ah, there you are."
    ALCOTT @talk "Captain Nyx, you are dismissed."
    NYX @shock "But this is my-"
    ALCOTT @angry "I would speak with my man now, {i}alone.{/i}"
    ALCOTT @angry "You are dismissed, Captain Nyx."
    NYX  '...Very well, Emperor.'
    'Captain Nyx after bringing her fist against her chest in a salute, turned to leave.'
    show nyx at blurin, cright
    hide nyx with easeoutright
    'As she passed by me, we both shared a knowing glance as the guards closed the door behind her.'
    show alcott with dissolve:
        xcenter 0.5
        xzoom -1.0
    ALCOTT @talk "So, what news do you bring?"
    ALCOTT @talk "And where is your friend? I had the two of you sent."
    MC @talk "He's fine, just... Perhaps a little shaken by what we saw."
    'Alcott raised an eyebrow at the comment, waiting on me to elaborate.'
    scene black with dissolve
    'After relaying the events to him to the best of my knowledge...'
    $ LocFlush()
    show alcott:
        xcenter 0.8
        xzoom -1.0
    show mc:
        xcenter 0.2
    with dissolve
    ALCOTT @talk "...Hmm, I see."
    ALCOTT @talk "So another major offensive is likely being planned soon."
    ALCOTT @talk "It is as I feared."
    MC @think "Uhh, you don't seem very surprised."
    ALCOTT @talk "That's because I'm not."
    ALCOTT @talk "I've known for quite some time about their dark {i}Emperor.{/i}"
    'I felt my heart sink into my stomach, turning pale white as I took a step back in disbelief.'
    'They knew... After all these years of telling us the Demorai were nothing more than savage monsters of primitive mind, {i}they knew the truth.{/i}'
    MC @surprised "You... {i}You knew?{/i}"
    MC @surprised "But... The Demorai... They're not supposed to be-"
    ALCOTT @angry "As far as most people are concerned, the Demorai are just savage beasts ready to rip and tear."
    ALCOTT @talk "It is best for everyone's sake we keep it that way."
    ALCOTT @talk "Muddying the waters only invites unnecessary divisive discussions."
    $ choicemenu = ["a", "b"]
    menu qst_TwoEmperors_3_guardDebrief_rootMenu:
        "So all this time you've been lying to people!?" if "a" in choicemenu:
            $ choicemenu.remove("a")
            ALCOTT @talk "It is a soft lie that the Demorai are unintelligible savages."
            ALCOTT @angry "Make no mistake, intelligent or not, their only goal is to see our destruction."
            ALCOTT @talk "We must keep that {i}ethical debate{/i} door shut, for questioning our means will only lead us astray."
            ALCOTT @talk "We must focus on military victory only; we cannot afford to be distracted and risk dividing ourselves further."
            menu:
                "But this means we can talk to the Demorai! Perhaps even negotiate a ceasefire or something!":
                    ALCOTT @joy 'Ha!'
                    ALCOTT @angry "Listen to me now, and listen good, boy."
                    ALCOTT @talk "The Demorai have zero interest in any sort of {i}negotiations{/i} while their 'Emperor' rules over them."
                    MC @talk "But why? Why are they doing all this?"
                    ALCOTT @talk "Even I do not know that..."
                    ALCOTT @talk "But I know for us there is no seat for us at any negotiations table."
                    ALCOTT @talk "We are no more to them than vermin that need to be wiped out."
                "I still have more questions!":
                    ALCOTT @talk "I don't have all day, so speak quickly." #Loops back to main menu
            jump qst_TwoEmperors_3_guardDebrief_rootMenu
        "How did you know?" if "b" in choicemenu:
            $ choicemenu.remove("b")
            ALCOTT "{i}*Sigh*{/i}"
            ALCOTT @talk "While we do not know much of their society, much like ours, it seems to be at least somewhat factional."
            ALCOTT @talk "{i}One{/i} of these factions has conducted secret meetings with us."
            MC @talk "You... {i}Meetings with the Demorai?{/i}"
            ALCOTT @talk "{i}A faction of Demorai,{/i} yes."
            ALCOTT @talk "And while they have been very vague on exactly what their intentions are, they have made it clear they want this war ended."
            menu:
                'I thought you said there was no room for negotiation?' if "a" not in choicemenu: #Option appears if player has mentioned the possibility of negotiations before 
                    ALCOTT @talk "I said {i}while{/i} their Emperor rules there is no room for negotiation."
                    MC @think "Wait... Does that mean they want-"
                    ALCOTT @talk "I do not know for sure, but before, we have privately assisted each other in matters of intelligence."
                    ALCOTT @talk "And while they are not our allies by any stretch of the imagination... I do believe they perhaps have their own designs outside of their dark Emperors plans."
                "Who is this faction you speak of?": #Loops back to main menu
                    ALCOTT @talk "We don't know fully."
                    ALCOTT @talk "All I have is one contact to communicate with them through."
                    ALCOTT @talk "And no, I'm not sharing who the contact is, before you ask."
            jump qst_TwoEmperors_3_guardDebrief_rootMenu
        "Why are you telling me all this?": #Moves main plot forward
            "Alcott smiled, but it had no warmth to it."
            ALCOTT @smile "{i}...My reasons are my own.{/i}"
            ALCOTT @talk "Now, you've served the realm well, here, your coin as promised." #Payment added 
            $ PlayerAddItem("gold", QstTwoEmperors().goldReward)
            ALCOTT @talk "Oh, and suffice to say..."
            ALCOTT @talk "Nothing I have said leaves this room, are we clear?"
            ALCOTT @talk "There would be {i}severe{/i} consequences for that."
            'Understanding the implication, I nodded.'
            MC @talk "Yes... Emperor."
            ALCOTT @talk "Now, you are dismissed."
            scene black with dissolve
            $ QstComplete(QstTwoEmperors)
            'Deciding it unwise to stay any longer, I turned to leave and was escorted out of the Fort by the guards.'
            MC '(I need to meet with Markus at the {i}Iron Unicorn{/i} later.)'
            MC '(I need to tell him what I know.)'
    $ LocSet("novaras_dist_army")
    $ LocEnter()