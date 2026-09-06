init python:
    @AppendToAllQuests
    class DialogueFawha(LogicModule):
        def extraDialogue(self):
            yield ("fawha_root", DNode(_("I should go."), "fawha_bye", nextNode = "DNodeExit", order = -100))
            yield ("fawha_root", DNode(_("I could use a drink."), "fawha_usedrink"))
            yield ("fawha_root", DNode(_("Are they always like this with Raza? They seem barely alive."), "fawha_aretheyalwayslikethiswithraza"))
            yield ("fawha_root", DNode(_("How much for your 'private' services?"), "fawha_privateservices"))

label fawha_talk:
    show fawha with dissolve:
        xcenter 0.25
    "The serving girl seemed lost in thought for a moment, perhaps due to all the Raza smoke..."
    FAWHA 'Yes?'
    call processDialogue("fawha_root") from _call_processDialogue_1
    $ LocEnter()

label fawha_usedrink:
    MC "I could use a drink."
    FAWHA "Sure, five gold for a glass of Diamond Special."
    if PlayerItemQty("gold") >= 5:
        menu:
            "Sure, I'll take it." (Req_Gold = 5):
                MC "Sure, I'll take it."
                $ PlayerRemItem("gold", 5)
                FAWHA @talk 'Here you go sir, enjoy.'
                return
            "I'll pass.":
                FAWHA @talk 'Fine, if you change your mind...'
                return
    else:
        MC 'Oh, nevermind...'
        return

label fawha_aretheyalwayslikethiswithraza:
    FAWHA @talk 'I-'
    FAWHA @talk 'You must be new here.'
    FAWHA @talk 'Raza feels wonderful when you start.'
    FAWHA @talk 'You are filed with energy and life.'
    FAWHA @talk 'But before you know it, the energy wears off quicker and quicker each time.'
    FAWHA @talk 'And instead of giving you energy, you begin to feel tired even with it, and insufferable without.'
    FAWHA @talk 'But by then, you {i}need{/i} it.'
    MC @talk 'You sound like you speak from experience.'
    FAWHA @talk '...Many girls here addicted, I have stayed away.'
    FAWHA @talk 'If they see me talking to you too long, they will ask questions.'
    FAWHA @talk 'Please, let us discuss something else.'
    return

label fawha_privateservices:
            FAWHA @talk 'Oh...'
            if BlackDiamondLogic().freeRide == True:
                FAWHA @talk 'For you? Free of charge.'
            else:
                FAWHA @talk 'One hundred coins to use my breasts.'
            menu:
                "I'm in!" if BlackDiamondLogic().freeRide == True:
                    jump fawhaRevisitBoobJob
                "I'll pay!" (Req_Gold = 100) if BlackDiamondLogic().freeRide == False:
                    $ PlayerRemItem("gold", 100)
                    jump fawhaRevisitBoobJob

                'On second thought...': #Reverts back to menu.
                    MC "Actually, forget it."
                    return

label fawha_bye:
    MC "I should go."
    FAWHA 'Alright, have a nice evening!'
    return

label fawhaRevisitBoobJob:
    FAWHA 'Come, sit down...'
    $ AutoMus(False)
    $ PlayMusicRandom("mus_sex")
    FAWHA "Shall I wear my mask while I please you my lord? Or do you wish to see my face?"
    menu:
        'Keep the Mask on':
            FAWHA 'As you wish my lord...'
            'Sitting down onto the soft, slightly worn down couch, Fawha fumbled with my belt as she pulled out my hardened cock, her eyes doing a double blink as she smiled looking at the member in front of her.'
            FAWHA 'Mmm... I like it big.'
            MC "Glad to serve..."
            hide fawha
            scene fawha_tj_mask
            with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
            $ Pause()
            'Wrapping both of her large nipple pierced brown tits around my cock, I let out a soft moan as she began to bop up and down, watching with a glint her eye for any changes in my expression.'
            FAWHA 'Would you like me to talk dirty sir?'
            MC 'Ahh... Yes...'
            MC 'Well Fawha, keep moving those tits and milk me dry!'
            FAWHA 'Of course sir!'
            MC 'Mmm... G-Good...'
            FAWHA 'Do you like that my lord? My master?'
            FAWHA 'Do you like feeling these fat tits stroking your wonderful, thick cock dry?'
            MC 'K-Keep going... Ahh...!'
            'Fawha pressed her large breasts together, wrapping them around my cock as she moved rhythmically up and down...'
            'The warm soft sensation of her breasts left me breathing heavily as I tried to control the impulse to leap onto her and fuck her senseless.'
            "All the while, Fawha's sultry eyes remained locked onto me, biting at her lower lip as I felt her body become flushed with desire."
            FAWHA 'Y-You... You are close...!'
            MC 'Y-Yes!'
            FAWHA 'Cum my lord! Cover me in your load!'
            scene fawha_tj_mask_finish with flash
            $ UnlockGalFlag("bd_girls","fawha_tj","var_mask")
        'Show me your face.':
            $ CharSetVar("fawha", "mask", False)
            show fawha at nod
            FAWHA 'As you wish my lord...'
            'Sitting down onto the soft, slightly worn down couch, Fawha fumbled with my belt as she pulled out my hardened cock, her eyes doing a double blink as she smiled looking at the member in front of her.'
            FAWHA 'Mmm... I like it big.'
            MC "Glad to serve..."
            scene fawha_tj_nomask with dissolve
            $ PlaySexFx("audio/sex_sounds/kiara_tent_fast.ogg",1)
            $ Pause()
            'Wrapping both of her large nipple pierced brown tits around my cock, I let out a soft moan as she began to bop up and down, watching with a glint her eye for any changes in my expression.'
            FAWHA 'Would you like me to talk dirty sir?'
            MC 'Ahh... Yes...'
            MC 'Well Fawha, keep moving those tits and milk me dry!'
            FAWHA 'Of course sir!'
            MC 'Mmm... G-Good...'
            FAWHA 'Do you like that my lord? My master?'
            FAWHA 'Do you like feeling these fat tits stroking your wonderful, thick cock dry?'
            MC 'K-Keep going... Ahh...!'
            'Fawha pressed her large breasts together, wrapping them around my cock as she moved rhythmically up and down...'
            'The warm soft sensation of her breasts left me breathing heavily as I tried to control the impulse to leap onto her and fuck her senseless.'
            "All the while, Fawha's sultry eyes remained locked onto me, biting at her lower lip as I felt her body become flushed with desire."
            FAWHA 'Y-You... You are close...!'
            MC 'Y-Yes!'
            FAWHA 'Cum my lord! Cover me in your load!'
            scene fawha_tj_nomask_finish with flash
            $ UnlockGalFlag("bd_girls","fawha_tj","var_nomask")
    $ PlaySexFx("audio/sex_sounds/kiara_tent_finish.ogg")
    $ ReduceInfectionFromSex("fawha")
    $ UnlockGalSceneAndGrantXp("bd_girls","fawha_tj")
    $ Pause()
    MC 'Grghhh...!'
    MC '{i}*Huff...*{/i}'
    FAWHA 'I hope this was satisfying for you sir...'
    MC '{i}Very.{/i}'
    $ LocFlush(dissolve)
    show fawha with dissolve:
        xcenter 0.25
    if QstDamzelInDiztrezz().fawhaOneShotAge == True:
        FAWHA "I'm glad I could please you my lord."
        FAWHA 'I must admit, there are younger girls here to choose... Why me?'
        MC 'Hm? How old are you Fawha?'
        FAWHA 'I... I am forty four sir.'
        menu:
            "I'd have never guessed! You're beautiful for your age!":
                FAWHA 'I... You are too kind my lord.'
                FAWHA 'L-Let me know should you wish for my services again!'
            "Don't worry, your body is still built to drain some cocks dry.":
                FAWHA '...Is that so my lord?'
                FAWHA 'Then return to me whenever you are need of my services.'
                FAWHA '{i}*Whispering*{/i} And this old lady will drain your balls better than any of the other whores here.'
                MC 'You know just the right thing to say...'
    $ CharSetVar("fawha", "mask", True)
    $ QstDamzelInDiztrezz().fawhaOneShotAge = False
    scene black with dissolve
    $ AutoMus(True)
    $ LocEnter()