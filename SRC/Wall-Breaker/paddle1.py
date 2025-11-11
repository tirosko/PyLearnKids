import pygame
# import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Break the Wall")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle
paddle = pygame.Rect(WIDTH//2 - 60, HEIGHT - 30, 120, 10)

# Ball
# WIDTH//2 - 400, HEIGHT//2 - 300
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)

ball_speed = [4, -4]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(6, 0)

    # Ball movement
    ball.move_ip(ball_speed)

    # Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # # Brick collision
    # hit_index = ball.collidelist(bricks)
    # if hit_index != -1:
    #     del bricks[hit_index]
    #     ball_speed[1] *= -1

    # Draw everything
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    # for brick in bricks:
    #     pygame.draw.rect(screen, RED, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
