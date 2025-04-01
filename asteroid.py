import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)


        V1 = self.velocity.rotate(random_angle)
        V2 = self.velocity.rotate(-random_angle)


        new_radius = self.radius - ASTEROID_MIN_RADIUS


        new_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)

        new_asteroid_one.velocity = V1 * 1.2
        new_asteroid_two.velocity = V2 * 1.2
