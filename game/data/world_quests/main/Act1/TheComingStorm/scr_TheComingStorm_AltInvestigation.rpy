################################################################
#ALT INVESTIGATION ROUTE: - IF THE PLAYER HASN'T UNLOCKED CARINA ETC
#IF Player heads home 
label qst_thecomingstorm_alt_investigation_reginatalk:
    # REGINA @shock "Ahh, there you are!"
    # REGINA @angry "Where have you been?"
    # REGINA @angry "The city's about to be sieged! You should be-"
    # MC @serious "Where's Erika? I must speak with her at once!"
    REGINA @think "Erika?"
    "[regina_ref_cap!t] paused for a moment."
    REGINA @sad "She was here the other day, she seemed quite worried about something."
    REGINA @shock "{i}She's looking for you as well.{/i}"
    MC @talk "Did she say anything? Did she mention the name Poltrik or anything about missing traders?"
    REGINA @think "Poltrik? Missing traders?"
    REGINA @think "... I don't recall the name, {i}but I do recall her mentioning something about missing guardsmen if that's what you mean?{/i}"
    "I felt my heart sink into my stomach, Erika {i}was{/i} looking for Poltrik too!"
    REGINA @think "Does that have something to do with the siege?"
    MC @surprised "Where did Erika go? Did she say when she would return?"
    REGINA @talk "No... But now that you mention it."
    REGINA @talk "She was carrying this letter she said to give to you if she wasn't back in time."
    REGINA @talk "I haven't read it yet, but..."
    show regina at nod
    "[regina_ref_cap!t] held it out for me to take."
    "Reaching out, I grabbed the letter and read its contents quickly."
    play sound "audio/cfx/letter.ogg"
    "{i}New information continues to come to light linking Captain Nyx and [player_name!t].{/i}"
    "{i}We are at last close to having sufficient evidence for an arrest.{/i}"
    "{i}Inquisitor Saren requests a private audience with you regarding a possible link between your investigation and hers, regarding the missing guards.{/i}"
    "{i}Your contact with Inquisitor Saren is at the city library.{/i}"
    "{i}You will first need to retrieve the correct password.{/i}"
    "{i}Start with...{/i}"
    "{i}'Dreams of Astatar.'{/i}"
    "{i}The correct password is a name of the book for you to inquire about at the library.{/i}"
    # "{i}Head to the national library, the true password can be found in one of the books.{/i}"
    # "{i}The librarian will connect you with Inquisitor Saren if you tell her the true password.{/i}"
    # "{i}{/i}"
    
    MC "(What the...)"
    MC "(I'm being investigated alongside Captain Nyx?)"
    $ GoalComplete(QstTheComingStorm, 40)
    show mc at shake
    MC "(Fuck... This is the last thing I needed to deal with right now!)"
    REGINA @sad "Dear?"
    REGINA @sad "Is everything alright?"
    MC @serious "I have to go, I'll be back soon!"
    show mc at blurin, cright
    hide mc with easeoutright
    "I turned to leave, hurrying out as [regina_ref!t] called out behind me."
    REGINA @shock "Wait! Where are you going?!"
    show regina at center with ease
    REGINA @talk "{i}*Sigh*{/i}"
    REGINA @talk "{i}... Well... I suppose it is time soon anyway.{/i}"
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    $ LocFlush(dissolve)
    show mc at cright_f with easeinright
    MC @think "('Dreams of Astatar' must be a book name. I'll play your little game...)"
    $ GoalShow(QstTheComingStorm, 45)
    $ LocEnter()

label qst_thecomingstorm_alt_investigation_vala_ask_about_astatar:
    VALA @talk "Dreams of Astatar, huh?"
    "Vala raised an eyebrow."
    VALA @talk "We do have it, you should be able to find it upstairs."
    $ QstTheComingStorm().ValaInvestigationOpenedSpecialBookshelf = True
    $ LocEnter()

label qst_thecomingstorm_alt_investigation_vala_returnbooksonexit:
    show vala at center_f with dissolve
    VALA @talk "Hey, I don't think I saw you put these books back on the shelf?"
    MC @talk "Ah, right, of course..."
    $ tmpvar = 0
    if PlayerItemQty("book_dreams_of_astatar") > 0:
        $ PlayerRemItem("book_dreams_of_astatar")
        $ AddItemTo(bookshelf_comingstorm_special, "book_dreams_of_astatar")
        $ tmpvar += 1
    if PlayerItemQty("book_the_first_darkness") > 0:
        $ PlayerRemItem("book_the_first_darkness")
        $ AddItemTo(bookshelf_comingstorm_special, "book_the_first_darkness")
        $ tmpvar += 1
    if PlayerItemQty("book_loving_ophelia") > 0:
        $ PlayerRemItem("book_loving_ophelia")
        $ AddItemTo(bookshelf_comingstorm_special, "book_loving_ophelia")
        $ tmpvar += 1
    if tmpvar > 1:
        "After I handled the books to Vala she left towards the shelves."
    else:
        "After I handled the book to Vala she left towards the shelves."
    hide vala with dissolve
    scene black with dissolve
    $ LocSet("novaras_dist_edu")
    $ LocEnter()

label qst_thecomingstorm_alt_investigation_vala_password:
    VALA @smile "What book?"
    $ tmpvar = 0
    menu:
        "Our blades...":
            pass
        "Our souls...":
            pass
        "Our enemies...":
            pass
        "Our hands...":
            $ tmpvar += 1

    menu:
        "...Were unbroken...":
            pass
        "...Remain pure...":
            pass
        "...Were bloodied...":
            $ tmpvar += 1
        "...Were destroyed...":
            pass

    menu:
        "...So the kingdom might endure.":
            pass
        "...So thine could stay clean.":
            $ tmpvar += 1
        "...For the promise of the dawn.":
            pass
        "...So thy could remember our oath.":
            pass

    if tmpvar < 3:
        VALA @sad "Hmm... Sorry, doesn't ring any bells."
        return
    else:
        "In a moment, Vala's expression changed, as she seemed to almost turn pale white."
        show vala scared at center_f
        with dissolve
        VALA @scared "You... {i}You're the contact?{/i}"
        MC @think "What?"
        VALA @scared "I... I thought-"
        MC @serious "Vala, do you know where I can find Inquisitor Saren? I must speak with them."
        VALA @sad "Please... {i}You have to help me.{/i}"
        VALA @scared "{i}She's going to kill me!{/i}"
        MC @surprised "What?"
        MC @serious "What are you talking about?"
        VALA @scared "Inquisitor Saren contacted me about a month ago."
        VALA @scared "They discovered some of the contraband books I had managed to recover and threatened to arrest me on charges of consulting with dark magecraft!"
        MC @surprised "What books?"
        VALA @sad "A couple books surrounding blood magecraft rites and summoning rituals."
        VALA @embar "{i}...And maybe there was talk of a heresy charge involving a very graphic novel about Newheart being seduced by an oil covered muscle-bound orc.{/i}"
        MC @surprised "... Wait, what was that last part?"
        show vala at shake
        VALA @angry "It doesn't matter! A girl is allowed to fantasize, okay?"
        VALA @scared "Point is... they keep giving me {i}assignments.{/i}"
        VALA @sad "If I don't do as they ask, I'm as good as dead."
        MC @think "What do you need?"
        VALA @sad "I've been told to pick up a parcel..."
        VALA @scared "But I'm terrified, the people I'm supposed to be meeting..."
        VALA @scared "{i}I think they might try to hurt me.{/i}"
        MC @talk "Where to is this parcel?"
        VALA @sad "After dark, at the market. Will you help me?"
        MC @serious "Vala, I really need to know where I can find Inquisitor Saren... I-"
        VALA @angry "I'm sorry, but I'm not telling you anything unless you help me!"
        "Her voice began to break as she spoke..."
        VALA @sad "{i}... I don't wanna die, alright?{/i}"
        menu qst_thecomingstorm_alt_investigation_vala_password_parcel_menu:
            "I'll get your parcel.":
                VALA @cry "Ah! Thank you! Thank you! THANK YOU!"
                VALA @cry "I owe you my life!"
                VALA @cry "Please, let me know when you have it!"
                pass

            "What's in the parcel?":
                VALA @sad "I don't know..."
                VALA @sad "{b}They told me to absolutely make sure I didn't look inside though.{/b}"
                jump qst_thecomingstorm_alt_investigation_vala_password_parcel_menu

    $ GoalComplete(QstTheComingStorm, 45)
    $ GoalShow(QstTheComingStorm, 55)
    $ LocEnter()

#########################################
label qst_thecomingstorm_alt_investigation_enter_market_district:
    show mc at cright_f with easeinright
    MC "(It looks like someone is waving me over towards that alleyway...)"
    hide mc with easeoutleft
    "Heading toward the man, he motioned with his head as I followed him deeper into one of Novaras' many labyrinthine alleyways."
    scene bg_alleyway_night
    show cg_bandit as guard1 at center
    show cg_bandit as guard2 at left
    show cg_dark_mage at cleft
    with dissolve
    show mc at right_f with easeinright
    "Further into the darkness, I soon found myself facing a strange, robed figure holding a book, flanked by two masked guards."
    MARKUS @angry "{i}*Whispering*{/i} I don't like this..."
    MARKUS @angry "{i}*Whispering*{/i} I can smell the death on that dark mage from here!"
    if CharInParty("elena"):
        ELENA "*Bark!*"
    if CharInParty("myu"):
        MYU @think "... Myu?"
    DARK_MAGE "... Do you have it?"
    MC @think "What?"
    show cg_dark_mage at shake
    DARK_MAGE "Don't lie to me! The black ravens told me YOU would be bringing it!"
    MC @angry "What are you talking about? I was sent to pick up some kind of parcel!"
    "The robed figure looked around in a nervous panic."
    DARK_MAGE "Is this some kind of trick?"
    MC @angry "Do you have the parcel or not?"
    DARK_MAGE "Of course I do! But you were supposed to bring the head!"
    MC @think "... {i}The head?{/i}"
    show cg_dark_mage at shake
    DARK_MAGE "YES, HER FUCKING HEAD, DAMN IT!"
    MC @angry "I have no idea what you're-"
    play sound "audio/cfx/arrow_flyby_hit_1.ogg"
    "A single stray arrow shot toward the guards."
    show mc at blurin, right
    "I turned to look where it had come from, but in the darkness it was impossible to tell."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    show cg_dark_mage at shake
    DARK_MAGE "TRAITORS!"
    show mc at blurin, right_f
    DARK_MAGE "WE'VE BEEN BETRAYED! HE'S HERE TO KILL US!"
    MC @angry "Fuck!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys_night", CharIDList_Right = [{"e_thug":7}, {"e_thug":6}, {"e_bandit":5}], CanTransform = False))

    scene bg_alleyway_night
    show cg_dark_mage at cleft
    show mc at cright_f
    with dissolve
    $ AutoMus(True)
    "As the last of the guards collapsed, dead on the floor, the cowering robed man backed away desperately."
    show cg_dark_mage at left with ease
    DARK_MAGE "Please! I'll give you whatever you want! Just don't-"
    
    play sound "audio/cfx/arrow_flyby_hit_2.ogg"
    $ Pause(0.3)
    play sound2 "audio/cfx/hit_blood_moan.ogg"
    hide cg_dark_mage
    show cg_dark_mage_arrow at shake
    with dissolve
    "Another stray arrow fired, this one piercing straight through his eye with a terrible *thud*."
    "He stumbled backward for a moment, shaky hands reaching for the arrow before falling flat onto his back."
    hide cg_dark_mage_arrow with dissolve
    show mc at blurin, cright
    "A small pool of blood began to form around him as I looked around frantically for the shooter."
    show mc at blurin, cright_f
    $ Pause(0.15)
    show mc at cleft_f with ease
    "Heart racing, I scrambled to pry the {i}'parcel'{/i} from the man's still-warm, dead hands."
    show mc at nod
    play sound "audio/cfx/arrow_flyby_hit_3.ogg"
    "As I reached out to grab the parcel, another arrow struck it, this one with a rope attached."
    "I yanked my hand back just in time as the rope retracted, yanking the parcel up toward a rooftop."
    scene cg_assassin_rooftop with dissolve
    MC @angry "(Shit!)"
    MC @angry "(I can't let them get away!)"
    scene bg_alleyway_night
    show mc at cleft
    with dissolve
    $ Pause(0.2)
    hide mc with easeoutright
    "Chasing after the elusive figure, I bolted toward the street, looking up to follow them as they ran along the rooftops."
    $ LocSet("novaras_market_stalls")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    "Finally out of the alleyways and into the main market, I looked around frantically for the assassin."
    MC @angry "(Damn it! Where did he go?!)"
    show markus at left with easeinleft
    MARKUS @angry "He went right! Come on!"
    hide markus with easeoutright
    "I snapped my head to the right, catching a glimpse of him sprinting across the lower rooftops toward the brothel district."
    MC @angry "(Fuck!)"
    hide mc with easeoutright
    scene black with dissolve

    # The player heads toward the brothel district.
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    "Scanning the streets for the assassin, I found no sign of him."
    "A few patrons still loitered, seeking whorehouses still open."
    MC @surprised "(Where did he go?)"
    "My eyes swept along the rooftops."
    "A sudden prickle crawled down my arm."
    play sound "audio/cfx/arrow_flyby_hit_1.ogg"
    show mc at nod
    "I heard the faintest *swish* of an arrow and dodged just in time."
    "As it landed at my feet, I saw the assassin turn heel and flee once more."
    MC @angry "STOP, DAMN YOU!"
    hide mc with easeoutright
    scene black with dissolve
    # Cuts to castle district
    $ LocSet("novaras_dist_centre")
    $ LocFlush()
    show mc at center
    with dissolve
    "I found myself in the wide, open streets of the royal court district."
    "Crowds moved through the area, many stopping to gawk at the majestic castle as I shoved and forced my way through them, chasing the deadly thief."
    "Getting close, I reached out to grab his hood, but he swept a man's legs out, sending the bystander crashing into me."
    show mc at cleft with ease
    show cg_bandit at cright_f with dissolve
    BANDIT "Watch where you're going!"
    MC @angry "I don't have time for this!"
    "The figure shoved me back slightly."
    show cg_bandit at shake
    BANDIT "You're not going anywhere."
    "A small group of his friends gathered, catching the attention of nearby guards watching the scene unfold."
    show cg_bandit as bandit2 at left with easeinleft
    show cg_bandit as bandit3 at right_f with easeinright
    #
    if CharInParty("elena"):
        ELENA "{i}*Growls*{/i}"
        show cg_bandit at shake
        BANDIT "Keep that mutt on a leash before I do it for you!"
    #
    MC @angry "(Fuck, I don't have time for this!)"
    menu:
        "Throw some coin into the air to distract everyone!" (Req_Gold = 50):
            play sound "audio/cfx/handful_of_coin_thrown.ogg"
            $ QstTheComingStorm().ValaInvestigationDistractedBanditsDuringChase = True
            $ PlayerRemItem("gold", 50)
            show mc at nod
            "Reaching into my bag, I tossed coins into the air."
            "As they hit the floor with a metallic jingle, the crowd stopped to scramble for them."
            hide bandit2 with dissolve
            hide cg_bandit with dissolve
            hide bandit3 with dissolve
            "Now free, I took off after the assassin again."
            hide mc with easeoutright
            "He had gained distance and was headed toward the poor district."
            pass

        "Barge past the men!":
            hide mc with easeoutright
            "Shoving through the men, I resumed the chase."
            "The assassin had gained some distance and was now headed toward the poor district."
            pass

    scene black with dissolve
    $ LocSet("novaras_dist_house")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    "I rushed into the poor housing district."
    show mc at center with ease
    $ Pause(0.2)
    "My eyes darted around for any sign of the assassin, but he had vanished like smoke."
    show mc at blurin, center_f
    "This district was a maze of winding alleyways and tight corridors... He could be anywhere."
    show mc at blurin, center
    $ Pause(0.2)
    if not QstTheComingStorm().ValaInvestigationDistractedBanditsDuringChase:    
        show cg_bandit at left with easeinleft
        BANDIT "Where do you think you're going?"
        show mc at blurin, center_f
        MC @angry "... Fuck."
        $ AutoMus(False)
        $ PlayMusicRandom("mus_battle_generic")
        
        play sound "audio/cfx/whistle_call_1.ogg"
        show cg_bandit as bandit2 at right_f with easeinright
        BANDIT "Cut him, boys!"

        $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys_night", CharIDList_Right = [{"e_bandit":4}, {"e_bandit":5}, {"e_bandit":5}], CanTransform = False))

        $ LocFlush()
        show mc at center_f
        with dissolve
        "With the last of them slain, I sighed and sheathed my blade."
        $ AutoMus(True)
        show mc at blurin, center
        MC @talk "Now, where in the hells did that-"

    show cg_assassin_mc at center with flash
    "I suddenly felt the sharp point of a dagger press against my neck."
    ASSASSIN "...Don't move."
    MARKUS @angry "[player_name!t]!"
    #
    if CharInParty("elena"):
        "Elena snarled, circling me with eyes locked onto the assassin."
    if CharInParty("myu"):
        MYU @angry "Hurt friend..."
        MYU_RED @angry "{i}And Myu will devour you.{/i}" 
    #
    MC @talk "You're making a terrible mistake."
    ASSASSIN "Who sent you after me?"
    MC @think "{i}After you?{/i}"
    ASSASSIN "Don't play stupid with me!"
    ASSASSIN "Did that {i}bitch{/i} send you?"
    MC @talk "I'm here for the parcel. Nothing else."
    ASSASSIN "DON'T LIE TO ME!"
    MC @serious "Where's the parcel?"
    ASSASSIN "Somewhere safe. Somewhere you won't find it unless you do what I say."
    MC @angry "What do you want?"
    ASSASSIN "Three days from now, the whore district."
    ASSASSIN "Outside the {i}Weeping Heart{/i} Bordello. You know it?"
    MC @angry "Yeah, I know it."
    ASSASSIN "There's a loose red brick in the wall across from it."
    ASSASSIN "Leave a thousand coins in a bag behind it."
    ASSASSIN "You'll get your damn package then."
    MC @angry "How will I receive the parcel? And how do I know you won't double-cross me?"
    ASSASSIN "Well, you're just going to have to trust me, aren't you?"
    "The blade pulled away from my neck."
    hide cg_assassin_mc
    show cg_assassin at cleft
    show mc at center
    with dissolve
    $ Pause(0.2)
    show mc at blurin, center_f
    play sound "audio/cfx/smoke_bomb.ogg"
    show cg_assassin at shake
    hide cg_assassin with dissolve
    "As I spun, reaching for my weapon, the assassin dropped a small bag onto the ground and it exploded in a thick smoke cloud."
    show mc at cleft_f with ease
    "I reached into the smoke to try and grab him, but he had already vanished."
    $ GoalComplete(QstTheComingStorm, 55)
    MC @serious "... A thousand coins."
    $ GoalShow(QstTheComingStorm, 65)
    $ Pause(0.25)
    show mc at blurin, cleft
    MC @talk "This is getting more and more interesting..."
    show markus at cright_f with easeinright
    MARKUS @think "Just what in the hells is in this damn package?"
    MARKUS @talk "What kind of librarian is involved in something like this?"
    MC @angry "I don't know... but there's going to be a lot of questions when we finally hand over this damned parcel."
    MC @angry "That, I can assure you."
    $ LocEnter()

##################
label qst_thecomingstorm_alt_investigation_stash_gold_next_night:
    show mc at cleft with easeinleft
    MC "(That's the spot.)"
    MC "(It's too early to stash the money though, {i}for what I have in mind{/i}.)"
    MC "(I must wait for another night.)"
    $ LocEnter()

##################
label qst_thecomingstorm_alt_investigation_stash_gold:
    show mc at cleft with easeinleft
    MC "(This is where he said to hide the coin... Should I?)"
    menu:
        "Hide the coin behind the brick." (Req_Gold = 1000):
            show mc at cright with ease
            $ PlayerRemItem("gold", 1000)
            show mc at nod
            $ Pause(0.2)
            "Placing the money behind the stone, I looked around cautiously for anyone who might be watching."
            "Carefully, I placed the coin into the gap and covered it back up with the brick."
            show mc at center with ease
            MC @serious "(There's no way in the seven hells I'm just going to trust that thief.)"
            MC @serious "(I'll keep from a distance and watch... )"
            pass
        "Not now.":
            $ LocEnter()

    scene black with dissolve
    $ TimeAdvBy(TIME_1H)
    "As I watched and waited... and waited... {i}and waited.{/i}"
    $ TimeAdvBy(TIME_1H)
    "Nothing seemed to come of it."
    $ LocFlush(dissolve)
    show messenger at cright_f with easeinright
    "Until finally, a small boy came hurrying down the lane, carefully looking from left to right as he removed the red brick."
    show messenger at nod
    "Taking the coins from behind it, he placed the red brick carefully back before hurrying off."
    show messenger at blurin, cright
    $ Pause(0.15)
    hide messenger with easeoutright
    "I tailed the boy, who kept looking out for anyone who might be watching him."
    show mc:
        xalign 0.0
        xoffset -500
        ease 2.5 xalign 1.25 xoffset 500
    scene black with dissolve
    "At last, for what felt like forever of him looping through alleyways and back-routes, I found him handing over the bag of coins to the assassin."
    scene bg_alleyway_night
    show cg_assassin at cright
    show messenger at right_f
    with dissolve

    show messenger at nod
    $ Pause(0.2)
    show mc at left with easeinleft
    show messenger at blurin, right
    $ Pause(0.1)
    hide messenger with easeoutright

    show cg_assassin at blurin, cright_f
    show mc at cleft with easeinleft

    MC @angry "Where is it?"
    ASSASSIN "Hmm..."
    ASSASSIN "{i}I knew you would come.{/i}"
    show mc at shake
    MC @angry "Where's the damn parcel?"
    MC @angry "We had a deal."
    ASSASSIN "Sorry... The deal's changed."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ GoalComplete(QstTheComingStorm, 65)
    ASSASSIN "{i}*She* wants there to be no witnesses.{/i}"
    play sound "audio/cfx/whistle_call_2.ogg"
    #show cg_bandit at left with dissolve
    show cg_bandit as bandit2 at right_f with dissolve
    "From every corner, masked men bearing daggers and blades appeared to surround us."
    $ GoalShow(QstTheComingStorm, 75)
    ASSASSIN "Your journey ends here."
    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys_night", CharIDList_Right = [{"e_thug":7}, {"e_assassin":6}, {"e_bandit":6}], CanTransform = False))
    scene bg_alleyway_night
    show mc at cleft
    show cg_assassin at cright_f
    with dissolve
    "Clutching at his bloody wound, the last one still standing, the assassin's breath trembled as he shakily raised his blade towards us."
    ASSASSIN "You..."
    ASSASSIN "{i}What in the hells are you?{/i}"
    $ AutoMus(True)
    MC @angry "The parcel... Hand it over."
    show cg_assassin at nod
    "With a shaky hand, the assassin reached into his cloak and tossed the parcel towards me."
    ASSASSIN "Take it... Take it and-"
    show cg_assassin at shake
    "The assassin clutched at his wound, his voice trembling as he spoke."
    ASSASSIN "I... I see now."
    ASSASSIN "Ha...Hahahahaha!"
    MC @think "Have you lost your mind?"
    ASSASSIN "Don't you get it, idiot?"
    ASSASSIN "This was all part of her plan, I can see that now."
    ASSASSIN "{i}I{/i} was the target all-"
    "The assassin dropped to his knees."
    MC @serious "What's wrong with you?"
    ASSASSIN "I felt... {i}*huff*{/i} weaker during the fight."
    ASSASSIN "That... {i}*Huff*{/i} bitch..."
    ASSASSIN "The tea... The fucking-"
    hide cg_assassin with easeoutbottom
    play sound "audio/cfx/body_collapse.ogg"
    "Wretched and gagging, unable to breath, he slammed face first onto the stone cobbled floor."
    "After a few agonizing moments, he lay silent and motionless."
    $ GoalComplete(QstTheComingStorm, 75)
    show markus at left with easeinleft
    MARKUS @talk "... What the fuck is going on?"
    show mc at center with ease
    $ PlayerAddItem("qst_vala_parcel")
    $ PlayerAddItem("gold", 1000)
    MC @angry "I don't know."
    show mc at blurin, center_f
    MC @angry "But I'm going to get some damn answers!"
    $ GoalShow(QstTheComingStorm, 85)
    $ LocEnter()

##############################################
#Player upon returning to the library - scene autoplays
label qst_thecomingstorm_alt_investigation_return_with_parcel:
    show mc at cleft with easeinleft
    "The library was unusually empty as I came storming inside."
    MC @angry "Vala!"
    show mc at center with ease
    $ Pause(0.1)
    show mc at shake
    MC @angry "VALA!"
    show vala at right_f with easeinright
    "The librarian came calmly, a soft smile on her face as her eyes narrowed onto me."
    VALA @talk "I trust you got the parcel?"
    show mc at shake
    MC @angry "What in the hells was that whole thing?"
    show mc at cleft with ease
    show vala at cright_f with ease
    VALA @smile "Oooh, sorry."
    VALA @talk "You did a great job though!"
    VALA @smile "Now with both that dark mage dead along with that wretched assassin, I'd say a good day's work done all in all!"
    MC @surprised "{i}... What in the hells kind of librarian are you?{/i}"
    VALA @talk "{i}...Have you really not figured it out?{/i}"
    MC @serious "What are you-"
    MC @surprised "..."
    VALA @smile "{i}Inquisitor Saren, at your service.{/i}"
    show vala at nod
    "Vala, or rather, Saren, offered a curt bow."
    VALA @smile "Now please... hand over the parcel."
    MC @surprised "You... {i}You're the inquisitor?{/i}"
    MC @surprised "But I thought-"
    MC @surprised "The password was meant to {i}get{/i} me to Saren?!"
    VALA @smile "Right."
    VALA @talk "Now please, if you don't mind handing over the parcel..."
    MC @angry "What the fuck is in it?"
    VALA @talk "Just the works of another desperate, half-mad dark mage."
    VALA @smile "Thankfully one less problem for the rest of us."
    MC @serious "Why... Why have you done all this?!"
    MC @serious "Why not just tell me from the start!"
    VALA @think "I must admit, when {i}you{/i} gave the password instead of Inquisitor Erika, I was taken aback at first."
    VALA @smile "But, an opportunity wasted is one you can't get back."
    MC @serious "So that's all this was, you using me?"
    VALA @talk "Nothing personal..."
    VALA @smile "But I think I can help you."
    VALA @smile "You're looking for information on Poltrik and the other missing guards, right?"
    MC @think "You expect me to just hand the parcel over like that?"
    show mc at shake
    MC @serious "You could have got me and my friends killed!"
    VALA @shock "Oh please, I was confident in your abilities."
    VALA @smile "Besides, the poison already did most of the work for you."
    MC @think "Why not just tell me the truth?"
    VALA @talk "Call it a {i}test{/i} if you will."
    VALA @smile "One I'm glad to see you passed."
    VALA @talk "Now please, the parcel..."
    VALA @talk "We have far bigger issues to deal with, {i}don't we?{/i}"
    $ PlayerRemItem("qst_vala_parcel")
    show mc at nod
    $ GoalComplete(QstTheComingStorm, 85)
    VALA @smile "So... You have questions, feel free to ask."
    
    menu qst_thecomingstorm_alt_investigation_return_with_parcel_questions_menu:
        "Why go through all these loops if you just wanted me to kill them?":
            VALA @smile "Obfuscation is a weapon in itself."
            MC @think "What?"
            VALA @talk "Well, right now, if someone were to investigate what has happened, what would they find?"
            MC @serious "A lot of dead bodies?"
            VALA @smile "Have you ever heard of the black ravens guild?"
            VALA @smile "They are an underground order of assassins for hire, who share a unique alliance with many dark mages who use their services."
            VALA @talk "They are known for using {i}distinct{/i} black arrows with a red feather fletching to leave their mark."
            MC @think "Where are you going with this?"
            VALA @talk "A dark mage, one who was part of a sub-sect of old god worshipers, is seemingly murdered by an assassin from the black raven's guild, jeopardizing the alliance."
            VALA @smile "You see, as part of that alliance, it was agreed a dark mage could only be killed with the written consent of the black raven guild's leadership."
            VALA @talk "... Now, for that same assassin later to die by a mixture of poison and stab wounds, what is either side to think?"
            VALA @smile "The dark mages will presume that the assassin murdered the mage to steal the parcel and broke the alliance."
            VALA @smile "The black ravens guild will presume the assassin broke rank and was murdered in retaliation for the mage's slaying."
            VALA @think "Of course, both sides will deny any wrong-doing..."
            VALA @talk "But well..."
            VALA @smile "Once that forged letter I created giving the assassin the all-clear to murder the dark mage is conveniently uncovered, well..."
            "A dark grin appeared on Vala's face."
            VALA @smile "I think both sides will kill each other for us."
            VALA @smile "And the inquisition's hands get to stay completely clean."
            "A chill ran down my spine."
            MC @scared "You're..."
            VALA @smile "Any more questions?"
            jump qst_thecomingstorm_alt_investigation_return_with_parcel_questions_menu

        "Don't you have a uniform to wear?":
            VALA @talk "For official business, yes."
            VALA @talk "Though hardly anyone has ever seen me actually wear it."
            VALA @think "I'm just not that kind of inquisitor."
            VALA @talk "Some prefer to kick in doors and blah blah blah..."
            VALA @talk "Me?"
            VALA @talk "I'm far more comfortable in my library... gathering whispers and information as I go."
            jump qst_thecomingstorm_alt_investigation_return_with_parcel_questions_menu

        "So... Your real name is Saren?":
            VALA @talk "No."
            MC @think "...Then it's Vala?"
            VALA @talk "Also no."
            MC @think "Then what should I call—"
            VALA @smile "Vala will do just fine."
            jump qst_thecomingstorm_alt_investigation_return_with_parcel_questions_menu

        "Why are you helping me now? Aren't you helping Erika investigate me?":
            VALA @smile "You really think it's about {i}you{/i} I had information?"
            MC @think "What does that mean?"
            VALA @smile "Let's just say, {i}perhaps you should look a little closer to those around you more often.{/i}"
            MC @talk "Who—"
            VALA @talk "Sorry, my business is in information."
            VALA @talk "And that's not the information {i}you{/i} need to hear."
            MC @serious "That doesn't answer the first question."
            VALA @smile "Maybe because it's just more entertaining this way?"
            MC @surprised "...What kind of inquisitor are you?"
            VALA @talk "..."
            jump qst_thecomingstorm_alt_investigation_return_with_parcel_questions_menu

        "What do you know about Poltrik and his men then?":
            pass

    VALA @talk "Aside from the fact that he and his men have been trying to snatch people from the street and drag them off to who-knows-where?"
    MC @think "What? They're trying to kidnap people?"
    VALA @talk "Yes, to what purpose though, I don't know."
    VALA @talk "Though someone managed to knock off one of their helmets, and described the most ghastly, pale face imaginable beneath it."
    VALA @talk "A face literally {i}rotting.{/i}"
    MC @serious "...So, you think it's the work of dark magecraft then?"
    VALA @talk "Well, the others seem convinced it's so..."
    MC @think "But you're not convinced?"
    VALA @think "Not quite... But that doesn't matter right now."
    VALA @smile "{i}What matters is I know where Poltrik may be hiding...{/i}"
    MC @surprised "Where?"
    VALA @talk "Poltrik's family is of a notable minor noble house."
    VALA @talk "They have a few properties scattered around the place, but they have a relatively large estate in the southern-east district."
    VALA @talk "With lots of strange rumors circling about {i}strange{/i} noises that can be heard passing by it in the night."
    MC @serious "Where is this place?"
    VALA @talk "I don't have the address."
    VALA @smile "But I know our dear Captain Nyx will have it."

    $ GoalShow(QstTheComingStorm, 95)
    $ QstTheComingStorm().ValaInvestigationPath = True

    MC @talk "Then I must go now!"
    show mc at blurin, cleft_f
    VALA @talk "[player_name!t]..."
    VALA @smile "If things go awry, return here."
    VALA @smile "I {i}might{/i} be able to help you."
    show mc at blurin, cleft
    MC @think "What could go awry that I need to return here?"
    VALA @talk "Just an offer."
    show vala at center_f with ease
    "Vala stepped closer towards me, placing her hands lightly on my chest."
    MC @surprised "What are you-"
    VALA @blush "I like interesting men."
    VALA @blush "And you're... {i}a very interesting man.{/i}"
    MC @surprised "This... {i}Here? Now?{/i}"
    VALA @blush "Do you see anyone else around?"
    "Her voice was soft, low, almost playful. One hand brushed slowly down my chest."
    VALA @blush "And don't worry... I know a quiet section of the library no one ever visits."
    VALA @blush "So, what do you say?"
    menu:
        "{i}*Give in*{/i}":
            # cont
            pass

        "No... I can't.":
            VALA @sad "Hmmm..."
            VALA @smile "Alright then."
            VALA @talk "You should go. Captain Nyx will be eager to hear what you have to tell her, I'm sure."
            show vala at blurin, center
            $ Pause(0.1)
            hide vala with easeoutright
            "With that, Vala turned to leave, disappearing into the rows of ancient books and silence."
            show mc at blurin, cleft_f
            MC "(She's right... I shouldn't delay. I should head straight to the Captain!)"
            $ Pause(0.1)
            hide mc with easeoutleft
            scene black with dissolve
            $ LocSet("novaras_dist_edu")
            $ LocEnter()

    "For a moment, I said nothing."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    "Then I took her hand."
    "Her eyes met mine, half-lidded with amusement and something else."
    "She pressed me into one of the cushioned chairs, her lips brushing my ear."
    VALA @talk "{i}Just relax... let me show you how I reward interesting men.{/i}"
    hide mc
    hide vala
    with dissolve
    "Letting her take my hand, Vala led me down one of the branching rows of books that seemed to stretch on forever."
    scene black with dissolve
    "Pulling up a chair, she smiled teasingly as she began to strip."
    VALA "Clothes off."
    MC "{i}Here?{/i}"
    MC "Anyone could see us if they {i}do{/i} walk by!"
    $ PlaySoundRandom("tentFlap")
    "With her breasts exposed, she gently pushed me back into the chair."
    $ PlaySoundRandom("tentFlap")
    VALA "Trust me."
    VALA "{i}That's part of the fun.{/i}"

    $ PlaySexFx("audio/sex_sounds/forgean_075.ogg", 1)
    scene vala_titjob_slow with dissolve
    $ Pause()

    MC "A-Ahh...!"
    "Vala smirked as she pressed her soft breasts together, squeezing them around my cock as she began to rhythmically massage and bounce."
    "Warm, and like being wrapped in silk, she spat onto my cock and squeezed me tighter."
    VALA "My... {i}From how pent-up you seem, you've really needed some release, haven't you?{/i}"
    "Her tits molded around my shaft perfectly, and with each bounce, her hardened nipples brushed against my skin."
    MC "H-Hrghh...!"
    MC "I think you might be insane."
    "She tightened her grip, each dip sending another wave of pleasure pulsing through me."
    VALA "Flattery will get you everywhere."
    VALA "{i}Now I'm going to wring you fucking dry.{/i}"
    "Her eyes stayed locked on mine, intense and curious, like she was studying every reaction."
    "If not for her soft, trembling breath, you'd think she was completely composed."
    MC "S-Saren..."
    VALA "It's Vala to you."
    "I swallowed hard, heat rushing through my body as the pressure grew."
    "I glanced upward, half-expecting someone to come around the corner."
    VALA "You know—Mmm..."
    VALA "I could use a man like you."
    VALA "{i}In more ways than one.{/i}"
    "A groan escaped my throat."
    
    scene vala_titjob_fast with dissolve
    $ Pause()

    "Her calm demeanor masked the quickened pace of her heartbeat—only noticeable by how close she was."
    MC "Is that more because you want me to—{i}*Huff*{/i} kill for you?"
    MC "{i}Or something else?{/i}"
    "Her breath warmed the head of my cock as she gave a sly smile."
    VALA "I told you..."
    VALA "{i}It's because I like interesting men.{/i}"
    "She bit her lower lip, glasses fogging up slightly as she picked up speed."
    "Sweat glistened on her chest as she leaned in, eyes never leaving mine."
    VALA "Just imagine everything we could do together."
    VALA "{i}*Huff*{/i} With you by my side, I could rise to head inquisitor."
    MC "Ahh! {i}If{/i} I survive that long by your side."
    VALA "Mhmmm...❤️"
    VALA "I think you can."
    VALA "And I think I'll {i}reward{/i} you for it every night.❤️"
    "Hot, pulsing pleasure overwhelmed my senses."
    "The need to finish was unbearable now. Every motion, every squeeze—electric."
    MC "H-HRGHHHHHH...!"

    $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
    $ ReduceInfectionFromSex("vala")
    $ UnlockGalSceneAndGrantXp("vala", "titjob")
    scene vala_titjob_finish 
    with flash
    $ Pause()

    "As the hot release splashed across her face and breasts, Vala twitched slightly, then smirked as she licked a bit from her lips."
    VALA "Mmmm..."
    $ CharSetClothes("mc", "pants")
    $ CharSetClothes("vala", "naked")
    $ LocFlush()
    show vala at cright_f
    show mc at cleft
    with dissolve
    "She rose gracefully to her feet and began dressing without skipping a beat."
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("vala", "normal")
    show vala at nod
    MC "{i}*Huff*{/i} Not even a kiss goodbye?"
    VALA "That can be your reward next time... if you ask nicely."
    "She smiled as she pulled her skirt back over her hips."
    VALA "Get dressed."
    VALA "Captain Nyx will be eager to hear what you have to say, I'm sure."
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("mc", "normal")
    show mc at nod
    "She didn't wait for me to finish dressing."
    show vala at blurin, cright
    $ Pause(0.1)
    hide vala with easeoutright
    "As she buttoned up her shirt and smoothed her hair, she strolled calmly back toward the main hall."
    $ AutoMus(True)
    show mc at center with ease
    MC "(Crazy bitch.)"
    show mc at blurin, center_f
    MC "(She's right though. I shouldn't delay—Captain Nyx needs to hear what I've learned!)"
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("novaras_dist_edu")
    $ LocEnter()

##############################################
label qst_TheComingStorm_GetToValaSneak_Arrived:
    MC "(The door is locked... And I can't see Vala anywhere.)"
    MC "(No choice. Gotta force my way in...)"
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    $ LocSet("novaras_library_int")
    $ Pause(0.25)
    $ LocFlush()
    show vala at cright_f
    with dissolve
    show mc at cleft with easeinleft
    VALA @surp "Oh... Now this is a surprise!"
    $ GoalComplete(QstTheComingStorm, 97)
    VALA @smile "How'd you escape?"
    show mc at shake
    MC @angry "You knew the inquisitors were already planning to storm the estate!"
    VALA @talk "I read the report that a raid was planned."
    VALA @talk "It seemed like an awfully convenient way to solve two investigations at once to send you in first."
    MC @serious "You used me... again."
    VALA @smile "Correct."
    MC @angry "You said you would help me!"
    VALA @talk "And I shall."
    MC @angry "You seriously think I'm going to just trust you after you set me up?"
    VALA @talk "Do you really have much of a choice?"
    VALA @smile "Besides... I believe you and the Captain are onto something."
    MC @think "What?"
    VALA @talk "My fellow inquisitors are often blinded by their zealousness to presume everything is the result of dark magecraft."
    VALA @talk "But I believe you are correct, this is the work of the Demorai."
    show vala at center_f with ease
    VALA @talk "So, {i}our interests align...{/i}"
    "Vala reaches out to take my hand."
    show vala at blurin, center
    VALA @talk "Come, there's a private room out back you can use."
    MC @think "A private room?"
    VALA @smile "I had it set up for myself in case I decided to stay overnight at the library."
    VALA @talk "You'll be able to lay low there... for now."
    scene black with dissolve
    #Re-use VIP brothel room art here
    scene bg_weeping_heart_brothel_room
    with dissolve
    show vala at cright with easeinleft
    show mc at cleft with easeinleft
    MC @serious "How do I know this isn't just another ruse?"
    show vala at blurin, cright_f
    VALA @talk "You don't, and you'd be correct not to fully trust me."
    VALA @talk "...But whether you trust me or not, I believe {i}you{/i} are going to be needed for whatever is to come."
    VALA @talk "Now, there's a small wash bowl in the room, I suggest you use it."
    VALA @talk "You smell rather... {i}Unpleasant.{/i}"
    hide vala with easeoutleft
    show mc at center with ease
    scene black with dissolve
    $ Pause(0.5)
    $ TimeAdvTo(TIME_NOON)
    jump qst_TheComingStorm_BrothelRoomWaitForNyx
