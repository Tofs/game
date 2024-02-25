
import logging
import pygame
from pygame import Vector2
from objects import GameObject, GameLogic


class DrawSurface:
    def __init__(self, objectList):
        logging.info("init draw")
        pygame.init()
        # TODO: Read display settings from settings file.
        self.xSize : int = 1300
        self.ySize : int = 800
        self.screen =  pygame.display.set_mode((self.xSize, self.ySize))
        self.objectList = objectList
        self.gridSizeX : int = 26
        self.gridSizeY : int = 16
    
    def DrawGrid(self):
        color = (0,0,0)
        xSize = self.xSize / self.gridSizeX
        ySize = self.ySize / self.gridSizeY
        for x in range(self.gridSizeX):
            for y in range(self.gridSizeY):
                xPos = x * xSize
                yPos = y * ySize
                rect = pygame.Rect(xPos,yPos,xSize, ySize)
                pygame.draw.rect(surface = self.screen, rect = rect, color=color, width = 1)



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

        self.DrawGrid()

        for drawObject in self.objectList:
            self.DrawObject(drawObject)


        self.DrawText(text=f"Health: '{gamelogic.lifeLeft}'", 
                    position=Vector2(0, 0))
        
        pygame.display.flip()
