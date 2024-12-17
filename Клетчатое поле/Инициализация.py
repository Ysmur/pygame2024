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

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
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
         screen.fill((0, 0, 0))
         board.render(screen)
         pygame.display.flip()

if __name__ == "__main__":
    main()

