import pygame

# W - сторона окна 
# N - количество клеток
pygame.init()
W, N = map(int, input().split())
size = (W, W)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
a = 0
b = 0
cell_x = 0 
cell_y = 0 
cell_height = (W // N)
cell_width = (W // N) 
board_height = cell_height * N
board_width = cell_width * N 
cell_color = pygame.Color('black')
if W % N == 0:
    for i in range(N * N):
        pygame.draw.rect(screen, cell_color, (cell_x, cell_y, cell_height, cell_width), 0)
        if cell_color == pygame.Color('black'):
            cell_color = pygame.Color('white')
        else:   
            cell_color = pygame.Color('black')
            
        cell_y += cell_width
        if cell_y == board_height:
            cell_y = 0
            cell_x += cell_width
            if cell_color == pygame.Color('black'):
                cell_color = pygame.Color('white')
            else:   
                cell_color = pygame.Color('black')

        pygame.display.flip()
else:
    print('W не кратно N')
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()