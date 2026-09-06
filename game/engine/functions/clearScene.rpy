init python:
    # aka "replace anything being shown with current location background"
    def LocFlush(transition = None):
        if _in_replay:
            return
        PlayerPos.GetLoc().setScene()
        if transition:
            renpy.with_statement(transition)
        return
    
    # internal, replaces default renpy scene call. arguments req-d. to match renpy.scene signature
    def ClearScene(layer = "master"): 
        renpy.scene(layer = "master")
        renpy.scene(layer = "scene_objects")
        renpy.scene(layer = "vfx")
        renpy.scene(layer = "characters")
        return