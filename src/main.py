import pygame

from pygame.locals import *

pygame.init()

# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')

# Creating Path
pathway = pygame.Surface((200,500))
pathway.fill('khaki3')

statBox = pygame.Surface((300, 500))
statBox.fill('blue')

pygame.display.set_caption("Growth Game")
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    canvas.blit(pathway, (550,0 ))
    canvas.blit(statBox, (0, 0))
    
    pygame.display.update()