label rom_Ves_2_FortAndCook_Rev:
    VES @talk "Yes, sure!"
    VES @talk 'I plan to set up some perimeter defences, just some bells and such on a wire that will jingle in case anyone tries to sneak in here.'
    menu:
        "{image=[ICON.CLOCK]} Let's do this.":
            $ NoteLock("VesHelpCamp")
            jump rom_Ves_2_FortAndCook
        "Perhaps another time.":
            VES @talk '... Oh, well, let me know when you’re able to, I suppose...'
            $ NoteUnlock("VesHelpCamp")
            $ LocEnter()

label rom_Ves_2_FortAndCook:
    VES @talk 'Great, let me get the stuff ready...'
    #EN. #SCENE FADES TO BLACK.'
    scene black with dissolve
    $ LocSet("ves_camp")
    $ TimeAdvBy(TIME_05H)
    'Over the next hour or so, Ves and I began to set up some primitive defences around her camp.'
    $ TimeAdvBy(TIME_05H)
    'A few spikes in the ground here and there alongside a wire running the camp’s perimeter...'
    $ TimeAdvBy(TIME_05H)
    'If someone knocked it with their foot, it would jingle the attached glass bottles and miscellaneous goods loudly enough to alert Ves of their presence.'
    $ TimeAdvBy(TIME_05H)
    'And God help them when it did.'
    'Wiping the sweat from my brow as I hammered in one of the posts and secured it in place, I noticed Ves sneakily watched me the whole time, still cautiously half alert to my presence as a human, and half with a great deal of curiosity.'
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    VES @talk 'You are strong.'
    'She watched me force one of the wooden posts into the ground.'
    MC @talk 'Yeah, when this {i}thing{/i} inside of me attached itself, it changed my body as well.'
    VES @talk '... I see.'
    scene black with dissolve
    $ TimeAdvTo(TIME_DAY_END)
    'Ves continued to observe as I worked until the sun began to set. If I caught her staring, she quickly made sure to look away and carry on working elsewhere, usually coiling the wires around the posts.'
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    MC @talk 'Alright... That’s about everything, I think.'
    VES @talk 'Yes, this is good.'
    VES '...'
    $ CharChangeRel("ves", 1)
    VES @talk 'Are you free for a few more hours?'
    MC @talk 'What for?'
    VES @talk 'Would you care to join me for food?'
    MC @talk 'Food?'
    VES @talk 'Yes... You must be hungry by now.'
    VES @talk '{i}And...{/i}'
    VES @talk 'It would be nice to have some company for a change.'
    MC @talk '... Sure, Ves, I’ll stay for some food.'
    MC @talk 'I’m pretty hungry myself anyway.'
    "Ves perked up with an actual smile."
    VES @talk 'Good!'
    VES @talk 'I’ll get started on preparing the meat!'
    hide ves with dissolve
    'With that Ves hurried off to begin cooking. As she bent forward to grab some pots and pans, I stared at her cute ass as it shifted through the gossamer material gathered around it.'
    BLACK '... This one I like.'
    BLACK 'She smells... {i}very appealing{/i}.'
    "From the corner of her eye, Ves looked back frequently over her shoulder at me, and from her expression, she must have realised that I kept glancing towards her as well because she'd shyly pull away."
    'I did my best to look away, coughing awkwardly to break the strange tension.'
    MC '...'
    BLACK '... Her heart rate has just increased exponentially, is she in heat and ready to procreate?'
    MC @angry 'Would you shut up?!'
    show ves surprised at cright_f
    with easeinright
    'Ves spun to look back at me, visible confusion on her face.'
    MC @surprised 'It’s... It’s the thing.'
    MC @talk 'It can speak to me in my head.'
    'Ves, now a little concerned, simply mouthed an ‘Oh’ as she quickly decided not to ponder too much on it and instead carried on grabbing what she needed.'
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    'We sat around the warm blazing fire outside of her tent, chewing on the tender meat from our hunt skewered onto sticks which we cooked over the flames.'
    'It was quiet tonight, and the fire provided the only light around for what must have been miles.'
    #SCENE 5 VES’ CAMP EVENING EN. SCENE FADES TO BLACK. WHEN IT RESUMES, VES AND THE MC ARE SAT ROUND A FIRE OUTSIDE OF HER TENT WITH COOKED FOOD SKEWERED ON STICKS FOR THEM TO EAT.
    # idea of separate cg_for this were scrapped. So just text indication
    $ LocFlush()
    show mc at cleft
    show ves at cright_f
    with dissolve
    'Ves waited and watched eagerly as I sat there with the meat on a stick, looking queasily at it as she observed me, waiting with bated breath as I took a tentative bite from it.'
    MC @talk'... It’s good.'
    "Ves' eyes seemed to glitter in the embers of the fire as she smiled triumphantly, her fists raised into the night air."
    VES @talk'YES!'
    VES @talk'My tribe said I’d never be a good cook!'
    VES @talk'Ha! They would eat dirt if they were here!'
    MC @talk'How big is your tribe?'
    VES @talk'Hm? Oh well, I think there’s about a hundred altogether...'
    MC @talk'A hundred?!'
    show ves smile
    'Ves laughed.'
    VES @talk'It’s a small tribe. The tribes all fall under the rule of the Great Chieftain should he command us, but all tribes are led by their Elders.'
    'Ves took a bite of her food and smiled.'
    VES @talk'Mmm, just needs some more salt...'
    VES @talk'In Skarshire, there are so many different spices and flavours for food.'
    MC @talk'I’ve never been.'
    VES @talk'Skarshire is beautiful, many small islands are interconnected. Our own little archipelago.'
    VES @talk'The water is so blue...'
    VES @talk'Perhaps one day I will show—'
    show ves
    'Ves paused, the smile dropping from her face. '
    VES @talk'Never mind.'
    MC @talk'... What? What is it?'
    VES @talk'It’s not going to happen — humans and orcs do not mix.'
    MC @talk'... We seem to get on pretty well.'
    VES @sad'...'
    MC @talk'Aren’t we proof it doesn’t have to just be fighting?'
    VES @talk'It’s not merely about just getting on! There is... too much pain... too much hate for that to happen.'
    MC @talk'Not all humans are the same, Ves.'
    VES @talk'I know that!'
    VES @talk'But a human wouldn’t understand.'
    MC @talk'Then try, try to make me understand!'
    show ves sad
    VES @sad_talk'... Our people have been slaves for generations.'
    VES @sad_talk'Rape... Violence... Torture...'
    VES @sad_talk'These things are everyday occurrences for the orcs still bound by their master’s whips. '
    VES @sad_talk'Made to feel an ugly people... Made to feel {i}dirty.{/i}'
    VES @sad_talk'Nothing but shame has been brought and inflicted upon us.'
    MC @talk'But that was the Greater Trading Company! What does that have to do with the rest of us?'
    show ves angry at shake
    VES @angry_talk'No!'
    show mc sad
    'Ves rose to her feet furiously, anger simmering beneath her voice.'
    VES @angry_talk'You are all the same!'
    VES @angry_talk'Alderay, YOUR PEOPLE, have been sending our enemies weapons, have been sending them supplies!'
    VES @angry_talk'Why? For gold!'
    VES @angry_talk'{i}For greed...{/i}'
    MC @sad'That’s not true! Yes, Alderay sold to the Greater Trading Company at first...'
    MC @sad'But Alderay officially cut ties with them after the {i}‘Battle of the Bay of Valar’{/i}, everyone knows that!'
    MC @sad'It was part of the peace deal Newheart secured! The one your people continue to violate by attacking innocent civilians!'
    'Ves gritted her teeth, swelling with rage. '
    VES @angry_talk'You idiot!'
    VES @angry_talk'Then why do we see unmarked ships docking into Borusmark with supplies, hmm?'
    VES @angry_talk'And why do you think the Greater Trading Company continue to send gold to your lands if they have no business with you? '
    MC @surprised'You can’t just assume that was us! Unmarked could be anyone!'
    MC @surprised'By the gods it could be pirates smuggling for all you know!'
    MC @surprised'Slavery has been abolished for years!'
    VES @angry_talk'Do you even hear yourself speak?'
    VES @angry_talk'The treaty was a lie!'
    VES @angry_talk'What did you expect us to do when you continue to aid our enemies?'
    VES @angry_talk'Sit back and let us be treated like animals? '
    MC @angry'So, killing civilians is the answer? '
    MC @angry'Innocent men and women who’ve played NO part in any of this! '
    VES @angry_talk'Grgh! There we go!'
    VES angry_talk'Always thinking like a human! Always finding a way to justify the horrors you inflict on others!'
    MC @angry'I’m not trying to justify it, Ves!'
    MC @angry'But you can’t justify committing one crime as a response to another!'
    VES @angry_talk'You have no idea what we’ve endured... You know nothing!'
    MC @sad'I’m trying to help!'
    VES @angry_talk'I didn’t want your help!'
    hide ves with flash
    'Ves kicked up some sand into the fire as she stormed off back into the sanctuary of her tent, shouting loudly behind at me. '
    VES @talk'Now leave me alone, human!'
    MC '(... Well that could have gone better.)'
    $ NoteUnlock("VesRomance1")
    $ RomanceVes().cooldownDay = GetGameDay() + 1
    $ QstSetProgress(RomanceVes, 5)
    $ LocEnter()
