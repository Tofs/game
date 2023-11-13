from pygame import Vector2
from enum import Enum

class GameObject:
    def __init__(self, position: Vector2 = Vector2(0,0), color: str = "pink"):
        self.color = color
        self.position = position
        self.velocity = Vector2(0,0)
        self.size = 10


class Spawner(GameObject):
    pass