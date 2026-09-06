label evscr_nijah_rescue_3:
    show regina at left
    'Leading Nijah back to mine, Regina smiled as she heard the door open, her face quickly turning to bewilderment when she caught sight of Nijah.'
    show mc at center_f
    show nijah at cright_f
    with easeinright
    REGINA @talk '[player_name!t]! There you—'
    REGINA @talk 'Uhhh... Who’s—'
    if CharGetVar("nijah", "prologueMet"):
        MC @talk 'She’s a friend of mine.'
        'Regina raised a curious eyebrow.'
        REGINA @talk '... A ‘friend’ hmm?'
        REGINA @talk "Well... Aren’t you going to introduce me to this {i}'friend?'{/i}"
    else:
        MC @talk 'Long story, I was just out when I heard some screaming.'
        MC @talk 'I followed the cries and found her being attacked by some street gangs.'
        'Nijah shyly hide behind me.'
        NIJAH 'F-Friend saved me.'
        'Regina folded her arms.'
        REGINA @talk '...So instead of just going to the guards, you thought to bring her {i}here?{/i}'
        MC @talk "Well I didn't know where else to take her!"
        REGINA @talk '{i}*Sigh*{/i} Well, does she have a name?'
    MC @talk '[regina_ref_cap!t], this is Nijah.'
    MC @talk 'Nijah, this is [regina_ref!t].'
    'Nijah softly waved her hand shyly,'
    NIJAH 'H-Hello...'
    NIJAH 'It iz good to make your...'
    'Nijah struggled on the word.'
    NIJAH 'It iz good to meet you!'
    'Regina smiled uncomfortably.'
    REGINA @talk 'Uhh, yes. likewise, dear.'
    MC @talk 'Nijah, go wait in my room a moment.'
    'Nijah looked puzzled as she looked around for a second.'
    NIJAH 'Such big home...'
    REGINA @talk '...'
    MC @talk 'My room is just there down the Hall.'
    'With my hand on her back, I pointed towards the door at the end of the hallway which Nijah nervously headed towards,'
    hide nijah with easeoutleft
    'With her hand on the door handle, she anxiously looking back at me again to be sure, to which I once again waved to tell her go in.'
    'As soon as Nijah stepped inside and was out of sight, [regina_ref!t] turned and snapped at me.'
    REGINA @talk "What in the seven hells do you think you're doing?!"
    MC @talk 'It’s not what you think!'
    REGINA @talk 'Oh? So that isn’t some Ramonian girl in your room right now?'
    MC @talk 'Well... Yes, but—'
    REGINA @talk 'You know she can’t stay here, right?'
    REGINA @talk 'If the guards find us giving residency to refugees without the right paperwork, we could be imprisoned!'
    MC @talk 'She was being attacked! What was I supposed to do? Sit back and let it happen?'
    REGINA @talk '{i}*Sigh*{/i} Please tell me you aren’t in love with her...'
    MC @talk 'What? No...'
    REGINA @talk "Then tell me she isn't pregnant."
    MC @talk 'Of course not!'
    BLACK "{b}YET.{/b}"
    MC @talk 'I told you! I just saved her back there!'
    REGINA @talk 'Good, because she can’t stay here.'
    MC @talk 'I can’t turn her back out onto the streets, people are after her!'
    REGINA @talk 'We don’t have a choice in the matter.'
    REGINA @talk "What don't you understand? It's a crime!"
    REGINA @'{i}*Sigh*{/i}'
    'Regina rubbed her brow in exasperation.'
    REGINA @talk 'She can stay the night but... that’s the best I can do, I’m sorry, dear.'
    MC @talk '... Alright, I’ll figure something out.'
    'As I passed by [regina_ref!t], she sighed dejectedly. She wasn’t a cruel person by nature, but she knew the dangers of defying the law in Alderay.'
    hide mc with easeoutleft
    'Still, it left me little time to deal with quite the predicament.'
    MC '(Nijah is waiting in my room, I should speak to her there.)'
    hide regina with dissolve
    return
