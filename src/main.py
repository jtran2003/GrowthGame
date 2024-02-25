import pygame

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')

# Creating Path
pathway = pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/path.png')
pathway = pygame.transform.scale(pathway, (150,500))

# Creating Player
player = pygame.Surface((25,25))
player.fill('Red')
playerYPos = 50


pygame.display.set_caption("Growth Game")
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    canvas.blit(pathway, (575,0))
    canvas.blit(player, (640,playerYPos))
    playerYPos += 2
    canvas.blit(player, (640,playerYPos))

    
    pygame.display.update()
    clock.tick(60)