import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
FONT = pygame.font.Font(None, 50)
COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Initialize grid
grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Add a new tile to the grid


def add_new_tile():
    empty_tiles = [(r, c) for r in range(GRID_SIZE)
                   for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty_tiles:
        r, c = random.choice(empty_tiles)
        grid[r][c] = 2 if random.random() < 0.9 else 4

# Merge tiles in a row


def merge_row(row):
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    return [num for num in new_row if num != 0] + [0] * (GRID_SIZE - len(new_row))

# Move tiles in a direction


def move(direction):
    global grid
    if direction in ('LEFT', 'RIGHT'):
        for r in range(GRID_SIZE):
            row = grid[r][::-1] if direction == 'RIGHT' else grid[r]
            grid[r] = merge_row(
                row)[::-1] if direction == 'RIGHT' else merge_row(row)
    elif direction in ('UP', 'DOWN'):
        for c in range(GRID_SIZE):
            col = [grid[r][c] for r in range(
                GRID_SIZE)][::-1] if direction == 'DOWN' else [grid[r][c] for r in range(GRID_SIZE)]
            merged_col = merge_row(
                col)[::-1] if direction == 'DOWN' else merge_row(col)
            for r in range(GRID_SIZE):
                grid[r][c] = merged_col[r]

# Check if the game is over


def is_game_over():
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == 0:
                return False
            if c < GRID_SIZE - 1 and grid[r][c] == grid[r][c + 1]:
                return False
            if r < GRID_SIZE - 1 and grid[r][c] == grid[r + 1][c]:
                return False
    return True

# Draw the grid


def draw_grid(screen):
    screen.fill((187, 173, 160))
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = grid[r][c]
            color = COLORS.get(value, (60, 58, 50))
            pygame.draw.rect(screen, color, (c * TILE_SIZE,
                             r * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text = FONT.render(
                    str(value), True, (119, 110, 101) if value <= 4 else (255, 255, 255))
                text_rect = text.get_rect(
                    center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)

# Main game loop


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048")
    clock = pygame.time.Clock()

    add_new_tile()
    add_new_tile()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move('LEFT')
                elif event.key == pygame.K_RIGHT:
                    move('RIGHT')
                elif event.key == pygame.K_UP:
                    move('UP')
                elif event.key == pygame.K_DOWN:
                    move('DOWN')
                add_new_tile()
                if is_game_over():
                    print("Game Over!")
                    pygame.quit()
                    sys.exit()

        draw_grid(screen)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
