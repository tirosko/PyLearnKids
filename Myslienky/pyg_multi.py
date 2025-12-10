import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

sprites = []
for i in range(50):
    surf = pygame.Surface((20, 20))
    surf.fill((random.randint(50,255), random.randint(50,255), random.randint(50,255)))
    rect = surf.get_rect(topleft=(random.randint(0, 600), random.randint(0, 440)))
    sprites.append((surf, rect, random.uniform(0.5, 2.0)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for surf, rect, speed in sprites:
        rect.x += speed  # integer rect → truncated movement
        if rect.x > 640:
            rect.x = -20
        screen.blit(surf, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()