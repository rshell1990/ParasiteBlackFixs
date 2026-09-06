init python:
    @AppendToAllQuests
    # adara romance logic, pretty much unused until her house becomes visitable and handles rep-scenes in there
    class RomanceAdara(LogicModule):
        def extraDialogue(self):
            yield ("adara_root", DNode(_("I was wondering if you could help give me some {i}relief{/i} again..."), "rom_adara_ask_to_have_sex"))

label rom_adara_ask_to_have_sex:
    # cockblock 2, daddy's out there
    if DialogueGerard().isPresent:
        ADARA @shame "I ... I can't."
        ADARA @shock "Not while father is downstairs!"
        return

    ADARA @joy "A-Alright then, what do you want to do?"
    menu:
        "Can you use your mouth again?":
            $ DialogueGerard().isPresent = True
            jump rom_adara_asked_blowjob
        "Could you used your tits to massage me again?":  
            $ DialogueGerard().isPresent = True
            jump rom_adara_asjked_titjob
        "On second thought...":
            ADARA @sad "Oh, um, alright then..."
            return
    return
