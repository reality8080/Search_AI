import pygame

def drawBtn(screen, font, BLUE, GRAY, White, button,hovered):
    label,rect=button
    color=BLUE if hovered else GRAY
    pygame.draw.rect(screen,color,rect)
    text=font.render(label,True,White)
    textRect=text.get_rect(center=rect.center)
    screen.blit(text,textRect)