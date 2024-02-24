import pygame

from pygame.locals import *

pygame.init()

canvas = pygame.display.set_mode((800,800))

pygame.display.set_caption("Growth Game")
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    pygame.display.update()