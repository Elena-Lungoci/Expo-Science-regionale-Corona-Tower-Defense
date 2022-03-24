from os import kill
import pygame
from data.game.general_stuff import*
from data.game.Economy import *


class Enemy:
    def __init__(self, vel,screen, image, path, alveoli_path, kill_reward = economy.enemy_kill_reward):
        self.width = image.get_width()
        self.height = image.get_height()
        self.screen = screen
        self.vel = vel
        self.path = path
        self.image = image
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_point = 0
        self.moving = True
        self.lungs_screen = True
        self.alveoli_screen = False
        self.alveoli_path = alveoli_path
        self.iter = 0
        self.attacking = None
        self.attacked_by = []
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        self.finished_path = False
        self.bullets = []

        self.max_health = economy.enemy_hp
        self.health = self.max_health
        self.dps = economy.enemy_dps
        self.kill_reward = kill_reward


    def move(self, player):
        if self.moving == True:
            if self.lungs_screen == True:
                p1 = self.path[self.path_point]
                p2 = self.path[self.path_point + 1]

                a = len(self.path)

            if self.alveoli_screen == True:
                p1 = self.alveoli_path[self.path_point]
                p2 = self.alveoli_path[self.path_point + 1]

                a = len(self.alveoli_path)
                

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
        
                if self.lungs_screen == True:
                    if player.instructions == True and player.changed_alveoli == False:
                        player.change_alveoli = True
                        player.changed_alveoli = True
                        
                    self.lungs_screen = False
                    self.alveoli_screen = True
                    self.path_point = 0
                    self.x = self.alveoli_path[0][0]
                    self.y = self.alveoli_path[0][1]
                else:
                    self.finished_path = True

                self.iter = 0
            self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        
            

    def attack(self):
        

        if self.attacked_by != []:
            if self.attacked_by[0].rect.colliderect(self.rect):
                self.attacked_by[0].health -= self.dps/60
            for tower in self.attacked_by:
                if tower.health <=0:
                    self.attacked_by.remove(tower)
                if tower.rect.colliderect(self.rect):
                    self.moving = False
                    tower.moving = False

        else:
            self.moving = True


        if self.bullets != []:
            for tower in self.bullets:
                if tower.health <=0:
                    self.bullets.remove(tower)
                if tower.rect.colliderect(self.rect):
                    self.health -= tower.dps/FPS
                    tower.health = 0
        


    def show(self):
         self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))
         self.health_bar()

    def health_bar(self):
        length = self.width
        hp_length = length / self.max_health
        green_bar = hp_length * self.health

        pygame.draw.rect(self.screen, RED, (self.x - self.width//2, self.y-self.height//2 - 10, length, 10), 0)
        pygame.draw.rect(self.screen, GREEN, (self.x - self.width//2, self.y-self.height//2 -10, green_bar, 10), 0)


