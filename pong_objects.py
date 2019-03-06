import pygame
from pygame.math import Vector2

NEUTRAL = 0
PLAYER1 = 1
PLAYER2 = 2

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(0,0)

        self.image = pygame.image.load('spiller.jpg')
        self.image = pygame.transform.scale(self.image, (20,80))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

class Ball(pygame.sprite.Sprite):
    def __init__(self, position, color, width, height, x_mid):
        pygame.sprite.Sprite.__init__(self)
        self.position = position

        self.speed = Vector2(0,0)
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        self.x_mid = x_mid
        self.owner = NEUTRAL

    def update(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        if self.owner == PLAYER2 and self.rect.x < self.x_mid:
            self.image.fill((255,255,255))
        if self.owner == PLAYER1 and self.rect.x > self.x_mid:
            self.image.fill((255,255,255))
        if self.owner > NEUTRAL:
            if self.rect.x > self.x_mid and self.owner == PLAYER2:
                self.image.fill((0,0,0))
            elif self.rect.x < self.x_mid and self.owner == PLAYER1:
                self.image.fill((0,0,0))
        if self.owner == NEUTRAL:
            self.image.fill((255,255,255))

    def color(self, color):
        self.image.fill(color)

class Wall(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(0,0)

        self.image = pygame.image.load('spiller.jpg')
        self.image = pygame.transform.scale(self.image, (1200,1))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

class Side_Wall(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(0,0)

        self.image = pygame.image.load('spiller.jpg')
        self.image = pygame.transform.scale(self.image, (7,125))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

class Goal(pygame.sprite.Sprite):
    def __init__(self, position, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(0,0)

        self.speed = Vector2(0,0)
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

class Power_Up(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(0,0)

        self.image = pygame.image.load('Mystery_box.png')
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y
