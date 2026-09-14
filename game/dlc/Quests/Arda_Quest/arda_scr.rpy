define ARDA = Character("???")
define VOIDSPIRIT = Character("Void Spirit")
label arda_intro:
    play sound "audio/cfx/church_bells.ogg"
    MC @think "... Do you hear that?"
    MARKUS @think "Hear what?"
    MC @talk "Those strange bells... I've never heard them before..."
    MARKUS @think "Bells?"
    MARKUS @smile "Perhaps you're finally losing it, friend."
    "I felt the softest whisper in my ear, an invisible hand resting reassuringly on my shoulder."
    ARDA "{i}Come... follow my voice...{/i}"
    ARDA "{i}To the garden.{/i}"
    "I suddenly felt the strangest urge... to head to a church?"
    $ QstStart(QstArda)
    $ QstSetProgress(QstArda, 0)
    $ LocEnter()

label arda_church:
    show mc at cleft with easeinleft
    show markus at left with easeinleft
    "... Entering into the halls of the church, once again, I heard the ringing of the bells."
    MC @shock "There it is again!"
    MC @shock "Markus, can't you hear-"
    hide mc
    show mc at cleft_f
    "As I turned to look towards him, he was gone."
    hide markus with dissolve
    MC @think "... Markus?"
    "As I looked around, I saw that everyone had vanished."
    hide mc
    show mc at left with easeinleft
    MC @shock "... H-Hello?"
    "Silence."
    "And as I looked towards the windows and the door, only bright, white light was visible outside."
    "It was as if the whole church had simply ceased to be where it was before... And was now somewhere else."
    show arda at right_f with easeinright
    ARDA "Come... Follow my voice."
    "The doors to the church opened once more to reveal a bright light, and with little other choice... I stepped through them."
    "Stepping through, I found myself in the most beautiful of gardens..."
    show bg_palam_garden with dissolve
    "And there, a great tree, its body seemingly made of space and twinkling with stars, called out once more like the gentlest whisper."
    ARDA "I called... And you answered."
    MC @think "... Who are you?"
    ARDA "A friend."
    ARDA "A voice."
    ARDA "A dream."
    "The whole garden seemed to move as one, its trees swaying in unison, and with it, the pleasant aroma of a warm summer's dew."
    ARDA "He would make of you a weapon."
    ARDA "He would make of you a tool."
    ARDA "You are not a tool, you are not a weapon..."
    ARDA "A flickering ember in the dark is no less beautiful because its light does not burn forever."
    MC "I don't... I don't understand."
    MC "Who would make me a weapon? Who would-"
    ARDA "Duty. Honor. Courage."
    ARDA "... Love."
    "The tree glows brighter for a moment, as though a thousand thoughts and voices rush at once."
    ARDA "I never wanted war I wanted to save them all."
    ARDA "I HAD TO LEAD THEM IT WAS THE ONLY WAY."
    "The tree suddenly dims once more."
    ARDA "... I am sorry."
    ARDA "My mind... like glass shards pulled together in my hands."
    ARDA "I... I need to give you something... something to-"
    ARDA "TRIED TRIED TRIED."
    ARDA "HOW MANY EMPIRES MUST I BUILD?"
    ARDA "WHY WHY WHY CAN'T I SAVE THEM?"
    "The voices begin to fight among themselves as the garden turns into a great forest, trees sprouting up and bending towards the great tree."
    ARDA "RULE THEM FOREVER."
    ARDA "LOVE THEM FOREVER."
    ARDA "NEVER LET THEM MAKE MISTAKES AGAIN."
    "The tree recoils from itself."
    ARDA "NO."
    ARDA "LET THEM GO."
    "The tree shuddered violently, twisting itself."
    ARDA "I CAN'T."
    "Something begins to tear through, as though reality itself were paper."
    "The voices once again begin to fight, one stern, one gentle, one afraid, and so on and so on."
    ARDA "NONONONONO."
    ARDA "PROVE HIMSELF."
    ARDA "DON'T HARM HIM!"
    ARDA "BREAK HIM AND REBUILD HIM SO HE CAN STAND BEFORE THE SHADOW!"
    ARDA "HE DOESN'T NEED TO PROVE ANYTHING."
    ARDA "EVERYONE MUST."
    hide arda with easeoutright
    show voidspirit with dissolve
    "As the voices argue with themselves, a being, white and strange, comes through the tear."
    "Ghostly white, celestial, the figure smiles, drawing a terrible scythe from out of its chest."
    "I reached for my sword almost instinctively as the figure smiled warmly, but something was wrong behind its eyes."
    "It bowed, almost politely, though its eyes never left mine."
    "Suddenly, it lunged forward to strike!"
    hide voidspirit
    hide mc
    $ StartBattle(BattleData(BackgroundImage = "bg_palam_garden", CharIDList_Left = ["mc"], CharIDList_Right = ["void_spirit"], CanTransform = False))
    if LastBattleOutcome != "victory":
        $ QstSetDelay(QstArda, 1)
        $ LocSet("novaras_church")
        $ LocEnter()
        return
    hide bg_palam_garden with dissolve
    show bg_church
    show mc at left
    show arda at right_f with easeinright 
    ARDA "I... I didn't mean for it to hurt you."
    ARDA "I DID."
    ARDA "I DIDN'T."
    ARDA "I can't hold myself together."
    ARDA "Go... Gift... Take it when you return..."
    ARDA "Go... Go now..."
    hide arda
    "A bright white light surrounded me, and once more... I was standing in the cathedral as though nothing had happened."
    show bg_church with fade
    show markus at right_f
    MARKUS @think "Are you alright?"
    MC @shock "What?"
    MARKUS @think "You just stared blankly ahead for a full minute."
    MC @talk "I... What?"
    MARKUS @talk "Are you suffering from a fever or something?"
    MC @sad "I... I'm fine... Let's keep moving."
    $ GoalComplete(QstArda, 0)
    $ LocSet("novaras_dist_house_south")
    $ LocEnter()
    
label arda_finish:
    show treasurechest at center
    "There, sitting awkwardly in the middle of my room, was a huge, ornate, white box."
    "{i}...Not mine.{/i}"
    "Warm beneath my fingers, with the faintest smell of rain on a summer day... Yet there wasn't a trace of moisture on it."
    "As I nervously stepped towards it, the latch opened with ease."
    "Inside, carefully arranged, were the most beautiful armor and blade I had ever seen."
    "Simply looking at them, they radiated a sense of warmth..."
    "Holding the blade in my hand, I could feel the surge of magecraft beneath my grip, a brief tingling sensation that even I, with no affinity for the craft, could sense."
    "Was it crafted by the new gods?"
    "I wasn't sure..."
    "But I knew one thing."
    "{i}It was mine now.{/i}"
    hide treasurechest
    $ PlayerAddItem("champion_armor")
    $ PlayerAddItem("star_bringer")
    $ QstComplete(QstArda)
    $ LocSet("mc_house_bedroom")
    $ LocEnter()