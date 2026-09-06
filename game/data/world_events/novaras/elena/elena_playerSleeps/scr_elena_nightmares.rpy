label event_Elena_nightmares:
    #Scene 17.5 #Begins when player goes to sleep
    scene black with dissolve
    $ TimeAdvTo(TIME_LATENIGHT)
    $ AutoMus(False)
    $ PlayMusic("audio/music/9_Burned_T.ogg")
    ELENA "...{i}No... No...!{/i}"
    'During the dead of night, I awoke to sounds of whines and other strange sounds.'
    'Looking up from my bed still half-asleep, I saw Elena, writhing around on the floor, feverish with a sweat.'
    $ LocFlush()
    with dissolve
    show mc with dissolve:
        xcenter 0.45
    ELENA "Stop... Please my lord!"
    "Elena dripped with sweat, her sleeptalk giving the unmistakable impression of some horrible nightmare plaguing her this evening."
    MC @talk 'Elena! Wake up!'
    'I reached down and lightly shook Elena.'
    ELENA 'No! Not again! Please!'
    ELENA "I'll be good!"
    MC @talk 'Elena!'
    "Elena's eyes began to half open as she looked dazed and confused at me."
    show mc with dissolve:
        xcenter 0.25
    show elena with dissolve:
        xcenter 0.55
        xzoom -1.0
    ELENA @shock 'H-Huh?'
    ELENA @sad 'Where am I?'
    MC @sad "It's alright Elena... You were having a nightmare."
    MC @talk "You're safe now."
    ELENA @shock 'I...'
    ELENA @sad "I'm sorry for waking you."
    MC @talk 'What was your nightmare about?'
    ELENA @sad 'It... It was nothing.'
    MC @talk 'You were pleading with Lord Vront not to do something.'
    "Elena's eyes widened."
    ELENA @shock 'You heard that?'
    ELENA @cry "You weren't supposed to hear that!"
    MC @sad 'Elena... What happened?'
    MC @talk 'Did Vront do something to you?'
    ELENA @sad '...Only when I misbehaved.'
    MC @talk 'Elena, what did he do?'
    ELENA @sad "He didn't hurt me... He knew he didn't need to."
    MC @talk 'What do you mean?'
    ELENA @sad 'When I misbehaved too much, he would have the staff take me down to the old Thornfall mines.'
    ELENA @sad 'He would have me put into a steel cage and lowered into the mines, long abandoned by this point but...'
    ELENA @sad '{i}Things... Moved down there.{/i}'
    ELENA @cry 'I would spend the whole night in terror, frozen.'
    ELENA @cry 'When I told I saw {i}things{/i} down there, horrible things...'
    ELENA @sad 'He always warned me one day, if I kept misbehaving, he would send me down there {i}without{/i} the cage.'
    menu:
        "He sounds like a monster!":
            ELENA @sad 'Maybe...'
            ELENA @cry 'But he was still the closest thing I had to a father.'
            ELENA @sad 'So, what is to be done?'
        "He was just trying to toughen you up, I doubt he would have let anything happen to you.":
            ELENA @sad 'Maybe... But I think in some dark, twisted way.'
            ELENA @sad 'He {i}wanted{/i} me to misbehave.'
            MC @talk 'Why do you say that?'
            ELENA @sad "I don't know... I think beneath the veneer of his wealth and his kindness and all of him..."
            ELENA @shock 'Something dark lurked.'
            ELENA @sad 'And only sometimes, I was unfortunate enough to catch a glimpse of it.'
            #Both routes continued
    MC @sad 'Elena, if he did that to you, why are you determined to find the Lady Grace?'
    MC @talk "It's sounds more like they used you, that they abused you than anything else..."
    ELENA @sad "Maybe so..."
    ELENA @sad "But they are the only family I've ever known."
    MC  '...'
    MC @sad "...Elena... How often do you have nightmares about the mines?"
    'Elena looked away to avoid the question, before, she gulped and turned to look me in the eyes, changing the subject quickly.'
    ELENA @sad "...Can I stay in the bed with you tonight?"
    MC @talk "Yes, if that's what you wish."
    ELENA @sad 'Thank you.'
    $ CharChangeRel("elena", 1)
    ELENA @sad "The nightmares will pass... {i}They always pass.{/i}"
    MC @sad '...{i}Elena.{/i}'
    ELENA @sad "Just hold me while I sleep..."
    'Elena climbed up onto the bed, resting her warm body against mine as I tenderly brushed against her fur.'
    #Fade to black
    scene black with dissolve
    ELENA @sad '{i}One day...{/i}'
    'She murmured.'
    ELENA @cry '{i}I think the nightmares will be gone for good.{/i}'
    $ AutoMus(True)
    $ TimeAdvTo(TIME_MORNING)
    $ QstComplete(EventElenaNightmares)
    $ LocEnter()
