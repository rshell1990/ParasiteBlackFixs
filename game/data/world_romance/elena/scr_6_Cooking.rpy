
# Scene 5 - MC living room - Scene only happens if Regina knows about Elena and only if player is in relationship with Elena - Elena is talking to Regina 
label rom_Elena_CookingIntro:
    show cg_regina_cooking_back at cleft
    show elena at center_f
    with dissolve

    'Upon entering the living room, to my surprise, [regina_ref_cap!t] seemed to be offering Elena ... cooking lessons?'
    ELENA @shock "So ... Is this right?"
    REGINA @talk "Did you add the spices like I asked?"
    ELENA @talk "Y-Yes ..."
    "[regina_ref_cap!t] took a spoonful of the broth."
    REGINA @talk "Hmmm ... It still needs a little more."
    ELENA @sad "{i}*Sigh*{/i}"
    show mc at right_f with easeinright
    MC @talk "Am I interrupting something?"
    show elena shock at shake
    $ Pause(0.3)
    show elena shock at center
    hide cg_regina_cooking_back
    show regina smile at cleft
    with dissolve
    ELENA @shock "[player_name!t]!"
    REGINA @smile_talk "Ahh, just teaching Elena here a few things about cooking."
    MC @surprised "You don't know how to cook?"
    show elena
    ELENA @sad "I ... I've never really needed to."
    ELENA @talk "The servants used to just cook for me when I was younger, and now, I can just survive on raw meat so ..."
    MC @talk "Hm? Then why the sudden urge to start learning now?"
    ELENA @lewd "N-No reason ..."
    REGINA @smile_talk "Anyway, dear, isn't there something you should be doing right now?"
    show regina
    REGINA @talk "I don't want you to distract Elena here too much from her lessons."
    MC @smile "Ah, don't mind me, I'll be on my way then."
    REGINA @talk "Thank you, dear."
    MC "(Maybe I should check in on Elena's cooking some other time?)"

    $ QstSetProgress(RomanceElena, 9)
    $ QstSetDelay(RomanceElena, 7)
    scene black with dissolve
    $ LocEnter()

#Scene 6 - MC living room - scene happens AFTER scene 5 the player is greeted by Elena just in a apron - Camera pan from bottom to top? - Make it occur a week after the events of scene 5
label rom_Elena_Cooking:
    $ AutoMus(False)
    $ PlayMusic("audio/music/33_Elena.ogg")
    $ tmpvar = {}
    $ tmpvar["elena_cooking_clothes"] = CharGetClothes("elena")
    $ CharSetClothes("elena", "apron")
    show elena at cleft
    with dissolve
    show mc at cright_f with easeinright
    'Upon entering into the living room, I froze at the sight before me.'

    $ HideUI(True)
    scene expression Composite((1920,1080), (0,0), "bg_mc_house_kitchen", (301,0), Transform("elena", xzoom=-1.0)) with Dissolve(0.2):
        crop (307, 42, 660, 1040)
        zoom 2.91
        yalign 1.0
        pause 0.5
        linear 5.0 yalign 0.05
    $ Pause()
    $ LocFlush()
    show elena at cleft
    show mc at cright_f
    with dissolve
    $ HideUI(False)

    ELENA @lewd "H-Hello."
    MC @surprised "Elena?!"
    ELENA @lewd "I've made you some food."
    ELENA @lewd "C-Come take a seat."
    'Elena motioned towards the table which was already laid out for me.'
    "My eyes wandered over Elena's body, covering only the front by the white apron she wore."
    "As she turned around to fetch the bowl, my eyes stared at her cute ass hurrying around the kitchen, as she nervously returned to place the bowl in front of me."
    show elena lewd
    ELENA @lewd "L-Let me know what you think!"
    "Elena waited patiently for me to try her food, her hands clasped together nervously as her tail lightly swayed."
    "Her cheeks were bright red as she stared intently for my reaction."
    "Gently, I tasted some of her food."
    MC @serious "Elena ..."
    ELENA @shock "Y-Yes?"
    show elena smile
    MC @smile "... It's great!"
    ELENA @smile "YESSSS!!"
    ELENA @smile "Gods, you have no idea how much I've been practising this!"
    MC @smile "Does it really matter to you that much I enjoy your cooking?"
    ELENA @shock "Of course it does."
    show elena lewd
    ELENA @lewd "T-That's why I've been learning."
    ELENA @grumpy "If ... If there's meant to be some kind of real future for us, I need to think about more than just us fighting together, right?"
    MC @smile2 "And what kind of future {i}are{/i} you planning for us?"
    ELENA @lewd "Y-You know ... {i}a nice one.{/i}"
    "Elena squirmed on the spot, it was cute watching her try and deal with her more feminine side."
    MC @lewd "And uhh ... {i}The outfit?{/i}"
    ELENA @lewd "Ah! She said I should {i}just{/i} wear this."
    ELENA @lewd "I have to admit, the whole thing felt a little ridiculous to me, but she assured me that common wives do this sort of thing all the time to cheer up their husbands."
    MC @talk "... {i}Did she now.{/i}"
    ELENA @shock "D-Do you not like it?"
    MC @smile "Of course I like it, just -"
    MC @lewd "Never mind, you look beautiful."
    ELENA @lewd "T-Thank you."
    ELENA @lewd "There was {i}one{/i} more thing she said women do to cheer up their lovers as well."
    MC @talk "Oh? And what's-"
    #Cut to black
    scene black with dissolve
    "Before I could finish my sentence, Elena was on the floor and crawled her way between my legs and began to wrestle the clothes off me."
    MC "Elena!"
    #Cut to under table Titjob Elena
    $ HideUI(True)
    $ PlayMusicRandom("mus_sex")
    hide elena
    hide mc
    scene elena_cooking_1 with dissolve
    'Between my legs, Elena wrapped her tits shyly around my cock and pressed them together.'
    'Moving them up and down, her face flushed red from embarrassment.'
    ELENA "H-How's this?"
    ELENA "Does it feel nice?"
    MC "Ahh! Elena ...!"
    "Caught off guard, Elena's warm breasts squeezed my thick member with ease."
    ELENA "Hey! Your food will go cold!"
    ELENA "J-Just let me carry on down here, okay?"
    "Did Elena really think this was some normal daily occurrence between lovers? Or was she just playing along for my sake?"
    "Grabbing the spoon, I did my best to try and focus on the food like she asked, but it was impossible to focus on it with what was going on beneath the table."
    "Every time I ate the food though, Elena with her elated smile would move faster, pressing her breasts together tighter as she worked my cock teasingly."
    ELENA "I'm doing a good job, huh? {image=[ICON.HEART]}"
    "I simply grunted in response, my cock began to tighten as the hot pressure mounted."
    MC "{i}*Huff*{/i} E-Elena ... Mmff ..."
    ELENA "{i} ... Tell me I'm a good girl?{/i}"
    MC "Ahh ...! What?"
    ELENA "{i}Tell me I'm a good girl who'll get lots of head-pats for this!{/i}"
    MC "Ahh! You're the best girl, Elena! The bestest girl!"
    ELENA "{i}*Heavy breathing*{/i} {image=[ICON.HEART]}"
    ELENA "T-That's right, {i}I am a good girl!{/i}"
    ELENA "And g-good girls get all the affection!!"
    scene elena_cooking_2 with dissolve
    "Elena seemed almost possessed, huffing and panting as she furiously milked my cock."
    MC "A-Ahh! T-That's it! Elena!"
    MC "I'm close ...!"
    ELENA "D-Do I make a good s-slut too for you?"
    MC "(Just what has [regina_ref_cap!t] been teaching her?!)"
    MC "Y-Yes! You're a good slut for me Elena!"
    ELENA "Ahhh! It's so shameful hearing you talk about me like that ..."
    ELENA "Do it more! Give your head-pat slut all of your cum!"
    ELENA "I want all of it to cover me like a good slut!"
    MC "(Oh fuck! I can't hold it anymore!)"
    MC "HRGHHH! E-ELENA YOU SLUT!" 
    "Unable to hold back any longer, Elena gasped as felt the first stream of hot cum splash onto her tits and face." #Cum
    scene elena_cooking_finish_1 with flash
    $ ReduceInfectionFromSex("elena")
    ELENA "Ooh!"
    "As another stream of my cum splashed onto her, and then another ... and another, Elena giggled and laughed, half in arousal, half embarrassment."
    ELENA "Does it ever stop?"
    MC "{i}*Huff*{/i} Around you? {i}*Huff*{/i} Never."
    ELENA "Fufu ... {image=[ICON.HEART]}"
    #Fade to black 
    $ PlayMusic("audio/music/33_Elena.ogg")
    scene black with dissolve
    '... After that, Elena rose to her feet and began to try and wipe the cum out of her fur, returning to her usual self.'
    $ LocFlush()
    $ HideUI(False)
    #back to showing characters etc 
    show mc at cleft
    show elena grumpy at cright_f
    with dissolve

    $ UnlockGalSceneAndGrantXp("elena","cooking")

    ELENA @grumpy "AHHH! It's all in my fur!"
    MC @think "You weren't complaining a moment ago."
    ELENA @grumpy "Yes, but now I have to actually deal with the consequences of my actions!"
    "Elena after her grumbles became shy once more."
    show elena sad
    ELENA @sad "So ... You did enjoy that, right?"
    ELENA @sad "You didn't just say all that stuff to make me happy?"
    ELENA @angry "And don't think for a moment I'll tolerate you calling me a slut!"
    show elena grumpy
    ELENA @grumpy "T-That was just pillow talk I've been practising."
    MC @smile "Haha, of course you made me happy."
    MC @smile "If only I could have all my food like that!"
    ELENA @lewd "W-Well ... We'll see."
    ELENA "({i}I can't believe her advice worked so well ... I thought it strange at first she was so open discussing these things but-{/i})"
    ELENA "(No, I shouldn't dwell on it too much!)"
    ELENA @smile "A-Anyway then, I'm going to clean myself up."
    show smile
    ELENA @smile "Be back shortly."
    show elena smile at cright
    hide elena smile with easeoutright
    #Elena walks off-screen
    MC "(Hm ... I wonder what was all that stuff about me calling her a 'good girl' and giving her head-pats?)"
    MC "(Is that some tide over from her canine side that she's ... fetishized?)"
    MC "{i}(I think I could definitely have some some fun with that.){/i}"

    $ QstSetProgress(RomanceElena, 10)
    $ CharSetClothes("elena", tmpvar.pop("elena_cooking_clothes"))
    $ AutoMus(True)
    scene black with dissolve
    $ LocEnter()
