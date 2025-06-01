# Analyza vytvorenie snake, pozícia, pohyb
# importing libraries
import pygame
from pygame.locals import *
import sys

snake_speed = 10

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

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

direction = 'RIGHT'
change_to = direction

while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Dôležité vysvetliť, že had sa môže pohybovať len jedným smerom
    # Ak sa stlačí klávesa, zmení sa smer pohybu. ale nemôže sa pohybovať dvoma smermi naraz a teda napríklad do protismeru
    # Ak sú stlačené dve klávesy súčasne nechceme, aby sa had pohyboval dvoma smermi naraz
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    # Ak sa had pohybuje tak sa pohybuje o 10 pixelov v smere, ktorý je nastavený
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    # Pop - odstraňuje posledný segment hadieho tela
    snake_body.pop()
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    # Refresh game screen
    pygame.display.update()
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

    if event.type == QUIT:
        pygame.quit()
        sys.exit()
