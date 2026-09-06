label rom_Ves_1_GetMeds:
    #SCENE 2 VES 'CAMP MORNING'
    #EN. THE PLAYER RETURNS TO THE CAMP THE NEXT DAY. '
    $ NoteLock("VesRomance0")
    show ves with dissolve:
        xcenter 0.55
        xzoom -1.0
    show mc with easeinleft:
        xcenter 0.15
    "Entering her tent, I saw Ves."
    "She seemed concerned over something, but dropped it the moment I appeared."
    MC @talk 'Still surviving, I see.'
    VES @talk 'Is there a reason you keep coming back here, human?'
    MC @talk 'No, just making sure you don’t need anything.'
    VES @talk '{i}*Sigh*{/i} I am fine.'
    VES @talk 'Why do you persist in checking up on me?'
    VES @talk 'Is this some kind of trick?'
    menu:
        'Oh yeah, me skipping out into the middle of the desert to check up on you is all just part of some elaborate joke.':
            VES @talk 'You... Is this human humour?'
            MC @talk 'More like sarcasm.'
            VES @talk '... Is that some kind of fish?' #Confused
            MC @talk 'It’s... Never mind.'
            'Ves contemplated my words for a moment, unsure if I was insulting her or not before shaking her head in annoyance.'
        'It’s not a trick, Ves... I’m concerned about you.':
            VES @talk 'Why? Why are you concerned about me?'
            menu:
                'Because you’re all alone out here.':
                    VES @talk 'I have been {i}alone{/i} most of my life...' #Sad
                    VES @talk 'Most of my friends and family are dead.'
                    MC @talk '... Ves.' #Sad
                    VES @talk '... {i}War{/i} is not kind to those with many friends.'
                    VES @talk 'You are better off alone.'
                'I don’t know... Just because, I suppose...':
                    VES @talk 'seemed taken aback by the comment.'
                    VES @talk 'You... You are a very strange man!' #Surprised
                    MC @talk 'Well... I guess I can’t argue with that.'#Laughing
                'Oh, I’m just trying to woo you into taking your clothes off if we’re being honest.':
                    VES @talk 'blushed at the comment, her eyes widened in surprise.'
                    VES @talk 'You... {i}What?{/i}' #Blushing
                    MC @talk ' I, uhh, that was supposed to make you laugh...' #Smiling
                    VES @talk 'Why would you say such a thing?' #Serious
                    'Ves raised her axes towards me once again.'
                    VES @talk 'Is this some kind of mind game sorcery?'
                    MC @talk 'Hey hey! It’s just a little flirting!' #Surprised
                    VES @talk 'Flirting?' #Confused
                    MC @talk 'You know! Like, I was just joking around a little to try and make you laugh!' #Neutral
                    'Strangely Ves’ eyes seemed to darken as her usual cold expression quickly returned to her features.'
                    VES @talk ' ... Oh... A joke... Yes.' #Serious
                    VES @talk 'I know what those are.'
                    MC @talk 'Uhh, it wasn’t— '
                    VES @talk '...'
                    MC @talk '... Never mind.'


    #ALL ROUTES CONTINUED
    MC @talk 'Look, do you need anything out here?' #Neutral
    MC @talk 'Supplies? Food? Water?'
    MC @talk 'I can bring whatever you need from Novaras if you want.'
    MC @talk 'If you’re going to stubbornly continue to stay out here, the least you could do is let me get you some stuff to help.'
    VES @talk '... I suppose...'
    VES @talk 'I could do with some medicine if there is any.'
    MC @talk 'Medicine? Are you sick?' #Concerned
    VES @talk 'No, but... I was stung by some beast a few nights ago and found myself in a terrible fever the nights that followed.'
    VES @talk 'It was lucky I had stocked up on enough food and water to survive but...'
    VES @talk 'Next time I may not be so lucky.'
    MC @talk '... Alright.'
    MC @talk ' I’ll see what I can do.' #Neutral
    'As I turned to leave, Ves’ hand raised to stop me and her mouth hung open to say something, but instead, she paused and withdrew once again.'
    $ CharChangeRel("ves", 1)
    MC '(If it’s anti-venom and potions for healing I’m looking for, the Mages of Palam would be my best bet.)'
    MC '(They have an entire tower at the Mage’s Academy devoted to the goddess Palam... I should head there.)'
    $ QstSetProgress(RomanceVes, 2)
    $ QstStart(QstGreenFever)
    $ LocEnter()
