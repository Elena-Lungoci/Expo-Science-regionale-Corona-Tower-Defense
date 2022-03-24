import pygame
from data.game.general_stuff import*
from data.game.Economy import *
class Lymphocyte_T:
    def __init__(self, vel, screen, x, y, image): 
        self.vel = vel
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.followed_enemy = None
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
    

    
      
        self.max_health = economy.tcell_hp
        self.health = self.max_health
        self.dps = economy.tcell_dps
        self.cost = economy.tcell_cost

      



    def follow_enemies(self, player): #similar to enemy move

        if player.infected_cells != []:

            """checks if enemy is still in player.enemies"""
            if player.infected_cells.count(self.followed_enemy) == 0 or self.health<=0:
                self.followed_enemy = None

            """initiate followd enemy"""
            if self.followed_enemy == None:
                if player.infected_cells != []:
                    distances = []
                    for enemy in player.infected_cells:
                        x_difference = enemy.x - self.x
                        y_difference = enemy.y -self.y
                        distance = math.sqrt(x_difference **2 + y_difference **2)
                        distances.append(distance)

                    self.followed_enemy = player.infected_cells[distances.index(min(distances))]
                    self.followed_enemy.attacked_by.append(self)


            enemy_location = (self.followed_enemy.x, self.followed_enemy.y)
            cell_location = (self.x, self.y)


            """makes cell follow enemy"""

            x_difference = self.followed_enemy.x - self.x
            y_difference = self.followed_enemy.y - self.y

            distance = math.sqrt(x_difference **2 + y_difference **2)

            x_movement = self.vel * x_difference / distance
            y_movement = self.vel * y_difference / distance

            self.x += x_movement
            self.y += y_movement
            self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)



    def health_bar(self):
        length = self.width
        hp_length = length / self.max_health
        green_bar = hp_length * self.health

        pygame.draw.rect(self.screen, RED, (self.x - self.width//2, self.y-self.height//2 - 10, length, 7), 0)
        pygame.draw.rect(self.screen, GREEN, (self.x - self.width//2, self.y-self.height//2 -10, green_bar, 7), 0)

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
        self.health_bar()



class Plasma_cell:
    def __init__(self, vel, screen, x, y, image, place): 
        self.vel = vel
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.followed_enemy = None
        self.width = image.get_width()
        self.height = image.get_height()
        self.place = place

        self.cost = economy.plasma_cell_cost
        self.spawn_rate = economy.plasma_cell_fire_rate #this is antibody spawn rate....ik its dumb but the higher it is the slower they spawn..also make it an even number
        self.max_health = economy.plasma_cell_hp
        self.health = self.max_health
        self.dps = 0
        self.range_size = economy.plasma_cell_range  #range is a python keyword


        self.followed_enemy = None
        self.followed_enemy_distance = None
        self.button = None

        
        self.free_squares = []

        distances = []

        if place == 1: #alveoli
        
            for square in squares:
                if square.occupied == False:
                    self.free_squares.append(square)
                    x_difference = square.x +square.width//2 - x
                    y_difference = square.y + square.height//2 - y
                    distance = math.sqrt(x_difference **2 + y_difference **2)
                    distances.append(distance)

            self.square = self.free_squares[distances.index(min(distances))]
   

            self.x = self.square.x + self.square.width//2
            self.y = self.square.y + self.square.height//2

        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)


    def attack(self, player):
        if player.alveoli_enemies != []:
            for enemy in player.alveoli_enemies:
                if self.rect.colliderect(enemy.rect) and enemy.attacked_by.count(self) == 0:
                    enemy.attacked_by.append(self)


    def health_bar(self):
        length = self.width
        hp_length = length / self.max_health
        green_bar = hp_length * self.health

        pygame.draw.rect(self.screen, RED, (self.x - self.width//2, self.y-self.height//2 - 10, length, 10), 0)
        pygame.draw.rect(self.screen, GREEN, (self.x - self.width//2, self.y-self.height//2 -10, green_bar, 10), 0)


    def show(self):
        self.button = Button(self.x - self.image.get_width()//2, self.y - self.image.get_height()//2, self.image, self.screen)
        

    def range(self):
        surface = pygame.Surface((self.range_size * 4,self.range_size *4), pygame.SRCALPHA)

        pygame.draw.circle(surface, TGREEN, (self.range_size,self.range_size), self.range_size, 0)
        self.screen.blit(surface, (self.x - self.range_size,self.y - self.range_size))
      
    def target_enemy(self, player): #alveoli player.enemies not infected player.cells..too lazy to change
        if player.alveoli_enemies != []:

            """checks if enemy is still in player.enemies"""
            if player.alveoli_enemies.count(self.followed_enemy) == 0 or self.health<=0:
                self.followed_enemy = None

            """initiate followd enemy"""
            if self.followed_enemy == None:
                if player.alveoli_enemies != []:
                    distances = []
                    for enemy in player.alveoli_enemies:
                        x_difference = enemy.x - self.x
                        y_difference = enemy.y -self.y
                        distance = math.sqrt(x_difference **2 + y_difference **2)
                        distances.append(distance)

                    if min(distances) <= self.range_size:

                        self.followed_enemy = player.alveoli_enemies[distances.index(min(distances))]
            
            if self.followed_enemy != None:
                x_difference = self.followed_enemy.x - self.x -self.followed_enemy.width//2
                y_difference = self.followed_enemy.y -self.y - self.followed_enemy.height//2
                self.followed_enemy_distance = math.sqrt(x_difference **2 + y_difference **2)

                if self.followed_enemy_distance >= self.range_size:
                    self.followed_enemy = None
                    self.followed_enemy_distance = None


class Antibody:
    def __init__(self, vel, screen, x, y, image, followed_enemy): 
        self.vel = vel
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.followed_enemy = followed_enemy
        self.width = image.get_width()
        self.health = 0.000001  #doesnt actually have hp but dont remove
        self.height = image.get_height()
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
    


    
      

        self.dps = economy.plasma_cell_dps

    def follow_enemies(self, player): #similar to enemy move

        


            enemy_location = (self.followed_enemy.x, self.followed_enemy.y)
            cell_location = (self.x, self.y)


            """makes cell follow enemy"""

            x_difference = self.followed_enemy.x + self.followed_enemy.width//2 - self.x
            y_difference = self.followed_enemy.y - self.y

            distance = math.sqrt(x_difference **2 + y_difference **2)

            x_movement = self.vel * x_difference / distance
            y_movement = self.vel * y_difference / distance

            self.x += x_movement
            self.y += y_movement
            self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

            if player.alveoli_enemies.count(self.followed_enemy) == 0:
                self.health = 0



    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
    

class Lymphocyte_B:
    def __init__(self, screen, x, y, image): 
        self.screen = screen
        self.image = image
        self.followed_enemy = None
        self.width = image.get_width()
        self.height = image.get_height()


        self.images = [image]*(FPS//2) + [lymphocyte_B_image2] *(FPS//2)


        self.range_size = economy.bcell_range

        self.max_health = economy.bcell_hp
        self.health = self.max_health
        self.dps = economy.bcell_dps
        self.cost = economy.bcell_cost

        self.attacked_enemies = []
        self.free_squares = []
        distances = []
        self.Aenemies = []
        for square in squares:
            if square.occupied == False:
                self.free_squares.append(square)
                x_difference = square.x +square.width//2 - x
                y_difference = square.y + square.height//2 - y
                distance = math.sqrt(x_difference **2 + y_difference **2)
                distances.append(distance)

        self.square = self.free_squares[distances.index(min(distances))]

        self.x = self.square.x + self.square.width//2
        self.y = self.square.y + self.square.height//2


        self.range_rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width + self.range_size, self.height)

        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        
        self.button = None
        self.attacking = False

    def attack(self, player):
        if player.alveoli_enemies != []:
            for enemy in player.alveoli_enemies: 
                if self.rect.colliderect(enemy.rect) and enemy.attacked_by.count(self) == 0:
                    enemy.attacked_by.append(self)
                    self.attacking =True
                if self.range_rect.colliderect(enemy.rect) and self.attacked_enemies.count(enemy) == 0:
                    self.attacked_enemies.append(enemy)

                

           
                

                if self.range_rect.colliderect(enemy.rect) and self.Aenemies.count(enemy) == 0:
                    self.Aenemies.append(enemy)

            
            for enemy in self.Aenemies:
                if player.alveoli_enemies.count(enemy) == 0 or not self.range_rect.colliderect(enemy.rect):
                    self.Aenemies.remove(enemy)
        if self.Aenemies != []:
            self.attacking = True
            self.Aenemies[0].health -= self.dps/FPS
        else:
            self.attacking = False
            
    def button_init(self):
        self.button = Button(self.x - self.image.get_width()//2, self.y - self.image.get_height()//2, self.image, self.screen, images = self.images)

    def health_bar(self):
        length = self.width
        hp_length = length / self.max_health
        green_bar = hp_length * self.health

        pygame.draw.rect(self.screen, RED, (self.x - self.width//2, self.y-self.height//2 - 10, length, 10), 0)
        pygame.draw.rect(self.screen, GREEN, (self.x - self.width//2, self.y-self.height//2 -10, green_bar, 10), 0)

    def show(self):
        #pygame.draw.rect(self.screen, RED, self.rect)

        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

        pygame.draw.rect(surface, TGREEN, self.range_rect, 100)
        self.screen.blit(surface, (0,0))

        ''' self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
        self.health_bar()
'''
