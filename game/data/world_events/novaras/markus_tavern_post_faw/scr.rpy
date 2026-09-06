label ev_markus_tavern:
    $ LocSet("novaras_dist_market")
    $ LocFlush()
    "Approaching the tavern, I suddenly caught the scent of a strange aroma, like wildflowers that made me stop and turn to look around."
    BLACK "{i}Mate... A good potential mate is near...{/i}"
    show sophira at center_f with dissolve
    "Looking around, I once again took a deep breath, and my eyes naturally drew the beauty heading in the opposite direction of me."
    "Aristocratic, she wore a beautiful blue dress and bonnet hat that elegantly conveyed a sense of class and sensuality."
    "Her face was soft, with long auburn brown hair that flowed with some of the bluest eyes I'd ever seen."
    hide sophira with easeoutleft
    BLACK '(We should follow her...)'
    MC '(I... No, I have to meet Markus.)'
    show mc at cleft with easeinleft
    MC '(I need to stay focused on things... talk to him first before anything else.)'
    BLACK '(I will keep her scent for as long as I can to track her...)'
    MC '(You can do that?)'
    BLACK '(Of course, there are many things you will have to learn.)'
    MC '(...)'
    hide mc with easeoutright
    $ LocSet("novaras_tavern")
    $ LocFlush()
    show markus at center
    with dissolve
    MARKUS @smile 'Ah! [player_name!t]! There you are...'
    MARKUS 'Over here, I have a table for us.'
    scene black with dissolve
    'Sitting at the table with Markus, we ordered a round of Ale over and sat back talking about the things that had happened.'
    'Markus seemed jovial, elated even with everything going on, grinning merrily as he talked about his plans for the future, whereas I remained much more... {i}reserved.{/i}'
    $ LocFlush()
    show markus at cright_f
    show mc at cleft
    with dissolve
    MARKUS @sad '[player_name!t], why the long face?'
    MARKUS @smile 'This is perfect for us!'
    MARKUS 'All we need to do is write a few speeches, smile and wave at some drunks in a tavern or two and make sure to visit a brothel once or twice in the meanwhile!'
    MC @talk "Somehow, I don't think everything is going to be quite as easy as you think."
    MARKUS @angry 'You over worry.'
    MC @talk "And you don't worry enough."
    MARKUS @angry 'Bah!'
    MC @talk "Markus, we hardly know anything about what's happened to us aside from what we've been told."
    MARKUS "What more do you need to know?"
    MARKUS "They made the rules fairly clear friend, and quite frankly, I'm looking forward to {i}finally{/i} having things easy for a while."
    MC @talk 'Will it be easy though Markus, {i}will it really?{/i}'
    MARKUS "{i}*Sigh*{/i}"
    "Markus pulled a sympathetic face, leaning closer towards me."
    MARKUS @sad "{i}Haven't we been through enough already?{/i}"
    MARKUS "Okay, things didn't exactly work out like we planned but..."
    MARKUS @smile 'This is our chance [player_name!t], we can make something good with this.'
    $ choicemenu = ['a','b']
    menu act1scene8_menu:
        'What about the war?' if 'a' in choicemenu:
            MARKUS 'What about it?'
            MARKUS @angry 'We did our part, we nearly {i}fucking died{/i} doing our    part.'
            MARKUS 'What more can they ask?'
            $ choicemenu.remove('a')
            jump act1scene8_menu
            # loop back
        'We should try do some research into these... {i}things.{/i}' if 'b' in choicemenu:
            MARKUS "I don't think we're going to have much luck there, these... {i}'things'{/i} aren't in any book I've read."
            MARKUS "And it's too much of a risk to talk to someone about all this."
            MARKUS "It only takes one wrong person blabbering and we'll find the inquisitors knocking on our doors."
            'Taking a sip of my drink, I pondered in thought.'
            MC @talk '...That skeleton down in the caverns.'
            MARKUS 'The mage?'
            'Markus leaned forward to whisper the next words.'
            MARKUS '{i}The dark mage?{/i}'
            MC @talk 'The letter said they were excavating those pillars.'
            MARKUS '...So?'
            MC @talk "Don't you remember the big hurry to get us out there?"
            MARKUS '...'
            MC @talk 'Markus, we were sent there to {i}recover{/i} these things.'
            MARKUS 'Well... Mission bloody accomplished I guess.'
            MC @angry "No, idiot! Don't you see?"
            MC @talk 'That means {i}someone{/i} somewhere still knows about these things.'
            MARKUS '...'
            MC @talk "And if they don't assume they were lost during the battle, they'll be looking for them."
            MARKUS @shock "{i}...You think someone's after us?{/i}"
            MC @talk "I don't know, maybe?"
            MC @talk '{i}We were{/i} the only survivors...'
            MC @talk "If I was {i}them,{/i} I'd look for us."
            'Markus seemed to ponder the thought for a moment, and we both were awkwardly silent till Markus finally asked:'
            MARKUS "Alright... Then tell me this, why haven't they already?"
            MC @talk 'Hm?'
            MARKUS @sad "If they know about our 'gifts' and know about us, why haven't we been arrested by inquisitors already?"
            MC @talk 'Good question.'
            MC @sad "I don't know."
            'Markus smirked and sipped his drink.'
            MARKUS @joy "See? You're always over-thinking."
            MARKUS 'That place was all bones and ruin... Whoever set it up is probably just like that mage you found, dead and gone.'
            MC @talk 'Then why the sudden push for us to go there?'
            MARKUS 'Who knows! Maybe someone who knew someone heard there was weapons there or important information.'
            MARKUS 'Maybe they wanted the place retaken for strategic reasons, maybe a hundred other possible reasons!'
            MC @talk '...'
            MARKUS @sad "[player_name!t], don't go chasing shadows."
            MARKUS @smile "Unless we're given a reason to be worried, I'm not going to be."
            $ choicemenu.remove('b')
            jump act1scene8_menu
            #(Loops back to main choice)
        'If you say so.':        
            MARKUS @smile 'See? Everything will work out.'
            MARKUS 'You just need to relax, {i}our{/i} war is over.'
            $ choicemenu = ['a','b']
            menu act1scene8_menu2:
                '...What if we lose though?' if 'a' in choicemenu:
                    MARKUS @sad 'What?'
                    MC @talk 'What if things take a turn for the worst Markus?'
                    MC @talk 'What {i}if{/i} the Demorai push us back and it looks-'
                    MARKUS @sad "That won't happen for years even if it does."
                    MC @talk "But what happens if it does? What if we settle down, have families and those things are clawing at our doors and it's all too late because we did nothing now?"
                    MARKUS @angry "Then we'll fight, or we'll flee when the time comes..."
                    MARKUS "[player_name!t] please, this is all hypotheticals and I'd rather just change the topic..." #loops back to root menu
                    $ choicemenu.remove('a')
                    jump act1scene8_menu2
                'These {i}things{/i} inside of us... They may be the key to winning this war.' if 'b' in choicemenu:
                    MARKUS "Ha!"
                    MARKUS @angry "Thanks but, I just left one battlefield littered with bodies and don't really need to see another."
                    MC @angry 'Markus we might have a chance to actually do something here!'
                    MARKUS 'By the gods man, do you hear yourself?'
                    MARKUS @sad "If Newheart couldn't win the damn thing what are we going to do?"
                    MC @sad 'What about Kiara? What about Duprey?'
                    MC @sad 'So many people have lost their lives in this war Markus, how many more are going to die needlessly?'
                    MARKUS @angry 'How is that {i}our{/i} responsibility?'
                    MARKUS @angry "We {i}did{/i} our damn part, by the hells we're {i}STILL{/i} doing our part rallying people!"
                    MC @talk "...Father's still in danger while this war continues."
                    'Markus paused when he heard my comment, sipping at his drink before answering sheepishly:'
                    MARKUS @sad 'Yes... But...'
                    MARKUS @sad '[player_name!t], your father will be home soon though, right?'
                    MC @talk '{i}Hopefully...{/i}'
                    MARKUS '[player_name!t] please...'
                    MARKUS 'Let someone else fight these accursed battles...'
                    MARKUS 'Playing hero was never part of the plan.' #loops back to main menu
                    $ choicemenu.remove('b')
                    jump act1scene8_menu2
                "You're right, I'm done thinking about the war.":                              
                    MARKUS @smile "That's the spirit!"
                    MARKUS "Let's just {i}focus on the plan{/i} [player_name!t], we've got a second chance to maybe have a good easy life again, let's take it."           
                    MARKUS @joy "Now come on, let's enjoy ourselves a bit."
                    MARKUS @smile "Have some 'fun,' you remember fun?"
                    MC @smile 'Alright, fine.'
                    MC @smile 'But the next round is on you.'
                    MARKUS @smile 'Deal!' #Cuts to 'a few drinks later...'
                'Alright, if you say so...':
                    MARKUS @smile 'Of course I say so!'
                    MARKUS @joy "Now come on, let's enjoy ourselves a bit."
                    MARKUS @smile "Have some {i}fun{/i}, you remember fun?"
                    MC @smile 'Alright, fine.'
                    MC @smile 'But the next round is on you.'
                    MARKUS @smile 'Deal!' #Cuts to 'a few rounds later...'

    scene black with dissolve
    $ TimeAdvBy(TIME_05H)
    "A few drinks later..."
    $ TimeAdvBy(TIME_05H)
    # Text appears on screen 'A few drinks later...'
    $ LocFlush()
    show markus at cright_f 
    show mc at cleft
    with dissolve
    MARKUS @smile "So look, I'm not saying elven pussy tastes different-"
    MC @smile "That's exactly what you're saying!"
    MARKUS @smile "That's what my friend Darlan's cousin says!"
    MC @talk 'Has he even met an elf?'
    MARKUS 'Well, he went out with Brianus.'
    MC @surprised 'Brianus is human!'
    MC @smile 'She went to our class!'
    MARKUS @smile "Yeah but she's got like, stupidly large ears so, what's the difference?"
    'Laughing in semi-drunken stupors as we tried to swallow down our ales, I suddenly smelt another strange aroma...'
    'This time, almost like... {i}honey?{/i}'
    'I quickly found myself frantically looking around for the source while my dark passengers animal like desire drew me to it.'
    'Looking over, the barmaid, a woman in her early thirties slowly approached, leaning forward with a smile on her face as she wiped up some of the spilled drink on our table with a rag.'
    show shay:
        xcenter 0.5
    with dissolve
    'My eyes hungrily looked her up and down and I once again felt the pangs of desire, red hot coursing through me like burning coal slithering its way through my veins.'
    BLACK '{i}(This one smells good too...){/i}'
    BLACK '{i}(This one... She is ripe).{/i}'
    'I swallowed hard, pushing back the darkness as I looked her over her ginger hair curled on the ends as her large bosom hung in front of me from where she was leaning forward.'
    'Her cheeks and large breasts were freckled, and I noticed as she kept wiping, her eyes would look to meet mine occasionally.'
    'It was hard not to notice her curvaceous body hidden by the rags she wore.'
    'I envisioned her naked, sweaty, panting as I-'
    'I breathed hard once again, pushing back the thoughts.'
    UNKNOWN 'You boys are having a good time I see!'
    MARKUS @smile 'It would be better if you joined us!'
    UNKNOWN 'Mmm, but then would serve the others their drinks?'
    MARKUS "I haven't seen you around here before, what's your name?"
    UNKNOWN 'Shay.'

    MARKUS "I'm Markus, and this is my friend."
    MC @talk '[player_name!t].'
    SHAY @smile 'Nice to meet you both.'
    MARKUS 'I thought Old man Gomar run this place?'
    SHAY @talk 'He and his wife left for Inma about two months ago.'
    SHAY @talk 'Me and my husband Varan bought the place and took over.'
    "When I heard the word 'husband' escape her lips, I felt my heart sink slightly, but it was quickly overcome by the burning desires of the thing inside me."
    MC @surprised "Old man Gomar's gone?"
    SHAY @think "Don't worry love."
    "A sly, sultry smile crawled across her lips."
    SHAY @smile2 "Think you'll miss him much?"
    MC @smile "I don't know... I think I quite like the change."
    'Shay laughed, taking our empties glasses onto a tray and standing upright.'
    SHAY @talk "Now if you'll excuse me, I best get back to some work."
    hide shay with dissolve
    'As Shay sauntered off towards another table, we watched as she leaned forward to pick up some glasses from the opposing table, and the outline of her round ass became visibly pressed against the fabric.'
    MARKUS @smile 'By the gods...'
    MARKUS @smile "I wouldn't complain waking up to fuck an ass like that every day."
    MC @smile 'Mmm...'
    MARKUS "She has her eye on you y'know."
    MC @surprised 'What?'
    MARKUS @smile "I mean don't get me wrong, if she looked too long at me she knew her marriage would be doomed."
    MARKUS 'But I saw the way she kept looking at you.'
    MC @surprised "She's married!"
    MARKUS 'So?'
    MARKUS 'You gotta start thinking about getting some girls on the side friend...'
    MARKUS "What if you don't have the coin for the brothel?"
    MARKUS "Gonna risk your life in a fight every night just to keep your thing happy?"
    MC '...'
    MARKUS @smile 'So, you gonna go for her?'
    MC @talk "...I'll think on it."
    MARKUS @smile "Okay [player_name!t], let's roll."
    MC "But I haven't finished my drink yet!"
    MARKUS @smile "Come on, there's only so much time you can spend drinking."
    MARKUS @smile "We've got the whole world to take on!"
    MC "You're drunk!"
    MARKUS "So what? Doesn't change the fact!"
    "I looked at the half-finished drink drink and nodded:"
    MC "You know what, you're right. Let's go."
    scene black with dissolve
    "As we walked out of the tavern, I thought that perhaps Markus was right."
    "Perhaps the worst truly was behind us."
    "But some part of me could not shake the feeling that this was only the beginning."
    $ LocSet("novaras_dist_market")
    $ QstComplete(EventNovarasMarkusTavernPostFaw)
    $ LocEnter()