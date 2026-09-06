label rom_ArlenaRepBj:
    show mc at cleft
    show drax at cright_f
    show arlena at right_f
    with dissolve
    ARLENA '[player_name!t]! There you are...'
    'Arlena’s voice had an almost lyrical quality to it these days, as she spoke she moved to entwine her arms with mine.'
    ARLENA 'I’ve got this project thing upstairs I need you to look at... Mind helping me with it a moment?'
    menu:
        'Sorry Arlena, too busy.':
            ARLENA 'Oh... Right.'
            ARLENA 'Perhaps another time then...'
            'Arlena clearly looked dissapointed for a moment there.'
            return
        'Let’s go!':
            $ RomanceArlena().bjRoomCheck = True
            $ LocSet("arlena_room")
            $ LocEnter()

label rom_ArlenaRepBj_02:
    show mc at cleft
    show arlena at cright_f
    with dissolve
    'Following Arlena up to her room, Drax gave us a sly but uncertain glance as we passed by him before resuming his work.'
    'Arlena slammed the door shut and threw me against it, pressing a kiss onto my lips before she squatted down onto her knees, fumbling with my belt buckle.'
    MC @talk 'Arlena! '
    ARLENA 'Sorry, just thinking about it’s got me all worked up.'
    scene arlena_bj_slow with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ Pause()
    'As Arlena greedily pulled out my member she wasted no time wrapping her lips over the head.'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg",1)
    MC @talk 'Ahh...'
    'With both her hands clinging to my thighs, Arlena began to take more of my cock down into her throat, bobbing her head hungrily as she stared up into my eyes, judging my reaction.'
    ARLENA 'Mmm...'
    ARLENA '{i}*Slurp!*{/i} Mmfgh...'
    'As I tried to stifle a grunt of pleasure, Arlena’s tongue thrashed and beat against my cock as she struggled to take as much of me as possible.'
    'I ran my hand soothingly through her hair, occasionally gripping at it to thrust her head onto my member before letting her up to breathe.'
    'When Arlena next brought her head up for a snatch of air she wrapped her fingers around the base of my cock and pulled back to admire it.'
    ARLENA '[player_name!t], I don’t mean to inflate your ego any more than it already is, but I really have never seen anything as big as this, I can barely take all of you in my mouth.'
    'Then she grinned mischievously at me and licked the head with the tip of her tongue, swirling it around in her mouth before creating a seal with her lips and sucking hard.'
    MC @talk 'S-Shit...'
    'I could feel the parasite within me rearing its head in fervour, its lecherous nature threatening to explode out of me and throw Arlena on the floor and mount her like a dog.'
    'Arlena’s head bobbed on happily.'
    'It wasn’t long before she began to gently fondle at her own breasts, tugging at her nipples until they were stiff, rolling them around under her fingertips, shifting around at my feet as she became more and more aroused.'
    'Soon, I was breathing heavily, unsure of how much longer I could hold on.'
    MC @talk 'Arlena... if you keep doing that...'
    scene arlena_bj_fast with dissolve
    $ Pause()
    'Spurred on by the knowledge that I was close, she immediately began to move her head faster, taking as much of me as she could.'
    'I could feel the head of my cock as it hit the back of her throat, I had to ease off before the animal in me took over, I didn’t want to choke her.'
    MC @talk 'Arlena... {i}*huff!*{/i} ... I’m about to cum! '
    'Arlena didn’t listen, carrying on with mischievous glee.'
    'Powerless to hold back anymore, I tangled my hands through her hair and held her still in anticipation, allowing myself to thrust inside her mouth.'
    'Arlena’s eyes widened as she choked slightly, I felt a stab of guilt, but by now I couldn’t hold back any longer and quickly flooded her mouth with my seed.'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    $ ReduceInfectionFromSex("arlena")
    scene arlena_bj_finish with flash
    $ UnlockGalSceneAndGrantXp("arlena","bj")
    $ Pause()
    'Arlena swallowed as much as she could before pulling back, coughing and spluttering as she wheezed for air.'
    'Some of the hot cum dripped off her chin onto the floor which she quickly wiped away with her sleeve.'
    'Her eyes had begun to water in those final few moments, and with a faint smile she managed to get out the words between coughs.'
    $ AutoMus(True)
    scene bg_arlena_bedroom
    $ CharSetClothes("arlena", "naked")
    show mc at cleft
    show arlena at cright_f
    with dissolve
    MC @talk 'Was that too much for you?'
    ARLENA 'Almost, but I think I can handle you... I’d like to carry on if you would.'
    'I smiled and raised a cocky eyebrow at Arlena, she knew as well as I did that I wouldn’t be going anywhere.'
    'She rose to her feet and quickly did her best to cover up what we’d just done.'
    ARLENA 'Thanks for the ‘help’.'
    MC @talk 'You maybe want to move this over onto the bed?'
    ARLENA 'Another time perhaps, can’t skirt too much work! '
    'As Arlena slid past me, she waved playfully, giving me a few moments to collect myself before heading back downstairs to face the accusatory gaze of her father as he held a hammer the size of my head.'
    $ CharSetClothes("arlena", "normal")
    return
