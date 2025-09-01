# https://www.geeksforgeeks.org/python/how-to-change-screen-background-color-in-pygame/
# Importing the library
import pygame
import sys

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))
# rozobrať
# surface = pygame.display.set_mode((400, 300), pygame.RESIZABLE)

# Initializing RGB Color - červená
# RGB = (Red, Green, Blue)
# RGB = (255, 0, 0) - červená farba
color = (255, 0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()

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
    surface.fill(color)

    # Update the display
    pygame.display.flip()

    # Set the FPS (frames per second)
    clock.tick(40)
