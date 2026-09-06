label qst_beneath_shadows_messenger:
    show mc at cleft with easeinleft
    MESSENGER "Sir knight! Sir!"
    show messenger at cright with easeinleft
    show messenger at blurin, cright_f
    "I ignored the voice for a moment before the young boy rushed out in front of me, clutching a small wax-sealed letter in his hand."
    MESSENGER "Sir knight!"
    menu:
        "You must be confused... I'm not a knight.":
            MESSENGER @talk "Oh, uh, forgive me, mi'lord!"
            MESSENGER @talk "Wearing that armor you looked like one!"
        "What is it, boy?":
            MESSENGER @talk "I - I have something for you!"
    show messenger at nod
    "The young boy carefully handed over the letter to me."
    MESSENGER @talk "Captain Nyx asked me to bring this to you immediately, sir!"
    MC @talk "What's this about?"
    MESSENGER @talk "No idea, sir; I'm only paid to deliver letters, not read them!"
    MESSENGER @talk "Now, if you'll excuse me, I have more letters to be delivered urgently!"
    hide messenger with easeoutleft
    "As the boy scurried off, I looked down towards the letter and unsealed it."
    "Rolling out the page, I glanced over its contents."
    "{i}Head to the Weeping Heart this evening; there is someone you need to meet. - N{/i}"
    $ QstSetProgress(PrimerBeneathTheShadows, 1)
    $ NoteUnlock("QstBeneathShadowsPrimerNote")
    MC "(Hmm... Interesting.)"
    MC "(I wonder what this is about?)"
    $ LocEnter()

################################################################################################################
label qst_beneath_shadows_enter_bordello_meet_carina:
    show arwen at center_f with dissolve
    if QstGetProgress(DialogueArwen) == 0:        
        ARWEN @talk "Ooh! You're new!"
        ARWEN @talk 'Arwen, a pleasure to make your acquaintance.'
        $ QstSetProgress(DialogueArwen, 1)
        $ CharMeet("arwen")
        ARWEN @talk 'What may I call you?'
        MC @talk '[player_name!t].'
        ARWEN @talk "[player_name!t]?"
        "She turned serious as she looked me up and down."

    ARWEN @talk "The boss wants to speak to you."
    MC @think "The boss?"
    ARWEN @talk "She said you'd be by; she asked me to take you to her."
    MC @talk "... Very well."
    $ NoteLock("QstBeneathShadowsPrimerNote")
    scene black with dissolve
    
    "After a short walk through one of the well-lit corridors, Arwen took me into a small, well-decorated room." 
    $ LocSet("novaras_bordello_office")
    $ LocFlush()
    show carina at cleft_f
    with dissolve
    show arwen at right_f with easeinright
    ARWEN @talk "He's here."
    show carina at blurin, cleft
    show mc at cright_f with easeinright

    CARINA @smile "Wonderful."
    CARINA @smile "I've been looking forward to meeting you."
    show arwen at blurin, right
    $ Pause(0.1)
    hide arwen with easeoutright
    "As Arwen left, I couldn't help but stare somewhat dumbfounded at the beautiful, sensual woman before me."
    "As attractive as even the most expensive courtesans could be, this woman was breathlessly beautiful."
    CARINA @talk "... My, it's been a while since I've found a man so..."
    
    "She looked me up and down, taking a drag of her pipe."
    CARINA @smile "{i}Interesting.{/i}"
    CARINA @talk "I am Carina Calworth, the owner of this establishment and a few more."
    hide carina
    show cg_carina_smoke_normal at cleft
    with dissolve
    CARINA @talk "Though, I was far more famous when I was... {i}Working.{/i}"
    "The more I think about the name, the more familiar it seems."
    MC @surprised "...You were the courtesan in Lord Halchek's scandal!"
    "A scandal that rocked all of Alderay just a few years ago, Lord Halchek, handsome, young and married to his beautiful wife, seemed like the perfect couple."
    "Romantic tales were often spun about him and his wife, and the promise of a {i}new,{/i} young aristocracy not embroiled in the corruption of old."
    "...That was until he was caught red-handed in the bed chamber of Carina Calworth's embrace."
    CARINA @talk "I must admit... Of all my dalliances and affairs, I'm always disappointed when people mention that one."
    CARINA @smile "I used to tend to the most powerful of diplomats and lords... Foreign kings willing to pay forty-thousand coins a night for me."
    "Carina's eyes seem almost starry as she thinks back nostalgically on that time."
    CARINA @talk "But no, my clumsy 'fun' with Lord Halchek is the one they remember."
    CARINA @smile "I can assure you, I've brought {i}far{/i} better men to their knees."
    hide cg_carina_smoke_normal
    show carina at cleft
    with dissolve
    $ CharMeet("carina")
    MC @think "...I wasn't brought here for you to reminisce, I take it."
    CARINA @smile "Fine, business it is then."
    CARINA @talk "As I'm sure you're aware, Novaras is a complicated place."
    CARINA @talk "So many wolves in the same den... All vying to take control."
    CARINA @talk "All too quickly devoured by the others once they sense a moment's weakness."
    MC @talk "And that's what you are?"
    MC @think "One of these wolves you speak of?"
    CARINA @talk "Of a sort... I know my place in the den, and I'm happy to continue {i}keeping{/i} it as is."
    MC @serious "I still fail to see what this has to do with me."
    CARINA @talk "It's quite simple, Captain Nyx and I have an... {i}arrangement.{/i}"
    CARINA @talk "She ignores some of the businesses, and I supply her with the necessary information about the real goings on of the city."
    MC @serious "And you're telling me this because...?"
    CARINA @smile "It's simple; sometimes, I ask the good captain to do a few favors for me."
    CARINA @talk "I, in turn, return the favors to keep our relationship healthy."
    CARINA @smile "Do you understand?"

    menu qst_beneath_shadows_enter_bordello_meet_carina_menu:
        "Captain Nyx is honest; she wouldn't strike deals like this!":
            show carina laugh
            "The woman laughed."
            CARINA @laugh "Oh my...!"
            CARINA @smile "That's adorable!"
            CARINA @smile "She is quite a talented woman, always willing to do what's necessary to maintain law and order."
            show carina talk
            CARINA @talk "Despite her limited resources."
            CARINA @talk "It's almost a shame though... With a body like hers, she could have easily avoided half the stress in her life if she chose a different path!"
            MC @angry "Is this going somewhere?"
            CARINA @talk "It's quite simple; the dear captain is usually in an impossible situation."
            CARINA @smile "Rather than fight all the wolves in the den, she's wisely chosen to ally herself with the most amicable ones like myself."
            jump qst_beneath_shadows_enter_bordello_meet_carina_menu

        "What makes you better than all the other 'wolves' in the den?":
            CARINA @talk "My girls are all cared for... None are enslaved or imprisoned."
            CARINA @talk "The Raza and other vices we keep as low and controlled as we can to avoid raising the ire of the guards."
            CARINA @talk "And murder is bad for business... I run safe, {i}mostly{/i} legal establishments."
            CARINA @talk "I'm usually also the one to mediate between the most blood-thirsty of the wolves and the city guard when things become too violent even for this city."
            jump qst_beneath_shadows_enter_bordello_meet_carina_menu

        # Continues
        "So what do you want from {i}me?{/i}": 
            pass

    CARINA @talk "Tonight, I need you to meet a few contacts of mine."
    CARINA @talk "Take the earnings from each of them, if any give you any trouble..."
    CARINA @talk "Feel free to do with them as you wish."
    MC @talk "And why exactly am I doing this for you?"
    CARINA @smile "I've heard a lot about you... I assure you, {i}the reward is worth it.{/i}"
    CARINA @talk "But, I'll also throw in three hundred coins on top."
    menu:
        "A good business relationship is built on trust, and I don't trust you yet... Four hundred coins." (Req_Barter = 9):
            $ QstBeneathTheShadows().RewardGold = 400
            CARINA @smile "You're a brave one, aren't you?"
            CARINA @talk "Fine, four hundred coins."
            menu:
                "For Captain Nyx's sake... I shall see to it.":
                    CARINA @smile "I have every faith in your abilities." 
                    pass

                "And I want to see you take your clothes off." (Req_Charm = 10):
                    $ QstBeneathTheShadows().RewardUndress = True
                    CARINA @surprised "{i}...You what?{/i}"
                    MC @lewd "Did I stutter?"
                    CARINA @surprised "..."
                    CARINA @laugh "Hahahaha!"
                    CARINA @smile "Men have died for saying less."
                    CARINA @lewd "I just {i}knew{/i} you'd be something quite special."
                    CARINA @smile "Anyone able to capture that ice queen's attention has to be."
                    MC @lewd "So, do we have a deal?"
                    CARINA @lewd "Nobles would have paid me upwards of ten thousand coins just for a peek, you know..."
                    CARINA @lewd "And here you are so brazenly asking for it."
                    MC @lewd "Would it make you feel better if I also took my clothes off?"
                    CARINA @lewd "...Mmmm."
                    CARINA @smile "{i}...Deal!{/i}"
                    CARINA @talk "Now, don't disappoint me!"
                    CARINA @talk "After THAT request, I'd {i}hate{/i} to have your balls cut off for failing me!" 
                    pass

        "For Captain Nyx's sake... I shall see to it.":
            CARINA @smile "I have every faith in your abilities." 
            pass

        "I'll think about it.":
            CARINA @smile "I'm afraid this wasn't a request."
            CARINA @talk "{i}Consider it an order from Captain Nyx herself.{/i}"
            menu:
                "Fine...":
                    CARINA @smile "Good, glad we're on the same page then."
                    pass

                "I don't take kindly to threats.":
                    CARINA @smile "I can assure you..."
                    CARINA @angry "If I was {i}threatening{/i} you, you'd know about it."
                    pass

    MC @think "Where are these contacts of yours I'm supposed to meet?"
    CARINA @talk "I see you have a city map with you..."
    # new 3 goals: Collect Carina's money
    $ QstStart(QstBeneathTheShadows)
    $ GoalShow(QstBeneathTheShadows, 10)
    $ GoalShow(QstBeneathTheShadows, 20)
    $ GoalShow(QstBeneathTheShadows, 30)
    CARINA @talk "I'll mark their locations for you."
    CARINA @talk "Remember, I don't tolerate excuses... Make sure they bring me what they owe."
    MC @talk "Understood."
    CARINA @talk "Now go, return once you bring me back what's mine."
    show mc at blurin, cright
    $ Pause(0.1)
    hide mc with easeoutright
    $ Pause(0.1)
    show carina at center with ease
    show carina at blurin, center_f
    CARINA @lewd "...Mmmm... My dear captain."
    CARINA @lewd "You are a bad girl, aren't you?"
    $ LocEnter()

##########################################################################################################################################
#Quest update: The 3 contacts are available to select exploring Novaras. 1.) Market district alleyway 2.) Poor district - MC home map section, 3.) Mage district
######## market district
label qst_beneath_shadows_dealer_market_dist:
    show cg_dealer at center with dissolve
    DEALER "And what do you want?"
    menu:
        "You've been holding out on Carina... That's good, I've been spoilin' for another kill." (Req_Perk = "terrifying"): 
            DEALER "H-Hold on now!"
            DEALER "Uhh, t-there's no need for violence!"
            DEALER "H-Here!"
            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
            DEALER "Tell Carina it won't happen again!"
            pass

        "Carina sends her regards... She wants her tribute.":
            DEALER "Bahh! Now, hold on a minute!"
            DEALER "I was going to bring it to her! I just uhh..."
            DEALER "I've kinda been robbed."
            MC @think "Robbed?"
            DEALER "They took the cut I planned to give Carina."
            DEALER "If you can get it back, it's all yours..."
            DEALER "Oh, and uhh..."
            DEALER "If you could apologize to Ms Calworth for me and let her know it won't happen again, I'd be grateful, friend."
            menu:
                "Fine, where are they?":
                    DEALER "I can lead you to them..."
                    DEALER "Follow me."
                    scene black with dissolve
                    "A short walk down a dark alley later..."
                    scene bg_alleyway_night
                    show cg_dealer at center
                    with dissolve
                    show cg_bandit_dark onlayer characters as bandit1:
                        xcenter 0.2
                        zoom 1.0
                    with dissolve
                    show cg_bandit_dark onlayer characters as bandit2:
                        xcenter 0.8
                        zoom 0.9
                        xzoom -1.0
                    with dissolve
                    show cg_bandit_dark onlayer characters as bandit3:
                        xcenter 0.7
                        zoom 0.8
                        yoffset 50
                        xzoom -1.0
                    with dissolve
                    BANDIT "Well, well, look what we have here."
                    BANDIT "Who's this then?"
                    show cg_dealer at shake
                    DEALER "Just another fool in way over his head..."
                    MC "(Fuck.)"
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_battle_generic")
                    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys_night", CharIDList_Right = [{"e_thug":6}, {"e_thug":5}, {"e_bandit":4}], CanTransform = False))
                    scene bg_alleyway_night
                    show cg_dealer at center
                    with dissolve
                    $ AutoMus(True)
                    show cg_dealer at shake
                    DEALER "N-Now, hold on now! Uhh!"
                    DEALER "T-They made me do that, you see? It w-was all their idea!"
                    menu:
                        "Take the coins":
                            "Reaching out, I snatched the bag of coins from his person as he cowered backwards."
                            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
                            MC @angry "Get the fuck out of here."
                            DEALER "T-Thank you!"
                            hide cg_dealer with easeoutleft
                            pass

                        "Kill the dealer":
                            "Not wanting to hear any more of the pitiful lies spewed from his mouth, I drew my blade and quickly cut the treacherous fool down."
                            hide cg_dealer with moveoutbottom
                            play sound "audio/cfx/body_collapse.ogg"
                            "He let out a sharp, shocked final gasp as his body hit the floor."
                            "Warm, red blood slowly pooled around him as I grabbed the bag of coins from his person."
                            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
                            pass

                "This sounds like bullshit... Do you really want to cross Carina Calworth... {i}Or me?{/i}" (Req_Charm = 9):
                    DEALER "... R-Right, uhh, now that you mention it."
                    DEALER "Perhaps I have some coins to spare, heh heh, no uhhh..."
                    show cg_dealer at nod
                    $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
                    DEALER "No hard feelings, right?"
                    pass

                "{i}*Grab the man by the throat and lift him up*{/i}" (Req_Strength = 10):
                    DEALER "G-Ghhhhfhh!!"
                    DEALER "C-Can't! Breathe!"
                    "The man squirmed and kicked in my hand as I held him there, my hand tightly wrapped around his throat."
                    MC @talk "No more lies... Hand over the coin, or I snap your neck like a twig."
                    "Weakly, the man reached to his side to grab a small bag of coins, which he handed over to me."
                    menu:
                        "Kill him anyway.":
                            "With one sharp twist, I heard the neck crunch as he suddenly became motionless."
                            hide cg_dealer with moveoutbottom
                            play sound "audio/cfx/body_collapse.ogg"
                            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
                            "Tossing his body to the ground, I carefully stored the bag of coins before moving on."
                            pass

                        "Let him go.":
                            "Releasing my grip, the man dropped to his knees, coughing and wheezing as I snatched the coins from him."
                            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
                            "Without another word, the man sprinted and ran for his life."
                            hide cg_dealer with easeoutright
                            "Carefully, I stored the bag of coins before moving on."
                            pass

    $ GoalComplete(QstBeneathTheShadows, 10)
    if all([IsGoalComplete(QstBeneathTheShadows, 10), 
            IsGoalComplete(QstBeneathTheShadows, 20), 
            IsGoalComplete(QstBeneathTheShadows, 30)]):
        $ GoalShow(QstBeneathTheShadows, 40)
    $ LocEnter()

######## 2.) housing dist
label qst_beneath_shadows_dealer_house_dist:
    show cg_dealer at center with dissolve
    DEALER "Hey, you lookin' for something to spice up your night, eh?"
    MC @talk "I'm here to collect."
    MC @talk "You owe Carina Calworth some tribute."
    DEALER "Tsch!"
    DEALER "Fuck the whore!"
    DEALER "Why should I give that slut anything?"
    menu:
        "Because I'll just kill you where you stand now?":
            DEALER "You can try!"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys_night", CharIDList_Right = [{"e_thug":6}, {"e_thug":5}, {"e_bandit":4}], CanTransform = False))
            $ LocFlush()
            show mc at center
            with dissolve
            $ AutoMus(True)
            "As the dealer slumped dead to the floor, I grabbed the bag of coins on him and left before anyone might see me."
            show mc at nod
            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
            hide mc with easeoutright
            pass

        "You're a nobody street dealer... Do you really think you're in a position to make enemies?" (Req_Barter = 9):
            DEALER "Ha! Who in all the damn hells are you calling a nobody!"
            DEALER "This whole cities going to remember my name!"
            MC @angry "Use your head."
            MC @talk "If you wanna make your name, you need to start proving yourself an asset to people."
            MC @talk "Prove you are someone reliable."
            MC @talk "What does robbing your boss for a few coins tell people?"
            MC @angry "That you're just a thief and a nobody who shouldn't be trusted with anything serious."
            DEALER "... Mmm."
            DEALER "Maybe you're onto something."
            DEALER "I guess I should bide my time more."
            DEALER "Here, take the damn coins."
            show cg_dealer at nod
            DEALER "You better remember me, though!"
            DEALER "When I run this city, you'll collect the 'tributes' for ME!"
            hide cg_dealer with easeoutright
            "The man dropped the bag of coins at my feet before storming off."
            $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
            MC "(What a fucking idiot.)"
            BLACK "{i}(Do not let the weaker male bother you.){/i}"
            BLACK "{i}(He will be dead in six months.){/i}"
            MC @think "How do you know that?"
            BLACK "{i}(He is impulsive and violent while being physically and mentally incapable to match his temper.){/i}"
            "I couldn't help but lightly snicker at the comment."
            pass

    $ GoalComplete(QstBeneathTheShadows, 20)
    if all([IsGoalComplete(QstBeneathTheShadows, 10), IsGoalComplete(QstBeneathTheShadows, 20), IsGoalComplete(QstBeneathTheShadows, 30)]):
        $ GoalShow(QstBeneathTheShadows, 40)
    $ LocEnter()

######## #3.) mage district
label qst_beneath_shadows_dealer_mage_dist:
    show cg_dealer at center with dissolve
    DEALER "You lookin' to make your night a little more interesting, friend?"
    MC @talk "I'm here to collect for Carina Calworth."
    DEALER "Hm? Ah... One moment."
    show cg_dealer at nod
    $ PlayerAddItem("gold", QstBeneathTheShadows().CollectAmount)
    "The man handed over the bag of coins to me."
    DEALER "You aren't the usual one she sends."
    MC @talk "Well, I am the one she's sent today."
    DEALER "Mmm..."
    MC @think "I'm surprised, I expected a lot more..."
    MC @talk "{i}Resistance,{/i} from you."
    DEALER "Some of the young pups with egos have something to prove."
    DEALER "But business is good, and the boss rewards those she can trust."
    $ GoalComplete(QstBeneathTheShadows, 30)
    MC @talk "I see..."
    DEALER "If you need anything, come to me first, by the way."
    $ QstStart(NovarasDealer)
    DEALER "I'll give you the good stuff, heh."
    menu:
        "Show me what you've got.":
            DEALER "Take a look..."
            call screen trade(ShopNovarasDealer)
        "I'm good.":
            DEALER "Should you change your mind..."
    DEALER "You know where to find me."
    if all([IsGoalComplete(QstBeneathTheShadows, 10), IsGoalComplete(QstBeneathTheShadows, 20), IsGoalComplete(QstBeneathTheShadows, 30)]):
        $ GoalShow(QstBeneathTheShadows, 40)
    $ LocEnter()

########################################################################################################################################################
#Returning to Carina 
label qst_beneath_shadows_talk_carina_office:
    CARINA @talk "Have you finished yet?"
    menu:
        "Here." (Req_Gold = QstBeneathTheShadows().CollectAmount * 3) if all([IsGoalComplete(QstBeneathTheShadows, 10), IsGoalComplete(QstBeneathTheShadows, 20), IsGoalComplete(QstBeneathTheShadows, 30)]):
            pass
        "Not yet.":
            CARINA @angry "Then what are you waiting for?"
            CARINA @angry "Chop! Chop!"
            $ LocEnter()

    $ PlayerRemItem("gold", QstBeneathTheShadows().CollectAmount * 3)
    CARINA @smile "Ahhh! I just KNEW you could be counted on!"
    CARINA @smile "Now, first things first, your reward..." #Carina pays the player 
    show carina at nod
    $ PlayerAddItem("gold", QstBeneathTheShadows().RewardGold)

    if QstBeneathTheShadows().RewardUndress == True: 
        MC @think "... And the {i}other{/i} reward?"
        "Carina smirked,"
        CARINA @smug "Oh... You want, {i}that.{/i}"
        CARINA @smug "Tell me, was the coin a greater motivator..."
        CARINA @lewd "Or a chance to see my body?"
        MC @bitelip "{i}I think we both know the answer to that?{/i}"
        CARINA @horny "Ahh... It's been so long since I felt like this."
        $ CharSetClothes("carina", "naked")
        $ PlaySoundRandom("tentFlap")
        show carina at nod
        "Carina softly chuckled, letting the dress slip off from her."
        "Her naked body exposed, she stared excitedly at me, her nipples hardening in the cool air as my eyes wandered lustfully over her body."
        CARINA @horny "{i}Was it worth it?{/i}"
        "My cock stiffened almost painfully hard at the sight of her groomed red bush and wet cunt."
        MC @lewd "{i}Every coin.{/i}"
        "Carina smirked again, satisfied with my answer as she began to put her clothes back on."
        $ CharSetClothes("carina", "normal")
        $ PlaySoundRandom("tentFlap")
        show carina at nod
        CARINA @lewd "Maybe next time I'll give you something more than just a quick look..."
        CARINA @talk "Now, where were we before we got... {i}distracted?{/i}"
        CARINA @smile "Ah, yes... Your future employment."
        MC @think "My future employment?"

    MC @talk "Thanks..."
    CARINA @talk "I could really use someone like you."
    CARINA @talk "Capable, reliable people are so hard to come by these days..."
    MC @think "Aren't you just going to summon me again no matter what?"
    CARINA @talk "Haha... Well, like I said, I can only {i}borrow{/i} you from the fair captain time from time."
    CARINA @talk "But if you were to walk in on your own and ask for more work, well..."
    "Carina smiles."
    CARINA @smile "I'm sure I could use your talents."
    MC @talk "Will that be all?"
    CARINA @talk "Not quite..."
    CARINA @smile "I promised you your {i}real{/i} reward, didn't I?"
    MC @think "My {i}'real'{/i} reward?"
    CARINA @smile "Come... Follow me."
    hide carina with easeoutright
    scene black with dissolve
    "Led down through one of the many winding hallways of the brothel, each room I walk past, I occasionally hear the sounds of moans, grunts and flesh slapping together as I pass on by."
    "The sweet smell of candles and incense did its best to mask the scent of sex and sweat, but to my hyper senses, it wasn't enough."
    "As I watched Carina's butt sway lightly from side to side, I couldn't help but feel aroused."
    $ LocSet("novaras_bordello_sex_dungeon")
    $ LocFlush()
    show carina at cleft
    with dissolve
    show mc at left with easeinleft
    CARINA @smile "Andddd..."
    CARINA @smile "We're here."
    show mc at cright with easeinleft
    $ Pause(0.25)
    show mc at blurin, cright_f
    MC @think "What is this place?"
    CARINA @smile "This room is a {i}special{/i} room."
    CARINA @talk "We deal with all kinds of clients here, you see."
    CARINA @talk "Men and women of all walks of life..."
    CARINA @talk "But {i}some{/i} of our most prestigious clients, those with reputations on the line, would never willingly want to be seen associating in a place like this."
    CARINA @smile "So... We created the red room just for them."
    CARINA @smile "A place where nobles, holy mages, and our {i}betters{/i} can behave like the depraved whores they are."
    MC @think "And why would they trust you with their secrets?"
    CARINA @smile "Because they pay me well for the privilege of not only keeping their secrets but letting them indulge in their darkest desires..."
    CARINA @talk "And for your continued services, I'm giving {i}you{/i} membership to use this room."
    MC @talk "All I did was run you an errand..."
    CARINA @laugh "Hahaha!"
    CARINA @smile "{i}You're going to do so much more than that...{/i}"
    CARINA @talk "Now, here's how it works."
    CARINA @talk "You simply write down on that list who you want invited to join you in the evening next to your initials, and we'll do the rest."
    MC @think "Just like that?"
    CARINA @smile "Just like that."
    $ IsGoalComplete(QstBeneathTheShadows, 40)
    $ QstComplete(QstBeneathTheShadows)
    CARINA @smile "Anyway, tours' over, so... Have fun."
    show carina at blurin, cleft_f
    $ Pause(0.1)
    hide carina with easeoutleft
    "With that, Carina turned and left me to own devices, inspecting the strange room filled with all sorts of sexual contraptions."
    show mc at blurin, cright
    show mc at center with ease
    MC "(I had heard some rumors about places like this existing, but...)"
    MC @surprised "(I didn't realize one was so close by this whole time!)"
    MC @think "(I wonder just how 'prestigious' some of these members really are?)"
    $ LocEnter()