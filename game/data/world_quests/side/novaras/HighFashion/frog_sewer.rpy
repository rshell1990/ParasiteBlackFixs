label palam_sewer:
    $ AutoMus(False)
    $ PlayMusic("audio/music/15_Experiments.ogg")
    'Following Sister Divine, we headed down into the bowels of the tower.'
    'Every so often, as we descended the long, winding and increasingly dark staircases lit only by flickering torchlight, we’d hear a loud thump followed by the vibrating of the tower.'
    scene pbat_sewer with dissolve

    show mc at cleft
    show divine at cright_f
    MC @talk 'What was that?'
    DIVINE 'I know not... It only began after we closed off the Sub-Basement following the incident.'
    MC @talk '... Hmm.'
    'At the bottom level of the dark and dreary tower, I was led towards a vault like oval door, sealed by a glowing blue aura that pulsated and acted as a barrier to keep whatever was on the other side trapped.'
    'Lightly touching its surface with my finger, I felt a zap of pain course through me.'
    MC @surprised 'Ah!'
    DIVINE 'This is the best we could do in the meanwhile.'
    DIVINE 'We heard a few screams from those still trapped inside but... we haven’t heard any for a while now.'
    'With a swipe of her hand, the glowing blue began to dissipate, and the opening into the darkness was now clear.'
    DIVINE 'Be careful in there...'
    MC @talk 'Is there no one to assist me?'
    DIVINE 'I cannot risk any more of our own.'
    DIVINE 'Good luck to you.'
    hide divine with easeoutright
    MC @talk '{i}*Sigh*{/i} Here goes nothing...'
    show mc at center
    with move
    'Stepping into the vault, the blue shield once again rose from behind, trapping me inside the dark forsaken caverns of the Palam Tower.'
    MC 'Why did I agree to this? This was a terrible idea.'
    MC 'Alright... I guess I better head further inside and then change when I’m out of sight of Divine.'
    MC 'Hopefully I won’t get eaten before then...'
    scene black with dissolve
    play sound2 "audio/cfx/transform.ogg"
    'Down in the depths of the Sub-Basement, I transformed into my ‘other’ form.'
    scene pbat_sewer
    show mc_transformed at center
    with dissolve
    'It was damp and cold down here, a place the mages rarely trod unless performing the most dangerous of spells.'
    'I could see better once transformed, through a red tint I could make out shapes, the tiled ground and more as I patrolled through the eerily quiet halls.'
    'Every so often I’d find a body or two, poor unlucky souls who had failed to make it out in time.'
    'They were mangled with flies crawling around the old, now festering wounds.'
    'Dried blood stained the walls, and as I inspected the wounds, I wondered what sort of creature could have done this?'
    'As I smelt the air, something wretched and rotten drew me deeper into the labyrinthine tunnels of the Sub-Basement.'
    'Finally, I arrived upon what seemed to be the site of the summoning, the white chalk now stained with dried blood splatters as corpses littered around the room had been moved and piled up into a decaying mound of death.'
    'From the small signs of struggle, it had been a massacre in here.'
    'Inexperienced mages conjuring up something beyond what they could possibly hope to control...'
    'We had heard of such stories before but... seeing the result up close and personal was one of the more horrifying things I’d had to bear witness to.'
    'Suddenly, a loud rumbling sound could be heard as a rhythmic stomping seemed to shake the walls around me.'
    'Looking towards one of the dark halls leading out, I could hear the thing coming closer towards me.'
    'Hiding behind a pillar, I waited and watched for whatever was approaching from the shadows.'
    $ PlayMusic("audio/music/28_Frog_Boss.ogg")
    scene cg_qstdivine_frog1 with flash

    'Appearing through the darkness, a giant green frog-like creature sprung its way forward.'
    'It’s eyes blinking independently of one another as it looked around at the many corpses on the floor.'
    'Its tongue snapped out, grabbing one of the decaying bodies before lurching it into its mouth.'
    'Its razor teeth chomped down, gnawing at the bones which snapped with the movement of its jaws.'
    'Hideous to behold, the creature smelled of some deep rot and mould as its mouth dripped old blood from the corpse it chewed.'
    'Its back was covered in thick black and sickly yellow spikes that seemed to tingle with the cold air, as if sensing for the slightest vibrations.'
    'Suddenly, the thing stopped chewing... Letting the mangled body roll out of its mouth and slip almost comically to the floor, it raised its snout and sniffed into the air, taking deep guttural breaths.'
    MC '... Does it know I’m here?'
    'Suddenly, its tongue lashed out, tearing away the pillar I was hiding behind!'
    MC '...!'
    MC 'Well, I guess that answers that!'
    MC 'There’s no choice now!'

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ StartBattle(BattleData("pbat_sewer", CharIDList_Right = ["e_frogBoss"]))

    $ TransformMC(False)
    $ TransformMarkus(False)

    scene cg_qstdivine_frog1
    with dissolve

    #PLAYER WINS
    'As the thing weaved drowsily back and forth, blood seeping from its wounds and mouth, it heaved and shuddered before collapsing onto its side.'
    'Its tongue flopped in defeat as it took one last long ragged breath, inflating its stomach before it simply fizzled out in a slow, pitiful death.'
    MC '{i}*Huff*{/i} Where did that thing come from?'
    BLACK 'This creature has proven formidable... We should consider training to enhance our combat abilities further should other predators arrive.'
    MC  'Ha, thanks for the tip, captain obv—'
    scene cg_qstdivine_frog1 with flash
    'The tongue suddenly lashed out, wrapping around my ankle as it tripped me up onto the cold, wet floor.'
    MC 'SHIT!'
    'Dragging me towards its gaping maw of a mouth, I glared at the dozen or so razor teeth waiting to gnash and grind my bones, one desperate last meal for a dying beast.'
    play sound "audio/cfx/magic_earthy_cast1.ogg"
    scene cg_qstdivine_frog2 with flash
    "Just before it's jaws landed on me, a sparkling blast of magic energy hit the beast."
    scene cg_qstdivine_frog3 with flash
    "The monster wailed and cried out desperately."
    'Finally, it dropped to the floor motionless, and the thing’s eyes rolled deathly white as it lay still again.'
    $ PlayMusic("audio/music/15_Experiments.ogg")
    scene pbat_sewer
    show mc_transformed at cleft
    show divine at cright_f
    with dissolve
    'Stood above me was Divine who flung her blade aside and smiled.'
    DIVINE '{i}I knew it...{/i}'
    DIVINE 'I knew you weren’t entirely human.'
    MC 'Wait! I can explain!'
    DIVINE 'No need, I do not care.'
    MC 'What? But I—'
    DIVINE 'Was the right man for the job, clearly!'
    DIVINE 'Next time though, {i}make sure it’s actually dead{/i} before you call it a job well done.'
    MC 'Yeah... Thanks for that.'
    show divine happy
    'As I rose to my feet, Sister Divine smirked and looked me up and down.'
    DIVINE 'I’ve never seen a being such as you.'
    MC 'H-How did you know?'
    show divine
    DIVINE 'The goddess Palam allowed me to sense it so...'
    MC '{i}... What?{/i}'
    DIVINE 'Magic, no matter the type, carries with it its own distinct scent.'
    DIVINE '{i}You{/i} smell unlike anything I have ever encountered before.'
    DIVINE 'I knew there was something different about you the moment I laid eyes on you.'
    MC '... Well, what are you going to do?'
    DIVINE '{i}... Nothing.{/i}'
    MC 'Nothing?'
    DIVINE 'Your secret is safe with me.'
    DIVINE 'I can think of {i}so{/i} many other things I’d rather do with you...'
    show divine at center_f with ease
    'Sister Divine stepped forward alluringly, her hands resting over the hard exoskeleton of my chest.'
    MC 'Uhh... Are you—'
    DIVINE 'You know what I’m asking for.'
    MC '... Wouldn’t you prefer I take my human form?'
    DIVINE 'Not at all, I could have a human any day of the week...'
    DIVINE '{i}But this...{/i} This form is something special.'
    MC  'I... What about the crystal?'
    'Sister Divine held up the glowing purple crystal bound in some ancient metal for me to see.'
    DIVINE '{i}All ready for when you leave.{/i}'
    DIVINE 'So... how about it?'
    DIVINE 'We could learn so much from each other...'
    menu:
        '{image=[ICON.HEART]} Well, when you put it like that... ({b}Warning FUTA ahead!{/b})':
            $ CharSetLover("divine")
            $ CharChangeRel("divine", 1)
            DIVINE 'I’m glad to hear that.'
            DIVINE 'Here, take this...'
            'In my hands, Sister Divine palmed a small blue stone with a white insignia on it.'
            MC 'What is this?'
            DIVINE 'It is my blessing to allow you to wander this tower at night.'
            $ HouseLockPalamTower().CanEnterAtNight = True
            $ AddNotif(_("You can now enter the Palam Tower at night."))
            MC 'You mean—'
            DIVINE 'We prefer our mages handle their dalliances with... discretion.'
            DIVINE 'This way suits both our needs.'
            $ QstStart(RomanceDivine)
            'With that, Sister Divine turned to leave the basement while I followed in her wake.'
            DIVINE 'Come, this way...'
            'In her hands, a glowing blue ball began to form, illuminating the passageways back for us.'
            'Along the way, I noticed Sister Divine kept looking back at me, perhaps contemplating what was to come between us.'
            scene black with dissolve
            'As I changed back into my human form, Divine remarked I should get dressed before making my way out of the basement, scrambling to locate the clothes I had left on my way in, we finally returned to the main halls of the tower.'
        '{image=[ICON.HEART_CROSS]} You’re not really my type... No offence.':
            $ CharChangeRel("divine", -1)
            DIVINE 'Hmm... A shame.'
            DIVINE 'Then I guess our business has concluded.'
            DIVINE 'Come, I will escort you out.'
            'In her hands, a glowing blue ball began to form, lighting the way back for us as I followed behind.'
            'I sensed the disappointment in Divine’s voice, but decided it was probably best to keep my mouth shut.'
            scene black with dissolve
            'As I changed back into my human form, Divine remarked I should get dressed before making my way out of the basement.'
            'I scrambled to gather up the clothes I has abandoned on my way in and we finally returned to the main halls of the tower.'
    scene bg_palam_mainhall
    show mc at cleft
    show divine at cright_f
    with dissolve
    DIVINE 'I thank you for your services to the Goddess Palam.'
    MC @talk 'Anytime... Although I hope that next time it won’t be so quite so dangerous.'
    show divine happy
    'Sister Divine smiled, holding out the crystal for me to take.'
    $ QstSetProgress(QstHighFasion, 3)
    $ PlayerAddItem("qst_dros_power_crystal")
    DIVINE 'It’s all yours.'
    MC @talk 'Glad to be of service.'
    if QstIsActive(RomanceDivine):
        DIVINE 'I look forward to our next meeting...'
    else:
        DIVINE "Of course."
        DIVINE "Now, if you will excuse me..."
    $ AutoMus(True)
    $ LocSet("novaras_dist_mage")
    $ LocEnter()
