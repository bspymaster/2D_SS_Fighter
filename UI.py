import pygame
import Map
import Wall
import GlobalVars


class UI:
    # constructor
    def __init__(self):
        # Initialize Pygame and create window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((GlobalVars.SCREENWIDTH, GlobalVars.SCREENHEIGHT))
        pygame.display.set_caption("Jake & Ben's Fall Break Project")
        self.clock = pygame.time.Clock()

        self.entities = pygame.sprite.Group()
        self.playerEntities = pygame.sprite.Group()
        self.nonUpdatedEntities = pygame.sprite.Group()

        self.gameMap = None

        self.run()

    # update the on screen visuals
    def update(self):
        self.entities.update()
        self.playerEntities.update()

        self.screen.fill(GlobalVars.COLORS["BLACK"])

        self.nonUpdatedEntities.draw(self.screen)
        self.entities.draw(self.screen)
        self.playerEntities.draw(self.screen)

        pygame.display.flip()

    # get user input
    # returns: boolean reflecting if the user stopped the program
    def getInput(self):
        for event in pygame.event.get():
            # stuff
            if event.type == pygame.QUIT:
                return False
        return True

    # add an entity for the UI to manage
    # spriteToAdd (pygame.sprite.Sprite): the sprite of the entity for the UI to manage
    # typeOfEntity (integer): 0 if the entity never needs to be updated, 1 if the entity does (it moves/changes), 2 if it is a player character
    def addEntity(self, spriteToAdd, typeOfEntity):
        if typeOfEntity == 0:
            self.nonUpdatedEntities.add(spriteToAdd)
        elif typeOfEntity == 1:
            self.entities.add(spriteToAdd)
        elif typeOfEntity == 2:
            self.playerEntities.add(spriteToAdd)
        else:
            raise TypeError("The sprite cannot be added to that group.")

    # take an image of a map and parse it into the game
    # mapImageFile (String): a .png image, where each pixel represents the type of block to add to the map
    def setMap(self, mapImageFile):
        self.gameMap = Map.Map(mapImageFile)
        data = self.gameMap.createMap()

        for y in range(0, len(data)):
            for x in range(0, len(data[y])):
                if data[y][x] == "0x0":
                    wall = Wall.Wall(x*GlobalVars.SPRITEWIDTH, y*GlobalVars.SPRITEHEIGHT)
                    self.addEntity(wall, 0)

    # main game loop of the game
    def run(self):
        # Game loop

        self.setMap("map1.png")

        running = True
        while running:
            # process input
            running = self.getInput()

            # update the visuals
            self.update()

            # lock the screen to a certain FPS
            self.clock.tick(GlobalVars.FPS)
