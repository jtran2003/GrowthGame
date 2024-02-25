import pygame
import time

pygame.init()

# Create Frame
canvas = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Growth Game")
canvas.fill('black')

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

game_on = True
current_scene = "menu"  

def menu():
    canvas.fill('black')
    canvas.blit(title_surface, (380, 10))
    canvas.blit(name_surface, (100, 100))
    pygame.draw.rect(canvas, 'white', input_rect)
    pygame.draw.rect(canvas, 'white', confirm_rect)
    text_surface_name = base_font.render(user_text, True, (0, 0, 0))
    canvas.blit(text_surface_name, (input_rect.x + 5, input_rect.y + 5))
    pygame.display.update()

def play_scene():
    canvas.fill('chartreuse4')
    # Create Grass
    grass = pygame.image.load('./src/Assets/grass.png')
    # Creating Path
    pathway = pygame.Surface((200, 500))
    pathway.fill('khaki3')
    canvas.blit(grass, (0, 0))
    canvas.blit(pathway, (550, 0))
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
    elif current_scene == "play":
        play_scene()
