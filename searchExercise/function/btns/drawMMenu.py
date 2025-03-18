import pygame
import sys

from function.btns.drawButton import drawBtn
from function.btns.createBtns import createBtn
from function.btns.handleBtn import handleBtn

def mainMenu(screen,Width,BLUE, GRAY, White,BLACK):
    font=pygame.font.Font(None,50)
    btns=createBtn()
    
    while True:
        screen.fill(White)
        tittle=font.render("Select Search Algorithm", True,BLACK)
        tittleRect=tittle.get_rect(center=(Width//2,100))
        screen.blit(tittle,tittleRect)
        
        mousePos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                selectedAlgorithm=handleBtn(btns,mousePos)
                if selectedAlgorithm:
                    return selectedAlgorithm
                
        for btn in btns:
            hovered=btn[1].collidepoint(mousePos)
            drawBtn(screen,font,BLUE, GRAY, White,btn,hovered)
        pygame.display.update()