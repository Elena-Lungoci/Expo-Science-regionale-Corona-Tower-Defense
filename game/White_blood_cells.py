import pygame
from data.game.general_stuff import *
from data.game.Economy import *


#must be defined with a bigger velocity than player.enemies so it gets to them
class White_Blood_Cell:
    def __init__(self, vel, screen, x, y, image, player, cell_type): 
        self.vel = vel
        self.screen = screen
        self.image = image
        self.followed_enemy = None
        self.width = image.get_width()
        self.height = image.get_height()
        self.type = cell_type

        self.image_index = 0
        self.free_squares = []

        self.attacking = False
        self.attacked_enemies = []

        if cell_type == 0:  #neutrophil
            self.max_health = economy.neutrophil_hp
            self.health = self.max_health
            self.dps = economy.neutrophil_dps
            self.cost = economy.neutrophil_cost
            self.x = x
            self.y = y

            self.images = [image]

        elif cell_type ==1:  #macrophage
            self.max_health = economy.macrophage_hp
            self.health = self.max_health
            self.dps = economy.macrophage_dps
            self.cost = economy.macrophage_cost

            distances = []
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

            self.images = [image]*(FPS//2) + [macrophage_image2] *(FPS//2)



        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        

    def follow_enemies(self, player): #similar to enemy move

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

                    self.followed_enemy = player.alveoli_enemies[distances.index(min(distances))]
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

    def attack(self, player):
        if player.alveoli_enemies != []:
            for enemy in player.alveoli_enemies:
                if self.rect.colliderect(enemy.rect) and enemy.attacked_by.count(self) == 0:
                    enemy.attacked_by.append(self)
                if self.rect.colliderect(enemy.rect) and self.attacked_enemies.count(enemy) == 0:
                    self.attacked_enemies.append(enemy)

        if self.attacked_enemies != []:
            self.attacking = True
            self.attacked_enemies[0].health -= self.dps/FPS

        else:
            self.attacking = False
            self.image = self.images[0]

        for enemy in self.attacked_enemies:
            if player.alveoli_enemies.count(enemy) == 0 or not self.rect.colliderect(enemy.rect):
                self.attacked_enemies.remove(enemy)


                


    def health_bar(self):
        length = self.width
        hp_length = length / self.max_health
        green_bar = hp_length * self.health

        pygame.draw.rect(self.screen, RED, (self.x - self.width//2, self.y-self.height//2 - 10, length, 10), 0)
        pygame.draw.rect(self.screen, GREEN, (self.x - self.width//2, self.y-self.height//2 -10, green_bar, 10), 0)

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
        self.health_bar()
