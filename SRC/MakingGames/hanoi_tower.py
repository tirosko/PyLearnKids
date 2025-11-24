# Hanoi Tower Game in Pygame
# Move all disks from left rod to right rod
# Rules: Only one disk at a time, larger disk cannot be on smaller disk

import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hanoi Tower - Move all disks to the right rod")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
GREEN = (50, 200, 50)
YELLOW = (255, 255, 0)
LIGHT_BLUE = (150, 200, 255)

# Font
font_large = pygame.font.Font('freesansbold.ttf', 48)
font_medium = pygame.font.Font('freesansbold.ttf', 32)
font_small = pygame.font.Font('freesansbold.ttf', 24)

# Rod positions
ROD_X = [200, 500, 800]
ROD_Y_BASE = 450
ROD_HEIGHT = 350
DISK_HEIGHT = 30

# Disk colors for each size
DISK_COLORS = {
    1: (255, 0, 0),      # Red
    2: (255, 165, 0),    # Orange
    3: (255, 255, 0),    # Yellow
    4: (0, 255, 0),      # Green
    5: (0, 0, 255)       # Blue
}

# Game state
rods = [[], [], []]  # Three rods with stacks of disks
# Initial state: all disks on left rod (largest to smallest)
rods[0] = [5, 4, 3, 2, 1]
selected_disk = None
selected_rod = None
moves = 0
hint_visible = False
solution_step = 0

# Animation state
auto_play = False
auto_play_delay = 0
# Frames between auto moves (60 = 1 second at 60fps)
AUTO_PLAY_FRAME_DELAY = 60

# Hanoi solution generator


def generate_hanoi_solution(n, source, target, auxiliary):
    """Generate moves to solve Hanoi puzzle"""
    if n == 0:
        return []
    moves_list = []
    moves_list.extend(generate_hanoi_solution(n-1, source, auxiliary, target))
    moves_list.append((source, target))
    moves_list.extend(generate_hanoi_solution(n-1, auxiliary, target, source))
    return moves_list


# Generate full solution
hanoi_moves = generate_hanoi_solution(5, 0, 2, 1)
total_moves = len(hanoi_moves)


def get_disk_width(disk_size):
    """Return width of disk based on size"""
    return 40 + disk_size * 30


def get_disk_y(rod_index):
    """Get Y position for the top disk on a rod"""
    num_disks = len(rods[rod_index])
    return ROD_Y_BASE - (num_disks * DISK_HEIGHT)


def is_valid_move(from_rod, to_rod):
    """Check if move is valid"""
    if not rods[from_rod]:
        return False
    if not rods[to_rod]:
        return True
    return rods[from_rod][-1] < rods[to_rod][-1]


def move_disk(from_rod, to_rod):
    """Move disk from one rod to another"""
    global moves
    if is_valid_move(from_rod, to_rod):
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        moves += 1
        return True
    return False


def check_win():
    """Check if puzzle is solved"""
    return len(rods[2]) == 5 and len(rods[0]) == 0 and len(rods[1]) == 0


def show_next_move():
    """Show hint for next move"""
    global hint_visible, solution_step
    if solution_step < len(hanoi_moves):
        hint_visible = True
    else:
        hint_visible = False


def toggle_auto_play():
    """Toggle automatic solution playback"""
    global auto_play
    auto_play = not auto_play


def auto_move_next():
    """Automatically make the next move in the solution"""
    global solution_step
    if solution_step < len(hanoi_moves):
        from_rod, to_rod = hanoi_moves[solution_step]
        if move_disk(from_rod, to_rod):
            solution_step += 1
            return True
    return False


def draw_rod(x, y, height):
    """Draw a single rod"""
    # Rod base
    pygame.draw.rect(screen, DARK_GRAY, (x - 5, y, 10, height))
    # Base platform
    pygame.draw.ellipse(screen, GRAY, (x - 60, y + height - 10, 120, 20))


def draw_disk(x, y, size, highlight=False):
    """Draw a disk"""
    width = get_disk_width(size)
    color = DISK_COLORS[size]
    if highlight:
        pygame.draw.rect(screen, LIGHT_BLUE,
                         (x - width // 2, y, width, DISK_HEIGHT), 3)
    else:
        pygame.draw.rect(
            screen, color, (x - width // 2, y, width, DISK_HEIGHT))
    pygame.draw.rect(screen, BLACK, (x - width // 2, y, width, DISK_HEIGHT), 2)
    # Draw size number
    size_text = font_small.render(str(size), True, WHITE)
    screen.blit(size_text, (x - 10, y + 5))


def draw_game():
    """Draw the entire game"""
    screen.fill(WHITE)

    # Draw title
    title = font_large.render("Hanoi Tower - 5 Disks", True, BLACK)
    screen.blit(title, (WIDTH // 2 - 200, 10))

    # Draw rules and stats in a box
    info_y = 70
    info_texts = [
        f"Moves: {moves} / Minimum: {total_moves} | Following solution: {solution_step}/{total_moves}",
        "RULES: Move one disk at a time • Larger disk cannot be on smaller disk",
        "GOAL: Move all disks from LEFT rod to RIGHT rod",
        f"CONTROLS: Click disk -> Click rod | H: Hint | A: Auto-Play {'[ON]' if auto_play else '[OFF]'} | R: Reset"
    ]
    for i, text in enumerate(info_texts):
        info_text = font_small.render(text, True, BLACK if i == 0 else GRAY)
        screen.blit(info_text, (15, info_y + i * 25))

    # Draw rod labels
    labels = ["LEFT", "MIDDLE", "RIGHT"]
    for rod_idx, label in enumerate(labels):
        label_text = font_small.render(label, True, DARK_GRAY)
        screen.blit(label_text, (ROD_X[rod_idx] - 25, ROD_Y_BASE + 30))

    # Draw rods and disks
    for rod_idx in range(3):
        x = ROD_X[rod_idx]
        draw_rod(x, ROD_Y_BASE - ROD_HEIGHT, ROD_HEIGHT)

        # Draw disks on this rod (from bottom to top)
        for disk_idx in range(len(rods[rod_idx])):
            disk_size = rods[rod_idx][disk_idx]
            y = ROD_Y_BASE - (disk_idx + 1) * DISK_HEIGHT
            highlight = (selected_rod == rod_idx and disk_idx ==
                         len(rods[rod_idx]) - 1)
            draw_disk(x, y, disk_size, highlight)

    # Draw hint arrow if active
    if hint_visible and solution_step < len(hanoi_moves):
        from_rod, to_rod = hanoi_moves[solution_step]
        from_x = ROD_X[from_rod]
        to_x = ROD_X[to_rod]
        from_y = ROD_Y_BASE - ROD_HEIGHT - 30
        to_y = ROD_Y_BASE - ROD_HEIGHT - 30

        # Draw arrow
        pygame.draw.line(screen, GREEN, (from_x, from_y), (to_x, to_y), 3)
        # Arrow head
        angle = math.atan2(to_y - from_y, to_x - from_x)
        for adj_angle in [-math.pi/6, math.pi/6]:
            end_angle = angle + adj_angle
            end_x = to_x - 15 * math.cos(end_angle)
            end_y = to_y - 15 * math.sin(end_angle)
            pygame.draw.line(screen, GREEN, (to_x, to_y), (end_x, end_y), 3)

    # Draw win message
    if check_win():
        win_text = font_medium.render(
            f"YOU WIN! Moves: {moves}/{total_moves}", True, GREEN)
        screen.blit(win_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
        reset_text = font_small.render("Press R to play again", True, BLACK)
        screen.blit(reset_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))

    pygame.display.flip()


def reset_game():
    """Reset game state"""
    global rods, selected_disk, selected_rod, moves, hint_visible, solution_step
    rods = [[], [], []]
    rods[0] = [5, 4, 3, 2, 1]
    selected_disk = None
    selected_rod = None
    moves = 0
    hint_visible = False
    solution_step = 0


# Main game loop
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            if event.key == pygame.K_h:
                show_next_move()
            if event.key == pygame.K_a:
                toggle_auto_play()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            # Check which rod was clicked
            for rod_idx in range(3):
                rod_x = ROD_X[rod_idx]
                if abs(mouse_x - rod_x) < 100 and ROD_Y_BASE - ROD_HEIGHT < mouse_y < ROD_Y_BASE:

                    if selected_disk is None:
                        # Select disk from this rod
                        if rods[rod_idx]:
                            selected_disk = rods[rod_idx][-1]
                            selected_rod = rod_idx
                    else:
                        # Try to move disk to this rod
                        if rod_idx != selected_rod:
                            if move_disk(selected_rod, rod_idx):
                                # Check if this was the next correct move
                                if solution_step < len(hanoi_moves):
                                    from_rod, to_rod = hanoi_moves[solution_step]
                                    if from_rod == selected_rod and to_rod == rod_idx:
                                        solution_step += 1
                                hint_visible = False
                        selected_disk = None
                        selected_rod = None
                    break

    # Handle auto-play animation
    if auto_play and not check_win():
        auto_play_delay += 1
        if auto_play_delay >= AUTO_PLAY_FRAME_DELAY:
            auto_move_next()
            auto_play_delay = 0

    draw_game()

pygame.quit()
