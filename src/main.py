import pygame

from pygame.locals import *

pygame.init()

# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')


# Creating Path
pathway = pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/path.png')
pathway = pygame.transform.scale(pathway, (150,500))


pygame.display.set_caption("Growth Game")
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    # canvas.blit(grass, (0,0))
    canvas.blit(pathway, (575,0))
    
    pygame.display.update()