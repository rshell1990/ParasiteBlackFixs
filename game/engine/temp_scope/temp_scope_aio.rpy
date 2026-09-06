init python:
    # experimental, yea its more cumbersome BUT we can do stuff with all the tmpvar interactions like this
    # might make sense longer-term, gonna try use it more
    def TmpGet(Key):
        return store.tmpvar[Key]

    def TmpSet(Key, Val):
        store.tmpvar[Key] = Val
        return

    def TmpFlush():
        store.tmpvar = {}
        return
