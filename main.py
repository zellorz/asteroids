import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up groups

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Game loop
    running = True
    while running:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB for black
        
        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)
        
        for shot in shots:
            if shot.is_off_screen():
                shots.remove(shot)
        
        # Update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
        #Check for collisions
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                return
            
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

if __name__ == "__main__":
    main()