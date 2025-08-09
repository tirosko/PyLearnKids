# https://www.geeksforgeeks.org/python/allowing-resizing-window-in-pygame/
import pygame
import sys

# Inicializácia modulu Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 400, 300
# Create a resizable window
screen = pygame.display.set_mode(
    (screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("My First Pygame")

# Define colors (RGB)
WHITE = (155, 155, 155)
BLACK = (0, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Player settings
player_width, player_height = 50, 50
player_x, player_y = screen_width // 4, screen_height // 4
player_speed = 10

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

        # Keep the player inside the screen bounds
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height

    # Fill screen with white color
    screen.fill(WHITE)

    # Draw the player (a simple rectangle)
    pygame.draw.rect(screen, BLACK, (player_x, player_y,
                     player_width, player_height))

    # Update display
    pygame.display.flip()
    clock.tick(90)
