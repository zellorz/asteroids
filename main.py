import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game loop
    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()