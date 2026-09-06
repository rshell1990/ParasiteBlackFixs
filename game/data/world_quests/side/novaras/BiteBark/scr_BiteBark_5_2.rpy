label qst_BiteBark_5_FoundWolfAtBaba:
    #Scene 6 - Soothsayer Hut
    #Elena/Wolf can be found here - Just show Babazhul but let dialogue flow
    show babazhul:
        pos (0.0, 0.0)
    with dissolve
    'As I entered the soothsayers hut, I found my wolf companion sat patiently in waiting as Babazhul laughed.'
    BABAZHUL @talk 'Ha! How charmed your companion is...'
    MC @talk'There she is! My apologies if my pet has disturbed you.'
    BABAZHUL @talk 'Not at all! I always appreciate the company of such an interesting lady.'
    MC @talk'...{i}Interesting lady?{/i}'
    MC @talk"I'm afraid you'll find little conversation from this one, she hardly even makes a sound!"
    BABAZHUL @talk 'Oh, she has said plenty already.'
    ELENA_W '...'
    'I looked back and forth from Babazhul to the wolf which sat silently, confused as to whether the old crow was simply playing some kind of trick on me.'
    'Suddenly, the crystal ball between her hands illuminated before she looked not at me, {i}but the wolf.{/i}'
    BABAZHUL @talk 'Hear my words Elena, what is lost to you shall return.'
    BABAZHUL @talk 'With this one here, shall the path become clear...'
    "Babazhul's boney hands pointed towards me, and the wolf looked towards me and then back towards Babazhul, barking frantically."
    MC @talk'{i}(Elena?){/i}'
    BABAZHUL @talk 'I can say no more girl.'
    "The ball dimmed and 'Elena' began to growl."
    MC @angry"That's enough now!"
    'Grabbing Elena by the scruff of the neck, I began to pull her away, she struggled at first but eventually relented, allowing me to drag her outside.'
    MC @talk "Come on, I'm taking you home."
    MC @talk 'Then, I have some questions...!'
    hide babazhul with dissolve
    $ QstSetProgress(QstBiteBark, 5)
    $ LocSet("novaras_dist_pleasure")
    $ LocEnterQ()
