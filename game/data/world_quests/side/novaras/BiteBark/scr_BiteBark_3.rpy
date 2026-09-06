label qst_BiteBark_3_ReturnToRegina:
    show regina at left with dissolve
    show mc at cright_f with easeinright
    REGINA @talk "Ah, you're back! Did you get-"
    show elena_w at center_f with easeinright
    REGINA @shock 'Ooh!'
    MC @smile 'I followed your advice and got myself a companion.'
    REGINA @smile_talk 'Yes, I can see that...'
    '[regina_ref_cap!t] looked the silent wolf up and down and smiled.'
    REGINA @talk 'Yes, this one will do perfectly.'
    MC @surprised 'Are you sure? I mean, she seems a little... {i}weird.{/i}'
    ELENA_W '...'
    REGINA @smile_talk "I don't think you have anything to worry about with this one dear."
    REGINA @talk "Now, don't be late home later, I have a nice stew brewing."
    MC @talk"Yes, [regina_ref!t]."
    REGINA @talk "You should take her to your room to let her familiarise herself with where she'll be sleeping."
    MC @talk 'Good idea.'
    REGINA @smile_talk 'Have fun.'
    'Still with a smile on her face, [regina_ref!t] happily humming went back to cooking.'
    hide regina with dissolve
    $ LocSet("mc_house_bedroom")
    $ LocFlush()
    with dissolve
    if QstIsActive(EventNijahRescue):
        if QstGetProgress(EventNijahRescue) in [2, 3]:
            NIJAH @smile 'Ooh!'
            NIJAH @smile 'And who iz this?'
            ELENA 'Bark!'
            MC @talk "Oh, I haven't given her a name yet."
            MC @talk "She'll be joining me on quests and such from now on hopefully."
            'Nijah smiled as she reached down to pet the slightly stoic looking wolf before she trotted off without saying a word.'
            NIJAH 'Hmm... Strange pet.'
            MC @talk "Don't worry about her, she won't harm you."
            NIJAH @smile 'I think she will warm to you in time.'
            MC @talk 'I hope so!'

    'I took the knee near the wolf.'
    show mc:
        xcenter 0.2
    show elena_w:
        xcenter 0.45
        xzoom -1.0
    with dissolve
    MC @talk "So, this is where you'll be staying..."
    'The wolf paced around my room house, inquisitively sniffing and looking around before it was finally satisfied.'
    hide elena_w with easeoutleft
    'Turning around to face me once again, the wolf sat down and remained stoically silent.'
    hide mc with dissolve
    show elena_w with dissolve:
        xcenter 0.35
        yoffset -50
        xzoom -1.0
    $ choicemenu = ["a", "b", "c"]
    menu qst_BiteBark_3_ReturnToRegina_choicemenu:
        "Wanna play fetch girl?" if "a" in choicemenu:
            ELENA_W "..."
            $ choicemenu.remove("a")
            jump qst_BiteBark_3_ReturnToRegina_choicemenu
        "Not much of a talker are you?" if "b" in choicemenu:
            ELENA_W "..."
            $ choicemenu.remove("b")
            jump qst_BiteBark_3_ReturnToRegina_choicemenu
        "I've never seen a blue wolf before..." if "c" in choicemenu:
            ELENA_W "..."
            $ choicemenu.remove("c")
            jump qst_BiteBark_3_ReturnToRegina_choicemenu
        "You hungry?":
            ELENA_W @bark "Bark!"
            MC @smile "Well, at least I know you aren't broken."
            if PlayerItemQty("red_meat") > 0:
                "As I presented her the meat, she carefully approached, sniffing it and then... Retreating."
                show elena_w at nod
                ELENA "Bark!"
                MC @think "What? Is something wrong with it?"
                "She prodded at it with her paws, moving it around, but never eating it."
                MC @serious "You fussy little..."
                MC @serious "Fine, let's find you a better cut."
            else:
                MC @talk "Come then, lets go find you some meat."
            MC "(I'm sure one of the traders at the market will sell me some)"
            $ QstSetProgress(QstBiteBark, 3)
            $ LocEnter()
