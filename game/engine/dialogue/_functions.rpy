init python:
    staticTopics = {}
    def addDialogueNode(fullTag,node):
        if fullTag not in staticTopics:
            staticTopics[fullTag] = []
        staticTopics[fullTag].append(node)

    def getNodesFor(fullTag):
        if fullTag in staticTopics:
            rv = [x for x in staticTopics[fullTag]]
        else:
            rv = []

        # Add quest nodes
        for qstObj in GetAllActiveQuests():
            if hasattr(qstObj,"extraDialogue"):
                for tag, dNode in qstObj.extraDialogue():
                    if tag == fullTag:
                        if isinstance(dNode,list):
                            rv.extend(dNode)
                        else:
                            rv.append(dNode)
        return [node for node in rv]

    def getAdjustedTag(curFullTag,nextTag):
        if nextTag is None:
            return curFullTag
        elif nextTag.startswith("_"):
            # relative
            rootTag = curFullTag.split("_")[0]
            return rootTag + nextTag
        else:
            return nextTag
