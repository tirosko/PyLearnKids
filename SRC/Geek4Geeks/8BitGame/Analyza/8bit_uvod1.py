# 8Bit Game with Pygame
# A simple 8-bit style game using pygame

import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('8Bit Game')
clock = pygame.time.Clock()

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
START_LIGHT = (169, 169, 169)
START_DARK = (100, 100, 100)
COLOR_LIST = [RED, GREEN, BLUE]

# Player
player_size = 40
player_x = 40
player_y = HEIGHT // 2
player_color = random.choice(COLOR_LIST)


# Enemy
enemy_size = 50
enemy_x = WIDTH
enemy_y = random.randint(50, HEIGHT - 50)

# Good block (blue)
good_size = 40
good_x = random.randint(WIDTH // 2, WIDTH - good_size)
good_y = random.randint(50, HEIGHT - 50)
good_color = BLUE

# Score and speed
score = 0
speed = 15

# Fonts
font = pygame.font.SysFont('Corbel', 35)
large_font = pygame.font.SysFont('Corbel', 60)

# Game Over function
def game_over():
    while True:
        screen.fill((65, 25, 64))
        game_over_text = large_font.render('GAME OVER', True, WHITE)
        restart_text = font.render('Restart', True, WHITE)
        exit_text = font.render('Exit', True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 60))
        pygame.draw.rect(screen, START_LIGHT, [WIDTH // 2 - 100, HEIGHT // 2 + 20, 100, 40])
        pygame.draw.rect(screen, START_DARK, [WIDTH // 2 + 20, HEIGHT // 2 + 20, 100, 40])
        screen.blit(restart_text, (WIDTH // 2 - 90, HEIGHT // 2 + 25))
        screen.blit(exit_text, (WIDTH // 2 + 35, HEIGHT // 2 + 25))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if WIDTH // 2 - 100 < mx < WIDTH // 2 and HEIGHT // 2 + 20 < my < HEIGHT // 2 + 60:
                    main_game()
                    return
                if WIDTH // 2 + 20 < mx < WIDTH // 2 + 120 and HEIGHT // 2 + 20 < my < HEIGHT // 2 + 60:
                    pygame.quit()
                    return

# Main game function

def main_game():
    player_x = 40
    player_y = HEIGHT // 2
    enemy_x = WIDTH
    enemy_y = random.randint(50, HEIGHT - 50)
    score = 0
    speed = 15
    # Good block position and speed
    good_x = WIDTH
    good_y = random.randint(50, HEIGHT - good_size)
    good_speed = 8
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= 10
        if keys[pygame.K_DOWN]:
            player_y += 10
        # Move enemy
        enemy_x -= 10
        if enemy_x < 0:
            enemy_x = WIDTH
            enemy_y = random.randint(50, HEIGHT - 50)
            score += 1
            speed = min(60, speed + 1)

        # Move good block (fly)
        good_x -= good_speed
        if good_x < 0:
            good_x = WIDTH
            good_y = random.randint(50, HEIGHT - good_size)

        # Drawing
        screen.fill((65, 25, 64))
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        good_rect = pygame.Rect(good_x, good_y, good_size, good_size)
        pygame.draw.rect(screen, player_color, player_rect)
        pygame.draw.rect(screen, RED, enemy_rect)
        pygame.draw.rect(screen, BLUE, good_rect)

        # Collision detection
        if player_rect.colliderect(enemy_rect):
            game_over()
            return
        if player_rect.colliderect(good_rect):
            score += 5  # More points for good block
            # Move good block to new random position at right
            good_x = WIDTH
            good_y = random.randint(50, HEIGHT - good_size)
        if player_y < 0 or player_y > HEIGHT - player_size:
            game_over()
            return
        # Score
        score_text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(score_text, (WIDTH - 150, 10))
        pygame.display.update()
        clock.tick(speed)
    pygame.quit()

# Intro screen
def intro():
    while True:
        screen.fill((65, 25, 64))
        title = large_font.render('8Bit Game', True, WHITE)
        start_text = font.render('Štart', True, WHITE)
        exit_text = font.render('Koniec', True, WHITE)
        # pygame.draw.rect(screen, START_LIGHT, [WIDTH // 2 - 100, HEIGHT // 2, 100, 40])
        pygame.draw.rect(screen, START_DARK, [WIDTH // 2 + 40, HEIGHT // 2, 110, 40])
        screen.blit(title, (WIDTH // 2 - 120, HEIGHT // 2 - 100))
        screen.blit(start_text, (WIDTH // 2 - 80, HEIGHT // 2 + 5))
        screen.blit(exit_text, (WIDTH // 2 + 45, HEIGHT // 2 + 5))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if WIDTH // 2 - 100 < mx < WIDTH // 2 and HEIGHT // 2 < my < HEIGHT // 2 + 40:
                    # main_game()
                    return
                if WIDTH // 2 + 20 < mx < WIDTH // 2 + 120 and HEIGHT // 2 < my < HEIGHT // 2 + 40:
                    pygame.quit()
                    return

if __name__ == '__main__':
    intro()
