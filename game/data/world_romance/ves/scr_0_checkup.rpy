label rom_Ves_0_checkup:
    'Ves raised a curious eyebrow at my comment.'
    VES @talk '... I’m fine.'
    VES @talk 'Why do you ask, human?”'
    MC @talk 'Just out of concern, you’re out here all alone.'
    MC @talk 'It’s not safe.'
    VES @talk '... Where is safe for an orc in this land?'
    VES @talk 'I have survived this long... I will find my kin eventually and leave this empty place.'
    MC @talk 'And what if you don’t find them?'
    VES @talk 'I will.'
    MC @talk 'But what if you {i}don’t?{/i}'
    VES @talk '{i}Tsch...{/i} Why do you care what happens to an orc anyway?'
    VES @talk 'Humans and orcs do not mix.'
    MC @talk 'You weren’t complaining when we saved you the other day.'
    'Ves growled menacingly at the comment.'
    VES @talk 'First off, you didn’t {i}save{/i} me.'
    VES @talk 'I could have handled that just fine on my own.'
    MC @talk '... I didn’t come here to fight.'
    VES @talk  'Then why did you come here?' #Raised Eyebrow
    'Ves pointed her axe towards me.'
    VES @talk 'You may not be fully human...' #Annoyed
    VES @talk 'But I’ve come to know the ways of man.'
    VES @talk 'You’ll be no different to the rest of them.'
    MC @talk '... Do you need some hel— '
    VES @talk 'No.'
    'Rising from her feet, Ves stretched and sauntered out the tent with her axe in hand, barging past my shoulder as she remarked.'
    VES @talk  'You’ve seen that I am well... Now {i}leave.{/i}' #'Neutral
    $ LocSet("ves_camp")
    $ LocFlush(dissolve)
    'With that, I watched as Ves made her way alone across the dunes of the Valley of Death, slowly disappearing into the distant blistering waves of heat.'
    'I called after her, asking where she was going, and she turned, still walking backwards as she cried out ‘to hunt!’ And like that, she was gone... Leaving me alone in the swirling hot sands of her campsite.'
    MC @talk '(... Well... That could have gone better.) '
    MC @talk '(Maybe I should check on her another time?)'
    $ AutoMus(True)
    $ QstSetProgress(RomanceVes, 1)
    $ DialogueVes().outHunting = True
    $ NoteUnlock("VesRomance0")
    $ LocEnterQ()
