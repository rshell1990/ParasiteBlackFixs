label qst_TwoEmperors_0:
    # after the events of 'The man in Black' 
    # trigger on mc_house_kitchen enter daytime
    # Knock at the door sfx 
    show regina at cleft
    with dissolve
    show mc at center_f with easeinright
    play sound "audio/cfx/door_knock.ogg"
    REGINA @talk '... Are you expecting company dear?'
    MC @talk 'Company? No, I-'
    LUKKAN 'Open up! By order of Emperor Alcott!'
    show mc at center_f, blurin
    MC '(Shit... What now?)'
    show lukkan at right_f with easeinright
    'Regina did her best to force a smile as Officer Lukkan stepped inside with four guards.'
    REGINA @talk 'Is there something we can help you with, Officer?'
    'Lukkan did not even acknowledge [regina_ref!t], instead, he focused only on me.'
    LUKKAN @talk "It's your lucky day."
    LUKKAN @talk "You and your friend have been given a new assignment coming straight from Emperor Alcott himself."
    MC @surprised 'The... The Emperor?'
    "Regina kept glancing back from me to Lukkan, and despite the pained smile on her face, I could tell she was wondering what in the seven hells I had done to cause this."
    REGINA @talk 'Haha, there must be some mistake, Officer.'
    REGINA talk '[player_name!t] no longer works within the Scouts Corps, so-'
    LUKKAN @talk 'There is no mistake.'
    LUKKAN @talk '...Tell the woman to leave.'
    LUKKAN @talk 'This next part is for your ears only.'
    '[regina_ref_cap!t] gritted her teeth in anger.'
    REGINA @angry "Who do you think you're talking-"
    MC @serious "[regina_ref_cap!t], it's okay."
    REGINA @sad 'But-'
    MC @talk '[regina_ref_cap!t]... You should go.'
    'On the tip of her tongue, [regina_ref!t] held back from saying something else.'
    'She glanced over at the guards and Lukkan, there was something deadly serious about them, and we could both sense it.'
    'After a brief sigh, she recomposed herself.'
    REGINA @talk 'I will be back shortly.'
    hide regina with easeoutright
    'The guards allowed [regina_ref!t] to pass, and waited till the door was closed behind her.'
    show mc at cleft
    show lukkan at cright_f
    with dissolve
    MC @talk 'Now what is this about?'
    LUKKAN @talk "To the South of here, we've noticed considerable Demorai movement over the last few days."
    LUKKAN @talk "They've also been acting... {i}strangely,{/i} recently."
    MC @think '{i}Strangely?{/i}'
    LUKKAN @talk "Keeping their distance... Watching troops move but not attacking."
    MC @talk "Maybe they're just scouting?"
    LUKKAN @talk "Maybe, but it's not like them to avoid ambushes or a fight, and they to be more focused on getting somewhere."
    LUKKAN @talk "We want you to find out what's going on out there."
    $ choicemenu = ["a","b"]
    menu qst_TwoEmperors_0_menu1:
        'Why is the emperor asking for us?' if "a" in choicemenu:
            $ choicemenu.remove("a")
            LUKKAN @talk "What? Did you seriously think we'd just let you fuck around in the Adventurers Guild forever?"
            LUKKAN @talk "No no no no... That's not how this works."
            LUKKAN @talk "We decide how you live and how you die."
            LUKKAN @talk "If you prove yourself useful, maybe we decide today's not the day you die."
            menu:
                "That doesn't answer my question.":
                    LUKKAN @talk "Urghh... Why does every prick who joins the Adventurers Guild think there's some 'special' reason they get picked?"
                    LUKKAN @talk "Maybe the Emperor wants to see what you and your friend can do."
                    LUKKAN @talk "Maybe he just picked your name up at random from a list."
                    LUKKAN @talk "Maybe some high lord just really wants to fuck that woman of yours and wants you out of the way."
                    LUKKAN @talk "What does it matter in the end?"
                    LUKKAN @talk "Doesn't change a goddamn thing."
                    jump qst_TwoEmperors_0_menu1
                "...Fine.":
                    LUKKAN @talk "Anymore inane questions?"
                    jump qst_TwoEmperors_0_menu1
        "Fine, I will do as you ask.":
            pass
        'What if I refuse?' if "b" in choicemenu:
            $ choicemenu.remove("b")
            LUKKAN @talk "That would be a {i}very{/i} fucking stupid decision."
            LUKKAN @talk "Simply put, not only would {i}you{/i} be punished, but the people you care most for would be punished as well."
            MC @talk "Was that a threat?"
            LUKKAN @talk "Take it however you want."
            MC "(Looks like {i}no{/i} isn't going to be an answer here.)" #Loops back to main menu
            jump qst_TwoEmperors_0_menu1
    LUKKAN @talk "Excellent!"
    LUKKAN @talk "See? You're learning fast already!"
    MC @angry 'Am I at least getting paid for this?'
    LUKKAN @talk "The Emperor always pays graciously for services rendered."
    LUKKAN @talk "Five hundred coins."
    $ choicemenu = ["a"]
    menu qst_TwoEmperors_0_menu2:
        "Five hundred coins for what could be another suicide run?" (Req_Charm = 7) if "a" in choicemenu:
            $ choicemenu.remove("a")
            LUKKAN @talk "Confident little fucker, aren't you?"
            LUKKAN @talk "Fine... Seven hundred coins and not one more."
            $ QstTwoEmperors().goldReward = 700

            menu:
                "If you're going to send me on another suicide mission, I could do with some supplies." (Req_Charm = 8):
                    LUKKAN @talk "{i}*Sigh*{/i} Fine, there you go."
                    $ PlayerAddItem("potion_heal_minor", 2)
                    $ PlayerAddItem("potion_heal_regular", 2)
                    LUKKAN @talk "Now, let's move on..." 
                "...Perfect.":
                    pass
            jump qst_TwoEmperors_0_menu2

        'Will I be left alone after this?':
            LUKKAN @talk "That depends."
            MC @angry 'On?'
            LUKKAN @talk "If you survive and if we decide we need you again."
            MC @angry '...Great.'
            LUKKAN @talk "Lighten up kid, you're hardly the first person to get fucked by higher ups."
            LUKKAN @talk "Now, moving on..."
            pass
    LUKKAN @talk "I'll mark on your map for you where we last saw some of the Demorai moving."
    LUKKAN @talk "Your friend should be waiting for you outside the gate."
    LUKKAN @talk "Meet him there and report back to me when you've found something."
    'I gritted my teeth and swallowed my pride as I answered him.'
    MC @angry '...Yes sir.'
    LUKKAN @talk "Don't fail us."
    hide lukkan with dissolve
    'Lukkan said nothing else, turning and leaving with his men the way he came.'
    'I sighed with relief once he left, feeling that heel pressed against my throat lift ever so slightly.'
    MC '(Fuck... Are they just going to keep sending me and Markus on missions till we eventually die?)'
    MC "(This can't go on forever, one of these missions...)"
    'The thought of the Man in Black crossed my mind once again, what if he or someone like him was waiting for me?'
    'I pushed the thought aside and swallowed hard.'
    "It doesn't matter now."
    "I need to focus on the mission ahead and meet with Markus."
    '...Not like there was any other choice in the matter.'
    $ QstStart(QstTwoEmperors)
    $ LocEnter()