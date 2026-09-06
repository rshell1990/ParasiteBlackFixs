init python:
    TravelRoutes["novaras_balun"] = {
        "biome_type":"forest",
        "connects_locations":["novaras_gates", "lake_balun"],

        "image_loc_bg":"bg_forest",
        "image_battle_bg":"pbat_forest",
        "image_camp":"bg_camp_forest",
        "image_map":"travel_map_novaras_balun",

        "travel_nodes":{
            0:{"position":(137, 258),   "draw_order":1,  "type":"exit",  "exit_location_tag":"lake_balun",},
            1:{"position":(194, 571),   "draw_order":5,  "type":"random",},
            2:{"position":(261, 291),   "draw_order":2,  "type":"random",},
            3:{"position":(593, 588),   "draw_order":6,  "type":"random",},
            4:{"position":(757, 473),   "draw_order":4,  "type":"random",},
            5:{"position":(617, 248),   "draw_order":0,  "type":"random",},
            6:{"position":(960, 464),   "draw_order":3,  "type":"random",},
            7:{"position":(1207, 630),  "draw_order":7,  "type":"exit",  "exit_location_tag":"novaras_gates",},
        },
        "travel_paths":{
            (0, 1):[(132, 482)],
            (0, 2):[(200, 267)],
            (0, 5):[(200, 267), (296, 217)],
            (1, 2):[(264, 527)],
            (1, 3):[(264, 527)],
            (1, 7):[(305, 656), (550, 702), (709, 673), (830, 662), (833, 599), (870, 594), (944, 648)],
            (2, 3):[(264, 527)],

            (2, 5):[(200, 267)],

            (3, 7):[(830, 662), (833, 599), (870, 594), (944, 648)],
            (3, 4):[],
            (4, 6):[],
            (6, 7):[],
            (5, 4):[],
            (2, 4):[(327, 330), (474, 326)],
            (5, 6):[(763, 285)],
            (5, 7):[(763, 285), (1065, 338)],
        },
        "path_costs_in_hours":{
            (0, 1):13,#
            (0, 2):6,#
            (0, 5):19,#
            (1, 2):12,#
            (1, 3):17,#
            (1, 7):46,#
            (2, 3):24,#
            (2, 5):19,
            (3, 7):29,#
            (3, 4):8,#
            (4, 6):9,#
            (6, 7):12,#
            (5, 4):10,#
            (2, 4):22,#
            (5, 6):16,#
            (5, 7):30,#
        },
        
        "world_map_sprite":"path_novaras_balun",
        "world_map_sprite_pos":(945, 905),
    }

