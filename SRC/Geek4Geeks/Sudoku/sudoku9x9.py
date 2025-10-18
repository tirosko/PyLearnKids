# Sudoku Game 9x9 with Pygame
# Simple playable Sudoku board with decision numbers support

import pygame
import sys
from sudoku_boards import BOARDS, save_game_progress, load_game_progress, get_next_level, get_difficulty

pygame.init()

WIDTH, HEIGHT = 540, 650  # Added height for more buttons
SIZE = 60  # Size of each cell
MARGIN = 5
DECISION_SIZE = SIZE // 3  # Size for decision numbers
SAVE_FILE = "sudoku_save.json"

# Colors
BUTTON_COLOR = (100, 100, 200)
BUTTON_HOVER_COLOR = (120, 120, 220)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku 9x9')
font = pygame.font.SysFont('Arial', 32)
small_font = pygame.font.SysFont('Arial', 24)
button_font = pygame.font.SysFont('Arial', 20)

# Try to load saved game, or start with first board
saved_game = load_game_progress(SAVE_FILE)
if saved_game:
    board, user_board, decisions, current_level = saved_game
else:
    current_level = list(BOARDS.keys())[0]
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

selected = None
user_board = [[board[r][c] for c in range(9)] for r in range(9)]
# Dictionary to store decision numbers for each cell {(row, col): set(numbers)}
decisions = {}

# Helper to check if a move is valid
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num:
                return False
    return True

def update_decisions(row, col, num):
    # Clear the number from decisions in the same row
    for c in range(9):
        pos = (row, c)
        if pos in decisions and num in decisions[pos]:
            decisions[pos].remove(num)
            if not decisions[pos]:  # Remove empty sets
                decisions.pop(pos)
    
    # Clear the number from decisions in the same column
    for r in range(9):
        pos = (r, col)
        if pos in decisions and num in decisions[pos]:
            decisions[pos].remove(num)
            if not decisions[pos]:
                decisions.pop(pos)
    
    # Clear the number from decisions in the same 3x3 box
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            pos = (i, j)
            if pos in decisions and num in decisions[pos]:
                decisions[pos].remove(num)
                if not decisions[pos]:
                    decisions.pop(pos)

def draw_button(text, x, y, width, height, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # Check if mouse is over button
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (x, y, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))
    
    text_surface = button_font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width/2, y + height/2)
    screen.blit(text_surface, text_rect)

def save_current_game():
    save_game_progress(SAVE_FILE, board, user_board, decisions, current_level)

def load_next_level():
    global board, user_board, decisions, current_level
    current_level = get_next_level(current_level)
    board = BOARDS[current_level]
    user_board = [[board[r][c] for c in range(9)] for r in range(9)]
    decisions.clear()

def draw_board():
    screen.fill((255, 255, 255))
    # Draw grid
    for i in range(10):
        width = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0), (MARGIN, MARGIN + i * SIZE), (MARGIN + 9 * SIZE, MARGIN + i * SIZE), width)
        pygame.draw.line(screen, (0, 0, 0), (MARGIN + i * SIZE, MARGIN), (MARGIN + i * SIZE, MARGIN + 9 * SIZE), width)
    # Draw numbers
    for r in range(9):
        for c in range(9):
            num = user_board[r][c]
            if num != 0:
                color = (0, 0, 0) if board[r][c] != 0 else (0, 0, 200)
                text = font.render(str(num), True, color)
                x = MARGIN + c * SIZE + SIZE // 2 - text.get_width() // 2
                y = MARGIN + r * SIZE + SIZE // 2 - text.get_height() // 2
                screen.blit(text, (x, y))
            # Draw decision numbers if cell is empty
            elif (r, c) in decisions and len(decisions[(r, c)]) > 0:
                decision_font = pygame.font.SysFont('Arial', 16)
                for num in sorted(decisions[(r, c)]):
                    # Calculate position within the cell (3x3 grid)
                    pos_x = (num - 1) % 3
                    pos_y = (num - 1) // 3
                    x = MARGIN + c * SIZE + pos_x * DECISION_SIZE + DECISION_SIZE // 2
                    y = MARGIN + r * SIZE + pos_y * DECISION_SIZE + DECISION_SIZE // 2
                    text = decision_font.render(str(num), True, (100, 100, 100))
                    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
    
    # Highlight selected cell
    if selected:
        r, c = selected
        pygame.draw.rect(screen, (255, 200, 0), (MARGIN + c * SIZE, MARGIN + r * SIZE, SIZE, SIZE), 4)
    # Draw instructions and level info
    msg = small_font.render('Left click: enter number, Right click: decision numbers', True, (0,0,0))
    screen.blit(msg, (10, HEIGHT - 100))
    msg2 = small_font.render('1-9: input, DEL: clear, Q: quit', True, (0,0,0))
    screen.blit(msg2, (10, HEIGHT - 75))
    
    # Draw difficulty and level
    level_text = f"Level: {current_level} ({get_difficulty(current_level)})"
    level_surface = small_font.render(level_text, True, (0, 0, 0))
    screen.blit(level_surface, (10, HEIGHT - 50))
    
    # Draw buttons
    draw_button("Save Game", 50, HEIGHT - 35, 100, 25, save_current_game)
    draw_button("Next Level", WIDTH - 150, HEIGHT - 35, 100, 25, load_next_level)

def main():
    global selected, board, user_board, decisions, current_level
    running = True
    
    while running:
        draw_board()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_current_game()  # Auto-save on quit
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                # Check if clicked on board
                if MARGIN < x < MARGIN + 9 * SIZE and MARGIN < y < MARGIN + 9 * SIZE:
                    c = (x - MARGIN) // SIZE
                    r = (y - MARGIN) // SIZE
                    selected = (r, c)
                    # Right click for decision numbers
                    if event.button == 3 and board[r][c] == 0:  # Right click and empty cell
                        if selected not in decisions:
                            decisions[selected] = set()
                
                # Check button clicks (handled in draw_button function)
                
            elif event.type == pygame.KEYDOWN and selected:
                r, c = selected
                if board[r][c] == 0:
                    if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        user_board[r][c] = 0
                        if selected in decisions:
                            decisions.pop(selected)  # Clear decision numbers too
                    elif pygame.K_1 <= event.key <= pygame.K_9:
                        num = event.key - pygame.K_0
                        if pygame.key.get_mods() & pygame.KMOD_RSHIFT or pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                            # Shift + number: toggle decision number
                            if selected not in decisions:
                                decisions[selected] = set()
                            if num in decisions[selected]:
                                decisions[selected].remove(num)
                            else:
                                decisions[selected].add(num)
                        else:
                            # Normal number input
                            if is_valid(user_board, r, c, num):
                                user_board[r][c] = num
                                if selected in decisions:
                                    decisions.pop(selected)  # Clear decisions when setting number
                                # Update decisions in affected cells
                                update_decisions(r, c, num)
        # Quit with Q
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            running = False
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
