#Jake and Ben's super awesome game for funsies. Hire us pls

import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 900
HEIGHT = 600
FPS = 60

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

# Game loop
running = True

