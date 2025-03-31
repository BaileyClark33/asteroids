import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            r = self.radius - ASTEROID_MIN_RADIUS
            new1 = Asteroid(self.position.x, self.position.y, r)
            new2 = Asteroid(self.position.x, self.position.y, r)
            new1.velocity = self.velocity.rotate(angle) * 1.2
            new2.velocity = self.velocity.rotate(angle * -1) * 1.2
