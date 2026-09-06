label qst_ValleyOfPrey:
    $ QstStart(QstValleyOfPrey)
    #Continued
    VES @smile_talk 'Good!'
    VES @talk 'Give me a moment to get my stuff...'
    hide ves with easeoutright
    'Ves pushed open the flap of her tent as she headed inside of it once again. My thoughts turned to the Skorn.'
    'I had heard about them in class, the great desert bison that roamed the harsh Valley of Death but had never seen one before with my own eyes.'
    show ves at cright_f
    with easeinright
    'Ves quickly returned holding her sharpened axes, a spear, and other such equipment.'
    VES @talk 'Are you ready?'
    MC @talk 'As I’ll ever be.'
    VES @talk 'It’s at least an hour or so trek on foot... I’ve got water but be prepared, the desert is harsher than you know.'
    MC @talk '... I think I can speed things up.'
    show ves surprised
    $ CharSetClothes("mc", "naked")
    show mc at nod
    'Ves’ eyes widened and she flushed red watching me strip off my clothes in front of her.'
    VES @surp_talk 'W-What are you doing?!'
    "Ves' eyes stared down at the cock dangling in front of her."
    MC @talk  'I’m going to transform.'
    MC @talk 'I can get us across the desert and back much faster in my other form.'
    'Turning paler white than I had ever seen her before, Ves looked away anxiously.'
    VES @surp_talk  'I... Yes, that makes sense.'
    scene black with dissolve
    'As I took off the last of my clothes, now accustomed to the once agonizing, brutal transformation after some painful ‘adjustments’...'
    play sound "audio/cfx/transform.ogg"
    'I changed myself into my second form in record time.'
    $ LocFlush()
    show mc_transformed at cleft
    show ves surprised at cright_f
    with dissolve
    MC 'Are you ready?'
    VES @surp_talk 'How will you—'
    VES @surp_talk 'H-HEY!'
    'I scoped Ves up under my arm.'
    MC 'Which way?'
    VES @surp_talk '... T-That way.'
    scene black with dissolve
    $ Pause(0.5)
    scene bg_valley_of_death with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/8_ValleyofDeath.ogg")
    $ LocNameSetTemp(_("Valley of Death")) # $ LocNameReset()
    'Ves pointed in the direction, and I followed.'
    'With Ves in my arms, I quickly began to propel us across the hot desert sands with the thick tentacles swinging us across like vines, covering miles in mere moments.'
    'Ves seemed slightly unsure of what to do as she was cradled in my arms.'
    'I towered over her in this form, and no doubt this shape still had some strange, terrifying quality to those unaccustomed to seeing it.'
    'Still, as the sun beat on my back and the cool breeze passed us by, she seemed to relax, curiously tracing her fingers along the hard exterior of my flesh inquisitively.'
    scene  cg_ves_hunt_desert with dissolve
    'Finally, we arrived upon some great flat valley where just across the ridge below revealed a great herd of Skorn.'
    'Huge towering three-eyed beasts with legs the size of small buildings, their long trunks pushed deep down into the desert, finding water in minutes that would take men hours to dig far enough down to find.'
    MC '...They are... bigger than I imagined.'
    VES 'Come... We must take the strongest one.'
    MC 'Huh? Why do you—'
    VES 'To go for the weak or young is shameful...'
    VES 'When we hunt, {i}what{/i} we hunt is of great importance.'
    'Readying her axes, Ves scanned across the many Skorn before pointing out one of the largest amongst them with a slightly darker complexion.'
    'Its ram-like horns formidable in size, made it appear like some ancient god of the desert.'
    MC 'What’s the plan to—'
    'Before I could finish my sentence, Ves charged like a woman possessed with both her axes towards the colossal Skorn.'
    VES 'GRGHHHHH!'
    MC '(... Well, fuck.)'
    'Following after her, the other now spooked Skorn noticing her presence instinctively began to flee.'
    'Soon there was a massive stampede of the beasts fleeing across the desert plains.'
    'Following behind Ves, I quickly grabbed her once again as the stampede hurried shoulder to shoulder, often smashing and barging violently into each other as they fled.'
    VES 'Don’t lose him!'
    'Ves shouted, pointing towards the great Skorn whose trunk smashed into the bulk of a smaller Skorn sending it toppling over onto its side as it fled from us.'
    VES 'Quick! Throw me!'
    MC 'What?!'
    VES 'Just do it!'
    'Throwing Ves hurtling through the air, she climbed onto the back of one of the Skorn and scaled her way up its hide.'
    'I watched with surprise as she leapt from Skorn to Skorn, gaining on the great beast with greater speed than even I was!'
    'Narrowly dodging the crazed Skorn, the two of us were finally catching up and close behind the when suddenly...'
    'The ground began to vibrate greater than even the herds stamping could cause.'
    'The sand ahead of us began to move as a small whirlpool formed and seemed to sink the ground, dragging nearby Skorn into its pull.'
    play sound "audio/cfx/scorpion_roar.ogg"
    scene  cg_ves_desert_worm_attack with flash
    $ AutoMus(False)
    $ PlayMusic("audio/music/27_Sands_Boss.ogg")
    'Suddenly, a great beast flung itself out of the sands and collided with our Skorn, its huge jaws clasping down onto the beast as it slammed it into the desert sands.'
    VES 'It’s a {i}bazark!{/i}'
    $ QstSetProgress(QstValleyOfPrey, 1)
    'Ves cried out in disbelief, watching as the Skorn screamed out and tried to escape before the bazark slammed its teeth around the throat of the Skorn, violently squeezing and shaking many times till it snapped its neck.'
    'Digging its colossal jaws into the soft hide of the Skorn, it gnashed and tore as it swallowed down pieces of its flesh.'
    'Then with a glint in its eye it noticed us still stood there rooted to the ground watching, and turned its attention towards us, snarling malevolently.'
    play sound "audio/cfx/scorpion_pain.ogg"
    MC 'VES!'

    $ TransformMC(True)
    $ TransformMarkus(True)

    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_LeftExtra = ["ves"], CharIDList_Right = ["e_bazarkWorm"]))

    ### achievement
    if can_unlock_achievement("DESERT_LORD"):
        $ unlock_achievement("DESERT_LORD")

    $ TransformMC(False)
    $ TransformMarkus(False)

    scene pbat_desert
    show mc_transformed at left
    show ves surprised at cright_f
    with dissolve
    'As the bloodied and battered bazark shook its head in a daze, blood dripping down its face onto the hot desert sand, Ves turned to me and shouted breathlessly.'
    VES @talk '{i}*Huff*{/i} It just won’t stop coming!'
    'As the bazark continued to shake violently, it pulled up enough of its hide to reveal the soft underbelly of the great beast, revealing some beating organ covered below the thin flesh.'
    MC '...Ves I have an idea!'
    VES @talk 'What are you—'
    VES @talk 'Whoa!'
    scene cg_mc_from_worm with dissolve
    'Grabbing Ves once again, with frantic motions I began to claw my way up the bazark, my tentacles slamming into the sides of its flesh, tearing out chunks of it as I swung towards the top of the thing.'
    'Its claws flailed and slashed around frantically as though we were some itch it needed to scratch, only narrowly missing us as the thing took a swipe at itself, leaving bloody claw marks on its own scaled flesh.'
    'Finally reaching the top of the bazark, Ves slammed her axes into the flesh to hold herself in place as the thing tried once more to shake us off. Ves looked to me uncertain of what to do next.'
    VES 'Now what?'
    MC 'I need you to go for its eyes!'
    VES 'What!'
    MC 'Its eyes! Just go for its eyes!'
    'Quickly, I swung in a circular descent towards the ground once again, feeling the rush of cool air and kicked up desert sand as I felt one of its swinging claws narrowly miss me, forcing me to drop and roll harshly onto the hot desert sand.'
    'Under normal circumstances, a few bones would have been broken, but thanks to the parasite’s hard exterior I was left a little bruised but mostly unscathed.'
    'Struggling to stay still on the bazark’s back as it tried desperately to rip her from itself, Ves dragged herself forward with swings of her axes.'
    'Piercing through the flesh to anchor herself in place till she made it to the front of the beast’s reptilian head.'
    'Its eyes twitched and focused on her when it noticed her lurking there above it, axes raised.'
    'Ves cried out as she slammed her axe into soft eye of the bazark but there was little it could do.'
    'Throwing itself backwards, the great beast flailed helplessly, unsure of what to do with its arms, unable to reach the orc on its head.'
    'For a moment, the thing seemed ready to slam itself onto its back and submerge back into the depths of the desert sands, if only to get rid of the orc still hacking away at its eyes.'
    'But now, with its underbelly exposed once again I lunged forward, claws ready as I slashed through the flesh and forced myself inside the beast.'
    'It now changed course in blind agonising panic and bellowed forward, obviously aware of my presence but it was again too late.'
    'Slashing and clawing my way through the bazark’s soft flesh with ease, it began desperately to claw at the gaping wound in its soft underbelly to try and pull me out, but it was impossible.'
    'Forcing my way through the back of the beast I tore my way out in a spray of violence and blood, thick chunks of red meat dropped down onto the coarse sand floor from the gaping hole in which I had emerged from.'
    play sound "audio/cfx/scorpion_roar.ogg"
    'With one final whimpering howl, the thing slammed dead into the hot sand, its mouth hanging open and quivering for a final few sickening motions in defeat.'
    scene pbat_desert
    show mc_transformed at left
    with dissolve
    $ PlayMusic("audio/music/8_ValleyofDeath.ogg")
    MC '{i}*Huff*{/i} Ves! Are you okay?'
    'I looked around frantically for her.'
    MC 'Ves!'
    show ves at cright_f
    with dissolve
    VES @talk 'I’m alright...'
    MC 'I can’t believe we actually managed to bring that thing down!'
    'Stepping forward towards the mouth of the dead beast, Ves reached down to carve out and take one of its scales.'
    VES @talk 'For such a prized kill as this, we’d normally take the skull to honour a War Hall.'
    VES @talk '{i}*Sigh*{/i} But I suppose this will have to do...'
    'Looking over at the dead Skorn we were hunting earlier, I glanced at Ves uncertainly.'
    MC 'Hey, how are we going to carry this damn thing back now?'
    'Ves looked at me and smiled.'
    MC '... Oh no.'
    scene black with dissolve
    $ CharChangeRel("ves", 1)
    $ QstSetProgress(QstValleyOfPrey, 2)
    jump rom_Ves_5_PostHunt
