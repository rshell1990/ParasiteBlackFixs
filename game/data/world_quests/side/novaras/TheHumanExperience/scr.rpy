label qst_HumanExp_0_checkup:
    show mc at cleft with easeinleft
    "Once Myu heard the door open, she ran out to greet me."
    show myu at center_f with easeinright
    MYU @joy "MYUUUU!"
    MC @smile "Ah! Easy!"
    MC @smile "You really are quite the excitable thing, aren't you?"
    show myu at cright_f with easeoutright
    "Her eyes looked pleadingly towards me, and as she looked down to her stomach, she began to rub at it."
    MC @think "...Are you hungry?"
    MYU @sad "Myuuuu."
    MC @talk "Hmm... Guess that makes sense."
    MC @talk "With all the growing you're doing, you're probably going to need some bigger portions too."
    MC "(Fuck... How much more growing is she going to do?)"
    MC "(There's no way I can hide her if she becomes the size of that thing in the lake.)"
    $ QstSetProgress(QstHumanExp, 1)
    if PlayerItemQty("red_meat") > 0:
        MC "(Good thing I still have some meat on me.)"
        $ PlayerRemItem("red_meat", 1)
        "As I held out the strips of meat in front of Myu, she snatched them and began to devour them quickly."
        MC @surprised "Easy! Not so fast!"
        "I watched as the meat was broken down and dissolved inside of Myu till there was nothing."
        jump qst_HumanExp_1_feedMyu_After
    else:
        MC @talk "Myu, I need to go get some food, understand?"
        "Myu tilted her head curiously."
        MC @serious "FOOD."
        "I began to rub my stomach and then point towards Myu."
        MC @serious "YOU. STAY. HERE."
        MYU @smile "Myu!"
        MC "Okay, I'll be back soon... Hide if someone comes."
        show mc at blurin, cleft_f
        hide mc with easeoutleft
        MYU @smile "Myu-u-u!"
        $ LocEnter()

label qst_HumanExp_1_feedMyuDialogue:
    MYU @joy "Myu!"
    $ PlayerRemItem("red_meat", 1)
    "As I held out the strips of meat in front of Myu, she snatched them and began to devour them quickly."
    MC @surprised "Easy! Not so fast!"
    "I watched as the meat was broken down and dissolved inside of Myu till nothing was left."
    jump qst_HumanExp_1_feedMyu_After

label qst_HumanExp_1_feedMyu_After:
    MC "(Well, I guess the question is, what now?)"
    MYU @think "...W-Words."
    MC @surprised "Huh?"
    MYU @talk "Myu... Words."
    "I pointed towards my mouth."
    MC @talk "You want to learn more words?"
    MYU @smile "Myu!"
    MC @smile "Uhh, well, alright!"
    MC "(I guess I should try devoting some time to teaching Myu some Alderian.)"
    MC "(Being able to talk to her more will at least make life easier.)"
    MC "(Maybe then I'll be able to figure out what to do with her at least.)"
    $ QstSetProgress(QstHumanExp, 2)
    $ LocEnter()

label qst_HumanExp_2_lesson:
    MYU @smile "O-Okay!"
    scene black with dissolve
    "After spending some time teaching Myu the basics, starting with just pointing to various objects and having her say the word associated with them, Myu began to pick things up very quickly."
    $ TimeAdvBy(TIME_1H)
    "Afterwards, we moved onto slowly walking her through some simple phrases and things, and Myu enthusiastically got to grips with these too."
    $ LocFlush()
    show mc at cleft
    show myu at cright_f
    with dissolve
    MC @smile "Very good, Myu, you're learning fast."
    MC "({i}Very fast{/i}.)"
    MC "(If she keeps this up she'll be speaking fluent Alderian in no time.)"
    MYU @joy "Myu... Happy... Learn."
    MC "(Maybe I could buy her some kind of reading material to help teach her?)"
    $ QstSetProgress(QstHumanExp, 3)
    $ LocEnter()

label qst_HumanExp_3_grabBook_atLibrary:
    VALA "Hm?"
    VALA "What do you need that for?"
    menu:
        "I'm hoping to improve my own mastery of the language.": #+1 Vala affection
            VALA "Oh my..."
            $ CharChangeRel("vala", 1)
            VALA "That's quite the noble commitment!"
            VALA "Always nice to see someone showing more appreciation for the nuances of our language!"
        "My reasons are my own.":
            VALA "Hm, well, okay then."
        "I'm trying to teach someone.":
            VALA "I never took you for a teacher!"
            VALA "How old are the students? Are they perhaps younger relatives of yours?"
            MC @talk "Uhh, not exactly..."
            VALA "Well, I'm always happy to help when it comes to education!"
    MC @talk "Do you perhaps have have a selection of books?"
    MC @think "Something to teach a beginner to something more advanced?"
    VALA "Well, you are in luck."
    VALA "I know we have plenty of copies of {i}'Agathons learning Alderian.'{/i}"
    MC @think "I don't remember studying from that collection."
    VALA "You very likely wouldn't have, it's not mandatory for students."
    VALA "It's very popular amongst Aristocrats teaching their children, however."
    MC @talk "Hmm... I see."
    MC @talk "How much for a copy of the collection?"
    VALA @sad "Hmm, well, this is the difficult part."
    VALA @sad "At least five hundred coins for the collection."
    MC @surprised "Five hundred?!"
    VALA @sad "... How do you think they keep the books circulating strictly amongst aristocracy?"
    VALA @sad "Make it too expensive a commodity for the common people of course."
    "I pushed my disgust aside, no good came from dwelling on it now."
    menu qst_HumanExp_3_grabBook_atLibrary_menu:
        "Is there no way you could sell it to me cheaper?" (Req_Charm = 7) if not QstHumanExp().haggledForBooks: #charm check 
            $ QstHumanExp().haggledForBooks = True
            $ QstHumanExp().booksPrice = 400
            VALA "I... There is a slightly damaged copy of the collection that I could sell it to you at a slight discount?"
            VALA "It's still perfectly fine, but no aristocratic family would want it."
            MC @smile "That would be great if you could."
            VALA "Alright, I can get away with selling it for four hundred coins."
            VALA "Any less, and its my job on the line."
            VALA "So, four hundred it is."
            jump qst_HumanExp_3_grabBook_atLibrary_menu

        "Here is the coin." (Req_Gold = QstHumanExp().booksPrice):
            VALA "Ah! Okay!"
            $ PlayerRemItem("gold", QstHumanExp().booksPrice)
            VALA "Let me just bind the collection for you and it's all yours!"
            scene black with dissolve
            $ Pause(0.5)
            $ LocFlush()
            show vala at center_f
            with dissolve
            VALA "Here you go!"
            $ PlayerAddItem("qst_myu_books")
            $ QstSetProgress(QstHumanExp, 4)
            show vala at nod
            MC @smile "Thank you, Vala."
            MC "(I better get this back to Myu.)"
            $ LocEnter()

        "I will be back soon.":
            $ QstHumanExp().valaRevisit = True
            VALA "I'll keep the books ready for you."
            $ LocEnter()

label qst_HumanExp_3_grabBook_atLibrary_revisit:
    if QstHumanExp().booksPrice == 500:
        VALA "Yeah, it's five hundred coins for the collection of books on Alderian language."
    if QstHumanExp().booksPrice == 400:
        VALA "Yeah, four hundred coins and the collection is yours."
    menu qst_HumanExp_3_grabBook_atLibrary_revisit_menu:
        "Is there no way you could sell it to me cheaper?" (Req_Charm = 7) if not QstHumanExp().haggledForBooks:
            $ QstHumanExp().haggledForBooks = True
            $ QstHumanExp().booksPrice = 400
            VALA "I... There is a slightly damaged copy of the collection that I could sell it to you at a slight discount?"
            VALA "It's still perfectly fine, but no aristocratic family would want it."
            MC @smile "That would be great if you could."
            VALA "Alright, I can get away with selling it for four hundred coins."
            VALA "Any less, and its my job on the line."
            VALA "So, four hundred it is."
            jump qst_HumanExp_3_grabBook_atLibrary_revisit_menu

        "Deal." (Req_Gold = QstHumanExp().booksPrice):
            VALA "Ah! Okay!"
            $ PlayerRemItem("gold", QstHumanExp().booksPrice)
            VALA "Let me just bind the collection for you and it's all yours!"
            scene black with dissolve
            $ Pause(0.5)
            $ LocFlush()
            show vala at center_f
            with dissolve
            VALA "Here you go!"
            $ PlayerAddItem("qst_myu_books")
            $ QstSetProgress(QstHumanExp, 4)
            show vala at nod
            MC @smile "Thank you, Vala."
            MC "(I better get this back to Myu.)"
            $ LocEnter()

        "Nevermind.":
            VALA "I'll keep the books ready if you reconsider."
            return

label qst_HumanExp_3_grabBook_returnBooks:
    show myu at cright_f with dissolve
    show mc at cleft with easeinleft
    MC @talk "Okay, Myu, I have some things to show you."
    $ PlayerRemItem("qst_myu_books")
    MYU @joy "Ooooh!"
    "Myu held one of the books in her hands and immediately began to eat it."
    MC @surprised "No! No! Myu!"
    MC @angry "Stop!"
    MYU @talk "Huh?"
    MC @smile "They're to help you learn."
    MYU @think "L-Learn?"
    MC @talk "Yes, look."
    "I opened up the book for Myu and spent some time going through the basics with her once again."
    "The sentences for the beginners' book were simple enough, and surprisingly quickly, Myu proved capable of reading simple sentences."
    MC @talk "Okay, I'll leave this with you to read for a while."
    MYU @smile "Mm!"
    MC "(I should check in on her and see how's she getting on later.)"
    $ QstSetProgress(QstHumanExp, 5)
    $ QstHumanExp().myuSpeaksDay = GetGameDay() + 2
    $ LocEnter()

label qst_HumanExp_5_checkIn_early:
    MC @smile "Hey, how goes your reading?"
    MYU @think "Myu... Have much... book... to read."
    MC @smile "Alright, I'll leave you to it."
    MC "(She's learning so fast.)"
    MC "(I should give her a little more time I guess.)"
    $ LocEnter()

label qst_HumanExp_5_checkIn_speaks:
    MYU @talk "H-Hello there!"
    MC @smile "Myu! That sounds great!"
    MYU @smile "Myu is... Happy you are happy."
    MYU @blush "{i}H-Husband.{/i}"
    MC @talk "Uhh, Myu, I think there was a wrong word there."
    "Myu looked at me puzzled."
    MYU @think "...Myu?"
    "Myu's cheeks cutely blushed red as her eyes shyly looked away."
    MYU @think "N-No mistake."
    MYU @blush "Myu... Belong... {i}to you.{/i}"
    MYU @blush "{i}Husband.{/i}"
    MC @surprised "Uhh, Myu!"
    MYU @sad "Myu... No good?"
    menu:
        "How about we get to know each other a little more first?":
            MYU "..."
            $ CharChangeRel("myu", 1)
            MYU @joy "OKAY!"
            MC "(Damn it, I can't deny she's not beautiful.)"
            MC "(But does she even fully understand the stuff she's saying yet?)"
            MC "(I feel like... I'm almost taking advantage of her at this point.)"
        "Oh yeah, your ass belongs to me.":
            MYU @blush "Oooh!"
            $ CharChangeRel("myu", 1)
            $ QstHumanExp().buttGrab = True
            MYU @smile "You like... Myu butt?"
            "Myu, with a mischievous smile stepped forward."
            show myu at center_f with easeinright
            MYU @blush "T-Touch Myu butt?"
            hide myu
            hide mc
            show cg_myu_hug_grab at center
            with dissolve
            "I obliged, giving Myu's ass a good squeeze."
            "Her cool, slightly sticky butt was soft, and I knew if I knead it with enough force, my hand could go right through inside of her."
            "But Myu kept the exterior strong enough that without forcing it, I could {i}touch{/i} her like anyone else."
            MYU "Mhmmm..."
            MYU "Touch... Warm."
            hide cg_myu_hug_grab
            show mc at cleft
            show myu at cright_f
            with dissolve
            "Myu shyly pulled away."
            MYU @blush "P-Please touch Myu more soon."
        "Myu, I'm sorry, I don't see you that way.":
            "Myu stared blankly at me, not quite understanding what I was trying to say."
            MC "(Fuck, I should try this again, maybe when she understands me a bit more?)"
    MYU @think "Myu... Want... To see... Outside."
    MC @talk "{i}Outside?{/i}"
    MC @think "I don't know about that, Myu... You'd need to be able to stay hidden."
    MC @talk "And you don't really fit in your old container as it is."
    "Myu pouted."
    MYU @sad "Whole world... {i}Outside.{/i}"
    MC "{i}*Sigh*{/i}"
    MC @talk "Alright, I will consider showing you around the city."
    MYU @joy "Yes!"
    MC "(I should talk to her when I'm ready for this.)"
    $ QstSetProgress(QstHumanExp, 6)
    $ LocEnter()

label qst_HumanExp_6_cityTour:
    MYU @joy "Myu! I mean... Yes!"
    MC @talk "...But you {i}can't{/i} be seen, are we clear?"
    hide myu with dissolve
    "Myu once again returned to her slime like form as a puddle on the ground and crawled her way back over towards the spilled container, pouring herself back inside of it."
    $ PlayerAddItem("qst_slime_jar")
    show mc at cleft_f, blurin
    MC @smile "Okay, Myu, are you ready?"
    MC @talk "Can you see from where you are?"
    MYU 'Yes!'
    hide mc with easeoutleft
    MC '(Well, guess I best show her around.)'
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_house_south")
    $ LocFlush()
    with dissolve
    show mc at right_f with easeinright
    MYU 'What... Is this place?'
    MC @talk "There is where most people live, Myu."
    MYU 'Most?'
    MC @talk "Farmers, Mages, aristocrats and their rich friends, they all live elsewhere."
    MYU '...Why?'
    MC @talk "It's just the way it is."
    MC @talk "Each of the places are called 'districts,' and they all serve different purposes."
    MYU 'Are the other districts nicer than this one?'
    MC @talk "Of course, much nicer."
    MYU '...Why?'
    MYU 'Are the people here... {i}not needed?{/i}'
    MC @smile "The people here are the most important, they keep everything going."
    MYU '...Then why do they not live in the nice districts?'
    MC @sad "It's... complicated."
    MC @sad "Things are harder now because of the war."
    MC @talk "Hopefully after the war, people will go back to living much better lives like they used to before."
    MYU 'Do the rich people live harder lives as well?'
    MC @think "Well, not exactly."
    MYU '...Why?'
    MC @talk "It depends on the person, Myu."
    MC @talk "Even if they have suffered because of the war, many still have enough wealth to get by comfortably."
    MC @talk "Let's move on now."
    MC @talk "There's much more to see."
    hide mc with easeoutleft
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_mage")
    $ LocFlush()
    with dissolve
    show mc at left with easeinleft
    MC @talk "There is where students come to learn how to use their magic."
    MYU "Do you have magic?"
    MC @talk "No, I failed every test on it."
    MC @talk "You're either born with magic, like my [erika_ref!t] Erika, where you're then taken off to study at one of the Academy's here."
    MC @talk "Or, you get stuck with the regular schooling like the rest of us."
    MYU "...Is Myu magic?"
    MC @think "You're a being of magical descent, so you likely have {i}some{/i} magic."
    MYU "Hrghhhhh!"
    MC @surprised "What are you doing?"
    MYU "Trying to magic! I wanna see if I can make bacon appear!"
    MC @smile2 "It doesn't quite work like that."
    MYU "Aww..."
    MC @talk "There's a lot of rules to magic, all of which, I don't even fully understand myself."
    MC @talk "Anyway, let's keep moving, shall we?"
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_farm")
    $ LocFlush()
    with dissolve
    show mc at right_f with easeinright
    MC @talk "There is where farmers work and live."
    MC @talk "Huge fields of land inside these walls are used for farming so that Novaras can sustain itself in the event of a siege."
    MYU "Siege?"
    MC @serious "If the Demorai tries to take this place, we could hold out for months, hopefully waiting on reinforcements from the North."
    MYU "Ooooooh."
    MYU "So, can we get food here?"
    MYU 'Myu, hungry.'
    MC @talk "No, the food here is rationed out to the army and districts."
    MC @talk "Everyone is given a bit of food, some more than others depending on their district."
    MC @talk "But you can buy additional food from what they allocate to the merchants to sell."
    MYU "Why..."
    'Myu puzzled out her thoughts.'
    MYU "Some get more than others?"
    MYU "If they are rich, Why they not just buy more food anyway?"
    MYU "Then more food... For poor."
    MC @think "Well, yes..."
    MC @smile "I guess no one's ever really thought about it much."
    MC @think "This is all some of us have ever known."
    MYU 'Not seem fair.'
    menu:
        "There's a difference between expecting people with more money and power to be more responsible, and {i}punishing{/i} them for their wealth.":
            MYU "...Okay, Myu think on what you said."
            MYU "But, if they {i}aren't{/i} responsible with money and power, is it not okay to punish them then?"
        "Personally, I think we could do without any of the Aristocracy... We could manage better on our own.":
            MYU "Mmm, won't people get hurt if you try get rid of them though?"
            MYU "Myu would be sad to see people hurt."
            MYU "And more people might be upset if you DO get rid of them, so even more people get hurt then."
            MC @smile "Very perceptive, Myu."
        "Someone needs to be in charge, they have tough decisions to make themselves.":
            MYU "But, who put them in charge?"
            MYU "It sounds to Myu like they also {i}have{/i} more just for making choices for everyone else."
            MYU "And, those choices seem to be more good for them than everyone."
    MC @smile "Heh, you're learning to speak and think way too fast for your own good sometimes, Myu."
    MYU "... Myu do bad?"
    MC @smile "Not at all, Myu."
    MC @talk "Anyway, moving on..."
    hide mc with easeoutleft
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_edu")
    $ LocFlush()
    with dissolve
    show mc at left with easeinleft
    MC @talk "This is where most normal students are taught."
    MYU 'Its so big!'
    MC @talk "Hundreds if not thousands are taught here every day."
    MYU 'What do you learn?'
    MC @smile "A lot actually, everything from basic defense to economics to about a hundred other things."
    MC @talk "The idea is they delegate you into a job best suited to your results during a festival we call the Terminus ceremony."
    MYU "What if you get a job you don't like?"
    MC @talk "Well, you're stuck with it."
    MC @talk "At least, until this war is over."
    MC @talk "But it doesn't always stay that way anyway, I mean, I was a scout, and now I'm officially employed by the Adventurers Guild."
    MC @talk "But those changes aren't the norm, more like, special circumstances."
    MYU "Myu see."
    MYU "Do all students learn together?"
    MC @talk "Mostly."
    MYU "{i}...Mostly?{/i}"
    MC @talk "The rich students tend to have different teachers and some additional classes than most of us."
    MC @talk "But other than that, yeah, we share lessons."
    MYU "So, do rich students get jobs they don't like?"
    MC @think "Uhh, that doesn't really happen."
    MYU "...Why?"
    MC @talk "Because it's expected that those students will fill in for their parents when they're gone."
    MYU "But what if they're dumb?"
    MC @smile "Well, bad luck for all of us I guess!"
    MYU "Except the dumb person?"
    MC @talk "Come on, enough of this place, there's still a couple more places to see."
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_pleasure")
    $ LocFlush()
    with dissolve
    show mc at right_f with easeinright
    MC @talk "This is um, where people go for {i}'entertainment.'{/i}"
    MYU "{i}Entertainment?{/i}"
    MC @talk "Uhh, well, it's kinda a place for people to have fun."
    MC @talk "And a big part of that is what happens when men and women {i}really{/i} like each other and-"
    if QstHumanExp().buttGrab:
        MYU '...Ooooh!'
        MYU "Do they touch each other's butts like you did to mine earlier?"
        MYU "{i}Myu liked that a lot.{/i}"
        MC @talk "Uhh, yeahhhh..."
        MC @talk "Kinda."
    MC @talk "Anyway, you don't need to know much about this place."
    MYU "So, people here work to make others happy?"
    MC @smile "That's a pretty good way of describing it."
    MYU "Are they happy too?"
    MYU "The people who work here?"
    MC @think "Well, uhh, I suppose it depends on the person."
    MC @talk "Some I'm sure are happy to be here, others, desperate to just survive."
    MC @serious "Unfortunately, a lot of girls from Ramon are trapped here, they were cut off from going home when the war started."
    MC @sad "Now, a lot just work here."
    MYU "That's so sad."
    MC @serious "That's war, Myu."
    MC @talk "Anyway, let's move on."
    hide mc with easeoutleft
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    with dissolve
    show mc at left with easeinleft
    MC @smile2 "So, this is the Market district."
    MC @talk "People here can buy any additional food they need and other things."
    MYU "Food smells so good!"
    MC @smile "Maybe one day, you'll get to walk around here yourself and experience things properly."
    MYU '...What those over there?'
    MC  'Hm?'
    MC @smile "Ah, those are Taverns, good places to meet friends for some food and ale."
    MYU "Ale?"
    MC @smile "It's a type of drink, but if you drink too much, well..."
    MC @smile2 "It goes from a nice feeling to a bad one the next day!"
    MYU 'Can Myu try?'
    MC @smile "Uhhh, I'll think on it."
    MC @talk "Anyway, let's keep going."
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_army")
    $ LocFlush()
    with dissolve
    show mc at left with easeinleft
    MC @serious "I need you to be quiet here... There is where the main military force for Novaras is stationed."
    MC @talk "Lots of guards everywhere."
    MYU "Myu no like this place... Can we go?"
    MC @talk "Of course, Myu."
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("novaras_dist_centre")
    $ LocFlush()
    with dissolve
    show mc at left with easeinright
    MC @talk "And this is the Royal District, the heart of the city."
    MC @talk "This is where the king and queen live, along with some other aristocrats."
    MYU "WOWWWW!"
    MYU "It's so big!"
    MYU "And only a few people live there?"
    MC @smile "Well, the place is also filed with guards, officials and servants of course."
    MYU "...Can we live there?"
    MC @smile "Heh... I wouldn't hold your breath on that."
    MC @talk "Okay, Myu, it's been quite a trip."
    MC @smile "Ready to go home?"
    MYU "Okay! Myu ready!"
    hide mc with easeoutright
    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    $ LocSet("azul_safehouse_bedroom")
    $ LocFlush()
    with dissolve
    show mc at cleft with easeinleft
    $ PlayerRemItem("qst_slime_jar")
    MC @talk "Well, Myu, did you enjoy your time out?"
    show myu at cright_f with dissolve
    MYU @smile "Myu did!"
    MYU @sad "But... Lots of things Myu did not understand."
    MC @think "Well, the worlds a complicated place, Myu."
    MC @talk "Even us living in it for years don't fully understand it sometimes."
    MYU @sad "Hmm, okay."
    MYU @blush "Myu has husband to keep her safe."
    MYU @blush "So Myu is okay."
    MC "(This {i}husband{/i} thing again.)"
    MC "(I really need to try clear this up with her soon.)"
    MYU @talk "Myu sleepy now, thank you for taking Myu out."
    MC @smile "You're welcome, Myu."
    hide myu with dissolve
    MC "(Myu's learning so fast... I wonder what she will truly make of all this when she fully comprehends things?)"
    MC "(I should let her rest anyway, at least, for now.)"
    $ QstSetProgress(QstHumanExp, 7)
    $ LocEnter()

##################
label qst_HumanExp_7_checkupAfterTour:
    show mc at left with easeinleft
    show myu at cright_f with easeinright
    'Myu stumbled her way towards me, barely able to hold herself together as she looked up to me weakly.'
    MYU @sad "N-Not feel good."
    MC @sad "Myu, what's wrong?"
    MYU @sad "Hungry... Weak..."
    MYU @sad "N-Not right."
    MC "(Fuck, it's been a while since she last fed properly.)"
    if PlayerItemQty("red_meat") > 0:
        MC @talk 'Here, I still have some food left, Myu.'
        $ PlayerRemItem("red_meat", 1)
        'Myu took the food and tried to eat it, but quickly she threw it back up.'
        MYU @sad'Grghhh!'
        MC @surprised "Huh? What's wrong with it?"
        MYU "Myu not know... Not good."
        MC '(Shit, maybe the meat was too old?)'
    else:
        MC "(Damn, and I've got nothing left to give her.)"
        MC @talk "Okay, Myu, I'll need to buy some more meat from the Butcher."
        'Myu shook her head.'
        MYU @sad "No!"
        MC @talk "What?"
        MYU @sad "No good... Try... Different."
        MC '(Maybe she needs different meat? Or...)'
    MC '(I guess I could get some food from the {i}Iron Unicorn{/i} instead.)'
    MC @talk "Myu... I'll be back shortly, okay?"
    MC @talk 'I know where I can get you some food.'
    MC @talk "Stay here."
    show mc at left_f, blurin
    'As I turned to leave, Myu reached out to stop me.'
    show myu at cleft_f with easeinright
    MYU @sad "Myu, come."
    MC @angry "Myu, you're sick, you can't leave."
    MYU @angry "If Myu stay much longer... Not good!"
    MC @angry "...Damn it!"
    MC @talk "Alright, fine, but you'll need to hide in your container."
    hide myu with dissolve
    $ PlayerAddItem("qst_slime_jar")
    $ CharSetVar("myu", "hide", True)
    MC '(This feels like a bad idea.)'
    hide mc with easeoutleft
    $ QstSetProgress(QstHumanExp, 8)
    $ LocEnter()

label qst_HumanExp_8_shayGetBetterFood:
    SHAY @smile 'Oh, of course!'
    SHAY @talk "What would you like?"
    MC @talk "(Hmm... Perhaps a finer meat is what Myu needs?)"
    MC @talk 'Do you perhaps have any deer, or...'
    SHAY @shock '{i}Deer?{/i}'
    SHAY @think "W-Well... We have some, but it's expensive."
    SHAY @smile 'Three hundred coins.'
    menu:
        'Here is the coin.' (Req_Gold = 300): #Only available if player has enough money
            $ PlayerRemItem("gold", 300)
            pass
        'Hm, I will come back another time then.':
            SHAY @talk 'Alright, just let me know if you change your mind.'
            return
    SHAY @smile2 'Ah! Oh my!'
    SHAY @shy "We haven't had to prep a deer in months!"
    SHAY @talk "Here, take a seat."
    SHAY @talk 'What drink shall I bring you?'
    MC @smile 'An Ale will suffice.'
    SHAY @smile 'Very well, I will be back shortly.'
    scene black with dissolve
    'As I sat down at one of the tables, Shay returned after a short while with my food and drink.'
    'The piping hot deer smelt amazing; it had been a long time since I had enjoyed a meal quite so expensive.'
    'A meal such as this now, was a reserved treat father would have bought us to celebrate Harvest Day once a year.'
    'Many would not even think of wasting the coin on such a thing, and it was simply unattainable for most.'
    'Here I was though, not only able to afford it, but enjoying it almost as though it was like any other meal.'
    'Despite the inherent danger... The mercenary life paid well alright.'
    'Beneath the table, I rested the container holding Myu, and would every so often palm a piece of the meat under the table which she would take from my hand gently with a tentacle to consume.'
    'Finally, once the meal was finished, I gathered Myu back into my possession once again and rose to my feet.'
    $ LocFlush()
    with dissolve
    show shay at center with easeinright
    SHAY @talk 'How was it?'
    MC @smile2 'It was perfect.'
    SHAY @smile "Ah! I'm so glad to hear that!"
    SHAY @talk 'Nice to see my cooking is still up to standard then!'
    MC @talk 'You cooked it?'
    SHAY @talk 'Ha... Did you think we hired a cook or something?'
    SHAY @talk 'No, just me and my husband.'
    MC @talk 'I see.'
    'The box Myu was in rumbled.'
    MC '(Damn it!)'
    MC '(Keep still!)'
    SHAY @shock 'Hm? Is everything okay?'
    SHAY @think 'You seem a little... pre-occupied with something.'
    MC @surprised 'Oh, uh...!'
    MC @talk 'I just remembered I had something to do is all!'
    SHAY @shock 'Oh, um, okay.'
    SHAY @talk "Well, don't let me-"
    'Feeling the box continue to rumble more erratically, I hurried off outside before even finishing my conversation with Shay.'
    MC 'Thanks for the food! Talk soon!'
    SHAY @talk '...Keep you here.'
    SHAY '(What was up with him back there?)'
    SHAY "(He's an odd one, isn't he?)"
    scene black with dissolve
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    with dissolve
    show mc at center_f with easeinright
    "In a hushed tone, I pulled Myu's container towards me."
    MC @angry 'Myu! Be quiet damn it!'
    show mc at shake
    'The container continued to rumble.'
    MC "(Damn it, I need to get her home and see what's wrong.)"
    scene black with dissolve
    $ LocSet("azul_safehouse")
    $ LocFlush()
    show mc at cleft
    with dissolve
    'Myu erupted out of the container on her hands and knees, violently shaking as she began to throw up the half-dissolved food.'
    $ PlayerRemItem("qst_slime_jar")
    show myu at cright with dissolve
    MC @surprised 'Myu!'
    'Myu weakly rose back to her feet trembling.'
    MYU @sad 'M-Myu... Not good.'
    'Myu, too weak to hold her form, collapsed into a puddle on the floor and dragged herself into a corner miserably.'
    hide myu with dissolve
    MC '(Fuck! FUCK!)'
    MC '(What did I do wrong?)'
    MC '(S-Shit!)'
    MC '(There has to be something I can do... Maybe I can find a book to read up on them or something?)'
    MC '(What am I missing?)'
    MC '(She ate the meat fine before, why not now?)'
    $ QstSetProgress(QstHumanExp, 9)
    $ LocEnter()

label qst_HumanExp_9_valaLearnSlimelarks:
    VALA 'Slimelarks?'
    VALA "Umm, I think they're mentioned in a couple bestiaries, but there's nothing devoted just to them."
    MC @talk 'Do you have one of these bestiaries?'
    VALA "I can try gather you up some if that's what you want..."
    VALA "What's this about?"
    VALA "It might help if I knew what you were looking to find out about them."
    MC @think "Uhh, their diet I guess."
    VALA 'Their diet?'
    VALA 'OOOH! Are you writing a new research journal on them?!'
    MC @think 'Uhh, not exactly...'
    VALA 'Hmmmm, interesting.'
    VALA "Well, okay then."
    VALA "I'll try narrow down the books to the most useful for you then."
    MC @smile 'Thank you, Vala.'
    VALA "Don't mention it! Always happy to help a fellow keen mind!"
    scene black with dissolve
    "A while later..."
    $ LocFlush()
    show mc at left
    with dissolve
    MC "(Damn it, what's taking so long? It's nearly been an hour!)"
    MC '(I need to get back and-)'
    show vala at right_f with easeinright
    VALA 'Phew!'
    VALA 'Well, there was a lot on Slimelarks but not much talking about what they eat.'
    MC @talk 'What did you find?'
    VALA 'This seems to be the best source of reference.'
    VALA "It was one of the earlier studies on Slimelarks, but it's one of the few that goes into their natural lives rather than just discussing the quickest way to kill them."
    MC @talk 'Ah, thank you, Vala.'
    VALA "Just leave the book here when you're done."
    hide vala with easeoutright
    '{i}Slimelarks, by their very nature, are omnivorous predators.{/i}'
    '{i}In their infancy, they rely far more on raw meat, often provided to them by their mothers, in order to build up their strength.{/i}'
    '{i}However, this is only one component of the slimelarks diet, it is essential for their growth they then move on to consume other substances, such as wildflower.{/i}'
    '{i}Slimelarks do not possess any sort of organs similar to mammals, and thus, they rely on consuming various substances in order to compensate for their internal processes.{/i}'
    '{i}For example, the wild flowers helps the slimelarks with internal acidic production, allowing them to break down the meat and other foods they consume, without it, a slimelark can very quickly become sick.{/i}'
    MC '(Wildflower... Perhaps I could gather some by the Lake?)'
    $ QstSetProgress(QstHumanExp, 10)
    $ LocEnter()

label qst_HumanExp_11_returnFlowers:
    'With the wildflower ready in my pouch, I practically burst through the door hurrying inside.'
    show mc at center with easeinleft
    MC @talk "Myu! Where are you?"
    MC @scared "MYU!"
    show mc at center_f, blurin
    MC "(Oh fuck... Fuck! Where did she go?)"
    MC "(I have to find her!)"
    "I noticed that outside the window, my house was seen."
    MC "(Could she?...)"
    MC "(Oh no!)"
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("mc_house_kitchen")
    $ LocFlush()
    show regina at cright_f
    show myu at cleft
    with dissolve
    show mc at right_f with easeinright
    'As I stepped inside my home, I was greeted by the sudden sight of Myu sat patiently at the dinner table as [regina_ref!t] served her a plate of vegetables.'
    MC @surprised "MYU?!"
    REGINA @smile "Ah! There you are dear!"
    REGINA @talk "Are those wildflowers? I'll take them."
    MC @surprised "I... Wait, I can-"
    REGINA @talk "Explain why a slimelark broke into our home asking for you?"
    REGINA @talk "{i}Yes, yes you can.{/i}"
    $ PlayerRemItem("qst_wild_flowers")
    "Taking the wild flower from my shaking hands, [regina_ref!t] poured the wild flower over Myu's food."
    REGINA @smile "Enjoy, Myu."
    MYU @joy "T-Tha... Thanks!"
    show myu at nod
    "Myu began to devour the food with both hands quickly as [regina_ref!t] turned to face me, her calm smiling expression giving away her obvious displeasure of the situation."
    REGINA @smile "Dear, if you could be so kind as to explain to me..."
    REGINA @angry "{i}...Why there is a slimelark in our home?{/i}"
    MC "(...Shit.)"
    scene black with dissolve
    "During the next ten minutes, I explained the full story as best as I could to [regina_ref!t]."
    $ LocFlush()
    show myu at cleft
    show regina at center_f
    show mc at cright_f
    with dissolve
    REGINA @angry "Are you crazy? Do you even know the first thing about caring for Slimelarks?"
    MC @scared "Well, I-"
    REGINA @angry "The answer is clearly no, the poor thing you've just been feeding meat and nothing else, haven't you?"
    MC @scared "Well... Yes, but..."
    MC @scared "She got sick so I-"
    REGINA @talk "I know she became sick!"
    REGINA @talk "She came crawling in here asking for you and threw up all over the floor."
    MC @think "{i}...Oh.{/i}"
    MC "(Fuck! I pray no one noticed her outside.)"
    REGINA @sad "{i}*Sigh*{/i}"
    REGINA @sad "Well, at least it was a good idea taking her to that abandoned safe house outside."
    "I glanced over towards Myu, who smiled and waved at me as she continued to make happy sounds while she ate and devoured her food."
    "As the food passed into Myu, I could see it being dissolved inside of her body till nothing was left."
    MC @smile "She seems better now at least."
    MC @think "But, how did you know what she needed?"
    REGINA @talk "That doesn't matter, I used to live nearby to some slimelarks when I was younger, that's all."
    MC @surprised "Wait, you lived by-"
    REGINA @talk "Don't try and change the subject mister!"
    REGINA @talk "It's {i}imprinted{/i} itself onto you now, so you're stuck with it."
    MC @surprised "What?"
    REGINA @talk "Oh for the love of..."
    REGINA @talk "Do you think it just took that form for the fun of it?"
    REGINA @talk "It thinks you are its {i}mate.{/i}"
    MC @surprised "Wait, what?!"
    REGINA @talk "It took a form it thought would be pleasing to you."
    REGINA @talk "Its also probably been copying your memories, that's how she's learning so fast."
    MC @talk "{i}It's... copying my memories?{/i}"
    REGINA @talk "Slimelarks are able to learn {i}a lot{/i} through touch alone."
    REGINA @talk "Why do you think she's so affectionate?"
    REGINA @talk "She's trying to learn quicker {i}through{/i} touch."
    REGINA @talk "It's how they learn to form new shapes so quickly."
    MC @talk "So, what should I do?"
    REGINA @sad "{i}*Sigh*{/i}"
    REGINA @sad "She's {i}Your{/i} responsibility now, just be prepared to accept all that entails."
    REGINA @talk "And she needs fresh blood."
    MC @scared "Fresh... {i}blood?{/i}"
    REGINA @talk "She's a predator, [player_name!t]."
    REGINA @talk "When she wants meat, her hunting instincts take over."
    "Grabbing the kitchen knife in hand, Regina gently nipped at her finger with the blade till it was dripping blood."
    show regina at nod
    MC @surprised "[regina_ref_cap!t]!"
    REGINA @talk "Watch."
    "Regina gently presented her bleeding finger to Myu, who immediately lunged forward and began to suckle on the finger."
    REGINA @talk "See? She still craves fresh blood and meat as well."
    "Regina pulled her finger away from Myu who reluctantly gave it up."
    MC @talk "So, what should I do when that happens?"
    REGINA @talk "Find her a human to eat."
    MC @surprised "Wha~"
    "Shivers ran down my spine as I realized that she was not kidding."
    MC @surprised "{i}... Human?{/i}"
    REGINA @talk "For conveniences sake at the very least, yes."
    REGINA @talk "Unless you plan to spend all your coin on buying her meat, or forever hunting in woodlands to feed her daily ... Which by the way, could draw unnecessary attention."
    REGINA @talk "Then she's going to need to hone her natural skills, isn't she?"
    REGINA @talk "If you're going to be risking your life and presumably she'll be there to protect you, it only makes sense she then eats what you kill."
    REGINA @talk "Not like there's a shortage of criminals these days either."
    MC @talk "Just, find some... bandits?"
    MC @talk "And let her {b}eat them?{/b}"
    REGINA @talk "Is there any real difference in nobility between you killing people and her eating them?"
    REGINA @talk "The end result is the same."
    MC "(Is it still her talking to me right now?)"
    MC "([regina_ref_cap!t]?)"
    $ choicemenu = ["a","b"]
    menu qst_HumanExp_11_returnFlowers_menu:
        "So, you {i}don't{/i} want me to get rid of her?" if "a" in choicemenu:
            $ choicemenu.remove("a")
            REGINA @talk "What part of {i}imprinting{/i} do you not understand?"
            REGINA @talk "She will just come crawling straight back, and now, other slimelarks are likely to reject her."
            MC @talk "What do you mean?"
            REGINA @talk "Slimelarks can tell when one of their own has been... {i}tainted,{/i} so to speak."
            REGINA @talk "If you {i}did{/i} manage to get rid of her, she'd be all alone."
            jump qst_HumanExp_11_returnFlowers_menu
        "I figured you'd be more afraid when you saw her..." if "b" in choicemenu:
            $ choicemenu.remove("b")
            REGINA @talk "Hm?"
            MC @think "Well, I figured you would be more afraid."
            MC @think "Instead, you seem more... {i}Annoyed.{/i}"
            REGINA @talk "It's like I said, I grew nearby to some, now can we change the subject please?"
            MC "(I have the distinct feeling she's hiding something from me.)"
            jump qst_HumanExp_11_returnFlowers_menu
        "So... What now?": #moves plot forward
            pass
    '[regina_ref_cap!t] frowned.'
    REGINA @angry "Just keep her out of sight, understand?"
    REGINA @talk "Inquisitors and their lot won't take kindly to a slimelark living within Novaras."
    MYU @joy "All done!"
    'Myu proudly presented her empty plate to show she was finished, and Regina took it from her with a smile.'
    REGINA @smile "Very good, Myu!"
    REGINA @talk "Now we will continue teaching you Alderian the next time you visit, yes?"
    MYU @joy "Yes!"
    REGINA @talk "Good."
    'Regina flashed one more look at me making it clear I needed to get a grip on this, {i}quickly.{/i}'
    hide regina with dissolve
    MC '(Shit... I guess I should do what [regina_ref!t] says and take her out {i}hunting{/i} one night.)'
    MC '(Hunting {i}people...{/i})'
    'Something about the wording of it made me slightly queasy, but [regina_ref!t] was right.'
    'Myu was a predator... And Myu would need to hunt.'
    #Fade to black
    scene black with dissolve
    $ LocSet("azul_safehouse")
    'After that, I headed back to the abandoned safe house with a much healthier Myu.'
    '[regina_ref_cap!t] followed us too at her insistence, in case she ever needed to visit the safe house and check on Myu herself.'
    #Cut to Azul safehouse
    $ LocFlush()
    show myu at right_f
    show mc at center_f
    show regina at left
    with dissolve
    REGINA @talk "Ah, so this is the place."
    REGINA @smile "...Not very homely, is it?"
    MC @talk "It's the best I could do on short notice."
    REGINA @talk "It'll serve it's purpose."
    '[regina_ref_cap!t] smiled as she turned to face Myu.'
    REGINA @smile "Anyway, it was nice to meet you Myu!"
    MYU @joy "Thank you for food!"
    REGINA @smile "You're very welcome."
    REGINA @talk "Now, I must make my leave so..."
    show regina at blurin, left_f
    REGINA @talk "Goodbye both!"
    MC @talk "Bye [regina_ref!t]."
    MYU @joy "Bye bye nice lady!"
    '[regina_ref_cap!t] chuckled as she closed the door behind her.'
    hide regina with easeoutleft
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    $ LocFlush()
    with dissolve
    show cg_regina_raven at cright with easeinright
    REGINA @talk "Make sure to notify me the next time the two of them leave together, understand?"
    show cg_regina_raven at nod
    play sound "audio/cfx/raven.ogg"
    RAVEN "{i}*Squarks!*{/i}" 
    scene black with dissolve
    $ LocSet("azul_safehouse_bedroom")
    $ CharSetVar("myu", "hide", False)
    $ QstSetProgress(QstHumanExp, 12)
    $ LocEnter()

label qst_HumanExp_12_goHunting:
    'Myu tilted her head as she puzzled out my words.'
    MYU @think '...Hunt?'
    MC @talk "Yeah, can you get back into-"
    'Looking down at the container, I could see after last time, it now had a large crack running down it.'
    MC '(Fuck, this is no good.)'
    MC @talk "Myu, wait here while I look for something for you to hide in."
    MYU @talk "No... Myu... help."
    show myu at center_f with easeinright
    MC @think "Help? What are you-"
    'Myu dropped down into her puddle like form once again, crawling toward me quickly as she clambered up through the crevices of my armour.'                 
    hide myu with dissolve
    MC @surprised 'WHAT ARE YOU-'
    'I could feel Myu warmly resting beneath my armour, she was calm, and only lightly shifting beneath me.'
    'To the untrained eye, no one would know the difference.' 
    MYU 'Myu! Myu!'
    MC @lewd 'H-Hey! Easy down there!'
    MYU 'Myu... Hide... People... No see.'
    MC "(It's almost alarming how fast she's learning to speak Alderian.)"
    MC "{i}*Sigh*{/i}"
    show mc at cleft_f, blurin
    MC @serious "Okay, Myu, but no coming out till I say, okay?"
    MYU 'Okay!'
    'Beneath all the shifting under my armour, I felt what seemed like a lone tentacle sneakily moving further down than the others.'
    hide mc with easeoutleft
    MC @talk "Myu... What are you doing?"
    'The tentacle quickly retreated.'
    MYU "{i}...Nothing!{/i}"
    MC '...'
    scene black with dissolve
    'With Myu shuffling beneath my armour, the two of us headed out into the Evening.'
    'The first thing I did was head into the darkened back streets, away from too many prying eyes where I knew bandits and other unsavoury figures tended to linger.'
    "It didn't take long before I was surrounded by a group of thugs, blades drawn ready."
    $ LocSet("novaras_dist_house")
    $ LocFlush()
    show mc at left
    show cg_bandit_dark at right_f as bandit1:
        zoom 0.9
    show cg_bandit_dark at cright as bandit2
    show cg_bandit_dark at center as bandit3:
        zoom 0.95
    with dissolve
    THUG "Enjoying a little evening stroll, are we?"
    THUG "Hand over your coin and we'll let you walk."
    MC @talk "...Myu, are you ready?"
    MYU "..."
    'Myu said nothing, but I can feel something {i}changing{/i} beneath my armour.'
    'She might not have been able to understand all the words said just now, but she could {i}sense{/i} the men before her were hostile, and just like that, her animal instincts kicked in.'
    'Pouring out of my armour, she re-formed herself in a frightening visage of sharp blades and teeth, snarling at the terrified bandits who immediately began to panic.' #Show Myu monster form
    hide mc with easeoutleft
    show cg_myu_monster at left with dissolve
    MYU "{i}*Snarls!*{/i}"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    THUG "WHAT THE FUCK IS THAT?!"
    THUG "Kill it! KILL IT NOW!"

    $ StartBattle(BattleData(BackgroundImage = "pbat_cityalleys", CharIDList_LeftExtra = ["myu"], CharIDList_Right = ["e_thug", "e_bandit", "e_thug"]))

    "As I drew my blade down across the last thug, I turned to see Myu."

    $ LocFlush()
    show cg_myu_monster_blood at center
    with dissolve

    "Having eviscerated one of the bandits into a bloody pulp of flesh and blood, she was dissolving and devouring his flesh."
    "The Blood splatter on her body was absorbed through her skin, and the cute innocence she had conveyed until now was all but gone."
    "Only this ghastly nightmare stood before me, lapping up the warm blood like milk."
    "One of the bandits still squirmed as she pressed her bladed hand into his body."
    show mc at left with easeinleft
    "Small tendrils pushed through his ripped open eye sockets and mouth."
    "Tentacles tore their way through his body and could be seen shifting about beneath the skin."
    show cg_myu_monster_blood at nod
    "He gargled and choked as the tentacles seemed to puppeteer him briefly till he finally fell still, dead and drained pale white."
    "For a moment, I considered abandoning this... {i}thing{/i} right here."
    "I could escape, let the City Guard handle this {i}monster{/i} standing before me."
    stop music fadeout 1.0
    "Myu, noticing my expression, stopped eating and dragged her way towards me, the voice once again sweet as that innocent face of hers returned."
    hide cg_myu_monster_blood
    show myu at cleft_f, blurin
    with dissolve
    MYU @sad "We... Go?"
    MC @sad "...Y-Yes, we go."
    $ AutoMus(True)
    #Fade to black - cut to MC home with Myu
    scene black with dissolve
    "The two of us hurried as we slipped away into the darkness back home before the guards stumbled upon the grizzly scene left in our wake."
    $ LocSet("azul_safehouse")
    $ LocFlush()
    show myu at cright_f
    show mc at cleft
    with dissolve
    MYU @sad "...[player_name!t]?"
    MC @talk "Myu? What is it?"
    MYU @sad "{i}Why... Look at Myu like that...{/i}"
    MC @surprised "Huh?"
    MYU @sad "Back in alley..."
    MYU @sad "Not seen look at me like that before."
    MYU @sad "Was Myu bad?"
    MC @sad "I-"
    MC @sad "No, Myu, you weren't bad." 
    MC @talk "I've just never seen you like that before."
    MYU @sad "Like what?"
    MC @think "Just..."
    "I didn't know how to answer her, what {i}could{/i} I say after what I just saw?"
    MC @smile "Myu, why don't you get some rest?"
    MC @smile "Its been a long night."
    'Myu nodded softly, making her way towards the bedroom.'
    show myu at cright, blurin
    hide myu with easeoutright
    show regina at left with easeinleft
    REGINA @talk "How did it go?"
    show mc at cleft_f, blurin
    MC @surprised "[regina_ref_cap!t]! How long have you-"
    REGINA @smile "Oh, I just slipped in earlier to see how Myu was doing!"
    REGINA @talk "When I noticed she was gone, I figured the two of you must have been {i}out,{/i} so I decided to wait for you."
    MC @think "O-Oh, right, of course."
    show mc at cright_f
    show regina at cleft
    with easeoutright
    REGINA @sad "...So, how was it?"
    MC @serious "It was... Difficult seeing her do that."
    MC @sad "Like, it felt like I was dealing with another {i}monster.{/i}"
    REGINA @sad "{i}*Sigh*{/i}"
    REGINA @sad "It's her nature, [player_name!t], no matter how much she learns to be around humans, that killer instinct will always be there."
    MC @talk "...Is she safe to keep around?"
    '[regina_ref_cap!t] shrugged.'
    REGINA @talk "People have kept and trained slimes before."
    REGINA @talk "But its not like keeping a dog."
    REGINA @talk "Even if they {i}*can*{/i} speak, they can still switch at a moment's notice."
    MC @surprised "But, you said she's imprinted on me, right?"
    REGINA @talk "Doesn't mean she wont attack others if she gets overwhelmed or any number of things could happen..."
    MC @talk "Then what should I do with her?"
    REGINA @talk "Just keep an eye on her, that's all."
    REGINA @talk "Only time will tell."
    MC @talk "{i}*Sigh*{/i}"
    MC @talk "I need some room."
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("azul_safehouse_bedroom")
    $ LocFlush()
    show myu at center_f
    with dissolve
    MYU @sad "..."
    MYU @sad "Myu is..."
    MYU @sad "{i}Monster.{/i}"
    scene black with dissolve
    $ LocSet("novaras_dist_house")
    $ QstComplete(QstHumanExp)
    $ LocEnter()