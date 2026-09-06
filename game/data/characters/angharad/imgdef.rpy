############### angharad expressions ##############
image angharad talk =   Composite((1000, 1362), (0, 0), "angharad_body", (0, 0), "angharad_animtalk")
image angharad angry =  Composite((1000, 1362), (0, 0), "angharad_body", (0, 0), "images/characters/angharad/face/angry.webp")
image angharad lewd =   Composite((1000, 1362), (0, 0), "angharad_body", (0, 0), "images/characters/angharad/face/lewd.webp")
image angharad furious =Composite((1000, 1362), (0, 0), "angharad_body", (0, 0), "images/characters/angharad/face/furious.webp")
image angharad smile =  Composite((1000, 1362), (0, 0), "angharad_body", (0, 0), "images/characters/angharad/face/smile.webp")
image angharad think =  Composite((1000, 1362), (0, 0), "angharad_body", (0, 0), "images/characters/angharad/face/think.webp")
##############################################

image angharad:
    "angharad_body"

image angharad_body = Composite(
    (1000, 1362),
    (0, 0), ConditionSwitch(
        "worldChars['angharad']['slave']", "images/characters/angharad/slave.webp",
        "True", "images/characters/angharad/normal.webp")
)

image angharad_animtalk:
    Null()
image angharad_animblink:
    Null()
