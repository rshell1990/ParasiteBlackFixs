label rom_Nijah_stage1_future_lines:
    MC @talk 'Say... Now that Tarek is dealt with, what are you going to do?'
    'Nijah pondered the thought for a moment, unsure of an opportunity she had never expected to have.'
    NIJAH 'I don’t know...'
    NIJAH 'I suppose I could go back to working at za Pleasure District...'
    NIJAH '... The money is good, but iz not the safest job...'
    MC @talk '... Is that your only option?'
    NIJAH 'There is other way, but I’d need investors.'
    MC @talk 'Investors? What are you planning?'
    NIJAH 'I can cook food...'
    MC @talk 'What? Like bakery food?'
    NIJAH 'No, no... Ramonian street food!'
    NIJAH 'Food quick, tasty for people to eat while on go...'
    MC @smile "Ha-ha! You're full of surprises..."
    MC @talk 'Well how much do you need?'
    NIJAH 'Enough for stall... Plus ingredients and cooking equipment...'
    NIJAH 'At least thousand gold...'
    '(That’s quite a lot.)'
    '(What should I encourage her to do?)'
    menu rom_Nijah_stage1_future_lines_menu:
        'Tell Nijah you’ll invest in her business':
            NIJAH @happy '...!'
            NIJAH @smile 'You will?'
            NIJAH @smile 'A thousand gold?'
            NIJAH 'I... I cannot ask you to do zis!'
            menu:
                'Give Nijah the gold' (Req_Gold = 1000):
                    $ PlayerRemItem('gold', 1000)
                    $ CharAddRelEntry("nijah", "market_stall")
                    NIJAH 'Zis is...'
                    'Nijah started to cry'
                    NIJAH @sad'... You haz done too much for me.'
                    scene black with dissolve
                    'Nijah hurried forward, wrapping her arms around me in a tight hug, when she pulled back, she smiled warmly, tears streaming down her cheeks in joy.'
                    jump rom_Nijah_stage2_afterInvest

                'I’ll be back soon.':
                    NIJAH 'Alright... I trust you... I shall wait for you.'
                    $ LocEnter()

        'Tell Nijah you’ll become her pimp':
            NIJAH 'You... Vat?'
            MC @talk "I’ll pay for you to have your own room."
            MC @talk 'As a Novaras citizen, I can quickly and legally get the paperwork you need.'
            MC @talk 'I can also guarantee you have some protection that before you was not privy to.'
            MC 'Nijah pondered the thought a moment, hesistant about the idea of returning to her old line of work.'
            NIJAH 'This... would be better.'
            NIJAH '{i}But...{/i}'
            MC 'Nijah opened her mouth to protest, but instead, her eyes simply dropped to the floor as she reached and grabbed at her other arm anxiously.'
            NIJAH 'In return, you want share of gold I earn?'
            MC @talk 'I do.'
            NIJAH '... Thirty percent?'
            menu:
                'Sure.':
                    MC @talk "Yeah, that's a deal."
                "Forty." (Req_Charm = 8):
                    $ RomanceNijah().pimpEarnRange += 100
                    NIJAH 'Alright... I suppose after all you have done zis iz fair...'
            NIJAH 'I come with you to speak to men in charge of district...'
            #SCREEN FADES TO BLACK.
            scene black with dissolve
            "Following Nijah down to the District, she introduced me to one of the officials there, a tall and uninspiring rake of a man who sat down in one of the few ‘offices’ littered around the District that the girls use when they want to lodge complaints."
            "When I showed him my gold, it didn’t exactly take long to have the right paperwork and such in place. In just a few hours, we were set to go..."
            'Nijah had her own room, and it was known to all that she was a protected girl now.'
            $ LocFlush()
            with dissolve
            show nijah:
                xcenter 0.5
                xzoom -1.0
            with dissolve
            NIJAH 'Zat was... very quick.'
            NIJAH 'It would take a Ramonian like me weeks to get anywhere with them.'
            MC @talk 'Being a citizen has its benefits.'
            NIJAH 'I suppose I better get back to za work... Stop by to collect your money once a fortnight.'
            MC @talk "Let me know if there are any problems, remember, you are protected by me now."
            MC @talk 'I will see to it that no harm comes to you.'
            'Nijah smiled unconvincingly, but nodded anyway.'
            NIJAH 'T-Thank you... Now if you excuse me, I should get ready.'
            MC "I watched as Nijah headed off, no doubt to prepare for her {i}'clients'{/i}"
            scene black with dissolve
            "And just like that, Nijah returned to her old work... A part of me wondered if I’d made the right choice, if perhaps, Nijah wanted and deserved better than this life?"
            'But, as I reminded myself, she was now safer than before... And my pockets were going to get a lot heavier. Morality aside, maybe this was for the best.'
            $ CharChangeRel("nijah", 1)
            $ CharAddRelEntry("nijah", "pimped_out")
            $ NoteUnlock("NijahRomancePimp")
            $ QstSetProgress(RomanceNijah, 2)
            $ RomanceNijah().becamePimp = True
            $ LocSet("novaras_dist_house")
            $ LocEnter()
        'On second thought...':
            call processDialogue("nijah_root") from _call_processDialogue_25
    return
