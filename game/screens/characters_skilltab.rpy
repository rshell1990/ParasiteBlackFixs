screen SkillTab(CharID, TabID, CharClassID = None):
######## MC & MARKUS #######################
    if CharClassID == "warrior":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "WarriorHeavySlash")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "WarriorObliteratingBlow")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "WarriorDualStrike")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "WarriorFinalBlow")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "WarriorFlailingStrikes")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "WarriorWhirlwindOfSteel")

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "WarriorDodge")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "WarriorTheDodgeMaster")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "WarriorDefensiveStance")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "WarriorWarriorStance")

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "WarriorGuardiansShield")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "WarriorLeadersCall")

##################################################################################
######## PARA BLACK (mc)
    elif CharClassID == "parasiteBlack":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteBlackRazorSlash", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteBlackVenomousStrike", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteBlackParasiteAttack", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteBlackAcidicBurst", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteBlackWindBreaker", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight(Flip = True)
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteBlackUnstoppable", AltFormSkill = True)

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteBlackTerrifyingScream", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteBlackParasiticSwarm", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteBlackPassiveAggressiveMode", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteBlackHealingWorms", AltFormSkill = True)

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ParasiteBlackPerfectOrganism", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ParasiteBlackParasiteBalance", AltFormSkill = True)

##################################################################################
######## PARA WHITE (markus) 
    elif CharClassID == "parasiteWhite":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteWhiteFireballCharge", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteWhiteParasiteCurse", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteWhiteScorchedEarth", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteWhiteCursedConnection", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteWhiteCrimsonSky", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ParasiteWhiteEternalFire", AltFormSkill = True)

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteWhiteFieryCounter", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteWhiteRegenerativeCocoon", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteWhiteInfernalParasite", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ParasiteWhiteAllForOne", AltFormSkill = True)

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ParasiteWhiteGerminatingParasites", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ParasiteWhiteProtectiveParasites", AltFormSkill = True)

################################################################################
######## ELENA
    elif CharClassID == "rogue":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RoguePiercingShot")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueFeralStrike")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()

                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueSquall")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueVenomousStrike")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueWipe")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()


        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueResilience")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueCalmStep")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueDarkening")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueForbiddenPower")
                    
        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "RogueAcrobaticManeuvers")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "RogueTeamUp")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "RogueHowlOfWar")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()

################################################################################
######## ELENA WOLF
    elif CharClassID == "rogueWolfForm":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueWolfRipNTear", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueWolfPoisonedFangs", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueWolfFeralStrikes", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueWolfRecklessBeast", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "RogueWolfSuddenStrike", AltFormSkill = True)

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueWolfDanceOfTheWolves", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueWolfFeralProtection", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueWolfLupineInstinct", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "RogueWolfHideNSeek", AltFormSkill = True)

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "RogueWolfHowl", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "RogueWolfForThePack", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "RogueWolfSnarl", AltFormSkill = True)

################################################################################
######## VES 
    elif CharClassID == "berserker":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BerserkerDeathblow")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BerserkerCrush")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BerserkerBloodForTheBloodGod")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BerserkerFrenziedState")

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BerserkerUnbreakable")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BerserkerWarCry")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BerserkerHealingWounds")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BerserkerFuriousWarCry")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BerserkerFinalSpirit")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BerserkerDeclareWar")
                    
        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BerserkerBerserkerTime")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BerserkerTheCryOfATrueWarrior")

################################################################################
######## KIARA
    elif CharClassID == "scout":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ScoutFastAndPreciseAttack")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ScoutBleedEmDry")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ScoutDanceOfDeath")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ScoutRainOfDeath")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ScoutPerfectStrike")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "ScoutTheNorthStarStrike")

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ScoutPrepare")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ScoutPreparationFromTheSkilled")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "ScoutDefensiveMode")

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ScoutKeepUp")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ScoutAttackTime")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "ScoutEaglesEye")

################################################################################
######## MYU
    elif CharClassID == "slime":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "SlimeAcidicSplash")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "SlimeCorrosiveCascade")

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "SlimeAdaptiveDefense")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "SlimeMalleableForm")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "SlimeExpandShape")

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 11
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimeSlimeRecharge")
                null height 8
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimeSoothingGel")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimeFirstAid")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown(BiggerYSize = False)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown(BiggerYSize = False)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimePrimordialUnity")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimeRegenerativeMire")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown(BiggerYSize = False)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown(BiggerYSize = False)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimeFirmingGel")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "SlimeSharingLife")

################################################################################
################################################################################
################################################################################
######## Kiara banshee
    elif CharClassID == "banshee":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BansheeASongOfPain", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BansheeShadowDive", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BansheeASongOfDeath", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BansheeTheVampiresSong", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "BansheeWingsOfDarkness", AltFormSkill = True)


        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BansheeWingShield", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "BansheeMoonlightDance", AltFormSkill = True)


        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BansheeASongOfMadness", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BansheeASongOfSacrifice", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BansheeASongOfVengeance", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BansheeASongOfRage", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "BansheeASongOfDarkBargains", AltFormSkill = True)

################################################################################
################################################################################
################################################################################
######## Erika inquisitor
    elif CharClassID == "inquisitor":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "InquisitorBurningJudgement")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "InquisitorBlindingRighteousness")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "InquisitorPurgingFire")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "InquisitorEyeForAnEye")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "InquisitorInquisition")

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "InquisitorFirewall")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "InquisitorPhoahsGlory")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "InquisitorGreatDodge")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "InquisitorNewGodsDeal")

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "InquisitorDefenderOfTheWeak")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "InquisitorAPrayerForTheDying")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "InquisitorOldGodsBargain")

################################################################################
################################################################################
################################################################################
######## sypha assassin
    elif CharClassID == "assassin":
        if TabID == "offense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "AssassinDeathByAThousandCuts")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "AssassinRecklessBackstab")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "AssassinCalculatingSwipe")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "AssassinTreacherousSlice")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offense", "AssassinCriticalBlows")

        elif TabID == "defense":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "AssassinAcrobaticDance")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "AssassinRecover")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defense", "AssassinDarkSwap")

        elif TabID == "support":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "AssassinADarkGift")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "AssassinAThousandDaggers")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "AssassinBleedingHearts")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "support", "AssassinALovingKissOfDeath")
################################################################################
######## LEARNED SKILLS (Tome Skills)
    if TabID == "learned":
        python:
            learned_skills = []
            char_obj = worldChars[CharID]
            
            # 1. Fetch permanent/tome skills
            if isinstance(char_obj, dict):
                char_skills = char_obj.get("CharSkills", {}) or {}
            else:
                char_skills = getattr(char_obj, "CharSkills", {}) or {}
            if isinstance(char_skills, dict):
                for sk in char_skills.keys():
                    if sk and str(sk).lower() not in learned_skills:
                        learned_skills.append(str(sk))
                        
            # 2. Check canonical inventory slots, plus legacy direct attributes.
            equip_slots = EQP_SLOTS.ALL + ["armor", "weapon", "accessory", "acc1", "acc2", "offhand", "head", "chest", "legs", "body"]
            for slot_name in equip_slots:
                item_val = getattr(char_obj, slot_name, None)
                if isinstance(char_obj, dict) and item_val is None:
                    item_val = char_obj.get(slot_name)
                    
                if item_val:
                    item_id = getattr(item_val, "id", getattr(item_val, "item_id", item_val))
                    if isinstance(item_id, str) and item_id in all_items:
                        item_def = all_items[item_id]
                        granted = item_def.get("grants_skill") or item_def.get("teaches_skill") or item_def.get("skill_key")
                        if granted and str(granted) not in learned_skills:
                            learned_skills.append(str(granted))

            # 3. Check nested equipment dictionaries
            eqp_container = getattr(char_obj, "equipment", getattr(char_obj, "Eqp", None))
            if isinstance(char_obj, dict) and eqp_container is None:
                eqp_container = char_obj.get("equipment") or char_obj.get("Eqp")

            if isinstance(eqp_container, dict):
                for item_val in eqp_container.values():
                    if item_val:
                        item_id = getattr(item_val, "id", getattr(item_val, "item_id", item_val))
                        if isinstance(item_id, str) and item_id in all_items:
                            item_def = all_items[item_id]
                            granted = item_def.get("grants_skill") or item_def.get("teaches_skill") or item_def.get("skill_key")
                            if granted and str(granted) not in learned_skills:
                                learned_skills.append(str(granted))

        # --- UI DISPLAY ADDITION HERE ---
        if len(learned_skills) > 0:
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                xfill True
                yfill True
                
                vpgrid:
                    cols 8
                    spacing 15
                    xalign 0.5
                    yalign 0.0
                    for skill_id in learned_skills:
                        use CharacterScreenLearnedSkillIcon(CharID, skill_id)
        else:
            text _("No learned skills available.") align (0.5, 0.5) color "#8d918e"
screen CharacterScreenSkillEmptySpace():
    null width 100
screen CharacterScreenLearnedSkillIcon(CharID, SkillID):
    $ SkillInstance = SkillLib[SkillID](Owner_PBCharID = CharID, ToLevel = 1)
    
    frame:
        xysize (100, 100)
        align (0.5, 0.5)
        background Frame(Transform("images/gui/frames/frame1.webp", matrixcolor = TintMatrix((255, 255, 255))), Borders(12,12,12,12))
        
        fixed:
            xfill True
            yfill True
            imagebutton:
                idle Transform(SkillInstance.Icon, matrixcolor = IdentityMatrix(), fit = "contain")
                hover Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.15), fit = "contain")
                hovered TooltipSetUI(Text(GetSkillDesc(SkillInstance)))
                action NullAction()

            # Optional: Display Passive / Active Tag
            add "black":
                size (90, 24)
                align (0.5, 1.0)
                fit "fill"
                matrixcolor OpacityMatrix(0.5)
            text _("Learned") size 18 xalign 0.5 text_align 0.5 yalign 1.0 color "#ffea9f"
screen CharacterScreenSkillArrowRight(Flip = False):
    frame:
        background Null()
        xsize 100
        ysize 100

        add "images/gui/unsorted/skilltree_arrow_right.webp":
            fit "contain"
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            if Flip:
                xzoom -1.0
                xoffset 20
            else:
                xoffset -20
            matrixcolor OpacityMatrix(0.85)

screen CharacterScreenSkillArrowDown(BiggerYSize = True):
    frame:
        background Null()
        xsize 100
        if BiggerYSize:
            ysize 65
        else:
            ysize 48

        add "images/gui/unsorted/skilltree_arrow_down.webp":
            size (90, 45)
            fit "contain"
            align (0.5, 0.5)
            yoffset -3
            matrixcolor OpacityMatrix(0.85)

screen CharacterScreenSkillIcon(CharID, CharClassID, SkillTabID, SkillID, AltFormSkill = False):
    $ SkillInstance = SkillLib[SkillID](Owner_PBCharID = CharID, ToLevel = GetWorldCharSkillLevel(CharID, SkillID, AltFormSkill = AltFormSkill))
    frame:
        xysize (100, 100)
        align (0.5, 0.5)
        if CharCanLevelUpSkill(CharID, CharClassID, SkillTabID, SkillID, SkillInstance, AltFormSkill):
            background Frame(Transform("images/gui/frames/frame1.webp", matrixcolor = TintMatrix((100, 255, 100))), Borders(12,12,12,12))
        else:
            if AltFormSkill:
                if worldChars[CharID]["AltForm_SkillPoints"] > 0:
                    if not CharMeetsSkillReq(CharID, CharClassID, SkillTabID, SkillID, AltFormSkill):
                        background Frame(Transform("images/gui/frames/frame1.webp", matrixcolor = TintMatrix((255, 100, 100))), Borders(12,12,12,12))
            else:
                if worldChars[CharID]["skillPoints"] > 0:
                    if not CharMeetsSkillReq(CharID, CharClassID, SkillTabID, SkillID):
                        background Frame(Transform("images/gui/frames/frame1.webp", matrixcolor = TintMatrix((255, 100, 100))), Borders(12,12,12,12))
        fixed:
            xfill True
            yfill True
            imagebutton:
                if SkillInstance.Level > 0:
                    idle Transform(SkillInstance.Icon, matrixcolor = IdentityMatrix(), fit = "contain")
                else:
                    idle Transform(SkillInstance.Icon, fit = "contain", matrixcolor = SaturationMatrix(0.0))

                hovered TooltipSetUI(Text(GetSkillDesc(SkillInstance) + 
                                GetSkillReq(CharID, CharClassID, SkillTabID, SkillID, SkillInstance, AltFormSkill = AltFormSkill)))
                if CharCanLevelUpSkill(CharID, CharClassID, SkillTabID, SkillID, SkillInstance, AltFormSkill):
                    hover Transform(SkillInstance.Icon, matrixcolor = BrightnessMatrix(0.15), fit = "contain")
                    action Function(CharAddOrRaiseSkill, CharID, SkillID, SkillInstance, CharClassID, SkillTabID, AltFormSkill = AltFormSkill)
                else:
                    action NullAction()

            if AltFormSkill:
                if SkillID in worldChars[CharID]["AltForm_CharSkills"]:
                    add "black":
                        size (90, 32)
                        align (0.5, 1.0)
                        fit "fill"
                        matrixcolor OpacityMatrix(0.5)
                    text "%s/%s" % (GetWorldCharSkillLevel(CharID, SkillID, AltFormSkill), SkillInstance.Level_Max) size 26 xalign 0.5 text_align 0.5 yalign 1.0
            else:
                if SkillID in worldChars[CharID]["CharSkills"]:
                    add "black":
                        size (90, 32)
                        align (0.5, 1.0)
                        fit "fill"
                        matrixcolor OpacityMatrix(0.5)
                    text "%s/%s" % (GetWorldCharSkillLevel(CharID, SkillID, AltFormSkill), SkillInstance.Level_Max) size 26 xalign 0.5 text_align 0.5 yalign 1.0

init python:
    def GetSkillReq(CharID, CharClassID, SkillTabID, SkillID, SkillInstance, AltFormSkill = False):
        text_strings = []

        SkillTree = Lib_BattleSkillTrees.get(CharClassID, {})
        SkillTab = SkillTree.get(SkillTabID, {})
        SkillData = SkillTab.get(SkillID, {})
        Req_Skills = SkillData.get("Reqs_SkillIDs", {})
        Req_Attributes = SkillData.get("Reqs_Attributes", {})

        if len(Req_Attributes) > 0 or len(Req_Skills) > 0:
            if CharMeetsSkillReq(CharID, CharClassID, SkillTabID, SkillID, AltFormSkill):
                text_strings.append("\n{size=+4}{color=[BATTLE_COLORS.REQ_SATISF]}" + tra(_("Requirements:")) + "{/color}{/size}")
            else:
                text_strings.append("\n{size=+4}{color=[BATTLE_COLORS.REQ_MISSING]}" + tra(_("Requirements:")) + "{/color}{/size}")

        if len(Req_Attributes) > 0:
            for AttrID, AttrVal in Req_Attributes.items():
                if worldChars[CharID][AttrID] >= AttrVal:                    
                    text_strings.append("{color=[BATTLE_COLORS.REQ_SATISF]}" + tra(GUI_STAT_NAME_MAP[AttrID]) + ": " + str(AttrVal) + "{/color}")
                else:
                    text_strings.append("{color=[BATTLE_COLORS.REQ_MISSING]}" + tra(GUI_STAT_NAME_MAP[AttrID]) + ": " + str(AttrVal) + "{/color}")

        if len(Req_Skills) is not None:
            for ReqSkillID in Req_Skills:
                RequiredSkill = SkillLib[ReqSkillID](Owner_PBCharID = CharID)
                if ReqSkillID in worldChars[CharID]["AltForm_CharSkills"] or ReqSkillID in worldChars[CharID]["CharSkills"]:
                    text_strings.append("{color=[BATTLE_COLORS.REQ_SATISF]}" + tra(RequiredSkill.DisplayName) + "{/color}")
                else:
                    text_strings.append("{color=[BATTLE_COLORS.REQ_MISSING]}" + tra(RequiredSkill.DisplayName) + "{/color}")

        return "\n".join(text_strings)

    def CharMeetsSkillReq(CharID, CharClassID, SkillTabID, SkillID, AltFormSkill = False):
        SkillTree = Lib_BattleSkillTrees.get(CharClassID, {})
        SkillTab = SkillTree.get(SkillTabID, {})
        SkillData = SkillTab.get(SkillID, {})
        Req_Skills = SkillData.get("Reqs_SkillIDs", {})
        Req_Attributes = SkillData.get("Reqs_Attributes", {})

        # "no requirements"
        if len(Req_Attributes) == 0 and len(Req_Skills) == 0:
            return True

        # attribute requirements
        if len(Req_Attributes) > 0:
            for AttrID, AttrVal in Req_Attributes.items():
                if worldChars[CharID][AttrID] < AttrVal:
                    return False

        # skill id requirements
        if len(Req_Skills) > 0:
            if AltFormSkill:
                for ReqSkillID in Req_Skills:
                    if ReqSkillID not in worldChars[CharID]["AltForm_CharSkills"]:
                        return False
            else:
                for ReqSkillID in Req_Skills:
                    if ReqSkillID not in worldChars[CharID]["CharSkills"]:
                        return False
        return True
    def TeachSkillToChar(char_id, skill_id):
        # Ensure 'CharSkills' exists as a dict
        if "CharSkills" not in worldChars[char_id]:
            worldChars[char_id]["CharSkills"] = {}

        # Add skill ID as learned (level 1)
        worldChars[char_id]["CharSkills"][skill_id] = 1

        # Fallback: keep list format if another system relies on it
        if "skills" not in worldChars[char_id]:
            worldChars[char_id]["skills"] = []
        if skill_id not in worldChars[char_id]["skills"]:
            worldChars[char_id]["skills"].append(skill_id)
    def CharCanLevelUpSkill(CharID, CharClassID, SkillTabID, SkillID, SkillInstance, AltFormSkill = False):
        if SkillInstance.Level >= SkillInstance.Level_Max:
            return False

        if AltFormSkill:
            if worldChars[CharID]["AltForm_SkillPoints"] == 0:
                return False
        else:
            if worldChars[CharID]["skillPoints"] == 0:
                return False

        if not CharMeetsSkillReq(CharID, CharClassID, SkillTabID, SkillID, AltFormSkill):
            return False

        return True

    def GetWorldCharSkillLevel(CharID, SkillID, AltFormSkill = False):
        if AltFormSkill:
            if SkillID not in worldChars[CharID]["AltForm_CharSkills"]:
                return 0
            else:
                return worldChars[CharID]["AltForm_CharSkills"][SkillID]
        else:
            if SkillID not in worldChars[CharID]["CharSkills"]:
                return 0
            else:
                return worldChars[CharID]["CharSkills"][SkillID]
        return SkillLevel