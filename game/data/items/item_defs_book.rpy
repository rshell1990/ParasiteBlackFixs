init 1 python:
######### novaras lib
    static_item_defs["book_dragonwars"] = {
        "name":     STR_BOOK.DRAGONWARS_NAME,
        "plural":   STR_BOOK.DRAGONWARS_NAME,
        "desc":     STR_BOOK.DRAGONWARS_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":100,
        "on_use_story":[[ItemOpenBook, STR_BOOK.DRAGONWARS]],
        "shop_category":"book",
        "sort_order":70,
    }
    static_item_defs["book_darkmages"] = {
        "name":     STR_BOOK.DARKMAGES_NAME,
        "plural":   STR_BOOK.DARKMAGES_NAME,
        "desc":     STR_BOOK.DARKMAGES_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":100,
        "on_use_story":[[ItemOpenBook, STR_BOOK.DARKMAGES]],
        "shop_category":"book",
        "sort_order":70,
    }
    static_item_defs["book_newheart"] = {
        "name":     STR_BOOK.NEWHEART_NAME,
        "plural":   STR_BOOK.NEWHEART_NAME,
        "desc":     STR_BOOK.NEWHEART_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":100,
        "on_use_story":[[ItemOpenBook, STR_BOOK.NEWHEART]],
        "shop_category":"book",
        "sort_order":70,
    }
    static_item_defs["book_mageguide"] = {
        "name":     STR_BOOK.MAGEGUIDE_NAME,
        "plural":   STR_BOOK.MAGEGUIDE_NAME,
        "desc":     STR_BOOK.MAGEGUIDE_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":100,
        "on_use_story":[[ItemOpenBook, STR_BOOK.MAGEGUIDE]],
        "shop_category":"book",
        "sort_order":70,
    }

######### hamun
init python:
    static_item_defs["book_prince_onji"] = {
        "name":     _("The Prince of Onji"),
        "plural":   _("The Prince of Onji"),
        "desc":     _("A historical storybook recounting the legend of Prince Onji."),
        "icon":     "images/items/books/book.webp",
        "value_per_unit": 50,
        "shop_category": "book",
        "sort_order": 10,
    }

    static_item_defs["book_legends_far_wide"] = {
        "name":     _("Legends Far & Wide"),
        "plural":   _("Legends Far & Wide"),
        "desc":     _("A collection of myths and folklore from distant lands."),
        "icon":     "images/items/books/book.webp",
        "value_per_unit": 75,
        "shop_category": "book",
        "sort_order": 15,
    }
    static_item_defs["book_legends_far_wide"] = {
        "name":     STR_BOOK.LEGENDS_FAR_WIDE_NAME,
        "plural":   STR_BOOK.LEGENDS_FAR_WIDE_NAME,
        "desc":     STR_BOOK.LEGENDS_FAR_WIDE_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":100,
        "on_use_story":[[ItemOpenBook, STR_BOOK.LEGENDS_FAR_WIDE]],
        "shop_category":"book",
        "shop_flag":"hamun_lib",
        "sort_order":70,
    }

# elena quest
    static_item_defs["book_thornfall"] = {
        "name":     STR_BOOK.ALDERIANHOUSES_NAME,
        "plural":   STR_BOOK.ALDERIANHOUSES_NAME,
        "desc":     STR_BOOK.ALDERIANHOUSES_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":100,
        "on_use_story":[[ItemOpenBook, STR_BOOK.ALDERIANHOUSES]],
        "shop_category":"book",
        "sort_order":70,
    }
# slavemaster quest
    static_item_defs["book_notes_on_slavers"] = {
        "name":     STR_BOOK.SLAVERS_NOTES_NAME,
        "plural":   STR_BOOK.SLAVERS_NOTES_NAME,
        "desc":     STR_BOOK.SLAVERS_NOTES_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":50,
        "on_use_story":[[ItemOpenBook, STR_BOOK.SLAVERS_NOTES]],
        "shop_category":"book",
        "sort_order":70,
    }
### coming storm quest vala investigation route
#####
    static_item_defs["book_dreams_of_astatar"] = {
        "name":     STR_BOOK.DREAMS_OF_ASTATAR_NAME,
        "plural":   STR_BOOK.DREAMS_OF_ASTATAR_NAME,
        "desc":     STR_BOOK.DREAMS_OF_ASTATAR_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":150,
        "on_use_story":[[ItemOpenBook, STR_BOOK.DREAMS_OF_ASTATAR]],
        "shop_category":"book",
        "sort_order":70,
    }
    static_item_defs["book_the_first_darkness"] = {
        "name":     STR_BOOK.THE_FIRST_DARKNESS_NAME,
        "plural":   STR_BOOK.THE_FIRST_DARKNESS_NAME,
        "desc":     STR_BOOK.THE_FIRST_DARKNESS_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":150,
        "on_use_story":[[ItemOpenBook, STR_BOOK.THE_FIRST_DARKNESS]],
        "shop_category":"book",
        "sort_order":70,
    }
    static_item_defs["book_loving_ophelia"] = {
        "name":     STR_BOOK.LOVING_OPHELIA_NAME,
        "plural":   STR_BOOK.LOVING_OPHELIA_NAME,
        "desc":     STR_BOOK.LOVING_OPHELIA_DESC,
        "icon":"images/items/books/book.webp",
        "value_per_unit":150,
        "on_use_story":[[ItemOpenBook, STR_BOOK.LOVING_OPHELIA]],
        "shop_category":"book",
        "sort_order":70,
    }
##################### SKILL BOOKS ###########################
    static_item_defs["skill_book_summoner"] = {
        "name":     _("Summoner Skill Book"),
        "plural":   _("Summoner Skill Books"),
        "desc":     _("A dusty tome containing secrets on how to manifest spectral guardians."),
        "teaches_skill": "Summon",
        "requires_mage": True,
        "icon":     "images/items/books/book.webp",
        "value_per_unit": 150,
        "on_use_story": None,
        "shop_category": "book",
        "sort_order": 70,
    }
    static_item_defs["skill_book_priest"] = {
        "name":     _("Priest Skill Book"),
        "plural":   _("Priest Skill Books"),
        "desc":     _("A dusty tome containing secrets on how to harness divine powers."),
        "teaches_skill": "HealingHands",
        "requires_mage": True,
        "icon":     "images/items/books/book.webp",
        "value_per_unit": 150,
        "on_use_story": None,
        "shop_category": "book",
        "sort_order": 70,
    }
    static_item_defs["skill_book_Saint"] = {
        "name":     _("Saint Skill Book"),
        "plural":   _("Saint Skill Books"),
        "desc":     _("A dusty tome containing secrets on how to harness divine powers as a Saint."),
        "teaches_skill": "Revive",
        "requires_mage": True,
        "icon":     "images/items/books/book.webp",
        "value_per_unit": 150,
        "on_use_story": None,
        "shop_category": "book",
        "sort_order": 70,
    }