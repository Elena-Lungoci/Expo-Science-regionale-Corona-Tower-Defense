
from data.game.general_stuff import *
from data.game.Economy import *


class Variants:
    def __init__(self, variant):

        self.variant = variant

        if variant == 1: #normal
            self.image = normal_corona_image
            economy.cell_infection_chance = economy.normal_infection_chance
            economy.enemy_hp = economy.normal_hp
            economy.enemy_dps = economy.normal_dps
            economy.cell_spawn_rate = economy.normal_spawn_rate

        if variant == 2: #gamma
            self.image = gamma_image
            economy.cell_infection_chance = economy.gamma_infection_chance
            economy.enemy_hp = economy.gamma_hp
            economy.enemy_dps = economy.gamma_dps
            economy.cell_spawn_rate = economy.gamma_spawn_rate

        if variant == 3: #alpha
            self.image = alpha_image
            economy.cell_infection_chance = economy.alpha_infection_chance
            economy.enemy_hp = economy.alpha_hp
            economy.enemy_dps = economy.alpha_dps
            economy.cell_spawn_rate = economy.alpha_spawn_rate

        if variant == 4: #delta
            self.image = delta_image
            economy.cell_infection_chance = economy.delta_infection_chance
            economy.enemy_hp = economy.delta_hp
            economy.enemy_dps = economy.delta_dps
            economy.cell_spawn_rate = economy.delta_spawn_rate