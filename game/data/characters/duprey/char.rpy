default DUPREY = Character(_("Captain Duprey"), image = "duprey")
init python:
    CharDefs["duprey"] = BuildCharTemplate(CharID = "duprey",
        BattleSkin =  "skin_duprey", 

        
        base_health = 150,

        Strength = 30,
        Endurance = 25,
        Willpower = 15,
        Agility = 12,
        Dexterity = 10,

        CharSkills = {"WarriorDualStrike":1, "WarriorDefensiveStance":1, "WarriorLeadersCall":1},

        RelTextIDs = {"initial"},

        experience = ExpSetToLevel(22),
        name = _("Captain Duprey"),
        portrait = "images/characters/duprey/portrait.webp",
        ExtraData = {"axe":False})

    config.tag_layer["duprey"] = "characters"

    RelText["duprey"] = {}
    RelText["duprey"]["initial"] = {
        "order":0,
        "text":_("One of the captains of the scouts’ divisions. A skilled, highly decorated warrior, loved by his men.")}
    RelText["duprey"]["prol_killed"] = {
        "order":1,
        "text":_("He was killed by no other than Zanarak himself during the battle at the abandoned fort.")}
