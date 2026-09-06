label dialogue_nothing:
    return

label processDialogue(topicTag):
    $ store.curDialogue = topicTag

label processDialogue_inner:
    $ optList = [(node.txtLabel,node) for node in getNodesFor(curDialogue)]
    $ optList.sort(key=lambda x: x[1].order, reverse=True)
    if len(optList) == 0:
        $ optList = [(debugNode.txtLabel, debugNode)]
    # Display menu and get input
    $ currentDNode = renpy.display_menu(optList)
    $ store.curDialogue = getAdjustedTag(curDialogue, currentDNode.nextNode)
    $ renpy.call(currentDNode.label)
    if curDialogue == "DNodeExit":
        return
    jump processDialogue_inner

###############################################
#                                             #
#  CENTER A TEXT IN THE MIDDLE OF THE SCREEN  #
#                                             #
###############################################

#
# "pause_" parameter: Use "None" if you want to force the player to click to hide the text
#
# call center_text(_("An hour later..."), pause_=None)
#
label center_text(msg, transition=fade, pause_=1.5):
    scene black with transition
    show center_ellipsis _(msg) at truecenter with dissolve
    pause pause_
    hide center_ellipsis with dissolve
    return

init -1:
    image center_ellipsis = renpy.ParameterizedText(style = "center_ellipsis_text")

#
# Style used for the text centered on the screen
#
style center_ellipsis_text is centered_text:
    size 72
