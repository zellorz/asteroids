import pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Hello, Pygame!")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    pygame.display.flip()
    clock.tick(60)
pygame.quit()