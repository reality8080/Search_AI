import pygame

def createBtn():
    btnLabels=[
        "BFS",
        "DFS",
        "UCS",
        "IDDFS",
        "Greedy",
        "AStar",
        "IDAStar",
        "SimpleHillClimbing",
        "SHillClimbing",
        "RHillClimbing",
        "SimulatedAnne",
        "Beam Search",
        "QUIT"
    ]
    btns=[]
    cols=2
    colWidth=190
    startX=225
    startY=100
    for i, label in enumerate(btnLabels):
        col=i%cols
        row=i//cols
        
        x=startX+col*colWidth
        y=startY+row*45
        
        btns.append((label,pygame.Rect(x,y,180,35)))
    return btns