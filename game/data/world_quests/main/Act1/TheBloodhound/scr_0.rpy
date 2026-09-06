label qst_bloodhound_0_pitch:
    NYX @talk "Well, looks like you can handle yourself at least."
    NYX @talk "I have another job for you, if you're still interested in a bit more coin that is."
    MC @talk 'Tell me about the job first.'
    NYX @talk "An informant of ours named Azul has gone missing and I can't spare the men to check on him."
    $ QstStart(QstTheBloodhound)
    NYX @talk "The last time he made contact he was... {i}erratic.{/i}"
    NYX @talk "I think he was on to something heavy, but now, no one can find him."
    MC @talk 'Is he dead?'
    NYX @shock "I hope not, he's one of our best."
    NYX @talk "You can't miss him, he carries around that fucking bird on his shoulder wherever he goes..."
    NYX @angry "Damn thing shit all over my desk once."
    NYX @talk 'So... What do you say?'
    menu:
        'Depends on the amount of coin...' (Req_Charm = 7):
            NYX @talk "Look, I have a limited fund I can spare on you, unlike {i}some{/i} divisions."
            NYX @talk "I don't have some infinite pool of coin and resources to pull from."
            NYX @talk "That said, you'll be paid well enough."
            NYX @talk 'How does five hundred coins sound?'
            menu:
                "Seems a little light for my pockets...":
                    NYX @talk '...Fine, six hundred coins and not coin more.'
                    $ PlayerAddItem("gold", 600)

                'How about some supplies from the armory?':
                    NYX @talk "I can't give you anything from the armory but, here, take these from my personal stash."
                    $ PlayerAddItem("gold", 500)
                    $ PlayerAddItem("potion_heal_regular", 4)

        "I'll do it.":
            NYX @laugh 'Excellent.'
            NYX @talk "There you go."
            $ PlayerAddItem("gold", 500)

        'I need some time to think on it.':
            NYX @angry "Don't waste my time, return when you've made up your mind."
            $ LocEnter()

    NYX @talk "Last time Azul was seen, he was speaking to some Adventurers at the Guild."
    NYX @talk "Some small time D-listers, call themselves {i}The Guardians of the Realm...{/i}"
    NYX @angry "Pretentious cocksuckers, anyway, I'd start with them."
    $ QstSetProgress(QstTheBloodhound, 1)
    $ LocEnter()

label qst_bloodhound_0_pitch_revisit:
    NYX @talk "Ah, right."
    NYX @talk "To recap..."
    NYX @talk "An informant of ours named Azul has gone missing and I can't spare the men to check on him."
    NYX @talk "The last time he made contact he was... erratic."
    NYX @talk "I think he was on to something heavy, but now, no one can find him."
    NYX @talk "You can't miss him if you see him, carries that fucking bird on his shoulder..."
    NYX @talk 'So... What do you say?'
    menu:
        'Depends on the amount of coin...' (Req_Charm = 7):
            NYX @talk "Look, I have a limited fund I can spare on you, unlike {i}some{/i} divisions."
            NYX @talk "I don't get some infinite pool of coin and resources to pull from."
            NYX @talk "That said, you'll be paid well enough."
            NYX @talk 'How does five hundred coins sound?'
            menu:
                "Seems a little light for my pockets...":
                    NYX @talk '...Fine, six hundred coins and not coin more.'
                    $ PlayerAddItem("gold", 600)

                'How about some supplies from the armory?':
                    NYX @talk "I can't give you anything from the armory but, here, take these from my personal stash."
                    $ PlayerAddItem("gold", 500)
                    $ PlayerAddItem("potion_heal_regular", 4)
        
        "I'll do it.":
            NYX @talk 'Excellent.'
            $ PlayerAddItem("gold", 500)

        'I need some time to think on it.':
            NYX @talk "Don't waste my time, return when you've made up your mind."
            $ LocEnter()

    NYX @talk "Last time Azul was seen, he was speaking to some Adventurers at the Guild."
    NYX @talk "Some small time D-listers, call themselves {i}The Guardians of the Realm...{/i}"
    NYX @talk "Pretentious cocksuckers, anyway, I'd start with them."
    $ QstSetProgress(QstTheBloodhound, 1)
    $ LocEnter()