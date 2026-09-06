label sexscene_ArwenCelesteChoice:
    ARWEN @laugh 'Wonderful!'
    ARWEN @talk 'Now, I mentioned before that I offered some {i}unique{/i} experiences.'
    ARWEN @talk 'Are you more interested in being the Adventurer who wooed the beautiful Celeste into bed... {i}Or the savage whose captured her?{/i}'
    menu:
        'I want to be the adventurer who won her heart.':
            ARWEN @laugh 'Ah, a romantic at heart... How sweet.'
            ARWEN @talk 'Right this way.'
            scene black with dissolve
            "I followed Arwen as she lead me into one of the bordello's private rooms."
            scene bg_weeping_heart_brothel_room
            $ LocNameSetTemp(_("Brothel Room"))
            show arwen at center_f
            with dissolve
            ARWEN @talk 'Hero of Alderay... I... I must confess.'
            ARWEN @sad 'Your bravery has moved me during these last few adventures.'
            ARWEN @sad "{i}I've never met another man like you.{/i}"
            MC "(She's pretty good at this.)"
            ARWEN '...'
            MC "(Shit, she's waiting on an answer, what should I say?)"
            MC @talk '{i}*Cough*{/i} I only did what uh... Needed to be done of course.'
            MC @talk 'It was the right thing to do.'
            ARWEN @laugh "You're always thinking about what's the right thing to do."
            scene black with dissolve
            ARWEN @blush "{i}I think it's time someone thought about what's right for you.{/i}"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            "Taking my hand, {i}'Celeste'{/i} led me over to the bed, where she laid down on her back and waited for me."
            scene arwen_cosp_won_prepen with dissolve
            $ Pause()
            ARWEN "Ahh, be careful my love... I've n-never-"
            ARWEN "Gods, are they a-all as big as you?"
            MC "{i}No Celeste... I'm bigger than most.{/i}"
            ARWEN '...B-Be gentle, {i}take me.{/i}'
            menu:
                'Put it in her pussy':
                    call sexscene_ArwenCelesteWonPuss from _call_sexscene_ArwenCelesteWonPuss
                    jump sexscene_ArwenCelestePostSex
                'Put it in her ass':
                    call sexscene_ArwenCelesteWonAss from _call_sexscene_ArwenCelesteWonAss
                    jump sexscene_ArwenCelestePostSex
        'I want to be the one who captured her.':
            ARWEN @laugh 'Oooh, interesting!'
            ARWEN @talk "Aren't you a dark horse!"
            ARWEN @talk 'Right this way... {i}your prisoner awaits.{/i}'
            scene black with dissolve
            "I followed Arwen as she lead me to one of the bordello's private rooms."
            'For a short while, Arwen had me wait outside of the room while she {i}prepared herself{/i} as she put it delicately.'
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            'Eventually, after a few minutes passed by and I began to become restless, I heard her voice call me inside.'
            $ LocNameSetTemp(_("Brothel Room"))
            scene arwen_cosp_cap_prepen with dissolve
            $ Pause()
            ARWEN 'Whose there?'
            ARWEN 'R-Release me now!'
            ARWEN 'What is it you want fiend? Coin?'
            ARWEN "The Red Arrows will come to save me!"
            "The whole setup was somewhat amusing, but as Arwen flailed on the chains and gave it her all, I couldn't help but find myself turned on by the performance."
            MC 'You think I want coin you little whore?'
            MC 'Oh no, I want something else entirely.'
            ARWEN 'What... What are you going to do to me?'
            MC "What will the Red Arrows do when they've found their precious Celeste broken in?"
            ARWEN "Y-You can't be serious! Please! No!"
            ARWEN "Release me! I'll never fall to you!"
            MC "We'll see about that!"
            menu:
                'Fuck her pussy.':
                    call sexscene_ArwenCelesteCapturedPuss from _call_sexscene_ArwenCelesteCapturedPuss
                    jump sexscene_ArwenCelestePostSex
                'Fuck her ass.':
                    call sexscene_ArwenCelesteCapturedAss from _call_sexscene_ArwenCelesteCapturedAss
                    jump sexscene_ArwenCelestePostSex

label sexscene_ArwenCelestePostSex:
    scene black with dissolve
    "With that, we returned to the bordello's main hall."
    $ LocNameReset()
    $ LocEnter()
