import pygame
from data.game.general_stuff import *
pygame.font.init()
import time
from pygame.constants import MOUSEBUTTONDOWN

TITLE_FONT = pygame.font.SysFont('comicsans', 50)
pygame.display.set_caption('Corona Tower Defense')

menu_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

play_button = Button(SCREEN_WIDTH//2 - play_button_image.get_width()//2, 250, play_button_image, menu_screen)
levels_button = Button(SCREEN_WIDTH//2 - levels_button_image.get_width()//2, 325, levels_button_image, menu_screen)
instructions_button = Button(SCREEN_WIDTH//2 - instruction_button_image.get_width()//2, 400, instruction_button_image, menu_screen)

buttons = [play_button, levels_button, instructions_button]

run_lvl1 = 1
run_instructions = 6
run_levels = 5

def display_things():

    menu_screen.blit(background_image, (0,0))


    play_button.draw()
    levels_button.draw()
    instructions_button.draw()


    title_text = TITLE_FONT.render('Corona Tower Defense', 1 , WHITE)
    menu_screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 20))


    pygame.display.update()




def main_menu():
    

    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 10

            pos = pygame.mouse.get_pos()
            for button in buttons:
                if event.type == MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                    button.clicked =True
            if event.type == pygame.VIDEORESIZE:
                menu_screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if play_button.clicked == True:
            run = False
            play_button.clicked = False
            return run_lvl1

        if levels_button.clicked == True:
            levels_button.clicked = False
            run = False
            return run_levels
        
        if instructions_button.clicked == True:
            instructions_button.clicked = False
            run = False
            return 6


        display_things()

        for button in buttons:
            button.clicked = False



   

    

if __name__ == '__main__':
    main_menu()




