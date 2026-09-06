label qst_bloodhound_1_guild_onEnter:
    show mc with easeinleft:
        xcenter 0.15
    MC "(Someone here must know something about the 'Guardians of the realm,' maybe I should ask Thea?)"
    $ LocEnter()

label qst_bloodhound_1_TheaOnGuardians:
    #Player selects on Thea 
    THEA @talk 'Hm? Well, not too much.'
    THEA @talk "They're newcomers but they seem quite popular."
    THEA @scared 'Maybe a little too cocky though.'
    MC @talk 'Not a fan?'
    THEA @talk "Mm, every rookie team thinks they're the chosen ones or something."
    THEA @smile2 'I prefer the ones who actually manage to stick around.'
    MC @talk 'Where are they now?'
    THEA @talk 'They took on a quest to take on a giant slimelark.'
    MC @surprised 'A what?'
    THEA @talk 'Uhh, think a very angry sentient pool of gunk that will force its way into you and consume you inside out.'
    MC @talk 'Can they handle it?'
    THEA @sad "I don't know... A slimelark isn't something to shrug off if you're a rookie."
    THEA @sad "Especially the one that's been causing so much trouble."
    THEA @sad "I told them not to take it but, when you've got something to prove..."
    THEA @talk "Anyway, the thing has been sighted near lake Balun, you know, a short hike to the West?"
    THEA @scared "Apparently its been pulling people in when they get too close to the water."
    MC @talk 'Thanks for the information.'
    THEA @sad "If you're thinking of going after them, I'd suggest being prepared..."
    THEA @talk "Slimelarks are difficult beasts."
    MC @talk "I'll take your word for it."
    $ WorldMapLocAdd("lake_balun")
    $ QstSetProgress(QstTheBloodhound, 2)
    $ LocEnter()
