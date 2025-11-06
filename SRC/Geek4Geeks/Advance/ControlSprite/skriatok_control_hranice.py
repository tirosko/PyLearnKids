# import random
import pygame
# https://www.geeksforgeeks.org/python/pygame-control-sprites/

# Global Variables
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500

# Object class


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        # keep inside right boundary
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # keep inside left boundary
        if self.rect.x < 0:
            self.rect.x = 0

    def moveForward(self, pixels):
        # moving downwards by fixed pixels
        self.rect.y += int(pixels)
        # keep inside bottom boundary
        if self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height

    def moveBack(self, pixels):
        # moving upwards by fixed pixels
        self.rect.y -= int(pixels)
        # keep inside top boundary
        if self.rect.y < 0:
            self.rect.y = 0


pygame.init()


RED = (255, 0, 0)


size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")


all_sprites_list = pygame.sprite.Group()

playerCar = Sprite(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
step = 2


all_sprites_list.add(playerCar)

exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(step)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(step)
    if keys[pygame.K_DOWN]:
        playerCar.moveForward(step)
    if keys[pygame.K_UP]:
        playerCar.moveBack(step)

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
