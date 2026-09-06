label ev_blackDiamondFawhaOnReturn:
    $ QstSetProgress(BlackDiamondLogic, 1)
    show fawha with dissolve:
        xcenter 0.3
    #If Fawha met the player
    if QstDamzelInDiztrezz().fawhaName == True:
        $ FAWHA = Character(_("Fawha"), image = "fawha")
        FAWHA '{i}*Gasp!*{/i}'
        FAWHA @smile "It's you!"
        MC @talk 'Fawha?'
        MC @talk "What's happened here?"
    #If Fawha has not met the player
    else:
        $ FAWHA = Character(_("Serving Girl"), image = "fawha")
        FAWHA @talk 'Why hello sir, you may call me Fawha.'
        $ FAWHA = Character(_("Fawha"), image = "fawha")
        $ QstDamzelInDiztrezz().fawhaName = True
        FAWHA @talk 'What pleasure do you seek tonight, sir?'
        MC @talk 'This place has changed since I was last here...'
        FAWHA @talk 'A-Ah... Yes, a lot has no doubt changed these past few days.'
        MC @talk 'Can you talk about it?'
        FAWHA @talk "It's not exactly much of a secret anymore what's been going on sir..."
    #If Tarek died in a assault or was assassinated 
    if BlackDiamondLogic().tarekFate == "died":
        FAWHA @talk "After Tarek was killed, the rival factions have been tearing each other apart to grab what they can of Tarek's old territory."
        FAWHA @talk 'The Khazhah have managed to push out the rival factions and take over management here.'
        MC @talk 'Are you treated well?'
        FAWHA @talk "Khazah's treat us well enough I suppose, but they're flooding the place with more raza than the Vulshan's ever did."
        FAWHA @sad "Things are becoming more violent than ever now... I fear things will only get worse before they get better."
    #If Tarek died due to Vulshan revolt
    if BlackDiamondLogic().tarekFate == "diedVulshan":
        FAWHA @talk "Since Tarek's death, the Vulshan have re-organised themselves and begun aggressively pushing back against Khazahs."
        FAWHA @talk 'Without Tarek holding everyone together, the usual in-fighting has returned.'
        FAWHA @talk "More and more factions are choosing sides, and I don't think it will be long before things become all out war."
        MC '(Hmm, I should maybe keep one eye on this situation.)'
        MC @talk 'How are the Vulshan treating you without Tarek?'
        FAWHA @smile 'Better than ever actually.'
        FAWHA @talk "Thanks to you and your friend, they've told us we are 'marked' girls."
        FAWHA @talk "We've been told to offer our services to you both for free."
        MC @smile 'Really?'
        FAWHA @talk 'You have found a friend in the Vulshan, they also wanted me to let you know they have prepared a private room for you to stay in... Should you wish.'
        MC '(A private room? This could prove useful if I ever need to stay low.)'
        MC "(But, do I really trust my safety in the hands of people like the Vulshan?)" 
        #Fawha and Alea services now free
        $ BlackDiamondLogic().freeRide = True
    #If Tarek walked away 
    if BlackDiamondLogic().tarekFate == "walked":
        FAWHA @talk "Things have been tense, but we're not at the point of all-out-war yet."
        FAWHA @talk 'Before he left, Tarek summoned a meeting of the leading gangs and announced he would be leaving.'
        FAWHA @talk 'He outlined how the territory under him was to be managed or divided, leaving this place to the Vulshan.'
        FAWHA @talk "It's the best outcome perhaps, but... The tension is still boiling beneath the surface, and I feel like it has only bought time before the inevitable."
    #All routes continued
    FAWHA @talk "I'll be around here for a while if you need anything, just ask."
    $ LocEnter()