init python:
    # its like just a flag
    @AppendToAllQuests
    class EventCrashedShipEncounter(LogicModule):
        def __init__(self):
            super().__init__()

######################################################################################################################################################
# Crashed ship encounter (rare, only 15% chance event triggers) – can only trigger ONCE in Act 2
label travel_event_crashed_ship:
    $ QstComplete(EventCrashedShipEncounter)
    show mc at center with easeinleft
    BLACK "{i}...Going wrong way.{/i}"
    show mc at shake
    MC @angry "We are not going the wrong way!"
    BLACK "{i}We are lost.{/i}"
    MC @angry "We are not lost!"
    show mc at blurin, center_f
    MC @talk "We just—"
    show mc at blurin, center
    MC @talk "We just need to find our—"
    play sound "audio/cfx/earthquake.ogg"
    "Suddenly, I felt the earth crumble beneath me."
    play sound2 "audio/cfx/earthy_rustle.ogg"
    hide mc with easeoutbottom
    "I gasped as I plummeted into a great chasm below."
    scene black with dissolve
    "The fall lasted only moments, wind whipping past as panic surged through me."
    "One of my blackened tentacles shot out, anchoring into the wall and halting my descent."
    MARKUS @shock "[player_name!t]!"
    stop sound fadeout 3.0
    "Lowering myself carefully, I landed on a patch of dirt below, lit faintly by the chasm's natural opening."
    MARKUS "Can you hear me?!"
    MC @talk "I'm alright."
    "As my eyes adjusted, the full scale of the pit became clear."
    scene cg_crashed_ship_cave
    show mc at left
    with dissolve
    $ AutoAmb(False)
    stop ambience fadeout 5.0
    MC @think "Is this... some kind of cave?"
    $ Pause()
    "There, partially submerged in shallow water, was something metallic—a ship?"
    "Ruined and entangled in vines, the strange relic beckoned."
    MARKUS "What do you see down there?!"
    MC @serious "You might want to come down here."
    show mc at cleft with easeinleft
    "The others climbed down with caution."
    show markus at left with easeinleft
    MARKUS @shock "What in seven hells is that thing?"
    MC @think "Some kind of ship?"
    MARKUS @talk "Where are its sails?"
    MC @think "Never seen a vessel like this... and this far from any sea?"
    #
    if CharInParty("myu"):
        show myu at center
        MYU @scared "M-Myu? Metal thing scary..."
        hide myu with easeoutright
    #
    if CharInParty("ves"):
        show ves at center
        VES @think "I've heard rumors of the Greater Trading Company reinforcing ships with armor, but this..."
        VES @talk "This is nothing like anything I've ever seen."
        hide ves with easeoutright
    #
    if CharInParty("elena"):
        show elena at cright_f with easeinright
        ELENA @grumpy "Perhaps... a relic of the old gods?"
        ELENA @grumpy "Judging by how deep this cavern is, it must've been buried here for thousands of years."
        show elena at blurin, cright
        hide elena with easeoutright
    #
    if CharInParty("sypha"):
        show sypha at center
        SYPHA @talk "{i}And so, in ages past, they rode mechanical beasts across the stars.{/i}"
        MC @think "What?"
        SYPHA @think "Nothing. Just old legends from childhood."
        hide sypha with easeoutright
    #
    menu:
        "Explore the strange 'ship.'":
            call travel_event_crashed_ship_inside from _call_travel_event_crashed_ship_inside
        "Leave.":
            MC @serious "Whatever it is, I don't like it."
            MC @talk "Let's leave sleeping ghosts to rest."
            MARKUS @talk "Agreed. Nothing good comes from disturbing the dead."
            scene black with dissolve
            "We climbed back out of the rift and resumed our journey."
    $ AutoMus(True)
    $ AutoAmb(True)
    $ GetOutToWorldMap()

label travel_event_crashed_ship_inside:
    hide mc with easeoutright
    "Carefully, I approached the wreck."
    "I stepped into the freezing water and laid my hand on the cold metal hull."
    show markus at center with easeinleft
    show markus at shake
    MARKUS @shock "[player_name!t]! What are you doing?"
    play sound "audio/cfx/spaceship_door_open.ogg"
    "A hiss of steam sounded as the metal twisted open like a door."
    MARKUS @shock "You're not actually going inside that thing, are you?"
    "I stepped in."
    MARKUS @angry "Gods be damned, man."
    hide markus with easeoutright
    scene black with dissolve
    $ AutoMus(False)
    $ PlayMusic("audio/music/9_Burned_T.ogg")
    "Inside, it was cold."
    scene cg_crashed_ship_interior with dissolve
    show mc at left
    "Our footsteps echoed across the metal floor."
    "Pipes snaked along the walls, choked in vines and pierced by jagged rock."
    
    show mc at center with easeinleft
    show markus at left with easeinleft
    play sound "audio/cfx/holo_hum.ogg"
    "A ghostly figure flickered into view inside a glowing circle."
    MC @angry "Who are you, specter?"
    ANDRAS "This is Captain Andras of the Maylark."
    ANDRAS "Day four-hundred and ninety-six since the end of... well, everything."
    MARKUS @think "Uhhh... hello?"
    MC @think "I don't think he can hear us."
    ANDRAS "...{i}*Sigh*{/i} I don't even know why I bother with these things anymore."
    ANDRAS "It's not like there's actually anyone left to log it."
    ANDRAS "For over a year and a half we've jumped from one dead star to the next."
    ANDRAS "One nightmarish, monster infested world to another, searching for someplace safe."
    ANDRAS "I still tell the crew that's what we're looking for... Someplace safe."
    ANDRAS "I'd just settle for finding some food, fuel... anything now."
    ANDRAS "It's been months since we found any survivors."
    ANDRAS "Well, unless you count the cannibals and freaks."
    ANDRAS "... We have enough fuel for one last try, some unknown world ready on the edge of the Zelma ring."
    ANDRAS "Atmospheric readings look good from orbit, and there seems to be no visual signs of corruption."
    ANDRAS "We'll probably stall out on the landing, but hopefully with power routed to the shields, we can at least survive the crash."
    ANDRAS "May the new gods... Ahhh, fuck it."
    ANDRAS "{i}It's not like they're listening anymore anyway.{/i}"
    "There was momentary flickering of the strange figure summoned."
    ANDRAS "Day, five hundred and two."
    ANDRAS "We survived the landing, but the ship's hull is too badly damaged to repair."
    ANDRAS "{i}*Chuckles*{/i} Not that we have to fuel left to go anywhere anyway."
    ANDRAS "The crew and I have decided to salvage what we can from the ship and head out."
    ANDRAS "Maybe we can etch out some kind of existence out here."
    ANDRAS "It might be a simple life... {i}But at least we're alive.{/i}"
    ANDRAS "... The gods."
    ANDRAS "How the fuck did it come to this?"
    ANDRAS "We blame it all on Malakai and his damned war, but in the end, maybe it was just our blind faith that sealed our fates."
    ANDRAS "We always presumed the gods were better than us, wiser, {i}more{/i} than us."
    ANDRAS "{i}But in the end, they fell to all the same trappings we do.{/i}"
    ANDRAS "{i}And they dragged everyone down with them.{/i}"
    ANDRAS "... Fuck the gods."
    ANDRAS "This is Captain Andras of the Maylark, signing off for the last time."
    "The image flickered, then began replaying."
    show mc at cright with ease
    show mc at blurin, cright_f
    MC @think "What do you make of that?"
    show markus at cleft with easeinleft
    MARKUS @talk "Jumping stars... Malakai's war... If this is from the Second War of the Gods... it's ancient."
    #
    if CharInParty("sypha"):
        show sypha at left with easeinleft
        SYPHA @talk "We shouldn't linger."
        SYPHA @think "Let ghosts rest."
        show sypha at blurin, left_f
        hide sypha with easeoutleft
    #
    hide markus with easeoutright
    show mc at center_f with ease
    show mc at blurin, center
    menu:
        "Look around for something to salvage.":
            "Most of it had decayed."
            "Anything that once had purpose crumbled in my hands."
            "Except... one thing."
            "A small metal box."
            "Inside, a glowing blue crystal pulsed rhythmically."
            menu:
                "Grab it.":
                    show mc at nod
                    "I reached in and took the orb."
                    "It detached easily from its cables."
                    "As I did, the specter's loop stopped."
                    show mc at cleft with ease
                    show markus at cright_f with easeinright
                    MARKUS @angry "What did you do?"
                    MC @talk "I just took this."
                    MC @talk "Looks like a power crystal, doesn't it?"
                    MARKUS @think "Not like any I've seen."
                    MARKUS @talk "Let's get out of here."
                    $ PlayerAddItem("spaceship_crystal")
                    MC @talk "Yeah..."
                "Leave it.":
                    "I decided not to touch anything."
                    show markus at cright_f with easeinright
                    MARKUS @talk "Ready to go?"
                    MC @talk "Yeah, let's leave this place."
        "Leave.":
            MC @talk "Let's leave then."
    scene black with dissolve
    "We climbed out of the chasm and continued on."
    $ AutoMus(True)
    return