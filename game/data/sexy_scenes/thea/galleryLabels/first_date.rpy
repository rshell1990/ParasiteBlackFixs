label gallery_thea_firstdate:
    $ tmpvar["gallery_mc_clothes"] = CharGetClothes("mc")
    $ tmpvar["gallery_mc_default_look"] = CharGetVar("mc", "default_look")
    $ tmpvar["gallery_thea_clothes"] = CharGetClothes("thea")

    $ CharSetClothes("mc", "normal")
    $ CharSetVar("mc", "default_look", "father_armor")
    $ CharSetClothes("thea", "normal")

    $ PlayMusic("audio/music/7_novaras_d.ogg")
    play ambience "audio/ambience_scenes/campfire.ogg" fadein 2.0
    scene bg_thea_room
    show thea at cright_f
    show mc smile at cleft
    with dissolve
    'Into her bedroom, Thea led me, quickly getting the fire going before she twirled around and smiled alluringly.'
    MC @smile "So then, what was it you wanted to give me?" #From here - the repeatable sections of this scene begin
    THEA @talk "Do you mind waiting here for a moment, this will only take a few minutes."
    MC @smile "Of course."
    hide thea with dissolve
    'Thea hurried off for a few moments, and after briefly looking around her room, the door swung open, and Thea re-emerged.'
    #Show Thea dressing gown
    $ CharSetClothes("thea", "gown")
    show thea blush at cright_f with dissolve
    THEA @blush "{i}... Do you think 'this' will help motivate you?{/i}"
    MC @lewd "I'm feeling motivated already."
    #Fade to black
    scene black with dissolve
    'Giggling to herself, Thea stepped forward and pushed me down onto her bed, moving swiftly to strip the clothes off of me.'
    THEA "I've been working on a little ... {i}dance{/i} that I want to show you."
    THEA "Tell me ... What do you think of what I'm wearing?"

    # case 1, all three
    if GalFlag("thea", "firstdate", ["var_gown", "var_ling", "var_naked"]):
        menu:
            "I like it. Keep it on.": #triggers robe and lingerie dance animations
                $ CharSetClothes("thea", "gown")

            "I prefer what's underneath.": #triggers lingerie only dance animations
                $ CharSetClothes("thea", "ling")

            "Take it all off ... It's in the way of what I really want.": #Triggers nude dance animations
                $ CharSetClothes("thea", "naked")
            
    # case 2 variants (only 2 unlocked)
    elif GalFlag("thea", "firstdate", ["var_gown", "var_ling"]):
        menu:
            "I like it. Keep it on.": #triggers robe and lingerie dance animations
                $ CharSetClothes("thea", "gown")
            "I prefer what's underneath.": #triggers lingerie only dance animations
                $ CharSetClothes("thea", "ling")
    elif GalFlag("thea", "firstdate", ["var_gown", "var_naked"]):
        menu:
            "I like it. Keep it on.": #triggers robe and lingerie dance animations
                $ CharSetClothes("thea", "gown")
            "Take it all off ... It's in the way of what I really want.": #Triggers nude dance animations
                $ CharSetClothes("thea", "naked")
    elif GalFlag("thea", "firstdate", ["var_ling", "var_naked"]):
        menu:
            "I prefer what's underneath.": #triggers lingerie only dance animations
                $ CharSetClothes("thea", "ling")
            "Take it all off ... It's in the way of what I really want.": #Triggers nude dance animations
                $ CharSetClothes("thea", "naked")

    # case 3 (only 1 of three options unlocked)
    elif GalFlag("thea","firstdate","var_gown"):
        $ CharSetClothes("thea", "gown")

    elif GalFlag("thea","firstdate","var_ling"):
        $ CharSetClothes("thea", "ling")

    elif GalFlag("thea","firstdate","var_naked"):
        $ CharSetClothes("thea", "naked")

    THEA "Just keep still ... {i}You're going to enjoy this.{/i}"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    #All choices continued - First dance animation - front
    if CharGetClothes("thea") ==  "gown":
        scene ss_thea_firstdate_gown_1 with dissolve
    elif CharGetClothes("thea") == "ling":
        scene ss_thea_firstdate_ling_1 with dissolve
    elif CharGetClothes("thea") == "naked":
        scene ss_thea_firstdate_naked_1 with dissolve
    
    $ Pause()
    'As Thea danced sensuously in front of me, the light from the fireplace flickered.'
    'Her hips swayed gently from side to side as her sultry eyes refused to leave me alone.'
    THEA "I've been thinking about this since the moment I first saw you."
    THEA "There's just something so ... {i}different{/i} about you."
    "The flickering flames shifted behind her as she run her hands up her body, cupping and squeezing at her breasts."
    "The room quickly became hot, and the trickle of sweat running down her black skin was illuminated by the flame's glow."
    "My eyes greedily run down her body, moving down from her tits to staring hungrily between her thighs."
    MC "Thea ..."
    MC "You look so-"
    THEA "Shhh, don't talk."
    THEA "{i}Just watch.{/i}"
    if CharGetClothes("thea") == "gown":
        scene ss_thea_firstdate_gown_2 with dissolve
    elif CharGetClothes("thea") == "ling":
        scene ss_thea_firstdate_ling_2 with dissolve
    elif CharGetClothes("thea") == "naked":
        scene ss_thea_firstdate_naked_2 with dissolve
    $ Pause()
    'Thea turned around with a sultry smile.' #Cut to second animation - back 
    'She sensually sway her hips enticingly as she looked over her shoulder at me.'
    "My eyes were unable to look away from her round, tight looking ass as Thea run her hands over her body once again."
    THEA "See something you like?"
    MC "Your ass looks incredible."
    'Thea laughed as she lightly shook her butt in front of me.'
    THEA "Haha ... I can feel the eyes watching me as I walk past."
    "As my cock hardened in front of her hot body, Thea's eyes looked down towards the standing appendage and she grinned."
    THEA "Seems I'm not the only one {i}blessed{/i} with assets."
    MC "Oh, so {i}you{/i} like what you see too, I take it?"
    THEA "Fufu~"
    #Fade to black 
    THEA "Alright, enough teasing."
    THEA "Time for the {i}real{/i} reward. {image=[ICON.HEART]}"
    if CharGetClothes("thea") == "gown":
        scene ss_thea_firstdate_gown_3 with dissolve
    elif CharGetClothes("thea") == "ling":
        scene ss_thea_firstdate_ling_3 with dissolve
    elif CharGetClothes("thea") == "naked":
        scene ss_thea_firstdate_naked_3 with dissolve
    $ Pause()
    #Cut to titjob animation (changes depending on level of clothes she wearing)
    'With her tits wrapped around my cock, Thea began to stroke my cock wedged between her breasts.'
    'Hot breath touched my member as she moved rhythmically up and down, biting down on her lower lip.'
    THEA "Do you like that?"
    THEA "Do you like seeing your huge cock shoved between my tits?"
    MC "Ahh! Thea!"
    MC "Mmfgh...!"
    'I grunted in pleasure as Thea continued to teasingly massage my member, biting down on her lower lip as she giggled to herself.'
    'Occasionally, Thea would spit down onto my cock, using it as a kind of lube to help as she now moved faster.'
    MC "Mmh! Thea!"
    BLACK "({i}She has exceptional talents as a breeding mate{/i})."
    THEA "Tell me how good it feels~"
    MC "Mhhff! You're d-doing a great job! Hrghh!"
    MC "{i}*Huff*{/i} Not sure how much longer I can hold on like this!"
    "Thea laughed softly to herself again, moaning softly to herself as continued for some time, letting the pleasure slowly build."
    THEA "That's it ... Mhhfgh!"
    THEA "I can feel how close you are ..."
    THEA "Come on, do it ... You know you want to!"
    THEA "Cover this fucking wench in your load!"
    THEA "Show me you can do whatever you want!"
    MC "(Hrgh! I'm so close!)"
    MC "T-Thea! I'm ..."
    MC "G-Grghhhh...!"
    if GalFlag("thea", "firstdate", ["var_face", "var_mouth"]):
        menu:
            'Cover Thea':
                $ tmpvar["gallery_finish_face"] = True
            'Make Thea swallow':
                $ tmpvar["gallery_finish_face"] = False

    elif GalFlag("thea","firstdate","var_face"):
        $ tmpvar["gallery_finish_face"] = True

    elif GalFlag("thea","firstdate","var_face"):
        $ tmpvar["gallery_finish_face"] = False

    if tmpvar.pop("gallery_finish_face"):
        if CharGetClothes("thea") == "gown":
            scene ss_thea_firstdate_gown_face 
        elif CharGetClothes("thea") == "ling":
            scene ss_thea_firstdate_ling_face
        elif CharGetClothes("thea") == "naked":
            scene ss_thea_firstdate_naked_face
        with flash
        $ Pause()
        'Unable to hold back any longer, I grunted loudly, tightening my fists into balls as I covered her tits and face in my hot cum.'
        "Thea giggled and laughed, her eyes wide in surprise at the size of the load."
        THEA "Oh...!"
        THEA "You really were pent up, weren't you, big boy? {image=[ICON.HEART]}"
    else:
        "Grabbing the back of Thea's head, I pulled her forward suddenly, forcing her wet lips over the head of my cock."
        THEA "Mmmfghh...?!"
        if CharGetClothes("thea") == "gown":
            scene ss_thea_firstdate_gown_mouth
        elif CharGetClothes("thea") == "ling":
            scene ss_thea_firstdate_ling_mouth
        elif CharGetClothes("thea") == "naked":
            scene ss_thea_firstdate_naked_mouth
        $ Pause()
        "Thea's wide-eyed protests soon stopped as she felt the rush of my warm seed flooding into her mouth."
        "She tried to swallow as much of the load as she could before pulling back to cough up the rest."
        "Some of the excess seed splashed onto her face and dark breasts as she did her best to smile afterwards, eyes slightly watering."
        THEA "That was - {i}*Cough!*{/i} quite the load! {image=[ICON.HEART]}"

    stop music fadeout 3.0

    $ CharSetClothes("mc", "naked")
    scene bg_thea_room
    show thea smile at cright_f
    show mc smile at cleft
    with dissolve
    MC @smile "Ahh ... Sorry, I didn't realize I was so-"
    THEA @smile2 "Haha, it's fine!"
    THEA @smile "I'm just happy you were blessed with such a fine ... {i}sword.{/i}"
    MC @lewd "You're more than welcome to polish it anytime you please."
    THEA @smile2 "Don't mind if I do then, fufu~"
    #cut to black 
    'After that, Thea threw me my clothes, and I began to re-dress myself, playfully remarking she might let me stay the night {i}next time.{/i}'
    hide mc with dissolve
    $ CharSetClothes("mc", "normal")
    show mc lewd at cleft with dissolve
    THEA @smile "I'm excited to hear about your next adventures."
    MC @lewd "Will they also end up with me being dragged back up to your bedroom?"
    THEA @smile2 "Mmmm, I guess you'll have to wait and see, won't you?"
    scene black with dissolve
    'I left a short time later after a quick kiss goodbye...'

    $ CharSetClothes("thea", "normal")

    scene black with dissolve
    $ CharSetClothes("mc", tmpvar.pop("gallery_mc_clothes"))
    $ CharSetClothes("thea", tmpvar.pop("gallery_thea_clothes"))
    $ CharSetVar("mc", "default_look", tmpvar.pop("gallery_mc_default_look"))

    return
