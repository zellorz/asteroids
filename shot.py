import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def is_off_screen(self):
        return (self.position.x < -self.radius or
            self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or
            self.position.y > SCREEN_HEIGHT + self.radius)
        