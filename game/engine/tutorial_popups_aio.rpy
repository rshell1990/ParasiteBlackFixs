default DEBUG_SupressTutorialPopups = False
init python:
    # call to show a tutorial message of given ID. directmessage to send in text manually (to pass in variables)
    def ShowTutorialPopup(TutorialMessageID, DirectMessage = None):
        # check whether the tutorial popup exists, add if not (old saves)
        if TutorialMessageID not in persistent.TutorialPopups:
            persistent.TutorialPopups[TutorialMessageID] = True

        # check if its true ("should we show it? yes/no?")
        if persistent.TutorialPopups[TutorialMessageID]:
            # set it to false (we've shown it)
            persistent.TutorialPopups[TutorialMessageID] = False

            if DirectMessage is not None:
                MessageText = DirectMessage 
            else:
                MessageText = Lib_TutorialTexts[TutorialMessageID]

            # call screen
            if not DEBUG_SupressTutorialPopups:
                renpy.call_screen(
                    "ok_popup", 
                    label = STR_UI.TUTORIAL_TITLE, 
                    text = MessageText)
                renpy.with_statement(transition_popup)
        return

##### for preferences, to set all to seen or not seen
    def UI_TutorialsSetAllToTrue():
        persistent.TutorialPopups = {MessageID:True for MessageID in persistent.TutorialPopups.keys()}
        return

    def UI_TutorialsSetAllToFalse():
        persistent.TutorialPopups = {MessageID:False for MessageID in persistent.TutorialPopups.keys()}
        return
#######

    # texts of (almost all) tutorial messages
    Lib_TutorialTexts = {}
    Lib_TutorialTexts["character_creation"] = _("Welcome to Parasite Black!\n\nTutorial pop-ups such as this one will accompany you throughout the game.\n\nBefore you begin your journey, you must first confirm or change your character's {i}starting attributes{/i} and name.\n\nTake your time to explore what each attribute affects by hovering over it. You can always revert your changes to default.\n\nAs the game is still in-development, alot of the underlying mechanics are still undergoind big design overhauls.\n\nThese tutorial pop-ups can be disabled in the options menu.")
    Lib_TutorialTexts["guild_board"] = _("As a member of the Adventurers Guild, you now have access to the Guild's quest board.\n\nYou can click the quest board at any time of day to explore quests available for your Adventurer rank.\n\nCompleting each quest once will let you advance your rank by unlocking a more challenging, special quest.\n\nCurrently though, {i}only first tier of quests is implemented.{/i}\n\nEach quest will reappear on the board a few days after it is completed, but the experience reward will only be granted once.")
    Lib_TutorialTexts["para_skills"] = _("You have gained access to an extra skill tree: {b}Parasite Skills{/b}.\n\nThese battle skills can only be used in a transformed state. You and Markus will earn one Parasite skill point each level, starting from level 4.")
    Lib_TutorialTexts["freeroam"] = _("You are now free to explore the world of Alderay.\n\nA globe icon can be found on a suitable location to initiate travel to a different location.\n\nYou can also open map screen (x) to explore the world map.\n\nIf you ever feel lost, you can find your currently active quests or important notes in the 'journal' screen.\n\nGood luck and have fun!")
    Lib_TutorialTexts["game_time"] = _("The game time will now progress with every action you take, except for navigating the user interface.\n\nYou can use the time tracker (upper left) to tell current time.\n\nSome events in the game are dependent on time: if you are caught wandering around the fort at night, there will be consequences.\n\nOutside of narrative sections, you will often be able to skip time by {i}waiting (t).{/i}")
    Lib_TutorialTexts["combat_first"] = _("Combat in the game is turn-based. In this exercise, you are to fight markus using simple {i}basic attacks{/i}.\n\nRegardless of their other skills or energy levels, any character in the game has a {i}basic attack{/i}.\n\nSelect the basic attack on the character panel, lower side of the screen and click Markus to attack him.\n\nYou are not required to win and will be able to repeat the exercise if you want to.")
    Lib_TutorialTexts["combat_skills_and_items"] = _("In this exercise, practice using your combat skills. Both you and Markus will also have a healing item to use.\n\nMost combat skills cost energy (the green bar) to use.\n\nYour energy is restored automatically each turn.\n\nTo use a skill, open up a 'skills' sub-menu on your character panel and select a skill in question, then select a target you want to use it on.\n\nItems are used in a similar way, from their corresponding sub-menu.\n\nUsing an item {i}does not end your turn{/i}, and you can use as many items per turn as you wish.\n\nAs in previous exercise, you are not required to win and will be able to repeat the exercise if you want to.")
    Lib_TutorialTexts["combat_team"] = _("In this exercise, you will be paired up with another recruit as a {i}combat team{/i}.\n\nYou will be fighting against Markus paired up with another recruit.\n\nThe two extra scouts {i}have other skills{/i} than you and Markus.\n\nAs your turn begins, you can click a character to select them. As you decide on their action and execute it, their turn will end, allowing other characters to act.\n\nYou do not have to claim victory and will be able to repeat the exercise if you want to.")
    Lib_TutorialTexts["party"] = _("Kiara and Markus are now members of your {i}party.{/i}\nThey will accompany you on your mission and fight alongside you.\n\nYour party characters will automatically reach the same level you are, allowing you to {i}distribute their level-up points{/i}.\n\nYou can examine their character sheets in the 'characters' screen. In the 'inventory' screen, you can switch between party characters to examine or change their equipment.")
    Lib_TutorialTexts["first_quest"] = _("You have just recieved your first {i}quest{/i}. You can examine all the currently active quests using the {i}journal (q){/i} screen.\n\nThe journal lists all the currently active quests and your next objectives. Using your journal is a sure way to never get lost.\n\n{i}Inventory (e){/i} and {i}Relationships (r){/i} screens list your inventory and character relationships respectively.")
    Lib_TutorialTexts["first_level_up"] = _("You have reached a new {i}experience level.{/i}\n\nYou can now open the 'characters' screen to distribute your {i}attribute and skill points{/i}. Your distribution of points will only apply if you hit 'confirm'.")
    Lib_TutorialTexts["perks"] = _("With this level-up, you have earned a perk point.\nPerks allow your parasite to develop certain unique abilities.\n\nPerk points are earned every 3 levels, starting from level 4.\nYou can find the new perks tab in the 'characters' screen.")
    Lib_TutorialTexts["experience"] = _("You have just earned some {i}experience points{/i}.\n\nIn Parasite Black, experience is earned mainly by completing quests and {i}unlocking lewd scenes{/i}. Fighting only awards small amounts of experience, and only {i}once for each unique enemy match-up{/i} you encounter.\n\nYou can track your progress to the next experience level in your 'equipment' screen.")

######## tutorial message flags
# means "whether to show tutorial popup of certain id"
default persistent.TutorialPopups = {
    "first_level_up":   True,
    "perks":            True,
    "first_quest":      True,
    "party":            True,
    "combat_team":      True,
    "combat_skills_and_items":True,
    "combat_first":     True,
    "game_time":        True,
    "freeroam":         True,
    "infection_bar":    True,
    "guild_board":      True,
    "character_creation":True,
    "experience":       True,
    "navigation":       True,
    "para_skills":      True,
}