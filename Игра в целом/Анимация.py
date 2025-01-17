import os
import random
import sys
import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, app, sheet, columns, rows, x, y):
        super().__init__(app.all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера

    def __init__(self, pos, dx, dy):
        super().__init__(app.par_sprites)
        self.fire = [app.load_image("star.png")]
        for scale in (5, 10, 20):
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.1

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(app.screen_rect):
            self.kill()


class App:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Mario')
        #pygame.key.set_repeat(200, 70)
        self.tile_width = self.tile_height = 50
        self.all_sprites = pygame.sprite.Group()
        self.par_sprites = pygame.sprite.Group()
        dragon = AnimatedSprite(self, self.load_image("pygame-8-1.png"), 8, 2, 50, 50)
        self.fps = 30
        self.screen_rect = (0, 0, self.width, self.height)


    def terminate(self):
        pygame.quit()
        sys.exit()

    def load_image(self, name, colorkey=None):
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

    def create_particles(self, position):
        # количество создаваемых частиц
        particle_count = 20
        # возможные скорости
        numbers = range(-5, 6)
        for _ in range(particle_count):
            Particle(position, random.choice(numbers), random.choice(numbers))

    def end_screen(self):
        intro_text = ["Game over"]

        fon = pygame.transform.scale(self.load_image('fon.jpg'), (self.width, self.height))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50

        string_rendered = font.render(intro_text[0], 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # создаём частицы по щелчку мыши
                    self.create_particles(pygame.mouse.get_pos())
            self.par_sprites.update()
            self.par_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

    def run_game(self):
        run = True
        self.game_over = 0

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    run = False
                    self.end_screen()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.hero.update((0, self.tile_height))
            if keys[pygame.K_UP]:
                self.hero.update((0, -self.tile_height))
            if keys[pygame.K_LEFT]:
                self.hero.update((-self.tile_width, 0))
            if keys[pygame.K_RIGHT]:
                self.hero.update((self.tile_width, 0))
            if self.game_over == 5:
                self.start_screen()
                run = False

            self.screen.fill(pygame.Color('blue'))
            self.all_sprites.draw(self.screen)
            self.all_sprites.update()
            pygame.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = App()
    app.run_game()