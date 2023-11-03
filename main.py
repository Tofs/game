from cmath import log
import pygame
import logging
import time

class GameObject:
    def __init__(self):
        self.colour = "pink"
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)

    def update(self):
        self.position += self.velocity
        self.velocity *= 0.9

#configure logging
logging.basicConfig(level=logging.DEBUG)

logging.info("Start game!")

logging.debug("Configure pygame")
pygame.init()

# TODO: Read display settings from settings file.
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()

#object deff
objectList = []
activeObject = GameObject()
objectList.append(activeObject)


logging.info("Enter mainloop")
run = True

def DrawObject(drawObject: GameObject):
    pygame.draw.circle(screen, drawObject.colour, drawObject.position, 40)


while run:
    start_time = time.time()

    logging.info("Handle input")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        activeObject.velocity.y -= 30 * dt
    if keys[pygame.K_s]:
        activeObject.velocity.y += 30 * dt
    if keys[pygame.K_a]:
        activeObject.velocity.x -= 30 * dt
    if keys[pygame.K_d]:
        activeObject.velocity.x += 30 * dt
    if keys[pygame.K_SPACE]:
        activeObject = GameObject()
        objectList.append(activeObject)


    logging.info("Update")
    for updateObject in objectList:
        updateObject.update()



    logging.info("Draw")
    screen.fill("blue")

    for drawObject in objectList:
        DrawObject(drawObject)

    pygame.display.flip()

    execTime = time.time() - start_time
    logging.debug("loop execution time: " + str(execTime))
    dt = clock.tick(60) / 1000

logging.info("End game!")