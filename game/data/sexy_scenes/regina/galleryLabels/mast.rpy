label gallery_regina_mast:
    $ tmpvar["reg_clothes"] = CharGetClothes("regina")
    scene black with dissolve
    'I dragged myself home. It was dark inside, and I called out for [regina_ref!t] but got no reply.'
    'As I listened out, I heard what seemed to be soft moans coming from her bedroom.'
    $ CharSetClothes("regina", "towel")
    scene regina_mast with dissolve
    $ PlaySexFx("audio/sex_sounds/reginamasturbate_loop.ogg", Loop = 1)
    $ Pause()
    'Creaking open the door ever so slightly, I peeked through the gap.'
    'Inside, [regina_ref!t] lay on the bed writhing in pleasure as she touched herself.'
    'The moonlight reflected off her pale skin as sweat dripped down from her onto the quilts.'
    'I felt a tingle of excitement growing as I watched her, unable to tear my eyes away as her soft mouth opened, letting out hot, elated gasps of pleasure as she plunged the fingers of one hand deep inside herself.'
    'She licked the fingers of her other hand then fondled her nipples, pulling them ever more erect as she contorted with pleasure.'
    'Stupidly, I leaned too far forward on one of the floorboards and it creaked loudly.'
    '[regina_ref_cap!t] looked {b}straight at me{/b} creeping through the gap.'
    $ StopSexFx()
    scene bg_mc_house_kitchen_night with dissolve
    show mcprologue at cright_f
    with dissolve
    'I darted away from the door and stepped back as I heard her footsteps coming closer.'
    'The door swung open as [regina_ref!t] stepped out stared at me, flushed red from embarrassment with a towel now wrapped around herself for dignity, looking both appalled and mortified.'
    show regina at cleft with easeinleft
    MC 'I didn’t mean to, uh, see you like {i}that.{/i}'
    REGINA @shock 'I...'
    REGINA @shock 'W-Why are you home so early?'
    scene black with dissolve
    $ CharSetClothes("regina", tmpvar["reg_clothes"])
    return
