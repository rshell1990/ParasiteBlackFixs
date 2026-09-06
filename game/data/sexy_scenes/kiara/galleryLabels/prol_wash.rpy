label gallery_kiara_prol_wash:
    $ tmpvar["stored_mc_clothes"] = CharGetClothes("mc")
    $ tmpvar["stored_kiara_clothes"] = CharGetClothes("kiara")
    $ tmpvar["stored_kiara_look"] = CharGetVar("kiara", "default_look")
    scene kiara_prol_wash with dissolve
    $ Pause(0.5)
    "It had felt like forever since I last got the chance to see a woman naked."
    "The temptation was too much to bear, and, letting my curiosity get the best of me, I peeked around the woman's side to take a look."
    "Kiara was squatted down naked, washing herself with a wet flannel and bucket."
    KIARA "So, are you just going to stand there and watch?"
    MC @scared "K-Kiara!"
    "Realizing I'd been caught, Kiara, grabbing a towel, wrapped it around herself as she marched over towards me, arms folded."
    MC @scared "It... It isn't what it looked like?"
    $ CharSetClothes("kiara", "towel")
    $ CharSetClothes("mc", "normal")
    scene bg_seb_train_area_night
    show mcprologue at cleft
    show kiara at cright_f
    with dissolve
    KIARA @angry "So you {i}weren't{/i} just spying on me then?"
    MC "N-No, I came here to clean the wash rooms, I swear it so!"
    "Kiara's stern expression softened as she laughed."
    KIARA @happy "Haha, relax."
    KIARA "I'm just playing with you."
    "Kiara winked."
    KIARA "You can take a look anytime you want, cutie."
    MC "I - {i}*Cough*{/i}"
    MC @talk "What are you doing here?"
    KIARA "Some guard fell sick, so I got pulled to do some evening patrol duty."
    KIARA "I decided to clean myself up before I went back to my bed."
    MC "I - I see..."
    "Kiara playfully smirked, tracing her finger down my chest."
    KIARA "So... Did you like what you saw then?"
    MC "K-Kiara..."
    KIARA "Don't think I haven't felt your eyes on my ass every time I walk past."
    "Kiara's fingers trailed down my chest towards my belt, which she grabbed a hold of as she pulled me closer."
    KIARA "Hardly fair though, is it?"
    KIARA "You get to go back to sleep now, stroking your cock thinking about my ass and what do I get? Hmm?"
    "Kiara's hands began to gently tug at my clothes to pull them down."
    "Inches away from me, there was something about her, her scent, her sultry eyes, her tight body..."
    "This girl drove me feral with desire."
    KIARA "{i}It's only fair I also get to see...{/i}"
    "Before Kiara could claim her prize, we heard the flap of some cloth."
    GUARD "How long are you going to be girl? HURRY UP!"
    KIARA @angry "In a moment!"
    KIARA @angry "{i}...Fuck.{/i}"
    "Grabbing her clothes up from the floor, Kiara smiled as she re-dressed herself, giving me a brief good second show of her body."
    $ CharSetClothes("kiara", "normal")
    show kiara at nod
    "As she left the washroom, she run her hand down my chest once more as she passed by."
    KIARA "We'll have to even the score next time, hm?"
    MC "S-Sure."
    KIARA "Hahaha, {i}you and I are going to make great friends...{/i}"
    hide kiara with easeoutleft
    GUARD "DON'T MAKE ME COME IN THERE GIRL!"
    KIARA @angry "I'M COMING!"
    scene black with dissolve
    $ CharSetClothes("mc", tmpvar["stored_mc_clothes"])
    $ CharSetClothes("kiara", tmpvar["stored_kiara_clothes"])
    $ CharSetVar("kiara", "default_look", tmpvar["stored_kiara_look"])
    return