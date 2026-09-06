init python:
    @AppendToAllQuests
    class EventBlackDiamondPostMassacre(LogicModule):
        def __init__(self):
            super().__init__()

            self.openDay = -1
    
        def onStart(self):
            self.openDay = GetGameDay() + 1

        def onMidnight(self):
            if GetGameDay() >= self.openDay:
                QstSetProgress(self, 666) # < wtf is this? -tmm -dont know -tmm
                QstComplete(self)

label black_diamond_post_massacre_lock_line:
    MC '(I better stay away from there for now... Not with all those guards and inquisitors walking about.)'
    $ LocEnterQ()

label black_diamond_post_massacre:
    $ QstSetProgress(EventBlackDiamondPostMassacre, 1)
    #Scene 4 - If player chose Assault route with with Tarek, for a short while, (about a week), player cannot return to Black Diamond - unique one time scene trigger
    show erika at left
    show cg_guard at right_f
    with dissolve
    ERIKA @talk 'Bring in more Guards to patrol the grounds and keep the crowds at bay while we deal with the investigation inside.'
    ERIKA @talk 'Last thing we need is the public seeing the bloodbath in there.'
    GUARD "Yes ma'am."
    hide cg_guard with dissolve
    MC @smile '...Erika?'
    show erika with ease:
        xcenter 0.6
        xzoom -1.0
    show mc with easeinleft:
        xcenter 0.15
    ERIKA @surp '[player_name!t]?'
    ERIKA @surp 'Is that you?'
    ERIKA @sad 'I... I had heard what had happened, I thought-'
    'For a moment Erika seemed like she might leap into my arms and hug me, but as she looked around at the many glaring eyes of inquisitors watching her, she stopped herself.'
    ERIKA @surp 'You look so... {i}different.{/i}'
    MC @talk 'A lot has changed...'
    MC @talk 'What happened here?'
    MC "(Hopefully she nor the other inquisitors suspect anything about what me and Markus did.)"
    ERIKA @talk "I can't really talk about it, but in a few days I will try come home."
    ERIKA @smile 'Then you and I no doubt have much to discuss.'
    MC @smile 'That sounds good, Erika.'
    MC @talk "...I've missed you a lot."
    ERIKA @sad 'I-'
    "Erika's name was called by what seemed to be an older, senior inquisitor."
    ERIKA @talk 'I have to go.'
    ERIKA @talk 'We shall speak once I am done with my work.'
    'I nodded as Erika left to join the others.'
    hide erika with easeoutright
    BLACK '{i}(Danger).{/i}' 
    MC "(Erika isn't a threat, she wouldn't betray us if she found out.)"
    BLACK '{i}(You cannot be sure where her allegiance lies more).{/i}'
    MC "(...She will not find out anyway, it will be better this way for everyone.)"
    BLACK '{i}(Then you more doubts about her than you admit).{/i}'
    MC '(...)'
    $ LocEnter()