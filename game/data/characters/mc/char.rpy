default MC = Character("[player_name!t]", image = "mc")
default MC_PARA = Character("[player_name!t]", image = "mc", show_slow_effect = slow_slide_left(25), show_slow_effect_delay = 0.5, show_always_effect = always_shake(x = 1, y = 0))
default BLACK = Character(_("Parasite Black"), what_color = "#ff0000", image = "black", show_slow_effect = slow_slide_left(25), show_slow_effect_delay = 0.5, show_always_effect = always_shake(x = 1, y = 0))
default SHYAHTAN = Character(_("Shyahtan"), what_color = "#ff0000", image = "black", show_slow_effect = slow_slide_left(25), show_slow_effect_delay = 0.5, show_always_effect = always_shake(x = 1, y = 0))
default MCFEM = Character("[player_name!t]", image = "mcfem") # for a perk

default mc_female_outfit = "normal"

init python:
##### mc main worldchar
    CharDefs["mc"] = BuildCharTemplate(CharID = "mc",
                                        BattleSkin =  "mc", # swapped for _p by prologue quest
                                        portrait = "images/characters/mc/portrait_p.webp",

                                        Strength    = 5,
                                        Endurance   = 4,
                                        Willpower   = 5,
                                        Agility     = 6,
                                        Dexterity   = 6,
                                        Luck        = 6,
                                        Charisma    = 5,

                                        Barter      = 4,

                                        BattleClass = "warrior",

                                        CharSkills = {"WarriorHeavySlash":1},

                                        HasAltForm = True,

                                        AltForm_BattleClass = "parasiteBlack",
                                        AltForm_CharSkills = {"ParasiteBlackRazorSlash":1},
                                        AltForm_BattleSkin = "mc_transformed",
                                        AltForm_TransformSkill = "McTransform",
                                        AltForm_UnTransformSkill = "McUnTransform",

                                        ExtraData = {"clothes" : "normal", # naked / pants / normal / scout
                                                    "default_look" : "normal", # for the farther armor thingy
                                                    })

    config.tag_layer["mc"] = "characters"
    config.tag_layer["mcprologue"] = "characters"
    config.tag_layer["mc_transformed"] = "characters"
    config.tag_layer["mc_transformed_erect"] = "characters"
    config.tag_layer["cg_assassin_mc"] = "characters"

    config.tag_layer["cg_mc_bull"] = "characters"

    def TransformMC(Val):
        worldChars["mc"]["Transformed"] = Val
        return

    def SetMCFemOutfit(NewID):
        store.mc_female_outfit = NewID
        return

    config.tag_layer["mcfem"] = "characters"