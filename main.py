from cmath import log
import pygame
import logging
import time
import drawSurface


#configure logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Start game!")


#object deff
objectList = []
activeObject = drawSurface.GameObject()
objectList.append(activeObject)

# create surface
logging.debug("Configure pygame")
game = drawSurface.drawSurface(objectList)
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
                activeObject = drawSurface.GameObject()
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
        updateObject.update()


    game.draw()

    execTime = time.time() - start_time
    logging.debug("loop execution time: " + str(execTime))
    dt = clock.tick(60) / 1000

logging.info("End game!")