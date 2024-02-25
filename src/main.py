import pygame
import user

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

character = user.User("Player")
grade_level = character.get_grade()


class icon: 
    # For image 
    def __init__(self, x_pos, y_pos, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect(topleft = (x_pos,y_pos))


    def draw(self):
        action = False
        canvas.blit(self.image, self.rect)
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                character.grade.grade += 1
                print("clicked")
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

# Create Frame
canvas = pygame.display.set_mode((1000,500))
canvas.fill('chartreuse4')

# Creating Path
pathway = pygame.image.load('./src/Assets/path.png')
pathway = pygame.transform.scale(pathway, (150,500))

# Grade Font & Surface
font = pygame.font.Font(None, 50)
temp_grade_level = str(grade_level)
font_surface = font.render('Grade Level: ' + temp_grade_level, False, 'Black')

# Creating Player
player = pygame.image.load('./src/Assets/kevin11.png')
player = pygame.transform.scale(player, (75,75))
player_y_pos = 50
player_x_pos = 620
player_rect = player.get_rect(topleft = (player_x_pos,player_y_pos))


mid_img = pygame.image.load('./src/Assets/mid_school.png').convert_alpha()
mid_school = icon(450, 35, mid_img, 0.2)

high_img = pygame.image.load('./src/Assets/high_school.png').convert_alpha()
high_school = icon(450, 35, high_img, 0.2)

col_img = pygame.image.load('./src/Assets/col_uni.png').convert_alpha()
college = icon(750, 35, col_img, 0.2)

uni_img = pygame.image.load('./src/Assets/col_uni.png').convert_alpha()
university = icon(750, 35, uni_img, 0.2)

work_img = pygame.image.load('./src/Assets/work.png').convert_alpha()
work = icon(750, 350, work_img, 0.2)

app_img = pygame.image.load('./src/Assets/trades.png').convert_alpha()
appren = icon(450, 175, app_img, 0.2)

sports_img = pygame.image.load('./src/Assets/sports.png').convert_alpha()
sports = icon(750, 200, sports_img, 0.2)

hobby_img = pygame.image.load('./src/Assets/hobbies.png').convert_alpha()
hobby = icon(450, 350, hobby_img, 0.2)

pygame.display.set_caption("Growth Game")
game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    
    canvas.blit(pathway, (575,0))
    canvas.blit(font_surface, (50,100))
    

    if grade_level < 9:
         mid_school.draw()
    elif grade_level < 13:
        high_school.draw()
    else:
        university.draw()
        appren.draw()
    appren.draw()
    work.draw()
    sports.draw()
    hobby.draw()

    canvas.blit(player, player_rect)

    
    pygame.display.update()
    clock.tick(60)