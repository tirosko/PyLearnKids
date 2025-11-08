import pygame
# import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_SIZE = 10
BRICK_WIDTH = 80
BRICK_HEIGHT = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2,
                                WINDOW_HEIGHT - 40,
                                PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 8

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2,
                                WINDOW_HEIGHT // 2,
                                BALL_SIZE, BALL_SIZE)
# modifikoval som rychlost lopty
        self.speed_x = 3
        self.speed_y = -3

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Wall collision
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)


class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)


def run_game():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Wall Breaker")
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    bricks = []
    for row in range(5):
        for col in range(WINDOW_WIDTH // (BRICK_WIDTH + 2)):
            bricks.append(Brick(col * (BRICK_WIDTH + 2) + 1,
                                row * (BRICK_HEIGHT + 2) + 1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        paddle.move()
        ball.move()

        # collisions
        if ball.rect.colliderect(paddle.rect):
            ball.speed_y *= -1
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.speed_y *= -1
                bricks.remove(brick)

        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        if ball.rect.bottom >= WINDOW_HEIGHT:
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    run_game()
