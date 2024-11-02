import pygame
from circleshape import CircleShape

#Intended to be used by the Player class

class Shot(CircleShape):
    def __init__(self, position, radius):
        super(Shot, self).__init__(0, 0, radius)
        self.position = position

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2 )

    def update(self, dt):
        self.position +=  self.velocity * dt
