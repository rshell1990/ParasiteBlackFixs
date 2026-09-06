init python:
    @AppendToAllQuests
    class EventKrishanaDay(LogicModule):
        def __init__(self):
            super().__init__()

            self.DayToFireEvent = -1

        def onStart(self):
            self.DayToFireEvent = GetGameDay() + 7

        def onEnter(self):  
            if not QstIsActive(QstTheComingStorm):
                if GetGameDay() >= self.DayToFireEvent:
                    if GetLocID() == renpy.random.choice(LocIDList_NovarasCityStreets):
                        return TriggeredEvent("ev_KrishanaDay")

        def onComplete(self):
            QstStart(HouseLockAdara)
            return

label ev_KrishanaDay:
    $ QstComplete(EventKrishanaDay)
    # Scene 1 - MC bedroom - morning (Winterized BG) (THIS ENTIRE EVENT IS ON-RAILS)
    #(event happens 2 days after quest ----)
    scene black with dissolve
    $ InfGainDaily(False)
    $ LocSet("mc_house_bedroom")
    $ CharSetClothes("mc", "pants")
    $ TimeAdvTo(TIME_MORNING)
    $ LocFlush(dissolve)
    "As the sunlight breaks through my bedroom window once more, my eyes slowly peel open to see the snowfall gently descending outside."
    show mc at cright_f with dissolve
    "I yawn, sleepily sitting up-right as I tried to remember what day it is."
    "Suddenly, [regina_ref!t] came bursting through the door."
    show regina at cleft with easeinleft
    REGINA @smile "Happy Krishana day!" 
    MC @surprised "Huh?"
    REGINA @shock "I know you've been busy lately with your quests, but did you seriously forget what day it is?"
    REGINA @smile "It used to be your favorite day when you were younger you know!"
    MC @smile "A-Ah ... It's come around so fast this year."
    MC @think "Guess I really have just been losing track of time these last few days."
    REGINA @talk "Indeed, we even have the northern snow from Angmurus managing to blow it's way down here this year."
    REGINA @smile "Very festive, wouldn't you agree?"
    menu ev_KrishanaDay_regina_dialogue_menu:
        "Will Erika be home this year?":
            REGINA @talk "She said she would come tomorrow morning for the winter feast and to deliver some gifts."
            jump ev_KrishanaDay_regina_dialogue_menu
        "Did father send any news?":
            REGINA @talk "A short letter arrived earlier, telling me he's well and misses everyone very much."
            REGINA @smile "He wanted me to wish you a happy Krishana day."
            jump ev_KrishanaDay_regina_dialogue_menu
        "Happy Krishana day to you too, [regina_ref!t]":
            pass
    "[regina_ref_cap!t] practically bounced on the spot in excitement."
    REGINA @smile "I have a small gift for you dear."
    show regina at blurin, nod
    "From her pouch, [regina_ref!t] produced a small bag that jingled with coins."
    MC @surprised "[regina_ref_cap!t]! No, I can't-"
    $ PlayerAddItem("gold", 250)
    REGINA @talk "Take it, you can never have enough coin."
    MC @smile "{i}*Sigh*{/i}"
    MC @smile "You know I don't have anything for you, right?"
    REGINA @talk "Having you back here safe is enough for me."
    "[regina_ref_cap!t] smiled warmly at me."
    REGINA @talk "Come now, hurry up and get dressed, you've got a lot of people to see!"
    MC @surprised "I do?"
    REGINA @smile "Yes! Now get dressed!"
    MC @smile2 "Alright, I'm coming, I'm coming..."
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    "No sooner had I got dressed and made my way into the living room, there was a loud banging knock at the door."
    $ PlaySoundRandom("woodenDoor")
    scene cg_krishday_mc_livingroom
    show regina at left
    with dissolve
    show mc at cleft with easeinleft
    show markus at right_f with easeinright
    MARKUS @smile "Welcome! WELCOME ALL!"
    MARKUS "Soon you'll get to experience a truly legendary sight!"
    MARKUS @smile "The feeble [player_name!t] trying to defeat me in a drinking game tonight!"
    "Markus smiles and leaps forward, embracing me in a hug before pulling back and grinning."
    show markus at cright_f with easeinright
    MARKUS @smile "I've already set the two of us down a tab and invited a few old friends!"
    MC @smile2 "Happy Krishana to you too, old friend."
    REGINA @angry "I hope you aren't planning on getting him too drunk."
    REGINA @smile "He does need to be conscious for the meal in the morning."
    MARKUS @smile "It'll just be a few drinks at the {i}Iron Unicorn,{/i} I'll return him to you in one piece!"
    REGINA @talk "Hmm, just be safe."
    MARKUS @smile "Don't worry, I'll keep him safe!"
    MC @think "Isn't it usually the other way around, {i}me{/i} escorting you home?"
    MARKUS @shock "I'm shocked at the allegations! Complete slander!"
    MC @smile "Ah, of course, totally not true, I didn't at all have to carry you home the previous year because you got too drunk and threw up all over Annette Lytwan."
    MARKUS @smile "No idea what you're talking about, didn't happen!"
    "Again, there was a knock at the door, but this time, they were a series of small, soft knocks."
    show adara at right_f with easeinright
    ADARA @smile "Happy-"
    ADARA @shock "Oh! Markus!"
    MARKUS @smile "Happy Krishana day to you as well, Adara."
    "For a moment, there was a brief awkward silence as Adara blushed looking at me, her eyes constantly darting towards the floor."
    ADARA @shame "U-Um, Markus..."
    MARKUS "Hm? What is it?"
    "Adara continued to blush, brushing her hair back as she looked at me."
    "Looking towards me, and then back at Adara, Markus finally caught on."
    MARKUS @shock "OH!"
    MARKUS @smile "I'll see you later, [player_name!t]."
    MARKUS @smile "You two love birds enjoy yourselves."
    MC @surprised "Markus!"
    ADARA @shock "M-MARKUS!"
    "Markus laughed as he made his way towards the door."
    hide markus with easeoutright
    REGINA @smile "Happy Krishana day, Markus!"
    MARKUS "And you!"
    $ PlaySoundRandom("woodenDoor")
    "As Markus closed the door behind him, [regina_ref!t], sensing the mood, clasped her hands together and smiled."
    show adara at cright_f with easeinright
    REGINA @smile "I just remembered I had some ingredients I was missing for the morning feast!"
    REGINA @talk "I'll head out and umm, leave you two to it."
    hide regina with easeoutright
    "Humming to herself, Regina headed out the door, waving the two of us goodbye as she closed the door shut behind herself."
    $ PlaySoundRandom("woodenDoor")
    $ CharSetVar("adara", "blush", True)
    ADARA @joy "Sooo, umm..."
    MC @lewd "ummm..."
    "Adara leapt forward, tightly hugging me."
    hide adara
    hide mc
    show cg_adara_hug_armor_2 at center
    with dissolve
    MC "Whoa! What's brought this on?"
    ADARA "Just ... {i}Happy that you're here.{/i}"
    "Adara took a deep breath as she nestled her face into my chest."
    ADARA "You smell really nice."
    MC "..."
    "Realising what she said, Adara pulled away abruptly."
    hide cg_adara_hug_armor_2
    show mc at cleft
    show adara at cright_f
    with dissolve
    ADARA @shock "U-Uhh!"
    ADARA @shame "S-Sorry."
    ADARA @shame "I don't know what came over me."
    menu:
        "It's fine ... You smell nice too.":
            ADARA @joy "T-Thanks..."
            ADARA @shame "(Gods, I'm going to die of embarrassement!)"
            ADARA @shame "(I can't believe I just said that!)"
        "So, what brings you here?":
            ADARA @smile "J-Just wanted to wish you a happy Krishana day I guess..."
    "Adara paused sheepishly, her hands clasping at her dress tightly."
    ADARA @shame "I was wondering if perhaps maybe we c-could..."
    ADARA @joy "G-Go for a walk?"
    $ CharSetVar("adara", "blush", False)
    MC @lewd "Where shall we head to?" 
    ADARA @smile "There's quite a lot going on at the Market I'm told, perhaps we should head there?"
    MC @smile2 "Alright, that sounds good to me."
    scene black with dissolve
    $ LocSet("novaras_market_stalls")
    "The two of us made our way through the winding Novaras streets, the gentle snow falling onto the ground as children hurried through excitedly to meet their friends."
    scene cg_krishday_market
    $ LocUpdateDynSound()
    show mc at cleft
    show adara at cright_f
    with dissolve
    "At the Market, it was like a kind of festive carnival."
    "Merchants, roasted meat over open fires that filled the air with a sweet aroma, with small crowds gathering around eager for a taste."
    "Children hurried around, throwing snowballs at their friends, parents watched and chatted amongst themselves from afar."
    "One merchant with huge mead barrels opened, poured patrons small cups who huddled together and laughed to themselves merrily."
    'For a brief moment in time, it was as though everyone forgot about the wars existence outside these city walls...'
    ADARA @smile "Isn't it nice to see everyone out and so cheery?"
    MC @think "The last time it was like this was when-"
    "I pushed the thought of the Terminus ceremony to the back of my mind."
    "This was a happy time."
    ADARA @smile "Look at this place! Isn't it wonderful?"
    "I smiled as the children chasing each other with snowballs hurried out in front of us."
    MC @smile2 "Yes, it's nice."
    ADARA @joy "What should we do now?"
    scene cg_krishana_cute with dissolve
    $ Pause()
    $ TimeAdvBy(TIME_2H)
    "The time went by quickly as we had fun, it was always easy letting time drift by with Adara."

    MAD_PROPHET 'GATHER! GATHER ALL!'
    scene cg_krishday_market 
    show cg_prophet at right
    with dissolve
    show mc at left with easeinleft
    show adara at cleft_f with easeinleft
    ADARA @shock "Isn't he cold wearing so little in this weather?"
    MAD_PROPHET "Come and hear the tale of Krishana the ice dragon!"
    ADARA @smile "What do you think? Wanna listen?"
    menu:
        "Why not?":
            hide mc
            hide adara
            with dissolve
            show cg_prophet at blurin, center
            "The two of us stepped closer and joined the growing crowd, mainly comprised of children but a few adults lingered."
            MAD_PROPHET "And so we begin, centuries long past, Krishana, the great ice dragon, sat on her ice throne in the mountains of Angmurus!"
            MAD_PROPHET "{i}Bored!{/i}"
            "The crowd laughed a little."
            MAD_PROPHET "{i}'I know!'{/i} Thought the mighty dragon, {i}'I shall see what the humans down south are up to!'{/i}"
            MAD_PROPHET "As her mighty wings soared, she headed down south, perching herself up on a small mountain, watching the villagers down below!"
            MAD_PROPHET "The people revered but feared the mighty dragons! And each parent warned the children not to approach the great Krishana!"
            MAD_PROPHET "Some young children, brave and adventurous, ignoring their parents advice, scaled the small mountain and approached the dragoness!"
            MAD_PROPHET "{i}'But what brings you small humans here?'{/i} The dragoness asked!"
            MAD_PROPHET "{i}'Oh great Krishana! It has not snowed in these lands for so long! Can you not make it so?{/i}"
            MAD_PROPHET "The dragon laughed, and laughed and laughed!"
            MAD_PROPHET "{i}But what in return shall thy give thee?{/i} The dragoness asked."
            MAD_PROPHET "{i}For my hordes of gold are vast, and I never suffer hunger long!{/i}"
            MAD_PROPHET "{i}What could you possibly have to offer me?{/i}"
            MAD_PROPHET "The children looked amongst themselves for a moment, till one stepped forward and offered the great Krishana a small stone."
            MAD_PROPHET "{i}But what is this?{/i} The dragoness asked."
            MAD_PROPHET "{i}It is a waystone!{/i} the child answered!"
            MAD_PROPHET "{i}So no matter where you fly, you will always be able to find your way home here!{/i}"
            MAD_PROPHET "Krishana took the small gift, and boomed, {i}'HOME? HERE? FOR ME?'{/i}" 
            MAD_PROPHET "The dragoness, so touched by the gift, said with a cool blow of air, {i}I've never had a home before.{/i}"
            MAD_PROPHET "Before the children could answer, the mighty Kirshana unleashed her icy breath into the sky, and the children celebrated as the snow fell down!"
            MAD_PROPHET "And so it was, Krishana returned every year to bring forth the snow in exchange for the children's gifts!"
            MAD_PROPHET "And thus, that is why yearly we share gifts amongst loved ones and friends! To celebrate this most joyous of times!"
            "The crowd clapped and handed over some coins towards the man, who collected them in a small jar."
            hide cg_prophet with dissolve
            show adara at cright_f
            show mc at cleft
            with dissolve
            ADARA @smile "Krishana was always one of my favorite stories growing up."
            ADARA @smile "Isn't it nice to just hear a story not always about death and violence once in a while?"
        "I've heard the story a hundred times before.":
            ADARA @talk "Ah, okay then..."
    ADARA @talk "It's getting quite late."
    ADARA @shame "Do you mind walking me home?"
    MC @lewd "Do you even need to ask that?"
    "Adara smiled."
    $ CharSetVar("adara", "blush", True)
    ADARA @talk "C-Come on then, it's cold just standing here talking!"
    show adara at blurin, cright
    hide adara with easeoutright
    hide mc with easeoutright
    scene black with dissolve
    $ LocSet("adara_house_living_room")
    $ LocUpdateDynSound()
    $ TimeAdvBy(TIME_05H)
    "{i}After a short walk back to Adara's home...{/i}"
    scene cg_krishday_adara_livingroom
    show adara at cleft
    show mc at cright_f
    with dissolve
    ADARA @talk "Thank you for walking me home, [player_name!t]."
    MC @smile "Anytime, Adara."
    MC @lewd "And uhh, I hope you had a nice time today."
    ADARA @joy "M-Mmm, I did..."
    "The two of us paused awkwardly for a moment, not knowing what to say to each other other."
    MC @think "Is... Your father not home?"
    ADARA @talk "He's probably resting right now ... He gets tired quite easily these days."
    MC @talk "Ah, of course."
    ADARA @shame "..."
    $ CharSetVar("adara", "blush", False)
    MC @surprised "...I should, um, probably get going."
    MC @smile2 "Markus is going to wonder where I am."
    ADARA @shame "R-Right, of course."
    show mc at blurin, cright
    "As I turned to leave, suddenly-"
    ADARA @shock "[player_name!t]! Wait!"
    hide adara
    hide mc
    show cg_adara_hug_armor_2 at center
    with dissolve
    "Adara forward into my arms to hug me."
    ADARA "...Can you come back here tonight when you're finished with Markus?"
    ADARA "{i}I have something important I need to tell you...{/i}"
    MC "What is it?"
    ADARA "Just ... Just come back here later please, okay?"
    MC "Alright, I'll try visit you later before heading home."
    hide cg_adara_hug_armor_2
    show adara at cleft
    show mc at cright_f
    with dissolve
    "Adara pulled herself away from me shyly."
    ADARA @shame "H-Have a nice evening."
    MC @lewd "I'll see you later."
    MC @smile2 "...Happy Krishana day, Adara."
    ADARA @joy "Y-You too..."
    show mc at blurin, cright
    hide mc with easeoutright
    $ PlaySoundRandom("woodenDoor")
    ADARA @shame "({i}I've waited so long... I won't risk losing him again without telling him how I really feel.{/i})"
    scene black with dissolve
    $ LocSet("novaras_tavern")
    $ LocUpdateDynSound()
    scene cg_krishday_tavern
    show markus at cright_f
    show shay at cleft
    with dissolve
    "The tavern fire roared as merry people gathered around, cheering and spilling ale and wine onto the floor."
    "A sweet aroma filled the air from the pig-roast being carved up and served to patrons."
    "As Shay sweatily bounced around serving drinks to the packed tavern, some ale accidentally spilled over onto her breasts, causing a roar of cheers from the men."
    hide shay with easeoutright
    show mc at cleft with easeinleft
    MARKUS @smile "[player_name!t]!"
    MARKUS @smile "You made it!"
    MC @smile "Of course, you didn't seriously think I'd miss the chance to humiliate you in a drinking competition, did you?"
    MARKUS @smile "Haha! We'll see about that!"
    scene black with dissolve
    "{i}...Many drinks later.{/i}"
    WHITE "(Why do our hosts continue to drink fluid that is toxic to them?)"
    BLACK "(Species bonding ritual from what I have assessed.)"
    BLACK "(...Or perhaps our hosts are mentally addicted and damaged, I shall make sure.)"
    WHITE "(I too shall evaluate my host isn't broken, for having to remove this much excess poison indicates some kind of wider issue at large.)"
    scene cg_krishday_tavern
    $ LocSet("novaras_tavern")
    $ CharSetClothes("mc", "mug")
    show mc at cright_f
    show cg_markus_mug at cleft
    with dissolve
    MARKUS @smile "Shhh...! Yhouu both need to lhearn to have mhoar fhun!"
    BLACK "(...)"
    WHITE "(...Ensuring no other parasitic lifeforms have infiltrated our hosts.)"
    menu:
        "Chomee ohnn! Cheer uphh yah sphooky fhuckkks!":
            BLACK "(You have successfully consumed enough alcohol to kill a sandworm.)"
            BLACK "(It is time to stop.)"
            MC @angry "BOOO!"
            BLACK "(...Petulant host.)"
            MC @angry "Whoo yho challin' penchant? I ahin't no pendulum!"
        "Ahhh, lhightenn uph!":
            MARKUS @angry "Yheahh! lghitenn uph!"
            WHITE "(I do find the affects of the alcohol ... relaxing.)"
            BLACK "(As do I.)"
            BLACK "(But our hosts must learn to respect their bodies more.)"
            BLACK "(Our {i}*gift*{/i} is not to be abused.)"
            MC @drunk "Shheshh, dhon't yhou twho have fhun ever?"
            WHITE "(The Hive must-)"
            MARKUS @smile "Uhuh, andh whathabout when yhour nhot sherving the hive? Hm?"
            BLACK "(...)"
            WHITE "(...{i}Fun{/i} This idea is strange.)"
            WHITE "(I remember doing things that were {i}fun,{/i} or at least...)"
            WHITE "(I remember the {i}feeling{/i} of fun, but cannot remember more than that.)"
            BLACK "(As can I...)"
            MC @drunk "Bahh! Kheep drhinkin!' You'll fhigure it out!"
        "Whath chu {i}thingss{/i} chelebrate theen?":
            BLACK "(...I remember fragments, like pieces of broken glass.)"
            BLACK "(A great parade with me riding some beast through the crowds.)"
            BLACK "(Roars filling the air as thousands march behind.)"
            BLACK "(Why am I here? What is... This memory?)"
            MC @drunk "Ughh, thatsh dhon't shound like - Mmm! Krishana nghight!"
            BLACK "(...Nevermind.)"
    BLACK "(...We have decided the best method to teach you both self control is to prevent the alcohol poisoning, but allow the morning fog to occur.)"
    BLACK "(Enjoy your heads in the morning.)"
    MC @angry "Heyy! Get bhackk here!"
    MARKUS @angry "Bhloody things..."
    MC @drunk "Should we shloww dhown?"
    show shay at center with easeinleft
    SHAY @smile "You boys ready for your next round?"
    MC @drunk "...Absolutely!"
    MARKUS @smile "Bring em' here!"
    hide shay with easeoutright
    scene black with dissolve
    MARKUS @smile "I think - Ahh! Thatsh enough for mhee..."
    MC @drunk "Quiting eh?"
    MARKUS @smile "Haha! Chomee ohnn, Lhet's call it a night."
    MARKUS "Befhore whee rhun out of - mhmm! Coin..."
    MC "Hmm, ghood point."
    "One drunken walk to Markus' home later..."
    $ TimeAdvBy(TIME_DAY_END)
    $ LocSet("markus_house_livingroom")
    $ CharSetClothes("mc", "normal")
    $ LocFlush()
    show mc at cleft
    show markus at cright_f
    with dissolve
    MARKUS @smile "Ahh, That washa good night, ehh?"
    MC @smile2 "Mhm, it was."
    MC @lewd "Anyway, I bhetter..."
    MARKUS @shock "Whait a second!"
    MC @drunk "Hmm?"
    MARKUS @smile "Whatchh this!"
    "Grinning from ear to ear, I watched as Markus transformed in front of me into a beautiful blonde woman."
    play sound "audio/cfx/detect_magic.ogg"
    hide markus
    show markus_fem at cright_f
    with flash
    MC @surprised "{i}Markus!{/i}"
    MC @surprised "You're-"
    MARKUS_FEM @drunk "Heheh! Whatcha think?"
    "Markus voice was completely different to match the change in body, soft, alluring, {i}womanly.{/i}"
    MARKUS_FEM @drunk "Yhou should be able to dhoo this soon as whell if you can't alrheady!"
    "As my eyes stared over Markus' new body, I couldn't help but feel embarrassed and try to look away as my cock twitched in excitement."
    "Maybe it was just the drink doing the thinking for me, but ... It was hard to deny Markus looked good."
    MC @talk "I-Itsh nice..."
    MARKUS_FEM @drunk "I know ehh?!"
    MARKUS_FEM @drunk "And lookhh at the shize of mhyy thits! Haha!"
    "Without hesitating, Markus pulled out their huge breasts and showed them to me."
    MARKUS_FEM @drunk "Fufu! Dho yhu think they're bhigger thann Adara's?"
    "When Markus noticed I was staring so intently at their body, they themselves suddenly began to blush."
    MARKUS_FEM @drunk_blush "...D-Dho yho mhaybe whanna fheel them?"
    MC @surprised "...!"
    MARKUS_FEM @drunk_blush "I dhon't mhind ... Whieve bheen fhriends shince lhike... Forhever."
    MARKUS_FEM @drunk_blush "And uhmm, when I change lhike thish, I feel ... {i}different{/i} when I look at yhu..."
    MC @talk "You do?"
    MARKUS_FEM @drunk_blush "Mmm, the vhoice said somethin' about it altering my pherceptionss or somethin' when I'm lhike this."
    "There was a brief pause."
    MARKUS_FEM @drunk_blush "S-So, you whanna fheel them, or not?"
    menu:
        "{i}Feel the tits.{/i}":
            $ AutoMus(False)
            $ PlayMusic("audio/music/39_Passions.ogg")
            $ PlaySexFx("audio/sex_sounds/moans_breaths_loop.ogg", 1)
            "Stepping closer towards Markus, there was now a distinctively feminine smell that was being released from them, only adding to the confusion."
            scene markus_fem_boob_squeeze_1 with dissolve
            $ Pause()
            "As my hands reached out, I gently caressed at the soft breasts." 
            "My hands moved in a circular motion as I cupped and played with them, Markus' face in turn flushed red."
            MARKUS_FEM "M-Mhmm..."
            MARKUS_FEM "T-That feelshh kinda niceee."
            "My cock now throbbed painfully hard as I continued to fondle the large breasts."
            MARKUS_FEM "{i}*Huff*{/i}"
            MARKUS_FEM "{i}F-Fuck...{/i}"
            MARKUS_FEM "They're - {i}*Huff*{/i} More shenshitive than I - {i}*Huff*{/i} thought..."
            MARKUS_FEM "A-Ahh... Maybe we should S-St- Mhmm ... {i}*huff*{/i}"
            scene markus_fem_boob_squeeze_2 with dissolve
            $ Pause()
            "Mesmerised by what I was doing, I reached out to begin to tug and pull at the nipples lightly, making Markus shudder and moan." 
            MARKUS_FEM "Tschh!"
            MARKUS_FEM "C-Careful! Mhm ...!"
            MARKUS_FEM "Ooooh... What are y-you doing to-"
            "A small whimper escaped Markus' lips, causing Markus to bite down on their lip in pleasure."
            $ PlaySexFx("audio/sex_sounds/moans_muffled_suckey.ogg", 1)
            scene markus_fem_boob_squeeze_3 with dissolve
            $ Pause()
            "Some strange thought seemed to possess me, my one thumb pressed up against Markus' lips, and without hesitation, they wrapped their lips around it and moaned softly."
            MARKUS_FEM "M-Mmhh..."
            "My other hand continued to rub against the soft, large breast as their mouth seductively suckled on my thumb."
            MARKUS_FEM "(W-What am I doingshh?)"
            MARKUS_FEM "{i}*Huff* *Huff*{/i}"
            MARKUS_FEM "(T-Thish isn't r-right...)"
            "Eventually the two of us seemed to snap out of it, and Markus lighty shoved me away." #Anim end
            $ StopSexFx()
            $ LocSet("markus_house_livingroom")
            $ LocFlush()
            show mc at cleft
            show markus_fem at cright_f
            with dissolve
            MARKUS_FEM @drunk_blush "H-Haha! You - um, you rheally do t-take a jhoke too far shometimes!"
            $ UnlockGalSceneAndGrantXp("markus", "fem_boob_squeeze")
            MC @talk "U-Uhh, yesh, shorry, haha..."
            MARKUS_FEM @drunk_blush "..."
            MC @surprised "...I s-should probably go."
            show mc at blurin, cleft_f
            hide mc with easeoutleft
            MARKUS_FEM @surp "W-Wait! [player_name!t]!"
            MARKUS_FEM @sad "{i}*Sigh*{/i}"
            play sound "audio/cfx/detect_magic.ogg"
            hide markus_fem
            show markus at cright_f
            with dissolve
            MARKUS "(...!)"
            $ AutoMus(True)
            MARKUS @shock "(What the fhuck just happened?)"
        "I don't think that's such a good idea...":
            MARKUS_FEM @drunk "O-Ohh!"
            MARKUS_FEM @drunk "Haha, it was jhustt a joke friend."
            MC @smile "Ha, well, I should ghooo..."
            MARKUS_FEM @drunk "Mhm, be safe, friend!"
            #MC leaves.
    #Both routes continued 
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/38_SinfulRetreat.ogg")
    "I stumbled my way out of Markus' home, remembering Adara wanted to speak to me about..."
    "{i}Something.{/i}"
    "After a tedious stumble towards her door, the whole world spinning, I ever so gently knocked on the door to avoid making too much noise."
    $ LocSet("adara_house_living_room")
    $ LocUpdateDynSound()
    $ TimeAdvBy(TIME_05H)
    play sound "audio/cfx/door_knock.ogg"
    ADARA "(Who in all the hells is knocking that loud at this-)"
    $ PlaySoundRandom("woodenDoor")
    $ LocFlush()
    show adara at cleft
    show mc at cright_f
    with dissolve
    ADARA @shock "...[player_name!t]!"
    MC @drunk "I chamee to shee yhouu."
    MC @drunk "Jhust lhike you asheddd."
    ADARA @shock "Oh gods, you reek of ale!"
    MC @drunk "I've only hadshaaa few!"
    ADARA @talk "Where's Markus?"
    MC @drunk "Markus?"
    MC @drunk "Heshh finee."
    MC @surprised "...The rhoom's sthartin' to spin a-"
    "I suddenly felt my legs give out beneath me."
    scene black with dissolve
    play sound "audio/cfx/body_fall_ground.ogg"
    ADARA "{i}[player_name!t]{/i}!"
    "The world went black as I dozed in and out of consciousness."
    $ TimeAdvBy(TIME_1H)
    "I felt myself being dragged across the floor somewhere, and next, I remember myself feeling lighter and cold as my armour was stripped from me."
    $ TimeAdvBy(TIME_1H)
    "A soft voice was speaking to me, but I couldn't tell whose it was."
    $ TimeAdvBy(TIME_1H)
    "{i}J-Just keep still! Almost done!{/i}" 
    $ TimeAdvBy(TIME_1H)
    "Finally, I found myself wrapped beneath some warm, soft quilts as someone cuddled up against me."
    $ TimeAdvBy(TIME_1H)
    "{i}Just so you know, t-this is only because we don't have a spare bed.{/i}"
    $ TimeAdvBy(TIME_1H)
    "The voice droned on about things as it nestled up against me, but as I drifted in and out of semi-consciousness, I could only pick up words and phrases."
    $ TimeAdvBy(TIME_1H)
    "{i}Waited so long-{/i}"
    $ TimeAdvBy(TIME_1H)
    "{i}To tell-{/i}"
    $ TimeAdvBy(TIME_1H)
    "{i}You, I-{/i}"
    $ TimeAdvBy(TIME_1H)
    "Eventually even this confused state of semi-consciousness passed, and everything fell silent into black, dreamless dreams."
    $ AutoMus(True)
    $ TimeAdvTo(TIME_MORNING)
    $ LocSet("adara_house_bedroom")
    $ LocFlush()
    $ CharSetClothes("mc", "pants")
    show mc at cleft
    show adara at cright_f
    with dissolve
    "Slowly, my eyes peeled open, the morning light piercing through the window and everything was far too bright for me."
    "My head felt almost removed from my body as I looked around dazedly."
    MC @scared "Urghh ... My head feels like it's been smashed in with a rock."
    ADARA @angry "I'm not surprised."
    "I winced in pain."
    MC @angry "Tschh!"
    MC @think "What am I doing here?"
    ADARA @shock "...How much did you drink?"
    MC @sad "Urghhh ... I don't remember."
    "Looking back at the bed quilts and then towards a shy looking Adara, the thought occurred to me..."
    MC @surprised "Did we-"
    $ CharSetVar("adara", "blush", True)
    ADARA @shame "N-No."
    ADARA @shame "I would have slept somewhere else if I could, but we don't have a spare r-room."
    $ CharSetVar("adara", "blush", False)
    MC @talk "Ahh..."
    MC @think "I should probably-"
    "I found myself feeling woozy and weak, my head still pounding."
    MC @angry "Grghh!"
    ADARA @shock "Take it easy!"
    ADARA @sad "You need more rest."
    MC @scared "I-"
    MC @talk "Yes, I suppose you're right."
    ADARA @angry "Of course I am, from the sounds of things, it's a miracle you and Markus didn't drink yourselves into early graves!"
    ADARA @angry "I hope you both know when you're recovered, I'll be slapping both of you for being so foolish!"
    MC @sad "Believe me, this is punishment enough."
    "My head continued to sorely throb as I heard what sounded like a mildly bemused chuckle in my head."
    BLACK "({i}...Heh.{/i})"
    MC "(Did you just laugh at MY misery?)"
    BLACK "({i}Of course not, I focus solely on the hive and our survival.{/i})"
    MC "(Is that so? If you're focusing so hard on our survival, why don't you do something about this headache then?)"
    BLACK "({i}To teach you to look after OUR body better.{/i})"
    BLACK "({i}I do not exist to purposely remove self inflicted poisons you put into your body for self-amusement.{/i})"
    BLACK "({i}Continuing to filter the poison from your system will only encourage you to behave even more recklessly.{/i})"
    MC "(It's called ale and it's fun, do you need a lesson in what 'fun' is or do I have to break that down for you too?)"
    ADARA @shock "Uhh, is everything okay, [player_name!t]?"
    ADARA @talk "You seemed kinda lost there for a second."
    MC @surprised "Oh, uh, yes, everything is fine."
    ADARA @talk "Why don't you lay down and rest some more, I'll come back in a bit and check in on how you're doing."
    "I groan groggily."
    MC @sad "That's ... Probably a good idea."
    "Adara smiled, turning to leave."
    MC @talk "Adara?"
    ADARA @talk "Hm?"
    MC @think "You mentioned wanting to talk to me about something last night before I got too drunk."
    MC @talk "What was it about?"
    $ CharSetVar("adara", "blush", True)
    ADARA @talk "I-"
    ADARA @shame "Nothing! J-Just..."
    $ CharSetVar("adara", "blush", False)
    "Adara pondered her next choice of words carefully."
    ADARA @joy "Ah! I'll tell you another time! It's nothing important!"
    "As Adara left the room and closed the door behind herself, I dropped back down onto the bed to rest a little longer."
    scene black with dissolve
    "({i}Later while resting...{/i})"
    if CharIsLover("adara"):
        jump ev_KrishanaDay_adaraSexScene
    else:
        jump ev_KrishanaDay_adaraNoSexScene

label ev_KrishanaDay_adaraSexScene:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    "{i}*...Slurp...Slurp*{/i}"
    "A pleasant, warm feeling enveloped my cock."
    "As my eyes slowly peeled opened, I awoke to the sight of Adara, naked on the bed in front of me, her mouth wrapped around my cock." #Cut to BJ anim 
    scene adara_krishana_bj with Dissolve(1.0)
    $ Pause()
    MC "Adara!?"
    MC "What are you-"
    MC "Ahh...!"
    "Adara pulled her lips away to speak, but her hand in it's place stroked my cock as she spoke."
    $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg", 1)
    scene adara_krishana_hj with dissolve
    $ Pause()
    ADARA "Ahh, s-sorry!"
    ADARA "Y-You were all hard and tense when I came back in and I couldn't wake you up."
    ADARA "S-So, I thought I would help you and take care of it?"
    "Adara added hastily."
    ADARA "I-I can stop if you'd like!"
    MC "Ah! N-No, carry on..."
    "Adara smiled softly as she adjusted her grip and moved her hand a little faster."
    ADARA "If - If I'm being honest, I kinda thought this would be my gift for you for Krishana day."
    ADARA "H-Hope you like it..."
    "I grunted in approval, her hand working my cock well."
    ADARA "Is this okay? Am I doing good?"
    MC "Mfghh! Y-Yes, you're doing great!"
    ADARA "Really? Umm, I heard some of my friends talk about h-how they did this with their lovers."
    ADARA "I've never d-done anything like this before so-"
    MC "Ahh ... You're doing fine!"
    "Encouraged by my words, Adara tightened her grip slightly as she continued to stroke my cock."
    "My eyes lingered over Adara's lushious body, her large butt pushed into the air with her huge soft tits pressing against my thigh."
    ADARA "...S-So, you like my butt?"
    MC "I - {i}*Huff*{/i} Like all of you!"
    "My words only seemed to excite Adara more, who heavy breaths grew more flustered as she continued."
    ADARA "B-Bet you'd like me more if I put my mouth back on your thing, h-huh?"
    MC "Mmmfghh! Adara...You-"
    "Adara's lips wrapped around my cock once more."
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)
    scene adara_krishana_bj with dissolve
    $ Pause()
    MC "Oh fuck!"
    "Adara's soft mouth wasted no time as her head began to lightly move up and down."
    ADARA "Mmmfgh...{i}*Slurp!*{/i}"
    ADARA "(My mouth feels like it can barely stretch over his thing!)"
    "My hands tightened, gripping the sheets as Adara's tongue thrashed and beat against my cock."
    "Wet slurping sounds escaped her lips as she brushed her hair back over her shoulder and did her best to dip her head down further."
    ADARA "(Mhmm... The other girls said doing this was exciting, b-but getting so wet just from doing this is really embarrassing.)"
    ADARA "(I-I feel like such a whore for him.)"
    ADARA "(Why does it feel so right though?)"
    "I groaned in pleasure as Adara's wet lips glided over my cock, coating my member in her warm saliva."
    "She seemed utterly absorbed in her task, her tight lips formed a thight seal around me and moved in a steady motion as arousing wet moans escaped her lips."
    ADARA "Mhmmhh... {i}*Slurp! *Slurp!*{/i}"
    MC "{i}*Huff*{/i} Adara..."
    MC "I don't know how much longer I can - Mfghh!"
    ADARA "Mhhfhh! {i}*Slurp!*{/i}"
    "Adara's tongue twisted and wrapped around my cock lovingly as my increasingly sensitive member finally felt unbearable to hold back any longer."
    MC "Adara ... {i}*Huff*{/i} I'm going to-"
    MC "HRGHHH...!!" #Cum in mouth
    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    scene adara_krishana_bj_finish with flash
    $ ReduceInfectionFromSex("adara")
    $ Pause()
    $ UnlockGalSceneAndGrantXp("adara", "krishana_bj")
    "Unable to hold back the overwhelming urge any longer, I poured my hot load into Adara's mouth."
    ADARA "Mmfghh?!"
    "Adara's eyes widened in shock as she felt the rush of hot fluid, but as her cheeks flushed red and her eyes softened, she did her best to swallow down the heavy load."
    "As her lips finally pulled away from my cock, she gasped for air and showed me her open mouth to show she'd swallowed everything." #sex scene ends 
    $ LocFlush()
    $ CharSetClothes("mc", "naked")
    show mc at cleft
    show adara at cright_f
    with dissolve
    ADARA @shame "How - {i}*Huff*{/i} Was that?"
    MC @bitelip "Well, do you think you could wake me up like that from now on?"
    ADARA @joy "Haha!"
    ADARA @joy "Maybeeeee."
    $ CharChangeRel("adara", 1)
    $ AutoMus(True)
    "Remembering why I stayed the night in Adara's home to begin with, it felt like now might be the right time to ask."
    MC @smile "Adara, I know you said it wasn't anything important..."
    MC @think "But why did you want to speak to me last night?"
    ADARA @shock "...I-"
    GERARD "Adara! Are you up girl?"
    GERARD "Help me out of this damn bed!"
    ADARA @shock "It's father!"
    ADARA @shock "Hurry, pack your things and leave before he sees you!"
    "Adara hastily ran to gather up my clothes."
    ADARA @shock "I-I'll keep him busy, just please, don't be seen!"
    show adara at blurin, cright
    hide adara with easeoutright
    "Before I could answer her, Adara hurried out of the room to keep her father distracted."
    MC "(Damn ... I better do as she says and get out of here.I am already going to face her wrath, Me and Markus both.)"
    scene black with dissolve
    $ CharSetClothes("mc", "normal")
    jump ev_KrishanaDay_returnHome

label ev_KrishanaDay_adaraNoSexScene:
    $ TimeAdvBy(TIME_2H)
    $ TimeAdvBy(TIME_2H)
    $ Pause(0.5)
    $ LocFlush()
    show mc at cleft
    show adara at cright_f
    with dissolve
    "My eyes once again slowly peeled open to see Adara stood before me."
    ADARA @talk "Feeling any better?"
    "I groaned in acknowledgment."
    MC @think "Yes... Well enough at least."
    ADARA @smile "Good."
    ADARA @talk "Father should be waking up soon, gather up your clothes and head home."
    show adara at blurin, cright
    "As Adara turned to leave, I called to her."
    MC @talk "Adara..."
    ADARA @talk "What is it?"
    show adara at blurin, cright_f
    MC @talk "Adara, I know you said it wasn't anything important..."
    MC @talk "But why did you want to speak to me last night?"
    ADARA @shock "...I-"
    GERARD "Adara! Are you up girl?"
    GERARD "Help me get out of this damn bed!"
    ADARA @angry "Damn it...!"
    ADARA @shock "Get your things and go, father can't see you like this."
    MC @talk "But we didn't {i}do{/i} anything."
    ADARA @talk "All he's going to see is a naked man in his daughters bed, do you think he's going to listen to what you have to say?"
    MC @think "Ahh, good point."
    ADARA @talk "I'll keep him busy for as long as I can, go on now, hurry!"
    show adara at blurin, cright
    hide adara with easeoutright
    "Before I could answer her, Adara hurried out of the room to keep her father distracted."
    MC "(Damn ... I better do as she says and get out of here. I am already going to face her wrath, Me and Markus both.)"
    scene black with dissolve
    $ PlaySoundRandom("woodenDoor")
    $ CharSetClothes("mc", "normal")
    jump ev_KrishanaDay_returnHome

label ev_KrishanaDay_returnHome:
    $ Pause(0.5)
    $ TimeAdvBy(TIME_05H)
    "After sneaking out of Adara's house, I swiftly made my way home..." #One line fade to black 
    $ LocSet("mc_house_kitchen")
    $ PlaySoundRandom("woodenDoor")
    $ LocFlush()
    show regina at cleft
    with dissolve
    show mc at cright_f with easeinright
    REGINA @shock "[player_name!t]!"
    REGINA @talk "There you are! Why didn't you come home last night?"
    MC @talk "I, uhh ... Got a little too drunk, Sorry."
    "I did my best to smile awkwardly as [regina_ref!t] sighed."
    REGINA @smile "Well, at least you're back now."
    show erika at left with easeinleft
    ERIKA @smile "Still getting yourself into trouble, I see?"
    MC @smile2 "Erika!"
    "Erika's eyes sized me up."
    ERIKA @smile "...You're looking different these days!"
    menu:
        "I know, even I didn't believe I could become MORE handsome somehow, yet here I stand.":
            ERIKA @talk "Ahhh ... Of course."
            ERIKA @smile "I see your time in the scouts has done nothing to reign in your ego."
            ERIKA @smile "Well, I suppose it's nice to know some things never change at least."
        "You're looking well too, Erika.":
            "Erika smiled warmly."
            ERIKA @smile "It's good to see you, [player_name!t]."
    if len(rel_known_chars) == 0: #If player DOESN'T have any characters romanced
        REGINA @talk "Take a seat, dear, the feast is almost ready."
        jump ev_KrishanaDay_dinner
    else: #If player has ANY of the following characters romanced, (Nyx, arlena, divine, Nijah, dros/draya, Elena, Myu).
        jump ev_KrishanaDay_gifts

label ev_KrishanaDay_gifts:
    REGINA @shock "...Oh! That reminds me."
    REGINA @smile "There's a couple gifts for you in your room, [player_name!t]."
    REGINA @talk "A few ladies stopped by to ask for you..."
    ERIKA @surp "Wait, you mean to tell me someone's actually fallen for his {i}'charms?'{/i}"
    ERIKA @surp "I'll have to conduct a thorough investigation at once, no doubt they're dark mage agents using him to try to get close to me!"
    ERIKA @smile "{i}...Or they're blind.{/i}"
    MC @angry "Hey!"
    ERIKA @smile "I jest ... though do try to do some thinking upstairs and not just downstairs."
    ERIKA @talk "One scornful maiden is enough."
    REGINA @angry "Erika..."
    ERIKA @talk "Yes, yes, don't mention {i}she who shall not be named{/i}, I won't bring it up again."
    REGINA @talk "Good, leave bad rot in the past."
    REGINA @talk "Go look at your presents, [player_name!t], I'll call you when the feast is ready."
    hide mc with easeoutleft
    scene black with dissolve
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    show mc at cleft
    with dissolve
    "Inside my room, I looked around for who visited the previous night while I was out..."
    if CharIsLover("nyx"):
        "One such letter was addressed to me with a formal seal, that when opened, was written in bold capitalized writing."
        "{b}YOU WILL APPRECIATE YOUR GIFT AND ENJOY IT GREATLY MORE THAN ALL THE OTHER GIFTS YOU RECIEVE - HAPPY KRISHANA DAY - Captain Nyx.{/b}"
        "A well-crafted sword sat next to the letter, and despite it's sharpness and sturdyness, the thing was undoubtedly light as a feather."
        "Its hilt was decorated in an exquisite manner: flowery patterns contrasted with aggressive, sharp lines."
        "I remembered seeing Alderian officers carry weapons of a similar design."
        "Admiring the sword I couldn't help but chuckle at Nyx's clumsy romantic abruptness..."
        $ PlayerAddItem("nyx_gift_sword")

    if CharIsLover("arlena"):
        "There was a small letter with an expensive looking gem that had been encased into a necklace." 
        "{i}I found this pure gem amongst the others you collected for me, and thought it'd make a nice gift, you can sell it if you wish, just don't bloody expect this cutesy nonsense all the time! - Happy Krishana day, Yours always, Arlena{/i}" 
        "I smirked, knowing Arlena likely spent considerable hours tidying up the crude gem and encasing it into the necklace ... It will likely fetch a pretty coin."
        $ PlayerAddItem("arlena_gift_amulet")
    
    if CharIsLover("divine"):
        "A letter was attached, and with it was one, beautiful amulet radiating some kind of magecraft."
        "{i}When I am around you, the years of loneliness seem to fade away... thank you, for making me feel what it means to be cared for - Happy Krishana day, my beast, your darling, - Sister Divine{/i}"
        "I stared down at the amulet, such a thing would normally be reserved for only those of much higher esteem than myself."
        "I felt the maddening encroach of my infection slow even just holding it to inspect..."
        $ PlayerAddItem("divine_gift_amulet")

    if CharIsLover("nijah"):
        "There was what seemed to be a letter, somewhat poorly written with some food attached."
        "{i}We do not celebrate this day in Ramon, but, I think it is important to you, so here is a gift my love - Love, Nijah. Iz my writing getting better?{/i}"
        "The food looked delicious, and even though it was now a little cold, no doubt I could eat it in the morning." 
        $ PlayerAddItem("ramonian_twister", 4)
     
    if CharIsLover("dros"):
        "A note was hastily attached to a shiny, ruby encrusted ring that seemed to radiate some kind of light energy."
        "{i}Look, just because you're an adventurer dear, doesn't mean you're excused from being unfashionable, hope this helps - yours truly, D.{/i}"
        if CharGetVar("dros", "Transformed") == True:
            "My thoughts lingered towards the elven shopkeeper, and I smirked at the thought of Dros no doubt carefully picking out the right ring for me."
            "The real question is, how did they know it would fit perfectly?"
        $ PlayerAddItem("dros_gift")
    
    if CharIsLover("elena"):
        "Elena approached me with a book in her mouth."
        show elena_w_book at center with easeinleft
        ELENA "BARK!"
        MC @smile "Hm? What's this?"
        "Taking the book from her mouth, Elena's tail wagged as she waited for me look at it."
        "{i}The dreams of Ashara - A love story.{/i}"
        MC "(This is that book I've heard everyone is reading ... Apparently it's very good.)"
        MC @smile "Thank you, Elena."
        MC @talk "When Erika leaves, we'll talk properly."
        ELENA "BARK!"
        hide elena_w_book with dissolve
        "Elena moved to curl up in a ball and waited patiently for Erika to leave."
        $ PlayerAddItem("elena_gift_book")

    if CharIsLover("myu"):
        "A letter with extremely poor writing was resting on top of a small jar of what seemed like ... slime?"
        "{i}MYU WISH HAPHY DAY, PHLES USE WHEN MYU NO HERE- LOVE MYU{/i}"
        "Looking towards the small jar, as I picked it up in my hand immediately, the slime inside reacted slightly, and seemed to be pouring out of the glass towards me."
        "Realizing it {i}was{/i} a part of Myu, I could sense arousal radiating from the jar."
        MC "(I think she wants me to... let it out when I'm turned on perhaps?)"
        $ PlayerAddItem("myu_gift_jar")

    REGINA "[player_name!t]! Come take a seat!"
    MC @talk "Coming now!"
    scene black with dissolve
    jump ev_KrishanaDay_dinner

label ev_KrishanaDay_dinner:
    scene black with dissolve
    $ TimeAdvTo(TIME_DUSK)
    "For the rest of the evening, I sat down with [regina_ref!t] and Erika to enjoy the hot feast prepared, chatting and laughing together as the world outside didn't seem to matter."
    "For just a few hours, we were together, we were happy, and the war and all of its horrors seemed so very far away."
    "I think I know that these days can't last forever, some terrible darkness I can feel draws ever closer, and the endless battles and wars still rage on outside."
    "I somehow know, I will end up caught in the crosswinds of it's blaze."
    "I knew, there were more battles to come."
    $ TimeAdvTo(TIME_DAY_END)
    "...But what the hell's the point of spending your life fighting if you just end up alone in the end?"
    $ InfGainDaily(True)
    $ LocEnter()