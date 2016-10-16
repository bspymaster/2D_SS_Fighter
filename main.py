#Jake and Ben's super awesome game for funsies. Hire us pls

import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 1024
HEIGHT = 700
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jake & Ben's Fall Break Project")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
        
    def update(self):
        pass
        #self.rect.x += 5
        #self.rect.x += -5
        
all_sprites = pygame.sprite.Group()   
player = Player()
all_sprites.add(player)     
# Game loop
running = True
while running:
    clock.tick(FPS)
    # Process input
    for event in pygame.event.get():
        # stuff
        if event.type == pygame.QUIT:
            running = False
            
    # Update
    all_sprites.update()
    
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    
pygame.quit()
    

