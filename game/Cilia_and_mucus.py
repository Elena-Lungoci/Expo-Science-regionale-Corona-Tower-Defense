import pygame
from data.game.general_stuff import *
from data.game.Economy import *

class Cilia:
    def __init__(self, screen, x, y, image, seconds):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = image.get_height()
        self.width = image.get_width()
        self.cost = economy.cilia_cost
        self.image = image
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        self.exist = True
        self.created_time = seconds
        self.lifespan = economy.cilia_lifespan

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width(), self.y - self.image.get_height()//2))

    def die(self, seconds):
        if seconds - self.created_time >= self.lifespan:
                self.exist = False


    



class Mucus:
    def __init__(self, screen, x, y, image, seconds):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = image.get_height()
        self.width = image.get_width()
        self.cost = economy.mucus_cost
        self.image = image
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        self.trapped_enemies = []
        self.exist = True
        self.created_time = seconds
        self.lifespan = economy.mucus_lifespan
        
        self.dps = 5 #wow i need this..doesnt do dmg tho

    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))

    def trap(self, player):

        if player.seconds - self.created_time >= self.lifespan:
            self.exist = False

        for enemy in player.enemies:
            if enemy.rect.colliderect(self.rect):
                self.trapped_enemies.append(enemy)


        if self.trapped_enemies != []:
            player.first_trap = True
            for enemy in self.trapped_enemies:
                enemy.moving = False

                if self.exist == False:
                    enemy.moving = True


        for cilia in player.cilias:
            if cilia.rect.colliderect(self.rect):
                cilia.exist = False
                self.exist = False
                if self.trapped_enemies != []:
                    for enemy in self.trapped_enemies:
                        enemy.health = 0

            