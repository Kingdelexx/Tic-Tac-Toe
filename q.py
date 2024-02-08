import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Personality Quiz")

# Create font
font = pygame.font.Font(None, 36)

# Questions and responses
questions = [
    "What is your favorite color?",
    "Do you prefer cats or dogs?",
    "What is your favorite hobby?",
    "Do you like horror movies?",
    "Are you a morning person or a night owl?",
]

responses = {
    "Awesome": ["Blue", "Dogs", "Playing video games", "No", "Night owl"],
    "Great": ["Green", "Cats", "Reading books", "Morning", "No", "person"],
    "Nice": ["Red", "Both", "Listening to music", "No", "Neutral"],
    "Boring": ["Gray", "None", "Watching TV", "No", "None"],
    "Good": ["Purple", "Birds", "Outdoor activities", "No", "Both"],
    "Bad": ["Other", "Other", "Other", "Yes", "Other"],
}

def ask_question(question):
    input_text = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(BLACK)

        display_text(question, (50, 50))
        display_text("Your answer:", (50, 200))
        display_text(input_text, (50, 250))

        pygame.display.flip()

def display_text(text, position):
    rendered_text = font.render(text, True, WHITE)
    screen.blit(rendered_text, position)

def main():
    clock = pygame.time.Clock()
    responses_count = {key: 0 for key in responses}

    for question in questions:
        answer = ask_question(question)

        # Check the answer and update responses_count
        for key, values in responses.items():
            if answer.lower() in [value.lower() for value in values]:
                responses_count[key] += 1

    # Determine the final result
    final_result = max(responses_count, key=responses_count.get)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        display_text("Personality Quiz Result:", (50, 50))
        display_text(f"You are {final_result}!", (50, 150))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
