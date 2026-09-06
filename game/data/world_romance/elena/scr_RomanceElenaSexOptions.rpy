label rom_ElenaSexOptions:
    ELENA @talk 'What did you have in mind?'
    menu:
        'On second thought...':
            MC @talk 'Never mind, I just remembered something I had to do.'
            ELENA @talk 'Oh... Well, very well then.' #Loops back to main dialogue
            return
        'How about we take another bath?':
            jump rom_ElenaRepBath
        'I was thinking maybe you could dance for me again...':
            jump rom_ElenaRepDanceGrind
        'I was wondering if you would be interested in {i}cooking{/i} for me again?' if QstGetProgress(RomanceElena) >= 10:
            jump rom_ElenaRepCooking
