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
FONT_SIZE = 36

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Current Affairs Quiz")

# Create font
font = pygame.font.Font(None, FONT_SIZE)

# Question bank
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who is the current President of the United States?", "answer": "Joe Biden"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What year did World War II end?", "answer": "1945"},
    {"question": "What is the currency of Japan?", "answer": "Yen"},
]

# Game variables
player1_score = 0
player2_score = 0
current_question = None
current_player = 1
asked_questions = []

def display_text(text, position):
    rendered_text = font.render(text, True, WHITE)
    screen.blit(rendered_text, position)

def ask_question():
    global current_question
    remaining_questions = [q for q in questions if q not in asked_questions]
    if remaining_questions:
        current_question = random.choice(remaining_questions)
        asked_questions.append(current_question)
    else:
        current_question = None

def main():
    global player1_score, player2_score, current_question, current_player
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and current_player == 1:
                    answer = input_text()
                    if answer.lower() == current_question["answer"].lower():
                        player1_score += 1
                        current_player = 2
                        ask_question()
                    else:
                        display_text("Incorrect", (50, 150))
                        current_player = 2
                elif event.key == pygame.K_2 and current_player == 2:
                    answer = input_text()
                    if answer.lower() == current_question["answer"].lower():
                        player2_score += 1
                        current_player = 1
                        ask_question()
                    else:
                        display_text("Incorrect", (50, 150))
                        current_player = 1

        screen.fill(BLACK)

        if player1_score < 5 and player2_score < 5:
            if current_question is None:
                ask_question()
            if current_question:
                display_text(current_question["question"], (50, 50))
                display_text(f"Player {current_player}'s turn", (50, 100))
        else:
            winner = "Player 1" if player1_score >= 5 else "Player 2"
            display_text(f"{winner} wins the game!", (50, 150))
            pygame.quit()
            sys.exit()

        display_text(f"Player 1 Score: {player1_score}", (50, 400))
        display_text(f"Player 2 Score: {player2_score}", (50, 450))

        pygame.display.flip()
        clock.tick(FPS)

def input_text():
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        display_text(f"Answer: {input_text}", (50, 150))
        pygame.display.flip()

if __name__ == "__main__":
    main()
