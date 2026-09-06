init python:
    # this will also dispatch bath scenes
    @AppendToAllQuests
    class DialogueLuna(LogicModule):
        def locationMod(self):
            btnMods = {}
            if GetLocID() == "hamun_spa":
                btnMods["btn_talk_luna"] =          BtnJumpLabel(_("Talk to Luna"), "luna_talk")
                btnMods["hamun_spa_to_female"] =    BtnJumpLabel(STR_LOC.HAMUN_SPA_FEMALE, "luna_talk_cantgothere")
                btnMods["hamun_spa_to_male"] =      BtnJumpLabel(STR_LOC.HAMUN_SPA_MALE, "luna_talk_cantgothere")
            return LocButtonMod(directMods = btnMods)

        def extraDialogue(self):
            yield ("luna_root", DNode(_("I have a few questions."),     "luna_questions"))
            yield ("luna_root", DNode(_("I'd like to use your baths."), "luna_use_baths"))
            yield ("luna_root", DNode(_("Bye."), "luna_bye", nextNode = "DNodeExit", order = -100))

label luna_talk:
    show luna at center_f with dissolve
    LUNA @smile "Hello! May I help you with something?"
    call processDialogue("luna_root") from _call_processDialogue_70
    $ LocEnter()

label luna_bye:
    LUNA "See you around!"
    return

label luna_talk_cantgothere:
    show luna at center_f with dissolve
    LUNA "Hey! You can't just walk in there."
    call processDialogue("luna_root") from _call_processDialogue_71
    $ LocEnter()

label luna_use_baths:
    LUNA @smile "Certainly!"
    LUNA @smile "For you and your companions that'll be two hundred and fifty coins."
    menu:
        "Here you go" (Req_Gold = 250):
            pass
            # cont
        "On second thought...":
            LUNA @talk "Okay then, should you make the decision, the {i}Princess' Dream{/i} is always ready to recieve guests."
            return
    $ PlayerRemItem("gold", 250)
    jump hamun_spa_use_main

label luna_questions:
    LUNA @talk "Hm? Questions?"
    LUNA @talk "What do you want to know?"
    menu luna_questions_menu:
        "How does a katai end up running a bathhouse in Hamun?":
            LUNA @talk "Ahh..."
            LUNA @talk "My husband was sea captain of a small merchant vessel."
            LUNA @talk "The coin was good, but the months at sea were long."
            LUNA @think "That's why we saved up what money we could,"
            MC @talk "He planned to retire and have us open up a store."
            LUNA @sad "That is... until his ship was taken by a storm."
            MC @sad "I am sorry to hear that."
            LUNA @sad "It's alright, it was a long time ago now."
            LUNA @sad "It's... easier to talk about now."
            LUNA @think "Anyway, after my husband died, I was left with the coin we had managed to save up."
            LUNA @smile "I thought, well, no point running off with my tail between my leg."
            LUNA @smile "So, I looked around, and decided instead of a store,"
            LUNA @smile "A bathhouse sounded more fun to run."
            LUNA @smile "Heh... Plus I get a warm bath whenever I want now."
            LUNA @talk "Hope that answers your question."
            jump luna_questions_menu
        "I see a lot of katai around Hamun... How come?":
            LUNA @talk "There's not many other places for a katai to start a business."
            MC @think "What?"
            MC @think "It's illegal for a katai to own a businss in Novaras or something?"
            LUNA @think "Not exactly."
            LUNA @sad "They just don't refuse to hand out any business licences."
            MC @think "... None?"
            LUNA @talk "Well, they either outright refuse to grant permits and licences,"
            LUNA @talk "Or, they charge ludicrous rates that no one in their right mind would pay."
            LUNA @talk "Sometimes as high as five times as much the asking price of a normal human."
            LUNA @sad "They tolerate some of the more powerful merchants when it comes to trade."
            LUNA @sad "For the rest of us though?"
            LUNA @sad "They're only interested in hiring us katai as either servants or whores."
            MC @talk "So that's why katai come here instead?"
            LUNA @talk "As dangerous as the free city is, it's {i}free.{/i}"
            LUNA @talk "At least here, we can etch out a life for ourselves."
            jump luna_questions_menu
        "That's all I wanted to ask.":
            LUNA @talk "Alright then."
            return

# peek-on-girls scenes
image numa_marbella_spa_day   = Movie(start_image = "images/sexy_scenes/_not_gallery/numa_marbella_spa/numa_marbella_spa_day_start.webp", play = "images/sexy_scenes/_not_gallery/numa_marbella_spa/numa_marbella_spa_day.webm")
image numa_marbella_spa_night = Movie(start_image = "images/sexy_scenes/_not_gallery/numa_marbella_spa/numa_marbella_spa_night_start.webp", play = "images/sexy_scenes/_not_gallery/numa_marbella_spa/numa_marbella_spa_night.webm")

image kiara_spa_day   = Movie(start_image = "images/sexy_scenes/_not_gallery/kiara_spa/kiara_spa_day_start.webp", play = "images/sexy_scenes/_not_gallery/kiara_spa/kiara_spa_day.webm")
image kiara_spa_night = Movie(start_image = "images/sexy_scenes/_not_gallery/kiara_spa/kiara_spa_night_start.webp", play = "images/sexy_scenes/_not_gallery/kiara_spa/kiara_spa_night.webm")

image katiya_spa_day   = Movie(start_image = "images/sexy_scenes/_not_gallery/katiya_spa/katiya_spa_day_start.webp", play = "images/sexy_scenes/_not_gallery/katiya_spa/katiya_spa_day.webm")
image katiya_spa_night = Movie(start_image = "images/sexy_scenes/_not_gallery/katiya_spa/katiya_spa_night_start.webp", play = "images/sexy_scenes/_not_gallery/katiya_spa/katiya_spa_night.webm")


