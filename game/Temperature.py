from data.game.general_stuff import *
from data.game.Economy import *

class Temperature:
    def __init__(self, screen, button):
        self.boost = False

        self.ready = False

        self.temperature = 20 #sooo what is normal body player.temperature?

        self.boost_duration = economy.boost_duration
        self.boost_cooldown = economy.boost_cooldown

        self.timer = economy.boost_cooldown

        self.timer_text = self.timer

        self.screen = screen

        self.button = button

        self.image_list = [temperature1_image, temperature2_image, temperature3_image, temperature4_image, temperature5_image, temperature6_image, temperature7_image, temperature8_image]
        self.images = []
        for i in self.image_list:
            self.images.append(scale_image(0.4, i))

    def activate_boost(self, player):
        if self.boost == True:
            for tower in player.towers:
                tower.dps *= economy.damage_boost
                tower.health = tower.max_health
                tower.cost /= economy.cost_boost

            economy.plasma_cell_range *= economy.boost_plasma_cell_range

            economy.neutrophil_cost /= economy.cost_boost
            economy.macrophage_cost /= economy.cost_boost
            economy.bcell_cost  /= economy.cost_boost
            economy.tcell_cost /= economy.cost_boost
            economy.plasma_cell_cost /= economy.cost_boost
            economy.mucus_cost /= economy.cost_boost
            economy.cilia_cost /= economy.cost_boost

            economy.neutrophil_dps *= economy.damage_boost
            economy.macrophage_dps *= economy.damage_boost
            economy.bcell_dps *= economy.damage_boost
            economy.tcell_dps *= economy.damage_boost
            economy.plasma_cell_dps *= economy.damage_boost
            


            

    def remove_boost(self,player):
        if self.boost == False:
            for tower in player.towers:
                tower.dps /= economy.damage_boost
                tower.cost *= economy.cost_boost
                
            economy.plasma_cell_range /= economy.boost_plasma_cell_range


            economy.neutrophil_cost *= economy.cost_boost
            economy.macrophage_cost *= economy.cost_boost
            economy.bcell_cost  *= economy.cost_boost
            economy.tcell_cost *= economy.cost_boost
            economy.plasma_cell_cost *= economy.cost_boost
            economy.mucus_cost *= economy.cost_boost
            economy.cilia_cost *= economy.cost_boost

            economy.neutrophil_dps /= economy.damage_boost
            economy.macrophage_dps /= economy.damage_boost
            economy.bcell_dps /= economy.damage_boost
            economy.tcell_dps /= economy.damage_boost
            economy.plasma_cell_dps /= economy.damage_boost


    def boost_timer(self, player):
        if self.boost == False:
            self.timer -= 1/FPS
            
            if self.timer <= 0:
                self.ready = True
                self.timer = 0

        if self.boost == True:
            if self.timer ==0: #might be better to let an outside function take care of this
                self.timer = self.boost_duration

            self.timer -= 1/FPS

            self.ready = False

            if self.timer <= 0:
                self.timer = self.boost_cooldown
                self.boost = False
                self.remove_boost(player)





        self.timer_text = int(self.timer)
                
    def show(self): 
        self.screen.blit(self.images[0], (self.button.x - self.images[0].get_width() - 20, self.button.y))

        timer_text = Cells_font.render(f'{self.timer_text} sec', 1 , BLACK)
        self.screen.blit(timer_text, (self.button.x + self.button.width//2 - timer_text.get_width()//2, self.button.y + self.button.height + 20))