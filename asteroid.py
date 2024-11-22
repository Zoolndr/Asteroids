import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.posit = pygame.Vector2(x, y)
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.posit, self.radius, 2)
        
    def update(self, dt):
        self.posit += (self.velocity * dt)