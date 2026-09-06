init python:
    # enabled by seeing the show-up event
    @AppendToAllQuests
    class NovarasAdvBoard(LogicModule):
        def __init__(self):
            super().__init__()

            self.player_tier = 0 # D at start
            # for reference: guild tiers/adv tiers & integer assigned
            # D Tier: Novice Adventurer,        0
            # C Tier: Seasoned Adventurer       1
            # B Tier: Elite Adventurer          2
            # A Tier: Valiant champions         3
            # S Tier: Protectors of the Realm   4

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "novaras_adv_guild":
                btnMods["btn_novaras_guild_board"] = BtnShowScreen(_("Quest Board"), "quest_board")
            return LocButtonMod(directMods = btnMods)
        
        def onMidnight(self):
            for quest_class in adv_guild_quests:
                if hasattr(quest_class(), "times_completed"): # only reappear repeatables
                    if quest_class().appears_on_board == False:
                        if GetGameDay() >= quest_class().reappear_day:
                            quest_class().appears_on_board = True

    def GetIconString(quest_class): # converts stuff like ["clock", "swords"] into a renpy-edible string
        return_string = ""
        if len(quest_class.ICONS) > 0:
            icon_list = []
            for entry in quest_class.ICONS:
                if entry == "clock":
                    icon_list.append("{image=[ICON.CLOCK]}")
                if entry == "swords":
                    icon_list.append("{image=[ICON.SWORDS]}")
            return_string = " ".join(icon_list)
            return_string += " "
        return return_string

    adv_guild_quests = [] # each board-related quest appends in here

label nov_adv_guild_board_choose_quest(quest_class): # used by all questboard-listed tasks
    show mc at cright_f with dissolve
    MC "Hmm..."
    $ board_quest_icon_string = GetIconString(quest_class)

    $ board_quest_desc_text_index = 0
    while board_quest_desc_text_index < len(quest_class.PRE_START_STRINGS_LIST):
        $ renpy.say(MC, quest_class.PRE_START_STRINGS_LIST[board_quest_desc_text_index])
        $ board_quest_desc_text_index += 1
    menu:
        "[board_quest_icon_string]Accept the task.":
            hide mc with dissolve
            jump expression quest_class.LABEL
        "Pick another quest.":
            hide mc with dissolve
            call screen quest_board
        "Leave.":
            hide mc with dissolve
    jump main_recheck

screen quest_board():
    tag ingame_menu
    modal True

    use close_outside("quest_board", do_return = True)
    use outer_frame():
        vbox:
            spacing 10
            xalign 0.5
            label _("Quest Board"):
                xalign 0.5
            frame:
                xsize 1400
                ysize 710
                vpgrid:
                    allow_underfull True
                    cols 3
                    xalign 0.5
                    spacing 4
                    mousewheel True
                    scrollbars "vertical"
                    for quest_class in adv_guild_quests:
                        if quest_class().appears_on_board:
                            use quest_board_entry(quest_class)

screen quest_board_entry(quest_class):
    default SuggestedLevel = getattr(quest_class(), "suggestedLevel", 0)
    button:
        idle_background  Transform(Frame("images/gui/frames/paper.webp", Borders(0, 0, 0, 0)))
        hover_background Transform(Frame("images/gui/frames/paper.webp", Borders(0, 0, 0, 0)), matrixcolor = BrightnessMatrix(0.15))
        align (0.5, 0.5)
        xsize 450
        ysize 300
        vbox:
            xfill True
            spacing 5
            null height 10
            text quest_class.TITLE:
                xalign 0.5
                color "#0f0f0f"
                style "quest_board_title_text"
            if SuggestedLevel > 0:
                if GetPlayerLevel() >= SuggestedLevel:
                    text "{color=#42ff55}" + tra(_("Suggested Level %s")) % SuggestedLevel + "{/color}":
                        xalign 0.5
                        size 30
                        outlines [(1, "#000000ff", 0, 0)]
                else:
                    text "{color=#ff4242}" + tra(_("Suggested Level %s")) % SuggestedLevel + "{/color}":
                        xalign 0.5
                        size 30
                        outlines [(1, "#000000ff", 0, 0)]
            text "{i}" + tra(quest_class.DESCRIPTION) + "{/i}":
                xalign 0.5
                text_align 0.5
                color "#161616"
                style "quest_board_desc_text"
        if hasattr(quest_class(), "times_completed"):
            if quest_class().times_completed >= 1:
                add "images/gui/unsorted/checkmark.webp":
                    align (0.98, 0.94)
        else:
            add "images/gui/unsorted/star.webp":
                align (0.98, 0.94)
        action [Hide("quest_board"), Call("nov_adv_guild_board_choose_quest", quest_class)]