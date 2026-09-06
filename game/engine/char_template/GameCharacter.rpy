init python:
    # PB prefix to avoid shadowing renpy Character
    class PBCharacter:
        def __init__(self, CharID):
            self.CharID = CharID
            self.TemplateRef = store.CharDefs[self.CharID]
            self.derivedProps = {}

            # Set default values
            self.props = {k:copy.deepcopy(v) for (k, v) in self.TemplateRef.items() if not k.startswith("_")}

            if "_derived" in self.TemplateRef:
                self.derivedProps = self.TemplateRef["_derived"].copy()
            if "_functions" in self.TemplateRef:
                for funName, funObj in self.TemplateRef["_functions"].items():
                    setattr(self, funName, types.MethodType(funObj, self))            
        
        def AddMissingPropsFromTemplate(self):
            VerboseLog_General = False
            for k, v in self.TemplateRef.items():
                if not k.startswith("_"):
                    if k not in self.props:
                        if VerboseLog_General:
                            print("save update: adding missing field %s to char %s with a default value of %s" % (k, self.CharID, v))
                        self.props[k] = v

        def __repr__(self):
            funList = []
            if "_functions" in self.TemplateRef:
                funList = self.TemplateRef["_functions"].keys()
            derivedVals = {}
            for key, fun in self.derivedProps.items():
                try:
                    derivedVals[key] = fun(self)
                except:
                    derivedVals[key] = None
            return "PBCharacter(Main: %s, Derived: %s)" % (str(self.props), str(derivedVals))

        def keys(self):
            return self.props.keys() + self.derivedProps.keys()

        def __contains__(self,key):
            return (key in self.props) or (key in self.derivedProps)

        def __getitem__(self, key, **kwargs):
            if key in self.derivedProps:
                return self.derivedProps[key](self, **kwargs)
            elif key in self.props:
                return self.props[key]
            else:
                raise Exception("Key '%s' not found on char '%s'" % (key, self.CharID))

        def __setitem__(self, key, value):
            #self.props[key] = value
            if key in self.props:
                self.props[key] = value
            else:
                raise Exception("Key '%s' not found on char '%s'" % (key, self.CharID))

        def get(self, key, default = None, **kwargs):
            if self.__contains__(key):
                return self.__getitem__(key, **kwargs)
            else:
                return default

        # WARNING: only used for char attributes screen. to do the copy shenanigans.
        # As of 20.04.2024 I see no scenario of this backfiring.
        # if you do, hit me -tmm
        def __eq__(self, other):
            return all([self.derivedProps == other.derivedProps, 
                        self.TemplateRef == other.TemplateRef, 
                        self.props == other.props, 
                        self.CharID == other.CharID])

    def CreateWorldCharFromID(CharID):
        store.worldChars[CharID] = PBCharacter(CharID)
        CharHeal(CharID)
        CharRestoreEnergy(CharID)
        CharRestoreMana(CharID)
        return