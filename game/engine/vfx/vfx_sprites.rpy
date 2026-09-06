# flickering round light sources
image lightpost_base = "images/vfx_sprites/vfx_lightpost_glow.webp"
image lightpost_big:
    "lightpost_base"
    matrixcolor MxWarm()
image lightpost_huge:
    "lightpost_big"
    zoom 3.0
image lightpost_small:
    "lightpost_big"
    zoom 0.5
image lightpost_big_indigo:
    "lightpost_base"
    matrixcolor TintMatrix((200, 140, 255))
image lightpost_small_indigo:
    "lightpost_base"
    zoom 0.5
    matrixcolor TintMatrix((200, 140, 255))

# do be aware, these are reused
# novaras city center
image light_crystal_red:
    "lightpost_base"
    zoom 2.5
    matrixcolor TintMatrix((255,100,100))

# palam tower
image light_crystal_yellow:
    "lightpost_base"
    zoom 2.5
    matrixcolor TintMatrix((255,255,100))
image light_crystal_blue:
    "lightpost_base"
    zoom 2.5
    matrixcolor TintMatrix((100,100,255))
image light_crystal_green:
    "lightpost_base"
    zoom 2.5
    matrixcolor TintMatrix((100,255,100))

# palam divine office
image light_crystal_teal:
    "lightpost_base"
    zoom 2.5
    matrixcolor TintMatrix((100, 200, 255))

image light_haze_fiery:
    "images/vfx_sprites/vfx_light_haze.webp"
    zoom 1.5
    matrixcolor TintMatrix((255, 140, 70)) * OpacityMatrix(0.5)
image light_haze_teal_magical:
    "images/vfx_sprites/vfx_light_haze.webp"
    zoom 2.0
    matrixcolor TintMatrix((100, 150, 255)) * OpacityMatrix(0.6)
image light_haze_pink_magical:
    "images/vfx_sprites/vfx_light_haze.webp"
    zoom 1.0
    matrixcolor TintMatrix((255, 0, 255)) * OpacityMatrix(0.6)

image circle_blip_blue:
    "images/vfx_sprites/circle_blip.webp"
    matrixcolor TintMatrix((100, 100, 255))

# makes that kylisa magic sprite overlap chars
init python:
    config.tag_layer["vfx_magick_glow"] = "characters"