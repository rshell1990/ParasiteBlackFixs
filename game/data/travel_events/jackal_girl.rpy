################################################################################################################################################
# Jackal Girl Encounter on global map,
## Question mark and animal nodes - travel maps (Lake Peacing to Hamun + Temple ruins to Hamun (30% chance of event trigger)
label travel_event_jackal_girl:
    if CharIsVisiblyPreg("jackal_girl"):
        call travel_event_jackal_girl_pregnant_variant from _call_travel_event_jackal_girl_pregnant_variant
        return
    else:
        call travel_event_jackal_girl_normal_variant from _call_travel_event_jackal_girl_normal_variant
        return

label travel_event_jackal_girl_normal_variant:
    show mc at cleft with easeinleft
    "Behind me, I heard the scuttling of feet on the desert sand, rushing quickly toward me."
    show mc at blurin, cleft_f
    show jackal_girl:
        xalign 0.0
        xoffset -500
        ease 1.0 xalign 1.25 xoffset 500
    show mc at blurin, cleft
    "I grabbed the handle of my blade, but before I could turn, I felt soft, dark fur barge past me and something come loose from my person."
    "The humanoid creature, like some kind of fox, cackled, sprinting off."
    show mc at shake
    MC @angry "Hey! Get back here!"
    menu:
        "Pursue the creature." (Req_Agi = 10):
            hide jackal_girl
            hide mc with easeoutright
            "Looking over its shoulder, the creature's eyes widened in panic as it realized I was getting closer..."
            show jackal_girl at cright with easeinleft
            show jackal_girl at blurin, cright_f
            "Finally, out of breath, the creature stopped and turned toward me sheepishly."
            show mc at cleft with easeinleft
            "Now, having a chance to properly inspect it, I was taken aback by the creature's... appeal."
            "Soft, dark fur clung to this desert fox-like girl's body, but her slenderness and round, perky tits naturally drew my eye."
            # 
            if CharInParty("elena"):
                MC @think "(Perhaps it's some kind of cousin to Elena?)"
            # 
            "The thing tilted its head curiously, waiting for my next move."
            menu:
                "Demand the items back.":
                    if PlayerHasPerk("natural_instincts"):
                        "Staring at me wide-eyed, the strange desert creature sniffed for a few moments as her tail began to sway back and forth sensually."
                        JACKAL_GIRL "{i}*Soft rumble*{/i}"
                        show jackal_girl at center_f with ease
                        "She stepped closer, continuing to sniff as her eyes narrowed in."
                        "She gently rested her paws onto me, pressing her soft breasts against my body."
                        MC @lewd "You're..."
                        MC @lewd "Friendly."
                        show jackal_girl at nod
                        "The creature licked at my face, waiting expectantly as she panted like a bitch in heat."
                        "She held up what she had stolen and began to gently lick at my neck whilst looking up towards me."
                        "It seemed she wanted to make a trade..."
                        menu:
                            "Agree.":
                                "I nodded, and the fox-like girl threw herself into my arms, licking all over as we tumbled to the ground."
                                call jackal_girl_sexscene from _call_jackal_girl_sexscene
                            "Reject.":
                                show jackal_girl at cright_f with ease
                                "I gently pushed the desert fox away."
                                show jackal_girl at nod
                                show jackal_girl at blurin, cright
                                hide jackal_girl with easeoutright
                                "She dropped the item she had stolen at my feet, then hurried off, visibly dejected."
                                show mc at center with easeinleft
                                show mc at nod
                                pass
                    else:
                        "The creature seemed to understand, even if she couldn't speak."
                        show jackal_girl at nod
                        show jackal_girl at right_f with ease
                        "She dropped the stolen items at my feet and backed away submissively."
                        show jackal_girl at blurin, right_f
                        hide jackal_girl with easeoutright
                        "She waited a couple seconds to confirm I was not giving chase, then fled, cackling as she ran towards distant dunes."
                        show mc at center with easeinleft
                        show mc at nod
                        pass

                "{image=[ICON.DEATH]} Strike the creature down.":
                    show mc at center with easeinleft
                    "Drawing my blade, I slashed the creature."
                    $ QstComplete(EventJackalGirlEncounter)
                    $ QstComplete(PregJackalGirl)
                    hide jackal_girl with dissolve
                    "It let out a pitiful, helpless yelp as its blood stained the desert sand... It didn't even try to fight back."
                    show mc at nod
                    "I grabbed my stolen possessions and returned to the path."
                    hide mc with easeoutright
                    pass

        "Forget it.":
            show mc at shake
            "I let out a low growl of frustration as I watched the creature vanish almost immediately."
            show mc at center with ease
            MC @angry "(Damn thief...)"
            pass

    # ends here
    return

###### jackal girl encounter, if seen & pregnant variant
# If Jackal girl is pregnant 
label travel_event_jackal_girl_pregnant_variant:
    show mc at cleft with easeinleft
    "While making my way along the path, I once more heard the familiar rush of feet and panting from behind."
    show jackal_girl at center
    show jackal_girl at blurin, center_f
    "Leaping out in front of me, the strange desert fox girl appeared again—this time with something in her mouth."
    show jackal_girl at nod
    show jackal_girl at cright_f with ease
    "She quickly dropped it at my feet before retreating a step."

    $ tmpvar = {}
    $ tmpvar = RngInt(1, 2)
    if tmpvar == 1:
        $ PlayerAddItem("gold", RngInt(20, 40))
    elif tmpvar == 2:
        $ PlayerAddItem("potion_heal_minor", 1)
    $ tmpvar = {}

    "I picked up the {i}gift{/i} and looked up to examine her more clearly."
    "A round, protruding belly was the first thing I noticed."
    "Stunned, I glanced from her belly to her face."
    show jackal_girl at center with ease
    "She moved closer, tail swishing, then gently took my hand and placed it onto her abdomen."
    MC @surprised "Y-You're pregnant?"
    "She didn't answer—instead, she nuzzled up against me, her tail curling softly."
    "It seemed she hadn't come just to deliver the news..."
    menu:
        "Agree.":
            "I nodded, and the fox girl lit up, throwing herself into my arms."
            "She licked me all over as we tumbled down onto the sand."
            call jackal_girl_sexscene from _call_jackal_girl_sexscene_1
            return
        "Reject.":
            show jackal_girl at cright_f with ease
            "I gently pushed the desert fox away."
            show jackal_girl at nod
            show jackal_girl at blurin, cright
            hide jackal_girl with easeoutright
            "She whimpered and slowly dropped her gift before running off."
            pass
    return

###### jackal girl encounter at camp, if the Jackal has given birth
label travel_event_jackal_girl_pregnant_camp_visit:
    scene black with dissolve
    "While resting in my tent, I heard soft panting outside."
    "{i}Something was circling the camp.{/i}"
    scene expression TravelRoutes[TravelState.RouteID]["image_camp"] 
    show cg_jackal_girl_baby at cright_f
    with dissolve
    show mc at cleft with dissolve
    "Grabbing my blade, I stepped out..."
    "But it wasn't a threat."
    "It was the same desert fox."
    show cg_jackal_girl_baby at center_f with ease
    "She approached, carefully cradling a small, furred baby in her arms."
    "Her tail swished as she looked up at me, as if to say: {i}'Look at what we made.'{/i}"
    show cg_jackal_girl_baby at cright_f with ease
    "I reached out instinctively, but she stepped back."
    MC @sad "U-Uhh... Do you need anything from me?"
    JACKAL_GIRL @think "...?"
    MC @sad "For the child, I mean—do you—"
    show cg_jackal_girl_baby at blurin, cright
    hide cg_jackal_girl_baby with easeoutright
    "But she turned away and fled before I could finish."
    "I stood there, stunned, watching her vanish once more into the desert dunes."
    $ PregJackalGirl().NumBabiesShown = PregJackalGirl().NumBirths
    if PregJackalGirl().NumBabiesShown == 1:
        if not QstIsOver(EventFirstImpreg):
            $ QstStart(EventFirstImpreg)
    return

label jackal_girl_sexscene:
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    $ tmpvar = {}
    $ tmpvar["preg"] = CharIsVisiblyPreg("jackal_girl")
    if tmpvar["preg"]:
        scene jackal_girl_missionary_preg_idle with dissolve
    else:
        scene jackal_girl_missionary_nopreg_idle with dissolve
    $ Pause()
    menu:
        "Put it in her pussy.":
            "On the floor, I rubbed my member against the creature's wet opening."
            "She let out soft, happy pants as her juices coated my cock."
            "Holding one of her legs in my arms, her soft tail swishes and brushes against me as her tight slit glistened in the light."
            MC "Are you ready for this?"
            JACKAL_GIRL "{i}*Pant* *Pant!*{/i}"
            "She said nothing, but her sultry eyes refused to look away as she looked up expectantly for her {i}mate{/i} to take charge."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_slow with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_slow with dissolve
            $ Pause()
            "I carefully aligned my cock against her tight slit, pushing it slowly into her."
            "Her insides felt different than a humans... Ribbed with tiny bumps, less pronounced than mine, but incredible all the same."
            "She let out a sudden, soft rumble that sounded an awful lot like a moan."
            "She squeezed tightly around me, her tail swishing happily as I slid deeper into her."
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_fast with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_fast with dissolve
            $ Pause()
            "Somehow, even without words, like two rutting beasts, I understood her perfectly."
            "She panted hotly, and as I thrust faster into her eager hole, she howled with delight."
            "She trembled beneath my hands as I stroke her soft, sweaty fur."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_tentacle_head_slow with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_tentacle_head_slow with dissolve
            $ Pause()
            "Her eyes widen as the first of my tentacles slithered toward her."
            "She tilted her head, watching as it pushed into her throat."
            "She let out a startled yelp, but once the aphrodisiac kicked in, she rumbles with pleasure."
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_tentacle_head_fast with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_tentacle_head_fast with dissolve
            $ Pause()
            "I smiled, slamming my cock deep into her as if in a trance, her paws curling in pleasure."
            JACKAL_GIRL "{i}*Slurp!* *Pant!* *Slurp!* *Pant!*{/i} ❤️"
            JACKAL_GIRL "{i}Arrfff!{/i}"
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_tentacle_faceful_slow with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_tentacle_faceful_slow with dissolve
            $ Pause()
            "The tentacle cupped her face as it latched on. She didn't resist — just moaned."
            "Her cunt tightened and squeezed me as she drew closer to her own climax."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_tentacle_faceful_fast with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_tentacle_faceful_fast with dissolve
            $ Pause()
            "By now, I was slamming into her greedy hole, her squeals muffled by the tentacle down her throat."
            "Her tail swished erratically, and I could feel her heart racing."
            "She was close. But I was not done yet..."
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_vag_tentacle_booba_face with dissolve
            else:
                scene jackal_girl_missionary_nopreg_vag_tentacle_booba_face with dissolve
            $ Pause()
            "Two more tentacles slithered around her, latching onto her breasts and suckling eagerly."
            "Her entire body trembled as I continued thrusting into her drenched pussy."
            "Even as she squirmed beneath me, I held her tight, rutting her without pause."
            "In this moment, she was mine. Mine to {i}devour{/i} completely."
            "She let out a howl-like moan, shaking as a powerful orgasm overtook her."
            "So caught up in the moment, I didn't realize how close I was."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            $ PregRoll("jackal_girl")
            $ ReduceInfectionFromSex("jackal_girl")
            if tmpvar["preg"]:
                $ UnlockGalFlag("jackal_girl", "missionary", "var_preg_vag")
                scene jackal_girl_missionary_preg_vag_finish with flash
            else:
                $ UnlockGalFlag("jackal_girl", "missionary", "var_nopreg_vag")
                scene jackal_girl_missionary_nopreg_vag_finish with flash
            $ UnlockGalSceneAndGrantXp("jackal_girl", "missionary")
            $ Pause()
            "With a final series of thrusts, I buried myself deep and flooded her womb with my seed."
            "She clenched tight around me, but by now she was exhausted."
            "As I pulled out, she let out a soft whimper, and my cock freed itself with a slick sound."
            "Her tail still wagged gently as she panted in the afterglow."
            scene black with dissolve
            "I knew she wouldn't be moving for a while... but I also knew I had to return to the path at once."
            "As I left, I swear I caught a glimpse of her silhouette trailing me for a few more miles before she finally vanished altogether..."
            pass

        "Put it in her ass.":
            "On the ground, I pressed the head of my cock against her tight rosebud."
            "She twisted her head to look towards me, panting and confused."
            "Holding her leg up, her tail swished as her asshole twitched under my touch."
            MC "Are you ready for this?"
            JACKAL_GIRL "{i}A-Aroo?{/i}"
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_slow with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_slow with dissolve
            $ Pause()
            "She didn't speak, but watched intently as I pressed into her tight ring."
            "Her mouth opened with a sharp howl as I pushed the head inside."
            "Her ass squeezed around me, resisting at first, but as I slid in deeper with practiced ease,"
            "Her eyes at first showed confusion — but she didn't resist, and soon, her body started to relax."
            "Still though, I felt like I could almost read her thoughts as she looked up to me, cock rammed firmly in her ass."
            "{i}'You put it THERE instead of where it belongs... now what?'{/i}"
            "Her asshole pulsed around my shaft as she looked back at me."
            "I moved slowly, letting her adjust. As I went deeper, she began to pant once more."
            "Soft rumbles escaped her lips. She was starting to enjoy it."
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_fast with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_fast with dissolve
            $ Pause()
            "Her ass gripped me like a vice, her tail brushing up along my side."
            "Again, like rutting beasts, we didn't need words to understand each other."
            "I thrust harder, and her moans only grew louder."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_normal.ogg", 1)
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_tentacle_head_slow with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_tentacle_head_slow with dissolve
            $ Pause()
            "Her eyes widened as the first tentacle crept forward and pushed into her throat."
            "She gagged, then moaned, the aphrodisiac having done it's work."
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_tentacle_head_fast with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_tentacle_head_fast with dissolve
            $ Pause()
            "Her paws curled, overcome with pleasure."
            JACKAL_GIRL "{i}*Slurp!* *Pant!* *Slurp!* *Pant!*{/i} ❤️"
            JACKAL_GIRL "{i}Arrfff!{/i}"
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_tentacle_faceful_slow with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_tentacle_faceful_slow with dissolve
            $ Pause()
            "The tentacle cupped her face, pulsing steadily."
            "She didn't resist, her ass tightening involuntarily."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_tentacle_faceful_fast with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_tentacle_faceful_fast with dissolve
            $ Pause()
            "I pounded into her greedy ass, her muffled squeals pushing me further toward the edge."
            "Her tail thrashed wildly, her body trembling from the stimulation."
            "But I was not finished."
            if tmpvar["preg"]:
                scene jackal_girl_missionary_preg_anal_tentacle_booba_face with dissolve
            else:
                scene jackal_girl_missionary_nopreg_anal_tentacle_booba_face with dissolve
            $ Pause()
            "Two more tentacles latched onto her breasts, suckling greedily."
            "She spasmed beneath me, unable to handle the overload of pleasure."
            "Even as she writhed, I held her firm, thrusting into her tight, stretched rear."
            "She was mine. Mine to {i}devour{/i} completely."
            "She howled into the tentacle as a powerful orgasm wracked her body."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            $ ReduceInfectionFromSex("jackal_girl")
            if tmpvar["preg"]:
                $ UnlockGalFlag("jackal_girl", "missionary", "var_preg_anal")
                scene jackal_girl_missionary_preg_anal_finish with flash
            else:
                $ UnlockGalFlag("jackal_girl", "missionary", "var_nopreg_anal")
                scene jackal_girl_missionary_nopreg_anal_finish with flash
            $ UnlockGalSceneAndGrantXp("jackal_girl", "missionary")
            $ Pause()
            "I was too far gone. With a final thrust, I slammed deep and empty myself into her bowels."
            "She clenched tightly as I pulled out, her body now limp, but her tail still wagged weakly."
            "My seed seeped from her ass as she panted softly."
            scene black with dissolve
            "I knew she wouldn't be moving for a while... but I also knew I had to return to the path at once."
            "As I left, I swear I caught a glimpse of her silhouette trailing me for a few more miles before she finally vanished altogether..."
            pass
    $ AutoMus(True)
    $ tmpvar = {}
    return