####### variant scene visiting Chanyi/Anya in the night. 
# 30% chance this scene triggers after returning to the Faymore Estate 
# after a bootycall request INSTEAD of the default.
label rom_faymore_girls_balcony:
    show mc at center with easeinleft
    "No sooner had I entered, I noticed the strange absence of servants."
    MC @think "Hello?"
    MC @talk "Is anyone—"
    show chanyi at cleft with easeinleft
    CHANYI @laugh "Ah! There you are!"
    show mc at blurin, cright_f with ease
    CHANYI @talk "There's been a slight change of plans."
    CHANYI @talk "We have some business to attend to, so our usual passion-fueled affair will have to wait."
    show anya at left with easeinleft
    "Anya steps forward, gently nudging at Chanyi as her eyes remain glued onto me."
    CHANYI @laugh "But we did have time for something a bit quicker and perhaps more..."
    CHANYI @lewd "Risky, if you're interested."
    MC @smile "What's the plan?"
    "Anya suddenly interjects, almost too excited at the prospect as she says gleefully,"
    ANYA @lewd "Bend us over the balcony and fuck us before the servants see us!"
    MC @think "Now?"
    CHANYI @talk "We gave the servants still awake some busy work."
    "The two women smirk as they slowly undo their dresses."
    ANYA @lewd "Don't keep us waiting..."
    $ tmpvar = {}
    menu:
        "Rip off their clothes and carry them upstairs.":
            $ tmpvar["clothes"] = "naked"
            "I didn't wait, choosing to pull off what little they wore."
            "Chanyi gasped, seemingly ready to ask me what I thought I was doing."
            "Before she could finish the thought, I flung both women over my shoulders."
        "Carry them both upstairs as they are.":
            $ tmpvar["clothes"] = "ling"
            "I wasted no time, throwing both women over my shoulders as they squirmed."
    #both variants continued
    label replay_faymore_balcony:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    ANYA "Eeeeep!"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_1
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_1
    with dissolve
    $ Pause()
    "There at the stairs, both women bent over the balcony, waving their asses towards me as they looked back expectantly."
    "They didn't need to wait long."
    "Carefully, I wedged my cock between her ass cheeks, beginning to rub against Chanyi as Anya watched excitedly."
    CHANYI "Oh? Me first?"
    ANYA "C-Chanyi..."
    ANYA "It's driving me crazy to think that thing is going to be inside you in a minute."
    "Chanyi grinned towards Anya, gently wiggling her butt to tease my cock."
    CHANYI "Perhaps he shouldn't fuck you at all."
    CHANYI "Perhaps he'd just prefer my tighter, wetter pussy this evening."
    CHANYI "While you just watch."
    ANYA "C-Chanyi!"
    "Anya bit down on her lower lip, watching in excitement."
    MC "Are you ready?"
    CHANYI "Do it."
    CHANYI "I want to feel that big, fat cock inside me while my silly wife wishes it was in {i}her{/i} instead."
    $ PlaySexFx(audio.forgean_075, 1)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_2
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_2
    with dissolve
    $ Pause()
    "I didn't wait, sliding my member into her tight, hot pussy as she groaned."
    CHANYI "Oooooh...!"
    CHANYI "Are you watching, Anya?"
    CHANYI "Are you watching his big cock stretch me out?"
    ANYA "M-Mhmmm! Yes!"
    "Chanyi squeezed instinctively around me."
    "I couldn't tell what she was enjoying more, my cock..."
    "Or teasing and tormenting her wife, who seemed to be almost drooling in excitement at the sight."
    CHANYI "Fufu, do you think he prefers my holes to yours?"
    ANYA "A-Ahh!"
    CHANYI "Say it."
    CHANYI "Say it or I'll have him stop."
    ANYA "Y-Yes! Mhmffghh! He no doubt prefers your tight holes to mine!"
    ANYA "I'm just a worthless, cheap whore compared to you!"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_3
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_3
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_3
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_3
    with dissolve
    $ Pause()
    "Chanyi grinned, pushing her ass back onto me to speed things up."
    CHANYI "Fuck me faster."
    CHANYI "Harder!"
    CHANYI "HARDER!"
    "I did as asked, slamming into her as she tightened around me."
    "A bright red Anya watched, transfixed, looking like she might faint from how worked up she was."
    ANYA "G-Gods, Chanyi..."
    ANYA "I don't know why it turns me on so much watching you get fucked like this."
    "Anya bit her lip in excitement as I continued to fuck her wife."
    ANYA "Maybe it's because you swear down you only like woman? Fufu..."
    CHANYI "Ah! AH! AH!"
    CHANYI "You just - Mmfgh! Have a fetish for seein me - AHH!"
    CHANYI "Get broken in by cock!"
    CHANYI "Oh fuckkkk!"
    CHANYI "That's it!"
    CHANYI "D-Don't stop!"
    CHANYI "Don't you dare fucking stop!"
    "I continued to pound away at Chanyi, the sounds of her ass being clapped echoed through the halls with her moans."
    ANYA "{i}*Huff*{/i} The servants could walk in any time, ha-ha!"
    ANYA "They could see their mistress cuckolded and never look at me the same again!"
    "Anya squirmed in excitement as Chanyi's breasts bounced wildly."
    CHANYI "S-So close...!"
    ANYA "C-Cum in her! CUM IN HER!"
    CHANYI "Wait! Anya! We—"

    $ PlaySexFx(audio.forgean_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_cum_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_cum_1
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_cum_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_cum_1
    with flash
    $ Pause()
    "Unable to hold back any longer, I buried myself to the hilt."
    "She squealed as she felt the rush of warmth inside her, gasping breathlessly."
    MC "HRGHHHH!"
    CHANYI "F-Fuckkkkk...!"
    ANYA "Now me!"
    ANYA "Please, please, please!"
    CHANYI "Anya... {i}*Huff*{/i} You just asked him to cum in me."
    ANYA "... Umm, s-sorry?"
    ANYA "I just got caught up in the moment, haha!"
    CHANYI "... Fuck her hard and make her pay for it."
    ANYA "Ooooh! I said I was sorry!"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_4
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_4
    with dissolve
    $ Pause()
    "Anya wiggled her butt enticingly as I positioned myself behind her."
    ANYA "Please, punish me by taking out your frustrations on my worthless pussy, fufu~"
    MC "Quite the little masochist, aren't we?"
    "Anya giggled, licking her lips as she continued to shake her butt on my cock."
    ANYA "Tell anyone and Chanyi will have your head on a stick."
    ANYA "But please... {i}Be as mean to me as possible when we're here!{/i}"
    MC "(They're both fucking crazy.)"
    $ PlaySexFx(audio.kiara_tent_slow, 1)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_5
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_5
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_5
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_5
    with dissolve
    $ Pause()
    "I pushed inside her as she spread wider."
    ANYA "OOOOOH! Yes!"
    "Her {i}'worthless'{/i} cunt squeezed around me with a tightness that would make a virgin seem loose."
    "I gritted my teeth, taking a deep breath to avoid finishing in her there and then." 
    "As I pounded away at her soft ass, my balls slapped up against her clit as she pushed herself back onto me."
    "Anya moaned happily as Chanyi watched."
    CHANYI "You really would crawl and beg for a big cock, wouldn't you?"
    CHANYI "The world's worst tribad."
    ANYA "N-Noooo...!"
    ANYA "I don't feel anything for men!"
    ANYA "I couldn't live without your pussy!"
    CHANYI "But you love it when I order you to suck cock, don't you?"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_6
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_6
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_6
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_6
    with dissolve
    $ Pause()
    "Anya shuddered, tightening around me."
    "The only thing I could do was pound at her faster, slamming into her eager hole as Anya cried out her unfiltered, lewd thoughts."
    ANYA "Y-Yes! It's so humiliating!"
    ANYA "Being made to crawl for them!"
    ANYA "To be just a hole for them to use!"
    CHANYI "Hahaha! How much more pathetic can you get?"
    ANYA "Y-Yes! I'm a joke!"
    ANYA "A failure as a wife!"
    "She pushed herself back onto me, grinding her round ass against me as she squeezed tightly."
    MC "(Oh F-Fuckkk!)"
    ANYA "M-Men are such - Mmfghh!"
    ANYA "Ignorant! AHH! Mean spirited!"
    ANYA "{i}*Huff*{/i} Muscular... Fucking..."
    ANYA "B-BASTARDS!"
    CHANYI "Present company included?"
    ANYA "Noooooo!"
    ANYA "H-He was gifted - {i}*huff*{/i} S-Such a lovely...{i}*Huff*{/i}"
    ANYA "Big...{i}*Huff*{/i} BIG..."
    MC "Anya, I'm gonna—"
    ANYA "GIVE IT TO ME!"

    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            $ UnlockGalFlag("anya_and_chanyi", "balcony", "var_preg_ling")
        elif tmpvar["clothes"] == "naked":
            $ UnlockGalFlag("anya_and_chanyi", "balcony", "var_preg_naked")
    else:
        if tmpvar["clothes"] == "ling":
            $ UnlockGalFlag("anya_and_chanyi", "balcony", "var_nopreg_ling")
        elif tmpvar["clothes"] == "naked":
            $ UnlockGalFlag("anya_and_chanyi", "balcony", "var_nopreg_naked")

    $ UnlockGalSceneAndGrantXp("anya_and_chanyi", "balcony")
    $ ReduceInfectionFromSex("chanyi")
    $ PregRoll("chanyi")

    $ PlaySexFx(audio.kiara_tent_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_cum_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_cum_2
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_cum_2
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_cum_2
    with flash
    $ Pause()
    "As she slammed back onto me, I lost control and came."
    MC "GODSSSSS!!"
    "Anya gasped as she felt the rush of warmth inside of her."
    ANYA "Oooooh!"
    ANYA "Did you see how much he filled me up?!"
    ANYA "{i}Mmmm....{/i} Our little stallion's incredible!"
    "Chanyi watched, amused."
    MC "{i}*Huff*{/i} Fuck... Ladies, I think I need a-"
    CHANYI "Hold your tongue!"
    CHANYI "We're not finished yet."
    MC "... Wait, but I've finished in you both?"
    "Chanyi reached back, spreading herself."
    CHANYI "{i}Here.{/i}"
    CHANYI "I want to feel you here."
    MC "You mean-"
    CHANYI "My ass... I want to feel that big cock in my ass."
    ANYA "Oooh! CHANYI!"
    "My cock hardened again at the invitation."
    ANYA "I thought you didn't like that?"
    CHANYI "When the mood strikes me, I do."
    "Chanyi licked her lips in anticipation."
    CHANYI "{i}And the mood is striking me...{/i}"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_1
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_1
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_1
    with dissolve
    $ Pause()
    "I aligned myself behind her once more."
    "Playfully, Chanyi began to playfully rock her ass back and forth."
    CHANYI "I've felt your eyes on my ass ever since we came here."
    CHANYI "My ass is going to leave you praying to the gods for mercy when I'm done."
    "I grinned."
    MC "Challenge accepted."
    MC "Are you sure you're ready?"
    CHANYI "Put it in me."
    $ PlaySexFx(audio.forgean_075, 1)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_7
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_7
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_7
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_7
    with dissolve
    $ Pause()
    "She groaned as she took me slowly."
    CHANYI "{i}*Huff*{/i} S-Shit..."
    ANYA "Are you alright?"
    CHANYI "Y-Yes... go slowly."
    "I did as she asked, easing into a steady rhythm."
    "Her tight ass wrapped and squeezed around me as I forced my cock in deeper into her rear."
    "Chanyi's face contorted, at first, painful winces, but soon, with nervous breathes, she began to relax."
    CHANYI "{i}*Huff*{/i} T-That's it... Put that big cock in my ass."
    CHANYI "Oooooh..."
    MC "Need me to stop?"
    CHANYI "Absolutely fucking not."
    "I couldn't help but chuckle as I continued to pound away at her rear until eventually she groaned." 
    CHANYI "... Harder."
    MC "Are you sure?"
    CHANYI "Stop talking and fuck me properly!"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_8
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_8
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_8
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_8
    with dissolve
    $ Pause()
    "I picked up the pace, driving into her harder."
    CHANYI "URGHHH!"
    CHANYI "Yes! That's it you - Ahh! FUCK!"
    CHANYI "Your big cock - Mmfghh! Is the - Ahh!"
    CHANYI "P-Propety of the Faymore's now! You-"
    CHANYI "Ooooh! Fuck! You're fucking my ass so hard!"
    MC "Sounds to me more like I own the Faymore women's asses to me!"
    "Anya giggled excitedly at the comment."
    ANYA "Did you hear that, Chanyi?"
    ANYA "He's come to {i}own{/i} our asses!"
    ANYA "How degrading!"
    "Chanyi could only groan in response as I turned her ass into my own private toy."
    CHANYI "Mmmfghhhhh!!"
    CHANYI "D-Don't stop!"
    CHANYI "Don't stop! Don't stop! Don't stop fucking my rear!"
    CHANYI "Don't stop till you cum!"
    "My now, Chanyi's ass had left me desperate to cum once more."
    MC "Hrghh! I'm close!"
    CHANYI "Do it!"
    $ PlaySexFx(audio.forgean_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_cum_3
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_cum_3
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_cum_3
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_cum_3
    with flash
    $ Pause()
    MC "HRGHHHH!"
    "I finished, watching my load pour into her tight ass."
    "Her tail swished excitedly, as the hungry katai's legs shook."
    "Her holes both fucked and satisfied."
    CHANYI "F-Fuck..."
    "As I pulled out, she struggled to stay standing."
    CHANYI "Gods... You're - {i}*Huff*{/i}"
    CHANYI "N-Not bad..."
    CHANYI "{i}For a man.{/i}"
    "Anya watched, wide-eyed and eager."
    MC "{i}Want to try?{/i}"
    "She nodded instantly."
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_4
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_4
    with dissolve
    $ Pause()
    "I moved behind her."
    "Once more, Anya shook her ass teasingly."
    "My cock, now aching, rose once again to the occasion as Anya giggled."
    ANYA "I need it too..."
    MC "Where do you want it?"
    "Anya giggled, biting her lower lip alluringly as she spoke in a coy, sweet voice."
    ANYA "{i}In my ass soon... I want you to fuck my big, fat... tight, ass.{/i}"
    $ PlaySexFx(audio.kiara_tent_slow, 1)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_9
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_9
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_9
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_9
    with dissolve
    $ Pause()
    "She took me quickly, pushing back eagerly."
    "Her ass was unlike anything I ever felt, crushing my cock as she smirked watching my expression contort."
    ANYA "It was incredible watching you."
    ANYA "No one's ever made her act like that."
    MC "Anya - {i}*Huff*{/i} You-"
    ANYA "Have your big, fat cock stretching out my rear?"
    "I gulped, still pounding away at her hole."
    MC "I was going to say - Ahh!"
    MC "Your ass is so fucking tight!"
    "Anya pouted, pushing her ass hard back onto me."
    ANYA "Awww, you're so sweet!"
    ANYA "But next time add a little bit about how I should sell this hole or something."
    MC "(Was she always this crazy? Or did Chanyi make her this way?)"
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_10
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_10
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_10
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_10
    with dissolve
    $ Pause()
    "The pace quickened."
    "Her round, tight ass now smashed back into me as the lewd words continued to tumble out."
    ANYA "Tell me you prefer her ass."
    MC "What?"
    ANYA "Tell me I'm worthless."
    ANYA "Tell me Chanyi's suchhhh a better fuck and that you can please her in ways I can't!"
    MC "You've got issues."
    ANYA "That's right!"
    "Anya's ass almost seemeed to pulse around me as she squeezed and then released."
    "There were professional whores less talented and skilled in draining men than this crazy wench."
    ANYA "And I'm - {i}*Huff*{/i} taking out ALLLL my issues on-"
    ANYA "Your big."
    ANYA "Fat."
    ANYA "COCK!"
    MC "Anya, I'm—"
    MC "{i}*Huff*{/i} I'm close again!"
    ANYA "Finish in me!"
    ANYA "Finish in my ass like one of those common whores!"
    $ PlaySexFx(audio.kiara_tent_finish)
    if CharIsVisiblyPreg("chanyi"):
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_preg_ling_cum_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_preg_naked_cum_4
    else:
        if tmpvar["clothes"] == "ling":
            scene faymore_quickie_nopreg_ling_cum_4
        elif tmpvar["clothes"] == "naked":
            scene faymore_quickie_nopreg_naked_cum_4
    with flash
    $ Pause()
    MC "HRGHHHH!"
    "I slammed into her, finishing again as I filled Anya's bowels."
    ANYA "{i}*Gasp!*{/i}"
    "She wiggled her ass as she smirked, keen to make sure every drop found it's way out of my balls and into her rear."
    ANYA "Ooooh! There's so much of it still!"
    ANYA "You really ARE a stallion! Haha!"
    MC "Good...{i}*Huff*{/i} Fuck..."
    MC "{i}rear whore.{/i}"
    "Anya allowed herself to slump down beside Chanyi, satisfied."
    "The two lay sprawled, exhausted and spent."
    ANYA "Mhmmm... {i}*Sighs*{/i}"
    ANYA "You can go now, fufu."
    ANYA "I think we're just going to stay here a while."
    MC "(Something tells me they won't make that engagement.)"
    "I dressed and carried them to bed before leaving."
    $ StopReplay()
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ AutoMus(True)
    MC "(I won't be forgetting tonight anytime soon.)"
    $ tmpvar = {}
    $ LocEnter()