# Jake and Ben's super awesome game for funsies. Hire us pls

import pygame

# Import local classes
import UI

# Create an instance of a UI and start it
ui = UI.UI()

"""
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        pass
        # self.rect.x += 5
        # self.rect.x += -5
"""

pygame.quit()
