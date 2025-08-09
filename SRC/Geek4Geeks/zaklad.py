import pygame
import sys

# Inicializácia modulu Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame")

# Define colors (RGB)
WHITE = (155, 155, 155)
BLACK = (0, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white color
    screen.fill(WHITE)

    # Update the display
    pygame.display.flip()

    # Set the FPS (frames per second)
    clock.tick(40)
