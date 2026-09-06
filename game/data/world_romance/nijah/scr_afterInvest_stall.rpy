label nijah_howgoesthestall_lines:
    $ rng = RngInt(0,2)
    if rng == 0:    #Continued
        NIJAH 'Good! Business goes zo well!'
        NIJAH 'No one can resist good Ramonian food when done right!'
        NIJAH 'Nice and spicy!'
    if rng == 1:
        NIJAH 'Iz good, but the rain yesterday make business slower.'
        NIJAH 'To be expected though.'
    if rng == 2:
        NIJAH 'Very business! We may need to expand soon with how things go!'
    return