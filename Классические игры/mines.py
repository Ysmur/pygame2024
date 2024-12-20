import random

from board_file import Board
import pygame


class Minesweeper(Board):
    # создание поля
    def __init__(self, width, height, mines):
        super().__init__(width, height)
        self.mines = mines
        self.board = [[-1] * self.width for _ in range(self.height)]
        tmp = self.mines
        while tmp:
            x = random.randrange(0, self.width)
            y = random.randrange(0, self.height)
            if self.board[y][x] != 10:
                self.board[y][x] = 10
                tmp -= 1


    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 10:
                    pygame.draw.rect(screen, pygame.Color(0, 255, 0),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                if 0 <= self.board[y][x] <= 8:
                    font = pygame.font.Font(None, 50)
                    text = font.render(str(self.board[y][x]), True, (100, 255, 100))
                    screen.blit(text, (x * self.cell_size + self.left, y * self.cell_size + self.top))
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        print(cell)
        self.open_cell(cell)

    def open_cell(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            return
        s = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                    continue
                if self.board[y + dy][x + dx] == 10:
                    s += 1
        self.board[y][x] = s


def main():
    pygame.init()
    size = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60

    board = Minesweeper(5, 5, 3)
    board.set_view(1, 1, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            # Генерируем следующее поколение по нажатию клавиши "пробел"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()