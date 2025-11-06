import pygame
# import random

# GLOBAL VARIABLES
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
        # make the filled background transparent
        self.image.set_colorkey(SURFACE_COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


class SpriteC(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        """A circular sprite drawn on a surface of size (width, height).

        Parameters keep the same order as `Sprite` (color, height, width).
        The circle is centered in the surface and its radius is the largest
        that fits inside the surface.
        """
        super().__init__()

        # create surface and make SURFACE_COLOR transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        # make the filled background transparent
        self.image.set_colorkey(SURFACE_COLOR)

        # draw a centered circle that fits inside the surface
        center = (width // 2, height // 2)
        radius = min(width, height) // 2
        pygame.draw.circle(self.image, color, center, radius)

        # rect is used for positioning by sprite groups
        self.rect = self.image.get_rect()


pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creating Sprite")

all_sprites_list = pygame.sprite.Group()

object_ = Sprite(BLUE, 20, 30)
object_.rect.x = 200
object_.rect.y = 300


object_2 = Sprite(RED, 30, 40)
object_2.rect.x = 50
object_2.rect.y = 50

circle = SpriteC(GREEN, 50, 50)
circle.rect.x = 150
circle.rect.y = 100

all_sprites_list.add(object_, object_2, circle)

exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
