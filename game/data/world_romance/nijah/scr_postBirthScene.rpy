label nijah_post_birth_scene:
    show nijah_baby at center with dissolve
    "Entering into Nijah's home, Nijah smiled as she held in her hands a small child of light dark complexion."
    NIJAH @smile 'Ah! There you are!'
    MC @surprised 'Is that-'
    NIJAH 'Look, our child...'
    'Nijah held out and showed the small baby to me, whose eyes seemed identical to mine.'
    BLACK '{i}(The seed is strong... Ours shall be a strong warrior).{/i}'
    #Insert option to name kid - default names for first three children are '...'
    $ PregNijah().LastBornBabyName = renpy.input(_("What name shall we give, my love?"), default = renpy.random.choice(PregNijah().BabyNameRandomList))
    NIJAH 'Hmm, [PregNijah().LastBornBabyName] iz a good name!'
    MC @talk 'How are you feeling?'
    NIJAH 'Tired, but went well.'
    NIJAH "Midwives were surprised, they said our child's birth was the easiest they had ever seen."
    NIJAH '...Zis because of your {i}gift?{/i}'
    BLACK "{i}(Yes, it is good to not allow hosts to die when they can sire many young for us).{/i}"
    MC @talk 'Uhh, yes.'
    NIJAH 'Zis is good to know because...'
    'Nijah alluringly stepped towards me, pressing her breasts against my chest as her hands run down my chest.'
    NIJAH @lewd "{i}We must have a very big family!{/i}"
    MC @surprised "{i}*Gulp!*{/i}"
    scene black with dissolve
    'For the next hour or so, I spent some time with Nijah and our new-born child, playing and watching them with a new-found pride.'
    'Whether it was by the {i}Dark passengers{/i} design within me, or my own natural paternal instincts stiring, I felt rejuvenated and stronger as I watched my child playfully reach out to grab my hand.'
    'A short while later, I left Nijah alone once again, onwards towards whatever was next.'
    $ LocSet("novaras_dist_house")
    $ LocEnter()