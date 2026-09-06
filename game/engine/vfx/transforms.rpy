init python:
    ########################
    # Class based transforms
    ########################

    # Makes object bop up and down using sine-wave function
    class FloatTrans(object):
        def __init__(self,cycleDur,maxOffset):
            self.cycleDur = cycleDur
            self.maxOffset = maxOffset

        def __call__(self,trans,st,at):
            deltaT = renpy.time.time()
            offset = self.maxOffset * math.sin(2.0*math.pi*(deltaT/self.cycleDur))
            trans.yoffset = offset
            return 0

    class MatrixPulseTrans(object):
        def __init__(self,cycleDur,matrixObj):
            self.cycleDur = cycleDur
            self.matrixObj = matrixObj

        def __call__(self,trans,st,at):
            deltaT = renpy.time.time()
            timeFrac = 0.5 + 0.5*math.sin(2.0*math.pi*(deltaT/self.cycleDur))
            trans.matrixcolor = _interpolateMatrices(Matrix.identity(),self.matrixObj,timeFrac)
            return 0

    # return m1 + (m2 - m1)*frac
    def _interpolateMatrices(m1,m2,frac):
        s1 = m1.__getstate__()
        s2 = m2.__getstate__()
        outState = {}
        for key, val in s1.items():
            if key != "origin":
                outState[key] = val + (s2[key] - val)*frac
        outM = Matrix(None)
        outM.__setstate__(outState)
        return outM

    # Performs a transition from matrixcolor matrix2 to matrix2
    # An optional timeWarpF function can be specified to remap the 0->1 transition space
    class MatrixTrans(object):
        def __init__(self,m1,m2,dur,timeWarpF=None,genTimeStart=None):
            self.m1 = m1
            self.m2 = m2
            self.dur = dur
            self.timeWarpF = timeWarpF
            self.genTimeStart = genTimeStart # If not None, indicates a renpy.time.time() relative to which animation is done

        def __call__(self,trans,st,at):
            if self.genTimeStart is None:
                timeSignal = st
            else:
                timeSignal = renpy.time.time() - self.genTimeStart
            timeFrac = st/self.dur
            timeFrac = min(max(0,timeFrac),1.0) # Restrict to 0-1 zone
            if self.timeWarpF != None:
                timeFrac = self.timeWrapF(timeFrac)
                timeFrac = min(max(0,timeFrac),1.0)

            trans.matrixcolor = _interpolateMatrices(self.m1,self.m2,timeFrac)
            if timeFrac == 1.0:
                return None
            return 0


    ###########################
    # Function based transforms
    ###########################

    def flicker_func(trans,st,at):
        trans.zoom = max(min(renpy.random.random(), 1.0), 0.9)
        return 0.1

    ###########
    # Constants
    ###########

    # Amplifies red channel and mutes others
    hurtMatrix = Matrix([   2.0, 0.0, 0.0, 0.0,
                            0.0, 0.5, 0.0, 0.0,
                            0.0, 0.0, 0.5, 0.0,
                            0.0, 0.0, 0.0, 1.0, ])

    # Amplifies green channel and mutes others
    healMatrix = Matrix([   0.5, 0.0, 0.0, 0.0,
                            0.0, 2.0, 0.0, 0.0,
                            0.0, 0.0, 0.5, 0.0,
                            0.0, 0.0, 0.0, 1.0, ])

    # Brightens
    enemySelMatrix = Matrix([   2, 0.0, 0.0, 0.0,
                                0.0, 2, 0.0, 0.0,
                                0.0, 0.0, 2, 0.0,
                                0.0, 0.0, 0.0, 1.0, ])

transform flicker(pos):
    pos (pos)
    anchor (0.5, 0.5)
    function flicker_func

transform battleSizeMultiplierFactor(fac):
    zoom fac

transform battleEnemySelTrans():
    function MatrixPulseTrans(2.0,enemySelMatrix)

transform battleSpriteDarken():
    matrixcolor SaturationMatrix(0.0)

transform battleSpritePosTrans(refPos):
    xanchor 0.5 yanchor 1.0 pos (refPos[0], refPos[1])

transform battleHurtTrans(tStart=None):
    matrixcolor hurtMatrix
    function MatrixTrans(hurtMatrix,Matrix.identity(),0.3,genTimeStart=tStart)

transform battleHealTrans(tStart=None):
    matrixcolor healMatrix
    function MatrixTrans(healMatrix,Matrix.identity(),0.3,genTimeStart=tStart)

transform battleDeathTrans():
    matrixcolor hurtMatrix
    linear 0.5 alpha 0

transform questMarkerFloat():
    subpixel True
    function FloatTrans(4,10)
