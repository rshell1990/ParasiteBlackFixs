# gallery
label nov_soothsayer_gallery:
    if PlayerItemQty('gold') >= 5:
        show babazhul with dissolve
        BABAZHUL @talk 'So be it...'
        $ PlayerRemItem('gold',5)
        BABAZHUL @talk 'But remember child, the past has already come and gone, only the present is a gift.'
        BABAZHUL @talk 'Do not linger too long on the shadows that have already vanished.'
        BABAZHUL @talk 'How easy it is to become lost to their sweetness...'
        hide babazhul with dissolve
        #########################
        # huge-ass gallery sequence

        show cg_nov_witch_glow
        with dissolve
        play sound "audio/cfx/detect_magic.ogg"

        $ tmpvar = {}
        $ tmpvar2 = {}

        $ tmpvar2["stored_FreezeAutoTime"] = store.FreezeAutoTime

        $ BlockWaitDynamic(True)
        $ AutoTimeFreeze(True)
        $ HideUI(True)
        $ AutoAmb(False)
        $ AutoMus(False)

        $ PlayerInGallery = True

        show screen LewdsGallery() ## a gallery label gets called via this screen
        scene black
        with dissolve
        $ Pause(0.1)

        
        $ PlayerInGallery = False

        $ BlockWaitDynamic(False)

        $ AutoTimeFreeze(tmpvar2["stored_FreezeAutoTime"])

        $ tmpvar = {}
        $ tmpvar2 = {}

        $ HideUI(False)
        $ AutoAmb(True)
        $ AutoMus(True)
        $ StopSexFx()
        $ LocNameReset()
        $ SetRepeatVariant(False)
        ###########################
        # phew!
        $ LocEnter()
    else:
        show babazhul with dissolve
        BABAZHUL @talk 'You do not possess enough coin, child, return when you do.'
        hide babazhul with dissolve
        $ LocEnterQ()