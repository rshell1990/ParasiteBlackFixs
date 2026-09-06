init python:
    @AppendToAllQuests
    class LukkanTavernEncounter(LogicModule):
        def __init__(self):
            super().__init__()

            self.interval = 3

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_tavern":
                if not IsDaytime():
                    if GetGameDay() % self.interval == 0: # makes him appear every 3rd day: 0*,1,2,3*,4,5,6*
                        if not QstIsActive(QstTheJackpot): # makes him not appear if jackpot quest mr winward is up
                            btnMods["lukkan_tavern_talk_btn"] = BtnJumpLabel(_("Talk to Lukkan"), "ev_lukkan_tavern_talk")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("lukkan_tavern_root", DNode(_("I wanted to ask you about something"), "ev_lukkan_tavern_talk_2"))
            yield ("lukkan_tavern_root", DNode(_("Very well, enjoy your Evening."), "ev_lukkan_tavern_bye", nextNode = "DNodeExit", order = -100))

label ev_lukkan_tavern_talk:
    show lukkan at center_f with dissolve
    LUKKAN @talk "Oh no... Not when I'm off work kid."
    LUKKAN @talk 'Leave me to drink in peace, would you?'
    call processDialogue("lukkan_tavern_root") from _call_processDialogue_38
    $ LocEnter()

label ev_lukkan_tavern_bye:
    'Lukkan turned away and continued to sip at his drink ignoring me.'
    $ LocEnter()

label ev_lukkan_tavern_talk_2:
    LUKKAN @talk "Well I don't care to answer it."
    LUKKAN @talk "Harrass me in work all you like, not during my downtime."
    menu:
        "Alright you miserable bastard, I'll leave you alone.":
            LUKKAN @talk 'Finally.' #dialogue ends.
            $ LocEnter()
        'How about I buy you the next round?' (Req_Gold = 5): #Player needs 5 coins 
            $ PlayerRemItem("gold",5)
            LUKKAN @talk 'Urghh... Fine.'
            LUKKAN @talk 'What do you want?'
            menu ev_lukkan_tavern_talk_2_menu:
                "How long have you been serving?":
                    LUKKAN @talk '...Who, {i}me?{/i}'
                    LUKKAN @talk 'I signed up when I was just a lad, barely fifteen.'
                    LUKKAN @talk 'Must have been... At least thirty years ago?'
                    LUKKAN @talk 'Things were different back then... {i}Better.{/i}'
                    LUKKAN @talk 'I mean you still have the usual shite to deal with, always some cunt knocking about somewhere causing trouble.'
                    LUKKAN @talk 'But even the bad days never came close to this.'
                    MC @talk 'If you served that long, did you ever meet Newheart?'
                    LUKKAN @talk 'I saw him a few times in passing, even followed under his command briefly.'
                    LUKKAN @talk 'But I never knew him as a man.'
                    LUKKAN @talk 'Only a living legend... Gods, how his armour glimmered in the light.'
                    MC @talk 'Were you there at Meadow Plains when he fell?'
                    LUKKAN @talk 'Nah, I was pulled away to fight in the Eastern Front while all that was going down, chasing off some straggler forces that were looping around Hamun trying to wreak havoc behind our lines.'
                    LUKKAN @talk "Heard about the shitshow that went down though and read the battle reports after... Wasn't pretty."
                    'Lukkan took another sip of Ale from his mug.'
                    LUKKAN @talk "But I can't say I'm surprised, the leadership back then had no real fucking common sense."
                    LUKKAN @talk 'I mean, really? What the fuck kind of plan was that?' 
                    LUKKAN @talk '{i}Trying to seige the largest fort we ever built while Newheart and a couple men tried some merry-band-of-heroes bullshit sneaking through a secret passage inside the fort to force down the drawbridge?{/i}' 
                    LUKKAN @talk 'No one had been down in those shafts in years, they had no idea whether the passageway was still even accessible but off they went anyway.'
                    LUKKAN @talk 'Not to mention the sheer volume of Demorai inside the fort and the fortifications they had been building up around it.'
                    LUKKAN @talk 'Granted the fort had been damaged a little when the Demorai first took it, but still!'
                    LUKKAN @talk 'It was a damn meat-grinder for those charging in!'
                    MC @talk 'Sounds like you blame Newheart.'
                    LUKKAN @talk 'Well... I do blame him a little, sacrilege though it may be seen.'
                    LUKKAN @talk "Adventurers are cocky glory-hound bastards all of them, and even Newheart still couldn't shake that 'Adventurer' mindset fully I think."
                    LUKKAN @talk 'Why did he {i}personally{/i} have to lead the men down there?'
                    LUKKAN @talk 'He could never sit back and just be a fucking {i}general,{/i} he had to always plant himself in the thick of battle somewhere.'
                    LUKKAN @talk 'And sure, he was a damn demon on the battlefield, and it usually inspired the men like nothing else!'
                    LUKKAN @talk  "But that's the catch isn't it? Because when he was then slain right there fucking in front of everyone, that morale boost he always gave came right back around and nearly finished us there and then."
                    LUKKAN @talk "Morale plummeted into total despair, the line fell apart because men started fleeing for their lives because of course they did? The 'great hero' just got butchered in front of them, what chance did they have?"
                    LUKKAN @talk "But... It wasn't all on him, his orders came down to take the Fort before the Demorai reinforcements arrived from the South and hold the line there."
                    LUKKAN @talk "He pleaded with them to dig in for a long war, to forget about Fort Rook for now and to lift the sieges at Gerano and Inma first to free up the trapped forces."
                    LUKKAN @talk 'But Mesamor and the high lords had their way and constantly meddled in military matters they had no business dealing with.' 
                    LUKKAN @talk 'Well, the rest is history.'
                    'Lukkan bitterly sipped at his drink.'
                    jump ev_lukkan_tavern_talk_2_menu
                "Did you side with Alcott to betray the king?":
                    LUKKAN @talk "...What's it to you, kid?"
                    MC @talk "I guess I just want to know more about it."
                    MC @talk "I hear a couple royalists grumble about Alcott's {i}'crimes'{/i} and I guess I wanted to hear the other side."
                    LUKKAN @talk "Fuck the Royalists, we'd all be worm food by now if we were still listening to them."
                    MC @talk 'So you did side with Alcott?'
                    LUKKAN @talk '...I did... Hardest decision I ever made.'
                    LUKKAN @talk 'Had to be done though.'
                    LUKKAN @talk "I was appointed one of Alcott's personal guards and followed him wherever he went."
                    LUKKAN @talk "I became privy as a silent observer to some of the madness in Mesamor's court."
                    MC @talk 'What {i}really{/i} happened?'
                    LUKKAN @talk  "It's hard to explain truthfully, it wasn't just one thing but something built up over time."
                    LUKKAN @talk 'After Alcott rose up and managed to repel the Demorai during the Great Seige, he was appointed head of the War council and supreme commander of all forces.'
                    LUKKAN @talk 'Only Mesamor himself had any authority higher than him, and very quickly the relationship between them fell apart.'
                    MC @talk 'How so?'
                    LUKKAN @talk 'When we managed to catch a second wind after repelling the Demorai, Mesamor took it as a sign we now had the enemy on the backfoot, and we needed to press the advance immediately.'
                    LUKKAN @talk "Alcott's position was always that Newheart's initial assessment was correct, we needed time and to make drastic changes to our forces before any kind of real counter offensive would pay off."
                    LUKKAN @talk 'And every single time, Mesamor was reluctant to embrace any kind of practical change.'
                    menu ev_lukkan_tavern_talk_2_menu2:
                        'Got an example?':
                            LUKKAN @talk 'Tell me, did you ever see the {i}old{/i} Alderian armour?'
                            LUKKAN @talk 'Beautiful stuff, purple and black cloaked, made by Syaxian ore.'
                            LUKKAN @talk 'It was some of the most durable and flexible armour around, light as a bloody feather too.'
                            LUKKAN @talk '...And it was fucking useless.'
                            MC @talk 'Huh? How come?'
                            LUKKAN @talk 'Because the ore was {i}always{/i} in short supply, limited to many of the mines found in the south which we were no longer in control of.'
                            LUKKAN @talk 'And frankly, the armour took {i}far{/i} too long to produce.'
                            LUKKAN @talk "Sure, in peace time when you have the luxury of time, it's fine."
                            LUKKAN @talk 'You can slowly plod on while you collect all your ore.'
                            LUKKAN @talk 'But what happens when ten thousand men are slain on the battlefield in one day, leaving behind all that armour?'
                            LUKKAN @talk "That armour doesn't just 'magically' return to re-stock itself."
                            LUKKAN @talk "And just like that, it dawns on them, pretty soon, they won't be able to produce anywhere near the amount of armour they need for fresh troops."
                            LUKKAN @talk 'So what did Alcott do? Well, he wanted to use a cheaper iron-based ore far more readily available that we could use to quickly churn out armour and weapons to every able hand and body.'
                            LUKKAN @talk "Don't get me wrong, this stuff is shite compared to what we {i}used{/i} to have."
                            LUKKAN @talk "But which is better? To have ten men who have average armour and passable swords? Or to have three men with great armour and weapons, but the other seven have nothing?"
                            LUKKAN @talk "The armoury’s ore master though, a man called Charlan Croshire, refused to compromise on quality and fought with Alcott."
                            LUKKAN @talk "So Alcott goes back to Mesamor to replace the Ore master, but Mesamor refused."
                            LUKKAN @talk 'It was a matter of national pride to him, his ego-overrode practicality.'
                            LUKKAN @talk "And that's just ONE example, there are dozens of other decisions Mesamor interfered with that constantly caused issues and resentment." 
                            jump ev_lukkan_tavern_talk_2_menu2
                        'So, what happened next?':
                            LUKKAN @talk '{i}Daggerfall...{/i}'
                            LUKKAN @talk "It wasn't the worst plan to be honest, at least, not at first."
                            LUKKAN @talk "The idea was to split the army into two and strike while the metal was still hot."
                            LUKKAN @talk "Gerano had fallen, but the city of Hamun was surprisingly holding it's own pretty well, as did Inma to the East."
                            LUKKAN @talk 'The idea was for us to lift the sieges at both Inma and Hamun and then re-group to begin a long seige to re-take Fort Rook once those two were secured.'
                            LUKKAN @talk 'Once we re-took Fort Rook, we could establish a new front line and safely leap-frog to any number of regions to support.'
                            LUKKAN @talk 'I was sent to the Eastern Front to relive Hamun, and for a while, it seemed to be working.'
                            LUKKAN @talk 'On our side, we managed to reach Hamun safely and began to help push back the Demorai forces there.'
                            LUKKAN @talk 'The Western Front though? That was a whole different game... Poor bastards.'
                            MC @talk 'Where do you think it went wrong?'
                            LUKKAN @talk 'Take your pick?'
                            LUKKAN @talk "Mesamor refused to listen to Alcott and insisted we didn't wait for the Summer, but struck now just before Winter begun."
                            LUKKAN @talk "Him and the High lords figured that with the Demorai now on the backfoot following the great siege, they wouldn't expect such a quick counter-offensive."
                            LUKKAN @talk 'Mesamor reasoned if we waited till the Summer, we would lose the window of opportunity to strike, and the Demorai forces would have recovered too much by then to nullify whatever offensive we mustered.'
                            LUKKAN @talk '...Which leads into the second major problem.'
                            LUKKAN @talk 'We were already struggling to supply our troops with proper armour and equipment, now, we were moving two massive forces simultaneously and our supply lines simply buckled.'
                            LUKKAN @talk "See that's the thing about Mesamor and all those High Lords, they only focused on the immediate statistics they thought were relevant."
                            LUKKAN @talk 'Things like troop numbers and which weapons were proving most effective in killing Demorai...'
                            LUKKAN @talk "What they were never concerned with though, was considering the amount of {i}food{/i} they'd need to send to these massive forces day to day."
                            LUKKAN @talk "They never considered the possibility that this 'counter offensive' could drag on into the long winter, and that the men would need Winter uniforms."
                            LUKKAN @talk "And that's exactly what happened... Just some half-starved, poorly-equipped nearly frozen to death men in the West."
                            LUKKAN @talk "We had to abandon our plans to meet at Fort Rook and move quickly to reform a new defence line deeper in-land to stop the Demorai and help the straggling forces there."
                            MC @talk "And that's when Alcott had enough?"
                            LUKKAN @talk 'No... The final straw was when Mesamor ordered Alcott to try the same thing {i}again.{/i}'
                            LUKKAN @talk 'He was delusional, telling everyone in Court that we {i}actually{/i} were on the verge of pushing through in the West and should have never retreated, that we should have ordered those men to wait till reinforcements arrived.'
                            LUKKAN @talk 'Gods, I can remember them arguing now...'
                            'Lukkan took a sip of his drink as he began to paraphrase his memory.'
                            LUKKAN @talk "{i}Gather some fresh troops and begin a new offensive at once Alcott! You cannot be such a fool to let this chance slip from your grasp!{/i}"
                            LUKKAN @talk "{i}Find more men!{/i}"
                            "Lukkan boomed, doing his best impression of Alcott's voice."
                            LUKKAN @talk "{i}THERE IS NO MORE MEN TO SPARE FOR YOUR FOOLISH PLANS!{/i}"
                            'Lukkan chuckled.'
                            LUKKAN @talk 'After that, Alcott was imprisoned by Mesamor briefly.'
                            LUKKAN @talk 'By then, most of the war council had enough of Mesamor, and the co-conspirators broke Alcott out and well...'
                            LUKKAN @talk 'The rest is history.'
                            LUKKAN @talk 'Mesamor was usurped and finally this war was run properly.'
                            MC @talk 'Why did Mesamor constantly interfere the way he did?'
                            'Lukkan shrugged.'
                            LUKKAN @talk 'Who knows? Court politics is a funny thing, and I imagine he had his reasons.'
                            LUKKAN @talk "...Or maybe, he really was just mad in the end."
                            LUKKAN @talk "Doesn't matter now though, what's done is done."
                            LUKKAN @talk "Anyway, that's enough history, don't you think."
                            LUKKAN @talk "Now if you don't mind, I'd like finish this drink in peace..."
                            'As Lukkan took a sip of his drink, he seemed pre-occupied with stirred up memories, shaking his head before taking another sip.'
                            MC @talk 'Thank you for talking to me, Lukkan... I will leave you be.'
                            $ LocEnter()