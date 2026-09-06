label scr_event_Elena_morningAfterBook:
    #Scene 16 - MC BEDROOM MORNING (2 days later)
    show cg_elena_reading with dissolve:
        pos (0.205,0.425)
        zoom 0.75
    'As my eyes peeled open, I found Elena sat legs crossed on the floor, tail swishing as she read some book.'
    MC @talk '...Hello there.'
    hide cg_elena_reading
    show cg_elena_reading_eyesup:
        pos (0.205,0.425)
        zoom 0.75
    with dissolve
    ELENA @talk "Hm? Oh! You're awake!"
    ELENA @talk "I hope I didn't wake you up."
    MC @talk "No, it's fine."
    MC @talk 'Enjoying the read?'
    ELENA @talk "Yes actually, it reminds me of what father used to read to me when I was little."
    MC @talk '{i}Father?{/i}'
    ELENA @talk 'I... Lord Vront insisted I call him father.'
    ELENA @talk 'He wanted me to know despite being adopted, he still saw me as one of his own flesh and blood.'
    MC @talk "Really?"
    ELENA @talk 'Yes, he oversaw that I received an education alongside Grace and taught me everything he could.'
    ELENA @talk 'How to cook, how to manage finances... How to fight.'
    MC @talk 'He taught you to fight?'
    ELENA @talk 'Not him personally but, he paid for me to learn from private tutors.'
    MC @talk 'Sounds like he really cared for you.'
    ELENA @talk "I think so... But he rarely opened up, and there was always the burden of expectation that my role was to serve as protector and companion to Grace."
    MC @talk 'But what of what you wanted?'
    ELENA @talk 'I think my own dreams and desires were seen as the things of fancy.'
    ELENA @talk 'While I think he wished I was happy, my happiness was not a goal nor a concern of his.'
    MC @talk 'That sounds like a complicated relationship.'
    ELENA @talk 'It was...'
    MC @talk 'And what of the now Lady Thornfall? How was things with her?'
    ELENA @talk 'I believe sisterly... To an extent.'
    MC @talk '{i}To an extent?{/i}'
    ELENA @talk 'I mean, she would constantly have me tag along with her.'
    ELENA @talk 'But somehow, she always seemed to find and encourage trouble.'
    MC @talk 'What do you mean?'
    ELENA @talk 'I was always there to protect her and get her out of whatever mess she landed herself into.'
    ELENA @talk 'But she would do... Strange things.'
    ELENA @talk 'Flirt with bachelors and then make the men fight over her when really she had no interest in either.'
    ELENA @talk 'Lie all the time and expect me to take the blame for whatever petty crime she did.'
    ELENA @talk 'And just generally seemed to enjoy causing chaos.'
    MC @talk 'Sounds like a spoilt brat.'
    ELENA @talk 'She could be... But then when I needed her, she was there.'
    ELENA @talk 'She was far more concerned than father with my actual happiness, and always wanted me to pursue whatever made me happy.'
    MC @talk "Hm, did the good parts to her outweigh the bad?"
    ELENA @talk "I've been asking myself that question my whole life..."
    'Elena seemed to daze off for a moment before closing her book shut.'
    ELENA @talk "Anyway, If you want to stay in bed, don't let me stop you."
    MC @talk '{i}*Groans*{/i}'
    MC @talk "I'm up now, may as well see what's about."
    #MC naked
    $ CharSetClothes("mc", "naked")
    show mc with dissolve:
        xcenter 0.65
        xzoom -1.0
    'As I rose from my feet and yawned, I quickly forgot I was still naked and Elena blushed as her wide eyes stared at the dangling appendage between my legs.'
    ELENA @talk "Y-You're...!"
    MC @talk 'Hm?'
    MC @surprised 'Oh! Sorry, sometimes I forget.'
    ELENA @talk "Um, i-it's fine!"
    "As Elena's cheeks burned red, I smirked remembering some words she previously teased me about."
    MC @talk "I thought you didn't care about how us humans dress ourselves?"
    ELENA @talk "Y-Yes, but your thing is... Um..."
    ELENA @talk '{i}Distracting.{/i}'
    hide cg_elena_reading_eyesup
    show cg_elena_reading:
        pos (0.205,0.425)
        zoom 0.75
    with dissolve
    MC @smile 'Distracting huh?'
    hide mc with dissolve
    $ CharSetClothes("mc", "normal")
    'I reached down to grab some of my clothes, dressing myself as Elena turned to look away still red-faced, her eyes occasionally glancing over in my direction subtly.'
    show mc with dissolve:
        xcenter 0.65
        xzoom -1.0
    #MC dressed
    MC @talk 'Alright, all done.'
    MC @talk 'You can look now.'
    hide cg_elena_reading
    show cg_elena_reading_eyesup:
        pos (0.205,0.425)
        zoom 0.75
    with dissolve
    'Elena slowly turned her head to look towards me once again, still flustered by the experience.'
    ELENA @talk "C-Come on now, adventures await."
    $ CharChangeRel("elena", 1)
    $ QstComplete(EventElenaMorning)
    $ LocEnter()
