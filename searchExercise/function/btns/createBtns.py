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
        "QUIT"
    ]
    btns=[]
    for i, label in enumerate(btnLabels):
        x,y,width,height=300,140+45*i,200,40
        btns.append((label,pygame.Rect(x,y,width,height)))
    return btns