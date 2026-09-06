init python:
    lewdsGalleryLib["betty"] = {}
    lewdsGalleryLib["betty"]["catIcon"] = "images/characters/betty/portrait.webp"
    lewdsGalleryLib["betty"]["catName"] = _("Betty")
    lewdsGalleryLib["betty"]["scenes"] = {}

    lewdsGalleryLib["betty"]["scenes"]["bj"] = {
        "preview":"betty_bj_preview",
        "name":_("Blowjob"),
        "label":"gallery_betty_bj",
    }
    lewdsGalleryLib["betty"]["scenes"]["missionary"] = {
        "preview":"betty_missionary_preview",
        "name":_("Missionary"),
        "label":"gallery_betty_missionary",
        "flags":[
            "var_nopreg_vag", "var_nopreg_anal",
            "var_preg_vag",   "var_preg_anal",
        ],
    }