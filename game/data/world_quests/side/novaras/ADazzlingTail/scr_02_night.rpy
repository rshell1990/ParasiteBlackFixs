label qst_ADazzlingTail_02_night:
    show mc at cleft
    with dissolve
    'Wandering into the smithy, I heard a weird noise from upstairs.'
    MC "Huh? Sounds like..."
    "Hypnotized by moans barely heard, I felt I {i}have{/i} to check it out."
    "Only as I quietly climbed the stairs did I realise the sound is coming from Arlena's room..."
    $ CharSetClothes("arlena", "apron")
    scene arlena_mirror
    with dissolve
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
    $ Pause()
    'As I gently pushed the door, I found myself standing in front of Arlena, inspecting her naked body in the mirror, a shiny toy wedged into her ass.'
    'She seemed to be lost in pleasure, letting out deep, heavy moans.'
    'Taking a moment to let the scene in, I bit my lip.'
    'It seemed as if it just produced a sound of a thousand hammers hitting an anvil!'
    '...For right the next moment Arlena was {b}glaring at me.{/b}'
    "Her cheeks red with either arousal or anger."
    $ StopSexFx()
    scene bg_arlena_bedroom
    show mc at cleft
    show arlena angry at cright_f
    with flash
    ARLENA @angry 'PERVERT!!!'
    show arlena angry at shake
    ARLENA @angry 'Haven’t you heard of knocking first?'
    MC @talk 'I just heard a suspicious noise! The door to the smithy was open! I-I didn’t think!'
    show arlena
    'Arlena folded her arms across her chest and pouted as she stared at the floor, furious.'
    MC @talk '... Were you trying them out for—'
    ARLENA 'I wanted to see if they looked good enough obviously, idiot!'
    MC @talk 'Right, right... Of course.'
    ARLENA '... W-Well?'
    MC @talk '... Well, what?'
    ARLENA 'Well, how did it look, idiot?'
    MC @talk 'OH!'
    MC @talk 'It looked...'
    menu:
        'I’d jump you right now if I could.':
            ARLENA 'U-Uhh...'
            'Arlena seemed to contemplate the idea for a moment before shaking it off.'
            ARLENA 'In your dreams!'
        'People will love them.':
            ARLENA 'Well... that’s good...'
            ARLENA 'Glad you enjoyed the view, pervert!'
        'Hmm, I’d need another look again to be sure!':
            'Arlena thought about the idea for moment, saying nothing as her cheeks turned a soft shade of pink.'
            $ CharSetClothes("arlena", "naked")
            'Dropping the quilt down, she turned around to give me a full view as she shyly looked over her shoulder to gauge my reaction.'
            ARLENA '... W-Well?'
            ARLENA 'What do you think? Does it look good?'
            $ CharSetClothes("arlena", "apron")
            'As I stared at her magnificent behind, utterly entranced, Arlena didn’t wait for my answer before she covered herself once again with the blanket.'
            ARLENA 'I’ll take that as a yes.'

    $ UnlockGalSceneAndGrantXp("arlena","mirror")
    MC @talk 'What do you need from me now?'
    ARLENA 'Nothing, I’ll be dropping the stuff over to the Pleasure District later.'
    ARLENA 'Come back in a day and I’ll give you your cut.'
    $ CharSetClothes("arlena", "normal")
    $ AutoAmb(True)
    return
