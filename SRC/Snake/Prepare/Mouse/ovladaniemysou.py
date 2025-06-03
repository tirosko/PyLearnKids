# Here's a simple tutorial to help you understand how to move an object with the mouse in Pygame. This example demonstrates how to create a window, draw a shape (like a circle), and move it based on the mouse's position.

# Code Example: Moving an Object with the Mouse
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move with Mouse")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Circle properties
circle_radius = 30

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the circle at the mouse position
    pygame.draw.circle(screen, BLUE, (mouse_x, mouse_y), circle_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

# Explanation:

# Initialization:

# pygame.init() initializes all Pygame modules.
# A screen is created with pygame.display.set_mode().

# Mouse Position:

# pygame.mouse.get_pos() retrieves the current position of the mouse as (x, y) coordinates.

# Drawing:

# The circle is drawn at the mouse's position using pygame.draw.circle().

# Event Handling:

# The pygame.QUIT event ensures the program exits cleanly when the window is closed.

# Screen Refresh:

# pygame.display.flip() updates the screen to reflect changes.
# Try It Out!

# Run the code, and you'll see a blue circle following your mouse cursor as you move it around the window. You can customize the shape, size, or even add more interactive elements to make it more engaging!