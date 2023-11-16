from re import A
from pygame import Vector2, Rect


class BaseGameObject:
    def __init__(self, position: Vector2 = Vector2(0,0), color: str = "pink"):
        self.color = color
        self.position = position
        self.velocity = Vector2()
        self.size = 10

type gameObjectList = list[BaseGameObject]

class GameLogic:
    def __init__(self, gameObjects: gameObjectList, chaseTarget: BaseGameObject):
        self.gameObjects = gameObjects
        self.chaseTarget = chaseTarget
        self.playerAlive = True
    
    def End(self):
        self.playerAlive = False

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
                gameLogic.End()

        self.position += self.velocity
        self.velocity *= 0.95

class Chaser(GameObject):
    def __init__(self, chaseTarget: GameObject,  position: Vector2 = Vector2(0, 0), color: str = "green"):
        self.speedFactor = 0.5
        self.chaseTarget = chaseTarget
        super().__init__(position, color)

    def update(self, gameLogic: GameLogic):
        bounchBack = 10

        # keep object in bounds
        if self.position.x < 0:
            self.velocity.x += bounchBack
        if self.position.y < 0:
            self.velocity.y += bounchBack
        if self.position.x > 1280:
            self.velocity.x -= bounchBack
        if self.position.y > 800:
            self.velocity.y -= bounchBack

        # keep object from stacking
        rectSize = self.size * 1.5
        thisRect = Rect(self.position.x, self.position.y, 0,0).inflate(rectSize,rectSize)
        for collideObject in gameLogic.gameObjects:
            # skip check for self and not other chasers.
            if collideObject is self or type(self) != type(collideObject):
                continue
            otherRect = Rect(collideObject.position.x, collideObject.position.y, 0,0).inflate(rectSize,rectSize)
            if thisRect.colliderect(otherRect):
                vector = self.position - collideObject.position
                vector = vector.normalize()
                self.velocity += vector * 0.1
                collideObject.velocity -= vector * 0.1

        # where should the object head?
        vector = self.chaseTarget.position - self.position
        vector = vector.normalize()

        #update the velocaity
        self.velocity += vector * self.speedFactor
        self.velocity *= 0.95

        # update possition
        self.position += self.velocity

class Spawner(GameObject):
    def __init__(self, position: Vector2 = Vector2(0, 0), color: str = "red"):
        self.spawnIntervall = 3 # in seconds
        self.spawnCoutner = 0
        super().__init__(position, color)

    def update(self, gameLogic: GameLogic):
        if self.spawnCoutner / 60 > self.spawnIntervall:
            self.spawnCoutner = 0
            gameLogic.gameObjects.append(Chaser(chaseTarget=gameLogic.chaseTarget, position=self.position.copy()))
        

        self.spawnCoutner += 1
