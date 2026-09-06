label travel_event_deer:
    "Whilst making my way through some meadows, I stumbled upon some deer grazing upon the grass."
    show cg_deer at cright_f with dissolve:
        yoffset -200
    "The thought crossed my mind that their hide and meat could prove valuable... {i}If we can catch them before they bolt.{/i}"
    menu:
        "Try and catch them." (Req_Agi = 10):
            $ rng = RngInt(1, 3)
            if rng == 1:
                "As I drew closer, I tried using one of my tentacles to spring and strike at the deer quickly!"
                "Rushing out to protect its mate, a stag came charging out, stood between me and my prize..."
                $ AutoMus(False)
                $ PlayMusicRandom("mus_battle_generic")
                $ StartBattle(BattleData(BackgroundImage = TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = ["e_stag"]))
                $ LocFlush(dissolve)
                $ AutoMus(True)
                "As the stag fell, the doe had long since sprinted off..."
                "Still though, the stag's hide and meat would prove worthwhile in itself."
            if rng == 2:
                "As I drew closer, I tried using one of my tentacles to spring and strike at the deer quickly!"
                "As the tentacle pierced the soft, warm, flesh, the doe yelped in pain as the others fled."
                hide cg_deer with dissolve
                "The doe quickly collapsed to the floor, shaking briefly before I put the thing out of it's misery with a quick blow."
                "As the red, warm blood pooled, I pulled out a small knife and began to skin my prize..."
                $ PlayerAddItem("animal_hide")
                $ PlayerAddItem("red_meat")
            if rng == 3:
                "I drew closer towards them, ready to strike with a tentacle I planned to spring from my palm like a spear."
                "Unfortunately, after feeling a fallen branch snap beneath my feet, the spooked deer bolted before I could make my move."
                show cg_deer at shake
                hide cg_deer with easeoutright
                MC "(Damn!)"
                MC "(Perhaps next time...)"
        "Leave them alone.":
            "Deciding to leave the deer alone, I simply walked on by and continue to let them continue grazing in peace."
            hide cg_deer with dissolve
    return