label travel_event_wolves:
    show mc at left with easeinleft
    "While trekking my way through the forests, I heard the distinct sound of...{i}howling?{/i}"
    "From the tree lines, a pack of hungry wolves descended upon me, snarling and circling."
    menu:
        "Snarl back" (Req_Perk = "terrifying"):
            "The wolves whined and howled as they scattered the winds."
            MC "(Damn beasts!)"

        "{image=[ICON.SWORDS]} Fight!":
            $ AutoMus(False)
            $ PlayMusicRandom("mus_battle_generic")
            $ StartBattle(BattleData(BackgroundImage = TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = ["e_wolf", "e_wolf", "e_wolf"]))
            $ AutoMus(True)
            $ LocFlush(dissolve)
            "With the last of the wolves yelping out in anguished pain, I quickly put the thing out of its misery."
            MC "{i}*Sigh*{/i}"
            MC "(These poor things are half-starved, no wonder they're attacking on sight...)"

        "Let Elena handle them." if CharInParty("elena"):
            show elena at cleft with easeinleft
            MC @think "I don't suppose {i}you{/i} could handle this?"
            ELENA "I mean, {i}I could try.{/i}"
            hide elena with easeoutright
            "Elena stepped forward and snarled towards the wolves, who tilted their heads curiously in understanding."
            "After some brief barking, Elena turns towards you."
            ELENA @sad "They're starving... They only want some food, and they'll leave us alone."
            menu:
                "Throw them some meat." if PlayerItemQty("strange_meat") > 0 or PlayerItemQty("red_meat") > 0:
                    if PlayerItemQty("strange_meat") > 0:
                        $ PlayerRemItem("strange_meat")
                    elif PlayerItemQty("red_meat") > 0:
                        $ PlayerRemItem("red_meat")
                    $ DialogueElena().FedWolves = True
                    "Tossing the meat towards them, the wolves happily whined and barked as they chowed down."
                    "Satisfied with their meal, they sped off into the forests, their leader looking back to give one last bark of appreciation."
                    show elena at right_f with easeinright
                    ELENA @smile "Looks like you've made a few new friends..."

                "I have nothing to give.":
                    "The wolves sadly whined... but then, once more, they began to snarl and bear their fangs."
                    ELENA "I don't think they're taking no for an answer!"
                    $ AutoMus(False)
                    $ PlayMusicRandom("mus_battle_generic")
                    $ StartBattle(BattleData(BackgroundImage = TravelRoutes[TravelState.RouteID]["image_battle_bg"], CharIDList_Right = ["e_wolf", "e_wolf", "e_wolf"]))
                    $ AutoMus(True)
                    $ LocFlush(dissolve)
                    "With the last of the wolves yelping out in anguished pain, I quickly put the thing out of its misery."
                    MC "{i}*Sigh*{/i}"
                    MC "(Well, that could have gone better.)"

    return