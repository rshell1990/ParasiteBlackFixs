label qst_DamzelDizzt_3_talkTarek_successCharm:
    TAREK 'But how? I have paid your people handsomely to stay away!'
    MC @talk 'That is the only reason you are getting this warning now.'
    MC @talk 'It is in all of our interests to avoid a messy investigation.'
    'Tarek angrily slammed his fist onto the table, grumbling beneath his breath.'
    TAREK 'You force us all into misery, you give us no choice but to become thieves and criminals to make a true living!'
    TAREK 'We play by your rules and what do we get? Nothing but lies and more misery!'
    TAREK 'What choice is there for us stranded in this wretched city of yours? You make monsters of us all!'
    menu:
        'Say nothing.':
            'Tarek sighed in exhaustion, dejected in defeat.'
            TAREK 'What will I do now?'
            MC @talk "Not our business, we’re just letting you know."
            TAREK '...'
            TAREK 'How do I know you are who you say you are?'
            MC @talk 'What?'
            TAREK 'Why is Nijah with you?'
            MC @talk 'We needed her to get an audience with you without raising suspicion.'
            TAREK '...'
            MC @talk 'We prefer to keep things quiet.'
            'Tarek remained unconvinced.'
            TAREK '... Prove to me you are Inquisitors.'
            MC @talk 'How?'
            TAREK 'Inquisitors are wielders of magic... Show me yours.'
            MC '(...Shit.)'
            TAREK 'Perhaps you are who you say you are, perhaps not.'
            TAREK 'You ask a lot but give no proof other than your word...'
            menu:
                'We are not as we seem...':
                    #2A.) Continued
                    TAREK 'What do you mean?'
                    MC @talk '(Damn it, I hope Nijah doesn’t overreact to this next part!)'
                    'Looking at Markus, he gave me an incredulous look as I nodded, and he reluctantly nodded back in understanding.'
                    scene black with dissolve
                    'Rising to our feet, the two of us transformed.'
                    play sound2 "audio/cfx/transform.ogg"
                    'Nijah kicked her seat backwards in fear, petrified as she stared at the strange beasts before her.'
                    'Tarek, himself taken back, rose from his chair and moved with his back up against the wall, reaching for his blade as he turned pale white at the sight of the beasts before him.'
                    $ LocFlush()
                    show markus_transformed:
                        xcenter 0.5
                    show mc_transformed:
                        xcenter 0.2
                    show tarek:
                        xcenter 0.8
                        xzoom -1.0
                    with dissolve
                    MC @talk 'As you can see, we are telling you the truth.'
                    TAREK 'What... What kind of monsters are you?!'
                    MC @talk 'Appearances are everything when working for the Inquisitors.'
                    MC @talk 'You know this.'
                    TAREK '...'
                    'Breathing heavily, Tarek slowly began to relax.'
                    'He began laughing to himself but I suspected it was more from shock than finding the situation amusing in any way.'
                    TAREK 'Very well... You win, inquisitors.'
                    TAREK 'I shall leave this city and take those who follow with me.'
                    $ BlackDiamondLogic().tarekFate = "walked"
                    $ QstDamzelInDiztrezz().PlayerMadeTarekLeaveInquisitors = True
                    MC @talk 'Then our business here is settled.'
                    TAREK 'What about Nijah?'
                    MC @talk 'She works for {i}us{/i} now.'
                    'Tarek glanced over at Nijah who now did her best to maintain some kind of neutral expression, despite the shock of what she’d just witnessed.'
                    TAREK '... Very well.'
                    TAREK 'I hope our paths never cross again.'
                    MC @talk 'For your sake, you should pray.'
                    TAREK '... Hmph.'
                    scene black with dissolve
                    'Changing back into our human forms, we threw some robes over us as we took Nijah to leave with us.'
                    'As we left Nijah tugged at my sleeve.'
                    NIJAH 'You... You have much explaining to do!'
                    MC @talk "In time Nijah, for now, let's just get somewhere safe!"
                    $ LocSet("novaras_dist_pleasure")
                    'Nijah reluctantly nodded, following us to safety as we left the Black Diamond.'
                    'We made our way through the streets of Novaras back to my home.'
                    'She asked if I thought Tarek would keep to his word, and I said I believed he would.'
                    'Satisfied with the answer, Nijah rested her head against my shoulder on the way back, a soft smile on her lips and a lonely tear in her eye.'
                    jump nijah_damzelDiztrezz_afterAction

                'We didn’t exactly bring paperwork.':
                    TAREK 'And that is why Tarek does not trust who you say you are.'
                    MC @talk 'Then don’t trust us.'
                    TAREK '...'
                    "Tarek's eyes squinted as he asked us, his voice slow and deliberate."
                    TAREK '... Tell me ‘Inquisitors’...'
                    TAREK 'What is the name of the Head Inquisitor who helps manage this District?'
                    MC @talk '...'
                    MC @talk '(... Fuck.)'
                    TAREK '...'
                    "Tarek's eyes widened as he saw the sweat drip down from my forehead."
                    TAREK 'MEN! DRAW YOUR BLADES!'
                    MC @talk '(Shit! Shit! Shit!)'
                    jump qst_DamzelDizzt_3_ruckus

        'Offer Tarek some wine to calm down.':
            MC @talk 'Here, have some wine.'
            TAREK @angry 'I don’t want your wine!'
            MC @talk '... As you wish, but you should know we have things set up for you once you leave the city.'
            'Tarek turned angrily towards us.'
            TAREK 'What do you mean?'
            MC @talk 'We plan to set you up in the Bay of Valor.'
            MC @talk 'We think you’ll be more useful to us smuggling there.'
            TAREK 'Tsch! You want me to leave Novaras for some second-rate dock city?'
            MC @talk 'It’s more lucrative there than you imagine.'
            MC @talk "Access to the Port will give you reach to Synmaria and more, only a fool couldn't see the value in that."
            TAREK 'Hmph... We shall see.'
            MC @talk 'And... to help smooth things over, that is why we have brought you Nijah.'
            TAREK '...'
            "Nijah's eyes refused to lift from the floor."
            MC @talk 'To take with you on your travels. A companion for... {i}all of your needs.{/i}'
            'Nijah looked away in disgust as Tarek smiled.'
            TAREK 'I suppose something good has come from this.'
            'Pouring out the cup of wine, I handed it to him.'
            MC @talk 'For the riches yet to come.'
            TAREK 'Well... That sounds like something I might be willing to drink to.'
            'As Tarek held up the cup, he tormentingly remarked to Nijah.'
            TAREK 'I always told you in the end you would be mine Nijah, one way or another.'
            NIJAH '...'
            TAREK 'Friends, drink with me.'
            'Me and Markus shared a nervous glance for a moment.'
            BLACK 'Drink... Fear not...'
            'Tarek stared at us uncertainly, guaging our delay and reaction.'
            TAREK '...Is something wrong friends?'
            MC @talk "Not at all Tarek, we just prefer not to drink on the job ourselves."
            'Feigning as much confidence as I could, I poured me and Markus a cup each.'
            MC "(Fuck fuck fuck, are we actually about to drink poison? By the gods monster if you're-)"
            BLACK 'Trust'
            WHITE 'Us.'
            MC '(Should I?)'
            MC '(So far these things inside of us have not lied before.)'
            MC '(But now they are asking us to trust them and drink literal poison...)'
            menu:
                "I'm not drinking poison!":
                    MC @talk 'Neither of us drink, sorry.'
                    'Tarek looked down at the cup, the swirling red liquid in his drink before his eyes raised and looked deathly towards us.'
                    TAREK '{i}...Deceivers.{/i}'
                    MC @talk '(Shit!)'
                    TAREK 'ASSASSINS! MEN! DRAW YOUR BLADES!'
                    MARKUS 'Well, time for plan B!'
                    jump qst_DamzelDizzt_3_ruckus

                'Trust the dark passenger, drink the poison...':
                    'I sighed, looking to Markus to give a nod of approval as we both gulped down the wine together.'
                    'Tarek waited a few seconds, his eyes looking over to see if we were about to drop dead at any moment.'
                    'Satisfied when we did not, he smiled.'
                    'Tarek gulped the wine down, confident that despite the setback, he would restart his ‘empire’ elsewhere.'
                    'But this time, with Nijah, subservient at his side and warming his bed every night.'
                    'Perhaps even, with access to the dock, he would make riches beyond his wildest dreams.'
                    '...But that dream was short-lived.'
                    'After a few seconds passed by, Tarek stopped smiling.'
                    'With a shaking hand, he dropped the cup to the floor and the wine poured out all over it.'
                    'The two guards who waited behind us drew their blades in a panic but I turned too quickly for them to even unsheathe their blades in time.'
                    scene cg_tarek_dead_off with dissolve
                    $ BlackDiamondLogic().tarekFate = "died"
                    $ QstDamzelInDiztrezz().PlayerAssassinatedTarek = True
                    play sound2 "audio/cfx/transform.ogg"
                    'From my back, two protruding tentacles quickly emerged and slammed their heads against the wall.'
                    'As I severed their heads off, the two corpses slumped down lifelessly against the wall, leaving behind dragging blood trails.'
                    $ LocFlush()
                    show markus_transformed:
                        xcenter 0.5
                    show mc_transformed:
                        xcenter 0.2
                    show nijah:
                        xcenter 0.8
                        xzoom -1.0
                    with dissolve
                    'Nijah, now terrified, kicked away her chair as she jumped away from us, ready to scream in terror.'
                    'I motioned desperately for her to be silent, but there was a wide-eyed terror in her eyes and I knew she might scream any moment.'
                    'Markus quickly rose to his feet, and grabbed her.'
                    'Covering her mouth as he motioned again for her to be quiet.'
                    MARKUS 'If you scream this place will become a bloodbath!'
                    'After a few minues of restless breathing, Nijah slowly began to calm.'
                    MARKUS "You weren't supposed to see that... But we need you to stay calm, can you do that?"
                    'Nijah nodded anxiously as Markus slowly loosened his grip over her mouth.'
                    'Tarek, now writhing in agony on the floor, desperately wheezed as he struggled to breathe.'
                    'His eyes rolled white as his jaw locked and he began to foam at the mouth. He clawed furiously at his throat...'
                    'Tearing through his own neck, the violent convulsions stopped as two bloody trails emerged from both of his eyes and dripped down onto the floor.'
                    'After a few more convulsions, Tarek stopped, blood gurgling out of his mouth.'
                    MC @talk '... Is he dead?'
                    '...I finally asked after a few moments of silence passed.'
                    MARKUS 'He’s seen better days.'
                    NIJAH 'We go, {i}now!{/i}'
                    scene black with dissolve
                    'Both me and Markus nodded and transformed back into our human forms.'
                    "About to leave, I snatched a hefty pouch of gold from Tarek's table."
                    $ PlayerAddItem("gold", RngInt(300, 500))
                    jump qst_DamzelDizzt_3_leavingTarekOffice

        '{image=[ICON.HEART_BROKE]} Offer to sell Nijah.':
            jump qst_DamzelDizzt_3_sellNijah
