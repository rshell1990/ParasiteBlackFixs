label qst_TheTarbecks2_enter_manor:
    show cg_guard_hamun at cright_f
    with dissolve
    show mc at cleft with easeinleft
    GUARD "Ah, Lady Tarbeck said to escort you straight to her upon arrival."
    GUARD "Please, come with me."
    scene black with dissolve
    $ LocSet("hamun_tarbeck_dining")
    $ LocFlush()
    show lady_tarbeck at cright_f 
    with dissolve
    "Following the guard, he led me towards the dining room where Lady Tarbeck sat, carefully sipping at her tea."
    show mc at cleft with easeinleft
    "Her eyes slowly lifted towards me with distant displeasure."
    LADY_TARBECK @think "Thank you for coming."
    LADY_TARBECK @angry "Now that you're here, I want to make one thing clear..."
    LADY_TARBECK @angry "{i}I have no need of you, nor do I have any interest in my husband's perverted games.{/i}"
    LADY_TARBECK @angry "And I CERTAINLY have no interest in helping those ghoulish GTC monsters."
    LADY_TARBECK @happy "So, I'm afraid you're just wasting your time here."
    SHYAHTAN "(Slow... Go slow for this one.)"
    MC @talk "... Very well."
    MC @smile "Then at least allow me to walk with you and guard you for the day."
    LADY_TARBECK @think "Didn't you just hear what I said?"
    LADY_TARBECK @angry "I have no interest in these games!"
    MC @talk "Be it so, my lady, your husband won't be pleased should we do nothing."
    MC @smile "So what is the harm in letting me walk with you?"
    MC @talk "It's not like Hamun isn't a dangerous place..."
    MC @smile "Is it truly so terrible to have the savior of Novaras as your guard for the day?"
    LADY_TARBECK "Funny... I hear people still call you the beast of Novaras."
    LADY_TARBECK "So which is it? Are you a noble man, or just a beast?"
    menu:
        "Whatever I'm paid to be.":
            LADY_TARBECK @sad "How... Unreassuring."
        "A noble man... Who sometimes plays the part of a beast.":
            LADY_TARBECK @angry "Many a man has said something similar to justify the terrible things he's done."
        "A beast... Who sometimes plays the part of a noble man.":
            LADY_TARBECK @think "And you're content with that?"
            LADY_TARBECK @sad "How... Sad."
    MC @talk "Well... What will it be, my lady?"
    "Lady Tarbeck paused for a long moment before sighing."
    LADY_TARBECK @talk "Fine..."
    LADY_TARBECK @angry "But you ask nothing of me and expect nothing for this."
    LADY_TARBECK @angry "I do this only to appease my husband so he might relent."
    LADY_TARBECK @talk "And hopefully this foolishness of his can end and we can all go back to being just miserable again."
    MC @talk "... Did you have anywhere you wished to go today, my lady?"
    LADY_TARBECK @talk "Hmph."
    LADY_TARBECK @angry "No talking. Just follow."
    hide lady_tarbeck with easeoutleft
    "As Lady Tarbeck stormed her way past me, I shadowed behind her..."
    show mc at blurin, cleft_f
    MC "(This needs to work, you know.)"
    SHYAHTAN "(It will.)"
    hide mc with easeoutleft
    scene black with dissolve
    $ QstSetProgress(QstTheTarbecks2, 1)
    #Scene 3 - This section is on rails as the player follows Lady Tarbeck around different locations. The first location = the markets
    $ TimeAdvBy(TIME_1H)
    "... Following Lady Tarbeck's lead, I watched as she turned down towards the city markets."
    $ LocSet("hamun_market")
    "Behind us, always shadowing in the distance, at least three to four guards."
    "And those were just the ones I could see."
    $ LocFlush()
    show lady_tarbeck at center
    show mc at cleft
    with dissolve
    "Carefully I watched as Lady Tarbeck explored around the different market stalls."
    MC @think "I must admit, my lady, this doesn't quite seem like the place for a lady of your station."
    LADY_TARBECK @talk "I'm a merchant lord's wife, I'd be laughed out of true noble circles, make no mistake."
    MC @talk "But here-"
    show lady_tarbeck at blurin, center_f
    LADY_TARBECK @angry "Your job isn't to speak."
    show lady_tarbeck at blurin, center
    LADY_TARBECK @talk "It's to follow and protect me... silently."
    show lady_tarbeck at cright with ease
    "I pulled back, allowing Lady Tarbeck to inspect some jewelled trinkets which she bartered softly over."
    "Handing over a pouch of coins for a small, almost gimmicky wrist piece, she smiled at it before turning her soft gaze towards me and sighing."
    show lady_tarbeck at blurin, cright_f
    LADY_TARBECK @think "I am done here, come."
    show lady_tarbeck at blurin, cright
    hide lady_tarbeck with easeoutright
    "As the lady wandered off in another direction, I couldn't help but roll my eyes."
    show mc at center with ease
    MC "(Am I even going to {i}want{/i} to fuck her at the end of this?)"
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    $ LocSet("hamun_library")
    "The next hour was spent within the libraries of Hamun, as Lady Tarbeck traced her fingers along the books."
    "Occasionally, she would pull one out to read a few pages before carefully putting it back."
    $ LocFlush()
    show lady_tarbeck at cright_f
    show mc at cleft
    with dissolve
    MC @think "... Do you come here to read often, my lady?"
    LADY_TARBECK @think "I thought we were walking in silence?"
    MC @talk "Well first you might actually want to find a book you like before we drag out the silence."
    LADY_TARBECK @angry "And you're going to recommend me my next read?"
    "She folded her arms, her brow creasing."
    LADY_TARBECK @angry "As you refuse to shut up, let's hear it then."
    menu:
        "{i}The dance of the Vampyre Asmaldicus.{/i}":
            LADY_TARBECK @angry "Macabre."
            LADY_TARBECK @think "Something for teenage girls to swoon over."
            LADY_TARBECK @think "No respectable woman would be interested in such a beast."
        "{i}Seven knights and the moon princess.{/i}":
            LADY_TARBECK @think "Boring."
            MC @surprised "It's a classic!"
            LADY_TARBECK @think "Yes, and it was all the rage... Ten years ago."
            LADY_TARBECK @think "I and every other woman who can afford to have already read it."
        "{i}Busty tavern wenches and other sordid tales, Vol. Six.{/i}":
            LADY_TARBECK @sad "Crass... Very, very crass."
            LADY_TARBECK @sad "Besides, my husband is already on volume eight."

    #Any choice continued
    "Rubbing her brow, once more Lady Tarbeck let out another sigh."
    LADY_TARBECK @sad "This isn't going to work."
    show lady_tarbeck at center_f with ease
    LADY_TARBECK @sad "Look, we should just-"
    show cg_guard_hamun at left with easeinleft
    GUARD "My lady, I am sorry to disturb you."
    LADY_TARBECK @think "What is it?"
    GUARD "Lady Belamore and her friends wished to know if you would still be attending for tea today."
    "The blood drained from her face as she answered sheepishly."
    LADY_TARBECK @scared "Y-Yes... Send word I will be there right away."
    show cg_guard_hamun at nod
    show cg_guard_hamun at blurin, left_f
    hide cg_guard_hamun with easeoutleft
    "The guard thumped at his chest before bowing and leaving to relay the message."
    MC @think "Trouble?"
    show lady_tarbeck at cright_f with ease
    LADY_TARBECK @angry "Yes, but not the kind {i}you{/i} can help with."
    MC @talk "Well, perhaps I could try-"
    LADY_TARBECK @angry "I don't need another idiot with a sword to-"
    "Lady Tarbeck paused, her eyes looking me up and down."
    LADY_TARBECK @shock "... Actually, maybe..."
    MC @think "My lady?"
    LADY_TARBECK @talk "Just keep quiet, don't speak unless spoken to."
    LADY_TARBECK @talk "If the old gods and the new favor us, this might just work..."
    hide lady_tarbeck with easeoutleft
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show cg_guard_hamun at left
    with dissolve
    show lady_tarbeck at cright_f with easeinright
    show mc at right_f with easeinright
    GUARD "Halt!"
    "The guard bowed his head."
    GUARD "Lady Tarbeck."
    "He motioned towards me."
    GUARD "He has not been granted the right of entry."
    LADY_TARBECK @talk "He has been assigned as my protection by my husband."
    GUARD "Lord Tarbeck knows the rules, my lady."
    "Lady Tarbeck offered a faint smile."
    LADY_TARBECK @talk "But he is not just a guard."
    LADY_TARBECK @talk "You are looking at the beast of Novaras himself."
    MC @talk "Saviour."
    show lady_tarbeck at shake
    "I felt a sharp foot kick me."
    MC @surprised "Ow!"
    LADY_TARBECK @happy "Surely you won't deny me the chance to introduce him to Lady Belamore?"
    show lady_tarbeck at cleft_f with ease
    show lady_tarbeck at nod
    "The guard sighed, as ever so subtly, Lady Tarbeck palmed over a small pouch of coins into his hand."
    show lady_tarbeck at center_f with ease
    LADY_TARBECK @happy "{i}Please?{/i}"
    GUARD "{i}Sigh{/i}"
    GUARD "Very well, but any trouble and I will-"
    LADY_TARBECK @talk "He'll be the model of perfect behaviour."
    "Lady Tarbeck snapped her neck towards me, forcing a strained smile."
    LADY_TARBECK @happy "{i}Won't you?{/i}"
    MC @talk "Yes... Of course, my lady."
    "Lady Tarbeck turned her gaze back towards the guard, who stepped aside."
    GUARD "... Lady Belamore is expecting you in the tea room."
    LADY_TARBECK @happy "Thank you."
    hide lady_tarbeck
    hide mc
    with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_castle_entrance")
    $ LocFlush()
    show lady_tarbeck at cright_f
    with dissolve
    show mc at right_f with easeinright
    "Upon entering the great hall,"
    "I was taken aback by the sheer grandeur and ornateness of the castle."
    "Wandering its gilded halls, powerful merchant lords, cliques of their wives and other power-hungry social climbers."
    MC @think "This isn't quite what I was expecting."
    LADY_TARBECK @talk "Never mind that, stay focused."
    LADY_TARBECK @talk "Now, when we meet Lady Belamore, smile and say nothing."
    LADY_TARBECK @talk "You are to be like an empty, beautiful statue."
    LADY_TARBECK @talk "Are we clear? They are interested in the novelty of you, {i}not{/i} you."
    "Opening my mouth to say something, no words had escaped my lips before she was suddenly dragging me off down one of the corridors."
    hide lady_tarbeck
    hide mc
    with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_castle_tea_room")
    $ LocFlush()
    show lady_narisha at left
    show lady_belamore at center
    show lady_bargore at cleft
    with dissolve
    show lady_tarbeck at cright_f with easeinright
    show mc at right_f with easeinright
    "Three women sat carefully around a table, each one dressed more ornately than the other."
    "Lady Tarbeck looked woefully their opposite, reserved and withdrawn with shyness, she seemed much... smaller in their presence."
    "The leader of the trio, and the most beautiful of them, after sipping her tea, gently placed her cup down onto the table before standing."
    "The other two followed, as the central figure smiled at Lady Tarbeck... but it was a smile lacking any warmth."
    LADY_BELAMORE @smile "Lady Tarbeck."
    LADY_TARBECK @talk "Lady Belamore."
    LADY_BELAMORE @smile "Come, sit with us."
    "The woman's eyes shifted towards me, the way a cat might look at a mouse that just walked into the room."
    LADY_BELAMORE @talk "And this is?"
    LADY_TARBECK @talk "M-My guard, my husband-"
    LADY_BELAMORE @smile "Your husband, how is he by the way?"
    LADY_TARBECK @sad "He... He is well."
    LADY_BELAMORE @smile "Really?"
    LADY_BELAMORE @talk "I heard he tried to seduce the young Lady Marcilla to attend one of his sordid little parties."
    "The two women snickered and laughed behind her."
    LADY_TARBECK @sad "A... A malicious rumor, I'm sure."
    LADY_BELAMORE @smile "Oh?"
    LADY_BELAMORE @smile "So you're saying Lady Marcilla is a liar then?"
    LADY_BELAMORE @smile "How shameful, a girl barely come of age and lying already."
    LADY_BELAMORE @talk "Let's speak to her directly and-"
    LADY_TARBECK @shock "T-THAT WON'T BE NECESSARY!"
    LADY_TARBECK @blush2 "I umm, I'm sure she just got confused is all."
    LADY_TARBECK @blush2 "She has little experience in matters such as these."
    LADY_NARISHA @smile "Sounds to us like your husband planned on providing her all the 'experience' she would need."
    LADY_BARGORE @smile "Oh really, how can you stomach the indignity of that creature you married?"
    "The two women laughed, stopping abruptly only when Lady Belamore snapped a deathly glare towards the two of them."
    LADY_BELAMORE @smile "You must forgive my ladies."
    LADY_BELAMORE @talk "They sometimes forget their place."
    "The two women said nothing, their eyes refusing to lift from the floor."
    LADY_TARBECK @sad "I... I can see you ladies are busy, perhaps I should leave and-"
    LADY_BELAMORE @smile "Nonsense, stay."
    LADY_BELAMORE @smile "We have so much to discuss!"
    "Reluctantly, Lady Tarbeck sat at the table."
    "Like watching a sheep surrounded by circling wolves, any feelings of irritation I had towards Lady Tarbeck were gone."
    "Now, it took every inch of restraint to stop myself from acting."
    LADY_BELAMORE @smile "So, did you think on what I said before?"
    LADY_TARBECK @blush2 "I... No, my lady, I'm not interested in that."
    LADY_BELAMORE @think "Why not?"
    LADY_BELAMORE @smile "He might not be a lord, but Faraka is a respectable, {i}handsome{/i} merchant."
    LADY_BELAMORE @smile "Did you not receive his poetry?"
    LADY_TARBECK @blush2 "I did, but..."
    LADY_TARBECK @blush2 "I did not reply."
    LADY_BELAMORE @smile "Oh... I see."
    LADY_BELAMORE @smile "So you're far too good and noble to find yourself a lover."
    LADY_BELAMORE @smile "Unlike us... Right?"
    LADY_TARBECK @shock "N-No! That's not what I meant at all!"
    LADY_NARISHA @angry "You think you're better than us!"
    LADY_BARGORE @angry "Always {i}So{/i} high and mighty till you come begging for the one thing coin can't buy."
    LADY_BARGORE @smile "{i}Dignity.{/i}"
    "The women snickered once again, like tormenting little imps, but this time, Lady Belamore did not rein them in."
    "Lady Tarbeck's eyes looked to the floor, taking the abuse until her eyes lifted just enough to see my hand on her shoulder."
    MC @serious "And is this dignified?"
    MC @serious "Endless jibes over a husband who dishonors her?"
    "The tea room fell silent, all conversation in the room now ceased."
    "A servant had spoken without permission."
    "A servant had just touched a lady of higher station without permission."
    "A servant had just dared to refuse to accept his place."
    "Lady Tarbeck's face turned pale white as she realized what was happening."
    LADY_BELAMORE @shock "... Did your guard just-"
    LADY_TARBECK @shock "Wait! He's not-"
    LADY_BELAMORE @angry "Really now?"
    LADY_BELAMORE @angry "You can't even control your own guard?"
    LADY_TARBECK @shock "He's..."
    MC @talk "The beast of Novaras."
    "Silence."
    "A long pause followed as the eyes looked around the room."
    "Lady Tarbeck seemed to sink deeper and deeper into her seat as the room became so quiet you could hear a pin drop."
    LADY_BELAMORE @talk "{i}... You're he?{/i}"
    "One of the women shifted uncomfortably."
    LADY_NARISHA @shock "Y-You saved my brother."
    LADY_NARISHA @talk "He was there, at the arena that day."
    "Lady Tarbeck seemed ready to explode, her breathing rapid and short as her heart raced."
    MC @talk "... If you will excuse me."
    "Reaching down, I scooped up Lady Tarbeck into my arms."
    LADY_TARBECK "Eeeeep!"
    MC @talk "I will take my leave and-"
    LADY_BELAMORE @smile "No, no...!"
    LADY_BELAMORE @smile "Stay. Please."
    "I looked around for a few moments before carefully placing Lady Tarbeck back onto her feet."
    LADY_BELAMORE @smile "Why Lady Tarbeck, you should have told us you were bringing us such a... unique companion this evening!"
    LADY_TARBECK @blush2 "I... I was trying to tell-"
    LADY_BELAMORE @smile "Sit, both of you."
    "For the next hour or so, the women asked me question after question."
    "The women asked about everything, regardless of how intrusive."
    "The war, tales of adventures, subtle inquiries into paramours and romances."
    "The more I spoke, the more they listened."
    LADY_NARISHA @smile "What's the bravest thing you've ever done?"
    MC @smile "I... never really ranked them."
    LADY_NARISHA @sad "Does it get lonely being an adventurer?"
    MC @think "Well, sometimes, but... I have people I can count on."
    "Even other tea tables across the way would stop, turning their heads to listen occasionally as I spoke."
    "The more I spoke, the more Lady Belamore seemed to inch herself closer to me..."
    "Her arm wrapping around mine as Lady Tarbeck watched carefully from the sides."
    LADY_BELAMORE @sad "Such a hard life..."
    LADY_BELAMORE @think "Did you truly fight THE Zanarak?"
    MC "(Survived more like.)"
    MC @talk "Yes, we fought."
    "The women all gasped."
    LADY_BARGORE "So he {i}is{/i} real?"
    LADY_NARISHA @sad "Were you afraid fighting Zanarak?"
    MC @sad "It's hard to not be a little afraid, my lady."
    MC @serious "But I wouldn't let fear stop me from trying."
    "Lady Narisha smiled warmly and fluttered her eyes."
    LADY_BARGORE "Do you think you could defeat the silver knight?"
    MC @think "Well, I-"
    LADY_BELAMORE @smile "Ladies, ladies... Please."
    LADY_BELAMORE @talk "I'm sure we've worn him out with all this talk."
    "Her hands slowly trailed up my arm as she pushed her chest against me."
    LADY_BELAMORE @smile "Perhaps you might be willing to join us this evening for-"
    LADY_TARBECK @happy "I'm afraid I'll be in need of him."
    "The woman turned towards Lady Tarbeck, the cute expression dropping as she glared coldly towards her."
    LADY_BELAMORE @talk "{i}What?{/i}"
    LADY_TARBECK @happy "He has to assist me and my husband with some other duties."
    LADY_TARBECK @happy "But..."
    LADY_TARBECK @talk "{i}Perhaps I could bring him with me to our next meeting?{/i}"
    "Lady Belamore's cold expression watched Lady Tarbeck for a few moments, reading every slight twitch or movement."
    "Then, once again she smiled warmly."
    LADY_BELAMORE @smile "What a wonderful idea."
    LADY_BELAMORE @smile "Yes, bring him next time."
    "Lady Tarbeck motioned for me to follow, and rising from my seat, I offered a curt bow before leaving."
    "As I did so, I could hear the chatter of the women behind me, quiet and distant enough no normal person could hear."
    LADY_NARISHA "Was he chiseled by the gods or something?"
    LADY_BARGORE "Why does he have to be cursed into serving that bore instead of one of us?"
    LADY_NARISHA "Do we really have to be nice to that bitch now just if we want to see him?"
    LADY_BELAMORE "Fear not, ladies."
    "Listening carefully, I heard the slightest sound of her tongue licking her lips."
    LADY_BELAMORE "We'll soon get to play with our new toy, then once we're done with him, we won't have to treat Lady Tarbeck like an equal anymore."
    MC "(We'll see about that...)"
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show lady_tarbeck at cright_f
    show mc at cleft
    with dissolve
    LADY_TARBECK @talk "Return to the manor this evening."
    LADY_TARBECK @talk "We have... Much to discuss."
    show lady_tarbeck at blurin, cright
    hide lady_tarbeck with easeoutright
    $ QstSetProgress(QstTheTarbecks2, 2)
    show mc at center with ease
    $ Pause(0.5)
    $ LocEnter()

# Upon entering the manor the scene begins immediately
label qst_TheTarbecks2_return_to_manor:
    scene black with dissolve
    $ QstSetProgress(HouseLockTarbeckHouse, 2)
    $ LocSet("hamun_tarbeck_mainhall")
    $ LocFlush()
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_TARBECK @talk "Ah, you made it. Good."
    MC @talk "So, you want my help, I take it."
    LADY_TARBECK @talk "Yes."
    LADY_TARBECK @think "But I'm still not willing to betray my husband."
    "She paused sheepishly, grabbing at her skirt as she looked to the floor, cheeks red."
    LADY_TARBECK @sad "His conduct is shameful, but I am still his wife."
    MC @think "Then what do you offer me, my lady?"
    LADY_TARBECK @talk "I will give you what you want."
    LADY_TARBECK @sad "I will... at least play the role my husband wants to convince him long enough to agree."
    MC @think "Why does this matter so much to you, my lady?"
    LADY_TARBECK @talk "Because he is my husband."
    LADY_TARBECK @sad "As much as I hate what he's become, it's my duty as his wife to help him."
    LADY_TARBECK @angry "I despise those wretches, Lady Belamore and her little minions."
    LADY_TARBECK @sad "... But I can't deny their wealth and power."
    LADY_TARBECK @sad "Lady Belamore's husband owns at least a quarter of all of Alderay's fishing exports."
    LADY_TARBECK @talk "With their support, my husband could elevate his status to a higher lord."
    LADY_TARBECK @talk "Do we have a deal?"
    menu qst_TheTarbecks2_return_to_manor_menu:
        "Yes... If you agree to spend more time with me outside of these tea parties.":
            "Lady Tarbeck seemed taken aback at the request."
            LADY_TARBECK @think "You know I'm not offering you sex, yes?"
            MC @talk "I know."
            LADY_TARBECK @sad "And... You still want to spend time with me even after how horrible I was to you before?"
            MC @smile "I do."
            LADY_TARBECK @shock "You are... a strange man."
            MC @smile "I am."
            LADY_TARBECK @talk "...{i}Sigh{/i}"
            LADY_TARBECK @talk "I agree to your terms."
            "I offered another curt bow."
            MC @smile "Then in that case, tomorrow I would like to take you for a walk around the city, my lady."
            LADY_TARBECK @think "And where will you be taking me?"
            MC @smile "A surprise, my lady."
            "Lady Tarbeck's eyes looked me up and down uncertainly."
            LADY_TARBECK @blush2 "...Very well."
            LADY_TARBECK @talk "Call upon me tomorrow."
            $ QstSetProgress(QstTheTarbecks2, 3)
        "I was hoping I might get a little more from you." (AppearIf = (QstTheTarbecks2().Stage2OfferLittleMorePicked == False)):
            $ QstTheTarbecks2().Stage2OfferLittleMorePicked = True
            LADY_TARBECK @blush2 "I... I'm sorry."
            LADY_TARBECK @blush2 "I'm just not that kind of woman."
            LADY_TARBECK @blush "If I wasn't already married..."
            "She let the sentence trail off, shaking her head."
            LADY_TARBECK @sad "N-Never mind, forget I said anything."
            jump qst_TheTarbecks2_return_to_manor_menu
        "I need time to think on it, my lady.":
            $ QstTheTarbecks2().Stage2OfferRepeat = True
            LADY_TARBECK @talk "I doubt there is much to think on. You need my support to get my husband's help."
            LADY_TARBECK @talk "But I will allow you to consider this proposal as long as you want."
    $ LocEnter()

label qst_TheTarbecks2_offer_repeat:
    show lady_tarbeck at center with dissolve
    LADY_TARBECK "Well, have you had any more thought on my offer?"
    jump qst_TheTarbecks2_return_to_manor_menu

#######################################################################
label qst_TheTarbecks2_prep_to_tour:
    show lady_tarbeck at center with dissolve
    LADY_TARBECK @talk "Well then, I suppose you have a plan for where you want to take me?"
    menu:
        "I know just the place.":
            LADY_TARBECK @talk "Then I'm in your hands..."
            pass
        "Not yet.":
            LADY_TARBECK @talk "Don't waste my time please..."
            $ LocEnter()

    #Fade to black - cut to the docks
    scene black with dissolve
    $ LocSet("hamun_port")
    $ LocFlush()
    with dissolve

    "... The cool breeze in the desert heat brought some relief,"
    "As the mist from the water gently kissed my cheeks."
    show lady_tarbeck at cright_f
    show mc at cleft
    with dissolve
    "Lady Tarbeck smiled as she watched the ships leave the docks."
    LADY_TARBECK @happy "Now this is unexpected."
    LADY_TARBECK @think "But why here?"
    MC @smile "I thought you might enjoy the views."
    MC @talk "But we can move on if you wish."
    "Lady Tarbeck gazed out across the water, watching one of the ships sail on by."
    LADY_TARBECK @talk "... There's something pleasant about watching ships sail on by, isn't there?"
    LADY_TARBECK @talk "It's like they're a constant reminder you could always hop on one to escape your troubles."
    MC @think "Is that what you want, my lady?"
    MC @think "{i}To escape?{/i}"
    "Lady Tarbeck's expression softened as she continued to watch the waves."
    LADY_TARBECK @sad "When we first started, we had nothing."
    LADY_TARBECK @sad "That's the painful truth most merchant lords like to forget."
    LADY_TARBECK @sad "We crawled our way through the dirt, half-starved, risking death at every turn."
    LADY_TARBECK @talk "Can you guess what I was before all this?"
    menu:
        "A thief.":
            LADY_TARBECK @happy "Correct."
            pass
        "A whore.":
            LADY_TARBECK @blush2 "Not... quite."
            LADY_TARBECK @blush "Though there was a time I thought I might end up that way."
            pass
        "An assassin.":
            "Lady Tarbeck laughed."
            LADY_TARBECK @happy "Gods, no."
            pass
    LADY_TARBECK @talk "When I was a little girl, I was a pickpocket."
    LADY_TARBECK @talk "One of my brothers would usually distract them as I cleared out their pockets."
    LADY_TARBECK @talk "Father was a drunk who didn't work and used to beat us."
    LADY_TARBECK @talk "Mother earned her coins working in taverns."
    LADY_TARBECK @sad "... Long hours, and often we saw her in the company of strange men."
    MC @think "How did you meet your husband?"
    LADY_TARBECK @happy "He caught me."
    MC @surprised "Quite the meeting!"
    LADY_TARBECK @happy "I thought he was going to kill me."
    LADY_TARBECK @happy "Instead... he gave me a job."
    "She let out a soft laugh."
    MC @think "A job?"
    LADY_TARBECK @talk "He peddled stolen goods on the street, anything he could get his hands on."
    LADY_TARBECK @talk "Fish, cloth, whatever."
    LADY_TARBECK @talk "While he put on a show, I would clean out the crowd as best as I could."
    LADY_TARBECK @happy "Hard to imagine me like that, isn't it?"
    MC @smile "I'll say."
    MC @think "How did you both end up the way you are now?"
    LADY_TARBECK @talk "Time, planning, endless deals..."
    LADY_TARBECK @talk "We were both such different people back then, now..."
    "She paused, her eyes falling heavy as she seemed to think back on distant memories before smiling."
    LADY_TARBECK @happy "It doesn't matter now."
    LADY_TARBECK @talk "This has been pleasant, but I will call upon you in a few days to join me for another tea party."
    MC @think "So, back to your estate?"
    LADY_TARBECK @happy "Yes."
    LADY_TARBECK @talk "... Oh, by the way."
    "Lady Tarbeck tossed a potion towards me." 
    show mc at nod
    #Not an item
    LADY_TARBECK @happy "You really should keep a closer eye on what you're carrying, you know."
    MC @think "How did you-"
    "Lady Tarbeck laughed once more."
    LADY_TARBECK @happy "Come, take me home."
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ QstSetProgress(QstTheTarbecks2, 4)
    $ QstSetDelay(QstTheTarbecks2, 2)
    $ LocEnter()

label qst_TheTarbecks2_tea_invite:
    #SCENE 6 
    #Two days later in-game while wandering around the city
    show mc at cleft with easeinleft
    show cg_guard_hamun at cright_f with easeinright
    GUARD "Lady Tarbeck requests your presence."
    GUARD "Please join her for another tea party with Lady Belamore."
    show cg_guard_hamun at blurin, cright
    hide cg_guard_hamun with easeoutright
    $ Pause(0.5)
    show mc at center with ease
    $ QstStart(HouseLockHamunCastle)
    $ QstSetProgress(QstTheTarbecks2, 5)
    MC "(Here we go again...)"
    $ LocEnter()

############################################################################################################################################################################################################
# SCENE 7
# Lady Tarbeck is waiting for the player in the grand hall of the castle/fort in Hamun
label qst_TheTarbecks2_tea_party2:
    show lady_tarbeck at center with dissolve
    LADY_TARBECK @talk "Ah, Lady Belamore and the others should be here shortly."
    LADY_TARBECK @talk "Are you ready?"
    menu:
        "Yes.":
            LADY_TARBECK @talk "Come then, follow me."
            pass
        "Not yet, my lady.":
            LADY_TARBECK @talk "{i}Sigh{/i}"
            LADY_TARBECK @talk "I can stall for a while, but let's not waste time, yes?"
            $ LocEnter()

    scene black with dissolve
    $ LocSet("hamun_castle_tea_room")
    $ TimeAdvBy(TIME_05H)
    "... The tea party went about as well as you would expect."
    $ LocFlush()
    show lady_narisha at center
    show lady_belamore at left
    show lady_bargore at cleft
    show mc at right_f
    show lady_tarbeck at cright_f
    with dissolve
    "The women lightly pecked and prodded at Lady Tarbeck, but were far more restrained than before."
    "Instead, their attention seemed focused more on me."
    LADY_BELAMORE @smile "You know, Lady Tarbeck."
    LADY_BELAMORE @smile "We would just {i}love{/i} to have a more private audience with your friend here!"
    LADY_BELAMORE @smile "Somewhere he would enthrall us with his tales further."
    "The other two women giggled and laughed between themselves, quietly whispering to one another."
    LADY_NARISHA "{i}Let us hope that is not all he will be enthralling us with.{/i}"
    "Lady Tarbeck smiled softly, sipping at her tea."
    LADY_TARBECK @happy "It could be arranged, my ladies..."
    "The trio looked at each other with assured, smug smiles."
    LADY_TARBECK @happy "But as you know, it could be quite the scandal for you to attend my home given my husband's eccentric reputation."
    "A small crack appeared on Lady Belamore's face, her words now carefully crafted."
    LADY_BELAMORE @talk "I see... Perhaps you could arrange for somewhere else other than your estate, then?"
    LADY_TARBECK @talk "I'm afraid my husband is very protective of me, especially in these troubling times."
    LADY_TARBECK @talk "He insists I see my friends in only places he deems safe and reputable."
    "You could see the growing frustration."
    LADY_BARGORE @talk "... And you think your estate is either of those things?"
    "Lady Belamore glared towards Lady Bargore, who retreated as quickly as she spoke up."
    LADY_TARBECK @sad "... Well, if none of you feel comfortable, I suppose we can abandon the whole-"
    LADY_BELAMORE @talk "What do you propose?"
    LADY_TARBECK @think "Hm?"
    LADY_BELAMORE @talk "To avoid a scandal, I suppose you have a proposal for us?"
    "Lady Tarbeck clapped her hands together."
    LADY_TARBECK @happy "Well, I {i}suppose{/i} if you were to come on business to my estate."
    LADY_TARBECK @happy "Perhaps to discuss my husband being allowed into the upper halls to conduct business there."
    "The women's eyes flickered between one another for a moment, as Lady Belamore smiled coyly once more."
    LADY_BELAMORE @smile "That is... An interesting proposal."
    LADY_BELAMORE @smile "Very well, we shall attend."
    LADY_NARISHA @shock "L-Lady Belamore! Surely you can't mean to-"
    LADY_BELAMORE @angry "{i}Quiet.{/i}"
    LADY_NARISHA @sad "..."
    LADY_BELAMORE @smile "Let us make the proper arrangements."
    LADY_TARBECK @happy "Let's."
    "Lady Belamore turned her gaze towards me."
    LADY_BELAMORE @smile "We hope you prepare something special for us after all the trouble we're going through."
    MC @smile "Don't worry, my lady."
    MC @smile "{i}I'm sure I can make it an unforgettable experience for you all.{/i}"
    "Lady Belamore smiled approvingly as the rest of our time together slowly wound down until at last, Lady Tarbeck announced the two of us would be departing."
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    MC @think "... Well, what do you-"
    "Lady Tarbeck suddenly flung herself into my arms, hugging me tightly as she giggled ecstatically."
    MC @laugh "My lady?"
    LADY_TARBECK @happy "It's going perfectly! I can't believe it!"
    LADY_TARBECK @talk "Finally, it won't be long now till I'm free of having to grovel and deal with them!"
    MC @smile "That's good, my lady."
    LADY_TARBECK @blush "... Well, then I suppose now you want me to live up to my end of the bargain."
    LADY_TARBECK @think "... Would you mind though if we went to the library?"
    MC @think "Again?"
    LADY_TARBECK @talk "It's... peaceful there."
    menu:
        "Of course, my lady.":
            pass
        "Well, if we're bartering..." (Req_Barter = 13):
            LADY_TARBECK @think "Tread carefully."
            menu:
                "A kiss on the cheek.":
                    LADY_TARBECK @blush2 "... W-Well, I suppose it's still within acceptable social bounds."
                    # kiss art to be added for full update release AFTER beta - Just move closer for now.
                    "Lady Tarbeck leaned forward, gently touching my left cheek with her lips."
                    LADY_TARBECK @blush "T-There."
                    pass
                "A kiss... A real one." (Req_Charm = 15):
                    LADY_TARBECK @blush "I said no..."
                    MC @smile "That's not bartering."
                    LADY_TARBECK @blush "... Why do you even want that? I've already said I will help you if you give me what I want."
                    MC @smile "Because I still like you."
                    "Lady Tarbeck froze at the words, pondering them for a moment."
                    LADY_TARBECK @blush "... One kiss, one."
                    LADY_TARBECK @blush "And no tongues!"
                    MC @smile "As you wish, my lady."
                    # kiss art to be added for full update release AFTER Beta - just move closer for now.
                    "Lady Tarbeck moved sheepishly closer, pressing her body and chest against me, her cheeks burning red as she leaned in."
                    "She closed her eyes nervously, and as I pressed my lips against hers, she moaned softly."
                    LADY_TARBECK "Mmm..."
                    "The soft moan escaped her lips as I embraced her, and slowly, after a few moments, I felt her hands move onto my chest to lightly push me away."
                    LADY_TARBECK @blush2 "T-That was..."
                    LADY_TARBECK @blush "S-Shameful."
                    pass
                "Show me what's beneath your clothes." (Req_Charm = 22):
                    LADY_TARBECK @shock "A-Are you mad?!"
                    LADY_TARBECK @angry "I told you neither of us would be having {i}that{/i} kind of relationship!"
                    LADY_TARBECK @angry "I'm a married woman!"
                    MC @smile "I didn't say I'd touch you."
                    MC @smile "I only asked if I could see what I was missing."
                    LADY_TARBECK @angry "This is very ungentlemanly of you!"
                    MC @smile "Just living up to the beast part of my title."
                    LADY_TARBECK @angry "Grhhh...!"
                    LADY_TARBECK @blush "... F-Fine, but..."
                    LADY_TARBECK @blush "I decide what you see!"
                    LADY_TARBECK @angry "And absolutely no touching or our deal is off!"
                    MC @talk "As you wish."
                    # Art ordered - should arrive in a few hours, otherwise, do nothing with the scene - we'll just say the art will be there for the finished release after the beta.
                    "She took a deep breath for a moment, looking around sheepishly."
                    "Nervously, Lady Tarbeck tugged down her dress to expose part of her breasts before quickly retreating."
                    LADY_TARBECK @blush2 "T-There... Satisfied?"
                    MC @smile "Very."
                    pass

    LADY_TARBECK @talk "Now, let's go already."
    scene black with dissolve
    $ LocSet("hamun_library")
    $ TimeAdvBy(TIME_05H)
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at cright_f
    with dissolve
    "Lady Tarbeck once again carefully traced her fingers along the many books on the library shelves."
    "Pulling one out, she'd read a few pages before carefully putting it back into place."
    "Slowly though, she would find one or two books that interested her after another, and a small pile began to grow."
    LADY_TARBECK @talk "... May I ask you some questions?"
    MC @think "About?"
    LADY_TARBECK @talk "Well, I don't often get to speak to adventurers."
    LADY_TARBECK @talk "Tell me more about yourself."
    menu:
        "Tell her about growing up in Novaras.":
            MC @think "I grew up like most children, I suppose."
            MC @talk "Perhaps slightly luckier, given my father became an officer in the army."
            LADY_TARBECK @think "What kind of studies do they teach you in Novaras?"
            MC @talk "Well, after basic math, religious studies and some classic literature deemed essential, students are usually branched out into different subjects."
            MC @talk "This usually happens at around thirteen."
            MC @think "Then those with some magecraft go into pre-mage studies, but people like me tend to end up in what's called exercise enhancement training."
            MC @talk "A few of the most promising go onto logistics, administration studies, whatever."
            MC @talk "Whilst others, like this girl I knew, Arlena, began 'pre-vocational training' because her father was already a blacksmith."
            LADY_TARBECK @think "So you were always set to be a soldier, whether you wanted to be or not?"
            MC @talk "Not quite."
            MC @talk "Me and Markus worked ourselves to the bone taking what's called the Valstead tests."
            MC @talk "The Valstead test is the one chance people get to prove they can be more than what they've already got planned for them. Anyone can take it, but it's one of the most difficult tests around."
            LADY_TARBECK @think "And you passed?"
            MC @smile "My friend Markus and I passed it just enough that we were considered for a more administration-based role."
            MC @talk "We thought we might end up working within the inner castle keep itself..."
            LADY_TARBECK @think "So, what happened?"
            MC @talk "That is... A question I would like the answer to myself one day."
            pass
        "Tell her about early romances.":
            MC @think "Wellll... things are different now, but..."
            MC @talk "There was a woman in my life back then."
            LADY_TARBECK @think "Oh?"
            LADY_TARBECK @happy "Is this a sordid tale, or a romance for the ages?"
            MC @smile "A bit of both perhaps."
            MC @talk "Her name was Elia."
            MC @talk "She and I were like fire and ice."
            MC @talk "We disagreed on almost everything but couldn't keep our hands off each other."
            LADY_TARBECK @talk "What happened?"
            MC @talk "A lot, I suppose..."
            MC @embarr "I had this friend, her name was Adara."
            MC @talk "She and I were always very close, practically grew up together."
            MC @sad "Elia couldn't stand it, she was convinced there was something going on between us."
            LADY_TARBECK @think "And was there?"
            menu:
                "Perhaps...":
                    MC @embarr "We didn't... go far."
                    MC @embarr "But well, there were one or two drunken kisses perhaps."
                    MC @embarr "And touching that should not have been."
                    LADY_TARBECK @happy "Tsk, tsk, tsk."
                    LADY_TARBECK @happy "Must have been quite scandalous at the time."
                    MC @smile "No one knew for sure what was between us, and I think that was the point."
                    pass
                "Nothing serious.":
                    MC @talk "Some flirting, perhaps."
                    MC @talk "But... Nothing that warranted betrayal."
                    LADY_TARBECK @talk "Clearly she didn't feel that way."
                    MC @sad "Yes... Clearly."
                    pass
            MC @talk "Regardless, Lord Murgo's son, Julian, wanted her."
            MC @talk "Seeing the rift between us, he swooped in."
            LADY_TARBECK @think "And you didn't fight for her?"
            MC @think "No... Not in the end."
            MC @talk "And she wanted coin and status that there was just no way I could give her."
            MC @talk "And that was that..."
            LADY_TARBECK @sad "Did you ever speak to her again?"
            "I paused for a moment, thinking back, remembering the {i}true{/i} last time I saw her."
            "Standing in the doorway, soaked through, her figure visible through the clothes she wore."
            "The night before she was-"
            MC @talk "No... I never saw her again."
            LADY_TARBECK @sad "... How sad."
            pass

    LADY_TARBECK @talk "I see... And if I may ask."
    LADY_TARBECK @think "This... {i}thing{/i} you change into."
    LADY_TARBECK @think "Is it fully you, or is it someone else?"

    menu:
        "It's me, I'm in control.":
            LADY_TARBECK @talk "Hmm, I see."
            LADY_TARBECK @think "But I heard that the creature called itself a name in the arena?"
            LADY_TARBECK @think "Shayzan or something?"
            MC @talk "Shyahtan."
            LADY_TARBECK @shock "That's it."
            MC @talk "The thing attached to me has... memories."
            LADY_TARBECK @think "Memories?"
            MC @talk "It's a living thing that speaks to me, but I control it, not the other way around."
            MC @talk "I'm still me."
            SHYAHTAN "(... Are you sure?)"
            LADY_TARBECK @think "It speaks to you?"
            LADY_TARBECK @sad "That must be... strange."
            pass
        "It has more control over me than I would like to admit.":
            LADY_TARBECK @shock "Really?"
            MC @talk "Our memories are interwoven. He can peer deep into my mind, but much of his past is a mystery he's forgotten."
            MC @talk "His powers come at a cost... I..."
            "I paused for a moment, debating whether it was worth revealing the next part about him potentially taking over my body."
            "No, she didn't need to know that part."
            MC @talk "Using his powers could kill me."
            LADY_TARBECK @shock "Then... Why use them at all?"
            MC @talk "Because without them I couldn't have got this far."
            MC @serious "Because so far these powers have kept me alive."
            LADY_TARBECK @sad "Perhaps for now..."
            LADY_TARBECK @sad "But will you ever be able to have a normal life?"
            LADY_TARBECK @sad "Power like yours, it's something people want to control."
            LADY_TARBECK @sad "You might survive, but will you ever truly be free?"
            MC @sad "..."
            pass
        "I'm not sure...":
            LADY_TARBECK @sad "I'm not sure if that answer gives me the most relief to hear..."
            LADY_TARBECK @sad "Or if it's the most dangerous thing you could have said."
            pass

    "Lady Tarbeck closed the book shut and pushed it back into the bookcase."
    LADY_TARBECK @talk "Come, escort me back to my manor."
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    with dissolve
    show lady_tarbeck at cleft
    show mc at left
    with easeinleft
    SHYAHTAN "(... Something is wrong.)"
    MC @think "(What?)"
    SHYAHTAN "(MOVE.)"
    show mc at cleft
    show lady_tarbeck at left
    with ease
    "Grabbing hold of Lady Tarbeck, she cried out as I suddenly pushed the two of us aside."
    "No sooner had I done so than a flung dagger barely missed us."
    show cg_assassin at right_f with dissolve
    "From the shadows, four masked men emerged with their blades drawn."
    KIDNAPPER "Hm... That's a shame."
    MC @angry "Stay behind me."
    LADY_TARBECK @scared "Who... Who sent you?!"
    LADY_TARBECK @scared "Where are my other guards?"
    KIDNAPPER "Sorry, no witnesses."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    MC @angry "LADY TARBECK! GET BACK!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_street", CharIDList_Right = [{"e_kidnapper":10}, {"e_kidnapper":12}, {"e_kidnapper":10}, {"e_kidnapper":12}]))
    scene black with dissolve
    "One crumpled into a pool of blood on the floor as I snapped my head towards Lady Tarbeck, struggling against one of them as he tried to drag her away."
    $ LocFlush()
    show lady_tarbeck at cright_f
    show cg_assassin at right_f
    show mc at left
    with dissolve
    LADY_TARBECK @shock "LET GO OF ME!"
    MC @surprised "LADY TARBECK!"
    #hide lady_tarbeck 
    #hide cg_assassin
    #hide mc
    #show cg_ladytarbeck_kill with dissolve
    scene black with dissolve
    "As she held out her hand defensively, her eyes began to glow a soft hue as a circle appeared around the man's waist."
    play sound "audio/cfx/magic_slice.ogg"
    "The strange enchantment circled him for a few seconds before closing around him, and suddenly the man was severed in half, his lower body dropping from the sky a few feet away from him."
    play sound2 "audio/cfx/crunch.ogg"
    scene cg_ladytarbeck_kill with flash
    play sound "audio/cfx/man_scream_terror.ogg"
    KIDNAPPER "GAHHHHHHHHHHHHHHH!"
    KIDNAPPER "MY LEGSSSS! MY FUCKING LEGSSSS!"
    $ LocFlush()
    $ AutoMus(True)
    show lady_tarbeck at cright
    show mc at cleft
    with dissolve
    LADY_TARBECK @shock "No, no, no, no!"
    LADY_TARBECK @shock "Not again!"
    MC @surprised "WHAT THE FUCK?"
    "The severed man continued to bleed out on the floor in agony as he flailed in horror and confusion."
    "Lady Tarbeck stood frozen, her eyes wide and unblinking, the blood drained completely from her face as she watched the man in his final moments,"
    "crawling his way over to his legs and reaching out for them, almost as if he was going to try to futilely pull himself back together."
    "He stopped, face in the sand as the blood continued to pool around his lifeless body."
    show mc at center with ease
    MC @serious "We need to go, now."
    show lady_tarbeck at blurin, cright_f
    LADY_TARBECK @scared "I... I..."
    MC @angry "NOW!"
    "I grabbed hold of her and shook her from her daze."
    show lady_tarbeck at shake
    MC @serious "LADY TARBECK!"
    LADY_TARBECK @scared "W-Wha...?"
    "Grabbing her wrist, I began to drag her away from the scene as quickly as I could."
    LADY_TARBECK "P-Please... Take me home."
    scene black with dissolve
    # Fade to black - cut back to Tarbeck manor.
    $ LocSet("hamun_tarbeck_mainhall")
    $ TimeAdvBy(TIME_05H)
    $ LocFlush()
    show lady_tarbeck at cright
    show mc at cleft
    with dissolve
    "Lady Tarbeck stumbled through the door, still dazed, as though she had seen a ghost."
    MC @angry "What was that?"
    MC @angry "WHAT THE FUCK WAS THAT?"
    show lady_tarbeck at blurin, cright_f
    LADY_TARBECK @shock "I... You cannot tell anyone, please!"
    show lord_tarbeck at right_f with easeinright
    TARBECK "What happened?!"
    "We both turned towards Lord Tarbeck, who came rushing down towards us."
    TARBECK @shock "My dear, are you alright?"
    TARBECK @shock "I heard some dogs attempted to kidnap you!"
    LADY_TARBECK @sad "I'm fine, dear..."
    LADY_TARBECK @sad "... I had someone to protect me."
    "Lord Tarbeck looked towards me approvingly and then back towards his wife."
    TARBECK @angry "It's the husband of one of those whores you waste your time courting with tea parties!"
    TARBECK @angry "That cunt Lady Belamore's husband! Or perhaps that worm Bargore!"
    LADY_TARBECK @shock "Please! Calm yourself!"
    TARBECK @angry "I'll have their fucking heads for daring to try and hurt you!"
    LADY_TARBECK @angry "NO!"
    TARBECK @shock "But...!"
    LADY_TARBECK @sad "I've worked too hard for this..."
    LADY_TARBECK @sad "You don't know that they're responsible, and it doesn't matter if it is."
    TARBECK @sad "But-"
    LADY_TARBECK @talk "I am {i}this{/i} close to getting those insufferable bitches to agree to my terms."
    LADY_TARBECK @sad "Once you become a higher lord, WE will be safe."
    TARBECK @sad "You are playing with fire..."
    TARBECK @sad "If one of those women's husbands IS responsible, then-"
    LADY_TARBECK @talk "Then I have {i}him{/i} to keep me safe."
    "Her hand gently rested on my chest, but her eyes never left her husband."
    TARBECK @sad "{i}*Sigh*{/i} I won't stop you, but..."
    TARBECK @sad "Be safe."
    hide lord_tarbeck with dissolve
    "He said nothing else as he left. For a man who supposedly didn't care or fuck his wife anymore,"
    "He sure did seem to light up when he thought he might actually lose her..."
    LADY_TARBECK @sad "... Thank you for not saying anything."
    MC @think "I want answers."
    LADY_TARBECK @talk "I've known about my magecraft my whole life, but I've chosen to keep it a secret, even from my husband."
    MC @think "Why?"
    LADY_TARBECK @talk "{i}Because my parents were dark mages.{/i}"
    MC @surprised "... What?!"
    LADY_TARBECK @talk "No one knows. As far as my husband knows, they're both dead."
    MC @think "Are they?"
    LADY_TARBECK @angry "I don't know... I ran away around the time they were planning on FUCKING SACRIFICING ME."
    MC @surprised "... By the gods."
    LADY_TARBECK @talk "It won't be a problem, are we clear?"
    LADY_TARBECK @talk "I have spent years suppressing it, and I intend to live the rest of my life doing exactly that and forgetting this little hiccup."
    MC @talk "... Fine."
    LADY_TARBECK @think "You will keep it a secret?"
    MC @talk "It's not my business, just tell me what you want next."
    MC @talk "Meet me at {i}The Pale Dragon{/i} when you are ready, my lady."
    LADY_TARBECK @talk "The Pale Dragon... Very well."
    "With a gentle bow, I turned to leave."
    show mc at nod
    $ Pause(0.25)
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    LADY_TARBECK @sad "(... Why does it bother me he seems upset with me?)"
    show lady_tarbeck at center_f with ease
    LADY_TARBECK @angry "(I don't owe him anything! He's not my husband!)"
    LADY_TARBECK @sad "(... S-Still...)"
    $ QstSetProgress(QstTheTarbecks2, 6)
    $ QstSetDelay(QstTheTarbecks2, 1)
    $ LocEnter()

##############################################################################################################################################################################################
#SCENE 8
#Quest update: Wait at the Pale Dragon a day or two...
#Quest descrip: 
#The next day at the The Pale Dragon 
label qst_TheTarbecks2_meet_at_pale_dragon:
    show mc at cleft with easeinleft
    show rania at cright_f with easeinright
    RANIA @talk "Got a lady looking for you."
    MC @think "Who?"
    RANIA @talk "Don't know, but she's standing there like a scared mouse and stands out just as much as one."
    "Looking over Rania's shoulder, I spotted Lady Tarbeck standing sheepishly with her hands clasped together, looking around at all times."
    RANIA @think "... She looks like she'd snap in half with a good fuck."
    MC @smile "Offering to jump in her place?"
    RANIA @smile "Ha! Maybe when you're less poor."
    "She eyed me up and down."
    RANIA @smile "Then again..."
    "She smirked."
    RANIA @smile "Maybe if I get rich enough I'll just keep you around myself..."
    hide rania with dissolve
    "Winking, Rania strutted off with a slightly exaggerated gait, knowing full well I would turn back to look at her as she went to fetch some more drinks for patrons."
    show lady_tarbeck at cright_f with easeinright
    LADY_TARBECK @angry "Enjoying the view?"
    MC @smile "Of course, why do you ask?"
    MC @smile "Would you prefer I was admiring a different view?"
    LADY_TARBECK @angry "N-No! Of course not!"
    MC @smile "You sound jealous."
    LADY_TARBECK @angry "Urghh! You're infuriating!"
    "She pouted, pausing for a moment."
    LADY_TARBECK @talk "Come back to the manor this evening, Lady Belamore and the others will be there."
    MC @think "Tonight?"
    LADY_TARBECK @talk "Yes, and then once I get what I want, we can put this whole thing behind us and go our separate ways."
    MC @talk "Hmm."
    LADY_TARBECK @angry "Not hmm! The. End!"
    MC @smile "If that's what you want."
    MC @smile "Now how about a drink while you're here?"
    LADY_TARBECK @blush "... I shouldn't."
    LADY_TARBECK @blush "Me, drinking with another man, what would other people think?"
    MC @talk "I know what your husband would think."
    MC @talk "{i}Can I watch in the corner?{/i}"
    "For the first time, Lady Tarbeck burst out laughing."
    LADY_TARBECK @laugh "Oh gods, he would!"
    LADY_TARBECK @laugh "You... You are..."
    LADY_TARBECK @laugh "Very dangerous for me to be around too long."
    "She paused for a moment."
    LADY_TARBECK @happy "{i}One drink.{/i}"
    "Ordering in a round, Lady Tarbeck spent the next hour with me talking, unusually relaxed."
    "One drink became two, which became..."
    "Her eyes wandered over me occasionally, but she would always catch herself and stop herself from going too far."
    LADY_TARBECK @happy "Oh gods, you're a menace."
    MC @smile "For sharing a drink with you?"
    LADY_TARBECK @happy "Ahhhh.... You know what you're doing!"
    LADY_TARBECK @talk "Gods, I can't believe you talked me into-"
    show lady_tarbeck at center_f with ease
    show lady_tarbeck at shake
    "Suddenly, Lady Tarbeck tripped, squealing as I managed to reach out and catch her before she fell."
    "Her eyes widened, her trembling breath quickening as she looked up towards me."
    hide lady_tarbeck with easeoutleft
    "Regaining her footing, she muttered 't-thank you' before hurrying away."
    show mc at center with ease
    $ QstSetProgress(QstTheTarbecks2, 7)
    MC @smile "(Cute.)"
    $ LocEnter()

######################################################################################################################################################################################################
#SCENE 9
label qst_TheTarbecks2_entertain:
    show lady_tarbeck at cright_f
    show mc at cleft with easeinleft
    LADY_TARBECK @shock "Finally! The ladies will be here any moment!"
    MC @talk "So, are you still sure about this?"
    LADY_TARBECK @talk "Yes, this is the only way."
    LADY_TARBECK @happy "Just keep them happy, and I'll handle the rest."
    show lady_tarbeck at right_f with ease
    show mc at blurin, cright_f with ease
    "No sooner had she finished speaking than the door opened as a guard escorted in Lady Belamore and her friends."
    show cg_guard_hamun at left with easeinleft
    GUARD "My lady, your guests have arrived."
    show lady_belamore at cleft with easeinleft

    hide cg_guard_hamun with easeoutleft
    show lady_bargore at left with easeinleft
    LADY_BELAMORE @smile "So good to see you all!"
    "Lady Belamore and her friends smirked and giggled as they hungrily looked me over."
    LADY_TARBECK @happy "So good of you all to make it, please... Why don't you all join me in one of the parlor rooms."
    LADY_BELAMORE @talk "I trust you can be... discreet with all this?"
    LADY_TARBECK @happy "If there is one thing we know, it's how and when to be discreet here."
    "Lady Belamore smiled and nodded assuredly."
    LADY_BELAMORE @smile "Then we are in your care, please, lead the way."
    scene black with dissolve
    scene bg_tarbeck_master_maid_room
    $ LocFlush()
    show mc at cleft
    show lady_tarbeck at left
    with dissolve
    show lady_belamore at cright_f
    show lady_bargore at right_f
    show lady_narisha at center_f

    hide lady_tarbeck with easeoutleft

    "... The ladies took to sitting around the parlor room as Lady Tarbeck ordered the servants to bring some of the best wine."
    "As the drinks flowed, idle chatter and questions soon turned more and more... personal."
    LADY_BELAMORE @smile "Now that we're away from prying eyes."
    LADY_BELAMORE @smile "Tell us, we want to hear tales of adventure or..."
    LADY_BELAMORE @smile "Pleasure..."
    "The women giggled as Lady Tarbeck turned towards me... What tale should I tell them?"
    menu:
        "Tell them about your romance with Elena." (AppearIf = CharIsLover("elena")):
            MC @smile "A woman, half wolf, half human... I took as a lover."
            "The women stared at each other incredulously for a moment."
            LADY_BELAMORE @think "A wolf girl?"
            LADY_BELAMORE @smile "Go on..."
            "As I told the story of Elena slowly coming to trust me, more and more the women seemed intrigued by my tale."
            LADY_BELAMORE @smile "It's certainly more romantic than I expected... Hmm... How curious."
            "One of the other women, Lady Narisha, seemed particularly teary-eyed."
            pass
        "Tell them about your romance with Ves." (AppearIf = CharIsLover("ves")): 
            $ QstTheTarbecks().Entertain_ToldAboutVes = True
            MC @smile "I saved an orcess who I have grown close to."
            "The women gasped, as though I had just confessed to some deep taboo."
            LADY_BELAMORE @shock "An orc?"
            LADY_BELAMORE @shock "A filthy orc?"
            "The words grated against me for some reason, especially comparing how much I'd rather have Ves than these harpies, but still I smiled."
            MC @smile "She's quite beautiful."
            LADY_NARISHA @talk "Do you... Love her?"
            "I pondered the thought for a moment, and as I glanced, I swear I saw a glimpse of someone listening around a corner."
            MC @talk "They are..."
            MC @smile "Very easy to love."
            show ves at left with easeinleft
            VES @blush "(Oh gods...)"
            "Lady Narisha oddly smiled, blushing lightly as if touched by the words."
            hide ves with easeoutleft
            LADY_BARGORE "Well, I think you're a degenerate, mating with an animal."
            "She grinned."
            LADY_BARGORE "{i}But tell us what it was like.{/i}"
            MC @talk "Tender..."
            "The women seemed almost disappointed with the answer, so I made sure not to lose them."
            MC @smile "And passionately ferocious when she's done kissing me."
            "The women gasped, shock descending into giggles as Lady Belamore, intrigued, asked,"
            LADY_BELAMORE @talk "Do they {i}taste{/i} different to us?"
            LADY_BARGORE @shock "L-LADY BELAMORE!"
            MC @smile "They do."
            MC @smile "{i}I would live between her legs if I could.{/i}"
            "The women roared with excitement as Lady Belamore licked her lips teasingly."
            pass
        "Tell them about a past fling.":
            MC @talk "There was... a woman from before I became an adventurer."
            LADY_NARISHA @smile "{i}*Gasp!*{/i}"
            LADY_NARISHA @smile "is this a romance of two lovers desperate to reunite? Have you spoken to her since? Oooh! Tell us all the details!"
            MC @talk "Her name was Elia."
            MC @talk "Our relationship was complicated."
            MC @talk "And very... {i}physical.{/i}"
            "The women giggled collectively."
            LADY_BELAMORE @talk "And this, Elia..."
            LADY_BELAMORE @talk "{i}What happened to her?{/i}"
            MC @talk "She was convinced that I was seeing another woman, a childhood friend."
            MC @talk "Things became worse between us, until eventually..."
            MC @talk "She chose to accept the hand of another suitor."
            "The women paused for a moment."
            LADY_NARISHA @sad "That's so sad... Do you miss her?"
            LADY_BARGORE @talk "I want to hear more about the fucking."
            LADY_NARISHA @shock "LADY BARGORE!"
            LADY_BARGORE @talk "What? That's why we're here!"
            LADY_BELAMORE @think "Is that how the story ends?"
            LADY_BELAMORE @think "So it just quietly fizzled out?"
            LADY_BELAMORE @talk "That's a little drab... Don't you think?"
            MC @talk "Not quite... My lady."
            "The ladies leaned in closer, intrigued by my words."
            MC @talk "Elia chose to marry him because he offered security... Wealth."
            MC @talk "Things I couldn't give her back then."
            MC @talk "... But the night before her wedding."
            MC @talk "{i}It was my door she knocked on.{/i}"
            "The women giggled in delight, while Lady Belamore sipped her wine, pleased."
            LADY_NARISHA @smile "HOW ROMANTIC!"
            LADY_BARGORE @smile "{i}How sordid.{/i}"
            LADY_BELAMORE @smile "And after this forbidden night of passion, what then?"
            MC @talk "Then we parted ways... Fully."
            MC @talk "I haven't seen her in years, and life has taken us towards very different paths."
            "The woman paused to soak in the story, sharing the wine freely."
            LADY_NARISHA @smile "How sad that it was just one night..."
            LADY_BARGORE @smile "I agree, you should have kept her on call for your bed."
            LADY_NARISHA @shock "Lady Bargore! You know that's not what I meant!"
            "The ladies dissolved into fits of laughter."
            pass
    LADY_BELAMORE @smile "Now then, the main event."
    LADY_BELAMORE @smile "Show us the beast of Novaras, show us what you become."
    "Lady Belamore sipped at her wine as the women waited and watched, mesmerised."
    LADY_NARISHA @smile "Yes! Show us!"
    LADY_BARGORE @smile "Is it true you grow two heads?"
    MC @smile "Haha, no, my lady, I don't grow two heads."
    MC @smile "But please, try not to be alarmed by the change."
    MC @smile "I am still myself."
    "The women didn't answer, they simply paused and waited for the spectacle to come."
    $ PlaySound(audio.transform)
    hide mc
    show mc_transformed at cleft
    with flash
    "As my body shifted form and shape, the women watched, mesmerised."
    "For a moment, their expressions were painted pale white with fear, but soon,"
    "as I gave them a curt bow, the tension broke as the women laughed."
    LADY_NARISHA @smile "Gods... I thought I was about to be eaten for a moment there!"
    MC "I'm still willing to eat {i}one{/i} part of you, Lady Narisha... If you ask nicely."
    "Lady Narisha laughed nervously, but she didn't say no."
    LADY_BARGORE @shock "Gods... Can I?"
    "Lady Bargore motioned to touch me and I let her,"
    "her delicate hand slowly ran down my body with bated breath, stopping just above my waist for a moment."
    "Her eyes looked up to mine, and seeing no disapproval, she smiled as her hand continued to move down, gently running over my cock."
    LADY_BARGORE @blush "It's so..."
    LADY_BARGORE @blush "{i}Heavy.{/i}"
    "Lady Belamore had seen enough."
    LADY_BELAMORE @smile "I want him."
    "The other ladies stopped giggling as Lady Belamore turned her head towards Lady Tarbeck."
    show lady_tarbeck at left with easeinleft
    LADY_BELAMORE @smile "Let me borrow your servant tonight."
    LADY_TARBECK @happy "Hmm..."
    LADY_TARBECK @happy "It could be arranged."
    LADY_TARBECK @happy "Should we come to terms."
    LADY_BELAMORE @smile "Hm... Let's cut to the chase, shall we?"
    LADY_BELAMORE @serious "You want to make your husband a high lord, yes?"
    LADY_TARBECK @talk "... Yes."
    LADY_BELAMORE @talk "Give us your servant to play with, and, ON THE CONDITION your husband is open to talks on mutual trade, then I will see to it my husband sees the {i}correct{/i} choice."
    LADY_TARBECK @think "And you're certain he will agree?"
    LADY_BELAMORE @smile "Of course dear... But do rest assured, I will expect you to continue to supply us {i}entertainment{/i} from now on."
    LADY_TARBECK @happy "... I'm sure we can oblige."
    SHYAHTAN "(I do not trust them.)"
    MC "(Neither do I, but what choice do we have?)"
    MC "(Threaten them? Find blackmail on them?)"
    SHYAHTAN "(... Analysis complete.)"
    SHYAHTAN "(I have a simpler solution.)"
    MC "(What?)"
    "Carefully, excreted from our flesh, invisible to the naked eye, I felt a shift in the air." 
    #Some kind of pink screen effect flash or something? 
    # Otherwise may need artwork here
    with Fade(0.1, 0.0, 1.0, color = "#ffa1f7ee")
    MC "(What was that?)"
    SHYAHTAN "(Insurance.)"
    LADY_TARBECK @happy "Then we have a deal."
    LADY_BELAMORE @smile "Excellent."
    LADY_TARBECK @happy "Let me take you to the guest-"
    LADY_BELAMORE @talk "Your quarters."
    LADY_TARBECK @think "W-What?"
    LADY_BELAMORE @smile "I want to fuck him in your bed."
    LADY_TARBECK @sad "... O-Oh..."
    LADY_BELAMORE @think "That won't be a problem now..."
    LADY_BELAMORE @smile "{i}Will it?{/i}"
    "Lady Tarbeck paused, as though she wished to protest, offering up only a forced smile."
    LADY_TARBECK @happy "N-No... Of course not."
    "The ladies smiled, rising from their seats."
    LADY_TARBECK @happy "I'll have a guard escort you to my chambers."
    LADY_BELAMORE @smile "Very good."
    "As the ladies were led off, I turned towards Lady Tarbeck, who seemed uncertain in herself."
    show mc_transformed at blurin, cright_f with ease
    show lady_tarbeck at cleft with ease
    MC "Are you sure about this?"
    "Lady Tarbeck seemed uncertain for a moment, as the question she had answered easily before now left her seemingly more perturbed than she would like to admit."
    LADY_TARBECK @sad "O-Of course."
    LADY_TARBECK @angry "Why wouldn't I be?"
    "For a moment, Lady Tarbeck seemed unsure of herself, even if she couldn't quite put into words why."
    LADY_TARBECK @think "Just... Go see to them, yes?"
    LADY_TARBECK @think "We had a deal, you keep up to your end, I will keep up to mine."
    MC @talk "... Very well."
    show mc_transformed at blurin, cright
    hide mc_transformed with easeoutright
    LADY_TARBECK @sad "... {i}*Sigh*{/i}"
    show lady_tarbeck at center with ease
    LADY_TARBECK @sad "(What am I doing?)"
    scene black with dissolve

    $ SetRepeatVariant(False)
    call rom_hamun_trio_foursome from _call_rom_hamun_trio_foursome

    # (continues from here after the sex scene ends)
    "Rising from the bed with a satisfied expression, Lady Belamore smiled towards me."
    $ LocFlush()
    show mc_transformed at cleft
    show lady_belamore at center_f
    show lady_bargore at cright_f
    show lady_narisha at right_f
    with dissolve
    LADY_BELAMORE @smile "That was... wonderful."
    MC "I'm glad you're satisfied."

    $ PlaySound(audio.door_knock)
    $ Pause(0.25)
    #"{i}Knock Knock Knock{/i}"
    show lady_tarbeck at left with easeinleft
    "The door opened as Lady Tarbeck stepped inside. Hit by the sudden heat and smell of sex, she seemed taken aback for a moment."
    LADY_TARBECK @shock "Gods, it smells like a brothel in here."
    LADY_BELAMORE @smile "A familiar smell for you, I'm sure."
    "Lady Tarbeck frowned at the comment."
    LADY_BELAMORE @smile "Relax, you've kept up to your end of the bargain, now I'll see to it I keep up with mine."
    LADY_BELAMORE @smile "Girls, gather your things."
    LADY_BELAMORE @smile "Lady Tarbeck will clean up after us."
    "Lady Tarbeck's face contorted into a forced smile, her hand tightening into a fist."
    LADY_TARBECK @happy "Of... course."
    LADY_BELAMORE @talk "I will make arrangements and be in touch soon."
    hide lady_belamore with dissolve
    hide lady_bargore with dissolve
    hide lady_narisha with dissolve
    "The women giggled as they left of their own accord."
    show lady_tarbeck at blurin, cright_f with ease
    LADY_TARBECK @sad "{i}Sigh{/i}"
    MC "What now?"
    LADY_TARBECK @talk "Now nothing. I will be in touch once Lady Belamore has confirmed the deal with my husband and then our business is concluded."
    MC "... Is that so?"
    LADY_TARBECK @sad "S-Stop making it sound so bad."
    LADY_TARBECK @sad "We both knew things would end this way."
    LADY_TARBECK @sad "And I ALWAYS said I wouldn't sleep with you from the start!"
    MC "Yes... Yes, you did tell me."
    MC "Then if you'll excuse me, my lady, I'll be heading back."
    LADY_TARBECK @sad "G-Goodnight."
    MC "Goodnight."
    show mc_transformed at blurin, cleft_f
    hide mc_transformed with easeoutleft
    LADY_TARBECK @sad "{i}Sigh{/i}"
    show lady_tarbeck at center_f with ease
    LADY_TARBECK @sad "(Just a little longer... And you can forget about this.)"
    LADY_TARBECK @sad "({i}And him.{/i})"
    scene black with dissolve
    $ QstSetProgress(QstTheTarbecks2, 8)
    $ QstSetDelay(QstTheTarbecks2, 2)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

##################################################################################################################################################################################################
# Quest description: 
# Two days later in-game Lady Tarbeck another city guard will approach the player while wandering around the city map
label qst_TheTarbecks2_lord_tarbeck_kidnapped:
    show mc at cleft with easeinleft
    show cg_guard_hamun at cright_f with easeinright
    GUARD "Lady Tarbeck requests your presence at once!"
    GUARD "It is an emergency!"
    MC @think "What's going on?"
    show cg_guard_hamun at shake
    GUARD "Lord Tarbeck has been KIDNAPPED!"
    MC @surprised "What?!"
    GUARD "I must go join the others searching for him! Please! Hurry to Lady Tarbeck at once!"
    hide cg_guard_hamun with easeoutleft
    #The guard exits offscreen
    show mc at center with ease
    MC @serious "(I should hurry to Lady Tarbeck's side as quickly as possible.)"
    $ QstSetProgress(QstTheTarbecks2, 9)
    $ LocEnter()

# exclusively for "that note"
screen QstTarbecksNote():
    add "qst_dreamhouse_note"
    text _("{size=+10}Relinquish rights to your mines, and I will see to it that your husband is returned unharmed.{/size}"):
        align (0.5, 0.5)
        xsize 470
        style "prologue_letter_text_main"
        color "#000000ff"
    button:
        xsize 1920
        ysize 1080
        background Null()
        action [With(Dissolve(0.15)), Return()]
    timer 1.5 action [With(Dissolve(0.15)), Return()]
   

#####################################################################################################################################################################################################
label qst_TheTarbecks2_kidnapped_arrive_mansion:
    show mc at cleft with easeinleft
    show lady_tarbeck at cright_f with easeinright
    LADY_TARBECK @scared "[player_name]!"
    LADY_TARBECK @scared "Thank the gods! I've been looking all over for you!"
    MC @think "Lady Tarbeck?"
    LADY_TARBECK @scared "They've taken him! THEY'VE TAKEN MY HUSBAND!"
    MC @serious "Tell me everything that has happened."
    LADY_TARBECK @sad "Lady Belamore had one of her men arranging a meeting with my husband to discuss a trade deal."
    LADY_TARBECK @cry "Oh gods..."
    MC @think "How do you know he was taken?"
    LADY_TARBECK @sad "He hasn't come home, and earlier, I received this letter."
    play sound audio.letter
    call screen QstTarbecksNote() with dissolve
    MC @think "They cannot be serious with this."
    MC @talk "How is that legal?"
    LADY_TARBECK @angry "It's not in Alderay, but this is Hamun."
    LADY_TARBECK @sad "I'm to meet Lady Belamore and the others later."
    LADY_TARBECK @angry "I'm certain those bitches have betrayed me!"
    MC @talk "Calm down... Now tell me what you want me to do."
    LADY_TARBECK @sad "Come with me, please."
    LADY_TARBECK @sad "I'm terrified that they might try something else."
    MC @talk "Alright."
    LADY_TARBECK @shock "Really?"
    MC @talk "I hardly have a choice if they've kidnapped your husband, do I?"
    MC @serious "{i}I need him, remember?{/i}"
    LADY_TARBECK @sad "R-Right..."
    LADY_TARBECK @sad "Tell me when you're ready then, and we'll head over together."
    scene black with dissolve
    $ QstSetProgress(QstTheTarbecks2, 10)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

#Lady Tarbeck in the day waits in The Pale Dragon for the player
label qst_TheTarbecks2_paledragon_kidnapgo:
    show lady_tarbeck at center_f with dissolve
    LADY_TARBECK @sad "Are you ready?"
    menu:
        "Let's go.":
            LADY_TARBECK @shock "C-Come with me..."
            pass
        "I still need some time.":
            LADY_TARBECK @sad "Please, hurry..."
            LADY_TARBECK @sad "I can't bear the thought if they hurt him."
            $ LocEnter()
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("hamun_castle_tea_room")
    $ LocFlush()
    show lady_belamore at cleft
    show lady_bargore at center
    show lady_narisha at left
    with dissolve
    show lady_tarbeck at cright_f with easeinright
    show mc at right_f with easeinright
    "As Lady Tarbeck stormed into the tea room, Lady Belamore and the others were sat around as usual, laughing about something."
    "When they saw Lady Tarbeck enter the room, the laughter died down as all eyes turned to her."
    LADY_TARBECK @angry "... Where is my husband?"
    LADY_BELAMORE @smile "Have you tried a brothel?"
    "The women burst into laughter as an enraged Lady Tarbeck swiped one of the cups of tea with her hand, watching it fling across the floor and shatter."
    LADY_BELAMORE @angry "Are you mad?"
    LADY_TARBECK @angry "WE HAD A DEAL."
    LADY_BELAMORE @smile "Did we?"
    LADY_BELAMORE @smile "I don't recall."
    LADY_TARBECK @angry "Don't test me."
    LADY_BELAMORE @angry "Then remember your place."
    LADY_TARBECK @sad "... Why?"
    LADY_BELAMORE @think "Did you really think we'd ever allow that embarrassment of a man here?"
    LADY_BELAMORE @angry "Your husband is a disgusting glutton and pervert."
    LADY_BELAMORE @smile "A joke."
    "Lady Tarbeck's hand reached out to slap Lady Belamore. The women gasped as Lady Belamore rubbed at her stinging cheek."
    LADY_BELAMORE @angry "You fucking BITCH!"
    LADY_TARBECK @angry "WHERE. IS. MY. HUSBAND?"
    LADY_BELAMORE @angry "HMMMM."
    LADY_BELAMORE @smile "How about you sign over your estate and ownership of those mines and then {i}maybe{/i} I'll help you find him!"
    LADY_TARBECK @angry "What... WHAT?!"
    LADY_BELAMORE @smile "Turns out, the fool has it legally bound that the estate and the mines require both your signatures."
    LADY_BELAMORE @smile "Otherwise, without both of you signing, the ownership defaults back to Alderian arbitration."
    LADY_BELAMORE @smile "And no one gets the mines then."
    LADY_BELAMORE @smile "Oh dear... What a hassle."
    LADY_BELAMORE @talk "Now give me what I want. YOUR signature."
    LADY_TARBECK @angry "You expect me to just roll over and give you everything?"
    LADY_BELAMORE @smile "Yes... {i}Like you always do for us.{/i}"
    "Lady Tarbeck stared for a moment, as though her soul had been crushed, before angrily storming away as I followed behind."
    show lady_tarbeck at blurin, cright
    hide lady_tarbeck with easeoutright
    show mc at blurin, right
    hide mc with easeoutright
    "The women went back to laughing..."
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show mc at cright_f
    show lady_tarbeck at cleft
    with dissolve
    LADY_TARBECK @angry "THOSE FUCKING BITCHES!"
    LADY_TARBECK @angry "I HATE THEM! I HATE THEM ALL SO MUCH!"
    "An enraged Lady Tarbeck kicked furiously at the sand, her hands clenched into fists as she growled loudly in impotent rage."
    LADY_TARBECK @sad "... Oh gods, why did I have to get involved with them?"
    LADY_TARBECK @sad "What in the hells am I going to do?"
    "As I opened my mouth to speak and comfort her, a voice called out in the back of my head."
    SHYAHTAN "(Wait.)"
    MC @think "(What?)"
    SHYAHTAN "(Tell her to wait... The solution is already in progress.)"
    MC @think "(What are you talking about?)"
    SHYAHTAN "(Wait... All you need to do is wait.)"
    MC @talk "Just wait."
    LADY_TARBECK @shock "What?"
    LADY_TARBECK @shock "What are you talking about?"
    LADY_TARBECK @angry "If I do nothing they'll just kill my husband!"
    MC @angry "I know that!"
    MC @sad "You just... Need to wait."
    LADY_TARBECK @angry "Give me one good reason why."
    MC @talk "The voice... The thing attached to me."
    MC @talk "It said to."
    LADY_TARBECK @angry "And I'm just supposed to trust that?"
    MC @talk "And if you don't, what happens?"
    MC @serious "If you retaliate, they'll just kill him!"
    LADY_TARBECK @sad "... If he's even alive still to begin with."
    LADY_TARBECK @sad "The whole thing could just be a bluff to get me to sign."
    MC @sad "Then what do you have to lose?"
    LADY_TARBECK @think "... Do you really trust this thing attached to you?"
    LADY_TARBECK @think "{i}Truly.{/i}"
    MC @surprised "I-"
    menu:
        "Yes.":
            $ QstTheTarbecks2().KidnappedTrustParasite = True
            "I felt something shift inside of me."
            "{i}...Surprise.{/i}"
            SHYAHTAN "(... You should be more cautious.)"
            SHYAHTAN "(... But it is noted.)"
            pass
        "No.":
            MC @talk "No, of course not."
            MC @talk "But whether I trust what's inside of me or not is irrelevant."
            MC @serious "{i}We need each other to stay alive.{/i}"
            pass
        "I don't know.":
            MC @talk "But my fate is intertwined with it."
            MC @talk "Whatever's pulled us together... We're heading down that road together whether we like it or not."
            pass

    LADY_TARBECK @sad "{i}Sigh{/i}"
    LADY_TARBECK @sad "Alright, I'll trust you."
    "Lady Tarbeck began to leave with some of her guards waiting nearby."
    "She stopped, looking back towards me before she left."
    LADY_TARBECK @sad "I just hope it won't all be for nothing."
    hide lady_tarbeck with easeoutright
    #Lady Tarbeck leaves
    show mc at center_f with ease
    MC @think "(You better be sure about this.)"
    show mc at blurin, center
    "I heard, for a brief moment, what sounded like laughter."
    SHYAHTAN "(In time...)"
    SHYAHTAN "(Just wait.)"
    $ QstSetProgress(QstTheTarbecks2, 11)
    $ QstSetDelay(QstTheTarbecks2, 1)
    $ LocEnter()

############################################################################################################################################################
#SCENE 11
label qst_TheTarbecks2_summoned_again:
    show mc at cleft with easeinleft
    show cg_guard_hamun at cright_f with easeinright
    GUARD "Lady Tarbeck requests your presence urgently!"
    MC @think "What for?"
    GUARD "She did not say, she simply told me to tell you to come quickly!"
    show cg_guard_hamun at blurin, cright
    hide cg_guard_hamun with easeoutright
    show mc at center with ease
    SHYAHTAN "(It's time.)"
    $ QstSetProgress(QstTheTarbecks2, 12)
    $ LocEnter()

#############################################################################################################################################################
#SCENE 12
label qst_TheTarbecks2_summoned_mansion:
    show lady_tarbeck at cright_f
    with dissolve
    show mc at cleft with easeinleft
    "Lady Tarbeck paced up and down the floors of the main hall anxiously."
    "When she saw me, she hurried over with a scowl on her face."
    LADY_TARBECK @angry "DID YOU POISON THEM?!"
    MC @surprised "What?"
    MC @angry "No!"
    LADY_TARBECK @angry "They're here! Those whores are here convinced one of us poisoned them!"
    LADY_TARBECK @angry "They're all raving mad!"
    MC @think "Let me speak to them."
    scene black with dissolve
#Brief fade to black
    $ LocFlush()
    show lady_belamore at cright_f
    show lady_bargore at right_f
    show lady_narisha at center_f
    with dissolve
    show mc at cleft
    show lady_tarbeck at left
    with easeinleft
    "The women were erratic, pacing up and down, scratching at their ragged hair, their eyes heavy with black circles."
    "When Lady Belamore saw me, she stormed over and slapped me."
    MC @angry "Fuck!"
    "The mark on my cheek stung as she growled angrily at me, beating at my chest with her fists before I pushed her off."
    MC @angry "WHAT'S THE MATTER WITH YOU?!"
    LADY_BELAMORE @angry "YOU'VE POISONED US!"
    MC @think "What in the hells are you talking about?!"
    LADY_BELAMORE @angry "Don't play dumb!"
    LADY_BELAMORE @angry "Since that night, none of us can sleep!"
    LADY_BELAMORE @angry "And every single one of us can't stop thinking about you!"
    "I nearly burst out laughing."
    MC @laugh "Is this some kind of a joke?"
    LADY_BELAMORE @angry "It's not fucking funny!"
    LADY_BELAMORE @angry "We're seeing things that aren't there!"
    LADY_BELAMORE @angry "It's TORTURE!"
    LADY_BELAMORE @angry "What did you do to us?!"
    "Lady Belamore didn't even get to finish her complaints when Lady Narisha threw herself towards me, planting her lips against mine."
    MC "...?!"
    "I pushed her away as she begged pitifully like a dog."
    LADY_NARISHA @shock "Please... Please fuck me again!"
    LADY_BARGORE @angry "No! Me first!"
    "Lady Belamore yanked the two women back by the collar."
    LADY_BELAMORE @angry "You will cure us of this affliction, or Lord Tarbeck will be found floating face down in the sea!"
    "Practically dragging the women away, Lady Tarbeck turned to me, completely baffled."
    LADY_TARBECK @shock "What in the world is going on?"
    MC @surprised "I'm not quite sure..."
    LADY_TARBECK @angry "Well you better figure out a 'cure' or whatever it is!"
    LADY_TARBECK @angry "Otherwise they'll-"
    "Lady Tarbeck stopped herself mid-sentence."
    LADY_TARBECK @shock "Wait."
    LADY_TARBECK @talk "This... This might actually work."
    MC @think "What?"
    LADY_TARBECK @happy "We have leverage now!"
    LADY_TARBECK @happy "We can demand they release my husband for a cure!"
    MC @think "So, what do we do now?"
    MC @talk "Do you want me to speak to Lady Belamore and demand your husband's return?"
    LADY_TARBECK @happy "No, they'll refuse if we ask now."
    LADY_TARBECK @happy "Let them suffer a few more days."
    LADY_TARBECK @think "... And figure out what the cure is in the meanwhile."
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show mc at center_f with easeinright
    MC @think "What's going on?"
    MC @angry "No more riddles."
    SHYAHTAN "Pheromone overload."
    MC @think "What?"
    SHYAHTAN "The hive encountered some troublesome species before, resistant to our natural pheromones."
    SHYAHTAN "Pheromone overload was developed as a way to overcome this, short, intense burst releases."
    MC @think "Will it... kill them?"
    SHYAHTAN "No."
    SHYAHTAN "But they will feel an intense desire to mate around us, and, the longer they are denied that, the more withdrawal-like symptoms will increase, such as restlessness."
    SHYAHTAN "It is an unpleasant experience."
    MC @think "And if we {i}don't{/i} fuck them?"
    SHYAHTAN "In about a month, the pheromone overload will have run its course and the symptoms will pass."
    SHYAHTAN "We do not force races to mate... If something's willpower is strong enough, they can still refuse."
    MC @serious "You never thought to mention this little trick before?"
    SHYAHTAN "It has not been needed."
    SHYAHTAN "... And it is unpleasant."
    SHYAHTAN "It is a biological weapon designed to bring down worlds... Not a toy to be abused."
    MC @talk "Do you think this plan will work?"
    SHYAHTAN "They will break."
    SHYAHTAN "They're weak-willed."
    MC @talk "I hope you're right..."
    MC "(I should wait at the Pale Dragon a while... until I recieve word.)"
    $ QstSetProgress(QstTheTarbecks2, 13)
    $ QstSetDelay(QstTheTarbecks2, 2)
    $ LocEnter()

#######################################################################################################################################
#SCENE 13
label qst_TheTarbecks2_paledragon_after_waiting:
    show mc at cright_f
    show rania at cleft
    with dissolve
    RANIA @talk "A message arrived for you."
    MC @think "What?"
    RANIA @talk "Lady Tarbeck has requested you come urgently."
    RANIA @think "I'm gonna start charging you soon if I end up having to deliver any more of these."
    MC @smile "Your services are appreciated."
    RANIA @talk "You're just lucky you're handsome."
    hide rania with easeoutright
    #Rania walks off
    show mc at center_f with ease
    MC @talk "(One of the women must be beginning to break...)"
    $ QstSetProgress(QstTheTarbecks2, 14)
    $ LocEnter()

##########################################################################################################################################
#SCENE 14
#The player returns to the Tarbeck Manor - There, Lady Bargore is talking to Lady Tarbeck
label qst_TheTarbecks2_return_to_manor_after_waiting:
    show lady_bargore at right_f
    show lady_tarbeck at cright
    with dissolve
    show mc at cleft with easeinleft
    LADY_BARGORE @scared "Please... L-Lady Tarbeck."
    LADY_BARGORE @scared "I beg of you! I don't deserve this! PLEASE!"
    LADY_TARBECK @angry "You and Lady Belamore are still holding my husband hostage!"
    LADY_BARGORE @shock "I DON'T KNOW WHERE HE IS!"
    LADY_BARGORE @shock "It was all Lady Belamore's idea! She doesn't tell us anything!"
    LADY_TARBECK @angry "Then you're even worse than just being an accomplice."
    LADY_TARBECK @angry "{i}You're an incompetent accomplice.{/i}"
    show lady_tarbeck at blurin, cright_f
    show lady_bargore at center_f with ease
    "When Lady Bargore turned towards me, her breathing became heavy, and it felt like barely a second passed before she flung herself towards me."
    LADY_BARGORE @shock "Please!"
    LADY_BARGORE @shock "I can't stop thinking about you since that night!"
    LADY_BARGORE @shock "I fucked my husband a dozen times, and it didn't fix anything!"
    LADY_BARGORE @shock "You! I NEED you to FUCK me!"
    "I gently pushed Lady Bargore away."
    MC @talk "Then you should ensure Lord Tarbeck is returned safely first, then we'll talk."
    LADY_BARGORE @sad "I... I..."
    LADY_BARGORE @angry "GRGHHH!"

    #Lady Bargore exits off-screen
    hide lady_bargore with easeoutleft
    LADY_TARBECK @talk "{i}Sigh{/i}"
    LADY_TARBECK @talk "I think one of them will break soon."
    LADY_TARBECK @think "Did you discover at all what the cure actually is?"
    MC @embarr "There's... not really a cure."
    LADY_TARBECK @shock "What?"
    MC @embarr "If I fuck them, the symptoms will go away for a while."
    MC @talk "But really, the only way for them to get over it is to just spend enough time away from me."
    "Lady Tarbeck stared blankly for a moment, and then nearly doubled over laughing."
    LADY_TARBECK @laugh "HAHAHAHA!"
    LADY_TARBECK @happy "How perfect!"
    LADY_TARBECK @happy "I'll contact those whores tonight..."
    LADY_TARBECK @happy "Let's see what happens when I dangle 'the cure' in front of them."
    LADY_TARBECK @happy "Something tells me they won't be able to hold on much longer..."
    MC @think "What should I do in the meanwhile?"
    LADY_TARBECK @smile "Hmm... Well, why don't you apply a little {i}pressure.{/i}"
    MC @think "Pressure?"
    LADY_TARBECK @smile "Introduce yourself to Lord Belamore, of course."
    LADY_TARBECK @smile "I'm sure Lady Belamore will be delighted for you two to meet."
    LADY_TARBECK @talk "Her husband is coming tomorrow morning to the keep... Why don't you have fun and run into him while he's there?"
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ QstSetProgress(QstTheTarbecks2, 15)
    $ LocEnter()

#############################################################################################################################################
label qst_TheTarbecks2_meetlord:
    show lord_belamore at cright_f
    show lady_belamore at right_f
    with dissolve
    LORD_BELAMORE @sad "My love, you look tired."
    LADY_BELAMORE @smile "I'm fine, my dear, just a little-"
    show mc at cleft with easeinleft
    MC @smile "Lady Belamore!"
    "The blood drained from her face as she saw me approaching, her husband turning towards me."
    LADY_BELAMORE @shock "... You-"
    MC @smile "So good to see you again."
    LORD_BELAMORE @think "My dear... {i}Do you know this man?{/i}"
    LADY_BELAMORE @scared "I-"
    MC @smile "Of course she does."
    LADY_BELAMORE @shock "WAIT! We-"
    MC @smile "I've been escorting Lady Tarbeck to her tea sessions with Lady Belamore and her friends."
    "Lady Belamore let out a nervous sigh of relief."
    LADY_BELAMORE @smile "Y-Yes...!"
    LADY_BELAMORE @smile "He is Lady Tarbeck's... uhh... acquaintance."
    LORD_BELAMORE @think "Hmm... I see."
    LORD_BELAMORE @smile "Such a shame to hear about his kidnapping."
    LORD_BELAMORE @smile "But I'm certain he'll be returned soon."
    MC @smile "How strange, my lord... Everyone, including you, seems so convinced he's kidnapped and not simply missing."
    MC @smile "Why is that?"
    "Lord Belamore let out a chuckle."
    LORD_BELAMORE @smile "Well... Missing... Kidnapped... He's not here, is he?"
    LORD_BELAMORE @smile "Perhaps Lady Tarbeck herself simply had enough of him."
    MC @smile "Well, as I'm sure you know, my lord."
    MC @smile2 "{i}Wives can be most treacherous.{/i}"
    LORD_BELAMORE @think "What do you mean by that?"
    LADY_BELAMORE @shock "D-DARLING!"
    LADY_BELAMORE @smile "L-Lady Pertruda and her husband are over there. Could you go make some introductions and I'll join you in a moment?"
    "Lord Belamore gave a suspicious glance back towards me."
    LORD_BELAMORE @talk "Of course, my love... I'll be right back."
    hide lord_belamore with easeoutright
    show lady_belamore at cright_f with ease
    LADY_BELAMORE @angry "What in the hells do you think you're playing at?!"
    MC @smile "Saying hello, of course."
    LADY_BELAMORE @angry "You piece of-"
    "Lady Belamore paused, her gaze lingering on my body for longer than I might have expected."
    LADY_BELAMORE @emb "... You... {i}Huff{/i}"
    MC @smile "Lady Belamore... Are you alright?"
    MC @smile "You seem a bit... {i}flushed.{/i}"
    "She shook her head."
    LADY_BELAMORE @angry "Tell your fucking mistress I'll visit her tonight."
    LADY_BELAMORE @angry "And if you ever come near my husband again..."
    LADY_BELAMORE @angry "{i}I'll kill you.{/i}"
    LORD_BELAMORE "Darling!"
    show lady_belamore at blurin, cright
    LADY_BELAMORE @smile "Coming, my love!"
    hide lady_belamore with easeoutright
    show mc at center with ease
    MC @smile "(Feisty.)"
    MC "(I should head back to Lady Tarbeck this evening then... See if the 'pressure' did any good.)"
    scene black with dissolve
    $ QstSetProgress(QstTheTarbecks2, 16)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

#############################################################################################################################################
#SCENE 15
label qst_TheTarbecks2_return_to_manor_once_more:
    show lady_belamore at center
    show lady_tarbeck at cright_f
    with dissolve
    show mc at left with easeinleft
    LADY_BELAMORE @angry "You... YOU...!"
    LADY_BELAMORE @angry "I know you did something!"
    LADY_BELAMORE @angry "FIX. IT."
    LADY_TARBECK @angry "BRING. BACK. MY. HUSBAND."
    "Lady Belamore snarled, her two minions looking particularly flushed behind her."
    LADY_BELAMORE @smile "This isn't over, you whore."
    LADY_BELAMORE @smile "Your husband is going to become food for one of my husband's newest 'pets' if you don't fix us soon."
    LADY_TARBECK @angry "You lay a finger on him and I'll leave you like this forever."
    LADY_BELAMORE @angry "FUCK YOU!"
    LADY_BELAMORE @angry "We'll see who outlasts whom!"
    show lady_belamore at blurin, center_f
    "As she turned to leave, she barged right into me and, for a moment, looked dazed as she stared into my eyes."
    "Her breathing quickened for a moment before she shook her head and stormed out, her minions chasing after her."
    hide lady_belamore with easeoutleft
    show mc at cleft with easeinleft
    MC @think "Negotiations going well, I see."
    LADY_TARBECK @angry "To the hells with them!"
    LADY_TARBECK @talk "{i}Sigh{/i} I'm going to go take a bath..."
    LADY_TARBECK @talk "I have a task for you, though."
    MC @think "Which is?"
    LADY_TARBECK @talk "One of my spies is meant to report back tonight if they've found any information on where my husband is being held."
    LADY_TARBECK @talk "They can't come into the city itself, it's too dangerous, and I've already lost three men..."
    LADY_TARBECK @talk "I suspect Belamore's assassins are waiting for him as well."
    LADY_TARBECK @sad "I need you to meet them outside the city walls after dark and find out what they know."
    MC @think "And if those same assassins try to kill me?"
    "Lady Tarbeck paused, the words stuttering out of her mouth."
    LADY_TARBECK @shock "I-"
    LADY_TARBECK @sad "{i}... You're the only one I trust anymore.{/i}"
    "I sighed."
    MC @talk "It will be done."
    LADY_TARBECK @smile "Thank you. Report back what you find."
    LADY_TARBECK @sad "And... Please be safe, alright?"
    scene black with dissolve
    $ QstSetProgress(QstTheTarbecks2, 17)
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()

#############################################################################################################################################
#Scene 15.5
#Quest update: Meet Lady Tarbeck's spy on the outskirts of Hamun.
#Quest description: Lady Tarbeck has asked me to meet one of her spies outside the city walls of Hamun tonight... I should tread carefully.
#The player clicks on the dark robed figure outside the city walls
label qst_TheTarbecks2_talkspy:
    show cg_assassin at cright_f
    with dissolve
    show mc at cleft with easeinleft
    SPY "Can I help you?"
    MC @talk "Lady Tarbeck sent me."
    SPY "Good."
    MC @think "What have you found? Do you know where Lord Tarbeck is being held?"
    SPY "Of course."
    show cg_assassin at nod
    "The figure unveiled from his robes the severed head of a man."
    MC @surprised "WHAT-"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    "Around me, I heard the unsheathing of blades as figures began to surround me."
    SPY "He will soon be joining his wife's spies in whatever hell awaits."
    "I snarled, unsheathing my blade!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_street", CharIDList_Right = [{"e_assassin":12}, {"e_assassin":14}, {"e_assassin":12}, {"e_assassin":11}]))
    "Cut down into bloody heaps, I pointed my blade at the last of them, barely still standing."
    $ LocFlush()
    show mc at cleft
    show cg_assassin at cright_f
    with dissolve
    MC @angry "Where the fuck is Lord Tarbeck?"
    MC @angry "Tell me and I will spare you!"
    SPY "Hahaha..."
    SPY "You fucking idiot."
    SPY "Even if you spared me, my masters would kill me before the sun rose."
    "The man reached for a vial which he quickly poured down his throat."
    show mc at shake
    hide cg_assassin with dissolve
    play sound "audio/cfx/body_falling.ogg"
    MC @surprised "NO!"
    "Almost instantly, the man began seizuring on the ground, his eyes rolling white as he wretched up blood."
    show mc at center with ease
    "I reached to grab his shoulders, but there was nothing to be done..."
    "In a few moments, he was dead."
    $ AutoMus(True)
    MC @serious "(Fuck... There goes our lead, I guess.)"
    show mc at blurin, center_f
    MC @sad "(What a shitty night... I'll report back to Lady Tarbeck tomorrow and tell her what happened.)"
    $ QstSetProgress(QstTheTarbecks2, 18)
    $ LocEnter()

#############################################################################################################################################
#SCENE 16
label qst_TheTarbecks2_return_to_manor_after_spy:
    show lady_belamore at center
    show lady_narisha at cright
    show lady_tarbeck at right_f
    with dissolve
    show mc at cleft with easeinleft
    LADY_BELAMORE @sad "Darling..."
    LADY_BELAMORE @sad "We used to be such good friends, didn't we?"
    LADY_TARBECK @angry "I can't recall."
    LADY_BELAMORE @smile "How about this? You forget about that brute of a husband of yours."
    LADY_BELAMORE @smile "He never deserved you anyway!"
    LADY_BELAMORE @smile "Now, Lord Visnara's son is a handsome young man who's always expressed an interest in-"
    LADY_TARBECK @talk "I want my husband back."
    LADY_BELAMORE @angry "OH FOR FUCK'S SAKE."
    LADY_BELAMORE @angry "Why? So the man can slobber over another maid? So he can fuck another whore and continue to humiliate you?"
    LADY_BELAMORE @smile "Or are you that pathetic that you actually enjoy being treated like that?"
    LADY_BELAMORE @smile "Is that it? Do you get off on being embarrassed?"
    LADY_TARBECK @angry "Get out!"
    LADY_TARBECK @angry "Leave and don't return until you're ready to tell me where my husband is!"
    LADY_NARISHA @scared "M-Mistress, maybe we should-"
    LADY_BELAMORE @angry "Shut up, you fool!"
    show lady_belamore at blurin, center_f
    show lady_narisha at blurin, cright_f
    hide lady_belamore
    hide lady_narisha
    with easeoutleft
    "Once more, Lady Belamore stormed out of the manor, the two dishevelled women chasing after her."
    MC @think "Are you alright?"
    LADY_TARBECK @talk "I'm fine. I've dealt with more venom spat at me than that before."
    MC @sad "Hmm..."
    LADY_TARBECK @think "Now, onto more important matters."
    LADY_TARBECK @shock "My spy, what did he report back? Does he know where my husband is?"
    MC @sad "... I'm sorry, Lady Tarbeck."
    MC @sad "I was too late. Assassins had already reached your man."
    "Lady Tarbeck paused, her mouth hanging open slightly as she caught her breath."
    LADY_TARBECK @sad "Are... {i}Are you alright?{/i}"
    MC @talk "I'm fine, my lady."
    LADY_TARBECK @sad "{i}Sigh{/i}"
    LADY_TARBECK @sad "Just how many lives are going to be lost to all this?"
    "Lady Tarbeck took a moment to compose herself."
    LADY_TARBECK @talk "... With any luck, they won't be able to hold out much longer."
    LADY_TARBECK @talk "One of them is bound to crack eventually."
    LADY_TARBECK @sad "... Just a few more days, hopefully."
    MC @talk "Of course, my lady."
    show mc at blurin, cleft_f
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show mc at cright_f with easeinright
    MC "(Just how much longer is this going to continue?)"
    MC "(I need a drink...)"
    $ QstSetProgress(QstTheTarbecks2, 19)
    $ LocEnter()

#############################################################################################################################################
#SCENE 17
#An icon appears in The Pale Dragon 'Drown your sorrows' - Clicking it triggers a fade to black and the next event 
label qst_TheTarbecks2_drown_sorrows:
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "...Ordering a few rounds, I let the hours drift on by, until..."
    $ TimeAdvBy(TIME_1H)
    $ LocFlush()
    show mc at cright_f
    with dissolve
    show lady_narisha at cleft
    show lady_bargore at left
    with easeinleft
    MC @think "... Ladies?"
    MC @think "How did you find me-"
    LADY_NARISHA @shock "P-Please! You have to help us!"
    LADY_NARISHA @sad "We'll tell you whatever you want if you cure us!"
    MC @serious "Where is Lord Tarbeck?"
    LADY_BARGORE @shock "We don't know! I promise you!"
    LADY_BARGORE @sad "Lady Belamore is going madder by the day."
    LADY_BARGORE @shock "She is threatening to let something called 'Hugo' rip off a part of Lord Tarbeck and send it to her as a message!"
    MC @angry "Ladies, you need to help your mistress see sense!"
    LADY_NARISHA @sad "Please... {i}*Huff*{/i} I can't sleep, but I still dream about you every night!"
    LADY_NARISHA @sad "My heart hurts so much! Please!"
    LADY_NARISHA @sad "I just want it to stop!"
    LADY_NARISHA @sad "E-Everytime you speak, it's so calming..."
    LADY_BARGORE @angry "Stop being so bloody hopeless!"
    LADY_BARGORE @angry "You want his cock shoved in every hole the same as me! You just dress it up in poetry!"
    MC @angry "LADIES."
    MC @angry "Help me, help you!"
    "The two ladies shared a knowing look with one another."
    LADY_BARGORE @sad "Y-Yes, we can try."
    LADY_NARISHA @sad "But if it all goes wrong, you'll s-still help us, right?"
    MC @serious "We'll see..."
    MC @serious "Now go. Do what needs to be done to free Lord Tarbeck."
    hide lady_narisha
    hide lady_bargore
    with easeoutleft
    "The two women quickly scurried away."
    show mc at center_f with ease
    MC @sad "(I hope Lady Belamore breaks before she causes too much harm...)"
    MC "{i}*Sigh*{/i}"
    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "Continuing a few more drinks, I eventually dragged myself off to bed."
    $ TimeAdvBy(TIME_1H)
    $ InfGainDaily(False)
    $ TimeAdvTo(TIME_MORNING)
    $ InfGainDaily(True)
    $ LocSet("hamun_dist_docks")
    $ LocFlush()
    with dissolve
    show mc at cleft with easeinleft
    MC "(Hmm... Perhaps the ladies made Lady Belamore see sense at last?)"
    MC "(Perhaps I should head to the castle myself?)"
    MC "(She might be more amicable if it's just me there...)"
    $ QstSetProgress(QstTheTarbecks2, 20)
    $ LocEnter()
#############################################################################################################################################
#SCENE 18
#The player heads to the tea room
label qst_TheTarbecks2_tearoom_after_drunk:
    show lady_belamore at cleft
    show lady_bargore at left
    show lady_narisha at center
    with dissolve
    show mc at cright_f with easeinright
    LADY_BELAMORE @laugh "HAHAHA! How PATHETIC!"
    LADY_NARISHA @scared "L-Lady Belamore! Please!"
    LADY_BELAMORE @angry "TRAITORS!"
    "Her gaze turned to me when she saw me enter the room."
    "Storming towards me, Lady Belamore's open palm collided with my cheek as the other ladies gasped."
    LADY_BARGORE @shock "L-LADY BELAMORE!"
    LADY_BELAMORE @angry "QUIET, YOU!"
    LADY_BELAMORE @angry "... Who do you think you are?"
    LADY_BELAMORE @angry "DO YOU THINK I'M AS WEAK AS THESE TWO FOOLS?"
    LADY_BELAMORE @angry "THEY'RE WEAK! THEY'RE PATHETIC INSECTS!"
    LADY_BELAMORE @angry "HOW DARE YOU DO THIS TO ME!"
    MC @serious "No... Lady Belamore."
    MC @talk "I do not think you are weak."
    "Lady Belamore stared for a moment, her eyes scanning over me for a long time."
    "{i}Too long.{/i}"
    MC @serious "But I do think you're making quite a scene."
    "Looking around, this little scene had indeed grabbed the attention of every lord and lady in the room."
    "With a nervous breath and a racing heart, Lady Belamore stuttered out a few words before frantically fleeing."
    hide lady_belamore with easeoutright
    LADY_NARISHA @shock "Lady Belamore! Wait!"
    hide lady_narisha
    hide lady_bargore
    with easeoutright
    "The women chased after her obediently."
    show mc at blurin, center with ease
    MC @talk "(... I fucking hate tea parties.)"
    MC "(I guess there's nothing left to do now but wait.)"
    $ QstSetProgress(QstTheTarbecks2, 21)
    $ QstSetDelay(QstTheTarbecks2, 1)
    $ LocEnter()
#############################################################################################################################################
#SCENE 19
label qst_TheTarbecks2_guard_approach_again:
    show mc at cleft with easeinleft
    show cg_guard_hamun at cright_f with easeinright
    GUARD "You there!"
    GUARD "Lady Tarbeck requests your presence at once!"
    GUARD "She wants me to relay to you that Lady Belamore and the others wish to negotiate terms!"
    show cg_guard_hamun at blurin, cright
    hide cg_guard_hamun with easeoutright
    show mc at center with ease
    MC @surprised "Finally."
    MC @talk "(We can put an end to this madness.)"
    MC "(I should head straight to the Tarbeck Manor at once.)"
    $ QstSetProgress(QstTheTarbecks2, 22)
    $ LocEnter()

###############################################################################################################################################
#SCENE 20
#The player returns to the Tarbeck estate to find Lady Belamore and the others already there, looking dishevelled as Lady Tarbeck smiles smugly
label qst_TheTarbecks2_return_to_manor_once_more_once_more:
    show lady_tarbeck at cright_f
    show lady_narisha at center
    show lady_belamore at cleft
    with dissolve
    show mc at left with easeinleft
    LADY_TARBECK @happy "Look who just arrived, ladies."
    "The women stared, practically drooling, as Lady Belamore, cheeks burning red, barely managed to compose herself."
    LADY_NARISHA @shock "L-Lady Belamore is like us and-"
    LADY_BELAMORE @angry "SHUT UP! SHUT UP! SHUT UP!"
    LADY_BELAMORE @angry "I'm not like either of you! {i}Huff{/i}"
    LADY_BELAMORE @angry "This is... {i}Huff{/i} MY choice!"
    "Her gaze turned back to Lady Tarbeck."
    LADY_BELAMORE @emb "What do you - {i}Huff{/i} want?"
    LADY_TARBECK @talk "My husband."
    LADY_TARBECK @talk "I want him back and alive."
    LADY_BELAMORE @angry "{i}Huff{/i} And in return what?"
    LADY_TARBECK @happy "I'll give you the cure."
    LADY_BELAMORE @angry "{i}Huff{/i} Fuck... {i}Huff{/i} You..."
    LADY_TARBECK @angry "Then go fuck yourself."
    LADY_BELAMORE @angry "I want - {i}Huff{/i} the original deal..."
    LADY_TARBECK @shock "... Are you mad?"
    LADY_TARBECK @angry "Why in the hells would I trust you?"
    LADY_TARBECK @angry "You've already proven you never intended to keep to it the first time around."
    LADY_BELAMORE @angry "Circumstances - {i}Huff{/i} have fucking changed..."
    LADY_TARBECK @happy "Right, and what's to stop you just trying to slit my throat again after you have what you want?"
    "Lady Belamore motioned for one of her guards to step forward, carefully handing over a document to Lady Tarbeck."
    LADY_BELAMORE @sad "{i}Huff{/i} My husband has already signed..."
    LADY_BELAMORE @sad "The deal is being ratified by - {i}Huff{/i} the Alderian Royal Bank."
    LADY_BELAMORE @sad "All legitimate... all - {i}Huff{/i}"
    LADY_BELAMORE @sad "Binding outside of Hamun."
    LADY_TARBECK @talk "... Hmm."
    LADY_TARBECK @angry "I'll need to have this confirmed, of course."
    LADY_TARBECK @think "But why... Why demand this now?"
    LADY_BELAMORE @sad "Because - {i}Huff{/i} Need something to show for all this..."
    LADY_BELAMORE @angry "Fuck - {i}Huff{/i} walking away with nothing!"
    LADY_TARBECK @talk "... Understandable."
    LADY_TARBECK @angry "But first, my husband's location."
    LADY_BELAMORE @angry "Grrhh... F-Fuck...!"
    LADY_BELAMORE @angry "How do {i}I{/i} know you won't turn the knife on me if I give his location?"
    "Lady Belamore winced, wiping the sweat from her brow."
    LADY_TARBECK @happy "That's the thing about trust, isn't it?"
    LADY_TARBECK @angry "{i}Sometimes you just have to presume the other person has integrity... Even if you don't.{/i}"
    "Lady Belamore didn't answer for a few moments. She just stared ahead, flushed as she tried to think of an answer."
    "Finally, she closed her eyes and nodded."
    LADY_BELAMORE @sad "Alright... {i}Huff{/i} We have a deal."
    LADY_TARBECK @shock "Where is he? Where is my husband?"
    LADY_BELAMORE @sad "The sewers."
    LADY_TARBECK @shock "What?"
    LADY_BELAMORE @sad "Beneath the castle... {i}Huff{/i}"
    LADY_BELAMORE @sad "I don't know more than that."
    "Lady Belamore offered up one last grin."
    LADY_BELAMORE @smile "Better hurry though..."
    LADY_BELAMORE @smile "{i}In case Hugo gets too hungry.{/i}"
    LADY_TARBECK @angry "YOU SWORE-!"
    LADY_BELAMORE @angry "I can't fucking control what happens where I'm not at, you crazy bitch!"
    LADY_BELAMORE @angry "Hugo is my husband's pet freak!"
    LADY_BELAMORE @angry "He put him down there to watch your husband, not me!"
    LADY_TARBECK @angry "GRGHH!"
    "Lady Tarbeck turned towards me."
    LADY_TARBECK @talk "Find him. Find my husband."
    MC @talk "Give me a piece of his clothing."
    LADY_TARBECK @think "What?"
    MC @talk "I'll be able to track his scent better down there."
    LADY_BELAMORE @sad "Oh gods... {i}Huff{/i}"
    LADY_BELAMORE @sad "We've been fucking a dog, it seems."
    "I glared at the comment before turning my attention back towards Lady Tarbeck."
    "From her pocket, she produced a small handkerchief."
    LADY_TARBECK @talk "Will this do?"
    "Grabbing the cloth, I began to take in the scent, doing my best not to wretch and hide it from Lady Tarbeck."
    MC @sad "Y-Yes... I'll be on my way."
    LADY_TARBECK @think "... Are you alright?"
    MC @sad "{i}Cough!{/i} Fine, fine!"
    hide mc with dissolve
    #MC exits off screen
    LADY_TARBECK @talk "(... Well, that was a strange reaction.)"
    LADY_TARBECK @sad "(Please... Bring my husband back though.)"
    LADY_BELAMORE @angry "One last thing, Lady Tarbeck."
    LADY_BELAMORE @smile "If you ever mention to our husbands our little 'dalliances'..."
    LADY_BELAMORE @angry "{i}I'll fucking kill you.{/i}"
    LADY_TARBECK @angry "Many have tried... bitch."
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show mc at cright_f with easeinright
    MC "(She said beneath the castle.)"
    MC "(There must be an entrance to the sewer works around there somewhere.)"
    $ QstSetProgress(QstTheTarbecks2, 23)
    $ LocEnter()

#Clickable icon appears in the rich/merchant district with the castle 'head to the sewers'
#Cut to sewers
label qst_TheTarbecks2_to_sewers:
    scene black with dissolve
    $ AutoAmb(False)
    $ PlayAmbience("audio/ambience_loc/prison.ogg", 1)
    "Following the scent, I made my way down towards the sewers."
    if IsDaytime():
        scene bg_hamun_sewers
    else:
        scene bg_hamun_sewers_night
    with dissolve
    "They were different than the ones in Novaras."
    "An open-air labyrinth beneath the city, with ladders and multiple passageways."
    "It seemed even more sophisticated, and as I stepped down onto the lower level, I began to walk along it, looking to pick up the scent."
    show mc at cleft with easeinleft
    MC "(Still nothing.)"
    SHYAHTAN "(He is here.)"
    MC @think "(How can you tell?)"
    SHYAHTAN "(Look closer.)"
    "Looking around, I spotted it."
    "What looked to be a torn bit of fabric caught on some jagged bit of metal."
    "{i}Expensive cloth.{/i}"
    "I carefully removed it and smelled it."
    MC "(It's him.)"
    "With a fresh scent, I made my way forward."
    MC "(He's not far from here...)"
    scene black with dissolve
    #Brief fade to black - cut to inner sewers
    scene bg_hamun_sewers_holding
    show cg_bandit at left
    show cg_bandit2 at right_f
    with dissolve
    BANDIT_DUMB "How much longer do we have to keep him here?"
    BANDIT "Till the boss says otherwise."
    BANDIT_DUMB "How long's that then?"
    BANDIT "Would you shut your fucking mouth already?"
    TARBECK "Please... Release me."
    TARBECK "I will pay you far greater coin than-"
    BANDIT "You shut that fat mouth of yours too."
    BANDIT "Otherwise I'll be cutting that tongue out of-"
    $ PlaySound(audio.door_kick_open)
    show mc at center with dissolve
    BANDIT_DUMB "What the fuck is that?"
    MC @smile "Ah, wonderful."
    MC @talk "Hand over Lord Tarbeck."
    "The men drew their blades."
    BANDIT "Who the fuck are you?!"
    menu:
        "{image=[ICON.SWORDS]} Death.":
            BANDIT_DUMB "K-Kill him! Kill this fool!"
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")

            if IsDaytime():
                $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_sewers_day", CharIDList_Right = [{"e_bandit":11}, {"e_bandit":12}, {"e_bandit":13}, {"e_bandit":13}]))
            else:
                $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_sewers_night", CharIDList_Right = [{"e_bandit":11}, {"e_bandit":12}, {"e_bandit":13}, {"e_bandit":13}]))

            scene bg_hamun_sewers_holding
            with dissolve
            show mc at cleft with dissolve
            "As the last of them collapsed into a bloody heap on the floor, I wiped the blood from my blade."
            $ AutoMus(True)
        "Leave this place, and I'll let you live." (Req_Charm = 14):
            BANDIT_DUMB "..."
            hide cg_bandit
            hide cg_bandit2
            with dissolve
            "The men shared a knowing look, and dropping their blades to the floor, chose to quickly run past me."
            show mc at cleft with ease
            MC @smile "Well that was easy."
        "Look, your pay is probably terrible. Why don't I just give you some coin and you walk away and pretend we never met, hmm?" (Req_Barter = 9, Req_Gold = 500):
            "The men stared at each other for a moment, and then nodded. Dropping their blades as they took the coin before fleeing."
            hide cg_bandit
            hide cg_bandit2
            with dissolve
            show mc at cleft with ease
            MC @smile "Nice and simple."
        "I'm going to see what happens if I sew your severed heads together and see if a dark mage can bring you back." (Req_Perk = "terrifying"): #Terrifying perk
            "In sheer pale-white terror, the men turned and ran for their lives screaming."
            hide cg_bandit
            hide cg_bandit2
            with dissolve
            show mc at cleft with ease

    show lord_tarbeck at cright_f with easeinright
    "Unshackling the battered Lord Tarbeck, he looked up pitifully towards me."
    TARBECK @sad "You... You are the one who-"
    MC @talk "Let's get you home, Lord Tarbeck."
    "He could only nod weakly as I began to escort him back."
    scene black with dissolve
    if IsDaytime():
        scene bg_hamun_sewers with dissolve
    else:
        scene bg_hamun_sewers_night with dissolve
    play sound "audio/cfx/hugo_roar.ogg"
    "{i}ROARRRRR{/i}"
    "As I turned, there stood, blocking my path, half a dozen guards holding back a great beast by chains."
    show mc at cleft with dissolve
    show cg_hugo at cright_f with dissolve
    TARBECK @scared "By the gods... What is that thing?!"
    MC @surprised "{i}Hugo.{/i}"
    TARBECK @scared "WHO THE FUCK IS HUGO?!"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    "Letting loose the chains, the beast came hurtling forward!"
    if IsDaytime():
        $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_sewers_day", CharIDList_Right = [{"e_hugo":15}, {"e_bandit":11}, {"e_bandit":11}, {"e_bandit":11}]))
    else:
        $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_sewers_night", CharIDList_Right = [{"e_hugo":15}, {"e_bandit":11}, {"e_bandit":11}, {"e_bandit":11}]))

    if IsDaytime():
        scene bg_hamun_sewers with dissolve
    else:
        scene bg_hamun_sewers_night with dissolve
    $ AutoMus(True)

    #play sound "audio/cfx/hugo_death.ogg"
    "Choking on its blood, the creature tumbled backwards,"
    "slamming hard onto the floor with a thunderous clap as it twitched for a few moments before falling still and silent."
    show mc at cright_f
    show markus at cleft
    with dissolve
    MC @angry "{i}Huff{/i} What was that thing?"
    MARKUS @think "My first guess is some kind of experiment."
    MARKUS @think "Maybe Lady Belamore's husband was trying to create... some kind of super warrior?"
    MC @think "What was your second guess?"
    MARKUS @smile "My last lover."
    MARKUS @smile "I heard things have gone terribly downhill for her since we parted."
    MC @laugh "For fuck's sake, man."
    "I couldn't help but laugh."
    show lord_tarbeck at right_f with easeinright
    TARBECK @sad "Umm... If you don't mind."
    TARBECK @sad "I would very much like to go home now..."
    MC @talk "Of course, Lord Tarbeck."
    scene black with dissolve
    $ AutoAmb(True)
    ######################################################################################################################################################################
    #Fade to black
    $ TimeAdvBy(TIME_1H)
    "A long journey across the city back to the Tarbeck manor later..."
    $ LocSet("hamun_tarbeck_mainhall")
    $ LocFlush()
    with dissolve
    show lord_tarbeck at center with easeinleft
    show lady_tarbeck cry at right_f with easeinright
    show lady_tarbeck cry at cright_f with ease
    LADY_TARBECK "DARLING!"
    show mc at left with easeinleft
    "She rushed towards Lord Tarbeck, embracing him tightly as he groaned painfully."
    TARBECK @talk "Ahh! E-Easy my love... Easy!"
    TARBECK @talk "These wounds of mine are quite tender."
    LADY_TARBECK "You damn fool..."
    LADY_TARBECK "You had me worried."
    LADY_TARBECK "Why did you not bring the extra guards like I asked?!"
    TARBECK @smile "Oh gods, must we do this now?"
    LADY_TARBECK "Y-Yes! They managed to... to...!"
    TARBECK @smile "My love, it's alright."
    TARBECK @talk "I am alright."
    LADY_TARBECK "... Don't ever go without guards again."
    show lord_tarbeck at blurin, center_f
    "Lord Tarbeck sighed as he turned towards me."
    TARBECK @talk "Thank you, for all you have done."
    TARBECK @talk "I will do as you ask. I will tell The Greater Trading Company that I will not stand in the way of the weapons deal."
    MC @think "Just like that."
    TARBECK @smile "Yes... Just like that."
    "Lord Tarbeck wiped the tears from his wife's eyes."
    show lady_tarbeck
    TARBECK @talk "Now then, did the two of you-"
    LADY_TARBECK @shock "No!"
    LADY_TARBECK @blush2 "I am married to you, I would never betray my vows like that!"
    "Lord Tarbeck looked towards me."
    MC @talk "It is true, your grace, your wife resisted my every advance."
    "Lord Tarbeck sighed, gently caressing his wife's cheek."
    TARBECK @talk "My dear, I've never doubted your loyalty or love for me for a moment."
    LADY_TARBECK @happy "Good, then you won't ask-"
    TARBECK @smile "It is very obvious to me that you like him."
    LADY_TARBECK @shock "W-Wha-?!"
    LADY_TARBECK @blush2 "N-No."
    TARBECK @smile "My love, it's quite alright."
    LADY_TARBECK @blush2 "But we-"
    TARBECK @talk "We need to face the truth, my love."
    TARBECK @talk "I am not... an ordinary man."
    TARBECK @talk "We both know the scale of my affairs and my depravity."
    TARBECK @sad "But it saddens me that this whole time, I continued to indulge who I was while hurting you."
    LADY_TARBECK @sad "But..."
    TARBECK @talk "You still have my blessing to see him, if you wish."
    LADY_TARBECK @shock "...!"
    TARBECK @smile "My love... I promise from now on I won't dishonor you the way I have."
    TARBECK @smile "You will be the jewel of my eye in all things."
    TARBECK @smile "... But you deserve to be happy too, no?"
    LADY_TARBECK @blush "I... I am happy."
    TARBECK @smile "No, my love."
    TARBECK @smile "You are not."
    TARBECK @smile "{i}... But it is alright for you to be happy.{/i}"
    "Lady Tarbeck seemed to ponder the words for a moment before shaking her head."
    LADY_TARBECK @think "Lady Belamore and the others..."
    LADY_TARBECK @talk "Shall I summon them for you?"
    menu:
        "Yes... A deal is a deal.":
            pass
        "No, it won't kill them... Let them suffer.":
            TARBECK @smile "Ha! This might be the only time I'm happy to tell a bunch of women to get fucked and not actually see them get it!"
            LADY_TARBECK @talk "Later, we can discuss... what my husband proposed."
            LADY_TARBECK @talk "For now though, I'd like to be alone."
            MC @talk "As you wish, my lady." 
            LADY_TARBECK @talk "{i}*Sigh*{/i}"
            LADY_TARBECK @talk "We can talk about... other things later."
            LADY_TARBECK @talk "For now, I will let the ladies know their 'cure' is ready for them."
            LADY_TARBECK @talk "Go now... Let the GTC know they have their wish."
            jump qst_TheTarbecks2_post_sewers_over

    scene black with dissolve
    "... A short while later, Lady Belamore and the others gathered in the mansion."
    LADY_BELAMORE @talk "{i}*Huff*{/i} Well, you survived then."
    LADY_BELAMORE @sad "Good for you. Now give us the cure!"
    LADY_TARBECK @happy "If it wasn't obvious, the cure is that he takes you wretches to his bed again."
    "The women shared a strange look."
    LADY_BELAMORE @sad "Fine, whatever... Just end this suffering already!"
    TARBECK @smile "Hold now!"
    LADY_BELAMORE @angry "What?! We had a deal!"
    "Lord Tarbeck grinned mischievously."
    TARBECK @smile "I am all for him fucking the three of you."
    TARBECK @smile "{i}But I have the PERFECT solution for how he should fuck you all.{/i}"
    
    "The blood drained from their faces as Lord Tarbeck's grin widened..."
    label replay_trio_table_firsttime:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Each of the women lay strapped to the table in the form of a loose triangle."
    scene hamun_trio_table_firsttime_1 with dissolve
    $ Pause()

    "Lady Tarbeck and her husband sat amused, watching the women covered in delicacies."
    TARBECK "So glad you could join us this evening, [player_name]."
    "He grinned, looking at the squirming, restrained women on the table, Lady Belamore particularly snarling towards him."
    LADY_BELAMORE "We won't forgive this fucking humiliation!"
    TARBECK "A little humiliation is a fair price to pay for trying to kill me."
    "Lady Belamore scowled in response as Lady Narisha looked up towards me sheepishly."
    LADY_NARISHA "H-Hello..."
    LADY_NARISHA "P-Please, be gentle with me, my knight!"
    LADY_TARBECK "Did you hear that, [player_name]? You're her 'knight,' it seems. Fufu..."
    TARBECK "How are you enjoying the food, my love?"
    LADY_TARBECK "It's wonderful, darling."
    LADY_TARBECK "... But the show really holds the meal together."
    LADY_BELAMORE "Oh, for the love of-"
    "I said nothing as I placed my cock against the entrance to her tight womanhood, rubbing against the wet mound."
    LADY_NARISHA "Ahhhh..."
    LADY_BELAMORE "Narisha! Don't give any of them the satisfaction!"
    "Lady Narisha bit her lower lip, watching the cock teasingly glide back and forth, her heart racing as she imagined it fitting inside her."
    LADY_NARISHA "T-That's alright, umm... Lady Belamore."
    LADY_NARISHA "{i}*Heavy breathing*{/i}"
    LADY_NARISHA "I c-can endure the humiliation... Ahh! If it's... my knight!"
    LADY_BELAMORE "L-Lady Narisha! You can't be-"

    $ PlaySexFx(audio.kiara_tent_slow, 1)
    scene hamun_trio_table_firsttime_2 with dissolve
    $ Pause()

    "Pressing my cock into Lady Narisha's tight hole, she moaned happily as I began to fuck her eager hole."
    "Her eyes rolled back almost immediately as her tight hole squeezed desperately around me."
    LADY_NARISHA "Mmmfghh!"
    LADY_NARISHA "M-Mistress Belamore!"
    LADY_NARISHA "H-He's in me! He's in me!"
    LADY_BELAMORE "D-Don't give him the satisfaction of your moans!"
    "As my cock slid in and out of her, Lady Narisha watched, drunk on lust, as she bit down on her lower lip."
    LADY_NARISHA "B-But..."
    LADY_NARISHA "Ahh! I CAN FEEL HOW MUCH HE LOVES ME, MISTRESS! Mmmfghh!"

    scene hamun_trio_table_firsttime_3 with dissolve
    $ Pause()

    "I began to move faster, thrusting into Lady Narisha as she moaned happily."
    "As I fed her hungry hole my cock, I could feel her tightening around me as I sensed her drawing near already."
    "... Not that I cared."
    "For all their wretchedness, I would see these three ladies as my whores and nothing else."
    LADY_NARISHA "I'M CUMMING! I'M CUMMING!"

    $ PlaySexFx(audio.kiara_tent_finish)
    scene hamun_trio_table_firsttime_cum_1 
    with flash
    $ Pause()

    "Lady Narisha's pussy clasped around me as I filled her up. She quivered and shook, moaning desperately as I gave her the 'cure' she so desperately craved."

    scene hamun_trio_table_firsttime_4 with dissolve
    $ Pause()

    "Unsheathing my cock from her hole, I spun the table towards Lady Bargore, her legs spread and waiting."
    LADY_BARGORE "M-Me...?"
    LADY_BARGORE "Me next?"
    "I grunted in acknowledgement, rubbing my hard cock against her body."
    LADY_BARGORE "H-How are you still hard?"
    TARBECK "Our house champion is always hard! Hahaha!"
    LADY_TARBECK "Have fun, Lady Bargore."
    "Her eyes flickered over towards Lady Narisha, fucked out of her mind in blissful contentment."
    "I didn't answer her."

    $ PlaySexFx(audio.nijah_miss_1, 1)
    scene hamun_trio_table_firsttime_5 with dissolve
    $ Pause()

    "Pressing my cock into her hole, Lady Bargore didn't even pretend to hold back."
    "Like Lady Narisha, her hole squeezed tightly around me as her tongue rolled from her mouth, her face contorted with pleasure."
    LADY_BARGORE "Harder! HARDER, PLEASE!"
    LADY_BARGORE "I can't bear my husband's cock anymore!"
    LADY_BARGORE "Give it to me, give it to me harder!"

    scene hamun_trio_table_firsttime_6 with dissolve
    $ Pause()

    "I did as she asked, slamming my cock into the eager noble wife as she let me take her for all she was worth."
    "It was strangely amusing seeing just how ready she was to abandon all her pretences of wealth, even her own husband."
    "As she shook desperately against the restraints, all she seemed to care about was my cock."
    LADY_BARGORE "Y-YES! MORE! GIVE ME MORE!"
    "Lady Belamore watched silently, her hands desperately trying to slip between her legs as she watched the perverted scene before her."
    "Ignoring her, I continued to slam into Lady Bargore's hole until at last, I poured myself into her eager hole."

    $ PlaySexFx(audio.nijah_miss_finish)
    scene hamun_trio_table_firsttime_cum_2 
    with flash
    $ Pause()

    "Lady Bargore let out a quiet, whimpering gasp as she shuddered and squeezed around my cock."
    LADY_BARGORE "MMFGHHH...!"
    LADY_BARGORE "GODSSS YESSS!"

    scene hamun_trio_table_firsttime_7 with dissolve
    $ Pause()

    "As I unsheathed my cock once more from another freshly fucked hole, I spun the table once more."
    "Now, at last, I found myself confronted by the sight of Lady Belamore's ass spread on the table."
    "My cock, having already cum twice, hardened quickly at the sight of the petty bitch bent over and placed into such a degrading position."
    "Lady Tarbeck giggled at the sight."
    LADY_TARBECK "My, my... How the mighty have fallen."
    TARBECK "Fallen straight down, ass up, it seems."
    "The two laughed as Lady Belamore scowled at them, struggling against the restraints."
    LADY_BELAMORE "I'll fucking kill you both!"
    LADY_BELAMORE "I swear to you both! I'll-"
    "Feeling my heavy cock rub between her cheeks, Lady Belamore became very quiet."
    LADY_TARBECK "I much prefer you tied down and with a cock in your ass."
    LADY_BELAMORE "You-!"
    $ PlaySexFx(audio.forgean_075, 1)
    scene hamun_trio_table_firsttime_8 with dissolve
    $ Pause()

    "As my cock slipped into Lady Belamore, she could only gasp in surprise."
    "Her wet insides squeezed tightly around me as she reluctantly cooed and moaned."
    LADY_BELAMORE "Ahh! This is... Mhmm..."
    LADY_BELAMORE "So fucking undignified."
    TARBECK "From the way you shake your ass to match his thrusts, you seem to rather like things 'undignified,' Lady Belamore."
    LADY_BELAMORE "FUCK - Ahh!"
    LADY_BELAMORE "YOU! Mmmfgh!"
    TARBECK "He seems to have me covered there."
    "Lady Belamore continued to grunt and moan, the sounds of her fleshy ass clapping with each thrust quickly filling the room."
    "{i}Phap! Phap! Phap!{/i}"
    LADY_BELAMORE "AHHHH! You... You bastards! Mmfghh!"
    LADY_TARBECK "Just shut up and cum already, Lady Belamore."
    LADY_TARBECK "What's the point in holding onto pride right now?"
    LADY_TARBECK "You may as well admit you're enjoying yourself."
    LADY_TARBECK "{i}Everyone can see he's about to make you cum.{/i}"
    "I slammed hard against her ass."
    LADY_BELAMORE "Oh fuck! FUCK! FUCK! FUCK!"
    LADY_BELAMORE "S-Shut up! Shut THE FUCK UP!"
    LADY_BELAMORE "You think some HUGE cock is going to - Ahh! TAME ME?!"
    LADY_BELAMORE "I AM A BELAMORE! I WON'T... WON'T..."

    scene hamun_trio_table_firsttime_9 with dissolve
    $ Pause()

    "I continued to pound into her pussy."
    LADY_BELAMORE "Ooooh! YES! That's it!"
    LADY_BELAMORE "G-Give me the medicine! Oh gods...!"
    LADY_BELAMORE "Fuck me! FUCK ME BETTER THAN ALL OF THEM!"
    "As I continued to slam away, I began to feel Lady Belamore's body tighten and shake beneath me."
    LADY_BELAMORE "Y-Yes... YES!"
    LADY_BELAMORE "I'm so close! Just a little more!"
    LADY_BELAMORE "I'M-"

    $ ReduceInfectionFromSex("lady_belamore")
    $ PregRoll("lady_belamore")
    $ UnlockGalSceneAndGrantXp("hamun_trio", "table")

    $ PlaySexFx(audio.forgean_finish)
    scene hamun_trio_table_firsttime_cum_3 
    with flash
    $ Pause()
  
    LADY_BELAMORE "CUMMMM!"
    "She rocked her head back, her whole body trembling as I pumped her full of my seed."
    "As her eyes rolled back into her skull, eventually she slumped forward, my cock slipping out of her pussy, now pouring out the thick load."
    scene black with dissolve
    $ StopReplay()
    $ AutoMus(True)
    "Lord Tarbeck clapped happily."
    $ LocFlush()
    show lord_tarbeck at cright_f
    show lady_tarbeck at right_f
    show mc at left
    with dissolve
    TARBECK "An excellent performance! Don't you agree, dear?"
    LADY_TARBECK "Quite, dear... But she's made quite the mess of our table."
    LADY_BELAMORE "{i}Huff{/i} M-More... {i}Huff{/i}"
    LADY_BELAMORE "Mhoreee chockk phlease..."
    LADY_TARBECK "How scandalous!"
    LADY_TARBECK "If only your husband and the other wives could hear you now..."
    LADY_BELAMORE "Mhmmm..."
    TARBECK "This has been a delight!"
    TARBECK "Do let one of us know, [player_name], if you wish to summon them again for a good fuck!"
    TARBECK "The least they can do is be good whores and drain your balls after everything they put you through!"
    "Lady Tarbeck smiled smugly, swirling a half-drunk glass of wine."
    LADY_TARBECK "I agree, dear."
    LADY_TARBECK "For now, though, I think we had best get them cleaned up and sent on their way."
    LADY_TARBECK "Do come by soon, though... [player_name]."
    LADY_TARBECK "We have... Other things to discuss, after all."
    jump qst_TheTarbecks2_post_sewers_over

label qst_TheTarbecks2_post_sewers_over:
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ QstSetProgress(QstTheTarbecks2, 24)
    $ LocEnter()

##############################################################################################################################################################
# Garen is waiting at The Pale Dragon
label qst_TheTarbecks2_garen_at_bar:
    show garen at cright_f
    with dissolve
    show mc at cleft with easeinleft
    GAREN @smile "So then, I have heard of your triumph."
    GAREN @smile "Lord Tarbeck will no longer intervene in our goals."
    MC @serious "Are we done here at last?"
    MC @serious "I'm getting sick of this lapdog bullshit."
    GAREN @talk "Hmm... Almost."
    GAREN @smile "I will be in touch."
    MC @serious "By the fucking gods, how much more-"
    GAREN @talk "You will be going home."
    MC @surprised "What?"
    GAREN @smile "I will be in touch soon."
    GAREN @smile "The emperor has... an offer for you."
    hide garen with dissolve
    #Garen leaves
    show mc at center with ease
    MC @think "(An... offer?)"
    MC "(This could either be very good... or very, very bad.)"
    $ QstComplete(QstTheTarbecks2)
    $ LocEnter()
