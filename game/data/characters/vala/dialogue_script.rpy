### vala firstmeet
label nov_vala_scr_firstmeet:
    #SCENE BEGINS FIRST TIME THE PLAYER ENTERS THE LIBRARY
    'As I stepped into the Library, I was greeted by the sudden warmth as I stepped through the door, the fire going as musky books laid scattered around on various tables.'
    MC @talk 'Hello? Is anyone here?'
    VALA 'Just a minute!'
    'Peering around, I noticed a blonde girl high up on some ladder, putting away a few old books they she slides back into place.'
    show cg_vala_meet1 with dissolve
    'Reaching onto her tip toes, the girl out-stretched her arms as she tried to reach the bookshelf, and her skirt begin to hike up, revealing the soft panties she wore beneath.'
    show cg_vala_meet2 with dissolve
    VALA 'Just... a little more!'
    show cg_vala_meet3 with dissolve
    MC @talk 'Are you okay up there? That ladder looks a little... {i}old.{/i}'
    VALA 'I’ll be fine! We’re getting a new-'
    'Suddenly, the weak ladder snapped beneath her foot as the girl began falling down!'
    hide cg_vala_meet1
    hide cg_vala_meet2
    hide cg_vala_meet3
    with flash
    VALA 'AHHHHH!'
    'Running forward, I managed to catch the girl just in time with my agile reflexes, gently letting her down safely.'
    show vala at center_f with dissolve:
        zoom 1.1
    VALA 'Phew...! Thank you for that!'
    'Stood before me, I now finally had a good chance to look at the girl properly, she was short, with long blonde hair and spectacle glasses.'
    if QstIsOver(QstTerminus):
        'Smiling cutely at me, I looked down to see the curves of her body and felt the tinge of the Parasite getting excited once again.'
    MC @talk 'No problem.'
    'The girl outstretched her hand for it to be shaken.'
    VALA 'Vala Bluestone at your service!'
    $ CharMeet("vala")
    'I reached out my hand to shake hers.'
    MC @talk 'A pleasure to meet you Vala Bluestone, I am [player_name!t].'
    VALA 'So, what brings you here?'
    MC @talk 'I was perhaps hoping to read a book or two...'
    VALA 'Ah, well the library is free for all, and always open.'
    VALA 'Just remember, while we can put books in the hold for you to keep reading once you come back, we can’t allow you to take any of the books with you.'
    'After so many students complained and asked for the library to be opened due to the ever-growing stress around studies, the education board agreed to give it extra funding to do so.'
    'Me and Markus, albeit reluctantly, were forced to spend a fair few of our evenings here.'
    'How long ago that all seems now...'
    VALA 'Is something the matter?'
    MC @talk 'Hmm?'
    VALA 'You seemed... {i}lost in thought{/i} for a second there.'
    MC @talk 'Oh, never mind.'
    MC @talk 'Just remembering some things, nothing important.'
    VALA 'Well, if you need anything, I’ll be around! Okay?'
    MC @talk 'Sounds good.'
    'As Vala smiled and waved shyly, I watched her cute butt as she sauntered off to go grab more books.'
    hide vala with dissolve
    if QstIsOver(QstTerminus):
        BLACK 'Her heartbeat raised when she saw you, and her hands began to sweat.'
        BLACK 'With some commitment, she would be a willing and good mate.'
        MC 'Stop... I... '
        'I shook my head to try push aside the dark thoughts.'
        MC @angry 'We’re here to try and gather some information, not hunting for another ‘mate’'
        BLACK 'As you wish.'
        MC '{i}*Sigh*{/i}'
    'Now, where to start? This place is huge...'
    return