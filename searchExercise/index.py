import pygame
import sys
import numpy as np
import abc

from Uninformed.BFS import searchBFS, actionHq
from Uninformed.DFS import DFS
from Uninformed.ID import ID
from Informed.Greedy import Greedy
from Uninformed.UCS import searchBFS_Heapq 
# import interface

pygame.init()

class drawAble(abc.ABC):
    @abc.abstractmethod
    def drawButton(self, button, hovered=False):
        pass

class Color():
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    GRAY=(113,113,113)
    RED=(255,0,0)
    BLUE=(0,0,255)
    GREEN=(0,255,0)

class Config:
    Height,Width=600,800
    WidthBoard = 500
    HeightBoard = 500
    boardRows=3
    boardCols=3
    squareSize= WidthBoard//boardCols
    LineWidth=5
        
class Screen:
    def __init__(self):
        self.screen=pygame.display.set_mode((Config.Width,Config.Height))

class board:
    def __init__(self):
        self.screen=pygame.display.set_mode((Config.WidthBoard,Config.HeightBoard))

class Font():
    def __init__(self):
        self.font = pygame.font.Font(None, 50)
        self.font_board = pygame.font.Font(None, 150)
        
class Button:
    def __init__(self,text:str,x:int,y:int,width=200,height=40):
        self.text=text
        self.rect=pygame.Rect(x,y,width,height)

class Buttons:
    def __init__(self):
        self.buttons=[
            Button("BFS",300,150),
            Button("DFS",300,200),
            Button("UCS",300,250),
            Button("Greedy",300,300),
            Button("ID",300,350),
            Button("QUIT",300,400),
        ]

class drawButtons(drawAble):
    def __init__(self, screen,font:Font,color:Color):
        self.screen=screen
        self.font=font
        self.color=color.GRAY
        self.colorHovered=color.BLUE
        self.White=color.WHITE
    def drawButton(self,button:Button,hovered=False):
        color=self.colorHovered if hovered else self.color
        pygame.draw.rect(self.screen,color,button.rect)
        text=self.font.font.render(button.text, True,self.White)
        textRect=text.get_rect(center=button.rect.center)
        self.screen.blit(text,textRect)

class drawMainMenu:
    def __init__(self,screen):
        self.screen=screen
        self.font=Font()
        self.buttons=Buttons()
        self.drawButtons=drawButtons(screen,self.font, Color())
    def mainMenu(self):
        while True:
            self.screen.fill(Color.WHITE)
            tittle=self.font.font.render("Select Search Algorithm", True,Color.BLACK)
            tittleRect=tittle.get_rect(center=(Config.Width//2,100))
            self.screen.blit(tittle,tittleRect)

            mousePos=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons.buttons:
                        if button.rect.collidepoint(mousePos):
                            return button.text

            for button in self.buttons.buttons:
                hovered=button.rect.collidepoint(mousePos)
                self.drawButtons.drawButton(button,hovered)
            pygame.display.flip()



class drawL():
    # def __init__(self):
    #     self.color=Color.WHITE
    #     self.squareSize=Config.squareSize
    #     self.font=Font()
    @staticmethod
    def drawLines(screen):
        for i in range(1, Config.boardRows):
            pygame.draw.line(screen, Color.WHITE, start_pos=(0, i*Config.squareSize), end_pos=(Config.WidthBoard, i*Config.squareSize), width=Config.LineWidth)
            pygame.draw.line(screen, Color.WHITE, start_pos=(i*Config.squareSize, 0), end_pos=(i*Config.squareSize, Config.HeightBoard), width=Config.LineWidth)
class drawF:
    @staticmethod
    def drawFigures(screen,font,position):
        screen.fill(Color.BLACK)
        drawL.drawLines(screen)
        for num, (x,y) in position.items():
            if num != 0:  # Không vẽ ô trống (0)
                textSurface = font.render(str(num), True, Color.WHITE)
                textRect = textSurface.get_rect(center=(x, y))
                screen.blit(textSurface, textRect)
        pygame.display.update()

class animated():
    @staticmethod
    def animation(boardRows,boardCols,squareSize,pre,next):
        # animating=True
        # currentStep=0
        pre = np.array(pre).reshape((3, 3))
        next = np.array(next).reshape((3, 3))
        prePosition={
            pre[row][col]:(col*squareSize+squareSize//2,row*squareSize+squareSize//2)
            for row in range(boardRows) for col in range(boardCols)
            if pre[row][col]!=0
        }
        nextPosition={
            next[row][col]:(col*squareSize+squareSize//2,row*squareSize+squareSize//2)
            for row in range(boardRows) for col in range(boardCols)
            if next[row][col]!=0
        }
        # pygame.display.update()
        return prePosition, nextPosition

class run:
    def __init__(self, pre,next):
        self.index=0
        self.moveSpeed=5
        self.animating=False
        self.currentStep=0
        self.steps=Config.squareSize//self.moveSpeed
        self.prePosition=pre
        self.nextPosition=next
        self.font=Font()
    def runPuzzle(self,start, end, path):
        # global position, animating, currentStep, prePosition, nextPosition, squareSize

        screenBoard = pygame.display.set_mode((Config.WidthBoard, Config.HeightBoard))
        FPS = 144

        self.currentState = np.array(start).reshape((3, 3))

        position = {
            start[row][col]: (col * Config.squareSize + Config.squareSize // 2, row * Config.squareSize + Config.squareSize // 2)
            for row in range(Config.boardRows) for col in range(Config.boardCols)
            if start[row][col] != 0
        }

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screenBoard.fill(Color.BLACK)
            drawF.drawFigures(screenBoard,self.font.font_board,position)
            pygame.display.update()

            if not self.animating and self.index<len(path)-1:
                self.currentState=np.array(path[self.index+1]).reshape((3,3))
                self.prePosition,self.nextPosition=animated.animation(Config.boardRows,Config.boardCols,Config.squareSize,path[self.index], path[self.index+1])
                self.index+=1
                self.animating=True

            # currenTime= pygame.time.get_ticks()
            if self.animating:
                self.currentStep+=1
                if self.currentStep<self.steps:
                    for num in self.prePosition:
                        x1,y1=self.prePosition[num]
                        x2,y2=self.nextPosition[num]
                        newX=x1+(x2-x1)*(self.currentStep+1)/self.steps
                        newY=y1+(y2-y1)*(self.currentStep+1)/self.steps
                        position[num]=(newX,newY)
                else:
                    position=self.nextPosition.copy()
                    self.animating=False
                    self.currentStep=0
                # pygame.time.delay(10)
            # drawF.drawFigures(screenBoard, start if self.index==0 else path[self.index], position,Color.WHITE,Color.BLACK,self.font.font_board,Config.squareSize)
            drawF.drawFigures(screenBoard,self.font.font_board,position)
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

            if self.index>len(path)-2 and not self.animating:
                pygame.time.wait(4000)
                return
    # def restart():
    #     self.
        
        
# screen=pygame.display.set_mode((Width,Height))

def main(start,end):
    global screen
    
    while True:
        screen = pygame.display.set_mode((Config.Width, Config.Height))
        # algorithm=drawMainMenu.mainMenu(screen)
        mainMenu=drawMainMenu(screen)
        algorithm=mainMenu.mainMenu()
        if algorithm=="BFS":
            path=searchBFS(start,end)
        elif algorithm=="DFS":
            path=DFS(start,end)
        elif algorithm=="UCS":
            path=searchBFS_Heapq(start,end)
        elif algorithm=="ID":
            path=ID(start,end)
        elif algorithm=="Greedy":
            path=Greedy(start,end)
        else:
            print("Ko dung")
            return
        running=True
        # interface.run(WidthBoard,HeightBoard, path)
        runner = run({}, {})
        runner.runPuzzle(start, end, path)
        # while running:
        #     for event in pygame.event.get():
        #         if event.type ==pygame.QUIT:
        #             running=False
        #     screen.fill(WHITE)
        #     pygame.display.flip()
        # pygame.quit()

if __name__ =="__main__":
    start=np.array([
        [2,6,5],
        [0,8,7],
        [4,3,1]
    ])
    # board=start.copy()
    end=np.array([
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ])
    main(start=start,end=end)