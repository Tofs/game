from re import A
from pygame import Vector2, Rect
from enum import Enum


class BaseGameObject:
    def __init__(self, position: Vector2 = Vector2(0,0), color: str = "pink"):
        self.color = color
        self.position = position
        self.size = 10

type gameObjectList = list[GameObject]

class GameLogic:
    def __init__(self, gameObjects: gameObjectList, chaseTarget: BaseGameObject):
        self.gameObjects = gameObjects
        self.chaseTarget = chaseTarget

class GameObject(BaseGameObject):
    def __init__(self, position: Vector2 = Vector2(0, 0), color: str = "pink"):
        self.velocity = Vector2(0,0)
        super().__init__(position, color)

    def update(self, gameLogic: GameLogic):
        bounchBack = 10
        if self.position.x < 0:
            self.velocity.x += bounchBack
        if self.position.y < 0:
            self.velocity.y += bounchBack

        if self.position.x > 1280:
            self.velocity.x -= bounchBack
        if self.position.y > 800:
            self.velocity.y -= bounchBack

        
        rectSize = self.size * 1.5
        thisRect = Rect(self.position.x, self.position.y, 0,0).inflate(rectSize,rectSize)

        for collideObject in gameLogic.gameObjects:
            if collideObject is self:
                continue
            otherRect = Rect(collideObject.position.x, collideObject.position.y, 0,0).inflate(rectSize,rectSize)
            if thisRect.colliderect(otherRect):
                collideObject.velocity = Vector2()
                self.velocity = Vector2()

        self.position += self.velocity
        self.velocity *= 0.95

class Chaser(GameObject):
    def __init__(self, position: Vector2 = Vector2(0, 0), color: str = "green"):
        super().__init__(position, color)

    def update(self, gameLogic: GameLogic):
        bounchBack = 10
        if self.position.x < 0:
            self.velocity.x += bounchBack
        if self.position.y < 0:
            self.velocity.y += bounchBack

        if self.position.x > 1280:
            self.velocity.x -= bounchBack
        if self.position.y > 800:
            self.velocity.y -= bounchBack

        vector = gameLogic.chaseTarget.position - self.position
        vector = vector.normalize()
        self.velocity += vector

        self.position += self.velocity
        self.velocity *= 0.95

class Spawner(GameObject):
    def __init__(self, position: Vector2 = Vector2(0, 0), color: str = "red"):
        self.spawnIntervall = 10 # in seconds
        self.spawnCoutner = 0
        super().__init__(position, color)

    def update(self, gameLogic: GameLogic):
        if self.spawnCoutner / 60 > self.spawnIntervall:
            self.spawnCoutner = 0
           gameLogic.gameObjects.append(Chaser(position=self.position.copy()))
        

        self.spawnCoutner += 1
