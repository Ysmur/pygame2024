import pygame
import os
import sys


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


class Hero(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('creature.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]



def main():
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60

    heros = pygame.sprite.Group()
    arrow = Hero(heros)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            heros.update((0, 10))
        if keys[pygame.K_UP]:
            heros.update((0, -10))
        screen.fill((176, 206, 189))
        heros.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()