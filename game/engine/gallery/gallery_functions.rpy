default persistent.galleryUnlocks = dict() # [charID][sceneID] = {unlocked:t/f,flags:[]}
default PlayerInGallery = False # for not being able to save in gallery scene (bad for compat)

default PlaythroughSeenGallerySceneIDs = set() # this will grant xp if player sees scene for the first time
# it might get polluted with redundant entries on saves as categoryIDs and sceneIDs are changed but whatever right? RIGHT?

init python:
    def UnlockGalSceneAndGrantXp(CatID, SceneID, GrantXP = True):
        if _in_replay:
            return
        ### grant xp if havent seen the cat+scene yet
        if GrantXP: # switch just in case we'll want a non-exp-granting scene
            if CatID + SceneID not in PlaythroughSeenGallerySceneIDs:
                AddExpPlayer(80)
                PlaythroughSeenGallerySceneIDs.add(CatID + SceneID)
        GallerySceneEnsurePersistentRecord(CatID, SceneID)
        if not persistent.galleryUnlocks[CatID][SceneID]["unlocked"]:
            persistent.galleryUnlocks[CatID][SceneID]["unlocked"] = True
            AddNotif(_("Scene unlocked!"), Kind = "scene_unlocked")
        return

    def UnlockGalFlag(CatID, SceneID, flagID, notify = True):
        if _in_replay:
            return
        GallerySceneEnsurePersistentRecord(CatID, SceneID)
        if flagID not in persistent.galleryUnlocks[CatID][SceneID]["flags"]:
            if len(persistent.galleryUnlocks[CatID][SceneID]["flags"]) > 0:
                if persistent.galleryUnlocks[CatID][SceneID]["unlocked"] == True:
                    if notify:
                        AddNotif(_("Scene memory updated!"), Kind = "scene_updated")
            persistent.galleryUnlocks[CatID][SceneID]["flags"].add(flagID)
        return

    def GalUnlockAllScenes():
        for catID in lewdsGalleryLib:
            for sceneID in lewdsGalleryLib[catID]["scenes"]:
                UnlockGalSceneAndGrantXp(catID, sceneID, GrantXP = False)
                if "flags" in lewdsGalleryLib[catID]["scenes"][sceneID]:
                    for flagID in lewdsGalleryLib[catID]["scenes"][sceneID]["flags"]:
                        UnlockGalFlag(catID,sceneID,flagID)
        return

    def GalLockAllScenes():
        persistent.galleryUnlocks = dict()
        return

    # check if one *or multiple* flags in gallery category. 'any' will return True if there's a single list match
    def GalFlag(catID, sceneID, flagID, anymatch = False):
        GallerySceneEnsurePersistentRecord(catID, sceneID)
        targetSceneFlags = persistent.galleryUnlocks[catID][sceneID]["flags"]
        if isinstance(flagID, list):
            if len(flagID) == 0:
                return False
            flagsIn = 0
            for flag in flagID:
                if flag in targetSceneFlags:
                    if anymatch:
                        return True
                    flagsIn += 1
            if flagsIn == len(flagID):
                return True
            else:
                return False
        return True if flagID in persistent.galleryUnlocks[catID][sceneID]["flags"] else False

    # returns a list of ["a_derp", "b_derp"] from ["d_herp", "c_hurr", "a_derp", "b_derp"] (if queried for a_derp, b_derp)
    def GalFlagsWithSubstring(CatID, SceneID, SubString):
        GallerySceneEnsurePersistentRecord(CatID, SceneID)
        Result = []
        TargetSceneFlags = persistent.galleryUnlocks[CatID][SceneID]["flags"]
        for Flag in TargetSceneFlags:
            if SubString in Flag:
                Result.append(Flag)
        return Result

    def GalFlagsWithSubstringAmt(CatID, SceneID, Substring):
        return len(GalFlagsWithSubstring(CatID, SceneID, Substring))

    def GalFlagCount(CatID, sceneID): # shorthand for len
        GallerySceneEnsurePersistentRecord(CatID, sceneID)
        return len(persistent.galleryUnlocks[CatID][sceneID]["flags"])

######################### internals more or less
    # its both doing "Create" and "asserts" 
    def GallerySceneEnsurePersistentRecord(CatID, SceneID):
        # check against lewdsgal
        Assert(CatID in lewdsGalleryLib, "category id %s not found in lewdsgallerylib" % CatID)
        Assert("scenes" in lewdsGalleryLib[CatID], "scenes not defined for category %s" % CatID)
        Assert(SceneID in lewdsGalleryLib[CatID]["scenes"], "scene ID not in scenes for %s" % CatID)

        # write persistent record
        if CatID not in persistent.galleryUnlocks:
            persistent.galleryUnlocks[CatID] = {}
        if SceneID not in persistent.galleryUnlocks[CatID]:
            persistent.galleryUnlocks[CatID][SceneID] = {}
        if "unlocked" not in persistent.galleryUnlocks[CatID][SceneID]:
            persistent.galleryUnlocks[CatID][SceneID]["unlocked"] = False
        if "flags" not in persistent.galleryUnlocks[CatID][SceneID]:
            persistent.galleryUnlocks[CatID][SceneID]["flags"] = set()
        return

    def IsPlayerInGalleryScene():
        if (store.PlayerInGallery == True) or (_in_replay == None):
            return False
        return True
