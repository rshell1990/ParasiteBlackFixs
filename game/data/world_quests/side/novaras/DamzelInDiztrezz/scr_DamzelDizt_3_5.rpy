# leaving tarek place after hes dealt with
label qst_DamzelDizzt_3_leavingTarekOffice:
    $ LocSet("novaras_black_diamond")
    $ LocFlush()
    show nijah at right_f
    show markus at cright_f
    show mc at center
    with dissolve
    show cg_bandit at left with easeinleft
    "As we left Tarek's office, we were approached by one of the thugs."

    THUG "Heard some noise in there."
    'He threw a suspicious glare at us...'
    THUG "Say, is the boss alright?"
    menu:
        'He asked us to leave him alone for now.' (Req_Charm = 6): #(Charm check - FAIL)
            $ rng = RngInt(1,3)
            if rng == 1:
                'Ouch, he clearly saw through it.'
                THUG '...'
                THUG 'Liar!'
                MC @talk '(Shit!)'
                THUG 'SPIES!'
                MC @talk '(Fuck!)'
                scene black with dissolve
                play sound2 "audio/cfx/transform.ogg"
                jump qst_DamzelDizzt_3_ruckus_TarekDead
            if rng >= 2:
                THUG 'Then why are you bringing the girl back with you?'
                MC @talk "I’m taking her somewhere on Tarek's orders."
                MC @talk 'Would you like to disturb Tarek and ask him yourself?'
                THUG '...'
                'The guard pondered the thought for a moment before shaking his head.'
                'Opening the door, he let us out into the night.'
                hide cg_bandit with easeoutleft
                NIJAH 'We must hurry, before they realise Tarek is gone!'
                'Quickly, we made our way hastily into the night.'
                jump nijah_damzelDiztrezz_afterAction
        '... Fuck you!':
            THUG 'Wha...'
            THUG 'SPIES! DRAW YOUR BLADES, MEN!'
            jump qst_DamzelDizzt_3_ruckus_TarekDead
