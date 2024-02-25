import pygame

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

class icon:
    # For blocks 
    def __init__(self, x_pos, y_pos, color):
        self.surface = pygame.Surface((25,25))
        self.color = color
        self.surface.fill(color)
        self.y_pos = y_pos
        self.rect = self.surface.get_rect(topleft = (x_pos,y_pos))
        
    
    # For image 
    # def __init__(self):
    #     pass

    def draw(self):
        canvas.blit(self.surface, self.rect)
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("clicked")
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("jasbjdkcm,")
# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')

# Creating Path
pathway = pygame.image.load('./src/Assets/grass.png')
pathway = pygame.transform.scale(pathway, (150,500))

# Creating Player
player = pygame.Surface((25,25))
player.fill('Red')
player_y_pos = 50
player_rect = player.get_rect(topleft = (640,player_y_pos))


# # Attributes Frame
# frame = pygame.Surface((25, 25))
# apprentice.fill('black')
# app_pos = 350

mid_school = icon(475, 50, 'Black')
high_school = icon(475, 50, 'White')
college = icon(800, 50, 'Black')
university = icon(800, 50, 'Black')
work = icon(475, 200, 'Black')
appren = icon(475, 200, 'Black')
sports = icon(800, 200, 'Black')
hobby = icon(475, 350, 'Black')

pygame.display.set_caption("Growth Game")
game_on = True
current_scene = "menu"  

title = pygame.font.SysFont(None, 50)
title_surface = title.render('Growth Game', False, (255, 255, 255))

text = pygame.font.SysFont(None, 40)
name_surface = text.render('What is your name: ', False, (255, 255, 255))

base_font = pygame.font.Font(None, 32)
user_text = ''
active = False
input_rect = pygame.Rect(400, 100, 400, 32)

confirm_text = pygame.font.SysFont(None, 32)
confirm_surface = confirm_text.render('CONFIRM', True, (0, 0, 0))
confirm_rect = pygame.Rect(400, 300, 140, 32)

def menu():
    canvas.fill('black')
    canvas.blit(title_surface, (380, 10))
    canvas.blit(name_surface, (100, 100))
    pygame.draw.rect(canvas, 'white', input_rect)
    pygame.draw.rect(canvas, 'white', confirm_rect)
    text_surface_name = base_font.render(user_text, True, (0, 0, 0))
    canvas.blit(text_surface_name, (input_rect.x + 5, input_rect.y + 5))
    pygame.display.update()

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(pygame.mouse.get_pos()):
                active = True
            if confirm_rect.collidepoint(pygame.mouse.get_pos()):
                current_scene = "play"
            else:
                active = False    
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    
    if current_scene == "menu":
        menu()
    
    canvas.blit(pathway, (575,0))
 
    high_school.draw()
    mid_school.draw()
    college.draw()
    university.draw()
    work.draw()
    appren.draw()
    sports.draw()
    hobby.draw()

    canvas.blit(player, player_rect)


    #player_y_pos += 2
    #canvas.blit(player, (640,player_y_pos))

    
    pygame.display.update()
    clock.tick(60)
