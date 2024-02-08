import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 48

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Create font
font = pygame.font.Font(None, FONT_SIZE)

# Game options
options = {"r": "Rock", "p": "Paper", "s": "Scissors"}
user_choice = None
computer_choice = None
result = ""

def display_text(text, position):
    rendered_text = font.render(text, True, WHITE)
    screen.blit(rendered_text, position)

def display_choices():
    display_text(f"Your choice: {options.get(user_choice, '')}", (50, 50))
    display_text(f"Computer's choice: {computer_choice}", (50, 150))
    display_text(result, (50, 250))

def determine_winner():
    global user_choice, computer_choice, result
    user_choice = random.choice(list(options.keys()))
    computer_choice = random.choice(list(options.values()))

    if user_choice == computer_choice.lower():
        result = "It's a tie!"
    elif (
        (user_choice == "r" and computer_choice == "Scissors")
        or (user_choice == "p" and computer_choice == "Rock")
        or (user_choice == "s" and computer_choice == "Paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_r, pygame.K_p, pygame.K_s]:
                    user_choice = event.unicode.lower()
                    determine_winner()
                elif event.key == pygame.K_SPACE:
                    result = ""
                    user_choice = None
                    computer_choice = None

        screen.fill(BLACK)
        display_choices()

        # Draw "Play Again" button
        pygame.draw.rect(screen, WHITE, (350, 400, 100, 50))
        display_text("Play Again", (355, 410))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
