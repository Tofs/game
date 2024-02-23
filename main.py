from pygame import Vector2
import pygame
import logging
import time
from objects import Castle, GameLogic, GameObject, Spawner, gameObjectList
from drawSurface import DrawSurface



#configure logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Start game!")


#object deff
objectList : gameObjectList = []
spawnpoint: GameObject = Spawner(
    position=Vector2(0, 400),
)
defender: GameObject = GameObject()
castle: GameObject = Castle()
objectList.append(spawnpoint)
objectList.append(castle)
gameLogic = GameLogic(objectList, castle=castle)
gameLogic.gameObjects.append(defender)

# create surface
logging.debug("Configure pygame")
screen = DrawSurface(objectList)
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
                defender = GameObject()
                objectList.append(defender)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        defender.velocity.y -= 30 * dt
    if keys[pygame.K_s]:
        defender.velocity.y += 30 * dt
    if keys[pygame.K_a]:
        defender.velocity.x -= 30 * dt
    if keys[pygame.K_d]:
        defender.velocity.x += 30 * dt

    logging.info("Update")
    for updateObject in objectList:
        updateObject.update(gameLogic)

    screen.draw(gamelogic=gameLogic)

    dt = clock.tick(60) / 1000
    util = 1000 / 60
    logging.debug("loop execution time: " + str(dt * 1000) + "ms utilazation " + str(util) + "%")

    if gameLogic.lifeLeft <= 0:
        run = False

logging.info("End game!")

