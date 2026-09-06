init -4 python:
    def tra(str, scope = None): # subst shorthand
        return renpy.substitute(str, scope = scope)
