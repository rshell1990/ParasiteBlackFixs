label dialogue_arwen_services:
    ARWEN @talk 'The kind that will drive you wild and leave you waking up in the dead of night muttering...'
    ARWEN @blush '{i}When will I see her again?{/i}'
    MC @talk "Quite the sales pitch."
    ARWEN @talk "Trust me darling, unlike {i}some{/i} here, I'm worth every coin."
    ARWEN @talk "Seven hundred and fifty for my mouth, eleven hundred for my womanhood, and fifteen hundred for special 'backdoor' access."
    menu:
        "I'll try your mouth." (Req_Gold = 750):
            $ PlayerRemItem("gold", 750)
            call sexscene_arwen_mouth from _call_sexscene_arwen_mouth
            jump dialogue_arwen_postSex
        "I'd take what's between your legs." (Req_Gold = 1100):
            $ PlayerRemItem("gold", 1100)
            call sexscene_arwen_betweenlegs from _call_sexscene_arwen_betweenlegs
            jump dialogue_arwen_postSex
        "I'd like the backdoor." (Req_Gold = 1500):
            $ PlayerRemItem("gold", 1500)
            call sexscene_arwen_backdoor from _call_sexscene_arwen_backdoor
            jump dialogue_arwen_postSex
        "On second thought...":
            ARWEN @talk "Your loss."
            ARWEN @talk "Anything else?"
            return

label dialogue_arwen_postSex:
    $ CharSetClothes("arwen", "normal")
    ARWEN @talk "Anyway, now that you're {i}satisfied,{/i} I need to return."
    MC @smile "Do you even have the energy to continue after that?"
    ARWEN @talk "Trust me, most of the clients don't even come close to making me break a sweat."
    ARWEN @talk '{i}...Unlike you.{/i}'
    MC @talk 'Glad to know I leave such an impression.'
    ARWEN @talk "Mmm... Come, the Madam gets suspicious if we spend {i}too{/i} long together."
    MC @talk 'Lead the way.'
    scene black with dissolve
    $ LocNameReset()
    #Fade to black
    'I followed Arwen back with a satisfied grin on my face.'
    $ LocEnter()
