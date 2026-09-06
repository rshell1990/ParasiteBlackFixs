label dros_warn:
    # Speaking to Dros
    # "There is a ritual, but we must talk.":
    DROS @shock 'There is? By the gods! You mean...'
    DROS @smile "They'll be able to help me?"
    MC @sad "Yes and no, Dros."
    MC @talk "That's what I'm here to talk to you about."
    MC @talk 'There is a ritual that can make you {i}appear{/i} more like a woman.'
    MC @sad "But it doesn't come without risk."
    MC @talk "The ritual is one understood in theory only, there's a chance you could get hurt." 
    DROS @shock 'How hurt?'
    MC @talk "We don't know."
    DROS @sad 'I... see.'
    MC @talk "Are you sure you want to do it?"
    'Dros seemed to ponder my words for a moment, his answer was one much softer than his usual hard abrasiveness.'
    DROS @sad "I've had lifetimes to think about it."
    DROS @sad "Elven lifespan is an impressive, terrible thing sometimes."
    DROS @sad 'It gives us what you would consider lifetimes to ponder our mistakes... Our worries... Our longing for what should have been.'
    DROS @sad "Our secrets and fears pile up, they eat away at us Elves till if we're not careful, only regret remains."
    DROS @sad "In truth, I was married twice before, and whether it was my treatment of them, or my 'inclinations,' neither could stand the sight of me in the end."
    DROS @sad "I swore to myself that I didnt need anyone else, that I was stronger on my own..."
    DROS @sad "But being alone for so long is no good for anyone."
    DROS @sad "I've become... {i}Hard...{/i} and cold to those around me over the years." 
    MC @talk "But changing your body so?"
    MC @talk "Such a change should not be made just because of loneliness."
    'Dros smiled.'
    DROS @sad '[player_name!t]... Why do you think I became a tailor?'
    DROS @sad 'If I could find someone to care for me for as I am now, I think I would be happy enough...'
    DROS @sad 'But I have always found myself drawn to women rarely because I wanted to sleep with them.'
    DROS @sad 'More-so, because I always {i}wanted to be them.{/i}'
    DROS @sad "So, yes... I'm willing to take the risk."
    MC @talk "...I got you."
    MC @talk "I will return when there is news."
    DROS @smile "Perfect!"
    $ GoalComplete(QstGracefulRebirth, 3)
    if IsGoalComplete(QstGracefulRebirth, 1) and IsGoalComplete(QstGracefulRebirth, 2):
        $ GoalShow(QstGracefulRebirth, 4)
    $ QstGracefulRebirth().warnedDros = True
    "Dros' answer actually surprised me."
    "For someone so hot-headed, with such a inflated ego, he seemed surprisingly humble and even brave when it came to this."
    return