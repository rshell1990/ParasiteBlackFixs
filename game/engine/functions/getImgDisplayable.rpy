init python:
    def getImgDisplayable(imgName):
        return renpy.display.image.images[tuple(imgName.split())]