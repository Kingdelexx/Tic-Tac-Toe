import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (255, 255, 255)
BOARD_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 255, 0)
LINE_WIDTH = 4
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize game variables
board = [['' for _ in range(COLS)] for _ in range(ROWS)]
current_player = 'X'
game_over = False
winner = None

# Function to draw grid lines
def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    for j in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (j * SQUARE_SIZE, 0), (j * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Function to draw X and O
def draw_xo():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col * SQUARE_SIZE, row * SQUARE_SIZE), 
                                 ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE), 
                                 (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), 
                                                      int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), 
                                   int(SQUARE_SIZE / 2 - LINE_WIDTH), LINE_WIDTH)

# Function to check for a winner
def check_winner():
    global winner
    # Check rows
    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            return True
    # Check columns
    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE
            if board[row][col] == '':
                board[row][col] = current_player
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
                if check_winner():
                    game_over = True

    # Clear the screen
    screen.fill(BOARD_COLOR)

    # Draw grid lines
    draw_grid()

    # Draw X and O
    draw_xo()

    # Display winner
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {winner} wins!", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()
