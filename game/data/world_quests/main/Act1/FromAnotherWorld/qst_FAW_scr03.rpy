label qst_FromAnotherWorld_GoToMarkusHouse:
    $ LocSet("markus_house_livingroom")
    'Markus’ house was only slightly smaller than mine but felt much more cramped.'
    "Littered about the place were various strange and extraordinary items his brother had collected over the years that clogged up much of the space, hence why me and Markus spent less time here growing up."
    $ LocFlush()
    show markus at center
    show skallion at right
    with dissolve
    "Entering through a door open ajar, I've realized that I walked into what could be described as a family conversation:"    
    show mc at left with easeinleft
    "It was Skallion, Markus' brother."
    'Having lost both of his parents during the war, Skallion, who used to live alone, was forced to take the young Markus under his wing.'
    'He was taller and more muscular than both of us has been before we joined the Scouts, but now we towered over him.'
    $ CharMeet("skallion")
    SKALLION "What I'm saying is, Markus..."
    show skallion at shake
    SKALLION 'Bah!'
    SKALLION 'Not you too!'
    MARKUS "[player_name!t]!"
    SKALLION 'What have they been feeding the two of you?!'
    MC @talk 'U-Uhhh, plenty of meat?'
    SKALLION 'Some bloody good meat...'
    SKALLION 'Anyway, you two should go to the Adventurers Guild now.'
    SKALLION 'Try not to get into any trouble on your way there.'
    'Skallion nodded briefly in my direction.'
    SKALLION 'It’s good to see you, [player_name!t].'
    SKALLION 'Try and stop Markus from getting too drunk, if that’s even possible.'
    MARKUS 'Urgh, I’m not a child anymore you know.'
    SKALLION 'I know I know...'
    SKALLION 'You’re an OVERGROWN child with a drinking problem.'
    'Markus pulled an unimpressed expression as Skallion snickered to himself.'
    SKALLION 'Oh, and don’t disturb me in my room plase...'
    SKALLION 'I’m working on a little project.'
    MARKUS 'Is this another one of your secret projects?'
    SKALLION '{i}Perhaps.{/i}'
    MARKUS 'Will we ever see one of these secret projects of yours?'
    SKALLION 'When it’s done, of course!'
    MARKUS '...Will it {i}ever{/i} be done?'
    SKALLION 'Such little faith you have, younger brother.'
    SKALLION 'I promise you, when this is done, we’ll be swimming in gold.'
    MARKUS 'For that I cannot wait!'
    hide skallion with easeoutright
    'Skallion smirked to himself as he headed back into his room, closing the door firmly behind him.'
    "Markus nodded and motioned for me to come into his room."
    $ PlaySoundRandom("woodenDoor")
    scene black with dissolve
    $ LocSet("markus_house_bedroom")
    $ LocFlush(dissolve)
    show markus at cright_f with easeinleft
    show mc at cleft with easeinleft
    "The room was smaller than mine, little more than box really with just two shelves and a chest."
    'His room used to be a place Skallion stored things before the young Markus abruptly arrived.'
    show markus at nod
    'Grabbing the small pouch from the shelf, Markus turned to dangle it in front of me.'
    'I heard the rustle of coin inside.'
    MARKUS "Say hello to tonight's entertainment."
    MARKUS "[player_name!t]? You in there?"
    MC @talk "No, nevermind me, I'm just estimating the amount of effort it will take to stop you from drinking this all up."
    MARKUS "Haha! No, I'm not really in the mood for getting {i}too drunk{/i} now..."
    MARKUS "Ever since the... The thing happened."
    "An eerie silence enveloped the room as we involuntarily recalled bits and pieces of the events at the fort."
    "I broke the silence with a probing question:"
    MC @talk "Say Markus, what do you remember about what happened to us?"
    MARKUS "*Sigh* Must we do this now?"
    MARKUS "I’d rather have a pint of ale or two first."
    MC @talk "I just need to know."
    MC @talk "Have you been hearing voices?"
    "Markus paused uncomfortably as his face turned sullen and uneasy."
    MARKUS "... Yes."
    MC @talk "What did the voice say?"
    MARKUS "That it was here to help, that it had saved me."
    MARKUS "I would really rather not think—"
    "Suddenly, Markus’ eyes widened in surprise as he stumbled backwards clumsily, shock etched on his face."
    MC @talk "... Markus?"
    "Turning pale white, Markus collapsed, but his hand reached out to grab onto one of the shelves, dragging everything off from it in one clean sweep as he fell backwards onto his bed."
    MC @talk "Markus!"
    show mc at center with ease
    "Stepping forward to help him, I suddenly felt an intense burning heat within my chest, like my lungs were filling with ash."
    scene black with dissolve
    $ AutoMus(False)
    $ AutoAmb(False)
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    "Something began to swirl and froth inside of me, I could feel it moving under my skin, stretching and splitting me."
    "Frantically, the two of us began to pull off our clothes to see what horror was beneath, we found a hot mass swelling on both of our chests, Markus’ white, mine black."
    scene cg_parasite_meet with dissolve
    $ PlayMusic("audio/music/16_Parasite_A.ogg")
    $ Pause()
    "We looked to each other, frozen in terror."
    "Before we could say anything, they moulded and took form; extending out of our bodies, the two liquids coiled around each other."
    "What appeared to be their heads now became bug-like in appearance with sharp pincers extending out of them as the creatures looked quizzically at each other before gradually retreating."
    "My heart stopped, I thought that at any moment these things that were inhabiting our bodies were going to split through our skin and kill us in some wretched, macabre display of violence."
    "We both looked at each other, half in disbelief, half in terror."
    "Now angled towards us, the things looked us dead in the eye and turned their strange heads inwards in curiosity."
    "Then... {i}they spoke without mouths{/i}."
    BLACK "{i}Hello...{/i}"
    "Me and Markus shared a look of panic as we waited for what came next."
    WHITE "{i}Do not be alarmed.{/i}"
    BLACK "{i}You are our hosts, we wish you no harm.{/i}"
    MC @talk "How... How can we hear you?"
    WHITE "{i}We have formed a link to communicate.{/i}"
    BLACK "{i}We have been learning your language from the archives of your memories.{/i}"
    MARKUS "W-What are you?"
    MARKUS "What are you doing inside of us?"
    WHITE "{i}No choice.{/i}"
    BLACK "{i}No choice.{/i}"
    BLACK "{i}Must find a host or die... We cannot survive without one.{/i}"
    MC @talk "... You were the things that attached to us at the fort."
    WHITE "{i}Yes.{/i}"
    WHITE "{i}We used our reserves of energy to return you to this city.{/i}"
    BLACK "{i}Now we have recovered to an extent and we wish to communicate with you.{/i}"
    MC @talk "Why is one of you white and the other black?"
    WHITE "{i}We are different strains of the same species.{/i}"
    BLACK "{i}We are different in many ways, yet the same in many others.{/i}"
    MARKUS "... W-What do you want from us?"
    BLACK "{i}As we speak... we are travelling up your nervous system to complete the infection of your cerebral cortex.{/i}"
    WHITE "{i}Once this is complete, the host shall be in our control.{/i}"
    MC @talk "You— You’re killing us?!"
    MARKUS "You said you meant us no harm!"
    BLACK "{i}We do not... This function is an autonomic response.{/i}"
    MC @talk "A what now?"
    WHITE "{i}We cannot prevent or stop it any more than you could will your heart to stop.{/i}"
    MC @talk "Then how are you going to help us?"
    BLACK "{i}Our autonomic response occurs when the primary function is not being met.{/i}"
    BLACK "{i}A lack of viable breeding hosts.{/i}"
    MARKUS "What?! What are you talking about?"
    WHITE "{i}The autonomic response can be halted or even regress when this function is met.{/i}"
    BLACK "{i}Breeding triggers a chemical reaction that informs us the needs of the hive are being met.{/i}"
    BLACK "{i}The autonomic response from mating is one that reduces us to a more feral, but incredibly powerful state.{/i}"
    BLACK "{i}It is designed only to aid a dying hive.{/i}"
    MC @talk "Hive? Are you some kind of bug or something?"
    WHITE "{i}We are both a symbiotic and parasitic race.{/i}"
    BLACK "{i}We have no name.{/i}"
    WHITE "{i}We instil upon our hosts enhanced traits, you may have already noticed a drastic increase of muscle tissue in your body.{/i}"
    MARKUS "So... let me get this straight..."
    MARKUS "It’s either fuck or die?"
    BLACK "{i}... This analysis is primitive but correct.{/i}"
    WHITE "{i}The hive must survive.{/i}"
    BLACK "{i}The hive must {b}always{/b} survive.{/i}"
    MARKUS "Well, what if we just try cut you both out?"
    "I gaped at Markus, incredulous at his stupidity, he just shrugged in my direction."
    "In that same moment, both me and Markus felt a sharp pain in our hearts, like something was tightening around them, restricting the space in which they had to beat."
    WHITE "{i}Without a host, we will die.{/i}"
    BLACK "{i}If we die, the hive dies.{/i}"
    WHITE "{i}And the hive must always survive.{/i}"
    BLACK "{i}Attempting to remove us will be treated as an act of aggression.{/i}"
    BLACK "{i}We will defend ourselves.{/i}"
    MARKUS "But then if you kill us! You’ll die!"
    WHITE "{i}This analysis is correct... But if you were to attempt to cut us out we would have nothing to lose, so hopefully this shall suffice to dissuade you from attempting to forcibly remove us.{/i}"
    "The pain in our chests ceased as they loosened their grip."
    MC @talk "Tell me something... {i}*huff*{/i} ... why even tell us? Why not just let the autonomic response take over?"
    BLACK "{i}Sentience will be lost if we enter our feral stage.{/i}"
    WHITE "{i}It is death for us.{/i}"
    BLACK "{i}To enter the feral stage is a last resort for hive survival, it is a sacrifice of the individual.{/i}"
    $ choicemenu = ["a", "b", "c"]
    menu act1scene4menu:
        "What else have you changed in our bodies?" if "a" in choicemenu:
            $ choicemenu.remove("a")
            BLACK "{i}We can release pheromones that aid in the act of attracting mates.{/i}"
            WHITE "{i}You may also transform into our secondary forms for combat or any other purposes you so wish.{/i}"
            MC @talk "We... We can change into what?"
            BLACK "{i}Our secondary forms, they are optimal in the use of the primary functions, should you so require.{/i}"
            MC @talk "How do we change into your... secondary form?"
            BLACK "{i}It is like having another limb... Focus on using it and you will transform.{/i}"
            BLACK "{i}The first time will be painful.{/i}"
            jump act1scene4menu
        "How long do we have before you take over completely?" if "b" in choicemenu:
            $ choicemenu.remove("b")
            BLACK "{i}A week.{/i}"
            MC @talk "A week?! That’s it?"
            BLACK "Mating reverses the feral process... Our species was genetically built to breed and multiply, failure to do so causes... Mutations."
            jump act1scene4menu
        "Where are you from?" if "c" in choicemenu:
            $ choicemenu.remove("c")
            BLACK "{i}We do not remember.{/i}"
            MC @talk "How do you not know?"
            WHITE "{i}Such functions are not deemed necessary for survival... Only the primary function remains.{/i}"
            BLACK "{i}... And what we have assimilated from you.{/i}"
            jump act1scene4menu
        "So... we’re stuck together?" if choicemenu == []:
            pass
    BLACK "{i}Yes...{/i}"
    $ QstStart(InfectionModule)
    $ ShowTutorialPopup("infection_bar", DirectMessage = _("The infection bar on top represents the Black Parasite's infection rate over [player_name!t]'s body and soul.\n\nIntense sexual activity will lower the infection rate.\n\nShould the infection rate ever reach maximum, the parasite will completely take control over [player_name!t], thus ending your journey."))
    WHITE "{i}Work with us. Do not fight us.{/i}"
    BLACK "{i}There are many benefits to a relationship such as this one.{/i}"
    WHITE "{i}Rest is needed now...{/i}"
    BLACK "{i}Yes... More rest.{/i}"
    "The voices fell silent."
    "Ever so slowly, the things retreated back into our chests and, eventually, our breathing calmed and our hearts stopped threatening to shudder to a stop."
    $ LocFlush()
    show mc at cleft
    show markus at cright_f
    with dissolve
    MARKUS "... Hello?"
    MARKUS "HELLO!"
    MARKUS "This... This is madness!"
    MC @talk "... Markus... You heard them."
    $ PlaySoundRandom("woodenDoor")
    "Before Markus could veer off into some screaming rant, the door swung open and Skallion peered in."
    show markus at right_f with easeoutright
    show mc at blurin, center_f with easeoutright
    show skallion at left with easeinleft
    SKALLION "What’s going on in here?"
    SKALLION "What you both wailing about?"
    MC @talk "I— We were just leaving, right, Markus?"
    show mc at blurin, center
    "Markus hesitated, I could see his mind racing as I caught his glance."
    MARKUS "I... Yes, let's go, [player_name!t]."
    show mc at blurin, left_f with easeoutleft
    show skallion at center with easeinleft
    "Skallion took a step into the room and scrutinised us both."
    show mc at blurin, left
    SKALLION "You two look like you’ve seen a bloody ghost!"
    MARKUS "Don't worry, it's nothing."
    MARKUS "Let's go, [player_name!t]."
    hide markus with easeoutleft
    "Before I could reply, Markus stormed out of the house."
    MC @talk "Umm, nice seeing you again, Skallion..."
    MC @talk "I should go."
    show mc at blurin, left_f
    hide mc with easeoutleft
    SKALLION "Hmph."
    stop music fadeout 2.0
    $ AutoMus(True)
    scene black with dissolve
    jump qst_FromAnotherWorld_GoToValleyWithMarkus