import pygame


class Map:
    def __init__(self,_imageName):
        self.imageName = _imageName

    def createMap(self):
        # load image
        mapImageSurface = pygame.image.load("maps/{0}".format(self.imageName))

        columnData = []

        # iterate through image
        for x in range(0,mapImageSurface.get_width()):
            rowData = []
            for y in range(0,mapImageSurface.get_height()):
                pixelColor = hex(mapImageSurface.get_at_mapped((x, y)))
                rowData.append(pixelColor)

            columnData.append(rowData)

        return columnData
