######## image-based animations are in sep file
init python:
    def RegisterCharSkin(SkinID, 
                        Portrait = "images/battle_skins/PlaceholderBattlePortrait.webp", 
                        Sprite = "images/battle_skins/PlaceholderBattleSprite.webp", 
                        Anims = {}, 
                        Sounds = {}, 
                        SoundsVolCorrection = {},
                        SoundsExtraSilence = {},
                        BasicAttackImpactImageID = "Battle_VfxImpact",
                        SpriteOffset = (0, 0), 
                        FocusRectSize = (200, 400), 
                        FocusRectOffset = (0, 0),
                        SpriteVFXOffset = (0, 0)):

        # by default everyone has these fallback static sprite anims
        NewAnims = {
            "idle":     BattleAnimation(AnimLoop = True),
            "attack":   BattleAnimation(),
            "cast":     BattleAnimation(),
            "hit":      BattleAnimation()}
        # and the ones defined in skin are then updated into it
        NewAnims.update(Anims)

        NewSounds = {
            # voice "urghs"
            "Char_BeenHit":          [],
            "Char_UseSkill":         [],
            "Char_Die":              [],

            # attack swing non-vocal sounds
            "BasicAttack_Swing":   [
                "audio/battle/swordSwing/hSword-01.ogg",
                "audio/battle/swordSwing/hSword-02.ogg",
                "audio/battle/swordSwing/hSword-03.ogg",
                "audio/battle/swordSwing/hSword-04.ogg",
                "audio/battle/swordSwing/hSword-05.ogg",],
            # attack hit 
            "BasicAttack_Impact":[
                "audio/battle/SwordImpact/SwordHit1.ogg",
                "audio/battle/SwordImpact/SwordHit2.ogg",
                "audio/battle/SwordImpact/SwordHit3.ogg",
                "audio/battle/SwordImpact/SwordHit4.ogg"]}

        NewSounds.update(Sounds)

        NewSoundsExtraSilence = {Key:0.0 for Key in NewSounds}
        if isinstance(NewAnims["attack"], list):
            NewSoundsExtraSilence["BasicAttack_Swing"] = max(NewAnims["attack"][0].WarmupTo - 0.05, 0.0) # recalculated on skin reset if simple anims are used
        else:
            NewSoundsExtraSilence["BasicAttack_Swing"] = max(NewAnims["attack"].WarmupTo - 0.05, 0.0) # recalculated on skin reset if simple anims are used
        NewSoundsExtraSilence.update(SoundsExtraSilence)

        NewSoundsVolCorrection = {Key:1.0 for Key in NewSounds}
        NewSoundsVolCorrection["BasicAttack_Impact"] = 0.65
        NewSoundsVolCorrection.update(SoundsVolCorrection)

        NewSpriteVFXOffset = ((0, -(int(FocusRectSize[1] * 0.75))) if SpriteVFXOffset == (0, 0) else SpriteVFXOffset)

        NewSkin = BattleSkinClass(SkinID = SkinID, 
            Portrait = Portrait, 
            Sprite = Sprite, 
            BasicAttackImpactImageID = BasicAttackImpactImageID, 
            AnimsDict = NewAnims, 
            SoundsDict = NewSounds, 
            SoundsVolCorrection = NewSoundsVolCorrection, 
            SoundsExtraSilence = NewSoundsExtraSilence,
            SpriteOffset = SpriteOffset, 
            FocusRectSize = FocusRectSize, 
            FocusRectOffset = FocusRectOffset,
            SpriteVFXOffset = NewSpriteVFXOffset)

        return NewSkin

    # animation warmup is how long it takes before its supposed effect should happen (like sword hitting its target)
    # animation cooldown is how long it takes after that effect to finish the anim
    class BattleAnimation:
        def __init__(self,
                Displayable = "StaticSprite",
                LengthInSeconds = 1.0,
                WarmupTo = 0.5,
                AnimLoop = False,
                Transform_AttackDelay = 0.0,
                ApplyTransform = True,
                SoundSwing_DoNotCutOffOnImpact = False, # keep playing "swing" sound after attack lands
            ):
            Assert(LengthInSeconds > WarmupTo, "Anim LengthInSeconds %s cannot be equal or less than WarmupTo %s" % (LengthInSeconds, WarmupTo))
            self.Displayable = Displayable # <- default fallback is "no anim"
            self.LengthInSeconds = LengthInSeconds
            self.WarmupTo = WarmupTo
            self.AnimLoop = AnimLoop

            self.Transform_AttackDelay = Transform_AttackDelay
            self.ApplyTransform = ApplyTransform

            self.SoundSwing_DoNotCutOffOnImpact = SoundSwing_DoNotCutOffOnImpact

    class BattleSkinClass:
        def __init__(self, 
                    SkinID = None, 

                    Portrait = None, 
                    Sprite = None, 
                    BasicAttackImpactImageID = None,

                    AnimsDict =     {}, 
                    SoundsDict =    {},

                    SoundsVolCorrection =   {},
                    SoundsExtraSilence =    {},

                    SpriteOffset =      (0, 0), 
                    FocusRectSize =     (0, 0),
                    FocusRectOffset =   (0, 0),
                    SpriteVFXOffset =   (0, 0)):
            self.SkinID = SkinID
            self.Portrait = Portrait
            self.Sprite = Sprite
            self.BasicAttackImpactImageID = BasicAttackImpactImageID

            self.AnimsDict = AnimsDict
            self.SoundsDict = SoundsDict
            self.SoundsVolCorrection = SoundsVolCorrection
            self.SoundsExtraSilence = SoundsExtraSilence
            

            self.SpriteOffset = SpriteOffset

            self.FocusRectSize = FocusRectSize
            self.FocusRectOffset = FocusRectOffset

            self.SpriteVFXOffset = SpriteVFXOffset

    skinLib["demorai_scout"] = RegisterCharSkin("demorai_scout",
        Portrait =  "images/battle_skins/demorai/scout/battle_sprite_demorai_scout_portrait.webp",
        Sprite =    "images/battle_skins/demorai/scout/battle_sprite_demorai_scout_static.webp",
        Anims = {
            "attack":   BattleAnimation(
                Displayable = "battle_anim_demorai_scout_attack", 
                LengthInSeconds = 0.65, 
                WarmupTo = 0.15
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/demorai_scout/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/demorai_scout/BeenHit.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/demorai_scout/UseSkill.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/demorai_scout/Die.ogg"]},

        FocusRectSize = (225, 375)
    )

    skinLib["debug_skin"] = RegisterCharSkin("debug_skin")

    skinLib["demorai_brute"] = RegisterCharSkin("demorai_brute",
        Portrait =  "images/battle_skins/demorai/brute/battle_sprite_demorai_brute_portrait.webp",
        Sprite =    "images/battle_skins/demorai/brute/battle_sprite_demorai_brute_static.webp",
        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_demorai_brute_attack", 
                LengthInSeconds = 0.8, 
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.3,
            )
        },

        Sounds = {
            "BasicAttack_Swing":[
                "audio/battle/battle_chars/demorai_brute/attack/swing_1.ogg", 
                "audio/battle/battle_chars/demorai_brute/attack/swing_2.ogg", 
                "audio/battle/battle_chars/demorai_brute/attack/swing_3.ogg"],
            "BasicAttack_Impact":[
                "audio/battle/battle_chars/demorai_brute/attack/impact_1.ogg", 
                "audio/battle/battle_chars/demorai_brute/attack/impact_2.ogg", 
                "audio/battle/battle_chars/demorai_brute/attack/impact_3.ogg",
                "audio/battle/battle_chars/demorai_brute/attack/impact_4.ogg"],

            "Char_BeenHit":          [
                "audio/battle/battle_chars/demorai_brute/roar_beenhit/beenhit1.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_beenhit/beenhit2.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_beenhit/beenhit3.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_beenhit/beenhit4.ogg"],
            "Char_UseSkill":         [
                "audio/battle/battle_chars/demorai_brute/roar_strike/strike1.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_strike/strike2.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_strike/strike3.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_strike/strike4.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_strike/strike5.ogg"],
            "Char_Die":              [
                "audio/battle/battle_chars/demorai_brute/roar_death/death1.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_death/death2.ogg",
                "audio/battle/battle_chars/demorai_brute/roar_death/death3.ogg"]},

        SoundsVolCorrection = {"BasicAttack_Impact":0.55},
        SoundsExtraSilence = {"BasicAttack_Swing":0.3},

        SpriteOffset = (0, 20),
        FocusRectSize = (250, 450)
    )

    skinLib["demorai_scorpion"] = RegisterCharSkin("demorai_scorpion",
        Portrait = "images/battle_skins/demorai/scorpion/battle_sprite_demorai_scorpion_portrait.webp",
        Sprite = "images/battle_skins/demorai/scorpion/battle_sprite_demorai_scorpion_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_demorai_scorpion_attack", 
                LengthInSeconds = 0.9, 
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.3,
            )
        },

        SpriteOffset = (0, 90),
        FocusRectSize = (400, 360),
        SpriteVFXOffset = (0, -175)
    )

    skinLib["demorai_scorpion_red"] = RegisterCharSkin("demorai_scorpion_red",
        Portrait =  "images/battle_skins/demorai/scorpion_red/battle_sprite_demorai_scorpion_portait.webp",
        Sprite =    "images/battle_skins/demorai/scorpion_red/battle_sprite_demorai_scorpion_red_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_demorai_scorpion_red_attack", 
                LengthInSeconds = 0.9, 
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.3,
            )
        },

        SpriteOffset = (0, 90), 
        FocusRectSize = (400, 360),
        SpriteVFXOffset = (0, -175)
    )

    skinLib["bazark_worm"] = RegisterCharSkin("bazark_worm",
        Portrait =  "images/battle_skins/neutral/bazark_worm/battle_sprite_bazark_portrait.webp",
        Sprite =    "images/battle_skins/neutral/bazark_worm/battle_sprite_bazark_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_bazark_attack", 
                LengthInSeconds = 0.8, 
                WarmupTo = 0.65,
                Transform_AttackDelay = 0.5,
            )
        },

        Sounds = {
            "BasicAttack_Swing":["audio/battle/battle_chars/bazark/BasicAttackSwing.ogg"],
            "Char_BeenHit":     ["audio/battle/battle_chars/bazark/BeenHit.ogg"],
            "Char_Die":         ["audio/battle/battle_chars/bazark/Die.ogg"]
        },

        FocusRectSize = (450, 620)
    )

    skinLib["demorai_frog"] = RegisterCharSkin("demorai_frog",
        Portrait =  "images/battle_skins/neutral/demon_frog/battle_sprite_demon_frog_portrait.webp",
        Sprite =    "images/battle_skins/neutral/demon_frog/battle_sprite_demon_frog_static.webp",

        Anims = {
            "idle":     BattleAnimation(
                Displayable = "battle_anim_demon_frog_idle", 
                ApplyTransform = False,
                AnimLoop = True,
            ),
            "attack":   BattleAnimation(
                Displayable = "battle_anim_demon_frog_attack",  
                LengthInSeconds = 0.9, 
                WarmupTo = 0.42,
                Transform_AttackDelay = 0.42,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/frog/BeenHit.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/frog/SkillUse.ogg",
                                    "audio/battle/battle_chars/frog/SkillUse2.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/frog/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/frog/BasicAttackImpact.ogg"]},

        FocusRectSize = (700, 620),
        SpriteVFXOffset = (0, -250)
    )

    skinLib["bandit_1"] = RegisterCharSkin("bandit_1",
        Portrait =  "images/battle_skins/bandits/band1/battle_sprite_bandit_1_portrait.webp",
        Sprite =    "images/battle_skins/bandits/band1/battle_sprite_bandit_1_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_bandit_1_attack", 
                LengthInSeconds = 0.55, 
                WarmupTo = 0.28, 
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/bandit/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bandit/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/bandit/BasicAttackImpact.ogg"]
        },

        FocusRectSize = (185, 335)
    )

    skinLib["bandit_2"] = RegisterCharSkin("bandit_2",
        Portrait =  "images/battle_skins/bandits/band2/battle_sprite_bandit_2_portrait.webp",
        Sprite =    "images/battle_skins/bandits/band2/battle_sprite_bandit_2_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_bandit_2_attack", 
                LengthInSeconds = 0.55, 
                WarmupTo = 0.28, 
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/bandit/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bandit/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/bandit/BasicAttackImpact.ogg"]
        },

        FocusRectSize = (185, 335)
    )

    skinLib["guard"] = RegisterCharSkin("guard",
        Portrait =  "images/battle_skins/novaras/guard/battle_sprite_guard_portrait.webp",
        Sprite =    "images/battle_skins/novaras/guard/battle_sprite_guard_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_guard_attack", 
                LengthInSeconds = 0.75, 
                WarmupTo = 0.33,
                Transform_AttackDelay = 0.3,
            ),
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/guard/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/guard/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/guard/Die.ogg"]
        },

        FocusRectSize = (185, 370)
    )

    skinLib["bigSlimelark"] = RegisterCharSkin("bigSlimelark",
        Portrait =  "images/battle_skins/neutral/bigSlimelark/battle_sprite_big_slimelark_portrait.webp",
        Sprite =    "images/battle_skins/neutral/bigSlimelark/battle_sprite_big_slimelark_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_big_slimelark_attack", 
                LengthInSeconds = 0.75, 
                WarmupTo = 0.37,
                Transform_AttackDelay = 0.35,
            )
        },

        Sounds = {
            "Char_UseSkill":         ["audio/battle/battle_chars/slimelark/SkillUse.ogg"],
        },

        FocusRectSize = (430, 430)
    )

    skinLib["caltrack"] = RegisterCharSkin("caltrack",
        Portrait =  "images/battle_skins/caltrack/battle_sprite_caltrack_portrait.webp",
        Sprite =    "images/battle_skins/caltrack/battle_sprite_caltrack_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_caltrack_attack", 
                LengthInSeconds = 0.9, 
                WarmupTo = 0.45,
                Transform_AttackDelay = 0.35,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/caltrack/attack_impact.ogg"],
            "Char_BeenHit":          ["audio/battle/battle_chars/caltrack/beenhit.ogg"],
            "Char_UseSkill":         ["audio/battle/battle_chars/caltrack/attack_1.ogg"],
            "Char_Die":              ["audio/battle/battle_chars/caltrack/death.ogg"],
        },

        FocusRectSize = (700, 600),
        SpriteOffset = (0, 100),
    )

    skinLib["abomination"] = RegisterCharSkin("abomination",
        Portrait =  "images/battle_skins/abomination/battle_sprite_abomination_portrait.webp",
        Sprite =    "images/battle_skins/abomination/battle_sprite_abomination_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_abomination_attack", 
                LengthInSeconds = 0.5, 
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":          ["audio/battle/battle_chars/abomination/been_hit.ogg"],
            "Char_UseSkill":         ["audio/battle/battle_chars/abomination/attack.ogg", "audio/battle/battle_chars/abomination/attack2.ogg"],
            "Char_Die":              ["audio/battle/battle_chars/abomination/death.ogg"],
        },

        FocusRectSize = (390, 362)
    )

    skinLib["man_in_black"] = RegisterCharSkin("man_in_black",
        Portrait =  "images/battle_skins/neutral/man_in_black/battle_sprite_mib_portrait.webp",
        Sprite =    "images/battle_skins/neutral/man_in_black/battle_sprite_mib_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mib_attack", 
                LengthInSeconds = 1.0, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },
        
        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/man_in_black/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/man_in_black/Die.ogg"],
            "BasicAttack_Swing":    ["audio/battle/battle_chars/man_in_black/BasicAttackSwing.ogg"],
            # unused
            "Skill_Gurgle1":        ["audio/battle/battle_chars/man_in_black/SkillUse.ogg"],
            "Skill_Gurgle2":        ["audio/battle/battle_chars/man_in_black/SkillUse_2.ogg"]
        },

        FocusRectSize = (210, 400)
    )

    skinLib["slimelark"] = RegisterCharSkin("slimelark",
        Portrait =  "images/battle_skins/neutral/slimelark/battle_sprite_slimelark_portrait.webp",
        Sprite =    "images/battle_skins/neutral/slimelark/battle_sprite_slimelark_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_slimelark_attack", 
                LengthInSeconds = 0.75, 
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_UseSkill":         ["audio/battle/battle_chars/slimelark/SkillUse.ogg"],
        },
        FocusRectSize = (310, 310)
    )

    skinLib["kraken"] = RegisterCharSkin("kraken",
        Portrait =  "images/battle_skins/neutral/kraken/battle_sprite_kraken_portrait.webp",
        Sprite =    "images/battle_skins/neutral/kraken/battle_sprite_kraken_static.webp",

        Anims = {
            "idle":BattleAnimation(ApplyTransform = False),
            #"hit":BattleAnimation(ApplyTransform = False),
            "attack":BattleAnimation(
                Displayable = "battle_anim_kraken_attack", 
                LengthInSeconds = 1.0, 
                WarmupTo = 0.45,
                ApplyTransform = False,
            )
        },

        FocusRectSize = (420, 360)
    )

    skinLib["crazy_rat"] = RegisterCharSkin("crazy_rat",
        Portrait =  "images/battle_skins/neutral/rat/battle_sprite_crazy_rat_portrait.webp",
        Sprite =    "images/battle_skins/neutral/rat/battle_sprite_crazy_rat_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_crazy_rat_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/rat/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/rat/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/rat/Die.ogg"]
        },
    
        FocusRectSize = (325, 240)
    )

    # unused/untested
    skinLib["rat_desert"] = RegisterCharSkin("rat_desert",
        Portrait =  "images/battle_skins/neutral/rat_desert/battle_sprite_desert_rat_portrait.webp",
        Sprite =    "images/battle_skins/neutral/rat_desert/battle_sprite_desert_rat_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_desert_rat_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/rat/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/rat/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/rat/Die.ogg"]
        },
    
        FocusRectSize = (325, 240)
    )

    skinLib["crazy_rat_mother"] = RegisterCharSkin("crazy_rat_mother",
        Portrait =  "images/battle_skins/neutral/rat_mother/battle_sprite_crazy_rat_mother_portrait.webp",
        Sprite =    "images/battle_skins/neutral/rat_mother/battle_sprite_crazy_rat_mother_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_crazy_rat_mother_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/rat_mother/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/rat_mother/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/rat_mother/Die.ogg"],

            # unused
            "Skill_Howl":           ["audio/battle/battle_chars/rat_mother/SkillHowl.ogg"]
        },
    
        SpriteOffset = (0, 25),
        FocusRectSize = (385, 400)
    )

    skinLib["raider"] = RegisterCharSkin("raider",
        Portrait =  "images/battle_skins/bandits/raider/battle_sprite_raider_portrait.webp",
        Sprite =    "images/battle_skins/bandits/raider/battle_sprite_raider_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_raider_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/bandit/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bandit/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/bandit/BasicAttackImpact.ogg"]
        },

        FocusRectSize = (195, 400)
    )
    
    skinLib["spiderman"] = RegisterCharSkin("spiderman",
        Portrait =  "images/battle_skins/neutral/spiderman/battle_sprite_spiderman_portrait.webp",
        Sprite =    "images/battle_skins/neutral/spiderman/battle_sprite_spiderman_static.webp",

        Anims = {
            "attack":[BattleAnimation(
                Displayable = "battle_anim_spiderman_attack1", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            ),
            BattleAnimation(
                Displayable = "battle_anim_spiderman_attack2", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
                ApplyTransform = False,
            ),],
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/camen/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/camen/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/camen/BasicAttackImpact.ogg"]
        },

        SpriteOffset = (0, 25),
        FocusRectSize = (340, 345),
    )
    
    skinLib["dark_soldier"] = RegisterCharSkin("dark_soldier",
        Portrait =  "images/battle_skins/dark_soldier/battle_sprite_dark_soldier_portrait.webp",
        Sprite =    "images/battle_skins/dark_soldier/battle_sprite_dark_soldier_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_dark_soldier_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },
    
        FocusRectSize = (195, 430)
    )
    
    skinLib["ghoul"] = RegisterCharSkin("ghoul",
        Portrait =  "images/battle_skins/ghoul/battle_sprite_ghoul_portrait.webp",
        Sprite =    "images/battle_skins/ghoul/battle_sprite_ghoul_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_ghoul_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (220, 390)
    )

    skinLib["ghoul_big"] = RegisterCharSkin("ghoul_big",
        Portrait =  "images/battle_skins/ghoul_big/battle_sprite_ghoul_big_portrait.webp",
        Sprite =    "images/battle_skins/ghoul_big/battle_sprite_ghoul_big_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_ghoul_big_attack", 
                LengthInSeconds = 0.8, 
                WarmupTo = 0.45,
                Transform_AttackDelay = 0.4,
            )
        },

        FocusRectSize = (260, 440)
    )
    
    skinLib["goblin"] = RegisterCharSkin("goblin",
        Portrait =  "images/battle_skins/neutral/goblin/battle_sprite_goblin_portrait.webp",
        Sprite =    "images/battle_skins/neutral/goblin/battle_sprite_goblin_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_goblin_attack", 
                LengthInSeconds = 0.6, 
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit": ["audio/battle/battle_chars/goblin/BeenHit.ogg"],
            "Char_UseSkill": ["audio/battle/battle_chars/goblin/skilluse1.ogg",
                            "audio/battle/battle_chars/goblin/skilluse2.ogg",
                            "audio/battle/battle_chars/goblin/skilluse3.ogg",
                            "audio/battle/battle_chars/goblin/skilluse4.ogg"],
            "Char_Die": ["audio/battle/battle_chars/goblin/Die.ogg"]
        },
        

        FocusRectSize = (170, 310)
    )

    skinLib["alderay_scout"] = RegisterCharSkin("alderay_scout",
        Portrait =  "images/battle_skins/novaras/scout/battle_sprite_scout_portrait.webp",
        Sprite =    "images/battle_skins/novaras/scout/battle_sprite_scout_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_scout_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.2,
            )
        },
    
        FocusRectSize = (170, 350)
    )

    skinLib["bear"] = RegisterCharSkin("bear",
        Portrait =  "images/battle_skins/neutral/bear/battle_sprite_bear_portrait.webp",
        Sprite =    "images/battle_skins/neutral/bear/battle_sprite_bear_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_bear_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_UseSkill":        ["audio/battle/battle_chars/bear/SkillUse.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/bear/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bear/Die.ogg"]
        },

        FocusRectSize = (360, 330)
    )
    
    skinLib["bear_white"] = RegisterCharSkin("bear_white",
        Portrait =  "images/battle_skins/neutral/bear_white/battle_sprite_bear_white_portrait.webp",
        Sprite =    "images/battle_skins/neutral/bear_white/battle_sprite_bear_white_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_bear_white_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_UseSkill":        ["audio/battle/battle_chars/bear/SkillUse.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bear/Die.ogg"]
        },

        FocusRectSize = (480, 380)
    )

    skinLib["lizard_red"] = RegisterCharSkin("lizard_red",
        Portrait =  "images/battle_skins/neutral/lizards/lizard_red/battle_sprite_lizard_red_portrait.webp",
        Sprite =    "images/battle_skins/neutral/lizards/lizard_red/battle_sprite_lizard_red_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_lizard_red_attack",
                LengthInSeconds = 0.5,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "BasicAttack_Impact":["audio/battle/battle_chars/lizards/BasicAttackImpact.ogg"],
            "Char_BeenHit":["audio/battle/battle_chars/lizards/BeenHit.ogg"],
            "Char_Die":["audio/battle/battle_chars/lizards/Die.ogg"]
        },

        FocusRectSize = (205, 350)
    )

    skinLib["lizard_blue"] = RegisterCharSkin("lizard_blue",
        Portrait =  "images/battle_skins/neutral/lizards/lizard_blue/battle_sprite_lizard_blue_portrait.webp",
        Sprite =    "images/battle_skins/neutral/lizards/lizard_blue/battle_sprite_lizard_blue_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_lizard_blue_attack",
                LengthInSeconds = 0.5,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        FocusRectSize = (205, 350)
    )

    skinLib["lizard_green"] = RegisterCharSkin("lizard_green",
        Portrait =  "images/battle_skins/neutral/lizards/lizard_green/battle_sprite_lizard_green_portrait.webp",
        Sprite =    "images/battle_skins/neutral/lizards/lizard_green/battle_sprite_lizard_green_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_lizard_green_attack",
                LengthInSeconds = 0.5,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        FocusRectSize = (205, 350)
    )

    skinLib["wolf"] = RegisterCharSkin("wolf",
        Portrait =  "images/battle_skins/neutral/wolf/battle_sprite_wolf_portrait.webp",
        Sprite =    "images/battle_skins/neutral/wolf/battle_sprite_wolf_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_wolf_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "BasicAttack_Impact":["audio/battle/battle_chars/wolf/attack_impact.ogg"],
            "Char_BeenHit":["audio/battle/battle_chars/wolf/beenhit.ogg"],
            # unused, unique
            "Howl":["audio/battle/battle_chars/wolf/use_skill.ogg"], 
            "Char_Die":["audio/battle/battle_chars/wolf/die.ogg"]},

        FocusRectSize = (290, 280)
    )

    skinLib["stag"] = RegisterCharSkin("stag",
        Portrait =  "images/battle_skins/neutral/stag/battle_sprite_stag_portrait.webp",
        Sprite =    "images/battle_skins/neutral/stag/battle_sprite_stag_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_stag_attack",
                LengthInSeconds = 0.8,
                WarmupTo = 0.55,
                Transform_AttackDelay = 0.5,
            )
        },

        Sounds = {
            "BasicAttack_Impact":["audio/battle/battle_chars/stag/BasicAttackHit.ogg"],

            "Char_BeenHit":["audio/battle/battle_chars/stag/BeenHit.ogg"],
            "Char_UseSkill":["audio/battle/battle_chars/stag/SkillUse.ogg"],
            "Char_Die":["audio/battle/battle_chars/stag/Die.ogg"]
        },

        FocusRectSize =     (240, 350),
        SpriteVFXOffset =   (45,  -175)
    )

    skinLib["skin_swindler"] = RegisterCharSkin("skin_swindler",
        Portrait =  "images/battle_skins/bandits/swindler/battle_sprite_swindler_portrait.webp",
        Sprite =    "images/battle_skins/bandits/swindler/battle_sprite_swindler_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_swindler_attack",
                LengthInSeconds = 0.55,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/bandit/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bandit/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/bandit/BasicAttackImpact.ogg"]
        },

        FocusRectSize = (170, 370)
    )

    skinLib["borras"] = RegisterCharSkin("borras",
        Portrait =  "images/characters/borras/portrait.webp",
        Sprite =    "images/battle_skins/borras/battle_sprite_borras_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_borras_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/borras/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/borras/BeenHit.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/borras/SkillUse.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/borras/Die.ogg"]
        },

        FocusRectSize = (200, 370)
    )

    skinLib["skin_duprey"] = RegisterCharSkin("skin_duprey",
        Portrait =  "images/characters/duprey/portrait.webp",
        Sprite =    "images/battle_skins/duprey/battle_sprite_duprey_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_duprey_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (205, 320)
    )

    skinLib["elena_human"] = RegisterCharSkin("elena_human",
        Portrait = "images/characters/elena/portrait.webp",
        Sprite = "images/battle_skins/elena/human/battle_sprite_elena_human_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_elena_human_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/elena_human/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/elena_human/Die.ogg"],
            "Transform":            ["audio/battle/battle_chars/elena_human/WolfTransform.ogg"]
        },

        FocusRectSize = (190, 350)
    )

    skinLib["elena_wolf"] = RegisterCharSkin("elena_wolf",
        Portrait =  "images/characters/elena/portrait_wolf.webp",
        Sprite =    "images/battle_skins/elena/wolf/battle_sprite_elena_wolf_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_elena_wolf_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Transform":            ["audio/battle/battle_chars/elena_human/WolfTransform.ogg"]
        },

        FocusRectSize = (270, 320)
    )

    skinLib["kiara"] = RegisterCharSkin("kiara",
        Portrait =  "images/characters/kiara/portrait.webp",
        Sprite =    "images/battle_skins/kiara/human/battle_sprite_kiara_human_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_kiara_human_attack",
                LengthInSeconds = 0.8,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.15,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/kiara/BeenHit.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/kiara/SkillUse.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/kiara/Die.ogg"]
        },

        FocusRectSize = (180, 340)
    )

    skinLib["kiara_party"] = RegisterCharSkin("kiara_party",
        Portrait =  "images/battle_skins/kiara/party/portrait.webp",
        Sprite =    "images/battle_skins/kiara/party/battle_sprite_kiara_party_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_kiara_party_attack",
                LengthInSeconds = 0.8,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.15,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/kiara/BeenHit.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/kiara/SkillUse.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/kiara/Die.ogg"]
        },

        FocusRectSize = (180, 340)
    )

    skinLib["markus_p"] = RegisterCharSkin("markus_p",
        Portrait =  "images/characters/markus/portrait_p.webp",
        Sprite =    "images/battle_skins/markus/prologue/battle_sprite_markus_prologue_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable =       "battle_anim_markus_prologue_attack",
                LengthInSeconds =   0.6,
                WarmupTo =          0.45,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/markus/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/markus/Die.ogg"]
        },

        FocusRectSize = (170, 350)
    )

    skinLib["markus"] = RegisterCharSkin("markus",
        Portrait = "images/characters/markus/portrait.webp",
        Sprite = "images/battle_skins/markus/postpara/battle_sprite_markus_postpara_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_markus_postpara_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/markus/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/markus/Die.ogg"],
            
            "Transform":            ["audio/cfx/transform.ogg"]
        },

        FocusRectSize = (170, 380)
    )

    skinLib["markus_fem_party"] = RegisterCharSkin("markus_fem_party",
        Portrait =  "images/battle_skins/markus/fem_party/portrait.webp",
        Sprite =    "images/battle_skins/markus/fem_party/battle_sprite_markus_fem_party_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_markus_fem_party_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/kiara/BeenHit.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/kiara/SkillUse.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/kiara/Die.ogg"]
        },

        FocusRectSize = (170, 380)
    )

    skinLib["markus_transformed"] = RegisterCharSkin("markus_transformed",
        Portrait =  "images/characters/markus/portrait_t.webp",
        Sprite =    "images/battle_skins/markus/transformed/battle_sprite_markus_tf_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable =       "battle_anim_markus_tf_attack",
                LengthInSeconds =   0.8,
                WarmupTo =          0.45,
                Transform_AttackDelay = 0.35,
            ),
            "attack_fire":BattleAnimation(
                Displayable =       "battle_anim_markus_tf_attack_2",
                LengthInSeconds =   0.9,
                WarmupTo =          0.3,
                ApplyTransform =    False,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/markus_transformed/BeenHit_1.ogg", "audio/battle/battle_chars/markus_transformed/BeenHit_2.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/markus_transformed/Die.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/markus_transformed/SkillUse.ogg"],

            "Transform":            ["audio/cfx/transform.ogg"]
        },

        SpriteOffset =  (0, 30),
        FocusRectSize = (320, 440)
    )

    # prologue
    skinLib["mc_p"] = RegisterCharSkin("mc_p",
        Portrait = "images/characters/mc/portrait_p.webp",
        Sprite = "images/battle_skins/mc/prologue/battle_sprite_mc_prologue_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mc_prologue_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/mc/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/mc/Die.ogg"],

            "BasicAttack_Swing":    ["audio/battle/battle_chars/mc/BasicAttackSwing.ogg"]
        },

        FocusRectSize = (170, 350)
    )

    # main
    skinLib["mc"] = RegisterCharSkin("mc",
        Portrait = "images/characters/mc/portrait.webp",
        Sprite = "images/battle_skins/mc/post_para/battle_sprite_mc_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mc_postpara_attack",
                LengthInSeconds = 0.65,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/mc/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/mc/Die.ogg"],

            "BasicAttack_Swing":    ["audio/battle/battle_chars/mc/BasicAttackSwing.ogg"],
            "Transform":            ["audio/cfx/transform.ogg"]
        },

        FocusRectSize = (210, 380)
    )
    
    # transformed
    skinLib["mc_transformed"] = RegisterCharSkin("mc_transformed",
        Portrait = "images/characters/mc/portrait_t.webp",
        Sprite = "images/battle_skins/mc/transformed/battle_sprite_mc_tf_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mc_tf_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/mc_transformed/char/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/mc_transformed/char/Die.ogg"],
            "Char_UseSkill":        ["audio/battle/battle_chars/mc_transformed/char/skilluse1.ogg",
                                    "audio/battle/battle_chars/mc_transformed/char/skilluse2.ogg",
                                    "audio/battle/battle_chars/mc_transformed/char/skilluse3.ogg",
                                    "audio/battle/battle_chars/mc_transformed/char/skilluse4.ogg",
                                    "audio/battle/battle_chars/mc_transformed/char/skilluse5.ogg"],
            "BasicAttack_Swing":    ["audio/battle/battle_chars/mc_transformed/basic_attack/swing.ogg"],
            "BasicAttack_Impact":    ["audio/battle/battle_chars/mc_transformed/basic_attack/impact1.ogg",
                                    "audio/battle/battle_chars/mc_transformed/basic_attack/impact2.ogg",
                                    "audio/battle/battle_chars/mc_transformed/basic_attack/impact3.ogg",
                                    "audio/battle/battle_chars/mc_transformed/basic_attack/impact4.ogg",
                                    "audio/battle/battle_chars/mc_transformed/basic_attack/impact5.ogg"],
            "Transform":            ["audio/cfx/transform.ogg"]
        },

        FocusRectSize = (320, 440)
    )

    # new armor
    skinLib["mc_na"] = RegisterCharSkin("mc_na",
        Portrait = "images/characters/mc/portrait.webp",
        Sprite = "images/battle_skins/mc/new_armor/battle_sprite_mc_new_armor_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mc_new_armor_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/mc/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/mc/Die.ogg"],
            "BasicAttack_Swing":    ["audio/battle/battle_chars/mc/BasicAttackSwing.ogg"],
            "Transform":            ["audio/cfx/transform.ogg"]
        },

        FocusRectSize = (219, 332)
    )

    # new armor
    skinLib["mc_party"] = RegisterCharSkin("mc_party",
        Portrait =  "images/battle_skins/mc/party/portrait.webp",
        Sprite =    "images/battle_skins/mc/party/battle_sprite_mc_party_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mc_party_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.2,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/mc/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/mc/Die.ogg"],
            "BasicAttack_Swing":    ["audio/battle/battle_chars/mc/BasicAttackSwing.ogg"],
            "Transform":            ["audio/cfx/transform.ogg"]
        },

        FocusRectSize = (219, 332)
    )

    skinLib["mika"] = RegisterCharSkin("mika",
        Portrait = "images/characters/mika/portrait.webp",
        Sprite = "images/battle_skins/mika/battle_sprite_mika_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_mika_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.4,
                
                ApplyTransform = False,
            )
        },
        
        Sounds = {
            "Char_BeenHit":["audio/battle/battle_chars/mika/BeenHit.ogg",   
                            "audio/battle/battle_chars/mika/BeenHit_2.ogg"],
            "Char_Die":["audio/battle/battle_chars/mika/Die.ogg"]
        },

        FocusRectSize = (180, 370)
    )

    skinLib["jana"] = RegisterCharSkin("jana",
        Portrait =  "images/characters/jana/portrait.webp",
        Sprite =    "images/battle_skins/jana/battle_sprite_jana_static.webp",
        
        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_jana_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.5,
                ApplyTransform = False,
            )
        },


        Sounds = {
            "Char_BeenHit":["audio/battle/battle_chars/mika/BeenHit.ogg",   
                            "audio/battle/battle_chars/mika/BeenHit_2.ogg"],
            "Char_Die":["audio/battle/battle_chars/mika/Die.ogg"]
        },

        FocusRectSize = (180, 370)
    )

    skinLib["myu"] = RegisterCharSkin("myu",
        Portrait =  "images/characters/myu/portrait.webp",
        Sprite =    "images/battle_skins/myu/battle_sprite_myu_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_myu_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/myu/BasicAttackHit.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/myu/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/myu/Die.ogg"],
            },

        FocusRectSize = (180, 400)
    )
    
    skinLib["skin_tarek"] = RegisterCharSkin("skin_tarek",
        Portrait =  "images/battle_skins/bandits/tarek/battle_sprite_tarek_portrait.webp",
        Sprite =    "images/battle_skins/bandits/tarek/battle_sprite_tarek_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_tarek_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/bandit/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bandit/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/bandit/BasicAttackImpact.ogg"]
        },

        FocusRectSize = (190, 350)
    )

    skinLib["ves"] = RegisterCharSkin("ves",
        Portrait =  "images/characters/ves/portrait.webp",
        Sprite =    "images/battle_skins/ves/battle_sprite_ves_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_ves_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },
        
        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/ves/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/ves/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/ves/BasicAttackImpact.ogg"],

            # unused
            "Skill_Shout":          ["audio/battle/battle_chars/ves/Skill_Shout.ogg"],
        },

        FocusRectSize = (220, 360)
    )
    
    skinLib["ves_party"] = RegisterCharSkin("ves_party",
        Portrait =  "images/battle_skins/ves/party/portrait.webp",
        Sprite =    "images/battle_skins/ves/party/battle_sprite_ves_party_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_ves_party_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.2,
                Transform_AttackDelay = 0.25,
            )
        },
        
        Sounds = {
            "Char_BeenHit":         ["audio/battle/battle_chars/ves/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/ves/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/ves/BasicAttackImpact.ogg"],

            # unused
            "Skill_Shout":          ["audio/battle/battle_chars/ves/Skill_Shout.ogg"],
        },

        FocusRectSize = (220, 360)
    )
    
    skinLib["ghoul_red"] = RegisterCharSkin("ghoul_red",
        Portrait =  "images/battle_skins/ghoul_red/battle_sprite_ghoul_red_portrait.webp",
        Sprite =    "images/battle_skins/ghoul_red/battle_sprite_ghoul_red_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_ghoul_red_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (250, 350)
    )
    
    skinLib["zanarak"] = RegisterCharSkin("zanarak",
        Portrait =  "images/battle_skins/demorai/zanarak/battle_sprite_zanarak_portrait.webp",
        Sprite =    "images/battle_skins/demorai/zanarak/battle_sprite_zanarak_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_zanarak_attack",
                LengthInSeconds = 1.1,
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.35,
            )
        },

        FocusRectSize = (380, 650),
        SpriteOffset = (0, 40)
    )
    
    skinLib["snakeman"] = RegisterCharSkin("snakeman",
        Portrait =  "images/battle_skins/demorai/snakeman/battle_sprite_snakeman_portrait.webp",
        Sprite =    "images/battle_skins/demorai/snakeman/battle_sprite_snakeman_static.webp",

        Anims = {
            "idle":     BattleAnimation(
                Displayable = "battle_anim_snakeman_idle",
                AnimLoop = True,
            ),
            "attack":   BattleAnimation(
                Displayable = "battle_anim_snakeman_attack",
                LengthInSeconds = 0.75,
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.3,
            )
        },

        FocusRectSize = (230, 380)
    )
    
    skinLib["poltrik"] = RegisterCharSkin("poltrik",
        Portrait =  "images/battle_skins/poltrik/battle_sprite_poltrik_portrait.webp",
        Sprite =    "images/battle_skins/poltrik/battle_sprite_poltrik_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_poltrik_attack",
                LengthInSeconds = 0.65,
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.35,
            )
        },

        FocusRectSize = (270, 380)
    )
    
    skinLib["erika"] = RegisterCharSkin("erika",
        Portrait = "images/characters/erika/portrait.webp",
        Sprite = "images/battle_skins/erika/battle_sprite_erika_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_erika_attack",
                LengthInSeconds = 0.55,
                WarmupTo = 0.2,
                Transform_AttackDelay = 0.15,
            )
        },


        FocusRectSize = (175, 340)
    )

    skinLib["kiara_banshee"] = RegisterCharSkin("kiara_banshee",
        Portrait =  "images/characters/kiara/demorai/portrait.webp",
        Sprite =    "images/battle_skins/kiara/banshee/battle_sprite_kiara_banshee_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_kiara_banshee_attack",
                LengthInSeconds = 0.8,
                WarmupTo = 0.45,
                Transform_AttackDelay = 0.35,
            )
        },

        FocusRectSize = (200, 370)
    )

    skinLib["assassin"] = RegisterCharSkin("assassin",
        Portrait =  "images/battle_skins/assassin/battle_sprite_assassin_portrait.webp",
        Sprite =    "images/battle_skins/assassin/battle_sprite_assassin_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_assassin_attack",
                LengthInSeconds = 0.55,
                WarmupTo = 0.4,
                ApplyTransform = False,
            )
        },

        Sounds = {
            "BasicAttack_Swing":    ["audio/battle/battle_chars/assassin/crossbow_shot_1.ogg", 
                                    "audio/battle/battle_chars/assassin/crossbow_shot_2.ogg",
                                    "audio/battle/battle_chars/assassin/crossbow_shot_3.ogg",
                                    ],
            "Char_BeenHit":         ["audio/battle/battle_chars/bandit/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/bandit/Die.ogg"],
            "BasicAttack_Impact":   ["audio/battle/battle_chars/bandit/BasicAttackImpact.ogg"]
        },

        SoundsVolCorrection = {
            "BasicAttack_Swing":0.5
        },

        FocusRectSize = (175, 360)
    )

    skinLib["valchek"] = RegisterCharSkin("valchek",
        Portrait =  "images/characters/valchek/portrait_hood.webp",
        Sprite =    "images/battle_skins/valchek/battle_sprite_valchek_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_valchek_attack",
                LengthInSeconds = 0.5,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.1,
            )
        },

        Sounds = {
            "Char_BeenHit":     ["audio/battle/battle_chars/mika/BeenHit.ogg",   
                                "audio/battle/battle_chars/mika/BeenHit_2.ogg"],
            "Char_Die":         ["audio/battle/battle_chars/mika/Die.ogg"],
            "Char_UseSkill":    ["audio/battle/battle_chars/kiara/SkillUse.ogg"]
        },

        FocusRectSize = (180, 360)
    )

    skinLib["sypha"] = RegisterCharSkin("sypha",
        Portrait =  "images/characters/sypha/portrait.webp",
        Sprite =    "images/battle_skins/sypha/battle_sprite_sypha_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_sypha_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.15,
            )
        },

        Sounds = {
            "Char_BeenHit":     ["audio/battle/battle_chars/mika/BeenHit.ogg",   
                                "audio/battle/battle_chars/mika/BeenHit_2.ogg"],
            "Char_Die":         ["audio/battle/battle_chars/mika/Die.ogg"],
            "Char_UseSkill":    ["audio/battle/battle_chars/kiara/SkillUse.ogg"]
        },

        FocusRectSize = (200, 390)
    )

    skinLib["merlanian_soldier"] = RegisterCharSkin("merlanian_soldier",
        Portrait =  "images/battle_skins/merlanian_soldier/battle_sprite_merlanian_soldier_portrait.webp",
        Sprite =    "images/battle_skins/merlanian_soldier/battle_sprite_merlanian_soldier_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_merlanian_soldier_attack",
                LengthInSeconds = 0.75,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.15,
            )
        },

        Sounds = {
            "BasicAttack_Impact":    ["audio/battle/battle_chars/merlanian_soldier/strike_impact.ogg"],
            "Char_BeenHit":     ["audio/battle/battle_chars/merlanian_soldier/been_hit.ogg"],
            "Char_Die":         ["audio/battle/battle_chars/merlanian_soldier/death.ogg"],
        },

        FocusRectSize = (200, 440)
    )

    skinLib["merlanian_general"] = RegisterCharSkin("merlanian_general",
        Portrait =  "images/battle_skins/merlanian_general/battle_sprite_merlanian_general_portrait.webp",
        Sprite =    "images/battle_skins/merlanian_general/battle_sprite_merlanian_general_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_merlanian_general_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.25,
                Transform_AttackDelay = 0.15,
                ApplyTransform = False,
                SoundSwing_DoNotCutOffOnImpact = True,
            )
        },

        Sounds = {
            "BasicAttack_Swing":    ["audio/battle/battle_chars/merlanian_general/attack_1.ogg", 
                                    "audio/battle/battle_chars/merlanian_general/attack_2.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/merlanian_general/been_hit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/merlanian_general/death.ogg"],
        },

        FocusRectSize = (240, 510)
    )

    skinLib["slime_green"] = RegisterCharSkin("slime_green",
        Portrait =  "images/battle_skins/neutral/slime_green/battle_sprite_slime_green_portrait.webp",
        Sprite =    "images/battle_skins/neutral/slime_green/battle_sprite_slime_green_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_slime_green_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.35,
                Transform_AttackDelay = 0.25,
            )
        },

        Sounds = {
            "Char_UseSkill":         ["audio/battle/battle_chars/slimelark/SkillUse.ogg"],
        },

        FocusRectSize = (430, 400)
    )

    skinLib["desert_rat_queen"] = RegisterCharSkin("desert_rat_queen",
        Portrait =  "images/battle_skins/neutral/desert_rat_queen/battle_sprite_desratq_portrait.webp",
        Sprite =    "images/battle_skins/neutral/desert_rat_queen/battle_sprite_desratq_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_desratq_attack",
                LengthInSeconds = 0.8,
                WarmupTo = 0.45,
                Transform_AttackDelay = 0.4,
            )
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/rat_mother/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/rat_mother/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/rat_mother/Die.ogg"],

            # unused
            "Skill_Howl":           ["audio/battle/battle_chars/rat_mother/SkillHowl.ogg"]
        },
    
        SpriteOffset = (0, 25),
        FocusRectSize = (385, 400)
    )

    skinLib["wolf_dire"] = RegisterCharSkin("wolf_dire",
        Portrait =  "images/battle_skins/neutral/wolf_dire/battle_sprite_wolf_dire_portrait.webp",
        Sprite =    "images/battle_skins/neutral/wolf_dire/battle_sprite_wolf_dire_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_wolf_dire_attack",
                LengthInSeconds = 0.7,
                WarmupTo = 0.5,
                Transform_AttackDelay = 0.3,
            )
        },

        Sounds = {
            "BasicAttack_Impact":["audio/battle/battle_chars/wolf/attack_impact.ogg"],
            "Char_BeenHit":["audio/battle/battle_chars/wolf/beenhit.ogg"],

            # unused, unique
            "Howl":["audio/battle/battle_chars/wolf/use_skill.ogg"], 

            "Char_Die":["audio/battle/battle_chars/wolf/die.ogg"]
        },

        FocusRectSize = (360, 390)
    )

    skinLib["corpse_eater"] = RegisterCharSkin("corpse_eater",
        Portrait =  "images/battle_skins/corpse_eater/battle_sprite_corpse_eater_portrait.webp",
        Sprite =    "images/battle_skins/corpse_eater/battle_sprite_corpse_eater_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_corpse_eater_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.4,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (360, 390)
    )

    skinLib["succubus"] = RegisterCharSkin("succubus",
        Portrait =  "images/battle_skins/succubus/battle_sprite_succubus_portrait.webp",
        Sprite =    "images/battle_skins/succubus/battle_sprite_succubus_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_succubus_attack",
                LengthInSeconds = 0.5,
                WarmupTo = 0.4,
                ApplyTransform = False,
            )
        },

        FocusRectSize = (360, 390)
    )

    skinLib["guard_hamun"] = RegisterCharSkin("guard_hamun",
        Portrait =  "images/battle_skins/novaras/guard_hamun/battle_sprite_guard_hamun_portrait.webp",
        Sprite =    "images/battle_skins/novaras/guard_hamun/battle_sprite_guard_hamun_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_guard_hamun_attack", 
                LengthInSeconds = 0.7,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            ),
        },

        Sounds = {
            "BasicAttack_Impact":   ["audio/battle/battle_chars/guard/BasicAttackImpact.ogg"],
            "Char_BeenHit":         ["audio/battle/battle_chars/guard/BeenHit.ogg"],
            "Char_Die":             ["audio/battle/battle_chars/guard/Die.ogg"]
        },

        FocusRectSize = (185, 370)
    )

    skinLib["x71"] = RegisterCharSkin("x71",
        Portrait =  "images/battle_skins/x71/battle_sprite_x71_portrait.webp",
        Sprite =    "images/battle_skins/x71/battle_sprite_x71_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_x71_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
            )
        },

        FocusRectSize = (360, 390)
    )
    
    skinLib["theface"] = RegisterCharSkin("theface",
        Portrait =  "images/battle_skins/theface/battle_sprite_theface_portrait.webp",
        Sprite =    "images/battle_skins/theface/battle_sprite_theface_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_theface_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (360, 470)
    )

    skinLib["lizardmonster"] = RegisterCharSkin("lizardmonster",
        Portrait =  "images/battle_skins/lizardmonster/battle_sprite_lizardmonster_portrait.webp",
        Sprite =    "images/battle_skins/lizardmonster/battle_sprite_lizardmonster_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_lizardmonster_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (390, 285)
    )

    skinLib["zombie_half"] = RegisterCharSkin("zombie_half",
        Portrait =  "images/battle_skins/zombie_half/battle_sprite_zombie_half_portrait.webp",
        Sprite =    "images/battle_skins/zombie_half/battle_sprite_zombie_half_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_zombie_half_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (200, 320)
    )

    
    skinLib["zombie_fem"] = RegisterCharSkin("zombie_fem",
        Portrait =  "images/battle_skins/zombie_fem/battle_sprite_zombie_fem_portrait.webp",
        Sprite =    "images/battle_skins/zombie_fem/battle_sprite_zombie_fem_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_zombie_fem_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },

        FocusRectSize = (220, 390),
        SpriteOffset = (0, 30),
    )

    skinLib["ghost_babyface"] = RegisterCharSkin("ghost_babyface",
        Portrait =  "images/battle_skins/ghost_babyface/battle_sprite_ghost_babyface_portrait.webp",
        Sprite =    "images/battle_skins/ghost_babyface/battle_sprite_ghost_babyface_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_ghost_babyface_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
                ApplyTransform = False,
            )
        },

        FocusRectSize = (320, 550)
    )

    skinLib["zombie_butcher"] = RegisterCharSkin("zombie_butcher",
        Portrait =  "images/battle_skins/zombie_butcher/battle_sprite_zombie_butcher_portrait.webp",
        Sprite =    "images/battle_skins/zombie_butcher/battle_sprite_zombie_butcher_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_zombie_butcher_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
                ApplyTransform = False,
            )
        },

        FocusRectSize = (320, 550)
    )

    skinLib["gator"] = RegisterCharSkin("gator",
        Portrait =  "images/battle_skins/neutral/gator/battle_sprite_gator_portrait.webp",
        Sprite =    "images/battle_skins/neutral/gator/battle_sprite_gator_static.webp",

        Anims = {
            "attack":   BattleAnimation(
                Displayable = "battle_anim_gator_attack",
                LengthInSeconds = 0.6, 
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.1,
            )
        },

        # Sounds = {
        #     "Char_BeenHit":         ["audio/battle/battle_chars/frog/BeenHit.ogg"],
        #     "Char_UseSkill":        ["audio/battle/battle_chars/frog/SkillUse.ogg",
        #                             "audio/battle/battle_chars/frog/SkillUse2.ogg"],
        #     "Char_Die":             ["audio/battle/battle_chars/frog/Die.ogg"],
        #     "BasicAttack_Impact":   ["audio/battle/battle_chars/frog/BasicAttackImpact.ogg"]
        # },

        FocusRectSize = (320, 430),
        #SpriteVFXOffset = (0, 0)
    )
        
    skinLib["nightmare_head"] = RegisterCharSkin("nightmare_head",
        Portrait =  "images/battle_skins/nightmare_head/battle_sprite_nightmare_head_portrait.webp",
        Sprite =    "images/battle_skins/nightmare_head/battle_sprite_nightmare_head_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_nightmare_head_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },
        FocusRectSize = (350, 450),
        SpriteOffset = (0, 0)
    )
            
        
    skinLib["nightmare_left_hand"] = RegisterCharSkin("nightmare_left_hand",
        Portrait =  "images/battle_skins/nightmare_left_hand/battle_sprite_nightmare_left_hand_portrait.webp",
        Sprite =    "images/battle_skins/nightmare_left_hand/battle_sprite_nightmare_left_hand_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_nightmare_left_hand_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },
        FocusRectSize = (320, 380),
        SpriteOffset = (-30, -50)
    )

    skinLib["nightmare_right_hand"] = RegisterCharSkin("nightmare_right_hand",
        Portrait =  "images/battle_skins/nightmare_right_hand/battle_sprite_nightmare_right_hand_portrait.webp",
        Sprite =    "images/battle_skins/nightmare_right_hand/battle_sprite_nightmare_right_hand_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_nightmare_right_hand_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                Transform_AttackDelay = 0.25,
            )
        },
        FocusRectSize = (320, 280),
        SpriteOffset = (00, 20)
    )

    skinLib["floating_eye"] = RegisterCharSkin("floating_eye",
        Portrait = "images/battle_skins/floating_eye/battle_sprite_floating_eye_portrait.webp",
        Sprite =   "images/battle_skins/floating_eye/battle_sprite_floating_eye_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_floating_eye_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
                ApplyTransform = False,
            )
        },

        FocusRectSize = (360, 390)
    )

    skinLib["hugo"] = RegisterCharSkin("hugo",
        Portrait = "images/battle_skins/hugo/battle_sprite_hugo_portrait.webp",
        Sprite =   "images/battle_skins/hugo/battle_sprite_hugo_static.webp",

        Anims = {
            "attack":BattleAnimation(
                Displayable = "battle_anim_hugo_attack",
                LengthInSeconds = 0.6,
                WarmupTo = 0.3,
            )
        },

        Sounds = {
            "Char_UseSkill": ["audio/battle/battle_chars/hugo/hugo_roar.ogg"],
            "Char_Die":     ["audio/battle/battle_chars/hugo/hugo_death.ogg"]
        },

        FocusRectSize = (260, 570)
    )

