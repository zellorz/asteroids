import pygame
from constants import *
from player import Player

def main():
    # Initialize pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Game loop
    running = True
    while running:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black
        player.draw(screen)
        # Update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()