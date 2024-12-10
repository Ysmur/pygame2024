import pygame

def draw(w, n):
    for x in range(n, -1, -1):
        pygame.draw.circle(screen, pygame.Color(colors[x % 3]),
                           (n * w * 2 // 2, n * w * 2 // 2), x * w)

w = 20
n = 10
colors = ['#ff0000', '#00ff00', '#0000ff']
pygame.init()
screen = pygame.display.set_mode((n * w * 2, n * w * 2))
pygame.display.set_caption('first')

draw(w, n)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()