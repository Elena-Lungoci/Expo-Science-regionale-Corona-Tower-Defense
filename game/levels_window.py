import pygame
from data.game.general_stuff import *
pygame.font.init()
from pygame.constants import MOUSEBUTTONDOWN


Level_title_font = pygame.font.SysFont('comicsans', 50)

run_level1 = 1
run_level2 = 2
run_level3 = 3
run_main_menu = 0

levels_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


level1_button = Button(SCREEN_WIDTH//5 - button_level1_image.get_width()//2, 325, button_level1_image, levels_screen)
level2_button = Button(SCREEN_WIDTH//5*2 - button_level2_image.get_width()//2, 325, button_level2_image, levels_screen)
level3_button = Button(SCREEN_WIDTH//5*3 - button_level3_image.get_width()//2, 325, button_level3_image, levels_screen)
level4_button = Button(SCREEN_WIDTH//5*4 - button_level4_image.get_width()//2, 325, button_level4_image, levels_screen)


exit_button = Button(SCREEN_WIDTH - button_exit_image.get_width() -50, SCREEN_HEIGHT - button_exit_image.get_height() - 50, button_exit_image, levels_screen)

buttons = [level1_button, level2_button, level3_button, level4_button, exit_button]

def display_things():
    levels_screen.blit(background_image, (0,0))

    Level_title_text = Level_title_font.render('Niveaux:', 1 , WHITE)
    levels_screen.blit(Level_title_text, (SCREEN_WIDTH//2 - Level_title_text.get_width()//2, 20))

    level1_button.draw()
    level2_button.draw()
    level3_button.draw()
    level4_button.draw()

    exit_button.draw()

    

    pygame.display.update()




def levels():

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return 10
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if event.type == MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                    button.clicked = True


        if level1_button.clicked == True:
            run = False
            level1_button.clicked = False
            return 1

        if level2_button.clicked == True:
            run = False
            level2_button.clicked = False
            return 2

        if level3_button.clicked == True:
            run = False
            level3_button.clicked = False
            return 3

        if level4_button.clicked == True:
            level4_button.clicked = False
            return 4

        if exit_button.clicked == True:
            run = False
            exit_button.clicked = False
            return 0



        display_things()
    
        for button in buttons:
            button.clicked = False

   


if __name__ == '__main__':
    levels()