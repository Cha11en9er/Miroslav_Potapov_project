import os
import pygame
import random

pygame.init()
size = (600, 300)
screen = pygame.display.set_mode(size)
#pygame.mouse.set_visible(False)
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
        image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

class Wall(pygame.sprite.Sprite):
    wall = load_image("gameover.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Wall.wall
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 150
 
all_sprites = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
pygame.quit()