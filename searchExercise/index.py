import pygame
import sys
import numpy as np
import timeit

from Uninformed.BFS import searchBFS
from Uninformed.DFS import DFS
from Uninformed.ID import ID
from Informed.Greedy import Greedy
from Uninformed.UCS import searchBFS_Heapq 
from Informed.AStar import AStar
from Informed.IDAStar import IDAStar

# from function.btns.drawButton import drawBtn
# import interface
from function.btns.drawMMenu import mainMenu
# from function.animated.run import runPuzzle
from function.btns.drawFigure import drawFigures
from function.animated.animation import animation

pygame.init()

# class drawAble(abc.ABC):
#     @abc.abstractmethod
#     def drawButton(self, button, hovered=False):
#         pass

# class Color():
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(113,113,113)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

# class Config:
Height,Width=600,800
WidthBoard = 500
HeightBoard = 500
boardRows=3
boardCols=3
squareSize= WidthBoard//boardCols
LineWidth=5
    
# class Screen:
#     def __init__(self):
        # self.
screen=pygame.display.set_mode((Width,Height))

# class board:
#     def __init__(self):
#         self.
screen=pygame.display.set_mode((WidthBoard,HeightBoard))

# class Font():
#     def __init__(self):
        # self.font = pygame.font.Font(None, 50)
        # self.font_board = pygame.font.Font(None, 150)
font = pygame.font.Font(None, 100)
fontBoard = pygame.font.Font(None, 150)

def main(start,end):
    global screen
    time=None
    algorithmLb=None
    BTN=[]
    while True:
        screen = pygame.display.set_mode((Width, Height))
        # screen.fill(WHITE)
        # algorithm=drawMainMenu.mainMenu(screen)
        # mainMenu=mainMenu(screen)
        algorithm=mainMenu(screen, Width, BLUE, GRAY, WHITE, BLACK,algorithmLb, time, BTN)
        if algorithm=="BFS":
            spaceState,path=searchBFS(start,end)
            timeTaken=timeit.timeit(lambda:searchBFS(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="DFS":
            spaceState,path=DFS(start,end)
            timeTaken=timeit.timeit(lambda:DFS(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="UCS":
            spaceState,path=searchBFS_Heapq(start,end)
            timeTaken=timeit.timeit(lambda:searchBFS_Heapq(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="ID":
            spaceState,path=ID(start,end)
            timeTaken=timeit.timeit(lambda:ID(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="Greedy":
            spaceState,path=Greedy(start,end)
            timeTaken=timeit.timeit(lambda:Greedy(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="AStar":
            spaceState,path=AStar.AStar(start,end)
            timeTaken=timeit.timeit(lambda:AStar.AStar(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="IDAStar":
            spaceState,path=IDAStar(start,end)
            timeTaken=timeit.timeit(lambda:IDAStar(start,end),number=1)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        else:
            print("Ko dung")
            return
        running=True
        # interface.run(WidthBoard,HeightBoard, path)
        runPuzzle(start, 30, path,WHITE,BLACK,WidthBoard,HeightBoard,squareSize,boardRows,boardCols,fontBoard,LineWidth)
        # while running:
        #     for event in pygame.event.get():
        #         if event.type ==pygame.QUIT:
        #             running=False
        #     screen.fill(WHITE)
        #     pygame.display.flip()
        # pygame.quit()



def runPuzzle(start, steps, path,WHITE,BLACK,WidthBoard, HeightBoard,squareSize,boardRows,boardCols,fontBoard,LineWidth):
    global position, prePosition, nextPosition

    screenBoard = pygame.display.set_mode((WidthBoard, HeightBoard))
    FPS = 144
    animating=False
    index = 0          
    currentStep=0

    currentState = np.array(start).reshape((3, 3))

    position = {
        start[row][col]: (col * squareSize + squareSize // 2, row * squareSize + squareSize // 2)
        for row in range(boardRows) for col in range(boardCols)
        if start[row][col] != 0
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screenBoard.fill(BLACK)
        drawFigures(screenBoard,fontBoard,position,WHITE,BLACK,boardRows,squareSize,WidthBoard,HeightBoard,LineWidth)
        pygame.display.update()

        if not animating and index<len(path)-1:
            currentState=np.array(path[index+1]).reshape((3,3))
            prePosition,nextPosition=animation(boardRows,boardCols,squareSize,path[index], path[index+1])
            index+=1
            animating=True

        # currenTime= pygame.time.get_ticks()
        if animating:
            currentStep+=1
            if currentStep<steps:
                for num in prePosition:
                    x1,y1=prePosition[num]
                    x2,y2=nextPosition[num]
                    newX=x1+(x2-x1)*(currentStep+1)/steps
                    newY=y1+(y2-y1)*(currentStep+1)/steps
                    position[num]=(newX,newY)
            else:
                position=nextPosition.copy()
                animating=False
                currentStep=0
            # pygame.time.delay(10)
        # drawF.drawFigures(screenBoard, start if index==0 else path[index], position,Color.WHITE,Color.BLACK,font.font_board,Config.squareSize)
        drawFigures(screenBoard,fontBoard,position,WHITE,BLACK,boardRows,squareSize,WidthBoard,HeightBoard,LineWidth)
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

        if index>len(path)-2 and not animating:
            pygame.time.wait(4000)
            return
def save_result_to_file(filename, algorithm, time, path,spaceState):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Thuật toán: {algorithm}\n")
        file.write(f"Thời gian chạy: {time:.6f} giây\n")
        file.write(f"Số trạng thái duyệt: {spaceState}\n")
        file.write(f"Số trạng thái đường đi: {len(path)}\n")
        file.write("Đường đi:\n")
        
        for i, step in enumerate(path):
            file.write(f"\nBước {i + 1}:\n")
            step_matrix = np.array(step).reshape(3, 3)  # Đảm bảo mỗi bước là ma trận 3x3
            for row in step_matrix:
                file.write(" ".join(map(str, row)) + "\n")
                    
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