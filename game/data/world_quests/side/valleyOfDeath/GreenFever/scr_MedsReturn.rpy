label greenFeverMedsReturn:
    "Ves' eyes widened in surprise as I held out the bag filled with various medicines and vials."
    VES @talk 'You... You actually bought it?'
    MC @talk 'I promised I would.'
    $ PlayerRemItem("qst_green_fever_meds")
    VES @talk 'I... Thank you.'
    $ QstComplete(QstGreenFever)
    $ CharChangeRel("ves", 1)
    MC @talk 'Is there anything else I can do?'
    VES '...'
    'Ves pondered the thought for a moment, before reluctantly remarking.'
    VES @talk 'Well... I suppose if you are offering...'
    VES @talk 'I plan to set up some perimeter defences, just some bells and such on a wire that will jingle in case anyone tries to sneak into my camp.'
    VES @talk 'I could use some help setting it up if you’re willing...'
    menu:
        '{image=[ICON.CLOCK]} No problem.':
            $ NoteLock("VesHelpCamp")
            jump rom_Ves_2_FortAndCook

        'Can’t right now, sorry.':
            $ NoteUnlock("VesHelpCamp")
            VES @talk '... Oh, well, let me know when you’re able to, I suppose...'
            $ QstSetProgress(RomanceVes, 4)
            $ LocEnter()
