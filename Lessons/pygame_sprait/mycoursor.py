import os
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    print(fullname)
    try:
        image1 = pygame.image.load('cursor.png')
        print('Immage was loaded:', name)        
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)  


pygame.init() 
screen = pygame.display.set_mode((800,600),0,32) 

mainLoop = True
showimage = True

  
while mainLoop:
    if showimage:
        showimage = False
        print('------------------------Immage was loaded:')    
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    white = [255, 255, 255]
    red = [255, 0, 0]
    screen.fill(white)
    newSurf = pygame.Surface((800, 600))
    image1 = pygame.image.load('cursor.png') 
    newSurf.blit(image1, (0,0)) 
    pygame.display.flip()