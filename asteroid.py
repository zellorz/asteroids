import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        print(self.velocity)
        self.kill()
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle) * 1.2
        vector2 = self.velocity.rotate(-random_angle) * 1.2

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split1 = Asteroid(self.position, 0, self.radius - ASTEROID_MIN_RADIUS)
            split2 = Asteroid(self.position, 0, self.radius - ASTEROID_MIN_RADIUS)
            split1.velocity = vector1
            split2.velocity = vector2
            print(f"Asteroid split into: {split1.velocity}, {split2.velocity}")


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)