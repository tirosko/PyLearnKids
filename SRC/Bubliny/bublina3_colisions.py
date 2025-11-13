# Importing the pygame module
import pygame
from pygame.locals import *
import random
import math

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
    # x = random.randint(0, WIDTH - priemer)
    x = 0
    y = random.randint(0, HEIGHT - priemer)
    speed = random.randint(1, 5)
    bubble = {
        'rect': Rect(x, y, priemer, priemer),
        'speed': speed,
        'priemer': priemer
    }
    return bubble


# Function to check collision between two bubbles
def check_collision(bubble1, bubble2):
    # Get center points
    center1_x = bubble1['rect'].centerx
    center1_y = bubble1['rect'].centery
    center2_x = bubble2['rect'].centerx
    center2_y = bubble2['rect'].centery

    # Get radii
    radius1 = bubble1['priemer'] / 2
    radius2 = bubble2['priemer'] / 2

    # Calculate distance between centers
    distance = math.sqrt((center1_x - center2_x)**2 +
                         (center1_y - center2_y)**2)

    # If distance is less than sum of radii, collision occurred
    return distance < (radius1 + radius2)


# Function to merge two bubbles
def merge_bubbles(bubble1, bubble2):
    # Merge into larger bubble
    new_priemer = int(math.sqrt(bubble1['priemer']**2 + bubble2['priemer']**2))
    new_x = (bubble1['rect'].centerx + bubble2['rect'].centerx) // 2
    new_y = (bubble1['rect'].centery + bubble2['rect'].centery) // 2
    new_speed = (bubble1['speed'] + bubble2['speed']) / 2

    merged_bubble = {
        'rect': Rect(new_x - new_priemer // 2, new_y - new_priemer // 2, new_priemer, new_priemer),
        'speed': new_speed,
        'priemer': new_priemer
    }
    return merged_bubble


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

    # Check for collisions between bubbles
    for i in range(len(bubbles)):
        for j in range(i + 1, len(bubbles)):
            if check_collision(bubbles[i], bubbles[j]):
                # Merge bubbles
                merged = merge_bubbles(bubbles[i], bubbles[j])
                # Remove original bubbles and add merged one
                bubbles.remove(bubbles[j])
                bubbles.remove(bubbles[i])
                bubbles.append(merged)
                break

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

pygame.quit()
