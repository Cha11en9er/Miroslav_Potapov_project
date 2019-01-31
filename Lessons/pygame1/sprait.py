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
    bomb = load_image("boom.png")
    image = load_image("bomb.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Wall.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(500)
        self.rect.y = random.randrange(500)
 
    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
 
    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)

# Поручим бомбочке получать событие и взрываться (поменяем картинку)
    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.image = self.boob

# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим спрайт
# sprite = pygame.sprite.Sprite()
# определим его вид
# sprite.image = load_image("cursor2.png")
# и размеры
# sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
# all_sprites.add(sprite)
for _ in range(50):
    Wall(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
pygame.quit()

