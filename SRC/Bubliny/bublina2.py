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

# List to store multiple bubbles
bubbles = []

# Function to create a new bubble


def create_bubble():
    priemer = random.randint(5, 50)
    x = random.randint(0, WIDTH - priemer)
    y = random.randint(0, HEIGHT - priemer)
    speed = random.randint(1, 5)
    bubble = {
        'rect': Rect(x, y, priemer, priemer),
        'speed': speed,
        'priemer': priemer
    }
    return bubble


# Create initial bubbles
for _ in range(5):
    bubbles.append(create_bubble())

# Creating a boolean variable that
# we will use to run the while loop
run = True

# Creating an infinite loop
# to run our game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Setting the framerate to 60fps
    clock.tick(60)

    # Update each bubble
    for bubble in bubbles[:]:
        bubble['rect'].left += bubble['speed']

        # Remove bubble if it goes off screen
        if bubble['rect'].right > WIDTH:
            bubbles.remove(bubble)

    # Add new bubble randomly
    if random.randint(1, 100) > 95:
        bubbles.append(create_bubble())

    # Drawing all bubbles
    for bubble in bubbles:
        pygame.draw.ellipse(window, (255, 0, 0), bubble['rect'], 1)

    # Updating the display surface
    pygame.display.update()

    # Filling the window with white color
    window.fill((255, 255, 255))
