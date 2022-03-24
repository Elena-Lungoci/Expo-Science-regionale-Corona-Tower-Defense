from data.game.general_stuff import*
from data.game.Economy import *


class Cell:
    def __init__(self, screen, location, image, seconds, infection_chance = economy.cell_infection_chance):
        self.screen = screen
        self.x = location[0]
        self.y = location[1]
        self.location = location
        self.height = image.get_height()
        self.width = image.get_width()
        self.image = image
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)
        self.exist = True
        self.created_time = seconds
        self.lifespan = 3
        self.infection_chance = infection_chance
        self.getting_infected = []
        self.infected = False
        self.attacked_by = []
        self.antibodies = []

        self.spawn_rate = economy.cell_spawn_rate

        self.max_health = economy.cell_hp
        self.dps = economy.cell_dps
        self.health = self.max_health


    def show(self):
        self.screen.blit(self.image, (self.x - self.image.get_width()//2, self.y - self.image.get_height()//2))

    def infect(self, seconds, player):
        if seconds - self.created_time >= self.lifespan:
            self.exist = False

        for enemy in player.enemies:
            if enemy.rect.colliderect(self.rect) and self.getting_infected.count(enemy) == 0:
                self.getting_infected.append(enemy)


        if self.getting_infected != []:
            for enemy in self.getting_infected:
                enemy.moving = False

                if self.exist == False:
                    enemy.moving = True

    def die(self):
        a = [0] * self.infection_chance
        for enemy in self.getting_infected:
            a.append(1)

        if a != []:
            index = random.randint(0, len(a)- 1)

            if a[index] == 1:
                self.infected = True

        else:
            self.infected = False
    

    def attack(self):
    
        if self.attacked_by[0].rect.colliderect(self.rect):
            self.attacked_by[0].health -= self.dps/60
        for tower in self.attacked_by:
            if tower.health <=0:
                self.attacked_by.remove(tower)
            if tower.rect.colliderect(self.rect):
                self.health -= tower.dps/FPS

    


    def health_bar(self):
        length = self.width
        hp_length = length / self.max_health
        green_bar = hp_length * self.health

        pygame.draw.rect(self.screen, RED, (self.x - self.width//2, self.y-self.height//2 - 5, length, 5), 0)
        pygame.draw.rect(self.screen, GREEN, (self.x - self.width//2, self.y-self.height//2 -5, green_bar, 5), 0)