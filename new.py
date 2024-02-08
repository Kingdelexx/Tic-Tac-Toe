import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
PLAYER_SIZE = 50
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Upgraded Game")

# Create player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Create clock
clock = pygame.time.Clock()

# Create falling blocks
blocks = []

# Lives
lives = 5

# Main game loop
while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < WIDTH - PLAYER_SIZE:
        player.x += 5

    # Create falling blocks
    if random.randint(1, 10) == 1:
        block = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
        blocks.append(block)

    # Move and draw falling blocks
    for block in blocks[:]:
        block.y += 5
        pygame.draw.rect(screen, RED, block)

        # Check for collisions with player
        if block.colliderect(player):
            blocks.remove(block)
            lives -= 1

    # Draw player
    pygame.draw.rect(screen, WHITE, player)

    # Display remaining lives
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(FPS)

    # Clear the screen
    screen.fill((0, 0, 0))

# Game over
font = pygame.font.Font(None, 50)
game_over_text = font.render("Game Over", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.delay(3000)

pygame.quit()
sys.exit()
