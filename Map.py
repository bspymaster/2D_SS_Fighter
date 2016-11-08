import pygame
class Map:
    def __init__(self,_imageName):
        self.imageName = _imageName

    def createMap(self):
        # load image
        mapImageSurface = pygame.image.load(self.imageName)

        # iterate through image
        for y in range(0,mapImageSurface.get_width()):
            rowText = ""
            for x in range(0,mapImageSurface.get_height()):
                pixelColor = mapImageSurface.get_at_mapped((x,y))
                if pixelColor == 0:
                    rowText += "0"
                else:
                    rowText += " "
            print(rowText)

            # TODO: return a list of what to build
