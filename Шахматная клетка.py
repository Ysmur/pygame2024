import  pygame

def grid(size, n):
    k = 1 # всегда нижняя левая клетка черная
    for y in range((n - 1) * size, -1, -1 * size):
        print(y, k)
        if k:
            for x in range(0, size * n, 2 * size):
                pygame.draw.rect(screen, pygame.Color('#ffdddd'), (x + size, y, size, size))
            k = 0
        else:
            for x in range(0, size * n, 2 * size):
                pygame.draw.rect(screen, pygame.Color('#dddddd'), (x, y, size, size))
            k = 1


if __name__ == "__main__":
    try:
        a, n = [int(x) for x in input().split()]
        pygame.init()
        pygame.display.set_caption("Шахматная клетка")
        screen = pygame.display.set_mode((a, a))
        grid(a // n, n)
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')