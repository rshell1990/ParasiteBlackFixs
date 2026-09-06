default MYRESU = Character(_("Myresu"), image="myresu")
init python:
    CharDefs["myresu"] = BuildCharTemplate(CharID = "myresu", ExtraData = {"clothes":"normal"})
    config.tag_layer["myresu"] = "characters"