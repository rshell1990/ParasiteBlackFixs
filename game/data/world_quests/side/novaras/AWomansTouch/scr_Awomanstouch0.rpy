
label scr_WomansTouch_primer:
    #Scene 18 - Scene auto triggers randomly when MC enters his bedroom AFTER READING MATERIAL QUEST
    MC @talk 'Elena, are you here?'
    MC "(Hmm... She must have gone on one of her 'walks' in disguise.)"
    MC "(Perhaps while she's out I could take a closer look at some of the things she's been reading.)"
    #Not sure whether to make this section the player has to click on book or not(?)
    "Picking up one of Elena's history books, a hidden book concealed amongst the pages felt out and landed on the floor."
    MC "(What's this?)"
    'I picked up the book to examine it.'
    '{i}Her Masters call, a lycanite love story - illustrated - By B. Rohmway{/i}'
    'Flipping through some of the pages, they depicted black and white sketch images of a wolf girl in various states of romance, passionate sex and... bondage with a muscular human man.'
    MC '(Elena!)'
    'The door suddenly creaked open as I turned to see Elena stood in the doorway in her wolf form, suddenly transforming human with a terrified expression on her face.'
    show elena with dissolve:
        xcenter 0.45
        xzoom -1.0
    ELENA @shock "T-That isn't what you think!"
    MC @talk 'Well, it looks to me to be VERY different kind of {i}fantasy{/i} book that I was expecting you to read.'
    ELENA @shock "It's v-very rare and banned! I was um, um! Amazed the library even had it!"
    ELENA @shock "S-So I-"
    MC @smile 'Elena, you can enjoy whatever you like.'
    ELENA @sad '...Really though?'
    ELENA @sad "You don't think it's wrong?"
    MC @talk 'Why would I?'
    ELENA @sad "...Because... I'm not human."
    MC @talk '...And?'
    ELENA @sad 'I... I always presumed my attraction to humans was some kind of unnatural perversion.'
    ELENA @sad 'No doubt the result of having been raised amongst humans with no interaction with my own kind...'
    MC @talk 'How do you know?'
    ELENA @talk 'What do you mean?'
    MC @talk "I mean, how do you know others of your kind don't find humans attractive?"
    ELENA @shock 'I-'
    ELENA @talk "...Father used to discourage me from anything like that, he said I had to keep my mind clear to focus on keeping Grace safe and nothing else."
    MC @talk "You're still a woman Elena, you cannot help having desires."
    ELENA @sad "I wouldn't really know..."
    MC @surprised '...Wait, are you a-'
    ELENA @sad "Yes, I'm a virgin."
    'Elena seemed visibly upset by this.'
    MC @talk "Elena, there's nothing to be ashamed of."
    ELENA @sad "Please... I know it shouldn't bother me but it does, the lady Grace was always chased after by suitors."
    ELENA @sad 'Those few who knew of my secret had little time for one such as I.'
    MC @sad 'None saw you as a woman?'
    ELENA @talk "...When I was younger, there were a few 'trusted' children from noble families who owed debts to father who would come and play with me and Grace."
    ELENA @grumpy "One of them, Trohan, always made his dislike of me quite vocal."
    ELENA @angry "{i}'What man would want a woman more hairier than himself?'{/i} He would tell me."
    ELENA @talk "One day though, as we grew older... I was bathing once beneath some falls in the privacy of the woods."
    ELENA @lewd "I saw him watching me in secret while he... {i}occupied himself.{/i}"
    MC @talk "What did you do?"
    ELENA @lewd "...I let him watch."
    MC @talk "Why?"
    ELENA @lewd "It was exciting... To see a man wanting me that way."
    ELENA @lewd "So...{i}I would keep letting him watch.{/i}"
    MC @talk "He never approached you?"
    ELENA @lewd "No, but one time our eyes met and he realized this whole time I was letting him continue."
    ELENA @lewd "After that, he was considerably nicer to me..."
    ELENA @talk "I'd never seen the lady Grace become jealous before."
    MC @talk "She wasn't happy for you?"
    ELENA @grumpy "She wasn't happy when {i}anyone{/i} took the attention away from her."
    MC @talk "...I see."
    ELENA @sad "But I suppose I never really got over my fascination with that first feeling of {i}being desired.{/i}"
    'Looking down at the book, I reached out to hand it back to Elena who took it from me.'
    ELENA @talk "Um...Thank you."
    ELENA @talk 'Could I ask another favor?'
    MC @talk 'What is it?'
    ELENA @lewd "...I want to learn about how to... {i}be desirable.{/i}"
    MC @bitelip "Uhh... Do you mean-"
    ELENA @shock "N-No! Not like that!"
    ELENA @talk "I um, I mean I'd like to speak to someone like a courtesan."
    MC @surprised "A courtesan?"
    ELENA @grumpy "I... want to understand my feelings more."
    ELENA @talk "T-That's all."
    MC @talk "...Well, if I can help I will see what I can do."
    ELENA @talk "Thank you, [player_name!t]."
    MC "(A courtesan willing to speak to Elena... This could prove difficult.)"
    $ QstComplete(PrimerWomansTouch)
    $ QstStart(QstWomansTouch)
    $ LocEnter()
