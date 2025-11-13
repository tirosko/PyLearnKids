# Importing the pygame module
import pygame
from pygame.locals import *
import random

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()


# Creating a new rect for first object
BUBLE_PRIEMER = random.randint(5, 50)
buble_rect = Rect(0, random.randint(0, HEIGHT-BUBLE_PRIEMER),
                  BUBLE_PRIEMER, BUBLE_PRIEMER)
print("Bublina priemer:", BUBLE_PRIEMER)

# Creating a new rect for second object
# player_rect2 = Rect(200, 0, 50, 50)


# Creating a boolean variable that
# we will use to run the while loop
run = True

# Speed for the objects
speed_a = 2
speed_b = -7

# Creating an infinite loop
# to run our game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Setting the framerate to 60fps
    clock.tick(60)

    # Adding speed in player rects
    buble_rect.left += speed_a
    # player_rect2.top += speed_b

    # Checking if player is colliding
    # with platform or not using the
    # colliderect() method.
    # It will return a boolean value
    # collide = pygame.Rect.colliderect(player_rect,
    #                                   player_rect2)

    # If the objects are colliding
    # then changing the speed direction
    # if collide:
    #     speed_a *= -1
    #     speed_b *= -1

    # Changing the direction if the objects
    # goes outside the window
    if buble_rect.right > WIDTH:
        # speed_a *= -1
        run = False
    # if player_rect2.bottom > 600 or player_rect2.top < 0:
    #     speed_b *= -1

    # Drawing player rect
    pygame.draw.ellipse(window, (0,   255,   0), buble_rect, 1)
    # Drawing player rect2
    # pygame.draw.rect(window, (0,   0,   255),
    #                  player_rect2)

    # Updating the display surface
    pygame.display.update()

    # Filling the window with white color
    window.fill((255, 255, 255))
