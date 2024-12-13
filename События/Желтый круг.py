import pygame

pygame.init()
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption('yellow_circle')
MYEVENTTYPE = 30
radius = 0
pos_circle = (-10, -10)


def draw(pos, r):

    pygame.draw.circle(screen, (255, 255, 0), pos, r)

screen.fill((0, 0, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((0, 0, 255))
            pos_circle = event.pos
            radius = 10
            draw(pos_circle, radius)
            pygame.time.set_timer(MYEVENTTYPE, 100)

        if event.type == MYEVENTTYPE:
            radius += 10
            draw(pos_circle, radius)

    pygame.display.flip()

pygame.quit()