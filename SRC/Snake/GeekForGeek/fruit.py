# importing libraries
import pygame
import time
import random
from pygame.locals import *
import sys

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

fruit_position[0] = 0
fruit_position[1] = 0
while True:  # main game loop
    for event in pygame.event.get():

        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
        pygame.display.update()
        time.sleep(1)
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
