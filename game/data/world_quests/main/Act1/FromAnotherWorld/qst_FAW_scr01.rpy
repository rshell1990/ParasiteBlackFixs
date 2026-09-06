label qst_FromAnotherWorld_Start:
    show text _("{size=150}ACT 1{/size}") with dissolve:
        yalign 0.5
    $ Pause()
    hide text
    $ HideUI(False)
    $ PlaySoundRandom("clockWind", Channel = "guisfx", Volume = 0.7)

    $ TimeAdvTo(TIME_MORNING)
    $ AutoMus(True)
    $ AutoAmb(True)
    $ CharSetClothes("mc", "pants")

    $ LocFlush()
    show bg_medwardoverlay onlayer characters
    with dissolve
    $ QstComplete(QstTheDarkPass)
    'Outside, I could hear birds chirping as they perched on the rooftops.'
    

    $ AddNotif(_("All your attributes have increased by 1."), Kind = "attr_raised")
    'As my eyes peeled open and the bright light from the stained-glass windows blazed into the infirmary, I rose from my slumber, still groggy, the light piercing my pounding head.'
    'Slowly, my blurred vision started to restore itself.'
    'I groaned painfully, my entire body aching.'
    'As I reached up to rub my temple, I noticed a peculiar thickness to my arm, which now appeared to be bulging with muscles and veins.'
    show mc at left behind bg_medwardoverlay with easeinleft
    MC '...What?'
    'Rising out of bed, I hauled myself over to the mirror, the reflection that stared back at me was not the same man as last night.'
    'I had grown a few inches in height and across every inch of my body was a layer of thick, refined muscle, defiant beneath my hospital gown.'
    'My cheekbones and jaw were far more defined than they had been, my hair was thicker and longer, as I ran my tongue along my teeth, even they felt straighter and stronger.'

    
    MC @surprised '...!'
    MC @surprised 'What... What’s happened to me?'
    MC @surprised 'That... {i}That horrible dream last night{/i}... It can’t have...'
    'I tried to call out to the thing that I dreaded to find lurking deep inside of me, desperate to know if I’d fabricated the events of last night... or not, but no answer came.'
    MC @sad 'It— I don’t remember...'
    'Looking down at the dent in the fabric tangled round my waist, I couldn’t resist the curiosity and peered under it to see if ‘everything’ had grown and, indeed, I found myself smiling slyly with the realisation that it had.'
    'Before I could get too excited about that particular aspect, I heard Markus’ voice call my name.'
    'Spinning around with a sense of dread, it became immediately apparent that Markus, too, had changed.'
    'Like mine, his face was more refined, more handsome, his hair now flowed in long golden curls, bouncing off his shoulders.'
    'His body too had become stronger, his muscles pressed against the material of his clothes which now struggled to contain them.'
    show markus at center_f behind bg_medwardoverlay with easeinright
    MARKUS @smile "Nice to see you’re up."

    $ tmpvar = {}
    $ tmpvar["faw_markus_firsttalk"] = ["what_happened", "you_look_diff", "where_is_everyone"]
    menu qst_FromAnotherWorld_Start_MarkusFirstTalk:
        "Markus! What’s happened?" if "what_happened" in tmpvar["faw_markus_firsttalk"]:
            $ tmpvar["faw_markus_firsttalk"].remove("what_happened")
            MARKUS "I’m not sure, I woke up about half an hour ago and apparently, I look like this now."
            MARKUS "I tried to wake you, but you were completely out of it."
            jump qst_FromAnotherWorld_Start_MarkusFirstTalk
        "You look... {i}different{/i}." if "you_look_diff" in tmpvar["faw_markus_firsttalk"]:
            $ tmpvar["faw_markus_firsttalk"].remove("you_look_diff")
            MARKUS "Yes... As do you."
            MC @talk "We need to talk about— "
            "Markus motioned frantically for me to shut up, nodding towards the door where guards were waiting outside."
            MARKUS "Yes... I think we’ll both need a drink later."
            MC @talk "... Yeah."
            jump qst_FromAnotherWorld_Start_MarkusFirstTalk
        "Where is everyone?" if "where_is_everyone" in tmpvar["faw_markus_firsttalk"]:
            $ tmpvar["faw_markus_firsttalk"].remove("where_is_everyone")
            MARKUS "I don’t know... A nun came here a while back to give me some water, she said a guard would be by shortly to speak to us."
            jump qst_FromAnotherWorld_Start_MarkusFirstTalk
        "Come on, we need to get out of here...":
            pass

    show lukkan at right_f behind bg_medwardoverlay with easeinright
    'As I finished speaking, the door unlocked and a high-ranking officer stepped inside with a few crumpled papers in his hand.'
    
    OFFICER @talk 'Good morning...'
    'We both stared nonplussed at the figure before us.'
    MC @talk '... Morning.'
    OFFICER 'I am Officer Lukkan.'
    LUKKAN @talk '... You two must be Markus Lucidican and [player_name!t]...'
    show lukkan at nod
    'The officer fumbled, checking the paperwork for a moment before looking up.'
    LUKKAN @talk 'Eh, fuck it, I got the right pair, right?'
    MARKUS 'Yes, that’s us.'
    LUKKAN @talk 'Right, I have come here today in representation of Emperor Alcott and hereby bestow upon you both a full pardon from active military service.'
    LUKKAN @talk 'Here are your membership certificates for the Adventurers Guild and so on and so forth.'
    LUKKAN @talk 'You’ve both already been approved, so it’s just a case of having you show up and introduce yourself...'
    MC @talk 'The Emperor said we have some type of ‘morale raising’ duty to fulfil?'
    LUKKAN @talk 'Yep, that’s right... We aim to hold at least one ‘Morale Rally’ a week, it’s good for the people to still feel we can win this war.'
    MC @talk 'Because we can... right?'
    LUKKAN @talk '... Uhhh... Yeah, sure, absolutely.'
    LUKKAN @talk 'Under the Emperor’s orders you’ll be expected to attend at least one a month.'
    LUKKAN @talk 'Do you understand?'
    $ tmpvar = {}
    $ tmpvar["faw_lukkan_talk"] = ["morale_rally", "if_we_forget", "where_do_we_go"]
    menu qst_FromAnotherWorld_LukkanTalkMenu:
        '‘Morale Rally’?' if 'morale_rally' in tmpvar["faw_lukkan_talk"]:
            $ tmpvar["faw_lukkan_talk"].remove('morale_rally')
            LUKKAN @talk 'They can be a relatively small or much larger affair depending on the individual who’s speaking.'
            LUKKAN @talk 'You could be asked to make a small speech at some tavern or on a podium in the street, talking about your heroic victories in battle or whatever it was you did to earn such favour with the Emperor.'
            LUKKAN @talk 'Keep it optimistic, boys... No breaking down talking about how you saw your best friend sliced in half and we’ll get along just fine.'
            MC @talk '... That’s it?'
            LUKKAN @talk 'Were you hoping for screaming crowds of adoring fans?'
            LUKKAN @talk 'You kids are small time... In fact, from your notes I’m not even sure why the Emperor’s awarded you so many privileges to begin with.'
            MC @talk '...'
            LUKKAN @talk '... But I suppose if you build on your reputation, perhaps we could make it a grander affair, so to speak.'
            jump qst_FromAnotherWorld_LukkanTalkMenu
        'What happens if we forget?' if 'if_we_forget' in tmpvar["faw_lukkan_talk"]:
            $ tmpvar["faw_lukkan_talk"].remove('if_we_forget')
            LUKKAN @talk 'If you ‘forget’, me and a few other officers will be dragging your sorry asses out of whatever dive you’re in and throwing you onto the bloody stage, and believe you me, we will not be gentle.'
            MC @talk 'What if we’re away on a quest?'
            LUKKAN @talk 'As long as your service to the Emperor is fulfilled, {i}one way or another{/i}, I really do not care.'
            LUKKAN @talk 'When you get back from whatever quest you’re on, it’s straight back to business as usual.'
            MARKUS 'I take it refusal isn’t an option?'
            LUKKAN @talk 'Sure, that’s an option!'
            LUKKAN @talk 'But if you don’t do as you’re told...'
            LUKKAN @talk '... You’ll find yourself back in the Scouts, serving the Emperor another way.'
            MARKUS 'Well, aren’t we spoiled for choice...'
            jump qst_FromAnotherWorld_LukkanTalkMenu
        "Where do we go to find out about this 'morale raising'?" if 'where_do_we_go' in tmpvar["faw_lukkan_talk"]:
            $ tmpvar["faw_lukkan_talk"].remove('where_do_we_go')
            LUKKAN @talk 'You can find me in my office on the third floor of the Central Fort.'
            LUKKAN @talk 'I manage all morale raising services and events around the kingdom, so just speak to me when you are able to attend and I will arrange a small rally.'
            jump qst_FromAnotherWorld_LukkanTalkMenu
        'Yes, we understand.':
            pass
    $ tmpvar = {}
    LUKKAN @talk 'Good, now both of you get dressed and make sure you hand in your paperwork to the Guild later.'
    MC @talk 'Are we free to go?'
    LUKKAN @talk 'For now.'
    $ CharMeet("lukkan")
    show lukkan at right_f, blurin
    hide lukkan with easeoutright
    'The man said nothing else, just turned on his heel to leave and closed the doors behind him with a resounding finality.'
    MARKUS 'Well, you heard the man.'
    MC @talk 'We should both head home first... let them see with their own eyes that we’re okay.'
    MC @talk 'Then we can head over to the Guild together.'
    MARKUS 'Agreed...'
    MARKUS 'Then let’s get that drink later... old friend.'
    MARKUS "By the way..."
    "Markus looked at me head to toe:"
    MARKUS "You should grab some... fitting clothes from the quartermaster."
    MC @talk "That psycho? I'm not having anything to do with him."
    MARKUS "Come on, you want to strut around looking like this, you'll never make it home."
    MARKUS "Crowds of fan-girls will stomp you into the streets."
    MC @talk "*Sigh* Okay, I'll talk to Joakim."
    MC @talk 'I’ll see you later then.'
    hide markus with easeoutright
    'Markus nodded and left.'
    scene black with dissolve
    "I went to see Master Joakim as Markus had suggested."
    "He was excited to see me alive {i}and{/i} in my new shape, commenting sarcastically on how the army 'brings out the best in men'..."
    "After sizing me up, he cobbled together a set of somewhat worn clothes and light armor bits for me."
    $ PlayerAddItem("leather_armor")
    if CanEquip(0, "leather_armor", EQP_SLOTS.CHEST[0]):
        $ EquipItem(0, "leather_armor", EQP_SLOTS.CHEST[0])
    $ TooltipClear()
    "When I asked where these clothes come from, he just gave me {i}that grin{/i} of his..."
    "Clean and well-fit as they were, I hoped the previous owners died a peaceful death."
    "As I was about to leave, Joakim pointed at a pile of rusty metal in the corner:"
    JOAKIM "Hey, you should grab one of these too."
    JOAKIM "I don't want to see that fresh and strong body of yours wandering about unarmed."
    "He smiled and watched me examine one of the {i}better condition{/i} swords I picked up from the pile."
    $ PlayerAddItem("scout_sword_rusty")
    if CanEquip(0, "scout_sword_rusty", EQP_SLOTS.HANDS[0]):
        $ EquipItem(0, "scout_sword_rusty", EQP_SLOTS.HANDS[0])
    $ TooltipClear()
    "Considering it a weapon would be a stretch."
    MC "...Okay, thanks I guess."
    JOAKIM "The Corp provides!"
    JOAKIM "Okay, off you go now! I've got some fresh recruits to work on."
    $ CharSetClothes("mc", "normal")
    $ LocFlush(dissolve)
    show mc at left with easeinleft
    $ QstStart(QstFromAnotherWorld)
    MC 'I guess it’s time to head home.'
    scene black with dissolve
    $ LocSet("novaras_dist_army")
    $ LocFlush(dissolve)
    show mc at left with easeinleft
    "Walking out of Fort Sebastian, I inhaled deeply and felt a tinge of relaxation:"
    MC "(Novaras City.)"
    MC "(Home.)"
    MC "(At least it was before I got into this whole Scouts thing...)"
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_house")
    $ LocFlush(dissolve)
    show mc at left with easeinleft
    "Taking a few steps towards my house, I imagined talking to [regina_ref_cap!t] and hesitated a bit."
    MC "(Will she even recognize me?)"
    MC "(*Sigh* It feels like an eternity has passed since I left.)"
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    jump qst_FromAnotherWorld_ReturnHome
