label qst_DamzelDizzt_0:
    MC @talk "I'm gonna deal with Tarek."
    MC @talk 'Where can I find him?'
    NIJAH 'Iz too dangerous!'
    NIJAH 'You will die! Iz stupid!'
    MC @talk 'Trust me Nijah, I won’t be the one dying.'
    NIJAH 'He...'
    NIJAH 'You find him at za {i}Black Diamond.{/i}'
    MC @talk 'The {i}‘Black Diamond?’{/i}'
    'Nijah nodded anxiously.'
    NIJAH 'Iz a Raza Den, they keep the girls hooked on Raza as much as the clients.'
    NIJAH '{i}Bad place...{/i}'
    MC "(I'll need Markus on this one...)"
    menu:
        "Okay, let's get this done.":
            MC @talk "Okay, let's get this done."
            $ QstStart(QstDamzelInDiztrezz)
            $ GoalShow(QstDamzelInDiztrezz, 1)
            "As I turned to leave for Markus' place, Nijah reached out and grabbed my hand."
            NIJAH 'Wait!'
            NIJAH 'Why... Why are you doing zis?'
            if CharGetVar("nijah", "prologueMet") == True:
                NIJAH 'We... only know each other for not very long...'
            else:
                NIJAH 'We have only just met... I am a stranger.'
                NIJAH 'Just another Ramonian girl...'

            menu: #I will deal with Tarek continued
                'Because it’s the right thing to do.':
                    MC @talk 'Because it’s the right thing to do.'
                    $ CharChangeRel("nijah", 1)
                    'Nijah smiled warmly at my response before letting me go.'
                    NIJAH 'You are... a good man.'
                    'Her eyes lit up all glassy like as they began welling up with tears as she looked up at me.'
                    jump nijah_damzelDiztrezz_getMarkus

                'Because {i}I{/i} intend to rule this city, and I don’t like competition.':
                    MC @talk 'Because {i}I{/i} intend to rule this city, and I don’t like competition.'
                    'Nijah seemed slightly taken aback at the answer, and a little unsure how to respond.'
                    NIJAH 'L-Let us hope you are kinder zan them then...'
                    'Nijah dropped my hand, not quite sure what to make of me.'
                    jump nijah_damzelDiztrezz_getMarkus

                'We fucked.' if CharGetVar("nijah", "prologueMet") == True:
                    MC @talk 'We fucked.'
                    'Nijah blushed at the comment,'
                    'She looked up coyly towards me, reminding me of the woman I’d met that first night in the Pleasure District.'
                    NIJAH '(...I fuck him that good?)'
                    jump nijah_damzelDiztrezz_getMarkus

                'My reasons are my own...':
                    MC @talk 'My reasons are my own.'
                    'Nijah didn’t respond to my answer, nor could I deduce anything from her face.'
                    'As she let go of my hand, she seemed more puzzled than anything else.'
                    jump nijah_damzelDiztrezz_getMarkus

        'I need some more time to think, wait here.':
            NIJAH 'Y-Yes, I wait here.'
            return
