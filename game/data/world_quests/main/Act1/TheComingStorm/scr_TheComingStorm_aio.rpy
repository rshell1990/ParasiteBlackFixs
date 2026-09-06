label qst_thecomingstorm_primer:
    show mc at cright_f with easeinright
    GUARD "HOLD!"
    show cg_guard at cleft with easeinleft
    MC @talk "Hm? What is this about?"
    GUARD "There is an emergency meeting at the Adventurers' Guild this evening."
    GUARD "All adventurers are to attend immediately."
    MC @think "Since when does the city guard involve itself in guild business?"
    GUARD "This is not guild business."
    GUARD "This is by direct order of Emperor Alcott himself."
    MC @surprised "What?!"
    MC @angry "What is this about?"
    GUARD "Your job isn't to question the Emperor's will, 'adventurer.'"
    show cg_guard at shake
    GUARD "Attend the meeting! That's an order!"
    hide cg_guard with easeoutright
    $ NoteUnlock("TheComingStormMeeting")
    $ QstSetProgress(PrimerTheComingStorm, 1)
    $ Pause(0.1)
    show mc at center_f with ease
    MC @think "(Something tells me this isn't something I can just ignore.)"
    $ LocEnter()

label qst_thecomingstorm_attendmeeting_button:
    show mc at center with easeinleft
    MC @talk "(I should finish up whatever I need to do first...)"
    MC @talk "{i}(I might not get another chance.){/i}"
    call screen ok_popup(label = _("Developers note"), text = _("You should really save your game before starting this quest."))
    menu:
        "{image=[ICON.CLOCK]} Attend the meeting":
            hide mc with easeoutright
            jump qst_thecomingstorm_guild_meeting_and_onwards
        "Not yet":
            show mc at blurin, center_f
            $ Pause(0.1)
            $ LocEnter()

label qst_thecomingstorm_guild_meeting_and_onwards:
    $ InfGainDaily(False)
    $ NoteLock("TheComingStormMeeting")
    scene black with dissolve
    "... The guild hall was bustling, yet eerily quiet."
    "There was a nervous energy to the place, a sense that something unprecedented was happening."
    "A heavy tension hung in the air, suffocating the usual rowdy chatter."    
    "The hall was packed with adventurers of all ranks, waiting for the announcement to come."
    $ LocFlush(dissolve)
    "And then, the door swung open."
    show cg_guard at center_f with easeinright

    GUARD "Greetings, adventurers."
    GUARD "I come bearing the words of Emperor Alcott, who thanks you all for your attendance and—"

    ADVENTURER_LEAN "I was recalled from my damn quest before those bastards, {i}The White Lions{/i}, swooped in and took the fucking prize!"
    ADVENTURER_LEAN "I expect my party to receive a share, damn it!"
    show cg_guard at blurin, center
    ADVENTURER_BULKY "Fuck off, Galdrick!"
    ADVENTURER_BULKY "You weren't even in the right cave!"
    show cg_guard at blurin, center_f
    ADVENTURER_REDHEAD "The grievances of the Blue Falcon party remain unaddressed!"
    ADVENTURER_REDHEAD "The Lunar Guardians stole our mage!"
    show cg_guard at blurin, center
    ADVENTURER_SHORT "We didn't steal anything, you pompous prick!"
    ADVENTURER_SHORT "She got tired of your limp leadership and found a real party!"
    "Arguments erupted among the adventurers, only silenced by the guard's roar."
    show cg_guard at shake
    GUARD "SILENCE!!"
    "The hall fell into a tense hush as all eyes turned toward the guard."
    show cg_guard at blurin, center_f
    GUARD "Your petty squabbles neither concern the Emperor nor the crown."
    show thea at left with easeinleft
    THEA @sad "Guardsman, why has everyone been summoned under veil of darkness?"
    $ AutoMus(False)
    stop music fadeout 1.0
    GUARD "... War."
    show thea scared
    "The room fell so still, I could hear a coin drop."
    $ PlayMusic("audio/music/13_AbandFort.ogg")
    GUARD "As I speak, reports of a massive Demorai force marching toward Novaras have been confirmed by the Inquisitors."
    GUARD "Emperor Alcott calls upon all available adventurers to abandon their quests and assist in the city's defense."
    GUARD "For the duration of the siege, you will fall under the direct command of Captain Vasaross."
    ADVENTURER_LEAN "Where's Celeste? Shouldn't the Red Arrows be here for this?"
    ADVENTURER_BULKY "Man the walls? The fuck? Isn't that what the guard and army are for?"
    GUARD "Celeste and the Red Arrows are unavailable..."
    GUARD "They were sent on a vital mission before the report was confirmed and won't be able to return in time."
    GUARD "I remind you all: your position as 'adventurers' grants you great freedom and privilege in Alderay."
    GUARD "Yet, as per your contracts, that freedom is revoked in times of crisis."
    EXPERIENCED_ADVENTURER "What exactly are we walking into?"
    EXPERIENCED_ADVENTURER "The Demorai have tried to siege the city before and failed. Why is this different?"
    GUARD "... This time is different."
    GUARD "To be blunt-this Demorai force is larger than that the city have faced during the Great Siege."
    GUARD "Emperor Alcott refuses to take any chances."
    GUARD "The city will enter lockdown after the official announcement tomorrow."
    GUARD "No one may leave or enter until the siege is lifted, with every able man and woman assigned into a temporary support role as either supply runners, milita, or helping tend to the wounded."
    GUARD "The Emperor expects your cooperation in maintaining order."
    GUARD "We cannot afford riots."
    show cg_guard at blurin, center
    ADVENTURER_REDHEAD "Since when the hell have we ever managed crowd control?"
    "As the guild erupted with protests and demands for answers, I could see the guard's patience wearing thin."
    GUARD "... I'm going to say this once, and only once."
    GUARD "Assisting with the city's defense is not optional."
    GUARD "Refusal... {i}is treason.{/i}"
    GUARD "If you attempt to flee tonight, you will be branded a traitor and stripped of your adventurer status."
    MC @talk "How long until the Demorai arrive?"
    GUARD "... Ten days."
    $ QstStart(QstTheComingStorm)
    GUARD "Return to the guild tomorrow for your assigned positions along the walls."
    hide cg_guard with easeoutright
    "The guild exploded into chaos once more, but the guard ignored the shouting and simply left."
    show thea scared at blurin, left_f
    $ Pause(0.1)
    hide thea with easeoutleft
    $ Pause(0.1)
    show mc at center_f with easeinright
    "As the arguments continued, I felt a hand on my shoulder."
    show markus at cright_f with easeinright
    MARKUS @talk "Let's go."
    hide mc with easeoutleft
    hide markus with easeoutleft
    scene black with dissolve
    
    $ LocSet("novaras_dist_market")
    $ AutoMus(True)
    $ LocFlush()
    
    show mc at cleft
    show markus at cright_f
    with dissolve
    MARKUS @talk "We need to leave."
    MARKUS @talk "Head to Hamun, find a boat—"
    MC @angry "We can't just abandon the city!"
    MC @angry "What about everyone here? Our friends?"
    MARKUS @angry "You and I both know something else is going on with this invasion."
    MARKUS @angry "They wouldn't try again without a plan."
    MC @angry "Then we find out what it is and stop it!"
    MC @angry "You want to live as criminals?"
    MC @angry "You want to abandon everyone we care about?"
    MARKUS @think "T-They can come with us!"
    MARKUS @angry "We gather them tonight, before the lockdown, and leave!"
    MC @angry "And how do you propose we do that?"
    MC @angry "Most of them wouldn't even get permission to leave Novaras on such short notice."
    MC @angry "And they'd still have to trek for DAYS to the Free City!"
    MARKUS @angry "Then let them stay here!"
    MARKUS @angry "With all the adventurers and guards, they'll be fine!"
    MC @angry "You just said you wanted to flee because things WON'T be fine!"
    MARKUS @fury "DAMN IT!"
    "Markus stomped, dragging a hand through his golden hair, his frustration boiling over."
    MARKUS @angry "... Fine, we stay in the damn city."
    MARKUS @angry "I just pray neither of us is right and that this siege ends swiftly."
    MC @sad "... I hope that too, Markus."
    MC @sad "I really do."
    show markus at blurin, cright
    MARKUS @sad "I'm going to warn some close friends."
    MARKUS @sad "You should do the same."
    hide markus with easeoutright
    $ Pause(0.1)
    show mc at center with ease
    MC "(Adara... I need to warn Adara.)"
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("adara_house_living_room")
    $ Pause(0.5)
    play sound "audio/cfx/door_knock.ogg"
    $ LocFlush()
    show adara shock at cright
    with dissolve
    ADARA @shock "[player_name!t]?"
    show mc at cleft_f with easeinright
    $ Pause(0.1)
    show adara shock at blurin, cright_f
    ADARA @talk "It's late... What's the matter?"
    show mc at blurin, cleft
    MC @talk "Adara, you need to listen to me."
    MC @talk "The city's about to be locked down in preparation for a siege."
    ADARA @shock "What?!"
    ADARA @shock "What are you talking about?"
    menu:
        "Adara, wake your father and head straight to Newyark tonight":
            ADARA @shock "Newyark? That would take weeks on foot!"
            ADARA @shock "And I don't have the coin for a horse and cart!"
            menu:
                # if this choice is taken, adara and her father survive
                "Take my coin and go, Adara... Please. Don't wait for the announcement in the morning." (Req_Gold = 1000):
                    $ QstTheComingStorm().GaveAdaraMoneyForEscape = True
                    $ PlayerRemItem("gold", 1000)
                    ADARA @shock "[player_name!t], you're scaring me..."
                    MC @sad "I know, Adara, but you have to trust me!"
                    MC @serious "Go—go now!"
                    MC @serious "Get your father and use that coin while you still can."
                    MC @serious "{i}Do not return to Novaras until you know it's safe.{/i}"
                    ADARA @cry "But... What about you?"
                    MC @sad "I'll be fine... Just go."
                    MC @sad "Go now!"
                    ADARA @sad "Then come with me! Gather the ones you care about, and we'll all leave tonight!"
                    MC @sad "I can't, Adara. They won't let any adventurers leave the city."
                    MC @sad "... But I can't be worrying about you when the battle starts."
                    pass

                # if this choice is taken, adara survives, her father doesnt
                "Damn it all! Board up your house, gather what food you can... and get a blade.":
                    $ QstTheComingStorm().GaveAdaraMoneyForEscape = False
                    ADARA @shock "B-Board up the house?"
                    ADARA @shock "Are we not going to be okay?"
                    ADARA @shock "The army has handled sieges before!"
                    MC @serious "Adara, just... listen to me, please."
                    MC @sad "You have to stay safe... I have to know you'll be alright."
                    pass

        # if this choice is taken, adara survives, her father doesnt
        "Listen to me, board up your house, gather what food you can... and get a blade.":
            $ QstTheComingStorm().GaveAdaraMoneyForEscape = False
            ADARA @shock "B-But... I don't understand."
            ADARA @shock "How do you know all this?"
            MC @serious "Adara, just... listen to me, please."
            MC @angry "Gather what you can and stay safe."
            MC @serious "I mean it, Adara."
            MC @sad "You have to stay safe... I need to know you'll be alright."
            pass

    # ALL choices continue here
    ADARA @cry "[player_name!t]..."
    MC @sad "Adara, please—"
    show adara cry at center_f with ease
    "Adara threw herself into my arms, sobbing."
    ADARA "... We should have left that day you came back."
    ADARA "We should have sailed far away from all of this."
    "Adara pulled back, looking into my eyes."
    ADARA "..."
    MC "Adara... What are you saying?"

    $ AutoMus(False)
    $ PlayMusic("audio/music/47_Bubbles.ogg")
    scene cg_adara_on_top with flash
    $ Pause()
    "Suddenly, Adara threw herself forward, knocking me back onto the floor as she pinned me down."
    MC "Adara!"
    "She clung to me tightly before gently tilting her head towards mine."
    ADARA "{i}... I love you.{/i}"
    "My pulse pounded in my ears." 
    ADARA "I've always loved you, [player_name!t]."
    "I said nothing, gently brushing her hair back."

    scene cg_adara_kissing with dissolve
    $ Pause()

    "And then, Adara's lips pressed against mine..."
    MC "... Adara."
    MC "I—"
    ADARA "Don't say it."
    ADARA "Don't give me your answer yet."
    ADARA "Just come back to me."
    ADARA "{i}Please...{/i}"

    scene black with dissolve
    $ TimeAdvTo(TIME_NOON)
    $ AutoMus(True)

    "... As morning light crept over the horizon, city guards began knocking on every house and shop door, directing people towards the royal palace."
    $ LocSet("novaras_dist_centre")
    "By now, most of Novaras had heard the rumors—whispers of the impending Demorai force marching ever closer to the city's walls."
    "A great unease hung in the air as thousands of people flooded the streets, murmuring anxiously, speculating... afraid."
    $ LocFlush()
    show cg_guard at cleft
    with dissolve
    show mc at cright_f with easeinright

    GUARD "Keep moving, citizens!"
    GUARD "An announcement will be held at the royal palace!"
    hide cg_guard with easeoutright
    show mc at cleft_f with ease
    "As the sea of people pressed forward, a familiar voice cut through the noise."
    MARKUS "[player_name!t]! [player_name!t]!"
    show mc at blurin, cleft
    "I turned to see Markus shoving his way through the crowd, his face strained with urgency."
    show markus at cright_f with easeinright
    MC "Markus."
    MARKUS "Did you manage to warn Regina or anyone?"
    MC "[regina_ref!t] didn't come home last night, and I have no idea where Erika even is."
    "Markus nodded in acknowledgment, but beneath his neutral expression, anxiety loomed like a shadow."
    MARKUS @angry "... Maybe we'll be lucky."
    MARKUS @angry "Maybe the Demorai aren't planning a siege after all."
    show mc at blurin, cleft_f
    $ Pause(0.1)
    hide mc with easeoutleft
    hide markus with easeoutleft
    "Neither of us truly believed that."
    "But clinging to hope, however fragile, was better than nothing."
    "Finally, we spilled out into the great courtyard of the Royal Palace, where a loud trumpet blast silenced the restless crowd."
    "Above us, standing on a grand balcony, Emperor Alcott emerged."
    $ AutoAmb(False)
    $ AutoMus(False)
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    $ PlayMusic("audio/music/45_Looming_Dusk.ogg")
    show alcott at center_f with dissolve
    "For but a moment, there was only silence."    
    "A held breath. A city waiting."
    ALCOTT "... CITIZENS OF NOVARAS!"
    ALCOTT "I COME TO YOU NOW IN AN HOUR OF GREAT NEED."
    "The crowd murmured amongst themselves, voices heavy with unease, before gradually falling silent again as the Emperor continued."
    ALCOTT "The rumors you have all heard are true."
    ALCOTT "The Demorai march against us once more."
    ALCOTT "In TEN days, their horde will reach our gates."
    "Panic spread like wildfire."
    play sound "audio/cfx/crowd_panic.ogg"
    "Fearful voices rose in a cacophony of confusion, only to be silenced once more by the Emperor's commanding voice."
    show alcott at shake
    ALCOTT "FEAR NOT!"
    ALCOTT "Even as I speak, our armies stand ready to defend these walls and drive back their foul scourge!"
    stop sound fadeout 5.0
    ALCOTT "The city is more fortified than ever before..."
    ALCOTT "AND ITS WALLS SHALL NEVER FALL!"
    play sound "audio/cfx/crowd_cheer.ogg"
    "A hesitant cheer rippled through the crowd, growing louder as the mood shifted, though unease still lingered beneath the surface."
    "A merchant clutched his ledger, muttering prayers under his breath, as a woman tightened her hold on her child, her knuckles pale as she swallowed her fear."
    ALCOTT "All able-bodied men will be assigned temporary roles in manning the city's defenses!"
    ALCOTT "Women must secure their homes and tend to their children."
    ALCOTT "Those without children are to assist the mages of Palam in tending to the wounded!"
    ALCOTT "Rest assured—we are prepared!"
    ALCOTT "We are ready!"
    ALCOTT "Their horde was pushed back once before,"
    ALCOTT "AND THEY SHALL TASTE OUR STEEL AS THEY ARE DRIVEN BACK AGAIN!"
    play sound "audio/cfx/crowd_cheer.ogg"
    hide alcott with dissolve
    scene black with dissolve
    play sound2 "audio/cfx/army_aye.ogg"
    "The growing roar of approval mixed with the rhythmic marching of the city guards as they paraded through the streets."
    "Even as I watched the spectacle, I felt an unsettling chill creep up my spine."
    $ LocFlush()
    show mc at cleft
    with dissolve
    MC "(It's almost reassuring to see so many guards ready like this, but...)"
    MC "(I can't shake the feeling that something terrible is about to happen.)"
    BLACK "({i}They seek to appear strong... as all weak things do.{/i})"
    MC "(What do you mean?)"
    BLACK "({i}Can you not feel it?{/i})"
    BLACK "({i}The fear radiating from them... all is not well here.{/i})"
    MC "(I need to think carefully about my next steps.)"
    MC "(There isn't much time left.)"
    hide mc with easeoutright
    $ Pause(0.1)
    show alcott at center_f with dissolve
    ALCOTT "In the coming days, expect further announcements as our defenses continue to be reinforced!"
    ALCOTT "This darkness shall pass as it always has."
    ALCOTT "ALDERAY SHALL STAND UNBROKEN, AS IT ALWAYS HAS BEFORE!"
    play sound "audio/cfx/crowd_cheer.ogg"
    scene black with dissolve
    $ QstTheComingStorm().ShowAndSpinCountdown = True
    $ AutoAmb(True)
    $ TimeAdvBy(TIME_1H)
    
    # hax
    $ tmpvar = copy.copy(LocIDList_NovarasCityStreets)
    $ tmpvar.remove("novaras_dist_centre")
    $ LocSet(renpy.random.choice(tmpvar))

    $ LocFlush()
    with dissolve

    $ Pause(0.5)
    show mc at center with easeinleft
    "... Wandering through the streets of Novaras, I noticed dozens of notices nailed to doors and walls."
    show mc at nod
    "I pulled one free and read it."
    "{i}ALL CITIZENS ARE FORBIDDEN FROM LEAVING NOVARAS WITHOUT AN OFFICIAL PERMIT, EFFECTIVE IMMEDIATELY. BY ORDER OF THE EMPEROR.{/i}"
    MC "(Fuck... Looks like I'm not getting out of the city anytime soon.)"
    "Kiara's voice echoed in my skull, colder than the morning air as she repeated her dire warning of the horrors to come."
    MC @surprised "(There isn't much time... If Kiara is telling the truth, I need to warn someone and prepare for what's coming!)"
    MC "(Maybe Captain Nyx?)"

    $ GoalShow(QstTheComingStorm, 10)
    $ InfGainDaily(True)
    $ AutoMus(True)
    hide mc with easeoutright
    $ LocEnter()


###################################################
label qst_thecomingstorm_route1_talktonyx_firsttime:
    NYX @think "Yes? What is it?"
    MC @talk "We need to talk about the siege... The Demorai are planning something."
    show nyx think
    NYX @think "Planning something?"
    NYX @think "What are you talking about?"
    MC @angry "This siege... there's more to it than just an attack on the walls!"
    MC @serious "{i}They have something planned...{/i}"
    $ GoalComplete(QstTheComingStorm, 10)
    NYX @think "We've known about the siege for months."
    NYX @think "I've received no reports of unusual troop movements."

    menu qst_thecomingstorm_route1_talktonyx_firsttime_menu:
        "You've known for over two months and said nothing?":
            NYX @sad "I'm sorry, [player_name!t], I was sworn to secrecy."
            NYX @sad "We were trying to avoid mass panic and food hoarding."
            NYX @talk "Many peasants are being called to assist in defending the walls or supplying the defenders."
            jump qst_thecomingstorm_route1_talktonyx_firsttime_menu

        "Not evacuating the city is a mistake...":
            NYX @sad "The Demorai are advancing too fast—we can't afford to escort a mass exodus through open fields."
            NYX @sad "Besides... we {i}need{/i} the extra manpower to reinforce the walls."
            MC @angry "So what, we're just leaving them as glorified bait?!"
            MC @angry "If the walls fall—where do they run?!"
            NYX @angry "DAMN IT, [player_name!t]!"
            "Nyx's fist slammed onto the desk, sending loose papers scattering. Half-finished defense plans and supply reports lay sprawled beneath her hands."
            NYX @think "This city is the best-defended place in Alderay."
            NYX @think "If we can't hold the line here—nowhere else will."
            jump qst_thecomingstorm_route1_talktonyx_firsttime_menu

        "I only know there is some wicked plan in motion...":
            pass

    NYX @think "What exactly are you saying?"
    MC @talk "A girl... A scout who died during my expedition appeared to me."
    NYX @shock "...A dead girl spoke to you?"
    show nyx think at shake
    NYX @think "Have you lost your mind?"
    MC @angry "I know how it sounds, damn it!"
    MC @angry "She came bearing a warning—the Demorai are moving unseen pieces into place!"
    MC @angry "This siege isn't what it seems!"
    MC @angry "They're making it look like it's just going to be a frontal assault but there's more to it!"
    MC @angry "I KNOW it!"
    NYX @angry "{i}Do you have any proof?{/i}"
    MC @think "Not yet."
    NYX @think "Then find some."
    NYX @think "If what you say is true, I need evidence before I can act."
    MC "(Shit.)"
    NYX @talk "But while you're here... I need you to look into something for me."
    NYX @talk "A group of my men, led by Sergeant Poltrik, vanished after investigating some traders who entered the city not long ago."
    NYX @think "We haven't heard from them in {i}over a month.{/i}"
    MC @serious "And you think they were targeted?"
    NYX @think "I {i}know{/i} they were."
    NYX @think "Poltrik was thorough—he wouldn't just disappear."
    NYX @talk "His last report said the traders' paperwork was a forgery. But before he could follow up, he and his men were gone."
    menu qst_thecomingstorm_route1_talktonyx_firsttime_menu2:
        "What were they investigating?":
            NYX @think "There have been strange reports about these traders."
            NYX @think "Apparently, the food they brought with them was already rotting."
            NYX @talk "They were let in because their paperwork checked out, but an officer flagged it as suspicious."
            NYX @think "When I looked closer, I realized the paperwork was a forgery."
            NYX @think "I sent my men, including Sergeant Poltrik, to track the traders, but none of them returned."
            jump qst_thecomingstorm_route1_talktonyx_firsttime_menu2

        "Is this really the time for this? The city is about to be sieged!":
            NYX @shock "That depends... Is the risk of a plague spreading through Novaras {i}during a siege{/i} worth ignoring?"
            NYX @shock "Or what if it's not disease, but explosives? Or something worse?"
            NYX @angry "Even if it's just smuggled contraband, I can't let gangs use this crisis to their advantage."
            jump qst_thecomingstorm_route1_talktonyx_firsttime_menu2

        "I'll look into it… and hope I find you the proof you need.":
            NYX @sad "{i}*Sigh*{/i} Without proof, I can't pull guards from the wall."
            NYX @sad "Let's pray your {i}'source'{/i} is wrong."
            MC @talk "Where were your men last seen?"
            NYX @talk "Sergeant Poltrik and his men were last seen questioning the gate guards."
            NYX @think "I'd start there if I were you."
            pass

    $ GoalShow(QstTheComingStorm, 20)
    $ LocEnter()

#####################################################################################################
label qst_thecomingstorm_route1_talk_to_guards_about_poltrik:
    GUARD "Ahh... Yes."
    GUARD "We told the sergeant all we could about those strange traders."
    GUARD "What do you want to know?"
    
    menu qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu1:
        "What can you tell me about the traders?":
            GUARD "They were... strange."
            GUARD "Pale as ghosts, and reeked of something foul."
            GUARD "Said they had come down from Angmurus, talking about a bad season and needing to restock before restarting their trade."
            GUARD "We almost didn't let them in."
            GUARD "But with all the paperwork in order… what were we supposed to do?"
            GUARD "Our kingdoms may be divided, but free trade is still honored."
            menu qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu2:
                "Did you not realize the documents were forged?":
                    GUARD "Of course not!"
                    GUARD "If we had, we'd have told them to sling their hook!"
                    GUARD "The paperwork was flawless—even had the correct wax seal."
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu2

                "What do you mean by pale and reeking of foul odor?":
                    GUARD "Like they hadn't washed in months."
                    GUARD "For a moment, I thought they were undead…"
                    GUARD "But no, they were alive alright."
                    GUARD "Figured they were just deep Northerners. I hear people in Angmurus can go months without washing."
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu2

                "I have more questions.":
                    GUARD "Ask away then..."  
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu1

        "Can you tell me more about their cargo?":
            GUARD "Food, mostly. But a lot of it was already rotting."
            GUARD "They claimed it was a bad season and wanted to restock in Novaras before heading back out."
            GUARD "Strange, but at the time, it didn't seem worth turning them away."
            menu qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu3:
                "Were they carrying any weapons?":
                    GUARD "They had personal blades… but that's nothing unusual."
                    GUARD "No weapons in their cargo."
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu3

                "Any sign of explosives?":
                    GUARD "None that I saw."
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu3

                "Why wasn't the rotten food destroyed?":
                    GUARD "They wanted to use it for compost, said they might be able to make some money back that way."
                    GUARD "Seemed reasonable enough at the time."
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu3

                "I have more questions.":
                    GUARD "Ask away then..."  
                    jump qst_thecomingstorm_route1_talk_to_guards_about_poltrik_menu1

        "Where did Poltrik and his men go?": 
            GUARD "Last I heard, Sergeant Poltrik and his team were heading toward {i}The Iron Unicorn.{/i}"
            GUARD "Maybe they thought the traders went there?"
            $ GoalComplete(QstTheComingStorm, 20)
            MC @talk "I see. Thank you for your help."
            MC "(Looks like my next stop is The Iron Unicorn...)"
            pass

    $ GoalShow(QstTheComingStorm, 30)
    $ LocEnter()

########################################################################
label qst_thecomingstorm_route1_visit_iron_unicorn:
    show mc at left with easeinleft
    "As I stepped into The Iron Unicorn, the atmosphere was tense. The windows were being boarded up, chairs overturned, and tables stacked against the window frames."
    "The tavern, once bustling with life, now felt like a barricaded fortress."
    show shay at center with dissolve
    SHAY @what "Sorry, boys. Service is closed until it's safe."
    menu qst_thecomingstorm_route1_visit_iron_unicorn_menu1:
        "Did Sergeant Poltrik and some city guards come by here recently?":
            SHAY @what "Hm?"
            SHAY @shock "Yes, actually!"
            SHAY @shock "Now that I think about it, I DO remember some guards asking strange questions."
            show shay shock
            MC @talk "What did they want to know?"
            SHAY @talk "They were asking about some traders—deathly looking fellows who wanted a room for the night."
            MC @think "Did you give it to them?"
            SHAY @talk "Well, they paid upfront in coin, so I did."
            SHAY @what "Funny bunch though... Didn't hear a peep from them all night, and by morning, they were gone."
            SHAY @shock "Didn't even stay for breakfast!"
            menu qst_thecomingstorm_route1_visit_iron_unicorn_menu2:
                "Do you know where the traders went?":
                    SHAY @talk "Like I said, I didn't hear from them after they checked in..."
                    SHAY @what "When I woke up, their room was empty."
                    jump qst_thecomingstorm_route1_visit_iron_unicorn_menu2

                "Did Poltrik or the others mention where they might go next?":
                    SHAY @what "Mmm... Not really."
                    SHAY @what "If I were you, though, traders like those... They looked like the type to hang around in {i}less reputable places.{/i}"
                    SHAY @what "Sorry I can't be more help."  
                    $ GoalComplete(QstTheComingStorm, 30)
                    MC "(Damn... Another dead end.)"
                    MC "(Less reputable places, huh?)"
                    pass

        "Where's your husband, Shay?":
            SHAY @shock "He's out gathering supplies for us."
            SHAY @what "Should be back soon... I hope."
            SHAY @shock "Gods, the whole city's in a panic."
            jump qst_thecomingstorm_route1_visit_iron_unicorn_menu1

    $ GoalShow(QstTheComingStorm, 40)
    $ LocEnter()

#################################
label qst_thecomingstorm_route1_talk_carina_refuse:
    CARINA @angry "{i}Before{/i} I start doing you any favors, why don't you prove you're fucking useful first?"
    CARINA @angry "Deal with my request first, and {i}then{/i} we'll talk."
    $ LocEnter()

label qst_thecomingstorm_route1_talk_carina:
    CARINA @think "Missing guards?"
    CARINA @smile "And what? You think they got lost between my girls' legs or something?"
    show carina at blurin, center_f
    $ Pause(0.1)
    show carina at cright_f with ease
    show mc at cleft with easeinleft
    MC @serious "Sergeant Poltrik and his men were ordered by Captain Nyx to investigate some strange traders."
    MC @talk "They've since vanished."
    CARINA @think "Hmm... Interesting."
    $ GoalComplete(QstTheComingStorm, 40)
    CARINA @smile "Well, I could put the word out and try to get some information for you."
    CARINA @smile "{b}...For a price, of course.{/b}"
    MC @angry "I don't have time for your games."
    CARINA @smile "You {i}do{/i} if you want my help."
    MC @think "{i}*Sigh*{/i}"
    MC @talk "What do you want?"
    CARINA @smile "Well... I suppose you have a choice."
    CARINA @smile "But first... Take your clothes off."
    MC @surprised "What?"
    CARINA @smile "Now, now, don't be shy... Chop chop."
    MC "..."
    CARINA @angry "Do you want my help or not?"
    $ CharSetClothes("mc", "naked")
    $ PlaySoundRandom("tentFlap")
    show mc at nod
    "With a roll of my eyes, I stripped off my armor in front of her."
    "Carina, slightly taken aback, blinked before a slow grin spread across her face."
    CARINA @lewd "Oh yes..."
    "She licked her lips before composing herself once more."
    CARINA @lewd "{i}You'll do very nicely.{/i}"
    MC @think "Very nicely for what?"
    CARINA @smile "Your first option is simple... {i}I want you to put on a show.{/i}"
    $ CharSetClothes("mc", "normal")
    $ PlaySoundRandom("tentFlap")
    show mc at nod
    MC @think "A show?"
    CARINA @think "One of my 'bull' talents is up in Newyark for a performance."
    CARINA @talk "As such, I have an open spot I need to fill."
    MC @think "I don't exactly follow... What are you asking me to do?"
    CARINA @angry "{i}*Sigh*{/i} Do you really need it spelled out for you?"
    CARINA @smile "I need you to fuck some of my new talent on stage."
    MC @surprised "I..."
    MC @surprised "You want me to fuck one of your whores on stage?"
    CARINA @smile "See? What a WONDERFUL offer, isn't it?"
    CARINA @smile "Men would kill for such a {i}generous{/i} opportunity."
    MC @think "And my other choices?"
    CARINA @smile "Don't tell me you are into men?"
    CARINA @think "{i}*Sigh*{/i}"
    CARINA @talk "Well... Alternatively, I need help with something."
    CARINA @talk "And it will require getting your hands more than a little dirty."
    MC @think "Go on."
    CARINA @talk "An associate of mine has decided to go rogue."
    CARINA @talk "He's stopped paying tributes and has gone silent on my messengers."
    CARINA @angry "Naturally, I'd just send someone over to 'adjust' his behavior..."
    CARINA @angry "But the stupid bastard hasn't just crossed me—he's intruding on my {i}associates'{/i} territories too."
    CARINA @talk "... And now, {i}I{/i} am expected to deal with him accordingly."
    MC @think "So, you want him dead?"
    "Carina shrugged."
    CARINA @talk "As long as neither I nor my associates ever see him again... the rest is just details."
    CARINA @talk "I leave that to your discretion."
    CARINA @talk "So, which will it be?"
    menu:
        "I'll help you put on your show.":
            CARINA @smile "Of course you will. What man wouldn't?"
            CARINA @smile "Come back tomorrow night—I'll have the girl and your outfit ready."
            menu qst_thecomingstorm_route1_talk_carina_menu1:
                "My outfit?":
                    CARINA @smile "You'll see soon enough."
                    jump qst_thecomingstorm_route1_talk_carina_menu1

                "Who will I be performing with?":
                    CARINA @smile "It'll be one of the newer girls."
                    "Carina grinned coyly."
                    CARINA @lewd "{i}But if there's a choice, I'll let you pick.{/i}"
                    jump qst_thecomingstorm_route1_talk_carina_menu1

                "I'll return tomorrow.":
                    hide mc with dissolve
                    show carina at center_f with ease
                    CARINA @smile "{i}I hope you put on a wonderful show.{/i}"
                    $ GoalShow(QstTheComingStorm, 150)
                    pass

        "I'll deal with your {i}'problem.'{/i}":
            CARINA @think "Really?"
            CARINA @talk "I'm surprised... Most men jump at the first option."
            CARINA @smile "But you're different, aren't you?"
            CARINA @smile "Hmm... Very well."
            CARINA @angry "The bastard's name is Valchek."
            CARINA @angry "He's been lurking around the Market District."
            CARINA @talk "Find him. Deal with him."
            CARINA @talk "Come back when it's done."
            $ GoalShow(QstTheComingStorm, 250)
            pass

    $ LocEnter()


###################################################################################################################################################
# Agreed  to help put on a show continued - player returns tomorrow night,  scene triggers upon entering into brothel Main hall
label qst_thecomingstorm_route1_subr1_sexshow:
    show carina at cright_f
    with dissolve
    show mc at cleft with easeinleft
    CARINA @smile "Ah! There you are!"
    CARINA @smile "Come, come!"
    CARINA @smile "Your outfit is ready..."
    MC "..."
    scene black with dissolve
    "Led into Carina's office, she presented me the outfit with a perverse, smug expression."
    $ LocSet("novaras_bordello_office")
    MC "... Surely you jest?"
    CARINA "Do I look like a woman whose interested in making you laugh?"
    CARINA "Now put it on..."
    $ PlaySoundRandom("tentFlap")
    "With a heavy sigh, I did as Carina asked..." 
    MC "... What in all of the gods am I wearing?" 
    $ LocFlush()
    show cg_mc_bull at cleft
    show carina at cright_f
    with dissolve
    $ Pause()
    CARINA @laugh "Welllll, would you look at that!"
    CARINA @smile "An outfit that finally suits you!"
    menu qst_thecomingstorm_route1_subr1_sexshow_menu1:
        "Want to try ride this 'bull' Carina?":
            CARINA @lewd "Hahaha...!"
            CARINA @smile "Why don't you prove how valuable an asset you are out there first?"
            CARINA @lewd "Then I'll show you just how... rewarding, it can be to work for me."
            jump qst_thecomingstorm_route1_subr1_sexshow_menu1

        "Do people seriously like this sort of thing?":
            CARINA @smile "Why yes, they do."
            CARINA @smile "And they're willing to pay plenty of coin to see it."
            jump qst_thecomingstorm_route1_subr1_sexshow_menu1

        "Who's the girl I'll be with?":
            pass

    CARINA @think "It's interesting you should ask that..."
    CARINA @talk "Originally, I was just going to give Shani, that whore we let hang outside a shot to start earning some real coin."
    CARINA @think "{i}But...{/i}"
    CARINA @think "A mystery girl approached me after you left last night, asking if she could fill in for Shani."
    CARINA @talk "She's a beauty... Sadly though, it seems she has no interest working here other than having a chance to play with {i}you.{/i}"
    CARINA @smile "Have any slightly obsessed lovers running around you want to tell me about?"
    MC "What's her name?"
    CARINA @think "She wouldn't say."
    MC "What did she look like?"
    CARINA @talk "She hid her face behind a mask, but..."
    CARINA @talk "Her body is quite exquisite."
    CARINA @think "Anyway, I said I'd leave the choice with you."
    CARINA @smile "So, what will it be?"
    CARINA @talk "Shani... Or the mystery girl?"
    menu:
        "I'll put on a show with the mystery girl":
            $ QstTheComingStorm().SexShowChoice = "regina"
            jump qst_thecomingstorm_route1_subr1_sexshow_regina

        "I'll put on a show with Shani":
            $ QstTheComingStorm().SexShowChoice = "shani"
            jump qst_thecomingstorm_route1_subr1_sexshow_shani

label qst_thecomingstorm_route1_subr1_sexshow_regina:
    CARINA @smile "I was hoping you would say that."
    "Carina chuckled to herself."
    CARINA @smile "This is going to be fun..."
    scene black with dissolve
    $ LocSet("novaras_bordello_interior")
    $ LocFlush()
    show cg_mc_bull at cleft
    show carina at cright_f
    with dissolve
    show cg_regina_masked at right_f with easeinright
    CARINA @smile "And here she is."
    UNKNOWN "I'm glad that you picked me."
    MC "You seem familar... Yet I can't quite put my finger on who you are."
    BLACK "({i}Her scent is familar... Yet... It is as though it is masked.{/i})"
    MC "(Masked?)"
    show cg_regina_masked at center_f with easeinright
    UNKNOWN "I'm simply someone with your best interests at heart."
    MC "What does that-"
    CARINA @angry "Enough talking!"
    CARINA @smile "The audience is waiting."
    CARINA @smile "Now follow me both!"
    scene black with dissolve
    "Led out toward the stage, the crowd cheered and applauded as the two of us emerged from behind the curtain."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "In a moment, the beautiful, alluring woman knelt down, presenting her huge breasts toward me as she smirked knowingly."
    UNKNOWN "Let's give them something they won't forget, {i}dear.{/i}"
    MC "(Dear?)"
    MC "(That sounds like something—)"
    "Before I could finish the thought, I felt my huge, hard cock pressed between her soft, massive tits as she began to massage my shaft."

    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    scene regina_sex_show_loop_tj_slow with dissolve
    $ Pause()

    "I let out a hot groan as the woman chuckled beneath her breath."
    UNKNOWN "You liked that, didn't you?"
    "I didn't answer. Her creamy, glistening breasts squeezed, pushed, and even slapped against my cock."
    "Her intense eyes beneath the mask never left mine, and I could {i}feel{/i} her gaze piercing through the bull head I wore."
    "Glancing at the crowd—enthralled by the lewd performance—I forced myself to focus on the act rather than be completely overtaken by her touch."
    MC "Have you ever seen a cock this good, slut?"
    "The woman grinned and raised her voice just enough for the audience to hear her coy response."
    UNKNOWN "Mmm, never, my lord!"
    UNKNOWN "If only my husband was as big as you!"
    UNKNOWN "I'd drain these huge balls every night!"
    "The crowd whistled and cheered as she continued working my cock with her breasts,"
    "Gliding them back and forth with practiced precision, determined to milk me dry."
    "Every twitch of mine, every involuntary gasp, seemed to thrill her."
    "The audience watched from the sidelines like hungry dogs as she coated my cock in whatever sticky fluid she'd slathered on herself."
    "Glistening under the candlelight, the soft pressure of her tits squeezing me was intoxicating."
    "I wanted her to keep going... but I knew the crowd would grow impatient for more."
    "Dragging her forward, I grabbed her by the hair, pulling her into place. She let me manhandle her freely, still wearing that wicked smile as she kissed the head of my cock."
    MC "Fuck your husband, whore!"
    MC "Put those lips around my cock and worship me!"
    "She chuckled again, her hypnotic, mask-framed eyes locking onto mine."
    UNKNOWN "Whatever you wish, {i}master.{/i}"
    UNKNOWN "I'll be a doting wife to that fool by day, and your perfect little whore at night—just keep feeding me that wonderful cock!"
    MC "(That voice... Why is it so familiar?)"
    "The crowd roared with excitement, chanting and whistling as the raven-haired vixen slowly leaned in."
    "Gently, she wrapped her lips around the head, stretching them as she began to suck me in."
    "I shuddered as the warmth of her mouth enveloped me."

    $ PlaySexFx("audio/sex_sounds/ves69_125.ogg", 1)
    scene regina_sex_show_loop_bj_slow with dissolve
    $ Pause()

    "Inch by inch, she took me deeper, her tongue thrashing and swirling over the most sensitive spots."
    "My balls tightened as loud, lewd slurps echoed through the room."
    UNKNOWN "Mhmm... {i}*Slurp*{/i}"
    "The crowd continued to cheer her on. Her eyes stayed fixed on mine—unblinking, intense, like a predator watching prey."
    "Her lips glided smoothly, coating my cock in saliva, her hands pressing her large tits back up against the shaft with each bob."
    MC "A-Ahh...!"
    MC "Your husband's a fool for—Mmfghh!"
    MC "Letting you wander around so freely!"
    "Her expression didn't change, but I could feel it—my words were getting to her."
    "Her tongue worked even faster, swirling, flicking, drawing me in."
    MC "H-Hrghh! Fuck!"
    "The crowd, catching on to my struggle to hold back, began chanting, drunk on lust and spectacle."
    "{i}TAME THE BULL! TAME THE BULL! TAME THE BULL!{/i}"
    "I looked down again, still buried in her throat, and from the slight curve of her lips, I realized—"
    "She was teasing me the whole time."
    "Suddenly, her tongue thrashed wildly as she sucked harder, a strange glint flickering in her eyes."
    "The sudden shift in rhythm was too much. She knew exactly what she was doing."
    "My cock throbbed violently in her mouth. Her gaze didn't waver."
    "She stared up at me like she'd just pulled the final thread of a trap I hadn't even known I'd stepped into."
    "I grunted loud and deep, unable to hold back as I erupted into her mouth."
    MC "H-HRGHHHH...!"

    $ ReduceInfectionFromSex("regina")
    $ UnlockGalSceneAndGrantXp("regina", "sex_show")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene regina_sex_show_finish1 with flash
    $ Pause()

    "As my thick seed flooded her throat, her cheeks puffed from the volume."
    "But without a single flinch, she began to swallow—mouthful after mouthful—her expression calm, almost smug."

    scene regina_sex_show_finish2 with dissolve
    $ Pause()

    "Her tongue swirled around my shaft, gathering every last trace of cum, as if she were savoring the taste."
    MC "{i}*Huff! Huff!*{/i} G-Gods, woman!"
    MC "There's nothing left to swallow!"
    "The crowd roared in perverted delight."
    "Girls waiting in the wings drifted in toward the dazed, aroused men in the audience, linking arms and fluttering their lashes."
    "The men didn't protest—happily led off to be thoroughly relieved of their coin for the night after that performance."
    "As the crowd finally began to dissipate, the masked woman slowly, sensually, dragged her lips off my cock."
    "With a wet {i}*plop*{/i}, I was free—her mouth now vacant as she rose to her feet."
    UNKNOWN "How delicious... I look forward to next time."

    scene black with dissolve
    $ Pause(0.1)
    $ AutoMus(True)
    $ LocFlush()
    show cg_mc_bull at cleft
    show cg_regina_masked at cright
    with dissolve

    MC "Next time?"
    MC "Who are—"

    CARINA "There you are!"

    show cg_mc_bull at blurin, cleft_f

    $ Pause(0.1)

    hide cg_regina_masked with easeoutright

    show cg_mc_bull at cright_f with ease
    show carina at cleft with easeinleft

    CARINA @smile "What a wonderful show! The crowd looked like they were possessed!"
    CARINA @think "Have you seen where that beauty went? I have a {i}very{/i} lucrative offer I'd like to make her!"
    MC "What are you talking about? She's right-"

    show cg_mc_bull at blurin, cright
    MC "Wait, she was just here a moment ago!" 
    show cg_mc_bull at blurin, cright_f
    CARINA @think "Hmm... Shame."
    CARINA @think "Well if you see her, send her my way at once!"
    jump qst_thecomingstorm_route1_subr1_sexshow_conclusion

label qst_thecomingstorm_route1_subr1_sexshow_shani:
    CARINA @smile "Very well, I'll let Shani know."
    CARINA @talk "Wait here a moment..."
    scene black with dissolve
    $ LocSet("novaras_bordello_interior")
    $ LocFlush()
    show cg_mc_bull at cleft
    show carina at cright_f
    with dissolve
    show cg_shani_bdsm at right_f with easeinright
    SHANI @smile "So you'll be the one I'm-"
    SHANI @shock "FUCK!"
    SHANI @smile "That's a huge piece of meat dangling between your legs!"
    SHANI @talk "Almost reminds me of..." 
    if DialogueShani().paidAmount != 0:
        SHANI @think "Say, don't I know you from somewhere?"
        CARINA @angry "Talk later, fuck now!"
        CARINA @talk "Now follow me you two."
    else:
        CARINA @talk "Okay, follow me you two."
    CARINA @smile "Your audience awaits!"
    scene black with dissolve
    "Led out onto the stage, the crowd roared and cheered as Shani, blindfolded and wearing nothing but leather straps, waited eagerly for me to approach."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "As she heard my footsteps creak across the wooden floor, she tilted her head toward the sound—anticipating what was to come."
    SHANI "H-Hello, my name's—"
    "A sharp slap to her ass cut her off."
    scene shani_sexshow_out_slow 
    with dissolve
    $ Pause()
    "She gasped as the fat rippled, the crowd whistling and cheering in delight."
    "Biting her lower lip, Shani raised her bound hands and bent forward."
    "Her bare asshole and already wet, glistening womanhood practically begged me to get closer."
    SHANI "Y-You're not much of a talker? H-Huh?"
    SHANI "T-This is my first time on the s-stage, so—"

    "With a thud, my heavy cock pressed between her ass cheeks, rubbing slowly against her skin. She let out a nervous whimper."
    SHANI "G-Gods!"
    scene shani_sexshow_out_fast
    with dissolve
    $ Pause()
    "Gently, I pulled at the lead around her neck as I rubbed my shaft across her soft, pale ass."
    "The crowd erupted in cheers, marveling with perverse awe at the size of what she was about to take."
    SHANI "Y-You're huge!"
    "Shani gulped but wiggled her hips enticingly, pleading softly from below."
    SHANI "S-Start easy, alright?"
    SHANI "I don't wanna pass out before we give the crowd a good show!"
    "Staring down at her tight, eager holes... the only question was: which one to take?"
    menu:
        "Fuck her pussy":
            jump qst_thecomingstorm_route1_subr1_sexshow_shani_vag
        "Fuck her ass":
            jump qst_thecomingstorm_route1_subr1_sexshow_shani_anal

label qst_thecomingstorm_route1_subr1_sexshow_shani_vag:
    scene shani_sexshow_vag_slow 
    with dissolve
    $ Pause()
    "Not wanting to push Shani too far, I aligned the head of my cock with her hot, dripping slit and gently pushed in."
    "She let out a hot moan as I slid in inch by inch, slowly sinking into her tight body."
    SHANI "M-Mhhfhh...!"
    "Her cunt tightened involuntarily as her legs began to shake from the stretch and fullness."
    SHANI "G-Gahhhh! It j-just keeps—Mhfhh! G-Going!"
    "The crowd clapped and cheered with perverse delight as I began to fuck her for their entertainment."
    SHANI "Ahh! Yes! Mhfhh! AH!"
    "Her tits bounced with every thrust, and she groaned hotly, trying to push her hips back to meet my rhythm."
    SHANI "H-Hmmfghh! Are you all—Ahh!—watching?"
    SHANI "G-Gods! It's like being fucked by a horse!"
    "The crowd jeered and howled, shouting obscenities and praise as I took her harder."
    "But as she squeezed tighter around me, I started focusing less on their hungry eyes, and more on the primal feeling surging through me."
    scene shani_sexshow_vag_fast 
    with dissolve
    $ Pause()
    "Yanking on the lead, I slammed into her faster, watching her ass ripple with every impact."
    SHANI "F-FUCKKK!!"
    "The wet slap of flesh filled the hall, even louder than the crowd's cheers."
    "Her cries only stoked the dark, burning need inside me."
    "I wanted to breed her—mark her—own her completely in front of everyone watching."
    "The thought of filling her hot womb, making her carry my child, pulsed in my mind."
    BLACK "{i}(Breed her.){/i}"
    BLACK "{i}(The hive must grow.){/i}"
    BLACK "{i}(Breed her... make her sire strong young for us.){/i}"
    "I tried to shake the dark voice away—but it clawed at the edge of my thoughts."
    "No doubt she had taken some Red Moon herbs before this, but still, I—"
    SHANI "H-Harder! Don't—Mhhfh!—stop!"
    SHANI "F-Fuck me!"
    SHANI "SHOW THEM HOW YOU FUCK ME!"
    "Her cries spurred me on. Her body shook under the force, sweat pouring from her skin as I drove her further over the edge."
    SHANI "FUCK ME! FUCK ME—HRGHH! MORE!"
    SHANI "D-Don't you dare—Ahhh!—stop!"
    "Suddenly, I choked up on the lead. Her pussy clamped down hard as she gasped and shuddered, teetering on the edge of pleasure and unconsciousness."
    SHANI "M-Mmmfghhhhhh...! ❤️"
    "The crowd roared, throwing coins onto the stage as I felt my own balls swell—ready to flood Shani's womb to the brim."
    "By now, she was a moaning mess—grunting incoherently between each wet slap as I used her like a toy."
    "Grunting like an animal, I gave one last sharp tug on her head and buried my cock deep in her soaking cunt."
    "Her mouth flew open, tongue rolling out, saliva drooling as she let out a strangled, choked gasp."
    "Buried to the hilt, I groaned loudly as I squeezed her soft ass, flooding her with my heavy, thick load."
    ### finish here
    $ UnlockGalFlag("shani", "sexshow", "var_vag")
    $ UnlockGalSceneAndGrantXp("shani", "sexshow")
    $ ReduceInfectionFromSex("shani")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene shani_sexshow_vag_finish
    with dissolve
    $ Pause()
    MC "H-HRGHHHHH...!" 
    "Her body went rigid as she felt the rush of hot seed pour into her, tiny gasps of overwhelmed bliss escaping her parted lips as the crowd leaned in, captivated."
    SHANI "S-Shooo... M-Mhuchh!!"
    "With a few gentle thrusts, I made sure every last drop was deposited inside her."
    "As I slowly pulled out, Shani collapsed to the floor."
    "The crowd howled with excitement as I gave her ass a final slap—my cum spilling from her well-used hole."
    scene black with dissolve
    "With more coin tossed than one could carry, the audience finally began to disperse."
    $ LocFlush()
    show cg_shani_bdsm at right_f
    show cg_mc_bull at cright_f
    with dissolve
    show carina at cleft with easeinleft
    CARINA @smile "What a wonderful performance!"
    "Carina, clapping gleefully, stepped onto the stage."
    CARINA @smile "To think—I never knew the girl had it in her!"
    CARINA @smile "With that much cum though, I wonder if the Red Moon will be able to hold?"
    "She tilted her head, pondering the thought as she glanced at the limp, twitching Shani—then smirked and shrugged."
    show cg_shani_bdsm at blurin, right
    $ Pause(0.10)
    hide cg_shani_bdsm with easeoutright
    CARINA @smile "Ah well... Some clients are into that sort of thing, you know!"
    jump qst_thecomingstorm_route1_subr1_sexshow_conclusion

label qst_thecomingstorm_route1_subr1_sexshow_shani_anal:
    scene shani_sexshow_anal_slow
    with dissolve
    $ Pause()
    "I knew what this ass could take—and I wanted to put on a show so fierce, Carina wouldn't dare argue I could've done better."
    "Carefully, I aligned my cock with Shani's tight, dark rosebud."
    "As she felt the head of my cock press against her forbidden hole, she gasped, clenching up slightly as she tilted her head over her shoulder to look back at me."
    SHANI "W-Wait! That's my—"
    "Her ass opened, spreading wide as the first inch sank in."
    "She gasped, her mouth falling open as a guttural sound tore from her throat."
    "The crowd roared as I slowly pushed a few inches into her tight ass."
    SHANI "A-ASSSH!"
    "Shani clenched hard around me, her hands balling into fists."
    "Gently, I began pounding her stretched ring, her gasps caught between shock and discomfort as my cock widened her from the inside."
    SHANI "G-Give me—ahh!—a moment to—"
    SHANI "ADJUST! HRGHH!"
    SHANI "You big fucking bastard!"
    "She caught her breath as I gently tugged the lead around her neck. Her breathing came hard and fast, her body tense—"
    "But slowly, surely, she began to push her ass back onto me, the initial shock beginning to fade."
    SHANI "Ah... Ahhh!"
    SHANI "T-That's it... Nghh!"
    SHANI "Let me—{i}*Huff*{/i}—get used to that thing in my ass!"
    "Whether the crowd was oblivious or just enjoying her struggle, they kept throwing coin onto the stage."
    "Doing her best to relax, Shani pushed her butt back, taking me deeper."
    "I groaned in pleasure—and she laughed, breathless."
    SHANI "You—{i}*Huff*{/i}—like that, ya big bastard?"
    SHANI "Mhfghh! Putting it in my—ahh!—ass without asking!"
    SHANI "F-Fuck! Nghh! I should—Mhmm..."
    SHANI "B-Beat you alone for that!"
    scene shani_sexshow_anal_fast
    with dissolve
    $ Pause()
    "Despite her words, she was moving faster, taking my cock deeper with every thrust, her moans growing hotter and more frustrated."
    SHANI "D-Don't—Mhmm!—drag this out!"
    SHANI "My ass is—ahh!—already on fire!"
    SHANI "H-Hurry up! Go faster and finish in me already!"
    "I did as she begged, slamming into her stretched hole, watching as her legs began to buckle beneath her."
    SHANI "F-FUCKKKK...!"
    "The crowd roared in delight. One voice shouted for me to {i}'destroy her ass,'{/i} another to {i}'fuck the whore good!'{/i}"
    "By now, Shani could only groan and moan, still doing her best to throw her ass back against me through the haze."
    SHANI "Ahh! AHH! AHH!"
    "My balls slapped against her ass, heavy and aching with need."
    "Grunting sharply, I rammed myself all the way in, hilting inside her tight, burning hole."
    "With a final roar, I erupted—flooding Shani's bowels with my thick seed."
    ### finish here
    $ UnlockGalFlag("shani", "sexshow", "var_anal")
    $ UnlockGalSceneAndGrantXp("shani", "sexshow")
    $ ReduceInfectionFromSex("shani")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene shani_sexshow_anal_finish
    with dissolve
    $ Pause()
    MC "G-GRGHHHHHHHH!!"
    "Shani let out a sharp gasp as if the air was knocked from her lungs."
    "Her mouth hung open, trembling in my grasp as I pumped her full of cum."
    SHANI "M-MHYYY ASHHH!"
    SHANI "Y-YHOURHH FLOODING MY A-ASHHH!"
    "The crowd cheered louder, some gasping as her stomach gave a slight bulge from the volume."
    "Once I was done, I slowly unsheathed my cock, watching my load pour out from her stretched hole."
    "Her legs gave out as she collapsed to the floor, dazed and twitching."
    scene black with dissolve
    "With enough coin thrown to fill a barrel, the crowd finally began to dissipate."
    $ LocFlush()
    show cg_shani_bdsm at right_f
    show cg_mc_bull at cright_f
    with dissolve
    show carina at cleft with easeinleft
    "Breathing hard, I gave Shani's ass a soft slap—watching it jiggle as she let out a groggy, content moan."
    CARINA @smile "What a wonderful performance!"
    "Carina clapped her hands with delight as she stepped onto the stage."
    CARINA @smile "To think—I never knew the girl had it in her!"
    CARINA @smile "Though with that much cum, I do wonder how long it'll be before she can sit properly again after {i}that{/i} performance."
    "She glanced down at the unresponsive, softly shivering Shani, then smirked and shrugged."
    show cg_shani_bdsm at blurin, right
    $ Pause(0.10)
    hide cg_shani_bdsm with easeoutright
    CARINA @smile "Well... at least I know her ass can handle some of our {i}bigger{/i} clients now!"
    jump qst_thecomingstorm_route1_subr1_sexshow_conclusion


label qst_thecomingstorm_route1_subr1_sexshow_conclusion:
    $ GoalComplete(QstTheComingStorm, 150)
    show carina at blurin, cleft_f
    $ Pause(0.1)
    show cg_mc_bull at center_f with ease
    "As Carina turned to leave, I reached out and grabbed her hand."
    MC "Hold."
    show carina at blurin, cleft
    CARINA @think "Hm?"
    MC "Now it's time for you to keep your end of the deal."
    CARINA @talk "...Ahh, yes. Of course."
    show cg_mc_bull at cright_f with ease
    CARINA @talk "My end."
    CARINA @smile "Give me a month."
    show cg_mc_bull at shake
    MC "What?! I don't have time for—"
    CARINA @talk "And I need time to check my contacts."
    MC "It'll already be too late by then!"
    "She paused, tilting her head as she studied my expression."
    CARINA @think "...Not that I care, but why is finding these men so important to you?"
    MC "The Demorai are planning something... beyond just the siege itself."
    CARINA @think "And you know this because...?"
    MC "It doesn't matter. Let's just say I have a reliable source."
    MC "(At least, I hope they're {i}still{/i} reliable...)"
    CARINA @talk "Hmm..."
    CARINA @talk "Fine then. Give me three days at least."
    CARINA @talk "Even I can't move faster than that."
    MC "Very well. I'll return in three days."
    MC "(Perhaps there's something else I can do in the meantime?)"
    CARINA @talk "Your clothes are in my office, by the way..."
    CARINA @talk "{i}Leave the outfit.{/i}"
    scene black with dissolve
    $ GoalShow(QstTheComingStorm, 300)
    $ QstSetDelay(QstTheComingStorm, 3)
    $ LocEnter()

label qst_thecomingstorm_return_to_carina_in_3_days_early:
    CARINA @talk "Not yet..."
    CARINA @talk "We'll find these guards you're looking for, don't worry."
    CARINA @talk "Soon."
    return

########################################################################################################
# Returning to Carina - 3 Days Later 
label qst_thecomingstorm_return_to_carina_in_3_days:
    show carina at cright_f
    with dissolve
    show mc at cleft with easeinleft
    CARINA @talk "We need to talk."
    $ GoalComplete(QstTheComingStorm, 300)
    MC @think "(I take it she has news...)"
    MC @talk "That bad, huh?"
    CARINA @serious "Yes, and I don't fucking like it one bit."
    MC @talk "What have you found?"
    CARINA @talk "Those guards you're looking for."
    CARINA @talk "They attacked some of my street girls—tried to lure them away."
    CARINA @talk "When they refused? They tried to drag them off."
    MC @surprised "What?!"
    CARINA @talk "They were only stopped because a group of Inquisitors spotted them and intervened."
    MC @surprised "Inquisitors?"
    CARINA @angry "What the fuck are you dragging me into?"
    CARINA @angry "Inquisitors."
    CARINA @angry "Fucking ghouls."
    show mc think
    MC @think "(Ghouls?)"
    MC @talk "...What do you mean?"
    CARINA @think "One of my girls got a look under one of their helmets."
    CARINA @scared "She said his face was rotting. Pale white, sunken in, like a corpse walking."
    MC @think "(Gods...)"
    CARINA @think "If I had to guess? Some kind of plague or sickness. And now, knowing no girl will ever warm their beds again—"
    CARINA @angry "They've decided to take what they want."
    MC @serious "That doesn't sound like a normal disease."
    CARINA @think "No, it fucking doesn't."
    MC @think "(This is worse than I thought...)"
    menu qst_thecomingstorm_return_to_carina_in_3_days_menu1:
        "Why wouldn't they just go to a mage of Palam?":
            CARINA @think "Maybe they can't. Maybe they're afraid of what the mages will find."
            CARINA @talk "Wouldn't be the first time the Mages of Palam refused to treat someone."
            MC @surprised "Really?"
            CARINA @talk "Murderers, rapists... the Mages have the right to refuse service."
            CARINA @think "And if I had to take a guess? Whatever those guards have—it's not just an illness."
            MC "(Nyx is desperate for men, but I doubt even she would knowingly keep something like that in her ranks...)"
            "Carina shrugged, taking a long drag from her pipe."
            CARINA @talk "But hey, just my guess."
            jump qst_thecomingstorm_return_to_carina_in_3_days_menu1

        "Where did they try to drag the girls to?":
            pass

    CARINA @talk "One of them mentioned a property in the south-eastern district."
    MC @think "The noble district?"
    MC @think "How could they be hiding there without anyone noticing?"
    CARINA @think "Hiding in plain sight, maybe?"
    CARINA @talk "There are so many guards patrolling that area, it's probably easy to blend in if they stay in full armor."
    MC @talk "Did the girls say what kind of building it was?"
    CARINA @talk "No. They ran and didn't look back."
    CARINA @think "...Might be worth speaking to Captain Nyx."
    CARINA @think "Maybe Poltrik or one of his men owns property there."
    CARINA @think "Or more likely... has a relative who does."
    MC @serious "That's a good lead."
    MC @talk "Thanks, Carina. I need to move fast."
    show mc at blurin, cleft_f
    $ Pause(0.1)
    hide mc with easeoutleft
    $ Pause(0.1)
    show carina at center with ease
    CARINA @smile "Anytime, {i}darling.{/i}"
    $ GoalShow(QstTheComingStorm, 310)
    $ LocEnter()

#####################################################################################################
#  If the player attempts to head to Captain Nyx's office in the morning, they're blocked.
label qst_thecomingstorm_return_to_nyx_after_carina_day:
    show cg_guard at cright_f with dissolve
    show mc at cleft with easeinleft
    $ Pause(0.1)
    show cg_guard at shake
    GUARD "Halt!"
    MC @talk "Where is Captain Nyx? I must speak with her at once!"
    GUARD "The Captain is attending a meeting with the war council."
    MC @serious "When will she return?"
    GUARD "I am not her keeper."
    GUARD "She returns when she returns."
    GUARD "If you must see her, wait until later today."
    hide cg_guard with dissolve
    $ Pause(0.1)
    show mc at center with ease
    MC @think "{i}Fuck... I'll have to come back later.{/i}"
    $ LocEnter()

#####################################################################################################
#  If the player attempts to head to Captain Nyx's office after dark, ambush
label qst_thecomingstorm_return_to_nyx_after_carina_night:
    show mc at center with easeinleft
    show mc at blurin, center_f
    "As I made my way towards Captain Nyx, I sensed a presence behind me."
    $ AutoMus(False)
    $ PlayMusic("audio/music/15_Experiments.ogg")
    "A lone guard was following me from a distance."
    show mc at blurin, center
    $ Pause(0.1)
    hide mc with easeoutright
    "When I turned a corner, another joined him. Then another."
    $ LocFlush()
    show mc at cleft_f
    show markus at cright_f
    with dissolve
    MC @think "{i}Fuck.{/i}"
    MARKUS @talk "...You see that, right?"
    MC @talk "Yeah."
    show mc at blurin, cleft
    MC @serious "There's an alley up ahead—let's lose them in there."
    MARKUS @think "Mmm..."
    hide mc with easeoutright
    $ Pause(0.1)
    show markus at blurin, cright
    hide markus with easeoutright
    scene black with dissolve
    "Darting left, we wove through the narrow, labyrinthine alleys."
    "For a moment, it seemed we'd shaken them."
    $ LocSet("novaras_dist_house_south")
    "The main street exit was just ahead."
    "Then, from every passageway, they emerged—blocking every escape route."
    scene bg_alleyway_night
    #$ LocFlush()
    show mc at cright_f
    show markus at right_f
    with dissolve
    MC @think "{i}Shit, they knew we'd come this way.{/i}"
    "A few feet away, the guards halted."
    show cg_guard_rot at left with easeinleft
    GUARD "I hear you've been looking for us..."
    "A nauseating stench filled the air."
    "Rotting. Putrid. Like corpses left to fester in the summer heat."
    MC @serious "Who are you?"
    GUARD "..."
    MC @think "{i}Poltrik?{/i}"
    POLTRIK "How many others are looking for us?"

    MARKUS @scared "{i}*Whispering*{/i} You smell that?"
    show markus at shake
    MARKUS @scared "{i}They reek of death...{/i}"
    MC @serious "What happened to the merchants, Poltrik?"
    MC @angry "What happened during your investigation?!"
    MC @angry "Why haven't you reported back to Captain Nyx?!"
    POLTRIK "..."
    MC @angry "SPEAK, DAMN YOU!"
    POLTRIK "The captain will know all she needs to know... soon."
    MARKUS @angry "[player_name!t]..."
    
    if CharInParty("elena"):
        ELENA "{i}*Growls*{/i}"

    MC @angry "Remove your helmets. {i}Now.{/i}"
    POLTRIK "…As you wish."
    "They reached for their helmets."

    scene cg_guards_ghouls with dissolve
    "As they pulled them off, the stench of death thickened."
    "Rotting flesh. {i}Sunken, blood-filled eyes.{/i}"
    MC @surprised "What in the hells—?!"
    "Their bodies seized violently."

    play sound "audio/cfx/massive_bone_crack.ogg"

    "Tremors wracked them as their weapons clattered to the ground."
    "Blood poured from their eyes, noses, mouths."

    play sound2 "audio/cfx/small_monst_death2.ogg"

    "Low, inhuman groans ripped from their throats."
    "Then, their {i}flesh bulged.{/i}"
    "Bone snapped."
    "{i}Something was shifting beneath their skin.{/i}"
    "As I locked eyes with one of them—{i}I understood.{/i}"
    "{i}Something was keeping them alive.{/i}"
    "{i}Feeding off them from the inside.{/i}"

    scene black with dissolve
    play sound "audio/cfx/prologue_guysnap.ogg"
    "With a sickening tear, their bodies {i}ripped open.{/i}"
    "From within, terrible, pale, ghoulish {i}abominations{/i} burst forth, covered in gore."
    MC @angry "ON ME!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_Right = [{"e_ghoul":3}, {"e_ghoul":4}, {"e_ghoul":5}, {"e_ghoul":3}]))
    scene bg_alleyway_night
    show mc at center_f
    with dissolve
    "When the last of the creatures collapsed, their bodies {i}melted away,{/i} dissolving into bubbling green sludge."
    "Poltrik was nowhere to be seen."

    show markus at cright_f with easeinright
    MARKUS @talk "What in all the hells were those things?!"
    
    if CharInParty("elena"):
        show elena_w at cleft_f with easeinright
        ELENA "{i}*Bark!*{/i}"
        hide elena_w with easeoutleft
    
    if CharInParty("myu"):
        "I watched as Myu crawled toward the nearest puddle of green filth."
        show mc at blurin, center
        "A single tentacle extended, hesitantly prodding the remains—"
        MYU "{i}*Squeeeek!*{/i}"
        show mc at nod
        MC @surprised "Careful, Myu!"
        MYU "Myuuu..."
        show mc at blurin, center_f

    MC @serious "We need to get to Captain Nyx. NOW."
    if QstTheComingStorm().ValaInvestigationPath:
        $ GoalHide(QstTheComingStorm, 95, Silent = True)
        $ GoalShow(QstTheComingStorm, 99, Silent = True)
    else:
        $ GoalHide(QstTheComingStorm, 310, Silent = True)
        $ GoalShow(QstTheComingStorm, 320, Silent = True)
    $ AutoMus(True)
    $ LocEnter()

#####################################################################################################
# RETURNING TO CAPTAIN NYX - dark
label qst_thecomingstorm_return_to_nyx_after_ambush:
    show nyx at cright_f
    with dissolve
    show mc serious at cleft with easeinleft
    MC @surprised "Captain Nyx! I must speak with you—NOW!"
    if QstTheComingStorm().ValaInvestigationPath:
        $ GoalComplete(QstTheComingStorm, 99)
    else:
        $ GoalComplete(QstTheComingStorm, 320)
    NYX @talk "What is it?"
    MC @talk "Poltrik... He's one of them, he's working with the Demorai!"
    NYX @shock "What?! What are you talking about?"
    MC @talk "They've changed him... The Demorai must have got to him and-"
    show nyx shock at shake
    NYX @scared "You're not making any sense!"
    MC @serious "The whole city is in peril if we don't find Poltrik and stop him now!"
    MC @talk "I need to know something..."
    MC @talk "Does Poltrik own any properties in the South-eastern district?"
    NYX @shock "What? No, not as far as I'm aware."
    MC @angry "There has to be something!"
    MC @angry "He's hiding somewhere in the city!"
    NYX @think "How do you know all this?"
    MC @angry "Because he ambushed me."
    MC @angry "Him and his men."
    show nyx shock at shake
    NYX @shock "What?!"
    MC @serious "He's possessed by something, Nyx."
    MC @angry "There were... THINGS inside of them."
    NYX @shock "{i}Things inside of them?!{/i} What the fuck do you mean?"
    NYX @arrogant "Is Poltrik dead?"
    show nyx think
    MC @think "No... maybe?"
    MC @serious "Whatever was controlling him fled."
    MC @serious "I killed the others. {i}They weren't human anymore.{/i}"
    MC @serious "We don't have much time! Does Poltrik have a relative in that district?"
    NYX @think "I... I'd have to check."
    "Nyx shook her head, looking pale."
    NYX @talk "{i}Wait here. Give me an hour.{/i}"
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "{i}... A little while later.{/i}"
    $ LocFlush()
    show mc at cleft
    with dissolve
    show nyx at cright_f with easeinright
    NYX @shock "He DOES have a relative."
    MC @talk "Where?"
    NYX @arrogant "Poltrik's uncle. {i}A minor noble.{/i}"
    NYX @talk "His estate is near the water."
    NYX @arrogant "If what you say is true, {i}there's no time to waste.{/i}"
    NYX @talk "Go there now. I'll gather my guards and follow shortly!"

    $ GoalShow(QstTheComingStorm, 330)
    
    if RomanceNyx().IsRomanced():
        show mc at blurin, cleft_f
        $ Pause(0.1)
        show nyx at center_f with ease
        "As I turned to leave, Nyx suddenly grabbed my wrist."
        NYX @talk "Wait."
        show mc at blurin, cleft
        MC @talk "What is—"
        "Before I could finish, she grabbed my collar and kissed me."
        "Her lips were firm—urgent—before she pulled away."
        show nyx at cright_f with ease
        MC "..."
        NYX "..."
        NYX @blush "{i}Don't get killed, idiot.{/i}"
        "She turned, {i}masking her expression.{/i}"
        scene black with dissolve
        $ LocSet("novaras_fort_seb_yard")
        "Smirking, I stepped outside."
        if CharInParty("elena"):
            if QstGetProgress(RomanceElena) >= 1:
                $ LocFlush()
                show mc at cleft
                show markus at cright_f
                with dissolve
                MARKUS @smile "Sooo, you and the Captain, huh?"
                MARKUS @smile "Well, I can't blame you. She's got a great—"
                show elena_w at center with dissolve
                ELENA "{i}*Low growl...*{/i}"
                MARKUS @smile "{i}Oh dear, looks like someone's a little jealous.{/i}"
                show elena_w at shake
                ELENA "{i}*BARK!*{/i}"
                MC @serious "Let's focus on the damn mission."
    $ LocEnter()

#####################################################################################################
# SCENE 6 - PLAYER ARRIVES AT POLTRIK'S UNCLE'S HOUSE
label qst_thecomingstorm_poltrik_family_estate:
    $ AutoMus(False)
    $ AutoAmb(False) 
    stop ambience fadeout 3.0
    $ PlayMusic("audio/music/15_Experiments.ogg")
    $ InfGainDaily(False)
    $ LocNameSetTemp(_("Poltrik's family estate"))
    if IsDaytime():
        scene bg_poltrik_mansion_ext_day
    else:
        scene bg_poltrik_mansion_ext_night
    with dissolve
    "...Upon arriving at the house, the air felt wrong."
    "Not a single light flickered within the darkened windows."
    "The curtains were drawn, and the home sat eerily still."
    "The front yard, once well-kept, had been left to ruin—the grass growing wild, untamed."
    show mc at cleft with easeinleft
    "A cold wind swept through the empty streets, and with it came a sensation that clawed at the back of my mind."
    "{i}Something was wrong here.{/i}"
    show markus at cright_f with easeinright
    "Then, the scent hit me."
    "That putrid, rotting stench. The same one I had smelled before."
    "It seeped from the very walls of the house. Sickly sweet. Overpowering."
    MARKUS @think "You smell it... right?"
    MC @serious "Yeah."
    MC @serious "We move carefully."
    "As we approached the wooden door, we considered our options."
    menu qst_thecomingstorm_poltrik_family_estate_menu:
        "Knock on the door":
            "I rapped my knuckles against the wood a couple times."
            play sound "audio/cfx/door_knock.ogg"
            "...Nothing."
            MARKUS @think "{i}...Were you really expecting that to work?{/i}"
            jump qst_thecomingstorm_poltrik_family_estate_menu

        "Try to open the door":
            "I grabbed the handle and twisted."
            play sound "audio/interactables/wooden_door_open_2.ogg"
            "Unsurprisingly, it was locked."
            jump qst_thecomingstorm_poltrik_family_estate_menu

        "Kick the door in":
            $ QstTheComingStorm().WayIntoPoltrikEstate = "kick"
            play sound "audio/cfx/door_kick_open.ogg"
            show mc at shake
            "With a sharp, hard boot, the door slammed open, the hinges groaning in protest."
            MARKUS @talk "Well... That's one way to announce our arrival."
            MC @think "Did you have a better idea?"
            MARKUS @talk "Sure. We torch the place from the outside and then head to the Iron—"
            pass

        "Try and lockpick the door" (Req_Dex = 11): 
            $ QstTheComingStorm().WayIntoPoltrikEstate = "pick"
            "Taking one of the hair pins, I knelt down and fiddled with the lock for a while."
            "Markus raised a brow as he watched me work, no doubt curious as to where I learned such a trick."
            "As the door 'clicked' I turned the lock and gently pushed the door open."

            play sound "audio/interactables/wooden_door_open_1.ogg"

            MARKUS @talk "... Good enough for me."
            pass

    #CONTINUE FROM ALL OPTIONS
    scene bg_poltrik_mansion_int with dissolve
    $ Pause(1.0)
    show mc angry2 at cleft with easeinleft
    show markus scared at left with easeinleft
    "The two of us froze."
    "As the door swung open, we were met with a vision from a nightmare."
    "The once-grand interior had been reduced to a butcher's slaughterhouse."
    "Skinless corpses hung upside down from the ceiling, stripped to bare muscle and bone."
    "Blood pooled across the marble floor, seeping through the cracks, thick and dark."
    "The walls—once adorned with noble decorations—were now drenched in red, clawed apart by something inhuman."
    show mc at cright with easeinleft
    "Markus clamped a hand over his mouth, struggling to contain the bile rising in his throat."
    MC @serious "{i}What... the fuck is this?{/i}"
    $ GoalComplete(QstTheComingStorm(), 330)
    "At the center of the room, where a dining table might have once stood, a grotesque mound of flesh sat piled high."
    show mc at blurin, cright_f
    "Intestines. Organs. Skin. Dumped in a heap."
    "Flies buzzed in an unholy symphony, circling the monstrous offering."
    MARKUS @scared "What kind of nightmare is this?!"
    "Then, our eyes lifted to the ceiling."
    "Dark green, bulbous eggs clung to the rafters, pulsating softly."
    "Each was the size of a child, their slimy shells shifting as something inside pressed against the walls."

    if CharInParty("myu"):
        MYU @scared "H-Home! We go home!"
        MYU @scared "Myu no like!"
        MC @serious "Calm yourself, Myu."

    if CharInParty("elena"):
        show elena at center with easeinleft
        ELENA @angry "I don't like this... We should wait for Captain Nyx and the other guards."
        hide elena with easeoutright

    if QstTheComingStorm().WayIntoPoltrikEstate == "kick":
        jump qst_thecomingstorm_poltrik_family_estate_kickedopen
    elif QstTheComingStorm().WayIntoPoltrikEstate == "pick":
        jump qst_thecomingstorm_poltrik_family_estate_snuckin

# If the player snuck in
label qst_thecomingstorm_poltrik_family_estate_snuckin:
    MC @serious "Now... While we have the element of surprise, we can kill them while they sleep."
    MARKUS @angry "Now would have been a lovely time for someone here to have some fire magecraft... But I guess our blades will do."
    hide mc with easeoutright
    hide markus with easeoutleft
    "The others nodded sheepishly, as each of us carefully found one of those wretching pulsing sacks of flesh."
    "Timed just right, each of us destroyed the sacks and killed the wretched, sleeping creatures inside one by one."
    "One tried to scream, awakening at just the right moment, but as the blade sliced across it's throat only a gargled bloody choke escape it's lips."
    "As we worked through in our silent slaughter, a voice suddenly boomed."
    POLTRIK "{i}Murderers...{/i}"
    show mc at cleft with easeinleft
    "We stopped in our bloody work to look around."
    show markus at cright_f with easeinright
    POLTRIK "{i}You think this has aided your cause?{/i}"
    POLTRIK "{i}We are inevitable.{/i}"
    POLTRIK "{i}God has shown us the way!{/i}"
    jump qst_thecomingstorm_poltrik_family_estate_poltrik_battle

label qst_thecomingstorm_poltrik_family_estate_kickedopen:
    # If kicked Door Open
    POLTRIK "{i}...You should have left us alone.{/i}"
    "Hand on my sword hilt, I scanned the shadows."
    MC @angry "Who are you, really?!"
    MC @angry "SHOW YOURSELF!"
    "My voice echoed through the desecrated halls."
    "From somewhere unseen, a voice answered back—twisted, broken."
    POLTRIK "{i}...Who are we?{/i}"
    POLTRIK "{i}We are beings who just want to belong...{/i}"
    POLTRIK "{i}God made us so cold... so very cold...{/i}"

    if CharInParty("elena"):
        show elena at center with easeinleft
        ELENA @shock "We must leave—NOW!"
        hide elena with easeoutright

    POLTRIK "{i}BUT THEN...{/i}"
    POLTRIK "{i}He showed us a way. A way to be warm.{/i}"
    POLTRIK "{i}A way we could all feel like we belonged...{/i}"
    "From the rafters above, something dripped."
    "A shadow shifted."
    "And then—the bones cracked."
    "A ghoulish, twisted figure peeled itself from the ceiling—limbs bending unnaturally as it hung upside down."
    "The milky eyes locked onto me."
    "Then, from the hallways."
    "From the walls."
    "From every godsforsaken corner of this house."
    "More of them began to emerge."
    MARKUS @scared "[player_name!t]..."
    MARKUS @scared "They're surrounding us!"
    "Dozens of inhuman shapes lurched forward—clawed hands dragging across the blood-soaked floors."
    POLTRIK "{i}...We just feel so very at home in your skin...{/i}"
    $ PlayMusicRandom("mus_battle_generic")
    scene black with dissolve
    "Then, the first of them lunged."

    scene black with dissolve
    $ Pause(0.1)
    $ StartBattle(BattleData(BackgroundImage = "pbat_poltrik_mansion", CharIDList_Right = [{"e_ghoul":5}, {"e_ghoul":8}, {"e_ghoul":5}, {"e_ghoul":7}]))

    scene black with dissolve
    "One by one, the wretched things fell."
    scene bg_poltrik_mansion_int
    show mc at cleft_f
    show markus at cright
    with dissolve
    jump qst_thecomingstorm_poltrik_family_estate_poltrik_battle

label qst_thecomingstorm_poltrik_family_estate_poltrik_battle:
    $ GoalShow(QstTheComingStorm, 340)
    POLTRIK "{i}You could have spent your final hours with your loved ones...{/i}"
    POLTRIK "{i}Yet you persist. You resist the inevitable...{/i}"
    show mc at shake
    MC @angry "Do you intend to do nothing but cower and taunt us from the shadows all night?!"
    MARKUS @angry "{i}*Muttering*{/i} Ah, yes. Let's piss him off even more. That'll help."
    POLTRIK "{i}Cowering in the shadows?{/i}"
    POLTRIK "{i}How can that be...?{/i}"
    POLTRIK "{i}After all...{/i}"
    "A massive, clawed hand reached from the darkness."
    scene black with dissolve
    "Before we could react—it slammed into us."
    play sound "audio/cfx/heavy_hit.ogg" volume 0.6
    "We were thrown backwards—deeper into the house of horrors."
    "From the roof above, something massive dropped to the floor—"
    $ PlayMusicRandom("mus_battle_generic")
    POLTRIK "{i}I'm right behind you...{/i}"
    MARKUS @scared "...Oh fuck."

    $ tmpvar = [{"e_poltrik":10}]
    if GetPartySize() >= 3:
        $ tmpvar.append({"e_ghoul":5})
    if GetPartySize() > 3:
        $ tmpvar.append({"e_ghoul":4})
        $ tmpvar.append({"e_ghoul":3})

    $ StartBattle(BattleData(BackgroundImage = "pbat_poltrik_mansion", CharIDList_Right = tmpvar))
    scene black with dissolve
    "Poltrik's twisted spine cracked as he collapsed onto the floor."
    "Blood pooled beneath him, his choking gasps barely audible."
    stop music fadeout 1.0

    scene cg_poltrik_dead with dissolve
    POLTRIK "{i}God... Where are you, God...?{/i}"
    POLTRIK "{i}I did as you commanded...{/i}"

    $ PlayMusic("audio/music/15_Experiments.ogg")

    "His flesh began to dissolve—his body breaking apart into steaming, bubbling filth."
    POLTRIK "{i}As you... commanded...{/i}"
    POLTRIK "{i}Goddddd...{/i}"

    scene bg_poltrik_mansion_int
    show mc at cleft
    show markus at left
    with dissolve

    $ GoalComplete(QstTheComingStorm, 340)
    $ Pause(1.0)
    
    "Metal boots clanked outside."
    "Through the ruined doorway, Captain Nyx and her guards finally arrived."

    show nyx at cright_f with easeinright
    show cg_guard at right_f with easeinright
    NYX @talk "I came as fast as I—"
    show nyx scared at shake
    NYX @scared "...BY THE GODS."
    
    show cg_guard at blurin, right, shake
    play sound "audio/cfx/vomit_muffled.ogg"
    "One of the guards vomited into his helmet."

    NYX @angry "What in all the hells is this place?!"
    hide cg_guard with easeoutright
    MC @surprised "It's a nest!"
    MC @serious "This is what the Demorai were planning!"
    MC @serious "The siege is just a distraction—once the city is weak, these things will overrun it!"

    NYX @shock "...By the gods."

    NYX @arrogant "We need to burn this place to the ground. NOW."
    show nyx at blurin, right with ease
    NYX @arrogant "Call Officer Lukkan—summon—"
    ERIKA "HOLD!"
    MC @think "{i}...What the fuck?{/i}"
    show mc at shake
    MC @surprised "Erika?!"

    scene bg_poltrik_mansion_int_inquisitors with dissolve
    $ Pause()

    if CharInParty("elena"):
        ELENA @shock "Shit."
        "Elena immediately transformed back into a wolf, sprinting past the first of the inquisitors."
        "They turned, eyes narrowing as the blue wolf vanished into the night."
        $ QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars.add("elena")
        $ PartyRemChar("elena")

    if CharInParty("myu"):
        "Myu dissolved into a puddle of slime, slithering away into the shadows."
        "Erika's expression, twitched for a moment as she saw me, and I saw her."
        "Quickly though, she re-composed herself, avoided my gaze with an unreadable, neutral expression."
        $ QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars.add("myu")
        $ PartyRemChar("myu")

    $ Pause(0.5)
    show mc at cleft
    show markus at left
    show nyx at right_f
    with dissolve
    $ Pause(0.25)

    show erika at center_f with dissolve
    ERIKA @angry "By order of the Inquisition, you are all to vacate immediately."
    show nyx angry at shake
    NYX @angry "On what fucking grounds?!"
    NYX @angry "This is a CITY GUARD issue!"
    ERIKA @angry "Not anymore."
    ERIKA @serious "By direct order of Head Inquisitor Marion—"
    show mc surprised at shake
    MC @surprised "Erika! You don't understand—this isn't dark magecraft!"
    MC @surprised "It's a Demorai plot!"
    ERIKA @sad "[player_name!t]... Orders are orders."
    show nyx angry at shake
    NYX @angry "WHAT A FUCKING FARCE!"
    NYX @angry "We need to do a city wide hunt to try and see if they have more of these nests!"
    NYX @angry "You can't just expect me to-"
    ERIKA @angry "I expect all of you to come in for questioning."
    MC @surprised "Erika! We don't have time for this!"
    "Feelings the eyes of her peers watching careful how she'd react, Erika's expression hardened."
    show erika at shake
    ERIKA @angry "Stop calling me Erika!"
    ERIKA @angry "You will address me as inquisitor!"
    MC @angry "Fine, 'inquisitor,' we don't have time for this!"
    ERIKA @angry "Guards! SEIZE THEM!"
    play sound "audio/cfx/army_aye.ogg"
    $ Pause(0.25)
    hide markus with dissolve

    $ QstTheComingStorm().PoltrikEstateLeftPlayerPartyChars.add("markus")
    $ PartyRemChar("markus")

    hide nyx with dissolve
    "Restrained and bound by the guards, each of us were dragged away from the scene."
    MC @angry "This is a mistake, you're going to get us all killed!"
    show mc at shake
    MC "Erika!"    
    hide mc with dissolve
    MC "ERIKA!"
    ERIKA @sad "..."
    scene black with dissolve
    jump qst_thecomingstorm_prison

label qst_thecomingstorm_prison:
    $ AutoMus(False)
    $ AutoAmb(False)
    $ QstTheComingStorm().ShowAndSpinCountdown = False
    $ LocNameSetTemp(_("Prison cell"))
    $ TimeAdvBy(TIME_2H)
    play ambience "audio/ambience_loc/prison.ogg" fadein 3.0
    $ AutoTimeFreeze(True)
    $ Pause(1.0)
    if IsDaytime():
        scene bg_prison_cell
    else:
        scene bg_prison_cell_night
    show mc at cright_f
    show cg_guard at left
    show nyx at cleft
    with dissolve
    "Thrown into a cold, dimly lit cell alongside Captain Nyx, I grabbed the bars, rattling them in frustration."
    show mc at shake
    MC @angry "{i}Damn it!{/i}"
    "I shouted at the guards as they marched away."
    MC @angry "Where are you taking the others?! What have you done with Markus?!"
    "The guards offered no answer, only the dull echo of their boots fading into the corridor beyond the heavy iron doors."
    GUARD @talk "...Keep your voice down, prisoner."
    hide cg_guard with dissolve
    "The door slammed shut, sealing us inside."
    MC @angry "Fuck!"
    NYX @think "It's no use."
    "Nyx exhaled sharply, slumping against the wall with crossed arms."
    NYX @talk "They won't tell us anything."
    MC @angry "I could rip through these fucking bars with ease—"
    show nyx at center with ease
    "Before I could finish, Nyx lunged forward, clamping a firm hand over my mouth."
    NYX @angry "{i}Shut the fuck up.{/i}"
    "Her voice was a low, urgent whisper."
    NYX @angry "Do you want them to realize {i}what{/i} you are? If they find out—"
    "She slowly peeled her hand away."
    show nyx at cleft with ease
    NYX @angry "...We are both dead."
    MC @serious "...So we just sit here and wait?"
    NYX @think "Someone will come for us. Eventually."
    MC @angry "Easy for you to say. My {i}friend{/i} is still in a fucking cell somewhere."
    NYX @sad "...Getting angry solves nothing."
    NYX @sad "Try to relax. {i}Stay focused.{/i}"
    "Silence settled between us as she retreated to her end of the cell, and I to mine."
    if RomanceNyx().IsRomanced():
        jump qst_thecomingstorm_prison_nyx_romance
    else:
        jump qst_thecomingstorm_prison_nyx_not_romance
    
label qst_thecomingstorm_prison_nyx_romance:
    scene black with dissolve
    "After what felt like hours of waiting, Nyx broke the silence."
    if IsDaytime():
        scene bg_prison_cell
    else:
        scene bg_prison_cell_night
    show mc at cright_f
    show nyx at cleft
    with dissolve
    NYX @talk "...You know, I was just thinking."
    "A scoff escaped her lips."
    NYX @laugh "They {i}might{/i} just execute me for this."
    MC @surprised "Don't say that."
    NYX @smile "Why not? There's no point in shying away from it."
    NYX @talk "Incompetent men have a habit of disposing of those more capable than them."
    NYX @think "They don't want to look bad. Even if it drags us all down with them."
    MC @think "Why are you telling me this now?"
    show nyx at center with ease
    "Nyx let out a quiet chuckle and took a step forward."
    NYX @smile "{i}Because, you idiot.{/i}"
    $ CharSetClothes("nyx", "naked")
    show nyx at nod
    "With slow, deliberate movements, she stripped off her armor, tossing it aside."
    MC @surprised "{i}Nyx?{/i}"
    MC @talk "{i}What are you doing?!{/i}"
    "She stood before me now, smirking as she pulled at her shirt strings, letting her toned form come into view."
    NYX @smile "If I'm going to die... I at least want {i}one last fuck{/i} before that happens."
    $ CharSetClothes("mc", "pants")
    show mc at nod
    "A hunger ignited in my gut as my cock strained painfully in my trousers."
    MC @surprised "Right now? Someone could—"
    "She stepped closer, leaning into my ear."
    NYX @blush "{i}Let the fuckers watch.{/i}"
    NYX @angry "Now, are you going to keep staring like a slack-jawed fool or remind me why you're supposed to be the {i}man{/i} in this relationship?"

    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    
    "She didn't need to ask twice..."
    
    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene nyx_prison_fuck_loop_wall_slow with flash
    $ Pause()
    
    NYX "Ahh...! ❤️"
    NYX "H-Harder! Harder, damn it!"
    "Holding her legs between my arms, pinning her against the cold cell wall, I continued slamming my cock into her."
    "Her hot breath touched my face as she clung to me tightly, her moans echoing off the stone walls as I pushed deeper inside her."
    NYX "F-Fuck!"
    
    scene nyx_prison_fuck_loop_kiss_slow with dissolve
    $ Pause()
    
    NYX "Mhmm!"
    "Her tight body clung to me as I poured all of my frustration and desire into each thrust."
    NYX "Ahhh! Y-Yes!"
    NYX "Mhmm, f-fuck me..."

    scene nyx_prison_fuck_loop_wall_slow with dissolve
    $ Pause()

    NYX "Fuck me harder with that huge cock of yours!"
    "Her slick, needy cunt gripped me with every thrust."
    "Her words only made her tighten more, as if teasing was its own form of seduction."
    MC "G-Grghh! I haven't been able to stop thinking about you since the first time!"
    "Nyx laughed low, breathlessly, doing her best to pull me closer."
    NYX "You've missed me...?"
    NYX "{i}Or my tight cunt?{/i}"
    "Her taunt made my cock twitch, and I responded by moving faster, deeper, until she was gasping again."
    NYX "Ahhh! Yes! That's it!"
    NYX "Mhmmfhh! F-Faster! {i}*Huff*{/i}"
    NYX "That's an order! Mhhfh!"
    "I obeyed, burying myself deeper inside her as her moans filled the cell."
    "Her nails clawed at my back, leaving sharp little reminders."
    NYX "Yes! Mhmm! Like that!"
    MC "Grghh..."
    MC "You feel so good."
    "Her hot breath brushed against my face again. She chuckled."
    NYX "Can't keep up, soldier?"
    NYX "Is t-that all you've got, sol—"

    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)
    scene nyx_prison_fuck_loop_wall_fast with dissolve
    $ Pause()

    "A sudden, deep thrust silenced her."
    "Her mouth dropped open, eyes wide, a choking moan escaping her lips."
    "She cupped my face, pulled me in, and kissed me hard—our tongues tangling hungrily."

    scene nyx_prison_fuck_loop_kiss_fast with dissolve
    $ Pause()

    NYX "Mhmm... ❤️"
    "As I pushed deeper, her eyes fluttered, rolling slightly as the kiss deepened. My hands roamed her body greedily."
    "Her toned frame was soft in just the right places, her legs gripping me with unexpected strength."
    NYX "M-Mhorhee ~ ❤️"
    "Her tongue danced with mine as her legs pulled me deeper."
    "I obliged, thrusting harder as she groaned between our kisses."
    "I pulled back, pounding faster, refusing to let go—her nails raked down my back as muffled cries of pleasure escaped her lips."

    scene nyx_prison_fuck_loop_wall_fast with dissolve
    $ Pause()

    "Sweat dripped from our bodies. For one fleeting moment, we found refuge in each other within this cold, cruel place."
    "Her breath warmed my skin, and I felt her body begin to tremble violently beneath me."
    "I fucked her like it might be the last time—my lips numb from kissing, my cock driving harder inside her as she pleaded."
    NYX "{i}Cum inhh mhee! Cumm! Mhmm!{/i}"
    "Unable to hold back, I drove myself fully into Nyx, releasing a wave of heat inside her."
    MC "H-HRGHHH!!"
    "She let out a scream of bliss as her tight womb was filled."
    "Her body squeezed me desperately as her eyes rolled back."

    $ UnlockGalSceneAndGrantXp("nyx", "prison_fuck")
    $ ReduceInfectionFromSex("nyx")
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene nyx_prison_fuck_finish1 with flash
    $ Pause()

    NYX "{i}GODSSS! YES!{/i} ❤️"
    "As I emptied into her, I kissed her neck softly—riding the fading wave of our shared climax."

    scene nyx_prison_fuck_finish2 with dissolve
    $ Pause()

    "Her legs slowly lowered to the floor, trembling, as I held her close between tender, breathless kisses."

    $ AutoMus(True)
    $ CharSetClothes("mc", "naked")
    $ CharSetClothes("nyx", "naked")
    scene black with dissolve
    $ Pause(0.5)
    
    if IsDaytime():
        scene bg_prison_cell
    else:
        scene bg_prison_cell_night
    show mc at cright_f
    show nyx at cleft
    with dissolve
    NYX "F-Fuck... that was..."
    NYX "Mhmm..."
    MC "Are you alright?"
    NYX "I'm fine, just..."
    NYX "{i}Hold me a moment.{/i}"
    "...Captain Nyx, despite her beauty, had always kept her softer side locked away."
    "And yet, in that moment—pressed against me, embracing me—I could feel the walls she'd built begin to fall."
    "Her hand slid down my chest, gentle, deliberate. She looked into my eyes... then quickly averted her gaze, blushing."
    NYX "D-Don't get used to all this."
    NYX "{i}I'm not that kind of girl.{/i}"
    "I smiled. She gently swatted my chest with a pout."
    MC "Ow! What was that for?"
    NYX "Cocky fucker."
    scene black with dissolve
    $ Pause(0.5)
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("nyx", "normal")
    "Slowly, the moment faded, and we began to redress in silence, unsure of what would come next—but for now, not alone."
    
    if IsDaytime():
        scene bg_prison_cell
    else:
        scene bg_prison_cell_night
    show mc at cright_f
    show nyx at right_f
    with dissolve

    "The heavy door violently swung open as four guards stepped inside."
    show cg_guard at cleft with easeinleft
    GUARD "Captain Nyx, you are to come with us."
    show nyx at center_f with easeinright
    MC @angry "Where are you taking her?"
    "The guards pulled Nyx from the cell, but as she stepped forward she looked back to stop me."
    show nyx at blurin, center_f
    $ Pause(0.1)
    NYX @talk "It's alright... They're just going to question me."
    MC @sad "Captain, I-"
    NYX @talk "Just stay here."
    NYX @talk "{i}That's an order.{/i}"
    show nyx at blurin, center_f
    $ Pause(0.1)
    hide nyx with easeoutleft
    show cg_guard at blurin, cleft_f
    $ Pause(0.1)
    hide cg_guard with easeoutleft
    "With a heavy sigh, and a painful knot in my stomach I watched as the guards lead Nyx away, locking the cell door behind them."
    jump qst_thecomingstorm_prison_erika_release

label qst_thecomingstorm_prison_nyx_not_romance:
    scene black with dissolve
    "Time passed at a crawl, my mind racing in circles."
    "Then, without warning, the heavy iron doors swung open."
        
    if IsDaytime():
        scene bg_prison_cell
    else:
        scene bg_prison_cell_night
    show mc at right_f
    show nyx at left
    with dissolve

    show cg_guard at center_f with dissolve
    GUARD @talk "Captain Nyx. You are to come with us."
    show mc at shake
    MC @angry "Where are you taking her?"
    "Two guards stepped inside, their hands reaching to restrain her. As I surged forward, Nyx shot me a look—firm, commanding."
    NYX @arrogant "It's alright."
    NYX @arrogant "They're just going to question me."
    MC @angry "Captain, I—"
    "She cut me off with a sharp glare."
    NYX @talk "Just stay here."
    NYX @arrogant "{i}That's an order.{/i}"
    "She turned away, stepping toward the guards."
    hide nyx 
    hide cg_guard
    with dissolve
    "As I watched her disappear beyond the doorframe, a weight sank in my gut."
    show mc at center with ease
    MC @angry "{i}Fuck.{/i}"
    jump qst_thecomingstorm_prison_erika_release
    
###############################################
label qst_thecomingstorm_prison_erika_release:
    scene black with dissolve
    "Hours drifted by in restless silence."
    "Then, at last, the heavy door creaked open."
    if IsDaytime():
        scene bg_prison_cell
    else:
        scene bg_prison_cell_night
    show mc at cleft
    with dissolve

    show erika at cright_f with easeinright

    "Erika entered the cell, her expression unreadable."
    MC @serious "Where are the others? Where's Markus?"
    ERIKA @talk "They're being interrogated separately."
    MC @angry "You have to let us go."
    show mc at shake
    MC @angry "The city is in danger!"
    ERIKA @talk "...We need to talk about what you were doing at that house."
    MC @angry "For fuck's sake—"
    show erika at center_f with ease
    ERIKA @angry "LISTEN. TO. ME."
    "I stopped short. Her voice was sharp, urgent."
    ERIKA @angry "Do you realize what's happening right now?"
    ERIKA @angry "The inquisition believes you're consorting with dark mages."
    MC @surprised "{i}What?!{/i}"
    MC @angry "That's ridiculous! I don't have any magecraft!"
    ERIKA @angry "IT DOESN'T MATTER!"
    "She ran a hand through her hair, exhaling sharply."
    ERIKA @serious "You've been red-flagged, [player_name!t]."
    ERIKA @serious "And the inquisition doesn't let go of people like you once they sink their claws in."
    MC @angry "So what—you're just going to let them kill me?"
    "She hesitated. For a split second, she looked away."
    MC @angry "{i}Erika, look at me.{/i}"
    ERIKA @sad "..."
    MC @sad "Look at me!"
    "Erika's eyes slowly lifted."
    MC @serious "Do you {i}really{/i} believe I'm a threat?"
    "Silence."
    show erika at cright_f with ease
    ERIKA @serious "...Do you truly believe Novaras is in peril?"
    MC @serious "Yes."
    ERIKA @serious "And you think you can stop it?"
    MC @talk "I have to."
    "She turned to leave."
    "Then—without looking back—she tossed something onto the floor."
    "A key."
    MC @surprised "{i}Erika...{/i}"
    "She didn't respond, only speaking loud enough for the empty cell to hear."
    ERIKA @serious "{i}The guards here can be... clumsy. Always dropping their keys.{/i}"
    ERIKA @serious "{i}If someone were to escape, they would only need to take the door at the end of the hallway.{/i}"
    ERIKA @serious "{i}Turn left. Then right. Then straight ahead.{/i}"
    "She paused in the doorway."
    ERIKA @serious "{i}...I hope the warden doesn't take too long to notice.{/i}"
    hide erika with dissolve
    "With that, she was gone."
    show mc at center with ease
    $ Pause(0.1)
    show mc at nod
    "Heart pounding, I grabbed the key."
    MC @serious "(I just hope Markus is okay...)"
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvTo(TIME_DAY_END)
    $ TimeAdvTo(TIME_DAY_START)
    $ TimeAdvTo(TIME_DAY_END)
    $ BlockWaitGlobal(True)
    "I slipped through the halls, following Erika's instructions to the letter. The cold night air hit me as I slipped through the back exit."
    $ LocNameReset()
    $ LocSet("novaras_dist_army")
    $ AutoMus(True)
    $ AutoAmb(True)
    $ LocFlush()
    show mc at cleft
    with dissolve
    MC @think "(I can't go home. The inquisitors will be looking for me.)"
    if QstTheComingStorm().ValaInvestigationPath:
        MC @think "(I need to lay low... Maybe Vala can help?)"
        $ GoalShow(QstTheComingStorm, 97)
    else:
        MC @think "(I need to lay low... Maybe Carina can help?)"
        $ GoalShow(QstTheComingStorm, 350)    

    $ LocEnter()

###### this is a section of blockers for the "speak to carina" post-prison section.
label qst_TheComingStorm_GetToCarinaSneak_CityGates:
    MC "(I don't think it's a good idea to strut around there right now...)"
    if QstTheComingStorm().ValaInvestigationPath:
        MC "(I should get to the library, {i}fast{/i}.)"
    else:
        MC "(I should get to Carina's, {i}fast{/i}.)"
    $ LocEnterQ()

### at army dist:
#### army to market bridge
label qst_TheComingStorm_GetToCarinaSneak_ArmyToMarketBridge:
    show mc at center_f with easeinright
    MC "(There's some commotion at the bridges.)"
    MC "(Guards. Lots of them.)"
    show mc at blurin, center
    if QstTheComingStorm().ValaInvestigationPath:
        MC "(I'll have to find another way to the library.)"
    else:
        MC "(I'll have to find another way to Carina's.)"
    hide mc with easeoutright
    $ LocEnterQ()
#### army to centre dist 
label qst_TheComingStorm_GetToCarinaSneak_ToCentreBridge:
    MC "(Royal district was never short on guards...)"
    MC "(Especially now, with the Demorai army marching towards the city.)"
    MC "(It's too risky to go through there.)"
    $ LocEnterQ()
#### army to fort sebastian
label qst_TheComingStorm_GetToCarinaSneak_ArmyToFortSebastian:
    MC "(I'm not coming anywhere near that place, not now.)"
    $ LocEnterQ()


### at house dist:
### mc house: 
label qst_TheComingStorm_GetToCarinaSneak_MCHouse:
    MC "(Too dangerous... They're bound to look for me once they realize I'm missing.)"
    MC "([regina_ref_cap!t]...)"
    MC "(I've got to move.)"
    $ LocEnterQ()

label qst_TheComingStorm_GetToCarinaSneak_NotNow:
    MC "(Not now...)"
    $ LocEnterQ()


## at mage dist:
### to palam hall:
label qst_TheComingStorm_GetToCarinaSneak_Palam:
    MC "(As much as I want to, I can't.)"
    MC "(It's too dangerous.)"
    $ LocEnterQ()

# at pleasure dist:
### lock bd
label qst_TheComingStorm_GetToCarinaSneak_BlackDiamond:
    MC "(The outlaws of the city.)"
    MC "(They would be the first to sell me out to the inquisition.)"
    MC "(Gotta move on.)"
    $ LocEnterQ()

# at market dist:
### block tavern
label qst_TheComingStorm_GetToCarinaSneak_Tavern:
    MC "(I can hear partying inside.)"
    MC "(These people... The Demorai must be just a couple days away by now.)"
    $ LocEnterQ()

### block guild
label qst_TheComingStorm_GetToCarinaSneak_AdvGuild:
    "Looking at the guild from the distance, I saw a couple of guards talking to a group of adventurers."
    MC "(That's it, they must be looking for me now.)"
    MC "(No time to waste.)"
    $ LocEnterQ()

### block bridge to army
label qst_TheComingStorm_GetToCarinaSneak_MarketToArmyBridge:
    show mc at cright with easeinleft
    MC "(From here, I can still see the guards patrolling the area.)"
    MC "(Wonder what is that about...)"
    show cg_guard at cleft with easeinleft
    show cg_guard at shake

    GUARD "CITIZEN!"
    show mc scared at cright
    "My heart sank."
    BLACK "Calm. Down."
    $ Pause(0.5)
    show mc scared at blurin, cright_f with ease
    MC @scared "Y-yes?!"
    GUARD "There has been an... accident that way."
    GUARD "You might want to steer clear of the area for a few hours."
    GUARD "...For your own sake."
    show mc at cright_f
    MC @talk "An- an accident?"
    GUARD "Yes."
    "The guard looked around before continuing:"
    GUARD "They have retrieved near dozen rotten corpses from underneath the bridge, horrid sight."
    MC @talk "W-what?"
    $ Pause(0.1)
    show mc at blurin, cright
    GUARD "Yeah, they are investigating the city's water supply as we speak."
    MC @talk "(Poltrik's creatures' doing... {i}whatever they were.{/i})"
    GUARD "Anyway, if I were you, I wouldn't go there."
    GUARD "Least you want to part with your dinner."
    show cg_guard at right with easeoutright
    show mc at blurin, cright_f
    hide mc with easeoutleft
    $ Pause(0.25)
    show cg_guard at blurin, right_f
    GUARD "Say, have we met?"
    GUARD "{i}*Sigh*{/i}"
    GUARD "They always just run on."
    $ QstTheComingStorm().SeenGuardSceneInSneakSession = True
    $ LocEnter()

label qst_TheComingStorm_GetToCarinaSneak_MarketToArmyBridge_seen:
    MC "(Just how much damage have Poltrik and his... flock had managed to do before we found them?)"
    MC "(Is there more like him?)"
    $ LocEnterQ()

label qst_TheComingStorm_GetToValaSneak_BordelloBlock:
    MC "(Not now. This place is all eyes and ears.)"
    $ LocEnterQ()

##################################
# finally returned to carina 
label qst_TheComingStorm_GetToCarinaSneak_Arrived:
    show carina at cleft_f
    with dissolve
    $ Pause(0.1)
    show mc at cright_f with easeinright
    $ Pause(0.1)
    show carina at blurin, cleft
    CARINA @angry "No."
    CARINA @angry "No, no, {i}no!{/i}"
    show carina at shake
    "Before I could even get a word in, Carina slammed her hand on the counter."
    CARINA @angry "The {i}last{/i} thing I need is inquisitors barging into my establishment!"
    MC @angry "Carina, I need your help."
    CARINA @angry "Of course you do!"
    CARINA @angry "Do you have any idea the shitstorm you've caused?"
    CARINA @angry "{i}Everyone{/i} is talking about how you, Captain Nyx, and Markus were taken in!"
    CARINA @think "How in the hells did you even escape?"
    MC @serious "That doesn't matter. Where's Captain Nyx?"
    MC @serious "And Markus? They still have him—I need to get him out!"
    "Carina let out a long, irritated sigh, rubbing her temples."
    CARINA @angry "Calm the fuck down, panicking won't solve anything."
    hide carina
    show cg_carina_smoke_normal at blurin, cleft
    CARINA @think "{i}Sigh{/i} Captain Nyx has been released."
    CARINA @talk "Probably because of the upcoming siege."
    CARINA @talk "They'll still come for her once the fighting is over, but for now, she's free."
    MC @serious "And Markus?"
    CARINA @think "No word."
    CARINA @think "If he's still in custody, that means they're holding onto him for something."
    hide cg_carina_smoke_normal
    show carina at blurin, cleft
    MC @angry "Where is he? I have to get him out!"
    CARINA @angry "No, you need to {i}stay put!{/i}"
    CARINA @angry "Do you not understand? The inquisitors are looking {i}everywhere{/i} for you."
    CARINA @angry "You step outside and you're done."
    "She exhaled sharply, shaking her head."
    CARINA @think "... You can stay in one of the VIP rooms for now."
    CARINA @think "It's the safest place for you."
    MC @talk "...Thank you."
    MC @think "{i}I didn't expect her to help so freely.{/i}"
    "Carina scoffed, folding her arms."
    CARINA @smile "Oh, make no mistake—both you {i}and{/i} the good captain owe me for this."
    CARINA @talk "Now, go wash up in your room. {i}You reek.{/i}"
    scene black with dissolve
    $ Pause(0.5)
    $ TimeAdvTo(TIME_NOON)

# carina route auto-falls through to here, 
# the label is for vala route (jumps here after getting to the library)
label qst_TheComingStorm_BrothelRoomWaitForNyx:
    "A few hours passed. The tension in my muscles never faded, even as I sat alone, waiting, planning."
    scene bg_weeping_heart_brothel_room
    show mc at cright_f
    with dissolve
    "Then, a knock at the door."
    play sound "audio/cfx/door_knock.ogg"
    MC @think "{i}Finally...{/i}"
    "The lock clicked, and as the door eased open, a familiar figure slipped inside."
    show nyx at cleft with easeinleft
    MC @surprised "Captain Nyx!"
    "Nyx scanned the room quickly before shutting the door behind her, her expression tight with worry."
    NYX @talk "Well… things have {i}definitely{/i} gone to shit, haven't they?"
    MC @surprised "Where's Markus?"
    NYX @arrogant "They refused to let him go."
    NYX @angry "And now that they know you escaped, they're losing their damn minds."
    show mc at blurin, cright
    $ Pause(0.1)
    MC @think "{i}Damn it…{/i}"
    NYX @talk "How did you escape?"
    show mc at blurin, cright_f
    $ Pause(0.1)
    MC @talk "It doesn't matter."
    MC @talk "What do we do now?"
    MC @serious "I have to get Markus out of there."
    show nyx at shake
    NYX @angry "Don't do anything!"
    "Her voice was sharp, her eyes locking onto mine."
    NYX @think "The inquisitors are looking {i}everywhere{/i} for you."
    MC @angry "So I just do {i}nothing?{/i}"
    NYX @angry "I'm pulling whatever last strings I have left to shift more guards inside the city before the siege."
    NYX @think "As for Markus…"
    NYX @think "{i}I'll keep trying.{/i}"
    MC @think "What do you mean {i}'last strings'?{/i}"
    "A shadow crossed her face."
    NYX @talk "Because once the siege is over, I'm heading back to my cell to stand trial."
    MC @surprised "{i}What?!{/i}"
    NYX @angry "I've been accused of insubordination, corruption, treachery, and {i}consulting with dark magecraft.{/i}"
    show mc at shake
    MC @angry "That's ridiculous!"
    NYX @talk "Doesn't matter."
    NYX @talk "The only reason I'm free right now is because Officer Lukkan interceded—with a {i}personal order{/i} from the Emperor himself."
    NYX @talk "Otherwise, I'd still be rotting in that damn cell."
    MC @angry "They can't just turn on you like that!"
    NYX @talk "They can, and they will."
    "She exhaled sharply, rubbing her temples."
    NYX @angry "But none of that matters if we're all dead in the next few days."
    MC @sad "…What am I supposed to do in the meantime?"
    NYX @think "Stay hidden. Lay low."
    NYX @think "If you {i}must{/i} leave, avoid anywhere they might be watching."
    NYX @talk "I have to go."
    show nyx at blurin, cleft_f
    $ Pause(0.1)
    NYX @talk "There's still too much to do before the siege begins."
    if RomanceNyx().IsRomanced():
        "As she moved to leave, I reached out and grabbed her hand."
        show mc at center_f with ease
        NYX @shock "What are y—"
        hide nyx
        hide mc
        show cg_nyx_kiss_armor relaxed at center_f
        with dissolve
        $ Pause()
        "Before she could finish, I pulled her into a kiss, my hand slipping to the curve of her ass, squeezing firmly."
        NYX @blush "...Mmh…"
        "For a moment, she melted into me, her fingers tangling into my shirt."
        "Then, reluctantly, she pulled back."
        hide cg_nyx_kiss_armor relaxed
        show mc at center_f
        show nyx at cleft
        with dissolve
        NYX @talk "I have to go."
        NYX @smile "{i}Keep safe, [player_name!t]{/i}."
        show nyx at blurin, cleft_f
        pass

    hide nyx with easeoutleft
    show mc at blurin, center with ease
    "As the door closed, silence settled once more."
    "I knew, no matter what happened next, there was no going back now."
    $ QstJudgementDay().PlayerPrepared = True
    $ AutoMus(False)
    stop music fadeout 3.0
    $ QstComplete(QstTheComingStorm)
    MC @think "{i}…This is it.{/i}"
    MC @think "The city is on the brink."
    MC @think "Markus is still inside."
    MC @think "{i}The siege is coming.{/i}"
    jump qst_JudgementDay_SiegeStart