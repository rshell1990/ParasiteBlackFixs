label qst_bloodhound_2_camp:
    MC "(Seems like this is the Guardians' camp.)"
    MC "(Let's take a closer look.)"
    menu qst_bloodhound_2_camp_menu:
        "A sword covered in blood":
            MC '(A blade covered in blood... But whose?)'
            jump qst_bloodhound_2_camp_menu
        "Torn up clothes":
            MC "(Some torn up clothes... Not a good omen.)"
            jump qst_bloodhound_2_camp_menu
        "Broken Mages staff":
            MC "(It's been snapped right in two.)"
            jump qst_bloodhound_2_camp_menu
        "A chained-up box" if PlayerItemQty("qst_draven_key") == 0:
            MC "(Hm? Why's this box been chained up?)"
            MC "(I could try tear it open... But I might damage whatever is inside.)"
            MC "(Maybe I should try and find a key first?)"
            $ QstTheBloodhound().sawChainedUpBox = True
            jump qst_bloodhound_2_camp_menu
        "A chained-up box" if PlayerItemQty("qst_draven_key") >= 1:
            MC "(Let's try open this...)"
            jump qst_bloodhound_2_lake_openbox
        "A sigil" if not "sigil" in QstTheBloodhound().clues:
            MC '(This looks like a guild party sigil... It must be them!)'
            MC "(But... Where are they? There's nobody in sight.)"
            $ QstTheBloodhound().clues.append("sigil")
            jump qst_bloodhound_2_camp_menu
        "A firepit" if not "note" in QstTheBloodhound().clues:
            MC "(An extinguished fire pit... Been dead for a while now.)"
            MC "(...Wait, there's something there in the pit!)"
            MC "..."
            MC "(A letter?)"
            "{i}We've captured a baby slimelark as per the clients request, but the big one is getting more and more agitated.{/i}"
            "{i}...Managed to hold it at bay for now, but-{/i}"
            MC "(The rest of it is burned beyond readability.)"
            MC '(I best stay away from the bank... For now at least.)'
            $ QstTheBloodhound().clues.append("note")
            jump qst_bloodhound_2_camp_menu
        "Leave":
            MC "(Let's move on.)"
            $ LocEnterQ()

label qst_bloodhound_2_lake_openbox:
    $ PlayerRemItem("qst_draven_key",1)
    $ LocFlush()
    show mc_transformed:
        xcenter 0.1
    with dissolve
    'As the lock dropped off the from the box, I opened it up to peer inside.'
    'Inside, a jar with an enchantment on it was filled with the slimelark-like substance.'
    MC '(This is what they came for.)'
    MC '(A baby slimelark.)'
    MC '(Well, what should I do with it?)'
    menu: 
        '{image=[ICON.DEATH]} Throw the jar into the lake':
            'While what happened here was no doubt horrific, something about punishing the youngling felt wrong.'
            'Even if it {i}was{/i} the offspring of a slimelark.'
            'With the jar in hand, I threw it straight into the lake, watching as it plumetted down with a splash.'
            play sound2 "audio/cfx/water_splash.ogg" volume 0.3
        '{image=[ICON.DEATH]} Destroy the creature':
            'Looking around at the horror inflicted by one of these beasts, I decided it was simply too much risk to keep it alive.'
            'It was young now... But it would grow up.'
            'Shattering the glass, the slimelark squealed in a death cry as I hacked away at the thing till it dissolved like its parent.'
            play sound2 "audio/cfx/bottleBreak.ogg"
            play sound "audio/cfx/slimelark_die.ogg"
        '{image=[ICON.HEART]} Take the jar with you':
            'For some strange reason, I felt compelled to take the jar with me.'
            'Oddly, as I held up the jar to inspect it more, the colour of the slime briefly turned pink.'
            'I thought for a moment I could hear a soft cooing sound from inside the jar, but after a few seconds more of inspection, the thing was silent again.'
            $ PlayerAddItem("qst_slime_jar", 1)
            MC "(I hope I don't end up regretting this.)"
    $ LocEnter()