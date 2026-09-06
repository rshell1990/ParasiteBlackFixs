label qst_TheDarkPass_MarchOut:
    $ LocSet("novaras_gates")
    $ AutoAmb(False)
    $ AutoMus(False)
    play ambience "audio/ambience_scenes/march.ogg" fadein 3.0
    scene cg_citywallsoldiers with dissolve
    'With the sounds of iron and steel reverberating into the sky, we marched towards the gate into the city.'
    'Our forces had been bolstered with a hundred strong cavalry men from another division, whatever this ‘secret’ mission was, it must be very important.'
    $ QstStart(QstTheDarkPass)
    'Crowds came out to cheer us along the way, held back by rows of city guards acting as barriers so we could pass through unhindered.'
    'Even with the adulation from the public, the tone was sombre given the many previous failed missions the Scouts had been made to embark on.'
    'Some openly sobbed, others desperately tried to cheer us on with cries of "Go get em’ boys!" and "Come home safe!".'
    'Suddenly, from the side, I heard a familiar voice cry out to me.'
    show regina at right_f with easeinright
    REGINA @talk'[player_name!t]! [player_name!t]!'
    show mcprologue at left with easeinleft
    'Upon hearing the sweet voice and realising who it was, I looked over across the immense crowd and saw her among it as she desperately reached out to wave and cheer me on.'
    MC '[regina_ref_cap!t]!'
    REGINA @talk'[player_name!t]! [player_name!t]! Come home safe! I love you!'
    hide regina with easeoutright
    'She was swept back by the tidal wave of people as she struggled to keep herself behind the barriers set up, waving frantically towards me.'
    'Damn...'
    'We marched on through the throngs of people, as we approached the archway to leave my ears picked another familiar voice from the crowd.'
    show adara sad at center_f with easeinright
    ADARA @sad '[player_name!t]!'
    'Somehow Adara had managed to burst through the rows of guards keeping the crowds back and sprinted towards me, leaping on me in a frenzied embrace, tears welling in her eyes.'
    MC 'Adara, what are you doing here? You should be—'
    show mcprologue at cleft with easeinleft
    ADARA @sad 'I had to come! I had to say goodbye!'
    MC 'Adara...'
    show adara at nod
    'Without hesitation, Adara sprung forward and planted a kiss onto my lips, her fingers twined through my hair as she clung to me one last time.'
    ADARA @sad 'G-Goodluck, [player_name!t]!'
    MC '... Adara... I...'
    ADARA @sad 'C-Come home, please, to me!'

    'The guards began to pull Adara away, she cried out to me in anguish, her hands still outstretched.'
    show adara sad at right_f with easeoutright

    GUARD 'GET BACK! Get back I say!'
    ADARA @sad '{i}Come home, [player_name!t]!{/i}'
    ADARA @sad 'I’ll be waiting for you!'
    stop ambience fadeout 10.0
    hide adara with easeoutright
    scene black with dissolve
    'I shook my head to try and regain some focus as our procession marched out into the Valley of Death.'
    $ LocSet("valley_of_death")
    $ LocFlush(dissolve)
    $ AutoMus(True)
    play ambience "audio/ambience_scenes/march_desert.ogg" fadein 1.0

    'We marched for hours along the desolate, barren roads of this dead world.'
    'Here and there were scorched out wooden houses long since abandoned and overturned carts still laden with rotten food.'
    'Much of this land was utterly devastated during The Great Siege of Novaras in 1152, turning much of the surrounding land into a dustbowl.'
    'However, if you were able to survive long enough to venture to the other side, greenery could once again be found.'
    'The roads were littered with the skeletal remains of previous travellers.'
    'Perhaps most ominously of all, in one burned out hut we have found what was left of a family sitting at a dinner table, their bones now lost amongst the carcass of their meal.'
    'In the mad rush to Novaras during the war, hundreds in their droves fled to the Capital, the last {i}true{/i} safe haven at the time.'
    'Many starved along the way and many were lost in the congested crowds to be trampled and left on the wayside.'
    'It was only thanks to Emperor Alcott, then just the son of a fledgling lord who had died some months prior, who’d rallied together the bannermen and held off the onslaught of Demorai while the others squabbled and bickered amongst themselves.'
    'Mesamor must have been pleased and presumed Alcott may prove to be the next Newheart.'
    'I doubt in a million years that he would have predicted that Alcott would one day rise up and overthrow him.'
    $ Pause(0.5)

    show duprey at center with dissolve
    DUPREY 'ONWARD MARCH!'
    play sound "audio/cfx/training_aye.ogg"
    'Captain Duprey himself rode by horse, leading us from the front. We constantly peered out across the deadlands for any signs of the Demorai, but rather unnervingly could not locate even a whisper of them.'
    hide duprey with dissolve
    $ TimeAdvBy(TIME_2H)
    'A couple hours into the slow, tedious march, the young First Officer rode up along beside us on a horse and peered down inquisitively.'
    show borras at right_f with easeinright
    'Second in command to Captain Duprey, he was notorious for being a dry, unemotional man.'
    show borras at nod
    BORRAS 'You three, come with me.'
    'Me, Markus and Kiara shared a look, all of us confused.'
    show borras at nod
    BORRAS 'Yes, you three idiots, come, now.'
    show mcprologue at center with easeinleft
    show markusprologue at cleft with easeinleft
    show kiara at left with easeinleft
    'Uneasy, we strayed away from the main bulk of the force and followed Borras down towards the front of the line towards Captain Duprey.'
    show duprey at cright with dissolve
    show borras at nod
    BORRAS 'Captain, I’d like to give these Scouts some horses so they can come with me and loop around onto the ridge of the gorge.'
    'The Captain gave us a cursory glance.'
    DUPREY '... With just these three?'
    show borras at nod
    BORRAS 'I think we’ll draw too much attention with any more. It’s unlikely, but the Demorai may have used the gorge to lay a trap.'
    DUPREY 'Hmm, permission granted, but make sure you’re careful with any engagement.'
    show borras at nod
    BORRAS 'Yes Captain, I’ll ride back and report if there’s any trouble.'
    hide duprey with dissolve
    'Borras whistled and waved over some of the men who trotted the horses over towards us.'
    'Taking the reins of the horses he handed them to each of us.'
    BORRAS 'I take it you can all ride?'
    MARKUS 'Yes.'
    KIARA 'Aye.'
    MC 'Uhh, somewhat.'
    show borras at nod
    BORRAS '‘Somewhat’?'
    MC 'It’s been a while, sir...'
    MC 'Can I ask why you’re taking us and not more experienced cavalry?'
    show borras at nod
    BORRAS 'I’m not risking cavalry men, you lot die, I just need to find a couple of new horses.'
    show borras at nod
    BORRAS 'They die and I’m looking at months of training to get new recruits up to {i}my{/i} standards.'
    'Well... that’s not very confidence inspiring.'
    show borras at nod
    BORRAS 'Now, enough questions! Come!'
    $ AutoAmb(True)
    hide borras with dissolve
    hide mcprologue
    hide markusprologue
    hide kiara
    with dissolve
    $ Pause(0.5)
    'Riding up behind Borras, we furtively looped around to the high ground of the ridge.'
    'If there were any Demorai waiting up there, they could easily clamber down from the sides and surround the men in minutes.'
    'Thankfully, as we trotted up to overlook the valley beneath, we couldn’t see any enemies lurking.'
    '{i}But...{/i} I had an eerie feeling we were being watched by something, somewhere...'
    show borras at right_f with easeinright
    BORRAS 'Hmph... Looks like the path is clear.'
    show kiara at cleft with easeinleft
    KIARA 'Are we done here then?'
    BORRAS 'Yes, we’re—'
    play sound "audio/cfx/demorai_roar_high2.ogg"
    'Bursting out of the sand, a dozen Demorai surrounded us!' with flash
    $ QstSetProgress(QstTheDarkPass, 1)
    show borras at shake
    BORRAS 'AMBUSH!!'
    scene black with dissolve

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_LeftExtra = ["borras"], CharIDList_Right = ["e_demorai_scout", {"e_demorai_scout":2}, {"e_demorai_scout":2}, "e_demorai_scout"], CanTransform = False))

    $ AutoMus(True)

    $ LocFlush()
    show borras at cright_f
    with dissolve

    show mcprologue at cleft with easeinleft
    show markusprologue at right_f with easeinright
    show kiara at left with easeinleft

    BORRAS '{i}*Huff* *Huff*{/i} Bastards... Little fuckers get everywhere...'
    MC 'Is everyone okay?'
    KIARA 'Phew! I think so!'
    $ QstSetProgress(QstTheDarkPass, 2)
    MARKUS 'One nearly took my damn head off!'
    MC 'Is that all of them?'
    BORRAS 'Most likely, they weren’t a main fighting force, just spies, probably been watching us since we left the gate...'
    BORRAS '{i}Fuck...{/i} The Captain needs to hear about this.'
    BORRAS 'Alright, come! Let’s get back and join the main force!'
    hide mcprologue
    hide markusprologue
    hide kiara
    hide borras
    with dissolve
    scene black with dissolve
    'We rode back with Borras, grateful to be re-joining our ranks.'
    $ TimeAdvBy(TIME_2H)
    'Flooded with adrenaline and in spite of the blood now seeping into the cracks of our armour, we were exhilarated at not only having survived, but having been {i}victorious{/i} over our enemies.'
    $ TimeAdvBy(TIME_2H)
    'Even though we knew we had only fought a fledgling force, it was our first real taste of battle... and victory.'
    $ TimeAdvTo(TIME_DAY_END)
    scene cg_desertcamp with dissolve
    'As we had passed through the gorge into the open plains, we set up camp for the evening and soon had fires crackling, hot ash swelling up into the air above us.'
    'Men patrolled around the borders of the camp on lookout for any signs of Demorai.'
    'For now, with a cup of mead in hand, I was free to do as I wished...'
    $ LocSet("qst_darkpass_desertcamp")
    $ LocEnter()


################## CAMP TALK MARKUS #########################
label qst_TheDarkPass_CampTalkMarkus:
    $ QstTheDarkPass().CampMarkusTalked = True
    show markusprologue at center with dissolve
    MC 'Hey, you okay?'
    MARKUS 'Yeah... A little shook-up still after the ridge...'
    menu:
        'We survived, that’s the main thing...':
            MARKUS '{i}*Sigh*{/i} Yeah... I know that.'
            MARKUS 'And we’ll know what we’re doing more next time...'
            MC 'And I’ve got your back!'
            MARKUS 'Heh, good to know.'
        'We showed them our mettle and made them taste our blades!':
            MARKUS 'You guys did, I nearly got killed.'
            MC 'You held your own.'
            MARKUS 'Yeah... but—'
            MC 'Markus, it was our first real fight and we won, take the win.'
            MARKUS '... Yeah... You’re right.'
        'I mean, even if they had cut your head off, it might’ve been an improvement to be honest...':
            MARKUS 'Ahhh, you’re right!'
            MARKUS 'Without this outrageously gorgeous face, the girls would only have this god-like body to look at, poor things, I’d have to start walking around shirtless so they don’t get too distraught!'
            MARKUS 'Let’s be honest though, at that point you’d just have to throw in the towel and accept that women would come from miles around just to have a glimpse.'
            MC 'Naturally.'
            MARKUS '... Thanks...'
            MARKUS '... I need to do better; I can’t let you and the others down again like that.'
            MC 'We’ll be alright, Markus; we just need to stick together.'
            MARKUS 'Yeah... I know...'
    MARKUS '[player_name!t]?'
    MC 'Yeah?'
    MARKUS 'If I get hurt out there and it’s me or you...'
    MC 'Markus, don’t—'
    MARKUS 'Leave me, save yourself.'
    MC 'It’s not going to come to that. '
    MARKUS 'Just promise me you will... if it does.'
    MC '...'
    MARKUS 'You’re like a brother, [player_name!t]. I can’t let you die for me.'
    MC 'Pretty sure Adara would kill us herself if one of us left the other behind.'
    MARKUS 'Oh yes! Although I reckon my death would be a particularly slow and painful one if it was me abandoning you...'
    MARKUS '[player_name!t]...'
    MC 'I’d never leave you behind. That’s a promise, whether you like it or not.'
    MARKUS 'Hmph... Stubborn bastard.'
    MC 'You know it.'
    'Markus rolled his eyes and smirked.'
    MARKUS '...{i}Brothers to the end{/i} still, huh?'
    MC '{i}Brothers till the end.{/i}'
    MARKUS 'Alright, go on now, think I’m gonna try my luck and see if I can cosy up to one of the cuter Scouts.'
    MC 'Good luck, got your eye on anyone in particular?'
    MARKUS 'That blonde with the big tits would be nice...'
    MC 'What is with you and blondes? ... Good luck.'
    $ LocEnter()

label qst_TheDarkPass_CampTalkMarkus_rep:
    show markusprologue at center with dissolve
    MARKUS "Hey [player_name!t]."
    MARKUS "Seen anything unusual?"
    MC "Nothing, just us still being alive."
    $ LocEnter()

################## CAMP TALK KIARA ##################################
label qst_TheDarkPass_CampTalkKiara:
    $ QstTheDarkPass().CampKiaraTalked = True
    show kiara at center_f with dissolve
    'Kiara was waiting patiently on the makeshift wall of the camp, peering out into the darkness of the unknown.'
    show kiara at cright_f with easeoutright
    show mcprologue at cleft with easeinleft
    MC 'Hey!'
    KIARA 'Gah! Didn’t see you there...'
    MC 'Everything alright?'
    KIARA 'Aye... Just strange being out here.'
    MC 'I know the feeling.'
    KIARA 'We spent our whole lives living in fear of the horrors and monsters beyond our walls, but there’s also this whole world out here that we know so little about, you know?'
    MC 'A {i}dangerous{/i} world.'
    KIARA 'Not like ours is that safe anyway.'
    MC 'True...'
    MC '... So, I’ve been meaning to ask you something, Kiara... What did the Captain say to you that one time?'
    KIARA @scared 'Hm?'
    MC 'When you had that big fight the first day, when he knocked you down, he whispered something in your ear.'
    KIARA 'Nosy, aren’t we?'
    MC 'Humour me.'
    KIARA 'He said something like, ‘sorry, lass, needed to put on a show so they know you aren’t JUST a piece of meat!’'
    MC 'Ha! Really?'
    KIARA 'Aye, scared me half to death at the time... but I think he’s a good man under the cold, hard exterior.'
    MC 'Hm... I think that too.'
    'Kiara looked at me and smiled.'
    KIARA 'So... changing the subject...'
    MC '...?'
    KIARA 'Was that girl who hugged you before we left your girlfriend?'
    MC 'Huh? Oh, Adara!'
    MC 'Uh... It’s complicated...'
    KIARA 'That’s alright... It usually is when you’re in the Scouts.'
    KIARA'I want to cut to the chase, [player_name!t].'
    MC 'Huh?'
    KIARA '{i}I like you.{/i}'
    MC 'H-Huh?!'
    KIARA 'You’re cute and you fight alright.'
    'Kiara, rather uncharacteristically, started to blush as she spoke.'
    KIARA 'Are you uhh, familiar with the term ‘Scout Wife’ at all?'
    MC '... Uhh...'
    KIARA 'Look, I know when you get home to ya wee lady friend, she’s probably gonna wanna talk about marriage and babies and all that...'
    KIARA 'But, while you’re out here...'
    KIARA '{i}I’d like some company in the night.{/i}'
    MC 'I... I’m not really... I didn’t expect—'
    KIARA 'I don’t care what you do when we get home, marriage, babies whatever... Not my game at all.'
    KIARA 'I’ll stay outta your way and you’ll stay out of mine...'
    KIARA 'But {i}I need{/i} to know someone out here is watching my back.'
    KIARA 'And I need something {i}good{/i} to help keep me sane out here... Just one good, normal thing to keep me going.'
    MC '... I don’t know. '
    KIARA 'No one needs to know, wouldn’t be anyone’s business but ours. '
    KIARA 'Everyone knows ‘Scout Husbands’ and ‘Scout Wives’ are there for each other before they go home to their {i}normal{/i} families.'
    KIARA 'It’s pretty much the most open secret of the Scouts...'
    KIARA '... The nights are cold, [player_name!t], and every day is a gamble as to whether we’ll make it or not... Do you really want to spend them alone?'
    menu:
        '{image=[ICON.HEART]} Okay...':
            $ CharSetVar("kiara", "romanced", True)
            $ QstTheDarkPass().AgreedToSleepWithKiara = True
            KIARA 'I’m really glad you said that, [player_name!t]. '
            KIARA 'I’ll meet you in your tent tonight after the next guard takes over, alright?'
            MC 'Sounds good.'
            show kiara at center_f with ease
            'With the softest lips, Kiara gave me a gentle kiss on the cheek.'
            KIARA 'See ya later, {i}lover.{/i}'
            hide kiara with easeoutright
            MC '(Oh man, I hope I’ve made the right call with this...)'
        '{image=[ICON.HEART_CROSS]} I’m sorry... It’s not my thing.':
            KIARA @sad 'Hmm... Shame.'
            MC 'Sorry, I really am.'
            KIARA 'I hope ya wee lady friend knows how lucky she is.'
            MC 'She’s not my—'
            MC 'Like I said, it’s complicated.'
            KIARA 'Aye... It always is.'
            KIARA '... Say, how did you and that friend of yours meet?'
            MC 'Huh?'
            KIARA 'Ya friend, the pale one? Thinks he’s God’s gift?'
            MC 'Markus?'
            KIARA 'That’s the one!'
            MC 'Heh, we’ve always known each other, ever since we were little.'
            KIARA 'Oh?'
            MC 'Even got sent to the same class. We’ve always been inseparable.'
            KIARA 'That must be nice to have a friend like that.'
            MC 'Yeah... We made all these plans about us both getting into the palace, wooing all the girls and becoming real big shots.'
            'Kiara laughed loudly.'
            KIARA @happy '{i}Really?{/i} Don’t know why you’d want to spend your time with a bunch of wankers like that palace lot.'
            MC 'Huh? '
            MC 'Most people idolise them.'
            KIARA 'Great if that’s what you’re into, but I couldn’t give less of a shit.'
            KIARA 'Some failed king who fucked up, a bimbo queen made of ice, an arrogant prince who has no time for anyone, and a sickly-sweet princess who’s probably just a spoilt little brat that knows how to put on a show for the boys.'
            MC '... I’ve never heard anyone talk about the royal family like that!'
            KIARA 'Aye, I think you will find outside of your precocious Capital, we don’t all share the same reverence for a bunch of upper-class twats who do little more than wave at us from their gilded balconies.'
            KIARA '... So, like I said, you’re better off without them, should be spending your time with some {i}real{/i} people.'
            MC 'Yeah... Too bad the {i}‘real’{/i} people are all starving.'
            KIARA 'Aye, that’s why we’ve gotta get this war won, get back to looking after our own.'
            KIARA '... Anyway, go on, shoo, I’d better get back to my duties.'
            MC 'Alright, talk soon.'
            KIARA 'Yeah... Talk soon.'
            hide kiara with easeoutright
    $ LocEnter()

label qst_TheDarkPass_CampTalkKiara_rep:
    show kiara at center_f with dissolve
    MC "Hey."
    KIARA "Shoo, [player_name!t]. I need to stand watch."
    if QstTheDarkPass().AgreedToSleepWithKiara:
        KIARA @happy "We'll see each other {i}later tonight{/i}, promise."
    MC "Okay."
    $ LocEnter()

################### CAMP TALK DUPREY ##########################
label qst_TheDarkPass_CampTalkDuprey:
    $ QstTheDarkPass().CampDupreyTalked = True
    show duprey at center_f with dissolve
    'Captain Duprey was sitting around one of the fires chatting to the men.'
    'As he gnawed into some bland looking chicken and swigged at his flask, he seemed more relaxed than usual as he spoke.'
    'When he saw me approach, he looked and gave a small nod of his head.'
    show duprey at cright_f with easeoutright
    show mcprologue at cleft with easeinleft
    MC 'Evening, Captain.'
    DUPREY 'You are one of the lads Borras took up on the ridge earlier, yes?'
    MC 'Yes, sir.'
    DUPREY 'Hm, nicely done, lad.'
    'The Captain offered me a swig of his drink which I accepted gratefully, and then welcomed me to sit.'
    show mcprologue at nod
    MC 'Thank you, sir.'
    DUPREY 'So, how’ve you settled in?'
    MC 'Fine I think, sir.'
    DUPREY 'Good, good...'
    MC '... Could I ask you about a couple things, sir?'
    DUPREY 'Hm?'
    MC 'If you don’t mind...'
    DUPREY 'Aye, feel free.'
    $ tmpvar["duprey_exh_talkmenu"] = ['many_battles', 'what_are_we_recovering', 'any_family_back_home']
    stop music fadeout 1.0
    menu qst_TheDarkPass_CampTalkDuprey_menu:
        'Have you fought in many battles?' if 'many_battles' in tmpvar["duprey_exh_talkmenu"]:
            $ tmpvar["duprey_exh_talkmenu"].remove('many_battles')
            $ AutoMus(False)
            $ PlayMusic("audio/music/9_Burned_T.ogg")
            DUPREY 'Lost count a long time ago.'
            DUPREY 'I’ve been here since the beginning...'
            MC 'You mean—'
            DUPREY 'When it all first started, we never took it seriously, far more concerned with the threat of Kalliban O’Nok and his army of orcs crossing the seas to invade...'
            MC '{i}The winter of 1149.{/i}'
            DUPREY 'Alright, clever clogs. That’s what they called it, aye.'
            DUPREY 'Villagers talked about {i}‘ghosts in the night’{/i} snatching people up... We figured it was just bandits.'
            DUPREY 'More ‘n’ more had been spotted what with all the famine; we were preoccupied with the kind of threats we could understand.'
            MC 'I know this part! After they found more and more bloody scenes, The High Lords and King Mesamor finally relented and got the High Mages and Inquisitors to investigate.'
            'Captain Duprey raised a curious eyebrow.'
            DUPREY @think 'Hmm... How’d you know all that? Most don’t know the full story.'
            MC 'I studied it.'
            DUPREY @laugh 'Ha! How very wise of you...'
            DUPREY 'Always good to know how you got to where you’re at but I’m afraid there aren’t many more lessons to learn from it that’d be useful.'
            DUPREY 'We underestimated the enemy, and we still thought at the time it was all some grand scheme from Kalliban. We overestimated him.'
            DUPREY 'We were ordered to defend the neighbouring villages and towns when we should have had the army brought in and amassed an all-out assault, they’d caught us on the backfoot. We were still naive then.'
            'Captain Duprey took another sip of his drink, he seemed lost in his memories.'
            DUPREY 'We paid the price for those mistakes at Meadow Plains.'
            MC '{i}You{/i} were at The Battle of Meadow Plains?'
            DUPREY 'That I was.'
            DUPREY 'I remember the bloodshed in the streets from the towns that had been annihilated.'
            DUPREY 'Every corner you turned around had death waiting for you on the other side.'
            DUPREY 'And there was the mad rush of thousands fleeing to Novaras to hide behind its walls.'
            DUPREY 'The butchered bodies of the mages and Inquisitors before we arrived to offer relief.'
            DUPREY 'But most of all, I remember THAT battle.'
            'We had all heard tales about the first great battle for Alderay and of how the ‘legendary General Newheart’ fell trying to relieve Fort Rook, the supposedly impenetrable Fortress of the South.'
            MC '... Were you there when General Newheart—'
            DUPREY 'Old Iron Heart? Aye, we were friends.'
            show mcprologue at shake
            MC '... No way!'
            MC 'You knew General Newheart?'
            MC 'As in, THE Newheart? '
            DUPREY 'He always hated how they changed his name, Lucan Erunheart was his real name before he was ‘blessed’ with ‘Newheart, Defender of The Realm’.'
            DUPREY 'But yes, I knew him alright.'
            DUPREY 'I was there at the war table with him; we strategized many a battle together.'
            DUPREY 'It was the two of us that pushed back Kalliban’s first invasion AND the Dark Elf King’s encroach. '
            MC 'That’s... That’s incredible!'
            DUPREY 'Bah... I was a younger man back then, I ain’t as fast as I used to be.'
            DUPREY 'Newheart though? The best warrior I’d ever met and a brilliant commander in the field.'
            DUPREY 'Handsome bastard as well, got all the girls swooning after him.'
            DUPREY 'They still singing about him?'
            MC 'All the time! The man’s a legend!'
            MC 'I can’t believe you actually met him! You’re bound to hear at least one song about him in any of the taverns once people have had a drink or two!'
            DUPREY @think 'Hmph...'
            MC '... Where did it all go wrong?'
            'The Captain had become morose as he reminisced, but his anger was now evident as his eyes glared into the embers of the fire.'
            DUPREY '{i}Mesamor happened.{/i}'
            MC 'What do you mean?'
            DUPREY 'I mean that old prick decided the siege tactics we had laid out would have taken too long.'
            DUPREY 'So, he decided in his infinite fucking wisdom to push through some other general’s much more aggressive strategy.'
            DUPREY 'Mesamor couldn’t stand the idea of a prolonged war, he wanted to take back Fort Rook as quickly as possible and march south to take back everything else he’d lost.'
            MC 'I take it you didn’t approve.'
            DUPREY 'Years of actual battle experience and advice were cast out the window for the sake of bureaucracy, what do you think?'
            MC '... So, what do you remember of the battle itself?'
            DUPREY 'Lots of fighting... Dead everywhere... I saw more bodies that day than most men see in a lifetime.'
            DUPREY 'From all the smoke and what felt like an avalanche of blood, it was hard just to breathe, never mind making sense of the field...'
            DUPREY 'Across the way on a small hill, I saw Newheart in that shimmering armour you lot like singing about so much. '
            DUPREY 'He stood alone against the Demorai General, a monstrous thing I can’t seem to forget even when I try...'
            DUPREY '{i}Zanarak.{/i}'
            '{i}Zanarak{/i}, the bogeyman of every child in Alderay.'
            'Stories spread far and wide of a supposed leader of the Demorai’s armies, unstoppable and ruthless, wings so large they could block out the sun and plunge an entire battlefield into a darkness as awful as himself...'
            'Some doubt if he ever existed, so few survivors remain whenever he’s claimed to have been sighted and the tales they told were wilder than the legends of Newheart.'
            MC 'He’s... {i}real?{/i}'
            DUPREY 'As real as you and me, boy... Make no mistake about that.'
            DUPREY '{i}*Sigh*{/i} He fought bravely...'
            MC 'How did—'
            DUPREY 'It took his head.'
            DUPREY 'I still remember that thing clutching him by the hair and holding it up for us all to see...'
            DUPREY 'Boasting of his kill, gloating at how easy it had been to take down the very best of us.'
            'A chilling sense of dread slithered into every bone in my body... {i}What if we encountered some monster Zanarak while we were scouting out here now?{/i}'
            DUPREY 'After that, you know the rest.'
            DUPREY 'Lots of fighting, {i}Daggerfall.{/i}'
            DUPREY 'Mesamor deposed and Alcott declaring himself Emperor...'
            MC 'Can I hear some more about Daggerfall?'
            DUPREY 'I’m not a history teacher, lad.'
            MC 'I know sir, sorry I... guess I just to wish to hear from someone who was actually there.'
            MC 'I’m not sure how reliable those books we were given are.'
            DUPREY 'Hmph... Wise boy, you are... They probably try to paint a rosier picture than it really was.'
            DUPREY 'Don’t wanna give you kids too many nightmares, we’d never get you fighting for us otherwise!'
            DUPREY 'Operation Daggerfall was our last real gamble.'
            DUPREY 'We had managed some years before, when the war with the Demorai first really started, to suspend previous conflicts and form a loose alliance with the other kingdoms and races;'
            DUPREY 'Elves, Dwarves, Orcs, even the bloody Greater Trading Company...'
            DUPREY 'Didn’t do much good though when the bastards kept showing up everywhere.'
            DUPREY 'Following the failure of The Great Demorai Siege, we were in high spirits after our first major win.'
            DUPREY 'We tried pushing back harder and faster to reclaim the South, but we were losing far too many men.'
            DUPREY 'We had left people starving on the home front and many were starting to think the whole thing was a mistake, that a new strategy was needed.'
            DUPREY 'I still remember stealing boots from some dead lieutenant because mine were literally rotting away...'
            DUPREY '{i}*Sigh*{/i} Then came {i}Daggerfall{/i}.'
            'The Captain took another uneasy swig of his drink, as if pushing down some vile memory.'
            DUPREY '{i}Fucking Daggerfall.{/i}'
            MC 'They tried to tell us in class that {i}Daggerfall{/i} wasn’t a total failure, that—'
            DUPREY 'Oh, did they now?'
            DUPREY 'Bullshit, it was a disaster, and don’t you ever let any fancy prick in shiny armour who wasn’t even there tell you otherwise.'
            MC '...'
            DUPREY 'It was Mesamor’s last real throw of the dice.'
            DUPREY 'He thought to divide the army in two and have them sweep down like scythes, hoping to crush the enemy between them on two fronts.'
            DUPREY 'By that point, what was it? 1155? 1156 maybe?'
            DUPREY 'Either way, we had neither the manpower nor the resources to pull it off, they quickly broke through our lines and we had to retreat, weaker than ever.'
            DUPREY '... After that, Alcott led his coup, Mesamor became just a puppet, a monarch in name and nothing more, and the kingdom got split into factions.'
            MC '... I see.'
            $ AutoMus(True)
        'What exactly are we recovering?' if 'what_are_we_recovering' in tmpvar["duprey_exh_talkmenu"]:
            $ tmpvar["duprey_exh_talkmenu"].remove('what_are_we_recovering')
            DUPREY 'Don’t know, orders are to secure the site and bring back the relics, that’s it.'
            DUPREY 'Frankly, I couldn’t give a shit about what we’re picking up.'
            DUPREY 'In and out is my only concern.'
        'Do you have any family back home?' if 'any_family_back_home' in tmpvar["duprey_exh_talkmenu"]:
            $ tmpvar["duprey_exh_talkmenu"].remove('any_family_back_home')
            DUPREY 'My wife passed to fever.'
            MC 'Oh... I’m sorry, sir.'
            DUPREY 'It’s alright, it was during the mass fleeing to Novaras, wasn’t just people hiding behind those walls but plague and famine as well...'
            DUPREY 'My wife was a beauty... She was ravaged by the plague and her body just gave up eventually.'
            DUPREY 'My daughter is alive though, somewhere up north in Angmurus, helping with the negotiations.'
            MC '...'
            DUPREY @happy 'Feisty little thing let me know straight up she’d learn how to swing an axe like me! Ha!'
            DUPREY 'Lord... I haven’t seen her in... {i}eight years{/i} now.'
            MC 'Do you know if she’s okay?'
            DUPREY 'We exchange letters monthly, and I still receive reports on her from time to time, mostly trouble that she’s been causing...'
            DUPREY 'When this is over, it’ll be good to see her again... I’d like to see that axe swing of her myself one day!'
            DUPREY '... How about you? Anyone back home?'
            MC 'Yeah... There’s a few people waiting for me.'
            DUPREY 'Hm... That’s good... You think of them... They’ll give you a reason to survive when you need it.'
    if len(tmpvar["duprey_exh_talkmenu"]) > 0:
        jump qst_TheDarkPass_CampTalkDuprey_menu
    else:
        $ tmpvar = {}
        MC "That's all, sir."
        DUPREY 'Enjoy your evening, boy.'
        MC 'Captain.'
    $ LocEnter()

label qst_TheDarkPass_CampTalkDuprey_rep:
    show duprey at center_f with dissolve
    MC 'Captain.'
    DUPREY 'Enjoy the rest of your evening now, boy.'
    MC "Aye Captain."
    $ LocEnter()

############### CAMP TALK BORRAS ####################
label qst_TheDarkPass_CampTalkBorras:
    $ QstTheDarkPass().CampBorrasTalked = True
    show borras at cright_f with dissolve
    show mcprologue at cleft with easeinleft
    MC 'Sir.'
    BORRAS 'Hm? Oh, it’s you.'
    BORRAS 'Nicely done out there on the ridge earlier.'
    MC 'Thank you, sir.'
    BORRAS 'I’d stay and chat, but I need to consult with some of the other lieutenants, farewell.'
    MC 'Farewell, sir.'
    'He seems tense... Maybe there’s something he’s not telling us.'
    $ LocEnter()

################# CAMP PLAY CARDS ###########################
label qst_TheDarkPass_CampPlayCards:
    $ QstTheDarkPass().CampPlayedCards = True
    'As I headed over towards the men gathered around playing cards, one of them pulled up a seat for me.'
    RANDOM_SOLDIER 'Oi oi! Fancy a game of cards?'
    MC 'Sure.'
    scene black with dissolve
    "We ran some rounds of Steel Maidens."
    "It was a popular game among warrior society due to it's lewd artwork paired with tactical, competitive gameplay."
    "Unfortunately, I never brought my own deck so I was hammered."
    $ LocEnter()

################ CAMP GOTO BED ###########################
label qst_TheDarkPass_TooLateGoToSleep:
    "It was getting late, so I have decided to go to my tent to catch some sleep before marching out again tomorrow."
    scene black with dissolve
    $ LocSet("qst_darkpass_desertcamp_mc_tent")
    $ LocFlush(dissolve)
    jump qst_TheDarkPass_GoToSleepInTent
    

label qst_TheDarkPass_GoToSleepInTent:
    if not QstTheDarkPass().AgreedToSleepWithKiara:
        'Peering out of my tent I noticed Kiara still overlooking the vast deadlands, watching carefully for signs of movement.'
        'When she saw me, she smiled faintly before awkwardly turning away.'
        'Markus, over on the other side of camp was relaxed, chatting animatedly with some of the other Scouts.'
        'It was nice seeing him happy, he hadn’t seemed quite so relaxed for a while, and neither had I.'
        scene black with dissolve
        'Rolling over, I soon began to drift off to sleep.'
        'My own thoughts turned to Adara and the others back home...'
        MC '... I’ll be home soon... I know I will...'
        jump qst_TheDarkPass_SleepAndMorningScene
    else:
        jump qst_TheDarkPass_KiaraSexScene
################ CAMP MENU ON BED ###################
label qst_TheDarkPass_ClickedSleepInTent:
    "I could hang around the camp more or try and catch some sleep."
    menu:
        "Go to sleep":
            jump qst_TheDarkPass_GoToSleepInTent
        "Not yet":
            $ LocEnter()

label qst_TheDarkPass_KiaraSexScene:
    show mcprologue at cleft
    with dissolve
    'After a moment, there was a rustling and Kiara’s head playfully poked inside.'
    $ PlaySoundRandom("tentFlap")
    show kiara at center_f with dissolve
    KIARA 'Hey, you.'
    'I smiled faintly as I answered her.'
    MC 'H-Hey, you...'
    'Kiara laughed, climbing into my tent with me.'
    KIARA 'Come on, let’s not waste too much time.'
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'Kiara quickly moved to undress herself.'
    $ CharSetClothes("kiara", "naked")
    show kiara at blurin, nod
    'My eyes stared at her freckled chest and cute round ass.'
    'I found my cock twitching with excitement.'
    'Kiara pressed a passionate kiss onto me, slipping her tongue in my mouth.'
    'Just as mine met hers she pulled back, letting her teeth catch lightly on my bottom lip.'
    'She stroked her fingers down my chest as she ripped off the rest of my clothes, revealing my hard-on.'
    KIARA 'There we go.'
    'Suddenly, Kiara turned around, waving her big butt in my face. My cock throbbed at the sight and sweet smell of her bare holes now in front of me.'
    MC 'What are you—'
    'Sitting her ass down onto my face, Kiara moaned happily as her hand toyed with my cock.'
    KIARA 'Sorry, lover, I’m in need... mmm... of a little foreplay... if you don’t mind, of course.'
    'Ecstatic at the idea, my tongue thrashed and twirled around her outer lips, the taste of her sending me wild.'
    'I pushed up against her pussy, letting my tongue slip inside before pulling it out to let it slide up and down over her clitoris.'
    'Kiara moaned, her legs trembling as she leaned forward, planting her warm lips onto the head of my cock.'
    scene kiara_prol_cowgirl_1
    with dissolve
    $ PlaySexFx("audio/sex_sounds/ves69_100.ogg", 1)
    $ Pause()
    'Delicately, Kiara began to bop her head back and forth as she sucked my cock, taking me into her mouth slowly, letting the wetness of her mouth drip down me.'
    'My cock began to throb against the warm sensations, Kiara’s hot moans and slurps only further incentivised me.'
    KIARA 'Mmm... Ahh... {i}*Slurp!* *Slurp!*{/i}'
    'Flushed from arousal, I continued to delicately eat Kiara’s sweet pussy while she made short work of my cock.'
    'The wet lewd sounds soon left me desperately hungry for more.'
    "Kiara's head began to bop up and down, gliding down my cock as she took it inch by inch deeper."
    KIARA "Mmfghh! {i}*Slurp!*{/i}"
    "Kiara moaned as my tongue slipped deeper into her womanhood, and she began to rub herself against my face to try and force my tongue deeper into her."
    "Between her muffled moans, I too was struggling to maintain composure as she began to thrash her tongue against my cock, enveloping it as she threw her head forward faster."
    "The wet grunts and moans grew louder as the intense sensation grew and grew with no reprive."
    "Kiara seemed possessed to drain me, to suck every inch of pleasure she could from the moment and I in turn did the same, enjoying every taste of her wonderful body."
    scene kiara_prol_cowgirl_2
    with dissolve
    $ Pause()
    KIARA "{i}*Slurp! *Slurp!*{/i} Mmmfhhh! Shooo ghoood! {i}*Slurp!*{/i}"
    KIARA "Mhorhee!"
    "After a few more moments, I knew I had finally reached my limit."
    "Kiara above me began to tremble and shake, and I knew any moment I was about to finish."
    "I tried to warn her, but Kiara continued to press her soft butt down against my face, muffling out my warning."
    "Unable to hold back any longer, I let loose inside of her warm, wet, mouth."
    $ PlaySexFx("audio/sex_sounds/ves69_finish.ogg")
    scene kiara_prol_cowgirl_finish_1
    with flash
    $ Pause()
    "Kiara's eyes opened in surprise first, but quickly, a smile stretched across her lips with my cock still in her mouth."
    "She swallowed down the hot load and after a tender kiss on the end of my cock, she lifted her head away and turned to face me once again."
    KIARA "That was a big one ... Hope you're still ready for the main course, lover."
    MC @talk "Ahh ... Kiara ... Your mouth feels heavenly."
    KIARA "{i}Wait till you feel the rest of me, stud.{/i}"
    KIARA "Mmm... Come now, love, don't keep a girl waiting."
    KIARA 'I need you to fuck me.'
    scene kiara_prol_cowgirl_3
    with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    $ Pause()
    'Kiara crawled over me, pinning my hands to the floor as she positioned herself eagerly above my member.'
    'Gently, Kiara slid herself down, gasping as she felt my member push deeply inside of her.'
    KIARA 'Mmm... {i}Fuck...{/i}'
    'Kiara began gently slowly bouncing, the soft flesh of her butt hit up against my crotch as her pussy lovingly enveloped my cock, each bounce causing sweet little moans to escape her lips.'
    KIARA 'Mmm, yes... That’s it...'
    'She soon loosened her grip on my hands so I could lean forward to grab a hold of her waist, helping her bounce harder on my member.'
    MC '{i}*Huff* *Huff*{/i} You’re so tight...'
    scene kiara_prol_cowgirl_4
    with dissolve
    $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
    $ Pause()
    KIARA 'Mmmm!'
    'My sweaty hands reached around to grope and fondle her soft butt, as I latched my mouth onto one of her breasts and began to suck, I felt her nipple stiffen in my mouth.'
    'Kiara’s hands reached down to pull my face up to look at her.'
    'She leaned forward to press another hot kiss onto me, slipping her tongue greedily into my mouth as she continued to bounce happily, her pussy so wet that she slid effortlessly up and down the length of me.'
    KIARA 'T-That’s it... Just a little more!'
    'As the two of us continued our session, we became drenched in sweat as our little tent warmed up.'
    'Before I knew it, Kiara threw her head back and moaned in ecstasy, her fingers digging into my chest.'
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    KIARA 'Mmm! That’s it! I’m gonna cum!'
    KIARA 'Cum with me! Cum—'

    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")

    scene kiara_prol_cowgirl_finish_2
    with flash

    $ UnlockGalSceneAndGrantXp("kiara", "prol_cowgirl")
    $ Pause()

    'Holding onto her tightly, I grunted as I felt her body tighten around me, and unable to hold back my own lust, I came with her there and then.'
    'Giggling, and with both of us now breathless, Kiara dropped down onto my chest.'

    scene bg_player_camp_tent
    show kiara at center
    with dissolve

    $ CharChangeRel("kiara", 1)

    KIARA 'Mmm... that was nice, lover boy.'

    $ CharSetLover("kiara")
    $ CharAddRelEntry("kiara", "prol_romance")

    KIARA 'You’re not too bad at making love y’know, with some more training, maybe I’ll try to steal you away for myself when we get back home!'
    MC 'I thought you said we were just fucking?'
    KIARA 'What’s the difference, love?'
    MC 'Well, um—'
    KIARA 'Shhh, stop talking, {i}just enjoy the moment{/i}.'
    'With a warm, naked Kiara tangled in my arms, I closed my eyes and allowed sleep to creep up to me at last.'
    scene black with dissolve
    ### achievement
    if "kiara" not in _total_cummed_characters:
        $ _total_cummed_characters.append("kiara")
    $ AutoMus(True)
    $ CharSetClothes("kiara", "normal")
    jump qst_TheDarkPass_SleepAndMorningScene

label qst_TheDarkPass_SleepAndMorningScene:
    scene black with dissolve
    $ HealParty()
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)
    $ Pause(0.5)
    $ LocFlush(dissolve)
    if QstTheDarkPass().AgreedToSleepWithKiara:
        'When I awoke in the morning, I was alone in my tent.'
        'Kiara must have slipped away in the night back to her own.'
        $ LocSet("qst_darkpass_desertcamp")
        $ LocFlush(dissolve)
        $ PlaySoundRandom("tentFlap")
        'Damn... I hope I made the right choice with this.'
    else:
        "Came dawn, I awoke to the noise of soldiers preparing to march on outside."
        $ LocSet("qst_darkpass_desertcamp")
        $ LocFlush(dissolve)
        $ PlaySoundRandom("tentFlap")
    
    show mcprologue at cleft with easeinleft
    "As I stepped out of the tent, I saw Markus walking over to my tent."
    show markusprologue at cright_f with easeinright
    MARKUS @smile "Morning, Lord [player_name!t]!"
    MC @think "Have I been made royalty in my sleep?"
    MARKUS "Sadly no, I just wanted to kick off your day proper."
    MC "What do you hear?"
    MARKUS "Nothing but the march."
    MARKUS "Word is, it's gonna be a month more of this..."
    MC "*Sigh* Okay then, let's pack up."
    show markusprologue at blurin, cright
    hide markusprologue with easeoutright
    hide mcprologue with easeoutright
    scene black with dissolve
    if PlayerItemQty("potion_heal_minor") < 2:
        $ PlayerAddItem("potion_heal_minor", 2)
    jump qst_TheDarkPass_LeaveCampToBurnedOutVillage

label qst_TheDarkPass_LeaveCampToBurnedOutVillage:
    $ LocSet("valley_of_death")
    $ LocNameSetTemp(_("Southwards of the Valley of Death"))
    play ambience2 "audio/ambience_scenes/march_desert.ogg" fadein 5.0
    'A couple of weeks of mostly uneventful marching later...'
    $ tmpvar["advancebydays"] = 10
    while tmpvar["advancebydays"] > 0:
        $ TimeAdvBy(SECS_IN_DAY)
        $ tmpvar["advancebydays"] -= 1
    $ tmpvar = {}
    $ TimeAdvTo(TIME_NOON)
    $ Pause(0.5)
    scene pbat_desert
    'Having left the deserted wasteland of the Valley of Death, we were finally seeing signs of life again as we trudged one foot in front of the other, an exhausted line of men who could see neither the start nor the end.'
    'Finally, and perhaps morbidly, having seen no sign of civilisation for miles, we passed through the remains of a burned-out village.'
    $ LocNameSetTemp(_("Abandoned village"))
    'As we reached a crossroads, Captain Duprey held his hand up and ordered us loudly to ‘STOP!’.'
    stop ambience2 fadeout 0.2
    play sound "audio/cfx/army_aye.ogg"
    'We looked around, bemused as to what had caused him to bark the order.'
    'There were at least a dozen small buildings, but each one had been pretty much obliterated into scorched ruins.'
    show mcprologue at cleft
    show kiara at left
    show markusprologue at center
    with dissolve
    MC 'What’s happening? Why are we stopping?'
    MARKUS 'I don’t know.'
    'Borras rode forward, trotting over towards Captain Duprey where they shared a few words together.'
    'Nodding, Borras once again rode back down towards us.'
    show borras at right_f with easeinright
    BORRAS 'You three, with me again.'
    'He whistled, signalling for some horses to be brought to us.'
    KIARA 'Why can’t it be one of the others?'
    KIARA 'Trying to knock us off or something?'
    BORRAS 'I’ll have you whipped for disobedience if you speak to me like that again!'
    KIARA '... Sorry, sir.'
    BORRAS '... And for your information, after your success on the ridge, I figured I could at least rely on you three to not immediately die.'
    BORRAS 'Am I mistaken?'
    PLAYER_KIARA_MARKUS 'No, sir!'
    BORRAS 'That’s more like it.'
    show borras at blurin, right
    hide borras with easeoutright
    'We each gave the other a disconcerted look as we realised that we were once again being placed in peril’s way.'
    hide mcprologue
    hide markusprologue
    hide kiara
    with dissolve
    'Mounted on horseback, we headed off towards the front of the march where Captain Duprey gazed ominously ahead.'
    show duprey at cleft with dissolve
    show borras at cright_f with easeinright
    BORRAS 'I’ve brought them up as you asked, sir.'
    DUPREY 'Good.'
    'Duprey’s steely eyes stayed on the horizon, unflinching.'
    BORRAS 'What is it, Captain, what do you see?'
    'He pointed towards the furthest house.'
    DUPREY 'Movement. {i}There.{/i}'
    'Borras’ eyes narrowed as he squinted at the house but clearly couldn’t see anything.'
    'There was a deathly silence in the air as he turned to look back at us, inclined his head towards the house and sealed our fate.'
    BORRAS 'Come, on me, you three.'
    'Before he could take off, the Captain stopped him sharply.'
    DUPREY 'Borras!'
    BORRAS '...'
    DUPREY '{i}Be careful.{/i}'
    hide duprey
    hide borras
    with dissolve
    'Cantering apprehensively behind Borras, we made our way towards the lone house.'
    show borras at cright
    with dissolve
    show markusprologue at center with easeinleft
    show mcprologue at cleft with easeinleft
    show kiara at left with easeinleft
    'As we made our way closer, we could hear the sounds of crying growing louder, we each gave the other perplexed looks.'
    'We knew there were people still living out here, but most had long since moved into other kingdoms or were well hidden...'
    'As we peered into the ruins, there sat a woman, long brown hair tangled between her fingers as she sobbed hysterically into her hands.'
    'All skin and bones, the palest white I’d ever seen a person.'
    'Naked and huddled over, she barely looked human.'
    'While I caught a glimpse of her tits and the brown bush nestled above her pussy, it was certainly not arousing by any means.'
    'It was pitiful to see the pale shadow that remained of what was once a person, now reduced to that of a starving animal.'
    'Both for her dignity and due to my own discomfort, I tore my eyes away.'
    BORRAS 'My lord... {i}What have they done to you?{/i}'
    show borras at blurin, cright_f
    'Borras looked back to the main force of men and shouted out.'
    BORRAS 'WE HAVE A SURVIVOR!'
    'He jumped down from his horse and quickly made his way over to the woman.'
    show borras at blurin, cright
    hide borras with easeoutright
    show markusprologue at cright_f with easeinright
    show mcprologue at center with easeinright
    show kiara at cleft with easeinleft
    MARKUS 'Captain, wait! Shouldn’t one of—'
    'Before Markus could even finish his sentence, Borras was crouched down in front of the woman, eye to eye with her like she was the only thing in the world.'
    BORRAS 'Ma’am, are you alright? Are there any others?'
    show mcprologue at blurin, center_f
    'We looked behind us to see the Captain galloping towards us, dust and rocks flying out from beneath the thundering hooves of his horse.'
    DUPREY 'GET AWAY FROM HER, YOU FOOLS!'
    'As Borras rested his hands on the woman’s shoulders, it was already too late.'
    show mcprologue at blurin, center
    scene black with dissolve
    $ AutoAmb(False)
    $ AutoMus(False)
    stop ambience
    stop music
    play ambience "audio/cfx/earthquake.ogg" volume 0.5
    'She stopped crying and the ground began to shake violently...'
    $ Pause(0.5)
    play sound "audio/cfx/darkness_erupt.ogg"
    'Her lifeless eyes rolled white as a huge, monstrous... thing dragged itself from inside of her.'
    'Scorpion like in appearance, with tentacles piercing its way through her orifices, it made the {i}dead{/i} woman scream.'
    play sound2 "audio/cfx/scorpion_roar.ogg" volume 0.65
    'The beast was a colossus, tearing down what remained of the house it had hidden under it rose onto its six legs.'
    'It’s skin black and red, its eyes were glowing with malevolence, as it slavered in anticipation.'
    stop ambience fadeout 0.5
    KIARA 'Get out of the way!'
    'Horrified, Borras froze in fear before he moved to grab his sword, but it was too late.'
    play sound2 "audio/cfx/scorpion_spit.ogg" volume 0.8
    play ambience "audio/ambience_scenes/sizzle.ogg" fadein 0.1 volume 2.5
    scene cg_borras_dead with dissolve
    $ CharKill("borras")
    $ CharAddRelEntry("borras", "prol_killed")
    'A toxic acid spewed from the thing’s mouth, Borras tried to roll to dodge the blast but was quickly engulfed and left writhing in agony, animal like cries shuddering through him.'
    'Desperately, he clawed at his own melting face before becoming deathly quiet, limply turning to face us one with only the sizzling sounds of the acid still dissolving through his bones.'
    stop ambience fadeout 10.0
    'His eyes blinked in disbelief that he was about to die, with a trembling hand he tried to motion something with his sword.'
    'There was nothing but horror etched onto what was left of his face before he collapsed, raising the sword up as if he was going to plunge it into himself.'
    'Instead, he planted it in the ground allowing it to take the weight of what we witnessed become his corpse, perhaps in a position he deemed more dignified than lying at the feet of the Demorai that killed him.'
    scene black with dissolve
    $ QstSetProgress(QstTheDarkPass, 3)
    stop ambience
    stop music
    stop sound
    stop sound2
    $ PlayMusic("audio/music/12_BossBattle1.ogg")
    play sound "audio/cfx/scorpion_pain.ogg"
    DUPREY 'ON ME!'
     
    $ PlayerAddItem("potion_heal_minor", 2)
    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_LeftExtra = ["duprey"], CharIDList_Right = ["e_scorpionBoss"], CanTransform = False))

    $ AutoMus(True)
    $ AutoAmb(True)
    scene pbat_desert
    with dissolve

    show markusprologue at left with easeinleft
    show mcprologue at center with easeinleft
    show kiara at cleft with easeinleft

    'Exhausted and at our breaking point, we watched as the thing slumped over to its side, bloodied and taking staggered breaths.'
    'Captain Duprey stormed towards it as it squirmed in agony, trying to drag itself away.'
    'Swinging his axe down one last time onto the thing’s head, in one clean cut Duprey eviscerated its skull and pierced through to its brain.'

    $ QstSetProgress(QstTheDarkPass, 4)

    'We all looked around in horror as we waited for what was to happen next, slowly the Captain turned to look at us with lifeless eyes.'
    show duprey at cright with dissolve
    MARKUS '... C-Captain... It... It just....'
    DUPREY '... We’re nearly there. Come on....'
    MARKUS 'But we—'
    DUPREY '{i}Come. On.{/i}'
    'As Markus stared at Borras’ corpse, frozen in horror, the Captain put his hand almost tenderly on his shoulder.'
    DUPREY 'We keep moving, you understand?'
    'Markus nodded weakly.'
    hide duprey with easeoutright
    'Staggering towards his horse, the Captain clambered onto it and began to trot on ahead.'
    scene black with dissolve
    $ HealParty()
    'The men, horrified at what they had just witnessed, once again fell into place behind him.'
    'By now, any optimism we had felt since our first small battle on the ridge was really and truly gone.'
    'We had all been brutally reminded that out here, we were not the hunters, but the {i}hunted{/i}.'
    play ambience2 "audio/ambience_scenes/march.ogg" fadein 3.0
    $ tmpvar["advancebydays"] = 6
    while tmpvar["advancebydays"] > 0:
        $ TimeAdvBy(86300)
        $ tmpvar["advancebydays"] -= 1
    $ tmpvar = {}
    $ TimeAdvTo(TIME_AFTERNOON)
    $ Pause(0.5)
    $ LocNameSetTemp(_("A forest passage"))
    'More than a week passed since Borras’ death.'
    'Days and days of travelling on mercilessly, Duprey pushing us harder and harder, fuelled by the death of his friend.'
    'We found ourselves marching through the thick, seemingly endless forest, every snap of a twig set us on edge as we looked out for enemies that might be lurking.'
    'I’d never before felt so vulnerable whilst being surrounded by so many people.'
    'I marvelled over how we’d proceeded so long on this journey, carelessly allowing ourselves the hope that we might just be alright.'
    'Now I found my heart was always racing.'
    'I allowed the fear to wash over me every morning, I depended on it to keep me on edge.'
    'Sleep was nightmare after nightmare, I made sure that whenever I did manage to steal a few hours of rest that my sword was always within arm’s reach.'
    'Finally, just as the rain began to hammer down onto the ground and dark grey clouds circled overhead, we arrived at the fort.'
    $ LocSet("qst_darkpass_abandoned_fort")
    $ LocNameReset()
    $ LocFlush(dissolve)
    'As we trudged our way inside the mud-soaked fort through what was left of the gate, we looked around at the dismal lifelessness of the place.'
    stop ambience2 fadeout 5.0
    'There was no sign of anyone and there hadn’t been for a while.'
    'Here and there were scattered the ruinous remains of the old buildings and overturned fruit carts.'
    show duprey at center with easeinleft
    'Perhaps most prominently, and propped up by the various wooden frames, was a colossal tunnel that had been dug into the mountain itself.'
    'Inside it was pitch black, but it was clear from the burned-out torches at the entrance that whoever had inhabited this place had spent a considerable amount of time in these tunnels.'
    'Captain Duprey looked around and then turned to us cautiously.'
    show duprey at right with easeoutright
    show mcprologue at center with easeinleft
    show markusprologue at left with easeinleft
    show kiara at cleft with easeinleft
    DUPREY 'Right, on me, you lot.'
    scene black with dissolve
    $ AutoAmb(False)
    play ambience "audio/ambience_loc/cave.ogg" fadein 3.0
    scene cg_runaway_cave
    with dissolve
    'With freshly lit torches, we followed Captain Duprey deeper into the tunnel.'
    'It seemed to drag on endlessly, meandering up and down, delving deeper and deeper into the mountain.'
    'We finally reached a formidable stone wall blocking our way, inscribed with strange markings I was not familiar with.'
    'As the Captain gently touched his hand on its cold wet surface, the inscribed markings began to glow an ominous red and he stepped back, more cautious than I’d ever seen him.'
    show duprey at right with easeinleft
    DUPREY 'Hmm...'
    show duprey at center with easeoutleft
    'He looked back at the others and whistled.'
    DUPREY 'Get one of those mages down here now!'
    DUPREY 'I’ll bet any one of you a keg of rum that what we’re looking for is behind here.'
    show cg_mage as mage1 at left with easeinleft:
        zoom 0.97
    show cg_mage as mage2 at cleft with easeinleft
    'As a couple of the mages rushed forward, they frantically began to inspect the inscription, running their hands over it and muttering to themselves.'
    hide mage1 with easeoutright
    hide mage2 with easeoutright

    MAGE 'This may take us some time to open, Captain.'
    DUPREY 'Hurry as quick as you can, I don’t like being caught in this forsaken place.'
    DUPREY 'MEN! TAKE POSITIONS ON THE FORT! SECURE THE AREA!'
    play sound "audio/cfx/training_aye.ogg"
    scene black with dissolve
    stop ambience fadeout 2.0
    'We leapt to attention at his order and made our way out once again into the fort.'
    MC '(Wonder what’s behind that thing?)'
    $ LocFlush(dissolve)
    $ AutoAmb(True)
    'The men moved to take positions around the remnants of the fort.'
    'Nervous, I went and asked for some supplies from the supply wagon.'
    $ PlayerAddItem("potion_heal_minor", 2)
    $ PlayerAddItem("potion_heal_regular", 2)
    $ PlayerAddItem("potion_heal_large", 2)
    'There was an eerie silence as we waited and watched impatiently, each of us wondering what had happened here, most of us too scared to voice our ideas.'
    'Painted on the face of every man and woman was the unease of the realisation that we were sitting ducks.'
    'We could do nothing more than pray that the seal would open and we could collect whatever was behind it quickly and leave this haunted place in our memories.'
    "Restless, I was pacing from one watch spot to another."
    $ QstSetProgress(QstTheDarkPass, 5)
    $ LocEnter()

label qst_TheDarkPass_TalkToMarkusInAbandFort:
    $ QstTheDarkPass().AbandFortMarkusTalked = True
    show markusprologue at cright_f with dissolve
    show mcprologue at cleft with easeinleft
    'Markus, much like me, was nervously patrolling the fort grounds.'
    'He feigned an awkward smile as I approached but the tension on his face was obvious. '
    MARKUS 'Hey, everything alright?'
    MC 'Yeah...'
    MC '... What do you think of this place?'
    MARKUS 'I think it’s a lot of bad news...'
    menu:
        'About what happened to Borras...':
            MARKUS 'No offence, [player_name!t], but the last thing I want to think about right now is that.'
            MC 'Right, sorry.'
            MARKUS ' ... {i}His face...{/i}'
            'Markus shook his head as if to push the thought away.'
            MC "Yeah... Let's try to think about something else for now."
            MARKUS "Right..."
        'Seen anything suspicious?':
            MARKUS 'No, thankfully, and I hope it stays that way.'
            MARKUS 'This place is... {i}cursed{/i}.'
            MC '... I might just be inclined to agree with you there.'
    MC "I'll get back to patrolling..."
    MARKUS 'Alright, talk later, [player_name!t].'
    show mcprologue at blurin, cleft_f
    hide mcprologue with easeoutleft
    $ LocEnter()

label qst_TheDarkPass_TalkToMarkusInAbandFort_rep:
    show markusprologue at center with dissolve
    MARKUS "[player_name!t]?"
    MC "Oh, nevermind me, I'm just looking around..."
    MC "(Hopefully this eerie feeling I've got is just that, a feeling.)"
    MARKUS "Right..."
    $ LocEnter()

label qst_TheDarkPass_TalkToKiaraInAbandFort:
    $ QstTheDarkPass().AbandFortKiaraTalked = True
    show kiara at cright_f with dissolve
    show mcprologue at cleft with easeinleft
    'Kiara was waiting patiently by the entrance to the cavern, inspecting the framework that had been setup.'
    KIARA 'They’ve done a good job of making sure it doesn’t fall in on their heads...'
    MC 'What do you think is behind that seal?'
    KIARA 'No idea, I’m afraid.'
    if CharGetVar("kiara", "romanced") == True:
        KIARA 'Hey, when we get out of here, I have a little proposal for you...'
        MC 'Oh?'
        KIARA 'Yeah, I do, but not here...'
        KIARA 'This place is... {i}bad.{/i}'
        MC 'Yeah... I know.'
        KIARA '...You free a moment?'
        MC 'What for?'
        'Kiara bit her lower lip a little, she seemed more anxious than normal but I got what she was hinting at.'
        MC 'What? {i}Now?{/i}'
        KIARA 'I’m just thinking maybe a quick distraction could be good.'
        MC 'We could get in trouble for this.'
        KIARA 'It’ll be quick, five minutes tops...'
        menu:
            'Okay.':
                jump qst_TheDarkPass_KiaraFortBj

            'We really should keep a lookout, this place isn’t safe...':
                KIARA 'I...'
                KIARA 'Yeah, of course, you’re right.'
                KIARA 'I’ll talk to you later.'
                MC 'Talk to you then...'
    else:
        KIARA 'Is there anything I can help you with?'
        MC 'No, just... trying to make myself useful.'
        KIARA 'It’s alright, I got it.'
        KIARA 'Hey... Can I ask you something?'
        MC 'What is it?'
        KIARA 'I... I’ll talk to you after about it, when we have a chance to talk properly.'
        MC '...Alright.'
    $ LocEnter()

label qst_TheDarkPass_TalkToKiaraInAbandFort_rep:
    show kiara at center_f with dissolve
    "Kiara was examining the cavern entrance, peering inside tensely."
    "She noticed me and asked:"
    KIARA "What is it, [player_name!t]?"
    MC "...Nothing, just can't really find a place for myself."
    KIARA "I understand... Let's hope for this to be over soon."
    MC "Right."
    $ LocEnter()

label qst_TheDarkPass_KiaraFortBj:
    MC'Let’s just be quick about it...'
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    'With a small smile, Kiara led me away to a quiet spot in one of the rooms of the old huts.'
    'Outside I could hear the nervous chatter of other Scouts as they passed by on patrol as Kiara crouched down and pulled out my member.'
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene kiara_prol_bj_no_hand with dissolve
    $ Pause()
    'Doing her best to keep quiet, Kiara began to tenderly suck my cock.'
    'Her bright wide eyes looked up to me with doe-like innocence as her lips formed a tight seal around my me.'
    'I did my best to hide my grunts of pleasure as her soft mouth moved back and forth along the shaft soothingly.'
    'Her tongue twisted around me, swirling around my head and making me shiver in pleasure as soft moans escaped through her pursed lips.'
    MC'Ahh... K-Kiara...'
    menu:
        'Put your hand on the back of her head.':
            $ UnlockGalFlag("kiara", "prol_bj", "var_hand")
            scene kiara_prol_bj with dissolve
            'I ran my hands through her short, soft hair, and holding her head in place began to push gently down so she could take my cock even deeper.' #Animation(s) with hand on back of Kiara head
        'Let her continue.':
            $ UnlockGalFlag("kiara", "prol_bj", "var_no_hand")
            pass
    'Sensing my enjoyment Kiara continued enthusiastically, my cock started to throb in her mouth.'
    'Every so often, she would pull away to run her tongue along the shaft and nuzzle at my balls, pulling each of them into her mouth one at a time, delicately surrounding them with her warm, wet mouth.'
    'I ran my hands through her short, soft hair, and holding her head in place began to push gently down so she could take my cock even deeper.'
    'She reached around with her hands and grabbed my ass, pulling me as far into her mouth as she could handle.'
    'For a few moments, I forgot about the nightmarish world outside of this hut and wished I could stay here with her forever.'
    'Knowing I wouldn’t be able to hold on much more, my hands coiled into her hair as I picked up the pace, now thrusting into Kiara.'
    'Unable to hold back, the lewd slurping sounds became louder as Kiara realized I was close to finishing.'
    'As Kiara moaned erotically, my balls began to rise up and tighten as I found myself right on the cusp of losing control.'
    menu:
        "Cum in Kiara's mouth":
            $ UnlockGalFlag("kiara", "prol_bj", "var_in")
            $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
            scene kiara_prol_bj_finish_in with flash
            $ Pause()
            'I gripped her head, pushing myself deeper into her eager mouth, Kiara’s eyes widened as she felt my hot seed pouring into her.'
            'She whimpered and moaned with pleasure, when she was sure I was finished she pulled back, swallowing down my seed and opening her mouth to lewdly show me she had done so.'
        "Cum on Kiara's face":
            $ UnlockGalFlag("kiara", "prol_bj", "var_out")
            $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
            scene kiara_prol_bj_finish_out with flash
            $ Pause()
            "Pulling my cock out of Kiara's mouth, she waited patiently with her mouth and tongue open as after quickly stroking my cock, I covered her face with my hot load."
            "As the thick cum splashed onto Kiara's face, she giggled as she swallowed the part of the load that landed on her tongue."
            KIARA "Fuckin' hells ... Are you sure we're eating the same rations?"
    $ UnlockGalSceneAndGrantXp("kiara", "prol_bj")

    ### achievement
    if "kiara" not in _total_cummed_characters:
        $ _total_cummed_characters.append("kiara")
    
    MC '{i}*Huff*{/i} Oh fuck... That was... That was {i}really{/i} good.'
    'Kiara laughed a little as she kissed my cock before standing up to wipe her mouth.'
    $ AutoMus(True)
    $ LocFlush()
    show kiara at cright_f
    show mcprologue at cleft
    with dissolve
    KIARA '{i}I needed that distraction.{/i}'
    MC 'Me too... Damn...'
    KIARA 'Come on, let’s get back to our posts before anyone realises we’re missing. '
    MC 'Good idea...'
    $ LocEnter()

label qst_TheDarkPass_CaveEntrance:
    MC "An entrance to the cave with the magic seal."
    MC "I wonder what it is, hidden and so well-protected in a place like this..."
    $ LocEnter()

label qst_TheDarkPass_SkipTimeAndGateIsOpen:
    scene black with dissolve
    "Nervous, I wondered about the fort."
    "Scouts exchanged looks of unease and anticipation."
    "We knew in our gut that something is off..."
    MC "(Whatever is behind that door, it should be worth all we have gone through...)"
    MC "(And fucking more.)"
    $ TimeAdvTo(TIME_DAY_END)
    jump qst_TheDarkPass_GateIsOpen

label qst_TheDarkPass_GateIsOpen:
    $ LocFlush(dissolve)
    'Come nightfall, the mages finally dragged themselves out from the tunnel and headed over towards Captain Duprey.'
    show duprey at cleft with dissolve
    show cg_mage at cright with easeinright

    MAGE 'The seal is open, Captain.'
    DUPREY 'Good work, let’s—'
    play sound "audio/cfx/slash_kill.ogg"
    'Suddenly, there was a loud scream from one of the men peering over the wooden wall.'
    hide cg_mage with easeoutright
    'A razor like tentacle swiped through, severing him in half.'
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadein 4.0
    hide duprey with easeoutleft
    $ AutoMus(False)
    $ PlayMusic("audio/music/10_Battle1.ogg")
    'The fort erupted into {i}chaos.{/i}'
    $ QstSetProgress(QstTheDarkPass, 6)
    'People were screaming, panicking, unable to see where or what was coming for us.'
    'Above the terrified din, one man could be heard above the others, "DEMORAI! DEMORAI ON THE WALLS!".'
    show markusprologue at cleft with easeinleft
    show mcprologue at center with dissolve
    show kiara at cright_f with easeinright
    'The first we saw of them was their claws on the upper fence line as they heaved the rest of their bodies over the walls.'
    'Hundreds of Demorai, all of them maniacally drooling as they swarmed us, euphoric at the prospect of devouring everyone below.'
    'We drew our blades and a feverish battle ensued.'
    hide kiara with easeoutright
    hide markusprologue with easeoutright
    hide mcprologue with easeoutright
    DUPREY 'HOLD THE WALLS! STOP THEM FLOODING IN!'
    DUPREY 'FORM A SHIELD WALL BY THE GATE! QUICKLY!'
    hide duprey with easeoutleft
    play sound "audio/cfx/army_aye.ogg"
    'As the men clambered around the gate, shields ready as they tried their best to fend off the ensuing horde, the Captain wildly swung his axe at the endless strays that managed to overpower the wall guards and clamber over.'
    'Turning on my heel I saw Markus and Kiara rush over to me, blades drawn as a small horde approached us, tongues lashing out of their mouths, ready to feast.'
    KIARA '[player_name!t]! LOOK OUT!'

    $ StartBattle(BattleData(BackgroundImage = "pbat_abandoned_fort_night", CharIDList_Right = ["e_demorai_scout", "e_demorai_scout", "e_demorai_scout"], CanTransform = False, AutoNightBackground = False, RiggedOnWinLoot = {"potion_heal_regular":2}))

    $ LocFlush()
    show mcprologue at center
    with dissolve

    MC'{i}*Huff* *Huff*{/i} Come on! We need to help the Captain!'
    show markusprologue at cright_f with easeinright
    show kiara at cleft with easeinleft
    MARKUS 'They’re everywhere!'
    KIARA 'Look! They’re tearing down the bloody walls!'
    'Looking over to the wall, blood and mud now soaking my face, I watched as the wood began to tremble and buckle under the weight of the swathes of Demorai clambering over it.'
    'In a tidal wave of teeth and claws, one side of the wall splintered and collapsed, dragging down with it all the Scouts fighting on it.'
    'Those that survived the collapse were immediately annihilated by the Demorai they found themselves encompassed by down below.'
    MC 'Fuck FUCK! Get back! GET BACK!'
    'As we withdrew towards the entrance of the cave, unable to flee in any direction, some of the archers fumblingly fired off their lit arrows at the Demorai, engulfing them in flames.'
    hide mcprologue with easeoutright
    show markusprologue at blurin, cright
    hide markusprologue with easeoutright
    hide kiara with easeoutright
    DUPREY 'COME AT ME BEASTIES! I’LL HAVE THE LOT OF YA!'
    'With a hard push, we desperately tried to force our way forward to help the Captain who had been encircled, but more of the Demorai vaulted towards us.'
    KIARA '[player_name!t]! Look out! These enemies are different than the last!'

    $ StartBattle(BattleData(BackgroundImage = "pbat_abandoned_fort_night", CharIDList_Right = ["e_demorai_brute", "e_demorai_scout", "e_demorai_scout"], CanTransform = False, AutoNightBackground = False))

    $ LocFlush()
    show markusprologue at cright_f
    show mcprologue at center
    show kiara at cleft
    with dissolve

    stop music fadeout 3.0
    MARKUS '{i}*Huff* *Huff*{/i} They just... {i}*Huff*{/i} Keep coming!'
    MC 'Come on! We’re almost there! The Captain is—'
    play sound "audio/cfx/roar_zan.ogg" volume 0.7
    $ PlayMusic("audio/music/14_Zanaraks.ogg")
    scene black with flash
    'There was a deafening roar that caused the ground itself to shudder, piercing through our very souls.'
    'As we all watched on ahead in horror, the men who had clustered around the gate with their shields and swords were flung aside in one mighty thrust.'
    'Dragging itself forward appeared a terrifying monstrosity unlike anything we had ever seen before.'
    'Almost humanoid in its shape, it stood up on its two thick hind legs.'
    'It’s feet and hands seemed more talon than anything else and its teeth were too large for a mouth which struggled to contain them.'
    'Its wings blocked out what little light there was, forcing us to battle in the darkness it created.'
    'With horns on its head, and a tail thrashing behind it, the thing was so much more than a nightmare.'
    'Its flesh seemed coated in a thick bone-like armour.'
    'One Scout who tried to swing his sword in an effort to pierce the creature, quickly found his blade bouncing off before the monster crushed him with his hand into nothing more than a pile of blood and bones and sinew.'
    show duprey at center with dissolve
    DUPREY 'You... {i}It’s you.{/i}'
    $ Pause(0.5)
    'In its hands, the monstrous being held a huge double ended spear of thick metal that pulsated dark energy.'
    'It seemed as large as the trunk of a tree, towering five times over any man.'
    '{i}... And it was heading right for us...{/i}'
    'The Captain, bloodied and weary, looked towards us as he saw the thing heading our way.'
    'Duprey loudly cried out to grab its attention.'
    scene cg_prologue_duprey1 with dissolve
    DUPREY 'ZANARAK!'
    'Hearing that name sent a shiver down my spine, I felt myself becoming increasingly delirious from all the fighting and bloodshed around me.'
    'It became hard to focus on the enormity of what was happening as that name sunk deep into the core of me, filling me with an icy terror.'
    'I felt that I might collapse at any moment as blackness crept into my vision.'
    'I started to pray for it, thinking it would be a small mercy to give myself over to the darkness and escape the decimation around me.'
    'But the adrenaline snapped me awake and forced me to watch as the two squared off.'
    'The thing glared at him, hatred spewing from its eyes as it became clear the monstrous bogeyman of our childhood {i}recognised him.{/i}'
    DUPREY '{i}After all these years...{/i} Again we face each other!'
    play sound "audio/cfx/demorai_roar_med.ogg"
    DUPREY 'Aye, beasty! So, you DO recognise me!'
    DUPREY ' I knew there was a brain behind that thick fucking skull of yours!'
    'Zanarak turned menacingly towards Captain Duprey, giving him its full attention.'
    DUPREY 'Come on then, you fuck! LET’S SEE YOU TRY TO FUCKING KILL ME!'
    DUPREY 'For Newheart! FOR ALDERAYYYYY!'
    'Lunging forward, the Captain flung himself screaming at the beast, dodging one of Zanarak’s swipes as he brought his mighty axe down on him, slashing at the beast’s ribs with all his strength.'
    'Zanarak staggered, the blade had bounced off his flesh and failed to cut him, but it must have hurt.'
    'The Captain once again moved to dodge Zanarak’s swishing tail as it smashed into one of the walls, flinging everything still climbing them to the mud and blood beneath.'
    'Once again lunging forward, Captain Duprey rolled forward to evade the sweeping swing of Zanarak’s spear and leapt up to attack, smashing Zanarak’s face with his axe, causing him to drop the spear.'
    KIARA 'Why doesn’t his axe pierce its flesh?!'
    MC'I don’t know! It’s hide must be too thick!'
    'While it staggered, the Captain once again continued a fury of heavy hits, causing Zanarak to fumble backwards, blood dripping down his face from where the axe had managed to pierce through his hard skin.'
    'For a moment, it felt like victory was at hand, that the Captain would overcome Zanarak and save the day.'
    DUPREY 'Come on! Is that all you’ve—'
    'Suddenly, Zanarak charged forward with such speed, he caught the Captain off guard. With one backhand of his claw, he sent the Captain tumbling into the mud.'
    'Coughing and retching up blood, he moved to grab his axe once again but before he could, Zanarak was on him, knocking the axe away with his foot as he grabbed Captain Duprey with both hands.'
    'Frantically, we continued to fight our way forward through the hordes of Demorai, but were powerless to save him, we could only watch... {i}and despair.{/i}'
    'As Zanarak squeezed the Captain’s body in its claws, there was a terrible snapping and screeching sound as the Captain retched blood out his mouth.'
    'Zanarak’s tongue licked its lips in anticipation as a cruel smile crawled across its face. It brought the Captain closer, quivering with excitement.'
    DUPREY '{i}Fucking... choke on me...{/i}'
    DUPREY '{i}YOU CUNT!{/i}'
    'In one last effort of defiance, the Captain swung his head forward to smash his forehead against Zanarak, causing his own head to bleed in the process as he spat his blood onto Zanarak’s darkly bemused face.'
    scene cg_prologue_duprey2 with dissolve
    play sound2 "audio/cfx/demorai_roar_high1.ogg"
    'Zanarak, in return, snarled angrily as he crushed the Captain in his powerful taloned hands.'
    play sound "audio/cfx/duprey_death.ogg"
    'Duprey’s agonising scream almost seemed to satiate him before he plunged his jaw forward and greedily tore him apart in a bloody, violent mess.'
    $ CharKill("duprey")
    $ CharAddRelEntry("duprey", "prol_killed")
    stop ambience fadeout 1.0
    stop ambience2 fadeout 1.0
    stop music fadeout 1.0
    'Distantly, I felt Markus’ hand on my shoulder pull me back as the world around me became quiet as a graveyard.'
    'When he spoke, I couldn’t quite hear what he was saying until he shook me violently and sound all seemed to rush back at once.'
    scene bg_abandoned_fort_night
    show markusprologue at cright_f
    show mcprologue at center
    show kiara at cleft
    with dissolve
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadein 3.0
    MARKUS '[player_name!t]! We need to get out of here now!'
    'Shaking my head fearfully, I turned towards Kiara.'
    show mcprologue at blurin, center_f
    MC 'We have to go!'
    'As Kiara battled off some of the Demorai and turned to face me, she suddenly stopped in her tracks with a shudder.'
    stop ambience fadeout 0.5
    scene cg_kiaradeath with flash
    $ Pause()
    $ PartyRemChar("kiara", Silent = True)
    $ CharKill("kiara")
    $ CharAddRelEntry("kiara", "prol_killed")
    $ PlayerRemItem("scout_sword", Silent = True)
    $ PlayerRemItem("scout_armor", Silent = True)
    'Peering down in an almost comical confusion she noticed what we all saw happen; a tentacle had thrust its way through Kiara’s chest.'
    'I looked at her, and she me, paralysed with terror.'
    'With a trail of blood seeping from the side of her mouth, she simply said...'
    KIARA '{i}Run...{/i}'
    'And with that Kiara was flung backwards into the throes of battle.'
    play ambience "audio/ambience_scenes/battle_cave.ogg" fadein 5.0
    'Feeling a surge of manic grief, I screamed as I tried to fling myself forward to save her, but Markus used all his strength and held me back.'
    MARKUS 'IT’S TOO LATE, SHE’S GONE!'
    'Determinedly pulling me back, Markus cried...'
    MARKUS 'The battle is lost! We have to retreat!'
    MC'We’re surrounded!'
    'Markus looked around wildly, staring back at the entrance to the cavern and pulled me along.'
    MARKUS 'Come on! It’s the only way!'
    stop music fadeout 3.0
    scene black with dissolve
    $ Pause(1.0)
    $ AutoTimeFreeze(True)
    scene cg_mc_eye with flash
    MC "HURRY!"
    MARKUS "It won’t close!"
    MC "CLOSE IT! CLOSE THE FUCKING DOOR!"
    MARKUS "I’m trying!"
    MC "MARKUS! HURRY! IT’S NEARLY—"
    scene black with flash
    $ Pause(0.5)
    stop ambience fadeout 3.0
    $ LocSet("qst_darkpass_obelisks")
    $ LocFlush()
    show markusprologue at cleft
    show mcprologue at cright_f
    with dissolve
    stop ambience fadeout 5.0
    'Exhausted, caked in dirt and grime, me and Markus looked at each other wearily.'
    'The sounds of fighting outside had slowly died down, only an eerie silence was left.'
    'We found ourselves speaking in whispers.'
    MARKUS 'Are we...?'
    MC '{i}We’re the only ones left.{/i}'
    'The dawning realisation caused the blood to run cold in our veins, slowly we turned to look around at what may be our tomb.'
    'The chamber was unusual.'
    'Two strange obelisks stood menacingly in the center of the room.'
    $ AutoMus(True)
    $ AutoAmb(True)
    show mcprologue at blurin, right_f with easeoutright
    show markusprologue at blurin, left with easeoutleft
    'One of the perfect pair black, the other white, they looked timeless, ancient.'
    MC 'What are those?...'
    #show mcprologue at blurin, cright
    'Reluctantly shifting my gaze to examine the room, I saw tables full of vials and half empty potions.'
    'Various pieces of paper were scattered around the floor — someone had left in a hurry.'
    MARKUS 'What is this place?'
    MC 'I can’t even guess...'
    MC 'There has to be a way out of here though so, let’s see if we can find some kind of secret exit or something...'
    hide markusprologue with easeoutleft
    MARKUS '{i}*Sigh*{/i} Well, it sure beats waiting around to die...'
    $ QstSetProgress(QstTheDarkPass, 7)
    $ BlockWaitGlobal(True)
    $ LocEnter()

label qst_TheDarkPass_ObelisksRoomPapers:
    $ QstTheDarkPass().ObelisksRoomSeenPapers = True
    show mcprologue think at cright_f with easeinright
    show mcprologue think at nod
    "Picking up some of the papers, I tried to piece them together and decipher some of what was going on."
    "{i}‘Subjects remain in petrified state until we can discover a means to try quelling their ‘parasitic’ natures.{/i}"
    "{i}Neither Kern, Luxma, Burning Wings or Scun seem to have any chemical impact on ‘controlling’ them.’{/i}"
    "Hastily scribbled on the bottom was..."
    "{i}‘All other current botanic ingredients local to Alderay have proven ineffective, requesting more ‘exotic’ ingredients to test with from neighbouring kingdoms.’{/i}"
    "{i}‘Just what will it take to get these things under control?’{/i}"
    MC "(What are they talking about?)"
    $ LocEnter()

label qst_TheDarkPass_ObelisksRoomSkeleton:
    $ QstTheDarkPass().ObelisksRoomSeenSkeleton = True
    show mcprologue think at cleft with easeinleft
    show mcprologue think at nod
    "Slumped down dead against the wall, still in his dark dusty robes, was the body of a Dark Mage clutching at some letter in his hands."
    MARKUS "What’s a Dark Mage doing here?"
    MC "I don’t know..."
    "Reaching down, I pulled the crumpled letter from the skeleton hands of the Dark Mage."
    "As I did so, some the skeleton's bones disintegrated into ash right before my eyes."
    "‘Consider this my final gift unto you, {i}my lord{/i}, I die safe in the knowledge that once you retrieve these things, you will finally turn the tide of this war...’"
    "‘But be wary, their power is still highly unstable... Choose only the finest to wield them, for to choose any less would spell {i}disaster{/i} for the realm.’"
    "‘Yours faithfully, forever, Kharlof.’"
    MC "(My lord? Turning the tide of the war? What is he talking about?)"
    $ LocEnter()

label qst_TheDarkPass_ObelisksRoomPotions:
    $ QstTheDarkPass().ObelisksRoomSeenPotions = True
    show mcprologue think at cright_f with easeinright
    show mcprologue think at nod
    "Inspecting the dust covered tables of potions, I tried reading the dozens of labels on each of the various jars and vials but recognized almost none of the ingredients."
    MC "What is all this for?"
    show markusprologue confused at left with easeinleft
    "Markus glanced over the potions and picked one up:"
    MARKUS "They were certainly working hard to solve... {i}something{/i}."
    $ LocEnter()

label qst_TheDarkPass_ObelisksRoomCheckObelisks:
    show markusprologue confused at cleft with easeinleft
    show mcprologue think at cright_f with easeinright
    'Apprehensively, the two of us finally made our way over to the obelisks.'
    'As I listened closely, I could almost hear a... {i}a heartbeat?{/i}'
    MARKUS 'What are these things?'
    'Feeling a gnawing urge to reach out and touch the monument, I rested my hand on its ice-cold surface.'
    scene cg_obelisks with dissolve
    'I’ve noticed Markus doing the same...'
    'This alone frightened me, and with a shudder I withdrew my hand just as fast.'
    'Markus looked at me, pulling his hand back as well.'
    MARKUS 'You okay?'
    MC'This is weird, I thought—'
    #scene cg_obelisks glow with dissolve
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/obelisks.ogg" fadein 3.0
    'Suddenly, both monuments began to illuminate with colorful markings...'
    'We stepped back fearfully, holding out our swords and mustering the remainders of our strength, naively hoping to protect ourselves from whatever dark magic these stones were channeling.'
    MARKUS 'Why did you touch it?!'
    MC'I don’t know! I felt I had to—'
    play sound "audio/cfx/darkness_erupt.ogg"
    play ambience2 "audio/ambience_scenes/whispers.ogg" fadein 5.0
    scene cg_obelisks_tentacles with flash
    '{b}A black mass of slithering tentacles{/b} erupted from the monument I fixed my gaze upon.'
    'Shocked, I instinctively tried to swing my sword at it, only to find my arm firmly locked in place, one of the squirmy limbs coiling tightly around it.'
    'In an instant, I was engulfed by the dark entity.'
    'Unable to fight it I broke into a desperate struggle, primordial terror clawing its way into my very soul.'
    stop ambience2 fadeout 5.0
    'The last thing I saw was Markus, devoured by a similar abomination bursting out from the second monument...'
    '...only of {i}pure white{/i}.'
    $ AutoMus(False)
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    scene black with dissolve
    $ DEBUG_PlayerRemoveAllItems()
    $ PartyRemChar("markus", Silent = True)
    $ Pause(0.5)
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("markus", "normal")
    play ambience2 "audio/ambience_scenes/obelisks.ogg" fadein 1.0
    play ambience "audio/ambience_scenes/darkdreams.ogg" fadein 1.0
    "Dark dreams circled in my head..."
    "...visions of hundreds of naked women of all the different races I had never seen..."
    "...fawning over me desperately, moaning in intense pleasure as I sat on what seemed like a golden throne..."
    "...storm clouds gathering overhead as lightning forked to the world below..."
    stop ambience fadeout 1.0
    stop ambience2 fadeout 1.0
    $ tmpvar["advancebydays"] = 7
    while tmpvar["advancebydays"] > 0:
        $ TimeAdvBy(86300)
        $ tmpvar["advancebydays"] -= 1
    $ tmpvar = {}
    $ TimeAdvTo(TIME_NOON)
    $ AutoTimeFreeze(False)
    $ LocSet("novaras_fort_seb_medward")
    $ LocFlush()
    $ HealParty()
    show bg_medwardoverlay onlayer characters
    with flash
    "My eyes shot open as I sat bolt upright in horror."
    "Drenched in sweat, I looked around frantically to get some sense of bearing on where I was."
    "I was sitting on one of many rows of beds made up in a stone-cold room."
    $ AutoMus(True)
    "Looking around I realised I was in... {i}Fort Sebastian?{/i}"
    "{i}The medical ward{/i}?"
    MARKUS '[player_name!t]...'
    show markusprologue at left behind bg_medwardoverlay with easeinleft
    'I turned my head to look to my side, Markus was leaning on the wall near the next bed, looking even paler than usual, his eyes dark and foreboding.'
    'One would think he was on death’s door as he spoke to me.'
    MC "How did we... {i}get here?{/i}"
    MARKUS "I don’t know... The nurses told me..."
    MARKUS "They found us naked outside the gates."
    MC "The gates? Are we—"
    MARKUS "Yeah... We’re home."
    "Despite my mind being awash with questions, I could at least allow a deep sigh of relief that we had by some miracle survived {i}the horrors of that abandoned fort{/i}."
    "My mind turned to Captain Duprey, Borras... {i}Kiara...{/i}"
    "I heard a clanking sound approaching and looked towards it."
    "A huge figure walked towards us, accompanied by four heavily armed guards and a beautiful mage."
    show kylisa behind bg_medwardoverlay at right with easeinright
    "Naturally, the mage caught my wandering gaze, but just as I managed to focus a familiar, menacing voice opened up..."
   
    MENACING_VOICE "Check them both."
    BEAUTIFUL_MAGE "Of course, my lord."
    show kylisa behind bg_medwardoverlay at center with move
    "As the mage stepped forward, I could not help but stare at her chest, deep cutout of her robes displaying a fair portion of her breasts."
    "My heartbeat rose, an unnatural wave of passion caressing my weakened body..."
    "She spoke in a soft, raspy voice, pointing her staff at me:"
    BEAUTIFUL_MAGE "Hold still."
    play sound "audio/cfx/detect_magic.ogg"
    show vfx_magick_glow with flash:
        anchor (0.5, 0.5)
        pos (0.59, 0.19)
        zoom 0.6
    "Her staff lit up, warm light following its cryptic tip as she slowly held it over my body, head to toe."
    "Markus was next, the procedure seemingly soothing his aching psyche."
    "In a few moments the mage was through examining us."
    hide vfx_magick_glow with dissolve
    show kylisa behind bg_medwardoverlay at cright with move
    "Her full, purple lips let out a conclusive mutter, then she spoke up:"
    BEAUTIFUL_MAGE "They do not possess magic, nor do they reek of any magical essence that shows they have been possessed or tainted by the Demorai’ magic."
    show alcott behind bg_medwardoverlay at center_f with easeinright
    MENACING_VOICE "Thank you, Kylisa, you may go now."
    show kylisa at nod
    'Kylisa bowed, as she stepped away and left the ward.'
    hide kylisa with easeoutright
    'Emperor Alcott’s attention was fully diverted to us now.'
    ALCOTT 'It is good to see you awake.'
    ALCOTT 'Now then, it’s time you boys told me what the hell happened out there.'
    'Clearly still deranged, I questioned if I was still dreaming...'
    '...or was it indeed Emperor Alcott himself, standing before me and Markus, giving a damn about what we’ve got to say.'
    ALCOTT "... You two deaf?"
    "I did my best to muster an answer."
    MC "I... My lord... I..."
    ALCOTT "Out with it!"
    MC "We reached the fort as instructed, my lord."
    MC "It was abandoned, but we were hit by a huge Demorai force."
    ALCOTT "How many?"
    MC "I don’t know, sir... Hundreds... maybe thousands..."
    ALCOTT "...Hmm..."
    MC "... {i}That thing{/i}... it killed Captain Duprey."
    ALCOTT "Who? What thing? What are you talking about?"
    MC "Demorai... Captain Duprey called it {i}Zanarak.{/i} It was there..."
    "For just a moment, the Emperor’s stoic face cracked as he heard those words, even his armed guards turned to glance at each other, the scent of fear now hanging in the air."
    ALCOTT "I see..."
    "After a brief pause, he proceeded:"
    ALCOTT "What did you find in the fort? Did you recover anything?"
    MC "As I searched for an answer, I suddenly felt the faintest voice in the back of my head whispering something."
    "Too distinct to be my own internal thoughts and yet..."
    BLACK_VOICE "{i}No.{/i}"
    MC "... No, sir."
    "I noticed that Markus had realised I was lying — he quickly looked to hide his expression."
    "The Emperor raised a curious eyebrow."
    ALCOTT "{i}‘No’?{/i}"
    MC "Everything inside was destroyed, the Demorai must have reached it long before we did."
    "My foggy mind didn’t seem to bother lying straight to Alcott’s face."
    ALCOTT "I see..."
    MC "Everyone was killed, we barely made it out alive..."
    "To my own surprise it effortlessly weaved together a story, line after line, of our escape."
    ALCOTT "No survivors?"
    MC "We were the only ones."
    "I felt as if {i}someone else{/i} took over."
    ALCOTT "And how did you two escape exactly?"
    MC "We managed to make a break for it after locking ourselves away in the tunnels, sir."
    MC "By nightfall they had left the fort, so we made our way back."
    "Alcott crossed his arms on his chestplate as he slowly paced the next question:"
    ALCOTT "You expect me to believe that you two made a month-long journey through enemy lands..."
    ALCOTT "On foot, alone, injured, starving..."
    ALCOTT "...{b}In one week?{/b}"
    "What?..."
    MC "A w— It’s only been a week?!"
    "Through just the slightest lowering of his eyebrows Alcott betrayed his surprise of my reaction."
    "Seconds later the emotionless mask was back in place."
    ALCOTT "Now give me {i}the truth{/i}."
    MC "I... That’s all I can remember."
    ALCOTT "Believe me when I say that you do not want to lie to me."
    MC "My lord, it is the truth!"
    MC "I can only remember so much of the journey back."
    MC "The rest... If there was anything, it is {i}missing{/i}..."
    "Alcott looked over towards Markus."
    ALCOTT "What about you?"
    ALCOTT "Do you have anything to add?"
    "Markus shook his head grimly."
    ALCOTT "How inconvenient."
    "Alcott took a thoughtful pause, then, as if remembered something, asked:"
    ALCOTT "Why were you both naked when we recovered you?"
    MC "I... I don’t know, sir."
    MC "Everything is daze, I’m sorry, my lord, it all feels like a nightmare..."
    ALCOTT "Hmm. I see."
    ALCOTT "You best hope your memories return swiftly, there are still many questions about what has happened to the Second Scouts."
    ALCOTT "Questions {i}I{/i} want answers to."
    MC "... I will do my best to remember, my lord."
    'I was convinced that Alcott did not entirely believe my story, but it must have satisfied him enough for now at least.'
    ALCOTT "... In light of the unusual circumstances surrounding the Second Scouts Division and the danger you single-handedly faced along with the losses your unit suffered, you are both hereby relinquished of your duties as Scouts."
    MC "Sir? You mean—"
    ALCOTT "HOWEVER, the two of you shall instead sign up to the Adventurer’s Guild."
    MC "The... The {i}Adventurer’s Guild?{/i}"
    ALCOTT "You are free to live and stay in the Capital unless the city itself falls under siege, upon which you, like all other able bodied, are still bound to heed the call to arms."
    ALCOTT "Elsewise you shall serve the Empire as Guild members instead."
    ALCOTT "This is offered to you solely on the highly unusual circumstances surrounding your... survival."
    ALCOTT "You are now far more useful to me alive than dead."
    ALCOTT "Both of you are forbidden to speak about your mission and its failure to anyone, understand?"
    "Me and Markus both nodded, giving our best ‘yes, sirs’."
    show markusprologue at nod
    ALCOTT "In return for this you will both {i}also{/i} be required to help me with... {i}raising morale.{/i}"
    "Both me and Markus just looked at each other, clueless."
    MC "... Sir?"
    ALCOTT "As far as anyone is concerned, you two single-handedly and {i}bravely{/i} fought together, slaying dozens of Demorai and returned not as lone survivors, but as {i}heroes{/i}. Understand?"
    MC "But—"
    ALCOTT "As of now, most of the city is talking about the two surviving heroes."
    ALCOTT "I intend to salvage something out of this affair to help people keep the faith."
    ALCOTT "They {b}will not{/b} hear of the massacre that you walked into, that story will die in this room and you two will only speak of the bravery and courage of your comrades."
    "The Emperor wants us..."
    "{i}To lie?{/i}"
    ALCOTT "Given the fate you have managed to escape, visiting public places to wave and smile around is not such a bad alternative."
    ALCOTT "Don’t you agree?"
    MC "... Yes, sir."
    MARKUS "Yes, my lord."
    ALCOTT "Good. I will leave you to rest now."
    ALCOTT "Farewell."
    hide alcott with easeoutright
    "The Emperor sauntered off with his guards."
    "I’ve let all the news sink in, then turned to Markus."
    "A sense of immense joy ignited deep inside me, as I have realised..."
    MC "We survived!"
    "Markus smiled back at me, and for the first time in what seemed like an eternity..."
    "{i}We truly felt our nightmare was over.{/i}"
    scene black with dissolve
    $ AutoMus(False)
    stop music fadeout 1.0
    $ Pause(0.5)
    $ TimeAdvTo(TIME_LATENIGHT)
    play ambience2 "audio/ambience_scenes/obelisks.ogg" fadein 5.0
    "I awoke in the dead of night, drenched in sweat."
    "Strange dreams plagued me where black liquid permeated my lungs and slithered its way through my veins until it filled my whole body, suffocating me from the inside out."
    $ LocFlush(dissolve)
    "Staggering out of bed, I dragged myself along the cold tiles over towards the stone taps."
    show mcprologue think at cleft with easeinleft
    "With both hands I splashed my face and—"
    $ AutoAmb(False)
    play ambience "audio/ambience_scenes/whispers.ogg" fadein 5.0
    BLACK_VOICE "{i}Hi...{/i}"
    show mcprologue think at blurin, cright_f with easeoutright
    "I jumped backwards, looking frantically around for the guttural, dark voice that spoke to me."
    "There were those asleep on the ward, but no one else awake or stirring."
    BLACK_VOICE "{i}Stop...{/i}"
    "I quickly wondered had I gone mad? Or had—"
    BLACK_VOICE "{i}Stop...{/i}"
    show mcprologue think at blurin, cleft with easeoutleft
    "With both hands clasping at my head, I hit myself until..."
    BLACK_VOICE "{i}STOP!{/i}"
    "My heart racing, with deep heavy breaths I whispered in my quietest voice."
    MC "... Who are you? {i}Where{/i} are you?"
    BLACK_VOICE "{i}In head.{/i}"
    MC "What?"
    BLACK_VOICE "{i}In head...{/i}"
    MC "What do you...? What do you want?"
    BLACK_VOICE "{i}Keep safe. Words... not... good... yet.{/i}"
    BLACK_VOICE "{i}Protect host.{/i}"
    MC "‘Host’? What are you—"
    show mcprologue think at blurin, cright_f with easeoutright
    "There was some shuffling from one of the beds, as I peered over to check, someone had simply rolled over onto their side and groaned a little, presumably in pain."
    BLACK_VOICE "{i}Learning... Assimilating...{/i}"
    BLACK_VOICE "{i}Need. Time. Talk. Better.{/i}"
    MC "... So, you’re not going to hurt me?"
    BLACK_VOICE "{i}Protect... host.{/i}"
    BLACK_VOICE "{i}Need. Rest.{/i}"
    MC "Can’t sleep... It’s like I’m burning up..."
    BLACK_VOICE "{i}Will... temperature... lower... Assimilate slower... Rest...{/i}"
    "As I felt my body suddenly begin to cool, I felt drowsy once again."
    MC "What do you mean... assilim... assim—"
    BLACK_VOICE "{i}Rest. Protect host.{/i}"
    stop ambience fadeout 4.0
    stop ambience2 fadeout 4.0
    scene black with dissolve
    "Dragging my feet, I made my way over towards my bed and collapsed down onto it, drifting away into dreams of darkness once again..."
    $ Pause(1.0)
    $ HideUI(True)
    scene cg_kiaraend1 with dissolve
    play ambience "audio/ambience_loc/grassland.ogg" fadein 1.0
    "A beautiful, purple-skinned Demorai woman was wandering around the scattered dead in the abandoned fort..."
    UNKNOWN "My, my... What have we here?"
    scene cg_kiaraend2 with dissolve
    "She knelt beside Kiara, examining her cold body."
    UNKNOWN "No, no, {i}no...{/i} This will simply not do."
    "After picking her up gently, the Demorai woman walked away, murmuring wistfully."
    stop ambience fadeout 3.0
    scene black with dissolve
    jump qst_FromAnotherWorld_Start