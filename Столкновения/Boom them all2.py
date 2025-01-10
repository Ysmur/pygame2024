import pygame
import os
import sys
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    def __init__(self, width, height, bombs):
        super().__init__(bombs)
        self.image = load_image('bomb.png')
        self.rect = self.image.get_rect()
        while True:
            self.rect.x = random.randrange(0, width - self.rect.width)
            self.rect.y = random.randrange(height - self.rect.height)
            if len(pygame.sprite.spritecollide(self, bombs, False)) == 1:
                break

    def update(self, *pos):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if pos:
            self.get_click(pos)

    def get_click(self, pos):
        if self.rect.collidepoint(pos):
            self.image = load_image('boom.png')



def main():
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60


    for i in range(10):
        Bomb(width, height, bombs)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bombs.update(event.pos)
                # for bomb in bombs:
                #     bomb.get_click(event.pos)
        screen.fill((176, 206, 189))
        bombs.draw(screen)
        bombs.update()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    bombs = pygame.sprite.Group()
    main()