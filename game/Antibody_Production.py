from data.game.general_stuff import *



class Bcell:
    def __init__(self, macrophage_location, screen):
        self.x = B_CELL_LOCATION[0]
        self.y = B_CELL_LOCATION[1]

        self.path = [B_CELL_LOCATION, (452,417), B_CELL_LOCATION]
        self.path_point = 0

        self.moving = True
        self.collected_antigen = False

        self.image = lymphocyte_B_image
        self.screen = screen
        self.width = self.image.get_width()
        self.height = self.image.get_height
        self.vel = 3
        self.iter = 0
        self.texts = [ "Récupère l'antigène...", "Endocytose...production d'anticorps...", "Clonage..."]
        self.current_text = 'Lymphocyte B'
        self.standard_text = 'Lymphocyte B'
        self.text = 'Lymphocyte B'
        self.time = 0
        self.max_time = FPS*5
        self.index = 0

        self.produced_antibodies = False

        self.producing_antibodies_time = 20 #seconds

        self.producing_antibodies_timer = 0
        self.finished_cloning = False

    def follow_path(self):
        

        if self.time != self.max_time:
            self.time+=1

        else:
            self.time =0
            if self.index == 0:
                self.index = 1
            else:
                self.index = 0

        if self.index ==1:
            self.text = self.standard_text
        else:
            self.text = self.current_text

        if self.collected_antigen == True and self.produced_antibodies == False:
            self.current_text = self.texts[1]
            self.producing_antibodies_timer += 1/FPS
            if self.producing_antibodies_timer >= self.producing_antibodies_time:
                self.produced_antibodies = True

        if self.produced_antibodies == True:
            self.current_text = self.texts[2]
        

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))    
        macrophage_text = Cells_font.render(self.text, 1 , BLACK)
        self.screen.blit(macrophage_text, (self.x - macrophage_text.get_width()//2, self.y - 65))       


class HelperT:
    def __init__(self, screen, bcell):
        self.x = HELPER_T_CELL_LOCATION[0]
        self.y = HELPER_T_CELL_LOCATION[1]

        self.bcell_point = (B_CELL_LOCATION[0] - bcell.width//2-50, B_CELL_LOCATION[1])
        
        self.path1 = [HELPER_T_CELL_LOCATION, self.bcell_point]
        self.path2 = [self.bcell_point, HELPER_T_CELL_LOCATION]
        self.path = self.path1
        self.path_point = 0

        self.moving = True
        self.collected_antigen = False

        self.image = Helper_T
        self.screen = screen
        self.width = self.image.get_width()
        self.height = self.image.get_height
        self.vel = 3
        self.iter = 0
        self.texts = [ "Récupère l'antigène...", "Stimule le clonage", "Clonage..."]
        self.current_text = None
        self.standard_text = 'Lymphocyte T auxiliaire'
        self.text = 'Lymphocyte T auxiliaire'
        self.time = 0
        self.max_time = FPS*5
        self.index = 0

    def follow_path(self, player):
        
        if self.moving == True:
         
            p1 = self.path[self.path_point]
            p2 = self.path[self.path_point + 1]

            a = len(self.path)

           

            x_difference = p2[0] - p1[0]
            y_difference = p2[1]-p1[1]

            distance = math.sqrt(x_difference **2 + y_difference **2) #pythagore power


            i = int(distance/self.vel) #number of iterations


            #does this make sense? woow it worked first try
            x_movement = self.vel * x_difference / distance
            y_movement = self.vel * y_difference / distance


            self.x += x_movement
            self.y += y_movement

            self.iter +=1

            #stop iterating at the end of the path
            max_i = self.path_point + 2
            

            if (self.iter == i) and max_i< a:
                self.path_point +=1
                self.iter = 0

            elif (self.iter == i) and max_i>= a:
                        
                self.collected_antigen = True
                self.moving = False


            self.current_text = self.texts[0]


        if self.time != self.max_time:
            self.time+=1

        else:
            self.time =0
            if self.index == 0:
                self.index = 1
            else:
                self.index = 0

        if self.index ==1:
            self.text = self.standard_text
        else:
            self.text = self.current_text

        if self.collected_antigen == True:
            self.current_text = self.texts[1]

        if player.Production_Bcell.finished_cloning == True:
            self.moving = True
            self.path = self.path2

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))    
        macrophage_text = Cells_font.render(self.text, 1 , BLACK)
        if self.moving == True:
            self.screen.blit(macrophage_text, (self.x - macrophage_text.get_width()//2, self.y - 65))       

        else:
            self.screen.blit(macrophage_text, (self.x - macrophage_text.get_width()//2, self.y + 65))

class KillerT:
    def __init__(self,screen):
        self.x = KILLER_T_CELL_LOCATION[0]
        self.y = KILLER_T_CELL_LOCATION[1]

        self.path = [KILLER_T_CELL_LOCATION, (452,417), KILLER_T_CELL_LOCATION]
        self.path_point = 0

        self.moving = True
        self.collected_antigen = False

        self.image = tcell_image
        self.screen = screen
        self.width = self.image.get_width()
        self.height = self.image.get_height
        self.vel = 3
        self.iter = 0
        self.texts = [ "Récupère l'antigène..."]
        self.current_text = None
        self.standard_text = 'Lymphocyte T tueuse naturelle'
        self.text = 'Lymphocyte T tueuse naturelle'
        self.time = 0
        self.max_time = FPS*5
        self.index = 0

        self.produced_antibodies = False

        self.producing_antibodies_time = 20 #seconds

        self.producing_antibodies_timer = 0
        self.finished_cloning = False

    def follow_path(self):

            self.text = self.standard_text

        

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))    
        macrophage_text = Cells_font.render(self.text, 1 , BLACK)
        self.screen.blit(macrophage_text, (self.x - macrophage_text.get_width()//2, self.y - 65))       



class Dendritic_Cell:
    def __init__(self,screen):
        self.x = DENDRITIC_CELL_LOCATION[0]
        self.y = DENDRITIC_CELL_LOCATION[1]

        self.path = [DENDRITIC_CELL_LOCATION, (452,417), KILLER_T_CELL_LOCATION, B_CELL_LOCATION, DENDRITIC_CELL_LOCATION]
        self.path_point = 0

        self.moving = True
        self.collected_antigen = False

        self.image = Dendritic_cell
        self.screen = screen
        self.width = self.image.get_width()
        self.height = self.image.get_height
        self.vel = 3
        self.iter = 0
        self.texts = [ "Récupère l'antigène...", "Transmet l'antigène"]
        self.current_text = None
        self.standard_text = 'Cellule Dendritique'
        self.text = 'Cellule Dendritique'
        self.time = 0
        self.max_time = FPS*5
        self.index = 0

        self.produced_antibodies = False

        self.producing_antibodies_time = 20 #seconds

        self.producing_antibodies_timer = 0
        self.finished_cloning = False

    def follow_path(self):
        
        if self.moving == True:
         
            p1 = self.path[self.path_point]
            p2 = self.path[self.path_point + 1]

            a = len(self.path)

           

            x_difference = p2[0] - p1[0]
            y_difference = p2[1]-p1[1]

            distance = math.sqrt(x_difference **2 + y_difference **2) #pythagore power


            i = int(distance/self.vel) #number of iterations


            #does this make sense? woow it worked first try
            x_movement = self.vel * x_difference / distance
            y_movement = self.vel * y_difference / distance


            self.x += x_movement
            self.y += y_movement

            self.iter +=1

            #stop iterating at the end of the path
            max_i = self.path_point + 2
            

            if (self.iter == i) and max_i< a:
                self.path_point +=1
                self.iter = 0

            elif (self.iter == i) and max_i>= a:
                        
                self.collected_antigen = True
                self.moving = False


            self.text = self.texts[0]

        #change text
        
        
        
            
        if self.path_point == 1 or self.path_point == 2 or self.path_point ==3:
            self.text = self.texts[1]
            
        if self.collected_antigen == True:
            self.text = self.standard_text

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))    
        macrophage_text = Cells_font.render(self.text, 1 , BLACK)
        self.screen.blit(macrophage_text, (self.x - macrophage_text.get_width()//2, self.y - 65))       

class Cloned:
    def __init__(self, screen):
        self.memoryb_location = MEMORY_B_LOCATION
        self.memory_x = MEMORY_B_LOCATION[0]
        self.memory_y = MEMORY_B_LOCATION[1]
        
        self.plasma_location = PLASMA_LOCATION
        self.plasma_x = PLASMA_LOCATION[0]
        self.plasma_y = PLASMA_LOCATION[1]
        
        self.screen = screen
        
        self.memory_image = Memory_B
        self.plasma_image = plasma_cell_image
        
        self.memory_width = Memory_B.get_width()
        self.memory_height = Memory_B.get_height()
        
        self.plasma_width = plasma_cell_image.get_width()
        self.plasma_height = plasma_cell_image.get_height()
        
        self.memory_text = 'Lymphocyte B Mémoire'
        self.plasma_text = 'Cellule Plasmatique'
        
        
        
    def show(self):
        self.screen.blit(self.memory_image, (self.memory_x - self.memory_image.get_width()//2, self.memory_y - self.memory_image.get_height()//2))    
        macrophage_text = Cells_font.render(self.memory_text, 1 , BLACK)
        self.screen.blit(macrophage_text, (self.memory_x - macrophage_text.get_width()//2, self.memory_y - 65))
        
        '''self.screen.blit(self.plasma_image, (self.plasma_x - self.plasma_image.get_width()//2, self.plasma_y - self.plasma_image.get_height()//2))    
        macrophage_text = Cells_font.render(self.plasma_text, 1 , BLACK)
        self.screen.blit(macrophage_text, (self.plasma_x - macrophage_text.get_width()//2, self.plasma_y - 65))'''
        
        