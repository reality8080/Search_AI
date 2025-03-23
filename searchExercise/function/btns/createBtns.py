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
        x,y,width,height=350,200+45*i,100,40
        btns.append((label,pygame.Rect(x,y,width,height)))
    return btns