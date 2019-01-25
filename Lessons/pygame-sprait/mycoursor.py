import os
import pygame

import os
 
 
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
load_image('cursor.jpg')