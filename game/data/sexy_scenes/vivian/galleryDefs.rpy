init python:
    lewdsGalleryLib["vivian"] = {}
    lewdsGalleryLib["vivian"]["catIcon"] = "images/characters/vivian/portrait.webp"
    lewdsGalleryLib["vivian"]["catName"] = _("Vivian")
    lewdsGalleryLib["vivian"]["scenes"] = {}

    lewdsGalleryLib["vivian"]["scenes"]["bj"] = {
        "preview":"vivian_bj_preview",
        "name":_("Blowjob"),
        "label":"gallery_vivian_bj",
        "flags":["var_nopreg", "var_preg"],
    }
    lewdsGalleryLib["vivian"]["scenes"]["missionary"] = {
        "preview":"vivian_missionary_preview",
        "name":_("Missionary"),
        "label":"gallery_vivian_missionary",
        "flags":[
            "var_nopreg_vag", "var_nopreg_anal",
            "var_preg_vag",   "var_preg_anal",
        ],
    }