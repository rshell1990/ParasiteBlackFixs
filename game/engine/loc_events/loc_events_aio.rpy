# if its empty when its polled, it refills 
default LocIDList_NovarasCityStreets_ActivePool = []


init python:
    LocIDList_NovarasCityStreets_SharedBtnIDMap = {
        "novaras_dist_centre":      "btn_shared_clickable_event_centre",
        "novaras_dist_edu":         "btn_shared_clickable_event_edu",
        "novaras_dist_farm":        "btn_shared_clickable_event_farm",
        "novaras_dist_house":       "btn_shared_clickable_event_house",
        "novaras_dist_house_south": "btn_shared_clickable_event_house_south",
        "novaras_dist_mage":        "btn_shared_clickable_event_mage",
        "novaras_dist_market":      "btn_shared_clickable_event_market",
        "novaras_dist_pleasure":    "btn_shared_clickable_event_pleasure",
    }

    def LocEvent_GetFreeNovarasDistrict():
        if len(store.LocIDList_NovarasCityStreets_ActivePool) == 0:
            store.LocIDList_NovarasCityStreets_ActivePool = LocIDList_NovarasCityStreets.copy()
            renpy.random.shuffle(store.LocIDList_NovarasCityStreets_ActivePool)
        return store.LocIDList_NovarasCityStreets_ActivePool.pop()

    LocIDList_NovarasCityStreets = [
        "novaras_dist_centre",
        "novaras_dist_edu",
        "novaras_dist_farm",
        "novaras_dist_house",
        "novaras_dist_house_south",
        "novaras_dist_mage",
        "novaras_dist_market",
        "novaras_dist_pleasure"]