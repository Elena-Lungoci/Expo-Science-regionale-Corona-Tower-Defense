from os import closerange
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from data.game.general_stuff import *
from data.game.Cilia_and_mucus import*
from data.game.Enemy import Enemy
from data.game.White_blood_cells import *
from data.game.player import *
from data.game.Lymphocytes import *
pygame.font.init()
from data.game.Cell import *
from data.game.Antibody_Production import *
from data.game.Temperature import *
from data.game.Levels import *




def display_menu(player):

    pygame.draw.rect(player.level1_screen, GREY, TOWERS_MENU)


    

    energy_text = Level_title_font.render('Énergie:', 1 , WHITE)
    player.level1_screen.blit(energy_text, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 10))

    temperature_text = Level_title_font.render('Humidité:', 1 , WHITE)
    player.level1_screen.blit(temperature_text, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 80))


    button_selected = False

    for button in player.selected_buttons:
        if button.selected ==True:
            button_selected = True

    white_blood_cells_text = Level_title_font.render('Globules blancs:', 1 , WHITE)
    cilia_and_mucus_text = Level_title_font.render('Cils et Mucus:', 1 , WHITE)
    cilia_text = Normal_font.render(f'{int(economy.cilia_cost)}', 1 , WHITE)
    mucus_text = Normal_font.render(f'{int(economy.mucus_cost)}', 1 , WHITE)
    wbc_cost_text = Normal_font.render(f'{int(economy.neutrophil_cost)}', 1 , WHITE)
    macrophage_cost_text = Normal_font.render(f'{int(economy.macrophage_cost)}', 1 , WHITE)
    neutrophil_text = Cells_font.render('Neutrophiles', 1 , BLACK)
    boost_text = Cells_font.render('Température', 1 , BLACK)
    macrophage_text = Cells_font.render('Macrophages', 1 , BLACK)
    plasma_cell_text = Cells_font.render('Cellules Plasmatiques', 1 , BLACK)
    Tcell_text = Cells_font.render('Lymphocytes T', 1 , BLACK)
    Bcell_text = Cells_font.render('Lymphocytes B', 1 , BLACK)
    player.pause_button.draw()

    if button_selected == False:

        player.temperature.show()
        player.temperature.button.draw()
        

        player.level1_screen.blit(white_blood_cells_text, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 150))

        
        player.level1_screen.blit(cilia_and_mucus_text, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 625))

       
        player.level1_screen.blit(cilia_text, (player.cilia_button.x + player.cilia_button.width//2 - cilia_text.get_width()//2, player.cilia_button.y + player.cilia_button.height +10))

        
        player.level1_screen.blit(mucus_text, (player.mucus_button.x + player.mucus_button.width//2 - mucus_text.get_width()//2, player.mucus_button.y + player.mucus_button.height + 10))
        
        
        player.level1_screen.blit(wbc_cost_text, (player.white_blood_cell_button.x + player.white_blood_cell_button.width//2 - wbc_cost_text.get_width()//2, player.white_blood_cell_button.y + player.white_blood_cell_button.height + 10))

        
        player.level1_screen.blit(macrophage_cost_text, (player.macrophage_button.x + player.macrophage_button.width//2 - macrophage_cost_text.get_width()//2, player.macrophage_button.y + player.macrophage_button.height + 10))

       
        player.level1_screen.blit(neutrophil_text, (player.white_blood_cell_button.x + player.white_blood_cell_button.width//2 - neutrophil_text.get_width()//2, player.white_blood_cell_button.y - 20))

        
        player.level1_screen.blit(boost_text, (player.white_blood_cell_button.x + player.white_blood_cell_button.width//2 - boost_text.get_width()//2 +20, player.boost_button.y - 20))

        

        player.macrophage_button.draw()
       
        player.level1_screen.blit(macrophage_text, (player.macrophage_button.x + player.macrophage_button.width//2 - macrophage_text.get_width()//2, player.white_blood_cell_button.y - 20))

        
        player.level1_screen.blit(plasma_cell_text, (player.plasma_cell_button.x + player.plasma_cell_button.width//2 - plasma_cell_text.get_width()//2, player.plasma_cell_button.y - 20))

        plasma_cell_cost_text = Normal_font.render(f'{int(economy.plasma_cell_cost)}', 1 , WHITE)
        player.level1_screen.blit(plasma_cell_cost_text, (player.plasma_cell_button.x + player.plasma_cell_button.width//2 - plasma_cell_cost_text.get_width()//2, player.plasma_cell_button.y + player.plasma_cell_button.height + 10))

        
        player.level1_screen.blit(Tcell_text, (player.Tcell_button.x + player.Tcell_button.width//2 - Tcell_text.get_width()//2, player.Tcell_button.y - 20))

        Tcell_cost_text = Normal_font.render(f'{int(economy.tcell_cost)}', 1 , WHITE)
        player.level1_screen.blit(Tcell_cost_text, (player.Tcell_button.x + player.Tcell_button.width//2 - Tcell_cost_text.get_width()//2, player.Tcell_button.y + player.Tcell_button.height + 10))

        player.Bcell_button.draw()
        
        player.level1_screen.blit(Bcell_text, (player.Bcell_button.x + player.Bcell_button.width//2 - Bcell_text.get_width()//2, player.Bcell_button.y -10))

        Bcell_cost_text = Normal_font.render(f'{int(economy.bcell_cost)}', 1 , WHITE)
        player.level1_screen.blit(Bcell_cost_text, (player.Bcell_button.x + player.Bcell_button.width//2 - Bcell_cost_text.get_width()//2, player.Bcell_button.y + player.Bcell_button.height +3))

        player.white_blood_cell_button.draw()
        player.cilia_button.draw()
        player.mucus_button.draw()
        player.plasma_cell_button.draw()
        player.Tcell_button.draw()
        neutrophil_info = Info(player.white_blood_cell_button.x + player.white_blood_cell_button.width//2 - neutrophil_text.get_width()//2 -25, player.white_blood_cell_button.y - 20, neutrophil_info_image, player.level1_screen)
        neutrophil_info.show()
        macrophage_info = Info(player.macrophage_button.x + player.macrophage_button.width//2 - macrophage_text.get_width()//2 - 40, player.white_blood_cell_button.y - 20, macrophage_info_image, player.level1_screen)
        
        bcell_info = Info(neutrophil_info.x,  player.Bcell_button.y -10, bcell_info_image, player.level1_screen)
        bcell_info.show()
        temperature_info = Info(neutrophil_info.x, player.boost_button.y - 20, temperature_info_image, player.level1_screen, False)
        temperature_info.show()
        plasma_cell_info = Info(macrophage_info.x, temperature_info.y, plasma_cell_info_image, player.level1_screen, False)
        plasma_cell_info.show()
        tcell_info = Info(macrophage_info.x, bcell_info.y, tcell_info_image, player.level1_screen)
        tcell_info.show()
        mucus_info = Info(player.mucus_button.x + player.mucus_button.width//2 - mucus_text.get_width()//2 - 70, player.mucus_button.y + player.mucus_button.height -50, mucus_info_image, player.level1_screen, False)
        mucus_info.show()
        cilia_info = Info(temperature_info.x, mucus_info.y, cilia_info_image, player.level1_screen, False)
        cilia_info.show()

        macrophage_info.show()
    else:
        player.discard_button.draw()

    player.exit_button.draw()

    player.show_energy_bar()
    player.show_humidity()

    player.humidity_info.show()
   
    
    
    


def display_lungs(player, pos):
    player.level1_screen.blit(lungs_image, (0,0))

    Level_title_text = Level_title_font.render(f'Cellules infectées: {player.infected_cells_count}', 1 , BLACK)
    player.level1_screen.blit(Level_title_text, (5,5))

    
    player.switch_to_alveoli_screen_button.draw()

    for button in player.selected_buttons:
        if button.selected == True:
            button.range1(pos)
            player.level1_screen.blit(button.display_image, (pos[0] - button.display_image.get_width()//2, pos[1] - button.display_image.get_height()//2))
            

    

    #learning transparent stuff

    """surface = pygame.Surface((1000,100), pygame.SRCALPHA)

    pygame.draw.rect(surface, TGREEN, surface.get_rect(), 100)
    player.level1_screen.blit(surface, (100,100))


    surface = pygame.Surface((1000,1000), pygame.SRCALPHA)

    pygame.draw.circle(surface, TGREEN, (100,100), 100)
    player.level1_screen.blit(surface, (100,100))"""
    
    #comment this later, its just for creating path
    '''for i in player.clicks:
            pygame.draw.circle(player.level1_screen, RED, (i[0], i[1]), 5, 0)
'''
    if player.cilias != []:
        for cilia in player.cilias:
            cilia.show()


    if player.mucus != []:
        for m in player.mucus:
            m.show()

    """show player.enemies"""
    if player.enemies != []:
        for enemy in player.enemies:
            enemy.show()

    if player.cells != []:
        player.cells[0].show()

    for cell in player.infected_cells:
        cell.show()
        cell.health_bar()

    for tcell in player.lymphocytes_T:
        tcell.show()
    if player.not_enough_energy == True:
        player.times = FPS * 1
        Energy_text = Not_enough_font.render('Énergie insuffisante!', 100 , DRED)
        player.level1_screen.blit(Energy_text, ((SCREEN_WIDTH - TOWERS_MENU.width)//2 - Energy_text.get_width()//2, SCREEN_HEIGHT//2 - Energy_text.get_height()//2))

    if player.times != None:
        if player.times > 0:
            Energy_text = Not_enough_font.render('Énergie insuffisante!', 1 , DRED)
            player.level1_screen.blit(Energy_text, ((SCREEN_WIDTH - TOWERS_MENU.width)//2 - Energy_text.get_width()//2, SCREEN_HEIGHT//2 - Energy_text.get_height()//2))
            player.times -= 1

    if player.won == True:
        
        '''pygame.draw.rect(player.level1_screen, BLACK, END_MENU)

        victory_text = Level_title_font.render('Félicitations! Vous avez vaincu la COVID-19!', 1 , GREEN)
        player.level1_screen.blit(victory_text, (END_MENU.x + END_MENU.width//2 - victory_text.get_width()//2, END_MENU.y +20))'''

        player.level1_screen.blit(win_image, (SCREEN_WIDTH//2 - win_image.get_width()//2, SCREEN_HEIGHT//2 - win_image.get_height()//2))

        for button in player.end_buttons:
            button.draw()

    if player.lost == True:

        '''pygame.draw.rect(player.level1_screen, BLACK, END_MENU)

        victory_text = Level_title_font.render('Oh non! Le corona a pris controle de votre corps!', 1 , RED)
        player.level1_screen.blit(victory_text, (END_MENU.x + END_MENU.width//2 - victory_text.get_width()//2, END_MENU.y +20))
'''
        player.level1_screen.blit(lose_image, (SCREEN_WIDTH//2 - lose_image.get_width()//2, SCREEN_HEIGHT//2 - lose_image.get_height()//2))
        for button in player.end_buttons:
            button.draw()
    


def display_alveoli(player, pos):

    player.level1_screen.blit(alveoli_image, (0,0))

    if player.macrophage_button.selected == True or player.plasma_cell_button.selected == True or player.Bcell_button.selected == True:

        display_squares(player.level1_screen)
    

    if player.alveoli_enemies != []:
        for enemy in player.alveoli_enemies:
            enemy.show()


    if player.wb_cells != []:
        for i in player.wb_cells:
            i.show()

            if i.attacking ==True:
                    a = len(i.images)-1
                    if i.image_index < a:
                        i.image_index +=1
                    else:
                        i.image_index = 0
                    
                    i.image = i.images[i.image_index]

    for plasma_cell in player.plasma_cells:
        if plasma_cell.button != None:
            if plasma_cell.button.selected == True:
                plasma_cell.range()
            plasma_cell.button.draw()    
        plasma_cell.health_bar()


    for bcell in player.lymphocytes_B:
        if bcell.button != None:
            if bcell.button.selected == True:
                bcell.show()
            if bcell.attacking ==True:
                a = len(bcell.button.images)-1
                if bcell.button.image_index < a:
                    bcell.button.image_index +=1
                else:
                    bcell.button.image_index = 0
                
                bcell.button.image = bcell.button.images[bcell.button.image_index]

            bcell.button.draw()
        bcell.health_bar()


    for button in player.selected_buttons:
        if button.selected == True:
            button.range1(pos)
            player.level1_screen.blit(button.display_image, (pos[0] - button.display_image.get_width()//2, pos[1] - button.display_image.get_height()//2))
            
    for antibody in player.antibodies:
        antibody.show()
    
    player.Production_Bcell.show()
    player.Helper_Tcell.show()
    player.Killer_Tcell.show()
    player.Dendritic_cell.show()
    
    if player.show_clones:
        player.clones.show()
    
    

    player.switch_to_lungs_button.draw()


    if player.not_enough_energy == True:
        player.times = FPS * 1
        Energy_text = Not_enough_font.render('Énergie insuffisante!', 100 , DRED)
        player.level1_screen.blit(Energy_text, ((SCREEN_WIDTH - TOWERS_MENU.width)//2 - Energy_text.get_width()//2, SCREEN_HEIGHT//2 - Energy_text.get_height()//2))

    if player.times != None:
        if player.times > 0:
            Energy_text = Not_enough_font.render('Énergie insuffisante!', 1 , DRED)
            player.level1_screen.blit(Energy_text, ((SCREEN_WIDTH - TOWERS_MENU.width)//2 - Energy_text.get_width()//2, SCREEN_HEIGHT//2 - Energy_text.get_height()//2))
            player.times -= 1





    if player.won == True:
        
        '''pygame.draw.rect(player.level1_screen, BLACK, END_MENU)

        victory_text = Level_title_font.render('Félicitations! Vous avez vaincu la COVID-19!', 1 , GREEN)
        player.level1_screen.blit(victory_text, (END_MENU.x + END_MENU.width//2 - victory_text.get_width()//2, END_MENU.y +20))'''
        player.level1_screen.blit(win_image, (SCREEN_WIDTH//2 - win_image.get_width()//2, SCREEN_HEIGHT//2 - win_image.get_height()//2))
        for button in player.end_buttons:
            button.draw()

    if player.lost == True:

        '''pygame.draw.rect(player.level1_screen, BLACK, END_MENU)

        victory_text = Level_title_font.render('Oh non! Le corona a pris controle de votre corps!', 1 , RED)
        player.level1_screen.blit(victory_text, (END_MENU.x + END_MENU.width//2 - victory_text.get_width()//2, END_MENU.y +20))'''

        player.level1_screen.blit(lose_image, (SCREEN_WIDTH//2 - lose_image.get_width()//2, SCREEN_HEIGHT//2 - lose_image.get_height()//2))
        for button in player.end_buttons:
            button.draw()
    

    #path
    ''' for i in player.clicks:
            pygame.draw.circle(player.level1_screen, RED, (i[0], i[1]), 5, 0)'''

    
def pause(player, pos):
    
    while player.paused:
        clock.tick(FPS)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player.run = False
                    player.ret =  10
                    player.run = False
                    return 10
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player.paused = False
    
        if player.alveoli_screen.active == True:
            display_alveoli(player, pos)
        else:
            display_lungs(player, pos)
            
            
        display_menu(player)
        
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        
        a = pygame.Rect(0,0, SCREEN_WIDTH, SCREEN_HEIGHT)

        pygame.draw.rect(surface, TGREY, a, SCREEN_WIDTH)
        player.screen.blit(surface, (0,0))
        
        pause_text = Not_enough_font.render("Pause", 100 , WHITE)
        pause_text2 = Not_enough_font.render("Cliquer n'importe où pour continuer", 100 , WHITE)
        player.level1_screen.blit(pause_text, ((SCREEN_WIDTH)//2 - pause_text.get_width()//2, SCREEN_HEIGHT//2 - pause_text.get_height()//2 - pause_text2.get_height()//2))
        player.level1_screen.blit(pause_text2, ((SCREEN_WIDTH)//2 - pause_text2.get_width()//2, SCREEN_HEIGHT//2 - pause_text.get_height()//2 + pause_text2.get_height()//2))
        
        
        
        
        pygame.display.update()
        
        
def instructions_pause(player):
    a = 0
    timer = 0
    
    for button in player.buttons:
        button.clicked = False
        button.selected = False
    while player.exit:
        timer +=1/60
        
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        
        if player.change_alveoli or player.pause_infected_cells or player.show_mucus or player.show_cilia or player.show_tcell:
            player.lungs_screen.active = True
            player.alveoli_screen.active = False
            
        if player.show_macrophage or player.show_energy or player.show_dendritic_cell or player.show_place or player.show_neutrophil or player.show_plasma or player.show_bcell:
            player.lungs_screen.active = False
            player.alveoli_screen.active = True
            
        
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player.run = False
                    player.ret =  10
                    player.run = False
                    return 10
                
                if timer >= 1:
                    if player.lungs_screen.active:
                        for button in player.lungs_screen_buttons:
                            if event.type == pygame.MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                                button.clicked =True

                    if player.alveoli_screen.active:
                        for button in player.alveoli_screen_buttons:
                            if event.type == pygame.MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                                button.clicked =True

                
                    if event.type == pygame.MOUSEBUTTONDOWN and (player.pause_infected_cells == True or player.show_macrophage or player.show_energy or player.show_dendritic_cell or player.show_lose or player.show_energy or player.show_costs):
                        player.exit = False
                        player.pause_infected_cells = False
                        player.show_macrophage = False
                        player.show_energy = False
                        player.show_dendritic_cell = False
                        player.show_lose = False
                        player.show_costs = False
                    
                        
                        for button in player.buttons:
                            button.clicked = False
                    
                    
                    
        if player.alveoli_screen.active == True:
            display_alveoli(player, pos)
        else:
            display_lungs(player, pos)
            
            
        display_menu(player)
        
        if player.pause_infected_cells:
            player.level1_screen.blit(E_infecting_cells, (0, SCREEN_HEIGHT-E_infecting_cells.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_image, (650, 0))                           
            if a >= (FPS + FPS):
                a = 0          
            a +=1
            
        
        if player.change_alveoli:
            player.level1_screen.blit(E_switch_to_alveoli, (0, 0))           
            if a <= FPS:
                player.level1_screen.blit(arrow_image, (1150, 100))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_alveoli_screen_button.clicked == True:
                player.exit = False
                player.change_alveoli = False
                
        if player.change_lungs:
            player.level1_screen.blit(E_switch_to_lungs, (0, SCREEN_HEIGHT-E_switch_to_lungs.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_image, (100, 0))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_lungs_button.clicked == True:
                player.exit = False
                player.change_lungs = False
                
        
        if player.show_macrophage:
            player.level1_screen.blit(E_macrophage, (0, SCREEN_HEIGHT-E_macrophage.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (250, 360))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_lungs_button.clicked == True:
                player.exit = False
                player.change_lungs = False
                
        if player.show_energy:
            player.level1_screen.blit(E_energy, (0, SCREEN_HEIGHT-E_energy.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (SCREEN_WIDTH - TOWERS_MENU.width - arrow_right.get_width()- 25, 0))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_lungs_button.clicked == True:
                player.exit = False
                player.change_lungs = False
                
        if player.show_dendritic_cell:
            player.level1_screen.blit(E_bcells_production, (0, SCREEN_HEIGHT-E_bcells_production.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, ((643 - arrow_right.get_width(), 333- arrow_right.get_height()//2)))  
                player.level1_screen.blit(arrow_right, ((945 - arrow_right.get_width(), 159- arrow_right.get_height()//2)))                            
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_lungs_button.clicked == True:
                player.exit = False
                player.change_lungs = False
                
        if player.show_place:
            player.level1_screen.blit(E_place_macrophage, (0, SCREEN_HEIGHT-E_place_macrophage.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1374 - arrow_right.get_width(), 278- arrow_right.get_height()//2))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.macrophage_button.clicked == True:
                player.exit = False
                player.show_place = False
            
        if player.show_neutrophil:
            player.level1_screen.blit(E_place_neutrophil, (0, SCREEN_HEIGHT-E_place_neutrophil.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1195 - arrow_right.get_width(), 270- arrow_right.get_height()//2))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.white_blood_cell_button.clicked == True:
                player.exit = False
                player.show_neutrophil = False
    
        if player.show_lose:
            player.level1_screen.blit(E_losing, (0, SCREEN_HEIGHT-E_losing.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (SCREEN_WIDTH - TOWERS_MENU.width - arrow_right.get_width()- 25, 100))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_lungs_button.clicked == True:
                player.exit = False
                player.change_lungs = False
            
        if player.show_costs:
            player.level1_screen.blit(E_costs, (0, SCREEN_HEIGHT-E_costs.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1195 - arrow_right.get_width(), 415- arrow_right.get_height()//2))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.switch_to_lungs_button.clicked == True:
                player.exit = False
                player.change_lungs = False
                
        if player.show_mucus:
            player.level1_screen.blit(E_place_mucus, (0, SCREEN_HEIGHT-E_place_mucus.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_down, (1412 - arrow_down.get_width()//2, 671- arrow_down.get_height()))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.mucus_button.clicked == True:
                player.exit = False
                player.show_mucus= False
                
        if player.show_cilia:
            player.level1_screen.blit(E_place_cilia, (0, SCREEN_HEIGHT-E_place_cilia.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_down, (1269 - arrow_down.get_width()//2, 671- arrow_down.get_height()))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.cilia_button.clicked == True:
                player.exit = False
                player.show_cilia = False
                
        if player.show_plasma:
            player.level1_screen.blit(E_place_plasma_cells, (0, SCREEN_HEIGHT-E_place_plasma_cells.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1387 - arrow_right.get_width(), 562- arrow_right.get_height()//2))                          
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.plasma_cell_button.clicked == True:
                player.exit = False
                player.show_plasma = False
                
                
                
        if player.show_temperature:
            player.level1_screen.blit(E_use_boost, (0, SCREEN_HEIGHT-E_use_boost.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1213 - arrow_right.get_width(), 564- arrow_right.get_height()//2))                           
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.boost_button.clicked == True:
                player.exit = False
                player.show_temperature = False
                
        if player.show_bcell:
            player.level1_screen.blit(E_place_bcell, (0, SCREEN_HEIGHT-E_place_bcell.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1225 - arrow_right.get_width(), 423- arrow_right.get_height()//2))                          
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.Bcell_button.clicked == True:
                player.exit = False
                player.show_bcell = False
                
        if player.show_tcell:
            player.level1_screen.blit(E_place_tcells, (0, SCREEN_HEIGHT-E_place_tcells.get_height()))           
            if a <= FPS:
                player.level1_screen.blit(arrow_right, (1382 - arrow_right.get_width(), 424- arrow_right.get_height()//2))                          
            if a >= (FPS + FPS):
                a = 0            
            a +=1           
            if player.Tcell_button.clicked == True:
                player.exit = False
                player.show_tcell = False
        
        
        pygame.display.update()
        

#ok maybe i should start commenting my code
def level1(variant, instructions = False):

    
    player = Player(variant)
    player.__init__(variant)
    player.wb_cells = []
    for square in squares:
                square.occupied = False
                for tower in player.square_towers:
                    if square.rect.collidepoint((tower.x, tower.y)):
                        square.occupied = True


    player.instructions = instructions
    #player.instructions = True
    
    if player.instructions:
        economy.first_enemy_kill_reward = economy.instructions_first_enemy_kill_reward
        economy.cell_spawn_rate = economy.instructions_spawn_rate
        economy.enemy_kill_reward = economy.instructions_enemy_kill_reward
 
    display_squares(player.level1_screen)


    player.__init__(variant)
    
    player.instructions = instructions
    #player.instructions = True
    
    if player.instructions:
        economy.first_enemy_kill_reward = economy.instructions_first_enemy_kill_reward
        economy.cell_spawn_rate = economy.instructions_spawn_rate
        economy.enemy_kill_reward = economy.instructions_enemy_kill_reward
        
        
    '''player.exit = True
    player.change_alveoli = True
    player.instructions = True'''
    
    while player.run:
        
        if player.paused == False and player.exit == False:
            player.run_game(display_alveoli, display_lungs, display_menu, variant, pause)
            
        else:
            pause(player, pygame.mouse.get_pos())
            
        if player.instructions == True:
            instructions_pause(player)
        
        

    
    if player.ret != None:
        return player.ret
    
    for button in player.buttons:
        button.selected = False


    run = True
    #SCREEN_WIDTH//2 - win_image.get_width()//2, SCREEN_HEIGHT//2 - win_image.get_height()//2

    if player.won == True:
        retry_button = Button(SCREEN_WIDTH//2 + win_image.get_width()//4 - retry_image.get_width(), SCREEN_HEIGHT//2 + win_image.get_height()//2 -retry_image.get_height() - 50, retry_image, player.level1_screen)
        player.exit_button2 = Button(SCREEN_WIDTH//2 - win_image.get_width()//4 , retry_button.y, menu_button_image2, player.level1_screen)

    if player.lost == True:
        retry_button = Button(SCREEN_WIDTH//2 + lose_image.get_width()//4 - retry_image.get_width(), SCREEN_HEIGHT//2 + lose_image.get_height()//2 -retry_image.get_height() - 50, retry_image, player.level1_screen)
        player.exit_button2 = Button(SCREEN_WIDTH//2 - lose_image.get_width()//4 , retry_button.y, menu_button_image2, player.level1_screen)

    player.end_buttons.append(retry_button)
    player.end_buttons.append(player.exit_button2)

    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return 10
            
            for button in player.end_buttons:
                    if event.type == MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                        button.clicked =True

        if player.lungs_screen.active == True:
            display_lungs(player, pos)

        if player.alveoli_screen.active == True:
                display_alveoli(player, pos)
        pygame.display.update()

        if player.exit_button2.clicked == True:
            player.__init__(variant)
            economy.__init__()
            return 0
            run = False

        if retry_button.clicked == True:
            player.__init__(variant)
            economy.__init__()
            return variant.variant

        for button in player.end_buttons:
            button.clicked = False

if __name__ == '__main__':
    level1(Variants(1))