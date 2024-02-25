import pygame

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

class icon:
    # # For blocks 
    # def __init__(self, x_pos, y_pos, color):
    #     self.surface = pygame.Surface((25,25))
    #     self.color = color
    #     self.surface.fill(color)
    #     self.y_pos = y_pos
    #     self.rect = self.surface.get_rect(topleft = (x_pos,y_pos))

      
    
    # For image 
    def __init__(self, x_pos, y_pos, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x_pos,y_pos))
        #self.info = info


    def draw(self):
        action = False
        canvas.blit(self.image, self.rect)
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("clicked")
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')

# Creating Path
pathway = pygame.image.load('./src/Assets/path.png')
pathway = pygame.transform.scale(pathway, (150,500))

# Creating Player
player = pygame.Surface((25,25))
player.fill('Red')
player_y_pos = 50
player_rect = player.get_rect(topleft = (640,player_y_pos))



mid_image = pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/mid_school.png').convert_alpha()
mid_school = icon(475, 50, mid_image, 0.18)

hs_image =  pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/high_school.png').convert_alpha()
high_school = icon(800, 50, hs_image, 0.2)

col_image =  pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/college.png').convert_alpha()
college = icon(475, 200, col_image, 0.18)

uni_image =  pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/uni2.png').convert_alpha()
university = icon(800, 200, uni_image, 0.2)

appren_image =  pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/appren.png').convert_alpha()
appren = icon(475, 350, appren_image, 0.18)

work_image =  pygame.image.load('C:/Users/jzham/PROJECTS/GrowthGame/src/Assets/workplace.png').convert_alpha()
workplace = icon(800, 350, work_image, 0.2)

pygame.display.set_caption("Growth Game")
game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    
    canvas.blit(pathway, (575,0))
    if high_school.draw():
        print("Drugs")
    if mid_school.draw():
        pass
    if college.draw():
        pass
    if university.draw():
        pass
    if workplace.draw():
        pass
    if appren.draw():
        pass
    # sports.draw()
    # hobby.draw()

    canvas.blit(player, player_rect)

     

    #player_y_pos += 2
    #canvas.blit(player, (640,player_y_pos))

    
    pygame.display.update()
    clock.tick(60)