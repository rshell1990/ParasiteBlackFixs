# what this does is, lets you glance all the non-default globals we've introduced

# init -999 python:
#     if config.developer:
#         RenpyGlobals = copy.deepcopy(list(globals().keys()))

# init 999 python:
#     if config.developer:
#         AllGlobals = copy.deepcopy(list(globals().keys()))
#         for Entry in RenpyGlobals:
#             AllGlobals.remove(Entry)
#         AllGlobals.sort()