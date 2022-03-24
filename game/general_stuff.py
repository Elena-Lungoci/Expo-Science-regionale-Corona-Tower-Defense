import pygame
import os

from pygame.transform import scale
pygame.font.init()
import math
import random


clock = pygame.time.Clock()

program_run = True
#dimensions
SCREEN_WIDTH = 1540
SCREEN_HEIGHT = 795


#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (153,153,153)
GREEN = (0,255, 0)
BLUE = (0,191,255)

DRED = (102, 0,0)

TGREEN = (255,0,0, 100)
TGREY = (32,32,32,200)


#is this ok?
FPS = 60

B_CELL_LOCATION = (1050, 150)
HELPER_T_CELL_LOCATION = (800, 75)
KILLER_T_CELL_LOCATION = (1030, 638)
MEMORY_B_LOCATION = (850, 75)
PLASMA_LOCATION = (800,64)
DENDRITIC_CELL_LOCATION = (86,710)

CELLS_SPAWN_RATE = 10

PATH1 = [(600, 292), (661, 331), (731, 385), (756, 406), (778, 434), (794, 471), (804, 495), (814, 530), (819, 569), (799, 604), (769, 625), (737, 634), (702, 634), (686, 621)]
PATH2 = [(596, 292), (536, 337), (481, 374), (440, 407), (416, 439), (396, 483), (386, 526), (384, 565), (395, 594), (416, 618), (445, 631), (478, 637), (499, 636), (519, 619)]
PATH3 = [(602, 292), (645, 317), (707, 361), (757, 397), (792, 392), (830, 379), (869, 368), (905, 365), (935, 366), (957, 373), (986, 381), (1007, 389), (1021, 394), (1046, 405), (1065, 416), (1075, 425)]
PATH4 = [(595, 292), (576, 306), (536, 331), (501, 358), (472, 379), (453, 397), (422, 400), (382, 382), (348, 373), (310, 363), (279, 364), (255, 369), (223, 376), (200, 388), (177, 401), (151, 407), (133, 421)]
PATH5 = [(593, 292),  (620, 302), (681, 346), (735, 384), (768, 427), (811, 495), (823, 541), (855, 542), (912, 564), (963, 575), (984, 580), (999, 601), (1017, 616), (1040, 646), (1048, 669), (1048, 694), (1035, 713), (1022, 719), (1003, 723)]
PATH6 = [(602, 292),  (594, 295), (538, 330), (488, 374), (444, 401), (423, 437), (401, 478), (393, 506), (383, 532), (348, 542), (318, 551), (267, 569), (230, 579), (211, 593), (187, 617), (169, 635), (157, 656), (154, 674), (155, 695), (166, 712), (169, 722), (163, 736)]
PATHS = [PATH1, PATH2, PATH3, PATH4, PATH5, PATH6]

BONUS_PATH = [(602, 6), (600, 292), (661, 331), (731, 385), (756, 406), (778, 434), (794, 471), (804, 495), (814, 530), (819, 569), (799, 604), (769, 625), (737, 634), (702, 634), (686, 621)]

path1 = [(1166, 299), (35, 306)]
path2 = [(1185, 413), (15, 420)]
path3 = [(1194, 299), (855, 298), (812, 251), (804, 197), (58, 206)]
path4 = [(1191, 294), (822, 299), (805, 233), (768, 162), (721, 138), (705, 89), (150, 99)]
path5 = [(1193, 416), (856, 430), (863, 503), (858, 529), (854, 546), (76, 533)]
path6 = [(1194, 412), (854, 427), (846, 506), (831, 568), (805, 599), (764, 620), (737, 650), (186, 638)]

ALVEOLI_PATHS = [path1, path2, path3, path4, path5, path6]

CELL_LOCATIONS = [(576, 18), (630, 50), (630, 68), (630, 80), (630, 93), (630, 105), (630, 116), (630, 128), (631, 138), (630, 150), (630, 165), (630, 178), (630, 189), (630, 200), (631, 213), (630, 227), (632, 242), (633, 255), (566, 258), (567, 241), (568, 222), (568, 200), (567, 185), (569, 171), (572, 160), (574, 141), (577, 120), (575, 97), (575, 76), (576, 56), (577, 42), (575, 28), (628, 34), (629, 18)]


square_locations = [(153, 32), (265, 27), (392, 17), (512, 24), (146, 140), (262, 140), (392, 140), (514, 140),  (144, 253), (261, 251), (389, 251), (513, 250), (632, 250), (631, 359), (514, 356), (391, 359), (261, 361), (147, 360), (147, 482), (259, 482), (389, 482), (514, 480), (630, 482), (261, 591), (390, 592), (510, 591), (633, 592)]
square_size = (100, 100)
squares = []


Level_title_font = pygame.font.SysFont('comicsans', 30)

Normal_font = pygame.font.SysFont('calibri', 20)

Cells_font = pygame.font.SysFont('calibri', 15)

Not_enough_font = pygame.font.SysFont('comicsans', 30, bold = True)

class Square:
    def __init__(self, square_location, square_size):
        self.x = square_location[0]
        self.y = square_location[1]
        self.width = square_size [0]
        self.height = square_size[1]

        self.rect = pygame.Rect(self.x, self.y, square_size[0], square_size[1])

        self.occupied = False

for i in square_locations:
    squares.append(Square(i, square_size))

def display_squares(screen):
    
    for square_location in square_locations:

        surface = pygame.Surface(square_size, pygame.SRCALPHA)

        pygame.draw.rect(surface, TGREEN, surface.get_rect(), 100)
        screen.blit(surface, square_location)

        





#much easier to create player.buttons
class Button():
    def __init__(self, x, y, image, screen, display_image = None, range_size = None, range_type = None, images = None):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.screen = screen
        self.selected = False
        self.x = x
        self.y = y
        self.image_index = 0
        if images !=None:
            self.images = images

        if range_size != None:
            self.range_size = range_size

        if display_image == None:
            self.display_image = image
        else:
            self.display_image = display_image

        self.range_type = range_type    #0 = plasma cell, 1 = bcell
        self.show_range = None

        

      
     
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        """pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
      

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
"""

    def range(self):
        surface = pygame.Surface((self.range_size * 4,self.range_size *4), pygame.SRCALPHA)

        pygame.draw.circle(surface, TGREEN, (self.range_size,self.range_size), self.range_size, 0)
        self.screen.blit(surface, (self.x - self.range_size,self.y - self.range_size))

    def range1(self, pos):
        if self.range_type ==1:
            range_rect = pygame.Rect(pos[0] - self.width//2, pos[1] - self.height//2, self.width + self.range_size, self.height)
            surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

            pygame.draw.rect(surface, TGREEN, range_rect, 100)
            self.screen.blit(surface, (0,0))
        if self.range_type == 0:
            surface = pygame.Surface((self.range_size * 4,self.range_size *4), pygame.SRCALPHA)
            pygame.draw.circle(surface, TGREEN, (self.range_size,self.range_size), self.range_size, 0)
            self.screen.blit(surface, (pos[0] - self.range_size,pos[1] - self.range_size))


def scale_image(scale, image):

    width = image.get_width()
    height = image.get_height()

    image = pygame.transform.smoothscale(image, (int(width * scale), int(height * scale)))
    return image

def E_scale(image):
    width = image.get_width()
    height = image.get_height()
    
    new_width = SCREEN_WIDTH-TOWERS_MENU.width
    new_height = new_width/width * height
    
    image = pygame.transform.smoothscale(image, (new_width, int(new_height)))
    
    return image
    
class Info():
    def __init__(self, x, y, box_image, screen, down = True, left = True):
        self.button_image = info_button_image
        self.x = x
        self.y = y
        self.box = box_image
        self.box_width = box_image.get_width()
        self.box_height = box_image.get_height()
        self.info_width = info_button_image.get_width()
        self.info_height = info_button_image.get_height()

        self.screen = screen
        self.rect = info_button_image.get_rect()
        self.rect.topleft = (x,y)

        self.down = down
        self.left = left



    def show(self):
        pos = pygame.mouse.get_pos()
        self.screen.blit(self.button_image, (self.x,self.y))
        if self.rect.collidepoint(pos):
            if self.left:
                x= pos[0] - self.box_width
            else:
                x = pos[0]

            if self.down:
                y = pos[1]

            else:
                y = pos[1] - self.box_height

            self.screen.blit(self.box, (x, y))  
            
#pictures import
#feel free to change any of these, ik they're trash

play_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_jouer.png'))
instruction_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_instructions.png'))
levels_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_niveaux.png'))


background_image = pygame.image.load(os.path.join('data', 'Pictures', 'potential_background_picture.png'))
background_image = scale_image(3, background_image)


humidity_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'humidity_info.png'))
humidity_info_image = scale_image(0.35, humidity_info_image)

temperature_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'Temperature_box.png'))
temperature_info_image = scale_image(0.3, temperature_info_image)
neutrophil_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'Neutrophils_box.png'))
neutrophil_info_image = scale_image(0.5, neutrophil_info_image)
macrophage_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'Macrophage_box.png'))
macrophage_info_image = scale_image(0.5, macrophage_info_image)
bcell_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'LymphocytesB_box.png'))
bcell_info_image = scale_image(0.6, bcell_info_image)
plasma_cell_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'plasma_cells_box.png'))
plasma_cell_info_image = scale_image(0.6, plasma_cell_info_image)
tcell_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'LymphocyteT_box.png'))
tcell_info_image = scale_image(0.6, tcell_info_image)
mucus_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'Mucus_box.png'))
mucus_info_image = scale_image(0.55, mucus_info_image)
cilia_info_image = pygame.image.load(os.path.join('data', 'Pictures', 'cilia_box.png'))
cilia_info_image = scale_image(0.4, cilia_info_image)

lose_image = pygame.image.load(os.path.join('data', 'Pictures', 'lose.png'))
lose_image = scale_image(0.5,lose_image)
win_image = pygame.image.load(os.path.join('data', 'Pictures', 'win.png'))
win_image = scale_image(0.9, win_image)


retry_image = pygame.image.load(os.path.join('data', 'Pictures', 'retry.png'))
retry_image = scale_image(2, retry_image)

button_level1_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_level1.png'))
button_level1_image = scale_image(2, button_level1_image)
button_level2_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_level2.png'))
button_level2_image = scale_image(2, button_level2_image)
button_level3_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_level3.png'))
button_level3_image = scale_image(2, button_level3_image)
button_level4_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_level4.png'))
button_level4_image = scale_image(0.22, button_level4_image)



button_exit_image = pygame.image.load(os.path.join('data', 'Pictures', 'button_retour-au-menu-principal.png'))

lungs_image = pygame.image.load(os.path.join('data', 'Pictures', 'lungs.png'))
switch_to_lungs_image = scale_image(0.1, lungs_image)
lungs_image = pygame.transform.scale(lungs_image, (SCREEN_WIDTH - button_exit_image.get_width() -50, SCREEN_HEIGHT))

normal_corona_image = pygame.image.load(os.path.join('data', 'Pictures', 'normal.png'))
normal_corona_image = scale_image(0.1, normal_corona_image)

gamma_image = pygame.image.load(os.path.join('data', 'Pictures', 'gamma.png'))
gamma_image = scale_image(0.1, gamma_image)

alpha_image = pygame.image.load(os.path.join('data', 'Pictures', 'alpha.png'))
alpha_image = scale_image(0.1, alpha_image)

delta_image = pygame.image.load(os.path.join('data', 'Pictures', 'delta.png'))
delta_image = scale_image(0.1, delta_image)


white_blood_cell_image = pygame.image.load(os.path.join('data', 'Pictures', 'Neutrophil.png'))
white_blood_cell_image = scale_image(0.08, white_blood_cell_image)

macrophage_image = pygame.image.load(os.path.join('data', 'Pictures', 'Macrophage.png'))
macrophage_image = scale_image(0.4, macrophage_image)

macrophage_image2 = pygame.image.load(os.path.join('data', 'Pictures', 'macrophage_image2.png'))
macrophage_image2 = scale_image(0.4, macrophage_image2)


plasma_cell_image = pygame.image.load(os.path.join('data', 'Pictures', 'plasma_cell.png'))
displayed_plasma_image = scale_image(0.25, plasma_cell_image)
plasma_cell_image = scale_image(0.2, plasma_cell_image)

lymphocyte_B_image = pygame.image.load(os.path.join('data', 'Pictures', 'B_cell.png'))
lymphocyte_B_image = scale_image(0.2, lymphocyte_B_image)

lymphocyte_B_image2 = pygame.image.load(os.path.join('data', 'Pictures', 'B_cell2.png'))
lymphocyte_B_image2 = scale_image(0.2, lymphocyte_B_image2)

Helper_T = pygame.image.load(os.path.join('data', 'Pictures', 'HelperT.png'))
Helper_T = scale_image(0.08, Helper_T)

Dendritic_cell = pygame.image.load(os.path.join('data', 'Pictures', 'Dendritic_cell.png'))
Dendritic_cell = scale_image(0.08, Dendritic_cell)

Memory_B = pygame.image.load(os.path.join('data', 'Pictures', 'MemoryB.png'))
Memory_B = scale_image(0.08, Memory_B)

tcell_image = pygame.image.load(os.path.join('data', 'Pictures', 'Tcell.png'))
tcell_image = scale_image(0.08, tcell_image)

alveoli_zoom_image = pygame.image.load(os.path.join('data', 'Pictures', 'alveoli_zoom.png'))
alveoli_zoom_image = pygame.transform.rotate(alveoli_zoom_image, 50)
alveoli_zoom_image = scale_image(0.9, alveoli_zoom_image)

cilia_image = pygame.image.load(os.path.join('data', 'Pictures', 'cilia.png'))
cilia_image = scale_image(0.15 ,cilia_image)
cilia_button_image = pygame.transform.scale(cilia_image, (white_blood_cell_image.get_width(), white_blood_cell_image.get_height()))

deployed_cilia_image = pygame.transform.rotate(cilia_image, 90)
deployed_cilia_image = scale_image(0.5, deployed_cilia_image)

mucus_image = pygame.image.load(os.path.join('data', 'Pictures', 'mucus.png'))
mucus_image = scale_image(0.25, mucus_image)
mucus_button_image = pygame.transform.scale(mucus_image, (white_blood_cell_image.get_width(), white_blood_cell_image.get_height()))

deployed_mucus_image = scale_image(0.5, mucus_image)

TOWERS_MENU = pygame.Rect(lungs_image.get_width(), 0, SCREEN_WIDTH - lungs_image.get_width(), SCREEN_HEIGHT)

END_MENU_DIMENSIONS = [700, 500]
END_MENU = pygame.Rect(SCREEN_WIDTH//2 - END_MENU_DIMENSIONS[0]//2, SCREEN_HEIGHT//2 - END_MENU_DIMENSIONS[1]//2, END_MENU_DIMENSIONS[0], END_MENU_DIMENSIONS[1])

alveoli_image = pygame.image.load(os.path.join('data', 'Pictures', 'alveoli.png'))
alveoli_image = pygame.transform.scale(alveoli_image, (SCREEN_WIDTH - TOWERS_MENU.width , SCREEN_HEIGHT))


cell_image = pygame.image.load(os.path.join('data', 'Pictures', 'cell.png'))
cell_image = scale_image(0.05, cell_image)

antibody_image = pygame.image.load(os.path.join('data', 'Pictures', 'antibody.png'))
antibody_image = scale_image(0.1, antibody_image)

temperature1_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature1.png'))
temperature2_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature2.png'))
temperature3_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature3.png'))
temperature4_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature4.png'))
temperature5_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature5.png'))
temperature6_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature6.png'))
temperature7_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature7.png'))
temperature8_image = pygame.image.load(os.path.join('data', 'Pictures', 'temperature8.png'))

boost_arrow_image = pygame.image.load(os.path.join('data', 'Pictures', 'boost_arrow.png'))
boost_arrow_image = scale_image(0.3, boost_arrow_image)

menu_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'menu_button.png'))

menu_button_image2 = scale_image(2, menu_button_image)

info_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'info_button.png'))
info_button_image = scale_image(0.4, info_button_image)

discard_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'discard_button.png'))
discard_button_image = scale_image(3, discard_button_image)


pause_button_image = pygame.image.load(os.path.join('data', 'Pictures', 'pause_button.png'))


E_switch_to_alveoli =  pygame.image.load(os.path.join('data', 'Pictures', 'alveoli_screen_change.png'))
E_switch_to_alveoli = scale_image(0.6, E_switch_to_alveoli)
E_bcells_production =  pygame.image.load(os.path.join('data', 'Pictures', 'bcells_production.png'))
E_bcells_production = E_scale(E_bcells_production)
E_switch_to_lungs =  pygame.image.load(os.path.join('data', 'Pictures', 'change_lungs_screen.png'))
E_switch_to_lungs = E_scale(E_switch_to_lungs)
E_costs =  pygame.image.load(os.path.join('data', 'Pictures', 'costs.png'))
E_costs = E_scale(E_costs)
E_energy =  pygame.image.load(os.path.join('data', 'Pictures', 'energy.png'))
E_energy = E_scale(E_energy)
E_infecting_cells =  pygame.image.load(os.path.join('data', 'Pictures', 'infecting_cells.png'))
E_infecting_cells = E_scale(E_infecting_cells)
E_losing =  pygame.image.load(os.path.join('data', 'Pictures', 'losing.png'))
E_losing = E_scale(E_losing)

E_place_bcell =  pygame.image.load(os.path.join('data', 'Pictures', 'place_bcell.png'))
E_place_bcell = E_scale(E_place_bcell)
E_place_cilia =  pygame.image.load(os.path.join('data', 'Pictures', 'place_cilia.png'))
E_place_cilia = E_scale(E_place_cilia)
E_place_macrophage =  pygame.image.load(os.path.join('data', 'Pictures', 'place_macrophage_fr.png'))
E_place_macrophage = E_scale(E_place_macrophage)
E_place_mucus =  pygame.image.load(os.path.join('data', 'Pictures', 'place_mucus.png'))
E_place_mucus = E_scale(E_place_mucus)

E_place_neutrophil =  pygame.image.load(os.path.join('data', 'Pictures', 'place_neutrophil.png'))
E_place_neutrophil = E_scale(E_place_neutrophil)

E_place_plasma_cells =  pygame.image.load(os.path.join('data', 'Pictures', 'place_plasma_cells.png'))
E_place_plasma_cells = E_scale(E_place_plasma_cells)
E_place_tcells =  pygame.image.load(os.path.join('data', 'Pictures', 'place_tcells.png'))
E_place_tcells = E_scale(E_place_tcells)
E_use_boost =  pygame.image.load(os.path.join('data', 'Pictures', 'use_boost.png'))
E_use_boost = E_scale(E_use_boost)
E_macrophage =  pygame.image.load(os.path.join('data', 'Pictures', 'place_macrophage.png'))
E_macrophage = E_scale(E_macrophage)


arrow_image = pygame.image.load(os.path.join('data', 'Pictures', 'arrow.png'))
arrow_image = scale_image(0.5, arrow_image)

arrow_right = pygame.transform.rotate(arrow_image, 180)

arrow_down = pygame.transform.rotate(arrow_image,90)
#is it dumb to make a class just for this?

class Active_screen:
    def __init__(self, active):
        self.active = active


 


