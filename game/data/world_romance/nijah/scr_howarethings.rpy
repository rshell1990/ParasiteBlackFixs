label rom_nijah_howarethings:
    $ rng = RngInt(0,3)
    if rng == 0:
        NIJAH 'Things are fine my love, though I do miss you vhen you iz gone so long...'
        MC @talk 'It cannot be helped I am afraid.'
        NIJAH 'That iz okay, you are good man.'
    if rng == 1:
        NIJAH 'Hmph, I was refused dress!'
        MC @talk 'What?'
        NIJAH 'I tried to buy a new dress today, but the store would not sell to me.'
        NIJAH '{i}*Sigh*{/i} This kingdom hates us... I wish you could take me home.'
        MC @talk 'Maybe one day Nijah, it’s not safe at the moment with the war going on.'
        NIJAH 'I know... But I dream anyway.'
    if rng == 2:
        NIJAH 'I received letter from my mother again today!'
        NIJAH 'She and father are doing well!'
        NIJAH '{i}*Sigh*{/i} I wish I could see them again one day.'
    if rng == 3:
        NIJAH 'Y-Yes my love...'
        MC @talk 'Nijah? What is it?'
        NIJAH '...C-Come take me to bed please, {i}I need you{/i} my love.'
        NIJAH 'You are zo... {i}addictive.{/i}'
        MC @talk "(That would be the creature's work.)"
    return