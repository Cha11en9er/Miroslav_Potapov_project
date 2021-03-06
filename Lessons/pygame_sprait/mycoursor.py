import os
import pygame

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(False)
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


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("cursor.png")
# и размеры
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(sprite)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            sprite.rect.x = event.pos[0]
            sprite.rect.y = event.pos[1]
        if pygame.mouse.get_focused():
            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
        pygame.display.flip()
pygame.quit()
