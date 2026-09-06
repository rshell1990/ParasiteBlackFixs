label travel_event_raider:
    show mc at left with easeinleft
    "While making my way along the roads, I suddenly had the strangest sense something was wrong..."
    BLACK "({i}Enemies ... all around us{/i})."
    show mc angry
    "A flying arrow suddenly landed itself at my foot, barely missing me as I drew my blade."
    "From out of their hiding spots, charged the group of bandits!"
    show cg_raider at right_f
    with moveinright
    MC "(Shit!)"
    BANDIT "Give us everything you've got or we'll pry it from your dead fucking hands!"

    if Travel_GetCurrentBiome() == "forest" and DialogueElena().FedWolves:
        $ DialogueElena().FedWolves = False
        BANDIT "Let's make this easy now, give us your-"
        "Suddenly, the bandit was toppled over in a flash, screaming as a wild wolf tore at his throat."
        BANDIT "AHHHHHHRGHHHH! GET IT OFF ME! GET IT FUCKING-"
        "Silence, choking on his blood as he clutched at his torn-out throat, the other bandits panicked as they desperately tried to either run away or rush over."
        "One by one, in quick succession, they were pulled and dragged down by the wolves who sprung out from the tall grass, howling with delight as they pressed their fangs into the warm blood and flesh."
        if CharInParty("elena"):
            "My heart racing, I held my hand on the hilt of my blade, ready to draw it, when I felt Elena's hand on my shoulder."
            ELENA "Keep your blade sheathed."
            ELENA "They're letting us pass..."
            "The leader of the pack looked up towards us, mouth covered in blood and panting."
            "He barked happily, before tucking back into his {i}'meal.'{/i}"
            ELENA @smile "Told you that you'd made new friends..."
        return

    menu:
        "{image=[ICON.SWORDS]} I don't think so...":
            BANDIT "HAVE IT YOUR WAY!"
            
            $ tmpvar = {}
            $ tmpvar = ["e_raider"] # We are balancing the battle
            if GetPartySize() > 1:
                $ tmpvar.append("e_bandit")
            if GetPartySize() > 2:
                $ tmpvar.append({"e_thug":2})
            if GetPartySize() > 3:
                $ tmpvar.append({"e_bandit":2})
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = tmpvar))
            $ tmpvar = {}
            $ AutoMus(True)
            "With the last of the bandits slain and dead at my feet, I carried on, leaving their corpses for the crows." 

        "I'll slaughter each and every one of you, and when I'm done, I'll wear your flayed skin as a trophy to show to your loved ones." (Req_Perk = "terrifying"):
            BANDIT "F-Fuck this! Boys! We're out of here!"
            hide cg_raider
            with moveoutright
            "The trembling bandits fled from where they came."
            hide mc
            with dissolve
        
        "There's no need to fight, I know where a much better haul is..." (Req_Charm = renpy.random.randint(5, 7)):
            "{i}After spending some time trying to convince them about about a caravan ambushed by Demorai down the road back the way I came...{/i}"
            BANDIT "Hmm, alright, you can go."
            BANDIT "But if we find you're lying, you're fucking dead!"
            hide cg_raider
            with moveoutright
            "The bandits left in the direction I pointed."
            show mc smile
            MC "(Idiots.)"
            hide mc
            with dissolve

        "I'll give you what you want...":
            BANDIT "Hand it over! Heh!"
            $ PlayerRemItem("gold", PlayerItemQty("gold"))

    return
