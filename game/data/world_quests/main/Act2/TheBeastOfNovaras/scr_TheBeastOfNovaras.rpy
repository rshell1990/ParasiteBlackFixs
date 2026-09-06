label qst_TheBeastOfNovaras_IntroWakeUp:
    show kiara at cright_f
    show markus at right_f
    with dissolve
    show mc at left with easeinleft
    "Downstairs, Kiara and the others were gathered around one of the tables with a couple of half-eaten plates of breakfast."
    "Cooked sausages, eggs, and bacon sweetly scented the air as they drank from their ale cups."
    KIARA @smile "Morning, love."
    KIARA @talk "I tried waking you, but you seemed pretty out of it."
    jump qst_TheBeastOfNovaras_BarSceneShared

label qst_TheBeastOfNovaras_IntroWalkIn:
    show kiara at cright_f
    show markus at right_f
    with dissolve
    show mc at left with easeinleft
    "Kiara and others were gathered around one of the tables, eating."
    "Cooked sausages, eggs, and bacon sweetly scented the air as they drank from their ale cups."
    KIARA @smile "Hey there, love."
    jump qst_TheBeastOfNovaras_BarSceneShared


label qst_TheBeastOfNovaras_BarSceneShared:
    MARKUS @smile "Mm, you should try the food here, [player_name!t]."
    MARKUS @smile "The sausages, they stuff them with... {i}something.{/i}"
    MARKUS @smile "Tasty, though!"
    if CharInParty("ves"):
        show ves at center with dissolve
        VES @talk "Not enough salt..."
        MARKUS @think "Do you intend to complain all day?"
        VES @angry "I do not just complain!"
        VES @think "... My people simply use much more salt."
        VES @smile "Food can be scarce in Skarshire."
        VES @smile "Salt preserves the meat longer."
        MARKUS @talk "It wouldn't be so scarce if your people actually traded instead of raiding everyone."
        VES @angry "We'll have time to {i}trade{/i} as much as we like once we're free, human."
        KIARA @smile "Gods, Markus... I never knew you were so skilled at making new friends!"
        MARKUS @angry "As if I could be friends with an orc!"
        VES @angry "The feeling is mutual."
        MC @talk "Enough squabbling."
        MC @talk "We have enough battles ahead without turning on each other in the meantime."
        pass
    "Kiara took a sip from her ale."
    MC @talk "... Well, where is this mistress of yours?"
    KIARA @talk "Feeling impatient, love?"
    KIARA @talk "Why don't you grab yourself some food?"
    MARKUS @smile "I agree, you should learn to relax a little, [player_name!t]."
    show rania at cleft with easeinleft
    show rania at nod
    "As Rania set down an ale for me and Markus, his eyes wandered over her backside as she left, smirking."
    hide rania with easeoutright
    MARKUS @smile "There's certainly plenty of... {i}talent{/i} around here."
    if CharInParty("ves"):
        VES @angry "Pig."
        MARKUS @angry "Don't worry, I'm certain men will spare you their gaze."
        VES @angry "Tsch!"
        if CharIsLover("ves"):
            menu:
                "I don't know... I could certainly enjoy gazing at her for a few hours.":
                    VES @blush "..."
                    MARKUS @shock "Oh gods... I think I might be sick."
                    VES @angry "Be silent for once!"
                "Would you both knock it off?":
                    MARKUS @angry "..."
                    VES @angry "..."
                    MARKUS @angry "{i}She started it.{/i}"
        else:
            MC @talk "Would you both knock it off?"
            MARKUS @angry "..."
            VES @angry "..."
            MARKUS @angry "{i}She started it.{/i}"
        hide ves with dissolve

    show mc at cleft with ease
    
    SYPHA @happy "Ahh...!"
    show sypha at left with easeinleft
    "Fingers, cool and soft, brushed my shoulder."
    "I stiffened, hand half-reaching for my blade before I turned."
    show mc at blurin, cleft_f
    "Sypha's smile greeted me instead, too warm to trust and too sharp to ignore."
    SYPHA @happy "Apologies for the delay."
    SYPHA @happy "I do enjoy making an entrance."
    "Every gaze in the room snapped toward her."
    "The Demorai woman stood as though she owned the air itself, her confidence a blade sharper than anything on my hip."
    "My chest tightened: instinct screamed to cut her down, but her grip on my shoulder pressed just enough to still me."
    "A warning, and a promise."
    show sypha at center with ease
    show mc at blurin, cleft
    KIARA @smile "Mistress Sypha! I did as you asked! I prepared your room and~"
    show sypha at nod
    "Sypha lifted her hand, brushing over Kiara's hair with casual intimacy."
    "Kiara flushed red, as though branded by the touch."
    MARKUS @angry "..."
    SYPHA @talk "... Is there a problem, soldier?"
    show markus at shake
    MARKUS @angry "Not yet. Still deciding if I'm meant to follow orders... or gut a snake before it coils too tight."
    hide kiara with dissolve
    show sypha at cright with ease
    SYPHA @laugh "Oh, delightful! A tongue as sharp as a sword."
    SYPHA @laugh "Amusing, really. HILARIOUS even!"
    SYPHA @happy "But be careful, jokes can get men killed. Try me, and I'll see your head displayed on a pike before dusk."
    MARKUS @angry "That a threat?"
    SYPHA @happy "No. A certainty you haven't earned yet."
    show mc at blurin, cleft_f
    show mc at left_f with ease
    "I glanced around the tavern and saw no alarm nor heard no whispers."
    "To them, Sypha was nothing more than another foreigner, perhaps a dark elf in fine dress."
    "Only those who had glimpsed true Demorai horrors could see the shadow beneath her smile."
    show mc at blurin, left
    show garen at center with dissolve
    "Beside her loomed a silent man in gold-trimmed robes, a sigil of quilt and coin stitched at his shoulder."
    "His silence spoke of power born from ink, not steel."
    if CharInParty("ves"):
        show ves at cleft with dissolve
        VES @talk "..."
        show sypha at blurin, cright_f
        SYPHA @happy "I don't believe we've formally met!"
        VES @talk "Ves."
        SYPHA @happy "Sypha."
        VES @think "You don't look like the other Demorai I've seen before..."
        SYPHA @happy "Ahh..."
        SYPHA @talk "My people are... complicated."
        hide ves with dissolve
    show mc at shake
    MC @serious "Why are we here?"
    MC @think "What do you want from us?"
    SYPHA @happy "Is that any way to speak to me, {i}husband?{/i}"
    MC @surprised "... Wait, what?"
    SYPHA @talk "Now now, things will be explained in time."
    SYPHA @talk "Let's just say your Emperor and my Order's goals align for now."
    MC @think "{i}Your{/i} Order?"
    SYPHA @happy "The Order of Xeriya."
    SYPHA @talk "But enough talk."
    SYPHA @talk "My {i}associate{/i} here will share the rest of the details."
    hide sypha with dissolve
    show garen at blurin, center_f
    "The man stepped forward with the calm of a banker opening a ledger, his voice silk over steel."
    GAREN @talk "In ink and honor, I greet you."
    GAREN @talk "Garen Quiltshire of the Greater Trading Company, at your service, whether you welcome it or not."
    MARKUS @angry "Greater Trading Company?"
    show garen at blurin, center
    MARKUS @angry "Thought Alderay cast your kind out after you starved villages with your 'disputes.'"
    GAREN @smile "Ancient history."
    GAREN @smile "Petty squabbles over fish and pride."
    GAREN @smile "Hardly worth remembering, unless you're the sort who nurses grudges instead of coin purses."
    MARKUS @angry "Tell that to the graves you left behind."
    GAREN @smile "Graves do not pay. But war does."
    show garen at blurin, center_f
    GAREN @smile "And this war has opened doors we intend to walk through, with or without your blessing."
    MC @serious "What do you want from us, Garen Quiltshire?"
    GAREN @talk "Want? Oh, nothing so crude."
    GAREN @talk "Consider me... an arranger."
    GAREN @talk "Emperor Alcott seeks weapons, Alderay seeks food, and mercenary steel greases the wheels."
    GAREN @talk "All perfectly tidy, all perfectly profitable."
    if CharInParty("ves"):
        show ves at cleft with dissolve
        VES @angry "Profitable for you, and slaughter for my people."
        GAREN @talk "The world bleeds regardless of your feelings, orc."
        GAREN @talk "My quill simply chooses where the ink dries."
        "His eyes lingered on Ves, narrowing with a distaste he didn't bother to hide before pulling away."
        hide ves with dissolve
    show garen at blurin, center
    "Garen's eyes now slid back towards Markus, gleaming with something sharper than disdain:"
    "Knowledge."
    GAREN @smile "Of course, there is the matter of {i}insurances{/i} we've taken to make sure you all understand this request is... {i}non-optional.{/i}"
    MARKUS @angry "What in the hells does that mean?"
    GAREN @smile "You do have an older brother, don't you, Markus?"
    GAREN @smile "Fine lad, working the mines."
    GAREN @smile "With a single letter, I could see him promoted!"
    GAREN @smile "... Or buried beneath a cave-in."
    show markus at shake
    MARKUS @shock "You bastard!"
    GAREN @smile "Now now."
    GAREN @smile "Why rage, when you could simply... cooperate?"
    GAREN @smile "Think of it as an investment."
    GAREN @smile "His life for your obedience."
    show garen at blurin, center_f
    GAREN @smile "A fair contract, wouldn't you say?"
    $ tmpvar = ["bus"]
    if CharInParty("ves"):
        $ tmpvar.append("orc_comp")
    label qst_TheBeastOfNovaras_BarSceneShared_garenmenu:
    if len(tmpvar) > 0:
        menu:
            "What business does the Greater Trading Company have in Alderay? Weren't you cast out?" if "bus" in tmpvar:
                $ tmpvar.remove("bus")
                GAREN @talk "Over a minor disagreement many years ago over some fishing disputes."
                GAREN @talk "{i}Petty stuff.{/i}"
                MARKUS @angry "I seem to recall a lot of villages starving over that {i}petty dispute.{/i}"
                GAREN @talk "Ancient history, nothing more."
                GAREN @talk "Besides, the war has changed everything now."
                GAREN @talk "While relations aren't fully formalized, we are poised to make a very important deal with you Alderians."
                MARKUS @angry "We'd be better off striking a bargain with a demon."
                GAREN @talk "I highly doubt that."
                MARKUS @angry "Tsch!"
                jump qst_TheBeastOfNovaras_BarSceneShared_garenmenu
            "I have an orc companion... {i}Is this going to be a problem?{/i}" if "orc_comp" in tmpvar:
                $ tmpvar.remove("orc_comp")
                "Garen looked towards Ves, who raised her lip to bare her teeth."
                "While his expression remained neutral, he radiated disgust as he looked upon her."
                GAREN @talk "... I've known many masters to keep strange {i}pets.{/i}"
                show garen at blurin, center_f
                GAREN @talk "As long as you can keep the green one on a leash, I don't see any issues."
                show ves at cleft with dissolve
                VES @angry "Spoken like a true GTC dog!"
                show ves at shake
                VES @angry "Give me one reason not to cut you down now."
                GAREN @smile "Look around you little greenskin."
                GAREN @smile "The guards here will kill you if you try."
                show ves at shake
                VES @angry "Not before I strike you down first..."
                show sypha at cright_f with dissolve
                SYPHA @talk "Now now, everyone."
                SYPHA @talk "You can all kill each other {i}later.{/i}"
                hide ves with dissolve
                hide sypha with dissolve
                jump qst_TheBeastOfNovaras_BarSceneShared_garenmenu
            "What do you want... Garen Quiltshire?":
                pass
    else:
        MC "So, what do you want... Garen Quiltshire?"

    GAREN @talk "The {i}Greater Trading Company{/i} are nearing completion of a secret trade deal with Alderay."
    GAREN @talk "Emperor Alcott will be shipping over weapons and supplies to help suppress the Orc rebellion on Skarshire in return for gold, food supplies, and mercenary forces."
    "Ves tightened her hands around her axe."
    VES @angry "And I'm just supposed to sit here and listen to how you plan to slaughter my people?"
    GAREN @talk "The deal is almost guaranteed to happen no matter what."
    GAREN @talk "What you, I, or anyone else {i}thinks{/i} is irrelevant."
    MC @angry "Why are you telling us this?"
    GAREN @talk "The supplies are to be moved in and out of the Free City's ports."
    GAREN @talk "Most of the merchant lords are on board... {i}but there are a few holdouts.{/i}"
    MC @serious "So, you want us to what, kill them?"
    show garen at shake
    GAREN @shock "Oh, gods... No, no no!"
    GAREN @think "That would be... difficult to explain."
    GAREN @smile "We simply need you to explain to them why it's in their interests to stop stalling this deal."
    show sypha at cleft with dissolve
    SYPHA @happy "I will of course, be assisting in this matter."
    show markus at shake
    MARKUS @angry "And why in all of Alderay would you want to help with this?"
    MARKUS @angry "How does strengthening Alderay's military benefit you in any way?"
    "Sypha smiled, exuding a kind of smug confidence."
    SYPHA @happy "My reasons are my own... and not for your concern."
    MC @think "And if we do this... we'll be able to return to Novaras?"
    GAREN @smile "At the Emperor's leisure."
    if CharInParty("ves"):
        "Garen's eyes glanced towards Ves."
        show garen at blurin, center
        GAREN @talk "He has even offered the Emperor's seal to let your orc companion have free passage throughout Alderay."
        show ves at cright_f with dissolve
        VES @angry "Why would the humans' emperor do such a thing?"
        VES @angry "Does he believe me so weak as to sell out my people for some trinket?"
        "Garen shrugged."
        GAREN @talk "That was the carrot."
        GAREN @angry "The stick is if you don't follow orders, he'll have the rest of your orc companions slaughtered."
        show ves at shake
        VES @angry "YOU LIE!"
        GAREN @talk "They are holed up in the northeast of Angmurus."
        GAREN @talk "As long as you obey, they won't be harmed... {i}For now.{/i}"
        "Ves seethed with rage, seemingly ready to strike the man down here and now."
        show ves at shake
        VES @angry "IF YOU SPEAK LIES..."
        GAREN @talk "Shall we have it in writing?"
        GAREN @talk "A contract that cannot be broken?"
        show ves at shake
        VES @angry "Shove your papers up your arse, dog!"
        GAREN @talk "Bark all you want, little greenskin."
        show garen at blurin, center_f
        GAREN @talk "{i}As long as you obey.{/i}"
        hide ves with dissolve

    $ tmpvar = ["what_if_refuse"]

    label qst_TheBeastOfNovaras_BarSceneShared_garenmenu2:
    if len(tmpvar) > 0:
        menu:
            "And if we refuse?" if "what_if_refuse" in tmpvar:
                $ tmpvar.remove("what_if_refuse")
                GAREN @serious "Then I'm afraid those closest to you will be remaining in confinement for a long time."
                GAREN @serious "{i}Or worse...{/i}"
                MC @surprised "What?"
                MC @angry "Are you threatening-"
                GAREN @talk "They have imprisoned your [erika_ref!t], Erika."
                GAREN @talk "As for Regina, they are also looking for her, to take her in for questioning."
                GAREN @talk "It's just a matter of time before they find her..."
                show mc at shake
                MC @surprised "WHAT?!"
                MC @angry "Erika hasn't done anything-"
                GAREN @talk "It matters not whether she is guilty or not."
                GAREN @talk "Only that she is leverage to get you to obey."
                if "elena" in QstJudgementDay().ImprisonedCharacters and "myu" in QstJudgementDay().ImprisonedCharacters:
                    GAREN @talk "Your pet she-bitch is also confined, I am told."
                    GAREN @talk "The wolf girl."
                    GAREN @talk "As is that curious slimelark."
                    GAREN @think "Strange creature, that one... Apparently she keeps calling out your name and crying."
                    show mc at shake
                    MC @angry "I swear upon the gods if any of them are harmed I'LL FUCKING-"
                    GAREN @talk "Calm yourself."
                    GAREN @talk "I swear it upon Vellomar's quill, no harm shall befall them."
                elif "elena" in QstJudgementDay().ImprisonedCharacters:
                    GAREN @talk "Your pet she-bitch is also confined, I am told."
                    GAREN @talk "The wolf girl."
                    show mc at shake
                    MC @angry "I swear upon the gods if she is harmed I'LL FUCKING-"
                    GAREN @talk "Calm yourself."
                    GAREN @talk "I swear it upon Vellomar's quill, no harm shall befall her."
                elif "myu" in QstJudgementDay().ImprisonedCharacters:
                    GAREN @talk "Your slimelark companion is also confined, I am told."
                    GAREN @think "Strange creature, that one... Apparently she keeps calling out your name and crying."
                    show mc at shake
                    MC @angry "I swear upon the gods if she is harmed I'LL FUCKING-"
                    GAREN @talk "Calm yourself."
                    GAREN @talk "I swear it upon Vellomar's quill, no harm shall befall her."
                MC @angry "If you're lying..."
                GAREN @talk "I am a member of the Greater Trading Company... Our word is gold."
                GAREN @talk "Perhaps a contract under Vellomar will please you?"
                GAREN @smile "{i}Our contracts are unbreakable.{/i}"
                MC "..."
                jump qst_TheBeastOfNovaras_BarSceneShared_garenmenu2

            "Who are these merchants?":
                pass
    else:
        MC "So who are these merchants?"

    SYPHA @happy "There are two of them."
    SYPHA @talk "But I want you to focus on Lord Zanzibat first."
    SYPHA @talk "His house is practically a fortress, it won't be an easy task breaking into there..."
    SYPHA @talk "However, perhaps we wouldn't have to."
    SYPHA @talk "He spends most of his time at the arena... He has a fondness for inviting new fighters to his home to discuss..."
    SYPHA @happy "{i}Private sponsorship arrangements{/i} with them."
    MC @think "I see..."
    GAREN @talk "I shall leave the fine details to all of you."
    show garen at nod
    "The man offered a curt bow."
    GAREN @talk "{i}May the ink dry.{/i}"
    hide garen with easeoutleft
    "He turned to leave without another word, leaving me and my mostly unhappy party to handle the {i}fine{/i} details as he put it."
    MC @serious "Well... What now?"
    SYPHA @happy "Now, we get to work."
    show sypha at blurin, cleft_f
    SYPHA @happy "{i}What fun!{/i}"
    hide sypha with easeoutleft
    $ QstStart(QstTheBeastOfNovaras)
    MC @serious "...{i}Fun.{/i}"
    $ LocEnter()


label qst_TheBeastOfNovaras_ApproachArena:
    show yarrick at cright_f with dissolve
    YARRICK @smile "Welcome... WELCOME! Step right up to glory's doorstep!"
    show mc at cleft with easeinleft
    "The man's eyes looked me up and down."
    YARRICK @smile "Ah, that stance, those scars!"
    YARRICK @smile "You look like a soul born for the sand and the roar!"
    YARRICK @smile "How about you..."
    YARRICK @think "... Wait."
    YARRICK @shock "No, it cannot be!"
    MC @think "Can I help you with something?"
    show yarrick at shake
    YARRICK @shock "YOU'RE HIM!"
    YARRICK @shock "THE BEAST OF NOVARAS!"
    MC @angry "... Damn it, man! Hold your tongue!"
    YARRICK @smile "You and your friends' posters are everywhere, friend."
    YARRICK @smile "The city hums with your name."
    YARRICK @smile "You know, some of the bards have started singing about you, right?"
    YARRICK @smile "A chorus of coin if ever I heard one."
    show markus at left with easeinleft
    MARKUS @shock "{i}They have?{/i}"
    MARKUS @smile "[player_name!t], where there are bards, there are women!"
    hide markus with dissolve
    if CharInParty("ves"):
        show ves at left with easeinleft
        VES @think "Vain..."
        hide ves with dissolve
    show sypha at left with easeinleft
    SYPHA @think "I once had a song written about me."
    SYPHA @happy "It was a death threat swearing revenge against me."
    SYPHA @happy "Quite beautiful, actually."
    KIARA @smile "Can I hear it sometime, mistress?"
    SYPHA @happy "Of course... Perhaps one day you'll try to betray me and write your own beautiful one!"
    KIARA @sad "N-No... I could never do that!"
    SYPHA @happy "Tsk... You still have so much to learn."
    hide sypha with dissolve
    MC @serious "What do you want from me?"
    YARRICK @smile "Forgive me, starstruck moment."
    YARRICK @smile "Heroes do that to a man."
    YARRICK @smile "Many still aren't sure what to make of you, but by saving Novaras, you saved a cousin of mine during the great siege."
    YARRICK @smile "For that, you have my voice and my venue."
    MC @think "Oh... Well... You're welcome, I suppose."
    YARRICK @smile "I am Yarrick, matchmaker of mayhem, ringmaster of the red sands."
    YARRICK @smile "If you're hunting coin and thunder, the crowd will pay dearly to see you and your companions baptize the arena with legend."
    show sypha at left with easeinleft
    "Sypha brushed up against me."
    SYPHA @happy "We would most definitely be interested!"
    SYPHA @think "But I'm afraid my husband here would need a worthy patron!"
    "I glanced at Sypha from the corner of my eye and she squeezed my arm tighter."
    YARRICK @smile "A worthy patron, you say? Names tumble, Lord Morritan, perhaps Calistos..."
    SYPHA @happy "I was thinking more... Lord Zanzibat."
    YARRICK @think "Zanzibat?"
    YARRICK @think "You... {i}are aware of their reputation for...{/i}"
    SYPHA @angry "I've heard that they are the finest patrons for fighters of the arena in the city!"
    SYPHA @angry "How could I accept anything less for my darling than the very best?"
    YARRICK @think "Hmm..."
    YARRICK @smile "Lord Zanzibat prefers veterans of the sands, champions who return for encore after encore."
    YARRICK @smile "I can send an invite... but to draw him from his silken chair we'll need a spectacle, noise enough to shake his jewels."
    "Yarrick paused for a moment as he stroked the sides of his beard."
    YARRICK @think "Even with your reputation, you must register and claim a few bouts."
    YARRICK @think "Paper before blood - such is the city."
    MC @think "How many?"
    YARRICK @think "The arena climbs in leagues, as all good stories do."
    YARRICK @smile "Clear the {i}Sun Forged{/i} ranks, survive the crucible, and the lords will sniff profit on the wind."
    $ QstSetProgress(QstTheBeastOfNovaras, 1)
    YARRICK @smile "Do that, and Zanzibat will see you as an investment with teeth."
    MC @angry "(How many times must I {i}prove{/i} myself?)"
    YARRICK @talk "I'll watch the boards."
    YARRICK @talk "When you're ready for the drumroll… come find me."
    $ LocFlush(dissolve)
    if HamunArena().Rank > 0:
        show mc at center with easeinleft
        MC "Wait... Sun Forged?"
        MC "But I already am!"
        $ QstSetProgress(QstTheBeastOfNovaras, 2)
        hide mc with easeoutright
    $ LocEnterQ()

label qst_TheBeastOfNovaras_SpeakToYarrickBeforeSunForged:
    show yarrick at center with dissolve
    YARRICK @sad "Ah, too soon for fireworks, friend."
    YARRICK @sad "Clear {i}Sun Forged{/i} first; then we set the city singing."
    YARRICK @talk "Return once your name climbs the slate."
    $ LocEnter()


label qst_TheBeastOfNovaras_SpeakToYarrickSunForged:
    show yarrick at right_f with dissolve
    show mc at cleft with easeinleft
    show markus at left with easeinleft
    YARRICK @smile "Ahh! Congratulations, my friend!"
    YARRICK @smile "Hamun has a new comet in its sky!"
    YARRICK @smile "They're already buzzing about the rising star of the Arena, your name rings like a war drum!"
    YARRICK @smile "Which means it's time for a {i}special{/i} show - one loud enough to pry Lord Zanzibat from his cushions."
    MC @think "What kind of {i}special{/i} show are we talking about?"
    YARRICK @serious "An opponent that drags the masses from their beds and makes the bookmakers sweat."
    YARRICK @talk "A common bandit is a yawn. We need wonder… or terror."
    "Yarrick's expression curved into a wicked smile."
    YARRICK @smile "I have just the thing."
    YARRICK @smile "An old whisper, a legend that has never kissed these sands."
    YARRICK @talk "A perfect mirror for {i}the Beast of Novaras{/i}, the crowd will lose its mind."
    YARRICK @think "... And you must be very sure you're ready to greet it."
    MC @think "What is the creature?"
    YARRICK @serious "Tradition binds my tongue."
    YARRICK @serious "Special bouts wear veils until the moment the gates open."
    MC @serious "(Hmm... I need to think this through. I should try and gather information on whatever we'd be...)"
    hide markus with dissolve
    show sypha at left with easeinleft
    "Sypha interjected, smiling as she placed her hand onto my chest."
    SYPHA @happy "{i}I'm sure my husband could handle anything in that arena of yours...{/i}"
    show mc at blurin, cleft_f
    "Forcing an awkward smile, I looked towards Sypha."
    MC @smile "Might I borrow you for a moment... {i}dear?{/i}"
    SYPHA @happy "Of course... {i}Husband.{/i}"
    hide yarrick with dissolve
    show mc at cright_f
    show sypha at cleft
    with ease
    MC @angry "What in the hells are you doing?"
    SYPHA @talk "Ensuring Zanzibat attends the arena."
    SYPHA @talk "You're not just {i}any{/i} fighter, you're an enigma to them right now, a great curiosity."
    SYPHA @talk "Fighting in the arena is sure to grab Zanzibat's attention if he knows you're coming."
    MC @angry "And if we die in the arena?"
    SYPHA @think "We will not die."
    SYPHA @think "As my husband, you are forbidden from doing so!"
    MC @angry "I am not your-"
    show yarrick at right_f with easeinright

    YARRICK @think "All smiles here, no cold feet, I trust?"
    show mc at blurin, cleft
    show sypha at left
    with ease
    SYPHA @happy "No, not at all!"
    YARRICK @smile "Good."
    YARRICK @talk "I'll begin the arrangements. We'll make Hamun hold its breath."
    SYPHA @think "And his cut?"
    YARRICK @think "Well, uhh... For a special match like this, the minimum is three thousand coins, house standard."
    SYPHA @angry "Five thousand coins."
    show yarrick at shake
    YARRICK @surprised "WHAT?!"
    YARRICK @smile "Ha! Those figures sing only for champions!"
    SYPHA @angry "Is my husband, the savior of Novaras, not worth five thousand coins?"
    MC @think "Where does this {i}husband{/i} talk keep coming-"
    YARRICK @surprised "E-Ehh..."
    YARRICK @smile "Very well. Five thousand."
    YARRICK @smile "Call it the Beast's premium."
    YARRICK @talk "Give me three days, then come find me."
    YARRICK @talk "Your stage will be set."
    show yarrick at blurin, right
    $ Pause(0.25)
    hide yarrick with easeoutright
    "With a curt bow, the arena master turned and left."
    show mc at blurin, cright_f
    show sypha at cleft
    with ease
    MC @angry "Did you just barter on my behalf?"
    SYPHA @think "Your behalf?"
    SYPHA @happy "Oh, I just wanted to make sure I earned something from it as well."
    SYPHA @happy "A thousand of those coins are mine."
    "My mouth hung agape."
    "I blinked, shaking my head slightly in disbelief."
    SYPHA @happy "Come now, we have other business to attend!"
    hide sypha with easeoutright
    $ QstTheBeastOfNovaras().YarrickSetsUpTheFightDay = GetGameDay() + 3
    $ QstSetProgress(QstTheBeastOfNovaras, 3)
    
    show mc at blurin, center
    with ease
    MC @angry "(This... girl!)"
    $ LocEnter()

label qst_TheBeastOfNovaras_SpeakToYarrickFightSetup:
    if QstTheBeastOfNovaras().YarrickSetsUpTheFightDay > GetGameDay():
        show yarrick at center with dissolve
        YARRICK @talk "Preparations for your match are still underway..."
        $ LocEnter()
    else:
        show yarrick at center with dissolve
        YARRICK @smile "Ahh... you're here, good."
        YARRICK @smile "Everything is ready if you are."
        YARRICK @talk "I should warn you... Zanzibat is only willing to attend a true spectacle."
        YARRICK @talk "You should be prepared before braving these sands..."
        menu:
            "I'm ready...":
                YARRICK @talk "Good... As per tradition, your companions will be taken to their own fight pits and will join you on the sands when the time comes."
                YARRICK @talk "Now, follow me... The sands await."
                scene black with dissolve
                jump qst_TheBeastOfNovaras_SpecialFightBloodworks

            "I'm not ready yet.":
                YARRICK @talk "Then prepare yourself for what is to come."
                $ LocEnter()

label qst_TheBeastOfNovaras_SpecialFightBloodworks:
    $ AutoMus(False)
    stop music fadeout 3.0
    $ LocNameSetTemp(_("Hamun arena, bloodworks"))
    $ AutoAmb(False)
    stop ambience fadeout 5.0
    scene bg_hamun_arena_bloodworks 
    show mc at center
    with dissolve
    "...There, as the stadium began to fill, I found myself anxiously waiting for my match to come."
    play sound "audio/cfx/crowd_cheer.ogg" volume 0.5
    "Above ground, the roar of the crowd shook the very foundations, bits of sand and dirt raining from the ceiling like the arena itself trembled with hunger."
    "I watched fighters shuffle past in tense silence."
    "The order was drilled in quickly: men against men for warm-up, men against beasts, the true bloodsport."
    "And at the end… {i}special{/i} matches."
    play sound "audio/cfx/crowd_cheer_smaller.ogg" volume 0.5
    "These were where legends were born, or broken."
    "Guards patrolled up and down the halls, ensuring no sudden fights and violence broke out."
    "{i}Blood was to only be spilt on the arena sands... Not down here in the bloodworks.{/i}"
    "They didn't want us killing each other before the crowd had a chance to pay for it."
    "A figure whose face was concealed by a full metal mask moved towards me."
    show cg_savage_kain at left with easeinleft
    SAVAGE_KAIN "Oi… You're that freak from Novaras, aren't ya?"
    show mc at blurin, right_f
    with ease
    show cg_savage_kain at left with ease
    MC @angry "..."
    SAVAGE_KAIN "Savage Kain's the name! Heh, though most just call me 'Savage'… saves 'em time when they're screaming for their lives." 
    SAVAGE_KAIN "When I'm done carving up whatever poor bastard they throw at me, it's you and me."
    SAVAGE_KAIN "On these sands. In front of every screaming throat out there."
    SAVAGE_KAIN "And when that time comes… I'll mount your ugly head on the walls of my piss-soaked tavern back home." 
    menu:
        "Did your mother not like you, giving you a name like that?":
            SAVAGE_KAIN "Keep my mother's name outta your filthy mouth!"
            MC @smile "Believe me, I'm sure plenty has been inside your mother's mouth."
        "Anyone who has to call themselves 'savage' couldn't fight his way out of a tavern brawl.":
            SAVAGE_KAIN "HAH! Big words from a caged beast. We'll see who leaves these walls alive today."
        "...":
            SAVAGE_KAIN "Cat got your tongue? Hah! Don't matter."
            SAVAGE_KAIN "I'll rip it out myself soon enough."
            MC @angry "You talk an awful lot for a soon to be dead man."
            show cg_guard_hamun at center with dissolve
            GUARD "That's enough you two!"
            GUARD "Save it for the sands."
            hide cg_guard_hamun with easeoutright
    "Snarling, Kain pointed his blade towards me, then motioned a slice across the neck, his laughter manic the whole time."
    "The arena master returned, unimpressed."
    show yarrick at center_f with dissolve
    YARRICK @talk "Kain. You're up."
    SAVAGE_KAIN "Finally! Ha! Watch close, freak!"
    SAVAGE_KAIN "This is what a real killer looks like!"
    SAVAGE_KAIN "I'M A FUCKING LEGEND BOYS!"
    hide cg_savage_kain with easeoutright
    "Clanging his blades together, he charged for the door, roaring loud enough to rattle the walls."
    show mc at blurin, cleft
    show yarrick at cright_f
    with ease
    YARRICK "{i}*Sigh*{/i}"
    "Yarrick's gaze slid toward me, his tone bone-dry."
    YARRICK @talk "Get ready, you're up soon."
    MC @think "Aren't you going to wait to see how 'Savage Kain' does?"
    play sound "audio/cfx/crowd_cheer.ogg" volume 0.5
    "The crowd roared again, and the doors swung open."
    show mc at left
    show yarrick at right_f
    with ease
    show cg_savage_kain_dead at center_f with easeinright
    "Moments later, a wagon cart wheeled past."
    "Kain's corpse split clean in half, blood pouring from him in steaming rivers."
    hide cg_savage_kain_dead with easeoutleft
    YARRICK @talk "Not fucking savage enough, it seems."
    MC @talk "... Still not going to tell me what I'll be facing up there?"
    YARRICK @talk "Tradition still stands on these sands."
    YARRICK @talk "I suggest you change into... {i}whatever it is you change into.{/i}"
    YARRICK @smile "The people hunger to see {i}the Beast,{/i} not {i}the Saviour.{/i}"
    "The thought twisted my stomach."
    "Was I still myself? Or only Shyahtan's shadow?"
    "Would I always be the beast? Or was there still a man buried in here somewhere?"
    "Yarrick slid a key into the lock and pushed the gate open."
    YARRICK @talk "When you hear the trumpet and the roar of the crowd, it's time."
    "I nodded."
    "He offered a small bow and vanished into the din."
    scene black with dissolve
    play sound2 "audio/cfx/transform.ogg"
    "...A short while later, I stood ready."
    "Every muscle - mine, or Shyahtan's - pulsed with dread and anticipation."
    play sound "audio/cfx/trumpet.ogg"
    "The trumpet bellowed. The doors swung open."
    $ LocNameSetTemp(_("Hamun arena"))
    scene cg_hamun_arena_day 
    show mc_transformed at cleft
    with flash
    play ambience "audio/ambience_loc/desert_day.ogg"
    "Blinding light seared through the dark tunnel as the announcer's voice thundered."
    HAMUN_ARENA_ANNOUNCER "And now! The moment you've all been waiting for!"
    HAMUN_ARENA_ANNOUNCER "You have heard whispers… tales already becoming legend!"
    "The air was thick, alive with the crowd's hunger."
    HAMUN_ARENA_ANNOUNCER "They say, in Novaras' darkest hour, {i}it{/i} answered the call!"
    HAMUN_ARENA_ANNOUNCER "A beast… a saviour… A MONSTER!"
    play sound "audio/cfx/crowd_cheer.ogg"
    "The crowd roared."
    "Half in awe, the other in hatred."
    "Their cheers and boos fused into one earth-shaking chorus."
    HAMUN_ARENA_ANNOUNCER "Some claim it is dark magecraft, born from the twilight of war."
    HAMUN_ARENA_ANNOUNCER "Others swear it is the hand of the new gods themselves!"
    "The ground shook beneath my claws."
    play sound "audio/cfx/crowd_cheer_smaller.ogg"
    "The noise was unlike anything I had ever felt, like standing at the heart of a storm."
    HAMUN_ARENA_ANNOUNCER "BUT MOST OF ALL…" 
    HAMUN_ARENA_ANNOUNCER "They say the Beast of Novaras would bless our sands!"
    HAMUN_ARENA_ANNOUNCER "And today... You will tell your children you were here when history was forged!"
    HAMUN_ARENA_ANNOUNCER "WHEN THE BEAST BECAME A GOD OF THE ARENA!"
    HAMUN_ARENA_ANNOUNCER "…OR DIED TRYING!"
    "I stepped into the sun."
    "The desert heat burned against my skin as thousands of eyes devoured me."
    "A freak, a monster, a saviour. All things at once, and none of them."
    "The arena was vast, grander than any pit I'd ever known."
    "More gates screeched open."
    play sound "audio/interactables/gate_drop.ogg"
    "Markus shuffled uneasily, eyes wide at the crowd."
    "His eyes nervously meeting mine briefly as the crowd roared once more."
    play sound "audio/cfx/crowd_cheer.ogg"
    "Sypha basked in their cheers, smiling, blowing kisses."
    if CharInParty("ves"):
        "Ves snarled as boos rained down, her glare cold enough to cut stone."
        play sound "audio/cfx/crowd_booing.ogg"
    "Then the announcer's voice rose higher still."
    HAMUN_ARENA_ANNOUNCER "And if that wasn't enough... we have a most honoured guest tonight!"
    HAMUN_ARENA_ANNOUNCER "You know her, you love her, empires have risen and fallen at her beauty!"
    HAMUN_ARENA_ANNOUNCER "THE HERO CELESTE!"
    play sound "audio/cfx/crowd_cheer.ogg"
    scene cg_celeste_arena_wave with dissolve
    "The roar was deafening, a tsunami of sound that rattled my bones."
    "Up on the raised, ornate seats, Celeste stood."
    "Radiant, her silver hair shimmering, her smile effortless, her presence commanding even the merchant lords beside her."
    "For a moment her eyes met mine. My breath caught. My chest tightened as though some unseen hand gripped it."
    "Celeste, {i}the{/i} Celeste, the jewel of Alderay, saviour of her own legendary party, was watching {i}me.{/i}"
    "Awe, terror, and something nameless flooded through me."
    "I felt small. I felt unworthy. And yet, for the first time, I wanted to be seen."
    scene cg_hamun_arena_day 
    show mc_transformed at cleft
    with dissolve
    HAMUN_ARENA_ANNOUNCER "But what is a legend without his rival?"
    HAMUN_ARENA_ANNOUNCER "Tonight, we bring you the perfect rival to make this match TRULY LEGENDARY!"
    "The portcullis across the sands began to lift with the cogs grinding like the growl of a beast. Darkness loomed beyond."
    play sound "audio/cfx/gate_gears_spin.ogg"
    "I braced. Claws curled. My heartbeat pounded with each mechanical grind."
    "With a loud THUD, the cogs stopped as the portcullis was fully raised."
    play sound "audio/cfx/gate_open_chains.ogg"
    HAMUN_ARENA_ANNOUNCER "Dragged from the deserts of Ramon… a nightmare born of the old gods' wars!"
    play sound "audio/cfx/demorai_roar_high1.ogg"
    "A roar shrieked from the black."
    "High, piercing, primal."
    play sound2 "audio/cfx/caltrack_approach_1.ogg"
    "Dust shook from the walls as titanic footsteps echoed closer."
    HAMUN_ARENA_ANNOUNCER "A beast so cursed, adventurers whisper its name with dread!"
    "A massive leg stepped forward, reptilian, clawed, each talon the size of a man's arm."
    $ AutoMus(False)
    stop music fadeout 1.0
    scene cg_caltrack_appear with flash
    $ Pause()
    "Another step, and its colossal body rolled into the light."
    play sound "audio/cfx/caltrack_approach_2.ogg"
    "Bronze scales glinted. Its great lashing tail gouged the sand."
    "Three serpent heads swayed on their long necks, tongues flicking, red eyes glimmering with hunger."
    HAMUN_ARENA_ANNOUNCER "THE CALTRACK!"
    $ PlayMusicRandom("mus_battle_generic")
    play sound "audio/cfx/demorai_roar_high2.ogg"
    play sound2 "audio/cfx/crowd_cheer.ogg"
    "The crowd howled in frenzy as the monster reared, all three heads snapping, hissing with enough force to whip the air."
    "The heat of its breath washed over me..."
    "Sulphur and blood, rancid and suffocating."
    "Dust swirled at my feet, whipped up by its sheer presence."
    "The sun beat down. Weapons raised."
    $ QstSetProgress(QstTheBeastOfNovaras, 4)
    "The sands would drink blood this day."
    "...Ours, or its."
    "And then… it struck!"
    $ TransformMC(True)
    $ TransformMarkus(True)
    $ TransformKiara(True)
    $ StartBattle(BattleData(BackgroundImage = "pbat_hamun_arena", CharIDList_Right = ["e_caltrack"], CanTransform = False))
    play sound "audio/cfx/demorai_roar_high1.ogg"
    scene cg_hamun_arena_day
    show mc_transformed at cleft
    with dissolve
    "The beast roared, its heads swaying as it fell, crashing down onto the hot sands."
    play sound "audio/cfx/crowd_cheer.ogg"
    "The crowd cheered in frenzied excitement as, exhausted, I turned towards the others, nodding at Markus."
    "I turned my gaze towards the lady Celeste, hoping, if a little vainly, that she would be cheering and applauding me for our efforts."
    $ AutoMus(True)
    scene cg_caltrack_crowd_attack_2 with dissolve
    "...And yet, with her face buried in her hand, she seemed..."
    "{i}Bored.{/i}"
    "Not bored. Not exactly."
    "Her shoulders trembled, not with sorrow but with a stifled laugh."
    "When her hand slipped, I caught the faintest glint in her eyes."
    "Hungry, feverish."
    "The crowd sought a hero's blessing, but Celeste's lips curved in something else entirely."
    "Not joy. Not pride. A strange, dark delight she tried to hide." 
    "I was taken aback."
    "After felling such a great beast, did it really not even elicit a-"
    "The tail suddenly whipped out, slamming Markus against one of the stone walls."
    $ AutoMus(False)
    $ PlayMusic("audio/music/46_Siege_Theme.ogg")
    scene cg_caltrack_revived with flash
    "He screeched in pain as the Caltrack sprung back into furious life."
    "For the first time, Sypha's cool expression cracked as in a sudden panic she dodged one of the heads slamming into the sand next to her."
    if CharInParty("ves"):
        "Ves cried out enraged as she began to hack at the thing with her axes."
        "Piercing through the thick hide of the beast, it let out a deafening screech, snapping its jaws at her, barely missing before slamming its head back to knock her to the ground."
    play sound "audio/cfx/crowd_cheer_smaller.ogg"
    "The audience's voice once again rose in a choir of excitement, then cracked into shrieks."
    play sound2 "audio/cfx/prologue_guysnap.ogg"
    "The Caltrack's heads writhed into the stands, one maw snapping a man in half."
    scene cg_caltrack_crowd_attack with dissolve
    "Blood sprayed across the seats."
    play sound "audio/cfx/crowd_panic.ogg"
    "Children wailed."
    "People shoved and clawed at each other in blind terror, trampling the fallen as they rushed for the exits."
    "Even the presenters seemed shaken at the beast's blind fury."
    "Suddenly, the neck of one of the heads stretched forward, grabbing a spectator from the stands and thrashing him until the body broke apart like a doll."
    "There was a split second of disbelief."
    "Then the crowd realized it could be {i}their{/i} blood next."
    "Cheers turned to chaos as the masses surged toward the exit gates, clogging the narrow tunnels. Dozens were crushed, pinned, screaming."
    "Total fear took over as the announcer bellowed out."
    HAMUN_ARENA_ANNOUNCER "REMAIN CALM! THE ARENA GUARD WILL ARRIVE MOMENTARILY AND-"
    "A loud whip of the Caltrack's tail left a huge gash in the stone wall; at this rate, the thing would bring the whole arena down!"
    "The organizers and high lords turned to each other in a panic, snapping orders to guards who rushed uselessly about."
    "Celeste leaned forward now, elbows on her knees."
    "At first glance, her face was the mask of irritation, as though waiting for wine."
    "But her lips were parted, just slightly, as her breath quickened."
    "Her eyes gleaming with... {i}excitement?{/i}"
    "Or was it something else?"
    "Either way, she did not act... What in the hells was she waiting for?" 
    "As the enraged heads of the Caltrack now focused on the mass of people attempting to escape, I hurled myself forward, driving my claws deep into one of the creature's feet."
    "As the blades pierced flesh, it bellowed in pain, turning its attention away from the helpless towards me."
    "I held out, but the frenzied beast moved faster, {i}hit harder.{/i}"
    scene cg_parasite_slammed with dissolve
    play sound "audio/cfx/explosion.ogg"
    "Slammed against the wall as it used its powerful neck to smash me aside, I dropped to the floor, agony giving way to exhaustion."
    "My ribs screamed. My vision blurred red."
    "I clawed at the stone, nails scraping, but my arms trembled uselessly."
    "Blood filled my mouth as I spat onto the sand, every breath fire through broken lungs."
    "Every limb, every muscle refused to move as I struggled against them."
    "The long, elongated necks loomed over me, fangs bared and dripping, breath hot and rancid on my skin."
    "A terrible sense of dread washed over me, not fear, but what comes after it."
    "{i}Acceptance.{/i}"
    "This… this really was it."
    "I had only narrowly escaped the jaws of death with Zanarak to find myself here."
    "Once more in death's grasp, once more unable to fight."
    "Weak."
    "Powerless."
    stop ambience fadeout 1.0
    scene black with dissolve
    "WEAK."
    $ Pause(1.0)
    $ narrator = Character(what_color = "#ff0000", show_always_effect = always_shake(x = 0, y = 2))
    "{i}POWERLESS.{/i}"
    $ Pause(1.0)
    $ narrator = Character()
    $ Pause(1.5)
    jump qst_TheBeastOfNovaras_ParasiteShipFlashback

label qst_TheBeastOfNovaras_FlashbackBattleDeathLines:
    SHYAHTAN "{i}Organs failing...{/i}"
    SHYAHTAN "No... This was no..."
    SHYAHTAN "Not what happened."
    SHYAHTAN "Why? Why can't I remember?"
    SHYAHTAN "Darkness... Darkness all around."
    return

label qst_TheBeastOfNovaras_ParasiteShipFlashback:
    $ AutoTimeFreeze(True)
    $ LocNameSetTemp(_("Parasite Ship Main Deck"))
    $ AutoAmb(False)
    $ AutoMus(False)
    stop sound fadeout 3.0
    $ PlayMusic("audio/music/49_Fauna_and_Space.ogg")
    play ambience "audio/ambience_scenes/para_ship_ambience.ogg"
    scene cg_para_ship_main_deck
    show mc_transformed at cright_f
    with dissolve
    show cg_zofn at left with easeinleft
    ZERO_ONE_FOUR_NINE "... Lord Shyahtan."
    ZERO_ONE_FOUR_NINE "Your Zarpod is ready."
    SHYAHTAN "What is the status of the siege?"
    ZERO_ONE_FOUR_NINE "Their capital still holds."
    ZERO_ONE_FOUR_NINE "Our Terran brothers have yet to breach the walls."
    ZERO_ONE_FOUR_NINE "It falls upon our clan to bring honor once more."
    SHYAHTAN "As is always the way."
    "I rose from my seat, the neural link tendrils withdrawing from my arms back into the hull of the ship."
    SHYAHTAN "How many of our kin stand ready to orbital drop?"
    ZERO_ONE_FOUR_NINE "Three thousand strong. Another ten thousand of the other clans already claw at the walls."
    SHYAHTAN "{i}And the enemy?{/i}"
    ZERO_ONE_FOUR_NINE "Thirty thousand Merlanians man the defenses. Five thousand royal guard."
    "There was a pause."
    ZERO_ONE_FOUR_NINE "{i}Shame… they would have sired fine warriors for us to convert.{/i}"
    SHYAHTAN "Their bodies will feed the young. Death does not excuse them from service."
    ZERO_ONE_FOUR_NINE "Of course, my lord. Their artillery still holds the clans at bay."
    ZERO_ONE_FOUR_NINE "The Tarakan requests we prioritize their rail guns."
    SHYAHTAN "The reinforcements will not be necessary."
    SHYAHTAN "{b}The honor shall be ours alone.{/b}"
    ZERO_ONE_FOUR_NINE "... What are your orders, my lord?"
    SHYAHTAN "Alert the others. They follow me down."
    ZERO_ONE_FOUR_NINE "Yes, Lord Shyahtan."
    "The officer pressed his palm to the hull."
    show cg_zofn at nod
    "Tendrils erupted from the walls to pierce his flesh, carrying my orders to the others."
    scene black with dissolve
    "I strode to the launch bay, where the fleshy maws of the Zarpods yawned open, their insides pulsing wetly with nervous anticipation."
    "I climbed inside. Its walls throbbed around me, veins glowing faintly as my tendrils sank into its flesh."
    "The bond was instant: its fear, its hunger, its obedience all became mine."
    SHYAHTAN "{i}Calm…{/i}"
    "{i}Zarpod rumbled in response...{/i}"
    SHYAHTAN "Once more into battle."
    stop ambience fadeout 1.0
    $ PlayMusic("audio/music/50_Hunting_Call.ogg")
    scene cg_zarpod_drop_1 with dissolve
    play sound "audio/cfx/zarpod_roar.ogg"
    "The beast roared and hurled itself into the void."
    "Dozens, then hundreds followed, a swarm of living meteors plummeting toward the Merlanian world."
    "The atmosphere screamed as we tore through it. Heat scorched the Zarpod's hide; fire licked its body until it glowed like a star."
    "Around me, others burned, their carcasses bursting into flaming shrapnel. But still we fell."
    "A railgun beam seared past, a line of blue death. One struck a kin to my left, annihilating him and his beast in a burst of ash."
    "Their screams joined the roar of re-entry. It did not matter."
    "{i}We had breached.{/i}"
    scene cg_zarpod_drop_2 with dissolve
    play sound "audio/cfx/explosion.ogg"
    play ambience "audio/ambience_scenes/merlanian_city_alarm.ogg" fadein 2.0
    play ambience2 "audio/ambience_scenes/merlanian_city_battle_1.ogg" fadein 2.0
    "The cities inner defences were little match for the speed of the Zarpod."
    "If their orbital defences couldn't stop them, the desperate cannons built to defend against ground forces were far too slow."
    "The city, already hanging on by a thread from the assault outside, descended into full blown chaos."
    "My Zarpod slammed into a tower, stone shattering, fire blossoming."
    "Rubble engulfed me as others crashed nearby, entire streets erased in a rain of monsters."
    scene cg_zarpod_drop_3 with dissolve
    "Through smoke and dust, yellow-skinned Merlanian soldiers scrambled, their weapons trembling as they circled, hoping we had perished in the fall."
    "They shared anxious looks behind their visors, terrified at the strange, motionless creature before them."
    "Nervously, they took a brave step closer, and..."
    scene cg_zarpod_drop_4 with dissolve
    "My Zarpod's tendrils exploded outward, skewering two, snapping their bodies like twigs."
    "Their blood ran hot across the rubble as the beast roared triumphant."
    "Those around screamed, fleeing the scene as they watched their finest warrior's blood and guts decorate the floor."
    "Their bodies in their final moments still twitched, a foot here, a trembling hand there."
    "It mattered not, next time though, I would ensure my Zarpod focused more on the heads or piercing the hearts."
    "{i}Quicker that way...{/i}"
    stop ambience fadeout 5.0
    $ LocNameSetTemp(_("Merlanian city"))
    scene cg_merlanian_city_fire_int
    show mc_transformed at left
    show cg_zarpod at right_f
    with dissolve
    "The alarms screamed as the building burned around me."
    "My Zarpod turned its heads toward me, expectant, grumbling."
    SHYAHTAN "I sense a trap outside, be ready to provide air support."
    play sound "audio/cfx/zarpod_roar.ogg"
    show cg_zarpod at shake
    $ Pause(0.25)
    hide cg_zarpod with easeouttop
    $ Pause(0.15)
    show mc_transformed at center with ease
    "It bowed and soared skyward as I marched into the city streets, my weapon humming with hunger."
    hide mc_transformed with moveoutright 
    play ambience2 "audio/ambience_scenes/merlanian_city_battle_2.ogg"
    scene cg_merlanian_city_fire
    show mc_transformed at left
    show cg_merlanian_soldier as merl2 at right_f with easeinright
    "There on the city streets, a Merlanian patrol swarmed me."
    MERLANIAN "DEATH TO THE FALSE GODS!"
    "They raised their weapons ready to fire as the battle raged all around us."
    scene cg_flesheater with dissolve
    play sound "audio/cfx/zarpod_roar.ogg"
    "Before their rounds could hit, my Zarpod slammed in front to take the brunt of the damage for me."
    "I plugged into the Zarpod's flesh, raising my flesheater as a few Merlanian warriors did their best to rush me."
    play sound "audio/cfx/flesheater.ogg"
    "The swarm shrieked as it erupted, devouring them to bone in the blink of an eye."
    "The hungry bugs quickly buzzed off when they were done, off to find someone else to eat."
    scene cg_merlanian_city_fire
    show mc_transformed at left
    show cg_zarpod at right_f
    SHYAHTAN "I can take it alone from here."
    SHYAHTAN "Destroy their rail guns. I will open the gate."
    play sound "audio/cfx/zarpod_roar.ogg"
    show cg_zarpod at shake
    $ Pause(0.25)
    hide cg_zarpod with easeouttop
    $ Pause(0.15)
    play sound "audio/cfx/zarpod_roar.ogg"
    "My Zarpod launched itself upwards into the sky once more, joining the others in the attack on the city's rail guns."
    hide mc_transformed with moveoutright
    "Rushing towards me, more Merlanian guards desperately charged in."
    show cg_merlanian_soldier as merl1 at left with easeinleft
    show cg_merlanian_soldier as merl2 at right_f with easeinright
    MERLANIAN "Stop him! Open fire at will!"
    SHYAHTAN "{i}Cute.{/i}"
    $ StartBattle(BattleData(BackgroundImage = "pbat_merlanian_bg", CharIDList_Left = ["shyahtan"], CharIDList_Right = ["e_merlanian_soldier", "e_merlanian_soldier", "e_merlanian_soldier", "e_merlanian_soldier"], CanTransform = False, CanUseItems = False, Label_BattleDefeatExtraNarrative = "qst_TheBeastOfNovaras_FlashbackBattleDeathLines"))
    scene black with dissolve

    "Overhead, I watched as some Zarpods slammed into one of the railguns, tearing the thing apart in their immense jaws as they let the wreck crash down onto the city below."
    "A few of the Merlanians were still desperately trying to hold out, rallying to defend the gate to their precious capital from both the siege outside {i}and{/i} within."
    "The leader among them, armored and bearing the marks of rank, screamed orders of air support: futile prayers to gods long deaf."
    "He turned to me, weapon raised, and charged with a final cry."
    MERLANIAN "FOR THE REPUBLIC!"
    $ StartBattle(BattleData(BackgroundImage = "pbat_merlanian_bg", CharIDList_Left = ["shyahtan"], CharIDList_Right = ["e_merlanian_soldier", "e_merlanian_general", "e_merlanian_soldier", "e_merlanian_soldier"], CanTransform = False, CanUseItems = False, Label_BattleDefeatExtraNarrative = "qst_TheBeastOfNovaras_FlashbackBattleDeathLines"))
    scene zarpod_kill with dissolve
    "Before I could deliver the killing blow, a Zarpod slammed into the ground and devoured him whole."

    SHYAHTAN "How... {i}disappointing.{/i}"
    "What strange words he spoke. 'Republic'... I will have one of the captured explain its meaning later."
    $ PlayMusic("audio/music/50_Hunting_Call.ogg")
    "Another foolish name for another doomed system of rule."
    scene cg_merlanian_city_fire
    show mc_transformed at cleft
    with dissolve
    "With each conquest I learned."
    "Kings, queens, gods, emperors... so many words, so much foolishness."
    "Why did they choose to refuse joining us Terrans?"
    "Could they not see the fight was impossible?"
    "Could they not see the unity we offered?"
    "Once their children were made Terran like us, they understood, {i}they became one.{/i}"
    "It was always the same. We welcomed their lust, it was in our very nature to do so."
    "...And they, no matter the race, could not resist."
    "A wise race accepted the end."
    "They accepted we would breed with them, that their children were perfect candidates to become Terrans, to merge with the sanja."
    "Their worlds ended peacefully, joyously, as they served the Hive in mating and in rest."
    "But some uncovered our truth too early. Some chose violence."
    "And when persuasion failed, violence always prevailed."
    "As I watched my clansmen tear apart the last guards at the gate, the walls themselves fell."
    "Terrans clambered over, flooding the city in a tide of black flesh and steel."
    "There was nothing left now, except claim the final piece of glory."
    "Their leader. King, queen, it mattered not."
    "{i}I would return with their head.{/i}"
    hide mc_transformed with easeoutright
    scene cg_merlanian_temple_approach with dissolve
    "The last of them stood on the steps, decorative armor glinting."
    "Royal guard. High guard. Whatever their name, they died the same."
    "I had expected more. But only a handful remained, the rest fled like cowards."
    "I would at least grant those who fought the mercy of a swift death."
    "The deserters I would leave to the flesheaters."
    "Ascending the steps, I pushed open the doors to their highest temple."
    stop ambience2 fadeout 3.0
    $ LocNameSetTemp(_("Merlanian temple"))
    scene cg_merlanian_temple with dissolve
    $ PlayMusic("audio/music/51_Arabesque.ogg")
    "...This temple was not as expected."
    "No cowering women. No warrior awaiting a last duel."
    "Only a vast chamber, darkness broken by the blue glow of a circular pool."
    show mc_transformed at left with easeinleft
    "I stepped closer. The doors sealed behind me."
    play sound "audio/cfx/stone_door_close.ogg"
    MYSTERIOUS_WOMAN "All hail... Shyahtan."
    show cg_merl_sage at cright_f with easeinright
    "A frail figure emerged from the shadows, cloaked, circling the pool like a carrion bird."
    MYSTERIOUS_WOMAN "The lord of a thousand stars, master of the Black Terran clan."
    SHYAHTAN "...Who are you, witch?"
    SHYAHTAN "How do you know my name?"
    MYSTERIOUS_WOMAN "Hahaha!"
    MYSTERIOUS_WOMAN "I know many things, Shyahtan."
    SHYAHTAN "Have you come to challenge me to battle?"
    MYSTERIOUS_WOMAN "Oh dear..."
    MYSTERIOUS_WOMAN "Always so preoccupied with the fight before you. You cannot see the war beyond."
    SHYAHTAN "You speak in riddles."
    SHYAHTAN "Make sense, or I will peel your cackling head from your shoulders."
    MYSTERIOUS_WOMAN "I give you truth."
    MYSTERIOUS_WOMAN "The great Shyahtan will be destroyed by the one reflected in that pool."
    "I looked at the water, then back to her."
    SHYAHTAN "{i}Mockery?{/i}"
    SHYAHTAN "Do you know what I will do to you, and the scraps of your people?"
    MYSTERIOUS_WOMAN "I speak truth. Or does the great Shyahtan fear truth?"
    SHYAHTAN "Tschh!"
    scene cg_shyahtan_water with dissolve
    "I looked closer into the water. The ripples stilled. The reflection cleared."
    "{i}Only myself stared back.{/i}"
    play sound "audio/cfx/water_splash_bath.ogg"
    play sound2 "audio/battle/battle_chars/mc_transformed/basic_attack/swing.ogg"
    scene cg_merlanian_temple 
    show mc_transformed at cleft
    with flash
    "Enraged, I slashed the pool, water spraying."
    SHYAHTAN "WHAT MOCKERY IS THIS?"
    SHYAHTAN "I ONLY SEE MYSELF!"
    show mc_transformed at cright with ease
    play sound "audio/cfx/merlanian_sage_laugh.ogg"
    "The figure was gone. Only her echoing laugh remained."
    MYSTERIOUS_WOMAN "Rejoice, Shyahtan! The truth shall set you free of your chains!"
    show mc_transformed at blurin, cright_f
    "I spun."
    "Empty halls, only laughter."
    play sound "audio/cfx/stone_door_open.ogg"
    "The doors burst open as one of my clansmen stumbled in."
    show cg_zofn at cleft with easeinleft
    ZERO_ONE_FOUR_NINE "Lord Shyahtan! The city is ours!"
    SHYAHTAN "Good."
    ZERO_ONE_FOUR_NINE "Are you wounded, my lord? Should I prepare-"
    SHYAHTAN "I am fine."
    ZERO_ONE_FOUR_NINE "My lord... What happened here?"
    SHYAHTAN "..."
    SHYAHTAN "Nothing. The temple was empty."
    SHYAHTAN "Prepare my Zarpod. We return to the Primaris."
    SHYAHTAN "{i}This world is ours...{/i}"
    scene black with dissolve
    jump qst_TheBeastOfNovaras_ReturnFromMerlanians

label qst_TheBeastOfNovaras_ReturnFromMerlanians:
    scene cg_zarpod_return with dissolve
    "...The journey back to the Primaris, my most prized ship, was short."
    "Of eighteen hundred and ninety-six conquests, this was my one hundred and twenty-second in its name."
    "Through the rift gates we leapt across space and time, as though reality folded just for us."
    "Sweet poisoned kisses or claws of steel, world by world joined the Hive."
    "I often wondered the true intent of the rift gates, these ancient monoliths found on every world."
    "Relics older than empires, yet still they functioned, weaving all worlds in their hidden tapestry."
    "My Zarpod pressed through the ship's flesh, muscle and bone parting to let it nest in its berth."
    play ambience "audio/ambience_scenes/para_ship_ambience.ogg"
    $ PlayMusic("audio/music/49_Fauna_and_Space.ogg")
    $ LocNameSetTemp(_("Parasite Ship Main Deck"))
    scene cg_para_ship_main_deck
    show dramora at cright_f
    with dissolve
    show mc_transformed at left with easeinleft
    "I crawled out and strode to the bridge."
    DRAMORA @smile "Once more, you bring honor to our clan, Lord Shyahtan."
    show mc_transformed at cleft with ease
    "I moved closer toward Dramora, my most prized concubine."
    SHYAHTAN "You were ordered to stay on Kalagon, zero-seven-nine."
    DRAMORA "Forgive me, my lord. The Hive Lord himself wishes to congratulate you."
    DRAMORA "I thought it wise to prepare for his arrival."
    MC "So soon? The council has not even convened to discuss the next conquest."
    DRAMORA "Apparently it is for another matter, one they would not disclose."
    "She wanted to embrace me, but held back. Affection was strange for our kind, but she was half-breed. Remnants of her old self persisted."
    SHYAHTAN "When does the Hive Lord arrive?"
    DRAMORA "Soon... his flagship joins us within the hour. I have arranged a feast, and two of our best to mate with him."
    SHYAHTAN "Bah!"
    SHYAHTAN "He had best come to reward me. Once again, it is my clan that secures victory while others fail."
    DRAMORA @smile "I couldn't agree more, my lord."
    "She stepped closer, tracing her finger down my chest. Other Terrans would have dragged her away for presumption. I found her disobedience… entertaining."
    DRAMORA "Shall I wait in your quarters? Or send another to please you? Perhaps one of the captured females?"
    "My eyes lingered. Her companionship offered more than simple mating."
    SHYAHTAN "Join me in my chambers."
    "Despite her composure, the curve of her smile betrayed her hunger."
    DRAMORA "As you wish, my lord."
    scene black with dissolve
    $ LocNameSetTemp(_("Parasite Ship, private quarters"))
    scene cg_para_ship_priv_quarters with dissolve
    show mc_transformed at cright_f
    show dramora at cleft
    with dissolve
    SHYAHTAN "Dramora, do not test me before the others."
    SHYAHTAN "I may humor your quirks, remnants of your old self. But others will question my authority."
    DRAMORA @smile "Mmm… imagine their questions if they knew you granted me a name without the Hive Lord's blessing."
    SHYAHTAN "Dramora..."
    DRAMORA @smile "{i}I've missed you, my lord.{/i}"
    DRAMORA @smile "My..."
    show dramora at center with ease
    DRAMORA @smile "Master."
    SHYAHTAN "Tschh! Must I punish you again?"
    "Dramora's hand slid down, grasping me."
    DRAMORA "Yes, my lord."
    DRAMORA "{i}Punish me.{/i}"
    scene black with dissolve
    $ PlayMusicRandom("mus_sex")
    "With my hand gripped to her throat, a gasp escaped her lips as I threw her down onto the soft, fleshy hull of the ship."
    scene dramora_missionary_idle
    with dissolve
    $ Pause()
    "She parted her legs expectantly, the length of my cock rubbing against her slit."
    DRAMORA "Oh my~"
    DRAMORA "It seems my lord is more than a little {i}'excited'{/i} to put me in my place!"
    SHYAHTAN "You are a strange Terran, Dramora."
    DRAMORA "You might have conquered me and turned me into this, my lord..."
    DRAMORA "{i}But I think I've conquered you too...{/i}"
    "As my cock slid along her wet slit, she cooed softly."
    SHYAHTAN "Conquered {i}me?{/i}"
    "Dramora whimpered, her cunt glistening in the light as she felt my cock press against her entrance."
    DRAMORA "M-Mhmm!"
    SHYAHTAN "It's time I put you back in your place, Dramora."
    DRAMORA "My lord protests too much when he should be focusing on fucking my-"
    $ PlaySexFx("audio/sex_sounds/nijah_miss_1.ogg", 1)
    scene dramora_missionary_slow
    with dissolve
    $ Pause()
    "Dramora gasped as she felt my cock thrust into her tight, welcoming heat."
    "She was a great warrior once... a great commander."
    "But as she squeezed her enhanced, altered cunt around my cock,"
    "{i}I took pride in what I had helped warp her body into.{/i}"
    "Dramora trembled as she felt the length of me stretch her out."
    "Of all my concubines, somehow, it always felt best to mate with Dramora."
    DRAMORA "H-Harder!"
    DRAMORA "{i}Show me why I bent the knee to you!{/i}"
    $ PlaySexFx("audio/sex_sounds/nijah_miss_2.ogg", 1)
    scene dramora_missionary_fast
    $ Pause()
    "Dramora gasped and choked as my hand tightened around her throat."
    "Her tight, soaking cunt squeezed me as I slammed deeper into her welcoming heat."
    "{i}It would be good for her to sire me another son.{/i}"
    "{i}Of all my concubines' wombs, she had given me the most.{/i}"
    DRAMORA "{i}*Choking*{/i}"
    DRAMORA "{i}H-Harder!{/i}"
    DRAMORA "Don't stop!"
    DRAMORA "Make me carry another of your spawn!"
    SHYAHTAN "{b}Beg me.{/b}"
    "Dramora quivered, her cunt twitching in excitement."
    DRAMORA "P-Please!"
    DRAMORA "M-My lord!"
    DRAMORA "Mmmfghhh! ❤️"
    DRAMORA "{i}Master!{/i}"
    "Dramora shook her hips as she did her best to take my cock as deeply as she could."
    SHYAHTAN "How many times must I punish you for your antics?"
    "Dramora's whole body trembled, her skin sheened with sweat in the dim light as she cried out."
    DRAMORA "I beg you! Breed me! Fill my womb!"
    DRAMORA "P-Please!"
    DRAMORA "{i}Please! Please! Please! Please! Please! Plea-{/i}"
    $ PlaySexFx("audio/sex_sounds/nijah_miss_finish.ogg")
    scene dramora_missionary_finish
    with flash
    $ UnlockGalSceneAndGrantXp("dramora", "missionary")
    $ Pause()
    "Dramora's cunt tightened and squeezed around me as I roared,"
    "Burying my cock to the hilt as I flooded her womb with my seed."
    DRAMORA "{b}Y-Yessssss! ❤️{/b}"
    "No sooner had I spilled into Dramora than the fleshy doors twisted open and steps approached from behind."
    $ PlayMusic("audio/music/49_Fauna_and_Space.ogg")
    scene cg_para_ship_priv_quarters 
    show mc_transformed at cright
    with dissolve
    show cg_zofn at left with easeinleft
    ZERO_ONE_FOUR_NINE "Forgive me, my lord, I-"
    show mc_transformed at blurin, cright_f
    "He paused, glancing down at Dramora, grinning as she lay sprawled on the floor, my seed leaking from her."
    SHYAHTAN "Why have you disturbed me and my mate?"
    ZERO_ONE_FOUR_NINE "The Hive Lord has arrived earlier than expected."
    "Zero-one-four-nine's eyes lingered a heartbeat longer on Dramora."
    SHYAHTAN "...You fought well in the recent battle, zero-one-four-nine."
    ZERO_ONE_FOUR_NINE "My lord?"
    SHYAHTAN "Select two of our veterans for commendation, promote them to your cadre."
    ZERO_ONE_FOUR_NINE "Lord Shyahtan!"
    ZERO_ONE_FOUR_NINE "You bestow a great honor upon me!"
    SHYAHTAN "Now, lead me to the Hive Lord."
    show cg_zofn at nod
    scene black with dissolve
    "Zero-one-four-nine nodded and led me toward the great chamber."
    "As the fleshy doors parted, the other Terrans bowed their heads in submission as I entered."
    $ LocNameSetTemp(_("Parasite Ship, great chamber"))
    scene cg_para_ship_hive_lord_anim with dissolve
    $ Pause()
    "There, the Hive Lord gazed out through one of the many great eyes of the blinking ship, staring into the vast sea of stars."
    "He tilted his head toward me as I entered, then returned his gaze to the void."
    HIVE_LORD "...You have done well, Lord Shyahtan."
    SHYAHTAN "I have done as expected of me. Nothing more, nothing less."
    HIVE_LORD "Of course."
    HIVE_LORD "You have never failed me before, have you?"
    "There was a long pause between us."
    SHYAHTAN "...Hive Lord?"
    HIVE_LORD "...I am told you are refusing the Great Joining once more this year."
    HIVE_LORD "May I ask why?"
    SHYAHTAN "The other Terran lords do not understand I am your hammer, great Hive Lord."
    SHYAHTAN "They seek to prove their clans would serve best as your will."
    SHYAHTAN "The Great Joining."
    SHYAHTAN "Merging all of our minds as one. This will only stoke the fires of their envy."
    SHYAHTAN "I cannot be your weapon if they undermine my plans."
    HIVE_LORD "{i}...Is that so?{/i}"
    "Once more, the Hive Lord broke his gaze from the black sea and stared toward me."
    HIVE_LORD "{b}Or could it be because you know your *true* feelings toward me would be laid bare for all to see?{/b}"
    SHYAHTAN "..."
    SHYAHTAN "...Great Hive Lord, my true feelings for you are nothing but-"
    "For the faintest moment I paused, the words coming out awkwardly."
    SHYAHTAN "{b}Loyalty and adoration.{/b}"
    HIVE_LORD "..."
    "The Great Hive Lord tilted his head forward once more."
    HIVE_LORD "{i}Of course, Shyahtan... my greatest general.{/i}"
    HIVE_LORD "Never have I doubted your loyalty."
    HIVE_LORD "{i}...Though some believe you are destined to become the new Hive Lord once I return to our great father.{/i}"
    SHYAHTAN "Then give me these traitors' names and I will see to it my Zarpod feasts upon them."
    HIVE_LORD "...Do you remember the Hive Wars, Shyahtan?"
    SHYAHTAN "Those of us who survived could never forget, Hive Lord."
    SHYAHTAN "{i}Do {b}you{/b} remember, Hive Lord, how we fought side by side to exterminate the rogue hive?{/i}"
    "The Hive Lord didn't answer."
    "With a heavy sigh, he turned fully to face me."
    HIVE_LORD "I have someone I wish for you to meet."
    HIVE_LORD "A new strain I have helped develop."
    HIVE_LORD "I hope you will adopt him under your clan's banners for now."
    "The Hive Lord turned to his personal guard."
    HIVE_LORD "Bring in Eight-Six-One."
    SHYAHTAN "One of your pet projects?"
    HIVE_LORD "{i}Something like that.{/i}"
    scene cg_para_ship_hive_lord_anim at blurin(HowLong = 1.5) with dissolve
    show cg_markus_tf_young at left with easeinleft:
        yoffset 100
    "As the fleshy spiral doors opened, a skinny, pale-white Terran approached."
    stop music fadeout 1.0
    play ambience2 "audio/ambience_scenes/obelisks.ogg" fadein 1.0    
    EIGHT_SIX_ONE "...G-Greetings, Lord Shyahtan."
    MARKUS "WAKE UP!"
    SHYAHTAN "A white strain?"
    SHYAHTAN "What is he-"
    "I felt the claws of the Hive Lord rest on my shoulder."
    HIVE_LORD "I will watch his performance with great interest, Lord Shyahtan."
    "The skinny Terran offered a nervous, curt bow."
    show cg_markus_tf_young at center with ease:
        yoffset 100
    EIGHT_SIX_ONE "I am... at your s-service, my lord."
    stop ambience fadeout 1.0
    scene black with dissolve
    $ Pause(0.5)

    jump qst_TheBeastOfNovaras_FlashbackOverCaltrackFinish


label qst_TheBeastOfNovaras_FlashbackOverCaltrackFinish:
    $ AutoAmb(False)
    $ AutoMus(False)
    stop ambience2 fadeout 1.0
    $ Pause(1.0)
    $ AutoTimeFreeze(False)
    $ LocNameSetTemp(_("Hamun arena"))
    MARKUS "[player_name!t]!"
    play sound2 "audio/cfx/crowd_panic_2.ogg" fadein 1.0
    $ PlayMusic("audio/music/16_Parasite_A.ogg")
    MARKUS "You have to... Ahh! WAKE UP!"
    scene cg_caltrack_crowd_attack with dissolve
    "My eyes peeled open as I stared out at the carnage before me."
    "The arena was drenched in blood as the Caltrack flailed; bodies and torn limbs littered the ground as people screamed."
    "Even Sypha, usually smug and composed, was barking orders."
    "Staggering, bleeding, forcing the others to keep moving and fight."
    "Now, with the Caltrack's eyes fixed on her, Sypha's pupils widened; for the first time, I saw fear in her face."
    "Any moment, it would come crashing down on her and her exhausted body wouldn't move in time..."
    "{i}...But something moved inside me now.{/i}"
    "I felt my whole body act on its own, rising as a hot surge of energy flooded through me."
    "{i}What was going on?{/i}"
    scene cg_caltrack_battle_post_1 with dissolve
    "Moments ago, I was dying, and now..."
    "I sprang forward. Faster than before."
    "Faster than I'd ever moved."
    play sound "audio/battle/battle_chars/caltrack/attack_1.ogg"
    "With a single motion, I swept Sypha from the sand and yanked her clear of the snapping jaws."
    "She stared up at me, shock and disbelief warring in her eyes."
    "I set her down gently and turned back to the Caltrack."
    "It snapped one of its many jaws toward me."
    "A quick pivot carried me past it."
    scene cg_caltrack_battle_post_2 with dissolve
    "A tentacle latched on and punched through the creature's cheek as I flung myself into the air, crashing down onto one of its heads and driving my claws through its eye."
    play sound "audio/cfx/demorai_roar_high1.ogg"
    "The beast bellowed, thrashing, a shriek so sharp the crowd clamped hands over ears."
    "{i}I wasn't controlling my limbs.{/i}"
    "{i}I didn't even know I *could* move like this.{/i}"
    "{i}What was happening?{/i}"
    "I slid and rolled down, claws grinding through jelly and bone, carving the socket wide."
    "{i}Were my claws sharper?{/i}"
    "{i}My muscles stronger?{/i}"
    "Landing, I dragged my talons in a clean arc, severing the throat of one Caltrack head."
    "It staggered back, one head limp, the others panicking."
    play sound "audio/cfx/demorai_roar_high2.ogg"
    scene cg_caltrack_death_blow with dissolve
    "In a last, desperate lunge, it charged."
    "I moved like lightning, {i}no{/i}, like something beyond it, hurling myself with my tentacles, a straight shot that punched clean through the Caltrack's chest and burst out its spine, leaving a gaping hole in my wake."
    "It's heads swayed in the air for a few moments, as though the creature itself was trying to understand what had just happened to it."
    play sound2 "audio/cfx/transform.ogg"
    scene cg_caltrack_battle_post_3 with flash
    "The creature tumbled lifelessly forward, smashing its heads against the wall, twitching in final spasms."
    "The crowds stared in stunned silence."
    "What had they just witnessed?"
    "A monster that could fell armies not merely defeated but {i}eviscerated{/i}."
    "Destroyed by a perfect predator."
    "{i}A god of the arena.{/i}"
    "My arms lifted on their own, and a voice thundered that wasn't mine."
    scene cg_caltrack_battle_post_4 with flash
    SHYAHTAN "I AM SHYAHTAN! LORD OF A THOUSAND STARS, UNBOWED AND UNBROKED! BRING ME YOUR KINGS OF MEN AND PETTY GODS SO THEY MAY TREMBLE BEFORE ME!"
    "The crowd was silent at first. Stunned."
    "Then, a single fist rose, a single voice cheered..."
    "And the stadium erupted."
    play sound "audio/cfx/crowd_cheer.ogg"
    scene cg_caltrack_battle_post_5 with dissolve
    $ Pause()
    "SHYAHTAN! SHYAHTAN! SHYAHTAN!"
    scene cg_caltrack_battle_post_6 with dissolve
    $ Pause()
    "As I looked to the stands, I caught Celeste."
    "Enthralled, leaning forward, her eyes wide as her hands clenched the fabric of her chair."
    "Flushed, lips parted, an excited breath escaped her."
    "Sypha and the others hurried toward me; most wore pain and worry."
    "Only Sypha smirked."
    KIARA @sad "[player_name!t], are you..."
    "And just like that, the power snapped out of me as control returned."
    scene black with dissolve
    $ TransformMC(False)
    $ TransformKiara(False)
    $ TransformMarkus(False)
    play sound "audio/cfx/body_fall_ground.ogg"
    "My legs gave way; I collapsed to the sand, the world blurring."
    "Figures gathered, voices muffled, my name swallowed by the roar. Then darkness."
    stop music fadeout 5.0
    "...In that darkness, I hear a familiar voice call to me."
    $ PlayMusic("audio/music/52_Mystery_Theme.ogg")
    REGINA "...Poor, sweet baby."
    $ Pause(1.0)
    scene cg_mc_room_space with dissolve
    $ LocNameSetTemp(_("Home?"))
    $ AutoAmb(False)
    stop ambience fadeout 1.0
    "My eyes open, and I find myself back home in my bedroom, the fire lit as I look around."
    "Outside the window I see... {i}stars.{/i}"
    "A deep black ocean of night sky and vibrant stars drifting by."
    REGINA "You're growing stronger."
    $ CharSetClothes("regina", "witch")
    show regina at center with dissolve
    "My eyes lock onto [regina_ref!t], emerging from a shadow in the corner."
    MC @angry "You...!"
    MC @angry "What do you want from me?"
    REGINA @talk "I sensed something awakening within you."
    REGINA @sad "I was worried, I—"
    MC @angry "Spare me your worry."
    MC @angry "I don't want it."
    REGINA @sad "{i}*Sigh*{/i}"
    REGINA @sad "How many times must I apologize?"
    MC @angry "This isn't about a few coins I left lying around!"
    MC @sad "You spent my and Erika's whole lives lying about {i}who{/i} you are."
    MC @sad "About {i}what{/i} you are."
    REGINA @sad "I have spent most of my life on the run."
    REGINA @sad "I wanted to tell you both. I did."
    REGINA @sad "You have to understand—their lies run deep."
    REGINA @sad "{i}I was a weapon, a soldier, a—{/i}"
    "[regina_ref!t] looks away, biting her lip."
    REGINA @sad "It doesn't matter now."
    REGINA @sad "I'm here for you."
    REGINA @sad "I've always been here for you, and I'm here for you now."
    MC @talk "...Where even are we?"
    REGINA @talk "A dream world."
    REGINA @talk "A place for us to speak."
    MC @serious "Tell me everything."
    REGINA @sad "Wait."
    MC @talk "What are you—"
    "[regina_ref!t] steps forward and wraps her arms around me."
    "Dream or not, the same warmth; the same scent; the same touch..."
    MC "..."
    REGINA "I've been so worried about you."
    MC "[regina_ref!t], I—"
    "She pulls back, concern flickering across her face—then something more controlled."
    REGINA @talk "Do you feel it?"
    REGINA @talk "{i}The thing inside you gnawing, feeding on your strength?{/i}"
    MC "[regina_ref!t], I-"
    "Her breathing trembles slightly in anticipation, as her face a mixture of concern and sultry need."
    REGINA @talk "Do I..."
    $ PlayMusicRandom("mus_sex")
    show regina at nod
    "She reached to gently undo her clothes."
    REGINA @talk "{i}Need to take care of you again?{/i}"       
    menu:
        "I... Maybe?":
            REGINA @smile "Shhh... I know without this you'll become unwell."
            MC @talk "You... know?"
            $ CharSetClothes("regina", "naked")
            show regina at blurin, nod
            $ PlaySoundRandom("tentFlap")
            "Slowly, and sensually, [regina_ref!t] dropped her clothes to the floor."
            "Stood naked before me, the scent of her body alone stiffening my cock in excitement."
            REGINA @talk "I can sense whatever's in you feeding on you from the inside."
            "Slowly, [regina_ref!t] stepped closer towards me."
            "With a snap of her fingers, I was stripped naked in a moment."
            MC @surprised "How did you-"
            REGINA @smile "It's a dream, dear."
            REGINA @smile "{i}My dream.{/i}"
            "Running her hands down my body, gently, she kisses at my chest, trailing her lips down as I sigh with relief from the tender touch."
            "Before she can kiss my most private part, she pulled away briefly."
            REGINA @smile "{i}We don't have time for the full event, sweetheart.{/i}"
            MC @surprised "Then... What are we-"
            "Laying down on my bed, she smiles and lures me over enticingly."
            REGINA "Lie down, sweetheart. Press yourself against me. Feel how much I want you— even if I can't give you all of me right now."
            MC @surprised "You-"
            REGINA "No more thinking, dear."
            REGINA "Just do it."
            scene regina_dream_buttjob_idle with dissolve
            $ Pause()
            "A part of me wants to protest, perhaps, {i}because I knew what we were doing was so terribly wrong.{/i}"
            "Or, perhaps, in the darkest pits of my mind, it was because I had hoped we would go even further..."
            "Still, I moved behind [regina_ref!t], pressing my cock between the soft cheeks of her round, incredible ass."
            scene regina_dream_buttjob_slow with dissolve
            $ Pause()
            "She looked back towards me, smiling as she felt my hands squeeze at her ass as my cock slowly grinded against her."
            REGINA "See? Isn't that better?"
            MC "Ahhh... [regina_ref!t]."
            MC "F-Fuck...!"
            REGINA "Haha... Feels that good, hmm?"
            "She was right of course, it {i}did{/i} feel that good, but there was something terribly wrong with admitting it out loud right now."
            "With a short playfully smile, she wiggled her ass slightly and continued to watch bemused."
            MC "Are you - {i}*Huff*{/i} enjoying this?"
            REGINA "Watching my big, strong man shove his cock between my ass and use me?"
            "I almost felt embarrassed hearing those kind of words slip from her mouth, but where my mind went in one direction, my body happily agreed as I moved faster."
            $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
            scene regina_dream_buttjob_fast with dissolve
            $ Pause()
            REGINA "Don't be so... Mhmm... Shy, dear."
            REGINA "I promised I would - Ahh! Take care of all your needs."
            MC "But we shouldn't-"
            REGINA "Shhh..."
            REGINA "Just remember dear."
            REGINA "{i}I want this too...{/i}"
            "I grunted, grinding and slapping my cock against her ass which wrapped perfectly around me."
            MC "{i}*Huff*{/i} Such a...{i}*Huff*{/i}"
            MC "{i}Meaty ass.{/i}"
            "[regina_ref!t] chuckled, her skin glistening in the strange light as I felt the hot, budding need to release becoming tighter, more intense by the minute."
            REGINA "{i}And it's all yours.{/i}"
            REGINA "{b}Whenever you want it.{/b}"
            "I grunted, letting myself become possessed as I continued to slam my hips against her."
            "The urge to just put my cock inside of her, to pass that line was almost overwhelming."
            "Still though, [regina_ref!t] continued to watch me, waiting patiently for me to finish with an almost curious look on her face."
            MC "[regina_ref!t]... I'm-"
            REGINA "Don't ask."
            REGINA "{i}Just do it, dear.{/i}"
            REGINA "Just-"
            $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
            scene regina_dream_buttjob_finish with flash
            $ ReduceInfectionFromSex("regina")
            $ UnlockGalSceneAndGrantXp("regina", "dream_buttjob")
            $ Pause()
            MC "H-HRGHHHH!!"
            "My whole body tightened and coiled as my cock throbbed,"
            "[regina_ref!t] gasped as she felt the hot splash of seed on her back and ass,"
            "But as the initial surprise passed, she giggled softly."
            REGINA "Well done... dear."
            "Her eyes wandered over my body for a moment, perhaps as {i}she{/i} contemplated crossing even more lines herself."
            "Reluctantly, she pulled her eyes away."
            REGINA "Let's get some clothes on,"
            REGINA "Before {i}I{/i} become the one who gets distracted..."
            scene black with dissolve
            $ PlaySoundRandom("tentFlap")
            $ Pause(1.0)
            $ CharSetClothes("regina", "witch")
            scene cg_mc_room_space
            show regina at center
            with dissolve

        "There's no time for that, I want answers!":
            "If a little disappointed, [regina_ref!t] stopped removing her clothes."
            stop music
            play sound "audio/cfx/scratch_stop.ogg"
            REGINA @sad "If... that is your wish."
            REGINA @talk "Ask. I'll tell you what I can."

    $ PlayMusic("audio/music/52_Mystery_Theme.ogg")
    $ tmpvar = ["a", "b"]
    label qst_TheBeastOfNovaras_FlashbackOverCaltrackFinish_reginatalkmenu:
    if len(tmpvar) > 0:
        menu:
            "Where are you?" if "a" in tmpvar:
                $ tmpvar.remove("a")
                REGINA @talk "Somewhere safe."
                REGINA @talk "The Inquisition hunts me now. I must be careful."
                REGINA @talk "Leave it at that... for now."
                jump qst_TheBeastOfNovaras_FlashbackOverCaltrackFinish_reginatalkmenu
            "How is everyone?" if "b" in tmpvar:
                $ tmpvar.remove("b")
                REGINA @talk "Depends who you mean."
                REGINA @sad "Erika is still under interrogation."
                REGINA @sad "They're convinced she must have known something about you."
                MC @sad "Can't you do something?"
                REGINA @think "I'm powerful... {i}not 'fight the entire Inquisition alone' powerful.{/i}"
                if "myu" in QstJudgementDay().ImprisonedCharacters:
                    REGINA @sad "As for your friend, the slimelark, Myu—"
                    REGINA @talk "She's also held captive. There's debate about what to do with her."
                if "elena" in QstJudgementDay().ImprisonedCharacters:
                    REGINA @sad "The wolf-girl, Elena."
                    REGINA @think "Last I heard, Inquisitor Marion was interrogating her personally."
                    REGINA @talk "That's all I know."
                if QstTheComingStorm().GaveAdaraMoneyForEscape:
                    REGINA @sad "Adara is... as well as can be."
                    REGINA @talk "Her work in the castle has introduced her to powerful figures."
                    REGINA @talk "When she can, she pleads your and Markus' case."
                else:
                    REGINA @sad "Adara... hasn't accepted her father's passing."
                    REGINA @sad "She's angry, but..."
                    REGINA @sad "I believe she misses you, no matter what she says."
                REGINA @talk "Captain Nyx is still under arrest. Likely to be released soon."
                REGINA @talk "But she's made powerful enemies for helping you."
                REGINA @talk "Sister Divine keeps her head down."
                if CharIsLover("divine"):
                    REGINA @think "There are... uncomfortable questions about your relationship."
                    REGINA @talk "For now, they're calling it you {i}seducing{/i} her—and blaming her 'condition'."
                REGINA @talk "As for anyone else... I don't know."
                REGINA @talk "Even my eyes can only see so much."
                jump qst_TheBeastOfNovaras_FlashbackOverCaltrackFinish_reginatalkmenu
            "What's happened since the battle?":
                pass
    else:
        MC "What's happened since the battle?"
    $ tmpvar = {}
    REGINA @talk "After you fell unconscious, I fled before the Inquisition arrived."
    REGINA @talk "A joint relief force from Angmurus and Newyark pushed back the Demorai."
    REGINA @talk "Once Prince Naran was secured, The Silver Knight rallied what remained and cleared the city."
    MC @think "Zanarak... Is he..."
    REGINA @think "Dead?"
    REGINA @think "No."
    MC @surprised "But... that light..."
    REGINA @think "A lucky strike that caught him off guard."
    REGINA @think "He's arrogant. He toys with victims before the kill."
    REGINA @think "{i}He will not forgive this wound to his pride.{/i}"
    MC @think "What happened after he fell? Did he flee?"
    REGINA @think "Not quite..."
    "[regina_ref!t] pauses, choosing her words."
    MC @think "What is it?"
    REGINA @think "He was enraged. I was sure he'd strike again."
    REGINA @talk "{i}But something stopped him.{/i}"
    REGINA @talk "Like an invisible hand plucking him from the sky."
    REGINA @talk "A blink later he was a black dot, and then gone."
    MC @think "Maybe the relief force scared him off?"
    REGINA @think "Perhaps..."
    REGINA @talk "But I doubt such a thing frightens a monster like him."
    MC @think "Then why...?"
    REGINA @think "I do not know."
    REGINA @think "But if his master is who I think..."
    REGINA @think "{i}We may have caught his eye.{/i}"
    REGINA @think "{b}Or perhaps he has always been watching us already...{/b}"
    MC @talk "{i}His master?{/i}"
    MC @think "You mean..."
    MC @think "{b}Malakai?{/b}"
    REGINA @angry "DON'T SPEAK HIS NAME!"
    REGINA @think "Especially here. The Lord of Shadows' reach is far."
    MC @surprised "Why would he care about me?"
    REGINA @think "I don't know."
    REGINA @think "But be careful, [player_name!t]."
    REGINA @sad "If the Lord of Lies is watching, {i}you are in grave danger.{/i}"
    MC @sad "I've been in danger since I joined the scouts."
    REGINA @sad "[player_name!t]... when you're a pawn in the games of gods, they rarely think twice before brushing you from the board."
    play sound "audio/cfx/earthquake.ogg"
    "The room shudders. The floor vibrates under my feet."
    MC @surprised "What's happening?"
    REGINA @talk "Ahh... our time ends."
    play sound2 "audio/cfx/wood_crack.ogg"
    "Cracks spider across the walls."
    MC @surprised "[regina_ref!t]!"
    REGINA @sad "Go now. Remember my words and GO!"
    scene cg_mc_room_space_fall with dissolve
    play sound "audio/cfx/wood_crack.ogg" volume 0.25
    play sound2 "audio/cfx/wooden_floor_shatters.ogg"
    "The floor gave way."
    "I plunged into darkness."
    "I reached out, crying her name as [regina_ref!t] receded."
    "Smaller, and smaller... until nothing remained but the void."
    "Her voice lingered as the world unraveled: {i}be safe...[player_name!t]{/i}"
    scene black with dissolve
    $ Pause(0.5)
    jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle

label qst_TheBeastOfNovaras_WakeUpInTavernPostBattle:
    $ InfGainDaily(False)
    $ tmpvar = 2
    while tmpvar > 0:
        $ TimeAdvBy(TIME_1H * 12)
        $ TimeAdvBy(TIME_1H * 12)
        $ TimeAdvTo(TIME_NOON)
        $ HealParty(Silent = True)
        $ tmpvar -= 1
    $ InfGainDaily(True)
    $ AutoMus(True)
    $ LocSet("hamun_hookah_bar_room")
    $ LocNameReset()
    $ LocFlush()
    show sypha at cleft
    with dissolve
    $ CharSetClothes("mc", "pants")
    show mc at cright_f with easeinright
    MC @surprised "...!"
    SYPHA @talk "Easy now, easy!"
    "My eyes darted around the room as Sypha moved closer, her hands resting on my shoulder and chest."
    SYPHA @happy "Calm now... You're safe."
    MC @surprised "What happened?"
    MC @surprised "Is everyone-"
    SYPHA @talk "Your friends are fine, if a little bruised up."
    SYPHA @talk "Once the battle was over, guards and healers rushed the arena to help tend to the wounded."
    "Sypha fluttered her eyes coyly as she smirked."
    SYPHA @happy "{i}It seems all of Hamun seems to have the name {i}Shyahtan{/i} on its lips...{/i}"
    $ tmpvar = ["a", "b", "c"]
    label qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_syphatalkmenu:
    if len(tmpvar) > 0:
        menu:
            "How did I end up here?" if "a" in tmpvar:
                $ tmpvar.remove("a")
                SYPHA @happy "After one of the doctors looked you over, I helped carry you here to rest."
                SYPHA @think "The arena has become a circus trying to deal with the bloodbath and damage caused."
                SYPHA @talk "I thought it best to try keep you away from all that."
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_syphatalkmenu
            "How long was I out?" if "b" in tmpvar:
                $ tmpvar.remove("b")
                SYPHA @talk "Two days."
                MC @surprised "TWO DAYS?!"
                SYPHA @talk "Your wounds were grievous, and I believe whatever you did to kill that thing pushed your body well beyond its limits."
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_syphatalkmenu
            "How many are dead?" if "c" in tmpvar:
                $ tmpvar.remove("c")
                SYPHA @think "Hmm?"
                SYPHA @think "A hundred or two at least."
                SYPHA @think "{i}Why do you care?{/i}"
                MC @angry "They were still people, Sypha!"
                SYPHA @talk "... And?"
                SYPHA @talk "They were not {i}your{/i} people, they were simply spectators who would have cheered if you lived or died."
                SYPHA @talk "Don't trouble yourself with such things."
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_syphatalkmenu
            "What... What exactly happened?":
                pass
    else:
        MC "What... What exactly happened?"
    $ tmpvar = {}
    
    SYPHA @happy "It's me who should ask {i}you{/i} that."
    SYPHA @think "Who exactly {i}is{/i} Shyahtan?"
    MC @sad "He's... the dark passenger."
    SYPHA @think "The what?"
    MC @serious "The thing attached to me."
    MC @serious "The thing that lets me change into that monster."
    SYPHA @think "And it speaks to you?"
    MC @sad "... Yes."
    SYPHA @happy "... {i}Fascinating!{/i}"
    SYPHA @happy "I had no idea your powers were actually sentient!"
    "There was a brief pause as Sypha seemed to ponder the meaning of it all."
    SYPHA @think "And you can't remember killing the caltrack?"
    MC @sad "It's like... {i}A dream within a dream.{/i}"
    MC @sad "But I remember something else."
    MC @surprised "{i}A memory that belonged to Shyahtan.{/i}"
    SYPHA @happy "Really?"
    SHYAHTAN "Yes."
    SYPHA @shock "What did you just say?"
    "Like a black sludge, the creature inside of me slowly emerged from my chest."
    "Sypha, slightly taken aback, pulled away for a moment as the creature, or rather, Shyahtan, spoke."
    SHYAHTAN "Forcing this body into a state of overdrive... it has pulled fragments loose."
    SHYAHTAN "I was blade and fire once."
    SHYAHTAN "Now, shards gnaw at me."
    SHYAHTAN "Hunger not for flesh, but for memory."
    SHYAHTAN "{i}It is weakness... and yet I cannot turn away.{/i}"
    MC @think "Isn't the fact you're beginning to remember a good thing?"
    SHYAHTAN "Good? It corrodes focus. I feel incomplete..."
    SHYAHTAN "Like broken glass."
    SHYAHTAN "Hold up a shard, and I glimpse myself."
    SHYAHTAN "But never whole."
    "Sypha's expression changed from shock to a strangely delighted smile."
    SYPHA @happy "Shyahtan..."
    SYPHA @happy "It's a pleasure to meet you."
    "The black sludge face weaved its way around examining Sypha who stood patiently still."
    SHYAHTAN "{i}... Your scent is strangely familiar.{/i}"
    SHYAHTAN "Yet I cannot recall who you are..."
    SHYAHTAN "Have we met?"
    SYPHA @think "No?"
    SYPHA @talk "The first time I saw you was in the temple of Niltakar."
    SHYAHTAN "{i}... Curious.{/i}"
    SHYAHTAN "Your heart rate is unusually calm at my appearance."
    SYPHA @happy "{i}What have I to fear when we're cut from the same cloth?{/i}"
    SHYAHTAN "How so? You are not Terran."
    SYPHA @happy "But we are {i}both{/i} children of the same god."
    SYPHA @happy "Children of Malakai, oh great old one."
    MC @angry "What in the hells are you talking about now?"
    MC @angry "Why do you invoke the lord of lies' name?"
    SYPHA @think "Lord of lies?"
    SYPHA @think "You mean..."
    SYPHA @happy "{i}The great savior?{/i}"
    MC @angry "Savior? Are you mad? HIS WAR DOOMED US ALL!"
    SHYAHTAN "Do you possess knowledge of my past?"
    SHYAHTAN "... I want to know more."
    "Sypha shrugged."
    SYPHA @talk "I have only heard stories."
    SYPHA @talk "Before the savior chose to save our people..."
    SYPHA @talk "He birthed the {i}star children{/i} in fire and shadow, so the realms would kneel."
    SYPHA @talk "Legends foretell that one of the star children will return, crowned in blood, to guide us back to Him."
    MC @angry "True path? Star children? What is all this madness?"
    show mc at shake
    MC @angry "{i}NO MORE SECRETS DAMN IT!{/i}"
    SYPHA @angry "..."
    MC @angry "If you expect me to trust you, I want to know what else you're hiding!"
    "Sypha folded her arms, her eyes narrowing on me."
    SYPHA @angry "I don't have to tell you anything."
    SYPHA @angry "{i}Need I remind you we are at war?{/i}"
    SYPHA @angry "Make no mistake, this alliance of ours is for convenience and nothing more... {i}'husband.'{/i}"
    "Sypha made her way towards the door."
    MC @angry "So what, you just expect me to play along and stay in the dark while you move pawns from the shadows?"
    "Her hand lingered on the doorframe, just long enough for me to notice the tremor in her fingers. When she spoke, her voice was velvet and steel at once."
    SYPHA @happy "{i}... Thank you for saving my life the other day.{/i}"
    SYPHA @angry "Now please."
    SYPHA @angry "{i}Trust me, and let me fucking save yours.{/i}"
    show sypha at blurin, cleft_f
    $ Pause(0.25)
    hide sypha with easeoutleft
    "With a loud thud, Sypha slammed the door shut."
    $ PlaySoundRandom("woodenDoor")
    play sound2 "audio/cfx/door_lock.ogg"
    show mc at center_f with ease
    SHYAHTAN "... A fine mate she shall make."
    $ tmpvar = ["a", "b", "c", "d"]
    label qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_shyahtantalkmenu:
    if len(tmpvar) > 0:
        menu:
            "You seemed so... {i}different{/i} in the memory." if "a" in tmpvar:
                $ tmpvar.remove("a")
                SHYAHTAN "I {i}was{/i} different."
                SHYAHTAN "I saw banners burning beneath twin suns. Screams. Concubines without faces. A child's hand reaching... then nothing."
                SHYAHTAN "Fragments. Nothing whole."
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_shyahtantalkmenu
            "Do you remember anything else other than what we saw?" if "b" in tmpvar:
                $ tmpvar.remove("b")
                SHYAHTAN "Flashes. Wars on nameless worlds."
                SHYAHTAN "Blood rivers, screams in alien tongues."
                SHYAHTAN "I do not like these feelings. They are heavy... illogical. Painful."
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_shyahtantalkmenu
            "Do you remember much of your people?" if "c" in tmpvar:
                $ tmpvar.remove("c")
                SHYAHTAN "Pieces. Wars beneath strange skies. Feasts after slaughter. Concubines by the hundred, nameless, blurred."
                SHYAHTAN "There is more. Locked away. Waiting."
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_shyahtantalkmenu
            "Where are your people now? How did you end up... here?" if "d" in tmpvar:
                $ tmpvar.remove("d")
                SHYAHTAN "I do not know."
                SHYAHTAN "Out there still, among the stars."
                SHYAHTAN "{i}I have no idea how I ended up on this world...{/i}"
                jump qst_TheBeastOfNovaras_WakeUpInTavernPostBattle_shyahtantalkmenu
            "That... Terran at the end of the dream... {i}didn't it kind of look like Markus?{/i}":
                pass
    else:
        MC "That... Terran at the end of the dream... {i}didn't it kind of look like Markus?{/i}"
    $ tmpvar = {}

    SHYAHTAN "Yes... And we must not let it know."
    MC @think "What, why?"
    SHYAHTAN "I have the faintest memory that only the most dangerous and unstable genes of my species were placed into stasis."
    SHYAHTAN "{i}The ferals.{/i}"
    MC @think "Ferals? You mean... What we'll turn into if we don't... uhhh... {i}mate?{/i}"
    SHYAHTAN "Correct."
    SHYAHTAN "If he and I were placed into stasis, best to keep this knowledge secret until we know more."
    MC @angry "Markus would never betray me."
    SHYAHTAN "{i}It is not Markus that concerns me...{/i}"
    "I paused for a moment, the next question uncomfortable, difficult to form the words for."
    MC @talk "... About what Sypha said."
    MC @serious "{i}About Malakai.{/i}"
    MC @serious "What did she mean by that?"
    SHYAHTAN "I do not know. My race serves no god. There is only the hive."
    MC @sad "Then what now... Where do we go from here?"
    SHYAHTAN "The past has no bearing on the present."
    SHYAHTAN "The Demorai still invade, with or without my memories intact."
    SHYAHTAN "Let us find this Yarrick. It is time for him to fulfill his end of the bargain."
    scene black with dissolve
    $ Pause(0.5)
    $ CharSetClothes("mc", "normal")
    $ PlaySoundRandom("tentFlap")
    $ AutoMus(True)
    $ AutoAmb(True)
    $ QstSetProgress(QstTheBeastOfNovaras, 5)
    $ TransformMarkus(False)
    $ TransformMC(False)
    $ LocEnter()

label qst_TheBeastOfNovaras_ReturnToYarrickAfterCaltrack:
    show yarrick at cright_f
    with dissolve
    show mc at cleft with easeinleft
    YARRICK @smile "Ahhh! The hero of Hamun returns!"
    MC @smile "{i}Hero of Hamun?{/i} Wasn't I {i}The beast of Novaras{/i} just a few days ago?"
    YARRICK @smile "Times change. Today, beast or hero, it doesn't matter."
    YARRICK @smile "What matters is they're all watching you now."
    YARRICK @smile "I hear there's even a new bard song about the great Shyahtan."
    MC @sad "R-Right..."
    MC @sad "Shyahtan you say?"
    YARRICK @think "A strange stage name, but..."
    YARRICK @smile "It's memorable. Better than the thousand self-titled buffoons with paragraph-long names."
    $ tmpvar = ["a"]
    label qst_TheBeastOfNovaras_ReturnToYarrickAfterCaltrack_yarrickreturntalk:
    if len(tmpvar) > 0:
        menu:
            "Did you not get in trouble for what happened with the Caltrack?" if "a" in tmpvar:
                $ tmpvar.remove("a")
                YARRICK @talk "W-Well..."
                YARRICK @talk "Some of the coin I had earned was..."
                YARRICK @sad "{i}Confiscated.{/i}"
                YARRICK @talk "But it wasn't my fault the Caltrack caused such carnage!"
                YARRICK @talk "I told them what I wanted to bring and they assured me the arena was capable of containing such a beast."
                YARRICK @sad "...It seems though, they didn't anticipate the Caltrack being quite so large."
                jump qst_TheBeastOfNovaras_ReturnToYarrickAfterCaltrack_yarrickreturntalk
            "I lived up to my end of the deal, now it's time for you to fulfill yours.":
                pass
    else:
        MC "I lived up to my end of the deal, now it's time for you to fulfill yours."

    YARRICK @talk "Lord Zanzibat has {i}already{/i} sent word he wishes to become your patron."
    MC @surprised "Really?"
    YARRICK @smile "After that performance, I don't think there's a merchant in the city who wouldn't consider it."
    MC @talk "Can you arrange a meeting for me?"
    YARRICK @smile "Of course!"
    YARRICK @talk "Lord Zanzibat's home can be found outside the Great Palace."
    YARRICK @talk "It's the great building to the left, with the huge dome on its rooftop... It cannot be missed."
    YARRICK @talk "Be warned... Lord Zanzibat is renowned for his cunning and trickery."
    YARRICK @talk "Even those bastards at the Greater Trading Company tread carefully around him."
    MC @serious "Thanks for the advice."
    hide yarrick with dissolve
    show mc at center with ease
    MC "(I should head to meet this Lord Zanzibat as soon as possible.)"
    $ QstStart(HouseLockZanzibatHouse)
    $ QstSetProgress(QstTheBeastOfNovaras, 6)
    $ LocEnter()

label qst_TheBeastOfNovaras_ZanzibatHouse_returnatday:
    MC "(Not at night.)"
    $ LocEnterQ()


label qst_TheBeastOfNovaras_ZanzibatHouse:
    show cg_guard_hamun as g1 at left with easeinleft
    show cg_guard_hamun as g2 at right_f with easeinright
    "As I arrived upon the great entranceway to Lord Zanzibat's home, two guards approached."
    GUARD "What business have you here?"
    show yarrick at cright_f with easeinright
    YARRICK @smile "Ahh, I'm just in time."
    YARRICK @smile "Your master has business here with my client."
    "The guard looked me up and down."
    GUARD "And what business is that?"
    YARRICK @angry "You're speaking to the savior of Hamun, the beast of Novaras himself boy!"
    YARRICK @angry "Do you wish to explain to your master how you turned away such an esteemed guest?"
    hide g2 with dissolve
    GUARD "... I shall check with Lord Zanzibat."
    GUARD "Wait here a moment."
    hide g1 with dissolve
    YARRICK @smile "Well, that went better than expected."
    show mc at cleft with easeinleft
    MC @think "Why wouldn't it?"
    YARRICK @think "Lord Zanzibat is... fickle." 
    YARRICK @think "Many a merchant has tried to meet him only for him to keep changing the time and date."
    YARRICK @think "{i}I believe he finds it amusing to see the lengths people will go to speak to him.{/i}"
    show mc at left
    show yarrick at blurin, center
    with ease
    show cg_guard_hamun at right_f with easeinright

    GUARD "Lord Zanzibat is ready to receive you."
    "As Yarrick stepped forward, the guard blocked his path."
    GUARD "Not you."
    GUARD "{i}Him.{/i}"
    "A disgruntled Yarrick took a step back, flashing me an awkward smile."
    show yarrick at blurin, center_f
    YARRICK @smile "I shall see you around I hope?"
    YARRICK @smile "Consider us even now."
    show cg_guard_hamun at blurin, right
    hide cg_guard_hamun with easeoutright
    show mc at nod
    $ Pause(0.5)
    hide mc with easeoutright
    "I nodded lightly, before following the guard."
    show yarrick at blurin, center
    $ Pause(0.5)
    scene black with dissolve
    $ LocSet("hamun_zanzibat_house")
    $ Pause(0.5)
    $ LocFlush(dissolve)
    show mc at center with easeinleft
    "Lord Zanzibat's home was unexpected. Ornate, and yet, plants, trees... A flowing stream of water through the centre."
    "It was more like standing inside a garden in the middle of the desert than it was a home."
    "As I heard the clap of hands, I turned towards Lord Zanzibat."
    show mc at blurin, cright_f with ease
    show zanzibat at cleft with easeinleft
    "Lord Zanzibat was not a towering figure, rather he was skinny, almost effeminate."
    ZANZIBAT @smile "I had many of them imported from Sylvania."
    ZANZIBAT @smile "It cost me a fortune of course, but..."
    ZANZIBAT @smile "I find they bring me great comfort."
    MC @talk "Lord Zanzibat."
    show mc at nod
    "I gave a curtly bow."
    MC @talk "You honour me with this meeting."
    ZANZIBAT @talk "Well, how could I resist a chance to meet the saviour of Novaras?"
    ZANZIBAT @talk "And especially after that arena performance..."
    MC @smile "It was a little closer than I would have liked."
    ZANZIBAT @smile "Mmm... I did think for a moment your blood might spill on the sands."
    ZANZIBAT @smile "But that rage at the end... It was..."
    ZANZIBAT @smile "Spectacular."
    "That rage... That blinding hot rage where my body moved without me, where the dark passenger – Shyahtan or whatever his name was, took full control."
    "I couldn't help but feel... Uncomfortable by the thought."
    MC @talk "... I've come here to ask something of you."
    ZANZIBAT @smile "Oh, this is a first."
    ZANZIBAT @talk "Normally, I make the offer and let you think on it."
    ZANZIBAT @talk "Now you have my attention, what is it you want?"
    MC @talk "You're one of the last barriers blocking the deal between Novaras and the Greater Trading Company... I want you to let it pass."
    "Lord Zanzibat considered my words carefully as he slowly paced around the room, gently brushing his hand along one of the plants."
    ZANZIBAT @talk "Tell me... do you know why Hamun is still free?"
    MC @talk "Because no side dares try to conquer it yet?"
    ZANZIBAT @smile "In part. But the truth is simpler: Hamun sells its table to *all* sides, and takes none."
    ZANZIBAT @smile "Kings, rebels, merchants, priests, each can bargain here."
    ZANZIBAT @smile "That is our shield."
    ZANZIBAT @serious "The Greater Trading Company would break that balance."
    ZANZIBAT @serious "They are not merchants, they are parasites."
    ZANZIBAT @serious "Once they take root, they twist every throne they touch."
    ZANZIBAT @talk "Do you know the fate of the People of Wei?"
    ZANZIBAT @talk "In less than fifty years, the GTC bought their land, scattered their bloodline, and sold the survivors on the backs of Paruh beasts."
    ZANZIBAT @smile "So tell me... why should I welcome that fate here?"
    $ tmpvar = ["a", "b"]
    label qst_TheBeastOfNovaras_ZanzibatHouse_zanzitalk:
    if len(tmpvar) > 0:
        menu:
            "The deal will pass anyway, will it not?" if "a" in tmpvar:
                $ tmpvar.remove("a")
                ZANZIBAT @talk "It shall, but it's the difference between the deal passing in the next three months and the next three years."
                jump qst_TheBeastOfNovaras_ZanzibatHouse_zanzitalk
            "You seem to hate them." if "b" in tmpvar:
                $ tmpvar.remove("b")
                ZANZIBAT @talk "I have had dealings with them in the past."
                ZANZIBAT @talk "None of which have ended well... For anyone involved."
                ZANZIBAT @talk "You would do well to be parted from their 'business' as soon as you can."
                jump qst_TheBeastOfNovaras_ZanzibatHouse_zanzitalk
            "Then what would it take to persuade you?": 
                pass
    else:
        MC "Then what would it take to persuade you?"
    ZANZIBAT @talk "... Hmm."
    ZANZIBAT @talk "The shipping rights."
    MC @think "What?"
    ZANZIBAT @talk "I want them to agree to only use my ships to transport the goods from Alderay to Skarshire and vice versa."
    MC @serious "For someone so against them, you seem more than ready to jump into business with them again."
    ZANZIBAT @smile "It's as the old proverb says."
    ZANZIBAT @talk "{i}Keep your friends close, and keep your enemies even closer.{/i}"
    ZANZIBAT @talk "Tell the GTC my answer."
    $ QstSetProgress(QstTheBeastOfNovaras, 7)
    ZANZIBAT @talk "{i}I will expect the agreement in writing... and on their god.{/i}"
    scene black with dissolve
    $ LocSet("hamun_dist_merch_lord")
    $ LocEnter()


label qst_TheBeastOfNovaras_TalkToGarenBar:
    show garen at center with dissolve
    GAREN "Can I help you with something?"
    menu:
        "Lord Zanzibat has an offer he wishes to put forward with regards to the deal..." if QstGetProgress(QstTheBeastOfNovaras) == 7: 
            GAREN @think "Go on?"
            MC @talk "He will step aside and allow the deal to pass {i}if{/i} his ships are used to transport the cargo to and from Skarshire."
            GAREN @smile "... Very well, I shall arrange the papers for him."
            MC @think "Just like that?"
            MC @think "No bartering, no negotiation?"
            GAREN @smile "The desert fox has made his offer."
            GAREN @smile "I am sure he will obsess over every word of the papers I send, but within a few days at the most we will conclude our business."
            MC @talk "How can you be so sure?"
            GAREN @talk "Because despite his hatred of us, he's always more than willing to do business with us."
            GAREN @talk "It is a game to him, I believe, to see if he can outsmart us."
            MC @think "If you're just giving him everything he wants, doesn't that mean he's already won?"
            GAREN @smile "{i}Only if he can keep to his end of the bargain.{/i}"
            MC @think "What do you mean by that?"
            GAREN @talk "{i}We are bound only by the wording of our contract... Nothing more.{/i}"
            GAREN @smile "If you have a moment, I could humour you with a tale."
            menu:
                "Go ahead.":
                    GAREN @talk "There was once a lord who swore, if we armed him and filled his ranks with our mercenaries, he would crush his rival within the year."
                    GAREN @talk "Payment was guaranteed. And if not, his castle would be ours."
                    GAREN @talk "A bold deal. Too bold. Because his rival came to us with the very same request."
                    MC @surprised "Surely that's a conflict of interest?"
                    GAREN @smile "Not if the contract doesn't forbid it."
                    GAREN @talk "So we sold both sides weapons. We took both their coin. And when their coffers ran dry... we took collateral."
                    GAREN @talk "First land. Then blood. Piece by piece, both lords fed us their realms rather than admit defeat."
                    GAREN @smile "By the second year, neither could pay another coin. One was hanged in the square. The other drowned in his own bath."
                    MC @scared "... That's monstrous."
                    GAREN @think "Is it? They could have stopped. Pride kept them blind."
                    GAREN @smile "That is the true lesson: greed makes men puppets, and we hold the strings."
                    pass

                "I'm afraid I have other business to tend to.":
                    GAREN @smile "Of course, another time perhaps." 
                    pass
            
        "That will be all.":
            GAREN @talk "Until the ink meets the page then."
            $ LocEnter()

    GAREN @smile "You have done well here."
    MC @think "All this trouble... Why not just ask Lord Zanzibat yourselves?"
    MC @think "Why use me?"
    GAREN @talk "Because Lord Zanzibat only plays the {i}great game{/i} on his terms."
    GAREN @talk "He would {i}expect{/i} some kind of enticing offer to even bring him to the table."
    GAREN @talk "...And."
    "Garen's face slowly shifts into a smile without any warmth."
    GAREN @smile "The Greater Trading Company is always looking for new assets."
    GAREN @smile "{i}You are so far proving yourself a valuable asset.{/i}"
    GAREN @talk "I shall return soon after I handle Lord Zanzibat."
    MC @think "What am I to do until then?"
    GAREN @talk "Whatever you so desire."
    GAREN @talk "{i}... The GTC is pleased with your progress.{/i}"
    GAREN @talk "{i}Good work.{/i}"
    hide garen with easeoutleft
    "With a small, curtly tilt of his head towards me, Garen Quiltshire left {i}The Pale Dragon.{/i}"
    "Once more, leaving me without direction."
    "As I stood there directionless I felt the brush of a soft hand on the back of my arm."
    show sypha at center_f with dissolve
    "Sypha appeared alongside me, smiling softly."
    SYPHA @happy "You and I."
    SYPHA @happy "Tonight... we slip away."
    SYPHA @happy "{i}Just the two of us.{/i}"
    MC @think "I thought you would still be angry with me?"
    SYPHA @happy "Oh, I am."
    SYPHA @happy "But anger burns bright... and bright flames can be put to better use, don't you think?"
    MC @think "You change your mind quickly."
    "A soft, coy smile curved on her lips, eyes gleaming with something equal parts danger and desire."
    SYPHA @happy "There's a night market. Music, smoke, secrets for sale."
    SYPHA @happy "Meet me there after dark, and I'll give you what you're craving."
    MC @serious "Answers?"
    SYPHA @happy "Some answers... some temptations."
    SYPHA @happy "Enough to keep you coming back for more."
    "She brushed herself along my arm deliberately, her breath hot against my ear."
    SYPHA @perv "Don't be late... {i}dear.{/i}"
    hide sypha with easeoutleft
    MC @serious "(Well... I have some time before Garen returns.)"
    MC @serious "(I should tread careful with this Sypha, she's no doubt toying with me.)"
    MC "(If she has answers, I need them. No matter the cost.)"
    $ QstSetProgress(QstTheBeastOfNovaras, 8)
    $ LocEnter()


label qst_TheBeastOfNovaras_SyphaDate:
    show sypha at cright_f
    with dissolve
    show mc at cleft with easeinleft
    SYPHA @happy "Ahh, you've arrived!"
    SYPHA @angry "{i}And you made me wait.{/i}"
    SYPHA @angry "I {b}hate{/b} to be made to wait."
    MC @serious "I'm here now, aren't I?"
    "Sypha pouted, before wrapping her arm around mine and smiling once more."
    SYPHA @happy "Come then, show me what you humans have to offer."
    "Sypha dragged me eagerly from stall to stall, tugging at my arm whenever something shiny caught her eye."
    "She was strangely inquisitive, asking about various trinkets as though every bauble might hide some secret."
    "A particular jeweled locket caught her attention."
    SYPHA @think "What purpose does this serve?"
    MERCHANT "Ahhh! A fine choice, my lady."
    MERCHANT "That is a lovers locket."
    MERCHANT "It separates into two pieces, for each lover to wear."
    MERCHANT "Some Ramonians give expensive ones such as these to their wives alongside a dowry."
    SYPHA @think "How much?"
    MERCHANT "Normally, this would go for a few thousand at least!"
    MERCHANT "For you though, only a thousand coins!"
    "In a heartbeat, Sypha turned towards me, eyes glittering."
    SYPHA @happy "Buy it."
    SYPHA @happy "I want it."
    $ tmpvar = ["give_answers", "negotiate_barter", "negotiate_charm"]
    menu qst_TheBeastOfNovaras_SyphaDate_marketmenu:
        "When do you plan to live up to your end of the deal and actually give me some answers?" if "give_answers" in tmpvar:
            $ tmpvar.remove("give_answers")
            SYPHA @angry "Don't be a bore."
            SYPHA @angry "{i}Our{/i} time first."
            SYPHA @happy "Then you can ask your questions."
            jump qst_TheBeastOfNovaras_SyphaDate_marketmenu

        "Here." (Req_Gold = 1000) if ("negotiate_barter" in tmpvar and "negotiate_charm" in tmpvar):
            $ PlayerRemItem("gold", 1000)
            $ PlayerAddItem("lovers_locket")
            $ QstTheBeastOfNovaras().BoughtLocket = True
            "The merchant bowed, taking my coin as he handed over the locket."
            "Sypha gave half of the locket to me, smiling as she kept the other half for herself."
            SYPHA @happy "Such cute courtships you humans have."
            MC @angry "We are not {i}'courting'{/i}, Sypha."
            SYPHA @happy "{i}We'll see about that.{/i}"
            pass
    
        "Here." (Req_Gold = 600) if "pay_600" in tmpvar:
            $ PlayerRemItem("gold", 600)
            $ PlayerAddItem("lovers_locket")
            $ QstTheBeastOfNovaras().BoughtLocket = True
            "The merchant bowed, taking my coin as he handed over the locket."
            "Sypha gave half of the locket to me, smiling as she kept the other half for herself."
            SYPHA @happy "Such cute courtships you humans have."
            MC @angry "We are not {i}'courting'{/i}, Sypha."
            SYPHA @happy "{i}We'll see about that.{/i}"
            pass

        "Here." (Req_Gold = 750) if "pay_750" in tmpvar:
            $ PlayerRemItem("gold", 750)
            $ PlayerAddItem("lovers_locket")
            $ QstTheBeastOfNovaras().BoughtLocket = True
            "The merchant bowed, taking my coin as he handed over the locket."
            "Sypha gave half of the locket to me, smiling as she kept the other half for herself."
            SYPHA @happy "Such cute courtships you humans have."
            MC @angry "We are not {i}'courting'{/i}, Sypha."
            SYPHA @happy "{i}We'll see about that.{/i}"
            pass
        
        "Half of the jewels in this are sub-par quality, it's worth five-hundred at the most." (Req_Barter = 12) if "negotiate_barter" in tmpvar:
            $ tmpvar.remove("negotiate_barter")
            $ tmpvar.remove("negotiate_charm")
            $ tmpvar.append("pay_600")
            
            MERCHANT "You must be joking!"
            MERCHANT "T-These jewels are sourced from the finest gem mines in all of Ramon!"
            MC @angry "I am not a fool."
            MC @angry "Come on, Sypha, let's find a different stall-"
            MERCHANT "WAIT!"
            MERCHANT "... Six hundred, please."
            MC @talk "... Better."
            jump qst_TheBeastOfNovaras_SyphaDate_marketmenu

        "How about seven-fifty? My... {i}'fiancee'{/i} and I don't have much coin." (Req_Charm = 9) if "negotiate_charm" in tmpvar:
            $ tmpvar.remove("negotiate_charm")
            $ tmpvar.remove("negotiate_barter")
            $ tmpvar.append("pay_750")
            MERCHANT "Hmm... Young love."
            MERCHANT "Ahhh, very well!"
            MERCHANT "Seven-fifty it is."
            MC @talk "... Better."
            jump qst_TheBeastOfNovaras_SyphaDate_marketmenu

        "I don't have that kind of coin, Sypha.":
            SYPHA @sad "Hmm... A shame."
            pass

    show sypha at center_f with ease
    "Sypha reached out to grab my hand."
    SYPHA @happy "Come along, there's another stall over here that looks interesting."
    "I pulled my hand away."
    show mc at shake
    MC @serious "Hold on a moment!"
    show sypha at cright_f with ease
    SYPHA @think "Hmm?"
    MC @think "Why do you keep telling people I'm your husband and other such strangeness?"
    SYPHA @happy "Oh, {i}that?{/i}"
    SYPHA @happy "Well, it's simple."
    SYPHA @happy "I've decided to claim you. Under Demorai law, {b}you belong to me.{/b}"
    MC @think "What?"
    SYPHA @talk "I've read pieces here and there on your cultures, including how one lays claim to property."
    SYPHA @happy "{i}Therefore, you are my husband now.{/i}"
    $ tmpvar = ["a", "b"]
    label qst_TheBeastOfNovaras_SyphaDate_marketmenu2:
    if len(tmpvar) > 0:
        menu:
            "You do know I have to agree to something like that, right?" if "a" in tmpvar:
                $ tmpvar.remove("a")
                "Sypha raised a curious brow."
                SYPHA @think "I've already consented {i}for you.{/i}"
                SYPHA @happy "It is within the right of every Demorai to lay a claim on a non-Demorai should they wish."
                MC @surprised "... What in the-"
                MC @angry "That's insane!"
                SYPHA @think "I fail to see how."
                SYPHA @talk "The strong dominate the weak, as it has always been."
                jump qst_TheBeastOfNovaras_SyphaDate_marketmenu2
                
            "I don't think you fully know what a 'husband' and 'wife' actually is..." if "b" in tmpvar:
                $ tmpvar.remove("b")
                "Sypha perked up excitedly."
                SYPHA @happy "Why of course I do!"
                SYPHA @happy "I read all about your 'marriages' and I'm quite obsessed!"
                MC @think "Uhh ... Really?"
                SYPHA @happy "Yes!"
                SYPHA @smug "Forcing your conquered mate in front of not just your own family, but theirs as well to submit to you!"
                SYPHA @smug "Forcing them to wear jewelry to signify their submission to you!"
                "Sypha squirmed on the spot, visibly turned on at the idea as she crossed her legs slightly, breathing heavier."
                SYPHA @smug "And then, claiming your mate there and then in front of everyone!"
                SYPHA @mad "{i}How delightful!{/i}"
                MC @surprised "(... Is she insane?)"
                MC @think "(No, she's just... perhaps a little confused?)"
                jump qst_TheBeastOfNovaras_SyphaDate_marketmenu2

            "What do you {i}really{/i} want, Sypha?":
                pass
    else:
        MC "What do you {i}really{/i} want, Sypha?"

    SYPHA @happy "To try the food at that next stall."
    SYPHA @happy "It smells delicious!"
    MC @think "That's not what I meant and you know it."
    SYPHA @talk "Enough questions for now."
    show sypha at center_f with ease
    SYPHA @talk "Come."
    scene cg_sypha_date_1 with dissolve
    "Once more she grabbed at my hand, dragging me towards the next stall."
    "Sypha continued to dart from store to store, her curiosity insatiable."
    scene cg_sypha_date_2 with dissolve
    "Despite her aloof exterior, she seemed genuinely fascinated by the food, trinkets, and smells."
    "Remarkably, {i}I actually started to find myself having fun... reluctantly.{/i}"
    $ LocFlush()
    show mc at center_f
    show sypha at cright_f
    with dissolve
    SYPHA @happy "Your food is surprisingly good."
    SYPHA @think "I didn't expect much from barbarians, but..."
    MC @think "{i}Barbarians?{/i} Really?"
    SYPHA @talk "Well, of course."
    SYPHA @talk "{b}All non-Demorai are barbarians.{/b}"
    MC @angry "Remind me again whose people slaughter indiscriminately?"
    SYPHA @sad "Ahh... I am afraid Mirnos is-"
    "She paused, considering her words carefully."
    SYPHA @sad "{i}Being treated harsher than usual, given the circumstances.{/i}"
    MC @angry "What circumstances?"
    MC @angry "Why must you always speak in riddles and half-truths?"
    "Sypha blinked, her expression softening. Whatever brief joy she'd had vanished, replaced by cold business."
    SYPHA @sad "Not here."
    SYPHA @sad "Come with me."
    hide sypha with easeoutleft
    hide mc with easeoutleft
    "In silence, I followed Sypha as she led me through the bustling streets of Hamun."
    scene black with dissolve
    "Several times, I nearly lost sight of her, but she always managed to find me with ease, tugging at my arm as she pulled me along."
    "Just where was she taking me?"
    "Some secret lair? Perhaps a dark alleyway with one of her so-called contacts?"
    "Maybe... this {i}was{/i} all part of some elaborate trap, and she was about to-"
    $ LocSet("hamun_spa")
    $ LocFlush()
    
    show luna at cright_f
    with dissolve
    show sypha at cleft with easeinleft
    show mc at left with easeinleft
    LUNA @smile "Hello and welcome to {i}The Princess' dream bathhouse!{/i}"
    LUNA @smile "Are you interested in the public baths?"
    LUNA @smile "Or... {i}Perhaps a private bath for this evening?{/i}"
    MC @surprised "H-Huh?"
    SYPHA @happy "A private bath for two, please."
    LUNA @smile "Of course, just let me get you some towels..."
    hide luna with dissolve
    MC @angry "What in the hells is this?"
    show mc at cleft
    show sypha at blurin, cright_f
    with ease
    SYPHA @think "What?"
    SYPHA @think "Relax, I have the coin to pay for us."
    MC @surprised "Why are we here?"
    MC @serious "We need to talk about-"
    SYPHA @happy "{i}Stop.{/i}"
    SYPHA @happy "There are eyes and ears everywhere."
    SYPHA @happy "Wait till we are somewhere private."
    show mc at left
    show sypha at blurin, cleft
    with ease
    show luna at cright_f with dissolve
    LUNA @smile "Here you both go."
    LUNA @smile "That'll be five hundred coins for the evening."
    LUNA @smile "If you wish for me to order wine or some light food, that will cost extra."
    SYPHA @happy "That sounds good."
    LUNA @smile "Very well, that'll be nine hundred."
    show sypha at nod
    "Sypha handed over the bag of coins to Luna."
    LUNA @talk "I'll have the wine and two glasses ready for you when you head on up, then I'll bring the food around shortly."
    show luna at blurin, cright
    $ Pause(0.25)
    hide luna with easeoutright
    "Happily humming to herself, the mature katai made her way into one of the backrooms, presumably to prepare us some food."
    hide sypha with easeoutright
    SYPHA @talk "Come on, this way."
    MC "{i}*Sigh*{/i}"
    hide mc with easeoutright
    $ PlaySoundRandom("tentFlap")
    scene black with dissolve
    $ Pause(0.25)
    $ LocNameSetTemp(_("Bathhouse, private room"))
    $ Pause(0.25)
    scene bg_hamun_spa_vip_night
    show sypha at cright_f
    with dissolve
    show mc at cleft with easeinleft
    $ AutoAmb(False)
    play ambience "audio/ambience_loc/hamun_spa.ogg" fadein 1.0
    MC @talk "Alright, now we're alone we can-"
    $ CharSetClothes("sypha", "naked")
    play sound2 "audio/cfx/clothes_drop.ogg"
    show sypha at blurin, nod
    MC @surprised "Sypha?!"
    "Stripped bare before me, Sypha grinned ear to ear, hands on her hips with smug pride."
    SYPHA @happy "Clothes off, {i}darling.{/i}"
    MC @angry "I thought you just wanted to talk!"
    SYPHA @happy "I {i}do{/i} want to talk."
    SYPHA @happy "Preferably with us both naked in this bath."
    MC @talk "You are..."
    MC @talk "{i}A very forward woman.{/i}"
    SYPHA @happy "Stop being shy."
    SYPHA @happy "I've already heard the reports about what you're packing between your legs."
    scene cg_sypha_tease_anim with dissolve
    play sound "audio/cfx/water_splash_bath.ogg"
    $ Pause()
    "After pouring herself a glass of wine,"
    "Sypha carefully stepped into the water, giving me a perfect view of her ass as she lowered herself in."
    "Tilting her head, she smirked as she looked over her shoulder towards me."
    SYPHA "{i}Enjoying the view?{/i}"
    MC "What man wouldn't?"
    SYPHA "Ha!"
    SYPHA "{i}Are you just going to stand there and gaze at my ass the whole evening then?{/i}"
    MC "Seems to me like you're enjoying my gaze quite a lot."
    SYPHA "{b}Oh, I intend to possess more than just your gaze.{/b}"
    SYPHA "{b}When I'm done, you won't be able to think about another other than me and *my* ass.{/b}"
    play sound "audio/cfx/water_splash_bath.ogg"
    scene cg_sypha_wine_bathhouse_anim with dissolve
    $ Pause()
    "As much as I didn't trust her, my cock twitched with excitement."
    "Her scent was... unlike anything I'd ever experienced before."
    "She poured another glass of wine that she left on the side just for me, before swirling her own glass playfully in her hand."
    SYPHA "Are you coming in, or not?"
    $ CharSetClothes("mc", "naked")
    $ PlaySoundRandom("tentFlap")
    "Stripping off my clothes, I slid into the warm, soothing waters beside her."
    "Sypha bit her lip, eyes lingering hungrily on the cock between my legs."
    SYPHA "So then..."
    SYPHA "How about this..."
    SYPHA "For every question you ask, I shall ask one too."
    MC "... Very well."
    SYPHA "Good."
    SYPHA "Do you believe peace can exist between the Demorai and the Alderians?"
    menu:
        "Yes, if the Demorai were actually willing to talk...":
            SYPHA "Really?"
            SYPHA "And what would you offer them at these talks?"
            MC "That's two questions."
            SYPHA "Ha! Forgive me, I get ahead of myself."
            pass
        "No... They are invaders.":
            SYPHA "{b}From our perspective, we're liberators.{/b}"
            MC "What?"
            SYPHA "Ah ah! Choose your next question carefully."
            pass
        "I don't know.":
            SYPHA "Hmm... I suppose that's fair enough."
            pass
    SYPHA "Well, your turn."
    menu:
        "Where did your people come from?":
            SYPHA "That answer is... {i}complicated.{/i}"
            SYPHA "Let's say for now that we have come to your world from across the stars."
            MC "... What?"
            SYPHA "Through the gateways left by the gods."
            SYPHA "Surely you must-"
            SYPHA "... Ahh, maybe not."
            MC "What are you talking about?"
            SYPHA "That's two questions!"
            pass
        "Why do all the Demorai look so... different?":
            SYPHA "The Demorai is not a {i}'race'{/i} as you think of it."
            SYPHA "Any species may join the Demorai."
            SYPHA "They simply need to welcome the great saviour into their heart and worship him as the true god."
            SYPHA "Then, his gift will be blessed upon you, and your body will be altered to his whims."
            MC "You mean, {i}the Demorai is actually made up of hundreds of different races?{/i}"
            SYPHA "{b}Correct.{/b}"
            pass
        "What do your people want?":
            SYPHA "To claim this world, of course."
            MC "That's not much of an answer."
            SYPHA "It's not an answer I'm comfortable to fully give yet."
            SYPHA "But make no mistake... for us,"
            SYPHA "{i}this is a holy war.{/i}"
            pass
    SYPHA "Let's say... hypothetically,"
    SYPHA "{i}you{/i} were the one in charge instead of that 'emperor' of yours."
    SYPHA "What would you do?"
    menu:
        "I would crush all dissent, including those still loyal to Alcott.":
            SYPHA "Pragmatic and brutal."
            SYPHA "Though people might start calling you a tyrant..."
            SYPHA "{i}You would make a good Demorai.{/i}"
            "Somehow, that made me a little uneasy..."
            pass
        "I would focus on unity, bringing together the fractured kingdoms.":
            SYPHA "Mmm, yes."
            SYPHA "It would be wise to unite them once more."
            SYPHA "{i}Perhaps under better leadership, they might have been a more formidable force.{/i}"
            pass
        "I would focus more on reform and economics... Things cannot improve till the rot on the inside is removed":
            SYPHA "... Hmm, a curious answer."
            SYPHA "More for the ink than the sword, are we?"
            MC "Don't worry, I can swing a blade just fine."
            SYPHA "Evidently."
            SYPHA "Your turn."
            pass
    menu:
        "Who was that man in the cave?":
            SYPHA "The great Khazel."
            SYPHA "The Eternal Emperor who saw the first of us made into Demorai."
            MC "Eternal?"
            SYPHA "He has sat for thousands of years on the great throne."
            SYPHA "He is all the Demorai have ever known."
            pass
        "Who is Zanarak to the Demorai?":
            SYPHA "A servant of the same god."
            SYPHA "But certainly not a Demorai."
            MC "... That's it? You have nothing more to say?"
            SYPHA "He is the saviour's champion."
            SYPHA "His hammer."
            SYPHA "... Or at least, so I am told."
            SYPHA "I, like any other sensible Demorai, know to stay well clear of him."
            pass
        "What are your people like?":
            SYPHA "What an odd question!"
            SYPHA "Hmm..."
            SYPHA "{i}To be brutal is not enough; one's mind must also be sharp as a dagger{/i} is a common belief amongst my people."
            SYPHA "It is not just common for a Demorai to betray their friends."
            SYPHA "It is celebrated."
            MC "That sounds like it might lead to a very lonely, paranoid life."
            SYPHA "... You get used to it."
            MC "If treachery is so common with your people, how am I supposed to trust you?"
            SYPHA "I could ask you the same thing."
            SYPHA "What's to stop you, an Alderian, simply betraying and having me killed, hmm?"
            MC "... "
            SYPHA "Much like I must have some faith in you, you must have faith in me."
            SYPHA "{i}Or we're both doomed.{/i}"
            pass

    SYPHA "Final question."
    SYPHA "If I told you... that I was part of a faction devoted solely to putting the empire first,"
    SYPHA "And {i}not{/i} the Eternal Emperor himself... What would you say?"
    MC "... I would wonder if anything you've told me tonight is the truth."
    MC "Or if you're just trying to manipulate me."
    SYPHA "Trust me."
    "Sypha glided across the water towards me, her hands pressing lightly to my chest."
    "Her voice softened, sultry, honeyed."
    SYPHA "I know you might struggle to believe this."
    SYPHA "But I want this war to end just as much as you."
    SYPHA "And if we work together... both of our people may yet walk away alive."
    "Her hands ran lower across my body, teasingly slow."
    SYPHA "I understand your... {i}courtship{/i} methods are different than ours."
    SYPHA "And even if I have laid claim to you, I {i}need{/i} you to trust me, so..."
    SYPHA "{i}Let me taste you... dear.{/i}"
    "Her words dripped like honey, warm and dangerous."
    menu:
        "{image=[ICON.HEART]} Kiss her.":
            scene black with dissolve
            "With my hands on her waist, she let out a soft gasp as I pulled her closer."
            $ AutoMus(False)
            $ PlayMusicRandom("mus_sex")
            "Her delicate lips pressed against mine as she slipped her tongue into my mouth."
            "My hands slowly glided down, grabbing her ass as she pressed her chest against mine."
            SYPHA "Mhmm... ❤️"
            "As I squeezed her round, toned ass, she bit at my lower lip, dragging it playfully before releasing."
            SYPHA "I could get used to that."
            MC "I don't even know what in the hells I'm doing with you right now."
            SYPHA "{i}Choosing a side.{/i}"
            if QstTheBeastOfNovaras().BoughtLocket == True:
                $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x2.ogg", 1)
                scene sypha_hamun_bath_hj_loop1 with dissolve
                $ Pause()
                "Sypha's hand reached down to grab a hold of my cock."
                MC "Ahhh..."
                SYPHA "Well, after buying me that lovely locket."
                SYPHA "I thought hmm... How could I thank him properly?"
                "Sypha's hand moved faster as she stroked my cock."
                MC "Ahhh... S-Sypha."
                MC "You're - Mhmm..."
                MC "{i}Very skilled at that.{/i}"
                SYPHA "I can assure you."
                $ PlaySexFx("audio/sex_sounds/adara_hj_loop_x3.ogg", 1)
                scene sypha_hamun_bath_hj_loop2 with dissolve
                $ Pause()
                SYPHA "Keeping you fed is almost as important to me as keeping you drained properly."
                "Her hand moved faster, stroking my hard member as she teasingly kissed at my neck."
                "Her soft, warm tongue running along it."
                MC "Urghhh...!"
                MC "Sypha... Ah..."
                "My cock throbbed in excitement."
                SYPHA "Cum for me."
                MC "{i}*Huff*{/i} Sypha...{i}*Huff*{/i}"
                SYPHA "{i}Cum. For. Me.{/i}"
                $ PlaySexFx("audio/sex_sounds/adara_hj_finish.ogg")
                scene sypha_hamun_bath_hj_finish with flash
                $ ReduceInfectionFromSex("sypha")
                $ UnlockGalSceneAndGrantXp("sypha", "hamun_bath_hj")
                $ CharSetLover("sypha")
                $ Pause()
                "Unable to hold back, I grunted as I finished."
                "A grinning Sypha pulled back her hand, licking the hot seed from her fingers with a smirk."
                SYPHA "Tasty."
                MC "Why do I get the feeling you're toying with me still?"
                $ AutoMus(True)
                scene cg_sypha_wine_bathhouse_anim with dissolve
                SYPHA "{i}A good Demorai relationship is built on power.{/i}"
                SYPHA "One is always submissive, the other dominant."
                MC "... Wait, are you trying to dom-"
                "The door swung open as Luna entered, wine bottle ready with a tray of food."
                LUNA "Your food, as requested."
                SYPHA "Lovely, just place it on the side."
                "Luna did as she was told before stepping out and closing the door behind her."
                
                MC "..."
                SYPHA "... Well, don't just keep staring at me, dig in."
                pass
            else:
                stop music
                play sound "audio/cfx/scratch_stop.ogg"
                "Sypha pulled herself away."
                MC "What?"
                SYPHA "Like I said... {i}I just wanted a taste for now.{/i}"
                MC "{i}You like to tease, don't you?{/i}"
                SYPHA "I want your cock throbbing the minute I walk in a room."
                SYPHA "When I'm done, you'll be grabbing my hand and desperately trying to pull me away for some fun."
                MC "You are... {i}different{/i} than I expected."
                $ AutoMus(True)
                $ CharSetFriend("sypha")
                pass

        "Reject her":
            "I lightly pushed Sypha away."
            SYPHA "... Hmm."
            SYPHA "Very well."
            SYPHA "{i}I'm not used to being told no.{/i}"
            SYPHA "No matter... I will make you fall in love with me eventually."
            MC "Most women don't just casually declare that kind of thing out loud."
            SYPHA "{i}Then your women are cowards.{/i}"
            SYPHA "A good Demorai takes what they want."
            $ CharSetFriend("sypha")
            pass

    scene black with dissolve
    "The rest of the evening was surprisingly unremarkable."
    "Sypha continued to tease me, but she refused to answer any questions too inquisitive."
    "Instead she seemed focused more on myself, my likes and dislikes."
    "Or questions about life in Alderay."
    $ CharSetClothes("mc", "naked")
    $ CharSetClothes("sypha", "naked")
    scene bg_hamun_spa_vip_night
    show sypha at cright_f
    with dissolve
    show mc at cleft with easeinleft
    MC @talk "Alright, now we're alone we can-"
    "Finally, as the last of the wine reached the end of the bottle, Sypha playfully pulled herself from the water once more,"
    "giving me another ample view of her bare, pale ass."
    SYPHA @happy "It's getting late, husband."
    SYPHA @happy "We should head back."
    scene black with dissolve
    $ AutoAmb(True)
    $ CharSetClothes("mc", "normal")
    $ CharSetClothes("sypha", "normal")
    $ LocNameReset()
    "Agreeing, we dressed and returned together to {i}The Pale Dragon.{/i}"
    $ LocSet("hamun_hookah_bar")
    jump qst_TheBeastOfNovaras_PostDateAtTavern


label qst_TheBeastOfNovaras_PostDateAtTavern:
    $ Pause(0.25)
    $ LocFlush()
    show mc at cright_f
    show sypha at cleft
    with dissolve
    MC @drunk "Well... Goodnight, Sypha."
    SYPHA @happy "May I join you in your quarters tonight?"
    SYPHA @happy "I have more important matters to discuss with you."
    MC @think "Now?"
    SYPHA @happy "{i}Yes... It can't wait.{/i}"
    "Sypha shifted mischievously on the spot."
    "Something told me if I allowed Sypha into my room,"
    "{i}I might be in for more than I bargained for...{/i}"
    SYPHA "Well?"
    menu:
        "Very well.":
            SYPHA @happy "Wonderful!"
            SYPHA @happy "I just need to grab another bottle of wine from my room and then I'll join you."
            MC @drunk "I'm not sure another bottle would do me any favors."
            SYPHA @happy "Oh, one more glass won't hurt."
            SYPHA @happy "{i}I'll be with you shortly...{/i}"
            hide sypha with easeoutright
            "Sypha, happily humming to herself, headed down the corridor towards her room."
            show mc at blurin, center with ease
            "For a terrifying assassin who I still wasn't entirely sure what to make of,"
            "She was surprisingly cute in her own, slightly alarming way."
            pass
    
        "I'm too drunk and too tired... It'll have to wait till the morning.":
            SYPHA @sad "A-Ahh... I see."
            SYPHA @sad "That is most frustrating."
            MC @drunk "Tomorrow we can discuss whatever it is you wanted to tell me."
            show sypha at blurin, cleft_f
            hide sypha with easeoutleft
            "A mixture of irritable and dejected, Sypha simply said nothing as she turned to leave."
            show mc at center_f with ease
            MC @think "(... Did I do something wrong?)"
            $ QstComplete(QstTheBeastOfNovaras)
            $ LocEnter()

    $ CharSetClothes("sypha", "ling_chain")
    scene black with dissolve
    $ LocSet("hamun_hookah_bar_room")
    $ LocFlush()
    with dissolve
    show mc at cright with easeinleft
    show mc at blurin, cright_f
    $ PlaySoundRandom("woodenDoor")
    "The door closed behind me, and I heard the distinct sound of the key turning as it locked."
    MC "Sypha?"
    show sypha at cleft with easeinleft
    "Holding out a chain in her hand, Sypha stepped closer towards me."
    show sypha at center with ease
    "I stepped back, for a brief moment, believing this to be some kind of ambush." 
    SYPHA @happy "I'll tell you one more secret."
    SYPHA @happy "{i}If you trust me to put this chain around you.{/i}"    
    MC @angry "What in the hells, Sypha?"
    SYPHA @happy "Just another little game."
    SYPHA @happy "It's a favorite among Demorai who are selecting their partner."     
    SYPHA @happy "One designed to test their partner's willpower..."
    SYPHA @perv "{i}... And endurance.{/i}"
    MC @angry "..."
    SYPHA @perv "So, how about it?"
    menu:
        "Agree.":
            pass

        "Refuse.":
            "In a moment, Sypha's whole demeanor changed as she dropped the chain with a thud onto the floor."
            SYPHA @sad "There's no point in conquest if your opponent simply surrenders."
            SYPHA @sad "I am... {i}Profoundly dissapointed.{/i}"
            MC @serious "I don't play games Sypha, if you want something, you'll have to ask."
            show sypha at blurin, center_f
            "Sypha seemed to almost cringe at the comment,"
            hide sypha with easeoutleft
            "Irritable, and with little more than a 'tsch!' sound, she stormed out from my quarters."
            show mc at center_f with ease
            "Just what is wrong with that girl?"
            $ CharSetClothes("sypha", "normal")
            $ QstComplete(QstTheBeastOfNovaras)

            $ LocEnter()

    SYPHA @perv "Haha..."
    SYPHA @perv "Don't disappoint me now!"
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    show mc at nod
    "Sypha moved closer, pulling at the chain."
    SYPHA @perv "This is going to be fun."
    scene black with dissolve
    "... Ten minutes later."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_slow.ogg", 1)
    scene sypha_hamun_room_tj_front_slow with dissolve
    $ Pause()
    "Tied and restrained, a grinning Sypha slid my cock between her thighs as she gently rocked her ass back and forth against it."
    MC "Hrghhhh!"
    SYPHA "Haha! How you holding on... {i}husband?{/i}"
    SYPHA "Your cock feels like it's throbbing already!"
    "My hands tightened as I struggled to hold myself back. Sypha reveled in every moment of teasing as she wiggled her ass against me."
    scene sypha_hamun_room_tj_pov_slow with dissolve
    $ Pause()
    "As she glided her thighs back and forth, my cock nestled just beneath her wet cunt, aching from how hard it was, desperate to fuck this Demorai pussy."
    SYPHA "Mmfghh...!"
    "She yanked on the chain."
    SYPHA "Don't cum yet."
    MC "G-Grghh!"
    MC "You bitch!"
    SYPHA "Mmm... Haha!"
    SYPHA "That's right, I am a bitch."
    SYPHA "But you're the one chained up right now, so that must make you..."
    SYPHA "My bitch."
    "I resisted against the chains. Perhaps I should use my powers, break free and pin her to the-"
    $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg", 1)
    scene sypha_hamun_room_tj_front_fast with dissolve
    $ Pause()
    SYPHA "*Huff* You should - *Huff* know something."
    "Between heavy, hot breaths, I strained against the ever-growing need to cum."
    MC "Tell me – Ahh! What it is you wanted to say!"
    MC "Mmffhh! We had a deal!"
    "Sypha continued to push her ass up against me, squeezing my cock between her thighs."
    SYPHA "One more *Huff* secret - *Huff* huh!"
    SYPHA "Fine."
    "Sypha tugged hard on the chain."
    SYPHA "I've already killed one of my kin who tried to claim you for herself."
    MC "WHAT?!"
    "Sypha laughed, moving her ass faster as she continued to squeeze and stroke my cock."
    scene sypha_hamun_room_tj_pov_fast with dissolve
    $ Pause()
    "The room had become like an inferno, unbearable as even the candles' warmth burned too hot. Too close."
    SYPHA "Romantic, isn't it?"
    "Sypha began to slam her hips back furiously as I grunted, down to the last vestiges of my resistance."
    SYPHA "Don't think *huff* for a second *huff* I do that for anyone!"
    SYPHA "If you weren't a prize to be – Mmfghh! Conquered! I'd have – ahh! Never bothered with such lengths!"
    "I can't believe the words I'm hearing."
    "Is she serious? Did she truly kill someone over me?"
    "Why is she boasting? Why-"
    "The flurry of thoughts was interrupted as she ground her ass against me. I couldn't hold on any longer."
    "Fuck... Fuck fuck fuck! It's too unbearable with her!"
    MC "S-Sypha, I'm-"
    SYPHA "Yes!"
    SYPHA "Yes, yes, yes!"
    "As she yanked sharply on the chain once more, I grunted. The overwhelming sensation became unbearable, and Sypha let out a pleased gasp as she felt my whole body tense up before I came."
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    scene sypha_hamun_room_tj_front_finish with flash
    $ ReduceInfectionFromSex("sypha")
    $ UnlockGalSceneAndGrantXp("sypha", "hamun_room_tj")
    $ CharSetLover("sypha")
    $ Pause()
    MC "H-HRGHHHHH!"
    SYPHA "That's it..."
    SYPHA "Cum for me."
    scene sypha_hamun_room_tj_pov_finish with dissolve
    SYPHA "I'm going to make all of you mine."
    MC "{i}*Huff*{/i} Sypha...{i}*Huff*{/i}"
    SYPHA "{i}*Giggles*{/i} So pent up... Perhaps I should surprise you more often, hmm?"
    scene black with dissolve
    "Fully spent, a satisfied and giggling Sypha gently stepped forward as my cock softened."
    "Between her legs, two glistening streams ran down from the wet patch as she caught her breath."
    $ AutoMus(True)
    $ CharSetClothes("sypha", "ling_chain")
    $ CharSetClothes("mc", "naked")
    $ LocFlush()
    show sypha at cright_f
    with dissolve
    SYPHA @laugh "Phew...!"
    SYPHA @laugh "I might have got a little carried away there."
    MC "You think?!"
    SYPHA @happy "What? I thought you humans appreciated romance!"
    MC "Romance?!"
    MC "In what world was that romantic!"
    SYPHA @embarr "Well, I find it a little embarrassing to be so lovey-dovey too, but still..."
    MC "Are you going to untie me, or do I need to break out of these things?"
    SYPHA @happy "Ah, just hold still."
    show mc at cleft with easeinleft
    SYPHA @happy "There, all untied."
    MC @angry "What in the seven hells was that madness about killing someone?"
    SYPHA @blush "By the saviour, stop... You're making me blush."
    SYPHA @blush "Do you have any idea how embarrassing it is to say you've killed for someone out loud?"
    SYPHA @blush "If my sisters saw me, the mockery I'd endure for such sweetness would never end."
    "The more she talked, the stranger it felt, as though her whole world was backwards compared to mine."
    "And yet, she spoke with such conviction, as though it was the most normal thing in the world."
    SYPHA @blush "I hope you don't mind how slow we're taking things..."
    MC @surprised "Slow?!"
    MC @surprised "SLOW?!"
    SYPHA @blush "I mean, all this talking and such."
    SYPHA @blush "Most Demorai would have simply claimed you by force by now, but..."
    SYPHA @happy "I'm rather enjoying all the buildup, aren't you?"
    menu qst_TheBeastOfNovaras_PostDateAtTavern_syphamenu:
        "Is this kind of thing... Normal for Demorai?":
            SYPHA @think "What do you mean?"
            SYPHA @think "I mean, I just don't want you to think I'm the kind of girl to just lay claim to anyone..."
            SYPHA @angry "I have standards, you know!"
            jump qst_TheBeastOfNovaras_PostDateAtTavern_syphamenu
        "Did you really mean what you said about killing someone?":
            SYPHA @blush "It's... Very embarrassing the way you keep bringing that up."
            SYPHA @angry "She was a second-rate assassin anyway."
            MC @serious "I feel like you're missing the real problem here..."
            SYPHA @blush "Don't tell anyone about it, please?"
            SYPHA @blush "I prefer to just keep such topics as pillow talk."
            jump qst_TheBeastOfNovaras_PostDateAtTavern_syphamenu
        "Is this really what your people call love and romance?":
            SYPHA @angry "Don't be so vulgar."
            SYPHA @angry "Love is weakness."
            SYPHA @happy "All Demorai know true relationships are built on power and control."
            SYPHA @happy "One master, one servant."
            MC @surprised "... I... I have no idea what to say to that."
            SYPHA @happy "No need, dear husband."
            SYPHA @happy "I'm curious to see what your counterstrike will be!"
            pass
    hide sypha with easeoutleft
    "With a slight, girlish giggle, Sypha made her way towards the door, blowing me a kiss before leaving."
    show mc at center with ease
    MC "... She's insane."
    $ PlaySoundRandom("tentFlap")
    $ CharSetClothes("sypha", "normal")
    $ CharSetClothes("mc", "normal")
    show mc at blurin, nod
    SHYAHTAN "I like her."
    show mc at blurin, center_f
    MC "You like anything that's breedable."
    SHYAHTAN "She will prove an excellent favored mate."
    SHYAHTAN "She will do well to keep the others in line when the time comes."
    MC @think "She oddly reminded me of that woman from your past."
    MC @think "Dramora, was it?"
    "The voice inside stirred."
    SHYAHTAN "Yes... Dramora."
    "The voice, Shyahtan or whatever its name was, seemed saddened by the mention of the name."
    MC @think "Do you remember what happened to her at all?"
    SHYAHTAN "No..."
    SHYAHTAN "Enough talking. Rest."
    MC "(Hm... I hope Garen returns soon.)"
    MC "(Who knows what 'romantic' idea Sypha will come up with again if left for her own devices too long.)"
    $ QstComplete(QstTheBeastOfNovaras)
    $ LocEnter()
