screen SkillTab(CharID, TabID, CharClassID = None):
############################################
############################################
######## MC & MARKUS #######################
    if CharClassID == "warrior":
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "WarriorHeavySlash")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "WarriorObliteratingBlow")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "WarriorDualStrike")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "WarriorFinalBlow")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "WarriorFlailingStrikes")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "WarriorWhirlwindOfSteel")

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "WarriorDodge")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "WarriorTheDodgeMaster")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "WarriorDefensiveStance")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "WarriorWarriorStance")

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteBlackRazorSlash", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteBlackVenomousStrike", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteBlackParasiteAttack", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteBlackAcidicBurst", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteBlackWindBreaker", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight(Flip = True)
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteBlackUnstoppable", AltFormSkill = True)

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteBlackTerrifyingScream", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteBlackParasiticSwarm", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteBlackPassiveAggressiveMode", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteBlackHealingWorms", AltFormSkill = True)

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteWhiteFireballCharge", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteWhiteParasiteCurse", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteWhiteScorchedEarth", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteWhiteCursedConnection", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteWhiteCrimsonSky", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ParasiteWhiteEternalFire", AltFormSkill = True)

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteWhiteFieryCounter", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteWhiteRegenerativeCocoon", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteWhiteInfernalParasite", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ParasiteWhiteAllForOne", AltFormSkill = True)

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RoguePiercingShot")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueFeralStrike")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()

                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueSquall")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueVenomousStrike")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueWipe")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()


        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueResilience")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueCalmStep")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueDarkening")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueForbiddenPower")
                    
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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueWolfRipNTear", AltFormSkill = True)
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueWolfPoisonedFangs", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueWolfFeralStrikes", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueWolfRecklessBeast", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "RogueWolfSuddenStrike", AltFormSkill = True)

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueWolfDanceOfTheWolves", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueWolfFeralProtection", AltFormSkill = True)
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueWolfLupineInstinct", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "RogueWolfHideNSeek", AltFormSkill = True)

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BerserkerDeathblow")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BerserkerCrush")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BerserkerBloodForTheBloodGod")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BerserkerFrenziedState")

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BerserkerUnbreakable")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BerserkerWarCry")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BerserkerHealingWounds")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BerserkerFuriousWarCry")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillArrowDown()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BerserkerFinalSpirit")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BerserkerDeclareWar")
                    
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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ScoutFastAndPreciseAttack")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ScoutBleedEmDry")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ScoutDanceOfDeath")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ScoutRainOfDeath")
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillArrowDown()
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillEmptySpace()
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ScoutPerfectStrike")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "ScoutTheNorthStarStrike")

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ScoutPrepare")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ScoutPreparationFromTheSkilled")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "ScoutDefensiveMode")

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "SlimeAcidicSplash")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "SlimeCorrosiveCascade")

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "SlimeAdaptiveDefense")
                    use CharacterScreenSkillArrowRight()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "SlimeMalleableForm")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "SlimeExpandShape")

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BansheeASongOfPain", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BansheeShadowDive", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BansheeASongOfDeath", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BansheeTheVampiresSong", AltFormSkill = True)
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "BansheeWingsOfDarkness", AltFormSkill = True)


        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BansheeWingShield", AltFormSkill = True)
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "BansheeMoonlightDance", AltFormSkill = True)


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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "InquisitorBurningJudgement")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "InquisitorBlindingRighteousness")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "InquisitorPurgingFire")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "InquisitorEyeForAnEye")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "InquisitorInquisition")

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "InquisitorFirewall")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "InquisitorPhoahsGlory")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "InquisitorGreatDodge")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "InquisitorNewGodsDeal")

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
        if TabID == "offence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "AssassinDeathByAThousandCuts")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "AssassinRecklessBackstab")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "AssassinCalculatingSwipe")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "AssassinTreacherousSlice")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "offence", "AssassinCriticalBlows")

        elif TabID == "defence":
            vbox:
                align (0.5, 0.0)
                xfill True
                null height 20
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "AssassinAcrobaticDance")
                    use CharacterScreenSkillEmptySpace()
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "AssassinRecover")
                null height 40
                hbox:
                    xalign 0.5
                    use CharacterScreenSkillIcon(CharID, CharClassID, "defence", "AssassinDarkSwap")

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

screen CharacterScreenSkillEmptySpace():
    null width 100

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

        Req_Skills = Lib_BattleSkillTrees[CharClassID][SkillTabID][SkillID].get("Reqs_SkillIDs", {})
        Req_Attributes = Lib_BattleSkillTrees[CharClassID][SkillTabID][SkillID].get("Reqs_Attributes", {})

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
        Req_Skills = Lib_BattleSkillTrees[CharClassID][SkillTabID][SkillID].get("Reqs_SkillIDs", {})
        Req_Attributes = Lib_BattleSkillTrees[CharClassID][SkillTabID][SkillID].get("Reqs_Attributes", {})

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