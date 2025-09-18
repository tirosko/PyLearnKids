# Importing pygame module
import pygame
import sys

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the outlined rectangle
sirka = 2
# ak sirka je nula tak je obdlznik vyplneny
pygame.draw.rect(window, (0, 0, 255),
                 [100, 100, 400, 100], sirka)
# pygame.draw.rect(window, (0, 0, 250), [
#                  100, 100, 400, 100], 3, -2, -2, -2, -2, 2)

# Draws the surface object to the screen.
pygame.display.update()

# --------------------------------------------------------------
# chýba slučka na trvalé zobrazenie
# Set up the game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()

    # Set the FPS (frames per second)
    clock.tick(60)
