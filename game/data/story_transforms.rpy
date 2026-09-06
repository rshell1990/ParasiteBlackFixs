init python:
    flash = Fade(.25, 0.0, .75, color="#fff")
    slowflash = Fade(1.5, 0.0, .75, color="#fff")
    bloodflash = Fade(.17, 0.0, .17, color="#f00")
image white:
    "black"
    matrixcolor BrightnessMatrix(1.0)

# standard slots to display chars
transform left:
    xcenter 0.13
    xzoom 1.0
transform cleft: # closer-to-center-left
    xcenter 0.325
    xzoom 1.0
transform center:
    xcenter 0.5
    xzoom 1.0
transform cright: # closer-to-center-right
    xcenter 0.675
    xzoom 1.0
transform right:
    xcenter 0.87
    xzoom 1.0

# flip X variants
transform left_f:
    xcenter 0.13
    xzoom -1.0
transform cleft_f: # closer-to-center-left
    xcenter 0.325
    xzoom -1.0
transform center_f:
    xcenter 0.5
    xzoom -1.0
transform cright_f: # closer-to-center-right
    xcenter 0.675
    xzoom -1.0
transform right_f:
    xcenter 0.87
    xzoom -1.0

transform shake:
    subpixel True
    ease .06 xoffset 24
    ease .06 xoffset -24
    ease .05 xoffset 20
    ease .05 xoffset -20
    ease .04 xoffset 16
    ease .04 xoffset -16
    ease .03 xoffset 12
    ease .03 xoffset -12
    ease .02 xoffset 8
    ease .02 xoffset -8
    ease .01 xoffset 4
    ease .01 xoffset -4
    ease .01 xoffset 0
transform nod:
    subpixel True
    ease .2 yoffset 24
    ease .1 yoffset 0

### to avoid re-showing a char at certain pos
transform alpha_out:
    ease 0.5 alpha 0.0
transform alpha_in:
    ease 0.5 alpha 1.0

transform kissandleave:
    subpixel True
    ease .5 xoffset -300
    0.3
    ease .9 xoffset 1500

transform sexy_flyby_upwards(FlyToYoff = -100): # some cgs like elena dressed up
    subpixel True
    yoffset -1000
    zoom 2.0
    pause 0.5
    ease 5.0 yoffset FlyToYoff
    pause 0.5

transform walk_left_right: # elena wolf form only
    subpixel True
    ease 2.0 xoffset 700
    xzoom -1.0
    ease 2.0 xoffset 0
    xzoom 1.0
    repeat

transform blurin(factor=10.0,HowLong=0.5):
    blur factor
    ease HowLong:
        blur 0.0

transform zoomin(factor=1.5,HowLong=0.5): # man in black
    zoom 1.0
    ease HowLong:
        zoom factor