import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Event Handling")


exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.MOUSEMOTION:
            if event.rel[0] > 0:
                print("Mouse moving to the right")
            elif event.rel[1] > 0:
                print("Mouse moving down")
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event
            if event.button == 3:
                print("Right mouse button pressed")
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released
            print("Mouse button has been released")

pygame.quit()
quit()
