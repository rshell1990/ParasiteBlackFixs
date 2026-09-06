#Quest updates: Bring Dros to Sister Divine 
#Upon returning to Dros, when speaking to Dros about his problem, new prompt 
label dros_4_getDros:
    DROS @shock 'A-Already?'
    DROS @talk 'Very well, lead the way.'
    scene black with dissolve
    #####
    $ Pause(0.5)
    $ LocSet("novaras_palam_mainhall")
    $ LocFlush()
    show dros at cleft
    show divine at cright_f
    with dissolve
    DIVINE "Ah, Dros... You've arrived."
    DROS @smile "It is good to see you, Sister Divine."
    DIVINE @angry "Given the trouble you've caused us in the past, I normally could not say the same..."
    DIVINE 'But I suppose these are special circumstances.'
    DROS @sad 'A-Ah... My behaviour has perhaps not always been the best, I admit, b-but-'
    DIVINE 'Come, Dros, I have prepared the ritual.'
    DROS @sad 'Will... Will it hurt?'
    DIVINE '...Hopefully not, Dros.'
    DIVINE 'Are you truly sure you wish to-'
    DROS @talk "Yes... I'm sure."
    DIVINE 'Very well, follow me then.'
    'As Dros and Sister Divine headed down one of the Hallways, Sister Divine stopped me.'
    DIVINE "I'm afraid this is as far as you go."
    DIVINE 'There are certain rules and traditions us Mages must follow.'
    DIVINE 'You need to wait here.'
    DIVINE 'We will return when ready.'
    MC @talk 'Very well.'
    'Dros sheepishly glanced over his shoulder and looked at me as Sister Divine led him on.'
    'After turning a corner, the two of them were finally out of sight, and I was left completely alone to ponder my thoughts.'
    scene black with dissolve
    MC '(Hm, I hope this was the right decision.)'
    $ TimeAdvBy(TIME_1H)
    'It felt like I was waiting for hours, when I heard the sudden strange sounds and bright lights flash from around the corner Dros and Sister Divine headed down.'
    play sound "audio/cfx/detect_magic.ogg"
    'With my hand at my blade, I took a few steps forward, when suddenly, Sister Divine emerged once again, smiling triumphantly.'
    $ LocFlush()
    with dissolve
    show divine at cright_f
    with easeinright
    DIVINE 'It pleases me to say, it was a success.'
    MC @talk 'Where is Dros?'
    DIVINE 'Dros is gone...'
    DIVINE 'Draya! Come here!'
    $ CharSetVar("dros", "Transformed", True)
    $ CharAddRelEntry("dros", "transformed")
    $ DROS = Character(_("Draya"), image = "dros")
    $ CharSetName("dros", _("Draya"))
    $ CharSetPortrait("dros", "images/characters/dros/fem/portrait.webp")
    'From around the corner, the beautiful elven girl shyly approached.'
    show dros at cleft
    with dissolve
    'For a moment, I did not recognize him, from the softening of the face to the widening of the hips, he looked so different than before.'
    'As he spoke, the voice was a higher pitch, and unmistakenly feminine.'
    DROS @talk 'H-Hello.'
    MC @talk 'Dros? Is that really-'
    DROS @smile '{i}*Cough*{/i} I prefer to go by Draya now.'
    MC @talk 'Oh... I see.'
    DIVINE 'My work here is done.'
    MC @talk 'What do I owe you for your services, Sister?'
    DIVINE 'Nothing.'
    DIVINE 'This spell was... enlightening.'
    DIVINE 'Consider it a gift.'
    MC @talk 'Thank you.'
    DIVINE "You're most welcome... Now, if you don't mind."
    DIVINE 'I have other business to attend.'
    MC @talk 'Of course.'
    scene black with dissolve
    'Sister Divine led us outside, and an ecstatic Draya leapt into my arms to hug me before I pulled her off.'
    #Characters speak over city district
    $ LocSet("novaras_dist_mage")
    $ LocFlush()
    show mc at cleft
    show dros at cright_f
    with dissolve
    DROS @smile "I... I can't believe it."
    DROS @smile "After all this time, I'm-"
    DROS @smile "I feel so alive!"
    MC @talk 'I am glad to help you, {i}Draya.{/i}'
    if DialogueDros().discount == 0:
        DROS @talk "And don't think I forgot what we mentioned."
        DROS @smile "I'll give you a permanent fifteen percent discount on my store from now on." #Permanent unlock of fifteen % off buying anything in Dros store.
        $ DialogueDros().discount = 15
        menu:
            "Only fifteen percent?" (Req_Charm = 7): #Charm check 
                $ DialogueDros().discount = 20
                DROS @talk '{i}*Cough*{/i} I see you still drive a hard bargain... Very well, twenty percent.' #Charm check pass - permanent 20% off buying anything in Dros store

            'I am happy for you.':
                'Draya began to blush.'
    $ GoalComplete(QstGracefulRebirth, 5)
    $ QstComplete(QstGracefulRebirth)
    if not QstIsActive(RomanceDros):
        DROS @lewd 'There um, is {i}one{/i} more thing I wanted to talk with you about.'
        MC @talk 'Oh?'
        DROS @lewd "I suppose I should just come out and say it, shouldn't I?"
        DROS @lewd "You're... {i}Very attractive.{/i}"
        "The comment was a surprising one, if they had given any hints prior to this, they certainly went over my head."
        DROS @smile "I mean, you've done so much for me."
        DROS @smile "And now I look like this, I finally feel I have the confidence to ask these things."
        MC @talk 'Draya, I...'
        DROS @shock "D-Don't feel you have to say yes!"
        DROS @sad 'I mean, I would understand if not... Just...'
        'Draya smiled shyly.'
        DROS @talk 'Well?'
        menu:
            '{image=[ICON.HEART]} I like you too.':
                $ CharSetLover("dros")
                $ CharReplaceRelEntry("dros", "initial", "romanced")
                if "romance_male" in worldChars["dros"]["RelTextIDs"]:
                    $ CharReplaceRelEntry("dros", "romance_male", "romance_female")
                else:
                    $ CharAddRelEntry("dros", "romance_female")
                $ QstStart(RomanceDros)
                pass
                # continues below
            '{image=[ICON.HEART_CROSS]} Sorry, not my type.':
                'Despite her claims I did not have to say yes, my answer clearly left her a little deflated.'
                DROS @sad 'I... I see.'
                DROS @sad 'Well, thank for being honest at least.'
                DROS @talk "It's no matter though! I shall see you around, {i}friend.{/i}"
                'With that, Draya headed off, presumably back to their Tailor shop.'
                $ LocEnter()

        DROS @shock 'You... You do?'
        DROS @lewd "I... Well, that's good!"
        'Draya seemed to ponder the thought before giggling.'
        DROS @lewd "So, what are we?" 
        DROS @lewd "I'm sorry, I'm still getting used to all this."
        DROS @lewd "What should I call you, [player_name!t]?"
        $ dros_player_ref = renpy.input(_("What should I call you, [player_name!t]?"), default = _("Master"))
        $ dros_player_ref = dros_player_ref.strip() or _("Master")
        DROS @smile "[dros_player_ref!t]? Well... If that's what you wish."
        DROS @talk 'I have to speak to the Madam and change some details about my arrangement with her.'
        MC @surprised 'You still intend to work at the Brothel?'
        DROS @smile 'No, not at all.'
        DROS @lewd "But we will need a safer place than my shop for more... {i}intimate{/i} moments."
        DROS @angry 'Having you come and go from the shop too much may draw some unwanted attention... Even with me like this.'
        DROS @angry 'Last thing I need is inquisitors or someone poking into my business.'
        MC @talk 'So, what will you do?'
        DROS @smile "It's simple, {i}I'm going to pay for the room myself.{/i}"
        MC @talk 'Will that not be costly?'
        DROS @smile "I can afford it... Being a tailor does have its perks."
        DROS @lewd 'Besides, {i}I cannot wait to see you there, [dros_player_ref!t].{/i}'
        MC @smile 'I will see you there then, Draya.'
    'Draya smiled once again as she leaned forward to kiss me on the cheek before hurrying off.' 
    hide dros with dissolve
    'All of that usual anger seemed to have washed away.'
    if QstIsActive(RomanceDros):
        MC "(Something tells me I'm in for a good time the next time I see them.)"
    $ LocEnter()