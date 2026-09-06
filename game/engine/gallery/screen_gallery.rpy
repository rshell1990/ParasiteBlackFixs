default galleryBoxSize = (200,200)

screen LewdsGallery():
    tag ingame_menu
    modal True
    default tab = "catMenu"
    use close_outside("LewdsGallery")
    use outer_frame(padd_top = 45):
        vbox:
            yoffset 20
            spacing 10
            xalign 0.5
            fixed:
                xmaximum 1400
                ymaximum 40
                xalign 0.5
                label _("Erotic Memories"):
                    xalign 0.5
                if tab != "catMenu":
                    textbutton _("Return"):
                        xalign 0.03
                        yoffset -5
                        action SetLocalVariable("tab", "catMenu")
            frame:
                xsize 1400
                ysize 710
                if tab == "catMenu":
                    vpgrid:
                        allow_underfull True
                        cols 6
                        xalign 0.5
                        spacing 4
                        #draggable True
                        mousewheel True
                        scrollbars "vertical"
                        for catID in lewdsGalleryLib.keys():
                            fixed:
                                xmaximum 225
                                ymaximum 225
                                if catID in persistent.galleryUnlocks:
                                    imagebutton:
                                        align (0.5,0.5)
                                        idle Transform(lewdsGalleryLib[catID]["catIcon"], matrixcolor = IdentityMatrix(), size = galleryBoxSize)
                                        hover Transform(lewdsGalleryLib[catID]["catIcon"], matrixcolor = MxMapHover(), size = galleryBoxSize)
                                        hovered TooltipSetUI(lewdsGalleryLib[catID]["catName"])
                                        action [TooltipClearUI(), SetLocalVariable("tab", catID)]
                                else:
                                    add lewdsGalleryLib[catID]["catIcon"]:
                                        align (0.5,0.5)
                                        matrixcolor BrightnessMatrix(-1.0)
                                        size galleryBoxSize
                                    #label lewdsGalleryLib[catID]["catName"]:
                                    #    align (0.5,0.85)
                                add "images/gui/unsorted/gallery_frame.webp":
                                    align (0.5,0.5)
                                    size (225,225)
                if tab != "catMenu":
                    vpgrid:
                        allow_underfull True
                        cols 6
                        xalign 0.5
                        spacing 4
                        #draggable True
                        mousewheel True
                        scrollbars "vertical"
                        use lewdsGalleryScenes(tab)

screen lewdsGalleryScenes(catID):
    for sceneID in lewdsGalleryLib[catID]["scenes"]:
        fixed:
            xmaximum 225
            ymaximum 225
            if sceneID in persistent.galleryUnlocks[catID] and persistent.galleryUnlocks[catID][sceneID]["unlocked"]:
                imagebutton:
                    align (0.5,0.5)
                    idle Transform(lewdsGalleryLib[catID]["scenes"][sceneID]["preview"],matrixcolor=IdentityMatrix(),size=galleryBoxSize)
                    hover Transform(lewdsGalleryLib[catID]["scenes"][sceneID]["preview"],matrixcolor=MxMapHover(),size=galleryBoxSize)
                    hovered TooltipSetUI(lewdsGalleryLib[catID]["scenes"][sceneID]["name"])
                    action [
                        TooltipClearUI(),
                        Hide("LewdsGallery",
                        transition = Dissolve(0.3)),
                        Call(lewdsGalleryLib[catID]["scenes"][sceneID]["label"])]
            else:
                add "images/gui/unsorted/gallery_lock.webp":
                    size galleryBoxSize
                    align (0.5,0.5)
            add "images/gui/unsorted/gallery_frame.webp":
                align (0.5,0.5)
                size (225,225)