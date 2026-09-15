define MALAKAI = Character("???")

label malakai_intro: 
#Malakai armor DLC
#IMPLEMENTATION: One-time scene. Available after completing 'Two Emperors'. Auto-triggers when entering the player's bedroom.
    $ PrimerMalakai().finish() # burn the one-shot primer only once the intro actually plays
    show mc at center with easeinleft
    "Entering my room, my eyes were drawn immediately to the strange, black envelope placed carefully on my bed."
    "The envelope was expensive, scented with lavender, with a red seal on the back marked M.B. I carefully opened it to read the letter inside."
    "{i}You are cordially invited to the Cathedral of Dreams... in your dreams. This invitation cannot be refused.{/i}"
    "I stared at the letter for the longest time, turning the page around to see if something was written on the back. There wasn't."
    MC "(... Is this a joke?)"
    show regina at right_f with easeinright
    REGINA @talk "What do you have there?"
    MC @think "Did you put this here?"
    hide regina
    show regina at cright_f
    "Stepping forward, she took the letter carefully from my hand, but recoiled at the touch."
    hide regina
    show regina at right_f
    REGINA @angry "... Where did you get that?"
    MC @think "What? It was just on my bed."
    REGINA @shock "Your bed?"
    REGINA @angry "Burn it."
    MC @shock "What, why?"
    REGINA @sad "I... Never mind."
    REGINA @sad "It just makes me uneasy, is all."
    "[regina_ref] offered the faintest, uneasy smile."
    REGINA @talk "I just don't like knowing how it got there, is all."
    "Her eyes continued to stare at the letter still in my hand."
    "She reached out suddenly, snapping it from my hands."
    hide regina
    show regina at cright_f
    MC @angry "[regina_ref]!"
    REGINA @smile "Not to worry! I'll just take care of that!"
    hide regina
    show regina at right
    "She hurried away to her room, slamming and bolting the door behind her."
    hide regina
    MC "(... What in the world?)"
    $ QstStart(QstMalakai)
    $ QstSetProgress(QstMalakai, 0)
    $ LocEnter()
####
#New quest appears: Sweet dreams...
#Quest detail: Go to sleep: Quest descrip: A mysterious letter was found on my bed saying someone would contact me in my dreams... Surely this is a joke? - XP reward: 250
#IMPLEMENTATION: Start 'Sweet dreams...' here. Sleeping while this quest stage is active triggers the following scene.
label malakai:
    "As I lay down on my bed and closed my eyes... I began to feel myself sink into it."
    show bg_black with dissolve
    "The world slowly became black around me, and suddenly, there was an eerie silence... As though the world outside simply ceased to be."
    "The bed was gone. I found myself standing in a starless realm of darkness, where red lightning boomed and cracked across the sky."
    "Ahead... A great temple."
    show bg_gates with fade
    "Looking down, I was suddenly wearing... my armor?"
    show mc at left
    "My blade was at my side."
    MC @shock "... How-"
    #The voice is marked as ??? - The voice is Malakai
    MALAKAI "Come."
    MALAKAI "COMECOMECOME..."
    show bg_church with fade
    "The great gates opened as I stepped towards them, revealing a grand cathedral beyond as the ghostly voice boomed."
    "Overlapping voices, distorted, some fighting with each other as though they were echoes that refused to agree with themselves."
    MALAKAI "PROPHET."
    MALAKAI "WAYWARD SON."
    MALAKAI "KEY."
    MALAKAI "MINE, NOT HIS."
    MALAKAI "DEVOUR THE GODS."
    MALAKAI "TRAITOR, TRAITOR, TRAITOR."
    MALAKAI "EMPIRES... CHAINS..."
    MALAKAI "GODS NOT TO RULE, THE CYCLE BROKEN."
    "A voice violently snapped back, causing the cathedral-like windows to shatter."
    MALAKAI "LIAR... THE CHAIN IS IN YOUR HAND!"
    "The voice drew in a breath, and the whole cathedral seemed to bend and breathe in with it as all the voices spoke as one."
    MALAKAI "FREEEEEEDOM."
    MALAKAI "CHAINS UPON GODS. CHAINS UPON MEN."
    MALAKAI "I SHALL BREAK THEM ALL."
    "A chill ran down my spine as I reached for my blade in the dream, still looking for whoever might answer."
    MC @shock "WHO IS THERE?"
    MC @angry "ANSWER ME!"
    "The voice laughed, answering all at once in a dozen conflicting voices."
    MALAKAI "PROVE,PROVE,PROVE."
    MALAKAI "MINE, MINE, MINE."
    "The ground seemed to coalesce with black smoke, warping and twisting into the shape of some colossal beast."
    show colossalbeast with dissolve
    MALAKAI "NO TEETH. NO CLAW."
    MALAKAI "FREEDOM DEMANDS STRENGTH."
    MALAKAI "PROVE."
    "Its eyes were covered in a thick bandage, with an enormous blade in its hands as it snarled towards me!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_black", CharIDList_Left = ["mc"], CharIDList_Right = ["colossalbeast"], CanTransform = False))
    if LastBattleOutcome != "victory":
        $ LocSet("mc_house_bedroom")
        $ LocEnter()
        return
    "With a desperate swing of my blade, the smoke beast vanished beneath it with a howl."
    hide colossalbeast
    MC @shock "{i}*Huff* *Huff*{/i}"
    MC @shock "SHOW YOURSELF!"
    hide mc
    "The voice doesn't answer; the very cathedral itself falls deathly silent."
    "The walls begin to buckle, and all at once, the floor opens up beneath my feet as I fall... and fall... and fall."
    show bg_bedroom with fade
    #The player wakes up
    MC @shock "...!"
    "Sweat poured from me as I looked down towards my trembling hands."
    "Was that really just a dream? It had felt so-"
    "There, in front of my bed, now sat a black chest that was not there before."
    show treasurechest at center
    "It looked... wrong... Like it had forced its way into a place where it didn't belong."
    "Just looking at it made me feel uneasy."
    "I stared at it for the longest time... and carefully moved forward to open it."
    "Inside, carefully laid on a velvet interior... Armor... and a sword."
    MC @shock "I... This can't be real."
    "Inside, a small letter was carefully folded."
    "{i}He has felt you now. Not seen you. Not yet. When he reaches for you, remember what you learned tonight. - M.B{/i}"
    $ PlayerAddItem("void_armor")
    $ PlayerAddItem("shadowreach")
    $ QstComplete(QstMalakai)
    $ LocSet("mc_house_bedroom")
    $ LocEnter()
