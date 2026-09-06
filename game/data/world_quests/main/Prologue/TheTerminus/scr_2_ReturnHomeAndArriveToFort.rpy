label qst_Terminus_ReturnHomeFromEitherTavernOrBordello:
    $ TimeAdvBy(TIME_1H)
    $ PlayMusic("audio/music/7_novaras_d.ogg")
    'Dragging myself in, I called out for [regina_ref!t] but got no reply.'
    $ PlaySoundRandom("woodenDoor")
    show mcprologue at cright_f with easeinright
    'As I listened out, I heard what seemed to be soft moans coming from her bedroom.'
    'As I approached the door, I contemplated what to do next...'
    play sound "audio/sex_sounds/reginamasturbate_loop_fade.ogg"
    $ CharSetClothes("regina", "towel")
    menu:
        "Peek through the door.":
            scene regina_mast with dissolve
            $ PlaySexFx("audio/sex_sounds/reginamasturbate_loop.ogg", 1)
            $ Pause()
            'Creaking open the door ever so slightly, I peeked through the gap.'
            'Inside, [regina_ref!t] lay on the bed writhing in pleasure as she touched herself.'
            'The moonlight reflected off her pale skin as sweat dripped down from her onto the quilts.'
            'I felt a tingle of excitement growing as I watched her, unable to tear my eyes away as her soft mouth opened, letting out hot, elated gasps of pleasure as she plunged the fingers of one hand deep inside herself.'
            'She licked the fingers of her other hand then fondled her nipples, pulling them ever more erect as she contorted with pleasure.'
            'Stupidly, I leaned too far forward on one of the floorboards and it creaked loudly.'
            '[regina_ref_cap!t] looked {b}straight at me{/b} creeping through the gap.'
            $ StopSexFx()
            $ UnlockGalSceneAndGrantXp("regina", "mast")
            $ LocFlush()
            show mcprologue at cright_f
            with dissolve
            $ PlaySoundRandom("woodenDoor")
            'I darted away from the door and stepped back as I heard her footsteps coming closer.'
            'The door swung open as [regina_ref!t] stepped out stared at me, flushed red from embarrassment with a towel now wrapped around herself for dignity, looking both appalled and mortified.'
            show regina at cleft with easeinleft
            MC 'I didn’t mean to, uh, see you like {i}that.{/i}'
            REGINA @shock 'I...'
            REGINA @shock 'W-Why are you home so early?'
            MC '... There’s something I need to talk to you about.'
        "Knock the door. ":
            'As I knocked the door gently, I heard the moans from the other side fall suddenly silent.'
            show mcprologue at nod
            MC 'Um, [regina_ref!t]? It’s me...'
            REGINA @talk 'One second, love!'
            $ PlaySoundRandom("woodenDoor")
            'After a few moments of shuffling from the other side of the door, it swung open to reveal [regina_ref!t] in a towel, wrapped tightly around the curves of her body.'
            show regina lewd at cleft with easeinleft
            REGINA @lewd_talk 'You’re home earlier than I expected...'
            MC 'Yeah... I need to talk to you about something...'
            REGINA '...'
    #BOTH ROUTES CONTINUED
    show regina sad
    'When she saw the solemnity of my face, she immediately realised something was wrong.'
    'I sat her down to explain what had happened and she burst into tears, hardly able to breathe between her sobs.'
    scene black with dissolve
    'I promised her I would be okay, and she made me promise I would come home safe.'
    'We both knew the likelihood of which was very low, but we lied to comfort each other anyway.'
    'The rest of the night was spent in a dolorous, awkward silence.'
    '[regina_ref_cap!t] kept to herself, frantically trying to avoid the topic before she retired to her room... to cry.'
    $ TimeAdvTo(TIME_VISUAL_DAWN)
    $ Pause(0.5)
    'After such a restless night, I saw [regina_ref!t] just once in the morning before my departure.'
    'I don’t think she could’ve managed more of it.'
    $ CharSetClothes("regina", "normal")
    $ LocFlush()
    show mcprologue sad at cright_f
    show regina sad at blurin, center with easeinleft
    'She rushed over to me and embraced me until she started to shake, it ended with me holding her up as she quietly begged me to do whatever I had to in order to stay safe so I could come back to her.'
    'I held back the tears so she couldn’t see me cry, I didn’t want her to see me like that.'
    scene black with dissolve
    'I slid out the door with my bag and made my way out towards the fort, where my training would truly begin...'
    $ QstSetProgress(QstTerminus, 5)
    $ LocSet("novaras_dist_house")
    $ LocEnter()

label qst_Terminus_ArriveToFort:
    $ TimeSetTo(TIME_NOON)
    show cg_guard at left
    show cg_guard at right_f as guard2
    with dissolve
    'Fort Sebastian was an old but well-maintained fort towering over Novaras Army District.'
    'A dark, foreboding monolith of a fortress with at least a few hundred men in it at any given time.'
    'It was not a welcoming place, cold, bare, and utterly practical.'
    'It was all the more dismal due to the ironclad guards who blocked each of the exits.'
    'Stone-faced, they didn’t need to say anything to let us know that leaving was not an option.'
    $ LocFlush(dissolve)
    show mcprologue at cleft with easeinleft
    'As we all waited in line, dejected, miserable looks on our faces which hung heavy below the dull grey skies, the only saving grace was the appearance of Markus, who took his place beside me.'
    show markusprologue at left with easeinleft
    'In our uncomfortable silence, I leaned over to whisper to Markus.'
    MC '... Hey.'
    MARKUS 'Hey.'
    MC 'Do you know what happens next?'
    MARKUS 'No idea, something about some commander coming to meet us.'
    $ CharSetClothes("kiara", "normal")
    'As I peered through the crowds of people one girl in particular caught my eye, she had short ginger hair and a freckled face.'
    show kiara at right_f with easeinright
    'When she saw me looking she smiled and winked before I averted my gaze, sheepish at having been caught.'
    show kiara happy
    'When I glanced back to look at her, she was chatting with some of the other recruits, my eyes wandered down her frame to take a good long look at her butt.'
    scene black with dissolve
    MC '(Damn... That is one cute ass.)'
    "My ogling was interrupted by a commanding shout:"
    $ LocFlush()
    show cg_guard at center_f
    with dissolve

    OFFICER "Ladies! W-w-w-welcome to Fort Sebastian!"
    "The crowd of recruits went silent and looked at the source of the sound."
    "Atop a wooden podium in the center of the yard stood one of the soldiers, his armor adorned with what seemed to be an insignia of a higher rank."
    OFFICER "I am the fort's quartermaster Joakim, but you fresh bloods can simply call me..."
    "He opened his arms wide:"
    OFFICER "Master!"
    "Some recruits chuckled at the pun, and as they did so, the guards around the crowd tilted their spears towards us in unison."
    "{i}Silence.{/i}"
    JOAKIM "Tsch tsch tsch!"
    "The quartermaster wagged his finger towards us."
    JOAKIM "When I speak. {i}You listen.{/i}"
    "No one said another word, and Joakim continued on as if nothing had just happened."
    JOAKIM "I was given the authority to deliver to you the following briefing for your first mission as members of the Scouts Corp..."
    "A wave of confused looks were shared amongst everyone in the crowd."
    MC "(What?! What mission?)"
    JOAKIM "Listen now!"
    JOAKIM "{i}I will not repeat myself.{/i}"
    JOAKIM "...You will head to the barracks,"
    "He paused for a moment and pointed at a door behind him, speaking slowly and clearly as if he was talking to a bunch of children:"
    JOAKIM "Which you can find through that door over there,"
    JOAKIM "...In there, you will find your set of scout gear, in your trunks."
    "I exhaled in relief."
    MC "(Fucking clown, what is his-)"
    show cg_guard at shake
    JOAKIM "WHILE THERE, you will have another crucial objective to complete..."
    JOAKIM "Memorize where your fucking bunk is!"
    "The clutches of tension finally started to let go off the crowd as the realization of the nature of our {i}mission{/i} sunk in."
    JOAKIM "After you greenhorns get your gear, you must swiftly execute a changing manoeuvre, then return here, to the yard."
    JOAKIM "Captain Duprey will then take over and... debrief you."
    JOAKIM "You've got but an hour to complete your mission."
    "The quartermaster raised both his hands in the air for a moment of silence."
    JOAKIM "Make your Emperor proud now!"
    play sound "audio/cfx/training_aye.ogg"
    hide cg_guard with easeoutright
    "A couple recruits moved to pose a question, but the quartermaster leapt off the wooden podium and walked swiftly towards the barracks without giving any of us another look."
    show markusprologue at left
    show mcprologue at cleft
    with dissolve
    MARKUS "So, [player_name!t], shall we discuss our mission strategy?"
    MARKUS "Or should we try and acquire that ass-et you've been evaluating?"
    MC "*Sigh* Let's just get on with it."
    hide mcprologue with easeoutright
    MARKUS "It might be a mission-critical one!"
    hide markusprologue with easeoutright
    $ QstComplete(QstTerminus)
    $ QstStart(QstForgedInFire)
    $ LocEnter()