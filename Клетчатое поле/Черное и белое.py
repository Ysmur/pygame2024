import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= cell_x < self.width and 0 <= cell_y < self.height:
            return cell_x, cell_y

    def on_click(self, cell_coords):
        cell_x, cell_y = cell_coords
        for x in range(self.width):
            self.board[cell_y][x] += 1
        for y in range(self.height):
            self.board[y][cell_x] += 1
        self.board[cell_y][cell_x] += 1

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] % 2:
                    pygame.draw.rect(screen, (125, 125, 125), ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                                       (self.cell_size, self.cell_size)))

                pygame.draw.rect(screen, (0, 255, 0), ((self.left + x * self.cell_size, self.top + y * self.cell_size),
                                                       (self.cell_size, self.cell_size)), 1)


def main():
     pygame.init()
     screen = pygame.display.set_mode((500, 500))
     board = Board(5, 7)

     running = True
     while running:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             if event.type == pygame.MOUSEBUTTONDOWN:
                 board.get_click(event.pos)
         screen.fill((0, 0, 0))
         board.render(screen)
         pygame.display.flip()

if __name__ == "__main__":
    main()

