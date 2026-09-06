label ev_Markus_tavern_postTwoEmps:
    $ LocSet("novaras_tavern")
    $ LocFlush()
    show markus at cright_f
    with dissolve
    show mc at cleft with easeinleft
    with dissolve
    MC @talk "There you are!"
    MARKUS "Ahh, sorry about that earlier."
    MC @talk "What was that?"
    'Markus became somewhat flustered as he answered.'
    MARKUS "I uh, needed to get {i}the thing we share{/i} under control..."
    MC @talk "Huh? Have you not-"
    MARKUS "Yes, don't worry so much."
    MARKUS "It's fine now."
    MARKUS "Anyway, how did it go after with Officer Lukkan?"
    MC @talk "Well... About that..."
    call center_text(_("Later...")) from _call_center_text
    $ LocFlush()
    show markus at right_f
    show mc at left
    with dissolve
    MARKUS @shock "...Y-You're joking, right?"
    "Markus' confusion and shock soon turned to frustration, and then finally anger."
    MARKUS @angry "Those fucking bastards!"
    MARKUS @sad "All these years..."
    MARKUS @angry "Nothing but lies!"
    MC @talk "We've always known we were being lied to about certain things."
    MARKUS @angry "Not this! Not fucking this!"
    MARKUS "Surely you can't agree with what they've done?"
    menu:
        'Maybe it was for the best they lied?':
            MARKUS @angry "What? How can you say that!"
            MC @talk "What does it really change?"
            MC @talk "If the Demorai really aren't willing to stop, should people really know?"
            MC @talk "I mean, doesn't it make it {i}easier{/i} to fight them thinking they really are just savage beasts?"
            MC @talk "Do {i}you{/i} really want to be thinking every time we have fight one of those things about who they are?"
            MC @talk "{i}Do they have families? Children and loved ones waiting at home like us? Do they mourn when their brothers and sisters fall?{/i}"
            MC @talk "Are those the kind of questions you really want to be putting in people's heads during a war?"
            MARKUS @angry "We've been lied to since we were children, [player_name!t]."
            MARKUS @angry "Who knows what else they've been keeping from us."
        "You're right.":
            MC @talk "That Demorai... That girl back in those ruins, Sypha."
            if QstTwoEmperors().tookSyphaHelp:
                MC @talk "She led us out safely like she said she would."
                MC @talk "AND she showed a willingness to work together... That means there has to be hope for other Demorai to do the same."
            else:
                MC @talk "She tried to help us and... We didn't listen."
                MC @talk "{i}She was telling the truth.{/i}"
            MC @talk "If we can't keep our minds open at all to even the {i}possibility{/i} of negotiations or peace, we rule them out entirely before they have a chance."
            MARKUS "So, you {i}do{/i} think there's a chance for peace talks?"
            MC @talk "Not with any of the current leadership on both sides it seems..."
            MC @talk "But there are parties {i}within both camps{/i} who probably would be willing to talk."
            MARKUS "Hmm... I'm mad about being lied to, but-"
            MARKUS "I'm not so sure if I like the idea of negotiations with those {i}'things'{/i} after everything they've done."
    MARKUS '{i}*Sigh*{/i}'
    MARKUS "I guess none of this really matters though, right?"
    MARKUS "I mean, we're just two nobodies from the Adventurers Guild, so..."
    MARKUS "Its not like either of us are going to be making a real difference anytime soon."
    "I couldn't help but feel slightly depressed at Markus' comment, he was of course, correct."
    "Even with all this knowledge and revelations, what difference could we really make?"
    "Even with our dark gifts, there was a sense of real powerlessness that even after learning all we had, it changed nothing."
    MC @sad "Yeah... I guess you're right."
    MARKUS @smile "...Hey, wanna get drunk and forget all this?"
    MC @talk "{i}Absolutely.{/i}"
    scene black with dissolve
    'After a couple drinks, me and Markus managed to push what had learned aside as we enjoyed having a merry conversation while reminiscing once again.'
    'The Tavern by now had begun to pick up, and soon the place was heaving with other patrons like us.'
    $ LocFlush()
    show markus at right_f
    show mc at left
    with dissolve
    MARKUS @smile "Haha! I almost forgot about that one!"
    MARKUS @smile "Gods, whatever happened to Joana Tepeha?"
    MARKUS @smile "Did those two actually marry in the end?"
    MC @smile "I'm pretty sure the engagement was called off after {i}THAT{/i} and she headed off with her family to Borusmark in Skarshire."
    show adara at center_f with dissolve
    ADARA @smile "I see you two are enjoying yourselves."
    MARKUS @joy "Adara!"
    MARKUS @smile "Where have you been?"
    ADARA @talk "Been busy between working and looking after father."
    ADARA @talk "Are you two celebrating something?"
    MC @talk "Uhh, not quite."
    MC @talk "Just getting drunk after a... {i}difficult{/i} quest."
    ADARA @sad "O-Oh... I'll leave you both be."
    ADARA @talk "You probably don't want me ruining your night."
    MARKUS @smile "Nonsense, Adara!"
    MARKUS "I'm heading up to get another round, would you like one?"
    ADARA @talk "Umm, perhaps just {i}one{/i} drink won't hurt."
    MARKUS @smile "That's the spirit! I'll be right back!"
    hide markus with easeoutright
    'As Markus did his best to fight his way over to order some drinks, Adara moved closer to me.'
    show adara at cleft_f with easeinright
    ADARA @sad "Are you okay?"
    MC @talk "I'm fine, Adara."
    MC @smile "It's good to see you."
    ADARA @sad "If... If something happened and you want to talk about it."
    ADARA @sad "We can go somewhere private if you want..."
    MC @sad 'No, Adara... I-'
    show cg_kiara_mask onlayer characters with dissolve:
        xcenter 0.8
        yoffset 380
        zoom 0.4
    'Suddenly, between the heaving crowds, something caught my eye.'
    'A robed figure amongst them, staring right at me.'
    "Sypha's words rung through me ear of her sending an 'agent' to make contact with us, and I rose quickly to my feet, much to Adara's surprise."
    hide cg_kiara_mask onlayer characters with dissolve
    MC @talk "Adara, I'll be right back." 
    ADARA @shock "Wait! [player_name!t]!"
    hide mc with easeoutright
    scene black with dissolve
    'As I pushed my way through the crowds to make my way towards them, the robed figure slipped outside into the cool night air.'
    ADARA @sad '[player_name!t]...'
    jump ev_Markus_tavern_postTwoEmps_2