
import logging
import pygame
from pygame import Vector2
from objects import GameObject, GameLogic


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

    def DrawText(self, text: str, position : Vector2):
        #tet stuff
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = font.render(text, True, green, blue)
        self.textRect = self.text.get_rect()

        # set the center of the rectangular object.
        self.textRect.topleft = (position.x, position.y)
        self.screen.blit(self.text, self.textRect)


        
    def draw(self, gamelogic : GameLogic):
        logging.info("Draw")
        self.screen.fill("blue")

        for drawObject in self.objectList:
            self.DrawObject(drawObject)


        self.DrawText(text=f"Health: '{gamelogic.lifeLeft}'", 
                    position=Vector2(0, 0))
        
        pygame.display.flip()
