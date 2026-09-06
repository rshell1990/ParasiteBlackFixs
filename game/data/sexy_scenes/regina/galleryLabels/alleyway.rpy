label gallery_regina_alleyway:
    $ tmpvar["mc_clothes"] = CharGetClothes("mc")

    $ HideUI(True)

    $ PlayMusic("audio/music/32_Mind_of_Mysteries.ogg")
    play ambience wLocs["novaras_dist_market"].dn_ambience.nightTrack
    scene black
    with dissolve

    "You chased her towards the Market district."
    #Player heads towards the markets
    MC "(Where is she?)"
    MC "(I thought you'd said she'd be here?)"
    BLACK "({i}She is here.{/i})"
    MC "(But where? I can't see her anywhere.)"
    BLACK "({i}She knows{/i})"
    MC "(She knows? How can she-)"
    scene bg_alleyway_night
    show mc at cleft
    $ tmpvar["regina_clothes"] = CharGetClothes("regina")
    $ CharSetClothes("regina", "robe")
    $ CharSetVar("regina", "hood", True)
    show regina at cright_f
    with hpunch
    "Suddenly, I felt something grab at my arm and with great strength pull me around the corner into the darkened alleyway."
    "[regina_ref_cap!t] stood in front of me, pulling down the hood from her dark robes as she stared intently."
    REGINA @talk "I told you, I'm meeting an old friend alone, {i}alone.{/i}"
    MC @talk "How did you know I was there?"
    REGINA @talk "You're not as subtle as you think."
    REGINA @talk "And I had my suspicions you might try something like this."
    MC @talk "{i} ... Who are you?{/i}"
    "The question gave [regina_ref_cap!t] pause, her expression softened as she opened her mouth to answer, before stopping herself."
    REGINA @talk "{i}*Sigh*{/i} There's so much you don't understand."
    MC @talk "Are you ..."
    MC @talk "{i}A mage?{/i}"
    "[regina_ref_cap!t] blinked at the comment."
    REGINA @talk "... Not quite."
    MC @talk "What does that mean?"
    REGINA @talk "It means not quite."
    "I felt the question on the tip of my tongue, the one I was afraid to ask."
    "I gulped, barely managing to force out the question."
    MC @talk "... Are you a dark mage, [regina_ref_cap!t]?"
    REGINA @talk "{i}Would it matter if I was?{/i}"
    "The words left me paralyzed."
    "I, like many others, had spent our whole lives hearing about the horrors of dark mages and their foul magic."
    "And now stood before me, [regina_ref_cap!t], speaking almost candidly about the notion of herself being one."
    MC @talk "Why won't you answer the question?"
    REGINA @talk "I did answer the question, you're just not ready for the answer."
    MC @talk "[regina_ref_cap!t], I-"
    show regina at center_f
    with easeinright
    "[regina_ref_cap!t] stepped forward, her hands cupping both of my cheeks."
    REGINA @talk "{i}It's still me, [player_name!t]... You understand?{/i}"
    REGINA @talk "No matter what, {i}I'll always love and protect you more than you could ever understand.{/i}"
    show regina at cright_f
    with easeinright
    "[regina_ref_cap!t]'s eyes moved downwards towards my crotch, before she smiled alluringly and stepped back."
    REGINA @talk "How long since you last fed the darkness within you?"
    MC @surprised "W-What?"
    REGINA @talk "Don't pretend you don't know what I'm talking about."
    REGINA @talk "There's two souls within your body."
    MC @talk "... How long have you known?"
    REGINA @talk "The moment you returned I sensed it."
    MC @talk "But the royal mage-"
    REGINA @talk "The mages in Alderay are only looking for dark magic or signs of the Demorai's taint."
    REGINA @talk "But what's within you is neither, but something else entirely different."
    REGINA @talk "Now tell me, when was the last time you sated the beast?"
    "I paused for a moment, unsure of how to answer as I thought back to the last time."
    MC @talk "Why do you want to know that?"
    REGINA @talk "Don't play coy with me, [player_name!t], even now I can sense the aroma it's emitting."
    REGINA @talk "It wants to fuck, doesn't it?"
    "I couldn't believe the words coming out of [regina_ref_cap!t]'s mouth, to hear her talk like this felt like a I was speaking to a totally different person."
    MC @talk "Yes, it ... It needs to mate, or-"
    REGINA @talk "I see."
    REGINA @talk "Well then ..."
    REGINA @talk "Do you want me to help you with your {i}problem{/i}, dear?"
    "[regina_ref_cap!t] began to unbutton her robes, and I suspected some dark line was about to be crossed if I let her continue ..."

    menu:
        "{i}*Let her continue*{/i}":
            $ PlayMusicRandom("mus_sex")
            hide regina
            show cg_regina_robe_open at cright_f 
            with dissolve
            "As [regina_ref_cap!t] began to undo her robes, she revealed her naked lush body hidden beneath."
            MC @surprised "Y-You came out here just wearing that?!"
            REGINA @talk "Stop talking."
            REGINA @talk "I want you to take it out for me."
            scene regina_alleyway with hpunch
            "[regina_ref_cap!t] stepped towards me, her gentle touch sharply pushing me against the cold wall."
            "As her hand reached down, gently resting over my crotch, she smiled alluringly once more."
            REGINA @talk "Your heart is racing dear ... {i}relax.{/i}"
            MC @talk "How am I supposed to relax with all of this going on?"
            scene regina_alleyway_handjob with Dissolve(0.3)
            "[regina_ref_cap!t] giggled, her hand reaching down to pull out my already hardened cock."
            REGINA @talk "Ahh, you seem so nervous but-"
            REGINA @talk "This part of me is telling me you're excited for what's about to happen."
            "My heart felt like it might burst out of my chest at any moment as my eyes looked down to see [regina_ref_cap!t] with my sword in her hand."
            $ PlaySexFx("audio/sex_sounds/adara_hj_loop.ogg",1)
            scene regina_alleyway_handjob_slow
            "She gently gripped her warm hand around it and began to stroke it back and forth."
            MC @talk "Someone could see us..."
            "[regina_ref_cap!t] softly laughed once again."
            REGINA @talk "Oh? That's the only thing you're worried about, hmm?"
            REGINA @talk "Being caught?"
            MC @talk "I don't know what to think right now, this is all so ... {i}wrong.{/i}"
            REGINA @talk "{i}Wrong?{/i}"
            scene regina_alleyway_thighjob_slow with dissolve
            "There was a soft, alluring quality to her voice as she slipped my cock between legs and nestled it up beneath her wet womanhood."
            REGINA @talk "{i}Then why does it feel so good?{/i}"
            "Gently, [regina_ref_cap!t] began to grind against me, her wet slit coating my cock in her juices as she moaned softly."
            REGINA @talk "S-Such a big boy..."
            MC @talk "{i}*Huff*{/i} [regina_ref_cap!t]..."
            REGINA @talk "That's right, baby, just relax."
            REGINA @talk "I'm h-here - Mmm ..."
            REGINA @talk "You feel so hard."
            REGINA @talk "Just let it out ... Cum for me."
            MC @talk "You ... We shouldn't be doing-"
            $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg",1)
            scene regina_alleyway_thighjob_fast with dissolve
            REGINA @talk "Don't worry about all that nonsense, dear."
            REGINA @talk "You don't have to play by any rules you don't want to, understand?"
            REGINA @talk "I'm here for you no matter what dear."
            REGINA @talk "Fuck me ... Breed me ... Make the women of this world your whores."
            REGINA @talk "Kill a thousand people, take the throne for yourself, it doesn't matter to me."
            "I couldn't believe the words I was hearing; it didn't sound like [regina_ref_cap!t] was speaking to me anymore."
            "The usual soft, warm friendliness to her voice was gone."
            "Before, her voice was a soothing presence, wholesome and comforting for everyone around her."
            "Now, as she continued to furiously rub herself against me, it was like she was possessed."
            "Her usual demeanour was replaced by that of some strange, dark vixen."
            REGINA @talk "You're beginning to - Mhmm - Throb, dear."
            REGINA @talk "Are you close?"
            "Her hot breath touched my cheeks as I stared into her deep pool like eyes that were...purple?"
            MC @talk "Your ... Your eyes are-"
            REGINA @talk "Shh, let me know when you're going to finish, dear."
            REGINA @talk "That's all you need to focus on now."
            "Indeed, all this time as she continued to grind and rub her wet slit against me, the intoxicating friction was becoming unbearable."
            "As she cooed and moaned hotly, it only further stiffened my throbbing cock."
            MC @talk "[regina_ref_cap!t]! {i}*Huff*{/i} I'm-"
            "Before I could finish my sentence, I grunted, my whole body hot and trembling as I knew any moment I was about to finish."

            MAN "Come along, dear, this way."
            WOMAN "Darling, why do we have to head through here? It's so ... dark."
            MC @talk "Shit! [regina_ref_cap!t]! Someone's com-"
            "[regina_ref_cap!t] didn't stop, instead, she gyrated her hips faster, crushing my cock between her thighs as she suddenly leaned forward to press a kiss onto me."
            $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
            scene regina_alleyway_finish_1 with flash
            "As her tongue pressed into my mouth and thrashed around in my mouth, I could take it no longer."
            "My hands clutched into her soft hips as she let out a hot surprised moan, and my throbbing cock finished, covering much of her pussy and ass in my hot seed."
            scene regina_alleyway_finish_2 with dissolve
            "As I finished, the couple wandered through, the female of the duo gasped in shock."
            scene cg_regina_alleyway_couple with dissolve
            WOMAN "H-Honey! They're-"
            MAN "Don't look my love, some people just have no decency."
            "[regina_ref_cap!t] completely ignored the passing couple, she was far too pre-occupied with her passionate kiss with me."
            WOMAN "(By the gods ... Look at the size of that thing.)"
            MAN "Dear! Avert your gaze and keep walking!"
            "The man snatched at his wife's hands and dragged her away from the scene, the whole time, she blushed and looked back in disbelief at the scene she had just witnessed."
            "Once the two of them were out of sight, [regina_ref_cap!t] pulled away and laughed, wiping at her mouth."

            $ PlayMusic("audio/music/32_Mind_of_Mysteries.ogg")

            scene bg_alleyway_night
            show mc at cleft
            show regina at cright_f
            with dissolve
            REGINA @smile "Oh my, I don't think she's going to forget that in quite the hurry!"
            MC @sad "We-"
            MC @surprised "What if they recognize us?"
            REGINA @talk "Relax my dear, they weren't focusing on our faces."
            "Now, with my seed dripping between [regina_ref_cap!t]'s legs down onto the floor and the haze of lust passing, the gravity of what we had just done did not allude me."
            MC @surprised "[regina_ref_cap!t] ... We-"
            REGINA @talk "We helped relieve you of your problem, right?"
            MC @talk "I ... Yes, but-"
            REGINA @talk "Then you don't need to trouble yourself with it any more than that."
            show regina at center_f
            with easeinright
            "Once more, [regina_ref_cap!t] stepped closer to caress my cheek."
            "The lover tenderness of the action from the glint in her eyes was overflowing but ... unnatural."
            REGINA @talk "From now on, you know."
            REGINA @talk "You only need to ask, and I'll take care of all your desires."
            REGINA @talk "I love you so much, it hurts."
            MC @talk "[regina_ref_cap!t]..."
            show regina purple_eyes at center_f with flash
            "[regina_ref_cap!t]'s eyes flashed purple, and soon, the world around me began to fall dark."
            play sound2 "audio/cfx/body_collapse.ogg"
            scene black with dissolve
            REGINA @talk "Shhh ... Rest now my sweet."
            REGINA @talk "I still have some business I need to attend to~"
        "{i}*Stop her*{/i}":
            "Reaching out, I clasped both of her hands."
            MC @surprised "I'll deal with it myself!"
            '[regina_ref_cap!t] seemed surprised at my reluctance, before a soft smile appeared on her face.'
            REGINA @smile "Very well then, dear."
            REGINA @talk "I'll always be here if you need me ... {i}No matter what.{/i}"
            show regina purple_eyes at cright_f with flash
            "[regina_ref_cap!t]'s eyes flashed purple, and soon, the world around me began to fall dark."
            play sound2 "audio/cfx/body_collapse.ogg"
            scene black with dissolve
            REGINA @talk "Shhh ... Rest now my sweet."
            REGINA @talk "I still have some business I need to attend to~"
    scene black with Dissolve(1.0)
    $ CharSetClothes("mc", tmpvar["mc_clothes"])
    $ CharSetClothes("regina", tmpvar["regina_clothes"])
    $ CharSetVar("regina", "hood", False)
    $ tmpvar.pop("mc_clothes")
    return
