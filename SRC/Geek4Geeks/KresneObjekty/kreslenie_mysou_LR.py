# Importing pygame module
import pygame

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))


# List to store (position, color, solid) for each circle
circle_data = []

# radius of the circle
circle_radius = 60


# List of colors to cycle through
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (0, 0, 0),      # Black
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (128, 128, 128)  # Gray
]
color_index = 0

# Creating a variable which we will use
# to run the while loop
run = True

# Creating a while loop
while run:

    # Iterating over all the events received from
    # pygame.event.get()
    for event in pygame.event.get():

        # If the type of the event is quit
        # then setting the run variable to false
        if event.type == pygame.QUIT:
            run = False

        # if the type of the event is MOUSEBUTTONDOWN
        # then storing the current position and assigning a color
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            circle_color = colors[color_index % len(colors)]
            # Left button: solid, Right button: not solid
            if event.button == 1:
                solid = True
            elif event.button == 3:
                solid = False
            else:
                continue  # Ignore other buttons
            circle_data.append((position, circle_color, solid))
            print(circle_data)
            color_index += 1

    # Draw each circle with its assigned color and fill style
    for position, circle_color, solid in circle_data:
        if solid:
            pygame.draw.circle(window, circle_color, position, circle_radius)
        else:
            pygame.draw.circle(window, circle_color, position,
                               circle_radius, 3)  # width=3 for outline

    # Draws the surface object to the screen.
    pygame.display.update()
