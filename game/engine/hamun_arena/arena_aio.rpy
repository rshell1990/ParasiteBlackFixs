init python:
    # enabled by beating judgement day quest 
    @AppendToAllQuests
    class HamunArena(LogicModule):
        def __init__(self):
            super().__init__()

            self.FirstMeet = True # turned false after
            # 0 is "unranked" meaning player havent beat the first one yet
            # 1 - sun forged
            # 2 - dune warrior
            # 3 - dune master
            # 4 - desert lord
            # 5 - god of the arena
            self.Rank = 0

            self.FoughtToday = False

            self.ShowFirstNightEnterScene = True # turned false later

            # this is dynamic so watch out
            self.SelectedBattle_Data = None         # points to dict in HamunArena_Battles, is shorthand because it can also be found with rank+index below
            self.SelectedBattle_Rank = None         # integer
            self.SelectedBattle_Index = False       # integer or "boss_battle", latter advances rank

            self.StoredPlayerRank = None # < dynamic for label jumps

            self.WonBattles = set() # will store tuples of (rank, index)

        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_arena_int":
                if IsDaytime():
                    if self.FirstMeet == True:
                        btnMods["btn_hamun_arena_master_talk"] = BtnJumpLabel(_("Arena Master"), "hamun_arena_master_talk_first_time")
                    else:
                        btnMods["btn_hamun_arena_master_talk"] = BtnJumpLabel(_("Arena Master"), "hamun_arena_master_talk")
            return LocButtonMod(directMods = btnMods)

        def onMidnight(self):
            self.FoughtToday = False
            return

        def onEnter(self):
            if GetLocID() == "hamun_arena_int":
                if not IsDaytime():
                    if self.ShowFirstNightEnterScene == True:
                        return TriggeredEvent("hamun_arena_first_night_enter")

        def extraDialogue(self):
            yield ("hamun_arena_master_root", DNode(_("Sign me up for a fight."),   "hamun_arena_master_signup"))
            yield ("hamun_arena_master_root", DNode(_("I have some questions..."),  "hamun_arena_master_questions"))
            yield ("hamun_arena_master_root", DNode(_("Another time perhaps."),     "hamun_arena_master_bye", nextNode = "DNodeExit", order = -100))

        def IsBossBattleUnlocked(self, Rank):
            for BattleIndex, BattleData in enumerate(HamunArena_Battles[Rank]["rank_battles"]):
                if (Rank, BattleIndex) not in self.WonBattles:
                    return False
            return True

        def IsBossBattleWon(self, Rank):
            if (Rank, "boss_battle") in self.WonBattles:
                return True
            return False

    ########## extra stuff for battle logic
        ## called when battle is initiated
        def ArenaBattle_Initiate(self, BattleInfo):
            self.FoughtToday = True

            Rank = BattleInfo[0]
            Index = BattleInfo[1] # int or "boss_battle"

            # warning we dont copy coz i think we wont need to mutate the entry so w/e? only read?
            if Index == "boss_battle":
                self.SelectedBattle_Data = store.HamunArena_Battles[Rank]["boss_battle"]
            else:
                self.SelectedBattle_Data = store.HamunArena_Battles[Rank]["rank_battles"][Index]
            self.SelectedBattle_Rank = Rank 
            self.SelectedBattle_Index = Index

            # for "rank advanced" scene
            self.StoredPlayerRank = self.Rank
            return

        ## gives reward and resets stuff
        def ArenaBattle_ProcessVictory(self):
            # first assemble battle data tuple for checks & storage
            BattleDataTuple = (self.SelectedBattle_Rank, self.SelectedBattle_Index)

            # give gold / item rewards
            if "gold_reward" in self.SelectedBattle_Data:
                if BattleDataTuple in self.WonBattles:
                    GoldRewardAdjustedAmount = round(self.SelectedBattle_Data["gold_reward"] * 0.25)
                else:
                    GoldRewardAdjustedAmount = self.SelectedBattle_Data["gold_reward"]
                PlayerAddItem("gold", GoldRewardAdjustedAmount)
            if "item_reward" in self.SelectedBattle_Data:
                # items are only given once
                if BattleDataTuple not in self.WonBattles:
                    for ItemID, ItemQty in self.SelectedBattle_Data["item_reward"].items():
                        PlayerAddItem(ItemID, ItemQty)

            # add battle to stored set of won battles for "which ones are completed" logic
            self.WonBattles.add(BattleDataTuple)

            # set new rank, warning this "lifts" you up to next rank so you can probably skip in dev mode
            if self.SelectedBattle_Index == "boss_battle":
                DefeatedBossRank = self.SelectedBattle_Rank + 1
                if self.Rank < DefeatedBossRank:
                    self.Rank = DefeatedBossRank

                    # dont think more crazy shit is reasonable so lets just inject a direct quest hook here
                    if self.Rank >= 1:
                        if QstIsActive(QstTheBeastOfNovaras):
                            if QstGetProgress(QstTheBeastOfNovaras) == 1:
                                QstSetProgress(QstTheBeastOfNovaras, 2)

                    # rank advanced, give xp reward
                    AddExpPlayer(HamunArena_Ranks[self.Rank]["xp_reward"])

            # clean up dynamic battle-related variables
            self.SelectedBattle_Data = None
            self.SelectedBattle_Rank = None
            self.SelectedBattle_Index = None
            return

    def DEBUG_HamunArenaBeatAllBattles():
        for RankIndex, RankBattle in enumerate(HamunArena_Battles[HamunArena().Rank]["rank_battles"]):
            HamunArena().WonBattles.add((HamunArena().Rank, RankIndex))


label hamun_arena_debug_rank_sunforged:
    "DEBUG: rank is now set to 1 (sun forged)"
    $ HamunArena().Rank = 1
    if QstIsActive(QstTheBeastOfNovaras):
        if QstGetProgress(QstTheBeastOfNovaras) == 1:
            $ QstSetProgress(QstTheBeastOfNovaras, 2)
    $ LocEnter()

label hamun_arena_first_night_enter:
    $ HamunArena().ShowFirstNightEnterScene = False
    show mc at center with easeinleft
    $ Pause(0.25)
    show mc at blurin, center_f
    MC "(The place is deserted.)"
    show mc at blurin, center
    MC "(Looks like nothing interesting is going on here at night.)"
    $ LocEnter()

label hamun_arena_master_talk_first_time:
    show cg_dealer at center with dissolve
    $ HamunArena().FirstMeet = False
    HAMUN_ARENA_MASTER "Greetings... Are you here to watch a battle in the arena, or to rank?"
    MC @talk "To rank."
    HAMUN_ARENA_MASTER "Excellent."
    "The figure slid over some paperwork with an inked quill."
    HAMUN_ARENA_MASTER "Any questions?"
    menu hamun_arena_master_questions_menu_first_time:
        "No joining fee?":
            HAMUN_ARENA_MASTER "You pay in blood here."
            jump hamun_arena_master_questions_menu_first_time
        "How do the rankings work?":
            HAMUN_ARENA_MASTER "There are five ranks within the arena."
            HAMUN_ARENA_MASTER "To move between ranks, you must defeat ten opponents in each rank."
            HAMUN_ARENA_MASTER "Followed by a special match of our choosing."
            HAMUN_ARENA_MASTER "...As a word of warning, we may restrict your access to some of the higher ranks if we don't feel you're ready."
            HAMUN_ARENA_MASTER "We want a glorious battle on the sand... not a bloody massacre before the audience even sits down."
            jump hamun_arena_master_questions_menu_first_time
        "What kind of things will we be facing?":
            HAMUN_ARENA_MASTER "Monsters, warriors... strange creatures from faraway lands."
            HAMUN_ARENA_MASTER "Whatever we think will draw in the most crowds."
            jump hamun_arena_master_questions_menu_first_time
        "What's the pay?":
            HAMUN_ARENA_MASTER "The higher the ranked matches, the higher the coin."
            HAMUN_ARENA_MASTER "Though sometimes, rewards may be offered in place of coin."
            jump hamun_arena_master_questions_menu_first_time
        "That's all I wanted to ask.":
            HAMUN_ARENA_MASTER "Good... Now shall we discuss arranging a match?"
            jump hamun_arena_master_talk_process

label hamun_arena_master_talk:
    show cg_dealer at center with dissolve
    if HamunArena().Rank == 0:
        HAMUN_ARENA_MASTER "Yes?"
    elif HamunArena().Rank == 1:
        HAMUN_ARENA_MASTER "Yes, Sun Forged?"
    label hamun_arena_master_talk_process:
    call processDialogue("hamun_arena_master_root") from _call_processDialogue_73
    $ LocEnter()

label hamun_arena_master_signup:
    if not IsDaytime():
        HAMUN_ARENA_MASTER "The sun is set, it's too late now."
        HAMUN_ARENA_MASTER "Come back tomorrow."
        $ LocEnter()
    if HamunArena().FoughtToday == True:
        HAMUN_ARENA_MASTER "The crowd have seen enough of you for today, warrior."
        HAMUN_ARENA_MASTER "Come back tomorrow for another fight."
        return
    HAMUN_ARENA_MASTER "Heh... Whose blood shall stain the sacred sands, then?"
    call screen HamunArenaSelectBattle() with Dissolve(0.25)
    with Dissolve(0.25)
    # if battle picked (next one or previously done ones)
    if _return != False:
        $ AutoMus(False)
        $ PlayMusicRandom("mus_battle_generic")
        $ HamunArena().ArenaBattle_Initiate(_return)
        scene black with dissolve
        #play sound2 "audio/cfx/transform.ogg"
        $ Pause(0.5)
        $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_arena", CharIDList_Right = HamunArena().SelectedBattle_Data["enemy_list"]))

        # gold / item / xp rewards, rank advancements
        $ HamunArena().ArenaBattle_ProcessVictory()

        $ Pause(0.5)

        $ AutoMus(True)

        # rank adv. narrative scene
        if HamunArena().Rank > HamunArena().StoredPlayerRank:
            jump hamun_arena_master_rank_advanced

        $ LocEnter()

    else:
        HAMUN_ARENA_MASTER "Stop wasting my time."
        return

screen Arena_NewRankPopup(RankIndex):
    #modal True
    zorder 200

    on "show" action Play("sound2", "audio/interface/fanfare_synth.ogg")

    add "images/gui/unsorted/black_under.webp"
    add HamunArena_Ranks[RankIndex]["icon"]:
        anchor (0.5, 0.3)
        pos (0.5, 0.4)
        at TF_Arena_NewRankFadeIn

    vbox:
        anchor (0.5, 0.5)
        pos (0.5, 0.15)
        label _("New arena rank!"):
            text_size 40
            xalign 0.5
        label HamunArena_Ranks[RankIndex]["name"]:
            text_size 90
            xalign 0.5
        at TF_Arena_NewRankText
    
    button:
        background Null()
        xsize 1920
        ysize 1080
        action Return()

    timer 4.5 action Return()

transform TF_Arena_NewRankText:
    subpixel True
    alpha 0.0
    ease 0.5:
        alpha 1.0
    linear 3.0:
        yoffset 40
    ease 1.5:
        yoffset 80
        alpha 0.0

transform TF_Arena_NewRankFadeIn:
    subpixel True
    yoffset 0
    alpha 0.0
    zoom 0.5
    ease 1.0:
        zoom 0.7
        alpha 1.0
    linear 2.5:
        yoffset 30
    ease 1.0:
        yoffset 90
        zoom 0.65
        alpha 0.0


label hamun_arena_master_rank_advanced:
    $ LocFlush()
    call screen Arena_NewRankPopup(1) with dissolve
    show cg_dealer at center     
    with dissolve
    HAMUN_ARENA_MASTER "Quite a fight, warrior!"
    HAMUN_ARENA_MASTER "You are now ranked {i}Sun Forged{/i}."
    HAMUN_ARENA_MASTER "Enjoy your fame!"
    HAMUN_ARENA_MASTER "...while it lasts."
    $ LocEnter()

label hamun_arena_master_questions:
    HAMUN_ARENA_MASTER "Then speak." 
    menu hamun_arena_master_questions_menu:
        "No joining fee?":
            HAMUN_ARENA_MASTER "You pay in blood here."
            jump hamun_arena_master_questions_menu
        "How do the rankings work?":
            HAMUN_ARENA_MASTER "There are five ranks within the arena."
            HAMUN_ARENA_MASTER "To move between ranks, you must defeat ten opponents in each rank."
            HAMUN_ARENA_MASTER "Followed by a special match of our choosing."
            HAMUN_ARENA_MASTER "...As a word of warning, we may restrict your access to some of the higher ranks if we don't feel you're ready."
            HAMUN_ARENA_MASTER "We want a glorious battle on the sand... not a bloody massacre before the audience even sits down."
            jump hamun_arena_master_questions_menu
        "What kind of things will we be facing?":
            HAMUN_ARENA_MASTER "Monsters, warriors... strange creatures from faraway lands."
            HAMUN_ARENA_MASTER "Whatever we think will draw in the most crowds."
            jump hamun_arena_master_questions_menu
        "What's the pay?":
            HAMUN_ARENA_MASTER "The higher the ranked matches, the higher the coin."
            HAMUN_ARENA_MASTER "Though sometimes, rewards may be offered in place of coin."
            jump hamun_arena_master_questions_menu
        "That's all I wanted to ask.":
            HAMUN_ARENA_MASTER "Good... Now shall we discuss arranging a match?"
            return

label hamun_arena_master_bye:
    if HamunArena().Rank == 0:
        HAMUN_ARENA_MASTER "Hmph..."
    elif HamunArena().Rank == 1:
        HAMUN_ARENA_MASTER "Goodbye."
    $ LocEnter()

screen HamunArenaSelectBattle():
    modal True
    #zorder 200

    add "images/gui/unsorted/black_under.webp"
    default CurrentPage = 0
    frame:
        style "frame_outer"
        align (0.5, 0.5)
        vbox:
            # screen title 
            #label "hamun city arena" xalign 0.5

            # rank selection
            if HamunArena().Rank == CurrentPage:
                if HamunArena().IsBossBattleUnlocked(HamunArena().Rank):
                    if HamunArena().IsBossBattleWon(HamunArena().Rank):
                        text _("You have cleared this rank."):
                            xalign 0.5
                    else:
                        text _("Defeat the boss to advance your rank!"):
                            xalign 0.5
                else:
                    text _("Beat every opponent to unlock the boss battle!"):
                        xalign 0.5
            elif HamunArena().Rank == CurrentPage + 1:
                text _("You have cleared this rank."):
                    xalign 0.5

            hbox:
                xalign 0.5
                spacing 10
                # textbutton "<":
                #     yalign 0.5
                #     #if CurrentPage > 0:
                #     #    action NullAction() 
                #         #action SetLocalVariable("CurrentPage", CurrentPage - 1)
                #     #hovered TooltipSetUI("these will cycle between ranks") 
                #     unhovered TooltipClearUI()
                label tra(HamunArena_Ranks[CurrentPage + 1]["name"]):
                    yalign 0.5
                    xalign 0.5
                    text_size 60
                # textbutton ">":
                #     yalign 0.5
                #     #if CurrentPage < 4:
                #         #action SetLocalVariable("CurrentPage", CurrentPage + 1)
                #         #action NullAction()
                #     #hovered TooltipSetUI("these will cycle between ranks") 
                #     unhovered TooltipClearUI()

            if CurrentPage == 0:
                # boss battle btn
                if HamunArena().IsBossBattleUnlocked(CurrentPage):
                    if HamunArena().IsBossBattleWon(CurrentPage):
                        add HamunArena_Ranks[CurrentPage + 1]["icon"]:
                            align (0.5, 0.5)
                            xysize (300, 300)
                    else:
                        use HamunArenaBattleButton(CurrentPage, "boss_battle")
                else:
                    use HamunArenaBattleButton(CurrentPage, "boss_battle")

                null height 5

                # battles   
                frame:
                    background Null()
                    vbox:
                        null height 5
                        # 6-10
                        hbox:
                            spacing 5
                            null width 5
                            for i in range(5, 10):
                                use HamunArenaBattleButton(CurrentPage, i)
                        
                        null height 5
                        # 1-5
                        hbox:
                            spacing 5
                            null width 5
                            for i in range(0, 5):
                                use HamunArenaBattleButton(CurrentPage, i)
                            null width 5
                        
                        null height 5
            
            null height 10
            textbutton _("Return"):
                xalign 0.5
                action [Return(False), With(Dissolve(0.25))]
    if config.developer:
        textbutton "(dev) beat all battles":
            xalign 0.5
            action Function(DEBUG_HamunArenaBeatAllBattles)

screen HamunArenaBattleButton(Rank, BattleIndex):
    button:
        align (0.5, 0.5)
        if BattleIndex == "boss_battle":
            idle_background Frame("images/gui/frames/frame2.webp", Borders(180, 180, 180, 180))
            hover_background Frame(Transform("images/gui/frames/frame2.webp", matrixcolor = BrightnessMatrix(0.08)), Borders(180, 180, 180, 180))
            padding (44, 44)
            xysize (300, 300)
        else:
            xysize (192, 192)

        frame:
            align (0.5, 0.5)
            if BattleIndex == "boss_battle":
                #style "frame_outer"
                if HamunArena().IsBossBattleUnlocked(Rank):
                    if HamunArena().IsBossBattleWon(Rank):
                        add HamunArena_Battles[Rank]["boss_battle"]["icon"]:
                            fit "contain"
                    else:
                        add HamunArena_Battles[Rank]["boss_battle"]["icon"]:
                            fit "contain"
                else:
                    add "images/gui/unsorted/gallery_lock.webp":
                        fit "contain"
            else:
                if HamunArena_Battles[Rank]["rank_battles"][BattleIndex]["icon"] != "someicon":
                    add HamunArena_Battles[Rank]["rank_battles"][BattleIndex]["icon"]:
                        fit "contain"
                else:
                    add "images/battle_skins/demorai/scorpion/battle_sprite_demorai_scorpion_portrait.webp":
                        fit "contain"
        if (Rank, BattleIndex) in HamunArena().WonBattles:
            add "images/gui/unsorted/arena_won_battle_mark.webp":
                fit "contain" 
                align (0.5, 0.5)
                zoom 0.96
                matrixcolor OpacityMatrix(0.8)

        if BattleIndex == "boss_battle":
            if HamunArena().IsBossBattleUnlocked(Rank):
                if HamunArena().IsBossBattleWon(Rank):
                    action NullAction()
                else:
                    action [Return((Rank, "boss_battle")), TooltipClearUI(), With(Dissolve(0.25))]
            else:
                action NullAction()
        else:
            action [Return((Rank, BattleIndex)), TooltipClearUI(), With(Dissolve(0.25))]
        
        if BattleIndex == "boss_battle":
            if HamunArena().IsBossBattleUnlocked(Rank):
                if HamunArena().IsBossBattleWon(Rank):
                    hovered TooltipSetUI(_("You have already beaten this boss: you can only fight an arena boss once."))
                else:
                    hovered TooltipSetUI(Arena_GetBattleDesc(Rank, BattleIndex))
            else:
                hovered TooltipSetUI(_("You must first beat all other opponents to unlock a boss fight."))
        else:
            hovered TooltipSetUI(Arena_GetBattleDesc(Rank, BattleIndex))
        unhovered TooltipClearUI()

init python:
    # rank index: name, xp reward, level
    HamunArena_Ranks = {
        1:{
            "name":_("Sun Forged"),
            "xp_reward":550,
            "level_req":None,
            "icon":"images/arena_ranks/arena_sun_forged.webp",
        },
        2:{
            "name":_("Dune Warrior"),
            "xp_reward":550,
            "level_req":20,
            "icon":"images/arena_ranks/arena_dune_walker.webp",
        },
        3:{
            "name":_("Dune Master"),
            "xp_reward":550,
            "level_req":25,
            "icon":"images/arena_ranks/arena_dune_master.webp",
        },
        4:{
            "name":_("Desert Lord"),
            "xp_reward":550,
            "level_req":30,
            "icon":"images/arena_ranks/arena_desert_lord.webp",
        },
        5:{
            "name":_("God of the Arena"),
            "xp_reward":550,
            "level_req":40,
            "icon":"images/arena_ranks/arena_god.webp",
        },
    }
    
    HamunArena_Battles = {
        # every rank's entry has a list of battles (order matters) and a boss battle definition
        # rank here means "the rank you must be to play these battles"
        # unranked->sun forged
        0:{
            "rank_battles":[
                {
                    "name":_("Red Lizards"),
                    "desc":_("A group of four red lizards"),
                    "icon":"images/arena_battle_icons/red_lizards.webp",
                    "enemy_list":[
                        {"e_lizard_red":5}, 
                        {"e_lizard_red":6}, 
                        {"e_lizard_red":7}, 
                        {"e_lizard_red":8}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Big ghoul"),
                    "desc":None,
                    "icon":"images/battle_skins/ghoul_big/battle_sprite_ghoul_big_portrait.webp",
                    "enemy_list":[
                        {"e_ghoul_big":10}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Rhuvan bears"),
                    "desc":_("A couple of wild Rhuvan bears"),
                    "icon":"images/arena_battle_icons/bears.webp",
                    "enemy_list":[
                        {"e_bear_white":8}, 
                        {"e_bear_white":10}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Green slime"),
                    "desc":None,
                    "icon":"images/battle_skins/neutral/slime_green/battle_sprite_slime_green_portrait.webp",
                    "enemy_list":[
                        {"e_green_slime":10}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Desert rat queen"),
                    "desc":None,
                    "icon":"images/battle_skins/neutral/desert_rat_queen/battle_sprite_desratq_portrait.webp",
                    "enemy_list":[
                        {"e_desert_rat_queen":10}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Wolf pack"),
                    "desc":_("A pack of wolves lead by a Great dire wolf"),
                    "icon":"images/arena_battle_icons/wolves.webp",
                    "enemy_list":[
                        {"e_wolf":10},
                        {"e_wolf":10},
                        {"e_wolf_dire":10},
                        {"e_wolf":10}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Mad raiders"),
                    "desc":_("A gang of raiders"),
                    "icon":"images/arena_battle_icons/raiders.webp",
                    "enemy_list":[
                        {"e_raider":6}, 
                        {"e_raider":7}, 
                        {"e_raider":8}, 
                        {"e_raider":9},
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Murderous goblins"),
                    "desc":None,
                    "icon":"images/arena_battle_icons/goblins.webp",
                    "enemy_list":[
                        {"e_goblin":11}, 
                        {"e_goblin":12}, 
                        {"e_goblin":13}, 
                        {"e_goblin":14}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("Elite assassins"),
                    "desc":_("A group of three assassins"),
                    "icon":"images/arena_battle_icons/assassins.webp",
                    "enemy_list":[
                        {"e_assassin":10}, 
                        {"e_assassin":11}, 
                        {"e_assassin":12}
                    ],
                    "gold_reward":200,
                },
                {
                    "name":_("The gang"),
                    "desc":_("A group of bandits"),
                    "icon":"images/arena_battle_icons/bandits.webp",
                    "enemy_list":[
                        {"e_bandit":14}, 
                        {"e_thug":12}, 
                        {"e_swindler":18}, 
                        {"e_bandit":16}
                    ],
                    "gold_reward":200,
                },
            ],
            "boss_battle":{
                "name":_("The Abomination"),
                "desc":None,
                "icon":"images/battle_skins/abomination/battle_sprite_abomination_portrait.webp",
                "enemy_list":["e_abomination"],
                "gold_reward":200,
            },
        },
        # sun forged -> dune warrior
        1:{},
        # dune warrior -> dune master
        2:{},
        # dune master -> desert lord
        3:{},
        # desert lord -> god of the arena
        4:{},
    }

    def Arena_GetBattleDesc(Rank, Index):
        if Index == "boss_battle":
            BattleData = HamunArena_Battles[Rank][Index]
        else:
            BattleData = HamunArena_Battles[Rank]["rank_battles"][Index]

        ### order of strings appended -> order of strings displayed
        Result = []

        # name
        Result.append(tra(BattleData["name"]))

        # desc
        if BattleData["desc"] is not None:
            Result.append("{size=27}{color=#c2c2c2}" + tra(BattleData["desc"]) + "{/size}{/color}")

        # gold reward
        if "gold_reward" in BattleData:
            if (Rank, Index) in HamunArena().WonBattles:
                Result.append("{color=#fff7cc}" + tra(_("Gold reward: ")) + str(round(BattleData["gold_reward"] * 0.25)) + "{/color}")
            else:
                Result.append("{color=#fff7cc}" + tra(_("Gold reward: ")) + str(BattleData["gold_reward"]) + "{/color}")

        # beaten notifier
        # if (Rank, Index) in HamunArena().WonBattles:
        #     Result.append("{size=27}{color=#c2c2c2}" + tra(_("{i}You have already beaten this opponent: the gold reward for this battle is adjusted to be one quarter of the original value.{/i}")) + "{/size}{/color}")

        return "\n".join(Result)