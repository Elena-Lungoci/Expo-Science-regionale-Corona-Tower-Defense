from data.game.general_stuff import *
from data.game.Economy import *
from os import closerange
import pygame
from pygame.constants import MOUSEBUTTONDOWN
from data.game.Cilia_and_mucus import*
from data.game.Enemy import Enemy
from data.game.White_blood_cells import *
from data.game.Lymphocytes import *
pygame.font.init()
from data.game.Cell import *
from data.game.Antibody_Production import *
from data.game.Temperature import *
from data.game.Levels import *



Data_font = pygame.font.SysFont('calibri', 15)


class Player:
    def __init__(self, variant):
        self.energy = economy.start_energy
        self.max_energy = economy.max_energy
        self.max_temperature = 50
        self.temperature = 20 #idk whats normal body temprature but change this later
        self.won = False
        self.lost = False
        self.infected_cells_count = 0
        self.humidity = 1
        self.max_humidity = economy.max_humidity



        self.times = None

        self.not_enough_energy = False
        self.run = True





        self.level1_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        self.humidity_info = Info(SCREEN_WIDTH- TOWERS_MENU.width , 90, humidity_info_image, self.level1_screen)




        self.exit_button = Button(SCREEN_WIDTH - menu_button_image.get_width() - 10,+10, menu_button_image, self.level1_screen)

        self.white_blood_cell_button =  Button(SCREEN_WIDTH- TOWERS_MENU.width + TOWERS_MENU.width//4 -white_blood_cell_image.get_width()//2, 230, white_blood_cell_image, self.level1_screen)

        self.macrophage_button =  Button(SCREEN_WIDTH- TOWERS_MENU.width//4 - macrophage_image.get_width()//2, self.white_blood_cell_button.y -20, macrophage_image, self.level1_screen)

        self.plasma_cell_button = Button(SCREEN_WIDTH- TOWERS_MENU.width//4 -plasma_cell_image.get_width()//2, 520, plasma_cell_image, self.level1_screen, displayed_plasma_image, range_type= 0, range_size=economy.plasma_cell_range)
        self.Bcell_button = Button(SCREEN_WIDTH- TOWERS_MENU.width + TOWERS_MENU.width//4 -plasma_cell_image.get_width()//2, 370, lymphocyte_B_image, self.level1_screen, range_type=1, range_size=economy.bcell_range)

        self.Tcell_button = Button(SCREEN_WIDTH- TOWERS_MENU.width//4 - tcell_image.get_width()//2, self.Bcell_button.y +10, tcell_image, self.level1_screen)

        self.switch_to_alveoli_screen_button = Button(820, 0, alveoli_zoom_image, self.level1_screen)
        self.switch_to_lungs_button = Button(0,0, switch_to_lungs_image, self.level1_screen)

        self.cilia_button = Button(SCREEN_WIDTH- TOWERS_MENU.width + TOWERS_MENU.width//4 -cilia_image.get_width(), 675, cilia_image, self.level1_screen, deployed_cilia_image)
        self.mucus_button = Button(SCREEN_WIDTH- TOWERS_MENU.width//4 - mucus_image.get_width(), self.cilia_button.y + self.cilia_button.height - mucus_image.get_height(), mucus_image, self.level1_screen, deployed_mucus_image)

        self.boost_button = Button(SCREEN_WIDTH-TOWERS_MENU.width + TOWERS_MENU.width//4 -boost_arrow_image.get_width()//2 +50, self.plasma_cell_button.y, boost_arrow_image, self.level1_screen)

        self.discard_button =  Button(SCREEN_WIDTH - TOWERS_MENU.width//2 - discard_button_image.get_width()//2, self.Bcell_button.y + discard_button_image.get_height() -100, discard_button_image, self.level1_screen)



        self.temperature = Temperature(self.level1_screen, self.boost_button)

        self.pause_button = Button(self.exit_button.x - pause_button_image.get_width() - 5, self.exit_button.y, pause_button_image, self.level1_screen)



        self.lungs_screen_buttons = [self.exit_button, self.switch_to_alveoli_screen_button, self.cilia_button, self.mucus_button, self.plasma_cell_button, self.Tcell_button, self.boost_button, self.discard_button, self.pause_button]
        self.alveoli_screen_buttons = [self.white_blood_cell_button, self.exit_button, self.switch_to_lungs_button, self.macrophage_button, self.plasma_cell_button, self.Tcell_button, self.Bcell_button, self.boost_button, self.discard_button, self.pause_button]
        self.buttons = self.lungs_screen_buttons + self.alveoli_screen_buttons
        self.selected_buttons = [self.cilia_button, self.mucus_button, self.plasma_cell_button, self.Tcell_button, self.white_blood_cell_button, self.macrophage_button, self.Bcell_button]
        self.end_buttons = []

        self.lungs_screen = Active_screen(True)
        self.alveoli_screen = Active_screen(False)
        self.clicks = []
    
        self.lungs_screen.active = True
        self.alveoli_screen.active = False

        self.alveoli_enemies = []

        self.enemies = [Enemy(2, self.level1_screen, variant.image, BONUS_PATH, ALVEOLI_PATHS[1], economy.first_enemy_kill_reward)]
        
        self.wb_cells = [White_Blood_Cell(3, self.level1_screen, 441, 409, macrophage_image, self, 1)]
        self.timer = 0
        self.cilias = []
        self.mucus = []
        self.cells = [Cell(self.level1_screen, CELL_LOCATIONS[0], cell_image, 0, 0)]
        self.infected_cells = []
        self.lymphocytes_T = []
        self.lymphocytes_B = []
        self.plasma_cells = []
        self.antibodies = []

        self.towers = self.wb_cells + self.cilias + self.mucus + self.lymphocytes_T + self.lymphocytes_B + self.plasma_cells

        self.Production_Bcell = Bcell(CELL_LOCATIONS[0], self.level1_screen)
        self.Helper_Tcell = HelperT(self.level1_screen, self.Production_Bcell)
        self.Killer_Tcell = KillerT(self.level1_screen)
        self.Dendritic_cell = Dendritic_Cell(self.level1_screen)
        self.First_enemy_death = False


        self.path_index = 0

        self.frame = 0
        self.second = 0
        self.seconds = None

        self.screen = self.level1_screen

        self.ret = None
        self.square_towers = self.lymphocytes_B + self.plasma_cells
        self.paused = False
        
        
        self.instructions = False
        
        self.exit = False
        
        self.pause_infected_cells = False
        self.paused_infected_cells = False
        
        self.change_alveoli = False
        self.changed_alveoli = False
        
        self.change_lungs = False
        self.changed_lungs = False
        
        self.show_macrophage = False
        self.showed_macrophage = False
        
        self.show_energy = False
        self.showed_energy = False
        
        self.clones = Cloned(self.level1_screen)
        
        self.show_clones = False
        
        self.cloning_time = 0
        
        self.show_dendritic_cell = False
        self.showed_dendritic_cell = False
        
        self.dtime = 0
        
        self.mtime = 0
        
        self.ntime = 0
        
        self.ctime = 0
        
        self.ttime = 0
        
        self.show_place = False
        self.showed_place = False
        
        self.show_neutrophil = False
        self.showed_neutrophil = False
        
        self.show_lose = False
        self.showed_lose = False
        
        self.first_finish = False
        
        self.show_costs = False
        self.showed_costs = False
        
        self.mutime = 0
        
        self.show_mucus = False
        self.showed_mucus = False
        self.first_trap = False
        
        self.show_cilia = False
        self.showed_cilia = False
        
        self.show_plasma = False
        self.showed_plasma = False
        
        self.show_temperature = False
        self.showed_temperature = False
        
        self.show_bcell = False
        self.showed_bcell = False
        
        self.show_tcell = False
        self.showed_tcell = False
        
    def show_energy_bar(self):
        length = 300
        energy_length = length / self.max_energy
        green_bar = energy_length * self.energy

        pygame.draw.rect(self.screen, RED, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 60, length, 10), 0)
        pygame.draw.rect(self.screen, GREEN, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 60, green_bar, 10), 0) #x,y,width,height
        energy_text = Data_font.render(f'{self.energy}/{self.max_energy}', 1 , WHITE)
        self.screen.blit(energy_text, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 70))

    def show_humidity(self):
        length = 300
        humidity_length = length / self.max_humidity
        green_bar = humidity_length * self.humidity

        pygame.draw.rect(self.screen, GREY, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 130, length, 10), 0)
        pygame.draw.rect(self.screen, BLUE, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 130, green_bar, 10), 0)

        humidity_text = Data_font.render(f'{self.humidity}/{self.max_humidity}', 1 , WHITE)
        self.screen.blit(humidity_text, (SCREEN_WIDTH- TOWERS_MENU.width + 20, 140))

    def restore_to_default(self):
        pass



    def run_game(self, display_alveoli, display_lungs, display_menu, variant, pause):

        while self.run:
            if self.energy >= self.max_energy:
                self.energy = self.max_energy
            clock.tick(FPS)
            self.timer+= 1
            self.seconds = round(self.timer/60, 2)
            self.frame +=1
            if self.frame == FPS+1:
                self.frame = 1
                self.second +=1
            pos = pygame.mouse.get_pos()  

            

            self.square_towers = self.lymphocytes_B + self.plasma_cells

            for wb_cell in self.wb_cells:
                if wb_cell.type == 1:
                    self.square_towers.append(wb_cell)

            for square in squares:
                square.occupied = False
                for tower in self.square_towers:
                    if square.rect.collidepoint((tower.x, tower.y)):
                        square.occupied = True

            all_squares_occupied = True
            for square in squares:
                if square.occupied == False:
                    all_squares_occupied = False

            
            self.not_enough_energy = False


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.ret =  10
                    self.run = False
                    return 10
                

                #this is  for drawing a path
                '''if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append(pos)
                    print(self.clicks)
'''
                
                # checks if self.buttons are clicked

                if self.lungs_screen.active:
                    for button in self.lungs_screen_buttons:
                        if event.type == pygame.MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                            button.clicked =True

                if self.alveoli_screen.active:
                    for button in self.alveoli_screen_buttons:
                        if event.type == pygame.MOUSEBUTTONDOWN and button.rect.collidepoint(pos):
                            button.clicked =True


                #turns off selections
                if event.type == pygame.MOUSEBUTTONDOWN and self.discard_button.clicked == True:
                    for button in self.buttons:
                            button.selected = False
                            button.clicked = False

                for plasma_cell in self.plasma_cells:
                    if event.type == pygame.MOUSEBUTTONDOWN and plasma_cell.button.selected == True:
                        plasma_cell.button.selected = False

                for bcell in self.lymphocytes_B:
                    if event.type == pygame.MOUSEBUTTONDOWN and bcell.button.selected == True:
                        bcell.button.selected =False



                """add blood cell on click"""
                if event.type == pygame.MOUSEBUTTONDOWN and self.white_blood_cell_button.selected == True and self.alveoli_screen.active == True: 
                    self.wb_cells.append(White_Blood_Cell(3, self.level1_screen, pos[0], pos[1], white_blood_cell_image, self, 0))
                    if self.energy - self.wb_cells[-1].cost < 0:
                        self.wb_cells.remove(self.wb_cells[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.wb_cells[-1].cost

                if event.type == pygame.MOUSEBUTTONDOWN and self.macrophage_button.selected == True and self.alveoli_screen.active == True and all_squares_occupied == False: 
                    self.wb_cells.append(White_Blood_Cell(3, self.level1_screen, pos[0], pos[1], macrophage_image, self, 1))
                    if self.energy - self.wb_cells[-1].cost < 0:
                        self.wb_cells.remove(self.wb_cells[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.wb_cells[-1].cost
                
                #add cilia
                if event.type == pygame.MOUSEBUTTONDOWN and self.lungs_screen.active == True and self.cilia_button.selected == True:
                    self.cilias.append(Cilia(self.level1_screen, pos[0], pos[1], deployed_cilia_image, self.seconds))
                    if self.energy - self.cilias[-1].cost < 0:
                        self.cilias.remove(self.cilias[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.cilias[-1].cost

                #add self.mucus
                if event.type == pygame.MOUSEBUTTONDOWN and self.lungs_screen.active and self.mucus_button.selected:
                    self.mucus.append(Mucus(self.level1_screen, pos[0], pos[1], deployed_mucus_image, self.seconds))
                    if self.energy - self.mucus[-1].cost < 0:
                        self.mucus.remove(self.mucus[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.mucus[-1].cost

                #add Tcells
                if event.type == pygame.MOUSEBUTTONDOWN and self.lungs_screen.active and self.Tcell_button.selected:
                    self.lymphocytes_T.append(Lymphocyte_T(3, self.level1_screen, pos[0], pos[1], tcell_image))
                    if self.energy - self.lymphocytes_T[-1].cost < 0:
                        self.lymphocytes_T.remove(self.lymphocytes_T[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.lymphocytes_T[-1].cost

                #add self.plasma_cells
                if event.type == pygame.MOUSEBUTTONDOWN and self.alveoli_screen.active and self.plasma_cell_button.selected and all_squares_occupied == False:
                    self.plasma_cells.append(Plasma_cell(3, self.level1_screen, pos[0], pos[1], displayed_plasma_image, 1))
                    self.plasma_cells[-1].show()
                    self.alveoli_screen_buttons.append(self.plasma_cells[-1].button)
                    self.buttons.append(self.plasma_cells[-1].button)
                    
                    if self.energy - self.plasma_cells[-1].cost < 0:
                        self.plasma_cells.remove(self.plasma_cells[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.plasma_cells[-1].cost
                #add Bcells
                if event.type == pygame.MOUSEBUTTONDOWN and self.alveoli_screen.active and self.Bcell_button.selected and all_squares_occupied == False:
                    self.lymphocytes_B.append(Lymphocyte_B(self.level1_screen, pos[0], pos[1], lymphocyte_B_image))
                    self.lymphocytes_B[-1].button_init()
                    self.alveoli_screen_buttons.append(self.lymphocytes_B[-1].button)
                    self.buttons.append(self.lymphocytes_B[-1].button)
                    if self.energy - self.lymphocytes_B[-1].cost < 0:
                        self.lymphocytes_B.remove(self.lymphocytes_B[-1])
                        self.not_enough_energy = True
                    else:
                        self.energy -= self.lymphocytes_B[-1].cost

                # self.temperature

                if event.type == pygame.MOUSEBUTTONDOWN and self.temperature.ready == True and self.boost_button.clicked == True:
                    self.temperature.boost = True
                    self.temperature.activate_boost(self)


            
            
                
            self.towers = self.wb_cells + self.cilias + self.mucus + self.lymphocytes_T + self.lymphocytes_B + self.plasma_cells
            #self.temperature
        
            self.temperature.boost_timer(self)

            economy.killerT_cost(self.Killer_Tcell)
            economy.b_cell_cost(self.Production_Bcell)
    
            '''make white blood self.cells follows self.enemies'''
            if self.wb_cells != []:
                
                for i in self.wb_cells:
                    if i.type == 0:
                        i.follow_enemies(self)
                        i.attack(self)
                    elif i.type == 1:
                        i.attack(self)
                    if i.health <= 0:
                        self.wb_cells.remove(i)
                    

            



            """selects white blood cell button"""
            if self.white_blood_cell_button.clicked == True and self.alveoli_screen.active == True:
                self.white_blood_cell_button.clicked = False
                self.white_blood_cell_button.selected = True  

            if self.macrophage_button.clicked == True and self.alveoli_screen.active == True:
                self.macrophage_button.selected = True    

            #select cilia
            if self.cilia_button.clicked == True and self.lungs_screen.active == True:
                self.cilia_button.selected = True

            #select self.mucus
            if self.mucus_button.clicked and self.lungs_screen.active:
                self.mucus_button.selected = True

            #select Tcells
            if self.Tcell_button.clicked and self.lungs_screen.active:
                self.Tcell_button.selected = True

            #select self.plasma_cells
            if self.plasma_cell_button.clicked and self.alveoli_screen.active:
                self.plasma_cell_button.selected = True

            #select Bcells
            if self.Bcell_button.clicked and self.alveoli_screen.active:
                self.Bcell_button.selected = True

            if self.pause_button.clicked == True:
                self.paused = True
                self.pause_button.clicked = False
                return None

            """move self.enemies, remove dead self.enemies"""
            if self.enemies != []:
                for enemy in self.enemies:
                    if enemy.moving == True:
                        enemy.move(self)
                    


                    if enemy.health <= 0:
                            
                        self.enemies.remove(enemy)
                        self.energy += enemy.kill_reward
                        

                    if enemy.alveoli_screen == True:
                        self.enemies.remove(enemy)
                        self.alveoli_enemies.append(enemy)


            if self.alveoli_enemies != []:
                for enemy in self.alveoli_enemies:
                    if enemy.moving == True:
                        enemy.move(self)

                    enemy.attack()
                    if enemy.health <= 0:
                        self.alveoli_enemies.remove(enemy)
                        self.energy += enemy.kill_reward
                        self.First_enemy_death = True
                        if self.showed_energy == False:
                            self.show_energy = True
                            self.showed_energy = True

                    if enemy.finished_path:
                        self.alveoli_enemies.remove(enemy)
                        self.humidity += economy.finish_path_humidity
                        
                        if self.first_finish == False:
                            self.first_finish = True
                        
                    

            #poopoo animation

            if self.First_enemy_death == True:
                self.Production_Bcell.follow_path()

            if self.Production_Bcell.produced_antibodies == True:
                self.Helper_Tcell.follow_path(self)

            if self.First_enemy_death == True:
                self.Killer_Tcell.follow_path()
            
            if self.First_enemy_death == True:
                self.Dendritic_cell.follow_path()
                
            if self.Dendritic_cell.path_point >= 3:
                self.Production_Bcell.collected_antigen = True
                self.Killer_Tcell.collected_antigen = True
                
                
                
            if self.Production_Bcell.produced_antibodies == True:
                
                self.cloning_time += 1/FPS
                
                if self.cloning_time >= 10:
                    self.show_clones = True

            #self.mucus
            if self.mucus != []:
                for m in self.mucus:
                    if m.exist == False:
                        self.mucus.remove(m)
                        
                    m.trap(self)


            #cilia

            if self.cilias != []:
                for cilia in self.cilias:
                    cilia.die(self.seconds)
                    if cilia.exist  == False:
                        self.cilias.remove(cilia)
                    
            #self.cells
            if self.cells != []:
                self.cells[0].infect(self.seconds, self)
                if self.cells[0].exist == False:
                    self.cells[0].die()
                    if self.cells[0].infected ==True:
                        self.infected_cells_count += 1
                        self.infected_cells.append(self.cells[0])
                        if self.paused_infected_cells == False:
                            self.pause_infected_cells = True
                            self.paused_infected_cells = True
                    self.cells.remove(self.cells[0])

                    
            #tcells
            if self.lymphocytes_T != []:
                for lymphocyte in self.lymphocytes_T:
                    lymphocyte.follow_enemies(self)

                    if lymphocyte.health <= 0:
                        self.lymphocytes_T.remove(lymphocyte)

            for bcell in self.lymphocytes_B:
                bcell.attack(self)
                if bcell.health <= 0:
                    self.lymphocytes_B.remove(bcell)
                

                if bcell.button.clicked == True and self.alveoli_screen.active == True:
                    bcell.button.selected = True

            #self.plasma_cells
        
            for lymphocyte in self.plasma_cells:
                lymphocyte.target_enemy(self)
                if self.seconds % lymphocyte.spawn_rate == 0 and self.alveoli_enemies != [] and lymphocyte.followed_enemy != None:
                    self.antibodies.append(Antibody(5, self.level1_screen, lymphocyte.x, lymphocyte.y, antibody_image, lymphocyte.followed_enemy))
                    self.antibodies[-1].followed_enemy.bullets.append(self.antibodies[-1])

                lymphocyte.attack(self)
                if lymphocyte.health <= 0:
                    self.plasma_cells.remove(lymphocyte)
                

                if lymphocyte.button.clicked == True and self.alveoli_screen.active == True:
                    lymphocyte.button.selected = True

                

            #self.antibodies

            for antibody in self.antibodies:
                antibody.follow_enemies(self)
                if antibody.health <= 0:
                    self.antibodies.remove(antibody)

            
            ''''spawn self.enemies every ENEMY_SPAWN_RATE self.seconds'''
            for cell in self.infected_cells:            
                if self.seconds % cell.spawn_rate == 0:

                    self.enemies.append(Enemy(1, self.level1_screen, variant.image, [cell.location] + PATHS[self.path_index], ALVEOLI_PATHS[random.randint(0,5)]))
                    if self.path_index < len(PATHS)-1:
                        self.path_index += 1
                    else:
                        self.path_index =0
            
                if cell.attacked_by != []:
                    cell.attack()

                if cell.health <= 0:
                    self.infected_cells.remove(cell)
                    self.infected_cells_count -= 1

            #spawn self.cells
            if self.seconds % CELLS_SPAWN_RATE == 0:
                self.cells.append(Cell(self.level1_screen, CELL_LOCATIONS[random.randint(0, len(CELL_LOCATIONS) -1)], cell_image, self.seconds, 10))

            if self.seconds == 30 and self.infected_cells_count == 1:  #just for not having a slow start...might remove later
                self.infected_cells_count += 1
                self.infected_cells.append(Cell(self.level1_screen, (617, 205), cell_image, self.seconds))


            #switch between screens

            if self.switch_to_alveoli_screen_button.clicked == True:
                        self.switch_to_alveoli_screen_button.clicked = False
                        self.lungs_screen.active = False
                        self.alveoli_screen.active = True
                        
            if self.switch_to_lungs_button.clicked == True:
                self.switch_to_lungs_button.clicked = False
                self.lungs_screen.active =True
                self.alveoli_screen.active = False

            
            if self.lungs_screen.active == True:
                display_lungs(self, pos)

            if self.alveoli_screen.active == True:
                display_alveoli(self, pos)

            display_menu(self)
            pygame.display.update()

            #win game
            if self.infected_cells_count == 0 and self.enemies == [] and self.alveoli_enemies == []:
                self.won = True
                self.run = False


            #lose game

            if self.humidity >= self.max_humidity:
                self.lost = True
                self.run = False


            #navigation menu
            if self.exit_button.clicked == True:
                self.exit_button.clicked = False
                self.run = False
                self.__init__(variant)
                economy.__init__()
                self.ret = 0
                self.run = False
                return 0

            #makes all self.buttons unclicked
            for button in self.buttons:
                button.clicked = False
                
            if self.instructions:
                if self.showed_energy and self.showed_place == False:
                    self.mtime +=1/60
                    
                    if self.mtime >= 3:               
                        self.showed_place = True
                        self.show_place = True

                if self.changed_alveoli == True and self.changed_lungs == False and self.change_alveoli == False:
                    self.change_lungs = True 
                    self.changed_lungs = True
                    
                    
                if self.changed_lungs == True and self.change_lungs ==False and self.showed_macrophage == False:
                    self.show_macrophage = True
                    self.showed_macrophage = True
                    
                if self.Dendritic_cell.path_point == 3 and self.showed_dendritic_cell == False:
                    
                    self.dtime +=1/60
                    if self.dtime >= 2:
                        self.show_dendritic_cell = True
                        self.showed_dendritic_cell = True
                        
                if self.showed_dendritic_cell and self.showed_neutrophil == False:
                    self.ntime += 1/60
                    
                    if self.ntime >= 2:
                        self.show_neutrophil = True
                        self.showed_neutrophil = True
                    
                if self.first_finish and self.showed_lose == False:
                    self.show_lose = True
                    self.showed_lose = True
                
                if self.showed_neutrophil and self.showed_costs == False:
                    self.ctime +=1/FPS
                    
                    if self.ctime >= 3:
                        self.show_costs = True
                        self.showed_costs = True
                        
                if self.showed_costs and self.showed_mucus == False:
                    
                    self.mutime += 1/ FPS
                    
                    if self.mutime >= 3:
                        if self.energy < economy.mucus_cost:
                            self.energy = economy.mucus_cost
                            
                        self.show_mucus = True
                        self.showed_mucus = True
                    
                if self.first_trap and self.showed_cilia == False:
                    
                    if self.energy < economy.cilia_cost:
                        self.energy = economy.cilia_cost
                    self.show_cilia = True
                    self.showed_cilia = True
                    
                if economy.plasma_cell_cost <= economy.plasma_min_cost and self.showed_plasma == False:
                    if self.energy < economy.plasma_cell_cost:
                        self.energy = economy.plasma_cell_cost
                        
                    self.show_plasma = True
                    self.showed_plasma = True
                    
                if self.temperature.ready and self.showed_temperature == False:
                    self.show_temperature = True
                    self.showed_temperature = True
                    
                    
                if economy.bcell_cost <= economy.bcell_min_cost and self.showed_bcell == False:
                    if self.energy < economy.bcell_cost:
                        self.energy = economy.bcell_cost
                        
                    self.show_bcell = True
                    self.showed_bcell = True
                    
                    
                if economy.tcell_cost <= economy.t_cell_min_cost and self.showed_tcell == False:
                    if self.energy < economy.tcell_cost:
                        self.energy = economy.tcell_cost
                        
                    self.show_tcell = True
                    self.showed_tcell = True
                    
                
            if self.instructions:
                if self.pause_infected_cells == True or self.change_alveoli or self.change_lungs or self.show_macrophage or self.show_energy or self.show_dendritic_cell or self.show_place or self.show_neutrophil or self.show_lose or self.show_costs or self.show_mucus or self.show_cilia or self.show_temperature or self.show_bcell or self.show_plasma or self.show_tcell:
                    self.exit  = True
                    return 0
                
                