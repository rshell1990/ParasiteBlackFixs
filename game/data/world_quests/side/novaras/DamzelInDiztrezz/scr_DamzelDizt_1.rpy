label qst_DamzelDizzt_1:
    # jump to black then to markus house
    scene black with dissolve
    "I have found Markus at his home."
    "With the two of us, we should be able to deal with Nijah's situation easily enough."
    $ LocFlush()
    show mc at left
    show markus at right_f
    with dissolve
    MARKUS 'What brings you here [player_name!t]?'
    MC @talk 'Markus, I need your help with something...'
    MARKUS 'Oh no...'
    MARKUS 'Not that face, I can tell when you have THAT face it isn’t going to be anything I want to be involved in.'
    MC @talk 'I want your help clearing out a gang who are preying on the Ramonian people.'
    MARKUS 'Anddddd there it is!'
    MARKUS "Impressive, one sentence in and I'm already shaking my head!"
    MC @talk 'Come on Markus!'
    MARKUS 'Why in all of Alderay are you dragging me into this mess?'
    MC @talk 'Because with our {i}‘gifts’{/i} we can have them gone by tonight!'
    MARKUS 'Urghh! Always trying to be the bloody hero!'
    MARKUS '... This is about a girl, isn’t it?'
    MC @talk 'That... That doesn’t matter!'
    MARKUS 'Uhuh, yeah, it’s about a girl.'
    MC @talk 'Markus!'
    MARKUS 'I don’t see why this is our business.'
    MARKUS 'Let the Ramonians sort out their own!'
    MARKUS 'They keep to their end; I keep to mine.'
    MC @talk 'I need you for this one.'
    MC @talk "I'm going to do it with, or without you."
    MARKUS '...'
    MC @talk "Now either you'll help me, or you won't."
    'Markus thought about it for a moment before sighing,'
    MARKUS '... Fine.'
    MARKUS 'You know if I didn’t love you like a brother this would never happen, right?'
    MC @talk 'I owe you for this, Markus.'
    MARKUS 'You owe me nothing you bloody fool.'
    MC @talk 'Then come, we have to head back to mine to plan for tonight...'
    'Markus nodded as he traipsed behind me back to mine.'
    hide mc
    hide markus
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    with dissolve
    # home again
    show nijah with dissolve:
        xcenter 0.75
        xzoom -1.0
    show mc at cleft
    show markus at left
    with easeinleft
    MARKUS "Well, are you ready to discuss whatever you've just dragged me into?"
    # black, maybe some diamond scenes?
    'Nijah explained to us everything she could about Tarek and his men.'
    scene bg_diamond with pixellate
    'She told us what she could remember of visiting the {i}Black Diamond{/i} herself when she came seeking a loan,'
    'And she told us that we should expect nearly two dozen of them inside, including Tarek himself.'
    'Through a complex series of heavy bribes, Tarek and his men have been allowed to continue uninterrupted by the City Guard,'
    'So it seems taking the matter to the law was now out of the question entirely.'
    # home scene again
    $ LocFlush()
    show nijah:
        xcenter 0.75
        xzoom -1.0
    show mc at cleft
    show markus at left
    with pixellate
    MARKUS 'That’s... a lot of men, you know.'
    MARKUS 'If we kick the door in, claws out, no doubt the City Guard will come to see what the ruckus is about.'
    NIJAH "Tarek's Office below..."
    MARKUS 'Below?'
    NIJAH 'Yis, zer is a iron door zat leads to his office below...'
    MARKUS 'They’re no doubt armed and ready... This might be like trying to storm a small fortress.'
    MARKUS 'Not to mention the people already there who might get caught up in the fight.'
    MC @talk 'You’re not bailing out on me, right?'
    MARKUS "Of course not, I've been itchin' to test our powers some more."
    MARKUS "But this isn't exactly what I had in mind."
    'Nijah raised a curious eyebrow at the phrase.'
    NIJAH 'Powers?'
    MARKUS 'Uhh, never mind.'
    MC @talk 'So, any ideas then?'
    MARKUS 'Well, our first option is that we just kick the door in and slaughter everyone inside.'
    MARKUS 'The second, if what Nijah is telling us is right, is that Tarek seems to be the only one holding together a loose connection of gangs.'
    'As long as we can get rid of him one way or another, we shouldn’t need to deal with the others.'
    MARKUS 'They’ll fall apart without him.'
    MC @talk 'Any other ideas?'
    MARKUS 'Hmm... I guess we could try persuading him very nicely to leave but...'
    MARKUS 'Something tells me that isn’t going to work.'
    return
