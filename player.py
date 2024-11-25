import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot



class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
         pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 0)
    

    def rotate(self, dt):
        self.rotation = (self.rotation + PLAYER_TURN_SPEED * dt) % 360


    def update(self, dt):
        self.timer = max(0, self.timer - dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
              
    def move(self, dt):
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    
    def shoot(self):
        if self.timer > 0:
            print("Cannons on Cooldown!")
        else:
            self.timer += PLAYER_SHOOT_COOLDOWN
            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            Shot(self.position.x, self.position.y, direction * PLAYER_SHOOT_SPEED)