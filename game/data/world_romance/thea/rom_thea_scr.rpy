
label rom_thea_invite:
    THEA @smile "... Would you be interested perhaps in buying me a drink this evening?"
    MC @smile "What's brought this on?"
    THEA @blush "I've been watching you ... You're already C-tier so fast, normally, it would take adventurers weeks or even months to get where you are."
    THEA @blush "I suppose I want to see what's so special."
    menu:
        "Shall I see you at the {i}Iron Unicorn{/i} tonight then?":
            THEA @blush "I would like that."
            THEA @smile "I'll be waiting for you there ..."
            $ QstSetProgress(RomanceThea, 1)
            $ NoteLock("romanceTheaInvite")
            $ NoteUnlock("romanceTheaDate")

        "I'm sorry, I'm too busy right now.":
            THEA @talk "I-"
            THEA @talk "Very well, let me know when you're more free, perhaps."
    return


label rom_thea_unicorn:
    if day < QstGetDelayVal(RomanceThea):
        MC "(I shouldn't bother her anymore tonight.)"
        $ LocEnterQ()

    else:
        scene bg_tavern_night
        show thea at cright_f
        with dissolve
        "When Thea saw me from across the room, she smiled and waved, coaxing me over."
        THEA @talk "So glad you could make it."
        THEA @smile "Come, join me for a while ..."
        show mc at cleft with easeinleft
        menu rom_thea_unicorn_menu1:
            "Can I get you a drink?":
                THEA @smile2 "Mmm, eager to spend all that coin you've earned adventuring, are you?"
                THEA @smile "There's a nice wine bottle I've been eyeing up, {i}'Huville Cépage'{/i}"
                THEA @talk "What do you say we share it?"
                $ choicemenu = False
                menu rom_thea_unicorn_menu2:
                    "One bottle coming right up." (Req_Gold = 100): #requires 100 coins - gives 1 point to Thea
                        $ PlayerRemItem("gold",100)
                        $ CharChangeRel("thea", 1)

                        THEA @smile2 "Oooh!"
                        "I ordered for the bottle to be fetched, placing the small pouch of coins in Shay's hand as she grabbed it for us."
                        THEA @smile "Cheers!"
                        MC @talk "So then, how does a girl like you end up running the Adventures Guild in Novaras?"
                        THEA @smile "Ahh ... good question!"
                        THEA @talk "My parents travelled to Alderay to settle when I was very young."
                        THEA @talk "Back then, Alderay was welcoming skilled businesses and migrants, and the old owner of the guild house here was ready to retire."
                        THEA @talk "So, we bought it off them, and the rest is history."
                        MC @talk "Where did you come from originally?"
                        THEA @talk "Ah, my family comes from Ramon."
                        MC @surprised "Ramon? But, you're-"
                        'I stopped myself from prodding too deeply, but Thea just smiled.'
                        THEA @smile "It's fine, people always ask about my complexion."
                        THEA @talk "You see, we all come from Ramon, but my people, the Khashan, come from the eastern side of the Darjan desert."
                        THEA @talk "The first of us travelled to Alderay to avoid the many hardships of the land."
                        THEA @talk "Unlike the West and South-Lands, the East of Ramon is a hard place to live ... Nothing truly grows beneath the scorched sun."

                        $ choicemenu = set()
                        menu rom_thea_unicorn_menu3:
                            "Do you miss it at all?" if 1 not in choicemenu:
                                THEA @talk "Hmm ... I miss the Darjan mountains, they stretched as far as the eye could see."
                                THEA @talk "As barren and brutal a place as it was to live, it was quite beautiful."
                                $ choicemenu.add(1)
                                if len(choicemenu) < 3:
                                    jump rom_thea_unicorn_menu3

                            'You say you were part of the first wave to travel to Alderay ... What do you think of the Ramonians here now?' if 2 not in choicemenu:
                                THEA @angry "What's there to say? They're a greedy, ungrateful bunch."
                                MC @talk "That's ... surprising to hear."
                                THEA @sad "Sorry, Ramonian politics is a difficult thing."
                                THEA @angry "Let's just say there are reasons we headed to Alderay and didn't just join our cousins in the West."
                                THEA @angry "They spent years being the oppressors, and now expect sympathy when they wouldn't shed a tear for the rest of us."
                                $ choicemenu.add(2)
                                if len(choicemenu) < 3:
                                    jump rom_thea_unicorn_menu3

                            "What was it like growing up in a guild house?" if 3 not in choicemenu:
                                THEA @smile "Ahh, it was ... different!"
                                THEA @talk "I grew up watching adventurers come and go."
                                THEA @smile "I quickly learned to pick up which ones I thought had a chance of climbing the ranks, and I usually got pretty good predicting where their limit would be."
                                $ choicemenu.add(3)
                                if len(choicemenu) < 3:
                                    jump rom_thea_unicorn_menu3

                        menu:
                            "How far do you think I'll get?":
                                THEA @smile "Where's the fun in telling you that?"
                                THEA @smile2 "{i}... Surprise me.{/i}"

                            "You must have seen some legends walk through those doors back then...":
                                THEA @talk "Quite a few."
                                THEA @talk "Lohan the Great, Marhaka {i}'the silver arrow.'{/i}"
                                THEA @sad "But that was all when I was still little."
                                THEA @talk "There aren't really many names left who'd I'd think qualify as legendary these days."
                                MC @talk "What about Celeste?"
                                THEA @sad "I-"
                                THEA @sad "There's something about her I don't like ... But I can't put my finger on why."
                        #Both choices continued

                        MC @smile "So, why did you only agree to meet with me now?"
                        "Thea smiled, twirling her hair."
                        THEA @smile "Well ... You see, the thing is."
                        THEA @smile "I usually spent my time growing up watching adventurers flirt with my mother, and I guess it kinda rubbed off on me."
                        MC @talk "What about your father, though? He couldn't have liked that."
                        THEA @talk "There wasn't a lot he could do, besides, Mother was just flirting to buy a few more rounds between quests."
                        THEA @blush "T-Though sometimes the adventurers did get a little 'handsy' with her, I suppose."
                        THEA @smile "But I'm sure she never let it go too far!"
                        MC "(I think I'm beginning to see where this fetish of hers has come from)."
                        THEA @smile2 "So, how would you like to come back to mine this evening?"
                        THEA @blush "I think I might have something to help {i}'motivate'{/i} you on your quests."
                        menu:
                            'Lead the way.':
                                THEA @smile2 "Follow me."
                                jump rom_thea_after_date
                            'Ah, another night perhaps.':
                                THEA @sad "Oh? Well ... Alright then."
                                $ QstSetDelay(RomanceThea, 1)
                                $ LocEnter()

                    "Sounds expensive." if not choicemenu:
                        THEA @smile "It is."
                        THEA @smile2 "But do you think I'm worth it?"

                        $ choicemenu = True
                        jump rom_thea_unicorn_menu2
                    
                    "I'm afraid I can't afford that right now.":
                        THEA @sad "{i}*Sigh*{/i}... Never mind then."
                        THEA @talk "Mmm, don't you think you should at least buy a girl a drink first?"
                        THEA @talk "You should definitely buy me one when you have some more coin... I'd love to hear more of your adventuring tales."

                        $ QstSetDelay(RomanceThea, 1)
                        $ LocEnter()
            "I'm afraid I'm busy tonight, perhaps next time.":
                THEA @talk "Booo ..."
                THEA @smile "Well maybe next time then."

                $ QstSetDelay(RomanceThea, 1)
                $ LocEnter()

label rom_thea_after_date:
    if not RomanceThea().eveningBoobjob: # First time
        $ AutoMus(False)
        $ AutoAmb(False)
        stop music fadeout 3.0
        stop ambience fadeout 3.0
        scene black with dissolve
        $ PlayMusic("audio/music/7_novaras_d.ogg")
        'Thea led me back towards the Adventurers Guild, but this time, she led me behind the counter up the stairs towards her bedroom.'
        play ambience "audio/ambience_scenes/campfire.ogg" fadein 3.0
        scene bg_thea_room
        show thea at cright_f
        show mc smile at cleft
        with dissolve
        'Into her bedroom, Thea led me, quickly getting the fire going before she twirled around and smiled alluringly.'
        MC @smile "So then, what was it you wanted to give me?" #From here - the repeatable sections of this scene begin
    else: # Repeated event
        show thea at cright_f
        with dissolve
        show mc smile at cleft with moveinleft
        THEA @smile "Ah, hello again... I trust you've been busy with all your adventures?"

    THEA @talk "Do you mind waiting here for a moment, this will only take a few minutes."
    MC @smile "Of course."
    hide thea with dissolve
    'Thea hurried off for a few moments, and after briefly looking around her room, the door swung open, and Thea re-emerged.'
    #Show Thea dressing gown
    $ CharSetClothes("thea", "gown")
    show thea blush at cright_f with dissolve
    THEA @blush "{i}... Do you think 'this' will help motivate you?{/i}"
    MC @lewd "I'm feeling motivated already."
    #Fade to black
    scene black with dissolve
    'Giggling to herself, Thea stepped forward and pushed me down onto her bed, moving swiftly to strip the clothes off of me.'
    THEA "I've been working on a little ... {i}dance{/i} that I want to show you."
    THEA "Tell me ... What do you think of what I'm wearing?"
    menu:
        "I like it. Keep it on.": #triggers robe and lingerie dance animations
            $ CharSetClothes("thea", "gown")

        "I prefer what's underneath.": #triggers lingerie only dance animations
            $ CharSetClothes("thea", "ling")

        "Take it all off ... It's in the way of what I really want.": #Triggers nude dance animations
            $ CharSetClothes("thea", "naked")
    THEA "Just keep still ... {i}You're going to enjoy this.{/i}"

    $ PlayMusicRandom("mus_sex")
    $ AutoMus(False)
    $ HideUI(True)

    #All choices continued - First dance animation - front
    if CharGetClothes("thea") == "gown":
        scene ss_thea_firstdate_gown_1 with dissolve
    elif CharGetClothes("thea") == "ling":
        scene ss_thea_firstdate_ling_1 with dissolve
    elif CharGetClothes("thea") == "naked":
        scene ss_thea_firstdate_naked_1 with dissolve

    $ Pause()
    'As Thea danced sensuously in front of me, the light from the fireplace flickered.'
    'Her hips swayed gently from side to side as her sultry eyes refused to leave me alone.'
    THEA "I've been thinking about this since the moment I first saw you."
    THEA "There's just something so ... {i}different{/i} about you."
    "The flickering flames shifted behind her as she run her hands up her body, cupping and squeezing at her breasts."
    "The room quickly became hot, and the trickle of sweat running down her black skin was illuminated by the flame's glow."
    "My eyes greedily run down her body, moving down from her tits to staring hungrily between her thighs."
    MC "Thea ..."
    MC "You look so-"
    THEA "Shhh, don't talk."
    THEA "{i}Just watch.{/i}"
    if CharGetClothes("thea") == "gown":
        scene ss_thea_firstdate_gown_2 with dissolve
    elif CharGetClothes("thea") == "ling":
        scene ss_thea_firstdate_ling_2 with dissolve
    elif CharGetClothes("thea") == "naked":
        scene ss_thea_firstdate_naked_2 with dissolve
    $ Pause()
    'Thea turned around with a sultry smile.' #Cut to second animation - back 
    'She sensually sway her hips enticingly as she looked over her shoulder at me.'
    "My eyes were unable to look away from her round, tight looking ass as Thea run her hands over her body once again."
    THEA "See something you like?"
    MC "Your ass looks incredible."
    'Thea laughed as she lightly shook her butt in front of me.'
    THEA "Haha ... I can feel the eyes watching me as I walk past."
    "As my cock hardened in front of her hot body, Thea's eyes looked down towards the standing appendage and she grinned."
    THEA "Seems I'm not the only one {i}blessed{/i} with assets."
    MC "Oh, so {i}you{/i} like what you see too, I take it?"
    THEA "Fufu~"
    #Fade to black 
    THEA "Alright, enough teasing."
    THEA "Time for the {i}real{/i} reward. {image=[ICON.HEART]}"
    if CharGetClothes("thea") == "gown":
        scene ss_thea_firstdate_gown_3 with dissolve
    elif CharGetClothes("thea") == "ling":
        scene ss_thea_firstdate_ling_3 with dissolve
    elif CharGetClothes("thea") == "naked":
        scene ss_thea_firstdate_naked_3 with dissolve
    $ Pause()
    #Cut to titjob animation (changes depending on level of clothes she wearing)
    'With her tits wrapped around my cock, Thea began to stroke my cock wedged between her breasts.'
    'Hot breath touched my member as she moved rhythmically up and down, biting down on her lower lip.'
    THEA "Do you like that?"
    THEA "Do you like seeing your huge cock shoved between my tits?"
    MC "Ahh! Thea!"
    MC "Mmfgh...!"
    'I grunted in pleasure as Thea continued to teasingly massage my member, biting down on her lower lip as she giggled to herself.'
    'Occasionally, Thea would spit down onto my cock, using it as a kind of lube to help as she now moved faster.'
    MC "Mmh! Thea!"
    BLACK "({i}She has exceptional talents as a breeding mate{/i})."
    THEA "Tell me how good it feels~"
    MC "Mhhff! You're d-doing a great job! Hrghh!"
    MC "{i}*Huff*{/i} Not sure how much longer I can hold on like this!"
    "Thea laughed softly to herself again, moaning softly to herself as continued for some time, letting the pleasure slowly build."
    THEA "That's it ... Mhhfgh!"
    THEA "I can feel how close you are ..."
    THEA "Come on, do it ... You know you want to!"
    THEA "Cover this fucking wench in your load!"
    THEA "Show me you can do whatever you want!"
    MC "(Hrgh! I'm so close!)"
    MC "T-Thea! I'm ..."
    MC "G-Grghhhh...!"
    menu: #I'm pretty sure we have swallow variant as well in the PSD, if we don't remove the choice and just do cover Thea 
        'Cover Thea':
            if CharGetClothes("thea") == "gown":
                scene ss_thea_firstdate_gown_face 
            elif CharGetClothes("thea") == "ling":
                scene ss_thea_firstdate_ling_face 
            elif CharGetClothes("thea") == "naked":
                scene ss_thea_firstdate_naked_face
            $ ReduceInfectionFromSex("thea")
            with flash
            $ Pause()
            'Unable to hold back any longer, I grunted loudly, tightening my fists into balls as I covered her tits and face in my hot cum.'
            "Thea giggled and laughed, her eyes wide in surprise at the size of the load."
            THEA "Oh...!"
            THEA "You really were pent up, weren't you, big boy? {image=[ICON.HEART]}"

            $ UnlockGalFlag("thea", "firstdate", "var_face")

        'Make Thea swallow':
            "Grabbing the back of Thea's head, I pulled her forward suddenly, forcing her wet lips over the head of my cock."
            THEA "Mmmfghh...?!"
            if CharGetClothes("thea") == "gown":
                scene ss_thea_firstdate_gown_mouth
            elif CharGetClothes("thea") == "ling":
                scene ss_thea_firstdate_ling_mouth
            elif CharGetClothes("thea") == "naked":
                scene ss_thea_firstdate_naked_mouth
            $ ReduceInfectionFromSex("thea")
            $ Pause()
            "Thea's wide-eyed protests soon stopped as she felt the rush of my warm seed flooding into her mouth."
            "She tried to swallow as much of the load as she could before pulling back to cough up the rest."
            "Some of the excess seed splashed onto her face and dark breasts as she did her best to smile afterwards, eyes slightly watering."
            THEA "That was - {i}*Cough!*{/i} quite the load! {image=[ICON.HEART]}"

            $ UnlockGalFlag("thea", "firstdate", "var_mouth")

    #Both choices continued - sex scene ends

    $ UnlockGalSceneAndGrantXp("thea", "firstdate")
    $ UnlockGalFlag("thea", "firstdate", "var_" + CharGetClothes("thea"))
    $ HideUI(False)
    stop music fadeout 3.0
    $ tmpvar = {}
    $ tmpvar["mc_clothes"] = CharGetClothes("mc")
    $ CharSetClothes("mc", "naked")
    scene bg_thea_room
    show thea smile at cright_f
    show mc smile at cleft
    with dissolve
    MC @smile "Ahh ... Sorry, I didn't realize I was so-"
    THEA @smile2 "Haha, it's fine!"
    THEA @smile "I'm just happy you were blessed with such a fine ... {i}sword.{/i}"
    MC @lewd "You're more than welcome to polish it anytime you please."
    THEA @smile2 "Don't mind if I do then, fufu~"
    #cut to black 
    'After that, Thea threw me my clothes, and I began to re-dress myself, playfully remarking she might let me stay the night {i}next time.{/i}'
    hide mc with dissolve
    $ CharSetClothes("mc", tmpvar.pop("mc_clothes"))
    show mc lewd at cleft with dissolve
    THEA @smile "I'm excited to hear about your next adventures."
    MC @lewd "Will they also end up with me being dragged back up to your bedroom?"
    THEA @smile2 "Mmmm, I guess you'll have to wait and see, won't you?"
    scene black with dissolve
    'I left a short time later after a quick kiss goodbye...'
    $ CharAddRelEntry("thea", "after_sex")

    $ CharSetClothes("thea", "normal")
    $ AutoMus(True)
    $ AutoAmb(True)
    $ TimeAdvTo(TIME_LATENIGHT)

    if not RomanceThea().eveningBoobjob: # First time
        $ NoteLock("romanceTheaDate")
        $ QstSetProgress(RomanceThea, 2)
        $ CharSetLover("thea")
    else:
        $ RomanceThea().eveningBoobjob = False
        $ NoteLock("romanceTheaEvening")

    $ LocSet("novaras_dist_market")
    $ LocEnter()



label rom_thea_rep_invite_boobjob:
    #New option replaces the 'date' option with Thea after this scene, asking 'I was wondering if I could visit you again this Evening ...'
    THEA @smile2 "Oh? Is that so?"
    THEA @blush "Come to my room Evening, I'll be waiting~"
    #If player heads up to Thea's room in Evening, lewd scene loops (from line)
    $ RomanceThea().eveningBoobjob = True
    $ NoteUnlock("romanceTheaEvening")
    return
