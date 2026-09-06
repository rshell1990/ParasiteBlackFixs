#define LENIN = Character("Lenin")
#define SPECTER = Character("Biggie Smalls")
#define SWEETIE = Character("Sweetie Fox")
#define HAMUN_GUARD = Character("Hamun Guard")
define VISNA = Character("Visna")

# TEST QUEST - absolutely not meant to make it into the final game.
# follow existing project patterns and use the logic module system
# the quest should return cleanly to normal gameplay after completion
###############################
# QUEST: The Dark Specter of Biggie Smalls
###############################
# Quest description:
# Garen Quiltshire has summoned me to deal with something urgent... I should find out what it is.
# While walking around Hamun, the player is approached by a Hamun city guard to trigger the quest.
label test_script1: 
    HAMUN_GUARD "You are summoned at once to speak to Garen Quiltshire."
    menu:
        "What now?":
            HAMUN_GUARD "GO AT ONCE!"
            # loops back to menu
        "You're not my dad! You can't tell me what to do!":
            HAMUN_GUARD "HA! I have the lead developer on my side, fool!"
            # loops back to menu
        "Tell the git I shall be there.": 
            # proceeds the main quest forward
            HAMUN_GUARD "ANOTHER WIN FOR CAPITALISM!"
            pass

# Quest starts here.
# Quest journal update: Meet Garen Quiltshire at {i}The Pale Dragon.{/i}
###############################
# The player clicks on Garen's sprite / speaks to him at The Pale Dragon.
    GAREN @smile "You have made it, good!"
    GAREN @think "I have been avoiding paying the IRS for years, and made the unfortunate decision of hiding some obscure records with an ancient deity mankind scarcely understood."
    GAREN @talk "The dark specter Biggie Smalls, a being who was sealed away after years of conflict with the wizard Tupac."
    GAREN @talk "Help me, and I shall reward you with a SINGLE coin!"
    menu:
        "Yes.":
            # Accept quest. Reward = 1 gold.
            pass
        "No.":
            GAREN @angry "UNACCEPTABLE! THE DEVELOPER WILL NOT ALLOW IT!"
            GAREN @talk "Return when you have found sense!"
            # IMPLEMENT: exit/re-enter dialogue without advancing.

            # If the player speaks to Garen again, he says: "Have you reconsidered my offer?"
            # Then return to this choice menu.
        "Give me one thousand coins or I report you myself.": # Available with Barter 8+.
            GAREN @angry "Damn you boy! I agree!"
            # Accept quest. Reward = 1,000 gold.
            pass
        "Nah, I can make more money just by growing tits, I have the perk you know!": # Available with Feminine Charm perk.
            GAREN @shock "You strike a hard bargain! Show me!"
            # Temporarily transform the player to the female form
            MC @smile "Like this?"
            GAREN @smile "Wonderful tits! You are right! I shall raise the bargain to one hundred coins!"
            # Restore the player's previous form/state afterwards rather than assuming a default state.
            # Accept quest. Reward = 100 gold.
            pass

    GAREN @talk "To summon Biggie, you must first battle Vladimir Lenin to win the sword and mantle of 'Russianest Russian ever.' You may find him hanging out at the library."
    GAREN @talk "You must also take this, and give Sweetie Fox this feline creature! It is the only way!"
    GAREN @talk "You may find her at the brothel ONLY at night!"
    GAREN @talk "Go now! Hurry!"
    GAREN @talk "Complete your tasks and return."

# Give the player the QUEST ITEM 'Feline' - a small cat to be delivered to Sweetie Fox. Value: 9999.
# Show BOTH objectives at the same time and allow them to be completed in either order:
#   1. Defeat Lenin at the library.
#   2. Give Sweetie Fox the cat. She can be found at brothel at night
# Only show "Return to Garen Quiltshire" once both objectives are complete.

##############################
# While the Lenin objective is active, entering the correct Hamun library location should expose an interaction:
# "Summon Lenin's ghost."
# Remove/disable it after Lenin has been defeated.
    LENIN "STALINNNNNNN!?! WHAT HAVE YOU DONE?!"
    LENIN "AND WHY AM I HERE?!"
    LENIN "Oh bother... Just die already!"
    # Battle against Lenin's ghost + TWO existing bandit enemies.
    # Assign sensible test stats to Lenin using the existing enemy/battle patterns.

    # After victory:
    LENIN "Shit..."
    LENIN "I am defeated!"
    LENIN "I crown you now an honorary Russian! Take this blade to defeat Biggie!"
    # Add weapon: "Trotsky's Bane".
    # Complete ONLY the Lenin objective here.



############################### 
# This quest interaction is only available at the brothel at NIGHT.
    SWEETIE "May I help you champion?"
    menu:
        "Here, take this.": # Only available if the player has the Feline quest item.
            # Remove the Feline from inventory here.
            SWEETIE "I thank you brave knight, wanna see my tits?"
            menu:
                "Yes.":
                    SWEETIE "Here you go."
                    # Brief existing CG/sprite change is fine; no new art required.
                    SWEETIE "Hope you enjoyed the view."
                    #Advance quest
                    pass
                "No.":
                    SWEETIE "Well that's gay, but okay."
                    # Advance quest
                    pass
        "I do not have it.": # Only available if the player does NOT have the Feline.
            SWEETIE "Return when you do!"
            # Exit conversation without advancing the objective.
            pass

    # Only continue to this reward after the Feline has actually been handed over.
    SWEETIE "Here sir knight, take this armor and use it to defeat Biggie."
    # Add armor: "Gooner Armor".
    MC @smile "THANK YOU!"
    # Complete ONLY the Sweetie objective here.



# If both Lenin + Sweetie objectives are now complete, update quest objective to: Return to Garen Quiltshire.
###############################
    GAREN @talk "You have returned! And I see you have completed my tasks! I can summon Biggie to battle whenever you are ready!"
    menu:
        "Summon him.":
            GAREN @talk "Excellent!"
            # Continue into the Biggie sequence.
            pass
        "Do not.":
            GAREN @talk "Well... I guess I'll just stand here and wait then?"
            # EXIT the dialogue here. Do NOT fall through into the summoning scene.
            # Speaking to Garen again should offer this menu again.
            pass

    # Only reached after choosing "Summon him."
    "The tavern suddenly tore itself apart as the great specter appeared."
    SPECTER "YOU DARE SUMMON THE NOTORIOUS?"
    SPECTER "FIGHT ME!"
    # BOSS BATTLE against Biggie
    # losing should allow the player to try again rather than falsely completing the quest.
    # After victory:
    SPECTER "You have defeated me, I will now return your records so you can continue defrauding the governments."
    # after defeat:
    "You failed to defeat Biggie. Retry?"
    # show yes/no menu

    # Add QUEST ITEM: "Dodgy Tax Receipts" scroll.
    SPECTER "Here, enjoy this free bitch as well."
    # Nijah enters.
    MC @smile "Nijah! What are you doing here?!"
    SPECTER "REMEMBER G, WITH GREAT POWER, COMES GREAT BITCHES." 
    # Specter/Biggie exits off-screen.
    NIJAH @smile "I have come to ride your cock like a mindless fuck doll!"
    menu:
        # Implement using the existing Nijah remake cowgirl scene assets up on the drive.
        "Yessss!": 
            # the scene should have all that a typical sex scene has:
            # sex music, sex sounds, infection loss, gallery scene etc
            # nijah_cowgirl_webm_1
            NIJAH "YES! SO GOOD!"
            NIJAH "YOU TRULY ARE THE PLAYER!"
            NIJAH "HUZZAH!"
            # nijah_cowgirl_webm_2
            NIJAH "DID I LEAVE THE OVEN ON?"
            NIJAH "DON'T FORGET TO WATCH THE BIG LEBOWSKI WHEN YOU CAN MY LOVE!"
            # nijah_cowgirl_cum
            NIJAH "AH! WE ARE MAKING A BABY! EXCELLENT!"
            NIJAH "THE DECLINING BIRTH RATE COMMITTEE WILL BE PLEASED!"
        "Not this time!":
            NIJAH @talk "Speak to Garen if you want to fuck sometime!"


###############################
# Return to Garen with the Dodgy Tax Receipts.
    GAREN @talk "You have done as I ask!"
    GAREN @talk "Now the government will never know I defrauded them to fund my crippling Warhammer addiction!"
    GAREN @talk "Here is your reward!"
    # Remove/turn in the Dodgy Tax Receipts.
    # Pay the reward selected during the original negotiation: 1 / 100 / 1,000 gold.
    GAREN @talk "Now urgently, I need you to take this form to {i}the department of very legitimate tax.{/i}"
    GAREN @talk "Go now! HURRY!"
    #Add item: Dodgy filled in tax form

####################################
    # Quest update: Head to the department of very legitimate tax and hand over the dodgy filled in tax-form.
    # Add a NEW registered world location/building the player can enter and leave normally.
    # Follow an existing PB location pattern; use an existing background.
    # Speak to the receptionist - Visna
    VISNA @talk "I hate this job."
    menu:
        "Take this dodgy form.":
            VISNA @talk "Woo... More paperwork."
            pass
        "Well bye then.":
            VISNA @talk "Whatever, asshole."
            # Exit here without handing over the form or advancing. Do not fall through.
            pass

    # Only continue here after the form has actually been handed over.
    VISNA @talk "Hey, my boyfriend sucks and you seem cool, can I be your girl?"
    MC @talk "Why not."
    VISNA @talk "Yay!"
    # Add Visna as a proper world character using an existing simple NPC as reference:
    # registration/world character, relationship entry, expressions and normal dialogue access.
    VISNA @smile "How is it going?"
    menu:
        "Wanna fuck?": # Add this scene to gallery Visna - Lewd Dream.
            # Unlock from the live scene; gallery replay must not advance the quest.
            VISNA @talk "Nah, but I can show you a vision of some sex if you want!"
            MC @think "You can?"
            VISNA @talk "Yes, take a look."
            # the scene should have all that a typical sex scene has:
            # sex music, sex sounds, infection loss, gallery scene etc
            # regina_missionary_webm_idle
            REGINA "Give to me please!"
            REGINA "Shove it in!"
            # regina_missionary_webm_1
            REGINA "AH! Sex at last! How wonderful!"
            REGINA "Sex is fun!"
            # regina_missionary_webm_2
            REGINA "HAVE YOU HEARD OF OUR LORD AND SAVIOR JESUS CHRIST?"
            REGINA "I like cats!"
            REGINA "Riveting dialogue! Yes!"
            # regina_missionary_cum
            REGINA "Wow! You came in me!"
            REGINA "Good job!"
            REGINA "I bet your parents are proud!"
            pass

            # Repeat variant - use this on later live encounters, NOT immediately after the first-time version.
            # Add this variant to the gallery AFTER the player experieces it.
            # regina_missionary_webm_idle
            REGINA "Wow! What a great cock!"
            REGINA "Just like in the movies!"
            # regina_missionary_webm_1
            REGINA "Oooh! Ahh! Repeat sex is the best!"
            REGINA "Did you know snake takes like chicken?"
            REGINA "The more you know!"
            # regina_missionary_webm_2
            REGINA "Oooh, ahh, lots of sex sounds!"
            REGINA "Do you remember Digimon?"
            REGINA "Fun times, eh?"
            # regina_missionary_cum
            REGINA "Congratulations!"
            REGINA "You have discovered how babies are made!"
            REGINA "Good job!"
            pass
        "Bye.":
            VISNA @talk "Later."

#################################
    #Return to Garen
    GAREN @talk "Did you do it?"
    menu:
        "Hell yeah I did! Fuck the government!":
            GAREN @talk "RADICAL BRO! Right on man!"
            # Complete the quest and award its intended 250 XP through the normal quest-completion system.
        "Nah.":
            GAREN @talk "Return when you have, skrub!"


###############################
# POST-QUEST GAREN INTERACTION
# This repeatable interaction must remain available after the quest is completed.
    GAREN @talk "Yes?"
    menu:
        "Summon the wench.":
            GAREN @talk "Of course!"
            # roll 50%
            # SUCCESS:
            NIJAH @smile "Wanna fuck?"
            menu:
                "Yes!":
                    # Replay/loop the Nijah scene using the proper existing scene flow.
                    NIJAH @talk "Yay!"
                    pass
                "No!":
                    NIJAH @talk "Then I am leaving!"
                    # Nijah sprite leaves; exit back to normal dialogue/world flow.
                    pass
            # FAILURE instead:
            # if player failed a roll today, it should stay so for today
            GAREN @talk "You've had enough ass for one night!"
            # Return to root menu
        "That is all!":
            GAREN @smile "Farewell then!"
            pass
