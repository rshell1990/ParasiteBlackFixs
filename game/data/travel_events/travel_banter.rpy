########## label records
init python:
    # all "map event" banter labels
    BanterLabels_Map = {
        "travelmodebanter_map_elena_mc_1",
        "travelmodebanter_map_elena_mc_2",
        "travelmodebanter_map_elena_mc_3_romance",

        "travelmodebanter_map_elena_markus_1",
        "travelmodebanter_map_elena_markus_2",
        "travelmodebanter_map_elena_markus_3",

        "travelmodebanter_map_myu_1",
        "travelmodebanter_map_myu_2",

        "travelmodebanter_map_myu_elena_1",
        "travelmodebanter_map_myu_elena_2",
        "travelmodebanter_map_myu_elena_3",

        "travelmodebanter_map_myu_markus_1",
        "travelmodebanter_map_myu_markus_2",
        "travelmodebanter_map_myu_markus_3",

        # you can just add more labels here & to the condition check, it should just work
        # check function: TravelModeBanter_CheckBanterLabelConditions
    }
    # all "camp event" banter labels
    BanterLabels_Camp = {
        "travelmodebanter_camp_myu_markus"
    }

########## actual labels below
# ELENA and MC - Travel Dialogue 1
label travelmodebanter_map_elena_mc_1:
    show elena at cright with easeinleft
    show mc at cleft with easeinleft
    show elena at blurin, cright_f
    ELENA @talk "Have you ever thought about leaving Alderay?"
    MC @think "Where'd that come from?"
    ELENA @talk "Just... curiosity."
    ELENA @talk "Growing up at Thornfalls, I dreamt of faraway places and adventures."
    ELENA @smile "It seems silly now, but... I still think about the places I want to see."
    menu:
        "Find me a ship and we'll leave now.":
            ELENA @shock "Just like that?"
            MC @smile "There's a whole world out there."
            ELENA @smile "And would there be room for one more?"
            MC @smile2 "I'm sure I could fit you in."
            ELENA @smile "I must admit, I'm surprised."
            ELENA @smile "Markus told me all you two wanted was a quiet life behind palace walls."
            MC @talk "Funny, isn't it?"
            MC @talk "That dream started feeling more like a cage after... everything."
            ELENA @smile "No. Not strange at all. Not to me."
        "I can't say I've thought about it.":
            ELENA @talk "Ahh, you seem more like a homebody."
            MC @think "Oh?"
            ELENA @grumpy "You and Markus dreamed of royal service, didn't you?"
            ELENA @smile "Not exactly an adventurous life."
            MC @talk "Is wanting a quiet life so wrong?"
            ELENA @smile "Not at all."
            ELENA @smile "It's your life to live."
            MC @think "{i}... And when this war is one day over.{/i}"
            MC @think "{i}Is it a life you'd want to be a part of?{/i}"
            ELENA @lewd "L-Let's leave that question for another day."
    show elena at blurin, cright
    hide elena with easeoutright
    hide mc with easeoutright
    return

# ELENA and MC - Travel Dialogue 2 
label travelmodebanter_map_elena_mc_2:
    show mc at cright with easeinleft
    show elena at cleft with easeinleft
    ELENA @grumpy "...Does it hurt?"
    show mc at blurin, cright_f
    MC @think "What?"
    ELENA @grumpy "When you change into that thing... does it hurt?"
    MC @talk "It... did. At first."
    show mc at blurin, cright
    MC @talk "It was agony."
    MC @talk "But it gets easier every time."
    show mc at blurin, cright_f
    MC @talk "Why do you ask?"
    ELENA @sad "Just worried about you."
    ELENA @talk "How are you holding up? After everything that's happened so fast..."
    menu:
        "I feel great.":
            ELENA @shock "Really? I'm surprised... most people would struggle."
            MC @talk "There are doubts, sure. But we can actually change things now."
            MC @smile "Before the gift, I felt powerless. Like my life wasn't mine."
            MC @smile "Now? It's like we finally have... {i}hope.{/i}"
            ELENA @smile "You're starting to sound like a hero from the old tales."
            MC @smile "Let's not go that far."
            ELENA @smile "Come. Let's keep moving."
        "As fine as I can be, I suppose.":
            ELENA @sad "That's... a relief. You can talk to me, you know."
            MC @smile "That means more than you think."
            ELENA @smile "Come on. Let's keep moving."
        "I still have nightmares...":
            ELENA @sad "I'm here if you want to talk."
            ELENA @sad "It weighs heavy, doesn't it? Memories that won't let go..."
            MC @sad "..."
            ELENA @sad "A-Anyway! I just wanted you to know you're not alone."
            ELENA @talk "I'm here if you need me."
            MC @smile "Thank you, Elena."
            ELENA @smile "Come. Let's keep going."
    hide elena with easeoutright
    show mc at blurin, cright
    hide mc with easeoutright
    return

# ELENA and MC - Travel Dialogue 3 (Romance - if bath scene triggered) 
# ^ scratch that bath condition, just if "lover"
label travelmodebanter_map_elena_mc_3_romance:
    show mc at cleft with easeinleft
    "While walking, something soft brushed against my side."
    show elena at center with easeinleft
    "Elena passed me with a coy smile and a soft hum."
    ELENA @smile "{i}*Happy humming*{/i}"
    MC @smile "Someone's in a good mood."
    show elena at blurin, center_f
    ELENA @smile "Of course. The weather's pleasant, the air is clean..."
    "She glanced back, her sultry eyes dancing."
    ELENA @smile "And {i}the view{/i} is quite nice, too."
    MC @smile "The view, huh?"
    "Her tail brushed me again playfully as she walked ahead."
    ELENA @smile "Yes. It's been on my mind a lot lately."
    show elena at blurin, center
    hide elena with easeoutright
    MC @smile "(Cute.)"
    return

# Elena and Markus - 1 (while traveling)
label travelmodebanter_map_elena_markus_1:
    show elena at cright with easeinleft
    show markus at cleft with easeinleft
    MARKUS @think "So, you're a lady, then?"
    show elena at blurin, cright_f
    ELENA @talk "Yes, I do indeed belong to the female gender."
    MARKUS @angry "You know that wasn't what I was talking about!"
    MARKUS @talk "I mean, you're a *lady* lady. Like, you grew up in some huge estate house."
    ELENA @smile "Yes. The ones with the very long tables and lots of food on them."
    ELENA @smile "Are you going somewhere with this?"
    MARKUS @talk "Sensitive much?"
    show elena at blurin, cright
    ELENA @talk "I can assure you, manor house or not, my time at the Thornfalls was... difficult."
    MARKUS @think "I find that hard to believe."
    MARKUS @think "Did you ever have to worry about where your next meal would come from?"
    MARKUS @think "Or constantly wonder when, not if, the next loved one would be taken by this infernal war?"
    ELENA @angry "No..."
    show elena at blurin, cright_f
    ELENA @angry "I just spent every night living in fear."
    ELENA @angry "Let me tell you something, Markus."
    ELENA @angry "It's one kind of hell to starve... it's another entirely to wonder if every meal you're served will be your last."
    show elena at blurin, cright
    hide elena with easeoutright
    show markus at center with easeinleft
    return

# Elena and Markus - 2 (while traveling)
label travelmodebanter_map_elena_markus_2:
    show elena at cright with easeinleft
    show markus at cleft with easeinleft
    MARKUS @talk "Tell me, Elena."
    show elena at blurin, cright_f
    MARKUS @talk "You must have spent some time traveling around before meeting us."
    MARKUS @smile "Got any interesting stories to tell?"
    ELENA @grumpy "...A while back, while I was in Newyark, I heard about a 'wolf woman' and naturally, my interest was piqued."
    ELENA @talk "It didn't sound like any kind of Katai, so I thought perhaps I might finally find another of my kind."
    MARKUS @think "What did you find?"
    ELENA @shock "It was a woman who had made some kind of... fur suit from different pelts of wolves."
    show elena at shake
    ELENA @shock "She was running around on stage pretending to be a wolf!"
    ELENA @shock "Can you imagine people doing such a strange thing?"
    MARKUS @think "...Too much salt in the air from the sea."
    MARKUS @think "That's why all those Newyark folk are so strange."
    show elena at blurin, cright
    hide elena with easeoutright
    hide markus with easeoutright
    return

# Elena and Markus - 3 (while traveling)
label travelmodebanter_map_elena_markus_3:
    show markus at cright with easeinleft
    show elena at cleft with easeinleft
    ELENA @smile "Markus, I'm curious about something..."
    show markus at blurin, cright_f
    MARKUS @talk "Ask away."
    ELENA @talk "I'm aware of [player_name!t]'s... umm, {i}paramours and dalliances.{/i}"
    ELENA @grumpy "But I never see you with anyone."
    ELENA @grumpy "Isn't your affliction the same?"
    MARKUS @smile "Ahh..."
    MARKUS @smile "Let's just say there isn't a brothel house in Novaras that probably doesn't know who my favorites are now."
    ELENA @grumpy "Doesn't that get a little lonely?"
    MARKUS @think "I think it's easier this way. For now, at least."
    MARKUS @think "The last thing I'd want is to hurt someone close to me having to deal with... {i}this.{/i}"
    MARKUS @think "I mean, can you imagine loving someone and having to accept that if you're not there, they {i}need{/i} to sleep with someone, or they—"
    ELENA @sad "..."
    MARKUS @shock "T-That's just my feelings, of course!"
    MARKUS @shock "I'm sure, umm, there are plenty of people who can make that sort of thing work if they truly loved the person!"
    ELENA @sad "R-Right."
    show markus at blurin, cright
    hide markus with easeoutright
    hide elena with easeoutright
    return

# MYU and MC - whilst travelling - 1
label travelmodebanter_map_myu_1:
    show mc at cright with easeinleft
    show myu at cleft with easeinleft
    MYU @talk "Q-Questions!"
    show mc at blurin, cright_f
    MC @think "Hmm?"
    MYU @talk "Myu has questions!"
    MC @smile "Ask away, Myu."
    MYU @talk "Is it different being solid?"
    MC @think "Uh... what?"
    MYU @talk "Myu can change. You can only change a little."
    MC @think "I'm not quite sure I get where you're going with this."
    MC @think "I mean... I suppose that's true."
    MC @think "But most people can't change at all."
    MYU @sad "N-No, Myu means..."
    MYU @sad "Myu took this form, but Myu can take any form."
    MYU @sad "But... Myu only take this form, who is Myu really?"
    MYU @sad "{b}Myu feels... Like she has a thousand faces.{/b}"
    MYU @sad "{b}But none are her own.{/b}"
    MC @sad "... Myu."
    menu:
        "I can't tell you who to be. Only you can decide that.":
            MYU @think "When will Myu know who she really is?"
            MC @smile "People spend their whole lives figuring that out. But you're not alone."
            MC @smile "But, the journey doesn't have to be a scary one."
            MC @smile "The people we care most about can help us figure out a few things along the way."
            MYU @talk "Myu... thinks she understands."
        "You're a slimelark, Myu. That's who you are.":
            MYU @sad "Is that all I am...?"
            MC @talk "Who you are and what you are aren't the same."
            "Myu looked mildly puzzled by my answer."
            MC @smile "Give it some thought."
            MYU @think "Myu will... think-y."
    show mc at blurin, cright
    hide mc with easeoutright
    show myu at center with easeinleft
    return

# MC and Myu – while traveling – 2
label travelmodebanter_map_myu_2:
    show mc at cright with easeinleft
    show myu at cleft with easeinleft
    MYU @talk "Is Myu a pet?"
    show mc at blurin, cright_f
    MC @think "What?"
    MYU @talk "Is Myu what you call a pet?"
    menu:
        "Yes, you're a pet.":
            MYU @smile "Yayyy! Does that mean I get lots of headpats?"
            MC @think "H-Huh?"
            MYU @talk "Humans always give headpats to the pets they have."
            MYU @talk "So... when does Myu get headpats?"
            MC @surprised "..."
            MC @smile "Myu, you can have as many headpats as you like."
            MYU @smile "Myu will keep you to your promise!"
        "No, you're not a pet.":
            MYU @think "Then... what is Myu?"
            MC @smile "You're just Myu... Myu."
            MYU @think "{i}*Pouts*{/i}"
            MYU @smile "So... Myu is... friend?"
            MC @smile "And more, Myu."
            MYU @smile "Ha! Myu has friends!"
            MYU @smile "The other slimelarks would be so jealous!"
    hide myu with easeoutright
    show mc at blurin, cright
    hide mc with easeoutright
    return

# MYU and ELENA - whilst travelling - 1
label travelmodebanter_map_myu_elena_1:
    show myu at cright with easeinleft
    show elena at cleft with easeinleft    
    ELENA @talk "Are you still keeping up with your reading studies, Myu?"
    show myu at blurin, cright_f
    MYU @smile "Yes!"
    ELENA @smile "Good, shall I help you read more of that book you like tonight?"
    show myu at nod
    MYU @smile "Myu!"
    ELENA @grumpy "Which one was it again?"
    MYU @smile "{i}The silver rose of Newyark{/i}"
    ELENA @smile "Ahh, that one."
    ELENA @smile "I must admit, it's quite the advanced read for you."
    ELENA @grumpy "Are you sure you understand everything that's going on in the story?"
    MYU @smile "Myu, likes to skip ahead to the sex scenes!"
    show elena at shake
    ELENA @shock "I... One day you and I are going to sit down and talk about a few things."
    hide elena with easeoutright
    show myu at blurin, cright
    MYU @think "Myu?"
    hide myu with easeoutright
    return

# MYU and ELENA - whilst travelling - 2
label travelmodebanter_map_myu_elena_2:
    show myu at cright with easeinleft
    show elena at cleft with easeinleft
    ELENA @talk "Still reading that book?"
    show myu at blurin, cright_f
    MYU @sad "Myu stopped."
    ELENA @sad "Why?"
    MYU @sad "The man she loved died."
    MYU @sad "Now she marries the friend."
    MYU @sad "But the friend is boring."
    MYU @angry "Myu doesn't like."
    ELENA @sad "Maybe she'll learn to love him."
    show myu at shake
    MYU @angry "No! That's not good enough!"
    ELENA @sad "Sometimes life doesn't have happy endings."
    ELENA @sad "Sometimes, it's more about making the best of the life you have."
    "Myu's body glowed ominously, her form distorting for a brief moment."
    hide myu
    show cg_myu_monster at cright_f
    with flash
    MYU_RED "Myu will have happy ending with ALL her friends!" 
    show elena at shake
    ELENA @shock "M-MYU!"
    hide cg_myu_monster
    show myu at cright_f
    with dissolve
    "She shifted back quickly, shrinking with shame."
    MYU @sad "Myu... needs alone time."
    show myu at blurin, cright
    hide myu with easeoutright
    show elena at center with ease
    ELENA @shock "What in the seven hells was that just now...?"
    return

# ELENA and MYU - whilst travelling - 3
label travelmodebanter_map_myu_elena_3:
    show elena at cright with easeinleft
    show myu at cleft with easeinleft
    MYU @smile "MYU!"
    show elena at blurin, cright_f
    ELENA @grumpy "Yes, Myu?"
    MYU @smile "Myu wants to buy dresses!"
    ELENA @shock "Huh? What brought that on?"
    MYU @smile "Myu saw pretty dresses! The kind that made men stare!"
    ELENA @grumpy "You mean the ones at the... ahem, 'evening establishments'?"
    MYU @smile "Yes! Very pretty!"
    ELENA @lewd "How about first We get you something... more appropriate."
    MYU @smile "Yayyy!"
    show elena at blurin, cright
    hide elena with easeoutright
    hide myu with easeoutright
    return

# Myu and Markus - 1 (while traveling)
label travelmodebanter_map_myu_markus_1:
    show myu at cright with easeinright
    show markus at cleft with easeinleft
    MARKUS @think "...Uhh, Myu, isn't it?"
    show myu at blurin, cright_f
    MYU @think "Myu?"
    MARKUS @think "Look, I'm not exactly a prude, but do you think you could do something about your... Umm..."
    MYU @think "...?"
    MARKUS @shock "...By the gods, girl, you're literally walking around with your tits hanging out!"
    MYU @think "..."
    MARKUS @talk "Your tits! Can't you put on some clothes or... or do something about them?!"
    MYU @smile "Myu!"
    hide myu
    show cg_myu_bimbo at cright_f
    with dissolve
    MYU @smile "Hmm!"
    show markus at shake
    MARKUS @shock "T-THAT WASN'T WHAT I MEANT AT ALL!"
    MYU @smile "[player_name!t] like!"
    MARKUS @shock "I-I'm sure he does!"
    MARKUS @talk "Just uhh, keep that little trick just between you and him, alright?"
    hide markus with easeoutright
    show cg_myu_bimbo at blurin, cright
    MYU @smile "Myu!"
    hide cg_myu_bimbo with easeoutright
    return

# Myu and Markus - 2 (while traveling)
label travelmodebanter_map_myu_markus_2:
    show myu at cright with easeinright
    show markus at cleft with easeinleft
    MARKUS @talk "Myu, I have a curious question for you."
    show myu at blurin, cright_f
    MYU @smile "Myu?"
    MARKUS @sad "Do you ever... you know, miss spending time with your own people?"
    MYU @think "Myu... is with own people?"
    MARKUS @sad "R-Right. I meant other slimelarks like yourself though."
    MYU @talk "...If no food to hunt, sometimes mother tried to eat me instead to feed the others."
    MARKUS @shock "...Well, that settles that then, I guess."
    hide markus with easeoutright
    show myu at blurin, cright
    MYU @think "...Myu?"
    hide myu with easeoutright
    return

# Myu and Markus - 3 (while traveling)
label travelmodebanter_map_myu_markus_3:
    show myu at cright with easeinright
    show markus at cleft with easeinleft
    MARKUS @talk "So, I'm curious, Myu."
    show myu at blurin, cright_f
    MARKUS @talk "You've spent some time now learning things—do you have any thoughts on the Emperor? The war?"
    MARKUS @talk "I'm curious what a slimelark thinks of what's going on..."
    MYU @think "..."
    MYU @smile "You're funny."
    MARKUS @talk "*Sigh* I guess that answers—"
    MYU @smile "Myu think the men in the castle are like mother."
    MARKUS @think "Wait, what?"
    MYU @talk "Mother would leave the weak to hunger, and take food for herself."
    MYU @talk "We knew mother did it because she had to."
    MYU @sad "...But now Myu think-y more, Myu realize mother never went hungry for long, and always ate first."
    MYU @talk "It was always everyone else who had to deal with being hungry all the time..."
    MARKUS @shock "That is... surprisingly insightful of you, Myu."
    show myu at shake
    MYU @smile "So, we should eat the people in the castle!"
    MARKUS @smile "M-Maybe let's revisit sometime who it is and isn't fine for you to eat."
    hide markus with easeoutright
    show myu at blurin, cright
    hide myu with easeoutright
    return

### camp
label travelmodebanter_camp_myu_markus:
    show myu at center with easeinleft
    MYU @smile "{i}*Nom* *Nom*{/i}"
    show markus at cleft with easeinleft
    MARKUS @think "...Myu, what are you eating?"
    show myu at cright with ease
    MYU @think "..."
    MYU "{i}*Chews faster*{/i}"
    hide myu
    hide markus
    with easeoutright
    #"They both dart off-screen."
    MARKUS "Myu! Open your mouth!"
    MARKUS "MYU!"
    return
