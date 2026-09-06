init python:
    TravelRoutes["valley_vescamp"] = {
        "biome_type":"desert",
        "connects_locations":["valley_of_death", "ves_camp"],

        "image_loc_bg":"pbat_desert",
        "image_battle_bg":"pbat_desert",
        "image_camp":"bg_camp_desert",
        "image_map":"travel_map_valley_ves_camp",
        
        "travel_nodes":{
            0:{"position":(193, 95),    "draw_order":0, "type":"exit", "exit_location_tag":"ves_camp"},
            1:{"position":(252, 448),   "draw_order":3, "type":"random"},
            2:{"position":(518, 685),   "draw_order":4, "type":"random"},
            3:{"position":(529, 149),   "draw_order":1, "type":"random"},
            4:{"position":(971, 288),   "draw_order":2, "type":"random"},
            5:{"position":(1104, 707),  "draw_order":5, "type":"exit", "exit_location_tag":"valley_of_death"},
        },
        "travel_paths":{
            (0, 1):[(151, 161), (150, 245)],
            (1, 2):[],
            (2, 5):[],
            (5, 4):[],
            (0, 3):[(392, 68)],
            (3, 4):[(651, 242), (865, 249)],
        },
        "path_costs_in_hours":{
            (0, 1):8,
            (1, 2):10,
            (2, 5):12,
            (5, 4):8,
            (0, 3):7,
            (3, 4):9,
        },
        
        "world_map_sprite":"path_valley_ves",
        "world_map_sprite_pos":(1122, 1086),
    }    
