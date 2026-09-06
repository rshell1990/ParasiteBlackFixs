init python:
    @AppendToAllQuests
    class QstHighFasion(BaseQuest):
        GOALS = {
            1: QuestStage(_("The Mages Guild should help"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("A power crystal huh? I should try Mage District.")),
            2: QuestStage(_("Divine's request"), trackTag = "btn_novaras_palam_mainhall_door", hintTxt = _("Sister Divine has the power crystal, but she wants my help in return. I am to deal with some rogue mages hiding in the sub-basements of the Palam tower. Alternatively, I can just buy the crystall off her for 1500 gold.")),
            3: QuestStage(_("Bring Dros the Power Crystal"), trackTag = "btn_novaras_clothes", hintTxt = _("I have acquired the power crystal Dros wanted. I should take it to his clothes' store now."))
            }
        TITLE = _("High Fashion")
        DESCRIPTION = _("An arrogant elf running Novaras clothes shop needs a power crystal.")
        def __init__(self):
            super().__init__()
    
            self.XpReward = 550
            self.suggestedLevel = 4

        def extraDialogue(self):
            if self.progress == 1:
                yield ("divine_root", DNode(_("Ask about a power crystal for Dros"), "divine_dros_crystal", order = 100))
            if self.progress == 2:
                yield ("divine_root", DNode(_("About the power crystal..."),"divine_dros_crystal_menu", order = 100))
            if PlayerItemQty("qst_dros_power_crystal") >= 1:
                yield ("dros_root", DNode(_("I got the crystal you asked for."), "dros_givecrystal", order = 100))

        def onComplete(self):
            QstStart(DrosInBordello)
            QstStart(EventBrothelAd)
            if QstIsOver(QstTwoEmperors):
                QstStart(PrimerBeneathTheShadows)
            return

label divine_dros_crystal:
    DIVINE 'Oh... {i}That elf.{/i}'
    MC @talk 'Could you help me out at all?'
    DIVINE 'Hmm... As I explained to him, even if we COULD sell him one, power crystals such as these are not the easiest things to come by...'
    DIVINE '{i}Or the cheapest.{/i}'
    MC @talk 'There must be something I can do...'
    DIVINE '... Well, we are having a small crisis at the moment in the Sub-Basement.'
    MC @talk '... Crisis?'
    DIVINE 'Sister Gracen took it upon herself to fool around with a couple of conjurors in the Sub-Basement.'
    DIVINE 'Apparently, they were merely trying to see if they could conjure up some form of light spirit.'
    MC @talk '... They didn’t conjure up a ‘light spirit’, I take it?'
    DIVINE '{i}No... No, they did not.{/i}'
    DIVINE 'We’ve sealed off the Sub-Basement until the Inquisitors can arrive to deal with the matter but...'
    DIVINE 'If {i}you{/i} can sort it out somehow and we were able to avoid an investigation, I would be eternally grateful.'
    MC @talk 'Uhh... I’m just a human though.'
    show divine happy
    'Sister Divine curiously smiled at the comment.'
    DIVINE '... Of course you are.'
    MC '(... Does she suspect something about me?)'
    show divine
    BLACK '(Her heart rate has remained at a steady rate this whole time... She is totally calm.)'
    DIVINE 'Or... We could skip the pleasantries.'
    DIVINE 'You can have the crystal for 1500 gold.'
    $ QstSetProgress(QstHighFasion, 2)

label divine_dros_crystal_menu:
    DIVINE 'Your call, warrior.'
    menu:
        'I’d rather just pay for the crystal.' (Req_Gold = 1500):
            $ PlayerRemItem("gold", 1500)
            DIVINE  '... Hm... Disappointing but...'
            DIVINE 'Very well, here is the crystal you seek...'
            $ PlayerAddItem("qst_dros_power_crystal")
            DIVINE '{i}*Sigh*{/i} Now to wait for the Inquisitors to arrive, I suppose.'
            DIVINE 'What a bloody mess.'
            $ QstSetProgress(QstHighFasion, 3)
            return
        'I’ll help you deal with the conjurers.':
            DIVINE 'Wonderful!'
            DIVINE 'I’ll lead you to the entrance to the Sub-Basement.'
            scene black with dissolve
            jump palam_sewer
        'I’ll decide later.':
            DIVINE 'Don’t take too long... Every moment you wait, the more likely it becomes that the Inquisitors will arrive and start asking impertinent questions.'
            return

label dros_givecrystal:
    DROS @talk 'Did you bring the crystal?'
    MC @talk'Yep, here it is.'
    DROS @talk 'Give it to me!'
    
    $ PlayerRemItem("qst_dros_power_crystal")
    
    MC @talk 'Whoa, whoa, remember your end of the deal?'
    DROS @talk 'Urgh, fine!'
    DROS @talk 'Here, your gold...'
    $ PlayerAddItem("gold", 400)
    $ QstComplete(QstHighFasion)
    $ CharChangeRel("dros", 1)
    $ DialogueDros().shopWorks = True
    scene black with dissolve
    $ Pause(0.1)
    'Taking the crystal, Dros Ulvrak slotted it into some strange contraption.'
    play sound "audio/cfx/dros_power_up.ogg"
    $ wLocs["novaras_clothes_int"].dn_ambience.dayTrack = "audio/cfx/dros_machine_loop.ogg"
    $ wLocs["novaras_clothes_int"].dn_ambience.nightTrack = "audio/cfx/dros_machine_loop.ogg"
    $ soundUpdate()
    'I watched dumfounded as the whole shop abruptly came to life.'
    'The strange machines were no longer motionless, coming alive, they began to work in synchronized automated unison as they stitched away at fancy fabrics on the workshop bench.'
    $ LocFlush(dissolve)
    DROS @smile 'Perfect!'
    DROS @talk 'Time to work some beauty into this city!'
    $ LocEnter()
