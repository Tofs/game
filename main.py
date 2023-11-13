from pygame import Vector2
import pygame
import logging
import time
from objects import GameObject, Spawner
from drawSurface import DrawSurface

type gameObjectList = list[GameObject]
class GameLogic:
    def __init__(self, screen :DrawSurface, objectList: gameObjectList):
        self.screen = screen
        self.objectList = objectList


    def update(self, gameObject: GameObject):
        bounchBack = 10
        if gameObject.position.x < 0:
            gameObject.velocity.x += bounchBack
        if gameObject.position.y < 0:
            gameObject.velocity.y += bounchBack

        if gameObject.position.x > 1280:
            gameObject.velocity.x -= bounchBack
        if gameObject.position.y > screen.screen.get_height():
            gameObject.velocity.y -= bounchBack

        
        rectSize = gameObject.size * 1.5
        thisRect = pygame.Rect(gameObject.position.x, gameObject.position.y, 0,0).inflate(rectSize,rectSize)

        for collideObject in self.objectList:
            if collideObject is gameObject:
                continue
            otherRect = pygame.Rect(collideObject.position.x, collideObject.position.y, 0,0).inflate(rectSize,rectSize)
            if thisRect.colliderect(otherRect):
                collideObject.velocity = Vector2()
                gameObject.velocity = Vector2()
                



        gameObject.position += gameObject.velocity
        gameObject.velocity *= 0.95


#configure logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Start game!")


#object deff
objectList : gameObjectList = []
spawnpoint: GameObject = Spawner(
    position=Vector2(0, 400),
    color="red"
)
activeObject: GameObject = GameObject()
objectList.append(spawnpoint)
objectList.append(activeObject)

# create surface
logging.debug("Configure pygame")
screen = DrawSurface(objectList)
logic  = GameLogic(screen, objectList)
clock = pygame.time.Clock()

logging.info("Enter mainloop")
run = True


while run:


    start_time = time.time()

    logging.info("Handle input")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                activeObject = GameObject()
                objectList.append(activeObject)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        activeObject.velocity.y -= 30 * dt
    if keys[pygame.K_s]:
        activeObject.velocity.y += 30 * dt
    if keys[pygame.K_a]:
        activeObject.velocity.x -= 30 * dt
    if keys[pygame.K_d]:
        activeObject.velocity.x += 30 * dt

    logging.info("Update")
    for updateObject in objectList:
        logic.update(updateObject)

    screen.draw()

    dt = clock.tick(60) / 1000
    util = 1000 / 60
    logging.debug("loop execution time: " + str(dt * 1000) + "ms utilazation " + str(util) + "%")

logging.info("End game!")