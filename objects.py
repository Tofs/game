import pygame

class GameObject:
    def __init__(self):
        self.color = "pink"
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        self.size = 10