
import logging
import pygame

class GameObject:
    def __init__(self):
        self.color = "pink"
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(0,0)
        self.size = 10


class drawSurface:
    def __init__(self, objectList):
        logging.info("init draw")
        pygame.init()
        # TODO: Read display settings from settings file.
        self.screen =  pygame.display.set_mode((1280, 800))
        self.objectList = objectList

    def DrawObject(self, drawObject: GameObject):

        point = pygame.mouse.get_pos()
        rect = pygame.Rect(drawObject.position.x, drawObject.position.y, 0,0).inflate(drawObject.size, drawObject.size)
        collide = rect.collidepoint(point)
        color = (255, 0, 0) if collide else drawObject.color
        pygame.draw.circle(self.screen, color, drawObject.position, drawObject.size)
        
    def draw(self):
        logging.info("Draw")
        self.screen.fill("blue")

        for drawObject in self.objectList:
            self.DrawObject(drawObject)

        pygame.display.flip()