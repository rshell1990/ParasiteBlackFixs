label qst_BiteBark_5_SeenWolfRegina: #move to char dialogue trees
    #Player can ask multiple people if they've seen the wolf
    #Regina
    REGINA @shock_talk "Don't tell me you've lost her already?"
    MC @talk 'I- Uhh, no?'
    REGINA @angry_talk 'Good, that wolf is {i}very{/i} important, I suggest finding her quickly.'
    MC '(Why is she so taken with this wolf?)'
    return

label qst_BiteBark_5_SeenWolfLucius:
    #Merchant
    LUCIUSMAL 'A blue wolf you say?'
    LUCIUSMAL "Can't say I have, but if you were willing to bring me its pelt, I would-"
    MC @talk "She's not for sale."
    LUCIUSMAL 'Hm, shame...'
    return

label qst_BiteBark_5_SeenWolfKennelMaster:
    #KENNEL MASTER
    show kennelmaster with dissolve:
        xcenter 0.65
        xzoom -1.0
    show mc with easeinleft:
        xcenter 0.15
    KENNELMASTER '...HAHAHAHAHA!'
    KENNELMASTER 'You lost her already?'
    MC @angry "It's not funny."
    KENNELMASTER "It's a little funny."
    MC @talk 'Well, any idea where she went?'
    KENNELMASTER 'No idea, the one time she did slip out, we found her wandering aimlessly in the Pleasure District.'
    MC @talk 'Why?'
    KENNELMASTER 'Maybe she was looking for someone? Maybe she could just smell food? Who knows...'
    KENNELMASTER "Anyway, I can't help you more than that sorry."
    $ LocEnter()

label qst_BiteBark_5_SeenWolfArlena:
    #ARLENA
    ARLENA 'A blue wolf?'
    ARLENA "No, I haven't seen anything like that sorry."
    return

label qst_BiteBark_5_SeenWolfDivine:
    #SISTER DIVINE
    DIVINE 'Hmm... A blue wolf you say?'
    DIVINE 'Strange you mention it so,'
    DIVINE 'One of the sisters mentioned in passing that they had seen a calm wolf wandering around the pleasure District.'
    DIVINE 'Apparently, it seemed almost like she was reading the signs and was peering into windows looking for someone...'
    DIVINE "Odd... Don't you think?"
    return
