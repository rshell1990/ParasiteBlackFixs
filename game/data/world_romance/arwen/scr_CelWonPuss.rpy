label sexscene_ArwenCelesteWonPuss:
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
    scene arwen_cosp_won_vag with dissolve
    $ Pause()
    ARWEN 'Ah! Ah!'
    ARWEN 'M-My love! Mmmfghh!'
    ARWEN 'You feel s-so good!'
    ARWEN 'Mmmff!'
    MC 'Ahhh! C-Celeste!'
    MC 'You feel so tight!'
    ARWEN '{i}*Huff*{/i} Is it {i}*Huff*{/i} good for you?'
    MC 'It feels - ah! Incredible!'
    "{i}'Celeste'{/i} clamped down onto me tightly with every thrust, her hot breathes and whimpers only further excited me as her cheeks blushed crimson red in excitement."
    'I watched as her body swallowed up my member, warmly tightening around me as I continued to push myself into her hot body.'
    "I had to keep reminding myself this {i}was{/i} still Arwen, but not only had her mannerisms changed, but her whole body felt different."
    'As she moaned to the sound of every thrust, how easy it was to convince myself I was fucking someone else...'
    ARWEN 'Ah! Mmhmm!'
    ARWEN 'A-Are you close?'
    ARWEN 'I c-can feel you throbbing inside of me!'
    MC 'Grghh... Celeste, I-'
    ARWEN  "Shhh... It's okay my love."
    ARWEN "{i}Just let it out.{/i}"
    ARWEN "Let's finish together!"
    'Celeste gasped as I pinned her down, going harder than before with a reckless kind of abandon as I thrust myself into her.'
    'She winced occasionally struggling with my size, but her wetness and moans gave away that the pleasure was overriding it.'
    MC "{i}*Huff*{/i} I'm close!"
    'Instinctively, she squeezed me tighter as her starry like eyes locked into mine as she pleaded.'
    ARWEN 'D-Do it! Hurry up and finish my love!'
    "Unable to hold back any longer, the darkness inside me coursing through my veins like fire as the Parasite's desire to {i}breed{/i} drove me maddeningly wild and unable to stop."
    'I finally grunted and thrust deep into Celeste, unloading the thick seed from my aching balls.'
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    scene arwen_cosp_won_vag_finish with flash
    $ Pause()
    $ ReduceInfectionFromSex("arwen")
    $ UnlockGalFlag("arwen","cosp_won","var_vag")
    $ UnlockGalSceneAndGrantXp("arwen","cosp_won")
    ARWEN 'Mmmhhh!'
    ARWEN "Oooh... There's so much of it."
    $ AutoMus(True)
    scene black with dissolve
    'I slowly pulled out of Arwen and stumbled backwards slightly as I tried to re-dress myself.'
    'Arwen, shakily rose back to her own feet, her legs trembling as she began to re-dress herself with a happy but exhaustive grin on her face.'
    scene bg_weeping_heart_brothel_room
    show arwen at center_f
    with dissolve
    ARWEN @laugh 'So... How was the {i}special{/i} service?'
    ARWEN @talk 'Did you enjoy your time with {i}Celeste?{/i}'
    MC @smile 'It was... {i}different.{/i}'
    MC @talk 'But very good.'
    ARWEN @talk "It pleases me to hear you say that... Now come, I need to escort you back I'm afraid."
    MC @talk 'As you wish.'
    return
