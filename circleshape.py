import pygame
from math import sqrt
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collison_check(self, other: 'CircleShape'):
        collision_trigger = self.radius + other.radius
        # My way to calulate distance
        # distance = sqrt((circle.position[0] - self.position[0])**2 + (circle.position[1] - self.position[1])**2)

        #pygames way
        distance = self.position.distance_to(other.position)

        if  distance <= collision_trigger:
            return True
        
        return False
