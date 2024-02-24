import pygame

from pygame.locals import *

pygame.init()

# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')

# Create Grass
grass = pygame.image.load('/grass.png')

# Creating Path
pathway = pygame.Surface((200,500))
pathway.fill('khaki3')

pygame.display.set_caption("Growth Game")
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    canvas.blit(grass, (0,0))
    canvas.blit(pathway, (550,0 ))
    
    pygame.display.update()