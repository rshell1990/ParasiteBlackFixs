label scr_SharedInThorns_valaClue:
    VALA 'Hmm, the Thornfalls?'
    VALA 'Well, I think I might have something-'
    VALA @surp 'Oh! And who is this?'
    MC @talk 'Uh, this is Elena, my new...{i}pet.{/i}'
    ELENA "{i}*Growls*{/i}"
    VALA @smile "Oh my! Isn't she gorgeous! I've never seen a wolf that colour before!"
    ELENA '...Bark!'
    MC @talk 'Uhh, about that book I was looking for.'
    VALA 'Hm? Oh yes... Let me just check.'
    'Vala hurried over towards some book shelves, bring with her the ladder which she climbed up high on.'
    "With her fingers tracing along the many old books, she finally stopped on one and pulled it out of it's slot."
    VALA 'Found it!'
    'Vala descended down the ladder and hurried back over towards me with the book in hand.'
    VALA 'Here you go, there should be some mention of the Thornfalls in here.'
    MC @talk 'Thanks Vala.'
    VALA 'Of course!'
    VALA "Might I so ask as to why you're reading up on old houses though?"
    MC @talk 'Just uh, researching something.'
    VALA "Hm, well don't let me keep you from whatever you're looking for!"
    'Elena turned to look up to me.'
    MC @talk '...Stop glaring, we need to keep up your disguise.'
    ELENA @talk '...'
    MC @talk "Don't just glare at me like that!"
    MC @talk 'Is this because of the pet comment?'
    ELENA "{i}Bark!{/i}"
    MC @talk 'Urghh! Do you want me to read this thing or not?'
    ELENA "..."
    MC @talk "That's what I thought..."
    MC "(Alright, let's read this thing.)"
    $ PlayerAddItem("book_thornfall")
    $ renpy.show_screen("book", STR_BOOK.ALDERIANHOUSES)
    $ Pause()
    MC '(All of his wives passed away during their pregnancies until he returned with the lady Grace...)'
    MC '(...To which no one ever saw the mother.)'
    BLACK '(You do not believe the child is his?)'
    MC "(I don't know, but something foul is afoot... This kind of misfortune cannot be natural.)"
    BLACK '(A curse?)'
    MC "(I believe so, but the full nature of it alludes me.)"
    $ PlayerRemItem("book_thornfall")
    MC @talk "Elena, do you know anything about this?"
    'Elena barked and shook her head.'
    MC @talk "Hm... Looks like we're going to need to keep digging."
    MC @talk "And we're still no closer to finding the Lady Grace."
    $ QstSharedInThorns().cluesCollected.append('book')
    $ GoalComplete(QstSharedInThorns, 2)
    $ GoalShow(QstSharedInThorns, 4)
    return
