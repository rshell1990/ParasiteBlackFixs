label vizura_caravan_battle:
    $ QstComplete(VizuraCaravan)
    show vizura surp
    GOBLIN "...Oh fuck!"
    show vizura angry
    GOBLIN "BOYS! GET OUT HERE! WE GOT TROUBLE!"
    "A scurry of goblins with spears hurried out of the caravan, weapons ready!"

    $ AutoMus(False)
    $ PlayMusicRandom("mus_battle_generic")
    $ tmpvar = ["e_goblin", "e_goblin"]
    if GetPartySize() > 1:
        $ tmpvar.append("e_goblin")
    if GetPartySize() > 2:
        $ tmpvar.append("e_goblin")

    $ StartBattle(BattleData(BackgroundImage = wLocs["travel_node_vizura_caravan"].bgImage, CharIDList_Right = tmpvar))
    $ tmpvar = {}
    $ LocFlush()
    show cg_goblin_caravan
    show mc angry at left with easeinleft
    "With the goblins dead at my feet, I approached the caravan doors and pried them open to loot whatever was inside."
    "Inside, the caravan was filed with armour and weapons and trinkets ... But that wasn't what drew my eyes' attention."
    "A singular goblin, still alive and sat in the center of the caravan holding a barrel of what seemed to be some powder,"
    "...raised his middle finger to me and snarled before slashing at the powder to trigger a spark."
    $ DamagePlayer(CharGetVar("mc", "Health") * 0.5)
    if CharGetVar("mc", "default_look") == "father_armor":
        $ CharSetVar("mc", "default_look", "father_armor_ash")
    hide cg_goblin_caravan
    hide mc
    play sound "audio/cfx/explosion.ogg"
    play sound2 "audio/cfx/fire_burning.ogg" loop
    show cg_goblin_caravan_on_fire
    with flash
    $ Pause()
    "Before I could stop him, the huge explosion sent me hurdling backwards as the caravan was engulfed in flames."
    show mc at left with easeinleft
    "The intense heat made me wince in pain as I painfully coughed up and exhaled the black smoke I had breathed in."
    $ AutoMus(True)
    show mc angry at center with dissolve
    if CharInParty("markus"):
        show markus at left with easeinleft
        MARKUS @shock "FUCK! Are you okay?"
        MC @angry "{i}*Cough!* *Cough!*{/i} I'm fine, just... Urghh!"
        MARKUS @angry "Green skins ... Can't trust any of them."
        MARKUS "You did the right thing, she'd have sunk a dagger in your back the moment she had a chance!"
        hide markus with dissolve
    if CharInParty("myu"):
        show myu scared at left with easeinleft
        MYU @talk "MYUUUUU!"
        MYU @sad "Myu was really scared!"
        MC @sad "Sorry - {i}*Cough!*{/i} Myu ... I'll try be more careful next time."
        MYU @scared "N-No fight unless have to!"
        hide myu with dissolve
    if CharInParty("elena"):
        show elena angry at left with easeinleft
        ELENA @shock "What in all of the hells did you do that for?!"
        MC @angry "{i}*Cough!* *Cough!*{/i} It was a trap!"
        ELENA @angry "You don't know that!"
        ELENA @angry "That was MADNESS!"
        if CharInParty("markus"):
            show markus at right with easeinright
            MARKUS @angry "Lay off she-wolf, you can't just assume everything is out to shake your hand and cuddle you!"
            ELENA @angry "WE DIDN'T EVEN GIVE THEM A CHANCE!"
            MARKUS @angry "They were armed! What more do you need?"
            ELENA @angry "EVERYONE IS ARMED ON THESE ROADS!"
            "Angrily, Elena stormed off, furious at what had happened."
            $ CharChangeRel("elena", -1)
            $ DialogueElena().PsychoPoints += 1
            hide elena
            with dissolve
            MARKUS "...She'll calm down eventually."
            hide markus
            with dissolve
        else:
            "Angrily, Elena stormed off, furious at what had happened."
            hide elena
            with dissolve
    hide mc with dissolve
    "Looking over at the now ruins of the caravan turned black from the intense flames, I couldn't help but wonder if I'd made the right decision?" 
    $ Pause()
    stop sound2 fadeout 1.0
    scene black with dissolve
    if CharGetVar("mc", "default_look") == "father_armor_ash":
        $ CharSetVar("mc", "default_look", "father_armor")
    $ GetOutToWorldMap()