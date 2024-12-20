from board_file import Board
import pygame


class Lines(Board):
    # создание поля
    def __init__(self, width, height):
        super().__init__(width, height)
        self.red = (-1, -1)

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.ellipse(screen, pygame.Color(0, 0, 255),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                if self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, pygame.Color(255, 0, 0),
                                     (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        print(cell)
        if self.red != (-1, -1) and self.has_path(self.red, cell) != 100:
            self.board[self.red[1]][self.red[0]] = 0
            self.red = (-1, -1)
        if self.red != (-1, -1) and self.has_path(self.red, cell) == 100:
            return
        if self.board[cell[1]][cell[0]] % 2 == 0:
            self.board[cell[1]][cell[0]] = 1
        else:
            self.board[cell[1]][cell[0]] = 2
            self.red = (cell[0], cell[1])

    def has_path(self, start, finish):
        """ волновой алгоритм"""
        distance = [[100] * self.width for _ in range(self.height)]
        distance[start[1]][start[0]] = 0
        queue = [start]  # кортеж координат стартовой клетки
        while queue:
            x, y = queue.pop(0)  # удаляем первый в очереди
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, - 1):
                if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                    continue
                if self.board[y + dy][x + dx] == 0 and distance[y + dy][x + dx] == 100:
                    distance[y + dy][x + dx] = distance[y][x] + 1
                    queue.append((x + dx, y + dy))
        return distance[finish[1]][finish[0]]


def main():
    pygame.init()
    size = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60

    board = Lines(10, 10)
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