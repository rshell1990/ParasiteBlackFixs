label qst_bloodhound_4_atFort:
    'The next hour was a kind of blur as the mages dressed me and helped me stumble by way back towards Fort Sebastian.'
    $ TimeAdvBy(TIME_05H)
    $ LocNameSetTemp(_("Hospital"))
    'Brought into the Medical Ward, the nuns hurried over to treat me alongside the influx of other poor bastards.'
    $ TimeAdvBy(TIME_05H)
    $ HealParty()
    'Here and there I noticed were a few Scouts.'
    'Battered, broken, some had limbs missing.'
    'Laying beside them, I remembered how I hoped never to end up here again.'
    'Yet, here I was.'
    scene bg_medward at blurin(1.0):
        blur 25
    with dissolve
    "Captain Nyx spoke to some of the Nuns."
    scene bg_medward at blurin(1.0):
        blur 5
    with dissolve
    "As I struggled to stay awake, I couldn't focus on what was being said..."
    scene bg_medward at blurin(1.0):
        blur 35
    with dissolve
    'At some point, one of the nuns came to see me and fed me some holly sap for the pain.'
    scene bg_medward at blurin(1.0):
        blur 3
    with dissolve
    "Since my {i}change{/i}, I hadn't experienced pain like this."
    scene bg_medward at blurin(1.0):
        blur 15
    with dissolve
    "Every muscle ached as I felt numerous broken bones inside me struggling to mend."
    scene bg_medward at blurin(1.0):
        blur 5
    with dissolve
    MC '(What happened back there?)'
    MC '(Shit shit! How in all the damn hells did she know about me?)'
    MC '(Urghh... Why is the healing taking so long?)'
    BLACK 'The effects of the poison are still active within our bloodstream.'
    MC '(That thing it... {i}It nearly killed us{/i}.)'
    BLACK 'Yes.'
    MC '(But how? I thought we were like, nearly impossible to kill or something!)'
    BLACK 'This assessment is incorrect.'
    MC "(What? Well... We've handled everything until now!)"
    BLACK 'Our battle form is durable but {i}not invincible{/i}, there are no doubt plenty of beings capable of killing us.'
    MC '(Well, there goes my power fantasy I guess.)'
    BLACK 'The battle form, like all abilities, must be nurtured to develop.'
    MC "(You mean like, I have to train more?)"
    BLACK 'Yes, your body will adapt and evolve to handle greater threats.'
    MC "(Great... That's something at least.)"
    scene black with dissolve
    "The thought of facing that {i}thing{/i} again filled me with dread."
    "As the holly sap took effect, I drifted off to sleep, haunted by the images of it's horrible face charging towards me."
    $ Pause(0.1)
    show cg_mib at zoomin(1.5, 1.5) with dissolve:
        anchor  (0.43, 0.0)
        pos     (0.52, 0.1)
        zoom    1.0
    play sound2 "audio/cfx/ticks.ogg"
    "Towards {i}us{/i}."
    scene black with dissolve
    $ PlaySoundRandom("clockWind")
    $ InfGainDaily(False)
    $ TimeAdvTo(TIME_MORNING)
    "A few hours later..."
    $ InfGainDaily(True)
    scene bg_medward

    $ AutoMus(False)
    show nyx at center_f
    show bg_medwardoverlay onlayer characters:
        align (0.5, 1.0)
    with dissolve
    NYX @shock 'Feeing alright?'
    $ PlaySound("audio/cfx/dark_chime.ogg")
    MC @talk "Yeah... Never better." # tiger fucking woods
    NYX @talk 'You look like shit.'
    MC @talk 'Well, I feel like shit so...'
    $ PlayMusic("audio/music/3_Novaras_L.ogg")
    'Captain Nyx forced a faint smile before nodding softly.'
    NYX @talk "I suppose you've got questions."
    MC @talk "Damn right."
    $ choicemenu = ["a", "b", "c", "d"]
    if choicemenu:
        menu qst_bloodhound_4_hospital_nyxChoices: # exhaustive options
            'How did you know about me?' if 'a' in choicemenu:
                NYX @talk "I've had you both followed since your return."
                MC @surprised 'What?'
                NYX @angry "When you and your friend returned, under the circumstances you did, I didn't buy that you just strolled your way back to Novaras in record time."
                NYX @angry 'At first, I considered you being Demorai spies.'
                NYX @talk 'So, I called in some favors and had you followed.'
                MC @angry "Why not just tell me!"
                NYX @talk 'I needed to test where your loyalties laid.'
                NYX @laugh 'Oh, and the whole strolling into the desert to change thing? Not very smart.'
                NYX @angry "Did you really think heading out there wasn't going to draw some attention?"
                NYX @talk "You're going to need to learn to be smarter than that."
                MC @angry 'You used me.'
                NYX @angry "This is war, you'll get used to being used."
                $ choicemenu.remove('a')
                jump qst_bloodhound_4_hospital_nyxChoices
            'What in all of the gods was that {i}thing{/i} down there?' if 'b' in choicemenu:
                NYX @talk 'I have no idea.'
                MC @talk 'What?'
                NYX @shock "I knew Azul was onto something big but... I didn't anticipate that."
                NYX @angry "All of Azul's private documents and scrolls have been taken, no doubt destroyed."
                $ choicemenu.remove('b')
                jump qst_bloodhound_4_hospital_nyxChoices
            '...Did you know I was going to be ambushed like that?' if 'c' in choicemenu:
                NYX @shock "...I'm sorry, I predicted there might be a trap waiting for whoever I sent."
                NYX @talk 'I knew that, with your abilities, you had a better chance handling whatever was thrown at you.'
                NYX @talk "But I still made sure to tail you, I couldn't be sure for whatever was waiting and expected the worst."
                MC @talk 'Could have done better with you about five minutes earlier into the fight.'
                NYX @angry "We moved as quickly as we could without drawing attention."
                $ choicemenu.remove('c')
                jump qst_bloodhound_4_hospital_nyxChoices
            'Are you going to tell anyone about me?' if 'd' in choicemenu:
                NYX @talk 'No.'
                MC '...'
                NYX @talk "You're a valuable asset, and I'm fairly confident now whose side you're on."
                NYX @angry 'That said, others may not feel the same.'
                MC @talk "So... No one else knows?"
                NYX @talk 'Your secret is still safe.'
                MC @talk 'But, the inquisitors-'
                NYX @angry 'Fuck the inquisitors.'
                NYX @angry 'And fuck Lukkan and the others.'
                NYX @angry "The city Watch needs all the help it can get, and none of those fuckers are willing to lift a damn finger to help if it involves pulling from their precious sectors."
                NYX @talk "I may call upon you again, for help."
                NYX @angry "You may be one of the only few in this wretched city I actually know I can trust."
                $ choicemenu.remove('d')
                jump qst_bloodhound_4_hospital_nyxChoices
    MC @talk "I'm done with questions..."
    MC @talk "What now?"
    NYX @talk 'Not much, you go back to doing whatever it is you were doing before.'
    MC @talk 'But... The investigation?'
    NYX @talk "Not your responsibility anymore."
    NYX @talk "At least, until I can do some more digging into what Azul found."
    $ QstComplete(QstTheBloodhound)
    MC @talk "...That {i}thing.{/i}"
    NYX @talk "Returned to its master, no doubt."
    MC @talk "{i}Master?{/i} You mean-"
    NYX @angry "Yes, that thing serves to cover the tracks of it's master."
    MC @talk "How do you know?"
    NYX @talk "Whatever Azul uncovered brought him into the sights of some {i}powerful{/i} people."
    NYX @talk "That thing didn't just kill him, it destroyed all of the sensitive information Azul had been gathering."
    NYX @angry "Whatever he found, Azul got too close."
    MC @talk "...If that {i}thing{/i} had already killed Azul, why leave the body like that?"
    MC @talk "Why was the thing still down there... {i}waiting?{/i}"
    NYX @angry 'I believe it was waiting {i}for me.{/i}'
    NYX @angry 'No doubt whoever is at play here knows of my involvement and would rather have me silenced.'
    NYX @angry 'As for why the body was left there?'
    NYX @angry 'Perhaps as a warning... A message, in case that monster failed.'
    'I felt ill with the thought.'
    'What kind of a person leaves a warning like {i}that?{/i}'
    NYX @talk '...Oh, that reminds me, here.'
    NYX @talk 'Your reward.'
    $ PlayerAddItem("gold",600)
    #MC is given some coins
    NYX @talk "Well, I best leave you be for now."
    NYX @talk "Watch yourself [player_name!t]..."
    NYX @angry "{i}You might be in their sights too now.{/i}"
    hide nyx with dissolve
    'As Nyx left, I dropped my head back onto the pillow.'
    scene bg_medward at blurin(5.0):
        blur 15
    with dissolve
    MC '(...Fucking great.)'
    #Text appears on screen
    hide bg_medwardoverlay onlayer characters
    scene black
    with dissolve
    'A couple hours later, a nun came by and said I could leave now.'
    'Leaving the hospital ward, I let out a grim chuckle at myself hoping to not end up here again.'
    MC '(Back into the world of the living...)'
    $ AutoMus(True)
    $ AutoAmb(True)
    $ CharSetClothes("mc", "normal")
    $ LocNameReset()
    $ LocSet("novaras_dist_house")
    $ LocEnter()