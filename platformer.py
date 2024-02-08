import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PLAYER_SIZE = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 30
OBSTACLE_SPEED = 5

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Game variables
player_x = WIDTH // 2
player_y = HEIGHT - PLAYER_SIZE
player_dy = 0
gravity = 0.5
jump_power = -10
obstacle_x = WIDTH
obstacle_y = HEIGHT - OBSTACLE_HEIGHT
obstacle_dx = -OBSTACLE_SPEED

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_y == HEIGHT - PLAYER_SIZE:
        player_dy = jump_power

    # Apply gravity
    player_dy += gravity

    # Update player position
    player_y += player_dy

    # Collision with ground
    if player_y >= HEIGHT - PLAYER_SIZE:
        player_y = HEIGHT - PLAYER_SIZE
        player_dy = 0

    # Update obstacle position
    obstacle_x += obstacle_dx

    # Reset obstacle if it goes off screen
    if obstacle_x + OBSTACLE_WIDTH < 0:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - OBSTACLE_HEIGHT

    # Check for collision with obstacle
    if player_x < obstacle_x + OBSTACLE_WIDTH and \
            player_x + PLAYER_SIZE > obstacle_x and \
            player_y < obstacle_y + OBSTACLE_HEIGHT and \
            player_y + PLAYER_SIZE > obstacle_y:
        # Collision detected, game over
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Draw obstacle
    pygame.draw.rect(screen, BLUE, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
