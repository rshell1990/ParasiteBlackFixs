label qst_BigTroubleLHamun_intro:
    $ QstComplete(PrimerBigTroubleLH)
    show marbella at left

    show cg_gtc_goon at center_f
    show cg_gtc_goon2 at cright_f
    with dissolve
    MARBELLA @angry "The answer's bloody no!"
    GTC_GOON "You really think you're in a position to refuse the Greater Trading Company?"
    GTC_GOON_2 "It's a good offer, Marbella."
    GTC_GOON_2 "You should accept it."
    MARBELLA @angry "I don't care how many {i}contracts{/i} they offer me, I ain't getting into bed with the Greater Trading Company!"
    show mc at right_f with easeinright
    "As Marbella looks past the goons toward me, they turn to look."
    MC @serious "Is there a problem here?"
    show cg_gtc_goon at blurin, center
    $ Pause(0.1)
    show cg_gtc_goon2 at blurin, cright
    GTC_GOON "No problem."
    GTC_GOON "We're just here to explain to Marbella why she should seriously reconsider the GTC's offer."
    hide cg_gtc_goon2 with easeoutright
    GTC_GOON_2 "If you care about your lady friend here... I'd suggest talking her into signing it."
    hide cg_gtc_goon with easeoutright
    "One signals to the other as the two of them make their way toward the door."
    show marbella at cleft with ease
    show mc at cright_f with ease
    # GTC Goons exit off-screen
    MARBELLA @sad "Fuck..."
    MC @think "What in the hells was that?"
    MARBELLA @angry "Those Greater Trading Company bastards!"
    MARBELLA @sad "The last thing they want is competition, so they're doing what they can to either buy me out or shut us down."
    $ tmpvar = ["a", "b"]
    menu qst_BigTroubleLHamun_intro_menu:
        "What deal are they offering you?" if "a" in tmpvar:
            $ tmpvar.remove("a")
            MARBELLA @angry "Some fucking deal!"
            MARBELLA @angry "They're offering me {i}protection{/i} and additional access to a few lesser mines in return for forty percent of my profits!"
            MARBELLA @angry "It'll bloody kill us!"
            MC @serious "{i}Protection,{/i} huh."
            MARBELLA @angry "Aye, protecting us from themselves burning this place to the fuckin' ground!"
            jump qst_BigTroubleLHamun_intro_menu
        "How long has this been going on?" if "b" in tmpvar:
            $ tmpvar.remove("b")
            MARBELLA @sad "Ever since we started expanding."
            MARBELLA @sad "Once you've caught the eye of the GTC, getting the fuckers to stay away is the hardest part."
            MARBELLA @angry "They do whatever they can to get rid of the competition and protect their {i}assets.{/i}"
            jump qst_BigTroubleLHamun_intro_menu
        "What are you gonna do?":
            pass
    $ tmpvar = {}
    MARBELLA @sad "I don't know..."
    MARBELLA @sad "If I take the contract, I'm screwed."
    MARBELLA @sad "If I don't, they'll find another way to screw me."
    MARBELLA @angry "Bastards like these only stop when they can't push you around anymore."
    "Marbella sighs."
    MARBELLA @sad "S-Shit..."
    MARBELLA @sad "I'm sorry, I really shouldn't be piling all this onto you."
    MARBELLA @sad "I'll figure something out."
    MARBELLA @sad "{i}Somehow.{/i}"
    MARBELLA @think "Anyway, {i}don't you have bigger things to think about right now than worrying about me?{/i}"
    MC @think "What do you mean?"
    MARBELLA @shock "You're the talk of the whole city!"
    MARBELLA @shock "They got posters drew up of you and... whatever it is you turned into at the arena everywhere!"
    MC @serious "Joy... Just what I need, {i}more{/i} people asking questions."
    MARBELLA @smile "Oh, come on."
    MARBELLA @smile "I mean, half the city thinks you're a hero!"
    MC @think "And the other half?"
    MARBELLA @think "Umm... Maybe they're thinking about whether you're going to eat them or not."
    MC @sad "{i}*Sigh*{/i}"
    MARBELLA @talk "{i}... Can I see it?{/i}"
    MC @think "What?"
    MARBELLA @smile2 "Yer monster form!"
    MARBELLA @talk "Whatever it is you turn into, come on, I've only heard the stories!"
    MARBELLA @think "... Do you really grow two heads?"
    MC @think "I... No."
    MARBELLA @sad "Oh come on, please show me?"
    MARBELLA @sad "{i}Please, please, please?{/i}"
    MC @serious "Alright, alright!"
    MARBELLA @smile "Great! How does it work, do you just-"
    $ PlaySound("audio/cfx/transform.ogg")
    hide mc
    show mc_transformed at cright_f 
    with flash
    MARBELLA @shock "HOLY FUCK!"
    MARBELLA @scared "Gods, no one wonder people are going crazy."
    MC "Satisfied?"
    MARBELLA @talk "I... I think so!"
    MARBELLA @scared "... You're not actually going to eat people, right?"
    MC "No."
    MC "I do not intend to eat people."
    MARBELLA @think "Then, uhh... What exactly {i}do{/i} you do."
    MC "I..."
    MC "{i}Need to mate.{/i}"
    MARBELLA @think "You need to..."
    MARBELLA @shock "You need to shag?!"
    MC "Yes."
    MARBELLA @think "Or what?"
    MC "{i}Or I die.{/i}"
    MARBELLA @shock "..."
    MARBELLA @laugh "HAHAHAHAAH!"
    MC "It's not funny!"
    MARBELLA @laugh2 "{i}Mi'lady please, if I don't shove ma prick in ya, it's all over!{/i}"
    MC "Ha-Ha..."
    MARBELLA @smile "Oh lighten up, even you've gotta see the funny side a bit."
    MARBELLA @smile2 "{i}You're the envy of horny teenage boys everywhere.{/i}"
    MC "Great... Satisfied?"
    MARBELLA @smile "yes."
    hide mc_transformed 
    show mc at cright_f
    $ PlaySound("audio/cfx/transform.ogg")
    with flash
    MARBELLA @talk "Anyway, thanks for the distraction, I really needed that."
    MARBELLA @sad "I'm gonna close up shop for tonight and speak to some of the boys... see what they think."
    MARBELLA @sad "Come back tomorrow, alright?"
    MC @talk "Very well."
    scene black with dissolve
    $ LocSet("hamun_dist_docks")
    $ QstBigTroubleLH().LockedDownForToday_First = True
    $ LocFlush()
    with dissolve
    show mc at cleft with easeinleft
    MC @think "(Hmm... There must be some kind of way to help Marbella out.)"
    MC @think "(As long as she has some kind of protection, the Greater Trading Company won't try anything.)"
    MC @serious "(My best bet might be to approach one of the Merchant Lords and see if they'll take Marbella under their protection.)"
    MC @serious "(There may be another way... but Lord Zanzibat is probably my best bet for now.)"
    hide mc with dissolve
    $ QstStart(QstBigTroubleLH)
    $ GoalShow(QstBigTroubleLH, 0)
    $ LocEnter()

label qst_BigTroubleLHamun_zanzibat_doors:
    if IsDaytime():
        MC "(As I approached, the guards let me through.)"
        scene black with dissolve
        $ LocSet("hamun_zanzibat_house")
        $ LocEnter()
    else:
        MC "(I should come by during the day.)"
        $ LocEnterQ()

label qst_BigTroubleLHamun_talk_to_zanzibat:
    ZANZIBAT @talk "What is it?"
    menu:
        "Marbella, the owner of the Crooked Shaft Mining Co., is in need of protection.":
            ZANZIBAT @think "Hmm?"
            ZANZIBAT @talk "I can't say the name is a familiar one to me."
            ZANZIBAT @talk "But I did hear some grumblings about a new mining company that's rattled the GTC."
            ZANZIBAT @smile "Suffice to say, I'm interested."
            MC @think "What do you want in return?"
            ZANZIBAT @talk "If I had to guess, they're asking for thirty-five percent of the profits in return for their... {i}protection.{/i}"
            MC @talk "{i}Forty percent.{/i}"
            ZANZIBAT @smile "Oh dear, they {i}are{/i} irritated."
            ZANZIBAT @smile "Here is my offer."
            ZANZIBAT @smile "Twenty percent of the profits, and I'll supply my own security to ensure that the Crooked Shaft is protected."
            ZANZIBAT @talk "And... {i}I want a favor from you.{/i}"
            MC "(Here we go...)"
            MC @talk "What do you want?"
            ZANZIBAT @talk "Have you heard of the Khazah?"
            ZANZIBAT @talk "They're a growing player in Novaras, alongside other gangs in the city."
            MC @think "What of them?"
            ZANZIBAT @think "Well, it seems they are no longer content to reside within their little underground fiefdom,"
            ZANZIBAT @angry "and are trying to branch out into new territories..."
            ZANZIBAT @angry "{i}Including mine.{/i}"
            MC @think "So, you want me to {i}persuade{/i} them to leave?"
            ZANZIBAT @talk "No."
            ZANZIBAT @angry "I want you to kill them all, and place their severed heads around the great fountain."
            MC @surprised "That's..."
            ZANZIBAT @smile "Extreme?"
            MC @serious "{i}Macabre.{/i}"
            ZANZIBAT @talk "I intend to send a message."
            ZANZIBAT @talk "One that will remind those small fish to stay in their pond."
            MC @talk "I will need to speak to Marbella first before I agree to anything."
            $ GoalComplete(QstBigTroubleLH, 0)
            ZANZIBAT @talk "Very well. Come back and let me know if we have a deal."
            $ LocSet("hamun_dist_merch_lord")
            scene black with dissolve
            $ LocFlush()
            show mc at center
            with dissolve
            MC @serious "(Hmm... Perhaps before returning to Marbella, I should look at all my options?)"
            show mc at blurin, center_f
            MC @serious "(There must be someone else who could help.)"
            $ QstBigTroubleLH().DoAmbush = True
            $ QstStart(HouseLockHamunKhazahHideout)
            $ GoalShow(QstBigTroubleLH, 1)
        "Never mind, actually.":
            ZANZIBAT @angry "Enough with wasting my time."
            return
    $ LocEnter()

################ ambush on returning to marbella
label qst_BigTroubleLHamun_miningco_ambush:
    $ QstBigTroubleLH().DoAmbush = False
    $ QstBigTroubleLH().DoPostAmbushScene = True
    MC "(Hm. Strange.)"
    MC "(No answer.)"

    if IsDaytime():
        scene cg_gas_bomb_day with dissolve

    else:
        scene cg_gas_bomb_night with dissolve

    "Suddenly, something rolled between my feet,"
    $ PlaySound("audio/cfx/poison_gas.ogg")
    "a small ball that screamed as it released a red gas!"
    SYPHA @shock "MOVE NOW!"
    menu:
        "Kick it away!" (Req_Dex = 15):
            "With a sharp boot, I sent the ball spinning into the air away from us."
            $ PlaySound("audio/cfx/poison_gas.ogg")
            $ LocFlush(dissolve)
            "As it crashed onto the sand, the red gas slowly filled up the area where it landed before disipating into nothing."
            GTC_GOON "Well, that's a shame."
            show cg_gtc_goon2 at cleft with dissolve
            show cg_gtc_goon at cright_f with dissolve
            "My eyes turned towards the masked servants of the GTC approaching."
            MC @angry "Give me one reason not to just kill you where you stand right now."
            GTC_GOON "We've been watching you these past few days..."
            GTC_GOON "I've been sent to deliver a message from the GTC."
            GTC_GOON "{i}Stay out of our business.{/i}"
            "I reach for my blade, ready to cut them down."
            "But rolling down another ball between his feet, a smoke cloud appeared engulfiing them."
            hide cg_gtc_goon
            hide cg_gtc_goon2
            with dissolve
            "When the smoke cleared, they were gone."
            MC @angry "Fucking GTC dogs..."
            $ LocEnterQ()
        "Try to move away!":
            MC @scared "FUCK!"
            $ PlaySound("audio/cfx/poison_gas.ogg")
            "I tried to move quickly, but as I breathed in the gas, I suddenly felt dizzy."
            scene black with dissolve
            "The world turned dark as my limbs grew heavy."
            play sound "audio/cfx/body_fall_ground.ogg"
            "Then, as my eyes closed and refused to open, I felt a thud as I collapsed onto the desert sands."
            scene black with flash
            $ PlayerRemItem("gold", round(PlayerItemQty("gold") * 0.5), Silent = True, MuteSfx = True)
            $ DamagePlayer(CharGetVar("mc", "Health") * 0.5)
            $ LocSet("hamun_gates")
            $ LocFlush(dissolve)
            show mc at blurin, center_f
            "Groggily, I awoke and rose to my feet."
            "Looking around through the haze, I realized I had been dropped outside the city walls."
            "My companion lay next to me as I shook them awake."
            show markus at left with easeinleft
            MARKUS @angry "Urghh...!"
            MARKUS @sad "I feel like death."
            "A hastily scrawled letter was left pinned beneath a rock."
            "{i}Stay out of the GTC's business.{/i}"
            MC @angry "Bastards...!"
            hide markus with easeoutleft
            if CharInParty("ves"):
                show ves at left with easeinleft
                VES @angry "Typical of cowardly GTC dogs."
                hide ves with easeoutleft
            show sypha at right_f with easeinright
            SYPHA @sad "Are you alright?"
            "Sypha approached, handing me some water."
            MC @talk "I feel like death."
            MC @talk "... What happened?"
            SYPHA @talk "I managed to leap out of the way and avoid the main blast."
            SYPHA @talk "Limped my way to the inn before collapsing from the fumes."
            SYPHA @talk "When I woke up, I came back to find you all."
            MC @think "You ran?"
            SYPHA @angry "I figured you were about to get kidnapped."
            SYPHA @talk "{i}Someone{/i} was going to need to rescue you all."
            SYPHA @talk "Looks like we got lucky, though... The GTC were just sending a message this time."
            hide sypha with easeoutright
            show markus at left with easeinleft
            MARKUS @angry "Doesn't feel very fucking lucky to me."
            show kiara at right_f with easeinright
            KIARA @sad "Ow ow ow!"
            KIARA @sad "My head is throbbing!"
            MC @serious "I need to speak to Marbella as soon as I can."
            "Looking down as I checked my person, I realized a few of my things were missing..."
            $ LocEnter()
    

################################################################################################
label qst_BigTroubleLHamun_return_to_marbella_after_ambush:
    $ QstBigTroubleLH().DoPostAmbushScene = False
    show mc at cright_f with easeinright
    show marbella at cleft with easeinleft
    MC @surprised "Marbella!"
    MARBELLA @shock "H-Huh?"
    MARBELLA @shock "Is something the matter, love?"
    MC @talk "We need to talk. The GTC threatened me."
    MARBELLA @shock "WHAT?!"
    MC @talk "I went to speak to Lord Zanzibat on your behalf..."
    MC @talk "The GTC didn't take too kindly to that, it seems."
    MARBELLA @angry "Damn it, man!"
    MARBELLA @sad "This is why I said to leave it to me to sort!"
    MC "..."
    MARBELLA @sad "{i}*Sigh*{/i}"
    "Marbella rubbed at her brow in frustration."
    MARBELLA @sad "... What in the hells am I to do?"
    MC @think "(Hmm... Now might be my last chance to see what other offers are out there.)"
    jump qst_BigTroubleLHamun_return_to_marbella_options


# entry point for repeat
label qst_BigTroubleLHamun_marbella_repeat_menu:
    "Marbella rubbed at her brow in frustration."
    MARBELLA @sad "Oh... Have you figured something out?"
    # All choices include: 
    # zanzibat deal (nope)
    # khazah route makes her public whore
    # buy golem
    menu qst_BigTroubleLHamun_return_to_marbella_options:
        "Lord Zanzibat is willing to make a deal.":
            # in its own love file
            jump qst_BigTroubleLHamun_marbella_love_offer
        ##########################################################################
        # The player must have spoken to the Khazah to have this option available
        "The Khazah are willing to lend you their muscle." (AppearIf = (QstBigTroubleLH().TalkedToKhazahOffer == True)):
            # in its own khazah file
            jump qst_BigTroubleLHamun_marbella_khazah_offer
        ###################################################################################
        #The player must have spoken to Beshar about the golem to have this option available
        "I can buy you a golem, for security." (AppearIf = (QstBigTroubleLH().TalkedToGolemOffer == True)):
            # in its own "golem" file
            jump qst_BigTroubleLHamun_marbella_golem_offer
        "There may be another way... Give me more time.":
            MARBELLA @sad "Alright... I trust you."
            $ LocEnter()


#################################################################
label qst_BigTroubleLHamun_marbella_closed:
    MC "(She said she'll be closing down shop for a day.)"
    MC "(I should come by later.)"
    $ LocEnterQ()
