init -1 python:
    # world LOCATION is "novaras church", world POSITION is "mc is currently AT novaras church"
    class WorldLocation(object):
        def __init__(self, tag, displayName, bgImage, questMarkers = True, parent = None, WorldMapRootLocTag = None):
            wLocs[tag] = self
            self.tag = tag
            self.displayName = displayName
            self.bgImage = bgImage
            self.btns = {}
            self.questMarkers = questMarkers
            self.parentTag = parent # Tag of parent location, or None
            self.parent = None
            self.dn_ambience = DaynightSound("ambience", None, None)
            self.dn_music = DaynightSound("music", None, None)
            self.sfxDict = {}
            self.routes = {}
            self.CanWait = True # is set to false for certain locs
            self.WorldMapRootLocTag = WorldMapRootLocTag

            # reinitialization of matrix happens at every time tick, from this class
            self.DayNightMatrixClass = None
            self.DayNightMatrix      = None

        def setParentRef(self):
            if self.parentTag is not None:
                self.parent = wLocs[self.parentTag]

        # == Setting Automatic Ambience Track ==
        def withDayAmbience(self,track):
            self.dn_ambience.dayTrack = track
            return self

        def withNightAmbience(self,track):
            self.dn_ambience.nightTrack = track
            return self

        def withGenAmbience(self,track):
            self.dn_ambience.dayTrack = track
            self.dn_ambience.nightTrack = track
            return self

        # == Setting Automatic Music Track ==
        def withDayMusic(self, track):
            self.dn_music.dayTrack = track
            return self

        def withNightMusic(self, track):
            self.dn_music.nightTrack = track
            return self

        def withGenMusic(self, track):
            self.dn_music.dayTrack = track
            self.dn_music.nightTrack = track
            return self

        # == End of automatic tracks ===
        def setScene(self):
            renpy.config.scene()

            SetGlobalAmbienceAndMusic(self)
            soundUpdate()

            TargetTag = self.bgImage

            for QuestObj in GetAllActiveQuests():
                if hasattr(QuestObj, "OverrideLocBg"):
                    BgDict = QuestObj.OverrideLocBg()
                    if len(BgDict) > 0:
                        if self.tag in BgDict:
                            TargetTag = BgDict[self.tag]

            # update tint matrix
            if self.DayNightMatrixClass is not None:
                self.DayNightMatrix = self.DayNightMatrixClass(GetDaytimeTintFactor())

            # if its night and if we have night image to show, show night un-tinted image
            ShowNightImg = False
            if IsInTimeFrame(TIME_DAY_END, TIME_DAY_START):
                if renpy.has_image(TargetTag + "_night"):
                    ShowNightImg = True
            if ShowNightImg:
                renpy.show("bg_dynamic", what = Transform(TargetTag + "_night", matrixcolor = None))
            else:
                renpy.show("bg_dynamic", what = Transform(TargetTag, matrixcolor = self.DayNightMatrix))

            renpy.show_screen("location_light_overlay", self.tag, _layer = "vfx")
            return

        def UpdateAllDynSound(self): # for cases where you traverse locations directly but want sound to play from wloc defs
            SetGlobalAmbienceAndMusic(self)
            soundUpdate()
            return

        def withActionSFXs(self, btnSfxDict):
            self.sfxDict = btnSfxDict
            return self

        def SetDayNightMatrixClass(self, Value):
            self.DayNightMatrixClass = Value
            if Value is not None:
                self.DayNightMatrix = Value()
            else:
                self.DayNightMatrix = None
            return self

        def withBtn(self, tag, btnBehaviour):
            self.btns[tag] = btnBehaviour
            return self

        def _getBtn(self, btnTag):
            locMods = []
            for qstObj in GetAllActiveQuests():
                if not hasattr(qstObj, "locationMod"):
                    continue
                locMod = qstObj.locationMod()
                if locMod is not None:
                    modValue = locMod.modBtn(btnTag)
                    if modValue is not None:
                        locMods.append(locMod)

            if locMods:
                if len(locMods) > 1:
                    locMods.sort(key = lambda x: x.priority, reverse = True)
                return locMods[0].modBtn(btnTag)

            # default behaviour
            if btnTag in self.btns:
                return self.btns[btnTag]
            else:
                return BtnDisabled()

        def isBtnQuestTracked(self, BtnID):
            if not self.questMarkers:
                return False
            for qstObj in GetAllActiveQuests():
                if qstObj.isTracked:
                    for GoalKey, GoalVal in qstObj.GoalStates.items():
                        if GoalVal == GoalState.VISIBLE:
                            TrackTags = []
                            if qstObj.GOALS[GoalKey].TrackTag is not None:
                                if isinstance(qstObj.GOALS[GoalKey].TrackTag, list):
                                    TrackTags = qstObj.GOALS[GoalKey].TrackTag
                                else:
                                    TrackTags = [qstObj.GOALS[GoalKey].TrackTag]
                            for TrackTag in TrackTags:
                                if BtnID == TrackTag:
                                    return True
            for NoteID in unlockedNotes:
                if getattr(notesLib[NoteID], "trackTag", None) == BtnID:
                    return True
            return False

        def isBtnEnabled(self,tag):
            return self._getBtn(tag).isEnabled()

        def getHoverTxt(self,tag):
            if DEV_VARIABLES["HOVER_BTN_TAGS"]:
                return tra(self._getBtn(tag).getHoverTxt()) + "\n{color=#949494}" + "(DEV) button tag: " + tag + "{/color}"
            else:
                return tra(self._getBtn(tag).getHoverTxt())

        def executeBtn(self, tag):
            TooltipClear()
            if tag in self.sfxDict:
                soundVal = self.sfxDict[tag]
                if isinstance(soundVal,list):
                    soundVal = renpy.random.choice(soundVal)
                return self._getBtn(tag).withSfx(soundVal).execute()
            else:
                return self._getBtn(tag).execute()

        # so that a loc can has world map repr
        def withWorldMap(self, displayName, connectsTo, spritePath, spritePos):
            self.wMap_DisplayName = displayName
            self.wMap_connectsTo = connectsTo # a list of wloc IDs
            self.wMap_spritePath = spritePath
            self.wMap_spritePos = spritePos # CENTER OF IMAGE! not top-left corner!
            return self

    def SetGlobalAmbienceAndMusic(WorldLocObject):
        store.dynamicAmbience = copy.copy(WorldLocObject.dn_ambience)
        store.dynamicMusic = copy.copy(WorldLocObject.dn_music)

        for QuestObj in GetAllActiveQuests():
            if hasattr(QuestObj, "OverrideAmbienceOrMusicTrack"):
                AmbienceOrMusicTrackReplacement = QuestObj.OverrideAmbienceOrMusicTrack()
                if AmbienceOrMusicTrackReplacement is not None:
                    for TrackToReplacePath, TrackToReplaceWithPath in AmbienceOrMusicTrackReplacement.items():
                        if store.dynamicAmbience.dayTrack == TrackToReplacePath:
                            store.dynamicAmbience.dayTrack = TrackToReplaceWithPath

                        if store.dynamicAmbience.nightTrack == TrackToReplacePath:
                            store.dynamicAmbience.nightTrack = TrackToReplaceWithPath

                        if store.dynamicMusic.dayTrack == TrackToReplacePath:
                            store.dynamicMusic.dayTrack = TrackToReplaceWithPath

                        if store.dynamicMusic.nightTrack == TrackToReplacePath:
                            store.dynamicMusic.nightTrack = TrackToReplaceWithPath
        return

    # this is also used by complex buttons, for tint
    def GetDaytimeTintFactor():
        Result = 1.0
        FULLLIGHT_START =   TIME_MORNING
        FULLLIGHT_END =     TIME_DUSK

        FULLDARK_START =    TIME_LATEEVENING
        FULLDARK_END =      TIME_DAWN

        # case 1 morning->dusk, constant 1.0 (its day)
        if IsInTimeFrame(FULLLIGHT_START, FULLLIGHT_END):
            Result = 1.0

        # case 2 dusk->evening, darken from 1.0 to 0.0 dep on span
        elif IsInTimeFrame(FULLLIGHT_END, FULLDARK_START):
            Diff = FULLDARK_START - FULLLIGHT_END
            CurrentTimeTruncated = rpTime - FULLLIGHT_END
            Ratio = CurrentTimeTruncated / Diff
            Result = 1.0 - Ratio

        # case 3 lightend->lightstart, 0.0 darkness
        elif IsInTimeFrame(FULLDARK_START, FULLDARK_END):
            Result = 0.0

        # case 4 dawn->morning, 0.0 to 1.0 
        elif IsInTimeFrame(FULLDARK_END, FULLLIGHT_START):
            Diff = FULLLIGHT_START - FULLDARK_END
            CurrentTimeTruncated = rpTime - FULLDARK_END
            Result = CurrentTimeTruncated / Diff

        return Result

    def DEBUG_VisitAllLocations():
        renpy.jump("debug_visit_all_locations")

label debug_visit_all_locations:
    $ debugvar = {}
    $ debugvar["orig_loc"] = GetLocID()
    $ debugvar["alllocs"] = [LocID for LocID in wLocs.keys()]
    $ debugvar["curlocindex"] = 0
    while(debugvar["curlocindex"] < len(debugvar["alllocs"])):
        $ LocSet(debugvar["alllocs"][debugvar["curlocindex"]])
        $ LocFlush(Dissolve(0.01))
        $ renpy.show_screen("loc_%s" % GetLocID(), _layer = "scene_objects")
        with Dissolve(0.01)
        pause 0.5
        $ debugvar["curlocindex"] += 1
    $ LocSet(debugvar["orig_loc"])
    $ LocEnter()