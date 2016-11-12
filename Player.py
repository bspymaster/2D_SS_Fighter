import pygame

import GlobalVars


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((GlobalVars.SPRITEWIDTH, GlobalVars.SPRITEHEIGHT))
        self.image.fill(GlobalVars.COLORS["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass