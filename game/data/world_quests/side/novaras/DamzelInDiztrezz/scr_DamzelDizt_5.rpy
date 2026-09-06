label qst_DamzelDizzt_5_evidence:
    TAREK @angry '...What?'
    TAREK @angry 'Who are you to tell me what to do?'
    MC @talk 'I also want you to leave Nijah and the others alone.'
    'Markus glanced over in my direction, unsure as to why I was straying from the plan so suddenly.'
    TAREK @smile 'Is this some kind of a fucking joke?'
    TAREK @angry 'Why should I not just kill you and your friend here and now?'
    menu:
        "If you stay here, you're going to inevitably die.":
            TAREK @angry 'What are you talking about?'
            TAREK @angry 'Are you threatening me?'
            menu:
                "Everyone here hates you, someone is gonna stick a knife in your back eventually!":
                    TAREK @smile "You are a fool, aren't you?"
                    TAREK @angry 'You think I am not aware of the danger?'
                    TAREK @angry 'Unlike you Alderians, we Ramonians have little rights here, THIS is the only life for many of us thanks to your government!'
                    MC @angry "Easy to say now, not so much when the daggers are drawn and surrounding you."
                    TAREK 'Hmph... And Nijah here, why do you care about some Ramonian whore?'
                    MC @talk "My reasons are my own."
                    TAREK 'So you come here, with veiled threats that I will be killed, demand I abandon my kin AND forgive the debt of this whore?'
                    TAREK 'I have one simple question... Why?'
                "The factions you hold together have little in common and actively despise each other, you're living in a house of cards.": #This option can only appear if player has received prior info speaking to people about the gangs.
                    TAREK "I'm strong enough to hold them together."
                    TAREK "Under my leadership we've taken more territory than any of them could have hoped to achieve on their own!"
                    TAREK 'Why would they risk giving that up?'
                    MC @talk "And what about when you aren't there to hold them together?"
                    TAREK 'What are you talking about?'
                    TAREK @angry 'Do not try to fool me with mind games!'
                    MC @talk "I'm not, what about if you get sick or you're arrested by the guards?"
                    MC @talk 'How long will they last without you?'
                    MC @talk 'The moment you leave, the ensuing void of power in your absence will cause infighting.'
                    TAREK @smile 'The guards will never arrest me! Half of them are in my pocket and I am not weak, no sickness will keep me down for long!'
                    MC @talk "You're missing the point, the moment they sense weakness, this alliance you've formed will turn on you."
                    MC @talk "If the guards arrest you even on some fake charge, you'll still be imprisoned for at best, a few days, at worse, months."
                    MC @talk 'How long do you give it before the Vulshans and Khazahs are at each others throats again?'
                    MC @talk 'How long till one faction decides to try and tip the scales of the alliance in their favor? Or begins pushing other alliance members territory boundaries?'
                    TAREK 'Then I will just bring them back into line once I return!'
                    MC @talk "Tarek... You know this cannot last."
                    MC @talk 'If you are the only thing holding them them together, collapse is inevitable.'
                    TAREK '...Hmph, perhaps you speak some truth.'
                    TAREK 'But I cannot just abandon my men, not after all we have achieved.'
                    MC @talk "What if I found you proof?"
                    TAREK 'Of what?'
                    MC @talk 'That one of these gang factions is going to betray you.'
                    'Tarek pondered the thought for a moment, his eyes staring into my very soul before he spoke.'
                    TAREK "...You're very strange, normally someone would just try and poison me or something."
                    TAREK @smile '{i}You{/i} on the other hand, just walk in here and ask me to leave...'
                    MC @talk 'Conflict is not always the answer, I believe I can persuade you to leave peacefully.'
                    TAREK "Tsch, are you a holy man or something? Look around you... There's little room left for mercy in this world."
                    MC @talk "You're wrong, there's always time for mercy."
                    TAREK '...{i}*Sigh*{/i} I cannot believe I am agreeing to this, but very well.'
                    TAREK 'If you can find me proof of impending betrayal, proof that all of {i}this{/i} will fall apart soon.'
                    TAREK 'Then I shall take my leave.'
                    MC @talk "Then it's settled, I shall find some proof."
                    TAREK @angry "Hmph... Don't return unless you have something to show me."
                    TAREK @angry 'Otherwise, you will not walk out of here alive...'
                            #Sub quest unlock, Finding Evidence.
                    jump qst_DamzelDizzt_5_evidence_initial
                            #Upon leaving the Office
        "{image=[ICON.SWORDS]} You may try.":
            TAREK @angry 'GUARDS! INTRUDER!'
            MARKUS "You just had to fucking show how ballsy you are, didn't you?"
            #Fight ensues, default to Assault route.
            jump qst_DamzelDizzt_3_ruckus

label qst_DamzelDizzt_5_evidence_initial:
    scene black with dissolve
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush(dissolve)
    $ QstStart(HouseLockBlackDiamond)
    $ HouseLockBlackDiamond().canBeAccessed = True
    $ HouseLockBlackDiamond().canExit = True
    $ GoalShow(QstDamzelInDiztrezz, 7)
    $ BlockWaitDynamic(False)
    $ QstSetProgress(QstDamzelInDiztrezz, 1)
    show mc at left
    show markus at right_f
    show nijah at center_f
    with dissolve
    MARKUS @shock 'Why the sudden change in plan?'
    MC @talk 'If I can avoid unnecessary bloodshed, then so be it.'
    MARKUS 'Hmph... Well, next time let me know before you change course suddenly.'
    MARKUS @angry 'I was ready to leap across the table and go for his throat!'
    MC @talk 'I know but, I feel this is the best way.'
    NIJAH @angry 'I do not understand... Tarek iz bad man, everyone would be better off if he were dead!'
    MC @talk "This is my choice, I prefer not to kill unless I have to."
    'Nijah seemed unsure of my decision, but begrudgingly remained silent.'
    MARKUS "What now? Where are we to find this 'proof' that may not even exist?"
    MC @talk "There will be proof, of that I'm certain."
    MC @talk 'With all these factions baying for blood, someone will know something around here...'
    $ LocEnter()