import pygame
from pygame.math import Vector2

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
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.speed = Vector2(0,0)

        self.image = pygame.image.load('spiller.jpg')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def update(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

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
