
label qsttheslavemaster_intro:
    show mc at cright with dissolve
    "As I made my way out through the city gates, I heard a voice calling behind me."
    UNKNOWN "Wait! STOPPPP!"
    show cg_random_boy at cleft_f with easeinleft:
        yoffset 300
    with dissolve
    "Behind me, a young boy, huffing and panting, sprinted up and handed me a sealed letter."
    show mc at cright_f with dissolve
    UNKNOWN "{i}*Huff!*{/i} An urgent letter for you mi'lord from Captain Nyx!"
    MC @talk "Captain Nyx? Did she say what this was about?"
    UNKNOWN "No mi'lord! But she said you must read it at once!"
    MC @talk "How did you know where to-"
    show cg_random_boy at cleft with Dissolve(0.2)
    hide cg_random_boy with easeoutleft
    "The boy was already hurrying off once again before I could even finish my sentence, sprinting back towards the gate, and soon, he was gone entirely from my line of sight."
    "I tore open the letter and read its contents inside."
    "{i} [player_name!t], please come at once to see me ...{/i}"
    "{i}I need to call upon your services once again.{/i}"
    "{i}Captain Nyx{/i}"
    MC "(I should head over there once I have some time, see what she wants.)"
    $ NoteUnlock("qstTheSlavemasterCall")
    $ QstSetProgress(PrimerTheSlavemaster, 1)
    $ LocEnter()


# Player quest first instruction in notes: "Captain Nyx wants to speak to me in her Office."
# Captain Nyx Office - scene begins automatically upon entering.
label qsttheslavemaster_pitch:
    if QstGetProgress(PrimerTheSlavemaster) == 1:
        show nyx at center_f with dissolve
        NYX @talk "Ah, there you are."
        NYX @talk "Just the person I've been looking for."
        MC @think "What's this about?"
        NYX @talk "Not long ago, we received word of a notorious slave master who we {i}think{/i} has arrived in Novaras."
        NYX @angry "They call him 'Angharad of a thousand chains.'" 
        NYX @talk "From what we've gathered, Angharad's been investing a lot of time and resources in the power struggle going on between the gangs in the city right now, and has struck some type of deal with the Khazahs."
        NYX @talk "We believe he's been supplying them with additional weapons, drugs, and armour in return for being the only slave master they consult with."
        MC @think "I see... And where do I fit into all this?"
        NYX @angry "We've managed to convince Angharad to attend what he believes is a business meeting with another high-profile slaver interested in working with him."
        NYX @talk "The plan is simple ... One of our men pretends to be the other slave master, goes in, finds proof it's definately Angharad at the meeting and not one of his men sent on his behalf,"
        NYX @talk "And once Angharad is confirmed to be present and agrees to the deal, the other city guards on standby will swarm the place and seize him."
        MC @talk "I take it this is where I come in?"
        NYX @talk "Well, aren't you clever?"
        NYX @talk "As you know, I'm stretched thin on manpower as it is, but to make matters worse, Angharad's done his research and knows who many of my men are."
        NYX @talk "I need a fresh face to go in and pretend to be the other slave master to negotiate with him."
        NYX @talk "Are we clear?"
        $ choicemenu = {'a','b'}
        menu qsttheslavemaster_pitch_menu:
            "I know nothing about being a slave master, how will I even convince him?" if 'a' in choicemenu:
                NYX @talk "I'll walk you through everything as best as I can, just push the thought of 'people' to the back of your mind and remember it's {i}product{/i} you're discussing."
                NYX @talk "Assisting you will be one of my very best pretending to be a slave concubine of yours."

                $ choicemenu.remove('a')
                jump qsttheslavemaster_pitch_menu

            "Why can't you just arrest him upon arrival?" if 'b' in choicemenu:
                NYX @angry "We need to confirm it's really him."
                NYX @talk "In the past, he's sent others impersonating him to handle negotiations."
                NYX @angry "We can't let him slip away, no matter what."
                MC @talk "And how will I be able to {i}'prove'{/i} it's really him?"
                NYX @sad "That's the tricky part ... But we'll have to find it." # SAD
                NYX @talk "If we arrest one his men acting on his behalf, Angharad will only hide himself further underground."
                menu:
                    'I see.':
                        NYX @talk "Any other questions?"
                        #Loops back to main menu
                    "Are there not dozens of slave masters doing the same? Why is he so important?":
                        NYX @angry "Angharad is no ordinary slave master, he's destabilised whole regions before."
                        NYX @talk "If we capture him alive, we can use his connections to weed out dozens if not hundreds of criminals in the city."
                        NYX @angry "But, if he entrenches himself here before we can do that, we'll never be able to uproot him."

                $ choicemenu.remove('b')
                jump qsttheslavemaster_pitch_menu

            "I think I've got the idea.": #Continues quest 
                NYX @talk "So then, can I count on you with this?"
                menu:
                    "What's in it for me first?":
                        NYX @laugh "My undying gratitude?"
                        MC @talk "Nice try."
                        NYX @angry "Fine, what do you want?"
                        menu:
                            "Coin of course.":
                                NYX @talk "Fine, how does six hundred sound?"
                                menu:
                                    "Make it seven-fifty and we're talking." (Req_Charm = 7):
                                        NYX @talk "Fine ... Seven-fifty and not a coin more." #success variant
                                        $ QstTheSlavemaster().reward = "money_success"
                                    "Okay.":
                                        pass

                            "I could do with some more useful equipment.":
                                NYX @shock "Equipment?"
                                NYX @talk "Well ... I could give you some health potions, and, while I can't give you any armour and weapons,"
                                NYX @talk "I can give you this amulet that offers some protection." # against poison." #amulet item - poison resistance 10%
                                menu:
                                    "That'll do.":
                                        NYX @laugh "Excellent."
                                        $ QstTheSlavemaster().reward = "amulet"

                            "I'll take your panties.":
                                NYX @disg "You ... you what?!"
                                NYX @angry "Be serious!"
                                menu:
                                    "(I probably shouldn't push my luck on this one.)":
                                        NYX @angry "Ask me that again and I'll cut your balls off!"

                                    "Do I sound like I'm {i}not{/i} serious?" (Req_Charm = 6):
                                        NYX @arrogant "It ... It doesn't even make any sense asking for my panties!" #success 
                                        NYX @arrogant "What benefit are they to you?"
                                        show nyx arrogant
                                        MC @lewd "Doesn't it make even less sense to deny me?"
                                        show nyx disg
                                        NYX @disg "W-What are you talking about?"
                                        MC @lewd "Rather than waste precious resources, all I ask for are the panties you're wearing."
                                        MC @lewd "What better deal could you get than that?"
                                        show nyx arrogant
                                        NYX @arrogant "... F-Fine."
                                        NYX @arrogant "But this degradation will not be forgotten!"
                                        MC @lewd "Oh, I'm sure it won't."
                                        show nyx angry
                                        NYX @angry "And no payment till AFTER the job is done!"
                                        MC @smile "Of course, I always live up to my end of the deal."
                                        show nyx blush
                                        "Captain Nyx pouted at the comment as her cheeks burned red."
                                        $ QstTheSlavemaster().reward = "panties_success"

        #All choices continued
        NYX @angry "Now that's out of the way, can we focus on the task at hand please?"
        show nyx
        MC @talk "What needs to be done first?"
        "From her table, Captain Nyx handed me a selection of sheets."
        NYX @talk "Wrote here are some details about various trade routes and things, as well as the common price of raza and slaves these days."
        NYX @talk "These things are common knowledge for any trader, and even more so for a criminal like Angharad."
        NYX @talk "Learn these things well, and report back to me when you're ready to begin the next part of our plan."
        #Item gained - Notes on traders and slavers 
        $ PlayerAddItem("book_notes_on_slavers")
        $ renpy.show_screen("book", STR_BOOK.SLAVERS_NOTES)
        $ Pause(0.1)
    #Upon re-speaking to Captain Nyx
    NYX @talk "Have you read the book thoroughly?"
    NYX @talk "You'll need to memorise as much of it as you can to pass as the real deal."
    NYX @talk "Are you sure you're ready for the next stage?"
    menu:
        "Yes, I'm ready.":
            NYX @talk "Good, there's no going back now then."
            MC @talk "I've been meaning to ask, how will we alert the guards once if we DO prove Angharad is there at the meeting?"
            show nyx laugh
            NYX @laugh "Ah, {i}by using this.{/i}"
            "Captain Nyx held out in her hand for me to see a small stone with a strange insignia on it in her hand."
            "The rest of my men are also carrying one each of these."
            MC @think "What is it?"
            NYX @laugh 'A Ghajan stone.'
            NYX @laugh "Once I crack it by crushing it in my hand, it'll begin to glow red, and as will all the other stones my men are using."
            NYX @talk "Once they see that, they'll know it's time to breach the room."
            MC @talk "Surely Angharad and his men might try to fight their way out?"
            NYX @laugh "Once we're sure we're dealing with the {i}real{/i} Angharad, I'll pour everyone some drinks and slip some sleeping powder into it."
            show nyx
            NYX @talk "Hopefully, it should be enough to avoid turning the place into a bloodbath."
            NYX @talk "Anyway, come back here tomorrow evening, then, we'll begin."

            if not QstIsActive(QstTheSlavemaster):
                $ QstComplete(PrimerTheSlavemaster)
                $ QstStart(QstTheSlavemaster)
                $ NoteLock("qstTheSlavemasterCall")

            $ QstSetProgress(QstTheSlavemaster, 1)
            $ GoalComplete(QstTheSlavemaster, 0)
            $ GoalShow(QstTheSlavemaster, 1)
            $ QstSetDelay(QstTheSlavemaster, 1)

        "Not yet.":
            NYX @angry "Come back when you're ready, not before."

            if not QstIsActive(QstTheSlavemaster):
                $ QstComplete(PrimerTheSlavemaster)
                $ QstStart(QstTheSlavemaster)
                $ GoalShow(QstTheSlavemaster, 0)
                $ NoteLock("qstTheSlavemasterCall")

    $ LocEnter()



# Quest update: Return to Captain Nyx in the evening.
# Upon entering in the evening, scene triggers
label qsttheslavemaster_noslave:
    show nyx angry at center_f with dissolve

    NYX @angry "Fuck! FUCK!"
    MC @surprised "What's the matter?"
    NYX @angry "The girl! The fucking girl!" 
    NYX @angry "The one who was supposed to accompany you has been pulled to a different job last minute!"
    NYX @angry "Damn it! Where am I supposed to find someone this late?"
    menu qsttheslavemaster_noslave_menu:
        "There's something I can do that might help!": #Requires MC gender bend ability - N/A for now
            "{i}This choice is not available yet.{/i}"

            jump qsttheslavemaster_noslave_menu

        'Why not fill in the role yourself?': 
            show nyx shock
            NYX @shock "W-What?!"
            MC @think "I mean, it's not like you aren't attractive."
            NYX @sad "I ..."
            show nyx angry
            NYX @angry "I'm the captain of the city guard!"
            NYX @angry "Not some slut!"
            MC @serious "Well, send me alone then?"
            NYX @sad "No, we assured him in the messages prior to this meeting we would attend with our most favored slave."
            NYX @angry "If you turned up alone, he'd likely be spooked."
            MC @serious "Well, what alternative is there then?"
            NYX @angry "..."
            "Captain Nyx stared blankly at me for a few moments, she opened her mouth to say something but stopped herself."
            NYX @angry "Tsch!"
            NYX @angry "... Fine!"
            NYX @disg "I can't believe I'm actually agreeing to this, but it's imperative we stop Angharad!"
            NYX @angry "But I swear, if you try to-"
            "Captain Nyx stopped herself, shaking her head once again."
            NYX @disg "Never mind, just meet me at this address."
            "Captain Nyx handed me the note with the address details and time."
            MC @talk "Wait, I know this place!" 
            NYX @disg "{i}Andddd of course you'd know the brothel ... Fucking degenerate.{/i}"
            "I rolled my eyes, ignoring Nyx's comment."
            MC @talk "I'll see you there."
            NYX @talk "Don't be late."
            $ QstSetProgress(QstTheSlavemaster, 2)
            $ GoalComplete(QstTheSlavemaster, 1)
            $ GoalShow(QstTheSlavemaster, 2)

    $ LocEnter()


# Quest update - Captain Nyx can be found waiting in her 'slave' attire in the brothel - upon clicking on her
label qsttheslavemaster_meeting:
    $ CharSetClothes("nyx", "slave")
    show nyx laugh at cright_f with dissolve
    show mc at cleft with easeinleft
    NYX @laugh "Master, there you are!"
    NYX @laugh "The client is waiting for us in the next private room, as per your instructions, are you ready?"
    menu:
        "You look amazing!":
            NYX @smile "Ooh ... Well ... t-thank you master!"
            show mc surprised
            show nyx angry at center_f with easeinright
            "Subtly, Nyx stepped forward and elbowed me sharply in the stomach."
            show nyx laugh at center_f with easeoutright
            MC @surprised "Urgh!"
            NYX @angry "{i}*Whispering*{/i} Idiot! Focus!"
            show nyx at cright_f with easeoutright
            "Captain Nyx stepped back, smiling from ear to ear once more."
            NYX @laugh "This way, master!"

        "I am; Let's begin.":
            hide nyx with dissolve
            show cg_nyx_slave_back at cright with dissolve
            NYX @laugh "Follow me, Master!" #Show the back of Nyx outfit

    scene black with dissolve
    scene bg_weeping_heart_brothel_room with dissolve

    show mc at cleft with easeinleft
    show nyx laugh at left with easeinleft

    "Upon entering into the luxurious room, Nyx stayed close to my side with a forced smile on her face and her head held low."
    
    show cg_bandit at cright_f with dissolve:
        zoom 0.9

    "Lingering around the place were a couple guards who I presumed were Khazahs, and upon noticing me entering, one of those guards approached."


    GUARD "What business have you here?"
    MC @serious "I am here to speak to Angharad."
    GUARD "There is no-"
    "A voice called from one of the conjoined rooms."
    ANGHARAD "Hold!"

    hide cg_bandit with dissolve
    show angharad at cright_f with easeinright
    "Emerging from the other room, a tall, imposing man who dragged in a chained girl crawling pitifully behind him."
    "The muscular man smiled and beamed pridefully, and while the attire he wore was not expensive garbs by any means, it was clear he lived well."
    "The girl in contrast, had only a doll like look to her eyes, it seemed like she was only half here in the moment with us."
    "Her cheeks were puffy, and it seemed like she had been crying recently, but she refused to look up away from the floor for me to get a good look to know for sure."
    "While she didn't look starved or have any visible bruises on her, it was clear this caged bird was broken, her wings clipped."
    "The man run his hand through his groomed beard as he stepped towards us, dragging the poor girl in heel."
    show angharad smile
    ANGHARAD @smile "Ahh ... Finally we meet."
    menu:
        "Likewise, friend.":
            ANGHARAD @smile "{i}Friend?{/i}"
            ANGHARAD @smile "Well, here is to hoping there is a long and fruitful partnership on the horizon."

        "Shall we discuss business?":
            ANGHARAD @smile "Haha ... Straight to business already?"
            ANGHARAD @smile "Relax, business soon."

    #Both choices continued 
    "Angharad looked down at the slave girl grovelling at his feet."
    show angharad think
    ANGHARAD @think "Alysha, fetch me and my guest some wine."
    "The slave girl Alysha nodded, and rose to her feet to go pour some wine into cups for us."

    hide angharad with Dissolve(0.3)
    $ CharSetVar("angharad", "slave", False)
    show angharad at cright_f
    show alysha at cright_f:
        xoffset -150
    with dissolve
    show alysha at cright with Dissolve(0.2):
        xoffset -150
    hide alysha with easeinright

    ANGHARAD @smile "Alysha is my {i}private{/i} slave."
    "Angharad's eyes lustfully looked over at Nyx."
    show angharad lewd
    ANGHARAD @lewd "{i}And this lovely creature is ...?{/i}"
    MC @talk "This is ..."
    "I hesitated for a brief moment, and Captain Nyx nervously looked towards me."
    MC @talk "Lyesha."
    ANGHARAD @think "Lyesha ..."
    "Angharad let the tongue roll off his name."
    ANGHARAD @lewd "Ly-esh-a..."
    ANGHARAD @think "Quite the unusual name."
    "Captain Nyx didn't say anything, but her whole body seemed to stiffen up to his words."
    "Nyx continued to smile and say nothing as he hungrily looked at her from the other side of the room, but I could sense her shiver in both revulsion and unease."
    ANGHARAD @lewd "What does she look like from behind?"
    show nyx shock
    "Nyx's eyes met mine."
    MC @talk "Turn around and show him slave."

    hide nyx with dissolve
    show cg_nyx_slave_back at left_f with dissolve

    "Nyx obediently did as she was told." #Show the back of Nyx
    ANGHARAD @smile "Very nice ... And where did this one come from?"

    show angharad
    hide cg_nyx_slave_back with dissolve
    show nyx laugh at left with dissolve

    MC @serious "She's told me she came from Gerano before it fell, I found her in one of the passing villages begging."
    "Angharad seemed to be pondering my answer for some time, without saying another word, and quickly, the room felt uneasily tense."
    MC @smile2 "I have so many slaves these days, I must admit, it becomes hard to remember all their names sometimes."
    MC @smile "But Lyesha here, she's a faithful servant to me."
    ANGHARAD @think "..."
    ANGHARAD @smile "Hahaha, now that is something I can understand!"
    ANGHARAD @smile "I used to try remembering names, but in the end, I decided it was simply easier to brand the product."
    ANGHARAD @smile "Much simpler that way."
    "Captain Nyx's hand balled up into a fist, but she did her best to remain submissively bowed with that same strained smile on her face."
    show alysha at right_f with moveinright
    "The slave girl Alysha returned with cups of wine on a tray, and Angharad snatched one, which he gulped at before slapping Alysha's ass loudly."
    play sound spank
    show alysha shock at shake
    ALYSHA @shock "{i}*Gasp!*{/i}"
    "Alysha spilled half of the other cup for me as she stumbled forward towards me."
    show alysha sad
    ALYSHA @sad "I'm sorry! I'm so sorry!"
    ANGHARAD @talk "Now look what you've done girl! Can't even hand someone a drink without fucking it up."
    ANGHARAD @talk "Should I fetch the coals again?"
    ALYSHA @shock "P-Please no."
    MC @talk "There's no harm, don't worry."
    "Gently, I took the half-empty cup and began to sip from it."
    MC @smile "Thank you, Alysha."
    show alysha
    "For a brief moment, some light seemed to return to Alysha's eyes before Angharad snapped."
    show alysha sad
    ANGHARAD @talk "Don't go too soft on your slaves, they start getting all the wrong ideas."

    play sound finger_snap
    show alysha at cright_f with easeinright:
        xoffset -150
    hide alysha
    hide angharad
    with dissolve
    $ CharSetVar("angharad", "slave", True)
    show angharad at cright_f with dissolve

    "Angharad moved over to the comfort of one of the seats and snapped his fingers, Alysha, with that returning blank look in her eyes moved over to kneel down obediently beside him."
    ANGHARAD @smile "Come then ... Before we discuss {i}this thing of ours,{/i} tell me more about you."
    MC @talk "Me?"
    ANGHARAD @talk "Of course! If we're going to be business partners, it's only natural I'd have a few questions, don't you agree?"
    MC @talk "Of course, though on some things, I am a private man."
    ANGHARAD @talk "Oh, of course, of course ..."
    ANGHARAD @talk "I'm curious, from what I've heard about you, you trade by day in fine silks and such."
    ANGHARAD @talk "How does the silk business fair?"
    MC @talk "Lucratively."
    ANGHARAD @smile "Lucratively you say? Hmm ..."
    ANGHARAD @talk "By which route do you normally move such goods?"
    $ tmpvar = {}
    $ tmpvar["angharad_quizz"] = 0
    menu:
        "The King's high Road.":
            ANGHARAD @talk "Hmm ... I see." #correct
            $ tmpvar["angharad_quizz"] += 1
        "The Revalian back roads.":
            ANGHARAD @talk "I see." #incorrect
        "By boat along the river streams.":
            ANGHARAD @talk "Is that so?" #incorrect

    #all choices continued 
    ANGHARAD @talk "I suppose the tax imposed by this 'Emperor' who reigns here is a nightmare on such goods."
    MC @talk "I do my best to pay as little as possible."
    ANGHARAD @talk "Oh, of course, of course."
    "Angharad swirled the remaining wine in his cup and took another sip before continuing,"
    ANGHARAD @smile "By day, I trade in rice and sugar."
    ANGHARAD @smile "It does wonders to keep the banks unquestioning about my coin."
    MC @talk "Interesting."
    ANGHARAD @smile "So ... You move much Raza too, then?"
    MC @talk "Oh plenty."
    ANGHARAD @think "What's the cost of a kilo of Raza in these lands?"
    menu:
        "One to two-thousand Alderian coins.":
            ANGHARAD @talk "Oh, of course, of course ..." #incorrect
        "Three to five-thousand Alderian coins":
            ANGHARAD @talk "Hmm, I see." #correct 
            $ tmpvar["angharad_quizz"] += 1
        "Five to seven-thousand Alderian coins.": 
            ANGHARAD @talk "Hmmm, well then ..." #incorrect

    #All choices continued 
    ANGHARAD @talk "And what route do you usually take to transport that?"
    $ choicemenu = True
    menu qsttheslavemaster_meeting_last_question:
        "What's with all the questions?" if choicemenu:
            ANGHARAD @talk "I'm just curious is all!"
            ANGHARAD @smile "If I'm going to make good business choices out here, these are the kind of things I'll need to know." #loops back to menu
            $ choicemenu = False
            jump qsttheslavemaster_meeting_last_question
        "The King's High Road.": #incorrect
            ANGHARAD @talk "Hm, I see."
        "By boat along the river streams": #incorrect
            ANGHARAD @talk "By boat you say? Interesting ..."
        "The Karisan routes.": #correct
            ANGHARAD @talk "Ah yes, I have heard of those routes."
            $ tmpvar["angharad_quizz"] += 1

    if tmpvar["angharad_quizz"] < 2:
        $ tmpvar = {}
        #all choices continued 
        #fail version - player got more than 1 question wrong 
        ANGHARAD @smile "I have just one more question ..."
        show angharad furious
        ANGHARAD @furious "Do you take me for a fucking fool?!"
        show mc serious
        show nyx
        $ AutoMus(False)
        $ PlayMusic( "audio/music/31_Encounter.ogg")
        MC @serious "(Shit!)"
        MC @serious "What are you talking about?"
        ANGHARAD @furious "What kind of trader doesn't know the answer to those questions?"
        ANGHARAD @furious "YOU'RE A SPY!"
        show mc
        MC @surprised "(... Oh fuck.)"
        show nyx angry
        NYX @angry "... Fuck it!"
        "Captain Nyx pulled out a small stone that she crushed in her hand, as she did so, it cracked and glowed red, and moments later, the doors burst open as the place was rushed by dozens of city guardsmen."

        $ AutoAmb(False)
        play ambience "audio/ambience_scenes/battle_swords_shouting.ogg" fadein 3.0 volume 0.6
        ANGHARAD @furious "SHIT!"
        "The place was soon a clash of blades, blood, and confusion as the few Khazah guards tried to battle their way out through the city guards while Angharad futilely looked for some kind of exit."
        "The khazah's screamed as their blades were no match for the city guards spears, which they tried to bat away with their blades but the spears soon prodded and pierced at their flesh."
        "Angharad hurried to the back of the room, grabbing Alysha by the arm as he pulled her back with him."
        "In the ensuing chaos, two of Angharad's guards rushed towards me, blades drawn with a maddening furious look in their eyes,"
        GUARD "KILL THE TRAITOR!"
         
        $ StartBattle(BattleData(BackgroundImage = "pbat_diamond_night", CharIDList_Right = ["e_thug", "e_bandit", {"e_bandit":2}]))

        scene bg_weeping_heart_brothel_room
        show mc serious at cleft
        show nyx angry at left
        show cg_angharad_hostage at cright:
            yoffset 45
        with dissolve

        $ AutoAmb(True)
        "With the two guards cut down, Angharad was now the only one left standing as he held a blade towards Alysha's throat."
        "Petrified, Alysha cried as tears streamed down her cheeks."
        ALYSHA "M-Master! What are you doing?!"
        ANGHARAD "Quiet you!"
        ALYSHA "N-No! M-Master!"
        ALYSHA "P-Please don't kill me!"
        ANGHARAD "SHUT IT WHORE! Shut the fuck up!"
        "The city guards cornered and surrounded Angharad, blades pointed towards him."
        MC @serious "Surrender now Angharad, there's nowhere to run!"
        ANGHARAD "Get back! All of you!"
        NYX "Let the girl go!"
        ANGHARAD "I'm walking out of here with this bitch whether you all like it or not!"
        NYX "It's over, Angharad!"
        NYX "Let the girl go and you'll still receive a fair trial!"
        ANGHARAD "{i}'Fair trial?'{/i}"
        ANGHARAD "Oh no, if I'm going to die, I'll die a free man, HERE AND NOW!"

        show mc surprised
        show nyx shock
        play sound knife_slice volume 0.3
        show cg_angharad_hostage killed with bloodflash

        "With a furious roar, Angharad dragged his blade across Alysha's throat, and the girl quickly dropped to the floor, grasping at her throat gushing blood."
        "Alysha clutched at her throat as she desperately tried stop the blood flowing down onto her body and the floor below."

        show mc serious
        show nyx angry

        $ CharSetVar("angharad", "slave", False)

        $ CharKill("alysha")
        $ QstTheSlavemaster().AlyshaDead = True
        play sound body_fall_ground
        hide cg_angharad_hostage
        show angharad furious at cright_f:
            xoffset -50
        with dissolve

        "After some gargling and choking on her blood, she plunged head first onto the flood, squirming and twitching before stopping moving entirely in a pool of her own blood."
        MC @surprised "FUCK!"
        play sound knife_slice
        hide angharad
        show cg_angharad_stabbed at cright with bloodflash:
            xoffset -50
        "Angharad charged forward with his blade towards Captain Nyx, but the other guards quickly interceded, plunging their spears into him."
        play sound knife_slice
        "Grunting in pain at the shock of the spears piercing his flesh, blood pouring from his mouth, he slashed desperately at one of the guards with his blade, leaving a gash in guardsmen's face." with bloodflash
        play sound [knife_slice, "<silence .05>", knife_slice]
        show cg_angharad_stabbed with bloodflash
        $ Pause(0.4)
        "As the guardsmen stumbled backwards to clutch at his face in pain and scream, Angharad managed to kick away another one of the guards before another spear pierced his side." with bloodflash
        "The blood seeped through the expensive fabric of his clothes as he gasped for air, his lungs quickly flooding with blood."
        
        show cg_angharad_stabbed at left with easeinright:
            xoffset 130
        play sound knife_slice
        "With one last furious roar, Angharad managed to break through the city guards line towards Nyx, managing to slice at her shoulder with his blade." with bloodflash
        show nyx angry
        NYX @shock "GAHHHHH!" with hpunch
        show mc surprised
        MC @surprised "CAPTAIN NYX!"

        show cg_angharad_stabbed at cright with easeinleft:
            xoffset -50

        play sound [knife_slice, "<silence 0.01>", knife_slice]
        show cg_angharad_stabbed with bloodflash
        $ Pause(0.4)
        "He was quickly pushed back by the guards blades which again pierced into him, making him whelp in pain." with bloodflash
        play sound knife_slice
        "One of the other guardsmen leapt forward, slashing at Angharad across his throat as he gargled and choked on his blood." with bloodflash
        
        play sound body_fall_ground_shorter
        show cg_angharad_stabbed at cright with easeintop:
            xoffset -50
            yoffset 300
        "It was this final strike that bought Angharad to his knees, and then, quickly to the floor with a loud thud."
        play sound body_fall_ground
        hide cg_angharad_stabbed with dissolve
        "Angharad clutched at the bleeding wounds to no avail, gasping and wheezing for air in a pool of his own blood."
        "Soon, after one last strained gasp of air, he lay motionless on the floor."
        stop music fadeout 3.0
        $ AutoMus(True)
        show mc surprised at cleft_f with dissolve
        "The carnage had finally stopped, and I rushed to Captain Nyx's side."
        MC @surprised "Captain Nyx! Are you-"
        show mc surprised at center_f with moveinright
        "Captain Nyx pushed me away."
        NYX @angry "I'm - urghh! Fine damn it!"
        NYX @angry "{i}*Huff*{/i} Fuck ... What a shitshow."
        NYX @angry "Arghh!"
        "In pain, Captain Nyx stumbled and I quickly reached out to grab her again."
        MC @surprised "Easy now!"
        "Angrily, Nyx looked towards the guards who were stood around inspecting the room and clumsily checking the dead bodies around us."
        NYX @angry "Would one of you idiots take me to the infirmary already?!"
        "Two of the guards snapped out of it and hurried over towards us, helping Captain Nyx to her feet as they helped carry her over towards the door."
        show mc sad
        MC @sad "What should I-"
        show nyx disg
        NYX @disg "Just get out of here ... This whole thing has been a complete fuck-up."
        NYX @disg "The last thing I need is someone else coming in to clean up this mess and finding out about {i}you.{/i}"
        "Captain Nyx winced in pain once again."
        NYX @disg "...Grghh!"
        show mc
        show nyx disg at left_f with dissolve
        hide nyx with easeoutleft
        $ CharSetClothes("nyx", "normal")
        "Before I could say anything to answer her, Captain Nyx was already being escorted out of the blood-soaked room."
        MC "(... Damn it.)"
        MC "(If only I'd known those answers better.)"
        MC "(I should check in on Captain Nyx in a few days once she's had a chance to recover.)"

        scene black with dissolve
        $ QstSetProgress(QstTheSlavemaster, 4)
        $ GoalComplete(QstTheSlavemaster, 2)
        $ GoalShow(QstTheSlavemaster, 4)
        $ QstSetDelay(QstTheSlavemaster, 3)
        $ TimeAdvBy(TIME_3H)
        $ LocSet("novaras_bordello_ext")
        $ LocEnter()

    else:
        $ tmpvar = {}
        #Success version - player got all questions correct (1 mistake allowed)
        show angharad smile
        show mc serious
        ANGHARAD @smile "It pleases me to know my future business partner is so knowledgeable."
        MC @serious "Am I to seriously believe you didn't already know all of those answers?"
        ANGHARAD @smile "... You can never be too careful these days."
        ANGHARAD @talk "I just needed to be sure you were {i}really{/i} one of us."
        MC @serious "Enough games; I came here to do business, not be toyed with."
        ANGHARAD @smile "Relax, friend, it's almost time for business, but first ..."
        ANGHARAD @lewd "Alysha, come."

        $ CharSetVar("angharad", "slave", False)
        hide angharad with Dissolve(0.3)
        show angharad lewd at cright_f with Dissolve(0.3)

        "Alysha sighed and climbed up onto one of the beds, waiting patiently."
        show mc surprised
        MC @surprised "What are you-"
        ANGHARAD @lewd "I never conduct business with a man unwilling to fuck one of his own slaves."
        ANGHARAD @furious "It tells me he doesn't have the kind of stomach needed for this kind of thing."
        show mc serious
        MC @serious "... You can't be serious?"
        ANGHARAD @talk "I am."
        show nyx shock
        "Nyx for the first time nearly broke character, her mouth opening to protest but no words came out."
        "She looked up towards me with a look of bewilderment before doing her best to pull herself back into character."
        show nyx laugh
        ANGHARAD @talk "There can be no further business discussions till I can see this commitment."
        hide angharad with dissolve
        "Angharad climbed onto the bed with Alysha, pouncing onto her like a predator." 
        "From Alysha's lifeless expression, I could tell he had done this many times, and she merely endured whatever he did to her."
        "Every so often, Angharad would glare up towards us, and I quickly realised this was again another one of his 'tests.'"
        show mc at cleft_f with dissolve
        show nyx blush
        "I grabbed Captain Nyx's shoulders and spun her to face me; She was stiff, her cheeks red from embarrassment and nervousness."
        MC @serious "Come, Lyesha ... You know what to do."
        show nyx shock
        "Captain Nyx stared frozen at the command, and as she looked over towards Angharad continuing to watch us while he had his way with Alysha, she gulped and looked back sheepishly towards me."
        NYX @sad "Y-Yes ... Of course M-Master!"
        "Shyly, Captain Nyx began to with shaky hands strip off my armour piece by piece."
        "I could tell she most certainly wasn't used to this kind of thing, her heart racing as she clumsily undid every strap."

        hide mc with dissolve
        $ CharSetClothes("mc", "naked")
        show mc lewd at cleft_f with dissolve
        "With the last of my armour stripped away, Nyx's eyes wandered up and down my naked body, her cheeks flushed red in surprise."
        NYX @shock "(He's ... Gods, his body looks like it was sculpted from marble!)"
        "Her eyes locked onto the dangling appendage between my legs."
        show nyx blush
        NYX @blush "(And the size of that-)"
        MC @lewd "... Ny- I mean, slave."
        "Captain Nyx looked up like a child who had just been caught stealing some sweet roll."
        MC @lewd "Don't just keep staring at it, girl."
        NYX @blush "Y-Yes Master."
        "Nyx run her hands down my chest; Her face flushed red as she began to breathe heavily."
        "Her eyes seemed transfixed on the muscles in front of her as she gently traced her fingers gently from my chest to my abs."
        NYX @blush "(You could chip a tooth on him ...)"
        "I tilted Nyx's head up."
        MC @lewd "Are you ready?"
        "Nyx nodded nervously, leaning in to whisper in my ear,"
        NYX @blush "{i}J-Just let me handle everything, okay?{/i}"
        "I nodded, and Nyx lightly pushed me down onto one of the opposing beds."

        $ AutoMus(False)
        $ PlayMusicRandom("mus_sex")
        $ HideUI(True)

        #Show CG - reverse cowgirl - Nyx - grind
        scene ss_nyx_slave_grind with dissolve
        "Nyx turned away from me, her cute ass now wiggling in front of me as she positioned her butt against my cock."
        NYX "(I - I can't believe I have to do this ...)"
        NYX "(But I have to! I have to focus on the task at hand!)"
        NYX "(Gods ... How am I ever going to look at him the same after this?)"
        NYX "(It's too embarrassing to look at him head-on.)"
        NYX "(I hope this works!)"
        scene ss_nyx_slave_grind_1 with dissolve
        MC "Lyesha!"
        "Her cheeks still flushed red, Nyx looked over her shoulder to watch me as she gently rubbed up against me."
        "Her blonde pubic hair brushed up against me as Nyx's womanhood began to wetly glisten."
        "From soft, drawn out breathes, I could tell it had been a long time since she'd done something like this."
        NYX "Ahhh ... T-This is your favorite position, right master?"
        NYX "(Please, please, PLEASE, say yes!)"
        MC "Ahh! O-Of course!"
        NYX "(Oh, thank the gods he's not a complete idiot!)"
        "Captain Nyx, for some time then continued to rub herself against me, at first, she was stiff and clearly uncomfortable."
        "It was quickly clear it had not just just 'been a while' since she last did this, Captain Nyx clearly wasn't very {i}experienced{/i} with this sort of thing at all."
        "After a while though, she began to relax, breathing heavily as she rocked back and forth, coating my cock in her juices."
        $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg",1)
        scene ss_nyx_slave_grind_2 with Dissolve(0.2)
        NYX "Mmmfghh...!"
        NYX "(W-What is happening to me?)"
        NYX "(It's been so long ... I thought I ... I'd ...)"
        "Another moan escaped Nyx's lips as she moved to quickly cover her mouth in embarrassment."
        NYX "(Oh g-gods! That f-feeling again!)"
        NYX "(No I need to stay focused!)"
        NYX "(What woman would seriously be interested in this f-fucking crude, moronic a-adhhh!)"
        NYX "(Grghhh! FOCUS! HE'S JUST ANOTHER TOOL FOR ME TO USE! JUST ANOTHER PIECE ON THE BOARD!)"
        NYX "(S-So what if he smells - Mmmm, really fucking good and has a c-cock blessed from the gods?)"
        NYX "(No! No no! Push the thoughts aside! H-He's not even human really! H-He's a monster!)"
        MC "Ahhh ... Ny-."
        "I barely managed to stop myself from calling out her real name."
        MC "G-Good slave!"
        "In the corner of my eye I could see Angharad was now more preoccupied with Alysha, satisfied that we were partaking, he only occasionally looked up towards us and grinned."
        "Nyx, flushed red, bit at her lower lip before speaking, her voice breaking up from nervousness."
        NYX "M-Master ..."
        NYX "I-I'm going to put it in now, okay?"
        "I didn't say anything; I just nodded my head as Nyx, taking a hold of my cock into her soft, warm hand, positioned it against the entrance of her tight womanhood."
        NYX "(Am ... Am I really going to do this?)"
        NYX "(I ... I have to! I can't stop now! I have to see this through!)"
        "Gently, Nyx guided herself slowly down onto my member, gasping as she took it a few inches in and suddenly stopping herself midway." #sex animation - penetration
        "Nyx trembled and shook for a moment, and I could tell she was struggling with my size."
        "For a moment, I thought to say something or help her in some way, but Nyx forced herself to continue to slide down and take my cock deeper."
        $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg",1)
        scene ss_nyx_slave_vag_1 with dissolve
        NYX "Mmmfghhh!!"
        NYX "(I- I've never felt one so-)"
        NYX "(Focus! FOCUS! FOCUS!)"
        NYX "(I can't lose myself to this! I n-need to remember my vows! I need to ... to ...)"
        "Gently, Nyx began to squat, bouncing up and down onto my cock, her incredibly tight pussy squeezing and wrapping around me."
        NYX "Mmmff ..."
        NYX "Oh g-gods ..."
        NYX "(T-This pleasure.)"
        NYX "(I'd forgotten how good it could feel.)"
        NYX "(N-No, {i}it'd never felt this good before!{/i})"
        NYX "(Ahhh ... I-Is this because of the beast inside of him?)"
        NYX "(O-Oh! What does that even say about me for enjoying this all the more then?)"
        NYX "(T-There's still time, I just - {i}*Huff*{/i} need to endure this!)"
        $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
        scene ss_nyx_slave_vag_2 with Dissolve(0.2)
        "Nyx slide down deeper, now moving faster as she worked herself up more and more."
        "Soon, she managed to bottom out, her soft ass now hitting against my groin as she dropped her hot body down onto me."
        NYX "Ah! Ahh! Mmff!"
        "With my whole cock somehow fitting inside of her body, Captain Nyx moaned hotly as she began to slam her hips back onto me."
        MC "Hrghh! S-Slave! Careful! You're going to-"
        BLACK "(Hormones successfully released, this mate should be experiencing an extreme rush of dopamine.)"
        MC "(Gah! Releasing of what? At least me know a little earlier before you do that!)"
        MC "(Ooofghh! She feels amazing! I wonder if it feels as good for her as it does me?)"
        NYX "(H-Hrghh! IT FEELS SO G-GOOD!)"
        NYX "(WHY ISHITSHOOO GHOOOOD!)"
        NYX "(Nooooo! I'm n-not so animal who loses c-control! I'm a loyal knight! The c-captain of the .. Mmmfghh!)"
        "Nyx's bubbly butt continue to slam against me, sweat pouring from her body as she moved like a woman possessed."
        "With her mouth hung agape, she no longer tried to suppress her cries, loudly grunting and sweetly moaning as she rode me."
        NYX "(I can't think! I CAN'T THINK ANYMORE! IT'S TOO MUCH! TOO MUCH!)"
        NYX "G-Give it to me!"
        NYX "Give me your big fucking cock master!!"
        NYX "(What's going on with me?! Why am I talking like this?)"
        NYX "Mmmfhghh!! Fuck my cunt! Fuck your little meat sleeve good! You - Hrghhh!!"
        NYX "(T-The words just keep tumbling out of my mouth!)"
        "As the soft flesh of her butt continued to grind and hit against me, her tight womanhood was quickly becoming too much."
        NYX "Yes! Yes! Fuck me Master! FUCK ME HARDER!"
        MC "{i}*Huff*{/i} N-Nyx! I'm getting close!"
        "Nyx wasn't listening, her mind seemed to have melted away entirely, all that mattered was slamming her hips greedily back down onto me as she trembled and moaned."
        NYX "D-Don't s-stop ... Don't ever s-stop!"
        NYX "It's shoooo good!"
        NYX "I'm ... I'm ..."
        NYX "...!"
        "Nyx froze for a moment, her whole body began to shake as she grinded herself on my cock, muttering over and over again."
        NYX "{i}Cumming! Cumming! Cumming! Cumming!{/i}"
        MC "Hrghh! I'm gonna cum!"
        $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
        scene ss_nyx_slave_finish with flash
        $ ReduceInfectionFromSex("nyx")
        "Grunting and unable to hold back any longer, I flooded my hot seed into Nyx, who felt the rush of thick cream pouring into her," #cum CG 
        "Nyx's whole body tightened and squeezed me as her mouth hung open, unable to make a sound as her eyes widened, feeling the pleasure wash over her."
        "Fully spent, Nyx breathlessly rose and pulled herself off from my cock, my cum pouring out of her as she shakily did her best to gather her bearings."
        NYX @blush "Oh gods ... {i}*huff*{/i} That was ... That was ..." #sex scene ends

        $ UnlockGalSceneAndGrantXp("nyx","slave")
        $ HideUI(False)

        $ AutoMus(True)

        scene bg_weeping_heart_brothel_room with dissolve
        show angharad smile at cright_f

        "Angharad suddenly sprung up, cheerfully smiling."
        ANGHARAD @smile "Now that was a show!"
        $ CharChangeRel("nyx", 1)
        show mc lewd at cleft
        show nyx at left
        $ CharSetClothes("mc", "normal")
        with dissolve
        ANGHARAD @smile "I can see now why he bought you!"
        show nyx blush
        "Captain Nyx blushed red from embarrassment and frustration once again, her hands balled into fist as Angharad laughed."
        ANGHARAD @smile "Oh, she is a feisty one, isn't she?"
        ANGHARAD @smile "No wonder this one is your favourite."
        NYX @blush "(This is ... so {i}humiliating.{/i})"
        NYX @blush "(I'm the Captain of the Alderian Guard for Novaras! A decorated knight of the Emperor!)"
        NYX @blush "(N-Not some ... some common whore!)"
        show mc
        show nyx laugh
        MC @talk "Angharad ..."
        MC @serious "Let us talk business, no more games."
        show angharad
        ANGHARAD @talk "{i}*Sigh*{/i} You really do need to learn to relax more, friend."
        ANGHARAD @talk "Very well, let's start with numbers, I have at least fifty of the finest girls to spare."
        ANGHARAD @talk "Ten Alderians, Thirty Ramonians and ten elves."
        ANGHARAD @talk "I can have them brought in through Hamun by next month, and transported anywhere in Novaras."
        ANGHARAD @talk "How many do your private {i}clients{/i} need?"
        MC @serious "How much for all of them?"
        show angharad smile
        ANGHARAD @smile "{i}All of them?{/i}"
        "Angharad chuckled,"
        ANGHARAD @smile "Allow me to check some numbers."
        MC @talk "Before you do that ..."
        show mc serious
        MC @serious "How do {i}I{/i} know I'm speaking to the {i}real{/i} Angharad?"
        show angharad furious
        ANGHARAD @furious "Are you calling me a liar?"
        MC @serious "I've done everything to jump through your hoops to prove I am who I say I am, yet if I am to spend this much coin, I too would like some reassurance."
        show angharad
        ANGHARAD @talk "{i}*Sigh*{/i} Very well."
        "Angharad for a moment headed over towards a small chest and produced from it what seemed to be an inscribed amulet, which he tossed towards me."
        "The thing was clunky and heavy, with a small green jewel in the middle and Ramonian written around it followed by 'Angharad XXII"
        ANGHARAD @talk "My slave number."
        "I stared down at the amulet, and then back at Angharad in disbelief."
        show mc
        MC @surprised "{i}You were a slave?{/i}"
        ANGHARAD @smile "Of course."
        ANGHARAD @smile "After proving my value to my master long enough, he came to trust me more and more."
        ANGHARAD @talk "And when his guard was down ... I slit his throat, and took everything he had." 
        menu:
            "Why didn't you free the others afterwards?":
                ANGHARAD @talk "Why should I have?"
                MC @sad "It's just, you must have felt {i}something{/i} for them?"
                ANGHARAD @talk "... You're an odd slaver, aren't you?"
                ANGHARAD @talk "No, I did not."
                ANGHARAD @talk "Had it not been me, someone else would have done the same given the opportunity."
                ANGHARAD @talk "Only people who have always had coin speak of luxuries like {i}righteousness.{/i}"
                ANGHARAD @talk "The starving man? The slave? The man with nothing to lose?"
                ANGHARAD @talk "He won't question whether something is good or evil when he drags the blade across your throat for just a few coins."
                "As I opened my mouth to say something, Captain Nyx suddenly tugged at my arm to intercede."

            "I can respect that.":
                ANGHARAD @smile "Of course you can."
                ANGHARAD @talk "You and I understand this world was not for us, our kind were never meant to climb the great ladder."
                ANGHARAD @talk "If we want to find happiness, it will come at the expense of everyone else."
                "Captain Nyx stepping towards me from behind tugged at my arm."

        #Both choices continued
        show nyx
        NYX @talk "Master? Should I fetch us all some wine?"
        "Nyx gripped my arm tightly and I could see from her eyes she was giving me the signal that we had the proof she needed."
        MC @talk "Yes, fetch us some wine."

        show nyx at left_f with dissolve
        hide nyx with easeoutleft

        "Captain Nyx hurried off to go pour some wine for us."
        show angharad smile
        ANGHARAD @smile "... So, do you love your slave?"
        MC @surprised "What?"
        ANGHARAD @smile "You'd hardly be the first."
        ANGHARAD @smile "And the way you two look at each other, well, even the blind could see that."

        show nyx at left with easeinleft

        "Captain Nyx, after making her way around the room handing each of the guards a cup, she gave Angharad one which he gulped down quickly and threw aside, before finally approaching me with the final cup."
        NYX @talk "Master~"
        "Nyx lightly nodded to signal to me as I took the cup, and with one sniff, I could tell from the potency of the drug she had placed inside of it, that it wouldn't take long to kick in."
        "I pretended to sip at my drink to not arouse suspicion before placing it down back onto the tray."
        MC @talk "Thank you, Lyesha."
        "After a few minutes of small talk and laughing amongst the men now they had relaxed in my pressence, Angharad finally interjected,"
        ANGHARAD @smile "Now then, what's say we-"
        "One of the Khazah guards suddenly collapsed onto the floor, the others turned to look in panic, reaching for their blades as one by one they fell to the floor."
        show angharad furious
        ANGHARAD @furious "WHAT THE FUCK IS THIS?!"
        "Captain Nyx pulled out the small stone that she crushed in her hand, and as she did so, it cracked and glowed red."
        "Moments later, the place was rushed by dozens of the city's guards, spears pointed and ready."
        ANGHARAD @furious "YOU SON OF A-"
        "Angharad himself tried to reach to grab his blade, gripping the handle as he fumbled and crashed his way into the pieces of furniture deliriously."
        ANGHARAD @furious "I'll ... kill ..."
        "Just as Angharad managed to unsheathe his blade, he too collapsed onto the floor with the others, fast asleep."
        hide angharad with dissolve
        show nyx angry
        NYX @angry "Seize them all at once!"
        show cg_guard at right_f with easeinright
        "The guards quickly swept across the room, gathering up and arresting Angharad and the other khazah bandits while they were unconscious."
        $ CharSetClothes("alysha", "free")
        show alysha at cright_f with easeinright
        "A shaking Alysha approached the two of us, dazed and confused as to what was going on."
        ALYSHA @talk "W-Who are you both?"
        NYX @talk "I am Captain Nyx of the Novaras city guard."
        show alysha shock
        ALYSHA @shock "C-Captain?"
        NYX @laugh "You're free now, Alysha."
        ALYSHA @shock "F-Free?"
        NYX @talk "We'll take you in for questioning, and then I'll personally see to it that you're looked after we're done, don't worry."
        NYX @talk "You, and hopefully the other girls too."
        "Alysha's expression was a strange kind of wistfulness, then the tears began to stream down her cheeks."
        show alysha crying
        ALYSHA @crying "It's ... It's really over? I'm free?"
        ALYSHA @crying "{i}I'm ... I'm free.{/i}"
        "Alysha suddenly collapsed to the floor, and a panicked Captain Nyx grabbed her."
        play sound body_fall_ground volume 0.3
        hide alysha with dissolve
        show nyx shock
        NYX @shock "Someone get this girl seen to!"
        show cg_guard at blurin, right
        show alysha at cright:
            xoffset 50
        with dissolve
        $ Pause(0.2)
        hide cg_guard
        hide alysha
        with easeoutright
        "A couple guards rushed over to grab and carrying her outside."
        MC @talk "Will she be okay?"
        show nyx
        NYX @talk "She's probably in shock."
        NYX @sad "Gods only know what that girl's been through."
        "Captain Nyx shuddered at the thought."
        NYX @talk "Anyway, you best clear off before some of the others get here."
        show mc lewd at cleft_f with dissolve
        show nyx blush
        "Neither of us moved for a moment, staring awkwardly at each other as we finally had a moment to process everything that had just happened."
        NYX @blush "W-What are you are you looking at me like that for?"
        "I gently reached out to grab Nyx's arm."
        show mc
        MC @talk "Don't you think we should maybe talk about what just happened in there?"
        show nyx angry
        play sound slap
        show mc surprised
        "Nyx slapped my hand away."
        NYX @angry "There's nothing to talk about!"
        NYX @angry "Everything that happened, happened for the mission! That's all!"
        NYX @angry "Are we clear?"
        MC @surprised "I just thought you might want to at least-"
        NYX @angry "J-Just get out of here!"
        NYX @angry "You'll just get in the way now, so leave!"
        show mc serious
        MC "..."
        MC @serious "Fine then, as you wish."
        "Disgruntled, I headed off without saying another word."
        "If she didn't want to talk about what had happened, then whatever."
        "If it was just {i}all for the mission,{/i} then I too could push it aside."
        hide mc with easeoutleft
        #MC exits off screen
        show nyx blush
        $ CharChangeRel("nyx", 1)
        NYX @blush "..."
        scene black with dissolve
        $ QstSetProgress(QstTheSlavemaster, 3)

        $ GoalComplete(QstTheSlavemaster, 2)
        $ GoalShow(QstTheSlavemaster, 3)
        $ QstSetDelay(QstTheSlavemaster, 1)
        $ CharSetClothes("nyx", "normal")
        $ TimeAdvBy(TIME_3H)
        $ LocSet("novaras_bordello_ext")

        $ LocEnter()


label qsttheslavemaster_reward:
    #The day after completing Captain Nyx's quest - small scene prompt when player exits the house
    #MC "(I should head to speak to Nyx to get my payment ... Not that she wants to see me now.)"

    #Next scene triggers when player enters Captain Nyx office 

    if QstGetProgress(QstTheSlavemaster) == 3:
        if day < QstGetDelayVal(QstTheSlavemaster) or (day == QstGetDelayVal(QstTheSlavemaster) and rpTime < TIME_MORNING):
            "It seems that Captain Nyx hasn't returned yet to her office after the mission. I'll come back later.."

        else:
            show nyx angry at cright_f with dissolve
            show mc at cleft with easeinleft
            NYX @angry "What are you doing here?"
            NYX @angry "I told you to-"

            if QstTheSlavemaster().reward == "panties_success":
                #IF PLAYER SELECTED PANTIES AS REWARD
                show mc smile
                MC @smile "Well I'm obviously here to collect on my payment."
                NYX @shock "Your ... {i}payment?{/i}"
                "Captain Nyx's face flushed red from embarrassment before her shocked expression coiled into a scowl."
                NYX @angry "Y-You can't be serious!"
                NYX @angry "After what happened?"
                MC @lewd "I'm very serious."
                MC @lewd "And I'm here to collect on that debt."
                NYX @angry "Y-You ..."
                "Captain Nyx's hands coiled tightly into fists, and I thought for a moment she might fling herself to hit me."
                hide nyx 
                show cg_nyx_halfnaked at cright_f
                with dissolve
                "Instead, she took a deep breathe, and angrily began to strip away at what armour she needed before pulling down the panties and flinging them at me."
                $ PlayerAddItem("qst_nyx_panties", 1)
                NYX @angry "Happy? {i}Satisfied?{/i}"
                hide cg_nyx_halfnaked with dissolve
                $ CharSetClothes("nyx", "normal")
                show nyx angry at cright_f with dissolve
                MC @lewd "Not yet, but I will be soon."
                NYX @angry "... G-Get out!"
                MC @smile "Later, Captain."
                #MC leaves
                show mc at cleft_f with dissolve
                hide mc with easeoutleft
                NYX @sad "..."
                NYX @blush "(What's wrong with me? Why was it so hard to get rid of him just now?)"
                $ CharChangeRel("nyx", 1)

            else:
                #If player completed the mission successfully
                MC @serious "Relax, I'm just here for my payment."
                show nyx sad
                NYX @sad "Your ... payment."
                "I felt the anger in her begin to subside to cool indifference."
                NYX @sad "Here. Your payment." #Player recieves the amulet or the coin.
                if QstTheSlavemaster().reward == "money_success":
                    $ PlayerAddItem("gold", 750)
                elif QstTheSlavemaster().reward == "amulet":
                    $ PlayerAddItem("amulet_protection", 1)
                elif QstTheSlavemaster().reward == "skill":
                    $ PlayerAddItem("amulet_protection", 1)
                else:
                    $ PlayerAddItem("gold", 600)
                NYX @sad "Now, get out."
                MC @sad "Nyx, I-"
                NYX @angry "GET OUT!"
                MC @talk "... Very well." 
                #MC leaves
                show mc at cleft_f with dissolve
                hide mc with easeoutleft
                NYX @sad "..."
            $ NoteUnlock("romanceNyxStart")
            $ GoalComplete(QstTheSlavemaster, 3)
            $ QstComplete(QstTheSlavemaster)

    else: # progress == 4
        #IF PLAYER FAILED THE QUEST 
        if day < QstGetDelayVal(QstTheSlavemaster) or (day == QstGetDelayVal(QstTheSlavemaster) and rpTime < TIME_MORNING):
            "It seems Captain Nyx hasn't recovered yet from her wounds. I should come back in few days."

        else:
            show nyx sad at cright_f with dissolve
            show mc at cleft with easeinleft
            NYX @sad "... What are you doing here?"
            MC @talk "I came for payment."
            show nyx angry
            NYX @angry "{i}Payment?{/i} You expect payment for that shit show?"
            show mc serious
            MC @serious "That's not how I wanted things to go either, Captain."
            show nyx sad
            NYX @sad "...{i}*Sigh*{/i}"
            NYX @sad "Here, it's half of your payment in coin."
            if QstTheSlavemaster().reward == "money_success":
                $ PlayerAddItem("gold", 375)
            else:
                $ PlayerAddItem("gold", 300)
            NYX @angry "Don't even fucking think of trying to sweet-talk me into raising it or asking for anything else."
            show mc sad
            MC @sad "Do you want talk about what happened at least?"
            NYX @sad "... No, I ... I want you to leave."
            show mc
            MC @talk "I see."
            MC @talk "Goodbye, Captain Nyx."
            show mc at cleft_f with dissolve
            hide mc with easeoutleft
            #MC leaves 
            NYX @angry "(At the very least I can take some solace in knowing that fucker is dead.)"
            NYX @sad "{i}*Sigh*{/i}"
            NYX @sad "(I shouldn't take it out on him too much ...)"

            $ GoalComplete(QstTheSlavemaster, 4)
            $ QstFail(QstTheSlavemaster)

    scene black with dissolve
    $ LocSet("novaras_fort_seb_barracks")
    $ LocEnter()