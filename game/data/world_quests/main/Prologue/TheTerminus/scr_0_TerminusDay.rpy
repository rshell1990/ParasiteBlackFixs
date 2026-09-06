label qst_Terminus_intro:
    scene black with dissolve
    $ Pause(0.25)
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadeout 1.0 fadein 5.0 volume 0.8
    $ PlayMusic("audio/music/2_Chase.ogg")
    scene cg_runaway_cave with dissolve
    MC "Markus!"
    MC "Run! RUN!"
    "We sprinted down deeper into the darkness of the unknown, the sounds of metal clanking, beasts snarling, and cries of agony followed behind us."
    scene cg_cave_and_runner with dissolve
    MARKUS "They’re gaining on us!"
    MC "Keep running! Don’t stop!"
    MARKUS "But... {b}{i}the others!{/i}{/b}"
    MC "There’s nothing we can do! We have to get to—"
    play sound "audio/cfx/demorai_roar_high2.ogg"
    show cg_demorai_brute_highrez at right_f with easeinright and flash
    "A Demorai claws its way through the catacomb wall, blocking their path. Standing in front of [player_name!t] and Markus, it snarls savagely."
    MARKUS"L-Look at it!"
    MC "Markus! Draw your sword, damn it!"
    "Unsheathing his blade with trembling hands, Markus fumbled and dropped it to the floor with a loud clank."
    MARKUS "Sh-Shit!"
    MC "MARKUS!"
    "The beast charges at Markus, but is suddenly attacked by one of the soldiers fighting the demonic creatures throughout the caves."
    play sound "audio/cfx/sword_swings_metalhit.ogg"
    show cg_scout at left with easeinleft
    SCOUT "Go! GO NOW!"
    MC "Markus, quickly!"
    MARKUS "Right!"
    "Darting around the battle, we managed to burst our way through into the Forbidden Chamber."
    MC "Seal the door! SEAL THE FUCKING DOOR!"
    MARKUS "But he—"
    MC "DO IT!"
    scene cg_heavy_fight with dissolve
    "As Markus moved to try and activate the seal by pulling the strange mechanical levers to our left, I looked up through the deep, seemingly endless darkness of the catacombs."
    "I watched as the monstrosity before me took a hold of the Scout with both of its colossal, wretched, claw like hands and held the flailing man out."
    "His cloak flapped helplessly as he swung desperately at the beast, retching up blood, unable to break free from its deathly grip."
    "The creature relished the moment, feverishly lapping up his blood, snarling in sick pleasure as the Scout croakily managed to cry out."
    SCOUT "FUCK YOU!"
    SCOUT "I HOPE YOU FUCKING CHO—"
    "We watched in horror as the beast twisted the body of the man, his cries of pain contorting into an animal like squeal."
    play sound "audio/cfx/prologue_guysnap.ogg"
    "What followed was a terrible snapping as he tore the body in two, flinging the man’s halves aside."
    "Behind it, barely visible was a myriad of other monsters, clawing and clambering their way down towards us."
    MC "Markus... hurry."
    "The beast roared and charged at us once again! A behemoth of tooth and claw, galloping, ready."
    scene cg_mc_eye with dissolve
    MC "HURRY!"
    MARKUS "It won’t close!"
    MC "CLOSE IT! CLOSE THE FUCKING DOOR!"
    play sound "audio/cfx/demorai_roar_high1.ogg"
    MARKUS "I’m trying!"
    MC "MARKUS! HURRY! IT’S NEARLY—"
    scene black with flash
    window hide
    stop music fadeout 1.5
    stop ambience fadeout 1.5
    play sound "audio/cfx/timeskip.ogg"
    scene black
    show text _("A few months earlier..."):
        yalign 0.5
    $ Pause()
    hide text
    $ PlayMusic("audio/music/3_Novaras_L.ogg")
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    show mcprologue:
        xcenter 0.3
    with dissolve
    window auto
    MC "Ah... Today’s the day... {i}Terminus Ceremony.{/i}"
    "Rising from my bed, I was hit by a {i}shockwave{/i}."
    MC "Urgh... {i}My head...{/i}"
    MC "Why did I let Markus talk me into drinking so much last night?"
    MC "Well, better get ready."
    MC "I should grab some gold before I head out, it is {i}a ceremony{/i} after all."
    $ QstStart(QstTerminus)
    $ ShowTutorialPopup("first_quest")
    $ LocEnter()

label qst_Terminus_KitchenEnterMorning:
    "Hm... Where is everyone?"
    "Looks like Regina is in her room."
    "...Should I?"
    menu:
        MC "...Should I?"
        "Peek":
            scene regina_peek with dissolve
            $ Pause()
            "Leaning in, I peered through the small gap in the door to watch as [regina_ref!t] was getting dressed, bare naked as she hummed happily to herself, slowly moving to put on her dress for the morning."
            $ Pause()
            MC "I... I shouldn’t watch this! This is... {i}perverse{/i}."
            MC "... But she does look {i}really{/i} pretty."
            MC "Gah! What’s wrong with me? It’s [regina_ref!t] for Rohark’s sake!"
            $ UnlockGalSceneAndGrantXp("regina", "peek")
            scene black with dissolve
            $ LocFlush(dissolve)
        "Don’t peek.":
            MC "No, of course I’m not gonna do that! What the hell am I even thinking?"
    show mcprologue at left with easeinleft
    $ PlaySoundRandom("woodenDoor")
    show erika at center_f with easeinright
    $ CharMeet("erika", DefaultRel = "rel_friend")
    $ RelSet_Erika()
    ERIKA @smile_talk "Well, good morning [player_name!t]."
    "Following the death of both Erika’s mother and my own due to winter fever, our fathers were sent to the front."
    "Regina, a friend to both families agreed to look after us till our respective fathers came home from the war."
    "Sadly, Erika’s father perished two years ago in battle, leaving [regina_ref!t] and myself the closest thing to family she had left."
    MC "Erika! I wasn’t expecting you to be here today!"
    MC "Aren’t you supposed to be on top secret Inquisitor work?"
    ERIKA @talk "I couldn’t miss seeing you on your big day."
    MC "You didn’t need to come but it means the world to me that you have."
    "Erika, thanks to her outstanding grades and increasing aptitude for magic, was snatched up and positioned with the Inquisitors on her final schooling day."
    "I must admit, I missed her deeply as she went off, gallivanting around on great adventures..."
    "But I knew the work she did was particularly important, so I was always proud of her."
    $ PlaySoundRandom("woodenDoor")
    $ CharMeet("regina", DefaultRel = "rel_friend")
    $ RelSet_Regina()
    show regina at cright_f with easeinright
    "Now dressed, [regina_ref!t] stepped out into the hallway, gasping with delight once she saw Erika."
    REGINA @talk "[player_name!t], I hope you haven’t—"
    REGINA @shock_talk "Erika!"
    ERIKA @smile_talk "Hello, [regina_ref!t]."
    REGINA @smile_talk "Oooh! Come here, my love!"
    show regina with easeinright:
        xcenter 0.6
    show regina at nod
    show erika at nod
    "[regina_ref_cap!t] darted over to give Erika a hug, squeezing her tightly, which Erika clearly found a little uncomfortable."
    ERIKA @surp_talk "Uhh, [regina_ref!t]?"
    ERIKA @surp_talk "Can’t... {i}breathe!{/i}"
    REGINA @shy_talk "Oh! Sorry, dear!"
    show regina smile
    show regina at cright_f with easeoutright
    REGINA @smile_talk "I can’t believe you’re already eighteen."
    REGINA @smile_talk "Your father would be so proud!"
    MC "Thanks, [regina_ref!t]."
    MC "... Is there any news on Father?"
    show regina
    REGINA @talk "... Well..."
    show regina sad
    REGINA @sad_talk "No, but..."
    MC sad "..."
    show erika
    ERIKA @talk "I’m sure he’s fine, he’s been sent to help with the negotiations with Lord Psydon."
    show mcprologue
    MC "That was six months ago."
    ERIKA @talk "Yes, but you know how these things are..."
    ERIKA @talk "The travel alone can take weeks, even months sometimes."
    MC "Has he sent any letters at least?"
    REGINA @talk "No, the last I received was him letting us know he was safe and that the men in his company were in good spirits."
    REGINA @talk "I’m sure he will write to us as soon as he can."
    MC @sad "{i}*Sigh*{/i}... I hope he’s okay."
    MC @sad "And I wish he was here."
    show regina smile
    REGINA @talk "We all do, my love..."
    REGINA @smile_talk "But come now! Today’s a big day!"
    show erika smile
    ERIKA @smile_talk "Yes! [player_name!t]!"
    ERIKA @smile_talk "Today, you have the glorious honour of scrubbing the outhouses clean!"
    MC @smile "... Ha-ha, how funny you are."
    ERIKA @smile_talk "Oh, lighten up, it’s an important day, right, [regina_ref!t]?"
    REGINA @smile_talk "Both he and Markus have been working tirelessly on their studies for months."
    ERIKA @smile_talk "Glad to hear it, and here I was worried you’d both spend too much time chasing girls."
    MC @smile "And risk our great chance at the palace?"
    ERIKA @lewd_talk "Ah yes, I forgot, you want to chase beautiful AND rich girls."
    MC "I’m a man with reputable tastes, Erika."
    ERIKA @smile_talk "Tastes well above your station, I might add."
    REGINA "So, I take it you’re both still planning on being administrators in the Royal Court, isn’t that right?"
    menu:
        "That’s right.":
            show erika
            ERIKA @smile_talk "Hoping for a nice easy life, huh?"
            REGINA @talk "Oh stop, Erika! Him and every other student is hoping to be designated a nicer role like that."
            ERIKA @talk "Most of them are also daydreaming about sleeping with the Princess."
            REGINA @shock_talk "Erika! Your mouth, young lady!"
            show regina smile
        "Now that you mention it, we’ve decided instead that we’d rather just work in the Pleasure District.":
            REGINA @talk "Y-You’re joking, right?"
            ERIKA @smile_talk "Finally! A job I think you two pervs would actually be good at!"
            show regina
            REGINA @lewd_talk "AHEM! I hope that wasn’t a {i}serious{/i} suggestion, I don’t know I’d be able to live with the embarrassment of having to explain your new role to people."
            MC "Yes, I’m only playing."
            REGINA @talk "I should hope so too!"
            REGINA @talk "You’ve both worked far too hard and are far too bright for that kind of work."
        "Markus wants that... I’m not so sure myself.":
            REGINA "... Well, that’s odd, it’s all the two of you have talked about for the last few years!"
            ERIKA "Yeah, why the sudden change of heart? Realised there’s no way in hell you’d be able to woo the Princess, huh?"
            MC "Cute."
            MC "And I dunno, I guess..."
            MC "{i}I’m just not quite sure what I want.{/i}"
            REGINA "... Well... I’m sure you’ll be good at whatever you end up doing, sweetie."
    ERIKA @talk "Well, this has been fun, but I really must get going."
    show regina
    REGINA @sad_talk "So soon? We haven’t seen you in weeks!"
    ERIKA @sad_talk "I know, I know... But there’s some particularly troubling business that needs my full attention."
    REGINA @sad_talk "... Hunting more Dark Mages, I suppose?"
    ERIKA @talk "You know I can’t discuss Inquisitor work."
    REGINA @sad_talk "If we only talked to them more—"
    ERIKA @sad_talk "We will {i}not{/i} allow tainted magic into Novaras."
    REGINA @talk "But times have changed! Our survival depends on cooperation now, not more division."
    ERIKA @talk "We have enough problems as it is without letting loose dangerous Black Mages across the city."
    show regina angry
    REGINA @angry_talk "But we need all the mages we can get!"
    show erika angry
    ERIKA @angry_talk "It’s the law, and one I am sworn to uphold."
    REGINA @angry_talk "Urgh... You’re definitely spending too much time with those Inquisitors; you’re starting to sound just like them."
    ERIKA @angry_talk "You barely know what you’re talking about!"
    show erika
    ERIKA @talk "I’ve seen with my own eyes some of the horrors from their twisted magic."
    show regina
    REGINA @talk "Not all magic is pretty, Erika."
    ERIKA @talk "[regina_ref_cap!t], please, you must learn to keep those kinds of beliefs quiet."
    REGINA @talk "They are born with their magic, you know this."
    REGINA @angry_talk "It’s not a crime to have sympathy for them. "
    ERIKA @talk "No, it’s not, but you know full well that being a sympathiser will lead to Inquisitors like myself investigating you and that will make things very {i}very{/i} difficult."
    ERIKA @talk "... For {i}both{/i} of us."
    REGINA @angry_talk "Well, I’m sorry Erika but my opinions on the matter—"
    MC angry "That’s enough! Both of you."
    REGINA @sad_talk "... Sorry dear, we shouldn’t be squabbling like this on your big day."
    ERIKA @talk "You’re right, now is not the time for debating politics."
    ERIKA @talk "Especially matters as important as this."
    show mcprologue
    MC "Will you be back when I get home, Erika?"
    ERIKA @talk "No, unfortunately, I’m afraid not..."
    MC @sad "... Oh... Well, I understand, I guess."
    ERIKA @smile_talk "But I promise I will be back soon! And you and I can both go and celebrate properly together then, I swear it."
    MC smile "That would be good..."
    MC sad "... I’ve missed you greatly."
    ERIKA @smile_talk "And I you."
    ERIKA @talk "... Anyhow, I must get going now."
    REGINA @talk "... Be safe, dear."
    ERIKA @talk "Will do, and you too, [player_name!t]."
    ERIKA @talk "Look after [regina_ref!t] while I’m gone."
    ERIKA @talk "And good luck for your results!"
    ERIKA @smile_talk "Who knows! Perhaps you will have the honour of serving under me!"
    show mcprologue
    MC "Me and Markus are hoping to celebrate after the results tonight, maybe we will see you out?"
    ERIKA @talk "Again, unlikely I’m afraid."
    REGINA @talk "{i}*Ahem!*{/i} I hope neither of you are planning to get {i}too{/i} drunk at the tavern this evening!"
    MC "... Noooooo."
    ERIKA @smile_talk "Enjoy yourselves."
    hide erika with easeoutright
    "Making her way towards the door, she smiled and waved us farewell."
    ERIKA "Love to you both! I shall return soon!"
    show mcprologue at cleft with easeinleft
    MC "Bye, Erika."
    REGINA  @talk "Come back soon!"
    ERIKA "I’ll make sure to buy you a drink!"
    "And with that, she closed the door behind her, vanishing from our lives once again."
    $ PlaySoundRandom("woodenDoor")
    REGINA @talk "... Right, you should probably get going as well, you don’t want to be late."
    REGINA @talk "Oh, and here by the way, I’ve got a special treat."
    show regina at center_f with easeinright
    REGINA @talk "Some grapes for you."
    $ PlayerAddItem("grapes")
    MC "... Are these {i}fresh?{/i} How did you afford them?"
    REGINA @lewd_talk "Oh, umm... I perhaps dipped into the savings a little for a special occasion such as this..."
    MC "[regina_ref_cap!t]!"
    REGINA @talk "Oh hush! I did the same for Erika when it was her time."
    MC "You shouldn’t have, it’s too expensive."
    REGINA @talk "I won’t hear none of it! It’s your big day!"
    REGINA @talk "Now, go on, shoo!"
    REGINA @talk "And you and Markus be safe!"
    MC "Will do, [regina_ref!t]!"
    MC "Be back soon!"
    hide mcprologue with easeoutright
    scene black with dissolve
    $ QstSetProgress(QstTerminus, 2)
    $ LocSet("novaras_dist_house")
    $ LocEnter()

label qst_Terminus_EnterPalace:
    $ TimeAdvBy(TIME_2H)
    scene cg_castle_square 
    with dissolve
    'There were not many occasions that our walled off capital was able to put aside the bloodshed and horrors of the outside. But every year {i}the Terminus ceremony{/i} was one that found its citizens energised enough to celebrate with real cheer.'
    'Novaras did its best to welcome those who had completed their basic education course and were waiting to be assigned their jobs... {i} for life.{/i}'
    'Both me and Markus had worked tirelessly to push our performance up to the top of our class, often toiling away with studies deep into the night, trying to gain our position in the palace.'
    'We often found ourselves fantasising in the early hours of the morning about how our lives would become a whirlwind of splendour far away from the hunger and drudgery of the {i}normal{/i} population.'
    'A favourite topic of ours was, of course, the court ladies we would try to woo, successfully charming our way into their beds each night.'
    'And the food, OH THE FOOD! We could eat for days till our bellies were fat! No more scrapping over what we’d managed to cobble together. We would eat until our bellies were ready to burst! We often pondered on what it must feel like to be that wealthy.'
    'Ah... But first we had to reach our Terminus. As I made my way to the ceremony being held at the entrance to the palace, many people greeted me happily along the way.'
    'Patting me on the back with many ‘Good luck lads!’ and other courteous expressions of well-wishing for me, I basked in admiration, anxious...'
    'When I finally made it to the ceremony itself, hundreds of other students like me gathered around and chattered away, their excitement electric.'
    'Thousands of commoners gathered to watch the affair from the sides with exuberant smiles on their faces. Confetti was gleefully thrown into the air as we all watched the podium, waiting for the speeches to begin before we’d formally be given our life duties.'
    $ PlaySound("audio/ambience_loc/crowd_city.ogg", FadeIn = 4.0, FadeOut = 4.0, Volume = 0.4, Channel = "ambience")
    window auto
    show mcprologue at cleft with easeinleft
    MARKUS 'There you are!'
    MC smile 'Markus!'
    $ CharMeet("markus", DefaultRel = "rel_friend")
    show markusprologue at cright_f with easeinright
    'Markus hurried over towards me, his voice palpable with excitement.'
    MARKUS 'I figured you were still passed out after all the drinking last night!'
    MC 'Nah, not me! Already looking forward to tonight!'
    MARKUS 'That’s what we like to hear!'
    MC 'I looked around to see where the rest of our class were, trying to pick out the individual faces of the crowd.'
    MC 'Did your brother make it?'
    MARKUS 'Hm? Oh no, Skallion’s busy down the mines today.'
    MC 'He couldn’t get the day off, not even for this?'
    MARKUS 'No, unfortunately Demorai attacks have driven up the demand for ore trade, he couldn’t refuse the gold.'
    MC @sad'Hmm... Still a shame...'
    MARKUS 'Ha! Don’t worry too much, he’s promised us both a barrel of ale to celebrate once he gets back!'
    MC 'No way! Almost glad he’s not here now!'
    MARKUS 'Uh-huh! Think of the girls we can entice over with that!'
    MC 'Heh, especially once we have our fancy palace uniforms! We’ll be rolling in—'
    'Suddenly, a cute high-pitched voice called out from between the chattering waves of happy crowd. A hand waved desperately, trying to grab my attention.'
    show adara at right_f with easeinright
    ADARA talk '[player_name!t]! [player_name!t]!'
    MARKUS 'Oooh! Your future wife is here!'
    $ CharMeet("adara", DefaultRel = "rel_friend")
    MC smile 'At least I won’t be dying alone like you!'
    MARKUS 'Alright heartthrob, she’s been chasing you down since she first laid eyes on you!'
    'I rolled my eyes at Markus’ comment as he chuckled to himself, but he was right, Adara would do anything in her power to spend time with me in and out of class.'
    'Not that I didn’t like her, she was very cute... {i}but{/i} our studies took up so much time that socialising was a difficult thing to do, and near enough impossible if you aimed as high as me and Markus.'
    'Adara finally managed to break through the throngs of people to reach us.'
    ADARA @talk'{i}*Huff*{/i} Hey, both!'
    MARKUS 'Did you {i}run{/i} all the way here?'
    ADARA @talk'Huh?! Uh... N-No...'
    MC smile 'You overslept again, didn’t you?'
    'Adara became flustered as I caught onto her, but I knew her like the back of my hand.'
    ADARA @angry'N-No!'
    'Markus and I shared a glance and chuckled.'
    ADARA @talk 'H-Hey! I DID NOT oversleep, guys!'
    MARKUS 'Long night dreaming about [player_name!t] was it? ... But I think I see Des over there, I’ll leave you two love birds alone for a bit!'
    MC 'We aren’t—'
    $ CharSetVar("adara", "blush", True)
    ADARA @shock 'W-What?! We are so not—'
    MARKUS 'Yeah, yeah!'
    hide markusprologue with easeoutleft
    'Markus left, fighting his way through the crowds as he called out to some classmates.'
    show adara at cright_f with easeinright
    ADARA @talk'He’s so infuriating when he talks about us like that!'
    ADARA @talk'... Right?'
    menu:
        'Will you join us for drinks after?':
            $ CharChangeRel("adara", 1)
            ADARA @talk 'Hmm? Oh! Umm, maybe? It’s... It’s not really my thing...'
            MC 'Ah, I see...'
            ADARA @talk '... But... if {i}you’re{/i} going, I guess I could come for a bit.'
        'You look really cute.':
            $ CharChangeRel("adara", 1)
            ADARA @shock 'E-Eh?!'
            ADARA @talk'S-Stop saying such weird things!'
            ADARA @talk '{i}Idiot!{/i}'
        'Come on, looks like they’re about to begin the speeches...':
            ADARA @talk 'Oh... Right...'

    $ CharSetVar("adara", "blush", False)
    play sound "audio/cfx/crowd_cheer.ogg"

    'Interrupting us, the crowd suddenly roared with cheers as Queen Adelaide and King Mesamor came to the podium, smiling and waving down at us in their luxurious royal wear, their arrogant son absent as usual.'
    'The Queen was a beauty, there was no doubt about that. Many a crude joke had been told in private amongst boys wishing they were her personal squires, helping to {i}tend to ALL her needs...{/i}'
    'She was a woman who was respected, but she was not loved.'
    'She did send money towards charity endeavours such as orphanages, but rarely wanted to be seen by the common people unless some official decorum demanded it, such as this occasion.'
    'Thankfully, she did not rule alone.'
    'The King smiled, but his eyes were heavy, after all, it had been several years since he’d been deposed in 1156 by our ‘Emperor,’ and he now occupied only a figurehead position...'
    '{i}But...{/i} despite this, he remained popular amongst the people, a symbol of the will to keep persevering in the fight against the Demorai... even though he now had only a shadow of his former power.'
    '{i}Ironic,{/i} given that at the time the people would have had his head on a stick for his handling of the war.'
    'I guess that time allows people to romanticise anyone if enough of it goes by.'
    ADARA @talk 'Where’s the Princess? Can you see her?'
    MC 'No, is she—'
    RANDOM_MAN 'LOOK! IT’S THE PRINCESS!'

    scene cg_princess with dissolve
    $ Pause()

    'Nervously stepping out onto the balcony, the beautiful Princess Cecilia smiled and waved at the crowds timidly. Adored and loved by all, {i}the realm’s Princess{/i} was renowned for her charitable and kind nature.'
    'I don’t think there was a single hot-blooded male that hadn’t dreamed about her at some point or another, me and Markus included.'
    'I must have had a thousand dreams where I climbed into her chambers through a window and we stole away together and—'
    scene cg_castle_square
    show mcprologue at cleft
    show adara at cright_f
    with dissolve
    show markusprologue at left with easeinleft
    'Markus reappeared from the crowd and playfully grabbed my shoulder, squeezing it tightly as he leaned over to speak in my ear.'
    MARKUS 'So, when we get to the Royal Court, which one you chasing?'
    ADARA @shock 'Markus!'
    MARKUS 'What? Come onnnn, it’s just a little fun, right, [player_name!t]?'
    ADARA @angry 'The royal family is our oldest and most respected institute!'
    MARKUS 'The royal family is comprised of women prettier than the most expensive whores in the land!'
    ADARA @angry'{i}*Groans!*{/i}'
    ADARA @angry'You’re both terrible.'
    MARKUS 'Oh, you love us really.'
    ADARA @angry'Urgh! You do know that when you’re both talking about dividing up women like the spoils of war, it makes me and every other woman want to vomit, right?'
    MARKUS 'Adara... Live safe in the knowledge that I know you belong in [player_name!t]’s harem, not mine.'
    $ CharSetVar("adara", "blush", True)
    ADARA @angry'I-I AM NOT GOING IN ANYONE’S HAREM, THANK YOU!'
    $ CharSetVar("adara", "blush", False)
    MARKUS 'So! You didn’t say, who you going for, [player_name!t]?'

    # this show is to update her blush state
    show adara
    menu:
        'I’m going for the Princess obviously!':
            MARKUS 'Not if I marry her first!'
            ADARA @angry'Grrr...'
            ADARA @angry'Can you perverts think of nothing else other than what’s between your legs?'
            MARKUS '...'
            MC '...'
            MARKUS 'Nope.'
            MC 'Definitely not.'
            ADARA @talk'{i}*Sigh*{/i} You two are hopeless!'
        'Heh... I think I’ll take my chances at wooing the Queen.':
            $ CharSetVar("adara", "blush", True)
            ADARA @shock'{i}You...{/i} You pervert!'
            MARKUS '{i}*Whistles*{/i} Well... you always did have a thing for older women.'
            ADARA @angry'S-Shut up!'
            MARKUS 'Don’t worry, Adara! All you need to do is wait a couple years and he’ll—'
            ADARA @angry 'Finish that sentence if you want to die.'
            MARKUS '...'
            ADARA '...'
            MARKUS 'WAIT A COUPLE YEARS AND HE’LL BE INTERESTED IN THAT WRINKLY—'
            play sound "audio/cfx/slap.ogg"
            'Adara slapped Markus across his face, leaving a stinging red mark in its wake.' with flash
            MARKUS 'Ow! Fuck! That hurt!'
            ADARA @angry'Hmph! Teach you to be so crude...'
        'I think Adara here would hit me with a brush if I tried wooing anyone in the palace!':
            $ CharSetVar("adara", "blush", True)
            ADARA @shock 'S-Shut up!'
            ADARA @angry'Someone has to stop you idiots getting your heads put on sticks!'
    $ CharSetVar("adara", "blush", False)
    scene cg_castle_square with dissolve

    $ AutoMus(False)
    $ AutoAmb(False)

    stop music fadeout 1.0
    stop ambience fadeout 7.0
    'The murmurs of the crowd died down suddenly; the sense of festivities soon became eerie silence.'
    'All heads turned to see our ‘Emperor’, Kendrick Alcott, as he slowly made his way towards the podium, donned in his thick golden armour that clanged with every step, his elite guard marching behind.'
    'There were murmurs and whispers amongst the crowd, Alcott was not popular by any metric, but he was respected, and above all... {i}feared.{/i}'
    show alcott at center_f with dissolve
    $ Pause()
    ALCOTT '... Today is a special day for this kingdom.'
    ALCOTT @smile 'It has been fourteen years since our war with the Demorai began. Fourteen years of sacrifices...'
    ALCOTT ' Fourteen years of losses too great to put into words.'
    ALCOTT 'Each of us has lost someone in this conflict, but the battle continues even now, with many of our kin away from home helping to secure and restore our once great kingdom!'
    ALCOTT 'The road ahead is hard, it is brutal... {i}and it is bloody.{/i} '
    ALCOTT 'But today is a day of new hope!'
    ALCOTT 'A day for a new generation to lead the fight!'
    ALCOTT 'And we WILL be victorious in this conflict!'
    ALCOTT 'We will survive and we WILL thrive once again!'
    ALCOTT 'And most importantly, we will do it for them!'
    ALCOTT 'We will build the world they fought for, the world they wanted you to have!'
    ALCOTT 'To those of you now bearing the responsibility of helping us restore this kingdom to its former glory, whether soldier or baker, blacksmith or humble street sweeper...'
    ALCOTT 'I salute you!'
    ALCOTT 'HEIL!'
    play sound "audio/cfx/crowd_cheer.ogg"
    
    CROWD 'HEIL EMPEROR ALCOTT! HEIL THE NEW ALDERIAN EMPIRE!'
    ALCOTT 'Go now and do your Emperor proud! Do your country proud and do yourselves proud!'
    hide alcott with dissolve

    $ AutoMus(True)
    $ AutoAmb(True)
    $ CharMeet("alcott")

    'And with that, Emperor Alcott descended from the podium, escorted back towards the fort from which he ruled and administered his government duties from.'
    'As he passed by me, he looked at me for a moment, with the coldest eyes I had ever seen, as though his gaze could cut through and freeze my very soul.'
    show mcprologue at cleft
    show markusprologue at left
    show adara at cright_f
    with dissolve
    ADARA @talk'He’s so scary...'
    MC 'Yeah...'
    MARKUS 'He might be scary, but without him this city would have fallen long ago.'
    MARKUS 'We need more leaders like him. Leaders who will do what has to be done.'
    ADARA @talk'Mmm, I’m not so sure... Not after deposing the King like that...'
    MARKUS 'Alcott led troops and repelled The Great Invasion from taking Novaras while the King continued to squander more troops lives pointlessly.'
    MARKUS 'If it wasn’t for him, this place would have fallen in 1152.'
    ADARA @talk 'He also split the alliance in half with his little coup!'
    MC 'Urgh, do you two need to keep arguing politics?'
    ADARA @angry'Hmph...'
    MARKUS 'Alright, let’s just drop it.'
    MARKUS 'Anyway, come on, it’s time we finally got our results, [player_name!t]!'
    MC 'Ah, right.'
    ADARA @talk'Goodluck, guys, I best get in my queue as well!'
    show adara at blurin, cright_f
    MC 'Good luck, Adara!'
    hide adara with easeoutright
    MARKUS 'Same, good luck to you.'
    hide markusprologue with easeoutleft
    scene black with dissolve
    'Each of us headed over to our respective queues, where hundreds of students would now wait for hours to receive the letter that would decide their life.'
    'Sometimes, the wait would leave some to not find out until the early hours of the next morning...'
    'After five hours, I finally arrived at the stall.'
    $ TimeAdvTo(TIME_AFTERNOON)
    'Markus had already come and gone half an hour before, after he’d managed to slip into the queue slightly ahead of me.'
    'He’d promised to meet me afterwards outside his home, then we’d head out to celebrate together.'    
    scene cg_castle_square 
    with dissolve
    'The woman looked up at me, smiling warmly.'
    WOMAN 'Name?'
    MC '[player_name!t].'
    WOMAN 'Class number?'
    MC '4D.'
    WOMAN 'Student number?'
    MC 'Three-Two-Six-Nine-One.'
    'The woman shuffled through the envelopes stamped down with the red wax seal of the Royal Court, and after finding mine, handed it over to me which I snatched greedily from her hands.'
    WOMAN 'Good luck!'
    MC 'Thank you!'
    'This is it! This is my destiny in my hands!'
    'All these years of work are finally going to pay off!'
    'Feverishly, I ripped into the letter with sweaty hands, my heart beating frantically.'
    $ AutoMus(False)
    $ AutoAmb(False)
    stop music fadeout 3.0
    stop ambience fadeout 3.0

    play ambience2 "audio/ambience_scenes/obelisks.ogg" fadein 10.0
    hide mcprologue with dissolve
    window hide
    play sound "audio/cfx/letter.ogg"
    show screen PrologueLetterText() 
    scene cg_letter
    with dissolve
    $ Pause()
    window auto
    'I read that tiny bit of text a couple times over before it actually started to make sense...'
    MC 'My... Training?'
    '...'
    MC 'Capital... What?!'
    MC 'I... {i}I’m going to the Scouts?{/i}'
    MC '... No... No! This is... This is wrong!'
    MC 'I can’t be in the Scouts! This is...'
    hide screen PrologueLetterText
    scene cg_castle_square 
    with dissolve
    'Looking up, I hurried back over the stall, frantically trying to speak to the lady but was immediately restrained by the guards.'
    'Other students berated me for cutting the line.'
    WOMAN 'Sir! Please wait in line for—'
    MC 'This! This has to be a mistake! I can’t be in the Scouts! I’m not—'
    WOMAN 'If it’s got your name on the front and that’s what’s written, then I’m afraid you are, sir.'
    MC 'But I... I—'
    GUARD 'Oi! Go on, son! Get out of here now!'
    'The guard shoved me back sharply, making me stumble as I fell on my ass, tears springing behind my eyes as I muttered to myself.'
    MC 'No... {i}No this can’t be!{/i}'
    MC 'I can’t... {i}This...{/i}... This is a nightmare!'
    MC '{i}It can’t be real!{/i}'
    scene black with dissolve
    $ TimeAdvTo(TIME_LATEEVENING)
    $ LocSet("novaras_dist_house")
    stop music fadeout 3.0
    stop ambience2 fadeout 3.0
    "Dazed, I walked the streets aimlessly for what seemed like an eternity, until I found myself in the housing district."
    'I dragged myself over to Markus’ home, dejected, destroyed... {i}broken.{/i}'
    $ AutoMus(True)
    $ AutoAmb(True)
    $ LocFlush()
    show markusprologue at cright_f
    with dissolve
    show mcprologue at cleft with easeinleft
    'I found him slouched against the wall by his front door, a solemn look on his face as he turned to me, still holding his own sheet in his hands.'
    MARKUS '... I’ve been placed in the Scouts.'
    'He said with a lifeless look in his eyes, my eyes widened in shock.'
    MC '... Y-You’re...'
    MARKUS 'Yes.'
    'I gulped hard, nodding.'
    MC '... {i}Me too.{/i}'
    'Markus’ mouth hung open in shock, all our dreams and hopes... just like that, {i}gone.{/i}'
    MARKUS '... No, you mean—'
    MC '... Heh... Well, looks like we’re still stuck together... Just...'
    MC 'Not in the way we hoped.'
    MARKUS '... Yeah...'
    MARKUS 'Instead of eating well and wooing court ladies together.'
    MARKUS '{i}We’re gonna fucking die...{/i}'
    MC 'We don’t know that! Come on, we’ll—'
    MARKUS 'Look, [player_name!t], you and I both know full well that the Scouts has the shortest life expectancy, short of just jumping off the fucking wall.'
    MARKUS 'Frankly, I’m half tempted just to get a rope and save myself the agony of dying by {i}their{/i} hands.'
    MC 'Don’t joke about that!'
    MARKUS 'Why not? We’re fucked anyway.'
    MC 'Well, you’ll definitely be fucked if you do that!'
    MC 'And you’ll be fucking me over! I need someone to have my back out {i}there!{/i}'
    MARKUS '[player_name!t]...'
    MC 'Don’t give me that shit! We’ve stuck together since we were kids, we’re gonna stick together and get through this now! Understand?'
    'Markus sighed deeply, not really believing me but playing along anyway.'
    MARKUS '... Yeah... We’ll make it out.'
    MARKUS '{i}*Sigh*{/i} Look, I don’t know about you, but for my last goddamn night of freedom I’m gonna head down the Pleasure District, you coming?'
    'My eyes lit up in surprise.'
    MC 'You’re... You’re going to get a girl {i}down there?{/i}'
    MARKUS 'Come on, we both know you’re not a virgin.'
    MC 'Y-Yeah, but...'
    MC '{i}It’s not really my thing...{/i}'
    MARKUS 'It’s not mine either, but chances are we aren’t going to get any for a couple months... and that’s assuming we survive so, I want to make the most of the time I have left.'
    MC '...'
    MARKUS '... So, you coming?'
    MC "I was thinking about joining Adara at the tavern."
    MARKUS 'Hmm... I guess that’s fair enough.'
    MC "I'll think about it..."
    MARKUS "{i}*Sigh*{/i} Either way, I guess we'll see each other tomorrow, at the fort."
    MC 'Y-Yeah...'
    MARKUS '... [player_name!t]?'
    MC 'Yeah?'
    MARKUS "If you do go and meet Adara, tell her how you really feel..."
    MARKUS "{i}You might not get another chance.{/i}"
    scene black with dissolve
    'Markus turned slowly, dragging his feet as he trudged over and made his way towards the Pleasure District.'
    'I stood there, unsure what to do, dark thoughts trailing around me.'
    $ QstSetProgress(QstTerminus, 3)
    $ LocEnter()

