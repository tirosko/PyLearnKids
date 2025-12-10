import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

sprites = []
for i in range(50):
    surf = pygame.Surface((20, 20))
    surf.fill((random.randint(50,255), random.randint(50,255), random.randint(50,255)))
    rect = pygame.FRect(random.uniform(0, 600), random.uniform(0, 440), 20, 20)
    speed = random.uniform(0.5, 2.0)
    sprites.append((surf, rect, speed))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    blit_list = []
    for surf, rect, speed in sprites:
        rect.x += speed  # float rect → smooth motion
        if rect.x > 640:
            rect.x = -20
        blit_list.append((surf, rect))

    pygame.fblits(blit_list)  # batch blitting for speed
    pygame.display.flip()
    clock.tick(60)

pygame.quit()