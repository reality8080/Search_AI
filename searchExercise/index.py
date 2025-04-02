import pygame
import sys
import numpy as np
import timeit, time
import imageio
import os

from Uninformed.BFS import searchBFS
from Uninformed.DFS import DFS
from Uninformed.ID import ID
from Informed.Greedy import Greedy
from Uninformed.UCS import searchBFS_Heapq 
from Informed.AStar import AStar
from Informed.IDAStar import IDAStar
from LocalSearch.RandomHillClimbing import search as RandomHillClimbing
from LocalSearch.SimpHillClimbing import search as SimpHillClimbing
from LocalSearch.SteepesHillClimbing import search as SteepesHillClimbing
from LocalSearch.SimulatedAnnealing import search as SimulatedAnnealing
from LocalSearch.BeamSearch import search as BeamSearch
from LocalSearch.GeneticAlgorithm import search as GeneticAlgorithm

from function.btns.drawMMenu import mainMenu
from function.btns.drawFigure import drawFigures
from function.animated.animation import animation

pygame.init()

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
    

screen=pygame.display.set_mode((Width,Height))


screen=pygame.display.set_mode((WidthBoard,HeightBoard))

font = pygame.font.Font(None, 100)
fontBoard = pygame.font.Font(None, 150)

def main(start,end):
    global screen
    time=None
    algorithmLb=None
    BTN=[]
    while True:
        screen = pygame.display.set_mode((Width, Height))

        algorithm=mainMenu(screen, Width, BLUE, GRAY, WHITE, BLACK,algorithmLb, time, BTN)
        if algorithm=="BFS":
            spaceState,path=searchBFS(start,end)
            timeTaken=timeit.timeit(lambda:searchBFS(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="DFS":
            spaceState,path=DFS(start,end)
            timeTaken=timeit.timeit(lambda:DFS(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="UCS":
            spaceState,path=searchBFS_Heapq(start,end)
            timeTaken=timeit.timeit(lambda:searchBFS_Heapq(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="ID":
            spaceState,path=ID(start,end)
            timeTaken=timeit.timeit(lambda:ID(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="Greedy":
            spaceState,path=Greedy(start,end)
            timeTaken=timeit.timeit(lambda:Greedy(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="AStar":
            spaceState,path=AStar.AStar(start,end)
            timeTaken=timeit.timeit(lambda:AStar.AStar(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="IDAStar":
            spaceState,path=IDAStar(start,end)
            timeTaken=timeit.timeit(lambda:IDAStar(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="SimpleHillClimbing":
            spaceState,path=SimpHillClimbing(start,end)
            timeTaken=timeit.timeit(lambda:SimpHillClimbing(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="SHillClimbing":
            spaceState,path=SteepesHillClimbing(start,end)
            timeTaken=timeit.timeit(lambda:SteepesHillClimbing(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="RHillClimbing":
            spaceState,path=RandomHillClimbing(start,end)
            timeTaken=timeit.timeit(lambda:RandomHillClimbing(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="SimulatedAnne":
            spaceState,path=SimulatedAnnealing(start,end)
            timeTaken=timeit.timeit(lambda:RandomHillClimbing(start,end),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="Beam Search":
            spaceState,path=BeamSearch(start,end,10)
            timeTaken=timeit.timeit(lambda:BeamSearch(start,end,10),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        elif algorithm=="Genetic Algorithm":
            spaceState,path=GeneticAlgorithm(start,end, 100,1000, 0.1)
            timeTaken=timeit.timeit(lambda:GeneticAlgorithm(start,end, 100,1000, 0.1),number=5)
            save_result_to_file("KetQua.txt",algorithm,timeTaken,path,spaceState)
        else:
            print("Ko dung")
            return
        running=True
        runPuzzle(start, 30, path,WHITE,BLACK,WidthBoard,HeightBoard,squareSize,boardRows,boardCols,fontBoard,LineWidth)

def runPuzzle(start, steps, path,WHITE,BLACK,WidthBoard, HeightBoard,squareSize,boardRows,boardCols,fontBoard,LineWidth):
    global position, prePosition, nextPosition

    screenBoard = pygame.display.set_mode((WidthBoard, HeightBoard))
    FPS = 60
    animating=False
    index = 0          
    currentStep=0
    frames = []

    currentState = np.array(start).reshape((3, 3))

    position = {
        start[row][col]: (col * squareSize + squareSize // 2, row * squareSize + squareSize // 2)
        for row in range(boardRows) for col in range(boardCols)
        if start[row][col] != 0
    }

    try:
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screenBoard.fill(BLACK)
            drawFigures(screenBoard,fontBoard,position,WHITE,BLACK,boardRows,squareSize,WidthBoard,HeightBoard,LineWidth)
            
            frame= pygame.surfarray.array3d(screenBoard)
            frames.append(frame)
            
            pygame.display.update()

            if not animating and index<len(path)-1:
                currentState=np.array(path[index+1]).reshape((3,3))
                prePosition,nextPosition=animation(boardRows,boardCols,squareSize,path[index], path[index+1])
                index+=1
                animating=True

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

            drawFigures(screenBoard,fontBoard,position,WHITE,BLACK,boardRows,squareSize,WidthBoard,HeightBoard,LineWidth)
            
            frame=pygame.surfarray.array3d(screenBoard)
            frames.append(frame)
            
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

            if index>len(path)-2 and not animating:
                break
        if frames:
            frames = [frame.swapaxes(0,1) for frame in frames]
            
            selectedFrames=frames[::2]
            timestamp=time.strftime("%Y%m%d_%H%M%S")
            filename=f"puzzleAnimation_{timestamp}.gif"
            imageio.mimsave(filename,selectedFrames,duration=FPS/2)
    except Exception as e:
        print(f"Lỗi khi lưu animation: {e}")
        pygame.time.wait(2000)
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
    