import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
 
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + self.cell_size * (i + 1),
                self.top + self.cell_size * (j * 1), self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(self)

    def get_cell(self, mouse_pos):
        coord_x = (mouse_pos[0] - self.left) // self.cell_size
        coord_y = (mouse_pos[1] - self.top) // self.cell_size
        if coord_x <= 0 and coord_x > self.width or coord_y <= 0 and coord_y > self.height:
            return None
        return coord_x, coord_y

    def on_click(self, cell_coords):
        pass
            
                
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
board = Board(5, 7)
board.set_view(100, 100, 50)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(board.get_cell(pygame.mouse.get_pos()))
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()