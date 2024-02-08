import pygame
import sys
 
# Initialize the game

pygame.init()

# Create the screen
gamewindow = pygame.display.set_mode((320, 540))

WHITE = (255, 255, 255)

while True:

 for event in pygame.event.get():
      if event.type==pygame.QUIT:
        sys.exit()
        gamewindow.fill(WHITE)
        pygame.display.flip()

#createthe textsurface
        # text=font.render("HelloWorld",True,BLACK)

        # screen.blit(text,(screen.get_width()text.get_width())/2,
        #         (screen.get_height()-text.get_height())/2)

pygame.display.flip()