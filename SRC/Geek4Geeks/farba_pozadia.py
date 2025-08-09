# https://www.geeksforgeeks.org/python/how-to-change-screen-background-color-in-pygame/
# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing RGB Color - červená
# RGB = (Red, Green, Blue)
# RGB = (255, 0, 0)
# RGB = (255, 0, 0) - červená farba
color = (255, 0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()
