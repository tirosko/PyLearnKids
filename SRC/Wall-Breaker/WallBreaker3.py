import pygame
# import random
import sys
# Sound
# https://pixabay.com/sound-effects/search/wav/

# 🎮 Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# 🖥️ Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Break the Wall")

# 🎨 Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# 🔊 Load sounds
# bounce_sound = pygame.mixer.Sound("bounce.wav")
# brick_sound = pygame.mixer.Sound("brick.wav")
# lose_life_sound = pygame.mixer.Sound("lose_life.wav")

# 🕹️ Paddle
paddle = pygame.Rect(WIDTH//2 - 60, HEIGHT - 30, 120, 10)

# ⚽ Ball
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
ball_speed = [4, -4]

# 🧱 Brick setup


def create_bricks(rows, cols):
    brick_width = WIDTH // cols
    brick_height = 30
    return [pygame.Rect(col * brick_width, row * brick_height, brick_width - 2, brick_height - 2)
            for row in range(rows) for col in range(cols)]


brick_rows, brick_cols = 5, 10
bricks = create_bricks(brick_rows, brick_cols)

# 🧠 Game state
score = 0
lives = 3
level = 1
font = pygame.font.SysFont(None, 36)

# 🔁 Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # 🎮 Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ⬅️➡️ Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-6, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(6, 0)

    # 🏃 Ball movement
    ball.move_ip(ball_speed)

    # 🧱 Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
        # bounce_sound.play()
    if ball.top <= 0:
        ball_speed[1] *= -1
        # bounce_sound.play()
    if ball.colliderect(paddle):
        ball_speed[1] *= -1
        # bounce_sound.play()

    # 💥 Brick collision
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        del bricks[hit_index]
        ball_speed[1] *= -1
        score += 10
        # brick_sound.play()

    # 💔 Missed ball
    if ball.bottom >= HEIGHT:
        lives -= 1
        # lose_life_sound.play()
        ball.topleft = (WIDTH//2, HEIGHT//2)
        ball_speed = [4, -4]
        if lives == 0:
            running = False

    # 🎯 Level up
    if not bricks:
        level += 1
        brick_rows += 1
        bricks = create_bricks(brick_rows, brick_cols)
        ball_speed[0] *= 1.1
        ball_speed[1] *= 1.1

    # 🖌️ Draw elements
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # 🧾 Draw score, lives, level
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))
    screen.blit(level_text, (WIDTH//2 - 50, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
