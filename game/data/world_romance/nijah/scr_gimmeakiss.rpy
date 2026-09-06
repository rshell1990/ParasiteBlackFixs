label rom_Nijah_gimmeakiss:
    NIJAH @smile 'Ah! Come here!'
    hide nijah with dissolve
    show cg_nijah_kiss_clothed with dissolve:
        align (0.5,0.0)
        yoffset 50
    $ Pause()
    #MC and Nijah kiss sprite 
    NIJAH 'S-Stay for while longer, yes?'
    hide cg_nijah_kiss_clothed with dissolve
    show nijah:
        xcenter 0.5
        xzoom -1.0
    with dissolve
    return