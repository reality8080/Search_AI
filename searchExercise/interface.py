import sys
import numpy as np
import pygame
# import searchExercise.BFS
from BFS import search_Heapq, actionHq

pygame.init()

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(113,113,113)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)

WIDTH = 500
HEIGHT = 500

LINEWIDTH = 5
FPS = 60
boardRows = 3
boardCols = 3

squareSize= WIDTH//boardCols
# circleRadius = squareSize//3
# circleWidth = 15
# crossWidth = 25

screen=pygame.display.set_mode((WIDTH, HEIGHT))
# board=np.zeros((boardRows, boardCols))

font = pygame.font.Font(None, 150)

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

def drawLines(color=WHITE):
    for i in range(1, boardRows):
        pygame.draw.line(screen, color, start_pos=(0, i*squareSize), end_pos=(WIDTH, i*squareSize), width=LINEWIDTH)
        pygame.draw.line(screen, color, start_pos=(i*squareSize, 0), end_pos=(i*squareSize, HEIGHT), width=LINEWIDTH)

def drawFigures(board,color=WHITE):
    screen.fill(BLACK)
    drawLines()
    for num, (x,y) in position.items():
        if num != 0:  # Không vẽ ô trống (0)
            textSurface = font.render(str(num), True, WHITE)
            textRect = textSurface.get_rect(center=(x, y))
            screen.blit(textSurface, textRect)
    pygame.display.update()

path=search_Heapq(start,end)
# if path:
#     currState=start.copy()
#     for move in path:
#         for nextState, m in actionHq(currState):
#             if m==move:
#                 currState=nextState
#                 drawFigures(currState)
#                 pygame.time.wait(500)
#                 break
index=0
lastUpdateTime=pygame.time.get_ticks()
moveDelay=20
moveSpeed=10
animating=False
currentStep=0
steps=squareSize//moveSpeed


position={num:(x,y) for y,row in enumerate(start) for x,num in enumerate(row)}

def animation(pre,next):
    global position,animating, currentStep,prePosition,nextPosition
    animating=True
    currentStep=0
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
   
currentState = start.copy()
while True:
    screen.fill(BLACK)
    drawFigures(currentState)
    pygame.display.update()

    # currentTime=pygame.time.get_ticks()
    # if(index<len(path) and currentTime-lastUpdateTime>=moveDelay):
    #     board=path[index]
    #     index+=1
    #     lastUpdateTime=currentTime

    currenTime= pygame.time.get_ticks()
    if animating and index<len(path)-1:
        lastUpdateTime=currenTime
        currentStep+=1
        if currentStep<=steps:
            for num in prePosition:
                x1,y1=prePosition[num]
                x2,y2=nextPosition[num]
                newX=x1+(x2-x1)*(currentStep+1)/steps
                newY=y1+(y2-y1)*(currentStep+1)/steps
                position[num]=(newX,newY)
        else:
            position=nextPosition.copy()
            animating=False
            index+=1
        # pygame.time.delay(10)
    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    if not animating and index<len(path)-1:
        currentState=np.array(path[index+1]).reshape((3,3))
        animation(path[index], path[index+1])

    pygame.time.Clock().tick(FPS)

pygame.quit()
sys.exit()
