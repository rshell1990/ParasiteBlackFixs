label gallery_lizard_anal:
    $ PlayMusicRandom("mus_sex")
    if GalFlagCount("skaliths", "anal") >= 2:
        "Was she..."
        menu:
            "A desert Skalith?" (AppearIf = GalFlag("skaliths", "anal", "red")):
                $ tmpvar = "red"
            "A forest Skalith?" (AppearIf = GalFlag("skaliths", "anal", "green")):
                $ tmpvar = "green"
            "A lake Skalith?" (AppearIf = GalFlag("skaliths", "anal", "blue")):
                $ tmpvar = "blue"
    else:
        if GalFlag("skaliths", "anal", "red"):
            $ tmpvar = "red"
        if GalFlag("skaliths", "anal", "green"):
            $ tmpvar = "green"
        if GalFlag("skaliths", "anal", "blue"):
            $ tmpvar = "blue"
#######################################
    "With my tentacles holding her firmly in place, I placed a clawed hand onto her soft, scaly ass."
    "I stared for a moment at her welcoming holes, glistening and silk-like in the light, as my cock twitched in excitement for what was to come."
    "As I pushed my cock against her silk-like asshole, she jerked for a moment in surprise, letting out a nervous-sounding hiss as she looked back towards me with uncertain eyes."
    "Continuing to prod against the hole, she didn't stop me, but I could feel her body tense slightly."
    $ PlaySexFx("audio/sex_sounds/forgean_100.ogg", 1)

    if tmpvar == "red":
        scene lizard_red_anal_slow with dissolve
    if tmpvar == "green":
        scene lizard_green_anal_slow with dissolve
    if tmpvar == "blue":
        scene lizard_blue_anal_slow with dissolve
    $ Pause()

    "I pushed the head in slowly at first, and as her tight asshole stretched and squeezed around my cock, I growled in approval."
    "She let out another short hiss of surprise; she was certainly not accustomed to taking things back {i}there.{/i}"
    "Still, though, she didn't lash out, and as I felt her relax slightly, slowly, I sunk the rest of my cock into her ass."
    "Her tight, cool asshole stretched around me with surprising ease as I pushed myself fully into her."

    if tmpvar == "red":
        scene lizard_red_anal_fast with dissolve
    if tmpvar == "green":
        scene lizard_green_anal_fast with dissolve
    if tmpvar == "blue":
        scene lizard_blue_anal_fast with dissolve
    $ Pause()

    "As she felt herself stretch to accommodate my size, she hissed in surprise, squirming slightly between my tentacles,"
    "but the tension in her body soon relaxed as she began to feel myself glide in and out of her."
    "She rumbled quietly in approval, looking back in a mixture of confusion and... {i}arousal.{/i}"
    
    if tmpvar == "red":
        scene lizard_red_anal_tentacle_slow with dissolve
    if tmpvar == "green":
        scene lizard_green_anal_tentacle_slow with dissolve
    if tmpvar == "blue":
        scene lizard_blue_anal_tentacle_slow with dissolve
    $ Pause()

    "I wondered if she fully understood what I was doing to her, {i}but it was clear she liked it either way.{/i}"
    "Now comfortably inside of her, I began to move faster, slamming my hips up against her ass as she cooed happily, pressing her cool scaly butt back up against me with every thrust."
    "As she looked over her shoulder towards me, I couldn't help but wonder if she was... {i}smiling?{/i}"
    "I wasn't sure if she was even capable of that kind of emotion, but as she observed my expressions, I could see a curious need to ensure her {i}mate{/i} was sufficiently satisfied."
    "I gently slapped at her butt, and she let out a small hiss, my clawed hand squeezing at her ass, feeling the thin layer of fat squish between my fingers."
    "Or perhaps her lizard brain was overwhelmed with all these new intense sensations?"

    if tmpvar == "red":
        scene lizard_red_anal_tentacle_fast with dissolve
    if tmpvar == "green":
        scene lizard_green_anal_tentacle_fast with dissolve
    if tmpvar == "blue":
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

    if tmpvar == "red":
        scene lizard_red_anal_finish with dissolve
    if tmpvar == "green":
        scene lizard_green_anal_finish with dissolve
    if tmpvar == "blue":
        scene lizard_blue_anal_finish with dissolve
    $ Pause()

    "Her eyes widened in surprise as the thick stream of my seed poured into her lightly bloating stomach."
    "She trembled and shook, her eyes rolling up as her body convulsed and tightened with her orgasm as I continued to spill the last of my seed into her backdoor."
    "Finally, fully drained by my little Skalith slut, I unsheathed my cock from her now well fucked ass and left it dangling behind her."
    "As I let my tentacles go slack, the Skalith, standing back on her feet, scurried away into the tall grass, but not before taking one last look at me before she vanished completely."
    return
    