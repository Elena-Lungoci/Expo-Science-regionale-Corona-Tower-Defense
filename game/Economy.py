import data.game.general_stuff as general_stuff
class Economy:
    def __init__(self):
        
        #make costs even numbers

        #game
        self.start_energy = 0
        self.max_energy = 100
        self.max_humidity = 100


        #player.enemies

        self.normal_hp = 10
        self.gamma_hp = 10
        self.alpha_hp = 10
        self.delta_hp = 12

        self.normal_dps = 1
        self.gamma_dps = 1.5
        self.alpha_dps = 1
        self.delta_dps = 2

        self.enemy_hp = None
        self.enemy_dps = None
        
        self.enemy_kill_reward = 4
        self.first_enemy_kill_reward = 50 #50
        
        self.instructions_first_enemy_kill_reward = 100
        self.instructions_enemy_kill_reward = 10

        self.finish_path_humidity = 10

        #Neutrophils

        self.neutrophil_hp = 0.2
        self.neutrophil_cost = 2
        self.neutrophil_dps = 5

        #macrophage

        self.macrophage_cost = 10
        self.macrophage_hp = 25
        self.macrophage_dps = 1 #1
      

        
        #plasma player.cells

        
        self.plasma_cell_range = 400
        self.plasma_cell_fire_rate = 1 #uhh the higher this is the slower it fires...dont make it decimal
        self.plasma_cell_hp = 10
        self.plasma_cell_dps = 50

        self.plasma_cell_max_cost = 200

        self.plasma_min_cost = 60
        self.plasma_max_cost = 200
        self.plasma_cell_cost = self.plasma_max_cost

        self.plasma_substract_cost = 10 # how often it diminishes
        self.plasma_substract_timer = 5 #by how much it diminishes

        #bcell

        self.bcell_range = 200
        self.bcell_hp = 5
        self.bcell_dps = 3

        self.bcell_max_cost = 110
        self.bcell_min_cost = 30
        self.bcell_cost = self.bcell_max_cost

        self.bcell_substract_cost = 10 #by how much it diminishes
        self.bcell_substract_time = 5 #how often it diminishes

        #tcell

        self.tcell_hp = 1000
        self.tcell_dps = 250

        self.t_cell_max_cost = 1000
        self.t_cell_min_cost = 100
        self.substract = 10 #by how much the cost diminishes
        self.substract_time = 2 #every x seconds, how often it diminishes


        self.tcell_cost = self.t_cell_max_cost




        #cilia

        self.cilia_cost = 2
        self.cilia_lifespan = 10 #seconds

        #player.mucus
        self.mucus_cost = 10
        self.mucus_lifespan = 10 #seconds

        #player.temperature boost

        self.damage_boost = 2 #tower damages are doubled
        self.cost_boost = 2 #costs are halved

        self.boost_duration = 10 #seconds
        self.boost_cooldown = 100 #seconds

        self.boost_plasma_cell_range = 1.5

        #cell

        self.normal_infection_chance = 10
        self.gamma_infection_chance = 9
        self.alpha_infection_chance = 7
        self.delta_infection_chance = 1

        self.cell_infection_chance = None


        self.normal_spawn_rate = 5
        self.gamma_spawn_rate = 4
        self.alpha_spawn_rate = 2
        self.delta_spawn_rate = 5
        
        self.instructions_spawn_rate = 10


        self.cell_spawn_rate = None #enemy spawn rate

        self.cell_hp = 1000
        self.cell_dps = 250



        #

        self.costs = [self.neutrophil_cost, self.macrophage_cost, self.plasma_cell_cost,self.bcell_cost,self.tcell_cost,self.mucus_cost,self.cilia_cost]
        self.dps = [self.neutrophil_dps, self.macrophage_dps,self.plasma_cell_dps, self.bcell_dps,self.tcell_dps]

        self.timer1 = 0
        self.timer2 = 0
        self.timer3 = 0

    def killerT_cost(self, killerT_cell):
        if killerT_cell.collected_antigen == True:
            self.timer1 += 1

            max_time = self.substract_time* general_stuff.FPS

            if self.timer1 >= max_time:
                self.timer1 = 0

                if self.tcell_cost >= self.t_cell_min_cost:
                    self.tcell_cost -= self.substract

                

    def b_cell_cost(self, Bcell):
        if Bcell.collected_antigen == True:
            self.timer2 += 1

            max_time = self.bcell_substract_time* general_stuff.FPS

            if self.timer2 >= max_time:
                self.timer2 = 0

                if self.bcell_cost >= self.bcell_min_cost:
                    self.bcell_cost -= self.bcell_substract_cost

            self.timer3 +=1

            max_time2 = self.plasma_substract_timer * general_stuff.FPS

            if self.timer3 >= max_time2:
                self.timer3 = 0

                if self.plasma_cell_cost >= self.plasma_min_cost:
                    self.plasma_cell_cost -= self.plasma_substract_cost


economy = Economy()
