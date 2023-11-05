
import logging
import pygame

from objects import GameObject

class DrawSurface:
    def __init__(self, objectList):
        logging.info("init draw")
        pygame.init()
        # TODO: Read display settings from settings file.
        self.screen =  pygame.display.set_mode((1280, 800))
        self.objectList = objectList

    def DrawObject(self, drawObject: GameObject):

        point = pygame.mouse.get_pos()
        rectSize = drawObject.size * 1.5
        rect = pygame.Rect(drawObject.position.x, drawObject.position.y, 0,0).inflate(rectSize,rectSize)
        collide = rect.collidepoint(point)
        color = (255, 0, 0) if collide else drawObject.color
        pygame.draw.circle(self.screen, color, drawObject.position, drawObject.size)
        
    def draw(self):
        logging.info("Draw")
        self.screen.fill("blue")

        for drawObject in self.objectList:
            self.DrawObject(drawObject)

        pygame.display.flip()