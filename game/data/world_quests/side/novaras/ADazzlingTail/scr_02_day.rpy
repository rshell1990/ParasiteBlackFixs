label qst_ADazzlingTail_02_day:
    show mc at left
    show drax at cright_f
    with dissolve
    MC @talk 'Drax? Where’s Arlena?'
    DRAX 'She said you’d be lookin’ for ‘er.'
    DRAX 'She’s upstairs in her room working on something fancy like.'
    MC @talk 'Alright.'
    hide drax with dissolve
    $ AutoAmb(False)
    stop ambience fadeout 1.0
    'As I wandered up towards her room, Drax shot a sly look in my direction before looking away.'
    MC @talk 'Arlena, are you—'
    $ CharSetClothes("arlena", "apron")
    scene arlena_mirror
    with dissolve
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
    $ Pause()
    'As I pushed open the door, I was shocked to find myself stood in front of a naked Arlena inspecting herself in the mirror, a shiny toy wedged into her ass.'
    'She seemed to be lost in pleasure, letting out deep, heavy moans.'
    "I couldn't tear my eyes of her, until she glanced back at me..."
    scene bg_arlena_bedroom
    show mc at cleft
    show arlena at cright_f
    with flash
    $ StopSexFx()
    $ UnlockGalSceneAndGrantXp("arlena", "mirror")
    'Quickly grabbing the quilt from her bed to cover herself with, Arlena glared, cheeks red with arousal.'
    show mc at shake
    MC @talk 'GAH! '
    show arlena at shake
    ARLENA @angry 'PERVERT!!!'
    ARLENA @angry 'Haven’t you heard of knocking first?'
    MC @talk 'Your father said you were up here! I-I didn’t think!'
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


    MC @talk 'What do you need from me now?'
    ARLENA 'Nothing, I’ll be dropping the stuff over to the Pleasure District later.'
    ARLENA 'Come back tomorrow and I’ll give you your cut.'
    hide arlena with dissolve
    $ CharSetClothes("arlena", "normal")
    $ AutoAmb(True)
    return
