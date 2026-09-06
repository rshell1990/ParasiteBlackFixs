#################################################################
# Wandering the streets, the player is approached by a city guard.
label qst_dreamhouse_primer_letter:
    show mc at cleft with easeinleft
    show cg_guard_hamun at cright_f with easeinright
    $ QstSetProgress(PrimerDreamhouse, 1)
    GUARD "Ladies Anya and Chanyi of Faymore estate wish to speak with you."
    MC @think "Who?"
    GUARD "I would suggest heading to their home at once."
    GUARD "Lady Chanyi is not to be ignored..."
    $ PlayerAddItem("qst_butterfly_letter")
    show cg_guard_hamun at nod
    "The guard handed over a small document with the house sigil of a butterfly attached."
    show cg_guard_hamun at blurin, cright
    $ Pause(0.3)
    hide cg_guard_hamun with easeoutright
    $ NoteUnlock("dreamhouse_primer")
    show mc at center with ease
    MC @serious "(What am I getting myself into this time?)"
    $ QstStart(HouseLockFaymoreManor)
    $ LocEnter()

label qst_dreamhouse_primer_approach_estate:
    $ NoteLock("dreamhouse_primer")
    $ PlayerRemItem("qst_butterfly_letter")
    "The guard carefully inspected the document, and then, after looking up towards me, stepped aside."
    show cg_guard_hamun at right_f with ease
    GUARD "Be on your best behaviour, or you will be removed by force at Lady Anya and Chanyi's pleasure."
    scene black with dissolve
    $ LocSet("hamun_faymore_manor")
    $ LocEnter()

# exclusively for "her letter"
screen QstDreamhouseLetter():
    add "qst_dreamhouse_note"
    text _("{size=+20}I'm sorry...{/size}"):
        align (0.5, 0.5)
        style "prologue_letter_text_main"
        color "#000000ff"
    button:
        xsize 1920
        ysize 1080
        background Null()
        action [With(Dissolve(0.15)), Return()]
    timer 1.5 action [With(Dissolve(0.15)), Return()]
   
label qst_dreamhouse_enter_manor:
    $ QstComplete(PrimerDreamhouse)
    show mc at center with easeinleft
    "Entering through the doors, I was greeted by the strangest sight."
    "The great hall seemed split in two halves: one made of black marble and stone, with macabre statues of old gods and skulls, like the home of some terrifying vampire lord."
    show mc at blurin, center_f
    "The other half was made of white marble and pink stone, complete with statues of majestic horses and beauty."
    show anya at right_f with easeinright
    ANYA @happy "OHHH! You made it!"
    show mc at blurin, cleft with ease
    "The excited, cheerful woman rushed over once she saw me."
    MC @think "Umm, you know who I am?"
    ANYA @happy "Of course, everyone's heard about you and what happened in that arena!"
    "The woman motioned towards herself."
    show anya at nod
    ANYA @talk "I am Anya Faymore."
    
    ANYA @happy "Thank you for accepting our invitation."
    MC @think "Right... But..."
    MC @think "What is this about?"
    CHANYI "Our daughter, sellsword."
    show chanyi at cright_f with easeinright
    "Descending the great stairs, another woman, this one a katai, adorned in a beautiful black dress, made her way over towards us."
    ANYA @happy "This is my beautiful wife, Chanyi!"
    ANYA @talk "Should I get us some tea or—"
    CHANYI @talk "Our daughter is missing. Given you and your party's set of *skills*, I want you to get her back for us."
    ANYA @sad "Chanyi, we said we'd take our time explaining things, not just—"
    #show chanyi at blurin, cright
    CHANYI @talk "Our daughter is missing."
    CHANYI @talk "We can waste time drinking tea when she's back."
    #show chanyi at blurin, cright_f
    ANYA @sad "Y-Yes... Of course."
    $ CharMeet("anya")
    $ CharMeet("chanyi")
    menu qst_dreamhouse_enter_manor_menu:
        "You two seem very... Different.":
            ANYA @emb "W-Well... You see."
            ANYA @talk "I used to be very different."
            ANYA @talk "I was in a difficult place until I met Chanyi here!"
            ANYA @happy "She just swooped me off my feet when I was at my lowest!"
            CHANYI @laugh "You and I have very different recollections of swooping you off your feet."
            CHANYI @laugh "I seem to remember it involved a lot more biting and pinning you against walls."
            ANYA @shock "CHANYI!"
            ANYA @emb "Must you always tell people that?"
            jump qst_dreamhouse_enter_manor_menu
        "Forgive me, but... She's both of your daughters?":
            CHANYI "Anya is her birth mother."
            CHANYI "But I have raised her since she was three."
            ANYA @sad "We're both terribly worried!"
            MC @think "And the father is...?"
            ANYA @sad "Umm... We are no longer together."
            ANYA @sad "It's... a long story."
            MC @talk "I see."
            jump qst_dreamhouse_enter_manor_menu
        "Tell me everything about your daughter's disappearance.":
            CHANYI @talk "Her name is Serafina. She's eighteen."
            CHANYI @talk "She disappeared about a month ago."
            CHANYI @angry "No doubt taken by that righteous cunt of a father of hers."
            ANYA @sad "Chanyi, we don't know for sure it was him."
            CHANYI @angry "Who else could it be?"
            CHANYI @angry "That prick has never accepted you leaving him for me!"
            MC @think "Who is the father?"
            ANYA @sad "His name is Davik... He's an inquisitor."
            pass
    menu qst_dreamhouse_enter_manor_menu2:
        "Has he been in contact with your daughter at all?":
            CHANYI @angry "Six months ago, I found a letter he wrote begging to see her."
            CHANYI @talk "She swore she never wrote him back, but I'm not convinced."
            CHANYI @angry "He's just trying to get in her head! He hardly had time for her or Anya when he was too busy running around playing inquisitor."
            jump qst_dreamhouse_enter_manor_menu2
        "Tell me more about your daughter.":
            pass
    "The two women shifted uncomfortably at the question."
    MC @think "What? What's the matter?"
    ANYA @sad "Serafina had... a gift."
    MC @talk "A gift?"
    CHANYI @talk "Her nightmares would come true."
    MC @surprised "... What?"
    ANYA @talk "She was a normal girl until her sixteenth birthday, then..."
    CHANYI @talk "Then the nightmares came."
    MC @serious "Slow down, what do you mean her nightmares came true?"
    CHANYI @talk "When she turned sixteen, a group of men tried to kidnap her."
    CHANYI @talk "No doubt to ransom her off, but our guards managed to get her to safety."
    CHANYI @talk "She was shaken up though, and that night... she woke up screaming."
    CHANYI @talk "She told us that she dreamed she was a monster chasing down the men who tried to kidnap her."
    CHANYI @talk "She described it in such vivid detail... I thought it was just an overactive imagination at first."
    ANYA @talk "... Then the bodies were found in the morning."
    ANYA @talk "Each man torn apart in exactly the way she told us her nightmare went."
    MC @think "... And there have been more nightmares since?"
    ANYA @sad "Yes... First it was one of our gardeners."
    ANYA @sad "Then others died in her nightmares."
    ANYA @sad "It got so bad, we started asking the staff to wear masks so she wouldn't see their faces... in case she dreamed about them."
    menu qst_dreamhouse_enter_manor_menu3:
        "She possesses a type of magecraft I've never heard of before... Why not contact a mage?":
            CHANYI @angry "Absolutely not!"
            CHANYI @angry "In a best-case scenario, they would take her away from us."
            CHANYI @angry "In a worst case, those infernal inquisitors might see her as a dark mage."
            jump qst_dreamhouse_enter_manor_menu3
        "Do you think her father wishes to harm her?":
            ANYA @sad "Gods, no!"
            CHANYI @angry "You can't know that for sure, Anya."
            ANYA @talk "He loved her, he wanted to be in her life."
            ANYA @talk "No matter what happens, I know he wouldn't want to hurt her!"
            MC @talk "Can you tell me more about why you separated from your husband?"
            ANYA @sad "To be married to an inquisitor isn't an easy thing."
            ANYA @sad "At first, they're gone for days, just here and there."
            ANYA @sad "Days become weeks."
            ANYA @sad "Weeks become months."
            ANYA @sad "The loneliness is crushing, and soon, you're not living with someone you love anymore, but just another stranger in your home."
            MC @talk "You chose to marry an inquisitor. You must have known how absent he would have to be?"
            CHANYI @angry "Easy to say when you're not the one coming home to an empty house every night."
            ANYA @angry "Chanyi!"
            ANYA @sad "... Yes, I knew how demanding the job would be."
            ANYA @sad "And the first time I kissed Chanyi, the guilt nearly killed me..."
            ANYA @talk "Till I saw him with *her.*"
            MC @think "Your husband was having an affair?"
            ANYA @talk "I don't know."
            MC @think "Then I don't understand..."
            ANYA @talk "She was an inquisitor like him. The two of them were smiling and laughing."
            ANYA @talk "They looked at each other the way we used to look, and I understood. He was lonely too."
            ANYA @talk "No one was happy, so I decided to do the only thing I could... I left."
            MC @talk "I take it your husband didn't take well to the news."
            CHANYI @talk "Neither did her cunt of a family."
            CHANYI @talk "I told them to fuck off too."
            ANYA @sad "But that's the full story, alright?"
            jump qst_dreamhouse_enter_manor_menu3
        "What happened the day she disappeared?":
            pass

    CHANYI @talk "A servant came to bring her breakfast, only to find the bed empty and a window open."
    CHANYI @talk "A note was left on the bed."
    "Lady Chanyi handed me the letter."
    play sound audio.letter
    call screen QstDreamhouseLetter() with dissolve
    CHANYI @talk "It's her handwriting."
    MC @think "And you're certain the father took her?"
    CHANYI @talk "Her father visited Hamun two nights before she was taken. He never came to see us, but it's far too much of a coincidence."
    CHANYI @talk "Find her father, and you will find our daughter."
    MC @talk "... And what's in it for me?"
    MC @talk "I *am* a sellsword after all."
    ANYA @talk "W-We can pay you a lot of coin, or—"
    CHANYI @talk "Ass."
    show anya at shake
    ANYA @emb "C-CHANYI!"
    CHANYI @talk "What? It would not be the first time we took a man to join us in our bed."
    "Chanyi's eyes wandered over me lustfully."
    CHANYI @laugh "Given the amount of women swooning over you since your little performance at the arena..."
    CHANYI @laugh "Well, I do like us being the envy of this city..."
    MC @think "So, a night with you two or coin?"
    CHANYI @laugh "Oh, it's more than just a night we want."
    CHANYI @laugh "Myself and Anya discussed bringing in a more 'regular' toy for our amusement."
    CHANYI @talk "So, here's the choice."
    CHANYI @talk "Either we'll pay you five thousand coins and gift you something extra as a *gift.*"
    "Chanyi's tail swished from side to side as she smirked."
    CHANYI @laugh "Orrrr we could take you as our toy lover."
    "Anya's cheeks burned bright red."
    CHANYI @think "So, what will it be?"
    menu:  
        "Coin.":
            $ QstDreamhouse().ChosenReward = 1
            CHANYI @talk "Hm... Can't say I'm not a little disappointed."
            CHANYI @talk "Very well, though."
        "Ass.":
            $ QstDreamhouse().ChosenReward = 0
            CHANYI @laugh "See, Anya?"
            CHANYI @laugh "Of course he was going to pick the fun choice."
    CHANYI @talk "Now go find our daughter."
    $ QstStart(QstDreamhouse)
    $ GoalShow(QstDreamhouse, 0)
    CHANYI @talk "Her father was last seen visiting the Hamun library... I suggest you start there."
    scene black with dissolve
    $ QstSetProgress(HouseLockFaymoreManor, 1)
##### outside the mansion
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush(dissolve)

    show mc at cright with easeinleft
    show sypha at cleft with easeinleft
    show mc at blurin, cright_f
## if chose ass
    if QstDreamhouse().ChosenReward == 0:
        SYPHA @happy "I have some rope if you're interested."
        SYPHA @happy "Personally, I prefer Chaniya. I imagine it'll be more fun breaking her in."
        if CharIsLover("kiara"):
            show kiara at left with easeinleft
            KIARA @sad "..."
            SYPHA @talk "Stop pouting."
            SYPHA @talk "If you're jealous, just kill the whores and fuck him."
            KIARA @angry "M-Mistress!"
            MC @angry "No, no killing."
            SYPHA @talk "Then tie them up and assert yourself as their master."
            SYPHA @think "You Alderians... so indecisive!"
## if chose gold
    elif QstDreamhouse().ChosenReward == 1:
        SYPHA @sad "Boo. Those two were a delightful treat."
        SYPHA @sad "They would have made delightful lesser concubines."
        if CharInParty("ves"):
            show ves at left with easeinleft
            show ves at shake
            VES @angry "He does not need more women!"
            VES @blush "Having to share him with you is more than enough!"
            SYPHA @happy "You just don't appreciate the fun of all the mind games to be had."
            SYPHA @happy "... And if you get bored of them, you can always just poison them."
            VES @angry "Careful, Demorai. I may just slip some of that poison in your drink while I'm at it!"
            SYPHA @happy "Flirting will get you everywhere with me."
    $ LocEnter()


###############################################################################################################################################
label qst_dreamhouse_numa_talk:
    NUMA @talk "Hm?"
    NUMA @talk "Now that you mention it, an inquisitor did come by here about a month ago."
    menu qst_dreamhouse_numa_talk_menu:
        "Did he have a girl with him?": 
            NUMA @talk "Not that I can remember..."
            NUMA @talk "Though it was a while ago."
            jump qst_dreamhouse_numa_talk_menu
        "What was he looking for?":
            pass
    NUMA @talk "I can't quite remember."
    NUMA @think "I remember him being particularly interested in texts about dreams and dark magecraft."
    menu qst_dreamhouse_numa_talk_menu2:
        "Aren't books on dark magecraft banned?":
            NUMA @talk "In general, yes."
            NUMA @talk "But this is the Free City, and the Inquisition doesn't have the same authority here as in the rest of Alderay."
            "Numa shrugged."
            NUMA @talk "Unless a dark mage is particularly troublesome, the merchant lords are unlikely to pursue the matter."
            jump qst_dreamhouse_numa_talk_menu2
        "Books on dreams?":
            NUMA @talk "I don't know. He kept asking all manner of strange questions."
            NUMA @talk "Something about peering beyond the veil."
            NUMA @talk "To be quite frank, I find talking to most inquisitors distasteful."
            NUMA @angry "Most of them are borderline more mad than the supposed dark mages they claim to hate."
            jump qst_dreamhouse_numa_talk_menu2
        "Did he mention at all where he was in the city?":
            pass
    NUMA @talk "No, but..."
    NUMA @talk "He had a strange companion."
    NUMA @angry "A mage who reeked of death."
    MC @surprised "What?"
    MC @think "A dark mage and an inquisitor..."
    MC @think "{i}Together?{/i}"
    SYPHA @happy "Oooh! The intrigue!"
    SYPHA @happy "What a delightful mystery this is becoming!"
    MC @think "What is it they were interested in? Just books?"
    NUMA @think "No, he mentioned he was looking to recruit some sellswords to his service."
    NUMA @talk "Perhaps it might be worth asking around?"
    NUMA @think "Whatever he was planning, he'd likely need to stock up on supplies for it."
    NUMA @talk "Anyway, that is all I know on the matter."
    $ GoalComplete(QstDreamhouse, 0)
    $ GoalShow(QstDreamhouse, 1)
    $ LocEnter()

#################################################################################################################################################
label qst_dreamhouse_talk_katiya:
    KATIYA @shock "Yes! How did you know?"
    MC @talk "Did he say what he was doing?"
    KATIYA @talk "I try not to ask too much when it comes to inquisitors."
    KATIYA @think "But... he did place a large order for general supplies."
    KATIYA @talk "Food, potions, and even asked me to procure horses."
    MC @think "Did he say where he was staying in Hamun?"
    KATIYA @think "No. In fact, I'm pretty sure he's long left the city by now."
    MC @angry "(Damn it.)"
    KATIYA @think "{i}Buttttt...{/i}"    
    KATIYA @talk "He placed an order for me to deliver by wagon to {i}this{/i} location."
    KATIYA @sad "I sent the wagon, but neither it nor the driver have returned."
    KATIYA @talk "If you promise to return my wagon and my man to me, should he still be alive, I will give you the location."
    $ GoalComplete(QstDreamhouse, 1)
    $ GoalShow(QstDreamhouse, 2)
    menu qst_dreamhouse_talk_katiya_wagonmenu:
        "I'll do it... But I want more than just the location." (AppearIf = (QstDreamhouse().KatiyaNegotiatedFor == None), Req_Barter = 15):
            KATIYA @think "What do you want?"
            menu:
                "From now on, you show me your tits whenever I come by your store.":
                    KATIYA @think "Really?"
                    KATIYA @talk "{i}*Sigh*{/i} Very well, pervert, as you wish." 
                    $ QstDreamhouse().KatiyaNegotiatedFor = "tits"
                    jump qst_dreamhouse_talk_katiya_wagonmenu
                "I want a discount" (Req_Barter = 18):
                    KATIYA @think "Five percent."
                    MC @talk "Ten percent."
                    KATIYA @talk "Hmm... Very well, I will give you a ten percent discount on all goods from now on."
                    $ QstDreamhouse().KatiyaNegotiatedFor = "discount"
                    jump qst_dreamhouse_talk_katiya_wagonmenu
                "Some supplies would be useful.":
                    KATIYA @think "Hmmm... I don't have much spare stock lying around."
                    KATIYA @talk "But I do have some of these goblin stimulants I bought from a merchant recently."
                    KATIYA @happy "I think they will be of great use to you."
                    $ QstDreamhouse().KatiyaNegotiatedFor = "supplies"
                    jump qst_dreamhouse_talk_katiya_wagonmenu
        "I'll do it.":
            if QstDreamhouse().KatiyaNegotiatedFor == "tits":
                $ DialogueKatiya().AlwaysShowTits = True
            elif QstDreamhouse().KatiyaNegotiatedFor == "discount":
                $ ShopHamunGeneral().Discount = 0.1
            elif QstDreamhouse().KatiyaNegotiatedFor == "supplies":
                $ PlayerAddItem("goblin_stims", 8)
            KATIYA @happy "Perfect."
            KATIYA @talk "Here, it's far, but..."
            KATIYA @talk "This is where he ordered the supply wagon to."
            $ WorldMapLocAdd("nubarian_tribelands")
            $ WorldMapLocAdd("ancient_forest")
            $ QstStart(HouseLockDreamhouse)
            $ GoalComplete(QstDreamhouse, 2)
            $ GoalShow(QstDreamhouse, 3)
            $ LocEnter()

        "I need time to think on it.":
            KATIYA @sad "Well... my wagon is still missing, so..."
            KATIYA @sad "Let me know if you change your mind, I suppose."
            $ LocEnter()

label qst_dreamhouse_katiya_rep:
    KATIYA @think "Well?"
    jump qst_dreamhouse_talk_katiya_wagonmenu
############################################################################
#Upon leaving the store
label qst_dreamhouse_after_katiya:
    $ QstDreamhouse().ShowPostKatiyaThreat = False
    show mc at cleft with easeinleft
    show cg_virgo at cright_f with easeinright
    "As I left the store, a man, shrouded in robes, moved closer towards me."
    "Instinctively, I reached for my blade, but he raised his hand defensively."
    UNKNOWN "Hold, sir knight."
    MC @angry "What is this about?"
    UNKNOWN "I know the Faymore women have sent you to try and recover their daughter."
    UNKNOWN "... Don't."
    UNKNOWN "Abandon this quest, for everyone's sake."
    MC @angry "Explain yourself."
    UNKNOWN "The girl, her gift... Her curse."
    UNKNOWN "Her parents do not know what horrors they will unleash."
    UNKNOWN "Do not come for her."
    $ PlaySound(audio.flock_of_crows)
    hide cg_virgo with dissolve
    "In a moment, the man dissolved away into a flurry of crows that screeched and flew off as his voice whispered one last time."
    UNKNOWN "{i}Do not come...{/i}"
    show mc at cright with ease
    show mc at shake
    MC @surprised "What foul magecraft was that?!"
    show kiara at cleft with easeinleft
    show mc at blurin, cright_f
    KIARA @think "If there is one thing I have learned from my brief time with the Demorai,"
    KIARA @think "it is that there is a sea of magecraft we still hardly understand."
    hide kiara with dissolve
    if CharInParty("ves"):
        show ves at cleft with easeinleft
        VES @think "Should we not heed his advice?"
        VES @sad "I have... the strangest feeling we could end up making things worse."
        show sypha at left with easeinleft
        SYPHA @happy "And where's the fun in just giving up?"
        SYPHA @happy "Besides, a damsel is in distress, is she not?"
        VES @talk "Are we sure that is what this is?"
        VES @sad "What if... her father really is doing the right thing here?"
        SYPHA @think "Then we will not know until we find out more."
        SYPHA @talk "Trust me, only start making assumptions once you have enough pieces."
        SYPHA @talk "Then you'll know who to plunge your dagger into."
    $ LocEnter()


##################################################################################################################################################################
#Upon finding yourself at the entrance of the creepy house
# triggered on entering ancient forest
label qst_dreamhouse_enter_forest:
    $ QstDreamhouse().SeenEnterForestOneOff = True
    show mc at cright_f with easeinright
    MC @think "... What is this place?"
    scene cg_dreamhouse_ext with dissolve
    "The house itself seemed painfully out of place."
    "Across the vastness of the forest, its winding trees and lands untouched by man,"
    "here lay a decrepit manor..."
    "As though it was plucked out of thin air and slammed onto the ground here without thought or reason."
    "The earth around it decayed and rotted, as the house itself gave off an eerie, uneasy presence."
    $ LocFlush()
    show mc at cright_f
    with dissolve
    show kiara at right_f with easeinright
    KIARA @scared "{i}... It's like the house is staring back at me.{/i}"
    MC @angry "(This place... There's something.)"
    MC @angry "({i}Off{/i} about it.)"
    SHYAHTAN "(Caution.)"
    $ LocEnter()

###################################################################################################################################################################
# LAYER 1  Upon entering the house - the player is LOCKED inside the house, unable to escape until the quest is complete
label qst_dreamhouse_enter_house:
    $ QstDreamhouse().L1_SeenEnterHouseOneOff = True
    show mc at cleft with easeinleft
    $ PlaySound(audio.door_lock)
    "As we entered the house, the door bolt locked behind us."
    show mc at blurin, cleft_f
    show mc at shake
    $ PlaySound(audio.lock_door_shake)
    "I grabbed at the door, attempting to unlock it, to no avail."
    MC @surprised "What?!"
    menu:
        "Destroy the door with your parasite form.":
            show mc at shake
            $ PlaySound(audio.door_crash)
            "With a swipe of my claw, I tore through the door with ease, as though it was paper."
            "... Only to reveal solid black rock on the other side."
        "Knock on the door.":
            $ PlaySound(audio.door_knock_intense)
            "I banged furiously on the door, calling out for someone to open it."
            "As I did so, someone—or something—knocked back from the other side."
            $ PlaySound(audio.door_knock_intense)
            MC @surprised "Hello?!"
            MC @surprised "Who's out there?"
            "{i}Silence.{/i}"
        "Put your ear to the door and listen.":
            "I put my ear to the door, listening for any sound."
            "{i}Silence.{/i}"
            "Not a trace of the outside world."
    show mc at blurin, cleft
    show sypha at cright_f with easeinright
    SYPHA @talk "It seems whatever presence is here doesn't want us to leave."
    show kiara at right_f with easeinright
    KIARA @scared "What now?"
    KIARA @scared "Please tell me it isn't fucking ghosts."
    KIARA @scared "I fucking hate ghosts!"
    "Sypha smirked, bemused."
    SYPHA @happy "Afraid of the dead?"
    KIARA @angry "I'm not afraid of the dead."
    KIARA @angry "I'm afraid of ghosts!"
    KIARA @scared "They're different!"
    MC @serious "It doesn't matter. We're stuck here now, so let's keep moving..."
    $ GoalShow(QstDreamhouse, 4)
    $ LocEnter()

label qst_dreamhouse_cant_exit:
    MC "(There is a solid wall where a way out was...)"
    $ LocEnterQ()

###################################
# The player is free to explore the house which has 2 floors + basement- there are some clickables about the place.
# bathroom
label qst_dreamhouse_l1_bathtub:
    "It doesn't seem to have been used in years..."
    $ LocEnterQ()
label qst_dreamhouse_l1_mirror:
    "A shattered mirror. There is broken glass all over the floor."
    $ LocEnterQ()

# nursery
label qst_dreamhouse_l1_toys:
    "Stuffed toys, dilapidated and worn out."
    "They look more creepy than anything else now."
    $ LocEnterQ()
label qst_dreamhouse_l1_crib:
    "An empty crib."
    "... Eerie."
    $ LocEnterQ()

# Master bedroom, (end of the hallway - KEYS are needed to unlock)
label qst_dreamhouse_l1_bedroom:
    if PlayerHasItem("qst_red_skull_key"):
        $ PlayerRemItem("qst_red_skull_key")
        scene black with dissolve
        jump qst_dreamhouse_l2_start
    else:
        show mc at cleft with easeinleft
        MC "(Locked... How strange.)"
        MC @think "(I can't hear anything from the other side?)"
        $ LocEnter()

# DOWNSTAIRS
label qst_dreamhouse_l1_candle:
    MC @think "(Who lit all these candles?)"
    $ LocEnterQ()

# DINING HALL (on enter once?)
label qst_dreamhouse_l1_dining_oneoff:
    $ QstDreamhouse().L1_SeenDiningHallEnterOneOff = True
    show mc at cleft with easeinleft
    show markus at left with easeinleft
    MARKUS @scared "Did you feel that?"
    MC @think "What?"
    MARKUS @scared "I... I swear I just felt something grab my hand!"
    MC @talk "I didn't see anything."
    "I looked back towards the others, they shrugged."
    show markus at shake
    MARKUS @angry "Fuck this place!"
    MARKUS @angry "Why can't it be a house haunted by the ghosts of horny whores with huge tits?"
    show kiara at cright_f with easeinright
    KIARA @think "Because you'd never leave if it was?"
    MARKUS @shock "I-"
    MARKUS @think "... Point taken."
    $ LocEnter()


# Clickables in dining hall
# 1 A set dinner table 
label qst_dreamhouse_l1_table:
    "(The table's already set...)"
    $ LocEnterQ()
# 2 Mounted wolf head 
label qst_dreamhouse_l1_wolfhead:
    "(The mounted head of a wolf.)"
    $ LocEnterQ()
# portrait of family
label qst_dreamhouse_l1_portrait:
    "A portrait of a family."
    "A wife, husband, and what seems to be two daughters and a son."
    "... Where are they?"
    $ LocEnterQ()

# KITCHEN (Connects through dining hall)
# (on enter)
label qst_dreamhouse_l1_kitchen_oneoff:
    $ QstDreamhouse().L1_SeenKitchenEnterOneOff = True
    show mc at cright_f with easeinright
    MC @think "(Nothing here.)"
    show sypha at right_f with easeinright
    SYPHA @happy "Anyone hungry?"
    if CharInParty("ves"):
        show ves at left with easeinleft
        VES @think "Why, of all places, was the girl taken here?"
    $ LocEnter()

# Clickables in kitchen
label qst_dreamhouse_l1_kitchen_cupboards:
# 1 - cupboards 
    "Upon opening the cupboards, they are surprisingly well-stocked."
    MC @serious "(These must be some of Katiya's provisions...)"
    MC @think "(But where is everyone?)"
    $ LocEnterQ()

label qst_dreamhouse_l1_kitchen_pot:
# 2 - cooking pot
    MC "(Someone's cooking stew?)"
    $ LocEnterQ()

label qst_dreamhouse_l1_kitchen_table:
# 3 "Note on table."
    "{i}Food provisions to last ten days. Fourteen if rationed.{/i}"
    "{i}Water should last two weeks at least.{/i}"
    "{i}- Should be enough to last.{/i}"
    MC @think "(Should be enough to last what?)"
    $ LocEnterQ()


# WINE CELLAR (Connects through kitchen)
label qst_dreamhouse_l1_cellar_oneoff:
    $ QstDreamhouse().L1_SeenCellarEnterOneOff = True
    show mc at cleft with easeinleft
    show markus at cright_f with easeinright
    MARKUS @scared "Finally, a room that DOESN'T send a chill up my spine."
    show sypha at left with easeinleft
    SYPHA @think "Still no sign of anyone, though..."
    $ LocEnter()


# Clickables (cellar)

# 1 Wine barrel
label qst_dreamhouse_l1_cellar_barrel:
    "The barrels appeared to be full, and yet... they were covered in dust?"
    $ LocEnterQ()

# 2 scattered paperwork
label qst_dreamhouse_l1_cellar_paper:
    $ QstDreamhouse().L1_TookSmallMystKey = True
    show mc at cright_f with easeinright
    "I picked up the paperwork to inspect it closer."
    "Covered in strange incantation markings and writings in blood, it was a macabre sight."
    MC "(What in the world is—)"
    show markus at cleft with easeinleft
    MARKUS "Looks like more fucking dark mage bullshit to me."
    "Suddenly, a small key dropped out from the pile of paperwork."
    $ PlayerAddItem("qst_small_myst_key")
    "(What's this?)"
    "(Hm... Might be useful.)"
    $ LocEnter()

##### LIBRARY ROOM
# (on enter)
label qst_dreamhouse_l1_library_oneoff:
    $ QstDreamhouse().L1_SeenLibraryEnterOneOff = True
    show mc at cleft with easeinleft
    show kiara at left with easeinleft
    KIARA @think "It's... almost kind of cozy in here."
    KIARA @scared "Almost."
    $ LocEnter()

# Clickables (library)
# Portrait of a smiling hanged man
label qst_dreamhouse_l1_library_portrait:
    "... Disturbing."
    if QstDreamhouse().L1_UnlockedStudy == True:
        $ LocEnterQ()
    "Hm? There's a keyhole at the bottom?"
    menu:
        "Insert the key." (AppearIf = PlayerHasItem("qst_small_myst_key")):
            $ PlayerRemItem("qst_small_myst_key")
            $ QstDreamhouse().L1_UnlockedStudy = True
            "As I inserted the key into the lock and twisted it, one of the bookcases opened up, revealing a hidden door behind."
            MC @think "(Huh...)"
            SYPHA @happy "Oh! Just like the one I have back home!"
            $ LocEnterQ()
        "Step back.":
            "I stepped away from the picture, feeling the eyes of the hanged man almost seem to follow me around the room as I moved."
            $ LocEnterQ()
# bookshelf l
label qst_dreamhouse_l1_library_bookshelf_1:
    "Nothing but grisly tales."
    "Just what kind of library is this?"
    $ LocEnterQ()
# bookshelf r
label qst_dreamhouse_l1_library_bookshelf_2:
    "Flipping through the pages of the books, most of them were completely blank."
    "... What?"
    $ LocEnterQ()
# fireplace
label qst_dreamhouse_l1_library_fireplace:
    "A still-lit fireplace."
    "The fire crackled as it burned the wood, but it radiated no warmth."
    $ LocEnterQ()


# SECRET STUDY ROOM (from library))
# 1 - Main desk
label qst_dreamhouse_l1_study_desk:
    show mc at cleft with easeinleft
    $ QstDreamhouse().L1_TookRedSkullKey = True
    "Heading over towards the main desk, I found a red key next to a small journal."
    $ PlayerAddItem("qst_red_skull_key")
    "{i}It's not a house.{/i}"
    "{i}It's not a house.{/i}"
    "{i}It's not a house.{/i}"
    "{i}It's not a house.{/i}"
    "{i}It's not a house.{/i}"
    "... What?"
    $ PlaySound(audio.man_scream_terror)
    "As I grabbed the red skull key, I heard a sharp scream."
    show mc at blurin, cleft_f
    MC @surprised "Upstairs!"
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("dreamhouse_library")
    $ LocEnter()

#########################################################################################################################################################
# LAYER 2 OF THE HOUSE (Zombies)
##########################################################################################################################################################
#The locked door to the master's bedroom opens - White screen - Player now finds themselves back in the main hallway they started in, more distorted.
label qst_dreamhouse_l2_start:
    $ PlaySound(audio.magic_earthy_cast1)
    MC @surprised "... What the f-"

    $ QstDreamhouse().HouseStage = 2
    $ LocSet("dreamhouse_hallway")
    scene bg_dreamhouse_l2_entrance
    with dissolve
    $ Pause()
    show markus at cleft
    show mc at cright_f
    with dissolve
    MARKUS @scared "How in the hells did we end up back down here?!"
    hide markus with easeoutright
    show kiara at cleft with easeinleft
    KIARA @scared "Uhh... Does this place look..."
    KIARA @scared "{i}Different?{/i}"
    "As I looked around, I realized Kiara was indeed right."
    hide kiara with dissolve
    "The house had become an even more twisted version of itself, now drenched in blood, with tombstones littered around the place as a light fog swept through."
    "The house itself seemed to breathe, when suddenly, wounded and stumbling through the corridor towards us..."
    "... An inquisitor?"
    show cg_davik at cleft with easeinleft
    UNKNOWN "Who the fuck are you?!"
    UNKNOWN "Help me! QUICKLY!"
    "Before I could answer him, hurling itself around the corner, came a horde of walking corpses."
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    "I barely had time to reach for my sword before they were upon us!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_zombie_fem":11}, {"e_zombie_half":12}, {"e_zombie_fem":11}]))
    "Slaying the last of the creatures with a clean swipe to sever its head, I turned towards inquisitor."
    $ AutoMus(True)
    scene bg_dreamhouse_l2_entrance
    show mc at cleft
    show cg_davik at cright_f
    with dissolve
    MC @serious "What in the hells is this?"
    UNKNOWN "Ahhh! Damn things tore right through my armour..."
    UNKNOWN "My name is Davik."
    DAVIK "Who sent you? You people shouldn't be here!"
    MC @talk "I was sent by the Faymore Estate to bring back their daughter."
    DAVIK "{i}*Sigh*{/i} Of fucking course you were."
    DAVIK "Well, you're trapped here now, same as everyone who enters this place."
    MC @serious "Start giving me some answers."
    MC @think "What the fuck is going on?"
    DAVIK "This place... She made it all."
    DAVIK "She conjured it up in her dream."
    DAVIK "It was supposed to contain all her nightmares and set her free, but..."
    DAVIK "The house hungers, it's taking a life of its own."
    MC @surprised "{i}This house... came from her dreams?{/i}"
    DAVIK "Yes..."
    menu qst_dreamhouse_l2_start_menu:
        "How long have you been here?":
            DAVIK "I... Only a few hours!"
            MC @think "Davik... It's been over a month since the disappearance."
            DAVIK "I... No."
            DAVIK "This house is... It's messing with me!"
            jump qst_dreamhouse_l2_start_menu
        "Where are your men?":
            DAVIK "Dead."
            DAVIK "I've been running from room to room, nightmare to nightmare, trying to reach Serafina."
            DAVIK "My men, one by one, have been picked off by... {i}things.{/i}"
            DAVIK "Trust me, the walking dead is the least of your worries."
            jump qst_dreamhouse_l2_start_menu
        "What were those things?":
            DAVIK "Nightmares made flesh."
            DAVIK "Whatever it is, the house is responding to one of Serafina's fears."
            jump qst_dreamhouse_l2_start_menu
        "Why did you kidnap your daughter?":
            pass

    DAVIK "I had no choice!"
    DAVIK "Once I confirmed how dangerous her powers had become, I knew I had to find a way to help her contain them!"
    DAVIK "{i}... Else my brothers and sisters would treat her as something too dangerous to live.{/i}"
    MC @think "So you found a dark mage?"
    DAVIK "How did you-"
    DAVIK "{i}*Sigh*{/i} Yes, a man named Virgo."
    DAVIK "He promised to help me contain her powers. In return, I set him free."
    MARKUS @shock "Are you mad?"
    MARKUS @angry "YOU... An inquisitor set a dark mage free!"
    DAVIK "I had no choice!"
    DAVIK "Virgo might be mad, but he's at least more reasonable than the rest."
    DAVIK "He told us the ritual would at least take a day."
    DAVIK "This house, he helped her channel her dream to forge it."
    DAVIK "It was supposed to be a prison for her nightmares, but it's..."
    "There was a loud crash, the sounds of groaning as the dead banged on the windows from outside."
    DAVIK "Damn it!"
    DAVIK "Find the keys, do you hear me?"
    DAVIK "Serafina and Virgo are at the core of this nightmare!"
    DAVIK "Each key through the master bedroom will take you one layer closer!"
    $ GoalShow(QstDreamhouse, 5)
    show cg_davik at right_f with ease
    MC @surprised "Wait! Where are you going?"
    DAVIK "We're not on the same layer right now, not really!"
    DAVIK "The key I need to find isn't the same as yours!"
    DAVIK "Go, hurry!"
    DAVIK "I will meet you at the center!"
    DAVIK "Then we can get my daughter out of this!"
    hide cg_davik with easeoutright
    show mc at center with ease
    MC @surprised "Wait! Hold on a min-"
    "Davik hurried as quickly as he could around a corner, slightly limping as he did so."
    $ PlaySound(audio.door_slam)
    "I tried to stop him, but as he exited through one of the doors, it slammed shut behind him."
    "Markus hurried over to try and rip the door open, only to find it bolted shut."
    show markus at right with easeinleft
    show markus at shake
    $ PlaySound(audio.lock_door_shake)
    MARKUS @angry "It's locked!"
    show mc at blurin, center_f
    MC @angry "Shit!"
    MC @think "The key has to be somewhere here... We just need to find it."
    KIARA @scared "Sure... As long as we don't get eaten first."
    $ LocEnter()

# BATHROOM - Clickables changed
label qst_dreamhouse_l2_bathtub:
    "Looks like a mercenary... Maybe one of Davik's men?"
    "I noticed something shimmer in the mixed blood water of the bath."
    menu:
        "Reach in and grab it.":
            "Shoving my hand into the bloody water, I pulled out a small, dull key."
            $ QstDreamhouse().L2_TookDullKey = True
            $ PlayerAddItem("qst_dull_key")
            KIARA @scared "I think I might be sick..."
            $ LocEnterQ()
        "Step back.":
            "(No way am I putting my hand in that.)"
            $ LocEnterQ()

# 2 - Broken mirror covered in blood
label qst_dreamhouse_l2_mirror:
    "Looks like there was a struggle in here."
    $ LocEnterQ()

# 3 - Corpse in bathtub
label qst_dreamhouse_l2_bathroom_oneoff:
    $ QstDreamhouse().L2_FoughtBathtubZombie = True
    show cg_babyface at center with dissolve
    "Entering the bathroom, a man lay dead in the tub, half-eaten as a strange specter appeared to be laping up his blood."
    "It tilted its head towards me as I drew my blade!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_ghost_babyface":15},]))
    $ AutoMus(True)
    scene bg_dreamhouse_l2_bathroom
    with dissolve
    MC @surprised "Was that a fucking ghost?!"
    KIARA @scared "No, no, no, no, no!"
    KIARA @scared "You've got to be kidding me!"
    $ LocEnter()
    

##### nursery (on enter)
label qst_dreamhouse_l2_nursery_oneoff:
    $ QstDreamhouse().L2_SeenNurseryOneOff = True
    "Entering the room, the twisted corpses inside turned their attention towards us."
    MC @scared "Shit!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_zombie_fem":11}, {"e_zombie_fem":11}, {"e_zombie_fem":11}]))
    $ AutoMus(True)
    scene bg_dreamhouse_l2_nursery
    with dissolve
    $ LocEnterQ()

#### Clickables nursery
label qst_dreamhouse_l2_toys:
    # 1 - Torn up Toys 
    "Blood-stained and torn up toys."
    $ LocEnterQ()
label qst_dreamhouse_l2_crib:
    #2 - Bloody Crib
    "A crib stained in blood."
    $ LocEnterQ()

##### Master bedroom door 
label qst_dreamhouse_l2_bedroom_door:
    MC "(We need the key to unlock this!)"
    menu:
        "Unlock." (AppearIf = PlayerHasItem("qst_blue_skull_key")):
            $ PlayerRemItem("qst_blue_skull_key")
            "Inserting the key into the lock, the door swung open as we scrambled through,"
            $ PlaySound(audio.magic_earthy_cast1)
            scene black with flash
            "a bright white light enveloping us all as we did so."
            jump qst_dreamhouse_l3_start
        "Step back.":
            $ LocEnterQ()

# DOWNSTAIRS hall
# The player clicks on lit blue candle in main hallway
label qst_dreamhouse_l2_candle:
    MC @think "(A blue flame... Why?)"
    $ LocEnterQ()

##### DINING HALL, l2 on enter
label qst_dreamhouse_l2_dining_oneoff:
    $ QstDreamhouse().L2_SeenDiningOneOff = True
    "Entering the dining hall, the table had become a ghoulish display of gore, as the creatures crowded around it."
    "Guts, blood, and indiscernible flesh sprawled across the table as they grabbed at the meat with their bare hands and devoured it."
    "The wretched smell of rot and death was too much for Kiara, who hurled onto the floor."
    KIARA @scared "Oh gods..."
    "As she did so, the dead looked up, dropping the meat in their hands as they began shambling towards us!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    MARKUS @angry "I FUCKING HATE THIS HOUSE!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_zombie_half":12}, {"e_zombie_fem":11}, {"e_zombie_half":12}, {"e_zombie_fem":11}]))
    $ AutoMus(True)
    scene bg_dreamhouse_l2_diningroom
    show mc at cleft
    show markus at cright_f
    with dissolve
    #Battle against zombies.
    MARKUS @shock "{i}*Huff*{/i} I think that's the last of them."
    if CharInParty("ves"):
        show ves at center with dissolve
        VES @angry "These creatures only fall when their head is cleaved from their neck!"
        show ves at shake
        VES @angry "How tedious!"
        hide ves with dissolve
    show sypha at left with easeinleft
    SYPHA @think "We can't stay here, come on."
    $ LocEnter()

# Clickables (dining hall l2)
label qst_dreamhouse_l2_table:
    "(... Gods, what a nightmare.)"
    $ LocEnterQ()

    # 2 Mounted wolf head 
label qst_dreamhouse_l2_wolfhead:
    "BARK!"
    "The mounted head snapped towards me with its jaws."
    "(Is it... Is it still alive?)"
    $ LocEnterQ()

label qst_dreamhouse_l2_portrait:
    # portrait of dead family
    "That's... disturbing."
    $ LocEnterQ()

#### KITCHEN (l2 on enter)
label qst_dreamhouse_l2_kitchen_oneoff:
    $ QstDreamhouse().L2_SeenKitchenOneOff = True
    "As we entered the kitchen, I heard the slamming of the cleaver as we looked to find one of the dead,"
    show cg_butcher at center with dissolve
    "a huge, decrepit, bulking figure hacking away at a man."
    "Still barely alive and choking on blood, the man reached out towards us in one desperate final act, only for the creature to hack off his fingers with the cleaver."
    "As the fingers dropped to the floor, the ghoulish creature turned towards us, placing down a platter of the man's remains on the table,"
    "it then stared blankly towards us, expectantly."
    MARKUS @scared "Does... Does this fucking thing expect us to eat that?!"
    menu:
        "*Eat the meat.*":
            "Carefully, I reached over to grab a piece of the meat."
            "With a shaky hand, I pushed the wet meat into my mouth as the creature offered a drooling grin of approval."
            "Markus pulled back in revulsion as Kiara looked like she was about to hurl."
            "The wet meat squeelched between my teeth, almost making me wretch as my eyes began to water from the foul taste."
            KIARA @sad "Oh gods... I might... I think I'm gonna be sick."
            MARKUS @scared "What in the hells is wrong with you?"
            SYPHA @think "... Is this is some kind of masochistic ritual humans perform?"
            #If Ves is present
            if CharInParty("ves"):
                VES @think "... Why no salt?"
            #
            "Seemingly satisfied that I had tasted his *food,* the creature went back to cooking, seemingly ignoring us and allowing us to pass."
            $ LocEnterQ()

        "I think I'll pass...":
            "The ghoulish dead creature stared for a moment,"
            "and realizing none of us will eat its {i}food,{/i}"
            "it grabbed for the cleaver and swung it wildly towards us!"
            # Battle against zombie chef 
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_zombie_butcher":14},]))
            $ AutoMus(True)
            scene bg_dreamhouse_l2_kitchen
            with dissolve
            "Stumbling backwards, blood running from the seeping gash in its head from where I struck,"
            "in the creature's final moments, it reached up to grab a chunk of meat, stuffing its mouth full of it before it fell silent."
            $ LocEnterQ()
    

# Clickables (kitchen l2)
label qst_dreamhouse_l2_kitchen_cupboards:
    # 1 - bloody cupboards 
    "The cupboards bled and were filled with nothing but pungent meat in a gory mess."
    MC "(I think I'll pass on dessert.)"
    $ LocEnterQ()

    # 2 - cooking pot
label qst_dreamhouse_l2_kitchen_pot:
    MC "A boiled, severed head floated to the top of the blood stew."
    $ LocEnterQ()

    # 3 ."
label qst_dreamhouse_l2_kitchen_table:
    "{i}Why does no one believe me?{/i}"
    "{i}We buried the servant boy the other day, mother says his lungs were sick.{/i}"
    "{i}I swear I saw him move, but no one believed me.{/i}"
    "{i}I dreamed he was still moving in that box, and he came to see me that night.{/i}"
    "{i}He was all mangled and gross, I screamed, but he was gone when mother came...{/i}"
    $ LocEnterQ()

    # CELLAR btn (locked l2)
label qst_dreamhouse_l2_kitchen_to_cellar:
    MC @think "Damn, it's locked!"
    menu:
        "Use Key." (AppearIf = PlayerHasItem("qst_dull_key")):
            $ PlayerRemItem("qst_dull_key")
            $ QstDreamhouse().L2_UnlockedCellarDoor = True
            "The door clicked as it unlocked."
            $ LocEnterQ()
        "Step back.":
            $ LocEnterQ()


# Clickables cellar l2
label qst_dreamhouse_l2_cellar_barrel:
    #1 blood barrel
    "No wine, only blood it seems... warm to the touch."
    $ LocEnterQ()

label qst_dreamhouse_l2_dead_mercenary:
    $ QstDreamhouse().L2_TookBlueSkullKey = True
    #2 dead mercenary
    "Inspecting the corpse of the man, I found clutched in his coiled, dead hand, the blue skull key."
    $ PlayerAddItem("qst_blue_skull_key")
    $ LocEnterQ()

# LIBRARY ROOM (on enter l2)
label qst_dreamhouse_l2_library_oneoff:
    $ QstDreamhouse().L2_SeenLibraryOneOff = True
    "Upon entering the room, the swarm of dead shuffling around turned their attention towards us!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_zombie_half":12}, {"e_zombie_fem":11}, {"e_zombie_fem":12}, {"e_zombie_fem":11}]))
    $ AutoMus(True)
    $ LocEnter()

# Clickables (library l2)
label qst_dreamhouse_l2_library_fireplace:
    # 1 fireplace
    "A still-lit fireplace."
    "The fire crackled as it burned the wood, but it radiated no warmth."
    $ LocEnterQ()

label qst_dreamhouse_l2_library_bookshelf_1:
    # 2 bookshelf 1
    "The pages were ruined and covered in blood."
    $ LocEnterQ()

label qst_dreamhouse_l2_library_bookshelf_2:
    # 3 bookshelf 
    "... Just what kind of nightmares did this girl have?"
    $ LocEnterQ()

# 4 Portrait of a man being devoured.
label qst_dreamhouse_l2_library_portrait:
    "There's a depiction of what seems to be a man devouring raw, bloody, flesh... How macabre."
    "There's no keyhole this time."
    $ LocEnterQ()


######################################################################################
# LAYER 3 - AFTER heading through the master bedroom, the player is taken to the third
# layer and appears in the entrance hall once again.
######################################################################################
label qst_dreamhouse_l3_start:
    $ QstDreamhouse().HouseStage = 3
    $ QstDreamhouse().SuspendPartyChars()
    $ LocSet("dreamhouse_hallway")
    scene bg_dreamhouse_l3_entrance
    with dissolve
    show mc at cleft
    with dissolve
    MC @surprised "Gods, what is this place?"
    MC @think "Does anyone-"
    show mc at blurin, cleft_f
    "As I turned to look back, I realized the others were not with me."
    MC @surprised "Markus?"
    MC @surprised "Kiara?"
    show mc at blurin, cleft
    MC @surprised "{i}Anyone?{/i}"
    show mc at center with ease
    MC @serious "... Fuck."
    MC "(Alright, you know what to do. Find the key, move onto the next floor.)"
    MC @sad "(I just hope the others are fine.)"
    $ LocEnter()

### BATHROOM - Clickables
label qst_dreamhouse_l3_bathtub:
# 1 - Bathtub
    "The water is black..."
    $ LocEnterQ()

# 2 - Strange mirror
label qst_dreamhouse_l3_mirror:
    show mc at cleft with easeinleft
    "Looking into it, I saw my own reflection, but it was distorted."
    menu:
        "Touch the mirror.":
            $ QstDreamhouse().L3_TouchedMirror = True
            "As I placed my hand onto the mirror, I felt it go {i}through{/i} the glass into the other side."
            "It was cool, and as I pushed my hand deeper, I grabbed at something."
            $ PlaySound(audio.slash_claw)
            "Pulling my hand and whatever it was out, something clawed at me!"
            $ DamagePlayer(20, Lethal = False)
            show mc at shake
            MC @surprised "AHH!"
            "I ripped back my hand, staring at the gash of blood."
            "Clutched in my hand, though, was a small, strange totem."
            $ PlayerAddItem("qst_strange_totem")
            MC "(What is this?)"
            $ LocEnter()
        "Don't touch the mirror.":
            "(Probably not a good idea.)"
            $ LocEnter()

label qst_dreamhouse_l3_granny_counter:
    if GetLocID() not in ["dreamhouse_bathroom", "dreamhouse_diningroom", "dreamhouse_kitchen", "dreamhouse_cellar", "dreamhouse_library"]:
        $ LocEnterQ()

    ## increment counter
    $ QstDreamhouse().L3_GrannyCounter += 1
    if QstDreamhouse().L3_GrannyCounter < 8:
        if QstDreamhouse().L3_GrannyCounter > 4:
            $ PlaySound(audio.granny_shears)
        $ LocEnterQ()
    $ QstDreamhouse().L3_GrannyCounter = 0

    ## cont
    $ AutoMus(False)
    $ tmpvar = RngInt(1, 2)
    if tmpvar == 1:
        $ PlayMusic("audio/music/56_Granny_Lullaby.ogg")
    elif tmpvar == 2:
        $ PlayMusic("audio/music/55_Granny_Chase.ogg")

    if GetLocID() == "dreamhouse_bathroom":
        jump qst_dreamhouse_l3_granny_bathroom
    elif GetLocID() == "dreamhouse_diningroom":
        jump qst_dreamhouse_l3_granny_diningroom
    elif GetLocID() == "dreamhouse_kitchen":
        jump qst_dreamhouse_l3_granny_kitchen
    elif GetLocID() == "dreamhouse_cellar":
        jump qst_dreamhouse_l3_granny_cellar
    elif GetLocID() == "dreamhouse_library":
        jump qst_dreamhouse_l3_granny_library

label qst_dreamhouse_l3_granny_bathroom:
    $ PlaySound(audio.granny_shears)
    MC "(She's coming!)"
    menu:
        "Hide behind the bath.":
            "I hid behind the bath."
            show cg_granny_oh_dreary at center
            with dissolve
            "Crouched beside it, the figure entered the bathroom and peered around, looking for me."
            if tmpvar == 1:
                "Crouched down behind the bathtub, the figure glanced from left to right for a moment before, thankfully, shuffling off."
                hide cg_granny_oh_dreary 
                with dissolve
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice

        "Get ready to barge past her!":
            "Deciding there was no point in hiding, I readied myself to try and slip past her!"
            if tmpvar == 2:
                "Barging through the figure, I barely managed to dodge the snap of her blades as I escaped!"
                jump qst_dreamhouse_l3_granny_cont
            else:
                # granny kill image
                jump qst_dreamhouse_l3_granny_wrongchoice

label qst_dreamhouse_l3_granny_diningroom:
    $ PlaySound(audio.granny_shears)
    MC @scared "(I need to hide!)"
    # (uses the same thing about music)
    menu:
        "Hide under the table.":
            if tmpvar == 1:
                #Success
                "Dropping to my knees, I crawled beneath the table and waited with bated breath."
                $ PlaySound(audio.granny_shears)
                show cg_granny_oh_dreary at center
                with dissolve
                "As I heard the sound of the shear blade snapping draw closer, the door to the dining room was kicked in as the figure walked on by."
                GRANNY_OH_DREARY "Precious... Where are you precious?"
                GRANNY_OH_DREARY "Come... Let granny take care of you forever!"
                "They stopped for a moment, looking around, before moving on into the next room."
                hide cg_granny_oh_dreary 
                with dissolve
                MC "(That was close...)"
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice
        "Prepare to throw a chair at her and run!":
            if tmpvar == 2:
                #Success
                "I grabbed the nearest chair,"
                $ PlaySound(audio.door_crash)
                "As the door burst open, I flung it towards her before fleeing!"
                $ PlaySound(audio.granny_shears)
                GRANNY_OH_DREARY "YOU CAN'T RUN FOREVER!"
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice
                # on fail, just art & game over

#IF GRANNY APPEARS when you enter kitchen
label qst_dreamhouse_l3_granny_kitchen:
    $ PlaySound(audio.granny_shears)
    MC "(I can hear her coming!)"
    menu:
        "Hide under the table.":
            if tmpvar == 1:
                "I crawled beneath the kitchen table and waited, hoping the monstrous figure would simply pass on by."
                $ PlaySound(audio.granny_shears)
                show cg_granny_oh_dreary at center
                with dissolve
                "The kitchen door swung open, shears snapping violently and tormentingly as she walked,"
                GRANNY_OH_DREARY "There's no need to run!"
                GRANNY_OH_DREARY "You'll make lots of friends with the other children!"
                hide cg_granny_oh_dreary 
                with dissolve
                "Granny Oh Dreary passed on by without noticing me... For now."
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice
        "Try and blockade the door with the table.":
            if tmpvar == 2:
                "Quickly, I moved to push the table against the door, blockading it."
                $ PlaySound(audio.door_knock_intense)
                "From the other side, I could hear loud banging on the door."
                MC @serious "(It won't hold long.)"
                MC @serious "(I need to get out of here!)"
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice

# if GRANNY APPEARS when you enter cellar
label qst_dreamhouse_l3_granny_cellar:
    $ PlaySound(audio.granny_shears)
    MC @scared "(Shit! She's coming!)"
    menu:
        "Hide behind some of the potions.":
            if tmpvar == 1:
                "Crouched down, I hide behind some of the many rows of potions and strange bottles."
                $ PlaySound(audio.granny_shears)
                show cg_granny_oh_dreary at center
                with dissolve
                "As the door opened, the figure stepped inside, shears snapping as she looked from left to right."
                GRANNY_OH_DREARY "Are you here, deary?"
                GRANNY_OH_DREARY "Come give granny a hug!"
                hide cg_granny_oh_dreary 
                with dissolve
                "I pulled back at the last second as she looked towards me, and as I did so, I heard the snapping sound grow distant as she moved on."
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice
        "Throw some of the potions at her!":
            if tmpvar == 2:
                "I didn't hesitate, grabbing the nearest bottle and launching it towards her as soon as she entered the room."
                $ PlaySound(audio.glass_shatter)
                "By pure luck, the bottle {i}somehow{/i} seemed to actually hit her."
                $ PlaySound(audio.poison_gas)
                show cg_granny_oh_dreary at center
                with dissolve
                "She screamed and wailed as it sizzled her, white steam rising from her as she seemed to shimmer."
                GRANNY_OH_DREARY "GAHHH! NAUGHTY! NAUGHTY FUCKING BRAT!"
                hide cg_granny_oh_dreary 
                with dissolve
                "She retreated... For now, at least."
                MC "(Too bad I didn't douse my sword in whatever that was first.)"
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice

label qst_dreamhouse_l3_granny_library:
    $ PlaySound(audio.granny_shears)
    "{i}*SNAP!*{/i}"
    GRANNY_OH_DREARY "Come out, prettyyyy!"
    GRANNY_OH_DREARY "Don't hide from grandmaaa!"
    menu:
        "Hide behind the bookshelves.":
            if tmpvar == 1:
                show cg_granny_oh_dreary at center
                with dissolve
                "Crouched down, I watched and waited patiently as Granny entered the library."
                "She glanced left."
                "Then right."
                hide cg_granny_oh_dreary 
                with dissolve
                "Then slowly turned to leave as I breathed a sigh of relief."
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice
            # failure does game over
        "Try and loop around one of the bookshelves and run for it.":
            if tmpvar == 2:
                show cg_granny_oh_dreary at center
                with dissolve
                "I timed it perfectly, waiting carefully for her to enter the room. Crouched low, I moved as silently as possible."
                hide cg_granny_oh_dreary 
                with dissolve
                "Before she knew it, I had managed to slip behind her and hurry out."
                jump qst_dreamhouse_l3_granny_cont
            else:
                jump qst_dreamhouse_l3_granny_wrongchoice


label qst_dreamhouse_l3_granny_wrongchoice:
    if PlayerHasItem("qst_strange_totem"):
        show cg_granny_oh_dreary at center
        show cg_granny_oh_dreary at shake
        "As Granny lunged towards me, the strange totem began to glow brightly,"
        "and as it did so, Granny shielded her eyes and fled from the room!"
        hide cg_granny_oh_dreary 
        with dissolve
        $ PlayerRemItem("qst_strange_totem")
        $ PlaySound(audio.magic_earthy_cast1)
        scene black with flash
        "As the totem dimmed, it cracked, crumbling away in my hands."
        MC "(... The totems... I need to find more of them if I can!)"
        jump qst_dreamhouse_l3_granny_cont
    else:
        $ PlaySound(audio.darkness_erupt)
        scene cg_dreamhouse_granny_gameover
        with flash
        $ Pause(1.5)
        jump defeat_generic

label qst_dreamhouse_l3_granny_cont:
    $ tmpvar = {}
    $ AutoMus(True)
    $ LocEnterQ()

#### nursery, l3 Clickables
label qst_dreamhouse_l3_toys:
# 1 - Dolls
    "Dolls."
    "... Oh gods."
    "Are those... {i}faces stitched to the dolls?{/i}"
    $ LocEnterQ()

# 2 - Crib with doll in it
label qst_dreamhouse_l3_crib:
    "Inside the crib was a doll clutching a small, diamond-head-shaped key."
    menu:
        "Take the key.":
            $ QstDreamhouse().L3_TookCribKey = True
            $ QstDreamhouse().L3_GrannyActive = True
            "I grabbed hold of the key."
            $ PlayerAddItem("qst_diamond_key")
            pass
        "Step back.":
            $ LocEnterQ()

    "As I took the key, from the shadowed corner of the room, I heard rocking."
    $ PlaySound(audio.rocking_chair)
    "Reaching for my blade, I turned to see a hunched, shrouded figure sitting in a rocking chair."
    "Had she been here this whole time?"
    MC @think "... Hello?"
    GRANNY_OH_DREARY "..."
    "The woman stopped rocking in her chair."
    MC @scared "... I'm looking for-"
    GRANNY_OH_DREARY "Do you know my song?"
    MC @think "What?"
    "I felt the air suck from the room as I took a step back."
    "The hair stood on end."
    GRANNY_OH_DREARY "Granny Oh Dreary, don't let children grow..."
    show cg_granny_oh_dreary at center
    "The woman rose from her rocking chair. She was tall... {i}too tall.{/i}"
    GRANNY_OH_DREARY "Snips off their faces so no one will know."
    GRANNY_OH_DREARY "Stay little, stay sweet, don't ever get tall…"
    GRANNY_OH_DREARY "Her dolls on the shelf used to speak, after all!"
    "From under her robes came the sharp glint of a huge pair of shears."
    GRANNY_OH_DREARY "Stitch up your smile, pull tight at the seam—"
    MC @scared "... Oh fuck."
    $ PlaySound(audio.granny_shears)
    "I stepped back, retreating as she pressed the blades together, grinning a hideous, oversized smile."
    "And as she inched closer, I could see {i}she was wearing someone's face.{/i}"
    GRANNY_OH_DREARY "Now you'll stay young in her quiet dream."
    "I drew my blade, swiping to slash across at the hag, only to find my blade went right through her as though she was made of air."
    MC @scared "SHIT!"
    $ PlaySound(audio.granny_shears)
    "Granny cackled, thrusting the shears towards me, which I narrowly dodged."
    "With little other option, I fled out of the room."
    hide cg_granny_oh_dreary 
    with dissolve
    scene black with dissolve
    $ LocSet("dreamhouse_hallway2")
    scene bg_dreamhouse_l3_hallway2
    show mc at cleft
    with dissolve
    MC @scared "Fuck! FUCK! FUCK!"
    MC @scared "(I can't fight her! I need to get the damn key and get out of here!)"
    $ LocEnter()

# DOWNSTAIRS clickey (l3)
# The player clicks on lit orange candle in main hallway
label qst_dreamhouse_l3_candle:
    MC @think "(A pink flame...)"
    $ LocEnterQ()

# DINING HALL door
label qst_dreamhouse_l3_diningdoor:
    MC "Fuck, it's locked."
    menu:
        "Open the door." (AppearIf = PlayerHasItem("qst_diamond_key")):
            $ PlayerRemItem("qst_diamond_key")
            $ QstDreamhouse().L3_DiningUnlocked = True
            "Inserting the key into the lock, the door opened."
            $ LocEnterQ()
        "Step back.":
            $ LocEnterQ()

### Dining hall (l3) clickeys
label qst_dreamhouse_l3_table:
    "(... I just hope those aren't the faces of {i}real{/i} children.)"
    $ LocEnterQ()

# 2 Mounted cat head
label qst_dreamhouse_l3_head:
    CAT "Why, hello."
    MC @surprised "You're... What?"
    CAT "Give me a pet, and I'll give you some advice."
    CAT "That {i}might{/i} just save your life."
    menu:
        "Pet the cat.":
            "The cat head purred with delight."
            CAT "Around this house may you find,"
            CAT "Totems that will bring you delight."
            CAT "When Granny strikes, they will shield you from your demise."
            MC "What?"
            "The cat closed its eyes and fell silent. It didn't respond again."
            $ QstDreamhouse().L3_GaveCatPet = True
            pass
        "Ignore the cat.":
            pass
    $ LocEnterQ()

label qst_dreamhouse_l3_portrait:
    "(Wait... I do remember old rhymes about her from when I was younger.)"
    "(Was she real? Or just something we told ourselves to scare each other?)"
    $ LocEnterQ()


# KITCHEN l3 clieckeys
#1 - cupboards 
label qst_dreamhouse_l3_kitchen_cupboards:
    "The cupboards were filled with various preserved jars and fragrant herbs."
    "There is nothing of use in here."
    $ LocEnterQ()

#2 - cooking pot
label qst_dreamhouse_l3_kitchen_pot:
    $ QstDreamhouse().L3_SeenKitchenPot = True
    MC "A stew boiled inside the pot."
    "In the burning wood beneath it, I noticed the end of a small item poking out."
    "Carefully removing it, I grabbed hold of a small, black totem."
    "Still hot to the touch, but somehow, I sensed this thing might be useful."
    $ PlayerAddItem("qst_strange_totem")
    $ LocEnter()


# WINE CELLAR  (l3)
# Clickables 
# 1 wine barrels have been replaced with row upon row of potions 
label qst_dreamhouse_l3_cellar_barrel:
    MC "(That's... different.)"
    MC "(Should I try and browse to see if I can find anything useful?)"
    menu:
        "Browse.":
            $ QstDreamhouse().L3_CheckedPotions = True
            "I quickly ran my hands along the various vials and potions. Amongst them, I found a small, strange totem-like item that seemed to almost call to me."
            $ PlayerAddItem("qst_strange_totem")
        "Forget it.":
            pass
    $ LocEnterQ()

# Key box
label qst_dreamhouse_l3_cellar_paper:
    "Upon closer inspection of the desk, I found a box of keys with some kind of strange mechanism attached to it."
    menu:
        "Remove cat key." (AppearIf = not PlayerHasItem("qst_cat_key")):
            if PlayerHasItem("qst_raven_key"):
                $ PlayerRemItem("qst_raven_key")
            if PlayerHasItem("qst_wolf_key"):
                $ PlayerRemItem("qst_wolf_key")
            $ PlayerAddItem("qst_cat_key")
            "I took the cat key, and as I did so, the mechanism triggered and locked the other keys into place."
        "Remove raven key." (AppearIf = not PlayerHasItem("qst_raven_key")):
            if PlayerHasItem("qst_wolf_key"):
                $ PlayerRemItem("qst_wolf_key")
            if PlayerHasItem("qst_cat_key"):
                $ PlayerRemItem("qst_cat_key")
            $ PlayerAddItem("qst_raven_key")
            "I took the raven key, and as I did so, the mechanism triggered and locked the other keys into place."
        "Remove wolf key." (AppearIf = not PlayerHasItem("qst_wolf_key")):
            if PlayerHasItem("qst_cat_key"):
                $ PlayerRemItem("qst_cat_key")
            if PlayerHasItem("qst_raven_key"):
                $ PlayerRemItem("qst_raven_key")
            $ PlayerAddItem("qst_wolf_key")
            "I took the wolf key, and as I did so, the mechanism triggered and locked the other keys into place."
    MC "(Looks like I'll have to put the one key back if I want to take out another.)"
    $ LocEnterQ()

#LIBRARY ROOM (l3)
label qst_dreamhouse_l3_library_sacrifice:
#Clickables 
    #1 Human sacrifice (on floor)
    MC "(... Oh gods.)"
    MC "(What the fuck did she do to him?)"
    MC "(There's a note in his hand...)"
    "{i}In halls of stone by firelight warm,{/i}"
    "{i}I walk in silence, soft of form.{/i}"
    "{i}I hunt the shade, I guard the grain,{/i}"
    "{i}With emerald eyes and velvet frame.{/i}"
    "{i}No knight am I, yet clawed and sly,{/i}"
    "{i}I wear no crown, yet rule nearby.{/i}"
    "{i}I purr like spells, I prowl at dusk—{/i}"
    "{i}What am I, in fur and musk?{/i}"
    $ LocEnterQ()

#2 fireplace 
label qst_dreamhouse_l3_library_fireplace:
    "The fireplace is burning, but the flame is an ominous blue for some reason."
    $ LocEnterQ()
#3 bookshelf 1
label qst_dreamhouse_l3_library_bookshelf_1:
    "The books are written in some strange language I don't understand, but there are numerous depictions of strange rituals and sacrifices."
    $ LocEnterQ()

#4 bookshelf 2
label qst_dreamhouse_l3_library_bookshelf_2:
    "There's something hidden between the books, a small, strange totem-like item that I feel compelled to take with me."
    $ QstDreamhouse().L3_SeenLibraryShelves2 = True
    $ PlayerAddItem("qst_strange_totem")
    $ LocEnterQ()

label qst_dreamhouse_l3_library_portrait:
    "A portrait of Granny Oh Dreary."
    "There's a keyhole below."
    if PlayerHasItem("qst_cat_key") or PlayerHasItem("qst_wolf_key") or PlayerHasItem("qst_raven_key"):
        menu:
            "Insert wolf key." (AppearIf = PlayerHasItem("qst_wolf_key")):
                "It doesn't fit..."
                $ LocEnterQ()
            "Insert raven key." (AppearIf = PlayerHasItem("qst_raven_key")):
                "This is the wrong key..."
                $ LocEnterQ()
            "Insert cat key." (AppearIf = PlayerHasItem("qst_cat_key")):
                $ PlayerRemItem("qst_cat_key")
                "The key fit into the slot perfectly,"
                "and as I turned it, the secret passageway revealed itself behind one of the bookcases."
                $ QstDreamhouse().L3_StudyUnlocked = True
                $ LocEnterQ()
    else:
        $ LocEnterQ()


# SECRET STUDY ROOM (l3)
#Clickables
#1 - Witch shrine
label qst_dreamhouse_l3_study_desk:
    $ QstDreamhouse().L3_CheckedWitchShrine = True
    "Placed carefully onto the shrine, there was a pink skull key next to a small journal."
    $ PlayerAddItem("qst_pink_skull_key")
    "{i}Why... Why did they need to tell me that awful story?{/i}"
    "{i}Every night now, I see her at my window.{/i}"
    "{i}Granny Oh Dreary asking me to let her in.{/i}"
    "{i}I don't think she's real yet... But...{/i}"
    "{i}The more I think about her, the more real she becomes...{/i}"
    "{i}Why... Why does this keep happening to me?{/i}"
    $ LocEnterQ()

label qst_dreamhouse_l3_bedroom_door:
    MC "(I need the key to unlock this!)"
    menu:
        "Unlock." (AppearIf = PlayerHasItem("qst_pink_skull_key")):
            $ PlayerRemItem("qst_pink_skull_key")
            "Inserting the key into the lock, the door swung open as I scrambled through,"
            $ PlaySound(audio.magic_earthy_cast1)
            scene black with flash
            "a bright white light enveloping me as I stepped inside."
            $ QstDreamhouse().RestorePartyChars()
            while PlayerHasItem("qst_strange_totem"):
                $ PlayerRemItem("qst_strange_totem", Silent = True, MuteSfx = True)
            jump qst_dreamhouse_l4_start
            # jump to l4 & entrance?
        "Unlock." (AppearIf = (PlayerHasItem("qst_cat_key") or PlayerHasItem("qst_wolf_key") or PlayerHasItem("qst_raven_key"))):
            "It is clearly not a key to this door..."
            $ LocEnterQ()
        "Step back.":
            $ LocEnterQ()

##########################################################################################################################################################################
#LAYER 4 - HOUSE OF TRAPS/DEATH PARTY
##########################################################################################################################################################################
# at entrance again, party reappears
label qst_dreamhouse_l4_start:
    $ QstDreamhouse().HouseStage = 4
    $ LocSet("dreamhouse_hallway")
    scene bg_dreamhouse_l4_entrance
    show mc at center
    with dissolve
    MC @angry "Oh joy..."
    MC @serious "Another round of terror."
    show markus at cleft with easeinleft
    MARKUS @scared "FUCK, FUCK, FUCK!"
    show mc at blurin, cright_f with ease
    MARKUS @scared "FUCKING SPIDERS!"
    MC @surprised "Markus!"
    "Markus' eyes lit up."
    show markus at shake
    MARKUS @angry "Where in the hells did you go?!"
    MC @angry "I could ask the same thing!"
    "I glanced back to make sure, indeed, everyone was now here."
    show kiara at left with easeinleft
    KIARA @scared "It seems I have a NEW phobia."
    KIARA @scared "Giant fucking spiders."
    hide kiara with dissolve
    MC @surprised "What?"
    show sypha at right_f with easeinright
    SYPHA @think "When we went through the door, the whole house was covered in cobwebs."
    SYPHA @think "We looked everywhere for you..."
    SYPHA @think "I presumed we were spiralling downwards, deeper into this girl's dreams or nightmares."
    SYPHA @think "But perhaps it's more like a tree, with different branching—"
    MARKUS @shock "Never fucking mind all that!"
    MARKUS @shock "Spiders! FUCKING SPIDERS!"
    MARKUS @angry "Spiders the size of dogs attacked us!"
    if CharInParty("ves"):
        show ves at left with easeinleft
        VES @smile "I killed the biggest one."
        "Ves smiles with a soft, triumphant arrogance."
        VES @smile "My ancestors smile upon me."
        MARKUS @angry "How about your ancestors actually do something useful?"
        VES @angry "Which one of us nearly burned the damn house down again because they panicked?"
        MARKUS @angry "They were crawling all over me!"
    "Sypha's gaze turned towards me."
    SYPHA @happy "So anyway, that was our delightful experience."
    SYPHA @think "What did you see?"
    menu:
        "I'd rather not talk about it.":
            SYPHA @sad "Hmm..."
            SYPHA @sad "That bad, huh?"
            pass
        "Granny Oh Dreary...":
            MARKUS @shock "What the fu-"
            MARKUS @think "You mean the story about that evil old hag taking faces?"
            MC @talk "The same one."
            KIARA @think "Is that some southern story or something?"
            MARKUS @think "What, you never heard of Granny Oh Dreary in Angmurus?"
            "Kiara shrugged."
            KIARA @talk "Most of our horror stories involve snow orcs stealing children in the night."
            if CharInParty("ves"):
                "Ves raised a brow at the comment."
                KIARA @think "... No offence."
                VES @think "What is a snow orc?"
                VES @angry "We are not made of snow! We are orcs!"
                KIARA @talk "I..."
                KIARA @talk "It's best just not to think about it too much, alright?"
            pass
        "Oh, just a crazy old lady who wanted to tear my face off and put it on a doll.":
            SYPHA @smug "How'd you know about mother?"
            "I couldn't help but burst out laughing at the comment."
            SYPHA @think "... Wait, what's so funny?"
            pass
    "Sypha's attention turned to the room around us."
    SYPHA @think "Does this place not seem eerily... Well..."
    SYPHA @think "{i}Not{/i} awful?"
    "As we paid attention to our surroundings at last, playing softly from another room, I could hear something... A harp?"
    MC @think "Do you all hear that?"
    MARKUS @smile "Maybe we'll get lucky."
    MARKUS @smile "Maybe this is her nightmare where she gets treated {i}too{/i} good by everyone around her."
    MC @think "Come on, let's investigate further..."
    $ LocEnter()

#BATHROOM - Clickables (l4)
#1 - Bathtub
label qst_dreamhouse_l4_bathtub:
    "The bubble bath was pristine, filled with hot, steaming water and bubbles."
    "Sypha's eyes lit up."
    SYPHA @happy "... A hot bath does sound nice right now."
    KIARA @talk "Can I join?"
    KIARA @talk "I'm pretty sure I still have some cobwebs in my hair."
    MARKUS @smile "As fun as it would be to watch you all get naked in the bath..."
    MARKUS @talk "The whole impending death thing kills the mood a bit."
    SYPHA @think "Who said you'd get to watch?"
    SYPHA @think "But I agree, we shouldn't trust anything we see here..."
    "Inside the water, through the bubbles, I saw a strange totem."
    menu:
        "Reach in and grab it.":
            $ QstDreamhouse().L4_TookTotemBath = True
            "Shoving my hand into the water to grab the totem, I suddenly yanked it out."
            "{i}It wasn't water.{/i}"
            $ PlaySound(audio.poison_gas)
            "Sizzling the flesh of my hand, I cried out."
            $ DamagePlayer(20, Lethal = False)
            MC "GRGHHHH!"
            MARKUS @shock "What in the hells?"
            KIARA @scared "FUCK!"
            MC @angry "Grghh! My damn hand!"
            "Rushing to my side, Sypha curiously did her best to tend to my injury."
            SYPHA @think "Hold still..."
            "Taking a small ointment from her pouch, she carefully applied it to my arm, calming the burning sensation."
            SYPHA @think "Be careful... This place is never what it seems."
            $ LocEnter()
        "Do nothing.":
            $ LocEnter()

# 2 - mirror
label qst_dreamhouse_l4_mirror:
    "It's a mirror."
    "... Well, I look good at least."
    $ LocEnterQ()

# door to Hallway 2 (l4) is locked
label qst_dreamhouse_l4_upstairs_to_hallway2:
    "The door to the right hallway is locked."
    "Looks like I'm going to need to find a key."
    menu:
        "Insert red demon key." (AppearIf = PlayerHasItem("qst_red_demon_key")):
            $ PlayerRemItem("qst_red_demon_key")
            pass
        "Insert white demon key." (AppearIf = PlayerHasItem("qst_white_demon_key")):
            $ PlayerRemItem("qst_white_demon_key")
            "Inserting the key into the lock, the door opened."
            $ QstDreamhouse().L4_Hallway2Unlocked = True
            $ LocEnterQ()
        "Insert orange demon key." (AppearIf = PlayerHasItem("qst_orange_demon_key")):
            $ PlayerRemItem("qst_orange_demon_key")
            pass
        "Insert blue demon key." (AppearIf = PlayerHasItem("qst_blue_demon_key")):
            $ PlayerRemItem("qst_blue_demon_key")
            pass
        "Do nothing.":
            $ LocEnterQ()
    "As I pressed the key into the lock and turned it, a blade shot out from the door, stabbing my hand."
    $ PlaySound(audio.knife_slice)
    $ DamagePlayer(10, Lethal = False)
    MC @angry "FUCK!"
    KIARA @sad "Wrong key, I guess...?"
    $ LocEnterQ()

#### nursery (l4)
# Clickables
# 1 - Toys 
label qst_dreamhouse_l4_toys:
    "The toys sit scattered across the floor."
    "Amongst the toys, three of them appear to be marked."
    "Should I check one?"
    label qst_dreamhouse_l4_toys_menu:
    if len(QstDreamhouse().L4_Toys_ToSee) > 0:
        menu:
            "Check the one marked 'ILLUSION'" (AppearIf = ("illusion" in QstDreamhouse().L4_Toys_ToSee)):
                $ QstDreamhouse().L4_Toys_ToSee.remove("illusion")
                "Picking up the one marked 'ILLUSION', a small key fell out from the back of it."
                $ PlaySound(audio.key_drop)
                MC "(Huh... This must be useful.)"
                $ PlayerAddItem("qst_dragon_key")
                jump qst_dreamhouse_l4_toys_menu
            "Check the one marked 'LIBERATION'" (AppearIf = ("liberation" in QstDreamhouse().L4_Toys_ToSee)):
                $ QstDreamhouse().L4_Toys_ToSee.remove("liberation")
                "As I picked up the toy a small string attached to it snapped, a concealed swinging pendulum came down to try and pierce me!"
                menu:
                    "Dodge!" (Req_Dex = 13):
                        $ PlaySound(audio.pendulum_swing)
                        "Quickly, I moved aside, dodging the swinging blade as it barely missed me!"
                        MC @surprised "Fuck...!"
                        pass
                    "Brace for the hit!":
                        $ PlaySound(audio.pendulum_swing)
                        "Bracing for the hit, the pendulum swung forward."
                        $ PlaySound(audio.blade_trap)
                        "Trying to grab and stop the blade in a last-ditch effort, it still violently sliced at my hands and lightly pierced my stomach!"
                        "Blood poured from my wounds as everyone panicked."
                        MC @angry "GHHHH!"
                        $ DamagePlayer(40, Lethal = False)
                        MARKUS @shock "[player_name]!"
                        KIARA @scared "No!"
                        "Pulling the blade out, I stumbled backwards, looking at the blood on my hands and wincing."
                        SHYAHTAN "(STABILIZING WOUNDS.)"
                        "As the others rushed to help and treat my injuries, I could feel something from within working desperately to try and seal up the wound."
                        MC @scared "That was... close."
                        pass
                jump qst_dreamhouse_l4_toys_menu
            "Check the one marked 'DEATH'" (AppearIf = ("death" in QstDreamhouse().L4_Toys_ToSee)):
                $ QstDreamhouse().L4_Toys_ToSee.remove("death")
                "Inspecting the one marked 'DEATH' closer,"
                $ PlaySound(audio.poison_gas)
                "as I reached to grab it, a green gas seeped from it, making my throat burn!"
                $ DamageParty(10, Lethal = False)
                MC "{i}*Cough!*{/i} S-Shit! {i}*Cough!*{/i}"
                jump qst_dreamhouse_l4_toys_menu
            "Step back":
                $ LocEnterQ()
    else:
        $ LocEnterQ()

# 2 - Crib
label qst_dreamhouse_l4_crib:
    $ PlaySound(audio.baby_crying)
    "A crib with... {i}Is that a baby crying?{/i}"
    menu:
        "Check the baby is okay!":
            $ QstDreamhouse().L4_SeenCrib = True
            "I hurry towards the crib, only to find, in the absence of a crying child, a doll with a wind-up key turning."
            MC @think "What the-"
            $ PlaySound(audio.explosion)
            "When the key stopped turning, the doll ceased crying, and as it did so, it suddenly exploded!"
            MC @surprised "DAMN IT!"
            $ DamagePlayer(15, Lethal = False)
            $ LocEnterQ()
        "Do nothing.":
            $ LocEnterQ()



# Master bedroom door (l4), (end of the hallway - GREEN SKULL key is needed to unlock)

label qst_dreamhouse_l4_bedroom_door:
    if QstDreamhouse().L4_UnlockedMasterBedroom == True:
        $ PlaySound(audio.magic_earthy_cast1)
        scene black with flash
        jump qst_dreamhouse_l5_start
    else:
        MC "(Locked...)"
        MC "Looks like we need another key to get out of here."
        menu:
            "Insert the green skull key" (AppearIf = PlayerHasItem("qst_green_skull_key")):
                $ PlayerRemItem("qst_green_skull_key")
                MC "(That worked.)"
                $ QstDreamhouse().L4_UnlockedMasterBedroom = True
                $ LocEnterQ()
            "Step away.":
                $ LocEnterQ()

    

#DOWNSTAIRS (l4)
#The player clicks on lit candle in main hallway - It is now Green
label qst_dreamhouse_l4_candle:
    MC @think "(A green flame this time...)"
    $ LocEnterQ()

#DINING HALL (l4)
#Clickables in the room 
#1 Set dinner table 
label qst_dreamhouse_l4_table:
    "(The food looks incredible!)"
    "(But... Where is everyone?)"
    label qst_dreamhouse_l4_table_menu:
    if len(QstDreamhouse().L4_Diningroom_StuffToSee) > 0:
        menu:
            "Eat some of the food." (AppearIf = ("food" in QstDreamhouse().L4_Diningroom_StuffToSee)):
                $ QstDreamhouse().L4_Diningroom_StuffToSee.remove("food")
                "Grabbing some of the food carefully with my hand, I take a bite."
                $ PlaySound(audio.crunch)
                "{i}*CRUNCH!*{/i}"
                $ DamagePlayer(10, Lethal = False)
                "I wince, spitting out the food along with some blood."
                MC @surprised "What?!"
                "Upon further inspection, I see small razor blades tucked into the food itself."
                MARKUS @scared "Couldn't this girl have nightmares about... I don't know, boy troubles or something normal!"
                jump qst_dreamhouse_l4_table_menu
            "Drink some of the wine." (AppearIf = ("wine" in QstDreamhouse().L4_Diningroom_StuffToSee)):
                $ QstDreamhouse().L4_Diningroom_StuffToSee.remove("wine")
                "I grab the wine and gulp it down."
                "The moment I do so, I know something is wrong... {i}very wrong.{/i}"
                "It starts as a hot tingle, and then it {b}burns.{/b}"
                $ PlaySound(audio.poison_gas)
                "I grasp at my throat, tightening as hot steam rises from my mouth, sizzling."
                "I try to scream, but it is only a choked cry as the others rush to gather around me in a panic."
                "I claw at my throat, literally tearing at the flesh in agony. It hurts... It hurts so fucking much."
                "Then I feel it—that burning from the inside as I begin to melt, Shyahtan panicking, desperately trying to contain it, but it's hopeless."
                "Whatever I just drank, it's... It's..."
                jump defeat_generic
            "Reach into the cake." (AppearIf = ("cake" in QstDreamhouse().L4_Diningroom_StuffToSee)):
                $ QstDreamhouse().L4_Diningroom_StuffToSee.remove("cake")
                "Carefully, I take a knife and delicately cut into the cake, and inside... is a small tree key."
                $ PlayerAddItem("qst_small_tree_key")
                jump qst_dreamhouse_l4_table_menu
            "Do nothing.":
                pass
    else:
        pass
    $ LocEnterQ()
#2 Mounted boar head 
label qst_dreamhouse_l4_boarhead:
    "(The mounted head of a boar.)"
    $ LocEnterQ()

#3 portrait 
label qst_dreamhouse_l4_portrait:
    SYPHA @happy "Reminds me of family get togethers."
    MARKUS @talk "Do your people even attend those, or do they just send out complimentary poison for everyone?"
    SYPHA @happy "Well, it's a more efficient way of dealing with in-laws I'll have you know!"
    $ LocEnterQ()

#KITCHEN (l4)
#Clickables in the room 
#1 - cupboards 
label qst_dreamhouse_l4_kitchen_cupboards:
    $ QstDreamhouse().L4_Kitchen_TookPotions = True
    "Upon opening the cupboards, I find they are fully stocked."
    MC @surprised "Oh! This looks useful..." 
    $ PlayerAddItem("potion_heal_minor", 3)
    $ LocEnterQ()

#2 - cooking pot
label qst_dreamhouse_l4_kitchen_pot:
    "The pot is bubbling over with what seems like stew."
    menu:
        "Have a taste of the stew.":
            $ DamagePlayer(5, Lethal = False)
            $ QstDreamhouse().L4_Kitchen_TastedStew = True
            "Grabbing a spoonful of the stew, I bring the substance to my lips."
            $ PlaySound(audio.poison_gas)
            "As I do so, I suddenly recoil from the burning heat."
            MC @surprised "(Gah! Too spicy!)"
            pass
        "Step back.":
            pass
    $ LocEnterQ()

#3 "letter on the table"
label qst_dreamhouse_l4_kitchen_table:
    "In a lord's great hall of torchlit stone,"
    "A sugared cake sat carved like a throne,"
    "Yet deep within its honeyed seam,"
    "Lay iron wrought from a darker dream."
    "Your key to salvation in sweetness pressed—"
    "To free a fate or seal a quest."
    $ LocEnterQ()

# WINE CELLAR - Locked - opened by tree key
label qst_dreamhouse_l4_kitchen_to_cellar:
    MC "(Locked. I need a key...)"
    menu:
        "Insert tree-shaped key" (AppearIf = PlayerHasItem("qst_small_tree_key")):
            $ PlayerRemItem("qst_small_tree_key")
            MC "(That seems to have worked.)"
            $ QstDreamhouse().L4_UnlockedCellar = True
            $ LocEnterQ()
        "Step away.":
            $ LocEnterQ()

# Clickables 
# 1 Wine barrels - Each one has a symbol on it
label qst_dreamhouse_l4_cellar_barrel:
    "... I guess I'm going to need to pry open one of these barrels, but which one?"
    label qst_dreamhouse_l4_cellar_barrel_menu:
    if len(QstDreamhouse().L4_BarrelsLeft) > 0:
        menu:
            "SKULL" (AppearIf = ("skull" in QstDreamhouse().L4_BarrelsLeft)):
                $ QstDreamhouse().L4_BarrelsLeft.remove("skull")
                $ PlaySound(audio.poison_gas)
                "I ripped open the lid of the barrel, and as I did so, a poisonous gas spilled out!"
                MC "{i}*Cough!*{/i} Shit! {i}*Cough!*{/i}"
                "As the poison cleared, inside, I saw a key with a demon-shaped end."
                $ PlayerAddItem("qst_red_demon_key")
                $ PoisonParty()
                jump qst_dreamhouse_l4_cellar_barrel_menu
            "EYES" (AppearIf = ("eyes" in QstDreamhouse().L4_BarrelsLeft)):
                $ QstDreamhouse().L4_BarrelsLeft.remove("eyes")
                "Tearing open the barrel, I was confronted by... a giant eye?"
                "The pupil frantically looked around before pushing itself out of the barrel."
                $ AutoMus(False)
                $ PlayMusicRandom("mus_battle_generic")
                "The floating, tendriled creature suddenly lashed out!"
                $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house", CharIDList_Right = [{"e_floating_eye":11},]))
                $ AutoMus(True)
                scene bg_dreamhouse_l4_cellar
                with dissolve
                "Dropping dead to the floor, its eye torn open by my blade, and inside it was... a demon-shaped key."
                $ PlayerAddItem("qst_white_demon_key")
                jump qst_dreamhouse_l4_cellar_barrel_menu
            "HEART" (AppearIf = ("heart" in QstDreamhouse().L4_BarrelsLeft)):
                $ QstDreamhouse().L4_BarrelsLeft.remove("heart")
                $ PlaySound(audio.many_arrows)
                "Opening up the barrel, a small burst of needles came flying out."
                "Shielding myself with my arm, a few of the pin-pricked fuckers still hit me."
                MC @angry "GAHH!"
                SYPHA @angry "Careful..."
                $ DamagePlayer(10)
                "Inside, was a key with a demon-shaped end."
                $ PlayerAddItem("qst_orange_demon_key")
                jump qst_dreamhouse_l4_cellar_barrel_menu
            "WINGS" (AppearIf = ("wings" in QstDreamhouse().L4_BarrelsLeft)):
                $ QstDreamhouse().L4_BarrelsLeft.remove("wings")
                $ PlaySound(audio.flock_of_crows)
                "Smashing open the barrel, a flock of birds screeched as they flew past me!"
                MC @surprised "GAHH!"
                MC @angry "Fucking birds!"
                "Inside the barrel... a demon key."
                $ PlayerAddItem("qst_blue_demon_key")
                jump qst_dreamhouse_l4_cellar_barrel_menu
            "Step back":
                $ LocEnterQ()
    else:
        $ LocEnterQ()

#Note on wall - (Clue for the correct barrel)
label qst_dreamhouse_l4_cellar_paper:
    "In the cellar where the dead things keep,"
    "Four sealed casks lie in patient sleep."
    "One breathes rot, one bleeds, one flies—"
    "One alone still softly spies."
    "Break the watcher, claim your prize."
    $ LocEnterQ()

# LIBRARY ROOM (l4) (door is initially locked - opened by dragon key)
label qst_dreamhouse_l4_diningroom_to_library:
    MC "(Locked.)"
    MC "(There must be a key somewhere.)"
    menu:
        "Insert dragon key" (AppearIf = PlayerHasItem("qst_dragon_key")):
            $ PlayerRemItem("qst_dragon_key")
            MC "(There.)"
            $ QstDreamhouse().L4_UnlockedLibrary = True
            $ LocEnterQ()
        "Step away.":
            $ LocEnterQ()


# Clickables 
#1 fireplace
label qst_dreamhouse_l4_library_fireplace:
    $ PlaySound(audio.fire_burning)
    "The fire is dim, but still crackling..."
    $ LocEnterQ()

#2 bookshelf 1
label qst_dreamhouse_l4_library_bookshelf_1:
    menu qst_dreamhouse_l4_library_bookshelf_1_menu:
        "Read {i}My new nightmare.{/i}":
            "It's something new now."
            "Not the same old faces who would visit me every night."
            "This one speaks to me."
            "It says it wants to be free."
            "That my mind is a prison."
            "... It... It's just another nightmare."
            "Right?"
            jump qst_dreamhouse_l4_library_bookshelf_1_menu
        "Read {i}My first rejection.{/i}" (AppearIf = QstDreamhouse().L4_LibSeenBurningBook == False):
            $ QstDreamhouse().L4_LibSeenBurningBook = True
            "{i}He said no.{/i}"
            $ PlaySound(audio.burst_into_flames)
            "The book suddenly burst into flames in my hands!"
            MC @surprised "FUCK!"
            $ DamagePlayer(5, Lethal = False)
        "Read {i}My new mother.{/i}":
            "Mother has just told me her friend, the lady with the cat tail, is now also my mommy."
            "She seems nice, but maybe a little strict."
            "... But I don't think I need another mother."
            "I just really miss father."
            jump qst_dreamhouse_l4_library_bookshelf_1_menu
        "Read {i}Where is father?{/i}":
            "I see father less and less."
            "It's been months now."
            "... Maybe he's just never coming back?"
            "Mother is talking about us leaving and heading to live in a place far away."
            "If that happens, will father still visit?"
            "{i}... Does he still love me?{/i}"
            jump qst_dreamhouse_l4_library_bookshelf_1_menu
        "Step back":
            pass
    $ LocEnterQ()

#3 bookshelf 2
label qst_dreamhouse_l4_library_bookshelf_2:
    menu qst_dreamhouse_l4_library_bookshelf_2_menu:
        "Read {i}A man tried to take me tonight.{/i}" (AppearIf = QstDreamhouse().L4_LibSeenGreenSkullBook == False):
            $ QstDreamhouse().L4_LibSeenGreenSkullBook = True
            "A man tried to kidnap me tonight. Thankfully, our guards managed to stop him."
            "My mothers are terrified, but..."
            "I'm more frightened about what I might dream happens tonight."
            "... Between the pages, a green skull key fell out."
            $ PlayerAddItem("qst_green_skull_key")
            jump qst_dreamhouse_l4_library_bookshelf_2_menu
        "Read {i}lonely{/i}":
            "I wish I had more actual friends."
            "I mean, the people at the academy are fine,"
            "but it's all cliques and coin and..."
            "No one is friends with anyone, really. It's all just strategic alignments."
            "... Fuck, I just wish someone was real for once."
            jump qst_dreamhouse_l4_library_bookshelf_2_menu
        "Read {i}Father came back!{/i}":
            "Father returned with a strange man."
            "He said the two of them were going to help me get rid of the nightmares once and for all."
            "Father... You still remembered me!"
            jump qst_dreamhouse_l4_library_bookshelf_2_menu
        "Read {i}A strange dream...{/i}":
            "I had a strange dream tonight. A man, handsome with black hair."
            "But he wasn't fully human. Inside of him... there was another soul."
            "He swore he would save me, but it's so strange..."
            "I've never even seen this man before in my life?"
            jump qst_dreamhouse_l4_library_bookshelf_2_menu
        "Step back":
            pass
    $ LocEnterQ()

#4 Portrait of a book with a key hidden inside it.
label qst_dreamhouse_l4_library_portrait:
    "Why would anyone paint this?"
    $ LocEnterQ()

##################################################################################################################################
#LAYER 5 - SWAMP HOUSE 
##################################################################################################################################
label qst_dreamhouse_l5_start:
    $ QstDreamhouse().HouseStage = 5
    if PlayerHasItem("qst_orange_demon_key"):
        $ PlayerRemItem("qst_orange_demon_key", Silent = True, MuteSfx = True)
    if PlayerHasItem("qst_red_demon_key"):
        $ PlayerRemItem("qst_red_demon_key", Silent = True, MuteSfx = True)
    if PlayerHasItem("qst_white_demon_key"):
        $ PlayerRemItem("qst_white_demon_key", Silent = True, MuteSfx = True)
    if PlayerHasItem("qst_blue_demon_key"):
        $ PlayerRemItem("qst_blue_demon_key", Silent = True, MuteSfx = True)
    $ LocSet("dreamhouse_hallway")
    $ LocFlush(dissolve)
    show mc at cleft with easeinleft
    show markus at cright_f with easeinright
    "As we pushed on once more through the bright light, we found ourselves again in the entrance hallway of the house,"
    "only to face a brand new horror..."
    MARKUS @scared "The house is flooded!"
    hide markus with easeoutleft
    show sypha at left with easeinleft
    show sypha at shake
    SYPHA @angry "Urgh... This better not ruin my clothes!"
    if CharInParty("ves"):
        show ves at cright_f with easeinright
        VES @talk "How much more of this damn house is there?!"
    show kiara at right_f with easeinright
    KIARA @sad "Brrr! This water's so cold!"
    hide ves with dissolve
    KIARA @sad "I can't see a damn thing beneath it!"
    hide kiara with dissolve
    show mc at center with ease
    $ PlaySound(audio.water_splash)
    "Hearing something splash, I quickly turned my attention toward it."
    show mc at blurin, center_f
    MC @serious "What was that?"
    show sypha at cleft with ease
    SYPHA @talk "I don't know, but the last thing we should do is wait around and find out..."
    $ LocEnter()

#UPSTAIRS are not as flooded but damp
#BATHROOM (l5) Clickables
#1 Bathtub
label qst_dreamhouse_l5_bathtub:
    "It's completely rotten away and covered in mold."
    $ LocEnterQ()
label qst_dreamhouse_l5_mirror:
#2 - dirty mirror
    "It's caked in so much dirt, I can't see anything reflected."
    $ LocEnterQ()


# door to Hallway2 is locked and needs GATOR key to escape
label qst_dreamhouse_l5_upstairs_to_hallway2:
    MC "(Locked...)"
    menu:
        "Insert gator key" (AppearIf = PlayerHasItem("qst_gator_key")):
            $ PlayerRemItem("qst_gator_key")
            $ QstDreamhouse().L5_Hallway2Unlocked = True
            MC "(That does it.)"
            $ LocEnterQ()
        "Step back":
            $ LocEnterQ()

# Left door - nursery
#Clickables (l5)
#1 - destroyed Toys 
label qst_dreamhouse_l5_toys:
    "The toys are completely ruined by the damp..."
    $ LocEnterQ()
#2 - Crib
label qst_dreamhouse_l5_crib:
    $ QstDreamhouse().L5_TookCribKey = True
    "The crib is damp and covered in mold. The wood is completely rotten."
    "There is a key inside."
    $ PlayerAddItem("qst_snake_key")
    $ LocEnter()

#Master bedroom door in hallway2, PURPLE SKULL KEY needed to unlock
label qst_dreamhouse_l5_bedroom_door:
    MC "(It's locked.)"
    MC "(I need a key...)"
    menu:
        "Insert purple skull key" (AppearIf = PlayerHasItem("qst_purple_skull_key")):
            $ PlayerRemItem("qst_purple_skull_key")
            $ QstDreamhouse().L5_BedroomUnlocked = True
            MC "(There...)"
            $ PlaySound(audio.magic_earthy_cast1)
            scene black with flash
            jump qst_dreamhouse_final_housescene
        "Step back":
            $ LocEnterQ()

#DOWNSTAIRS
label qst_dreamhouse_l5_candle:
    #The player clicks on lit candle in main hallway
    MC @think "(A purple flame now...)"
    $ LocEnterQ()

#DINING HALL (l5)
# Clickables in the room 
# 1 Ruined table
label qst_dreamhouse_l5_table:
    "(The table is completely rotten and overrun with mold and vines.)"
    $ LocEnterQ()
#2 Mounted lizard head 
label qst_dreamhouse_l5_head:
    "(The mounted head of a lizard, eroded and filthy.)"
    $ LocEnterQ()
#3 portrait of house in a swamp.
label qst_dreamhouse_l5_portrait:
    "A portrait of a derelict house in swamp land."
    $ LocEnterQ()


#KITCHEN (l5)
# Clickables in the room 
# 1 - cupboards 
label qst_dreamhouse_l5_kitchen_cupboards:
    "Completely empty and rotten."
    $ LocEnterQ()
# 2 - cooking pot
label qst_dreamhouse_l5_kitchen_pot:
    MC "(The fire is out. There's nothing in the pot other than black, pungent water.)"
    $ LocEnterQ()


# WINE CELLAR l5 (Locked) - Requires the snake key to open
label qst_dreamhouse_l5_kitchen_to_cellar:
    MC "(Locked...)"
    menu:
        "Insert snake key" (AppearIf = PlayerHasItem("qst_snake_key")):
            $ PlayerRemItem("qst_snake_key")
            $ QstDreamhouse().L5_UnlockedCellar = True
            MC "(That does it.)"
            $ LocEnterQ()
        "Step back":
            $ LocEnterQ()

# 1 Destroyed Wine barrel
label qst_dreamhouse_l5_cellar_barrel:
    "There's nothing left..."
    $ LocEnterQ()
# 2 rotting desk
label qst_dreamhouse_l5_cellar_paper:
    $ QstDreamhouse().L5_TookCellarKey = True
    "There... carefully placed in the center of the desk, a purple skull key."
    $ PlayerAddItem("qst_purple_skull_key")
    $ LocEnter()

# LIBRARY ROOM (l5)
#Clickables 
label qst_dreamhouse_l5_library_fireplace:
#1 fireplace
    $ QstDreamhouse().L5_TookGatorKey = True
    "The fire is out and completely soaked."
    "There though, hidden beneath a wet, rotten log, is a key with a lizard-shaped head."
    $ PlayerAddItem("qst_gator_key")
    $ LocEnterQ()

#2 bookshelf 1
label qst_dreamhouse_l5_library_bookshelf_1:
    "The books are all soaking wet and destroyed."
    $ LocEnterQ()

#3 bookshelf 2
label qst_dreamhouse_l5_library_bookshelf_2:
    "The pages are completely illegible."
    "A book literally rots away in my hand as I try to pick it up."
    $ LocEnterQ()

#4 Portrait of two yellow eyes above a dark waterline
label qst_dreamhouse_l5_library_portrait:
    "... Creepy."
    $ LocEnterQ()


label qst_dreamhouse_l5_gator_counter:
    if GetLocID() not in ["dreamhouse_hallway", "dreamhouse_diningroom", "dreamhouse_library", ",dreamhouse_kitchen", "dreamhouse_hallway_upstairs", "dreamhouse_bathroom", "dreamhouse_cellar", "dreamhouse_hallway2", "dreamhouse_nursery"]:
        $ LocEnterQ()

    ## increment counter
    $ QstDreamhouse().L5_GatorCounter += 1
    if QstDreamhouse().L5_GatorCounter < 8:
        if QstDreamhouse().L5_GatorCounter > 4:
            $ tmpvar = RngInt(1, 2)
            if tmpvar == 1:
                $ PlaySound(audio.water_splash)
            else:
                $ PlaySound(audio.reptile_hiss)
            $ tmpvar = {}
        $ LocEnterQ()
    $ QstDreamhouse().L5_GatorCounter = 0

    #if GATOR APPEARS when sound meter is full.
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    show cg_gator at center with flash

    $ PlaySound(audio.water_splash)
    "Suddenly, erupting from the water, a terrible, lizard-like creature snapping its jaws blocked our path!"
    $ PlaySound(audio.reptile_hiss)
    MC @angry "Shit!"

    $ StartBattle(BattleData(BackgroundImage = "pbat_ghost_house_flood", CharIDList_Right = [{"e_gator":10}]))
    $ LocFlush(dissolve)

    if len(player_party) == 1:
        $ AutoMus(True)
        $ LocEnter()

    $ tmpvar = renpy.random.choice([x for x in player_party if x != "mc"])
    # GATOR SNATCHES A PARTY MEMBER VARIANTS
    # Kiara snatched 
    if tmpvar == "kiara":
        show mc at cright_f
        show kiara at cleft
        with dissolve
        KIARA @scared "What in the world is that thing?!"
        KIARA @talk "Phew... That was close, he almost-"
        "The creature suddenly lunged forward, grabbing hold of Kiara as it dragged her down towards the black water."
        show kiara at shake
        KIARA "AHHHHH!"
        hide kiara with dissolve
        show mc at center_f with ease
        show mc at shake
        $ QstDreamhouse().GatorEatsChar("kiara")
        MC @surprised "KIARA!"
        "The creature dived."
        $ PlaySound(audio.water_splash)
        "It moved quickly, its scaled tail swaying through the black water for a moment before it dipped beneath the darkness."
        show mc at shake
        MC @surprised "KIARA! CAN YOU HEAR ME? KIARA!"
        MC "(Damn it!)"
    #Ves snatched
    elif tmpvar == "ves":
        show ves at center
        with dissolve
        $ PlaySound(audio.reptile_hiss)
        "Ves wrestled with the creature as it snarled and hissed."
        show ves at shake
        VES @angry "BACK YOU BEAST! I SAID-"
        "With a swipe of its tail, it tripped Ves to the floor."
        hide ves with dissolve
        $ QstDreamhouse().GatorEatsChar("ves")
        "She gasped, as the creature grabbed at her leg and began to pull her away with tremendous speed and power!"
        show mc at cleft with easeinleft
        MC @surprised "VES!"
        $ PlaySound(audio.water_splash)
        "There was a great deal of splashing as Ves vanished beneath the dark water... then silence."
        show mc at center with ease
        MC @sad "Ves... No..."
    #Markus snatched
    elif tmpvar == "markus":
        show markus at center with dissolve
        show markus at shake
        MARKUS @angry "FUCK OFF, FUCK OFF, FUCK OFF!"
        "Markus furiously struck at the creature, which for a moment seemed like it might limp away."
        hide markus with dissolve
        $ PlaySound(audio.reptile_hiss)
        "With a defiant hiss, he charged towards Markus, knocking him off his feet as he charged straight towards the black water!"
        show mc at cleft with easeinleft
        MC @angry "MARKUSSSS!"
        $ QstDreamhouse().GatorEatsChar("markus")
        $ PlaySound(audio.water_splash)
        "Markus struggled as a tremendous splash erupted in the black waters... and then... nothing."
        show mc at center with ease
        MC @scared "(Markus...)"
        MC @scared "(Don't you dare die on me!)"
    #Sypha snatched
    elif tmpvar == "sypha":
        show sypha at center with dissolve
        "The creature whined as it retreated and lowered itself for a moment."
        SYPHA @happy "Ha! How pitiful!"
        SYPHA @happy "Starting a fight and then cowering when you realize you can't even fin-"
        "Suddenly, the gator flung itself forward!"
        show sypha at shake
        SYPHA @shock "{i}*Gasp!*{/i}"
        hide sypha with dissolve
        "Before she could react, she and the gator were rolling across the ground as she struggled against it."
        SYPHA "GET OFF OF ME!"
        $ QstDreamhouse().GatorEatsChar("sypha")
        $ PlaySound(audio.water_splash)
        "I hurried to help her, but before I knew it, the creature had dragged her beneath the black waters... and there was only silence."
        show mc at center with easeinleft
        show mc at shake
        MC @surprised "SYPHA!"
    # other party member snatched
    else:
        $ PlaySound(audio.reptile_hiss)
        "The creature snarled, desperately charging towards us."
        show mc at center with dissolve
        MC @surprised "NO!"
        $ PlaySound(audio.water_splash)
        "As it dragged another member of my party beneath the black water with a splash, I waited for something... anything... to resurface."
        $ QstDreamhouse().GatorEatsChar(tmpvar)
        "... But nothing came."
        show mc at shake
        MC @surprised "Where did they go?!"
        "The black water calmed as it rippled softly... And then there was silence."
    $ tmpvar = {}
    $ AutoMus(True)
    $ LocEnter()

############################################################################################################################################
# AFTER ENTERING INTO THE MASTER BEDROOM IN L5 THE SCENE CONTINUES 
label qst_dreamhouse_final_housescene:
    $ QstDreamhouse().HouseStage = 6 # <- this is to kill all stage related logic
    $ QstDreamhouse().RestoreGatorTakenChars()
    "This time, as we pushed through the doorway, we found ourselves, for the first time, not looping back to the entrance hallway,"
    "but within the master bedroom itself at last... Or at least,"
    "what I thought was supposed to be the master bedroom."
    "Looking behind me, I could see everyone was back—dazed and confused, perhaps—but... alive and present."
    $ GoalComplete(QstDreamhouse, 5)
    scene cg_dreamscape with dissolve
    show mc at cleft with easeinleft
    show cg_virgo at cright_f with easeinright
    show serafina at right_f with easeinright
    with dissolve
    "A blonde girl turned to face me as I entered. Stood stoically behind her, an elderly mage watched."
    VIRGO "Ah, good, you made it through."
    SERAFINA @shock "You..."
    SERAFINA @shock "You're the one from my dreams!"
    MC @think "What?"
    VIRGO "Where is Davik? Did he send for you?"
    MC @talk "No, we were sent here by the girl's mothers."
    "I raised a brow at the youthful face in front of me."
    MC @think "You're Serafina, I take it?"
    "The girl nodded."
    SERAFINA @sad "Where is father?"
    SERAFINA @sad "He went back through the house to gather supplies."
    SERAFINA @scared "We need him back before {i}it{/i} comes!"
    MC @think "{i}It?{/i}"
    VIRGO "This house was designed for containment."
    VIRGO "A place to store and contain her nightmares..."
    VIRGO "And hopefully, to gain mastery of her powers."
    show sypha at left with easeinleft
    with dissolve
    SYPHA @talk "You still haven't answered what {i}it{/i} is."
    "Around us, the world seems to bend and crackle, as {i}something{/i} fights its way through."
    "Serafina's eyes glow purple, bleeding tears streaming down her face as she clutches her head, teeth gritted in pain."
    SERAFINA @scared "I can't hold it back much longer!"
    VIRGO "The heart of her fears—it has manifested itself as this creature."
    VIRGO "And it refuses to stay a prisoner here."
    $ PlaySound(audio.thunder)
    "The sky ripples and tears as the creature begins to force its way into this reality."
    MC @serious "What do we do?"
    "With a tap of his staff, I felt a surge of energy rush through me!"
    # Party is fully healed 
    $ HealParty(NotifyLine = _("Your party is fully healed!"))
    show cg_virgo at cright 
    hide cg_virgo with easeoutright
    VIRGO "Damn it... It seems we can wait no longer for your father, Serafina."
    "The dark mage motioned to all of us."
    VIRGO "You hold the creature back!"
    VIRGO "{i}I'll seal the rift...{/i}"
    show markus at center with easeinleft
    with dissolve
    MARKUS @scared "That's..."
    MARKUS @scared "{i}big.{/i}"
    "Kiara and Sypha readied themselves."
    SYPHA @angry "The power radiating from that thing... This won't be easy!"
    if CharInParty("ves"):
        "Ves tightened her hands around her axe."
        VES @angry "Let it come!"
    "The sky ripped open, revealing a black void behind it."
    "Two great, pale hands reached through as the creature's head pushed through the darkness,"
    "scowling at us as it opened its mouth to roar!"
    $ PlaySound(audio.scorpion_roar)
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    MC @surprised "Here we go!"
    MC @angry "ALL AT ONCE!"
    # Boss battle against the nightmare - After winning
    $ StartBattle(BattleData(BackgroundImage = "pbat_dreamscape", CharIDList_Right = [{"e_nightmare_head":16}, {"e_nightmare_right_hand":11}, {"e_nightmare_left_hand":16}]))
    $ AutoMus(True)
    VIRGO "NOW!"
    scene cg_dreamhouse_nightmare_retreats with dissolve
    "The nightmare creature retreated, pushed back into the darkness from which it tore through."
    "With trembling hands, Virgo's body was pushed to its aboslute limits, the veins in his arms and temples seeming ready to burst at any moment,"
    "the great tear was slowly sealed shut, until at last, it was gone."
    scene cg_dreamscape
    show cg_virgo at cright_f
    with dissolve
    "Dropping to his knees breathlessly, he looked up towards us."
    show mc at left with easeinleft
    show serafina at right_f with easeinright
    VIRGO "Thank you... Your assistance was..."
    VIRGO "welcomed."
    "No sooner had he finished than Davik appeared through the doorway."
    show cg_davik at cleft with easeinleft
    DAVIK "Serafina! SERAFINA!"
    SERAFINA @smile "Father!"
    DAVIK "Are you alright, girl?"
    DAVIK "What happened?"
    SERAFINA @smile "It's alright... Father."
    SERAFINA @smile "We did it, we sealed it away!"
    DAVIK "Thank the gods..."
    "Davik turned towards me."
    show cg_davik at cleft_f
    with dissolve
    DAVIK "You have my eternal thanks for helping save my daughter."
    show cg_davik at cleft
    with dissolve
    DAVIK "Come, Serafina, let's go..."
    MC @think "Wait, hold for a moment."
    MC @talk "I've been ordered to bring Serafina back to her mother."
    show cg_davik at cleft_f
    with dissolve
    DAVIK "You must think me a fool to just hand her back over!"
    DAVIK "Not after all these years!"
    VIRGO "WAIT!"
    VIRGO "Both of you..."
    show cg_davik at cleft
    with dissolve
    "Slowly, the dark mage rose back to his feet."
    VIRGO "Bring the girl back to her mothers and let me take the girl as an apprentice."
    DAVIK "ARE YOU INSANE?"
    DAVIK "Your vile services were hired just to help me protect MY daughter!"
    DAVIK "I'm an inquisitor! You really think I'm going to let a fucking dark mage tutor her?"
    DAVIK "No! She will come back with me to Novaras. There, she will learn under the Inquisition."
    VIRGO "Don't be a fool!"
    VIRGO "The Inquisition will only leash her!"
    VIRGO "Her power is too valuable! With my help, she could learn to master it and turn the tide of this war!"
    SERAFINA @shock "S-STOP FIGHTING!"
    SERAFINA @sad "... You."
    "Serafina's gaze turns towards me."
    SERAFINA @sad "What do you think I should do?"
    DAVIK "You can't seriously be—"
    SERAFINA @talk "I saw him... {i}father.{/i}"
    SERAFINA @talk "In my dreams."
    SERAFINA @talk "I think he's the one to tell me which way to go!"
    VIRGO "... Interesting."
    SERAFINA @talk "So then... What do you think I should do?"
    # remember both outcomes
    menu: 
        "Go with your father, the Inquisition will teach you how to control your power.":
            $ QstDreamhouse().SerafOutcome = "father"
            SERAFINA @sad "If... If that is the path you think I should take."
            SERAFINA @talk "Father, I'll come with you."
            VIRGO "Damn fools."
            VIRGO "You're wasting your potential with the Inquisition!"
            VIRGO "They'll show you the ceiling, but never show you how to break through it!"
            DAVIK "And that's fine with me!"
            DAVIK "She's my daughter, not a damn weapon!"
            VIRGO "No... Now she's going to become something worse."
            VIRGO "Just a puppet for the Inquisition."
            "Davik carefully took his daughter's hand."
            DAVIK "Come on, let's leave this place. We have a long journey ahead of us."
            show cg_davik at cleft_f
            with dissolve
            "Davik turned to me once more, nodding."
            DAVIK "I promise you, I will repay this debt."
            VIRGO "Tschh...!"
            SERAFINA @shock "Wait! Father!"
            show cg_davik at cleft
            with dissolve
            SERAFINA @talk "Before we go..."
        "Come home and learn under Virgo, if we lose the war, nothing else matters.":
            $ QstDreamhouse().SerafOutcome = "virgo"
            VIRGO "Finally, someone making sense."
            DAVIK "You cannot seriously expect me to just let you take—"
            "As he reached for the hilt of his blade, Serafina stepped in to stop him, grabbing at his hands."
            SERAFINA @shock "Father! No!"
            DAVIK "Serafina, I—"
            SERAFINA @sad "He's right, father."
            SERAFINA @sad "This power... If I can wield it better, I can do some good."
            DAVIK "You cannot trust a dark mage, Serafina!"
            DAVIK "If you walk this path... I... I don't know if I can—"
            SERAFINA @sad "Father... {i}I have to do this.{/i}"
            SERAFINA @sad "I have to try."
            DAVIK "..."
            show cg_davik at cleft_f
            with dissolve
            "Davik turned towards me."
            DAVIK "I won't forgive you for this."
            show cg_davik at cleft
            with dissolve
            VIRGO "Come, Serafina."
            VIRGO "Let us take you home."
            SERAFINA @talk "Wait!"
    #Both choices continued
    SERAFINA @sad "... In my dreams, I saw {i}things.{/i}"
    MC @think "Things?"
    SERAFINA @sad "I saw you on a throne with a blood-stained crown."
    SERAFINA @sad "Amidst a battlefield, skulls at your feet."
    SERAFINA @sad "... And a dozen knives in your back."
    MC @surprised "I..."
    SERAFINA @sad "I wish you well in what's to come."
    SERAFINA @sad "... I think you're going to need it."
    MC @serious "Your dreams then, they can show you the future?"
    SERAFINA @sad "No... More like something that can be."
    "She lowered her head."
    SERAFINA @sad "I'm sorry I can't help you more,"
    SERAFINA @sad "but while we are here..."
    "Closing her eyes, Serafina waved her hand towards us."
    SERAFINA @talk "{i}I can dream you and your friends are better.{/i}"
    # Party fully healed - infection dropped to zero
    $ HealParty(NotifyLine = _("Your party is fully healed!"))
    $ InfChangeBy(0, SetTo = True)
    play sound "audio/cfx/detect_magic.ogg"
    MC @surprised "That was..."
    SERAFINA @talk "Before I go."
    SERAFINA @smile "What is your name?"
    MC @smile "[player_name]."
    "Serafina smiles warmly."
    SERAFINA @smile "Then I look forward to seeing you again soon, [player_name]."
    $ PlaySound(audio.finger_snap)
    "With that, Serafina snapped her fingers, and there was a bright flash."


    $ PlaySound(audio.magic_earthy_cast1)
    $ LocSet("ancient_forest")
    $ LocFlush()
    show mc at cleft
    show kiara at cright_f
    with flash
    #The player and party are outside the dream house 
    MC @surprised "I... Where are—"
    $ GoalComplete(QstDreamhouse, 4)
    show markus at right_f with easeinright
    MARKUS @smile "Oh, thank the gods we made it out of that place!"
    hide markus with dissolve
    KIARA @smile "Air... Sunlight... Warmth!"
    show sypha at left with easeinleft
    "Sypha pointed towards something."
    SYPHA @think "Is that not the wagon that the shop woman was looking for?"
    "I turned to follow her finger, and indeed, now placed as though it had always been there, a wagon and two horses."
    MC @smile "I think it is."
    $ GoalComplete(QstDreamhouse, 3)
    if CharInParty("ves"):
        show ves at right_f with dissolve
        VES @think "How did it get here?"
        MARKUS @smile "Don't know, don't care!"
        MARKUS @smile "First bit of luck we've had since taking on this wretched job!"
        hide ves with dissolve

    hide sypha with easeoutright
    show kiara at blurin, cright
    hide kiara with easeoutright
    MC @talk "Well, at least this makes the journey back easier."
    show mc at center with ease
    MC "(I just hope Serafina and the others are alright.)"
    MC @serious "(What she said about her dream with me...)"
    MC @serious "(Surely that was just some trickery, right?)"
    MC @smile "(Me... A crown? A throne? I mean, it's not possible, I don't—)"
    show markus at right_f with easeinright
    MARKUS "Stop standing there and smirking to yourself and get in!"
    MC @talk "Oh, right...!"
    scene black with dissolve

    # skip a couple days
    # Fade to black - cut back to Hamun and skip the travel (Possible story CG here)
    $ InfGainDaily(False)
    $ TimeAdvBy(TIME_1H * 12)
    $ TimeAdvBy(TIME_1H * 12)
    $ TimeAdvBy(TIME_1H * 12)
    $ TimeAdvBy(TIME_1H * 12)
    $ TimeAdvTo(TIME_VISUAL_DUSK)
    $ InfGainDaily(True)
    "... The ride back was long,"
    "but certainly quicker than how we had travelled before."
    "When we arrived upon Hamun, I returned the wagon to Katiya."
    $ LocSet("hamun_general_store")
    $ LocFlush()
    show mc at cleft
    show katiya at cright_f
    with dissolve
    KATIYA @happy "You're alive!"
    KATIYA @talk "I mean, uh... Well done!"
    #KATIYA @happy "Your reward, as requested."
    # Reward(s) dependent on previous interaction
    # nope she already fucking gives the reward when you commit
    KATIYA @think "And my man, is he..."
    MC @sad "I'm sorry, we didn't find him."
    KATIYA @sad "I see..."
    KATIYA @sad "Well, all our fates are in the hands of the gods in the end."
    KATIYA @sad "Perhaps he just got lucky and..."
    "She doesn't finish the sentence."
    KATIYA @talk "Anyway, I won't keep you."
    KATIYA @talk "Come by the shop anytime if you need anything."
    MC @smile "Will do, Katiya."
    hide katiya with dissolve
    # Katiya exits off screen
    show mc at center with ease
    MC "(Now to report back to the Faymore women and conclude this business at last.)"
    $ GoalShow(QstDreamhouse, 6)
    $ LocEnter()

#Upon returning to the Faymore estate the event can play out two ways depending on choice:
label qst_dreamhouse_return_after_rescue:
    if config.developer:
        "DEBUG: set serafina decision to? currently set to '[QstDreamhouse().SerafOutcome]'"
        menu:
            "DEBUG: leave with her father":
                $ QstDreamhouse().SerafOutcome = "father"
            "DEBUG: study under virgo":
                $ QstDreamhouse().SerafOutcome = "virgo"
                "DEBUG: set reward chosen to? currently set to '[QstDreamhouse().ChosenReward]' (0 == ass 1 == coin)"
                menu:
                    "DEBUG: set to ass":
                        $ QstDreamhouse().ChosenReward = 0
                    "DEBUG: set to coin":
                        $ QstDreamhouse().ChosenReward = 1

    $ GoalComplete(QstDreamhouse, 6)
    if QstDreamhouse().SerafOutcome == "father":
    #Variant 1: The player told Serafina to leave with her father.
        jump qst_dreamhouse_conclusion_serafina_father
    elif QstDreamhouse().SerafOutcome == "virgo":
        jump qst_dreamhouse_conclusion_serafina_virgo
    
label qst_dreamhouse_conclusion_serafina_father:
    "No sooner had I entered the estate's walls than I was beset by a furious Chanyi and a tearful Anya."
    show mc at center with easeinleft
    show chanyi angry at cright_f with easeinright
    show anya sad at cleft with easeinleft
    CHANYI @angry "WHERE IS SHE?"
    CHANYI @angry "WHERE IS OUR DAUGHTER?"
    ANYA @sad "Serafina wrote us a letter. She said she is safe but is heading to Novaras with her father!"
    MC @talk "Your daughter is safe."
    MC @talk "But she is with her father to learn how to—"
    "Anya burst into tears, covering her face with her hands."
    show anya at shake
    ANYA @sad "No!"
    show chanyi at shake
    CHANYI @angry "You idiot! You were supposed to bring her back to us!"
    menu:
        "She needs to learn to control her powers, the Inquisition will teach her how.":
            show chanyi at shake
            CHANYI @angry "FUCK THE INQUISITION!"
            CHANYI @angry "Damn you! It wasn't your choice to make!"
            ANYA @sad "Chanyi... I..."
            ANYA @sad "Maybe it's for the best."
            CHANYI @shock "What?!"
            ANYA @sad "Serafina... She needs... She needs people who can help her, who can—"
            CHANYI @angry "It wasn't his choice to make!"
            pass
        "I did what was best for Serafina.":
            show chanyi at shake
            CHANYI @angry "What was best for her was bringing her back to US!"
            CHANYI @angry "Her fucking father is an inquisitor!"
            CHANYI @angry "What if they just decide she's too dangerous to keep alive, hmm?"
            CHANYI @angry "Or that her powers are tainted by dark magecraft?"
            show chanyi at shake
            CHANYI @angry "WHAT THEN, HMM?"
            ANYA @sad "Chanyi... Please... Please stop."
            pass
    #Both variants continued
    MC @sad "I'm sorry, but if you saw what I saw..."
    MC @sad "you'd understand why her powers need guidance and—"
    show chanyi at shake
    CHANYI @angry "Get out, GET OUT!"
    CHANYI @angry "FUCKING LEAVE US!"
    "Grabbing a half bag of coins, Chanyi flung it towards me angrily."
    CHANYI @angry "Half pay for half a fucking job!"
    $ PlayerAddItem("gold", 2500)
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocFlush()
    show mc at cleft
    with dissolve
    MC @sad "... That could have gone better."
    show kiara at cright_f with easeinright
    KIARA @sad "Did you really expect any other reaction from them?"
    MC @think "So you think I chose wrong?"
    KIARA @sad "No, just... I don't think they'd ever see it that way."
    show markus at left with easeinleft
    MARKUS @talk "You made the right call... They mean well, but..."
    MARKUS @talk "If she doesn't learn to control that power and get a grip on it, she could become too dangerous."
    hide markus with dissolve
    show sypha at right_f with easeinright
    SYPHA @sad "With your inquisitors, she may now never fully know what she was capable of."
    SYPHA @sad "How... sad."
    MC @think "Do you really think another dark mage is what this world needs?"
    SYPHA @talk "Are you so sure it doesn't?"
    if CharInParty("ves"):
        show ves at left with easeinleft
        VES @talk "She's a strong girl."
        VES @smile "I believe whatever path she walks, she will be alright."
    $ QstSetProgress(HouseLockFaymoreManor, 2)
    $ QstComplete(QstDreamhouse)
    $ LocEnter()

# VARIANT 2: The player told Serafina to study under Virgo
label qst_dreamhouse_conclusion_serafina_virgo:
    show serafina at cleft
    show anya at left
    show chanyi at center
    show cg_virgo at right_f
    with dissolve
    "Upon entry, the two Faymore women stood beside Serafina, but their eyes were firmly locked onto the dark mage beside her, explaining everything."
    VIRGO "So you see, that is why it is imperative you allow me to continue her—"
    show serafina at shake
    SERAFINA @smile "[player_name]!"
    MC @smile "Serafina."
    CHANYI @talk "This... mage here was explaining everything that has happened."
    show anya at nod
    ANYA @happy "Thank you, thank you, thank you, thank you!"
    ANYA @happy "You've brought our daughter home!"
    "Chanyi smiled as well, but she seemed more... reserved and unsure."
    CHANYI @serious "So just to be clear, you wish to stay here and tutor our daughter, yes?"
    VIRGO "Yes."
    CHANYI @serious "And you are..."
    "She paused for a moment."
    CHANYI @serious "A dark mage, yes?"
    VIRGO "... Yes."
    "There was a long, awkward pause."
    CHANYI @serious "You can see why this might make us worried, right?"
    VIRGO "I do."
    SERAFINA @talk "Mothers, I promise you."
    SERAFINA @talk "Virgo is a good man, he's just... {i}different.{/i}"
    "The mage didn't shift an inch."
    "Chanyi stared, but didn't answer."
    "Anya, though, clapped her hands together and smiled."
    ANYA @happy "We shall have a guest room made up for you."
    "The mage offered a curt bow."
    VIRGO "You honor me."
    CHANYI @serious "... We will discuss later what you plan to teach our daughter."
    CHANYI @serious "{i}And boundaries.{/i}"
    SERAFINA @shock "Mother!"
    CHANYI @serious "This is for the best, Serafina."
    ANYA @sad "Chanyi is right, Sera, we have to keep you safe, and this is still—"
    VIRGO "It is only fair you are concerned for your daughter's wellbeing."
    VIRGO "I can assure you, I do not seek to harm her."
    VIRGO "{i}... Only to study and learn more myself of her great power.{/i}"
    "For some reason, that answer hadn't quite sat right with me."
    "But... all mages pursue knowledge of magecraft."
    "Especially dark mages."
    SERAFINA @smile "I'm pretty tired, so I might lay down for a while to rest."
    VIRGO "We will begin training soon, young mistress."
    SERAFINA @think "You know I hate it when you call me that..."
    VIRGO "Yes... Serafina."
    hide serafina with dissolve
    hide cg_virgo with dissolve
    "Serafina returned to her quarters as Virgo was escorted away by one of the servants."
    show anya at cleft with ease
    CHANYI @think "Well... I can't say I don't have mixed feelings on the outcome."
    ANYA @happy "Our daughter is back, Chanyi, that's all that matters."
    CHANYI @laugh "{i}*Sigh*{/i} I suppose it is."
    CHANYI @laugh "Now then..."
    "Chanyi raised a brow."
    CHANYI @laugh "Let us discuss your reward."
    if QstDreamhouse().ChosenReward == 1:
        ANYA @happy "Here, please, take it."
        show anya at nod
        $ PlayerAddItem("gold", 5000)
        CHANYI @laugh "And we mentioned something a little more {i}special{/i} than just coin, didn't we?"
        "With a snap of her fingers, servants entered the room with some of the most beautiful armor I had ever seen, radiating a soft magecraft."
        MC @surprised "What is this?"
        ANYA @happy "Armor worn by my great, great grandfather."
        ANYA @happy "Strigon Faymore."
        ANYA @happy "One of the greatest knights of his age."
        ANYA @happy "For generations, we have done our best to maintain his armor."
        ANYA @talk "And now... we gift it to you."
        $ PlayerAddItem("faymore_armor")
        $ PlayerAddItem("faymore_blade")
        CHANYI @talk "And with that, our business is concluded."
        CHANYI @talk "Do come by from time to time, I do believe Serafina would appreciate it."
        CHANYI @serious "... And it might help keep that dark mage in line."
    elif QstDreamhouse().ChosenReward == 0:
        "The two women shared a knowing look at each other, Anya's cheeks flushed red as she bit at her lower lip."
        "Chanyi's tail swished back and forth seductively as she grinned."
        CHANYI @talk "Come back tomorrow evening."
        CHANYI @laugh "{i}We'll be waiting.{/i}"
    $ QstComplete(QstDreamhouse)
    $ LocEnter()
