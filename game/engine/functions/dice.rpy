init python:
    def dice(Amount, sides):
        returnVal = 0
        for i in range(0, Amount):
            returnVal += RngInt(1, sides)
        return returnVal

    # NOT JUST A shorthand for random.randint(incl.)
    # but also makes devmode random non-revertable
    # inclusive on both ends
    def RngInt(range_a, range_b): 
        # in developer mode, random is "real"
        if config.developer:
            return random.randint(range_a, range_b)
        # in public mode, random is rigged (rollback stores seed)
        else:
            return renpy.random.randint(range_a, range_b)

    # inclusive on both ends
    def RngFloat(RangeA, RangeB):
        # in developer mode, random is "real"
        if config.developer:
            return random.uniform(RangeA, RangeB)
        # in public mode, random is rigged (rollback stores seed)
        else:
            return renpy.random.uniform(RangeA, RangeB)
