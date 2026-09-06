init python:
    def clearPersistent():
        persistent._clear(progress=True)
        newPersDict = {}
        for key,value in persistent.__dict__.items():
            if key.startswith("_"):
                newPersDict[key] = value
                if key == "_seen_translates":
                    newPersDict[key] = set()
                if key == "_seen_audio":
                    newPersDict[key] = {}
                if key == "_console_line_history":
                    newPersDict[key] = []
                if key == "_placeholder_gender":
                    newPersDict[key] = {}
        persistent.__dict__ = newPersDict
        renpy.quit(relaunch=True)

    def delSaves():
        for filename in renpy.list_slots():
            renpy.unlink_save(filename)
