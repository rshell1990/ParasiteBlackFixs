init python:
    lewdsGalleryLib["lucy"] = {}
    lewdsGalleryLib["lucy"]["catIcon"] = "images/characters/lucy/portrait.webp"
    lewdsGalleryLib["lucy"]["catName"] = _("lucy")
    lewdsGalleryLib["lucy"]["scenes"] = {}

    lewdsGalleryLib["lucy"]["scenes"]["bj"] = {
        "preview":"lucy_bj_preview",
        "name":_("Blowjob"),
        "label":"gallery_lucy_bj",
        "flags":["var_nopreg", "var_preg"],
    }
    lewdsGalleryLib["lucy"]["scenes"]["sidefuck"] = {
        "preview":"lucy_sidefuck_preview",
        "name":_("Sidefuck"),
        "label":"gallery_lucy_sidefuck",
        "flags":[
            "var_nopreg_vag", "var_nopreg_anal",
            "var_preg_vag",   "var_preg_anal",
        ],
    }