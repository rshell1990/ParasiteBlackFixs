label travel_event_lizard_green:
    scene bg_forest_clearing with dissolve
    show mc at left with easeinleft
    "As I make my way through into the forest clearing, I can't help but {i}feel{/i} like I'm being watched." 
    "Other than the singing of birds and the gentle breeze brushing through the leaves of trees and the blades of grass, there is nothing of note."
    "And yet... I pause and wait, refusing to step any further."
    "As I do so, I hear it."
    play sound "audio/cfx/snake_hiss_1.ogg"
    "{i}*Hissing.*{/i}"
    "From the tall grass, three Skalith leapt out towards me, bone-bladed claws ready."
    "Humanoid, but distinctively reptilian."
    play sound "audio/cfx/snake_hiss_2.ogg"
    "They hissed and snarled, covered only with some loose, torn fabric."
    "One amongst them, completely naked but with hair, unlike the bald others, stepped out and hissed towards me."
    show lizard_green at right_f with easeinright
    if CharInParty("markus"):
        show markus at cleft with easeinleft
        MARKUS "SKALITHS!"
        hide markus with dissolve
    if CharInParty("elena"):
        show elena at cleft with easeinleft
        ELENA @angry "Don't let their blades touch you! They coat them in their venom!"
        hide elena with dissolve
    if CharInParty("myu"):
        show myu at cleft with easeinleft
        MYU @angry "MYUUUUUUUU!"
        hide myu with dissolve
    if CharInParty("ves"):
        show ves at cleft with easeinleft
        VES @angry "Bah! These things plague even these lands!"
        hide ves with dissolve
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    
    $ tmpvar = {}
    $ tmpvar = ["e_lizard_green"]
    if RngInt(1, 3) > 1:
        $ tmpvar.append("e_lizard_green")
    if GetPartySize() > 1:
        if RngInt(1, 2) == 1:
            $ tmpvar.append("e_lizard_green")
    if GetPartySize() > 2:
        if RngInt(1, 2) == 1:
            $ tmpvar.append("e_lizard_green")

    $ StartBattle(BattleData(BackgroundImage = "pbat_forest", CharIDList_Right = tmpvar))
    $ tmpvar = {}
    scene bg_forest_clearing with dissolve
    show mc at cleft with easeinleft
    $ AutoMus(True)
    if not PlayerHasPerk("natural_instincts"):
        "After striking down the last of them, their leader was already fleeing and escaping into the tall grass, hissing as it left."
        play sound "audio/cfx/snake_hiss_1.ogg"
        MC "(Damn things...)"
        MC "(They've slain no end of passing soldiers and travelers coming through.)"
        MC "(I best be careful, else I too might end up on the menu...)"
        return

    # natural instincts perk is present, begin potential sex scene
    "As the last of their warriors fell, their leader, at first aggressive, suddenly became demure."
    show lizard_green at right_f with easeinright
    "While neither of us could speak to one another, there was a strange... shared feeling between us, a language unspoken with words."
    "As I took a deep breath, I could smell her desire to mate... {i}to breed.{/i}"
    "She flicked her tongue out and gently traced her hands over her body, enticingly."
    show lizard_green at cright_f with easeinright
    "Instead of hissing, she now only let out a low rumble as she continued to stare towards me."
    if CharInParty("markus"):
        MARKUS "Uhh... [player_name!t], are you seriously going to-"
        MARKUS "{i}With a Skalith?{/i}"
    if CharInParty("elena"):
        ELENA @angry "I swear by the gods, if that thing bites your cock off, I'll tell everyone how foolishly you died!"
    if CharInParty("ves"):
        VES @talk "It's good this creature recognizes you for the strong mate you are."
        VES @angry "But I have seen many orcs die foolishly trying to stick their cock somewhere it doesn't belong!"
    if CharInParty("regina"):
        REGINA @lewd "Oh my...!"
        REGINA @smile "How wonderful to see even the darkest creatures recognizing your power!"
        REGINA @lewd "Break its feeble mind and let her know who her new master is!"
    if CharInParty("myu"):
        MYU "...Myu?"
        MYU @blush "...Myu!"

    menu:
        "Signal, you want to mate.":
            "Slowly, as I approach the Skalith, she leads me slightly deeper into the grass, making sure to wiggle her ass enticingly as she does so." #Fade to black
            "Finding a comfortable patch, she prostrates herself onto the ground, sticking out her round ass and wiggling it towards me." #idle - GREEN LIZARD
            call travel_event_lizard_sex("green") from _call_travel_event_lizard_sex

            # post-sex
            scene bg_forest_clearing with dissolve
            show mc at left with easeinleft
            MC "Wait! Come back!"
            MC "(Damn...)"
            MC "(I wonder if our paths should cross again?)"
            return

        "Reject her advances.":
            "It doesn't take much, a snort of air from my nostrils and the tightening up of my body, to let her know I'm not interested in mating."
            "Sensing my rejection, she turned tail and ran deep into the tall grass, escaping with a sudden burst of speed."
            hide lizard_green with easeoutright
            MC "(Hm... I wonder if I'll run into that one again?)"
            return

label travel_event_lizard_blue:
    scene bg_forest_clearing with dissolve
    show mc at left with easeinleft
    "As I make my way through alongside the banks of the water, I can't help but {i}feel{/i} like I'm being watched." 
    "Other than the sounds of running water and the gentle breeze brushing through the blades of grass, there is nothing of note."
    "And yet... I pause and wait, refusing to step any further."
    "As I do so, I hear it."
    play sound "audio/cfx/snake_hiss_1.ogg"
    "{i}*Hissing.*{/i}"
    "Springing out from the water itself, the three Skalith leap out towards me, bone-bladed claws ready."
    "Humanoid, but distinctively reptilian."
    "They hissed and snarled, covered only with some loose, torn fabric."
    show lizard_blue at right_f with easeinright
    play sound "audio/cfx/snake_hiss_2.ogg"
    "One amongst them, completely naked but with hair unlike the others, stepped out and hissed towards me."
    if GetPartySize() > 1:
        MC @angry "WATER SKALITHS!"
    if CharInParty("markus"):
        show markus at cleft with easeinleft
        MARKUS "Keep back! Their poison is lethal!"
        hide markus with dissolve
    if CharInParty("elena"):
        show elena at cleft with easeinleft
        ELENA @angry "C-Careful! There may be more in hiding!"
        hide elena with dissolve
    if CharInParty("myu"):
        show myu at cleft with easeinleft
        MYU @angry "MYUUUUUUUU!"
        hide myu with dissolve
    if CharInParty("ves"):
        show ves at cleft with easeinleft
        VES @angry "Fish or lizard, they bleed all the same!"
        hide ves with dissolve

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ tmpvar = {}
    $ tmpvar = ["e_lizard_blue"]
    if RngInt(1, 3) > 1:
        $ tmpvar.append("e_lizard_blue")
    if GetPartySize() > 1:
        if RngInt(1, 2) == 1:
            $ tmpvar.append("e_lizard_blue")
    if GetPartySize() > 2:
        if RngInt(1, 2) == 1:
            $ tmpvar.append("e_lizard_blue")

    $ StartBattle(BattleData(BackgroundImage = "pbat_forest", CharIDList_Right = tmpvar))
    $ tmpvar = {}
    scene bg_forest_clearing with dissolve
    show mc at cleft with easeinleft
    $ AutoMus(True)
    if not PlayerHasPerk("natural_instincts"):
        "After striking down the last of them, their leader leapt into the depths of the water with a loud splash."
        "They briefly re-emerged half of their head from the water deep-in, glaring towards me before sinking back beneath the depths."
        MC "(Damn things...)"
        MC "(They've slain no end of passing soldiers and travelers coming through.)"
        MC "(I best be careful, else I too might end up on the menu...)"
        return

    # got perk, go on
    "As the last of their warriors fell, their leader, at first aggressive, became suddenly demure."
    show lizard_blue at right_f with easeinright
    "While neither of us could speak to one another, there was a strange... shared feeling between us, a language unspoken with words."
    "As I took a deep breath, I could smell her desire to mate... {i}to breed.{/i}"
    "She flicked her tongue out and gently traced her hands over her body, enticingly."
    show lizard_blue at cright_f with easeinright
    "Instead of hissing, she now only let out a low rumble as she continued to stare towards me."
    if CharInParty("markus"):
        MARKUS "Alright, I KNOW you're willing to stick your cock in some crazy things..."
        MARKUS "But perhaps this is a little much even for you?"
    if CharInParty("elena"):
        ELENA @angry "You can't be seriously contemplating sleeping with that thing!"
        ELENA @angry "{i}She just tried to eat us!{/i}"
    if CharInParty("ves"):
        VES @talk "If this is some trick, I'm going to smash that thing's head in."
    if CharInParty("regina"):
        REGINA @lewd "...{i}Fascinating.{/i}"
        REGINA @lewd "Break its feeble mind and let her know who her new master is!"
    if CharInParty("myu"):
        MYU "...Myu?"
        MYU @blush "...Myu!"
    menu:
        "Signal, you want to mate.":
            "Slowly, as I approach the Skalith, she leads me towards a soft patch of grass near the water bank, making sure to wiggle her ass enticingly as she does so." #Fade to black
            "Now comfortable, she prostrates herself onto the ground, sticking out her round ass and shaking it towards me." #idle - BLUE LIZARD
            call travel_event_lizard_sex("blue") from _call_travel_event_lizard_sex_1

            # post-sex
            scene bg_forest_clearing with dissolve
            show mc at left with easeinleft

            "As I let my tentacles go slack, the Skalith, standing back on her feet, now satisfied, hurried to get away and dive into the nearest pool of water. Bobbing in the water, she stared at me momentarily before fully submerging herself, vanishing completely."
            MC "Wait! Come back!"
            MC "(Damn...)"
            MC "(I wonder if our paths should cross again?)"
            return

        "Reject her advances.":
            "It doesn't take much, a snort of air from my nostrils and the tightening up of my body, to let her know I'm not interested in mating."
            "Sensing my rejection, she turns tail and dives into the nearest pool of water, escaping with a sudden burst of speed."
            hide lizard_blue with easeoutright
            MC "(Hm... I wonder if I'll run into that one again?)"
            return

label travel_event_lizard_red:
    scene pbat_desert with dissolve
    show mc at left with easeinleft
    "As I make my way traipsing through the hot desert sands, I can't help but {i}feel{/i} like I'm being watched." 
    "But besides the sounds of the desert grains rolling over the desert dunes and the howling desert winds, there is nothing else of note."
    "And yet... I pause and wait, refusing to step any further."
    "As I do so, I hear it."
    play sound "audio/cfx/snake_hiss_1.ogg"
    "{i}*Hissing.*{/i}"
    "Springing out from under the desert sands like scorpions, the three Skalith leapt out towards me, bone-bladed claws ready."
    "Humanoid, but distinctively reptilian."
    "They hissed and snarled, covered only with some loose torn fabric."
    show lizard_red at right_f with easeinright
    play sound "audio/cfx/snake_hiss_2.ogg"
    "One amongst them, completely naked but with hair unlike the others, stepped out and hissed towards me."
    
    if GetPartySize() > 1:
        MC @angry "SKALITHS!"
    if CharInParty("markus"):
        show markus at cleft with easeinleft
        MARKUS "Don't let them slice you with those blades! They coat them in their poison!"
        hide markus with dissolve
    if CharInParty("elena"):
        show elena at cleft with easeinleft
        ELENA @angry "Red Skaliths! Be careful!"
        hide elena with dissolve
    if CharInParty("myu"):
        show myu at cleft with easeinleft
        MYU @angry "MYUUUUUUUU!"
        hide myu with dissolve
    if CharInParty("ves"):
        show ves at cleft with easeinleft
        VES @angry "Cowardly beasts hiding in the sand!"
        hide ves with dissolve
    
    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")

    $ tmpvar = {}
    $ tmpvar = ["e_lizard_red"]
    if RngInt(1, 3) > 1:
        $ tmpvar.append("e_lizard_red")
    if GetPartySize() > 1:
        if RngInt(1, 2) == 1:
            $ tmpvar.append("e_lizard_red")
    if GetPartySize() > 2:
        if RngInt(1, 2) == 1:
            $ tmpvar.append("e_lizard_red")
    $ StartBattle(BattleData(BackgroundImage = "pbat_desert", CharIDList_Right = tmpvar))
    $ tmpvar = {}
    scene pbat_desert with dissolve
    show mc at cleft with easeinleft
    $ AutoMus(True)
    if not PlayerHasPerk("natural_instincts"):
        "After striking down the last of them, their leader sprinted off across the desert dunes at great speed."
        "I debated pursuing the thing, but it wasn't worth it."
        MC "(Damn things...)"
        MC "(They've slain no end of passing soldiers and travelers coming through.)"
        MC "(I best be careful, else I too might end up on the menu.)"
        return

    # got perk, go on
    "As the last of their warriors fell, their leader, at first aggressive, suddenly became demure."
    show lizard_red at right_f with easeinright
    "While neither of us could speak to one another, there was a strange... shared feeling between us, a language unspoken with words."
    "As I took a deep breath, I could smell her desire to mate... {i}to breed.{/i}"
    "She flicked her tongue out and gently traced her hands over her body, enticingly."
    show lizard_red at cright_f with easeinright
    "Instead of hissing, she now only let out a low rumble as she continued to stare towards me."
    if CharInParty("markus"):
        MARKUS "Are nice, human girls not doing it for you anymore?"
    if CharInParty("elena"):
        ELENA @angry "This is stupid; YOU'RE stupid if you try and fuck that thing!"
        ELENA @angry "{i}Skaliths. Eat. Us!{/i}"
    if CharInParty("ves"):
        VES @talk "She seems...{i}keen.{/i}"
    if CharInParty("regina"):
        REGINA @lewd "Mmm, can I watch?"
        REGINA @lewd "{i}*Cough!*{/i} I mean, be careful, dear!"
    if CharInParty("myu"):
        MYU "...Myu?"
        MYU @blush "...Myu!"
    menu:
        "Signal, you want to mate.":
            "Slowly, as I approach the Skalith, she leads me over one of the dunes for somewhere more privacy, making sure to wiggle her ass enticingly as she does so." #Fade to black
            "Now comfortable, she prostrates herself onto the ground, sticking out her round ass and shaking it towards me." #idle - RED LIZARD
            call travel_event_lizard_sex("red") from _call_travel_event_lizard_sex_2
            # post-sex
            scene pbat_desert with dissolve
            show mc at left with easeinleft

            "As I let my tentacles go slack, the Skalith, now satisfied, stood back on her feet and hurried away across the desert dunes without saying another word to me."
            "At the dune's crest, she briefly tilted her head to look back at me and stare one last time before disappearing over the edge."
            MC "Wait! Come back!"
            MC "(Damn...)"
            MC "(I wonder if our paths should cross again?)"
            return
        "Reject her advances.":
            "It doesn't take much, a snort of air from my nostrils and the tightening up of my body, to let her know I'm not interested in mating."
            "Sensing my rejection, she turns tail and rushes to escape across the desert dunes, and in a moment, she's gone."
            hide lizard_red with easeoutright
            MC "(Hm... I wonder if I'll run into that one again?)"        
            return
    
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################

label travel_event_lizard_sex(lizard_color):
    if lizard_color == "green":
        scene lizard_green_idle with dissolve
    if lizard_color == "blue":
        scene lizard_blue_idle with dissolve
    if lizard_color == "red":
        scene lizard_red_idle with dissolve
    $ Pause()

    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")

    "She lets out another low rumble as she looks back towards me, signalling her readiness."
    "Now, the only question was... How did I want to claim her?"
    menu:
        "Blowjob":
            call lizard_sex_blowjob(lizard_color) from _call_lizard_sex_blowjob

        "Vaginal":
            call lizard_sex_vaginal(lizard_color) from _call_lizard_sex_vaginal

        "Anal":
            call lizard_sex_anal(lizard_color) from _call_lizard_sex_anal

    $ AutoMus(True)
    return

label lizard_sex_blowjob(LizardColor):
    $ PlaySexFx("audio/sex_sounds/kiara_bj_loop.ogg", 1)

    if LizardColor == "red":
        scene lizard_red_bj_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_slow with dissolve
    $ Pause()

    "With my tentacles holding her firmly in place, I moved around to the front of the female Skalith, pointing my cock directly towards her mouth." 
    "At first, she seemed confused, but as I pushed my cock against her cold lips, her mouth opened up with ease as she allowed the cock to slide down her throat."
    "There was no resistance, no impulsive choking, as my cock slid back and forth down her cool but tight throat, I could sense her willingness to please her new, {i}strange{/i} mate."

    if LizardColor == "red":
        scene lizard_red_bj_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_fast with dissolve
    $ Pause()

    "As her mouth coated my cock in what I could only assume is some type of aphrodisiac substance."
    "The more I fucked her mouth, the more excited I became; the saliva soaking in caused me to burn with lust."

    if LizardColor == "red":
        scene lizard_red_bj_tentacle_vag_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_tentacle_vag_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_tentacle_vag_slow with dissolve
    $ Pause()

    "Now, deciding to have some more fun with my new {i}mate,{/i} I slipped around one of the tentacles, which pushed and prodded against her slit." 
    "She let out a slight jerking motion of surprise as she felt the tentacle head push into her, but then let out another low rumble of approval."
    "As her thin, long tongue wrapped and twisted around my cock, her eyes looked up expectantly towards me."

    if LizardColor == "red":
        scene lizard_red_bj_tentacle_vag_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_tentacle_vag_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_tentacle_vag_fast with dissolve
    $ Pause()

    "Despite the sharpness of her fangs, she was as delicate as she was thorough in her attempts to swallow my cock whole."
    "As she rocked her head back and forth, I couldn't help but wonder if the eagerness of this sucking was so she might absorb the {i}'nutrients'{/i} of her mate... Or if she did just want to please me."
    "Perhaps it was both?"

    if LizardColor == "red":
        scene lizard_red_bj_tentacle_ass2_vag_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_tentacle_ass2_vag_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_tentacle_ass2_vag_slow with dissolve
    $ Pause()

    "Either way, I decided to take things a step further; with another tentacle slipping past, I prodded and pushed against her cool, tight asshole with it." 
    "Her smooth, silk-like asshole welcomed me with ease as well as I slid my tentacle back and forth in her intimate hole."
    "She let out a slight hiss as she felt the tentacle sliding deep into her ass, it was clear she wasn't used to {i}this{/i} kind of mating."
    "Yet, despite her clear unfamiliarity, she welcomed whatever I did to her, continuing to let out low rumbles of approval."
    "Her heart raced faster as I continued to play and treat her body like my plaything; I could sense her excitement and curiosity for whatever was to come next."
    "Perhaps she had only anticipated we would breed and rut like animals, but she was clearly enjoying letting me take my time with her body."

    if LizardColor == "red":
        scene lizard_red_bj_tentacle_ass2_vag_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_tentacle_ass2_vag_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_tentacle_ass2_vag_fast with dissolve
    $ Pause()

    "Her rumbles only became more frequent as she eagerly tried to swallow even more of my cock, her eyes looking up with an obedient, puppy-eyed glossiness as she continued."
    "Finally, I pushed both of the teasingly tentacles fully into the Skalith, and she let out a hiss of surprise for the first time as she felt the suctions of the tentacle attach itself fully to her behind." #Full Tentacle attachment
    "She was completely at my mercy as my tentacles thrashed about her insides."
    if LizardColor == "red":
        scene lizard_red_bj_tentacle_ass_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_tentacle_ass_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_tentacle_ass_slow with dissolve
    $ Pause()
    "I could feel her trembling and shaking as she continued to stare up towards me, half in disbelief at what she was feeling, half in pure, overwhelming ecstasy."
    "Did she even know what was happening to her body at this point? Or did that part of her brain cease to care?"
    "Overwhelmed with the pleasure flooding into her body, unsure as to all these strange new sensations... Still, she continued to desperately suck at my cock."
    "Her tongue thrashing and wrapping around it in such a spastic, intense motion, I could {i}feel{/i} how desperate she was to make me finish."
    "{i}And she would get her wish.{/i}"
    if LizardColor == "red":
        scene lizard_red_bj_tentacle_ass_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_bj_tentacle_ass_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_bj_tentacle_ass_fast with dissolve
    $ Pause()
    "I began to feel my cock tighten, the budding urge to fill her with my seed nearly reaching its climax as she continued to glide her lips back and forth over my member."
    "Finally, the sensation became too much, and like a river bursting its banks, I growled as I flooded the Skalith's little mouth with my load."
    "Her eyes widened, yet with each heavy gulp, she swallowed down the thick stream of my seed pouring into her lightly bloating stomach."

    $ PlaySexFx("audio/sex_sounds/kiara_bj_finish.ogg")
    $ UnlockGalFlag("skaliths", "bj", LizardColor)
    $ UnlockGalSceneAndGrantXp("skaliths", "bj")
    if LizardColor == "red":
        $ ReduceInfectionFromSex("lizard_red")
        scene lizard_red_bj_finish with dissolve
    if LizardColor == "green":
        $ ReduceInfectionFromSex("lizard_green")
        scene lizard_green_bj_finish with dissolve
    if LizardColor == "blue":
        $ ReduceInfectionFromSex("lizard_blue")
        scene lizard_blue_bj_finish with dissolve
    $ Pause()

    "She trembled and shook, her body convulsing and tightening with her orgasm as I continued to spill the last of my seed down her expanding throat."
    "Finally, fully drained by my little Skalith slut, I unsheathed my cock from her mouth and left it dangling limp in front of her."
    "As I let my tentacles go slack, the Skalith, standing back on her feet, scurried away into the tall grass, but not before taking one last look at me before she vanished completely."
    return

label lizard_sex_vaginal(LizardColor):
    "With my tentacles holding her firmly in place, I placed a clawed hand onto her soft, scaly ass." 
    "I stared for a moment at her welcoming homes, glistening and silk-like in the light, as my cock twitched in excitement for what was to come."
    "As I rubbed my cock against her wet slit, I sensed her eager willingness to feel me inside of her."

    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)

    if LizardColor == "red":
        scene lizard_red_vag_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_vag_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_vag_slow with dissolve
    $ Pause()

    "She soothingly rumbled as I pushed first the head, then the rest of my cock slowly into her." 
    "Her tight, cool hole stretched around me with ease as I pushed myself fully into her."
    "As she felt herself stretch to accommodate my size, she hissed in surprise, but the tension in her body quickly relaxed as she began to feel myself glide in and out of her."
    "Now comfortably inside of her, I began to move faster, slamming my hips up against hers as she cooed happily, pressing her cool scaly butt back up against me with every thrust."
    "As she looked over her shoulder towards me, I couldn't help but wonder if she was... {i}smiling?{/i}"
    
    if LizardColor == "red":
        scene lizard_red_vag_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_vag_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_vag_fast with dissolve
    $ Pause()

    "I wasn't sure if she was even capable of that kind of emotion, but as she observed my expressions, I could see a curious need to ensure her {i}mate{/i} was sufficiently satisfied."
    "I gently slapped at her butt, and she let out a small hiss, my clawed hand squeezing at her ass, feeling the thin fat layer squish between my fingers."
    "As I continued to take her, a mischievous, instinctual idea took root."
    
    if LizardColor == "red":
        scene lizard_red_vag_tentacle_ass_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_vag_tentacle_ass_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_vag_tentacle_ass_slow with dissolve
    $ Pause()

    "With one of my smaller tentacles, I moved it around to prod at her tight, silk-like asshole gently." 
    "She rumbled in approval, but her eyes widened in surprise as she felt the tongue-like tentacle work its way into her back door."
    "Was this embarrassment she was experiencing? I doubt she'd ever {i}mated{/i} like this before."
    "Or perhaps her lizard brain was overwhelmed with all these new intense sensations?"
    "I couldn't help but wonder as she continued to wiggle and rock her ass back to try and take me deeper excitedly,"

    if LizardColor == "red":
        scene lizard_red_vag_tentacle_ass_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_vag_tentacle_ass_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_vag_tentacle_ass_fast with dissolve
    $ Pause()

    "{i}that perhaps she was intrigued and interested what else I'd be able to do to her?{/i}"
    "As the tongue pushed deeper into her ass, I began to feel her body tremble, her heart racing as her breathing pace quickened."
    "Secreting from her holes and body more and more, a strange, aphrodisiac-like substance that seeped through my skin."
    "The burning desire, thanks to the aphrodisiac, only made me growl like an animal as I slammed my hips against my Skalith mate."
    "I began to feel, as the walls of her hole tightened and flexed around me, how desperate she was becoming for me to finish."
    "{i}And she would get her wish.{/i}"
    "I began to feel my cock tighten, the budding urge to fill her with my seed nearly reaching its climax as her tight hole squeezed me desperately."
    "Finally, the sensation became too much, and like a river bursting its banks, I growled as I flooded the Skalith's womb with my load."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ UnlockGalFlag("skaliths", "vag", LizardColor)
    $ UnlockGalSceneAndGrantXp("skaliths", "vag")
    if LizardColor == "red":
        $ PregRoll("lizard_red")
        $ ReduceInfectionFromSex("lizard_red")
        scene lizard_red_vag_finish with dissolve
    if LizardColor == "green":
        $ PregRoll("lizard_green")
        $ ReduceInfectionFromSex("lizard_green")
        scene lizard_green_vag_finish with dissolve
    if LizardColor == "blue":
        $ PregRoll("lizard_blue")
        $ ReduceInfectionFromSex("lizard_blue")
        scene lizard_blue_vag_finish with dissolve
    $ Pause()

    "Her eyes widened in surprise as the thick stream of my seed poured into her lightly bloating stomach."
    "She trembled and shook, her eyes rolling up as her body convulsed and tightened with her orgasm as I continued to spill the last of my seed into her."
    "Finally, fully drained by my little Skalith slut, I unsheathed my cock from her now well fucked hole and left it dangling behind her."
    "As I let my tentacles go slack, the Skalith, standing back on her feet, scurried away into the tall grass, but not before taking one last look at me before she vanished completely."
    return

label lizard_sex_anal(LizardColor):
    "With my tentacles holding her firmly in place, I placed a clawed hand onto her soft, scaly ass."
    "I stared for a moment at her welcoming holes, glistening and silk-like in the light, as my cock twitched in excitement for what was to come."
    "As I pushed my cock against her silk-like asshole, she jerked for a moment in surprise, letting out a nervous-sounding hiss as she looked back towards me with uncertain eyes."
    "Continuing to prod against the hole, she didn't stop me, but I could feel her body tense slightly."
    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)

    if LizardColor == "red":
        scene lizard_red_anal_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_anal_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_anal_slow with dissolve
    $ Pause()

    "I pushed the head in slowly at first, and as her tight asshole stretched and squeezed around my cock, I growled in approval."
    "She let out another short hiss of surprise; she was certainly not accustomed to taking things back {i}there.{/i}"
    "Still, though, she didn't lash out, and as I felt her relax slightly, slowly, I sunk the rest of my cock into her ass."
    "Her tight, cool asshole stretched around me with surprising ease as I pushed myself fully into her."

    if LizardColor == "red":
        scene lizard_red_anal_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_anal_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_anal_fast with dissolve
    $ Pause()

    "As she felt herself stretch to accommodate my size, she hissed in surprise, squirming slightly between my tentacles,"
    "but the tension in her body soon relaxed as she began to feel myself glide in and out of her."
    "She rumbled quietly in approval, looking back in a mixture of confusion and... {i}arousal.{/i}"
    
    if LizardColor == "red":
        scene lizard_red_anal_tentacle_slow with dissolve
    if LizardColor == "green":
        scene lizard_green_anal_tentacle_slow with dissolve
    if LizardColor == "blue":
        scene lizard_blue_anal_tentacle_slow with dissolve
    $ Pause()

    "I wondered if she fully understood what I was doing to her, {i}but it was clear she liked it either way.{/i}"
    "Now comfortably inside of her, I began to move faster, slamming my hips up against her ass as she cooed happily, pressing her cool scaly butt back up against me with every thrust."
    "As she looked over her shoulder towards me, I couldn't help but wonder if she was... {i}smiling?{/i}"
    "I wasn't sure if she was even capable of that kind of emotion, but as she observed my expressions, I could see a curious need to ensure her {i}mate{/i} was sufficiently satisfied."
    "I gently slapped at her butt, and she let out a small hiss, my clawed hand squeezing at her ass, feeling the thin layer of fat squish between my fingers."
    "Or perhaps her lizard brain was overwhelmed with all these new intense sensations?"

    if LizardColor == "red":
        scene lizard_red_anal_tentacle_fast with dissolve
    if LizardColor == "green":
        scene lizard_green_anal_tentacle_fast with dissolve
    if LizardColor == "blue":
        scene lizard_blue_anal_tentacle_fast with dissolve
    $ Pause()

    "Her tight asshole squeezed and flexed around my cock; the sensation was incredible; it was as though her ass, once adjusted, was trying to suck me in deeper."
    "I couldn't help but wonder as she continued to wiggle and rock her ass back to try and take me deeper excitedly,"
    "{i}that perhaps she was intrigued and interested what else I'd be able to do to her?{/i}"
    "Finally, I felt her body tremble, her heart racing as her breathing pace quickened."
    "Secreting from her holes and body more and more, a strange, aphrodisiac-like substance that seeped through my skin."
    "The burning desire, thanks to the aphrodisiac, only made me growl like an animal as I slammed my hips against my Skalith mate."
    "I began to feel, as the walls of her silk-like asshole tightened and flexed around me, how desperate she was becoming for me to finish."
    "{i}And she would get her wish.{/i}"
    "I began to feel my cock tighten, the budding urge to fill her with my seed nearly reaching its climax as her tight forbidden hole squeezed me desperately."
    "Finally, the sensation became too much, and like a river bursting its banks, I growled as I flooded the Skalith's tight ass with my load."

    $ PlaySexFx("audio/sex_sounds/forgean_finish.ogg")
    $ UnlockGalFlag("skaliths", "anal", LizardColor)
    $ UnlockGalSceneAndGrantXp("skaliths", "anal")
    if LizardColor == "red":
        $ ReduceInfectionFromSex("lizard_red")
        scene lizard_red_anal_finish with dissolve
    if LizardColor == "green":
        $ ReduceInfectionFromSex("lizard_green")
        scene lizard_green_anal_finish with dissolve
    if LizardColor == "blue":
        $ ReduceInfectionFromSex("lizard_blue")
        scene lizard_blue_anal_finish with dissolve
    $ Pause()

    "Her eyes widened in surprise as the thick stream of my seed poured into her lightly bloating stomach."
    "She trembled and shook, her eyes rolling up as her body convulsed and tightened with her orgasm as I continued to spill the last of my seed into her backdoor."
    "Finally, fully drained by my little Skalith slut, I unsheathed my cock from her now well fucked ass and left it dangling behind her."
    "As I let my tentacles go slack, the Skalith, standing back on her feet, scurried away into the tall grass, but not before taking one last look at me before she vanished completely."
    return