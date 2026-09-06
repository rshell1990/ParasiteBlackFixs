label qst_BiteBark_0_startEvent:
    $ QstComplete(PrimerBiteBark)
    show regina at left with dissolve
    show mc at cright_f with easeinright
    REGINA @talk 'There you are.'
    MC '{i}*Sigh*{/i}'
    MC @talk 'What have I done now?'
    REGINA @talk "Nothing, well, I want to talk to you about your new 'adventuring' role."
    MC @talk 'Hm? What about it?'
    REGINA @talk 'I want you to get yourself a pet.'
    'I stared dumbfounded at [regina_ref!t] for a few moments.'
    MC @surprised 'A... {i}pet?{/i}'
    REGINA @talk 'Not just any pet, something that could act as a companion for you.'
    REGINA @talk 'Lots of new adventurers usually saddle themselves with a wolf or a war hound or something.'
    MC @talk "{i}*Sigh*{/i} I don't know, that sounds like a lot of work."
    REGINA sad_talk "[player_name!t]... It's important to me that you keep safe out there."
    MC @talk "Alright, fine, I'll look into it."
    REGINA @smile_talk 'Thanks sweetie.'
    hide regina with easeoutright
    'Regina kissed me on the cheek as she slide on by, going about her business as usual.'
    MC '(I suppose I could check down at the kennel to see what the beast master has to offer...)'
    $ QstStart(QstBiteBark)
    $ LocEnter()
