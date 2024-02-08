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

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Unscramble Game")

# Load background image
background_image = pygame.image.load("background.jpg")  # Replace "background.jpg" with your image file
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Create font
font = pygame.font.Font(None, 36)

# List of words to unscramble
words = ["one", "two", "three", "four", "five", "word"]

def get_scrambled_word():
    word = random.choice(words)
    scrambled_word = list(word)
    random.shuffle(scrambled_word)
    return ''.join(scrambled_word)

def display_text(text, position):
    rendered_text = font.render(text, True, WHITE)
    screen.blit(rendered_text, position)

def main():
    clock = pygame.time.Clock()
    current_word = get_scrambled_word()
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == current_word:
                        current_word = get_scrambled_word()
                        input_text = ""
                        print("Correct! New word:", current_word)  # Print for verification
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.blit(background_image, (0, 0))  # Blit the background image

        display_text("Unscramble the word:", (50, 50))
        display_text(current_word, (50, 100))
        display_text("Your answer:", (50, 200))
        display_text(input_text, (50, 250))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
