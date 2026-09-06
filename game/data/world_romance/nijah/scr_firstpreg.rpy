label preg_Nijah_goodNews_intro:
    show mc:
        xcenter 0.15
    show nijah:
        xcenter 0.5
        xzoom -1.0
    with dissolve
    'As I entered her home, Nijah came to me with hands clasped, nervous.'
    NIJAH 'Must speak with you.'
    'Sensing her distress, I placed my hands on her shoulders.'
    MC @talk 'Nijah, what’s wrong?'
    NIJAH 'I... I carry your child.'
    'I pulled back, surprised at the comment.'
    MC @talk "...{i}You’re pregnant?{/i}"
    'Nijah sheepishly nodded.'
    NIJAH '...Zis not problem?'
    MC @talk 'What do you mean?'
    NIJAH 'M-any Alderian men... They get Ramonian girls with child and go.'
    NIJAH '...many forced to get rid of child while still in womb.'
    NIJAH 'But... I want to keep your child.'
    BLACK 'She is fit to carry many of our young.'
    BLACK 'We should keep this one close as a mate.'
    MC @talk '...Nijah, I-'
    NIJAH 'I do not care if child can change into monster like you.'
    NIJAH 'It is {i}our{/i} baby, and that is good enough for me.'
    'Nijah seemed to wait anxiously for a few moments. Almost stand-offish, perhaps expecting me to tell her to get rid of the child or that I didn’t want to see her anymore.'
    MC @talk 'Nijah... {i}You are mine.{/i}'
    MC @talk 'I am pleased you carry my child.'
    "Nijah’s eyes seemed to light up."
    NIJAH 'R-Really?'
    'With a bright smile, Nijah flung herself onto me, planting  kiss onto my lips.'
    NIJAH 'M-Master... I love you so much!'
    MC @talk 'Nijah, you know you don’t need to-'
    'Nijah interrupted me again mid-sentence to plant another kiss on my lips.'
    NIJAH 'I shall get some dinner on, stay a while.'
    'With that, Nijah turned, humming happily to herself as she made her way to the kitchen to prepare some food.'
    # SCREEN FADES TO BLACK
    scene black with dissolve
    if not QstIsOver(EventFirstImpreg):
        $ QstStart(EventFirstImpreg)
    'After eating with Nijah, I departed once again, thinking about my soon to be new-born child I was now having with Nijah.'
    $ LocSet("novaras_dist_house")
    $ LocEnter()
