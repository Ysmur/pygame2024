import os
import sys
import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # if colorkey is not None:
    #     image = image.convert()
    #     if colorkey == -1:
    #         colorkey = image.get_at((0, 0))
    #     image.set_colorkey(colorkey)
    # else:
    #     image = image.convert_alpha()
    return image

class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self, height):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height

class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos, mountain):
        super().__init__(all_sprites)
        self.mountain = mountain
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, self.mountain):
            self.rect = self.rect.move(0, 1)

def main():
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    FPS = 60
    mountain = Mountain(height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos, mountain)

        screen.fill((176, 206, 189))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    main()